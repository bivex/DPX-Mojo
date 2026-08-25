"""Compile-Time Metaprogramming and Parameter Specialization rules for Mojo."""

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


class ComptimeParameterSpecializationRule(BaseRule):
    """Detects compile-time parameter specialization ('[type: DType, width: Int]')."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if s.comptime_params:
                evidences = [
                    Evidence(
                        rule_code="COMPTIME_STRUCT_PARAMETERS",
                        description=f"Struct '{s.name}[{', '.join(s.comptime_params)}]' specializes compile-time machine code parameters",
                        weight=0.95,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMPTIME_PARAMETER_SPECIALIZATION,
                        pattern_category=PatternCategory.COMPTIME_METAPROGRAMMING,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )

        for fn in model.all_functions:
            if fn.comptime_params:
                evidences = [
                    Evidence(
                        rule_code="COMPTIME_FN_PARAMETERS",
                        description=f"Function '{fn.name}[{', '.join(fn.comptime_params)}]' parameterizes compile-time hardware types",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMPTIME_PARAMETER_SPECIALIZATION,
                        pattern_category=PatternCategory.COMPTIME_METAPROGRAMMING,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class AliasTypeMetaprogrammingRule(BaseRule):
    """Detects compile-time 'alias' constants and type bindings."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for a in model.all_aliases:
            evidences = [
                Evidence(
                    rule_code="COMPTIME_ALIAS_DECLARATION",
                    description=f"Alias '{a.name} = {a.target_expr}' defines compile-time type or constant expression",
                    weight=0.90,
                    location=a.location,
                )
            ]
            detections.append(
                Detection(
                    pattern_type=PatternType.ALIAS_TYPE_METAPROGRAMMING,
                    pattern_category=PatternCategory.COMPTIME_METAPROGRAMMING,
                    target_name=a.name,
                    target_kind="alias",
                    confidence=Confidence(score=0.90, evidences=evidences),
                    primary_location=a.location,
                    evidences=evidences,
                )
            )
        return detections


class CompileTimeBranchSpecializationRule(BaseRule):
    """Detects compile-time branch specialization ('@parameter if')."""

    PARAM_IF_PATTERN = re.compile(r"@parameter\s+(?:if|elif)\b|@parameter\s*\n\s*(?:if|elif)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.PARAM_IF_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="COMPTIME_PARAMETER_IF_BRANCH",
                        description=f"Function '{fn.name}' uses @parameter if for zero-cost compile-time branch elimination",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMPILE_TIME_BRANCH_SPECIALIZATION,
                        pattern_category=PatternCategory.COMPTIME_METAPROGRAMMING,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
