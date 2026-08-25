"""GoF Creational design pattern detection rules for Mojo (5/5)."""

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


class SingletonGlobalInstanceRule(BaseRule):
    """Detects Singleton instances represented as zero-field structs or global static managers."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if s.is_singleton:
                score = 0.90 if "Singleton" in s.name else 0.85
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_SINGLETON_STRUCT",
                        description=f"Struct '{s.name}' serves as a unique Singleton instance",
                        weight=score,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SINGLETON_GLOBAL_INSTANCE,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class FactoryMethodConstructorRule(BaseRule):
    """Detects Factory Method pattern instantiating specialized types."""

    FACTORY_NAME_PATTERN = re.compile(r"\b(create_[a-zA-Z0-9_]+|make_[a-zA-Z0-9_]+|build_[a-zA-Z0-9_]+)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.FACTORY_NAME_PATTERN.search(fn.name) or ("Factory" in fn.name):
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_FACTORY_METHOD",
                        description=f"Function '{fn.name}' encapsulates instance creation as a Factory Method",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FACTORY_METHOD_CONSTRUCTOR,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class AbstractFactoryTraitRule(BaseRule):
    """Detects Abstract Factory traits defining contracts for component families."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_traits:
            if "Factory" in t.name or "Provider" in t.name or "Builder" in t.name:
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_ABSTRACT_FACTORY",
                        description=f"Trait '{t.name}' defines Abstract Factory contract for component families",
                        weight=0.90,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ABSTRACT_FACTORY_TRAIT,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=t.name,
                        target_kind="trait",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class BuilderFluentStructRule(BaseRule):
    """Detects Builder pattern structs accumulating configuration options."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Builder" in s.name:
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_BUILDER_STRUCT",
                        description=f"Struct '{s.name}' implements Builder pattern accumulating configuration parameters",
                        weight=0.90,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.BUILDER_FLUENT_STRUCT,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class PrototypeCloneCopyRule(BaseRule):
    """Detects Prototype pattern duplication via '__copyinit__' or explicit clone() methods."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_copy = any(m.name in ("__copyinit__", "clone", "copy") for m in s.methods)
            if has_copy or "Copyable" in s.traits:
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_PROTOTYPE_CLONE",
                        description=f"Struct '{s.name}' implements Prototype pattern for object cloning and duplication",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PROTOTYPE_CLONE_COPY,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections
