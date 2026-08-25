"""Unit tests for Mojo SOLID and clean code quality rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_mojo_parser import NativeMojoParserAdapter
from pattern_detector.domain.rules.solid_principles_rules import (
    FatTraitIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    ManualTypeSwitchOcpRule,
    MonolithicStructSrpRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_monolithic_struct_srp() -> None:
    fields_code = "\n".join(f"    var field_{i}: Float32" for i in range(12))
    code = f"""struct BigDataStruct:
{fields_code}
"""
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("big.mojo", code)])

    rule = MonolithicStructSrpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MONOLITHIC_STRUCT_SRP


def test_fat_trait_isp() -> None:
    methods_code = "\n".join(f"    fn method_{i}(self) -> None: ..." for i in range(8))
    code = f"""trait MegaTrait:
{methods_code}
"""
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("mega.mojo", code)])

    rule = FatTraitIspRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FAT_TRAIT_ISP


def test_manual_type_switch_ocp() -> None:
    code = """
    fn render_shape(s: Shape):
        if s.kind == 1:
            draw_circle()
        elif s.kind == 2:
            draw_rect()
        elif s.kind == 3:
            draw_triangle()
        elif s.kind == 4:
            draw_poly()
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("switch.mojo", code)])

    rule = ManualTypeSwitchOcpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MANUAL_TYPE_SWITCH_OCP


def test_kiss_cyclomatic_complexity() -> None:
    branches = "\n".join(f"    if x == {i}: print({i})" for i in range(10))
    code = f"""fn complex_decision(x: Int):
{branches}
"""
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("complex.mojo", code)])

    rule = KissCyclomaticComplexityRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.KISS_CYCLOMATIC_COMPLEXITY


def test_kiss_long_parameter_list() -> None:
    code = """
    fn configure_kernel(grid_x: Int, grid_y: Int, block_x: Int, block_y: Int, shared_mem: Int, stream: Int, sync: Bool):
        pass
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("params.mojo", code)])

    rule = KissLongParameterListRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.KISS_LONG_PARAMETER_LIST
