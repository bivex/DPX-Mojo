fn vectorized_add[width: Int](a: SIMD[DType.float32, width], b: SIMD[DType.float32, width]) -> SIMD[DType.float32, width]:
    return a + b

fn tiled_matmul_kernel[tile_size: Int](a: Tensor, b: Tensor, inout c: Tensor):
    alias tile_m = 32
    alias tile_n = 32

    @parameter
    if tile_size == 32:
        for i in range(0, a.shape.rows, tile_m):
            for j in range(0, b.shape.cols, tile_n):
                c.data_ptr.store(i * b.shape.cols + j, 1.0)

fn parallel_tensor_dispatch(inout tensor: Tensor):
    parallelize[worker_func](tensor.shape.rows)
