# 🔥 DPX-Mojo: SIMD Vectorization, Ownership, Memory Safety, GoF 23 & AI Hardware Acceleration Architectural Pattern Detector

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Mojo Version](https://img.shields.io/badge/Mojo-24.x%20--%2025.x+-FF4500?logo=mojo&logoColor=white)](https://modular.com/mojo)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Architecture: Hexagonal DDD](https://img.shields.io/badge/Architecture-Hexagonal%20DDD-blueviolet)](https://alistair.cockburn.us/hexagonal-architecture/)
[![CLI: Typer & Rich](https://img.shields.io/badge/CLI-Typer%20%26%20Rich-009688)](https://typer.tiangolo.com)
[![SARIF OASIS v2.1.0](https://img.shields.io/badge/SARIF-OASIS%20v2.1.0-blue)](https://sarifweb.azurewebsites.net)

**DPX-Mojo** is an enterprise-grade static analysis engine and architectural pattern detector for Mojo codebases. Designed for **AI Hardware Acceleration, Machine Learning Kernels (MAX / Modular), GPU/CPU Computing, High-Performance Systems, and Vectorized Algorithms**, it analyzes **SIMD Vectorization, Ownership & Borrowing Conventions (`borrowed`, `inout`, `owned`, `^`), Value Semantics (`@value`, `@register_passable`), Traits, Compile-Time Metaprogramming (`alias`, `@parameter if`), all 23 GoF Design Patterns**, and **Mojo Memory Safety Hazards (Unchecked `UnsafePointer`, Dynamic `def` in compute loops, Accidental copy overheads, Dangling transfer lifetimes)**.

[Features](#-key-features) • [Installation](#-installation) • [CLI Usage](#-cli-usage) • [Supported Rules](#-supported-pattern-rules--checks) • [The DPX Suite Family](#-the-dpx-suite-family)

</div>

---

## 🌟 Key Features

- ⚡ **SIMD Vectorization & AI Hardware:** Audits multi-element hardware vector registers (`SIMD[type, width]`, `vectorize`), multi-core execution (`parallelize`), raw memory buffers (`UnsafePointer`, `DTypePointer`), and cache-blocked 2D/3D tensor tiling kernels.
- 🛡️ **Ownership & Value Semantics:** Inspects explicit argument conventions (`borrowed`, `inout`, `owned`), transfer move operator (`^`), `@value` synthesized lifecycle, `@register_passable` register layouts, and RAII destructors (`__del__`).
- 🧩 **Compile-Time Metaprogramming:** Analyzes compile-time parameter specialization (`[type: DType, width: Int]`), compile-time `alias` bindings, and `@parameter if` dead-code elimination.
- 🏛️ **100% Complete Gang of Four (GoF 23/23):** Comprehensive detection of all 23 classic Creational, Structural, and Behavioral patterns adapted for Mojo's struct/trait value-ownership paradigm.
- 🚨 **Safety, Performance & Resilience Hazard Detection:** Identifies unchecked raw `UnsafePointer` dereferences, dynamic Python-mode `def` in compute-heavy loops, accidental memory copies of large buffers, scalar compute loops missing SIMD, and dangling variables after `^` transfers.
- 📊 **Interactive Architecture Observability HUD:** Zero-dependency interactive HTML dashboard with instant search, KPI breakdown, and built-in **`🤖 Copy AI Context Prompt`** generator for LLMs (Claude, GPT-4, Gemini).
- 🔒 **CI/CD & GitHub Security Ready:** Standardized **OASIS SARIF v2.1.0**, JSON, and Markdown reports.

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/bivex/DPX-Mojo.git
cd DPX-Mojo

# Install dependencies using uv or pip
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

---

## 💻 CLI Usage

### 1. Scan a Mojo Project or ML Kernel Package
```bash
# Terminal scan with Rich formatting
dpx-mojo scan /path/to/mojo/project

# Scan Mojo files (.mojo and .🔥)
dpx-mojo scan src/ -H reports/mojo_hud.html

# Generate AI Context Prompt for LLMs
dpx-mojo scan src/ --llm

# Filter for specific SIMD or Ownership rules
dpx-mojo scan src/ -p simd_vectorization_kernel -p explicit_ownership_borrow

# Export SARIF for GitHub Code Scanning
dpx-mojo scan src/ -S reports/results.sarif
```

### 2. Inspect Supported Architectural Rules
```bash
dpx-mojo rules
```

### 3. Query Deep Pattern Documentation
```bash
dpx-mojo info simd_vectorization_kernel
dpx-mojo info explicit_ownership_borrow
```

---

## 📋 Supported Pattern Rules & Checks

### 1. ⚡ Mojo Idiomatic & Ownership
- `struct_value_semantics`: Value-semantic struct with `@value` or copy/move lifecycle hooks.
- `trait_contract_interface`: Static compile-time polymorphic trait contract (`trait ...:`).
- `explicit_ownership_borrow`: Argument ownership conventions (`borrowed`, `inout`, `owned`).
- `transfer_move_operator`: Move ownership transfer operator (`^`) without deep cloning.
- `destruct_raii_lifecycle`: Deterministic resource cleanup via `__del__` destructor.
- `register_passable_layout`: Struct decorated with `@register_passable` for direct register passing.

### 2. 🚀 SIMD & Hardware Acceleration
- `simd_vectorization_kernel`: Hardware vector register operations (`SIMD[DType, width]`, `vectorize`).
- `parallelize_multi_core`: Multi-core thread distribution using `parallelize`.
- `unsafe_raw_pointer_buffer`: Direct memory buffer manipulation via `UnsafePointer` / `DTypePointer`.
- `tensor_tiling_kernel`: Cache-blocked matrix multiplication tiling for L1/L2 cache locality.

### 3. 🧩 Compile-Time Metaprogramming
- `comptime_parameter_specialization`: Compile-time parameters (`[type: DType, width: Int]`).
- `alias_type_metaprogramming`: Compile-time `alias` type and shape bindings.
- `compile_time_branch_specialization`: Compile-time dead-code elimination via `@parameter if`.

### 4. 🏛️ GoF Creational Patterns (5/5)
- `singleton_global_instance`: Static global coordinator or zero-field singleton struct.
- `factory_method_constructor`: Static constructor or factory function instantiating specialized types.
- `abstract_factory_trait`: Trait defining contracts for component families.
- `builder_fluent_struct`: Struct accumulating configuration options before final instantiation.
- `prototype_clone_copy`: Object duplication via `__copyinit__` or explicit `clone()` methods.

### 5. 🧱 GoF Structural Patterns (7/7)
- `adapter_struct_wrapper`: Struct adapting external or foreign types to domain traits.
- `bridge_hardware_driver`: Decoupling compute abstraction from hardware implementor drivers.
- `composite_tree_hierarchy`: Recursive tree node collections for syntax and compute graphs.
- `decorator_forwarding_wrapper`: Struct wrapping an underlying instance to layer functionality.
- `facade_unified_api`: Unified top-level API struct coordinating multiple subsystems.
- `flyweight_shared_pool`: Sharing immutable instances via pool or dictionary cache.
- `proxy_lazy_resource`: Surrogate controlling access or delaying allocation of heavy GPU buffers.

### 6. 🎯 GoF Behavioral Patterns (11/11)
- `chain_of_responsibility_chain`: Middleware/handler structs delegating requests along a pipeline.
- `command_callable_task`: Command objects encapsulating actions and execution parameters.
- `interpreter_ast_eval`: Domain expression AST evaluator executing custom mathematical grammar.
- `iterator_trait_protocol`: Collection traversal protocol implementing `__iter__` and `__next__`.
- `mediator_coordinator`: Central coordinator mediating interaction between independent subsystems.
- `memento_snapshot_state`: State snapshot struct capturing internal state for checkpoint restoration.
- `observer_dispatch_registry`: Event broadcasting to subscribed listeners or callbacks.
- `state_trait_fsm`: Finite state machine dispatching over a common state trait.
- `strategy_trait_injection`: Interchangeable algorithm strategy injected via trait bounds.
- `template_method_skeleton`: Algorithm skeleton coordinating customizable step hooks.
- `visitor_double_dispatch`: Double-dispatch operations traversing heterogeneous node hierarchies.

### 7. 🛡️ Safety, Performance & Resilience Hazards
- `unchecked_unsafe_pointer`: Raw pointer arithmetic/loads without bounds assertions.
- `dynamic_def_in_hot_path`: Python-style dynamic `def` inside compute-heavy loops instead of `fn`.
- `accidental_copy_overhead`: Large struct passed by value without `borrowed` or `inout`.
- `scalar_compute_loop`: Element-by-element loop in numerical algorithm missing SIMD vectorization.
- `dangling_transfer_lifetime`: Variable referenced after ownership was moved (`^`).

### 8. 📐 SOLID & Clean Code Principles
- `monolithic_struct_srp`: Struct declaring too many fields, violating SRP.
- `fat_trait_isp`: Trait requiring too many method implementations, violating ISP.
- `manual_type_switch_ocp`: Manual `if type == ...` branching instead of Trait polymorphism.
- `kiss_cyclomatic_complexity`: High cyclomatic complexity (> 8 branch points).
- `kiss_long_parameter_list`: Functions with excessive parameters (>= 6).
- `dry_duplicate_logic`: Duplicated algorithmic sequences across functions.
- `demeter_law_train_wreck`: Law of Demeter deep field access chains (`a.b.c.d.e`).

---

## 🌐 The DPX Suite Family

Cross-language architectural static analysis across all modern programming languages:

| Repository | Language / Ecosystem | Primary Paradigms & Focus |
|---|---|---|
| **[`DPX-Huff`](https://github.com/bivex/DPX-Huff)** | **Huff / EVM Stack Assembly** (0.3.x+ / Cancun) | **Macros, Stack Layout, Jumpdest Labels, Selector Dispatchers, GoF 23** |
| **[`DPX-Yul`](https://github.com/bivex/DPX-Yul)** | **Yul / EVM Assembly** (0.8.x - 0.8.28+ / Cancun) | **Memory Management, Storage Packing, Transient Storage (EIP-1153), GoF 23** |
| **[`DPX-Cairo`](https://github.com/bivex/DPX-Cairo)** | **Cairo** (Cairo 1.0 - 2.8+ / Starknet) | **Components, Storage Mapping, Syscalls, Account Abstraction, Upgrades, GoF 23** |
| **[`DPX-Move`](https://github.com/bivex/DPX-Move)** | **Move** (Move 2024 / Aptos / Sui) | **Linear Resources, Abilities, Sui Objects, Hot Potato, Prover, GoF 23** |
| **[`DPX-Lua`](https://github.com/bivex/DPX-Lua)** | **Lua / Luau** (5.1 - 5.4 / LuaJIT) | **Metatable OOP, Coroutines, LuaJIT FFI, GameDev (Roblox/Neovim), GoF 23** |
| **[`DPX-Solidity`](https://github.com/bivex/DPX-Solidity)** | **Solidity** (0.8.x - 0.8.28+) | **EVM Gas Optimization, Proxies, CEI Reentrancy, Yul, GoF 23, Security** |
| **[`DPX-Zig`](https://github.com/bivex/DPX-Zig)** | **Zig** (0.11 - 0.14+) | **Comptime Generics, Allocator RAII, Defer Cleanup, SIMD, GoF 23** |
| **[`DPX-Gleam`](https://github.com/bivex/DPX-Gleam)** | **Gleam** (1.0 - 1.8+) | **Type-Safe OTP Actors, Algebraic Data Types, Railway Monads, GoF 23** |
| **[`DPX-Mojo`](https://github.com/bivex/DPX-Mojo)** | **Mojo** (24.x - 25.x+) | **SIMD Vectorization, Ownership, Memory Safety, GoF 23, AI Acceleration** |
| **[`DPX-Julia`](https://github.com/bivex/DPX-Julia)** | **Julia** (1.6 - 1.11+) | **Multiple Dispatch, Holy Traits, Metaprogramming, Tasks, GoF 23** |
| **[`DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin)** | **Kotlin** (1.8 - 2.0+) | **Coroutines, Flow, Jetpack Compose, Multiplatform, GoF 23** |
| **[`DPX-Swift`](https://github.com/bivex/DPX-Swift)** | **Swift** (5.5 - 6.0+) | **Protocol-Oriented, Actor Concurrency, SwiftUI, ARC Safety** |
| **[`DPX-CSharp`](https://github.com/bivex/DPX-CSharp)** | **C#** (10 - 13 / .NET 8-9) | **Clean Architecture, CQRS MediatR, Channel Pipelines** |
| **[`DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript)** | **TypeScript / JavaScript** | **Hexagonal DI, Decorator Meta, Reactive Streams, React/NestJS** |
| **[`DPX-Rust`](https://github.com/bivex/DPX-Rust)** | **Rust** (Edition 2021/2024) | **Zero-Cost Abstractions, RAII Lifetimes, Typestate Pattern** |
| **[`DPX-Go`](https://github.com/bivex/DPX-Go)** | **Go** (1.18 - 1.24+) | **Goroutine Channels, CSP Concurrency, Pipeline Streaming** |
| **[`DPX-Py`](https://github.com/bivex/DPX-Py)** | **Python** (3.8 - 3.13+) | **Multi-Paradigm Hexagonal, Data Flow Engine, AsyncIO** |
| **[`DPX-Php`](https://github.com/bivex/DPX-Php)** | **PHP** (8.1 - 8.4+) | **Attribute-driven DDD, Fiber Concurrency, Laravel/Symfony** |
| **[`DPX-Haskell`](https://github.com/bivex/DPX-Haskell)** | **Haskell** (GHC 9.2 - 9.12+) | **Category Theory, Monad Transformers, Free Monads, Optics** |
| **[`DPX-OCaml`](https://github.com/bivex/DPX-OCaml)** | **OCaml** (4.14 - 5.3+ Multicore) | **Functor Modules, Effect Handlers, GADTs, Railway Monads** |
| **[`DPX-Elixir`](https://github.com/bivex/DPX-Elixir)** | **Elixir** (OTP 25 - 27+) | **GenServer, DynamicSupervisor, Actor Fault Tolerance** |
| **[`DPX-Erlang`](https://github.com/bivex/DPX-Erlang)** | **Erlang/OTP** (24 - 27+) | **OTP Behaviors, Supervision Trees, Message Passing** |
| **[`DPX-C`](https://github.com/bivex/DPX-C)** | **C** (C99 - C23) | **Opaque Structs, VTables, MISRA/CERT Safety, Arena Allocators** |
| **[`DPX-Cpp`](https://github.com/bivex/DPX-Cpp)** | **C++** (C++14 - C++20) | **CRTP, Policy-Based Design, RAII Memory Safety, ANTLR4 AST** |
| **[`DPX-Java`](https://github.com/bivex/DPX-Java)** | **Java** (17 - 23+) | **Virtual Threads, Spring Boot / Jakarta EE, GoF Patterns** |
| **[`DPX`](https://github.com/bivex/DPX)** | **Clojure** / Meta Engine | **Pure Functional, Multimethods, Homoiconic Macro Architecture** |
---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
