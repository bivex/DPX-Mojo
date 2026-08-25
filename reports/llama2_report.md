# 🔥 DPX-Mojo: Architectural Context & Pattern Report

- **Target Project:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo`
- **Scanned Files:** 6
- **Total Detections:** 58
- **Scan Time:** 0.010s

## 📊 Summary by Category

| Category | Detections |
|---|:---:|
| `mojo_idiomatic` | 27 |
| `principle` | 11 |
| `resilience` | 8 |
| `simd_hardware_acceleration` | 7 |
| `creational` | 2 |
| `structural` | 2 |
| `comptime_metaprogramming` | 1 |

## 🔍 Detailed Pattern Instances & Violations

### 1. explicit_ownership_borrow on `str_concat` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:150:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'str_concat' enforces explicit memory conventions (a: borrowed, b: borrowed)

### 2. explicit_ownership_borrow on `string_compare` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:153:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'string_compare' enforces explicit memory conventions (a: borrowed, b: borrowed)

### 3. explicit_ownership_borrow on `softmax` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:386:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'softmax' enforces explicit memory conventions (mut x: borrowed, size: borrowed)

### 4. explicit_ownership_borrow on `softmax` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:390:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'softmax' enforces explicit memory conventions (mut x: borrowed, start: borrowed, end: borrowed)

### 5. explicit_ownership_borrow on `matmul` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:459:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'matmul' enforces explicit memory conventions (C: borrowed, A: borrowed, B: borrowed)

### 6. explicit_ownership_borrow on `add` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:470:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'add' enforces explicit memory conventions (dest: borrowed, src: borrowed, size: borrowed)

### 7. explicit_ownership_borrow on `argmax` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:664:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'argmax' enforces explicit memory conventions (v: borrowed, size: borrowed)

### 8. explicit_ownership_borrow on `sample` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:673:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'sample' enforces explicit memory conventions (probabilities: borrowed, size: borrowed)

### 9. explicit_ownership_borrow on `bpe_encode` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:682:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'bpe_encode' enforces explicit memory conventions (mut tokens: borrowed, text: borrowed, tok: borrowed)

### 10. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:25:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, *dims: borrowed)

### 11. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:34:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, ptr: borrowed, *dims: borrowed)

### 12. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:42:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, ptr: borrowed)

### 13. explicit_ownership_borrow on `__getitem__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:78:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__getitem__' enforces explicit memory conventions (y: borrowed, x: borrowed)

### 14. explicit_ownership_borrow on `__getitem__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:83:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__getitem__' enforces explicit memory conventions (z: borrowed, y: borrowed, x: borrowed)

### 15. explicit_ownership_borrow on `__setitem__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:90:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__setitem__' enforces explicit memory conventions (x: borrowed, val: borrowed)

### 16. explicit_ownership_borrow on `__setitem__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:94:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__setitem__' enforces explicit memory conventions (y: borrowed, x: borrowed, val: borrowed)

### 17. explicit_ownership_borrow on `slice` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:118:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function 'slice' enforces explicit memory conventions (idx1: borrowed, idx2: borrowed)

### 18. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:173:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, vocab_size: borrowed, filename: borrowed)

### 19. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:231:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, filename: borrowed, print_config: borrowed)

### 20. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:270:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, config: borrowed)

### 21. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:300:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, file_name: borrowed, config: borrowed)

### 22. explicit_ownership_borrow on `__init__` (90% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:480:1`
- **Summary:** Explicit function argument conventions ('borrowed', 'inout', 'owned') preventing memory copies.
- **Evidence Trail:**
  - `+90%` (MOJO_EXPLICIT_OWNERSHIP): Function '__init__' enforces explicit memory conventions (out self: borrowed, workers: borrowed)

### 23. transfer_move_operator on `bpe_encode` (92% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:682:1`
- **Summary:** Explicit ownership transfer utilizing the '^' move operator without deep cloning.
- **Evidence Trail:**
  - `+92%` (MOJO_TRANSFER_MOVE_OPERATOR): Function 'bpe_encode' uses '^' transfer operator to move ownership without memory copying

### 24. transfer_move_operator on `test_string_from_bytes` (92% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-llama2.mojo:145:1`
- **Summary:** Explicit ownership transfer utilizing the '^' move operator without deep cloning.
- **Evidence Trail:**
  - `+92%` (MOJO_TRANSFER_MOVE_OPERATOR): Function 'test_string_from_bytes' uses '^' transfer operator to move ownership without memory copying

### 25. transfer_move_operator on `test_matrix_slice` (92% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-llama2.mojo:365:1`
- **Summary:** Explicit ownership transfer utilizing the '^' move operator without deep cloning.
- **Evidence Trail:**
  - `+92%` (MOJO_TRANSFER_MOVE_OPERATOR): Function 'test_matrix_slice' uses '^' transfer operator to move ownership without memory copying

