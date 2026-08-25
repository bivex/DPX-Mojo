"""Domain value objects, enums, and locations for Mojo pattern detection."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class PatternCategory(str, Enum):
    """Categorical classification of detected Mojo architectural patterns."""

    MOJO_IDIOMATIC = "mojo_idiomatic"
    SIMD_HARDWARE_ACCELERATION = "simd_hardware_acceleration"
    COMPTIME_METAPROGRAMMING = "comptime_metaprogramming"
    CREATIONAL = "creational"
    STRUCTURAL = "structural"
    BEHAVIORAL = "behavioral"
    RESILIENCE = "resilience"
    PRINCIPLE = "principle"


class PatternType(str, Enum):
    """Catalog of all 43 supported Mojo architectural patterns and checks."""

    # 1. Mojo Idiomatic & Ownership (6)
    STRUCT_VALUE_SEMANTICS = "struct_value_semantics"
    TRAIT_CONTRACT_INTERFACE = "trait_contract_interface"
    EXPLICIT_OWNERSHIP_BORROW = "explicit_ownership_borrow"
    TRANSFER_MOVE_OPERATOR = "transfer_move_operator"
    DESTRUCT_RAII_LIFECYCLE = "destruct_raii_lifecycle"
    REGISTER_PASSABLE_LAYOUT = "register_passable_layout"

    # 2. SIMD & Hardware Acceleration (4)
    SIMD_VECTORIZATION_KERNEL = "simd_vectorization_kernel"
    PARALLELIZE_MULTI_CORE = "parallelize_multi_core"
    UNSAFE_RAW_POINTER_BUFFER = "unsafe_raw_pointer_buffer"
    TENSOR_TILING_KERNEL = "tensor_tiling_kernel"

    # 3. Compile-Time Metaprogramming (3)
    COMPTIME_PARAMETER_SPECIALIZATION = "comptime_parameter_specialization"
    ALIAS_TYPE_METAPROGRAMMING = "alias_type_metaprogramming"
    COMPILE_TIME_BRANCH_SPECIALIZATION = "compile_time_branch_specialization"

    # 4. GoF Creational (5/5)
    SINGLETON_GLOBAL_INSTANCE = "singleton_global_instance"
    FACTORY_METHOD_CONSTRUCTOR = "factory_method_constructor"
    ABSTRACT_FACTORY_TRAIT = "abstract_factory_trait"
    BUILDER_FLUENT_STRUCT = "builder_fluent_struct"
    PROTOTYPE_CLONE_COPY = "prototype_clone_copy"

    # 5. GoF Structural (7/7)
    ADAPTER_STRUCT_WRAPPER = "adapter_struct_wrapper"
    BRIDGE_HARDWARE_DRIVER = "bridge_hardware_driver"
    COMPOSITE_TREE_HIERARCHY = "composite_tree_hierarchy"
    DECORATOR_FORWARDING_WRAPPER = "decorator_forwarding_wrapper"
    FACADE_UNIFIED_API = "facade_unified_api"
    FLYWEIGHT_SHARED_POOL = "flyweight_shared_pool"
    PROXY_LAZY_RESOURCE = "proxy_lazy_resource"

    # 6. GoF Behavioral (11/11)
    CHAIN_OF_RESPONSIBILITY_CHAIN = "chain_of_responsibility_chain"
    COMMAND_CALLABLE_TASK = "command_callable_task"
    INTERPRETER_AST_EVAL = "interpreter_ast_eval"
    ITERATOR_TRAIT_PROTOCOL = "iterator_trait_protocol"
    MEDIATOR_COORDINATOR = "mediator_coordinator"
    MEMENTO_SNAPSHOT_STATE = "memento_snapshot_state"
    OBSERVER_DISPATCH_REGISTRY = "observer_dispatch_registry"
    STATE_TRAIT_FSM = "state_trait_fsm"
    STRATEGY_TRAIT_INJECTION = "strategy_trait_injection"
    TEMPLATE_METHOD_SKELETON = "template_method_skeleton"
    VISITOR_DOUBLE_DISPATCH = "visitor_double_dispatch"

    # 7. Safety, Performance & Resilience Hazards (5)
    UNCHECKED_UNSAFE_POINTER = "unchecked_unsafe_pointer"
    DYNAMIC_DEF_IN_HOT_PATH = "dynamic_def_in_hot_path"
    ACCIDENTAL_COPY_OVERHEAD = "accidental_copy_overhead"
    SCALAR_COMPUTE_LOOP = "scalar_compute_loop"
    DANGLING_TRANSFER_LIFETIME = "dangling_transfer_lifetime"

    # 8. SOLID & Clean Code Principles (7)
    MONOLITHIC_STRUCT_SRP = "monolithic_struct_srp"
    FAT_TRAIT_ISP = "fat_trait_isp"
    MANUAL_TYPE_SWITCH_OCP = "manual_type_switch_ocp"
    KISS_CYCLOMATIC_COMPLEXITY = "kiss_cyclomatic_complexity"
    KISS_LONG_PARAMETER_LIST = "kiss_long_parameter_list"
    DRY_DUPLICATE_LOGIC = "dry_duplicate_logic"
    DEMETER_LAW_TRAIN_WRECK = "demeter_law_train_wreck"


class ConfidenceLevel(str, Enum):
    """Categorical confidence level thresholds."""

    VERY_HIGH = "VERY_HIGH"  # >= 0.85
    HIGH = "HIGH"            # >= 0.70
    MEDIUM = "MEDIUM"        # >= 0.50
    LOW = "LOW"              # < 0.50


@dataclass(frozen=True)
class SourceLocation:
    """Precise source code location in a Mojo file (.mojo, .🔥)."""

    file_path: str
    line: int
    column: int = 1

    def __str__(self) -> str:
        return f"{self.file_path}:{self.line}:{self.column}"


@dataclass(frozen=True)
class Evidence:
    """Individual heuristic evidence contributing to a detection."""

    rule_code: str
    description: str
    weight: float
    location: SourceLocation | None = None


@dataclass
class Confidence:
    """Aggregate confidence score and associated evidence list."""

    score: float
    evidences: list[Evidence] = field(default_factory=list)

    @property
    def level(self) -> ConfidenceLevel:
        if self.score >= 0.85:
            return ConfidenceLevel.VERY_HIGH
        if self.score >= 0.70:
            return ConfidenceLevel.HIGH
        if self.score >= 0.50:
            return ConfidenceLevel.MEDIUM
        return ConfidenceLevel.LOW

    @property
    def percentage_str(self) -> str:
        return f"{int(self.score * 100)}%"
