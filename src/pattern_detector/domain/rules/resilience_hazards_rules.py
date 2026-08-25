"""Resilience, Memory Safety & Performance Hazards rules for Mojo."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
)


class UncheckedUnsafePointerRule(BaseRule):
    """Detects raw pointer arithmetic and loads without bounds validation."""

    POINTER_OP_PATTERN = re.compile(r"\.(load|store|offset)\s*\(")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            has_ptr = any("Pointer" in p.type_name for p in fn.parameters) or "UnsafePointer" in fn.body or "DTypePointer" in fn.body
            if has_ptr and self.POINTER_OP_PATTERN.search(fn.body or "") and "assert" not in fn.body and "if " not in fn.body:
                evidences = [
                    Evidence(
                        rule_code="HAZARD_UNCHECKED_UNSAFE_POINTER",
                        description=f"Function '{fn.name}' performs raw pointer operations without bounds assertions or bounds checks",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.UNCHECKED_UNSAFE_POINTER,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class DynamicDefInHotPathRule(BaseRule):
    """Detects Python-style dynamic 'def' in compute-intensive functions."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.kind == "def" and ("simd" in fn.body.lower() or "for " in fn.body or "matrix" in fn.name.lower() or "kernel" in fn.name.lower()):
                evidences = [
                    Evidence(
                        rule_code="HAZARD_DYNAMIC_DEF_HOT_PATH",
                        description=f"Dynamic 'def' function '{fn.name}' incurs runtime overhead; convert to strictly typed 'fn' for zero-cost compilation",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DYNAMIC_DEF_IN_HOT_PATH,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class AccidentalCopyOverheadRule(BaseRule):
    """Detects large struct or buffer parameters passed by value without 'borrowed' or 'inout'."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        struct_names = {s.name for s in model.all_structs if len(s.fields) >= 3}
        for fn in model.all_functions:
            for p in fn.parameters:
                if p.type_name in struct_names and p.convention not in ("borrowed", "inout", "ref", "owned"):
                    evidences = [
                        Evidence(
                            rule_code="HAZARD_ACCIDENTAL_COPY_OVERHEAD",
                            description=f"Function '{fn.name}' parameter '{p.name}: {p.type_name}' may incur accidental copy overhead; specify 'borrowed' or 'inout'",
                            weight=0.85,
                            location=fn.location,
                        )
                    ]
                    detections.append(
                        Detection(
                            pattern_type=PatternType.ACCIDENTAL_COPY_OVERHEAD,
                            pattern_category=PatternCategory.RESILIENCE,
                            target_name=fn.name,
                            target_kind="fn",
                            confidence=Confidence(score=0.85, evidences=evidences),
                            primary_location=fn.location,
                            evidences=evidences,
                        )
                    )
        return detections


class ScalarComputeLoopRule(BaseRule):
    """Detects element-by-element scalar loops in numerical kernels missing SIMD vectorization."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            is_kernel = "kernel" in fn.name.lower() or "matmul" in fn.name.lower() or "conv" in fn.name.lower()
            if is_kernel and "for " in fn.body and "SIMD" not in fn.body and "vectorize" not in fn.body:
                evidences = [
                    Evidence(
                        rule_code="HAZARD_SCALAR_COMPUTE_LOOP",
                        description=f"Compute kernel '{fn.name}' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SCALAR_COMPUTE_LOOP,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class DanglingTransferLifetimeRule(BaseRule):
    """Detects usage of a variable after ownership has been moved ('^')."""

    TRANSFER_PATTERN = re.compile(r"\b([a-zA-Z_]\w*)\^")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            matches = self.TRANSFER_PATTERN.findall(fn.body or "")
            for var in matches:
                # Check if var appears again after the transfer line
                lines = fn.body.splitlines()
                transferred = False
                for line in lines:
                    if f"{var}^" in line:
                        transferred = True
                        continue
                    if transferred and re.search(rf"\b{var}\b", line):
                        evidences = [
                            Evidence(
                                rule_code="HAZARD_DANGLING_TRANSFER_LIFETIME",
                                description=f"Variable '{var}' referenced in function '{fn.name}' after ownership was transferred via '^'",
                                weight=0.92,
                                location=fn.location,
                            )
                        ]
                        detections.append(
                            Detection(
                                pattern_type=PatternType.DANGLING_TRANSFER_LIFETIME,
                                pattern_category=PatternCategory.RESILIENCE,
                                target_name=fn.name,
                                target_kind="fn",
                                confidence=Confidence(score=0.92, evidences=evidences),
                                primary_location=fn.location,
                                evidences=evidences,
                            )
                        )
                        break
        return detections
