"""GoF Behavioral design pattern detection rules for Mojo (11/11)."""

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


class ChainOfResponsibilityChainRule(BaseRule):
    """Detects Chain of Responsibility holding next handler pointer or middleware chain."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_next = any(f.name in ("next", "next_handler", "successor") or "Handler" in f.type_name for f in s.fields)
            if (has_next and "Handler" in s.name) or "Middleware" in s.name or "Pipeline" in s.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_CHAIN_OF_RESPONSIBILITY",
                        description=f"Struct '{s.name}' implements Chain of Responsibility delegating unhandled requests along handler chain",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.CHAIN_OF_RESPONSIBILITY_CHAIN,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class CommandCallableTaskRule(BaseRule):
    """Detects Command pattern encapsulating executable operations into callable structs."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Command" in s.name or "Action" in s.name or "Task" in s.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_COMMAND_TASK",
                        description=f"Struct '{s.name}' encapsulates executable operation as a Command object",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMMAND_CALLABLE_TASK,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class InterpreterAstEvalRule(BaseRule):
    """Detects Interpreter pattern evaluating domain AST expressions."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            has_eval = fn.name in ("evaluate", "interpret", "eval_expr", "interpret_ast")
            if has_eval or ("AST" in fn.name or "Expression" in fn.signature):
                score = 0.90 if has_eval else 0.82
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_INTERPRETER_AST",
                        description=f"Function '{fn.name}' implements Interpreter pattern evaluating domain AST expressions",
                        weight=score,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.INTERPRETER_AST_EVAL,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class IteratorTraitProtocolRule(BaseRule):
    """Detects Iterator protocol implementation ('__iter__' and '__next__')."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_next = any(m.name == "__next__" for m in s.methods)
            has_iter = any(m.name == "__iter__" for m in s.methods)
            if has_next or has_iter:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_ITERATOR_PROTOCOL",
                        description=f"Struct '{s.name}' implements Mojo collection traversal protocol via __iter__/__next__",
                        weight=0.95,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ITERATOR_TRAIT_PROTOCOL,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class MediatorCoordinatorRule(BaseRule):
    """Detects Mediator coordinator decoupling subsystem communication."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Coordinator" in s.name or "Mediator" in s.name or "Dispatcher" in s.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_MEDIATOR_COORDINATOR",
                        description=f"Struct '{s.name}' acts as Mediator coordinating subsystem communication",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MEDIATOR_COORDINATOR,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class MementoSnapshotStateRule(BaseRule):
    """Detects Memento state snapshot structs for checkpointing and restoration."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Snapshot" in s.name or "Memento" in s.name or "Checkpoint" in s.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_MEMENTO_SNAPSHOT",
                        description=f"Struct '{s.name}' captures internal state snapshot for Memento restoration",
                        weight=0.90,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MEMENTO_SNAPSHOT_STATE,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class ObserverDispatchRegistryRule(BaseRule):
    """Detects Observer pattern dispatching notifications to registered listeners."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_subscribers = any(
                "subscriber" in f.name.lower() or "listener" in f.name.lower() or "observer" in f.name.lower()
                for f in s.fields
            )
            if has_subscribers or "Subject" in s.name or "Observable" in s.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_OBSERVER_REGISTRY",
                        description=f"Struct '{s.name}' implements Observer pattern notifying registered listeners",
                        weight=0.90,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.OBSERVER_DISPATCH_REGISTRY,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class StateTraitFsmRule(BaseRule):
    """Detects State pattern modeled over a common state trait."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_traits:
            if "State" in t.name or "Status" in t.name or "Phase" in t.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_STATE_TRAIT_FSM",
                        description=f"Trait '{t.name}' defines Finite State Machine (FSM) contract across state transitions",
                        weight=0.92,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STATE_TRAIT_FSM,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind="trait",
                        confidence=Confidence(score=0.92, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class StrategyTraitInjectionRule(BaseRule):
    """Detects Strategy pattern selecting algorithms via trait injection."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            strat_fields = [f for f in s.fields if "Strategy" in f.type_name or "Algorithm" in f.type_name or "Solver" in f.type_name]
            if strat_fields or "Strategy" in s.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_STRATEGY_TRAIT",
                        description=f"Struct '{s.name}' injects interchangeable Strategy algorithm via '{strat_fields[0].name if strat_fields else 'strategy'}'",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STRATEGY_TRAIT_INJECTION,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class TemplateMethodSkeletonRule(BaseRule):
    """Detects Template Method pattern coordinating lifecycle step hooks."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            has_steps = any(kw in fn.body for kw in ("step1", "step2", "pre_process", "post_process", "hook"))
            if has_steps and ("process" in fn.name or "run" in fn.name or "execute" in fn.name):
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_TEMPLATE_METHOD",
                        description=f"Function '{fn.name}' implements Template Method algorithm skeleton coordinating step hooks",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.TEMPLATE_METHOD_SKELETON,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class VisitorDoubleDispatchRule(BaseRule):
    """Detects Visitor pattern traversing heterogeneous node hierarchies."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if "visit" in fn.name or "accept" in fn.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_VISITOR_DISPATCH",
                        description=f"Function '{fn.name}' implements Visitor double-dispatch over node hierarchies",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.VISITOR_DOUBLE_DISPATCH,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=fn.name,
                        target_kind="fn",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
