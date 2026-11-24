# v16.0.0 → v16.0.1 · 要調査の変更候補 (32)

[一覧の目次](README.md)

<a id="compare-4ddcf64b2b44e7ca7de44aff51dd0a7a"></a>

### [`0093eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eca4.md) → [`0093ee40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md) FUN_0093ee40

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 2件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`00ab4d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab4/00ab4d00.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093ecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eca4.md#insn-0093ecc8) · [`0093ed10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eca4.md#insn-0093ed10) · [`0093ed30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eca4.md#insn-0093ed30)
- 新版 [`0093ee64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md#insn-0093ee64) · [`0093eeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md#insn-0093eeac) · [`0093eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md#insn-0093eecc)

~~~diff
- 0093ecc8 ["INT_ADD", "register:40f0:8", ["const:93ecc8:8", "const:4:8"]]
- 0093ecc8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0093ee64 ["INT_ADD", "register:40f0:8", ["const:93ee64:8", "const:4:8"]]
+ 0093ee64 ["CALL", null, ["callee:00c57fe0:8"]]
- 0093ecc8 bytes c6630c94
+ 0093ee64 bytes 5f640c94
- 0093ed10 ["INT_ADD", "register:40f0:8", ["const:93ed10:8", "const:4:8"]]
- 0093ed10 ["CALL", null, ["callee:00c57e90:8"]]
+ 0093eeac ["INT_ADD", "register:40f0:8", ["const:93eeac:8", "const:4:8"]]
+ 0093eeac ["CALL", null, ["callee:00c57e90:8"]]
- 0093ed10 bytes 60630c94
+ 0093eeac bytes f9630c94
- 0093ed30 ["INT_ADD", "register:40f0:8", ["const:93ed30:8", "const:4:8"]]
- 0093ed30 ["CALL", null, ["callee:00c57f40:8"]]
+ 0093eecc ["INT_ADD", "register:40f0:8", ["const:93eecc:8", "const:4:8"]]
+ 0093eecc ["CALL", null, ["callee:00c57f40:8"]]
- 0093ed30 bytes 84630c94
+ 0093eecc bytes 1d640c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99510371c1a4e7d90614efc890fb9611"></a>

### [`0093ed98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md) → [`0093ef34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md) FUN_0093ef34

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093ee10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md#insn-0093ee10) · [`0093ee20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md#insn-0093ee20) · [`0093ee34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md#insn-0093ee34)
- 新版 [`0093efac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md#insn-0093efac) · [`0093efbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md#insn-0093efbc) · [`0093efd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md#insn-0093efd0)

~~~diff
- 0093ee10 ["INT_ADD", "register:40f0:8", ["const:93ee10:8", "const:4:8"]]
- 0093ee10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093efac ["INT_ADD", "register:40f0:8", ["const:93efac:8", "const:4:8"]]
+ 0093efac ["CALL", null, ["callee:00c57eb0:8"]]
- 0093ee10 bytes 28630c94
+ 0093efac bytes c1630c94
- 0093ee20 ["INT_ADD", "register:40f0:8", ["const:93ee20:8", "const:4:8"]]
- 0093ee20 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093efbc ["INT_ADD", "register:40f0:8", ["const:93efbc:8", "const:4:8"]]
+ 0093efbc ["CALL", null, ["callee:00c57eb0:8"]]
- 0093ee20 bytes 24630c94
+ 0093efbc bytes bd630c94
- 0093ee34 ["INT_ADD", "register:40f0:8", ["const:93ee34:8", "const:4:8"]]
- 0093ee34 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093efd0 ["INT_ADD", "register:40f0:8", ["const:93efd0:8", "const:4:8"]]
+ 0093efd0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0093ee34 bytes 1f630c94
+ 0093efd0 bytes b8630c94
~~~


<a id="compare-3bbbdc6208d24de914b31ae24e0cb071"></a>

### [`0093ee80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ee80.md) → [`0093f01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f01c.md) FUN_0093f01c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093eec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ee80.md#insn-0093eec8)
- 新版 [`0093f064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f01c.md#insn-0093f064)

~~~diff
- 0093eec8 ["INT_ADD", "register:40f0:8", ["const:93eec8:8", "const:4:8"]]
- 0093eec8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093f064 ["INT_ADD", "register:40f0:8", ["const:93f064:8", "const:4:8"]]
+ 0093f064 ["CALL", null, ["callee:00c57eb0:8"]]
- 0093eec8 bytes fa620c94
+ 0093f064 bytes 93630c94
~~~


<a id="compare-6de30eb02cee472a6f35f659e7909e76"></a>

### [`0093eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eef8.md) → [`0093f094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md) FUN_0093f094

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093ef44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eef8.md#insn-0093ef44) · [`0093ef54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eef8.md#insn-0093ef54) · [`0093ef64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eef8.md#insn-0093ef64)
- 新版 [`0093f0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md#insn-0093f0e0) · [`0093f0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md#insn-0093f0f0) · [`0093f100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md#insn-0093f100)

~~~diff
- 0093ef44 ["INT_ADD", "register:40f0:8", ["const:93ef44:8", "const:4:8"]]
- 0093ef44 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093f0e0 ["INT_ADD", "register:40f0:8", ["const:93f0e0:8", "const:4:8"]]
+ 0093f0e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0093ef44 bytes db620c94
+ 0093f0e0 bytes 74630c94
- 0093ef54 ["INT_ADD", "register:40f0:8", ["const:93ef54:8", "const:4:8"]]
- 0093ef54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093f0f0 ["INT_ADD", "register:40f0:8", ["const:93f0f0:8", "const:4:8"]]
+ 0093f0f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0093ef54 bytes d7620c94
+ 0093f0f0 bytes 70630c94
- 0093ef64 ["INT_ADD", "register:40f0:8", ["const:93ef64:8", "const:4:8"]]
- 0093ef64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093f100 ["INT_ADD", "register:40f0:8", ["const:93f100:8", "const:4:8"]]
+ 0093f100 ["CALL", null, ["callee:00c57eb0:8"]]
- 0093ef64 bytes d3620c94
+ 0093f100 bytes 6c630c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9ebeb1e5ce4a66741f5373d265e7dbc"></a>

### [`0093f03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md) → [`0093f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md) FUN_0093f1d8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00938f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0093f214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f214.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009390b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00939/009390b4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0093f3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3b0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093f0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md#insn-0093f0dc) · [`0093f1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md#insn-0093f1c0) · [`0093f1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md#insn-0093f1d0)
- 新版 [`0093f278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md#insn-0093f278) · [`0093f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md#insn-0093f35c) · [`0093f36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md#insn-0093f36c)

~~~diff
- 0093f0dc ["INT_ADD", "register:40f0:8", ["const:93f0dc:8", "const:4:8"]]
- 0093f0dc ["CALL", null, ["callee:00c57e90:8"]]
+ 0093f278 ["INT_ADD", "register:40f0:8", ["const:93f278:8", "const:4:8"]]
+ 0093f278 ["CALL", null, ["callee:00c57e90:8"]]
- 0093f0dc bytes 6d620c94
+ 0093f278 bytes 06630c94
- 0093f1c0 ["INT_ADD", "register:40f0:8", ["const:93f1c0:8", "const:4:8"]]
- 0093f1c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093f35c ["INT_ADD", "register:40f0:8", ["const:93f35c:8", "const:4:8"]]
+ 0093f35c ["CALL", null, ["callee:00c57eb0:8"]]
- 0093f1c0 bytes 3c620c94
+ 0093f35c bytes d5620c94
- 0093f1d0 ["INT_ADD", "register:40f0:8", ["const:93f1d0:8", "const:4:8"]]
- 0093f1d0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0093f36c ["INT_ADD", "register:40f0:8", ["const:93f36c:8", "const:4:8"]]
+ 0093f36c ["CALL", null, ["callee:00c57eb0:8"]]
- 0093f1d0 bytes 38620c94
+ 0093f36c bytes d1620c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f4489ebaeb607947ac399295b7c50ad"></a>

### [`00943fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md) → [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md) FUN_00944178

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) [`009426f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md) [`009437fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00942570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md) [`00942df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00944014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md#insn-00944014) · [`00944054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md#insn-00944054) · [`00944084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md#insn-00944084)
- 新版 [`009441b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md#insn-009441b0) · [`009441f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md#insn-009441f0) · [`00944220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md#insn-00944220)

~~~diff
- 00944014 ["INT_ADD", "register:40f0:8", ["const:944014:8", "const:4:8"]]
- 00944014 ["CALL", null, ["callee:00942f94:8"]]
+ 009441b0 ["INT_ADD", "register:40f0:8", ["const:9441b0:8", "const:4:8"]]
+ 009441b0 ["CALL", null, ["callee:00942f94:8"]]
- 00944014 bytes 79fbff97
+ 009441b0 bytes 79fbff97
- 00944054 ["INT_ADD", "register:40f0:8", ["const:944054:8", "const:4:8"]]
- 00944054 ["CALL", null, ["callee:0043bb20:8"]]
+ 009441f0 ["INT_ADD", "register:40f0:8", ["const:9441f0:8", "const:4:8"]]
+ 009441f0 ["CALL", null, ["callee:0043bb20:8"]]
- 00944054 bytes a3deeb97
+ 009441f0 bytes 4cdeeb97
- 00944084 ["INT_ADD", "register:40f0:8", ["const:944084:8", "const:4:8"]]
- 00944084 ["CALL", null, ["callee:0043bb20:8"]]
+ 00944220 ["INT_ADD", "register:40f0:8", ["const:944220:8", "const:4:8"]]
+ 00944220 ["CALL", null, ["callee:0043bb20:8"]]
- 00944084 bytes 97deeb97
+ 00944220 bytes 40deeb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d200220cc064495dc3e7200fca2f536f"></a>

### [`0094453c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md) → [`009446d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md) FUN_009446d8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009445a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md#insn-009445a8) · [`009445b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md#insn-009445b8) · [`009445c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md#insn-009445c8)
- 新版 [`00944744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md#insn-00944744) · [`00944754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md#insn-00944754) · [`00944764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md#insn-00944764)

~~~diff
- 009445a8 ["INT_ADD", "register:40f0:8", ["const:9445a8:8", "const:4:8"]]
- 009445a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00944744 ["INT_ADD", "register:40f0:8", ["const:944744:8", "const:4:8"]]
+ 00944744 ["CALL", null, ["callee:00c57eb0:8"]]
- 009445a8 bytes 424d0c94
+ 00944744 bytes db4d0c94
- 009445b8 ["INT_ADD", "register:40f0:8", ["const:9445b8:8", "const:4:8"]]
- 009445b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00944754 ["INT_ADD", "register:40f0:8", ["const:944754:8", "const:4:8"]]
+ 00944754 ["CALL", null, ["callee:00c57eb0:8"]]
- 009445b8 bytes 3e4d0c94
+ 00944754 bytes d74d0c94
- 009445c8 ["INT_ADD", "register:40f0:8", ["const:9445c8:8", "const:4:8"]]
- 009445c8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00944764 ["INT_ADD", "register:40f0:8", ["const:944764:8", "const:4:8"]]
+ 00944764 ["CALL", null, ["callee:00c57eb0:8"]]
- 009445c8 bytes 3a4d0c94
+ 00944764 bytes d34d0c94
~~~


<a id="compare-b0c582c5c540d017f8ecc81d4cf24d05"></a>

### [`00944e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944e18.md) → [`00944fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md) FUN_00944fb4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00944ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944e18.md#insn-00944ef0) · [`00944f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944e18.md#insn-00944f08) · [`00944f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944e18.md#insn-00944f14)
- 新版 [`0094508c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md#insn-0094508c) · [`009450a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md#insn-009450a4) · [`009450b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md#insn-009450b0)

~~~diff
- 00944ef0 ["INT_ADD", "register:40f0:8", ["const:944ef0:8", "const:4:8"]]
- 00944ef0 ["CALL", null, ["callee:0046d5a8:8"]]
+ 0094508c ["INT_ADD", "register:40f0:8", ["const:94508c:8", "const:4:8"]]
+ 0094508c ["CALL", null, ["callee:0046d5a8:8"]]
- 00944ef0 bytes 9ea1ec97
+ 0094508c bytes 47a1ec97
- 00944f08 ["INT_ADD", "register:40f0:8", ["const:944f08:8", "const:4:8"]]
- 00944f08 ["CALL", null, ["callee:00c58430:8"]]
+ 009450a4 ["INT_ADD", "register:40f0:8", ["const:9450a4:8", "const:4:8"]]
+ 009450a4 ["CALL", null, ["callee:00c58430:8"]]
- 00944f08 bytes 4a4c0c94
+ 009450a4 bytes e34c0c94
- 00944f14 ["INT_ADD", "register:40f0:8", ["const:944f14:8", "const:4:8"]]
- 00944f14 ["CALL", null, ["callee:00c58430:8"]]
+ 009450b0 ["INT_ADD", "register:40f0:8", ["const:9450b0:8", "const:4:8"]]
+ 009450b0 ["CALL", null, ["callee:00c58430:8"]]
- 00944f14 bytes 474c0c94
+ 009450b0 bytes e04c0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2708037bc04fb556473946a24c12a73"></a>

### [`009450ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md) → [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) FUN_00945288

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`009450ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md) · 呼出先 7件 [`009450ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md) [`009460ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/009460ec.md) [`00946428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946428.md) [`00946780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md) [`00946ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md)
- 新版 呼出元 2件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) · 呼出先 7件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) [`009465c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/009465c4.md) [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009451c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md#insn-009451c4) · [`009451e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md#insn-009451e8) · [`009451f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md#insn-009451f8)
- 新版 [`00945360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md#insn-00945360) · [`00945384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md#insn-00945384) · [`00945394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md#insn-00945394)

~~~diff
- 009451c4 ["INT_ADD", "register:40f0:8", ["const:9451c4:8", "const:4:8"]]
- 009451c4 ["CALL", null, ["callee:009465c4:8"]]
+ 00945360 ["INT_ADD", "register:40f0:8", ["const:945360:8", "const:4:8"]]
+ 00945360 ["CALL", null, ["callee:009465c4:8"]]
- 009451c4 bytes 99040094
+ 00945360 bytes 99040094
- 009451e8 ["INT_ADD", "register:40f0:8", ["const:9451e8:8", "const:4:8"]]
- 009451e8 ["CALL", null, ["callee:009465c4:8"]]
+ 00945384 ["INT_ADD", "register:40f0:8", ["const:945384:8", "const:4:8"]]
+ 00945384 ["CALL", null, ["callee:009465c4:8"]]
- 009451e8 bytes 90040094
+ 00945384 bytes 90040094
- 009451f8 ["INT_ADD", "register:40f0:8", ["const:9451f8:8", "const:4:8"]]
- 009451f8 ["CALL", null, ["callee:009465c4:8"]]
+ 00945394 ["INT_ADD", "register:40f0:8", ["const:945394:8", "const:4:8"]]
+ 00945394 ["CALL", null, ["callee:009465c4:8"]]
- 009451f8 bytes 8c040094
+ 00945394 bytes 8c040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1943e2b0523401622ed8c13ac5a7649"></a>

### [`009460ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/009460ec.md) → [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) FUN_00946288

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009450ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md) [`00946780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md) · 呼出先 3件 [`00946ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) · 呼出先 3件 [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0094612c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/009460ec.md#insn-0094612c) · [`009461c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/009460ec.md#insn-009461c0) · [`00946270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/009460ec.md#insn-00946270)
- 新版 [`009462c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md#insn-009462c8) · [`0094635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md#insn-0094635c) · [`0094640c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md#insn-0094640c)

~~~diff
- 0094612c ["INT_ADD", "register:40f0:8", ["const:94612c:8", "const:4:8"]]
- 0094612c ["CALL", null, ["callee:00946c50:8"]]
+ 009462c8 ["INT_ADD", "register:40f0:8", ["const:9462c8:8", "const:4:8"]]
+ 009462c8 ["CALL", null, ["callee:00946c50:8"]]
- 0094612c bytes 62020094
+ 009462c8 bytes 62020094
- 009461c0 ["INT_ADD", "register:40f0:8", ["const:9461c0:8", "const:4:8"]]
- 009461c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0094635c ["INT_ADD", "register:40f0:8", ["const:94635c:8", "const:4:8"]]
+ 0094635c ["CALL", null, ["callee:00c57eb0:8"]]
- 009461c0 bytes 3c460c94
+ 0094635c bytes d5460c94
- 00946270 ["INT_ADD", "register:40f0:8", ["const:946270:8", "const:4:8"]]
- 00946270 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0094640c ["INT_ADD", "register:40f0:8", ["const:94640c:8", "const:4:8"]]
+ 0094640c ["CALL", null, ["callee:00c57eb0:8"]]
- 00946270 bytes 10460c94
+ 0094640c bytes a9460c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f40ea0406ba97522a3e0d8c7a4f459a"></a>

### [`00946ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md) → [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md) FUN_00946c50

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009450ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md) [`009460ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/009460ec.md) [`00946780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md) · 呼出先 3件 [`00946428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946428.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) · 呼出先 3件 [`009465c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/009465c4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00946af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md#insn-00946af0) · [`00946b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md#insn-00946b84) · [`00946c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md#insn-00946c38)
- 新版 [`00946c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md#insn-00946c8c) · [`00946d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md#insn-00946d20) · [`00946dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md#insn-00946dd4)

~~~diff
- 00946af0 ["INT_ADD", "register:40f0:8", ["const:946af0:8", "const:4:8"]]
- 00946af0 ["CALL", null, ["callee:009465c4:8"]]
+ 00946c8c ["INT_ADD", "register:40f0:8", ["const:946c8c:8", "const:4:8"]]
+ 00946c8c ["CALL", null, ["callee:009465c4:8"]]
- 00946af0 bytes 4efeff97
+ 00946c8c bytes 4efeff97
- 00946b84 ["INT_ADD", "register:40f0:8", ["const:946b84:8", "const:4:8"]]
- 00946b84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00946d20 ["INT_ADD", "register:40f0:8", ["const:946d20:8", "const:4:8"]]
+ 00946d20 ["CALL", null, ["callee:00c57eb0:8"]]
- 00946b84 bytes cb430c94
+ 00946d20 bytes 64440c94
- 00946c38 ["INT_ADD", "register:40f0:8", ["const:946c38:8", "const:4:8"]]
- 00946c38 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00946dd4 ["INT_ADD", "register:40f0:8", ["const:946dd4:8", "const:4:8"]]
+ 00946dd4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00946c38 bytes 9e430c94
+ 00946dd4 bytes 37440c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af173b724abe2ac0184bbd7548562c7a"></a>

### [`00982030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982030.md) → [`009821cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md) FUN_009821cc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) [`00980c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980c74.md) [`009812a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00982160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982160.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) [`00980e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980e10.md) [`00981440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981440.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009822fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009822fc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00982064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982030.md#insn-00982064) · [`00982084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982030.md#insn-00982084) · [`009820c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982030.md#insn-009820c0)
- 新版 [`00982200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md#insn-00982200) · [`00982220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md#insn-00982220) · [`0098225c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md#insn-0098225c)

~~~diff
- 00982064 ["INT_ADD", "register:40f0:8", ["const:982064:8", "const:4:8"]]
- 00982064 ["CALL", null, ["callee:009822fc:8"]]
+ 00982200 ["INT_ADD", "register:40f0:8", ["const:982200:8", "const:4:8"]]
+ 00982200 ["CALL", null, ["callee:009822fc:8"]]
- 00982064 bytes 3f000094
+ 00982200 bytes 3f000094
- 00982084 ["INT_ADD", "register:40f0:8", ["const:982084:8", "const:4:8"]]
- 00982084 ["CALL", null, ["callee:00c57e90:8"]]
+ 00982220 ["INT_ADD", "register:40f0:8", ["const:982220:8", "const:4:8"]]
+ 00982220 ["CALL", null, ["callee:00c57e90:8"]]
- 00982084 bytes 83560b94
+ 00982220 bytes 1c570b94
- 009820c0 ["INT_ADD", "register:40f0:8", ["const:9820c0:8", "const:4:8"]]
- 009820c0 ["CALL", null, ["callee:0043bb20:8"]]
+ 0098225c ["INT_ADD", "register:40f0:8", ["const:98225c:8", "const:4:8"]]
+ 0098225c ["CALL", null, ["callee:0043bb20:8"]]
- 009820c0 bytes 88e6ea97
+ 0098225c bytes 31e6ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eae2ceb7cc4aed134401173f5c5b2e6d"></a>

### [`0098c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c7b8.md) → [`0098c954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098c954.md) FUN_0098c954

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 1件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 2件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 1件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0098c7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c7b8.md#insn-0098c7dc)
- 新版 [`0098c978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098c954.md#insn-0098c978)

~~~diff
- 0098c7dc ["INT_ADD", "register:40f0:8", ["const:98c7dc:8", "const:4:8"]]
- 0098c7dc ["CALL", null, ["callee:00676a60:8"]]
+ 0098c978 ["INT_ADD", "register:40f0:8", ["const:98c978:8", "const:4:8"]]
+ 0098c978 ["CALL", null, ["callee:00676a60:8"]]
- 0098c7dc bytes 91a8f397
+ 0098c978 bytes 3aa8f397
~~~


<a id="compare-0ca86e7b5e847ee7314a79f8aea4f199"></a>

### [`009a9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9e44.md) → [`009a9fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9fe0.md) FUN_009a9fe0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 3件 [`009b2074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2074.md) [`009b60d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b60d4.md) [`009b66ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b66ac.md) · 呼出先 1件 [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 3件 [`009b2210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b2210.md) [`009b6270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6270.md) [`009b6848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6848.md) · 呼出先 1件 [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009a9e60",
      "incomplete_value": true,
      "site": "009a9e70",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009a9e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9e44.md#insn-009a9e70)
- 新版 [`009aa00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9fe0.md#insn-009aa00c)

~~~diff
- 009a9e70 ["INT_ADD", "register:40f0:8", ["const:9a9e70:8", "const:4:8"]]
- 009a9e70 ["CALL", null, ["callee:00c58430:8"]]
+ 009aa00c ["INT_ADD", "register:40f0:8", ["const:9aa00c:8", "const:4:8"]]
+ 009aa00c ["CALL", null, ["callee:00c58430:8"]]
- 009a9e70 bytes 70b80a94
+ 009aa00c bytes 09b90a94
~~~


<a id="compare-0da3e2a2548012bc2bcc68652ff46934"></a>

### [`009abf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abf70.md) → [`009ac10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac10c.md) FUN_009ac10c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`009abfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abfa8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`009ac144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac144.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009abf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abf70.md#insn-009abf98)
- 新版 [`009ac134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac10c.md#insn-009ac134)

~~~diff
- 009abf98 ["INT_ADD", "register:40f0:8", ["const:9abf98:8", "const:4:8"]]
- 009abf98 ["CALL", null, ["callee:009ac144:8"]]
+ 009ac134 ["INT_ADD", "register:40f0:8", ["const:9ac134:8", "const:4:8"]]
+ 009ac134 ["CALL", null, ["callee:009ac144:8"]]
- 009abf98 bytes 04000094
+ 009ac134 bytes 04000094
~~~


<a id="compare-ece6e8d95d240b364c42946712c6888d"></a>

### [`009ac65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac65c.md) → [`009ac7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md) FUN_009ac7f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086d204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d204.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0086d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d244.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ac6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac65c.md#insn-009ac6a8) · [`009ac6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac65c.md#insn-009ac6bc) · [`009ac6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac65c.md#insn-009ac6c4)
- 新版 [`009ac844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md#insn-009ac844) · [`009ac858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md#insn-009ac858) · [`009ac860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md#insn-009ac860)

~~~diff
- 009ac6a8 ["INT_ADD", "register:40f0:8", ["const:9ac6a8:8", "const:4:8"]]
- 009ac6a8 ["CALL", null, ["callee:00c53d00:8"]]
+ 009ac844 ["INT_ADD", "register:40f0:8", ["const:9ac844:8", "const:4:8"]]
+ 009ac844 ["CALL", null, ["callee:00c53d00:8"]]
- 009ac6a8 bytes 8e9c0a94
+ 009ac844 bytes 2f9d0a94
- 009ac6bc ["COPY", "register:0:8", ["register:4040:8"]]
- 009ac6bc ["INT_ADD", "register:40f0:8", ["const:9ac6bc:8", "const:4:8"]]
- 009ac6bc ["CALLIND", null, ["register:0:8"]]
+ 009ac858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ac858 ["INT_ADD", "register:40f0:8", ["const:9ac858:8", "const:4:8"]]
+ 009ac858 ["CALLIND", null, ["register:0:8"]]
- 009ac6bc bytes 00013fd6
+ 009ac858 bytes 00013fd6
- 009ac6c4 ["INT_ADD", "register:40f0:8", ["const:9ac6c4:8", "const:4:8"]]
- 009ac6c4 ["CALL", null, ["callee:00c57e80:8"]]
+ 009ac860 ["INT_ADD", "register:40f0:8", ["const:9ac860:8", "const:4:8"]]
+ 009ac860 ["CALL", null, ["callee:00c57e80:8"]]
- 009ac6c4 bytes efac0a94
+ 009ac860 bytes 88ad0a94
~~~


<a id="compare-b832f783dbffe6f469cd487e8f681232"></a>

### [`009ac888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac888.md) → [`009aca24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009aca24.md) FUN_009aca24

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009af7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af7ec.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`009af988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009af988.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ac8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac888.md#insn-009ac8a4) · [`009ac8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac888.md#insn-009ac8c4)
- 新版 [`009aca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009aca24.md#insn-009aca40) · [`009aca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009aca24.md#insn-009aca60)

~~~diff
- 009ac8a4 ["INT_ADD", "register:40f0:8", ["const:9ac8a4:8", "const:4:8"]]
- 009ac8a4 ["CALL", null, ["callee:00c53d00:8"]]
+ 009aca40 ["INT_ADD", "register:40f0:8", ["const:9aca40:8", "const:4:8"]]
+ 009aca40 ["CALL", null, ["callee:00c53d00:8"]]
- 009ac8a4 bytes 0f9c0a94
+ 009aca40 bytes b09c0a94
- 009ac8c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ac8c4 ["INT_ADD", "register:40f0:8", ["const:9ac8c4:8", "const:4:8"]]
- 009ac8c4 ["CALLIND", null, ["register:0:8"]]
+ 009aca60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009aca60 ["INT_ADD", "register:40f0:8", ["const:9aca60:8", "const:4:8"]]
+ 009aca60 ["CALLIND", null, ["register:0:8"]]
- 009ac8c4 bytes 00013fd6
+ 009aca60 bytes 00013fd6
~~~


<a id="compare-ae26e2570d86555db2d89ef9798b3d77"></a>

### [`009b0338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b0/009b0338.md) → [`009b04d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b0/009b04d4.md) FUN_009b04d4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b0350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b0/009b0338.md#insn-009b0350)
- 新版 [`009b04ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b0/009b04d4.md#insn-009b04ec)

~~~diff
- 009b0350 ["INT_ADD", "register:40f0:8", ["const:9b0350:8", "const:4:8"]]
- 009b0350 ["CALL", null, ["callee:00869ef4:8"]]
+ 009b04ec ["INT_ADD", "register:40f0:8", ["const:9b04ec:8", "const:4:8"]]
+ 009b04ec ["CALL", null, ["callee:00869ef4:8"]]
- 009b0350 bytes d9e6fa97
+ 009b04ec bytes 82e6fa97
~~~


<a id="compare-187e2048aad0bcf4ba34c866051c76f1"></a>

### [`009b64d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b64d8.md) → [`009b6674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6674.md) FUN_009b6674

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009b39cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009b3b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b68.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b6514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b64d8.md#insn-009b6514)
- 新版 [`009b66b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6674.md#insn-009b66b0)

~~~diff
- 009b6514 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6514 ["INT_ADD", "register:40f0:8", ["const:9b6514:8", "const:4:8"]]
- 009b6514 ["CALLIND", null, ["register:0:8"]]
+ 009b66b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b66b0 ["INT_ADD", "register:40f0:8", ["const:9b66b0:8", "const:4:8"]]
+ 009b66b0 ["CALLIND", null, ["register:0:8"]]
- 009b6514 bytes 00013fd6
+ 009b66b0 bytes 00013fd6
~~~


<a id="compare-75f3060376e71691dcaae4e9acd1b8e1"></a>

### [`009b6528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6528.md) → [`009b66c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b66c4.md) FUN_009b66c4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`009a9ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9ec8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009aa064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa064.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b6558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6528.md#insn-009b6558) · [`009b6584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6528.md#insn-009b6584) · [`009b65bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6528.md#insn-009b65bc)
- 新版 [`009b66f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b66c4.md#insn-009b66f4) · [`009b6720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b66c4.md#insn-009b6720) · [`009b6758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b66c4.md#insn-009b6758)

~~~diff
- 009b6558 ["INT_ADD", "register:40f0:8", ["const:9b6558:8", "const:4:8"]]
- 009b6558 ["CALL", null, ["callee:009aa064:8"]]
+ 009b66f4 ["INT_ADD", "register:40f0:8", ["const:9b66f4:8", "const:4:8"]]
+ 009b66f4 ["CALL", null, ["callee:009aa064:8"]]
- 009b6558 bytes 5cceff97
+ 009b66f4 bytes 5cceff97
- 009b6584 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6584 ["INT_ADD", "register:40f0:8", ["const:9b6584:8", "const:4:8"]]
- 009b6584 ["CALLIND", null, ["register:0:8"]]
+ 009b6720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b6720 ["INT_ADD", "register:40f0:8", ["const:9b6720:8", "const:4:8"]]
+ 009b6720 ["CALLIND", null, ["register:0:8"]]
- 009b6584 bytes 00013fd6
+ 009b6720 bytes 00013fd6
- 009b65bc ["INT_ADD", "register:40f0:8", ["const:9b65bc:8", "const:4:8"]]
- 009b65bc ["CALL", null, ["callee:00459d74:8"]]
+ 009b6758 ["INT_ADD", "register:40f0:8", ["const:9b6758:8", "const:4:8"]]
+ 009b6758 ["CALL", null, ["callee:00459d74:8"]]
- 009b65bc bytes de8dea97
+ 009b6758 bytes 878dea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aad6cb7f8586e48b9bf72ac1c3fa4855"></a>

### [`009b6a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6a6c.md) → [`009b6c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c08.md) FUN_009b6c08

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009b4c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009b4e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4e2c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b6aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6a6c.md#insn-009b6aa8)
- 新版 [`009b6c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c08.md#insn-009b6c44)

~~~diff
- 009b6aa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6aa8 ["INT_ADD", "register:40f0:8", ["const:9b6aa8:8", "const:4:8"]]
- 009b6aa8 ["CALLIND", null, ["register:0:8"]]
+ 009b6c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b6c44 ["INT_ADD", "register:40f0:8", ["const:9b6c44:8", "const:4:8"]]
+ 009b6c44 ["CALLIND", null, ["register:0:8"]]
- 009b6aa8 bytes 00013fd6
+ 009b6c44 bytes 00013fd6
~~~


<a id="compare-3788fafd95b7c1d1af998fba19139893"></a>

### [`009b6abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6abc.md) → [`009b6c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c58.md) FUN_009b6c58

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`009aa488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa488.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`009aa624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa624.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b6b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6abc.md#insn-009b6b1c) · [`009b6b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6abc.md#insn-009b6b2c) · [`009b6b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6abc.md#insn-009b6b58)
- 新版 [`009b6cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c58.md#insn-009b6cb8) · [`009b6cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c58.md#insn-009b6cc8) · [`009b6cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c58.md#insn-009b6cf4)

~~~diff
- 009b6b1c ["INT_ADD", "register:40f0:8", ["const:9b6b1c:8", "const:4:8"]]
- 009b6b1c ["CALL", null, ["callee:005a9d24:8"]]
+ 009b6cb8 ["INT_ADD", "register:40f0:8", ["const:9b6cb8:8", "const:4:8"]]
+ 009b6cb8 ["CALL", null, ["callee:005a9d24:8"]]
- 009b6b1c bytes 72ccef97
+ 009b6cb8 bytes 1bccef97
- 009b6b2c ["INT_ADD", "register:40f0:8", ["const:9b6b2c:8", "const:4:8"]]
- 009b6b2c ["CALL", null, ["callee:009aa624:8"]]
+ 009b6cc8 ["INT_ADD", "register:40f0:8", ["const:9b6cc8:8", "const:4:8"]]
+ 009b6cc8 ["CALL", null, ["callee:009aa624:8"]]
- 009b6b2c bytes 57ceff97
+ 009b6cc8 bytes 57ceff97
- 009b6b58 ["INT_ADD", "register:40f0:8", ["const:9b6b58:8", "const:4:8"]]
- 009b6b58 ["CALL", null, ["callee:005aa184:8"]]
+ 009b6cf4 ["INT_ADD", "register:40f0:8", ["const:9b6cf4:8", "const:4:8"]]
+ 009b6cf4 ["CALL", null, ["callee:005aa184:8"]]
- 009b6b58 bytes 7bcdef97
+ 009b6cf4 bytes 24cdef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1413e5a975140494d1424c57edb5ad3f"></a>

### [`009b6e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e5c.md) → [`009b6ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6ff8.md) FUN_009b6ff8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b6e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e5c.md#insn-009b6e9c) · [`009b6ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e5c.md#insn-009b6ed0) · [`009b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e5c.md#insn-009b6ed4)
- 新版 [`009b7038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6ff8.md#insn-009b7038) · [`009b706c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6ff8.md#insn-009b706c) · [`009b7070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6ff8.md#insn-009b7070)

~~~diff
- 009b6e9c ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6e9c ["INT_ADD", "register:40f0:8", ["const:9b6e9c:8", "const:4:8"]]
- 009b6e9c ["CALLIND", null, ["register:0:8"]]
+ 009b7038 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b7038 ["INT_ADD", "register:40f0:8", ["const:9b7038:8", "const:4:8"]]
+ 009b7038 ["CALLIND", null, ["register:0:8"]]
- 009b6e9c bytes 00013fd6
+ 009b7038 bytes 00013fd6
- 009b6ed0 ["INT_ADD", "register:40f0:8", ["const:9b6ed0:8", "const:4:8"]]
- 009b6ed0 ["CALL", null, ["callee:00459d74:8"]]
+ 009b706c ["INT_ADD", "register:40f0:8", ["const:9b706c:8", "const:4:8"]]
+ 009b706c ["CALL", null, ["callee:00459d74:8"]]
- 009b6ed0 bytes 998bea97
+ 009b706c bytes 428bea97
- 009b6ed4 ["INT_ADD", "register:40f0:8", ["const:9b6ed4:8", "const:4:8"]]
- 009b6ed4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 009b7070 ["INT_ADD", "register:40f0:8", ["const:9b7070:8", "const:4:8"]]
+ 009b7070 ["CALL", null, ["callee:00c57ee0:8"]]
- 009b6ed4 bytes 03830a94
+ 009b7070 bytes 9c830a94
~~~


<a id="compare-cba2d3c99c9391a2e8ca6a770b4f8579"></a>

### [`009b724c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b724c.md) → [`009b73e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b73e8.md) FUN_009b73e8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009b5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b53bc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b7288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b724c.md#insn-009b7288)
- 新版 [`009b7424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b73e8.md#insn-009b7424)

~~~diff
- 009b7288 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b7288 ["INT_ADD", "register:40f0:8", ["const:9b7288:8", "const:4:8"]]
- 009b7288 ["CALLIND", null, ["register:0:8"]]
+ 009b7424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b7424 ["INT_ADD", "register:40f0:8", ["const:9b7424:8", "const:4:8"]]
+ 009b7424 ["CALLIND", null, ["register:0:8"]]
- 009b7288 bytes 00013fd6
+ 009b7424 bytes 00013fd6
~~~


<a id="compare-39016d9676fd34703d08735daf8c0189"></a>

### [`009b750c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b750c.md) → [`009b76a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b76a8.md) FUN_009b76a8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009b5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b53bc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b7548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b750c.md#insn-009b7548)
- 新版 [`009b76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b76a8.md#insn-009b76e4)

~~~diff
- 009b7548 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b7548 ["INT_ADD", "register:40f0:8", ["const:9b7548:8", "const:4:8"]]
- 009b7548 ["CALLIND", null, ["register:0:8"]]
+ 009b76e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b76e4 ["INT_ADD", "register:40f0:8", ["const:9b76e4:8", "const:4:8"]]
+ 009b76e4 ["CALLIND", null, ["register:0:8"]]
- 009b7548 bytes 00013fd6
+ 009b76e4 bytes 00013fd6
~~~


<a id="compare-90256a1491bb41f5f914de55843d8598"></a>

### [`009b755c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b755c.md) → [`009b76f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b76f8.md) FUN_009b76f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b7578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b755c.md#insn-009b7578)
- 新版 [`009b7714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b76f8.md#insn-009b7714)

~~~diff
- 009b7578 ["INT_ADD", "register:40f0:8", ["const:9b7578:8", "const:4:8"]]
- 009b7578 ["CALL", null, ["callee:00459d74:8"]]
+ 009b7714 ["INT_ADD", "register:40f0:8", ["const:9b7714:8", "const:4:8"]]
+ 009b7714 ["CALL", null, ["callee:00459d74:8"]]
- 009b7578 bytes ef89ea97
+ 009b7714 bytes 9889ea97
~~~


<a id="compare-f2787fcc346751f027c993392f03cf66"></a>

### [`009b78f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b78f0.md) → [`009b7a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7a8c.md) FUN_009b7a8c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009b4764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009b4900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4900.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b78f0.md#insn-009b792c)
- 新版 [`009b7ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7a8c.md#insn-009b7ac8)

~~~diff
- 009b792c ["COPY", "register:0:8", ["register:4040:8"]]
- 009b792c ["INT_ADD", "register:40f0:8", ["const:9b792c:8", "const:4:8"]]
- 009b792c ["CALLIND", null, ["register:0:8"]]
+ 009b7ac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b7ac8 ["INT_ADD", "register:40f0:8", ["const:9b7ac8:8", "const:4:8"]]
+ 009b7ac8 ["CALLIND", null, ["register:0:8"]]
- 009b792c bytes 00013fd6
+ 009b7ac8 bytes 00013fd6
~~~


<a id="compare-bc7bc1f02a543a222a06b3b044e4b7be"></a>

### [`009b7fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7fe4.md) → [`009b8180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8180.md) FUN_009b8180

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b801c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7fe4.md#insn-009b801c) · [`009b8050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7fe4.md#insn-009b8050) · [`009b8054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7fe4.md#insn-009b8054)
- 新版 [`009b81b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8180.md#insn-009b81b8) · [`009b81ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8180.md#insn-009b81ec) · [`009b81f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8180.md#insn-009b81f0)

~~~diff
- 009b801c ["COPY", "register:0:8", ["register:4040:8"]]
- 009b801c ["INT_ADD", "register:40f0:8", ["const:9b801c:8", "const:4:8"]]
- 009b801c ["CALLIND", null, ["register:0:8"]]
+ 009b81b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b81b8 ["INT_ADD", "register:40f0:8", ["const:9b81b8:8", "const:4:8"]]
+ 009b81b8 ["CALLIND", null, ["register:0:8"]]
- 009b801c bytes 00013fd6
+ 009b81b8 bytes 00013fd6
- 009b8050 ["INT_ADD", "register:40f0:8", ["const:9b8050:8", "const:4:8"]]
- 009b8050 ["CALL", null, ["callee:00459d74:8"]]
+ 009b81ec ["INT_ADD", "register:40f0:8", ["const:9b81ec:8", "const:4:8"]]
+ 009b81ec ["CALL", null, ["callee:00459d74:8"]]
- 009b8050 bytes 3987ea97
+ 009b81ec bytes e286ea97
- 009b8054 ["INT_ADD", "register:40f0:8", ["const:9b8054:8", "const:4:8"]]
- 009b8054 ["CALL", null, ["callee:00c57ee0:8"]]
+ 009b81f0 ["INT_ADD", "register:40f0:8", ["const:9b81f0:8", "const:4:8"]]
+ 009b81f0 ["CALL", null, ["callee:00c57ee0:8"]]
- 009b8054 bytes a37e0a94
+ 009b81f0 bytes 3c7f0a94
~~~


<a id="compare-489bdcf4fe6a86021a662469ee877c82"></a>

### [`009b82a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82a4.md) → [`009b8440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8440.md) FUN_009b8440

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b82c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82a4.md#insn-009b82c0)
- 新版 [`009b845c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8440.md#insn-009b845c)

~~~diff
- 009b82c0 ["INT_ADD", "register:40f0:8", ["const:9b82c0:8", "const:4:8"]]
- 009b82c0 ["CALL", null, ["callee:00459d74:8"]]
+ 009b845c ["INT_ADD", "register:40f0:8", ["const:9b845c:8", "const:4:8"]]
+ 009b845c ["CALL", null, ["callee:00459d74:8"]]
- 009b82c0 bytes 9d86ea97
+ 009b845c bytes 4686ea97
~~~


<a id="compare-e560a45997a08c1d3c7689d81060bc44"></a>

### [`009b86d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md) → [`009b886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b886c.md) FUN_009b886c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084874c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084874c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 3件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084878c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/0084878c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b86f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md#insn-009b86f4) · [`009b8708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md#insn-009b8708) · [`009b8728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md#insn-009b8728)
- 新版 [`009b8890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b886c.md#insn-009b8890) · [`009b88a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b886c.md#insn-009b88a4) · [`009b88c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b886c.md#insn-009b88c4)

~~~diff
- 009b86f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b86f4 ["INT_ADD", "register:40f0:8", ["const:9b86f4:8", "const:4:8"]]
- 009b86f4 ["CALLIND", null, ["register:0:8"]]
+ 009b8890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b8890 ["INT_ADD", "register:40f0:8", ["const:9b8890:8", "const:4:8"]]
+ 009b8890 ["CALLIND", null, ["register:0:8"]]
- 009b86f4 bytes 00013fd6
+ 009b8890 bytes 00013fd6
- 009b8708 ["INT_ADD", "register:40f0:8", ["const:9b8708:8", "const:4:8"]]
- 009b8708 ["CALL", null, ["callee:00c53d00:8"]]
+ 009b88a4 ["INT_ADD", "register:40f0:8", ["const:9b88a4:8", "const:4:8"]]
+ 009b88a4 ["CALL", null, ["callee:00c53d00:8"]]
- 009b8708 bytes 766c0a94
+ 009b88a4 bytes 176d0a94
- 009b8728 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b8728 ["INT_ADD", "register:40f0:8", ["const:9b8728:8", "const:4:8"]]
- 009b8728 ["CALLIND", null, ["register:0:8"]]
+ 009b88c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b88c4 ["INT_ADD", "register:40f0:8", ["const:9b88c4:8", "const:4:8"]]
+ 009b88c4 ["CALLIND", null, ["register:0:8"]]
- 009b8728 bytes 00013fd6
+ 009b88c4 bytes 00013fd6
~~~


<a id="compare-db3aed1638c6f8133646285d76c9d384"></a>

### [`009b92f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md) → [`009b948c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b948c.md) FUN_009b948c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ba1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba1e0.md) · 呼出先 4件 [`00935c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935c98.md) [`009ad7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad7e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009ba37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba37c.md) · 呼出先 4件 [`00935e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e34.md) [`009ad980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009ad980.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b9320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md#insn-009b9320) · [`009b9378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md#insn-009b9378) · [`009b9388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md#insn-009b9388)
- 新版 [`009b94bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b948c.md#insn-009b94bc) · [`009b9514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b948c.md#insn-009b9514) · [`009b9524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b948c.md#insn-009b9524)

~~~diff
- 009b9320 ["INT_ADD", "register:40f0:8", ["const:9b9320:8", "const:4:8"]]
- 009b9320 ["CALL", null, ["callee:009ad980:8"]]
+ 009b94bc ["INT_ADD", "register:40f0:8", ["const:9b94bc:8", "const:4:8"]]
+ 009b94bc ["CALL", null, ["callee:009ad980:8"]]
- 009b9320 bytes 31d1ff97
+ 009b94bc bytes 31d1ff97
- 009b9378 ["INT_ADD", "register:40f0:8", ["const:9b9378:8", "const:4:8"]]
- 009b9378 ["CALL", null, ["callee:00935e34:8"]]
+ 009b9514 ["INT_ADD", "register:40f0:8", ["const:9b9514:8", "const:4:8"]]
+ 009b9514 ["CALL", null, ["callee:00935e34:8"]]
- 009b9378 bytes 48f2fd97
+ 009b9514 bytes 48f2fd97
- 009b9388 ["INT_ADD", "register:40f0:8", ["const:9b9388:8", "const:4:8"]]
- 009b9388 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009b9524 ["INT_ADD", "register:40f0:8", ["const:9b9524:8", "const:4:8"]]
+ 009b9524 ["CALL", null, ["callee:00c57eb0:8"]]
- 009b9388 bytes ca790a94
+ 009b9524 bytes 637a0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2080b5b45ce125a84337e9cfb14ba95"></a>

### [`009b93e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b93e4.md) → [`009b9580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b9580.md) FUN_009b9580

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 6件 [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b6efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6efc.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`009ad7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad7e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 6件 [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b6f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f40.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`009ad980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009ad980.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b9418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b93e4.md#insn-009b9418) · [`009b9438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b93e4.md#insn-009b9438) · [`009b944c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b93e4.md#insn-009b944c)
- 新版 [`009b95b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b9580.md#insn-009b95b4) · [`009b95d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b9580.md#insn-009b95d4) · [`009b95e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b9580.md#insn-009b95e8)

~~~diff
- 009b9418 ["INT_ADD", "register:40f0:8", ["const:9b9418:8", "const:4:8"]]
- 009b9418 ["CALL", null, ["callee:009ad980:8"]]
+ 009b95b4 ["INT_ADD", "register:40f0:8", ["const:9b95b4:8", "const:4:8"]]
+ 009b95b4 ["CALL", null, ["callee:009ad980:8"]]
- 009b9418 bytes f3d0ff97
+ 009b95b4 bytes f3d0ff97
- 009b9438 ["INT_ADD", "register:40f0:8", ["const:9b9438:8", "const:4:8"]]
- 009b9438 ["CALL", null, ["callee:008b79c8:8"]]
+ 009b95d4 ["INT_ADD", "register:40f0:8", ["const:9b95d4:8", "const:4:8"]]
+ 009b95d4 ["CALL", null, ["callee:008b79c8:8"]]
- 009b9438 bytes 53f9fb97
+ 009b95d4 bytes fdf8fb97
- 009b944c ["INT_ADD", "register:40f0:8", ["const:9b944c:8", "const:4:8"]]
- 009b944c ["CALL", null, ["callee:008b6f40:8"]]
+ 009b95e8 ["INT_ADD", "register:40f0:8", ["const:9b95e8:8", "const:4:8"]]
+ 009b95e8 ["CALL", null, ["callee:008b6f40:8"]]
- 009b944c bytes acf6fb97
+ 009b95e8 bytes 56f6fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d922fe1186af9129951e06252c48af17"></a>

### [`009b9548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9548.md) → [`009b96e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b96e4.md) FUN_009b96e4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`009ad9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9cc.md) [`00acbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`009adb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adb68.md) [`00acbf2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbf2c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9548.md#insn-009b956c) · [`009b9580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9548.md#insn-009b9580)
- 新版 [`009b9708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b96e4.md#insn-009b9708) · [`009b971c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b96e4.md#insn-009b971c)

~~~diff
- 009b956c ["INT_ADD", "register:40f0:8", ["const:9b956c:8", "const:4:8"]]
- 009b956c ["CALL", null, ["callee:009adb68:8"]]
+ 009b9708 ["INT_ADD", "register:40f0:8", ["const:9b9708:8", "const:4:8"]]
+ 009b9708 ["CALL", null, ["callee:009adb68:8"]]
- 009b956c bytes 18d1ff97
+ 009b9708 bytes 18d1ff97
- 009b9580 ["INT_ADD", "register:40f0:8", ["const:9b9580:8", "const:4:8"]]
- 009b9580 ["CALL", null, ["callee:00acbf2c:8"]]
+ 009b971c ["INT_ADD", "register:40f0:8", ["const:9b971c:8", "const:4:8"]]
+ 009b971c ["CALL", null, ["callee:00acbf2c:8"]]
- 009b9580 bytes ec490494
+ 009b971c bytes 044a0494
~~~


<a id="compare-23fea9f6823653b53e61602ef3bb4705"></a>

### [`009b9ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9ea0.md) → [`009ba03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba03c.md) FUN_009ba03c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`009ad9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9cc.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`009adb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adb68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b9eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9ea0.md#insn-009b9eb4)
- 新版 [`009ba050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba03c.md#insn-009ba050)

~~~diff
- 009b9eb4 ["INT_ADD", "register:40f0:8", ["const:9b9eb4:8", "const:4:8"]]
- 009b9eb4 ["CALL", null, ["callee:009adb68:8"]]
+ 009ba050 ["INT_ADD", "register:40f0:8", ["const:9ba050:8", "const:4:8"]]
+ 009ba050 ["CALL", null, ["callee:009adb68:8"]]
- 009b9eb4 bytes c6ceff97
+ 009ba050 bytes c6ceff97
~~~


<a id="compare-5fd2adeb23084f9663c8957193106ccd"></a>

### [`009c0d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0d64.md) → [`009c0f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0f00.md) FUN_009c0f00

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009c03f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c03f0.md) [`009c0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0bdc.md) · 呼出先 3件 [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`009c058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c058c.md) [`009c0d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0d78.md) · 呼出先 3件 [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c0d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0d64.md#insn-009c0d8c) · [`009c0da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0d64.md#insn-009c0da4) · [`009c0dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0d64.md#insn-009c0dbc)
- 新版 [`009c0f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0f00.md#insn-009c0f28) · [`009c0f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0f00.md#insn-009c0f40) · [`009c0f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0f00.md#insn-009c0f58)

~~~diff
- 009c0d8c ["INT_ADD", "register:40f0:8", ["const:9c0d8c:8", "const:4:8"]]
- 009c0d8c ["CALL", null, ["callee:00c53cd0:8"]]
+ 009c0f28 ["INT_ADD", "register:40f0:8", ["const:9c0f28:8", "const:4:8"]]
+ 009c0f28 ["CALL", null, ["callee:00c53cd0:8"]]
- 009c0d8c bytes c94a0a94
+ 009c0f28 bytes 6a4b0a94
- 009c0da4 ["INT_ADD", "register:40f0:8", ["const:9c0da4:8", "const:4:8"]]
- 009c0da4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 009c0f40 ["INT_ADD", "register:40f0:8", ["const:9c0f40:8", "const:4:8"]]
+ 009c0f40 ["CALL", null, ["callee:00c53cd0:8"]]
- 009c0da4 bytes c34a0a94
+ 009c0f40 bytes 644b0a94
- 009c0dbc ["INT_ADD", "register:40f0:8", ["const:9c0dbc:8", "const:4:8"]]
- 009c0dbc ["CALL", null, ["callee:00c53cd0:8"]]
+ 009c0f58 ["INT_ADD", "register:40f0:8", ["const:9c0f58:8", "const:4:8"]]
+ 009c0f58 ["CALL", null, ["callee:00c53cd0:8"]]
- 009c0dbc bytes bd4a0a94
+ 009c0f58 bytes 5e4b0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe1945284222f92a20c80085e59c672b"></a>

### [`009c0e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0e48.md) → [`009c0fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0fe4.md) FUN_009c0fe4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869788.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008697c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008697c8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c0e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0e48.md#insn-009c0e6c)
- 新版 [`009c1008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0fe4.md#insn-009c1008)

~~~diff
- 009c0e6c ["INT_ADD", "register:40f0:8", ["const:9c0e6c:8", "const:4:8"]]
- 009c0e6c ["CALL", null, ["callee:008697c8:8"]]
+ 009c1008 ["INT_ADD", "register:40f0:8", ["const:9c1008:8", "const:4:8"]]
+ 009c1008 ["CALL", null, ["callee:008697c8:8"]]
- 009c0e6c bytes 47a2fa97
+ 009c1008 bytes f0a1fa97
~~~


<a id="compare-1b5a643b4eec4b9fdb4dc65333ef57e6"></a>

### [`009c137c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c137c.md) → [`009c1518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c1/009c1518.md) FUN_009c1518

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md) [`008b9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md) [`00a83390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md) [`00a83588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83588.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c1390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c137c.md#insn-009c1390) · [`009c1398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c137c.md#insn-009c1398) · [`009c13e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c137c.md#insn-009c13e0)
- 新版 [`009c152c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c1/009c1518.md#insn-009c152c) · [`009c1534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c1/009c1518.md#insn-009c1534) · [`009c157c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c1/009c1518.md#insn-009c157c)

~~~diff
- 009c1390 ["INT_ADD", "register:40f0:8", ["const:9c1390:8", "const:4:8"]]
- 009c1390 ["CALL", null, ["callee:008b9290:8"]]
+ 009c152c ["INT_ADD", "register:40f0:8", ["const:9c152c:8", "const:4:8"]]
+ 009c152c ["CALL", null, ["callee:008b9290:8"]]
- 009c1390 bytes afdffb97
+ 009c152c bytes 59dffb97
- 009c1398 ["INT_ADD", "register:40f0:8", ["const:9c1398:8", "const:4:8"]]
- 009c1398 ["CALL", null, ["callee:008514f8:8"]]
+ 009c1534 ["INT_ADD", "register:40f0:8", ["const:9c1534:8", "const:4:8"]]
+ 009c1534 ["CALL", null, ["callee:008514f8:8"]]
- 009c1398 bytes 4840fa97
+ 009c1534 bytes f13ffa97
- 009c13e0 ["INT_ADD", "register:40f0:8", ["const:9c13e0:8", "const:4:8"]]
- 009c13e0 ["CALL", null, ["callee:008514f8:8"]]
+ 009c157c ["INT_ADD", "register:40f0:8", ["const:9c157c:8", "const:4:8"]]
+ 009c157c ["CALL", null, ["callee:008514f8:8"]]
- 009c13e0 bytes 3640fa97
+ 009c157c bytes df3ffa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5477702dd1374d2547304be23bc877d"></a>

### [`009c75e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c75e8.md) → [`009c7784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7784.md) FUN_009c7784

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`009a3064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3064.md) · 呼出先 1件 [`009c7630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7630.md)
- 新版 呼出元 2件 [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`009a3200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3200.md) · 呼出先 1件 [`009c77cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c77cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c7600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c75e8.md#insn-009c7600)
- 新版 [`009c779c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7784.md#insn-009c779c)

~~~diff
- 009c7600 ["INT_ADD", "register:40f0:8", ["const:9c7600:8", "const:4:8"]]
- 009c7600 ["CALL", null, ["callee:009c77cc:8"]]
+ 009c779c ["INT_ADD", "register:40f0:8", ["const:9c779c:8", "const:4:8"]]
+ 009c779c ["CALL", null, ["callee:009c77cc:8"]]
- 009c7600 bytes 0c000094
+ 009c779c bytes 0c000094
~~~


<a id="compare-01f1b0ed3adc8d684a8be4bf87fa0557"></a>

### [`009c7a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7a0c.md) → [`009c7ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7ba8.md) FUN_009c7ba8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00996780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996780.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`0099b8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0099b/0099b8d4.md) [`009c7630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7630.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`0099691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/0099691c.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) [`009c77cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c77cc.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c7ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7a0c.md#insn-009c7ab8) · [`009c7af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7a0c.md#insn-009c7af4)
- 新版 [`009c7c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7ba8.md#insn-009c7c54) · [`009c7c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7ba8.md#insn-009c7c90)

~~~diff
- 009c7ab8 ["INT_ADD", "register:40f0:8", ["const:9c7ab8:8", "const:4:8"]]
- 009c7ab8 ["CALL", null, ["callee:00c57e90:8"]]
+ 009c7c54 ["INT_ADD", "register:40f0:8", ["const:9c7c54:8", "const:4:8"]]
+ 009c7c54 ["CALL", null, ["callee:00c57e90:8"]]
- 009c7ab8 bytes f63f0a94
+ 009c7c54 bytes 8f400a94
- 009c7af4 ["INT_ADD", "register:40f0:8", ["const:9c7af4:8", "const:4:8"]]
- 009c7af4 ["CALL", null, ["callee:0043bba4:8"]]
+ 009c7c90 ["INT_ADD", "register:40f0:8", ["const:9c7c90:8", "const:4:8"]]
+ 009c7c90 ["CALL", null, ["callee:0043bba4:8"]]
- 009c7af4 bytes 1cd0e997
+ 009c7c90 bytes c5cfe997
~~~


<a id="compare-898301145b76e8279009ea9ac1300c31"></a>

### [`009c7b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7b14.md) → [`009c7cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7cb0.md) FUN_009c7cb0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`009a2c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2c70.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`009a2e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2e0c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c7bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7b14.md#insn-009c7bc0) · [`009c7c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7b14.md#insn-009c7c00)
- 新版 [`009c7d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7cb0.md#insn-009c7d5c) · [`009c7d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7cb0.md#insn-009c7d9c)

~~~diff
- 009c7bc0 ["INT_ADD", "register:40f0:8", ["const:9c7bc0:8", "const:4:8"]]
- 009c7bc0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009c7d5c ["INT_ADD", "register:40f0:8", ["const:9c7d5c:8", "const:4:8"]]
+ 009c7d5c ["CALL", null, ["callee:00c57e90:8"]]
- 009c7bc0 bytes b43f0a94
+ 009c7d5c bytes 4d400a94
- 009c7c00 ["INT_ADD", "register:40f0:8", ["const:9c7c00:8", "const:4:8"]]
- 009c7c00 ["CALL", null, ["callee:0043bba4:8"]]
+ 009c7d9c ["INT_ADD", "register:40f0:8", ["const:9c7d9c:8", "const:4:8"]]
+ 009c7d9c ["CALL", null, ["callee:0043bba4:8"]]
- 009c7c00 bytes d9cfe997
+ 009c7d9c bytes 82cfe997
~~~


<a id="compare-7a1c6390fb3d9e589c664350c1f68aa0"></a>

### [`009c7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7c20.md) → [`009c7dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7dbc.md) FUN_009c7dbc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c7c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7c20.md#insn-009c7c54) · [`009c7c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7c20.md#insn-009c7c84) · [`009c7cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7c20.md#insn-009c7cd8)
- 新版 [`009c7df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7dbc.md#insn-009c7df0) · [`009c7e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7dbc.md#insn-009c7e20) · [`009c7e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7dbc.md#insn-009c7e74)

~~~diff
- 009c7c54 ["INT_ADD", "register:40f0:8", ["const:9c7c54:8", "const:4:8"]]
- 009c7c54 ["CALL", null, ["callee:00480178:8"]]
+ 009c7df0 ["INT_ADD", "register:40f0:8", ["const:9c7df0:8", "const:4:8"]]
+ 009c7df0 ["CALL", null, ["callee:00480178:8"]]
- 009c7c54 bytes 39e1ea97
+ 009c7df0 bytes e2e0ea97
- 009c7c84 ["INT_ADD", "register:40f0:8", ["const:9c7c84:8", "const:4:8"]]
- 009c7c84 ["CALL", null, ["callee:00480178:8"]]
+ 009c7e20 ["INT_ADD", "register:40f0:8", ["const:9c7e20:8", "const:4:8"]]
+ 009c7e20 ["CALL", null, ["callee:00480178:8"]]
- 009c7c84 bytes 2de1ea97
+ 009c7e20 bytes d6e0ea97
- 009c7cd8 ["INT_ADD", "register:40f0:8", ["const:9c7cd8:8", "const:4:8"]]
- 009c7cd8 ["CALL", null, ["callee:00c57e90:8"]]
+ 009c7e74 ["INT_ADD", "register:40f0:8", ["const:9c7e74:8", "const:4:8"]]
+ 009c7e74 ["CALL", null, ["callee:00c57e90:8"]]
- 009c7cd8 bytes 6e3f0a94
+ 009c7e74 bytes 07400a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62b04247a61797fa80148b2a132cb363"></a>

### [`009c86c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c86c4.md) → [`009c8860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8860.md) FUN_009c8860

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c86f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c86c4.md#insn-009c86f4) · [`009c870c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c86c4.md#insn-009c870c) · [`009c8728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c86c4.md#insn-009c8728)
- 新版 [`009c8890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8860.md#insn-009c8890) · [`009c88a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8860.md#insn-009c88a8) · [`009c88c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8860.md#insn-009c88c4)

~~~diff
- 009c86f4 ["INT_ADD", "register:40f0:8", ["const:9c86f4:8", "const:4:8"]]
- 009c86f4 ["CALL", null, ["callee:00480b90:8"]]
+ 009c8890 ["INT_ADD", "register:40f0:8", ["const:9c8890:8", "const:4:8"]]
+ 009c8890 ["CALL", null, ["callee:00480b90:8"]]
- 009c86f4 bytes 17e1ea97
+ 009c8890 bytes c0e0ea97
- 009c870c ["INT_ADD", "register:40f0:8", ["const:9c870c:8", "const:4:8"]]
- 009c870c ["CALL", null, ["callee:00480b90:8"]]
+ 009c88a8 ["INT_ADD", "register:40f0:8", ["const:9c88a8:8", "const:4:8"]]
+ 009c88a8 ["CALL", null, ["callee:00480b90:8"]]
- 009c870c bytes 11e1ea97
+ 009c88a8 bytes bae0ea97
- 009c8728 ["INT_ADD", "register:40f0:8", ["const:9c8728:8", "const:4:8"]]
- 009c8728 ["CALL", null, ["callee:00480b90:8"]]
+ 009c88c4 ["INT_ADD", "register:40f0:8", ["const:9c88c4:8", "const:4:8"]]
+ 009c88c4 ["CALL", null, ["callee:00480b90:8"]]
- 009c8728 bytes 0ae1ea97
+ 009c88c4 bytes b3e0ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05d747c3a3ef5016d9b9f4a42ac1a08c"></a>

### [`009c8940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md) → [`009c8adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8adc.md) FUN_009c8adc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c3874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c3874.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009c3a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c3a10.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c89f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md#insn-009c89f0) · [`009c8a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md#insn-009c8a00) · [`009c8a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md#insn-009c8a08)
- 新版 [`009c8b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8adc.md#insn-009c8b8c) · [`009c8b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8adc.md#insn-009c8b9c) · [`009c8ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c8/009c8adc.md#insn-009c8ba4)

~~~diff
- 009c89f0 ["INT_ADD", "register:40f0:8", ["const:9c89f0:8", "const:4:8"]]
- 009c89f0 ["CALL", null, ["callee:00494610:8"]]
+ 009c8b8c ["INT_ADD", "register:40f0:8", ["const:9c8b8c:8", "const:4:8"]]
+ 009c8b8c ["CALL", null, ["callee:00494610:8"]]
- 009c89f0 bytes f82eeb97
+ 009c8b8c bytes a12eeb97
- 009c8a00 ["INT_ADD", "register:40f0:8", ["const:9c8a00:8", "const:4:8"]]
- 009c8a00 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009c8b9c ["INT_ADD", "register:40f0:8", ["const:9c8b9c:8", "const:4:8"]]
+ 009c8b9c ["CALL", null, ["callee:00c57eb0:8"]]
- 009c8a00 bytes 2c3c0a94
+ 009c8b9c bytes c53c0a94
- 009c8a08 ["INT_ADD", "register:40f0:8", ["const:9c8a08:8", "const:4:8"]]
- 009c8a08 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009c8ba4 ["INT_ADD", "register:40f0:8", ["const:9c8ba4:8", "const:4:8"]]
+ 009c8ba4 ["CALL", null, ["callee:00c57eb0:8"]]
- 009c8a08 bytes 2a3c0a94
+ 009c8ba4 bytes c33c0a94
~~~


<a id="compare-ec4ce127caa4f54b59a195ac1e63a63a"></a>

### [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) → [`009c9bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md) FUN_009c9bb8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009c3874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c3874.md) [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) [`009c9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md) · 呼出先 4件 [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) [`009c9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md) [`009c9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md) [`009ca19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md)
- 新版 呼出元 3件 [`009c3a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c3a10.md) [`009c9bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md) [`009ca054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca054.md) · 呼出先 4件 [`009c9bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md) [`009c9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9ee0.md) [`009ca054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca054.md) [`009ca338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c9a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md#insn-009c9a70) · [`009c9ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md#insn-009c9ae0) · [`009c9b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md#insn-009c9b0c)
- 新版 [`009c9c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md#insn-009c9c0c) · [`009c9c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md#insn-009c9c7c) · [`009c9ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md#insn-009c9ca8)

~~~diff
- 009c9a70 ["INT_ADD", "register:40f0:8", ["const:9c9a70:8", "const:4:8"]]
- 009c9a70 ["CALL", null, ["callee:009c9ee0:8"]]
+ 009c9c0c ["INT_ADD", "register:40f0:8", ["const:9c9c0c:8", "const:4:8"]]
+ 009c9c0c ["CALL", null, ["callee:009c9ee0:8"]]
- 009c9a70 bytes b5000094
+ 009c9c0c bytes b5000094
- 009c9ae0 ["INT_ADD", "register:40f0:8", ["const:9c9ae0:8", "const:4:8"]]
- 009c9ae0 ["CALL", null, ["callee:009c9ee0:8"]]
+ 009c9c7c ["INT_ADD", "register:40f0:8", ["const:9c9c7c:8", "const:4:8"]]
+ 009c9c7c ["CALL", null, ["callee:009c9ee0:8"]]
- 009c9ae0 bytes 99000094
+ 009c9c7c bytes 99000094
- 009c9b0c ["INT_ADD", "register:40f0:8", ["const:9c9b0c:8", "const:4:8"]]
- 009c9b0c ["CALL", null, ["callee:009c9ee0:8"]]
+ 009c9ca8 ["INT_ADD", "register:40f0:8", ["const:9c9ca8:8", "const:4:8"]]
+ 009c9ca8 ["CALL", null, ["callee:009c9ee0:8"]]
- 009c9b0c bytes 8e000094
+ 009c9ca8 bytes 8e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead8d4480ecc8eb0d50dca02cc3b5953"></a>

### [`009c9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md) → [`009c9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9ee0.md) FUN_009c9ee0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) [`009c9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md) [`009ca19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`009c9bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md) [`009ca054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca054.md) [`009ca338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c9db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md#insn-009c9db8) · [`009c9df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md#insn-009c9df4) · [`009c9e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md#insn-009c9e48)
- 新版 [`009c9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9ee0.md#insn-009c9f54) · [`009c9f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9ee0.md#insn-009c9f90) · [`009c9fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9ee0.md#insn-009c9fe4)

~~~diff
- 009c9db8 ["INT_ADD", "register:40f0:8", ["const:9c9db8:8", "const:4:8"]]
- 009c9db8 ["CALL", null, ["callee:00c57e90:8"]]
+ 009c9f54 ["INT_ADD", "register:40f0:8", ["const:9c9f54:8", "const:4:8"]]
+ 009c9f54 ["CALL", null, ["callee:00c57e90:8"]]
- 009c9db8 bytes 36370a94
+ 009c9f54 bytes cf370a94
- 009c9df4 ["INT_ADD", "register:40f0:8", ["const:9c9df4:8", "const:4:8"]]
- 009c9df4 ["CALL", null, ["callee:0043bba4:8"]]
+ 009c9f90 ["INT_ADD", "register:40f0:8", ["const:9c9f90:8", "const:4:8"]]
+ 009c9f90 ["CALL", null, ["callee:0043bba4:8"]]
- 009c9df4 bytes 5cc7e997
+ 009c9f90 bytes 05c7e997
- 009c9e48 ["INT_ADD", "register:40f0:8", ["const:9c9e48:8", "const:4:8"]]
- 009c9e48 ["CALL", null, ["callee:00c57e90:8"]]
+ 009c9fe4 ["INT_ADD", "register:40f0:8", ["const:9c9fe4:8", "const:4:8"]]
+ 009c9fe4 ["CALL", null, ["callee:00c57e90:8"]]
- 009c9e48 bytes 12370a94
+ 009c9fe4 bytes ab370a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f508705e5241fdaa52495ae6286fb994"></a>

### [`009c9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md) → [`009ca054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca054.md) FUN_009ca054

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) · 呼出先 2件 [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) [`009c9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md)
- 新版 呼出元 1件 [`009c9bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md) · 呼出先 2件 [`009c9bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md) [`009c9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009c9f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md#insn-009c9f04) · [`009c9f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md#insn-009c9f94) · [`009c9fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md#insn-009c9fc8)
- 新版 [`009ca0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca054.md#insn-009ca0a0) · [`009ca130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca054.md#insn-009ca130) · [`009ca164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca054.md#insn-009ca164)

~~~diff
- 009c9f04 ["INT_ADD", "register:40f0:8", ["const:9c9f04:8", "const:4:8"]]
- 009c9f04 ["CALL", null, ["callee:009c9ee0:8"]]
+ 009ca0a0 ["INT_ADD", "register:40f0:8", ["const:9ca0a0:8", "const:4:8"]]
+ 009ca0a0 ["CALL", null, ["callee:009c9ee0:8"]]
- 009c9f04 bytes 90ffff97
+ 009ca0a0 bytes 90ffff97
- 009c9f94 ["INT_ADD", "register:40f0:8", ["const:9c9f94:8", "const:4:8"]]
- 009c9f94 ["CALL", null, ["callee:009c9ee0:8"]]
+ 009ca130 ["INT_ADD", "register:40f0:8", ["const:9ca130:8", "const:4:8"]]
+ 009ca130 ["CALL", null, ["callee:009c9ee0:8"]]
- 009c9f94 bytes 6cffff97
+ 009ca130 bytes 6cffff97
- 009c9fc8 ["INT_ADD", "register:40f0:8", ["const:9c9fc8:8", "const:4:8"]]
- 009c9fc8 ["CALL", null, ["callee:009c9ee0:8"]]
+ 009ca164 ["INT_ADD", "register:40f0:8", ["const:9ca164:8", "const:4:8"]]
+ 009ca164 ["CALL", null, ["callee:009c9ee0:8"]]
- 009c9fc8 bytes 5fffff97
+ 009ca164 bytes 5fffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa6aff2a2aac6a22cb62754201bc619"></a>

### [`009ca19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md) → [`009ca338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md) FUN_009ca338

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) [`009ca19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md) · 呼出先 4件 [`009c9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md) [`009ca19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`009c9bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9bb8.md) [`009ca338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md) · 呼出先 4件 [`009c9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c9/009c9ee0.md) [`009ca338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ca214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md#insn-009ca214) · [`009ca28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md#insn-009ca28c) · [`009ca384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md#insn-009ca384)
- 新版 [`009ca3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md#insn-009ca3b0) · [`009ca428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md#insn-009ca428) · [`009ca520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ca/009ca338.md#insn-009ca520)

~~~diff
- 009ca214 ["INT_ADD", "register:40f0:8", ["const:9ca214:8", "const:4:8"]]
- 009ca214 ["CALL", null, ["callee:009c9ee0:8"]]
+ 009ca3b0 ["INT_ADD", "register:40f0:8", ["const:9ca3b0:8", "const:4:8"]]
+ 009ca3b0 ["CALL", null, ["callee:009c9ee0:8"]]
- 009ca214 bytes ccfeff97
+ 009ca3b0 bytes ccfeff97
- 009ca28c ["INT_ADD", "register:40f0:8", ["const:9ca28c:8", "const:4:8"]]
- 009ca28c ["CALL", null, ["callee:009c9ee0:8"]]
+ 009ca428 ["INT_ADD", "register:40f0:8", ["const:9ca428:8", "const:4:8"]]
+ 009ca428 ["CALL", null, ["callee:009c9ee0:8"]]
- 009ca28c bytes aefeff97
+ 009ca428 bytes aefeff97
- 009ca384 ["INT_ADD", "register:40f0:8", ["const:9ca384:8", "const:4:8"]]
- 009ca384 ["CALL", null, ["callee:009c9ee0:8"]]
+ 009ca520 ["INT_ADD", "register:40f0:8", ["const:9ca520:8", "const:4:8"]]
+ 009ca520 ["CALL", null, ["callee:009c9ee0:8"]]
- 009ca384 bytes 70feff97
+ 009ca520 bytes 70feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e3863657a2b9e3cb0d7f04a27631dd8"></a>

### [`009cc4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc4ac.md) → [`009cc648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009cc648.md) FUN_009cc648

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00802efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802efc.md) · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0087eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00802f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802f3c.md) · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0087eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009cc4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc4ac.md#insn-009cc4e0) · [`009cc4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc4ac.md#insn-009cc4f8) · [`009cc50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc4ac.md#insn-009cc50c)
- 新版 [`009cc67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009cc648.md#insn-009cc67c) · [`009cc694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009cc648.md#insn-009cc694) · [`009cc6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009cc648.md#insn-009cc6a8)

~~~diff
- 009cc4e0 ["INT_ADD", "register:40f0:8", ["const:9cc4e0:8", "const:4:8"]]
- 009cc4e0 ["CALL", null, ["callee:0087eb20:8"]]
+ 009cc67c ["INT_ADD", "register:40f0:8", ["const:9cc67c:8", "const:4:8"]]
+ 009cc67c ["CALL", null, ["callee:0087eb20:8"]]
- 009cc4e0 bytes 80c9fa97
+ 009cc67c bytes 29c9fa97
- 009cc4f8 ["INT_ADD", "register:40f0:8", ["const:9cc4f8:8", "const:4:8"]]
- 009cc4f8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 009cc694 ["INT_ADD", "register:40f0:8", ["const:9cc694:8", "const:4:8"]]
+ 009cc694 ["CALL", null, ["callee:00c53cd0:8"]]
- 009cc4f8 bytes ee1c0a94
+ 009cc694 bytes 8f1d0a94
- 009cc50c ["INT_ADD", "register:40f0:8", ["const:9cc50c:8", "const:4:8"]]
- 009cc50c ["CALL", null, ["callee:00c53d00:8"]]
+ 009cc6a8 ["INT_ADD", "register:40f0:8", ["const:9cc6a8:8", "const:4:8"]]
+ 009cc6a8 ["CALL", null, ["callee:00c53d00:8"]]
- 009cc50c bytes f51c0a94
+ 009cc6a8 bytes 961d0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584840aa5ccf2277a2d23c94e8ffb9f4"></a>

### [`009d3408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3408.md) → [`009d35a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d35a4.md) FUN_009d35a4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d3470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3408.md#insn-009d3470) · [`009d34a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3408.md#insn-009d34a8)
- 新版 [`009d360c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d35a4.md#insn-009d360c) · [`009d3644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d35a4.md#insn-009d3644)

~~~diff
- 009d3470 ["INT_ADD", "register:40f0:8", ["const:9d3470:8", "const:4:8"]]
- 009d3470 ["CALL", null, ["callee:00c57e90:8"]]
+ 009d360c ["INT_ADD", "register:40f0:8", ["const:9d360c:8", "const:4:8"]]
+ 009d360c ["CALL", null, ["callee:00c57e90:8"]]
- 009d3470 bytes 88110a94
+ 009d360c bytes 21120a94
- 009d34a8 ["INT_ADD", "register:40f0:8", ["const:9d34a8:8", "const:4:8"]]
- 009d34a8 ["CALL", null, ["callee:0043bba4:8"]]
+ 009d3644 ["INT_ADD", "register:40f0:8", ["const:9d3644:8", "const:4:8"]]
+ 009d3644 ["CALL", null, ["callee:0043bba4:8"]]
- 009d34a8 bytes afa1e997
+ 009d3644 bytes 58a1e997
~~~


<a id="compare-d3ea5331ccd9676dcfee75850405c647"></a>

### [`009d34d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d34d0.md) → [`009d366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d366c.md) FUN_009d366c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d3538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d34d0.md#insn-009d3538) · [`009d3570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d34d0.md#insn-009d3570)
- 新版 [`009d36d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d366c.md#insn-009d36d4) · [`009d370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d366c.md#insn-009d370c)

~~~diff
- 009d3538 ["INT_ADD", "register:40f0:8", ["const:9d3538:8", "const:4:8"]]
- 009d3538 ["CALL", null, ["callee:00c57e90:8"]]
+ 009d36d4 ["INT_ADD", "register:40f0:8", ["const:9d36d4:8", "const:4:8"]]
+ 009d36d4 ["CALL", null, ["callee:00c57e90:8"]]
- 009d3538 bytes 56110a94
+ 009d36d4 bytes ef110a94
- 009d3570 ["INT_ADD", "register:40f0:8", ["const:9d3570:8", "const:4:8"]]
- 009d3570 ["CALL", null, ["callee:0043bba4:8"]]
+ 009d370c ["INT_ADD", "register:40f0:8", ["const:9d370c:8", "const:4:8"]]
+ 009d370c ["CALL", null, ["callee:0043bba4:8"]]
- 009d3570 bytes 7da1e997
+ 009d370c bytes 26a1e997
~~~


<a id="compare-9537b69d50ff03eeacbd6e8cc62856b5"></a>

### [`009d3598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3598.md) → [`009d3734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3734.md) FUN_009d3734

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d35dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3598.md#insn-009d35dc)
- 新版 [`009d3778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3734.md#insn-009d3778)

~~~diff
- 009d35dc ["INT_ADD", "register:40f0:8", ["const:9d35dc:8", "const:4:8"]]
- 009d35dc ["CALL", null, ["callee:00c58050:8"]]
+ 009d3778 ["INT_ADD", "register:40f0:8", ["const:9d3778:8", "const:4:8"]]
+ 009d3778 ["CALL", null, ["callee:00c58050:8"]]
- 009d35dc bytes 9d110a94
+ 009d3778 bytes 36120a94
~~~


<a id="compare-323562bb72dbe620b3870fb463458d3b"></a>

### [`009d3600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3600.md) → [`009d379c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d379c.md) FUN_009d379c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d3668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3600.md#insn-009d3668) · [`009d36a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3600.md#insn-009d36a4)
- 新版 [`009d3804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d379c.md#insn-009d3804) · [`009d3840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d379c.md#insn-009d3840)

~~~diff
- 009d3668 ["INT_ADD", "register:40f0:8", ["const:9d3668:8", "const:4:8"]]
- 009d3668 ["CALL", null, ["callee:00c57e90:8"]]
+ 009d3804 ["INT_ADD", "register:40f0:8", ["const:9d3804:8", "const:4:8"]]
+ 009d3804 ["CALL", null, ["callee:00c57e90:8"]]
- 009d3668 bytes 0a110a94
+ 009d3804 bytes a3110a94
- 009d36a4 ["INT_ADD", "register:40f0:8", ["const:9d36a4:8", "const:4:8"]]
- 009d36a4 ["CALL", null, ["callee:0043bba4:8"]]
+ 009d3840 ["INT_ADD", "register:40f0:8", ["const:9d3840:8", "const:4:8"]]
+ 009d3840 ["CALL", null, ["callee:0043bba4:8"]]
- 009d36a4 bytes 30a1e997
+ 009d3840 bytes d9a0e997
~~~


<a id="compare-5ed70c00e9a34adfad98ae948a700ca1"></a>

### [`009d36cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d36cc.md) → [`009d3868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3868.md) FUN_009d3868

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d3778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d36cc.md#insn-009d3778) · [`009d3780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d36cc.md#insn-009d3780)
- 新版 [`009d3914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3868.md#insn-009d3914) · [`009d391c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3868.md#insn-009d391c)

~~~diff
- 009d3778 ["INT_ADD", "register:40f0:8", ["const:9d3778:8", "const:4:8"]]
- 009d3778 ["CALL", null, ["callee:00494610:8"]]
+ 009d3914 ["INT_ADD", "register:40f0:8", ["const:9d3914:8", "const:4:8"]]
+ 009d3914 ["CALL", null, ["callee:00494610:8"]]
- 009d3778 bytes 9603eb97
+ 009d3914 bytes 3f03eb97
- 009d3780 ["INT_ADD", "register:40f0:8", ["const:9d3780:8", "const:4:8"]]
- 009d3780 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009d391c ["INT_ADD", "register:40f0:8", ["const:9d391c:8", "const:4:8"]]
+ 009d391c ["CALL", null, ["callee:00c57eb0:8"]]
- 009d3780 bytes cc100a94
+ 009d391c bytes 65110a94
~~~


<a id="compare-1ab54bec1f0ec18fd4c7c44ebb40fea6"></a>

### [`009d3794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3794.md) → [`009d3930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3930.md) FUN_009d3930

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 8件 [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00a34020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34020.md) [`00a34558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34558.md) [`00a354d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a354d8.md) [`00a354e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a354e8.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 8件 [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`00a34218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34218.md) [`00a34750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34750.md) [`00a356d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356d0.md) [`00a356e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d37d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3794.md#insn-009d37d8) · [`009d37e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3794.md#insn-009d37e0) · [`009d37e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3794.md#insn-009d37e4)
- 新版 [`009d3974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3930.md#insn-009d3974) · [`009d397c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3930.md#insn-009d397c) · [`009d3980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3930.md#insn-009d3980)

~~~diff
- 009d37d8 ["INT_ADD", "register:40f0:8", ["const:9d37d8:8", "const:4:8"]]
- 009d37d8 ["CALL", null, ["callee:00800378:8"]]
+ 009d3974 ["INT_ADD", "register:40f0:8", ["const:9d3974:8", "const:4:8"]]
+ 009d3974 ["CALL", null, ["callee:00800378:8"]]
- 009d37d8 bytes d8b2f897
+ 009d3974 bytes 81b2f897
- 009d37e0 ["INT_ADD", "register:40f0:8", ["const:9d37e0:8", "const:4:8"]]
- 009d37e0 ["CALL", null, ["callee:00a35b98:8"]]
+ 009d397c ["INT_ADD", "register:40f0:8", ["const:9d397c:8", "const:4:8"]]
+ 009d397c ["CALL", null, ["callee:00a35b98:8"]]
- 009d37e0 bytes 70880194
+ 009d397c bytes 87880194
- 009d37e4 ["INT_ADD", "register:40f0:8", ["const:9d37e4:8", "const:4:8"]]
- 009d37e4 ["CALL", null, ["callee:00a38b6c:8"]]
+ 009d3980 ["INT_ADD", "register:40f0:8", ["const:9d3980:8", "const:4:8"]]
+ 009d3980 ["CALL", null, ["callee:00a38b6c:8"]]
- 009d37e4 bytes 64940194
+ 009d3980 bytes 7b940194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-603d8a77085bf88f498879d73969f917"></a>

### [`009d590c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d590c.md) → [`009d5aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5aa8.md) FUN_009d5aa8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 22件 [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006b37cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 22件 [`0066d6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d6a0.md) [`00677a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/00677a40.md) [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) [`006b380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b380c.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d5938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d590c.md#insn-009d5938) · [`009d5950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d590c.md#insn-009d5950) · [`009d5958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d590c.md#insn-009d5958)
- 新版 [`009d5ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5aa8.md#insn-009d5ad4) · [`009d5aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5aa8.md#insn-009d5aec) · [`009d5af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5aa8.md#insn-009d5af4)

~~~diff
- 009d5938 ["INT_ADD", "register:40f0:8", ["const:9d5938:8", "const:4:8"]]
- 009d5938 ["CALL", null, ["callee:00c53d00:8"]]
+ 009d5ad4 ["INT_ADD", "register:40f0:8", ["const:9d5ad4:8", "const:4:8"]]
+ 009d5ad4 ["CALL", null, ["callee:00c53d00:8"]]
- 009d5938 bytes eaf70994
+ 009d5ad4 bytes 8bf80994
- 009d5950 ["COPY", "register:0:8", ["register:4040:8"]]
- 009d5950 ["INT_ADD", "register:40f0:8", ["const:9d5950:8", "const:4:8"]]
- 009d5950 ["CALLIND", null, ["register:0:8"]]
+ 009d5aec ["COPY", "register:0:8", ["register:4040:8"]]
+ 009d5aec ["INT_ADD", "register:40f0:8", ["const:9d5aec:8", "const:4:8"]]
+ 009d5aec ["CALLIND", null, ["register:0:8"]]
- 009d5950 bytes 00013fd6
+ 009d5aec bytes 00013fd6
- 009d5958 ["INT_ADD", "register:40f0:8", ["const:9d5958:8", "const:4:8"]]
- 009d5958 ["CALL", null, ["callee:00c57e80:8"]]
+ 009d5af4 ["INT_ADD", "register:40f0:8", ["const:9d5af4:8", "const:4:8"]]
+ 009d5af4 ["CALL", null, ["callee:00c57e80:8"]]
- 009d5958 bytes 4a080a94
+ 009d5af4 bytes e3080a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e03e18f4256426790e09476505569fde"></a>

### [`009d7890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md) → [`009d7a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7a2c.md) FUN_009d7a2c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`009dcf54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcf54.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009dd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd0f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d7958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md#insn-009d7958) · [`009d79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md#insn-009d79a4) · [`009d79b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md#insn-009d79b8)
- 新版 [`009d7af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7a2c.md#insn-009d7af4) · [`009d7b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7a2c.md#insn-009d7b40) · [`009d7b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7a2c.md#insn-009d7b54)

~~~diff
- 009d7958 ["INT_ADD", "register:40f0:8", ["const:9d7958:8", "const:4:8"]]
- 009d7958 ["CALL", null, ["callee:00c57e90:8"]]
+ 009d7af4 ["INT_ADD", "register:40f0:8", ["const:9d7af4:8", "const:4:8"]]
+ 009d7af4 ["CALL", null, ["callee:00c57e90:8"]]
- 009d7958 bytes 4e000a94
+ 009d7af4 bytes e7000a94
- 009d79a4 ["INT_ADD", "register:40f0:8", ["const:9d79a4:8", "const:4:8"]]
- 009d79a4 ["CALL", null, ["callee:00c58000:8"]]
+ 009d7b40 ["INT_ADD", "register:40f0:8", ["const:9d7b40:8", "const:4:8"]]
+ 009d7b40 ["CALL", null, ["callee:00c58000:8"]]
- 009d79a4 bytes 97000a94
+ 009d7b40 bytes 30010a94
- 009d79b8 ["INT_ADD", "register:40f0:8", ["const:9d79b8:8", "const:4:8"]]
- 009d79b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009d7b54 ["INT_ADD", "register:40f0:8", ["const:9d7b54:8", "const:4:8"]]
+ 009d7b54 ["CALL", null, ["callee:00c57eb0:8"]]
- 009d79b8 bytes 3e000a94
+ 009d7b54 bytes d7000a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c323160e5335d24cda7bc36255ae00a2"></a>

### [`009d93a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d93a8.md) → [`009d9544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9544.md) FUN_009d9544

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`007f1e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e78.md) [`0080f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080f0e8.md) [`0080fb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fb8c.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1eb8.md) [`0080f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080f128.md) [`0080fbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fbcc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d942c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d93a8.md#insn-009d942c) · [`009d9484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d93a8.md#insn-009d9484) · [`009d949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d93a8.md#insn-009d949c)
- 新版 [`009d95c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9544.md#insn-009d95c8) · [`009d9620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9544.md#insn-009d9620) · [`009d9638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9544.md#insn-009d9638)

~~~diff
- 009d942c ["INT_ADD", "register:40f0:8", ["const:9d942c:8", "const:4:8"]]
- 009d942c ["CALL", null, ["callee:00c57e90:8"]]
+ 009d95c8 ["INT_ADD", "register:40f0:8", ["const:9d95c8:8", "const:4:8"]]
+ 009d95c8 ["CALL", null, ["callee:00c57e90:8"]]
- 009d942c bytes 99f90994
+ 009d95c8 bytes 32fa0994
- 009d9484 ["INT_ADD", "register:40f0:8", ["const:9d9484:8", "const:4:8"]]
- 009d9484 ["CALL", null, ["callee:0043bba4:8"]]
+ 009d9620 ["INT_ADD", "register:40f0:8", ["const:9d9620:8", "const:4:8"]]
+ 009d9620 ["CALL", null, ["callee:0043bba4:8"]]
- 009d9484 bytes b889e997
+ 009d9620 bytes 6189e997
- 009d949c ["INT_ADD", "register:40f0:8", ["const:9d949c:8", "const:4:8"]]
- 009d949c ["CALL", null, ["callee:0080f128:8"]]
+ 009d9638 ["INT_ADD", "register:40f0:8", ["const:9d9638:8", "const:4:8"]]
+ 009d9638 ["CALL", null, ["callee:0080f128:8"]]
- 009d949c bytes 13d7f897
+ 009d9638 bytes bcd6f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd1d3b4113e836db38962086ef426176"></a>

### [`009dbbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbbbc.md) → [`009dbd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbd58.md) FUN_009dbd58

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 2件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dbc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbbbc.md#insn-009dbc0c)
- 新版 [`009dbda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbd58.md#insn-009dbda8)

~~~diff
- 009dbc0c ["INT_ADD", "register:40f0:8", ["const:9dbc0c:8", "const:4:8"]]
- 009dbc0c ["CALL", null, ["callee:004700b4:8"]]
+ 009dbda8 ["INT_ADD", "register:40f0:8", ["const:9dbda8:8", "const:4:8"]]
+ 009dbda8 ["CALL", null, ["callee:004700b4:8"]]
- 009dbc0c bytes 1a51ea97
+ 009dbda8 bytes c350ea97
~~~


<a id="compare-0c742841d5e6c6b04433f880c4861f41"></a>

### [`009dbc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbc34.md) → [`009dbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbdd0.md) FUN_009dbdd0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 2件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dbc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbc34.md#insn-009dbc84)
- 新版 [`009dbe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbdd0.md#insn-009dbe20)

~~~diff
- 009dbc84 ["INT_ADD", "register:40f0:8", ["const:9dbc84:8", "const:4:8"]]
- 009dbc84 ["CALL", null, ["callee:004700b4:8"]]
+ 009dbe20 ["INT_ADD", "register:40f0:8", ["const:9dbe20:8", "const:4:8"]]
+ 009dbe20 ["CALL", null, ["callee:004700b4:8"]]
- 009dbc84 bytes fc50ea97
+ 009dbe20 bytes a550ea97
~~~


<a id="compare-efa1e98d3b5ee5c45faaa245f6741709"></a>

### [`009dbcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbcac.md) → [`009dbe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbe48.md) FUN_009dbe48

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 2件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dbcfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbcac.md#insn-009dbcfc)
- 新版 [`009dbe98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbe48.md#insn-009dbe98)

~~~diff
- 009dbcfc ["INT_ADD", "register:40f0:8", ["const:9dbcfc:8", "const:4:8"]]
- 009dbcfc ["CALL", null, ["callee:004700b4:8"]]
+ 009dbe98 ["INT_ADD", "register:40f0:8", ["const:9dbe98:8", "const:4:8"]]
+ 009dbe98 ["CALL", null, ["callee:004700b4:8"]]
- 009dbcfc bytes de50ea97
+ 009dbe98 bytes 8750ea97
~~~


<a id="compare-a016e5b417337c1eefce8765989d76e7"></a>

### [`009dbd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbd24.md) → [`009dbec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbec0.md) FUN_009dbec0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 2件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dbd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbd24.md#insn-009dbd74)
- 新版 [`009dbf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbec0.md#insn-009dbf10)

~~~diff
- 009dbd74 ["INT_ADD", "register:40f0:8", ["const:9dbd74:8", "const:4:8"]]
- 009dbd74 ["CALL", null, ["callee:004700b4:8"]]
+ 009dbf10 ["INT_ADD", "register:40f0:8", ["const:9dbf10:8", "const:4:8"]]
+ 009dbf10 ["CALL", null, ["callee:004700b4:8"]]
- 009dbd74 bytes c050ea97
+ 009dbf10 bytes 6950ea97
~~~


<a id="compare-53690660f30c5132cb73cc05817adfc9"></a>

### [`009dbd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbd9c.md) → [`009dbf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbf38.md) FUN_009dbf38

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 2件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dbdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbd9c.md#insn-009dbdec)
- 新版 [`009dbf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbf38.md#insn-009dbf88)

~~~diff
- 009dbdec ["INT_ADD", "register:40f0:8", ["const:9dbdec:8", "const:4:8"]]
- 009dbdec ["CALL", null, ["callee:004700b4:8"]]
+ 009dbf88 ["INT_ADD", "register:40f0:8", ["const:9dbf88:8", "const:4:8"]]
+ 009dbf88 ["CALL", null, ["callee:004700b4:8"]]
- 009dbdec bytes a250ea97
+ 009dbf88 bytes 4b50ea97
~~~


<a id="compare-cb4ac5116f4e0a6853b2d28d67b99a58"></a>

### [`009dbe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbe14.md) → [`009dbfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbfb0.md) FUN_009dbfb0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 2件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dbe64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbe14.md#insn-009dbe64)
- 新版 [`009dc000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbfb0.md#insn-009dc000)

~~~diff
- 009dbe64 ["INT_ADD", "register:40f0:8", ["const:9dbe64:8", "const:4:8"]]
- 009dbe64 ["CALL", null, ["callee:004700b4:8"]]
+ 009dc000 ["INT_ADD", "register:40f0:8", ["const:9dc000:8", "const:4:8"]]
+ 009dc000 ["CALL", null, ["callee:004700b4:8"]]
- 009dbe64 bytes 8450ea97
+ 009dc000 bytes 2d50ea97
~~~


<a id="compare-40a570fa61de4e55d69c2f7d950ece91"></a>

### [`009dbe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbe8c.md) → [`009dc028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc028.md) FUN_009dc028

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 2件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dbedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbe8c.md#insn-009dbedc)
- 新版 [`009dc078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc028.md#insn-009dc078)

~~~diff
- 009dbedc ["INT_ADD", "register:40f0:8", ["const:9dbedc:8", "const:4:8"]]
- 009dbedc ["CALL", null, ["callee:004700b4:8"]]
+ 009dc078 ["INT_ADD", "register:40f0:8", ["const:9dc078:8", "const:4:8"]]
+ 009dc078 ["CALL", null, ["callee:004700b4:8"]]
- 009dbedc bytes 6650ea97
+ 009dc078 bytes 0f50ea97
~~~


<a id="compare-0ae611d706ea8596ecf08cb710f15291"></a>

### [`009dcca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcca4.md) → [`009dce40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dce40.md) FUN_009dce40

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 80件 [`005fa7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa7e4.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0060eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`006122a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00612/006122a4.md) · 呼出先 2件 [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md) [`0085b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b26c.md)
- 新版 呼出元 80件 [`005fa824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fa/005fa824.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006122e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00612/006122e4.md) · 呼出先 2件 [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dcccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcca4.md#insn-009dcccc) · [`009dcce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcca4.md#insn-009dcce0) · [`009dccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcca4.md#insn-009dccf0)
- 新版 [`009dce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dce40.md#insn-009dce68) · [`009dce7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dce40.md#insn-009dce7c) · [`009dce8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dce40.md#insn-009dce8c)

~~~diff
- 009dcccc ["INT_ADD", "register:40f0:8", ["const:9dcccc:8", "const:4:8"]]
- 009dcccc ["CALL", null, ["callee:0085b2a4:8"]]
+ 009dce68 ["INT_ADD", "register:40f0:8", ["const:9dce68:8", "const:4:8"]]
+ 009dce68 ["CALL", null, ["callee:0085b2a4:8"]]
- 009dcccc bytes 66f9f997
+ 009dce68 bytes 0ff9f997
- 009dcce0 ["INT_ADD", "register:40f0:8", ["const:9dcce0:8", "const:4:8"]]
- 009dcce0 ["CALL", null, ["callee:0085b2a4:8"]]
+ 009dce7c ["INT_ADD", "register:40f0:8", ["const:9dce7c:8", "const:4:8"]]
+ 009dce7c ["CALL", null, ["callee:0085b2a4:8"]]
- 009dcce0 bytes 61f9f997
+ 009dce7c bytes 0af9f997
- 009dccf0 ["INT_ADD", "register:40f0:8", ["const:9dccf0:8", "const:4:8"]]
- 009dccf0 ["CALL", null, ["callee:0085b2ac:8"]]
+ 009dce8c ["INT_ADD", "register:40f0:8", ["const:9dce8c:8", "const:4:8"]]
+ 009dce8c ["CALL", null, ["callee:0085b2ac:8"]]
- 009dccf0 bytes 5ff9f997
+ 009dce8c bytes 08f9f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d9ca67eb77bfb4bea519b5f8dddb798"></a>

### [`009dcd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcd30.md) → [`009dcecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcecc.md) FUN_009dcecc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 21件 [`0063ac74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063ac74.md) [`0063b50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b50c.md) [`0063bc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063bc58.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006c0ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0ef8.md) · 呼出先 4件 [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md) [`0085b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b26c.md) [`0085b274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b274.md) [`0085b27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b27c.md)
- 新版 呼出元 21件 [`0063acb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063acb4.md) [`0063b54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b54c.md) [`0063bc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063bc98.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006c0f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0f38.md) · 呼出先 4件 [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md) [`0085b2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2b4.md) [`0085b2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dcd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcd30.md#insn-009dcd58) · [`009dcd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcd30.md#insn-009dcd6c) · [`009dcd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcd30.md#insn-009dcd7c)
- 新版 [`009dcef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcecc.md#insn-009dcef4) · [`009dcf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcecc.md#insn-009dcf08) · [`009dcf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcecc.md#insn-009dcf18)

~~~diff
- 009dcd58 ["INT_ADD", "register:40f0:8", ["const:9dcd58:8", "const:4:8"]]
- 009dcd58 ["CALL", null, ["callee:0085b2a4:8"]]
+ 009dcef4 ["INT_ADD", "register:40f0:8", ["const:9dcef4:8", "const:4:8"]]
+ 009dcef4 ["CALL", null, ["callee:0085b2a4:8"]]
- 009dcd58 bytes 43f9f997
+ 009dcef4 bytes ecf8f997
- 009dcd6c ["INT_ADD", "register:40f0:8", ["const:9dcd6c:8", "const:4:8"]]
- 009dcd6c ["CALL", null, ["callee:0085b2a4:8"]]
+ 009dcf08 ["INT_ADD", "register:40f0:8", ["const:9dcf08:8", "const:4:8"]]
+ 009dcf08 ["CALL", null, ["callee:0085b2a4:8"]]
- 009dcd6c bytes 3ef9f997
+ 009dcf08 bytes e7f8f997
- 009dcd7c ["INT_ADD", "register:40f0:8", ["const:9dcd7c:8", "const:4:8"]]
- 009dcd7c ["CALL", null, ["callee:0085b2ac:8"]]
+ 009dcf18 ["INT_ADD", "register:40f0:8", ["const:9dcf18:8", "const:4:8"]]
+ 009dcf18 ["CALL", null, ["callee:0085b2ac:8"]]
- 009dcd7c bytes 3cf9f997
+ 009dcf18 bytes e5f8f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5876eb40f94aeff12357d7237b1a596"></a>

### [`009ddf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dd/009ddf4c.md) → [`009de0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de0e8.md) FUN_009de0e8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`009de4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de4d4.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`009de670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de670.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ddfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dd/009ddf4c.md#insn-009ddfe0) · [`009de01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dd/009ddf4c.md#insn-009de01c) · [`009de060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dd/009ddf4c.md#insn-009de060)
- 新版 [`009de17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de0e8.md#insn-009de17c) · [`009de1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de0e8.md#insn-009de1b8) · [`009de1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de0e8.md#insn-009de1fc)

~~~diff
- 009ddfe0 ["INT_ADD", "register:40f0:8", ["const:9ddfe0:8", "const:4:8"]]
- 009ddfe0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009de17c ["INT_ADD", "register:40f0:8", ["const:9de17c:8", "const:4:8"]]
+ 009de17c ["CALL", null, ["callee:00c57e90:8"]]
- 009ddfe0 bytes ace60994
+ 009de17c bytes 45e70994
- 009de01c ["INT_ADD", "register:40f0:8", ["const:9de01c:8", "const:4:8"]]
- 009de01c ["CALL", null, ["callee:0043bba4:8"]]
+ 009de1b8 ["INT_ADD", "register:40f0:8", ["const:9de1b8:8", "const:4:8"]]
+ 009de1b8 ["CALL", null, ["callee:0043bba4:8"]]
- 009de01c bytes d276e997
+ 009de1b8 bytes 7b76e997
- 009de060 ["INT_ADD", "register:40f0:8", ["const:9de060:8", "const:4:8"]]
- 009de060 ["CALL", null, ["callee:00c58450:8"]]
+ 009de1fc ["INT_ADD", "register:40f0:8", ["const:9de1fc:8", "const:4:8"]]
+ 009de1fc ["CALL", null, ["callee:00c58450:8"]]
- 009de060 bytes fce70994
+ 009de1fc bytes 95e80994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bb754a002ff9715fb7121abdb6eb501"></a>

### [`009de4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de4d4.md) → [`009de670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de670.md) FUN_009de670

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007dd324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd324.md) · 呼出先 4件 [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`009ddf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dd/009ddf4c.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`007dd364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd364.md) · 呼出先 4件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`009de0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de0e8.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009de4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de4d4.md#insn-009de4ec) · [`009de4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de4d4.md#insn-009de4f4) · [`009de508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de4d4.md#insn-009de508)
- 新版 [`009de688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de670.md#insn-009de688) · [`009de690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de670.md#insn-009de690) · [`009de6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de670.md#insn-009de6a4)

~~~diff
- 009de4ec ["INT_ADD", "register:40f0:8", ["const:9de4ec:8", "const:4:8"]]
- 009de4ec ["CALL", null, ["callee:00802b58:8"]]
+ 009de688 ["INT_ADD", "register:40f0:8", ["const:9de688:8", "const:4:8"]]
+ 009de688 ["CALL", null, ["callee:00802b58:8"]]
- 009de4ec bytes 8b91f897
+ 009de688 bytes 3491f897
- 009de4f4 ["INT_ADD", "register:40f0:8", ["const:9de4f4:8", "const:4:8"]]
- 009de4f4 ["CALL", null, ["callee:00802ca8:8"]]
+ 009de690 ["INT_ADD", "register:40f0:8", ["const:9de690:8", "const:4:8"]]
+ 009de690 ["CALL", null, ["callee:00802ca8:8"]]
- 009de4f4 bytes dd91f897
+ 009de690 bytes 8691f897
- 009de508 ["INT_ADD", "register:40f0:8", ["const:9de508:8", "const:4:8"]]
- 009de508 ["CALL", null, ["callee:009de0e8:8"]]
+ 009de6a4 ["INT_ADD", "register:40f0:8", ["const:9de6a4:8", "const:4:8"]]
+ 009de6a4 ["CALL", null, ["callee:009de0e8:8"]]
- 009de508 bytes 91feff97
+ 009de6a4 bytes 91feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53d8a8c9ff1378c350e2ceabb6d719d"></a>

### [`009de55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de55c.md) → [`009de6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de6f8.md) FUN_009de6f8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`006bed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bed1c.md) · 呼出先 3件 [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`006bed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) · 呼出先 3件 [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009de57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de55c.md#insn-009de57c) · [`009de5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de55c.md#insn-009de5d0) · [`009de5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de55c.md#insn-009de5d4)
- 新版 [`009de718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de6f8.md#insn-009de718) · [`009de76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de6f8.md#insn-009de76c) · [`009de770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de6f8.md#insn-009de770)

~~~diff
- 009de57c ["INT_ADD", "register:40f0:8", ["const:9de57c:8", "const:4:8"]]
- 009de57c ["CALL", null, ["callee:008514f8:8"]]
+ 009de718 ["INT_ADD", "register:40f0:8", ["const:9de718:8", "const:4:8"]]
+ 009de718 ["CALL", null, ["callee:008514f8:8"]]
- 009de57c bytes cfcbf997
+ 009de718 bytes 78cbf997
- 009de5d0 ["INT_ADD", "register:40f0:8", ["const:9de5d0:8", "const:4:8"]]
- 009de5d0 ["CALL", null, ["callee:005e8198:8"]]
+ 009de76c ["INT_ADD", "register:40f0:8", ["const:9de76c:8", "const:4:8"]]
+ 009de76c ["CALL", null, ["callee:005e8198:8"]]
- 009de5d0 bytes e226f097
+ 009de76c bytes 8b26f097
- 009de5d4 ["INT_ADD", "register:40f0:8", ["const:9de5d4:8", "const:4:8"]]
- 009de5d4 ["CALL", null, ["callee:008514f8:8"]]
+ 009de770 ["INT_ADD", "register:40f0:8", ["const:9de770:8", "const:4:8"]]
+ 009de770 ["CALL", null, ["callee:008514f8:8"]]
- 009de5d4 bytes b9cbf997
+ 009de770 bytes 62cbf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2adfcaa5a6efeb2e9e6185a667f1a541"></a>

### [`009de668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md) → [`009de804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de804.md) FUN_009de804

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2de6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2d/00a2de6c.md) · 呼出先 2件 [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md)
- 新版 呼出元 1件 [`00a2e064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e064.md) · 呼出先 2件 [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009de680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md#insn-009de680) · [`009de68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md#insn-009de68c) · [`009de698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md#insn-009de698)
- 新版 [`009de81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de804.md#insn-009de81c) · [`009de828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de804.md#insn-009de828) · [`009de834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de804.md#insn-009de834)

~~~diff
- 009de680 ["INT_ADD", "register:40f0:8", ["const:9de680:8", "const:4:8"]]
- 009de680 ["CALL", null, ["callee:004801d8:8"]]
+ 009de81c ["INT_ADD", "register:40f0:8", ["const:9de81c:8", "const:4:8"]]
+ 009de81c ["CALL", null, ["callee:004801d8:8"]]
- 009de680 bytes c686ea97
+ 009de81c bytes 6f86ea97
- 009de68c ["INT_ADD", "register:40f0:8", ["const:9de68c:8", "const:4:8"]]
- 009de68c ["CALL", null, ["callee:004801d8:8"]]
+ 009de828 ["INT_ADD", "register:40f0:8", ["const:9de828:8", "const:4:8"]]
+ 009de828 ["CALL", null, ["callee:004801d8:8"]]
- 009de68c bytes c386ea97
+ 009de828 bytes 6c86ea97
- 009de698 ["INT_ADD", "register:40f0:8", ["const:9de698:8", "const:4:8"]]
- 009de698 ["CALL", null, ["callee:004802f8:8"]]
+ 009de834 ["INT_ADD", "register:40f0:8", ["const:9de834:8", "const:4:8"]]
+ 009de834 ["CALL", null, ["callee:004802f8:8"]]
- 009de698 bytes 0887ea97
+ 009de834 bytes b186ea97
~~~


<a id="compare-da966b1b7d6327c630037400355e3691"></a>

### [`009de6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de6b0.md) → [`009de84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de84c.md) FUN_009de84c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e370.md) · 呼出先 2件 [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md)
- 新版 呼出元 1件 [`00a2e568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e568.md) · 呼出先 2件 [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009de6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de6b0.md#insn-009de6d0) · [`009de6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de6b0.md#insn-009de6dc)
- 新版 [`009de86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de84c.md#insn-009de86c) · [`009de878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de84c.md#insn-009de878)

~~~diff
- 009de6d0 ["INT_ADD", "register:40f0:8", ["const:9de6d0:8", "const:4:8"]]
- 009de6d0 ["CALL", null, ["callee:00480be8:8"]]
+ 009de86c ["INT_ADD", "register:40f0:8", ["const:9de86c:8", "const:4:8"]]
+ 009de86c ["CALL", null, ["callee:00480be8:8"]]
- 009de6d0 bytes 3689ea97
+ 009de86c bytes df88ea97
- 009de6dc ["INT_ADD", "register:40f0:8", ["const:9de6dc:8", "const:4:8"]]
- 009de6dc ["CALL", null, ["callee:00480be8:8"]]
+ 009de878 ["INT_ADD", "register:40f0:8", ["const:9de878:8", "const:4:8"]]
+ 009de878 ["CALL", null, ["callee:00480be8:8"]]
- 009de6dc bytes 3389ea97
+ 009de878 bytes dc88ea97
~~~


<a id="compare-7eee0a6c51d9ba05b8b806c35214a8fd"></a>

### [`009dea84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009dea84.md) → [`009dec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009dec20.md) FUN_009dec20

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009dfc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc70.md) · 呼出先 11件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`007f9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e44.md)
- 新版 呼出元 1件 [`009dfe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md) · 呼出先 11件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`007f9e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009deac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009dea84.md#insn-009deac8) · [`009deb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009dea84.md#insn-009deb24) · [`009deb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009dea84.md#insn-009deb34)
- 新版 [`009dec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009dec20.md#insn-009dec64) · [`009decc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009dec20.md#insn-009decc0) · [`009decd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009dec20.md#insn-009decd0)

~~~diff
- 009deac8 ["INT_ADD", "register:40f0:8", ["const:9deac8:8", "const:4:8"]]
- 009deac8 ["CALL", null, ["callee:00480118:8"]]
+ 009dec64 ["INT_ADD", "register:40f0:8", ["const:9dec64:8", "const:4:8"]]
+ 009dec64 ["CALL", null, ["callee:00480118:8"]]
- 009deac8 bytes 8485ea97
+ 009dec64 bytes 2d85ea97
- 009deb24 ["INT_ADD", "register:40f0:8", ["const:9deb24:8", "const:4:8"]]
- 009deb24 ["CALL", null, ["callee:00480178:8"]]
+ 009decc0 ["INT_ADD", "register:40f0:8", ["const:9decc0:8", "const:4:8"]]
+ 009decc0 ["CALL", null, ["callee:00480178:8"]]
- 009deb24 bytes 8585ea97
+ 009decc0 bytes 2e85ea97
- 009deb34 ["INT_ADD", "register:40f0:8", ["const:9deb34:8", "const:4:8"]]
- 009deb34 ["CALL", null, ["callee:00480118:8"]]
+ 009decd0 ["INT_ADD", "register:40f0:8", ["const:9decd0:8", "const:4:8"]]
+ 009decd0 ["CALL", null, ["callee:00480118:8"]]
- 009deb34 bytes 6985ea97
+ 009decd0 bytes 1285ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ba8f067f06c5431e986914d34ac5d0"></a>

### [`009df1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df1d4.md) → [`009df370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df370.md) FUN_009df370

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009dff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dff34.md) · 呼出先 2件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md)
- 新版 呼出元 1件 [`009e00d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e00d0.md) · 呼出先 2件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009df214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df1d4.md#insn-009df214) · [`009df22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df1d4.md#insn-009df22c) · [`009df238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df1d4.md#insn-009df238)
- 新版 [`009df3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df370.md#insn-009df3b0) · [`009df3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df370.md#insn-009df3c8) · [`009df3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df370.md#insn-009df3d4)

~~~diff
- 009df214 ["INT_ADD", "register:40f0:8", ["const:9df214:8", "const:4:8"]]
- 009df214 ["CALL", null, ["callee:00480b38:8"]]
+ 009df3b0 ["INT_ADD", "register:40f0:8", ["const:9df3b0:8", "const:4:8"]]
+ 009df3b0 ["CALL", null, ["callee:00480b38:8"]]
- 009df214 bytes 3986ea97
+ 009df3b0 bytes e285ea97
- 009df22c ["INT_ADD", "register:40f0:8", ["const:9df22c:8", "const:4:8"]]
- 009df22c ["CALL", null, ["callee:00480b90:8"]]
+ 009df3c8 ["INT_ADD", "register:40f0:8", ["const:9df3c8:8", "const:4:8"]]
+ 009df3c8 ["CALL", null, ["callee:00480b90:8"]]
- 009df22c bytes 4986ea97
+ 009df3c8 bytes f285ea97
- 009df238 ["INT_ADD", "register:40f0:8", ["const:9df238:8", "const:4:8"]]
- 009df238 ["CALL", null, ["callee:00480b38:8"]]
+ 009df3d4 ["INT_ADD", "register:40f0:8", ["const:9df3d4:8", "const:4:8"]]
+ 009df3d4 ["CALL", null, ["callee:00480b38:8"]]
- 009df238 bytes 3086ea97
+ 009df3d4 bytes d985ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9606c80e62fa0a94f94b4c12e79ac979"></a>

### [`009df4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df4cc.md) → [`009df668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df668.md) FUN_009df668

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009df750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df750.md) · 呼出先 5件 [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009df8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8ec.md) · 呼出先 5件 [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009df518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df4cc.md#insn-009df518) · [`009df524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df4cc.md#insn-009df524) · [`009df594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df4cc.md#insn-009df594)
- 新版 [`009df6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df668.md#insn-009df6b4) · [`009df6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df668.md#insn-009df6c0) · [`009df730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df668.md#insn-009df730)

~~~diff
- 009df518 ["INT_ADD", "register:40f0:8", ["const:9df518:8", "const:4:8"]]
- 009df518 ["CALL", null, ["callee:00c53cd0:8"]]
+ 009df6b4 ["INT_ADD", "register:40f0:8", ["const:9df6b4:8", "const:4:8"]]
+ 009df6b4 ["CALL", null, ["callee:00c53cd0:8"]]
- 009df518 bytes e6d00994
+ 009df6b4 bytes 87d10994
- 009df524 ["INT_ADD", "register:40f0:8", ["const:9df524:8", "const:4:8"]]
- 009df524 ["CALL", null, ["callee:006647c0:8"]]
+ 009df6c0 ["INT_ADD", "register:40f0:8", ["const:9df6c0:8", "const:4:8"]]
+ 009df6c0 ["CALL", null, ["callee:006647c0:8"]]
- 009df524 bytes 9714f297
+ 009df6c0 bytes 4014f297
- 009df594 ["COPY", "register:0:8", ["register:4040:8"]]
- 009df594 ["INT_ADD", "register:40f0:8", ["const:9df594:8", "const:4:8"]]
- 009df594 ["CALLIND", null, ["register:0:8"]]
+ 009df730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009df730 ["INT_ADD", "register:40f0:8", ["const:9df730:8", "const:4:8"]]
+ 009df730 ["CALLIND", null, ["register:0:8"]]
- 009df594 bytes 00013fd6
+ 009df730 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6d35f4589c07c9bff5562aa1beda4ad"></a>

### [`009df728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df728.md) → [`009df8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8c4.md) FUN_009df8c4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`006cba34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cba34.md) [`006ccb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cc/006ccb38.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 19件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`006cba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cba74.md) [`006ccb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cc/006ccb78.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009df744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df728.md#insn-009df744)
- 新版 [`009df8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8c4.md#insn-009df8e0)

~~~diff
- 009df744 ["INT_ADD", "register:40f0:8", ["const:9df744:8", "const:4:8"]]
- 009df744 ["CALL", null, ["callee:00c53cd0:8"]]
+ 009df8e0 ["INT_ADD", "register:40f0:8", ["const:9df8e0:8", "const:4:8"]]
+ 009df8e0 ["CALL", null, ["callee:00c53cd0:8"]]
- 009df744 bytes 5bd00994
+ 009df8e0 bytes fcd00994
~~~


<a id="compare-9625b5c2016e645c4fc98ab1426450b6"></a>

### [`009df900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df900.md) → [`009dfa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfa9c.md) FUN_009dfa9c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f9820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md) · 呼出先 1件 [`009df750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df750.md)
- 新版 呼出元 1件 [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) · 呼出先 1件 [`009df8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009df948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df900.md#insn-009df948)
- 新版 [`009dfae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfa9c.md#insn-009dfae4)

~~~diff
- 009df948 ["INT_ADD", "register:40f0:8", ["const:9df948:8", "const:4:8"]]
- 009df948 ["CALL", null, ["callee:009df8ec:8"]]
+ 009dfae4 ["INT_ADD", "register:40f0:8", ["const:9dfae4:8", "const:4:8"]]
+ 009dfae4 ["CALL", null, ["callee:009df8ec:8"]]
- 009df948 bytes 82ffff97
+ 009dfae4 bytes 82ffff97
~~~


<a id="compare-3321426f6d042b3ef56d9f1c1dd4d2bd"></a>

### [`009dfc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc10.md) → [`009dfdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfdac.md) FUN_009dfdac

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`009df97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df97c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`009dfb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfb18.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dfc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc10.md#insn-009dfc30) · [`009dfc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc10.md#insn-009dfc44) · [`009dfc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc10.md#insn-009dfc6c)
- 新版 [`009dfdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfdac.md#insn-009dfdcc) · [`009dfde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfdac.md#insn-009dfde0) · [`009dfe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfdac.md#insn-009dfe08)

~~~diff
- 009dfc30 ["INT_ADD", "register:40f0:8", ["const:9dfc30:8", "const:4:8"]]
- 009dfc30 ["CALL", null, ["callee:009dfb18:8"]]
+ 009dfdcc ["INT_ADD", "register:40f0:8", ["const:9dfdcc:8", "const:4:8"]]
+ 009dfdcc ["CALL", null, ["callee:009dfb18:8"]]
- 009dfc30 bytes 53ffff97
+ 009dfdcc bytes 53ffff97
- 009dfc44 ["INT_ADD", "register:40f0:8", ["const:9dfc44:8", "const:4:8"]]
- 009dfc44 ["CALL", null, ["callee:005c179c:8"]]
+ 009dfde0 ["INT_ADD", "register:40f0:8", ["const:9dfde0:8", "const:4:8"]]
+ 009dfde0 ["CALL", null, ["callee:005c179c:8"]]
- 009dfc44 bytes c686ef97
+ 009dfde0 bytes 6f86ef97
- 009dfc6c ["INT_ADD", "register:40f0:8", ["const:9dfc6c:8", "const:4:8"]]
- 009dfc6c ["CALL", null, ["callee:00c57ee0:8"]]
+ 009dfe08 ["INT_ADD", "register:40f0:8", ["const:9dfe08:8", "const:4:8"]]
+ 009dfe08 ["CALL", null, ["callee:00c57ee0:8"]]
- 009dfc6c bytes 9ddf0994
+ 009dfe08 bytes 36e00994
~~~


<a id="compare-c89cab92101ea0df6280a980e84b3402"></a>

### [`009dfc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc70.md) → [`009dfe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md) FUN_009dfe0c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0bdc.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md)
- 新版 呼出元 1件 [`009e0d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0d78.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dfca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc70.md#insn-009dfca0) · [`009dfcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc70.md#insn-009dfcb4) · [`009dfccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc70.md#insn-009dfccc)
- 新版 [`009dfe3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md#insn-009dfe3c) · [`009dfe50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md#insn-009dfe50) · [`009dfe68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md#insn-009dfe68)

~~~diff
- 009dfca0 ["INT_ADD", "register:40f0:8", ["const:9dfca0:8", "const:4:8"]]
- 009dfca0 ["CALL", null, ["callee:0086ab38:8"]]
+ 009dfe3c ["INT_ADD", "register:40f0:8", ["const:9dfe3c:8", "const:4:8"]]
+ 009dfe3c ["CALL", null, ["callee:0086ab38:8"]]
- 009dfca0 bytes 962bfa97
+ 009dfe3c bytes 3f2bfa97
- 009dfcb4 ["INT_ADD", "register:40f0:8", ["const:9dfcb4:8", "const:4:8"]]
- 009dfcb4 ["CALL", null, ["callee:00480178:8"]]
+ 009dfe50 ["INT_ADD", "register:40f0:8", ["const:9dfe50:8", "const:4:8"]]
+ 009dfe50 ["CALL", null, ["callee:00480178:8"]]
- 009dfcb4 bytes 2181ea97
+ 009dfe50 bytes ca80ea97
- 009dfccc ["INT_ADD", "register:40f0:8", ["const:9dfccc:8", "const:4:8"]]
- 009dfccc ["CALL", null, ["callee:004801d8:8"]]
+ 009dfe68 ["INT_ADD", "register:40f0:8", ["const:9dfe68:8", "const:4:8"]]
+ 009dfe68 ["CALL", null, ["callee:004801d8:8"]]
- 009dfccc bytes 3381ea97
+ 009dfe68 bytes dc80ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08cfe5b8dda810a6de11a7e7a2442f73"></a>

### [`009dff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dff34.md) → [`009e00d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e00d0.md) FUN_009e00d0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e0d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0d5c.md) · 呼出先 4件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`009df1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df1d4.md)
- 新版 呼出元 1件 [`009e0ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0ef8.md) · 呼出先 4件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`009df370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dff58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dff34.md#insn-009dff58) · [`009dff88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dff34.md#insn-009dff88) · [`009dffa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dff34.md#insn-009dffa0)
- 新版 [`009e00f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e00d0.md#insn-009e00f4) · [`009e0124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e00d0.md#insn-009e0124) · [`009e013c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e00d0.md#insn-009e013c)

~~~diff
- 009dff58 ["INT_ADD", "register:40f0:8", ["const:9dff58:8", "const:4:8"]]
- 009dff58 ["CALL", null, ["callee:00480b90:8"]]
+ 009e00f4 ["INT_ADD", "register:40f0:8", ["const:9e00f4:8", "const:4:8"]]
+ 009e00f4 ["CALL", null, ["callee:00480b90:8"]]
- 009dff58 bytes fe82ea97
+ 009e00f4 bytes a782ea97
- 009dff88 ["INT_ADD", "register:40f0:8", ["const:9dff88:8", "const:4:8"]]
- 009dff88 ["CALL", null, ["callee:00480b90:8"]]
+ 009e0124 ["INT_ADD", "register:40f0:8", ["const:9e0124:8", "const:4:8"]]
+ 009e0124 ["CALL", null, ["callee:00480b90:8"]]
- 009dff88 bytes f282ea97
+ 009e0124 bytes 9b82ea97
- 009dffa0 ["INT_ADD", "register:40f0:8", ["const:9dffa0:8", "const:4:8"]]
- 009dffa0 ["CALL", null, ["callee:00480b38:8"]]
+ 009e013c ["INT_ADD", "register:40f0:8", ["const:9e013c:8", "const:4:8"]]
+ 009e013c ["CALL", null, ["callee:00480b38:8"]]
- 009dffa0 bytes d682ea97
+ 009e013c bytes 7f82ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17c71403be9e941d6f6345f1f88ed90b"></a>

### [`009e01b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e01b4.md) → [`009e0350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0350.md) FUN_009e0350

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 1件 [`009e01e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e01e0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 1件 [`009e037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e01c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e01b4.md#insn-009e01c4)
- 新版 [`009e0360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0350.md#insn-009e0360)

~~~diff
- 009e01c4 ["INT_ADD", "register:40f0:8", ["const:9e01c4:8", "const:4:8"]]
- 009e01c4 ["CALL", null, ["callee:009e037c:8"]]
+ 009e0360 ["INT_ADD", "register:40f0:8", ["const:9e0360:8", "const:4:8"]]
+ 009e0360 ["CALL", null, ["callee:009e037c:8"]]
- 009e01c4 bytes 07000094
+ 009e0360 bytes 07000094
~~~


<a id="compare-02e8724b72cca5a4a1b3f8fda2262525"></a>

### [`009e0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0bdc.md) → [`009e0d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0d78.md) FUN_009e0d78

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`0086aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e0c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0bdc.md#insn-009e0c10) · [`009e0c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0bdc.md#insn-009e0c20) · [`009e0c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0bdc.md#insn-009e0c3c)
- 新版 [`009e0dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0d78.md#insn-009e0dac) · [`009e0dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0d78.md#insn-009e0dbc) · [`009e0dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0d78.md#insn-009e0dd8)

~~~diff
- 009e0c10 ["INT_ADD", "register:40f0:8", ["const:9e0c10:8", "const:4:8"]]
- 009e0c10 ["CALL", null, ["callee:0086aadc:8"]]
+ 009e0dac ["INT_ADD", "register:40f0:8", ["const:9e0dac:8", "const:4:8"]]
+ 009e0dac ["CALL", null, ["callee:0086aadc:8"]]
- 009e0c10 bytes a327fa97
+ 009e0dac bytes 4c27fa97
- 009e0c20 ["INT_ADD", "register:40f0:8", ["const:9e0c20:8", "const:4:8"]]
- 009e0c20 ["CALL", null, ["callee:00480178:8"]]
+ 009e0dbc ["INT_ADD", "register:40f0:8", ["const:9e0dbc:8", "const:4:8"]]
+ 009e0dbc ["CALL", null, ["callee:00480178:8"]]
- 009e0c20 bytes 467dea97
+ 009e0dbc bytes ef7cea97
- 009e0c3c ["INT_ADD", "register:40f0:8", ["const:9e0c3c:8", "const:4:8"]]
- 009e0c3c ["CALL", null, ["callee:0043bba4:8"]]
+ 009e0dd8 ["INT_ADD", "register:40f0:8", ["const:9e0dd8:8", "const:4:8"]]
+ 009e0dd8 ["CALL", null, ["callee:0043bba4:8"]]
- 009e0c3c bytes ca6be997
+ 009e0dd8 bytes 736be997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03129af57d88450aeeab17d3765deb7f"></a>

### [`009e0d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0d5c.md) → [`009e0ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0ef8.md) FUN_009e0ef8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 4件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`009dff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dff34.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`009e00d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e00d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e0d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0d5c.md#insn-009e0d80) · [`009e0d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0d5c.md#insn-009e0d9c) · [`009e0da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0d5c.md#insn-009e0da8)
- 新版 [`009e0f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0ef8.md#insn-009e0f1c) · [`009e0f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0ef8.md#insn-009e0f38) · [`009e0f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0ef8.md#insn-009e0f44)

~~~diff
- 009e0d80 ["INT_ADD", "register:40f0:8", ["const:9e0d80:8", "const:4:8"]]
- 009e0d80 ["CALL", null, ["callee:00480b90:8"]]
+ 009e0f1c ["INT_ADD", "register:40f0:8", ["const:9e0f1c:8", "const:4:8"]]
+ 009e0f1c ["CALL", null, ["callee:00480b90:8"]]
- 009e0d80 bytes 747fea97
+ 009e0f1c bytes 1d7fea97
- 009e0d9c ["INT_ADD", "register:40f0:8", ["const:9e0d9c:8", "const:4:8"]]
- 009e0d9c ["CALL", null, ["callee:00480b38:8"]]
+ 009e0f38 ["INT_ADD", "register:40f0:8", ["const:9e0f38:8", "const:4:8"]]
+ 009e0f38 ["CALL", null, ["callee:00480b38:8"]]
- 009e0d9c bytes 577fea97
+ 009e0f38 bytes 007fea97
- 009e0da8 ["INT_ADD", "register:40f0:8", ["const:9e0da8:8", "const:4:8"]]
- 009e0da8 ["CALL", null, ["callee:00480d48:8"]]
+ 009e0f44 ["INT_ADD", "register:40f0:8", ["const:9e0f44:8", "const:4:8"]]
+ 009e0f44 ["CALL", null, ["callee:00480d48:8"]]
- 009e0da8 bytes d87fea97
+ 009e0f44 bytes 817fea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4c1c28c0f1d6b8882b1c7ee1340fc01"></a>

### [`009e0fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0fbc.md) → [`009e1158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1158.md) FUN_009e1158

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009e10dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 3件 [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 3件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e1020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0fbc.md#insn-009e1020) · [`009e1048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0fbc.md#insn-009e1048) · [`009e10c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0fbc.md#insn-009e10c0)
- 新版 [`009e11bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1158.md#insn-009e11bc) · [`009e11e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1158.md#insn-009e11e4) · [`009e125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1158.md#insn-009e125c)

~~~diff
- 009e1020 ["INT_ADD", "register:40f0:8", ["const:9e1020:8", "const:4:8"]]
- 009e1020 ["CALL", null, ["callee:00c58450:8"]]
+ 009e11bc ["INT_ADD", "register:40f0:8", ["const:9e11bc:8", "const:4:8"]]
+ 009e11bc ["CALL", null, ["callee:00c58450:8"]]
- 009e1020 bytes 0cdc0994
+ 009e11bc bytes a5dc0994
- 009e1048 ["INT_ADD", "register:40f0:8", ["const:9e1048:8", "const:4:8"]]
- 009e1048 ["CALL", null, ["callee:00c58450:8"]]
+ 009e11e4 ["INT_ADD", "register:40f0:8", ["const:9e11e4:8", "const:4:8"]]
+ 009e11e4 ["CALL", null, ["callee:00c58450:8"]]
- 009e1048 bytes 02dc0994
+ 009e11e4 bytes 9bdc0994
- 009e10c0 ["INT_ADD", "register:40f0:8", ["const:9e10c0:8", "const:4:8"]]
- 009e10c0 ["CALL", null, ["callee:00802b58:8"]]
+ 009e125c ["INT_ADD", "register:40f0:8", ["const:9e125c:8", "const:4:8"]]
+ 009e125c ["CALL", null, ["callee:00802b58:8"]]
- 009e10c0 bytes 9686f897
+ 009e125c bytes 3f86f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45d60b816c2592b7a92d1ed755dac2a9"></a>

### [`009e10dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md) → [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) FUN_009e1278

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 24件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`007f9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e44.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md)
- 新版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 24件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f9e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e1134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md#insn-009e1134) · [`009e114c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md#insn-009e114c) · [`009e11a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md#insn-009e11a8)
- 新版 [`009e12d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md#insn-009e12d0) · [`009e12e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md#insn-009e12e8) · [`009e1344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md#insn-009e1344)

~~~diff
- 009e1134 ["INT_ADD", "register:40f0:8", ["const:9e1134:8", "const:4:8"]]
- 009e1134 ["CALL", null, ["callee:009e1158:8"]]
+ 009e12d0 ["INT_ADD", "register:40f0:8", ["const:9e12d0:8", "const:4:8"]]
+ 009e12d0 ["CALL", null, ["callee:009e1158:8"]]
- 009e1134 bytes a2ffff97
+ 009e12d0 bytes a2ffff97
- 009e114c ["INT_ADD", "register:40f0:8", ["const:9e114c:8", "const:4:8"]]
- 009e114c ["CALL", null, ["callee:009e2254:8"]]
+ 009e12e8 ["INT_ADD", "register:40f0:8", ["const:9e12e8:8", "const:4:8"]]
+ 009e12e8 ["CALL", null, ["callee:009e2254:8"]]
- 009e114c bytes db030094
+ 009e12e8 bytes db030094
- 009e11a8 ["INT_ADD", "register:40f0:8", ["const:9e11a8:8", "const:4:8"]]
- 009e11a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 009e1344 ["INT_ADD", "register:40f0:8", ["const:9e1344:8", "const:4:8"]]
+ 009e1344 ["CALL", null, ["callee:00c57e90:8"]]
- 009e11a8 bytes 3ada0994
+ 009e1344 bytes d3da0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fdc4a5b67d4796e1c44c433164e2496"></a>

### [`009e20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md) → [`009e2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md) FUN_009e2254

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`009e10dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md) [`009e29a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e29a4.md) [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md) [`009e2f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2f50.md) [`009e321c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e321c.md) · 呼出先 3件 [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 7件 [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) [`009e2b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2b40.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md) [`009e30ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e30ec.md) [`009e33b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e33b8.md) · 呼出先 3件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e2130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md#insn-009e2130) · [`009e2158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md#insn-009e2158) · [`009e21d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md#insn-009e21d4)
- 新版 [`009e22cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md#insn-009e22cc) · [`009e22f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md#insn-009e22f4) · [`009e2370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md#insn-009e2370)

~~~diff
- 009e2130 ["INT_ADD", "register:40f0:8", ["const:9e2130:8", "const:4:8"]]
- 009e2130 ["CALL", null, ["callee:00c58450:8"]]
+ 009e22cc ["INT_ADD", "register:40f0:8", ["const:9e22cc:8", "const:4:8"]]
+ 009e22cc ["CALL", null, ["callee:00c58450:8"]]
- 009e2130 bytes c8d70994
+ 009e22cc bytes 61d80994
- 009e2158 ["INT_ADD", "register:40f0:8", ["const:9e2158:8", "const:4:8"]]
- 009e2158 ["CALL", null, ["callee:00c58450:8"]]
+ 009e22f4 ["INT_ADD", "register:40f0:8", ["const:9e22f4:8", "const:4:8"]]
+ 009e22f4 ["CALL", null, ["callee:00c58450:8"]]
- 009e2158 bytes bed70994
+ 009e22f4 bytes 57d80994
- 009e21d4 ["INT_ADD", "register:40f0:8", ["const:9e21d4:8", "const:4:8"]]
- 009e21d4 ["CALL", null, ["callee:00802b58:8"]]
+ 009e2370 ["INT_ADD", "register:40f0:8", ["const:9e2370:8", "const:4:8"]]
+ 009e2370 ["CALL", null, ["callee:00802b58:8"]]
- 009e21d4 bytes 5182f897
+ 009e2370 bytes fa81f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efc1ad2a212839f4fe07049d7d954ed7"></a>

### [`009e21f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e21f0.md) → [`009e238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e238c.md) FUN_009e238c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086ab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ab70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e220c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e21f0.md#insn-009e220c) · [`009e221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e21f0.md#insn-009e221c) · [`009e2224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e21f0.md#insn-009e2224)
- 新版 [`009e23a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e238c.md#insn-009e23a8) · [`009e23b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e238c.md#insn-009e23b8) · [`009e23c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e238c.md#insn-009e23c0)

~~~diff
- 009e220c ["INT_ADD", "register:40f0:8", ["const:9e220c:8", "const:4:8"]]
- 009e220c ["CALL", null, ["callee:00c57eb0:8"]]
+ 009e23a8 ["INT_ADD", "register:40f0:8", ["const:9e23a8:8", "const:4:8"]]
+ 009e23a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 009e220c bytes 29d60994
+ 009e23a8 bytes c2d60994
- 009e221c ["INT_ADD", "register:40f0:8", ["const:9e221c:8", "const:4:8"]]
- 009e221c ["CALL", null, ["callee:00c57eb0:8"]]
+ 009e23b8 ["INT_ADD", "register:40f0:8", ["const:9e23b8:8", "const:4:8"]]
+ 009e23b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 009e221c bytes 25d60994
+ 009e23b8 bytes bed60994
- 009e2224 ["INT_ADD", "register:40f0:8", ["const:9e2224:8", "const:4:8"]]
- 009e2224 ["CALL", null, ["callee:0086abb0:8"]]
+ 009e23c0 ["INT_ADD", "register:40f0:8", ["const:9e23c0:8", "const:4:8"]]
+ 009e23c0 ["CALL", null, ["callee:0086abb0:8"]]
- 009e2224 bytes 5322fa97
+ 009e23c0 bytes fc21fa97
~~~


<a id="compare-593cbc308883a5b4764e76a55413dd79"></a>

### [`009e224c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e224c.md) → [`009e23e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e23e8.md) FUN_009e23e8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e2298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e224c.md#insn-009e2298)
- 新版 [`009e2434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e23e8.md#insn-009e2434)

~~~diff
- 009e2298 ["INT_ADD", "register:40f0:8", ["const:9e2298:8", "const:4:8"]]
- 009e2298 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009e2434 ["INT_ADD", "register:40f0:8", ["const:9e2434:8", "const:4:8"]]
+ 009e2434 ["CALL", null, ["callee:00c57eb0:8"]]
- 009e2298 bytes 06d60994
+ 009e2434 bytes 9fd60994
~~~


<a id="compare-22e4f24e87458df880e1a2280903ae9a"></a>

### [`009e22c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e22c8.md) → [`009e2464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md) FUN_009e2464

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007f95a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f95a0.md) [`009e10dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md)
- 新版 呼出元 2件 [`007f95e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md) [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e2328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e22c8.md#insn-009e2328) · [`009e2354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e22c8.md#insn-009e2354) · [`009e23c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e22c8.md#insn-009e23c0)
- 新版 [`009e24c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md#insn-009e24c4) · [`009e24f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md#insn-009e24f0) · [`009e255c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md#insn-009e255c)

~~~diff
- 009e2328 ["INT_ADD", "register:40f0:8", ["const:9e2328:8", "const:4:8"]]
- 009e2328 ["CALL", null, ["callee:009e2f94:8"]]
+ 009e24c4 ["INT_ADD", "register:40f0:8", ["const:9e24c4:8", "const:4:8"]]
+ 009e24c4 ["CALL", null, ["callee:009e2f94:8"]]
- 009e2328 bytes b4020094
+ 009e24c4 bytes b4020094
- 009e2354 ["INT_ADD", "register:40f0:8", ["const:9e2354:8", "const:4:8"]]
- 009e2354 ["CALL", null, ["callee:0043bba4:8"]]
+ 009e24f0 ["INT_ADD", "register:40f0:8", ["const:9e24f0:8", "const:4:8"]]
+ 009e24f0 ["CALL", null, ["callee:0043bba4:8"]]
- 009e2354 bytes 0466e997
+ 009e24f0 bytes ad65e997
- 009e23c0 ["INT_ADD", "register:40f0:8", ["const:9e23c0:8", "const:4:8"]]
- 009e23c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009e255c ["INT_ADD", "register:40f0:8", ["const:9e255c:8", "const:4:8"]]
+ 009e255c ["CALL", null, ["callee:00c57e90:8"]]
- 009e23c0 bytes b4d50994
+ 009e255c bytes 4dd60994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea4b23eaba3868b87ee08cb97da37ed"></a>

### [`009e298c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e298c.md) → [`009e2b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2b28.md) FUN_009e2b28

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00744238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744238.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b092d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092d8.md)
- 新版 呼出元 1件 [`00744278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744278.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b09700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e2994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e298c.md#insn-009e2994)
- 新版 [`009e2b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2b28.md#insn-009e2b30)

~~~diff
- 009e2994 ["INT_ADD", "register:40f0:8", ["const:9e2994:8", "const:4:8"]]
- 009e2994 ["CALL", null, ["callee:008514f8:8"]]
+ 009e2b30 ["INT_ADD", "register:40f0:8", ["const:9e2b30:8", "const:4:8"]]
+ 009e2b30 ["CALL", null, ["callee:008514f8:8"]]
- 009e2994 bytes c9baf997
+ 009e2b30 bytes 72baf997
~~~


<a id="compare-6b9617428d4cfef377b6871d5d3bbed3"></a>

### [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md) → [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md) FUN_009e2f94

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 66件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`00658bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658bac.md) [`00658d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658d6c.md) · 呼出先 3件 [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`009e20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md)
- 新版 呼出元 66件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`00658bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658bec.md) [`00658dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658dac.md) · 呼出先 3件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`009e2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e2e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md#insn-009e2e1c) · [`009e2e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md#insn-009e2e78) · [`009e2e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md#insn-009e2e90)
- 新版 [`009e2fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md#insn-009e2fb8) · [`009e3014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md#insn-009e3014) · [`009e302c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md#insn-009e302c)

~~~diff
- 009e2e1c ["INT_ADD", "register:40f0:8", ["const:9e2e1c:8", "const:4:8"]]
- 009e2e1c ["CALL", null, ["callee:009e2254:8"]]
+ 009e2fb8 ["INT_ADD", "register:40f0:8", ["const:9e2fb8:8", "const:4:8"]]
+ 009e2fb8 ["CALL", null, ["callee:009e2254:8"]]
- 009e2e1c bytes a7fcff97
+ 009e2fb8 bytes a7fcff97
- 009e2e78 ["INT_ADD", "register:40f0:8", ["const:9e2e78:8", "const:4:8"]]
- 009e2e78 ["CALL", null, ["callee:00802b58:8"]]
+ 009e3014 ["INT_ADD", "register:40f0:8", ["const:9e3014:8", "const:4:8"]]
+ 009e3014 ["CALL", null, ["callee:00802b58:8"]]
- 009e2e78 bytes 287ff897
+ 009e3014 bytes d17ef897
- 009e2e90 ["INT_ADD", "register:40f0:8", ["const:9e2e90:8", "const:4:8"]]
- 009e2e90 ["CALL", null, ["callee:00802ee0:8"]]
+ 009e302c ["INT_ADD", "register:40f0:8", ["const:9e302c:8", "const:4:8"]]
+ 009e302c ["CALL", null, ["callee:00802ee0:8"]]
- 009e2e90 bytes 0480f897
+ 009e302c bytes ad7ff897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d34e40f6061014a709261eda29056c42"></a>

### [`009e31d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e31d0.md) → [`009e336c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e336c.md) FUN_009e336c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e31ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e31d0.md#insn-009e31ec)
- 新版 [`009e3388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e336c.md#insn-009e3388)

~~~diff
- 009e31ec ["INT_ADD", "register:40f0:8", ["const:9e31ec:8", "const:4:8"]]
- 009e31ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 009e3388 ["INT_ADD", "register:40f0:8", ["const:9e3388:8", "const:4:8"]]
+ 009e3388 ["CALL", null, ["callee:00c57eb0:8"]]
- 009e31ec bytes 31d20994
+ 009e3388 bytes cad20994
~~~


<a id="compare-fa4db4a2e76fa571e1ad8a05f2cb40fa"></a>

### [`009e321c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e321c.md) → [`009e33b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e33b8.md) FUN_009e33b8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`007f9820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`009df750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df750.md) [`009e20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md)
- 新版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`009df8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8ec.md) [`009e2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e3260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e321c.md#insn-009e3260) · [`009e3274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e321c.md#insn-009e3274) · [`009e3284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e321c.md#insn-009e3284)
- 新版 [`009e33fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e33b8.md#insn-009e33fc) · [`009e3410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e33b8.md#insn-009e3410) · [`009e3420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e33b8.md#insn-009e3420)

~~~diff
- 009e3260 ["INT_ADD", "register:40f0:8", ["const:9e3260:8", "const:4:8"]]
- 009e3260 ["CALL", null, ["callee:00802b58:8"]]
+ 009e33fc ["INT_ADD", "register:40f0:8", ["const:9e33fc:8", "const:4:8"]]
+ 009e33fc ["CALL", null, ["callee:00802b58:8"]]
- 009e3260 bytes 2e7ef897
+ 009e33fc bytes d77df897
- 009e3274 ["INT_ADD", "register:40f0:8", ["const:9e3274:8", "const:4:8"]]
- 009e3274 ["CALL", null, ["callee:00802ee0:8"]]
+ 009e3410 ["INT_ADD", "register:40f0:8", ["const:9e3410:8", "const:4:8"]]
+ 009e3410 ["CALL", null, ["callee:00802ee0:8"]]
- 009e3274 bytes 0b7ff897
+ 009e3410 bytes b47ef897
- 009e3284 ["INT_ADD", "register:40f0:8", ["const:9e3284:8", "const:4:8"]]
- 009e3284 ["CALL", null, ["callee:009e2254:8"]]
+ 009e3420 ["INT_ADD", "register:40f0:8", ["const:9e3420:8", "const:4:8"]]
+ 009e3420 ["CALL", null, ["callee:009e2254:8"]]
- 009e3284 bytes 8dfbff97
+ 009e3420 bytes 8dfbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a7724e6cbd0e97d81db73e93754b597"></a>

### [`009e354c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e354c.md) → [`009e36e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e36e8.md) FUN_009e36e8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md) [`00b092d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092d8.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md) [`00b09700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e354c.md#insn-009e35b8) · [`009e35bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e354c.md#insn-009e35bc) · [`009e35c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e354c.md#insn-009e35c4)
- 新版 [`009e3754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e36e8.md#insn-009e3754) · [`009e3758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e36e8.md#insn-009e3758) · [`009e3760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e36e8.md#insn-009e3760)

~~~diff
- 009e35b8 ["INT_ADD", "register:40f0:8", ["const:9e35b8:8", "const:4:8"]]
- 009e35b8 ["CALL", null, ["callee:008514f8:8"]]
+ 009e3754 ["INT_ADD", "register:40f0:8", ["const:9e3754:8", "const:4:8"]]
+ 009e3754 ["CALL", null, ["callee:008514f8:8"]]
- 009e35b8 bytes c0b7f997
+ 009e3754 bytes 69b7f997
- 009e35bc ["INT_ADD", "register:40f0:8", ["const:9e35bc:8", "const:4:8"]]
- 009e35bc ["CALL", null, ["callee:008514f8:8"]]
+ 009e3758 ["INT_ADD", "register:40f0:8", ["const:9e3758:8", "const:4:8"]]
+ 009e3758 ["CALL", null, ["callee:008514f8:8"]]
- 009e35bc bytes bfb7f997
+ 009e3758 bytes 68b7f997
- 009e35c4 ["INT_ADD", "register:40f0:8", ["const:9e35c4:8", "const:4:8"]]
- 009e35c4 ["CALL", null, ["callee:00b09700:8"]]
+ 009e3760 ["INT_ADD", "register:40f0:8", ["const:9e3760:8", "const:4:8"]]
+ 009e3760 ["CALL", null, ["callee:00b09700:8"]]
- 009e35c4 bytes 45970494
+ 009e3760 bytes e8970494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cc1e771240d8482fc718fe916eda283"></a>

### [`009e385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e385c.md) → [`009e39f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e39f8.md) FUN_009e39f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007f95a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f95a0.md) · 呼出先 1件 [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007f95e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md) · 呼出先 1件 [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e3864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e385c.md#insn-009e3864)
- 新版 [`009e3a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e39f8.md#insn-009e3a00)

~~~diff
- 009e3864 ["INT_ADD", "register:40f0:8", ["const:9e3864:8", "const:4:8"]]
- 009e3864 ["CALL", null, ["callee:009e2f94:8"]]
+ 009e3a00 ["INT_ADD", "register:40f0:8", ["const:9e3a00:8", "const:4:8"]]
+ 009e3a00 ["CALL", null, ["callee:009e2f94:8"]]
- 009e3864 bytes 65fdff97
+ 009e3a00 bytes 65fdff97
~~~


<a id="compare-647ff4aa5fdabe35696d1d055a7b03c0"></a>

### [`009e3880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3880.md) → [`009e3a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a1c.md) FUN_009e3a1c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007f9820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md) · 呼出先 1件 [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) · 呼出先 1件 [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e3888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3880.md#insn-009e3888)
- 新版 [`009e3a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a1c.md#insn-009e3a24)

~~~diff
- 009e3888 ["INT_ADD", "register:40f0:8", ["const:9e3888:8", "const:4:8"]]
- 009e3888 ["CALL", null, ["callee:009e2f94:8"]]
+ 009e3a24 ["INT_ADD", "register:40f0:8", ["const:9e3a24:8", "const:4:8"]]
+ 009e3a24 ["CALL", null, ["callee:009e2f94:8"]]
- 009e3888 bytes 5cfdff97
+ 009e3a24 bytes 5cfdff97
~~~


<a id="compare-878c95f9c9900ea7933409dba65d19a6"></a>

### [`009e38e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e38e4.md) → [`009e3a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md) FUN_009e3a80

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007f9154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9154.md) [`007f94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b8.md) [`007f95a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f95a0.md) [`007fa020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fa/007fa020.md) · 呼出先 2件 [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`007f9194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9194.md) [`007f94f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f94f8.md) [`007f95e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md) [`007fa060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa060.md) · 呼出先 2件 [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e38f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e38e4.md#insn-009e38f0) · [`009e394c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e38e4.md#insn-009e394c) · [`009e397c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e38e4.md#insn-009e397c)
- 新版 [`009e3a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md#insn-009e3a8c) · [`009e3ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md#insn-009e3ae8) · [`009e3b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md#insn-009e3b18)

~~~diff
- 009e38f0 ["INT_ADD", "register:40f0:8", ["const:9e38f0:8", "const:4:8"]]
- 009e38f0 ["CALL", null, ["callee:009e2f94:8"]]
+ 009e3a8c ["INT_ADD", "register:40f0:8", ["const:9e3a8c:8", "const:4:8"]]
+ 009e3a8c ["CALL", null, ["callee:009e2f94:8"]]
- 009e38f0 bytes 42fdff97
+ 009e3a8c bytes 42fdff97
- 009e394c ["INT_ADD", "register:40f0:8", ["const:9e394c:8", "const:4:8"]]
- 009e394c ["CALL", null, ["callee:00c57eb0:8"]]
+ 009e3ae8 ["INT_ADD", "register:40f0:8", ["const:9e3ae8:8", "const:4:8"]]
+ 009e3ae8 ["CALL", null, ["callee:00c57eb0:8"]]
- 009e394c bytes 59d00994
+ 009e3ae8 bytes f2d00994
- 009e397c ["INT_ADD", "register:40f0:8", ["const:9e397c:8", "const:4:8"]]
- 009e397c ["CALL", null, ["callee:00c57eb0:8"]]
+ 009e3b18 ["INT_ADD", "register:40f0:8", ["const:9e3b18:8", "const:4:8"]]
+ 009e3b18 ["CALL", null, ["callee:00c57eb0:8"]]
- 009e397c bytes 4dd00994
+ 009e3b18 bytes e6d00994
~~~


<a id="compare-54181c54eae8bf7ac953ba8561a81bf2"></a>

### [`009e39a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e39a4.md) → [`009e3b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3b40.md) FUN_009e3b40

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 2件 [`009e20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md) [`009e8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e8/009e8780.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 2件 [`009e2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md) [`009e891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e891c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e39bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e39a4.md#insn-009e39bc)
- 新版 [`009e3b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3b40.md#insn-009e3b58)

~~~diff
- 009e39bc ["INT_ADD", "register:40f0:8", ["const:9e39bc:8", "const:4:8"]]
- 009e39bc ["CALL", null, ["callee:009e2254:8"]]
+ 009e3b58 ["INT_ADD", "register:40f0:8", ["const:9e3b58:8", "const:4:8"]]
+ 009e3b58 ["CALL", null, ["callee:009e2254:8"]]
- 009e39bc bytes bff9ff97
+ 009e3b58 bytes bff9ff97
~~~


<a id="compare-c11f760da2b5e98d6ab501024b58ccb3"></a>

### [`009e3a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3a70.md) → [`009e3c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3c0c.md) FUN_009e3c0c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 1件 [`009e20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 1件 [`009e2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2254.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e3a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3a70.md#insn-009e3a88)
- 新版 [`009e3c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3c0c.md#insn-009e3c24)

~~~diff
- 009e3a88 ["INT_ADD", "register:40f0:8", ["const:9e3a88:8", "const:4:8"]]
- 009e3a88 ["CALL", null, ["callee:009e2254:8"]]
+ 009e3c24 ["INT_ADD", "register:40f0:8", ["const:9e3c24:8", "const:4:8"]]
+ 009e3c24 ["CALL", null, ["callee:009e2254:8"]]
- 009e3a88 bytes 8cf9ff97
+ 009e3c24 bytes 8cf9ff97
~~~


<a id="compare-a79efd1cf9d01b10b3c61657c299f425"></a>

### [`009e3ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3ae8.md) → [`009e3c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3c84.md) FUN_009e3c84

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) · 呼出先 1件 [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md)
- 新版 呼出元 1件 [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) · 呼出先 1件 [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e3b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3ae8.md#insn-009e3b00)
- 新版 [`009e3c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3c84.md#insn-009e3c9c)

~~~diff
- 009e3b00 ["INT_ADD", "register:40f0:8", ["const:9e3b00:8", "const:4:8"]]
- 009e3b00 ["CALL", null, ["callee:009e2f94:8"]]
+ 009e3c9c ["INT_ADD", "register:40f0:8", ["const:9e3c9c:8", "const:4:8"]]
+ 009e3c9c ["CALL", null, ["callee:009e2f94:8"]]
- 009e3b00 bytes befcff97
+ 009e3c9c bytes befcff97
~~~


<a id="compare-35ee165abd64d6b08ec82b6149d78cbf"></a>

### [`009e3b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3b18.md) → [`009e3cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3cb4.md) FUN_009e3cb4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) · 呼出先 2件 [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md)
- 新版 呼出元 1件 [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) · 呼出先 2件 [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e3b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3b18.md#insn-009e3b2c) · [`009e3b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3b18.md#insn-009e3b38)
- 新版 [`009e3cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3cb4.md#insn-009e3cc8) · [`009e3cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3cb4.md#insn-009e3cd4)

~~~diff
- 009e3b2c ["INT_ADD", "register:40f0:8", ["const:9e3b2c:8", "const:4:8"]]
- 009e3b2c ["CALL", null, ["callee:009e2f94:8"]]
+ 009e3cc8 ["INT_ADD", "register:40f0:8", ["const:9e3cc8:8", "const:4:8"]]
+ 009e3cc8 ["CALL", null, ["callee:009e2f94:8"]]
- 009e3b2c bytes b3fcff97
+ 009e3cc8 bytes b3fcff97
- 009e3b38 ["INT_ADD", "register:40f0:8", ["const:9e3b38:8", "const:4:8"]]
- 009e3b38 ["CALL", null, ["callee:00802ca8:8"]]
+ 009e3cd4 ["INT_ADD", "register:40f0:8", ["const:9e3cd4:8", "const:4:8"]]
+ 009e3cd4 ["CALL", null, ["callee:00802ca8:8"]]
- 009e3b38 bytes 4c7cf897
+ 009e3cd4 bytes f57bf897
~~~


