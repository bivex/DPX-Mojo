alias DTypeFloat = DType.float32
alias SIMDWidth = 8

trait ComputeLayer:
    fn forward(self, input: Tensor) -> Tensor:
        ...

@value
struct TensorShape:
    var rows: Int
    var cols: Int

@register_passable("trivial")
struct Vec2:
    var x: Float32
    var y: Float32

@value
struct Tensor:
    var shape: TensorShape
    var data_ptr: UnsafePointer[Float32]

    fn __del__(owned self):
        if self.data_ptr:
            self.data_ptr.free()
