"""Rules registry and aggregation factory for Mojo pattern detector."""

from __future__ import annotations

from pattern_detector.domain.rules.base import BaseRule
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
from pattern_detector.domain.rules.comptime_rules import (
    AliasTypeMetaprogrammingRule,
    CompileTimeBranchSpecializationRule,
    ComptimeParameterSpecializationRule,
)
from pattern_detector.domain.rules.creational_rules import (
    AbstractFactoryTraitRule,
    BuilderFluentStructRule,
    FactoryMethodConstructorRule,
    PrototypeCloneCopyRule,
    SingletonGlobalInstanceRule,
)
from pattern_detector.domain.rules.idiomatic_rules import (
    DestructRaiiLifecycleRule,
    ExplicitOwnershipBorrowRule,
    RegisterPassableLayoutRule,
    StructValueSemanticsRule,
    TraitContractInterfaceRule,
    TransferMoveOperatorRule,
)
from pattern_detector.domain.rules.resilience_hazards_rules import (
    AccidentalCopyOverheadRule,
    DanglingTransferLifetimeRule,
    DynamicDefInHotPathRule,
    ScalarComputeLoopRule,
    UncheckedUnsafePointerRule,
)
from pattern_detector.domain.rules.simd_hardware_rules import (
    ParallelizeMultiCoreRule,
    SimdVectorizationKernelRule,
    TensorTilingKernelRule,
    UnsafeRawPointerBufferRule,
)
from pattern_detector.domain.rules.solid_principles_rules import (
    DemeterLawTrainWreckRule,
    DryDuplicateLogicRule,
    FatTraitIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    ManualTypeSwitchOcpRule,
    MonolithicStructSrpRule,
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

DEFAULT_RULES: list[type[BaseRule]] = [
    # 1. Mojo Idiomatic & Ownership (6)
    StructValueSemanticsRule,
    TraitContractInterfaceRule,
    ExplicitOwnershipBorrowRule,
    TransferMoveOperatorRule,
    DestructRaiiLifecycleRule,
    RegisterPassableLayoutRule,

    # 2. SIMD & Hardware (4)
    SimdVectorizationKernelRule,
    ParallelizeMultiCoreRule,
    UnsafeRawPointerBufferRule,
    TensorTilingKernelRule,

    # 3. Comptime Metaprogramming (3)
    ComptimeParameterSpecializationRule,
    AliasTypeMetaprogrammingRule,
    CompileTimeBranchSpecializationRule,

    # 4. Creational GoF (5/5)
    SingletonGlobalInstanceRule,
    FactoryMethodConstructorRule,
    AbstractFactoryTraitRule,
    BuilderFluentStructRule,
    PrototypeCloneCopyRule,

    # 5. Structural GoF (7/7)
    AdapterStructWrapperRule,
    BridgeHardwareDriverRule,
    CompositeTreeHierarchyRule,
    DecoratorForwardingWrapperRule,
    FacadeUnifiedApiRule,
    FlyweightSharedPoolRule,
    ProxyLazyResourceRule,

    # 6. Behavioral GoF (11/11)
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

    # 7. Hazards & Safety (5)
    UncheckedUnsafePointerRule,
    DynamicDefInHotPathRule,
    AccidentalCopyOverheadRule,
    ScalarComputeLoopRule,
    DanglingTransferLifetimeRule,

    # 8. SOLID & Clean Code (7)
    MonolithicStructSrpRule,
    FatTraitIspRule,
    ManualTypeSwitchOcpRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    DryDuplicateLogicRule,
    DemeterLawTrainWreckRule,
]


def get_default_rules() -> list[BaseRule]:
    """Instantiate and return full suite of default Mojo rules."""
    from pattern_detector.domain.rules.structural_rules import (
        AdapterStructWrapperRule,
        BridgeHardwareDriverRule,
        CompositeTreeHierarchyRule,
        DecoratorForwardingWrapperRule,
        FacadeUnifiedApiRule,
        FlyweightSharedPoolRule,
        ProxyLazyResourceRule,
    )

    return [
        # 1. Idiomatic & Ownership
        StructValueSemanticsRule(),
        TraitContractInterfaceRule(),
        ExplicitOwnershipBorrowRule(),
        TransferMoveOperatorRule(),
        DestructRaiiLifecycleRule(),
        RegisterPassableLayoutRule(),

        # 2. SIMD & Hardware
        SimdVectorizationKernelRule(),
        ParallelizeMultiCoreRule(),
        UnsafeRawPointerBufferRule(),
        TensorTilingKernelRule(),

        # 3. Comptime Metaprogramming
        ComptimeParameterSpecializationRule(),
        AliasTypeMetaprogrammingRule(),
        CompileTimeBranchSpecializationRule(),

        # 4. Creational (5/5)
        SingletonGlobalInstanceRule(),
        FactoryMethodConstructorRule(),
        AbstractFactoryTraitRule(),
        BuilderFluentStructRule(),
        PrototypeCloneCopyRule(),

        # 5. Structural (7/7)
        AdapterStructWrapperRule(),
        BridgeHardwareDriverRule(),
        CompositeTreeHierarchyRule(),
        DecoratorForwardingWrapperRule(),
        FacadeUnifiedApiRule(),
        FlyweightSharedPoolRule(),
        ProxyLazyResourceRule(),

        # 6. Behavioral (11/11)
        ChainOfResponsibilityChainRule(),
        CommandCallableTaskRule(),
        InterpreterAstEvalRule(),
        IteratorTraitProtocolRule(),
        MediatorCoordinatorRule(),
        MementoSnapshotStateRule(),
        ObserverDispatchRegistryRule(),
        StateTraitFsmRule(),
        StrategyTraitInjectionRule(),
        TemplateMethodSkeletonRule(),
        VisitorDoubleDispatchRule(),

        # 7. Hazards & Safety
        UncheckedUnsafePointerRule(),
        DynamicDefInHotPathRule(),
        AccidentalCopyOverheadRule(),
        ScalarComputeLoopRule(),
        DanglingTransferLifetimeRule(),

        # 8. SOLID & Clean Code
        MonolithicStructSrpRule(),
        FatTraitIspRule(),
        ManualTypeSwitchOcpRule(),
        KissCyclomaticComplexityRule(),
        KissLongParameterListRule(),
        DryDuplicateLogicRule(),
        DemeterLawTrainWreckRule(),
    ]
