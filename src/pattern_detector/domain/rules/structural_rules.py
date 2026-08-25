"""GoF Structural design pattern detection rules for Mojo (7/7)."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
)


class AdapterStructWrapperRule(BaseRule):
    """Detects Adapter pattern wrapping third-party or foreign types."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Adapter" in s.name or "Wrapper" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_ADAPTER_WRAPPER",
                        description=f"Struct '{s.name}' adapts target type to domain trait contracts",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ADAPTER_STRUCT_WRAPPER,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class BridgeHardwareDriverRule(BaseRule):
    """Detects Bridge pattern decoupling domain abstraction from hardware implementor drivers."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            driver_fields = [
                f for f in s.fields
                if any(suffix in f.type_name for suffix in ("Driver", "Backend", "Engine", "Device", "Implementor"))
            ]
            if driver_fields or "Bridge" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_BRIDGE_DRIVER",
                        description=f"Struct '{s.name}' decouples abstraction from hardware implementor via '{driver_fields[0].name if driver_fields else 'driver'}'",
                        weight=0.85,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.BRIDGE_HARDWARE_DRIVER,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class CompositeTreeHierarchyRule(BaseRule):
    """Detects Composite pattern with recursive tree node collections."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_children = any(
                f.type_name in (f"List[{s.name}]", f"Vector[{s.name}]", "List[Node]", "DynamicVector[Node]")
                or f.name in ("children", "nodes", "elements")
                for f in s.fields
            )
            if has_children or "Composite" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_COMPOSITE_TREE",
                        description=f"Struct '{s.name}' implements Composite pattern holding recursive tree collections",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMPOSITE_TREE_HIERARCHY,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class DecoratorForwardingWrapperRule(BaseRule):
    """Detects Decorator pattern wrapping an inner struct and augmenting behavior."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_inner = any(f.name in ("inner", "wrapped", "base", "parent") for f in s.fields)
            if (has_inner and len(s.fields) <= 3) or "Decorator" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_DECORATOR_WRAPPER",
                        description=f"Struct '{s.name}' decorates and augments an underlying instance",
                        weight=0.85,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DECORATOR_FORWARDING_WRAPPER,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class FacadeUnifiedApiRule(BaseRule):
    """Detects Facade Unified API struct coordinating multiple subsystem components."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Facade" in s.name or (len(s.fields) >= 3 and len(s.methods) >= 4):
                score = 0.90 if "Facade" in s.name else 0.80
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_FACADE_API",
                        description=f"Struct '{s.name}' acts as unified Facade API coordinating multiple subsystem components",
                        weight=score,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FACADE_UNIFIED_API,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class FlyweightSharedPoolRule(BaseRule):
    """Detects Flyweight pattern sharing instances via pool cache or dictionary."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_cache = any("cache" in f.name.lower() or "pool" in f.name.lower() for f in s.fields)
            if has_cache or "Flyweight" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_FLYWEIGHT_POOL",
                        description=f"Struct '{s.name}' shares fine-grained instances via Flyweight pool cache",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FLYWEIGHT_SHARED_POOL,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class ProxyLazyResourceRule(BaseRule):
    """Detects Proxy pattern controlling access or delaying allocation of heavy GPU buffers."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Proxy" in s.name or "Lazy" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_PROXY_SURROGATE",
                        description=f"Struct '{s.name}' acts as Proxy surrogate controlling access to target resource",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PROXY_LAZY_RESOURCE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections
