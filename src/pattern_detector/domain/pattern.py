"""Pattern metadata and catalog definitions for Mojo static analyzer."""

from __future__ import annotations

from dataclasses import dataclass
from pattern_detector.domain.value_objects import PatternCategory, PatternType


@dataclass(frozen=True)
class PatternDefinition:
    """Detailed architectural definition for a Mojo design pattern."""

    type: PatternType
    name: str
    category: PatternCategory
    description: str
    mojo_version: str = "24.x - 25.x+"
    recommendation: str | None = None


PATTERN_CATALOG: dict[PatternType, PatternDefinition] = {
    # 1. Mojo Idiomatic & Ownership
    PatternType.STRUCT_VALUE_SEMANTICS: PatternDefinition(
        type=PatternType.STRUCT_VALUE_SEMANTICS,
        name="Struct Value Semantics",
        category=PatternCategory.MOJO_IDIOMATIC,
        description="Value-semantic struct with explicit field memory layout and copy/move lifecycle hooks.",
        recommendation="Use '@value' decorator for automatic synthesization of __init__, __copyinit__, and __moveinit__.",
    ),
    PatternType.TRAIT_CONTRACT_INTERFACE: PatternDefinition(
        type=PatternType.TRAIT_CONTRACT_INTERFACE,
        name="Trait Contract Interface",
        category=PatternCategory.MOJO_IDIOMATIC,
        description="Mojo Trait contract enabling static zero-cost polymorphic interface conformance.",
        recommendation="Define focused traits to decouple component algorithms and enforce compile-time bounds.",
    ),
    PatternType.EXPLICIT_OWNERSHIP_BORROW: PatternDefinition(
        type=PatternType.EXPLICIT_OWNERSHIP_BORROW,
        name="Explicit Ownership & Borrowing",
        category=PatternCategory.MOJO_IDIOMATIC,
        description="Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.",
        recommendation="Prefer 'borrowed' for read-only access and 'inout' for in-place mutation to eliminate allocations.",
    ),
    PatternType.TRANSFER_MOVE_OPERATOR: PatternDefinition(
        type=PatternType.TRANSFER_MOVE_OPERATOR,
        name="Transfer Move Operator (^)",
        category=PatternCategory.MOJO_IDIOMATIC,
        description="Explicit ownership transfer utilizing the '^' move operator without deep cloning.",
        recommendation="Use value^ when transferring ownership of large tensors and buffers to prevent duplicate copies.",
    ),
    PatternType.DESTRUCT_RAII_LIFECYCLE: PatternDefinition(
        type=PatternType.DESTRUCT_RAII_LIFECYCLE,
        name="Destruct RAII Lifecycle",
        category=PatternCategory.MOJO_IDIOMATIC,
        description="Deterministic resource cleanup via '__del__' destructor method.",
        recommendation="Ensure raw pointers and GPU device memory allocations are freed within __del__.",
    ),
    PatternType.REGISTER_PASSABLE_LAYOUT: PatternDefinition(
        type=PatternType.REGISTER_PASSABLE_LAYOUT,
        name="Register Passable Layout",
        category=PatternCategory.MOJO_IDIOMATIC,
        description="Struct decorated with '@register_passable' or passed directly in machine registers.",
        recommendation="Apply '@register_passable' to small primitives and SIMD wrapper structs to avoid memory spills.",
    ),

    # 2. SIMD & Hardware Acceleration
    PatternType.SIMD_VECTORIZATION_KERNEL: PatternDefinition(
        type=PatternType.SIMD_VECTORIZATION_KERNEL,
        name="SIMD Vectorization Kernel",
        category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
        description="SIMD hardware vector registers (AVX-512, ARM Neon) performing multi-element parallel operations.",
        recommendation="Use 'vectorize[simd_width]' and 'SIMD[type, width]' for compute kernels.",
    ),
    PatternType.PARALLELIZE_MULTI_CORE: PatternDefinition(
        type=PatternType.PARALLELIZE_MULTI_CORE,
        name="Parallelize Multi-Core Execution",
        category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
        description="Multi-core task distribution using 'parallelize' and thread pools.",
        recommendation="Use 'parallelize' across outer matrix/tensor loops for linear multi-core scaling.",
    ),
    PatternType.UNSAFE_RAW_POINTER_BUFFER: PatternDefinition(
        type=PatternType.UNSAFE_RAW_POINTER_BUFFER,
        name="Unsafe Raw Pointer Buffer",
        category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
        description="Direct memory buffer manipulation via 'UnsafePointer' or 'DTypePointer'.",
        recommendation="Wrap raw pointers in safe RAII structs with boundary validation.",
    ),
    PatternType.TENSOR_TILING_KERNEL: PatternDefinition(
        type=PatternType.TENSOR_TILING_KERNEL,
        name="Tensor Tiling & Cache Blocking",
        category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
        description="2D/3D cache-blocked matrix multiplication tiling to fit inside L1/L2 CPU/GPU caches.",
        recommendation="Implement tile-based iteration for high-arithmetic-intensity tensor kernels.",
    ),

    # 3. Compile-Time Metaprogramming
    PatternType.COMPTIME_PARAMETER_SPECIALIZATION: PatternDefinition(
        type=PatternType.COMPTIME_PARAMETER_SPECIALIZATION,
        name="Comptime Parameter Specialization",
        category=PatternCategory.COMPTIME_METAPROGRAMMING,
        description="Compile-time parameters ('[type: DType, width: Int]') generating specialized machine code.",
        recommendation="Parameterize data types and SIMD widths for zero-overhead hardware adaptation.",
    ),
    PatternType.ALIAS_TYPE_METAPROGRAMMING: PatternDefinition(
        type=PatternType.ALIAS_TYPE_METAPROGRAMMING,
        name="Alias Type Metaprogramming",
        category=PatternCategory.COMPTIME_METAPROGRAMMING,
        description="Compile-time 'alias' declarations binding types, dimensions, or constants.",
        recommendation="Use 'alias' for compile-time tensor shape constants and DType aliases.",
    ),
    PatternType.COMPILE_TIME_BRANCH_SPECIALIZATION: PatternDefinition(
        type=PatternType.COMPILE_TIME_BRANCH_SPECIALIZATION,
        name="Compile-Time Branch Specialization",
        category=PatternCategory.COMPTIME_METAPROGRAMMING,
        description="'@parameter if' compile-time dead code elimination.",
        recommendation="Use '@parameter if' to eliminate runtime branches on hardware capabilities.",
    ),

    # 4. Creational Patterns (GoF 5/5)
    PatternType.SINGLETON_GLOBAL_INSTANCE: PatternDefinition(
        type=PatternType.SINGLETON_GLOBAL_INSTANCE,
        name="Singleton Global Instance",
        category=PatternCategory.CREATIONAL,
        description="Unique global instance or static coordinator struct.",
    ),
    PatternType.FACTORY_METHOD_CONSTRUCTOR: PatternDefinition(
        type=PatternType.FACTORY_METHOD_CONSTRUCTOR,
        name="Factory Method Constructor",
        category=PatternCategory.CREATIONAL,
        description="Static constructor or factory function instantiating specialized types.",
    ),
    PatternType.ABSTRACT_FACTORY_TRAIT: PatternDefinition(
        type=PatternType.ABSTRACT_FACTORY_TRAIT,
        name="Abstract Factory Trait",
        category=PatternCategory.CREATIONAL,
        description="Trait defining a contract for creating families of related structs.",
    ),
    PatternType.BUILDER_FLUENT_STRUCT: PatternDefinition(
        type=PatternType.BUILDER_FLUENT_STRUCT,
        name="Builder Fluent Struct",
        category=PatternCategory.CREATIONAL,
        description="Struct accumulating configuration options before final object construction.",
    ),
    PatternType.PROTOTYPE_CLONE_COPY: PatternDefinition(
        type=PatternType.PROTOTYPE_CLONE_COPY,
        name="Prototype Clone Copy",
        category=PatternCategory.CREATIONAL,
        description="Object duplication via '__copyinit__' or explicit clone() methods.",
    ),

    # 5. Structural Patterns (GoF 7/7)
    PatternType.ADAPTER_STRUCT_WRAPPER: PatternDefinition(
        type=PatternType.ADAPTER_STRUCT_WRAPPER,
        name="Adapter Struct Wrapper",
        category=PatternCategory.STRUCTURAL,
        description="Struct wrapping external or low-level types to conform to domain traits.",
    ),
    PatternType.BRIDGE_HARDWARE_DRIVER: PatternDefinition(
        type=PatternType.BRIDGE_HARDWARE_DRIVER,
        name="Bridge Hardware Driver",
        category=PatternCategory.STRUCTURAL,
        description="Decoupling compute abstraction from hardware implementor drivers (CPU/GPU/TPU).",
    ),
    PatternType.COMPOSITE_TREE_HIERARCHY: PatternDefinition(
        type=PatternType.COMPOSITE_TREE_HIERARCHY,
        name="Composite Tree Hierarchy",
        category=PatternCategory.STRUCTURAL,
        description="Recursive tree node structures for syntax trees and tensor computation graphs.",
    ),
    PatternType.DECORATOR_FORWARDING_WRAPPER: PatternDefinition(
        type=PatternType.DECORATOR_FORWARDING_WRAPPER,
        name="Decorator Forwarding Wrapper",
        category=PatternCategory.STRUCTURAL,
        description="Struct wrapping an underlying instance to augment functionality.",
    ),
    PatternType.FACADE_UNIFIED_API: PatternDefinition(
        type=PatternType.FACADE_UNIFIED_API,
        name="Facade Unified API",
        category=PatternCategory.STRUCTURAL,
        description="Unified top-level API struct coordinating multiple subsystem components.",
    ),
    PatternType.FLYWEIGHT_SHARED_POOL: PatternDefinition(
        type=PatternType.FLYWEIGHT_SHARED_POOL,
        name="Flyweight Shared Pool",
        category=PatternCategory.STRUCTURAL,
        description="Sharing immutable instances via pool or dictionary to conserve memory.",
    ),
    PatternType.PROXY_LAZY_RESOURCE: PatternDefinition(
        type=PatternType.PROXY_LAZY_RESOURCE,
        name="Proxy Lazy Resource",
        category=PatternCategory.STRUCTURAL,
        description="Surrogate controlling access or delaying allocation of heavy GPU buffers.",
    ),

    # 6. Behavioral Patterns (GoF 11/11)
    PatternType.CHAIN_OF_RESPONSIBILITY_CHAIN: PatternDefinition(
        type=PatternType.CHAIN_OF_RESPONSIBILITY_CHAIN,
        name="Chain of Responsibility",
        category=PatternCategory.BEHAVIORAL,
        description="Middleware or handler structs passing requests sequentially along a pipeline.",
    ),
    PatternType.COMMAND_CALLABLE_TASK: PatternDefinition(
        type=PatternType.COMMAND_CALLABLE_TASK,
        name="Command Callable Task",
        category=PatternCategory.BEHAVIORAL,
        description="Command objects encapsulating actions and execution parameters.",
    ),
    PatternType.INTERPRETER_AST_EVAL: PatternDefinition(
        type=PatternType.INTERPRETER_AST_EVAL,
        name="Interpreter AST Eval",
        category=PatternCategory.BEHAVIORAL,
        description="Domain AST expression evaluator executing custom mathematical grammar.",
    ),
    PatternType.ITERATOR_TRAIT_PROTOCOL: PatternDefinition(
        type=PatternType.ITERATOR_TRAIT_PROTOCOL,
        name="Iterator Trait Protocol",
        category=PatternCategory.BEHAVIORAL,
        description="Mojo collection traversal protocol implementing '__iter__' and '__next__'.",
    ),
    PatternType.MEDIATOR_COORDINATOR: PatternDefinition(
        type=PatternType.MEDIATOR_COORDINATOR,
        name="Mediator Coordinator",
        category=PatternCategory.BEHAVIORAL,
        description="Central coordinator mediating interaction between independent subsystems.",
    ),
    PatternType.MEMENTO_SNAPSHOT_STATE: PatternDefinition(
        type=PatternType.MEMENTO_SNAPSHOT_STATE,
        name="Memento Snapshot State",
        category=PatternCategory.BEHAVIORAL,
        description="State snapshot struct capturing internal state for checkpoint restoration.",
    ),
    PatternType.OBSERVER_DISPATCH_REGISTRY: PatternDefinition(
        type=PatternType.OBSERVER_DISPATCH_REGISTRY,
        name="Observer Dispatch Registry",
        category=PatternCategory.BEHAVIORAL,
        description="Event broadcasting to subscribed listeners or callbacks.",
    ),
    PatternType.STATE_TRAIT_FSM: PatternDefinition(
        type=PatternType.STATE_TRAIT_FSM,
        name="State Trait FSM",
        category=PatternCategory.BEHAVIORAL,
        description="Finite state machine where states conform to a common state trait.",
    ),
    PatternType.STRATEGY_TRAIT_INJECTION: PatternDefinition(
        type=PatternType.STRATEGY_TRAIT_INJECTION,
        name="Strategy Trait Injection",
        category=PatternCategory.BEHAVIORAL,
        description="Interchangeable algorithm strategy injected via trait bounds.",
    ),
    PatternType.TEMPLATE_METHOD_SKELETON: PatternDefinition(
        type=PatternType.TEMPLATE_METHOD_SKELETON,
        name="Template Method Skeleton",
        category=PatternCategory.BEHAVIORAL,
        description="Algorithm skeleton coordinating customizable step hooks.",
    ),
    PatternType.VISITOR_DOUBLE_DISPATCH: PatternDefinition(
        type=PatternType.VISITOR_DOUBLE_DISPATCH,
        name="Visitor Double Dispatch",
        category=PatternCategory.BEHAVIORAL,
        description="Double-dispatch operations traversing heterogeneous node hierarchies.",
    ),

    # 7. Hazards & Resilience
    PatternType.UNCHECKED_UNSAFE_POINTER: PatternDefinition(
        type=PatternType.UNCHECKED_UNSAFE_POINTER,
        name="Unchecked Unsafe Pointer",
        category=PatternCategory.RESILIENCE,
        description="Raw UnsafePointer offset and dereference without bounds checking.",
        recommendation="Wrap UnsafePointer in safe abstraction or validate indices before pointer arithmetic.",
    ),
    PatternType.DYNAMIC_DEF_IN_HOT_PATH: PatternDefinition(
        type=PatternType.DYNAMIC_DEF_IN_HOT_PATH,
        name="Dynamic 'def' in Hot Path",
        category=PatternCategory.RESILIENCE,
        description="Dynamic Python-style 'def' function used in compute-intensive code.",
        recommendation="Replace 'def' with strictly typed 'fn' for compile-time optimization and zero runtime overhead.",
    ),
    PatternType.ACCIDENTAL_COPY_OVERHEAD: PatternDefinition(
        type=PatternType.ACCIDENTAL_COPY_OVERHEAD,
        name="Accidental Copy Overhead",
        category=PatternCategory.RESILIENCE,
        description="Large struct or buffer passed by value without 'borrowed' or 'inout'.",
        recommendation="Annotate parameter as 'borrowed' or 'inout' to eliminate expensive memory copies.",
    ),
    PatternType.SCALAR_COMPUTE_LOOP: PatternDefinition(
        type=PatternType.SCALAR_COMPUTE_LOOP,
        name="Scalar Compute Loop",
        category=PatternCategory.RESILIENCE,
        description="Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.",
        recommendation="Refactor scalar loop to use 'vectorize' or SIMD registers for hardware acceleration.",
    ),
    PatternType.DANGLING_TRANSFER_LIFETIME: PatternDefinition(
        type=PatternType.DANGLING_TRANSFER_LIFETIME,
        name="Dangling Transfer Lifetime",
        category=PatternCategory.RESILIENCE,
        description="Value used after ownership transfer ('^').",
        recommendation="Do not reference a variable after moving it with the transfer operator.",
    ),

    # 8. SOLID Principles
    PatternType.MONOLITHIC_STRUCT_SRP: PatternDefinition(
        type=PatternType.MONOLITHIC_STRUCT_SRP,
        name="Monolithic Struct (SRP)",
        category=PatternCategory.PRINCIPLE,
        description="Struct declaring excessive fields or methods, violating SRP.",
    ),
    PatternType.FAT_TRAIT_ISP: PatternDefinition(
        type=PatternType.FAT_TRAIT_ISP,
        name="Fat Trait (ISP)",
        category=PatternCategory.PRINCIPLE,
        description="Trait requiring too many method implementations, violating ISP.",
    ),
    PatternType.MANUAL_TYPE_SWITCH_OCP: PatternDefinition(
        type=PatternType.MANUAL_TYPE_SWITCH_OCP,
        name="Manual Type Switch (OCP)",
        category=PatternCategory.PRINCIPLE,
        description="Manual 'if type == ...' branching instead of polymorphic traits, violating OCP.",
    ),
    PatternType.KISS_CYCLOMATIC_COMPLEXITY: PatternDefinition(
        type=PatternType.KISS_CYCLOMATIC_COMPLEXITY,
        name="High Cyclomatic Complexity",
        category=PatternCategory.PRINCIPLE,
        description="Function containing excessive decision branch points (> 8).",
    ),
    PatternType.KISS_LONG_PARAMETER_LIST: PatternDefinition(
        type=PatternType.KISS_LONG_PARAMETER_LIST,
        name="Long Parameter List",
        category=PatternCategory.PRINCIPLE,
        description="Function accepting >= 6 positional parameters.",
    ),
    PatternType.DRY_DUPLICATE_LOGIC: PatternDefinition(
        type=PatternType.DRY_DUPLICATE_LOGIC,
        name="Duplicate Logic (DRY)",
        category=PatternCategory.PRINCIPLE,
        description="Duplicated algorithmic sequences across multiple functions.",
    ),
    PatternType.DEMETER_LAW_TRAIN_WRECK: PatternDefinition(
        type=PatternType.DEMETER_LAW_TRAIN_WRECK,
        name="Law of Demeter Violation",
        category=PatternCategory.PRINCIPLE,
        description="Deep field/method navigation chains ('a.b.c.d.e').",
    ),
}
