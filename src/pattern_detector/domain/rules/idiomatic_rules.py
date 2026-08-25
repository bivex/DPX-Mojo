"""Mojo Idiomatic, Ownership, and Value Semantics rules."""

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


class StructValueSemanticsRule(BaseRule):
    """Detects value-semantic structs synthesized via '@value' or manual move/copy lifecycle."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if s.has_value_decorator:
                evidences = [
                    Evidence(
                        rule_code="MOJO_VALUE_SEMANTICS_DECORATOR",
                        description=f"Struct '{s.name}' implements value semantics with @value synthesized constructors",
                        weight=0.95,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STRUCT_VALUE_SEMANTICS,
                        pattern_category=PatternCategory.MOJO_IDIOMATIC,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
            elif any(m.name in ("__copyinit__", "__moveinit__") for m in s.methods):
                evidences = [
                    Evidence(
                        rule_code="MOJO_MANUAL_VALUE_LIFECYCLE",
                        description=f"Struct '{s.name}' explicitly implements __copyinit__/__moveinit__ value semantics",
                        weight=0.90,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STRUCT_VALUE_SEMANTICS,
                        pattern_category=PatternCategory.MOJO_IDIOMATIC,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class TraitContractInterfaceRule(BaseRule):
    """Detects static polymorphic Trait contracts."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_traits:
            evidences = [
                Evidence(
                    rule_code="MOJO_TRAIT_CONTRACT",
                    description=f"Trait '{t.name}' defines static compile-time interface contract with {len(t.methods)} method(s)",
                    weight=0.95,
                    location=t.location,
                )
            ]
            detections.append(
                Detection(
                    pattern_type=PatternType.TRAIT_CONTRACT_INTERFACE,
                    pattern_category=PatternCategory.MOJO_IDIOMATIC,
                    target_name=t.name,
                    target_kind="trait",
                    confidence=Confidence(score=0.95, evidences=evidences),
                    primary_location=t.location,
                    evidences=evidences,
                )
            )
        return detections


class ExplicitOwnershipBorrowRule(BaseRule):
    """Detects explicit function argument ownership conventions ('inout', 'borrowed', 'owned')."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            ownership_params = [p for p in fn.parameters if p.convention in ("inout", "owned", "borrowed", "ref")]
            if len(ownership_params) >= 2:
                evidences = [
                    Evidence(
                        rule_code="MOJO_EXPLICIT_OWNERSHIP",
                        description=f"Function '{fn.name}' enforces explicit memory conventions ({', '.join(f'{p.name}: {p.convention}' for p in ownership_params[:3])})",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.EXPLICIT_OWNERSHIP_BORROW,
                        pattern_category=PatternCategory.MOJO_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class TransferMoveOperatorRule(BaseRule):
    """Detects explicit ownership transfer using the '^' move operator."""

    TRANSFER_PATTERN = re.compile(r"\b([a-zA-Z_]\w*)\^")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            matches = self.TRANSFER_PATTERN.findall(fn.body or "")
            if matches or fn.has_transfer_move:
                evidences = [
                    Evidence(
                        rule_code="MOJO_TRANSFER_MOVE_OPERATOR",
                        description=f"Function '{fn.name}' uses '^' transfer operator to move ownership without memory copying",
                        weight=0.92,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.TRANSFER_MOVE_OPERATOR,
                        pattern_category=PatternCategory.MOJO_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.92, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class DestructRaiiLifecycleRule(BaseRule):
    """Detects deterministic cleanup via '__del__' destructor."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            del_methods = [m for m in s.methods if m.is_destructor]
            if del_methods:
                evidences = [
                    Evidence(
                        rule_code="MOJO_RAII_DESTRUCTOR",
                        description=f"Struct '{s.name}' implements deterministic RAII resource cleanup via __del__",
                        weight=0.95,
                        location=del_methods[0].location or s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DESTRUCT_RAII_LIFECYCLE,
                        pattern_category=PatternCategory.MOJO_IDIOMATIC,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=del_methods[0].location or s.location,
                        evidences=evidences,
                    )
                )
        return detections


class RegisterPassableLayoutRule(BaseRule):
    """Detects structs decorated with '@register_passable' passed directly in CPU/GPU registers."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if s.is_register_passable:
                evidences = [
                    Evidence(
                        rule_code="MOJO_REGISTER_PASSABLE",
                        description=f"Struct '{s.name}' is decorated with @register_passable for direct zero-overhead register passing",
                        weight=0.95,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.REGISTER_PASSABLE_LAYOUT,
                        pattern_category=PatternCategory.MOJO_IDIOMATIC,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections
