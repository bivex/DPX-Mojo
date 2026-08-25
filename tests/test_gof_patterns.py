"""Unit tests for all 23 GoF Creational, Structural, and Behavioral patterns in Mojo."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_mojo_parser import NativeMojoParserAdapter
from pattern_detector.domain.rules.behavioral_rules import (
    ChainOfResponsibilityChainRule,
    CommandCallableTaskRule,
    InterpreterAstEvalRule,
    IteratorTraitProtocolRule,
    MediatorCoordinatorRule,
    MementoSnapshotStateRule,
    ObserverDispatchRegistryRule,
    StateTraitFsmRule,
    StrategyTraitInjectionRule,
    TemplateMethodSkeletonRule,
    VisitorDoubleDispatchRule,
)
from pattern_detector.domain.rules.creational_rules import (
    AbstractFactoryTraitRule,
    BuilderFluentStructRule,
    FactoryMethodConstructorRule,
    PrototypeCloneCopyRule,
    SingletonGlobalInstanceRule,
)
from pattern_detector.domain.rules.structural_rules import (
    AdapterStructWrapperRule,
    BridgeHardwareDriverRule,
    CompositeTreeHierarchyRule,
    DecoratorForwardingWrapperRule,
    FacadeUnifiedApiRule,
    FlyweightSharedPoolRule,
    ProxyLazyResourceRule,
)
from pattern_detector.domain.value_objects import PatternType


# --- Creational (5/5) ---

def test_singleton_global_instance() -> None:
    code = """
    struct GlobalEngineConfig:
        pass
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("singleton.mojo", code)])

    rule = SingletonGlobalInstanceRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SINGLETON_GLOBAL_INSTANCE


def test_factory_method_constructor() -> None:
    code = """
    fn create_dense_layer(in_features: Int, out_features: Int) -> DenseLayer:
        return DenseLayer(in_features, out_features)
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("factory.mojo", code)])

    rule = FactoryMethodConstructorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FACTORY_METHOD_CONSTRUCTOR


def test_abstract_factory_trait() -> None:
    code = """
    trait LayerFactory:
        fn build_layer(self) -> Layer:
            ...
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("factory_trait.mojo", code)])

    rule = AbstractFactoryTraitRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ABSTRACT_FACTORY_TRAIT


def test_builder_fluent_struct() -> None:
    code = """
    struct ModelGraphBuilder:
        var layers_count: Int
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("builder.mojo", code)])

    rule = BuilderFluentStructRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.BUILDER_FLUENT_STRUCT


def test_prototype_clone_copy() -> None:
    code = """
    struct TensorBuffer(Copyable):
        var size: Int

        fn __copyinit__(inout self, existing: Self):
            self.size = existing.size
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("proto.mojo", code)])

    rule = PrototypeCloneCopyRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PROTOTYPE_CLONE_COPY


# --- Structural (7/7) ---

def test_adapter_struct_wrapper() -> None:
    code = """
    struct LegacyStreamAdapter:
        var stream_handle: Int
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("adapter.mojo", code)])

    rule = AdapterStructWrapperRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ADAPTER_STRUCT_WRAPPER


def test_bridge_hardware_driver() -> None:
    code = """
    struct ComputePipeline:
        var backend_driver: CudaBackendDriver
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("bridge.mojo", code)])

    rule = BridgeHardwareDriverRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.BRIDGE_HARDWARE_DRIVER


def test_composite_tree_hierarchy() -> None:
    code = """
    struct ComputeGraphNode:
        var name: String
        var children: DynamicVector[Node]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("composite.mojo", code)])

    rule = CompositeTreeHierarchyRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMPOSITE_TREE_HIERARCHY


def test_decorator_forwarding_wrapper() -> None:
    code = """
    struct ProfilingDecorator:
        var inner: ExecutionEngine
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("decorator.mojo", code)])

    rule = DecoratorForwardingWrapperRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DECORATOR_FORWARDING_WRAPPER


def test_facade_unified_api() -> None:
    code = """
    struct EngineFacade:
        var parser: Int
        var compiler: Int
        var runtime: Int

        fn init_all(self): ...
        fn compile_model(self): ...
        fn execute(self): ...
        fn shutdown(self): ...
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("facade.mojo", code)])

    rule = FacadeUnifiedApiRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FACADE_UNIFIED_API


def test_flyweight_shared_pool() -> None:
    code = """
    struct ConstantPool:
        var cache: Dict[String, Int]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("flyweight.mojo", code)])

    rule = FlyweightSharedPoolRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FLYWEIGHT_SHARED_POOL


def test_proxy_lazy_resource() -> None:
    code = """
    struct LazyGpuBufferProxy:
        var device_id: Int
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("proxy.mojo", code)])

    rule = ProxyLazyResourceRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PROXY_LAZY_RESOURCE


# --- Behavioral (11/11) ---

def test_chain_of_responsibility() -> None:
    code = """
    struct SecurityHandler:
        var next_handler: Handler
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("chain.mojo", code)])

    rule = ChainOfResponsibilityChainRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CHAIN_OF_RESPONSIBILITY_CHAIN


def test_command_callable_task() -> None:
    code = """
    struct LaunchKernelCommand:
        var grid_dim: Int
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("command.mojo", code)])

    rule = CommandCallableTaskRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMMAND_CALLABLE_TASK


def test_interpreter_ast_eval() -> None:
    code = """
    fn evaluate(ast_expr: ASTNode) -> Float32:
        return 42.0
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("eval.mojo", code)])

    rule = InterpreterAstEvalRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.INTERPRETER_AST_EVAL


def test_iterator_trait_protocol() -> None:
    code = """
    struct TensorIterator:
        var index: Int

        fn __iter__(self) -> Self:
            return self

        fn __next__(inout self) -> Int:
            self.index += 1
            return self.index
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("iter.mojo", code)])

    rule = IteratorTraitProtocolRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ITERATOR_TRAIT_PROTOCOL


def test_mediator_coordinator() -> None:
    code = """
    struct PipelineCoordinator:
        var channel_id: Int
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("mediator.mojo", code)])

    rule = MediatorCoordinatorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MEDIATOR_COORDINATOR


def test_memento_snapshot_state() -> None:
    code = """
    struct OptimizerStateSnapshot:
        var step: Int
        var loss: Float32
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("memento.mojo", code)])

    rule = MementoSnapshotStateRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MEMENTO_SNAPSHOT_STATE


def test_observer_dispatch_registry() -> None:
    code = """
    struct EpochProgressSubject:
        var observers: List[Observer]
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("observer.mojo", code)])

    rule = ObserverDispatchRegistryRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.OBSERVER_DISPATCH_REGISTRY


def test_state_trait_fsm() -> None:
    code = """
    trait TrainingState:
        fn on_enter(self): ...
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("state.mojo", code)])

    rule = StateTraitFsmRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STATE_TRAIT_FSM


def test_strategy_trait_injection() -> None:
    code = """
    struct TrainingLoop:
        var solver_strategy: AdamStrategy
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("strategy.mojo", code)])

    rule = StrategyTraitInjectionRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STRATEGY_TRAIT_INJECTION


def test_template_method_skeleton() -> None:
    code = """
    fn process_pipeline(data: Tensor):
        step1_validate(data)
        step2_transform(data)
        step3_save(data)
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("template.mojo", code)])

    rule = TemplateMethodSkeletonRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TEMPLATE_METHOD_SKELETON


def test_visitor_double_dispatch() -> None:
    code = """
    fn visit(node: Node, inout visitor: ASTVisitor):
        visitor.count += 1
    """
    parser = NativeMojoParserAdapter()
    model = parser.parse_codebase([("visitor.mojo", code)])

    rule = VisitorDoubleDispatchRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.VISITOR_DOUBLE_DISPATCH
