"""Unit tests for Mojo SIMD vectorization and hardware acceleration rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_mojo_parser import NativeMojoParserAdapter
from pattern_detector.domain.rules.simd_hardware_rules import (
    ParallelizeMultiCoreRule,
    SimdVectorizationKernelRule,
    TensorTilingKernelRule,
    UnsafeRawPointerBufferRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_simd_vectorization_kernel() -> None:
    code = """
    fn vector_add[width: Int](a: SIMD[DType.float32, width], b: SIMD[DType.float32, width]) -> SIMD[DType.float32, width]:
        return a + b
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("simd.mojo", code)])

    rule = SimdVectorizationKernelRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SIMD_VECTORIZATION_KERNEL


def test_parallelize_multi_core() -> None:
    code = """
    fn parallel_matrix_fill(inout matrix: Tensor):
        parallelize[worker_closure](matrix.rows)
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("parallel.mojo", code)])

    rule = ParallelizeMultiCoreRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PARALLELIZE_MULTI_CORE


def test_unsafe_raw_pointer_buffer() -> None:
    code = """
    struct RawTensorBuffer:
        var data_ptr: UnsafePointer[Float32]
        var size: Int
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("buffer.mojo", code)])

    rule = UnsafeRawPointerBufferRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.UNSAFE_RAW_POINTER_BUFFER


def test_tensor_tiling_kernel() -> None:
    code = """
    fn tiled_matmul(a: Tensor, b: Tensor, inout c: Tensor):
        alias tile_m = 64
        alias tile_n = 64
        for i in range(0, a.rows, tile_m):
            for j in range(0, b.cols, tile_n):
                compute_block(i, j)
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("tiling.mojo", code)])

    rule = TensorTilingKernelRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TENSOR_TILING_KERNEL
