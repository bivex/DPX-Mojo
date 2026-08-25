"""Unit tests for Mojo Compile-Time Metaprogramming rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_mojo_parser import NativeMojoParserAdapter
from pattern_detector.domain.rules.comptime_rules import (
    AliasTypeMetaprogrammingRule,
    CompileTimeBranchSpecializationRule,
    ComptimeParameterSpecializationRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_comptime_parameter_specialization() -> None:
    code = """
    struct Matrix[dtype: DType, rows: Int, cols: Int]:
        var data: InlineArray[Scalar[dtype], rows * cols]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("mat.mojo", code)])

    rule = ComptimeParameterSpecializationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMPTIME_PARAMETER_SPECIALIZATION


def test_alias_type_metaprogramming() -> None:
    code = """
    alias FloatVector = SIMD[DType.float32, 16]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("alias.mojo", code)])

    rule = AliasTypeMetaprogrammingRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ALIAS_TYPE_METAPROGRAMMING
    assert detections[0].target_name == "FloatVector"


def test_compile_time_branch_specialization() -> None:
    code = """
    fn dispatch_kernel[simd_width: Int]():
        @parameter
        if simd_width == 16:
            avx512_kernel()
        else:
            scalar_fallback()
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("branch.mojo", code)])

    rule = CompileTimeBranchSpecializationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMPILE_TIME_BRANCH_SPECIALIZATION
