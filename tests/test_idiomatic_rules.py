"""Unit tests for Mojo Idiomatic, Ownership, and Value Semantics rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_mojo_parser import NativeMojoParserAdapter
from pattern_detector.domain.rules.idiomatic_rules import (
    DestructRaiiLifecycleRule,
    ExplicitOwnershipBorrowRule,
    RegisterPassableLayoutRule,
    StructValueSemanticsRule,
    TraitContractInterfaceRule,
    TransferMoveOperatorRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_struct_value_semantics() -> None:
    code = """
    @value
    struct TensorShape:
        var dims: DynamicVector[Int]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("shape.mojo", code)])

    rule = StructValueSemanticsRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STRUCT_VALUE_SEMANTICS
    assert detections[0].target_name == "TensorShape"


def test_trait_contract_interface() -> None:
    code = """
    trait Layer:
        fn forward(self, input: Tensor) -> Tensor:
            ...
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("layer.mojo", code)])

    rule = TraitContractInterfaceRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TRAIT_CONTRACT_INTERFACE
    assert detections[0].target_name == "Layer"


def test_explicit_ownership_borrow() -> None:
    code = """
    fn update_weights(inout weights: Tensor, borrowed gradients: Tensor, owned lr: Float32):
        weights.data = weights.data - (gradients.data * lr)
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("opt.mojo", code)])

    rule = ExplicitOwnershipBorrowRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.EXPLICIT_OWNERSHIP_BORROW


def test_transfer_move_operator() -> None:
    code = """
    fn process_tensor(owned t: Tensor):
        var dest = t^
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("move.mojo", code)])

    rule = TransferMoveOperatorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TRANSFER_MOVE_OPERATOR


def test_destruct_raii_lifecycle() -> None:
    code = """
    struct DeviceBuffer:
        var ptr: UnsafePointer[Float32]

        fn __del__(owned self):
            self.ptr.free()
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("buf.mojo", code)])

    rule = DestructRaiiLifecycleRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DESTRUCT_RAII_LIFECYCLE


def test_register_passable_layout() -> None:
    code = """
    @register_passable("trivial")
    struct Float2:
        var x: Float32
        var y: Float32
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("vec2.mojo", code)])

    rule = RegisterPassableLayoutRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.REGISTER_PASSABLE_LAYOUT
