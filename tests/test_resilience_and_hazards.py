"""Unit tests for Mojo Resilience, Safety, and Performance Hazards."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_mojo_parser import NativeMojoParserAdapter
from pattern_detector.domain.rules.resilience_hazards_rules import (
    AccidentalCopyOverheadRule,
    DanglingTransferLifetimeRule,
    DynamicDefInHotPathRule,
    ScalarComputeLoopRule,
    UncheckedUnsafePointerRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_unchecked_unsafe_pointer() -> None:
    code = """
    fn read_memory(ptr: UnsafePointer[Float32]) -> Float32:
        return ptr.load(10)
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("ptr.mojo", code)])

    rule = UncheckedUnsafePointerRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.UNCHECKED_UNSAFE_POINTER


def test_dynamic_def_in_hot_path() -> None:
    code = """
    def compute_kernel(data):
        for i in range(1000):
            process(data[i])
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("def.mojo", code)])

    rule = DynamicDefInHotPathRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DYNAMIC_DEF_IN_HOT_PATH


def test_accidental_copy_overhead() -> None:
    code = """
    struct LargeMatrix:
        var a: Int
        var b: Int
        var c: Int

    fn process_matrix(m: LargeMatrix):
        pass
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("copy.mojo", code)])

    rule = AccidentalCopyOverheadRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ACCIDENTAL_COPY_OVERHEAD


def test_scalar_compute_loop() -> None:
    code = """
    fn matmul_kernel(a: Tensor, b: Tensor):
        for i in range(100):
            c[i] = a[i] * b[i]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("scalar.mojo", code)])

    rule = ScalarComputeLoopRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SCALAR_COMPUTE_LOOP


def test_dangling_transfer_lifetime() -> None:
    code = """
    fn bad_transfer(owned t: Tensor):
        var dest = t^
        print(t.size)
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("transfer.mojo", code)])

    rule = DanglingTransferLifetimeRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DANGLING_TRANSFER_LIFETIME