### 26. transfer_move_operator on `__init__` (92% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:42:1`
- **Summary:** Explicit ownership transfer utilizing the '^' move operator without deep cloning.
- **Evidence Trail:**
  - `+92%` (MOJO_TRANSFER_MOVE_OPERATOR): Function '__init__' uses '^' transfer operator to move ownership without memory copying

### 27. transfer_move_operator on `read_weights` (92% [VERY_HIGH])
- **Category:** `mojo_idiomatic`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:308:1`
- **Summary:** Explicit ownership transfer utilizing the '^' move operator without deep cloning.
- **Evidence Trail:**
  - `+92%` (MOJO_TRANSFER_MOVE_OPERATOR): Function 'read_weights' uses '^' transfer operator to move ownership without memory copying

### 28. simd_vectorization_kernel on `softmax` (95% [VERY_HIGH])
- **Category:** `simd_hardware_acceleration`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:390:1`
- **Summary:** SIMD hardware vector registers (AVX-512, ARM Neon) performing multi-element parallel operations.
- **Evidence Trail:**
  - `+95%` (HARDWARE_SIMD_VECTORIZATION): Function 'softmax' executes SIMD vector operations across hardware vector registers

### 29. simd_vectorization_kernel on `compute_row` (95% [VERY_HIGH])
- **Category:** `simd_hardware_acceleration`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:432:1`
- **Summary:** SIMD hardware vector registers (AVX-512, ARM Neon) performing multi-element parallel operations.
- **Evidence Trail:**
  - `+95%` (HARDWARE_SIMD_VECTORIZATION): Function 'compute_row' executes SIMD vector operations across hardware vector registers

### 30. simd_vectorization_kernel on `add` (95% [VERY_HIGH])
- **Category:** `simd_hardware_acceleration`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:470:1`
- **Summary:** SIMD hardware vector registers (AVX-512, ARM Neon) performing multi-element parallel operations.
- **Evidence Trail:**
  - `+95%` (HARDWARE_SIMD_VECTORIZATION): Function 'add' executes SIMD vector operations across hardware vector registers

### 31. simd_vectorization_kernel on `read_bytes_as` (95% [VERY_HIGH])
- **Category:** `simd_hardware_acceleration`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:177:1`
- **Summary:** SIMD hardware vector registers (AVX-512, ARM Neon) performing multi-element parallel operations.
- **Evidence Trail:**
  - `+95%` (HARDWARE_SIMD_VECTORIZATION): Function 'read_bytes_as' executes SIMD vector operations across hardware vector registers

### 32. simd_vectorization_kernel on `loop_over_heads` (95% [VERY_HIGH])
- **Category:** `simd_hardware_acceleration`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:590:1`
- **Summary:** SIMD hardware vector registers (AVX-512, ARM Neon) performing multi-element parallel operations.
- **Evidence Trail:**
  - `+95%` (HARDWARE_SIMD_VECTORIZATION): Function 'loop_over_heads' executes SIMD vector operations across hardware vector registers

### 33. parallelize_multi_core on `head_loop` (95% [VERY_HIGH])
- **Category:** `simd_hardware_acceleration`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:494:1`
- **Summary:** Multi-core task distribution using 'parallelize' and thread pools.
- **Evidence Trail:**
  - `+95%` (HARDWARE_PARALLELIZE_MULTI_CORE): Function 'head_loop' distributes compute tasks across CPU cores via parallelize

### 34. parallelize_multi_core on `loop_over_heads` (95% [VERY_HIGH])
- **Category:** `simd_hardware_acceleration`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:590:1`
- **Summary:** Multi-core task distribution using 'parallelize' and thread pools.
- **Evidence Trail:**
  - `+95%` (HARDWARE_PARALLELIZE_MULTI_CORE): Function 'loop_over_heads' distributes compute tasks across CPU cores via parallelize

### 35. comptime_parameter_specialization on `read_bytes_as` (95% [VERY_HIGH])
- **Category:** `comptime_metaprogramming`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:177:1`
- **Summary:** Compile-time parameters ('[type: DType, width: Int]') generating specialized machine code.
- **Evidence Trail:**
  - `+95%` (COMPTIME_FN_PARAMETERS): Function 'read_bytes_as[dtype: DType]' parameterizes compile-time hardware types

### 36. singleton_global_instance on `Config` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:218:1`
- **Summary:** Unique global instance or static coordinator struct.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_SINGLETON_STRUCT): Struct 'Config' serves as a unique Singleton instance

### 37. singleton_global_instance on `RunState` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:258:1`
- **Summary:** Unique global instance or static coordinator struct.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_SINGLETON_STRUCT): Struct 'RunState' serves as a unique Singleton instance

### 38. facade_unified_api on `Matrix` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:20:1`
- **Summary:** Unified top-level API struct coordinating multiple subsystem components.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_API): Struct 'Matrix' acts as unified Facade API coordinating multiple subsystem components

### 39. facade_unified_api on `Tokenizer` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:166:1`
- **Summary:** Unified top-level API struct coordinating multiple subsystem components.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_API): Struct 'Tokenizer' acts as unified Facade API coordinating multiple subsystem components

### 40. scalar_compute_loop on `test_matmul_all_ones` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:53:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_matmul_all_ones' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 41. scalar_compute_loop on `test_matmul_larger` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:82:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_matmul_larger' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 42. scalar_compute_loop on `test_matmul_zero` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:116:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_matmul_zero' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 43. scalar_compute_loop on `test_batch_matmul_single` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:145:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_batch_matmul_single' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 44. scalar_compute_loop on `test_batch_matmul_two` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:177:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_batch_matmul_two' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 45. scalar_compute_loop on `test_batch_matmul_three` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:223:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_batch_matmul_three' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 46. scalar_compute_loop on `test_matmul_dimension_validation` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:279:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_matmul_dimension_validation' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 47. scalar_compute_loop on `test_batch_matmul_consistency` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-matmul.mojo:312:1`
- **Summary:** Element-by-element scalar loop in numerical algorithm instead of SIMD vectorization.
- **Evidence Trail:**
  - `+88%` (HAZARD_SCALAR_COMPUTE_LOOP): Compute kernel 'test_batch_matmul_consistency' executes scalar loop without SIMD vectorization; refactor with 'vectorize' or SIMD registers

### 48. monolithic_struct_srp on `Matrix` (82% [HIGH])
- **Category:** `principle`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:20:1`
- **Summary:** Struct declaring excessive fields or methods, violating SRP.
- **Evidence Trail:**
  - `+82%` (SRP_MONOLITHIC_STRUCT): Struct 'Matrix' is a Monolithic Struct declaring 3 fields; consider decomposing into cohesive sub-structs

### 49. monolithic_struct_srp on `Config` (82% [HIGH])
- **Category:** `principle`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:218:1`
- **Summary:** Struct declaring excessive fields or methods, violating SRP.
- **Evidence Trail:**
  - `+82%` (SRP_MONOLITHIC_STRUCT): Struct 'Config' is a Monolithic Struct declaring 11 fields; consider decomposing into cohesive sub-structs

### 50. monolithic_struct_srp on `TransformerWeights` (90% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:284:1`
- **Summary:** Struct declaring excessive fields or methods, violating SRP.
- **Evidence Trail:**
  - `+90%` (SRP_MONOLITHIC_STRUCT): Struct 'TransformerWeights' is a Monolithic Struct declaring 14 fields; consider decomposing into cohesive sub-structs

### 51. monolithic_struct_srp on `Transformer` (82% [HIGH])
- **Category:** `principle`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:477:1`
- **Summary:** Struct declaring excessive fields or methods, violating SRP.
- **Evidence Trail:**
  - `+82%` (SRP_MONOLITHIC_STRUCT): Struct 'Transformer' is a Monolithic Struct declaring 1 fields; consider decomposing into cohesive sub-structs

### 52. kiss_cyclomatic_complexity on `bpe_encode` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:682:1`
- **Summary:** Function containing excessive decision branch points (> 8).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function 'bpe_encode' has high cyclomatic complexity (10 branch points), violating KISS

### 53. kiss_cyclomatic_complexity on `get_token_str` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:715:1`
- **Summary:** Function containing excessive decision branch points (> 8).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function 'get_token_str' has high cyclomatic complexity (11 branch points), violating KISS

### 54. kiss_cyclomatic_complexity on `argparse` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:766:1`
- **Summary:** Function containing excessive decision branch points (> 8).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function 'argparse' has high cyclomatic complexity (13 branch points), violating KISS

### 55. kiss_cyclomatic_complexity on `test_rope_rotation` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/tests/test-transformer.mojo:27:1`
- **Summary:** Function containing excessive decision branch points (> 8).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function 'test_rope_rotation' has high cyclomatic complexity (12 branch points), violating KISS

### 56. kiss_long_parameter_list on `matmul` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `fn`
- **Location:** `/Volumes/External/Code/DPX-Mojo/benchmarks/llama2.mojo/llama2.mojo:459:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'matmul' accepts 6 parameters; consider bundling into a configuration struct

### 57. dry_duplicate_logic on `file_exists` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `fn`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 2 function(s): file_exists, file_exists

### 58. dry_duplicate_logic on `resolve_model_path` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `fn`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 2 function(s): resolve_model_path, resolve_model_path
