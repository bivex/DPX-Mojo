"""SIMD vectorization and hardware acceleration rules for Mojo."""

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


class SimdVectorizationKernelRule(BaseRule):
    """Detects SIMD vector register usage ('SIMD[DType, width]', 'vectorize')."""

    SIMD_PATTERN = re.compile(r"\b(SIMD\s*\[|vectorize\s*\[|simdwidthof\s*\[)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.SIMD_PATTERN.search(fn.body or "") or any("SIMD" in p.type_name for p in fn.parameters):
                evidences = [
                    Evidence(
                        rule_code="HARDWARE_SIMD_VECTORIZATION",
                        description=f"Function '{fn.name}' executes SIMD vector operations across hardware vector registers",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SIMD_VECTORIZATION_KERNEL,
                        pattern_category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ParallelizeMultiCoreRule(BaseRule):
    """Detects multi-core thread pool distribution ('parallelize')."""

    PARALLEL_PATTERN = re.compile(r"\bparallelize\s*\[")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.PARALLEL_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="HARDWARE_PARALLELIZE_MULTI_CORE",
                        description=f"Function '{fn.name}' distributes compute tasks across CPU cores via parallelize",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PARALLELIZE_MULTI_CORE,
                        pattern_category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class UnsafeRawPointerBufferRule(BaseRule):
    """Detects raw pointer memory buffers ('UnsafePointer', 'DTypePointer')."""

    POINTER_PATTERN = re.compile(r"\b(UnsafePointer|DTypePointer)\s*\[")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            ptr_fields = [f for f in s.fields if self.POINTER_PATTERN.search(f.type_name)]
            if ptr_fields:
                evidences = [
                    Evidence(
                        rule_code="HARDWARE_UNSAFE_POINTER_BUFFER",
                        description=f"Struct '{s.name}' manages direct memory buffer via '{ptr_fields[0].name}: {ptr_fields[0].type_name}'",
                        weight=0.92,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.UNSAFE_RAW_POINTER_BUFFER,
                        pattern_category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.92, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class TensorTilingKernelRule(BaseRule):
    """Detects cache-blocked matrix/tensor tiling kernels."""

    TILING_PATTERN = re.compile(r"\b(tile|tile_size|tile_m|tile_n|tile_k|block_size)\b", re.IGNORECASE)

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if len(self.TILING_PATTERN.findall(fn.body or "")) >= 2 or ("tile" in fn.name.lower() and "matmul" in fn.name.lower()):
                evidences = [
                    Evidence(
                        rule_code="HARDWARE_TENSOR_TILING",
                        description=f"Function '{fn.name}' performs cache-blocked tensor tiling to maximize L1/L2 data reuse",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.TENSOR_TILING_KERNEL,
                        pattern_category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
