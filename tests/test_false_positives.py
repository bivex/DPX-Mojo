"""Unit tests verifying zero false positives on clean, idiomatic Mojo code."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_mojo_parser import NativeMojoParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.rules.resilience_hazards_rules import (
    AccidentalCopyOverheadRule,
    DanglingTransferLifetimeRule,
    DynamicDefInHotPathRule,
    ScalarComputeLoopRule,
    UncheckedUnsafePointerRule,
)
from pattern_detector.domain.rules.solid_principles_rules import (
    FatTraitIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    ManualTypeSwitchOcpRule,
    MonolithicStructSrpRule,
)
from pattern_detector.domain.services.rule_engine import RuleEngineService
from pattern_detector.domain.value_objects import PatternCategory


def test_clean_simd_kernel_no_scalar_hazard() -> None:
    code = """
    fn vector_dot[width: Int](a: SIMD[DType.float32, width], b: SIMD[DType.float32, width]) -> Float32:
        return (a * b).reduce_add()
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("dot.mojo", code)])

    rule = ScalarComputeLoopRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_clean_ownership_transfer_no_dangling_hazard() -> None:
    code = """
    fn move_and_consume(owned t: Tensor) -> Tensor:
        var dest = t^
        return dest^
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("clean_move.mojo", code)])

    rule = DanglingTransferLifetimeRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_clean_borrowed_params_no_accidental_copy() -> None:
    code = """
    struct BigBuffer:
        var a: Int
        var b: Int
        var c: Int

    fn process_buf(borrowed b: BigBuffer):
        pass
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("borrow.mojo", code)])

    rule = AccidentalCopyOverheadRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_clean_focused_trait_no_fat_trait() -> None:
    code = """
    trait Serializable:
        fn serialize(self) -> String:
            ...
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("clean_trait.mojo", code)])

    rule = FatTraitIspRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_pure_domain_service_no_hazards() -> None:
    code = """
    @value
    struct LinearLayer[dtype: DType, in_dim: Int, out_dim: Int]:
        var weights: InlineArray[Scalar[dtype], in_dim * out_dim]

        fn forward(self, borrowed x: SIMD[dtype, in_dim]) -> SIMD[dtype, out_dim]:
            return x * self.weights[0]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("linear.mojo", code)])

    engine = RuleEngineService(rules=get_default_rules())
    detections = engine.evaluate(model)

    hazards = [d for d in detections if d.pattern_category in (PatternCategory.RESILIENCE, PatternCategory.PRINCIPLE)]
    assert len(hazards) == 0
