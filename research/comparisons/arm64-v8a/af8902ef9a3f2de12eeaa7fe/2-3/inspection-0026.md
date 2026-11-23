# v16.0.0 → v16.0.1 · 要調査の変更候補 (26)

[一覧の目次](README.md)

<a id="compare-719f51163ed68b8aba1461a3ca7743d2"></a>

### [`0080da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080da1c.md) → [`0080da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md) FUN_0080da5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d820.md) [`00b2a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0080d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md) [`00b2abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080da98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080da1c.md#insn-0080da98) · [`0080dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080da1c.md#insn-0080dae0)
- 新版 `0080dad8`（命令位置の公開資料なし） · `0080db20`（命令位置の公開資料なし）

~~~diff
- 0080da98 ["INT_ADD", "register:40f0:8", ["const:80da98:8", "const:4:8"]]
- 0080da98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080dad8 ["INT_ADD", "register:40f0:8", ["const:80dad8:8", "const:4:8"]]
+ 0080dad8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0080da98 bytes 06281194
+ 0080dad8 bytes f6281194
- 0080dae0 ["INT_ADD", "register:40f0:8", ["const:80dae0:8", "const:4:8"]]
- 0080dae0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080db20 ["INT_ADD", "register:40f0:8", ["const:80db20:8", "const:4:8"]]
+ 0080db20 ["CALL", null, ["callee:00c57eb0:8"]]
- 0080dae0 bytes f4271194
+ 0080db20 bytes e4281194
~~~


<a id="compare-1f15e828d3823779595f8c9652a49f4c"></a>

### [`0080db38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080db38.md) → [`0080db78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080db78.md) FUN_0080db78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080db6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080db38.md#insn-0080db6c) · [`0080dbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080db38.md#insn-0080dbbc)
- 新版 `0080dbac`（命令位置の公開資料なし） · `0080dbfc`（命令位置の公開資料なし）

~~~diff
- 0080db6c ["INT_ADD", "register:40f0:8", ["const:80db6c:8", "const:4:8"]]
- 0080db6c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080dbac ["INT_ADD", "register:40f0:8", ["const:80dbac:8", "const:4:8"]]
+ 0080dbac ["CALL", null, ["callee:00c57eb0:8"]]
- 0080db6c bytes d1271194
+ 0080dbac bytes c1281194
- 0080dbbc ["INT_ADD", "register:40f0:8", ["const:80dbbc:8", "const:4:8"]]
- 0080dbbc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080dbfc ["INT_ADD", "register:40f0:8", ["const:80dbfc:8", "const:4:8"]]
+ 0080dbfc ["CALL", null, ["callee:00c57eb0:8"]]
- 0080dbbc bytes bd271194
+ 0080dbfc bytes ad281194
~~~


<a id="compare-e2dc06c8b97ebf754f78c1ffba63a706"></a>

### [`0080dbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080dbf4.md) → [`0080dc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080dc34.md) FUN_0080dc34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0080de00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080de00.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de40.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080dca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080dbf4.md#insn-0080dca0) · [`0080dce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080dbf4.md#insn-0080dce4) · [`0080dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080dbf4.md#insn-0080dd28)
- 新版 `0080dce0`（命令位置の公開資料なし） · `0080dd24`（命令位置の公開資料なし） · `0080dd68`（命令位置の公開資料なし）

~~~diff
- 0080dca0 ["INT_ADD", "register:40f0:8", ["const:80dca0:8", "const:4:8"]]
- 0080dca0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080dce0 ["INT_ADD", "register:40f0:8", ["const:80dce0:8", "const:4:8"]]
+ 0080dce0 ["CALL", null, ["callee:00c57e90:8"]]
- 0080dca0 bytes 7c271194
+ 0080dce0 bytes 6c281194
- 0080dce4 ["INT_ADD", "register:40f0:8", ["const:80dce4:8", "const:4:8"]]
- 0080dce4 ["CALL", null, ["callee:00c58090:8"]]
+ 0080dd24 ["INT_ADD", "register:40f0:8", ["const:80dd24:8", "const:4:8"]]
+ 0080dd24 ["CALL", null, ["callee:00c58090:8"]]
- 0080dce4 bytes eb271194
+ 0080dd24 bytes db281194
- 0080dd28 ["INT_ADD", "register:40f0:8", ["const:80dd28:8", "const:4:8"]]
- 0080dd28 ["CALL", null, ["callee:00c58090:8"]]
+ 0080dd68 ["INT_ADD", "register:40f0:8", ["const:80dd68:8", "const:4:8"]]
+ 0080dd68 ["CALL", null, ["callee:00c58090:8"]]
- 0080dd28 bytes da271194
+ 0080dd68 bytes ca281194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccbdf8ca502553c6ee4a53de70e29eba"></a>

### [`0080de14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080de14.md) → [`0080de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md) FUN_0080de54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0080e06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e06c.md) [`0080e244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e244.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e0ac.md) [`0080e284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e284.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080ded4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080de14.md#insn-0080ded4) · [`0080df0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080de14.md#insn-0080df0c) · [`0080df58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080de14.md#insn-0080df58)
- 新版 `0080df14`（命令位置の公開資料なし） · `0080df4c`（命令位置の公開資料なし） · `0080df98`（命令位置の公開資料なし）

~~~diff
- 0080ded4 ["INT_ADD", "register:40f0:8", ["const:80ded4:8", "const:4:8"]]
- 0080ded4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080df14 ["INT_ADD", "register:40f0:8", ["const:80df14:8", "const:4:8"]]
+ 0080df14 ["CALL", null, ["callee:00c57e90:8"]]
- 0080ded4 bytes ef261194
+ 0080df14 bytes df271194
- 0080df0c ["INT_ADD", "register:40f0:8", ["const:80df0c:8", "const:4:8"]]
- 0080df0c ["CALL", null, ["callee:00c58090:8"]]
+ 0080df4c ["INT_ADD", "register:40f0:8", ["const:80df4c:8", "const:4:8"]]
+ 0080df4c ["CALL", null, ["callee:00c58090:8"]]
- 0080df0c bytes 61271194
+ 0080df4c bytes 51281194
- 0080df58 ["INT_ADD", "register:40f0:8", ["const:80df58:8", "const:4:8"]]
- 0080df58 ["CALL", null, ["callee:00c58090:8"]]
+ 0080df98 ["INT_ADD", "register:40f0:8", ["const:80df98:8", "const:4:8"]]
+ 0080df98 ["CALL", null, ["callee:00c58090:8"]]
- 0080df58 bytes 4e271194
+ 0080df98 bytes 3e281194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea5d2147fbec19bf1dc0c867245029bb"></a>

### [`0080e06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e06c.md) → [`0080e0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e0ac.md) FUN_0080e0ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080de14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080de14.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0080de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e06c.md#insn-0080e0e8) · [`0080e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e06c.md#insn-0080e130)
- 新版 `0080e128`（命令位置の公開資料なし） · `0080e170`（命令位置の公開資料なし）

~~~diff
- 0080e0e8 ["INT_ADD", "register:40f0:8", ["const:80e0e8:8", "const:4:8"]]
- 0080e0e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080e128 ["INT_ADD", "register:40f0:8", ["const:80e128:8", "const:4:8"]]
+ 0080e128 ["CALL", null, ["callee:00c57eb0:8"]]
- 0080e0e8 bytes 72261194
+ 0080e128 bytes 62271194
- 0080e130 ["INT_ADD", "register:40f0:8", ["const:80e130:8", "const:4:8"]]
- 0080e130 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080e170 ["INT_ADD", "register:40f0:8", ["const:80e170:8", "const:4:8"]]
+ 0080e170 ["CALL", null, ["callee:00c57eb0:8"]]
- 0080e130 bytes 60261194
+ 0080e170 bytes 50271194
~~~


<a id="compare-c978b76a7fc3f5337af989283feffbd1"></a>

### [`0080e188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e188.md) → [`0080e1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e1c8.md) FUN_0080e1c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e188.md#insn-0080e1bc) · [`0080e20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e188.md#insn-0080e20c)
- 新版 `0080e1fc`（命令位置の公開資料なし） · `0080e24c`（命令位置の公開資料なし）

~~~diff
- 0080e1bc ["INT_ADD", "register:40f0:8", ["const:80e1bc:8", "const:4:8"]]
- 0080e1bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080e1fc ["INT_ADD", "register:40f0:8", ["const:80e1fc:8", "const:4:8"]]
+ 0080e1fc ["CALL", null, ["callee:00c57eb0:8"]]
- 0080e1bc bytes 3d261194
+ 0080e1fc bytes 2d271194
- 0080e20c ["INT_ADD", "register:40f0:8", ["const:80e20c:8", "const:4:8"]]
- 0080e20c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080e24c ["INT_ADD", "register:40f0:8", ["const:80e24c:8", "const:4:8"]]
+ 0080e24c ["CALL", null, ["callee:00c57eb0:8"]]
- 0080e20c bytes 29261194
+ 0080e24c bytes 19271194
~~~


<a id="compare-e83198d3b59461d2edca8f0cac0d3ed8"></a>

### [`0080e26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e26c.md) → [`0080e2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e2ac.md) FUN_0080e2ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0080e398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e398.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e3d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e26c.md#insn-0080e2e4) · [`0080e308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e26c.md#insn-0080e308) · [`0080e334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e26c.md#insn-0080e334)
- 新版 `0080e324`（命令位置の公開資料なし） · `0080e348`（命令位置の公開資料なし） · `0080e374`（命令位置の公開資料なし）

~~~diff
- 0080e2e4 ["INT_ADD", "register:40f0:8", ["const:80e2e4:8", "const:4:8"]]
- 0080e2e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080e324 ["INT_ADD", "register:40f0:8", ["const:80e324:8", "const:4:8"]]
+ 0080e324 ["CALL", null, ["callee:00c57e90:8"]]
- 0080e2e4 bytes eb251194
+ 0080e324 bytes db261194
- 0080e308 ["INT_ADD", "register:40f0:8", ["const:80e308:8", "const:4:8"]]
- 0080e308 ["CALL", null, ["callee:00c58090:8"]]
+ 0080e348 ["INT_ADD", "register:40f0:8", ["const:80e348:8", "const:4:8"]]
+ 0080e348 ["CALL", null, ["callee:00c58090:8"]]
- 0080e308 bytes 62261194
+ 0080e348 bytes 52271194
- 0080e334 ["INT_ADD", "register:40f0:8", ["const:80e334:8", "const:4:8"]]
- 0080e334 ["CALL", null, ["callee:00c58090:8"]]
+ 0080e374 ["INT_ADD", "register:40f0:8", ["const:80e374:8", "const:4:8"]]
+ 0080e374 ["CALL", null, ["callee:00c58090:8"]]
- 0080e334 bytes 57261194
+ 0080e374 bytes 47271194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97a552e1cba167ebf0e87c4e314e0c94"></a>

### [`0080e3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e3ac.md) → [`0080e3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e3ec.md) FUN_0080e3ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0080e5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e5b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e5f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e3ac.md#insn-0080e458) · [`0080e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e3ac.md#insn-0080e49c) · [`0080e4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e3ac.md#insn-0080e4e0)
- 新版 `0080e498`（命令位置の公開資料なし） · `0080e4dc`（命令位置の公開資料なし） · `0080e520`（命令位置の公開資料なし）

~~~diff
- 0080e458 ["INT_ADD", "register:40f0:8", ["const:80e458:8", "const:4:8"]]
- 0080e458 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080e498 ["INT_ADD", "register:40f0:8", ["const:80e498:8", "const:4:8"]]
+ 0080e498 ["CALL", null, ["callee:00c57e90:8"]]
- 0080e458 bytes 8e251194
+ 0080e498 bytes 7e261194
- 0080e49c ["INT_ADD", "register:40f0:8", ["const:80e49c:8", "const:4:8"]]
- 0080e49c ["CALL", null, ["callee:00c58090:8"]]
+ 0080e4dc ["INT_ADD", "register:40f0:8", ["const:80e4dc:8", "const:4:8"]]
+ 0080e4dc ["CALL", null, ["callee:00c58090:8"]]
- 0080e49c bytes fd251194
+ 0080e4dc bytes ed261194
- 0080e4e0 ["INT_ADD", "register:40f0:8", ["const:80e4e0:8", "const:4:8"]]
- 0080e4e0 ["CALL", null, ["callee:00c58090:8"]]
+ 0080e520 ["INT_ADD", "register:40f0:8", ["const:80e520:8", "const:4:8"]]
+ 0080e520 ["CALL", null, ["callee:00c58090:8"]]
- 0080e4e0 bytes ec251194
+ 0080e520 bytes dc261194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d64ca45f37b3294a5fceb784fdf703f6"></a>

### [`0080e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e5cc.md) → [`0080e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e60c.md) FUN_0080e60c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0080e6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e6ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0080e72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e72c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e5cc.md#insn-0080e638) · [`0080e65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e5cc.md#insn-0080e65c) · [`0080e688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e5cc.md#insn-0080e688)
- 新版 `0080e678`（命令位置の公開資料なし） · `0080e69c`（命令位置の公開資料なし） · `0080e6c8`（命令位置の公開資料なし）

~~~diff
- 0080e638 ["INT_ADD", "register:40f0:8", ["const:80e638:8", "const:4:8"]]
- 0080e638 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080e678 ["INT_ADD", "register:40f0:8", ["const:80e678:8", "const:4:8"]]
+ 0080e678 ["CALL", null, ["callee:00c57e90:8"]]
- 0080e638 bytes 16251194
+ 0080e678 bytes 06261194
- 0080e65c ["INT_ADD", "register:40f0:8", ["const:80e65c:8", "const:4:8"]]
- 0080e65c ["CALL", null, ["callee:00c58090:8"]]
+ 0080e69c ["INT_ADD", "register:40f0:8", ["const:80e69c:8", "const:4:8"]]
+ 0080e69c ["CALL", null, ["callee:00c58090:8"]]
- 0080e65c bytes 8d251194
+ 0080e69c bytes 7d261194
- 0080e688 ["INT_ADD", "register:40f0:8", ["const:80e688:8", "const:4:8"]]
- 0080e688 ["CALL", null, ["callee:00c58090:8"]]
+ 0080e6c8 ["INT_ADD", "register:40f0:8", ["const:80e6c8:8", "const:4:8"]]
+ 0080e6c8 ["CALL", null, ["callee:00c58090:8"]]
- 0080e688 bytes 82251194
+ 0080e6c8 bytes 72261194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7b6329cfdafac2a200ed83adbcefa72"></a>

### [`0080e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e700.md) → [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) FUN_0080e740

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0080c838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c838.md) [`0080d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d4c8.md) [`0080e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e700.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849c58.md) · 呼出先 2件 [`0080e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e700.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0080c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c878.md) [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) · 呼出先 2件 [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e700.md#insn-0080e720) · [`0080e72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e700.md#insn-0080e72c)
- 新版 `0080e760`（命令位置の公開資料なし） · `0080e76c`（命令位置の公開資料なし）

~~~diff
- 0080e720 ["INT_ADD", "register:40f0:8", ["const:80e720:8", "const:4:8"]]
- 0080e720 ["CALL", null, ["local:b0:8"]]
+ 0080e760 ["INT_ADD", "register:40f0:8", ["const:80e760:8", "const:4:8"]]
+ 0080e760 ["CALL", null, ["local:b0:8"]]
- 0080e720 bytes f8ffff97
+ 0080e760 bytes f8ffff97
- 0080e72c ["INT_ADD", "register:40f0:8", ["const:80e72c:8", "const:4:8"]]
- 0080e72c ["CALL", null, ["local:b0:8"]]
+ 0080e76c ["INT_ADD", "register:40f0:8", ["const:80e76c:8", "const:4:8"]]
+ 0080e76c ["CALL", null, ["local:b0:8"]]
- 0080e72c bytes f5ffff97
+ 0080e76c bytes f5ffff97
~~~


<a id="compare-96e3a600936d25ca28c1df21693fffdf"></a>

### [`0080e744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e744.md) → [`0080e784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e784.md) FUN_0080e784

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d4c8.md) [`00a662bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`00a664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a664b4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e744.md#insn-0080e7ec) · [`0080e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e744.md#insn-0080e834)
- 新版 `0080e82c`（命令位置の公開資料なし） · `0080e874`（命令位置の公開資料なし）

~~~diff
- 0080e7ec ["INT_ADD", "register:40f0:8", ["const:80e7ec:8", "const:4:8"]]
- 0080e7ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0080e82c ["INT_ADD", "register:40f0:8", ["const:80e82c:8", "const:4:8"]]
+ 0080e82c ["CALL", null, ["callee:00c57e90:8"]]
- 0080e7ec bytes a9241194
+ 0080e82c bytes 99251194
- 0080e834 ["INT_ADD", "register:40f0:8", ["const:80e834:8", "const:4:8"]]
- 0080e834 ["CALL", null, ["callee:0043bba4:8"]]
+ 0080e874 ["INT_ADD", "register:40f0:8", ["const:80e874:8", "const:4:8"]]
+ 0080e874 ["CALL", null, ["callee:0043bba4:8"]]
- 0080e834 bytes ccb4f097
+ 0080e874 bytes ccb4f097
~~~


<a id="compare-3cc4fbe2405922d03be12de3e283c0e6"></a>

### [`0080e860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e860.md) → [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) FUN_0080e8a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0080d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d4c8.md) [`0080e860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e860.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849c58.md) · 呼出先 2件 [`0080e860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e860.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) · 呼出先 2件 [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e860.md#insn-0080e880) · [`0080e88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e860.md#insn-0080e88c)
- 新版 `0080e8c0`（命令位置の公開資料なし） · `0080e8cc`（命令位置の公開資料なし）

~~~diff
- 0080e880 ["INT_ADD", "register:40f0:8", ["const:80e880:8", "const:4:8"]]
- 0080e880 ["CALL", null, ["local:b0:8"]]
+ 0080e8c0 ["INT_ADD", "register:40f0:8", ["const:80e8c0:8", "const:4:8"]]
+ 0080e8c0 ["CALL", null, ["local:b0:8"]]
- 0080e880 bytes f8ffff97
+ 0080e8c0 bytes f8ffff97
- 0080e88c ["INT_ADD", "register:40f0:8", ["const:80e88c:8", "const:4:8"]]
- 0080e88c ["CALL", null, ["local:b0:8"]]
+ 0080e8cc ["INT_ADD", "register:40f0:8", ["const:80e8cc:8", "const:4:8"]]
+ 0080e8cc ["CALL", null, ["local:b0:8"]]
- 0080e88c bytes f5ffff97
+ 0080e8cc bytes f5ffff97
~~~


<a id="compare-92295d3a45a6bbc3fe4fac0915285bfc"></a>

### [`0080e8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e8a4.md) → [`0080e8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8e4.md) FUN_0080e8e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d4c8.md) [`00a66ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66ec4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`00a670bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a670bc.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e8a4.md#insn-0080e94c) · [`0080e994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e8a4.md#insn-0080e994)
- 新版 `0080e98c`（命令位置の公開資料なし） · `0080e9d4`（命令位置の公開資料なし）

~~~diff
- 0080e94c ["INT_ADD", "register:40f0:8", ["const:80e94c:8", "const:4:8"]]
- 0080e94c ["CALL", null, ["callee:00c57e90:8"]]
+ 0080e98c ["INT_ADD", "register:40f0:8", ["const:80e98c:8", "const:4:8"]]
+ 0080e98c ["CALL", null, ["callee:00c57e90:8"]]
- 0080e94c bytes 51241194
+ 0080e98c bytes 41251194
- 0080e994 ["INT_ADD", "register:40f0:8", ["const:80e994:8", "const:4:8"]]
- 0080e994 ["CALL", null, ["callee:0043bba4:8"]]
+ 0080e9d4 ["INT_ADD", "register:40f0:8", ["const:80e9d4:8", "const:4:8"]]
+ 0080e9d4 ["CALL", null, ["callee:0043bba4:8"]]
- 0080e994 bytes 74b4f097
+ 0080e9d4 bytes 74b4f097
~~~


<a id="compare-3abf76f2e162b034750e3d27a98e14db"></a>

### [`0080e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e9c0.md) → [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md) FUN_0080ea00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0080d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d4c8.md) [`0080e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e9c0.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849c58.md) · 呼出先 2件 [`0080e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e9c0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) · 呼出先 2件 [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080e9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e9c0.md#insn-0080e9e0) · [`0080e9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e9c0.md#insn-0080e9ec)
- 新版 `0080ea20`（命令位置の公開資料なし） · `0080ea2c`（命令位置の公開資料なし）

~~~diff
- 0080e9e0 ["INT_ADD", "register:40f0:8", ["const:80e9e0:8", "const:4:8"]]
- 0080e9e0 ["CALL", null, ["local:b0:8"]]
+ 0080ea20 ["INT_ADD", "register:40f0:8", ["const:80ea20:8", "const:4:8"]]
+ 0080ea20 ["CALL", null, ["local:b0:8"]]
- 0080e9e0 bytes f8ffff97
+ 0080ea20 bytes f8ffff97
- 0080e9ec ["INT_ADD", "register:40f0:8", ["const:80e9ec:8", "const:4:8"]]
- 0080e9ec ["CALL", null, ["local:b0:8"]]
+ 0080ea2c ["INT_ADD", "register:40f0:8", ["const:80ea2c:8", "const:4:8"]]
+ 0080ea2c ["CALL", null, ["local:b0:8"]]
- 0080e9ec bytes f5ffff97
+ 0080ea2c bytes f5ffff97
~~~


<a id="compare-1680c3d9aa4646d12d77c4690a5e9561"></a>

### [`0080ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080ea04.md) → [`0080ea44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea44.md) FUN_0080ea44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d4c8.md) [`00a674e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a674e8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0080d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d508.md) [`00a676e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a676e0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080eaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080ea04.md#insn-0080eaac) · [`0080eaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080ea04.md#insn-0080eaf4)
- 新版 `0080eaec`（命令位置の公開資料なし） · `0080eb34`（命令位置の公開資料なし）

~~~diff
- 0080eaac ["INT_ADD", "register:40f0:8", ["const:80eaac:8", "const:4:8"]]
- 0080eaac ["CALL", null, ["callee:00c57e90:8"]]
+ 0080eaec ["INT_ADD", "register:40f0:8", ["const:80eaec:8", "const:4:8"]]
+ 0080eaec ["CALL", null, ["callee:00c57e90:8"]]
- 0080eaac bytes f9231194
+ 0080eaec bytes e9241194
- 0080eaf4 ["INT_ADD", "register:40f0:8", ["const:80eaf4:8", "const:4:8"]]
- 0080eaf4 ["CALL", null, ["callee:0043bba4:8"]]
+ 0080eb34 ["INT_ADD", "register:40f0:8", ["const:80eb34:8", "const:4:8"]]
+ 0080eb34 ["CALL", null, ["callee:0043bba4:8"]]
- 0080eaf4 bytes 1cb4f097
+ 0080eb34 bytes 1cb4f097
~~~


<a id="compare-f3f3da7aa759ca96e498b48dc8b3915e"></a>

### [`0080eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080eeb0.md) → [`0080eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080eef0.md) FUN_0080eef0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007c7b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7b80.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`007f1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007c7bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7bc0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`007f1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080eef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080eeb0.md#insn-0080eef0) · [`0080ef0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080eeb0.md#insn-0080ef0c) · [`0080ef38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080eeb0.md#insn-0080ef38)
- 新版 `0080ef30`（命令位置の公開資料なし） · `0080ef4c`（命令位置の公開資料なし） · `0080ef78`（命令位置の公開資料なし）

~~~diff
- 0080eef0 ["INT_ADD", "register:40f0:8", ["const:80eef0:8", "const:4:8"]]
- 0080eef0 ["CALL", null, ["callee:0048793c:8"]]
+ 0080ef30 ["INT_ADD", "register:40f0:8", ["const:80ef30:8", "const:4:8"]]
+ 0080ef30 ["CALL", null, ["callee:0048793c:8"]]
- 0080eef0 bytes 83e2f197
+ 0080ef30 bytes 83e2f197
- 0080ef0c ["COPY", "register:0:8", ["register:4040:8"]]
- 0080ef0c ["INT_ADD", "register:40f0:8", ["const:80ef0c:8", "const:4:8"]]
- 0080ef0c ["CALLIND", null, ["register:0:8"]]
+ 0080ef4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0080ef4c ["INT_ADD", "register:40f0:8", ["const:80ef4c:8", "const:4:8"]]
+ 0080ef4c ["CALLIND", null, ["register:0:8"]]
- 0080ef0c bytes 00013fd6
+ 0080ef4c bytes 00013fd6
- 0080ef38 ["INT_ADD", "register:40f0:8", ["const:80ef38:8", "const:4:8"]]
- 0080ef38 ["CALL", null, ["callee:0048793c:8"]]
+ 0080ef78 ["INT_ADD", "register:40f0:8", ["const:80ef78:8", "const:4:8"]]
+ 0080ef78 ["CALL", null, ["callee:0048793c:8"]]
- 0080ef38 bytes 71e2f197
+ 0080ef78 bytes 71e2f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4070a203ee7fa61046faf420eaa8b20e"></a>

### [`0080fa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fa8c.md) → [`0080facc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080facc.md) FUN_0080facc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0078597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md) [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) · 呼出先 1件 [`0081080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/0081080c.md)
- 新版 呼出元 9件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007859bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007859bc.md) [`00787518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787518.md) · 呼出先 1件 [`0081084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/0081084c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080fad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fa8c.md#insn-0080fad0)
- 新版 `0080fb10`（命令位置の公開資料なし）

~~~diff
- 0080fad0 ["INT_ADD", "register:40f0:8", ["const:80fad0:8", "const:4:8"]]
- 0080fad0 ["CALL", null, ["callee:0081084c:8"]]
+ 0080fb10 ["INT_ADD", "register:40f0:8", ["const:80fb10:8", "const:4:8"]]
+ 0080fb10 ["CALL", null, ["callee:0081084c:8"]]
- 0080fad0 bytes 4f030094
+ 0080fb10 bytes 4f030094
~~~


<a id="compare-80918592507adfa379f95474a797e7a9"></a>

### [`0080fad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fad4.md) → [`0080fb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fb14.md) FUN_0080fb14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`0081080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/0081080c.md) [`00810820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810820.md)
- 新版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0081084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/0081084c.md) [`00810860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080fb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fad4.md#insn-0080fb28) · [`0080fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fad4.md#insn-0080fb2c)
- 新版 `0080fb68`（命令位置の公開資料なし） · `0080fb6c`（命令位置の公開資料なし）

~~~diff
- 0080fb28 ["INT_ADD", "register:40f0:8", ["const:80fb28:8", "const:4:8"]]
- 0080fb28 ["CALL", null, ["callee:0081084c:8"]]
+ 0080fb68 ["INT_ADD", "register:40f0:8", ["const:80fb68:8", "const:4:8"]]
+ 0080fb68 ["CALL", null, ["callee:0081084c:8"]]
- 0080fb28 bytes 39030094
+ 0080fb68 bytes 39030094
- 0080fb2c ["INT_ADD", "register:40f0:8", ["const:80fb2c:8", "const:4:8"]]
- 0080fb2c ["CALL", null, ["callee:00810860:8"]]
+ 0080fb6c ["INT_ADD", "register:40f0:8", ["const:80fb6c:8", "const:4:8"]]
+ 0080fb6c ["CALL", null, ["callee:00810860:8"]]
- 0080fb2c bytes 3d030094
+ 0080fb6c bytes 3d030094
~~~


<a id="compare-a35a63ed336e065df382c8953b195eb7"></a>

### [`0080fb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fb40.md) → [`0080fb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fb80.md) FUN_0080fb80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`00810834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810834.md)
- 新版 呼出元 3件 [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`00810874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810874.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080fb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fb40.md#insn-0080fb68)
- 新版 `0080fba8`（命令位置の公開資料なし）

~~~diff
- 0080fb68 ["INT_ADD", "register:40f0:8", ["const:80fb68:8", "const:4:8"]]
- 0080fb68 ["CALL", null, ["callee:00810874:8"]]
+ 0080fba8 ["INT_ADD", "register:40f0:8", ["const:80fba8:8", "const:4:8"]]
+ 0080fba8 ["CALL", null, ["callee:00810874:8"]]
- 0080fb68 bytes 33030094
+ 0080fba8 bytes 33030094
~~~


<a id="compare-4fb0159971bef3f0a0ca6072c1424c8a"></a>

### [`00810510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810510.md) → [`00810550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810550.md) FUN_00810550

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080f0e8.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`007f1e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e78.md) [`00810788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810788.md) [`008107f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/008107f8.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`0080f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080f128.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1eb8.md) [`008107c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008107c8.md) [`00810838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810838.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008105bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810510.md#insn-008105bc) · [`00810608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810510.md#insn-00810608) · [`00810620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810510.md#insn-00810620)
- 新版 `008105fc`（命令位置の公開資料なし） · `00810648`（命令位置の公開資料なし） · `00810660`（命令位置の公開資料なし）

~~~diff
- 008105bc ["INT_ADD", "register:40f0:8", ["const:8105bc:8", "const:4:8"]]
- 008105bc ["CALL", null, ["callee:00c57e90:8"]]
+ 008105fc ["INT_ADD", "register:40f0:8", ["const:8105fc:8", "const:4:8"]]
+ 008105fc ["CALL", null, ["callee:00c57e90:8"]]
- 008105bc bytes 351d1194
+ 008105fc bytes 251e1194
- 00810608 ["INT_ADD", "register:40f0:8", ["const:810608:8", "const:4:8"]]
- 00810608 ["CALL", null, ["callee:00c57e90:8"]]
+ 00810648 ["INT_ADD", "register:40f0:8", ["const:810648:8", "const:4:8"]]
+ 00810648 ["CALL", null, ["callee:00c57e90:8"]]
- 00810608 bytes 221d1194
+ 00810648 bytes 121e1194
- 00810620 ["INT_ADD", "register:40f0:8", ["const:810620:8", "const:4:8"]]
- 00810620 ["CALL", null, ["callee:00c58000:8"]]
+ 00810660 ["INT_ADD", "register:40f0:8", ["const:810660:8", "const:4:8"]]
+ 00810660 ["CALL", null, ["callee:00c58000:8"]]
- 00810620 bytes 781d1194
+ 00810660 bytes 681e1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6201c9e147defe4f0c4113dba06a6f6f"></a>

### [`00810788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810788.md) → [`008107c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008107c8.md) FUN_008107c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00810510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810510.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00810550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810550.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008107ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810788.md#insn-008107ac)
- 新版 `008107ec`（命令位置の公開資料なし）

~~~diff
- 008107ac ["INT_ADD", "register:40f0:8", ["const:8107ac:8", "const:4:8"]]
- 008107ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 008107ec ["INT_ADD", "register:40f0:8", ["const:8107ec:8", "const:4:8"]]
+ 008107ec ["CALL", null, ["callee:00c57eb0:8"]]
- 008107ac bytes c11c1194
+ 008107ec bytes b11d1194
~~~


<a id="compare-3107a21ec8c3a02f9aa46c5df629251b"></a>

### [`00810848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810848.md) → [`00810888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810888.md) FUN_00810888

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080fb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fb6c.md) · 呼出先 5件 [`007f1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0080fbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fbac.md) · 呼出先 5件 [`007f1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081088c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810848.md#insn-0081088c) · [`008108d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810848.md#insn-008108d4) · [`008108fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810848.md#insn-008108fc)
- 新版 `008108cc`（命令位置の公開資料なし） · `00810914`（命令位置の公開資料なし） · `0081093c`（命令位置の公開資料なし）

~~~diff
- 0081088c ["INT_ADD", "register:40f0:8", ["const:81088c:8", "const:4:8"]]
- 0081088c ["CALL", null, ["callee:00c57eb0:8"]]
+ 008108cc ["INT_ADD", "register:40f0:8", ["const:8108cc:8", "const:4:8"]]
+ 008108cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0081088c bytes 891c1194
+ 008108cc bytes 791d1194
- 008108d4 ["INT_ADD", "register:40f0:8", ["const:8108d4:8", "const:4:8"]]
- 008108d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00810914 ["INT_ADD", "register:40f0:8", ["const:810914:8", "const:4:8"]]
+ 00810914 ["CALL", null, ["callee:00c57e90:8"]]
- 008108d4 bytes 6f1c1194
+ 00810914 bytes 5f1d1194
- 008108fc ["INT_ADD", "register:40f0:8", ["const:8108fc:8", "const:4:8"]]
- 008108fc ["CALL", null, ["callee:00c58000:8"]]
+ 0081093c ["INT_ADD", "register:40f0:8", ["const:81093c:8", "const:4:8"]]
+ 0081093c ["CALL", null, ["callee:00c58000:8"]]
- 008108fc bytes c11c1194
+ 0081093c bytes b11d1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-725f0b6cf907d3c27716ca08fb221508"></a>

### [`00810978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810978.md) → [`008109b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/008109b8.md) FUN_008109b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080fb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fb8c.md) · 呼出先 5件 [`007f1e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e78.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0080fbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fbcc.md) · 呼出先 5件 [`007f1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1eb8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008109bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810978.md#insn-008109bc) · [`00810a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810978.md#insn-00810a04) · [`00810a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810978.md#insn-00810a2c)
- 新版 `008109fc`（命令位置の公開資料なし） · `00810a44`（命令位置の公開資料なし） · `00810a6c`（命令位置の公開資料なし）

~~~diff
- 008109bc ["INT_ADD", "register:40f0:8", ["const:8109bc:8", "const:4:8"]]
- 008109bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 008109fc ["INT_ADD", "register:40f0:8", ["const:8109fc:8", "const:4:8"]]
+ 008109fc ["CALL", null, ["callee:00c57eb0:8"]]
- 008109bc bytes 3d1c1194
+ 008109fc bytes 2d1d1194
- 00810a04 ["INT_ADD", "register:40f0:8", ["const:810a04:8", "const:4:8"]]
- 00810a04 ["CALL", null, ["callee:00c57e90:8"]]
+ 00810a44 ["INT_ADD", "register:40f0:8", ["const:810a44:8", "const:4:8"]]
+ 00810a44 ["CALL", null, ["callee:00c57e90:8"]]
- 00810a04 bytes 231c1194
+ 00810a44 bytes 131d1194
- 00810a2c ["INT_ADD", "register:40f0:8", ["const:810a2c:8", "const:4:8"]]
- 00810a2c ["CALL", null, ["callee:00c58000:8"]]
+ 00810a6c ["INT_ADD", "register:40f0:8", ["const:810a6c:8", "const:4:8"]]
+ 00810a6c ["CALL", null, ["callee:00c58000:8"]]
- 00810a2c bytes 751c1194
+ 00810a6c bytes 651d1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c83fca0710de7cb78654dcde6ef34277"></a>

### [`00810aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md) → [`00810ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md) FUN_00810ae8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0080fbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fbc8.md) [`00810aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848350.md) · 呼出先 2件 [`00810aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0080fc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fc08.md) [`00810ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848390.md) · 呼出先 2件 [`00810ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00810ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md#insn-00810ac8) · [`00810ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md#insn-00810ad4) · [`00810b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md#insn-00810b10)
- 新版 `00810b08`（命令位置の公開資料なし） · `00810b14`（命令位置の公開資料なし） · `00810b50`（命令位置の公開資料なし）

~~~diff
- 00810ac8 ["INT_ADD", "register:40f0:8", ["const:810ac8:8", "const:4:8"]]
- 00810ac8 ["CALL", null, ["local:b0:8"]]
+ 00810b08 ["INT_ADD", "register:40f0:8", ["const:810b08:8", "const:4:8"]]
+ 00810b08 ["CALL", null, ["local:b0:8"]]
- 00810ac8 bytes f8ffff97
+ 00810b08 bytes f8ffff97
- 00810ad4 ["INT_ADD", "register:40f0:8", ["const:810ad4:8", "const:4:8"]]
- 00810ad4 ["CALL", null, ["local:b0:8"]]
+ 00810b14 ["INT_ADD", "register:40f0:8", ["const:810b14:8", "const:4:8"]]
+ 00810b14 ["CALL", null, ["local:b0:8"]]
- 00810ad4 bytes f5ffff97
+ 00810b14 bytes f5ffff97
- 00810b10 ["INT_ADD", "register:40f0:8", ["const:810b10:8", "const:4:8"]]
- 00810b10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00810b50 ["INT_ADD", "register:40f0:8", ["const:810b50:8", "const:4:8"]]
+ 00810b50 ["CALL", null, ["callee:00c57eb0:8"]]
- 00810b10 bytes e81b1194
+ 00810b50 bytes d81c1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aae8752daa5b074ac2983d94bdf4d4a6"></a>

### [`00810b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810b3c.md) → [`00810b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810b7c.md) FUN_00810b7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080fbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fbc8.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00810ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810ce4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0080fc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080fc08.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00810d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810d24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00810bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810b3c.md#insn-00810bc8) · [`00810c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810b3c.md#insn-00810c9c) · [`00810cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810b3c.md#insn-00810cb8)
- 新版 `00810c08`（命令位置の公開資料なし） · `00810cdc`（命令位置の公開資料なし） · `00810cf8`（命令位置の公開資料なし）

~~~diff
- 00810bc8 ["INT_ADD", "register:40f0:8", ["const:810bc8:8", "const:4:8"]]
- 00810bc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00810c08 ["INT_ADD", "register:40f0:8", ["const:810c08:8", "const:4:8"]]
+ 00810c08 ["CALL", null, ["callee:00c57e90:8"]]
- 00810bc8 bytes b21b1194
+ 00810c08 bytes a21c1194
- 00810c9c ["INT_ADD", "register:40f0:8", ["const:810c9c:8", "const:4:8"]]
- 00810c9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00810cdc ["INT_ADD", "register:40f0:8", ["const:810cdc:8", "const:4:8"]]
+ 00810cdc ["CALL", null, ["callee:00c57eb0:8"]]
- 00810c9c bytes 851b1194
+ 00810cdc bytes 751c1194
- 00810cb8 ["INT_ADD", "register:40f0:8", ["const:810cb8:8", "const:4:8"]]
- 00810cb8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00810cf8 ["INT_ADD", "register:40f0:8", ["const:810cf8:8", "const:4:8"]]
+ 00810cf8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00810cb8 bytes 7e1b1194
+ 00810cf8 bytes 6e1c1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49146be6f40011c9da25becdd38917fe"></a>

### [`00813914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813914.md) → [`00813954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813954.md) FUN_00813954

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813914.md#insn-00813930) · [`00813940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813914.md#insn-00813940)
- 新版 `00813970`（命令位置の公開資料なし） · `00813980`（命令位置の公開資料なし）

~~~diff
- 00813930 ["INT_ADD", "register:40f0:8", ["const:813930:8", "const:4:8"]]
- 00813930 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00813970 ["INT_ADD", "register:40f0:8", ["const:813970:8", "const:4:8"]]
+ 00813970 ["CALL", null, ["callee:00c57eb0:8"]]
- 00813930 bytes 60101194
+ 00813970 bytes 50111194
- 00813940 ["INT_ADD", "register:40f0:8", ["const:813940:8", "const:4:8"]]
- 00813940 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00813980 ["INT_ADD", "register:40f0:8", ["const:813980:8", "const:4:8"]]
+ 00813980 ["CALL", null, ["callee:00c57eb0:8"]]
- 00813940 bytes 5c101194
+ 00813980 bytes 4c111194
~~~


<a id="compare-0431449de2eee62d9798bdfecee2e557"></a>

### [`00813968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md) → [`008139a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md) FUN_008139a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`00813e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`00813e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md#insn-00813a10) · [`00813a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md#insn-00813a34) · [`00813a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md#insn-00813a48)
- 新版 `00813a50`（命令位置の公開資料なし） · `00813a74`（命令位置の公開資料なし） · `00813a88`（命令位置の公開資料なし）

~~~diff
- 00813a10 ["INT_ADD", "register:40f0:8", ["const:813a10:8", "const:4:8"]]
- 00813a10 ["CALL", null, ["callee:00813e50:8"]]
+ 00813a50 ["INT_ADD", "register:40f0:8", ["const:813a50:8", "const:4:8"]]
+ 00813a50 ["CALL", null, ["callee:00813e50:8"]]
- 00813a10 bytes 00010094
+ 00813a50 bytes 00010094
- 00813a34 ["INT_ADD", "register:40f0:8", ["const:813a34:8", "const:4:8"]]
- 00813a34 ["CALL", null, ["callee:00813fd8:8"]]
+ 00813a74 ["INT_ADD", "register:40f0:8", ["const:813a74:8", "const:4:8"]]
+ 00813a74 ["CALL", null, ["callee:00813fd8:8"]]
- 00813a34 bytes 59010094
+ 00813a74 bytes 59010094
- 00813a48 ["INT_ADD", "register:40f0:8", ["const:813a48:8", "const:4:8"]]
- 00813a48 ["CALL", null, ["callee:00813fd8:8"]]
+ 00813a88 ["INT_ADD", "register:40f0:8", ["const:813a88:8", "const:4:8"]]
+ 00813a88 ["CALL", null, ["callee:00813fd8:8"]]
- 00813a48 bytes 54010094
+ 00813a88 bytes 54010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fe2567a2451a5d553be3ff1a1063ae5"></a>

### [`00813dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813dbc.md) → [`00813dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813dfc.md) FUN_00813dfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813dbc.md#insn-00813dd8) · [`00813de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813dbc.md#insn-00813de8)
- 新版 `00813e18`（命令位置の公開資料なし） · `00813e28`（命令位置の公開資料なし）

~~~diff
- 00813dd8 ["INT_ADD", "register:40f0:8", ["const:813dd8:8", "const:4:8"]]
- 00813dd8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00813e18 ["INT_ADD", "register:40f0:8", ["const:813e18:8", "const:4:8"]]
+ 00813e18 ["CALL", null, ["callee:00c57eb0:8"]]
- 00813dd8 bytes 360f1194
+ 00813e18 bytes 26101194
- 00813de8 ["INT_ADD", "register:40f0:8", ["const:813de8:8", "const:4:8"]]
- 00813de8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00813e28 ["INT_ADD", "register:40f0:8", ["const:813e28:8", "const:4:8"]]
+ 00813e28 ["CALL", null, ["callee:00c57eb0:8"]]
- 00813de8 bytes 320f1194
+ 00813e28 bytes 22101194
~~~


<a id="compare-e59ab16e042877f09a4f37856b028fda"></a>

### [`00813e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md) → [`00813e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md) FUN_00813e50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00813968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md) · 呼出先 4件 [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`008139a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md) · 呼出先 4件 [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md#insn-00813e58) · [`00813e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md#insn-00813e70) · [`00813e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md#insn-00813e98)
- 新版 `00813e98`（命令位置の公開資料なし） · `00813eb0`（命令位置の公開資料なし） · `00813ed8`（命令位置の公開資料なし）

~~~diff
- 00813e58 ["INT_ADD", "register:40f0:8", ["const:813e58:8", "const:4:8"]]
- 00813e58 ["CALL", null, ["callee:00c57e90:8"]]
+ 00813e98 ["INT_ADD", "register:40f0:8", ["const:813e98:8", "const:4:8"]]
+ 00813e98 ["CALL", null, ["callee:00c57e90:8"]]
- 00813e58 bytes 0e0f1194
+ 00813e98 bytes fe0f1194
- 00813e70 ["INT_ADD", "register:40f0:8", ["const:813e70:8", "const:4:8"]]
- 00813e70 ["CALL", null, ["callee:00c58000:8"]]
+ 00813eb0 ["INT_ADD", "register:40f0:8", ["const:813eb0:8", "const:4:8"]]
+ 00813eb0 ["CALL", null, ["callee:00c58000:8"]]
- 00813e70 bytes 640f1194
+ 00813eb0 bytes 54101194
- 00813e98 ["INT_ADD", "register:40f0:8", ["const:813e98:8", "const:4:8"]]
- 00813e98 ["CALL", null, ["callee:00c57e90:8"]]
+ 00813ed8 ["INT_ADD", "register:40f0:8", ["const:813ed8:8", "const:4:8"]]
+ 00813ed8 ["CALL", null, ["callee:00c57e90:8"]]
- 00813e98 bytes fe0e1194
+ 00813ed8 bytes ee0f1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3f1ed75908f1282584e5199a0ada157"></a>

### [`00813f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813f98.md) → [`00813fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813fd8.md) FUN_00813fd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00813968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md) [`008b6e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e80.md) · 呼出先 5件 [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`008139a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/008139a8.md) [`008b6ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ec4.md) · 呼出先 5件 [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00813fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813f98.md#insn-00813fdc) · [`00814024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813f98.md#insn-00814024) · [`0081404c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813f98.md#insn-0081404c)
- 新版 `0081401c`（命令位置の公開資料なし） · `00814064`（命令位置の公開資料なし） · `0081408c`（命令位置の公開資料なし）

~~~diff
- 00813fdc ["INT_ADD", "register:40f0:8", ["const:813fdc:8", "const:4:8"]]
- 00813fdc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0081401c ["INT_ADD", "register:40f0:8", ["const:81401c:8", "const:4:8"]]
+ 0081401c ["CALL", null, ["callee:00c57eb0:8"]]
- 00813fdc bytes b50e1194
+ 0081401c bytes a50f1194
- 00814024 ["INT_ADD", "register:40f0:8", ["const:814024:8", "const:4:8"]]
- 00814024 ["CALL", null, ["callee:00c57e90:8"]]
+ 00814064 ["INT_ADD", "register:40f0:8", ["const:814064:8", "const:4:8"]]
+ 00814064 ["CALL", null, ["callee:00c57e90:8"]]
- 00814024 bytes 9b0e1194
+ 00814064 bytes 8b0f1194
- 0081404c ["INT_ADD", "register:40f0:8", ["const:81404c:8", "const:4:8"]]
- 0081404c ["CALL", null, ["callee:00c58000:8"]]
+ 0081408c ["INT_ADD", "register:40f0:8", ["const:81408c:8", "const:4:8"]]
+ 0081408c ["CALL", null, ["callee:00c58000:8"]]
- 0081404c bytes ed0e1194
+ 0081408c bytes dd0f1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd8014f6654c14a02856e8015caeb7b3"></a>

### [`008140c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md) → [`00814108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md) FUN_00814108

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00812e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00812/00812e8c.md) [`008140c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`008140c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00812ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00812/00812ecc.md) [`00814108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`00814108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814108.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008140e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md#insn-008140e4) · [`008140f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md#insn-008140f0) · [`00814100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md#insn-00814100)
- 新版 `00814124`（命令位置の公開資料なし） · `00814130`（命令位置の公開資料なし） · `00814140`（命令位置の公開資料なし）

~~~diff
- 008140e4 ["INT_ADD", "register:40f0:8", ["const:8140e4:8", "const:4:8"]]
- 008140e4 ["CALL", null, ["local:b0:8"]]
+ 00814124 ["INT_ADD", "register:40f0:8", ["const:814124:8", "const:4:8"]]
+ 00814124 ["CALL", null, ["local:b0:8"]]
- 008140e4 bytes f9ffff97
+ 00814124 bytes f9ffff97
- 008140f0 ["INT_ADD", "register:40f0:8", ["const:8140f0:8", "const:4:8"]]
- 008140f0 ["CALL", null, ["local:b0:8"]]
+ 00814130 ["INT_ADD", "register:40f0:8", ["const:814130:8", "const:4:8"]]
+ 00814130 ["CALL", null, ["local:b0:8"]]
- 008140f0 bytes f6ffff97
+ 00814130 bytes f6ffff97
- 00814100 ["INT_ADD", "register:40f0:8", ["const:814100:8", "const:4:8"]]
- 00814100 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00814140 ["INT_ADD", "register:40f0:8", ["const:814140:8", "const:4:8"]]
+ 00814140 ["CALL", null, ["callee:00c57eb0:8"]]
- 00814100 bytes 6c0e1194
+ 00814140 bytes 5c0f1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5a85846f74dd0286af4cd355dc57a91"></a>

### [`008155cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00815/008155cc.md) → [`0081560c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/0081560c.md) FUN_0081560c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00815764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00815/00815764.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008157a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/008157a4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081560c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00815/008155cc.md#insn-0081560c) · [`0081561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00815/008155cc.md#insn-0081561c) · [`0081562c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00815/008155cc.md#insn-0081562c)
- 新版 `0081564c`（命令位置の公開資料なし） · `0081565c`（命令位置の公開資料なし） · `0081566c`（命令位置の公開資料なし）

~~~diff
- 0081560c ["INT_ADD", "register:40f0:8", ["const:81560c:8", "const:4:8"]]
- 0081560c ["CALL", null, ["callee:0048793c:8"]]
+ 0081564c ["INT_ADD", "register:40f0:8", ["const:81564c:8", "const:4:8"]]
+ 0081564c ["CALL", null, ["callee:0048793c:8"]]
- 0081560c bytes bcc8f197
+ 0081564c bytes bcc8f197
- 0081561c ["INT_ADD", "register:40f0:8", ["const:81561c:8", "const:4:8"]]
- 0081561c ["CALL", null, ["callee:0048793c:8"]]
+ 0081565c ["INT_ADD", "register:40f0:8", ["const:81565c:8", "const:4:8"]]
+ 0081565c ["CALL", null, ["callee:0048793c:8"]]
- 0081561c bytes b8c8f197
+ 0081565c bytes b8c8f197
- 0081562c ["INT_ADD", "register:40f0:8", ["const:81562c:8", "const:4:8"]]
- 0081562c ["CALL", null, ["callee:0048793c:8"]]
+ 0081566c ["INT_ADD", "register:40f0:8", ["const:81566c:8", "const:4:8"]]
+ 0081566c ["CALL", null, ["callee:0048793c:8"]]
- 0081562c bytes b4c8f197
+ 0081566c bytes b4c8f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cad39833b1bbf57978053f10a000558b"></a>

### [`00817360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00817/00817360.md) → [`008173a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00817/008173a0.md) FUN_008173a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`006b8c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`006b8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c44.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008173e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00817/00817360.md#insn-008173e4) · [`00817410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00817/00817360.md#insn-00817410) · [`00817458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00817/00817360.md#insn-00817458)
- 新版 `00817424`（命令位置の公開資料なし） · `00817450`（命令位置の公開資料なし） · `00817498`（命令位置の公開資料なし）

~~~diff
- 008173e4 ["INT_ADD", "register:40f0:8", ["const:8173e4:8", "const:4:8"]]
- 008173e4 ["CALL", null, ["callee:0044108c:8"]]
+ 00817424 ["INT_ADD", "register:40f0:8", ["const:817424:8", "const:4:8"]]
+ 00817424 ["CALL", null, ["callee:0044108c:8"]]
- 008173e4 bytes 1aa7f097
+ 00817424 bytes 1aa7f097
- 00817410 ["INT_ADD", "register:40f0:8", ["const:817410:8", "const:4:8"]]
- 00817410 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00817450 ["INT_ADD", "register:40f0:8", ["const:817450:8", "const:4:8"]]
+ 00817450 ["CALL", null, ["callee:00c57eb0:8"]]
- 00817410 bytes a8011194
+ 00817450 bytes 98021194
- 00817458 ["COPY", "register:0:8", ["register:4040:8"]]
- 00817458 ["INT_ADD", "register:40f0:8", ["const:817458:8", "const:4:8"]]
- 00817458 ["CALLIND", null, ["register:0:8"]]
+ 00817498 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00817498 ["INT_ADD", "register:40f0:8", ["const:817498:8", "const:4:8"]]
+ 00817498 ["CALLIND", null, ["register:0:8"]]
- 00817458 bytes 00013fd6
+ 00817498 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fecdb19d41fcc15584a3a63d8baf5dde"></a>

### [`0081996c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/0081996c.md) → [`008199ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/008199ac.md) FUN_008199ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 1件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 1件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/0081996c.md#insn-00819988) · [`00819998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/0081996c.md#insn-00819998) · [`008199a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/0081996c.md#insn-008199a8)
- 新版 `008199c8`（命令位置の公開資料なし） · `008199d8`（命令位置の公開資料なし） · `008199e8`（命令位置の公開資料なし）

~~~diff
- 00819988 ["INT_ADD", "register:40f0:8", ["const:819988:8", "const:4:8"]]
- 00819988 ["CALL", null, ["callee:0048793c:8"]]
+ 008199c8 ["INT_ADD", "register:40f0:8", ["const:8199c8:8", "const:4:8"]]
+ 008199c8 ["CALL", null, ["callee:0048793c:8"]]
- 00819988 bytes ddb7f197
+ 008199c8 bytes ddb7f197
- 00819998 ["INT_ADD", "register:40f0:8", ["const:819998:8", "const:4:8"]]
- 00819998 ["CALL", null, ["callee:0048793c:8"]]
+ 008199d8 ["INT_ADD", "register:40f0:8", ["const:8199d8:8", "const:4:8"]]
+ 008199d8 ["CALL", null, ["callee:0048793c:8"]]
- 00819998 bytes d9b7f197
+ 008199d8 bytes d9b7f197
- 008199a8 ["INT_ADD", "register:40f0:8", ["const:8199a8:8", "const:4:8"]]
- 008199a8 ["CALL", null, ["callee:0048793c:8"]]
+ 008199e8 ["INT_ADD", "register:40f0:8", ["const:8199e8:8", "const:4:8"]]
+ 008199e8 ["CALL", null, ["callee:0048793c:8"]]
- 008199a8 bytes d5b7f197
+ 008199e8 bytes d5b7f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4c224396c1e6a571a18013c57c66c46"></a>

### [`00819a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819a3c.md) → [`00819a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819a7c.md) FUN_00819a7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819a3c.md#insn-00819aa4) · [`00819ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819a3c.md#insn-00819ab4) · [`00819ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819a3c.md#insn-00819ac4)
- 新版 `00819ae4`（命令位置の公開資料なし） · `00819af4`（命令位置の公開資料なし） · `00819b04`（命令位置の公開資料なし）

~~~diff
- 00819aa4 ["INT_ADD", "register:40f0:8", ["const:819aa4:8", "const:4:8"]]
- 00819aa4 ["CALL", null, ["callee:0048793c:8"]]
+ 00819ae4 ["INT_ADD", "register:40f0:8", ["const:819ae4:8", "const:4:8"]]
+ 00819ae4 ["CALL", null, ["callee:0048793c:8"]]
- 00819aa4 bytes 96b7f197
+ 00819ae4 bytes 96b7f197
- 00819ab4 ["INT_ADD", "register:40f0:8", ["const:819ab4:8", "const:4:8"]]
- 00819ab4 ["CALL", null, ["callee:0048793c:8"]]
+ 00819af4 ["INT_ADD", "register:40f0:8", ["const:819af4:8", "const:4:8"]]
+ 00819af4 ["CALL", null, ["callee:0048793c:8"]]
- 00819ab4 bytes 92b7f197
+ 00819af4 bytes 92b7f197
- 00819ac4 ["INT_ADD", "register:40f0:8", ["const:819ac4:8", "const:4:8"]]
- 00819ac4 ["CALL", null, ["callee:0048793c:8"]]
+ 00819b04 ["INT_ADD", "register:40f0:8", ["const:819b04:8", "const:4:8"]]
+ 00819b04 ["CALL", null, ["callee:0048793c:8"]]
- 00819ac4 bytes 8eb7f197
+ 00819b04 bytes 8eb7f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b8947c75c2211b1ba260a3ecc7cf1c2"></a>

### [`00819c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819c9c.md) → [`00819cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819cdc.md) FUN_00819cdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081c510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c510.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0081c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819c9c.md#insn-00819ce8) · [`00819cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819c9c.md#insn-00819cfc) · [`00819d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819c9c.md#insn-00819d04)
- 新版 `00819d28`（命令位置の公開資料なし） · `00819d3c`（命令位置の公開資料なし） · `00819d44`（命令位置の公開資料なし）

~~~diff
- 00819ce8 ["INT_ADD", "register:40f0:8", ["const:819ce8:8", "const:4:8"]]
- 00819ce8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00819d28 ["INT_ADD", "register:40f0:8", ["const:819d28:8", "const:4:8"]]
+ 00819d28 ["CALL", null, ["callee:00c53d00:8"]]
- 00819ce8 bytes fee61094
+ 00819d28 bytes f6e71094
- 00819cfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00819cfc ["INT_ADD", "register:40f0:8", ["const:819cfc:8", "const:4:8"]]
- 00819cfc ["CALLIND", null, ["register:0:8"]]
+ 00819d3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00819d3c ["INT_ADD", "register:40f0:8", ["const:819d3c:8", "const:4:8"]]
+ 00819d3c ["CALLIND", null, ["register:0:8"]]
- 00819cfc bytes 00013fd6
+ 00819d3c bytes 00013fd6
- 00819d04 ["INT_ADD", "register:40f0:8", ["const:819d04:8", "const:4:8"]]
- 00819d04 ["CALL", null, ["callee:00c57e80:8"]]
+ 00819d44 ["INT_ADD", "register:40f0:8", ["const:819d44:8", "const:4:8"]]
+ 00819d44 ["CALL", null, ["callee:00c57e80:8"]]
- 00819d04 bytes 5ff71094
+ 00819d44 bytes 4ff81094
~~~


<a id="compare-f522504153df0c65aa3465b4ee4da313"></a>

### [`00819d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d34.md) → [`00819d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819d74.md) FUN_00819d74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d34.md#insn-00819d50) · [`00819d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d34.md#insn-00819d70)
- 新版 `00819d90`（命令位置の公開資料なし） · `00819db0`（命令位置の公開資料なし）

~~~diff
- 00819d50 ["INT_ADD", "register:40f0:8", ["const:819d50:8", "const:4:8"]]
- 00819d50 ["CALL", null, ["callee:00c53d00:8"]]
+ 00819d90 ["INT_ADD", "register:40f0:8", ["const:819d90:8", "const:4:8"]]
+ 00819d90 ["CALL", null, ["callee:00c53d00:8"]]
- 00819d50 bytes e4e61094
+ 00819d90 bytes dce71094
- 00819d70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00819d70 ["INT_ADD", "register:40f0:8", ["const:819d70:8", "const:4:8"]]
- 00819d70 ["CALLIND", null, ["register:0:8"]]
+ 00819db0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00819db0 ["INT_ADD", "register:40f0:8", ["const:819db0:8", "const:4:8"]]
+ 00819db0 ["CALLIND", null, ["register:0:8"]]
- 00819d70 bytes 00013fd6
+ 00819db0 bytes 00013fd6
~~~


<a id="compare-351a0269ea04ac8ae35a2aad15a64ab6"></a>

### [`00819d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d84.md) → [`00819dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819dc4.md) FUN_00819dc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a550.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00830234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830234.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0081a590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a590.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00830274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830274.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00819de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d84.md#insn-00819de8) · [`00819dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d84.md#insn-00819dfc) · [`00819e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d84.md#insn-00819e10)
- 新版 `00819e28`（命令位置の公開資料なし） · `00819e3c`（命令位置の公開資料なし） · `00819e50`（命令位置の公開資料なし）

~~~diff
- 00819de8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00819de8 ["INT_ADD", "register:40f0:8", ["const:819de8:8", "const:4:8"]]
- 00819de8 ["CALLIND", null, ["register:0:8"]]
+ 00819e28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00819e28 ["INT_ADD", "register:40f0:8", ["const:819e28:8", "const:4:8"]]
+ 00819e28 ["CALLIND", null, ["register:0:8"]]
- 00819de8 bytes 00013fd6
+ 00819e28 bytes 00013fd6
- 00819dfc ["INT_ADD", "register:40f0:8", ["const:819dfc:8", "const:4:8"]]
- 00819dfc ["CALL", null, ["callee:0048793c:8"]]
+ 00819e3c ["INT_ADD", "register:40f0:8", ["const:819e3c:8", "const:4:8"]]
+ 00819e3c ["CALL", null, ["callee:0048793c:8"]]
- 00819dfc bytes c0b6f197
+ 00819e3c bytes c0b6f197
- 00819e10 ["INT_ADD", "register:40f0:8", ["const:819e10:8", "const:4:8"]]
- 00819e10 ["CALL", null, ["callee:0048793c:8"]]
+ 00819e50 ["INT_ADD", "register:40f0:8", ["const:819e50:8", "const:4:8"]]
+ 00819e50 ["CALL", null, ["callee:0048793c:8"]]
- 00819e10 bytes bbb6f197
+ 00819e50 bytes bbb6f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84ef29d520e7c2739356a48ce79449ad"></a>

### [`0081a550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a550.md) → [`0081a590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a590.md) FUN_0081a590

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 4件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00819d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 4件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00819dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819dc4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081a5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a550.md#insn-0081a5b8) · [`0081a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a550.md#insn-0081a5c8) · [`0081a5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a550.md#insn-0081a5d8)
- 新版 `0081a5f8`（命令位置の公開資料なし） · `0081a608`（命令位置の公開資料なし） · `0081a618`（命令位置の公開資料なし）

~~~diff
- 0081a5b8 ["INT_ADD", "register:40f0:8", ["const:81a5b8:8", "const:4:8"]]
- 0081a5b8 ["CALL", null, ["callee:0048793c:8"]]
+ 0081a5f8 ["INT_ADD", "register:40f0:8", ["const:81a5f8:8", "const:4:8"]]
+ 0081a5f8 ["CALL", null, ["callee:0048793c:8"]]
- 0081a5b8 bytes d1b4f197
+ 0081a5f8 bytes d1b4f197
- 0081a5c8 ["INT_ADD", "register:40f0:8", ["const:81a5c8:8", "const:4:8"]]
- 0081a5c8 ["CALL", null, ["callee:0048793c:8"]]
+ 0081a608 ["INT_ADD", "register:40f0:8", ["const:81a608:8", "const:4:8"]]
+ 0081a608 ["CALL", null, ["callee:0048793c:8"]]
- 0081a5c8 bytes cdb4f197
+ 0081a608 bytes cdb4f197
- 0081a5d8 ["INT_ADD", "register:40f0:8", ["const:81a5d8:8", "const:4:8"]]
- 0081a5d8 ["CALL", null, ["callee:0048793c:8"]]
+ 0081a618 ["INT_ADD", "register:40f0:8", ["const:81a618:8", "const:4:8"]]
+ 0081a618 ["CALL", null, ["callee:0048793c:8"]]
- 0081a5d8 bytes c9b4f197
+ 0081a618 bytes c9b4f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95c22317e289fb1c525c065a8de29777"></a>

### [`0081a6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a6a4.md) → [`0081a6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a6e4.md) FUN_0081a6e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081a6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a6a4.md#insn-0081a6f0) · [`0081a704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a6a4.md#insn-0081a704) · [`0081a70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a6a4.md#insn-0081a70c)
- 新版 `0081a730`（命令位置の公開資料なし） · `0081a744`（命令位置の公開資料なし） · `0081a74c`（命令位置の公開資料なし）

~~~diff
- 0081a6f0 ["INT_ADD", "register:40f0:8", ["const:81a6f0:8", "const:4:8"]]
- 0081a6f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0081a730 ["INT_ADD", "register:40f0:8", ["const:81a730:8", "const:4:8"]]
+ 0081a730 ["CALL", null, ["callee:00c53d00:8"]]
- 0081a6f0 bytes 7ce41094
+ 0081a730 bytes 74e51094
- 0081a704 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081a704 ["INT_ADD", "register:40f0:8", ["const:81a704:8", "const:4:8"]]
- 0081a704 ["CALLIND", null, ["register:0:8"]]
+ 0081a744 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081a744 ["INT_ADD", "register:40f0:8", ["const:81a744:8", "const:4:8"]]
+ 0081a744 ["CALLIND", null, ["register:0:8"]]
- 0081a704 bytes 00013fd6
+ 0081a744 bytes 00013fd6
- 0081a70c ["INT_ADD", "register:40f0:8", ["const:81a70c:8", "const:4:8"]]
- 0081a70c ["CALL", null, ["callee:00c57e80:8"]]
+ 0081a74c ["INT_ADD", "register:40f0:8", ["const:81a74c:8", "const:4:8"]]
+ 0081a74c ["CALL", null, ["callee:00c57e80:8"]]
- 0081a70c bytes ddf41094
+ 0081a74c bytes cdf51094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eedb07082fe2e4bfe295cf5996f6667"></a>

### [`0081a784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a784.md) → [`0081a7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a7c4.md) FUN_0081a7c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00830020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a784.md#insn-0081a7a0) · [`0081a7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a784.md#insn-0081a7c0)
- 新版 `0081a7e0`（命令位置の公開資料なし） · `0081a800`（命令位置の公開資料なし）

~~~diff
- 0081a7a0 ["INT_ADD", "register:40f0:8", ["const:81a7a0:8", "const:4:8"]]
- 0081a7a0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0081a7e0 ["INT_ADD", "register:40f0:8", ["const:81a7e0:8", "const:4:8"]]
+ 0081a7e0 ["CALL", null, ["callee:00c53d00:8"]]
- 0081a7a0 bytes 50e41094
+ 0081a7e0 bytes 48e51094
- 0081a7c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081a7c0 ["INT_ADD", "register:40f0:8", ["const:81a7c0:8", "const:4:8"]]
- 0081a7c0 ["CALLIND", null, ["register:0:8"]]
+ 0081a800 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081a800 ["INT_ADD", "register:40f0:8", ["const:81a800:8", "const:4:8"]]
+ 0081a800 ["CALLIND", null, ["register:0:8"]]
- 0081a7c0 bytes 00013fd6
+ 0081a800 bytes 00013fd6
~~~


<a id="compare-941d91a47d3e3519cfb12844e7843caf"></a>

### [`0081c264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c264.md) → [`0081c2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2a4.md) FUN_0081c2a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c264.md#insn-0081c280) · [`0081c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c264.md#insn-0081c2a0)
- 新版 `0081c2c0`（命令位置の公開資料なし） · `0081c2e0`（命令位置の公開資料なし）

~~~diff
- 0081c280 ["INT_ADD", "register:40f0:8", ["const:81c280:8", "const:4:8"]]
- 0081c280 ["CALL", null, ["callee:00c53d00:8"]]
+ 0081c2c0 ["INT_ADD", "register:40f0:8", ["const:81c2c0:8", "const:4:8"]]
+ 0081c2c0 ["CALL", null, ["callee:00c53d00:8"]]
- 0081c280 bytes 98dd1094
+ 0081c2c0 bytes 90de1094
- 0081c2a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081c2a0 ["INT_ADD", "register:40f0:8", ["const:81c2a0:8", "const:4:8"]]
- 0081c2a0 ["CALLIND", null, ["register:0:8"]]
+ 0081c2e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081c2e0 ["INT_ADD", "register:40f0:8", ["const:81c2e0:8", "const:4:8"]]
+ 0081c2e0 ["CALLIND", null, ["register:0:8"]]
- 0081c2a0 bytes 00013fd6
+ 0081c2e0 bytes 00013fd6
~~~


<a id="compare-2208b0e7ba48c529990ce89507547568"></a>

### [`0081c2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md) → [`0081c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md) FUN_0081c2f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`0082d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d768.md) [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md) [`00830618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830618.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) [`00830658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830658.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md#insn-0081c2d4) · [`0081c310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md#insn-0081c310) · [`0081c324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md#insn-0081c324)
- 新版 `0081c314`（命令位置の公開資料なし） · `0081c350`（命令位置の公開資料なし） · `0081c364`（命令位置の公開資料なし）

~~~diff
- 0081c2d4 ["INT_ADD", "register:40f0:8", ["const:81c2d4:8", "const:4:8"]]
- 0081c2d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0081c314 ["INT_ADD", "register:40f0:8", ["const:81c314:8", "const:4:8"]]
+ 0081c314 ["CALL", null, ["callee:00c57eb0:8"]]
- 0081c2d4 bytes f7ed1094
+ 0081c314 bytes e7ee1094
- 0081c310 ["INT_ADD", "register:40f0:8", ["const:81c310:8", "const:4:8"]]
- 0081c310 ["CALL", null, ["callee:00c53d00:8"]]
+ 0081c350 ["INT_ADD", "register:40f0:8", ["const:81c350:8", "const:4:8"]]
+ 0081c350 ["CALL", null, ["callee:00c53d00:8"]]
- 0081c310 bytes 74dd1094
+ 0081c350 bytes 6cde1094
- 0081c324 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081c324 ["INT_ADD", "register:40f0:8", ["const:81c324:8", "const:4:8"]]
- 0081c324 ["CALLIND", null, ["register:0:8"]]
+ 0081c364 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081c364 ["INT_ADD", "register:40f0:8", ["const:81c364:8", "const:4:8"]]
+ 0081c364 ["CALLIND", null, ["register:0:8"]]
- 0081c324 bytes 00013fd6
+ 0081c364 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f4acac35c3d8054edf2fd45b052054c"></a>

### [`0081c3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c3cc.md) → [`0081c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c40c.md) FUN_0081c40c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c3cc.md#insn-0081c404) · [`0081c44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c3cc.md#insn-0081c44c) · [`0081c460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c3cc.md#insn-0081c460)
- 新版 `0081c444`（命令位置の公開資料なし） · `0081c48c`（命令位置の公開資料なし） · `0081c4a0`（命令位置の公開資料なし）

~~~diff
- 0081c404 ["INT_ADD", "register:40f0:8", ["const:81c404:8", "const:4:8"]]
- 0081c404 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0081c444 ["INT_ADD", "register:40f0:8", ["const:81c444:8", "const:4:8"]]
+ 0081c444 ["CALL", null, ["callee:00c57eb0:8"]]
- 0081c404 bytes abed1094
+ 0081c444 bytes 9bee1094
- 0081c44c ["INT_ADD", "register:40f0:8", ["const:81c44c:8", "const:4:8"]]
- 0081c44c ["CALL", null, ["callee:00c53d00:8"]]
+ 0081c48c ["INT_ADD", "register:40f0:8", ["const:81c48c:8", "const:4:8"]]
+ 0081c48c ["CALL", null, ["callee:00c53d00:8"]]
- 0081c44c bytes 25dd1094
+ 0081c48c bytes 1dde1094
- 0081c460 ["COPY", "register:0:8", ["register:4040:8"]]
- 0081c460 ["INT_ADD", "register:40f0:8", ["const:81c460:8", "const:4:8"]]
- 0081c460 ["CALLIND", null, ["register:0:8"]]
+ 0081c4a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0081c4a0 ["INT_ADD", "register:40f0:8", ["const:81c4a0:8", "const:4:8"]]
+ 0081c4a0 ["CALLIND", null, ["register:0:8"]]
- 0081c460 bytes 00013fd6
+ 0081c4a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afae573c6a3373ca75c080241e802007"></a>

### [`0081c510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c510.md) → [`0081c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md) FUN_0081c550

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 10件 [`00819c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819c9c.md) [`0082fd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fd2c.md) [`0083000c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083000c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 10件 [`00819cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819cdc.md) [`0082fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md) [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c510.md#insn-0081c564) · [`0081c5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c510.md#insn-0081c5ac) · [`0081c5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c510.md#insn-0081c5e0)
- 新版 `0081c5a4`（命令位置の公開資料なし） · `0081c5ec`（命令位置の公開資料なし） · `0081c620`（命令位置の公開資料なし）

~~~diff
- 0081c564 ["INT_ADD", "register:40f0:8", ["const:81c564:8", "const:4:8"]]
- 0081c564 ["CALL", null, ["callee:00c57e90:8"]]
+ 0081c5a4 ["INT_ADD", "register:40f0:8", ["const:81c5a4:8", "const:4:8"]]
+ 0081c5a4 ["CALL", null, ["callee:00c57e90:8"]]
- 0081c564 bytes 4bed1094
+ 0081c5a4 bytes 3bee1094
- 0081c5ac ["INT_ADD", "register:40f0:8", ["const:81c5ac:8", "const:4:8"]]
- 0081c5ac ["CALL", null, ["callee:00c53cd0:8"]]
+ 0081c5ec ["INT_ADD", "register:40f0:8", ["const:81c5ec:8", "const:4:8"]]
+ 0081c5ec ["CALL", null, ["callee:00c53cd0:8"]]
- 0081c5ac bytes c1dc1094
+ 0081c5ec bytes b9dd1094
- 0081c5e0 ["INT_ADD", "register:40f0:8", ["const:81c5e0:8", "const:4:8"]]
- 0081c5e0 ["CALL", null, ["callee:0082fd6c:8"]]
+ 0081c620 ["INT_ADD", "register:40f0:8", ["const:81c620:8", "const:4:8"]]
+ 0081c620 ["CALL", null, ["callee:0082fd6c:8"]]
- 0081c5e0 bytes d34d0094
+ 0081c620 bytes d34d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-090e270c91583e4228be73ee7dc23607"></a>

### [`0081c6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c6c8.md) → [`0081c708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c708.md) FUN_0081c708

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008215f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/008215f4.md) · 呼出先 5件 [`00830234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830234.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00821634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00821/00821634.md) · 呼出先 5件 [`00830274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830274.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c6c8.md#insn-0081c768) · [`0081c780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c6c8.md#insn-0081c780) · [`0081c790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c6c8.md#insn-0081c790)
- 新版 `0081c7a8`（命令位置の公開資料なし） · `0081c7c0`（命令位置の公開資料なし） · `0081c7d0`（命令位置の公開資料なし）

~~~diff
- 0081c768 ["INT_ADD", "register:40f0:8", ["const:81c768:8", "const:4:8"]]
- 0081c768 ["CALL", null, ["callee:00c57e90:8"]]
+ 0081c7a8 ["INT_ADD", "register:40f0:8", ["const:81c7a8:8", "const:4:8"]]
+ 0081c7a8 ["CALL", null, ["callee:00c57e90:8"]]
- 0081c768 bytes caec1094
+ 0081c7a8 bytes baed1094
- 0081c780 ["INT_ADD", "register:40f0:8", ["const:81c780:8", "const:4:8"]]
- 0081c780 ["CALL", null, ["callee:00c58000:8"]]
+ 0081c7c0 ["INT_ADD", "register:40f0:8", ["const:81c7c0:8", "const:4:8"]]
+ 0081c7c0 ["CALL", null, ["callee:00c58000:8"]]
- 0081c780 bytes 20ed1094
+ 0081c7c0 bytes 10ee1094
- 0081c790 ["INT_ADD", "register:40f0:8", ["const:81c790:8", "const:4:8"]]
- 0081c790 ["CALL", null, ["callee:00830274:8"]]
+ 0081c7d0 ["INT_ADD", "register:40f0:8", ["const:81c7d0:8", "const:4:8"]]
+ 0081c7d0 ["CALL", null, ["callee:00830274:8"]]
- 0081c790 bytes a94e0094
+ 0081c7d0 bytes a94e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52814a1bd2db7a8bc53e1ff05929cd8f"></a>

### [`0081c7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c7b4.md) → [`0081c7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md) FUN_0081c7f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00822db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822db0.md) [`00822ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822ef0.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00822df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822df0.md) [`00822f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822f30.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081c868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c7b4.md#insn-0081c868) · [`0081c89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c7b4.md#insn-0081c89c)
- 新版 `0081c8a8`（命令位置の公開資料なし） · `0081c8dc`（命令位置の公開資料なし）

~~~diff
- 0081c868 ["INT_ADD", "register:40f0:8", ["const:81c868:8", "const:4:8"]]
- 0081c868 ["CALL", null, ["callee:00c57e90:8"]]
+ 0081c8a8 ["INT_ADD", "register:40f0:8", ["const:81c8a8:8", "const:4:8"]]
+ 0081c8a8 ["CALL", null, ["callee:00c57e90:8"]]
- 0081c868 bytes 8aec1094
+ 0081c8a8 bytes 7aed1094
- 0081c89c ["INT_ADD", "register:40f0:8", ["const:81c89c:8", "const:4:8"]]
- 0081c89c ["CALL", null, ["callee:0043bba4:8"]]
+ 0081c8dc ["INT_ADD", "register:40f0:8", ["const:81c8dc:8", "const:4:8"]]
+ 0081c8dc ["CALL", null, ["callee:0043bba4:8"]]
- 0081c89c bytes b27cf097
+ 0081c8dc bytes b27cf097
~~~


<a id="compare-fe333fbda207eb192910719d85ddbc83"></a>

### [`0081d18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d18c.md) → [`0081d1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1cc.md) FUN_0081d1cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0072b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b104.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b3dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md)
- 新版 呼出元 3件 [`0072b144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b144.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b3e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081d194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d18c.md#insn-0081d194)
- 新版 `0081d1d4`（命令位置の公開資料なし）

~~~diff
- 0081d194 ["INT_ADD", "register:40f0:8", ["const:81d194:8", "const:4:8"]]
- 0081d194 ["CALL", null, ["callee:008514f8:8"]]
+ 0081d1d4 ["INT_ADD", "register:40f0:8", ["const:81d1d4:8", "const:4:8"]]
+ 0081d1d4 ["CALL", null, ["callee:008514f8:8"]]
- 0081d194 bytes c9d00094
+ 0081d1d4 bytes c9d00094
~~~


<a id="compare-61f80659386a84feae50214471df3e48"></a>

### [`0081d1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d1ac.md) → [`0081d1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1ec.md) FUN_0081d1ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`007add18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00816b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00816/00816b30.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`007add58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081d214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d1ac.md#insn-0081d214) · [`0081d248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d1ac.md#insn-0081d248) · [`0081d2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d1ac.md#insn-0081d2d8)
- 新版 `0081d254`（命令位置の公開資料なし） · `0081d288`（命令位置の公開資料なし） · `0081d318`（命令位置の公開資料なし）

~~~diff
- 0081d214 ["INT_ADD", "register:40f0:8", ["const:81d214:8", "const:4:8"]]
- 0081d214 ["CALL", null, ["callee:00c57e90:8"]]
+ 0081d254 ["INT_ADD", "register:40f0:8", ["const:81d254:8", "const:4:8"]]
+ 0081d254 ["CALL", null, ["callee:00c57e90:8"]]
- 0081d214 bytes 1fea1094
+ 0081d254 bytes 0feb1094
- 0081d248 ["INT_ADD", "register:40f0:8", ["const:81d248:8", "const:4:8"]]
- 0081d248 ["CALL", null, ["callee:0043bba4:8"]]
+ 0081d288 ["INT_ADD", "register:40f0:8", ["const:81d288:8", "const:4:8"]]
+ 0081d288 ["CALL", null, ["callee:0043bba4:8"]]
- 0081d248 bytes 477af097
+ 0081d288 bytes 477af097
- 0081d2d8 ["INT_ADD", "register:40f0:8", ["const:81d2d8:8", "const:4:8"]]
- 0081d2d8 ["CALL", null, ["callee:008514f8:8"]]
+ 0081d318 ["INT_ADD", "register:40f0:8", ["const:81d318:8", "const:4:8"]]
+ 0081d318 ["CALL", null, ["callee:008514f8:8"]]
- 0081d2d8 bytes 78d00094
+ 0081d318 bytes 78d00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b19326d91a55db134f41b49508e62f3"></a>

### [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) → [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) FUN_0082071c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00820258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/00820258.md) [`00822c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822c58.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`00830020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md) · 呼出先 10件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00819d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d34.md) [`0083000c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083000c.md) [`00830130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830130.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 4件 [`00820298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/00820298.md) [`00822c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822c98.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) · 呼出先 10件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00819d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00819/00819d74.md) [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00830170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830170.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00820734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md#insn-00820734) · [`0082074c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md#insn-0082074c) · [`00820778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md#insn-00820778)
- 新版 `00820774`（命令位置の公開資料なし） · `0082078c`（命令位置の公開資料なし） · `008207b8`（命令位置の公開資料なし）

~~~diff
- 00820734 ["INT_ADD", "register:40f0:8", ["const:820734:8", "const:4:8"]]
- 00820734 ["CALL", null, ["callee:00c57e90:8"]]
+ 00820774 ["INT_ADD", "register:40f0:8", ["const:820774:8", "const:4:8"]]
+ 00820774 ["CALL", null, ["callee:00c57e90:8"]]
- 00820734 bytes d7dc1094
+ 00820774 bytes c7dd1094
- 0082074c ["INT_ADD", "register:40f0:8", ["const:82074c:8", "const:4:8"]]
- 0082074c ["CALL", null, ["callee:00c58000:8"]]
+ 0082078c ["INT_ADD", "register:40f0:8", ["const:82078c:8", "const:4:8"]]
+ 0082078c ["CALL", null, ["callee:00c58000:8"]]
- 0082074c bytes 2ddd1094
+ 0082078c bytes 1dde1094
- 00820778 ["INT_ADD", "register:40f0:8", ["const:820778:8", "const:4:8"]]
- 00820778 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008207b8 ["INT_ADD", "register:40f0:8", ["const:8207b8:8", "const:4:8"]]
+ 008207b8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00820778 bytes 4ecc1094
+ 008207b8 bytes 46cd1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff29a93b6c60974fd663bb10f842325b"></a>

### [`00822db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822db0.md) → [`00822df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822df0.md) FUN_00822df0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0081c7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c7b4.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0081c7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00822e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822db0.md#insn-00822e20) · [`00822e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822db0.md#insn-00822e54) · [`00822eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822db0.md#insn-00822eec)
- 新版 `00822e60`（命令位置の公開資料なし） · `00822e94`（命令位置の公開資料なし） · `00822f2c`（命令位置の公開資料なし）

~~~diff
- 00822e20 ["INT_ADD", "register:40f0:8", ["const:822e20:8", "const:4:8"]]
- 00822e20 ["CALL", null, ["callee:00c58450:8"]]
+ 00822e60 ["INT_ADD", "register:40f0:8", ["const:822e60:8", "const:4:8"]]
+ 00822e60 ["CALL", null, ["callee:00c58450:8"]]
- 00822e20 bytes 8cd41094
+ 00822e60 bytes 7cd51094
- 00822e54 ["INT_ADD", "register:40f0:8", ["const:822e54:8", "const:4:8"]]
- 00822e54 ["CALL", null, ["callee:00c58450:8"]]
+ 00822e94 ["INT_ADD", "register:40f0:8", ["const:822e94:8", "const:4:8"]]
+ 00822e94 ["CALL", null, ["callee:00c58450:8"]]
- 00822e54 bytes 7fd41094
+ 00822e94 bytes 6fd51094
- 00822eec ["INT_ADD", "register:40f0:8", ["const:822eec:8", "const:4:8"]]
- 00822eec ["CALL", null, ["callee:0049f3f0:8"]]
+ 00822f2c ["INT_ADD", "register:40f0:8", ["const:822f2c:8", "const:4:8"]]
+ 00822f2c ["CALL", null, ["callee:0049f3f0:8"]]
- 00822eec bytes 31f1f197
+ 00822f2c bytes 31f1f197
~~~


<a id="compare-3864b1d0126f888f3b4ea33802821ff8"></a>

### [`00822ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822ef0.md) → [`00822f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00822/00822f30.md) FUN_00822f30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0081c7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c7b4.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0081c7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c7f4.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00822f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822ef0.md#insn-00822f80) · [`00822fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822ef0.md#insn-00822fcc)
- 新版 `00822fc0`（命令位置の公開資料なし） · `0082300c`（命令位置の公開資料なし）

~~~diff
- 00822f80 ["INT_ADD", "register:40f0:8", ["const:822f80:8", "const:4:8"]]
- 00822f80 ["CALL", null, ["callee:00c58450:8"]]
+ 00822fc0 ["INT_ADD", "register:40f0:8", ["const:822fc0:8", "const:4:8"]]
+ 00822fc0 ["CALL", null, ["callee:00c58450:8"]]
- 00822f80 bytes 34d41094
+ 00822fc0 bytes 24d51094
- 00822fcc ["INT_ADD", "register:40f0:8", ["const:822fcc:8", "const:4:8"]]
- 00822fcc ["CALL", null, ["callee:0049f3f0:8"]]
+ 0082300c ["INT_ADD", "register:40f0:8", ["const:82300c:8", "const:4:8"]]
+ 0082300c ["CALL", null, ["callee:0049f3f0:8"]]
- 00822fcc bytes f9f0f197
+ 0082300c bytes f9f0f197
~~~


<a id="compare-f52f375704268c7858b700a363b6b1c7"></a>

### [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) → [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) FUN_00823010

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0082eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md) [`0082ebd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ebd4.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) [`00818d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00818/00818d00.md)
- 新版 呼出元 6件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0082eb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md) [`0082ec14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ec14.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`00816b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00816/00816b30.md) [`00818d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00818/00818d40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md#insn-0082305c) · [`0082312c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md#insn-0082312c) · [`0082313c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md#insn-0082313c)
- 新版 `0082309c`（命令位置の公開資料なし） · `0082316c`（命令位置の公開資料なし） · `0082317c`（命令位置の公開資料なし）

~~~diff
- 0082305c ["INT_ADD", "register:40f0:8", ["const:82305c:8", "const:4:8"]]
- 0082305c ["CALL", null, ["callee:008307f8:8"]]
+ 0082309c ["INT_ADD", "register:40f0:8", ["const:82309c:8", "const:4:8"]]
+ 0082309c ["CALL", null, ["callee:008307f8:8"]]
- 0082305c bytes d7350094
+ 0082309c bytes d7350094
- 0082312c ["INT_ADD", "register:40f0:8", ["const:82312c:8", "const:4:8"]]
- 0082312c ["CALL", null, ["callee:00822c98:8"]]
+ 0082316c ["INT_ADD", "register:40f0:8", ["const:82316c:8", "const:4:8"]]
+ 0082316c ["CALL", null, ["callee:00822c98:8"]]
- 0082312c bytes cbfeff97
+ 0082316c bytes cbfeff97
- 0082313c ["INT_ADD", "register:40f0:8", ["const:82313c:8", "const:4:8"]]
- 0082313c ["CALL", null, ["callee:0082071c:8"]]
+ 0082317c ["INT_ADD", "register:40f0:8", ["const:82317c:8", "const:4:8"]]
+ 0082317c ["CALL", null, ["callee:0082071c:8"]]
- 0082313c bytes 68f5ff97
+ 0082317c bytes 68f5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72aeb07ef3e0fa5cb3ff09a4fb3b086a"></a>

### [`008242f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md) → [`00824330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md) FUN_00824330

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00826d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d7c.md) · 呼出先 2件 [`0080234c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00826dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) · 呼出先 2件 [`0080238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00824300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md#insn-00824300) · [`00824314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md#insn-00824314) · [`00824320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md#insn-00824320)
- 新版 `00824340`（命令位置の公開資料なし） · `00824354`（命令位置の公開資料なし） · `00824360`（命令位置の公開資料なし）

~~~diff
- 00824300 ["INT_ADD", "register:40f0:8", ["const:824300:8", "const:4:8"]]
- 00824300 ["CALL", null, ["callee:008514f8:8"]]
+ 00824340 ["INT_ADD", "register:40f0:8", ["const:824340:8", "const:4:8"]]
+ 00824340 ["CALL", null, ["callee:008514f8:8"]]
- 00824300 bytes 6eb40094
+ 00824340 bytes 6eb40094
- 00824314 ["INT_ADD", "register:40f0:8", ["const:824314:8", "const:4:8"]]
- 00824314 ["CALL", null, ["callee:0080238c:8"]]
+ 00824354 ["INT_ADD", "register:40f0:8", ["const:824354:8", "const:4:8"]]
+ 00824354 ["CALL", null, ["callee:0080238c:8"]]
- 00824314 bytes 0e78ff97
+ 00824354 bytes 0e78ff97
- 00824320 ["INT_ADD", "register:40f0:8", ["const:824320:8", "const:4:8"]]
- 00824320 ["CALL", null, ["callee:008514f8:8"]]
+ 00824360 ["INT_ADD", "register:40f0:8", ["const:824360:8", "const:4:8"]]
+ 00824360 ["CALL", null, ["callee:008514f8:8"]]
- 00824320 bytes 66b40094
+ 00824360 bytes 66b40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a5a4db82e8dfcc36b2b94450a6278a8"></a>

### [`0082449c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md) → [`008244dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md) FUN_008244dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00826d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d7c.md) · 呼出先 2件 [`0080234c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00826dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) · 呼出先 2件 [`0080238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008244ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md#insn-008244ac) · [`008244c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md#insn-008244c4) · [`008244cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md#insn-008244cc)
- 新版 `008244ec`（命令位置の公開資料なし） · `00824504`（命令位置の公開資料なし） · `0082450c`（命令位置の公開資料なし）

~~~diff
- 008244ac ["INT_ADD", "register:40f0:8", ["const:8244ac:8", "const:4:8"]]
- 008244ac ["CALL", null, ["callee:008514f8:8"]]
+ 008244ec ["INT_ADD", "register:40f0:8", ["const:8244ec:8", "const:4:8"]]
+ 008244ec ["CALL", null, ["callee:008514f8:8"]]
- 008244ac bytes 03b40094
+ 008244ec bytes 03b40094
- 008244c4 ["INT_ADD", "register:40f0:8", ["const:8244c4:8", "const:4:8"]]
- 008244c4 ["CALL", null, ["callee:0080238c:8"]]
+ 00824504 ["INT_ADD", "register:40f0:8", ["const:824504:8", "const:4:8"]]
+ 00824504 ["CALL", null, ["callee:0080238c:8"]]
- 008244c4 bytes a277ff97
+ 00824504 bytes a277ff97
- 008244cc ["INT_ADD", "register:40f0:8", ["const:8244cc:8", "const:4:8"]]
- 008244cc ["CALL", null, ["callee:008514f8:8"]]
+ 0082450c ["INT_ADD", "register:40f0:8", ["const:82450c:8", "const:4:8"]]
+ 0082450c ["CALL", null, ["callee:008514f8:8"]]
- 008244cc bytes fbb30094
+ 0082450c bytes fbb30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5090b53d0614ad2c46672a0e658a8cf4"></a>

### [`0082b4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082b4b8.md) → [`0082b4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b4f8.md) FUN_0082b4f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00831ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831ab8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0082ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00831af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831af8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082b508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082b4b8.md#insn-0082b508) · [`0082b538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082b4b8.md#insn-0082b538) · [`0082b54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082b4b8.md#insn-0082b54c)
- 新版 `0082b548`（命令位置の公開資料なし） · `0082b578`（命令位置の公開資料なし） · `0082b58c`（命令位置の公開資料なし）

~~~diff
- 0082b508 ["INT_ADD", "register:40f0:8", ["const:82b508:8", "const:4:8"]]
- 0082b508 ["CALL", null, ["callee:0043bba4:8"]]
+ 0082b548 ["INT_ADD", "register:40f0:8", ["const:82b548:8", "const:4:8"]]
+ 0082b548 ["CALL", null, ["callee:0043bba4:8"]]
- 0082b508 bytes 9741f097
+ 0082b548 bytes 9741f097
- 0082b538 ["INT_ADD", "register:40f0:8", ["const:82b538:8", "const:4:8"]]
- 0082b538 ["CALL", null, ["callee:00831af8:8"]]
+ 0082b578 ["INT_ADD", "register:40f0:8", ["const:82b578:8", "const:4:8"]]
+ 0082b578 ["CALL", null, ["callee:00831af8:8"]]
- 0082b538 bytes 60190094
+ 0082b578 bytes 60190094
- 0082b54c ["INT_ADD", "register:40f0:8", ["const:82b54c:8", "const:4:8"]]
- 0082b54c ["CALL", null, ["callee:00c57e90:8"]]
+ 0082b58c ["INT_ADD", "register:40f0:8", ["const:82b58c:8", "const:4:8"]]
+ 0082b58c ["CALL", null, ["callee:00c57e90:8"]]
- 0082b54c bytes 51b11094
+ 0082b58c bytes 41b21094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abdb2c5836e24708d82b878625316dea"></a>

### [`0082ccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccbc.md) → [`0082ccfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082ccfc.md) FUN_0082ccfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009dce3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dce3c.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac8440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8440.md)
- 新版 呼出元 1件 [`009dcfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcfd8.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ac863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac863c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082ccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccbc.md#insn-0082ccc4)
- 新版 `0082cd04`（命令位置の公開資料なし）

~~~diff
- 0082ccc4 ["INT_ADD", "register:40f0:8", ["const:82ccc4:8", "const:4:8"]]
- 0082ccc4 ["CALL", null, ["callee:008514f8:8"]]
+ 0082cd04 ["INT_ADD", "register:40f0:8", ["const:82cd04:8", "const:4:8"]]
+ 0082cd04 ["CALL", null, ["callee:008514f8:8"]]
- 0082ccc4 bytes fd910094
+ 0082cd04 bytes fd910094
~~~


<a id="compare-97584e50d06d565b8cf603cef8a81057"></a>

### [`0082d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d250.md) → [`0082d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md) FUN_0082d290

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) [`00831fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831fb4.md) [`00838b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838b60.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 5件 [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) [`0082f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md) [`00831ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff4.md) [`00838ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ba0.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082d258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d250.md#insn-0082d258) · [`0082d268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d250.md#insn-0082d268) · [`0082d270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d250.md#insn-0082d270)
- 新版 `0082d298`（命令位置の公開資料なし） · `0082d2a8`（命令位置の公開資料なし） · `0082d2b0`（命令位置の公開資料なし）

~~~diff
- 0082d258 ["INT_ADD", "register:40f0:8", ["const:82d258:8", "const:4:8"]]
- 0082d258 ["CALL", null, ["callee:008514f8:8"]]
+ 0082d298 ["INT_ADD", "register:40f0:8", ["const:82d298:8", "const:4:8"]]
+ 0082d298 ["CALL", null, ["callee:008514f8:8"]]
- 0082d258 bytes 98900094
+ 0082d298 bytes 98900094
- 0082d268 ["INT_ADD", "register:40f0:8", ["const:82d268:8", "const:4:8"]]
- 0082d268 ["CALL", null, ["callee:008b79c8:8"]]
+ 0082d2a8 ["INT_ADD", "register:40f0:8", ["const:82d2a8:8", "const:4:8"]]
+ 0082d2a8 ["CALL", null, ["callee:008b79c8:8"]]
- 0082d268 bytes c7290294
+ 0082d2a8 bytes c8290294
- 0082d270 ["INT_ADD", "register:40f0:8", ["const:82d270:8", "const:4:8"]]
- 0082d270 ["CALL", null, ["callee:008514f8:8"]]
+ 0082d2b0 ["INT_ADD", "register:40f0:8", ["const:82d2b0:8", "const:4:8"]]
+ 0082d2b0 ["CALL", null, ["callee:008514f8:8"]]
- 0082d270 bytes 92900094
+ 0082d2b0 bytes 92900094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db169eb8d5599a6b98b5ca388ac608f3"></a>

### [`0082d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d4a0.md) → [`0082d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d4e0.md) FUN_0082d4e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`00838a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md) · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b6f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f0c.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 2件 [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) [`00838a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a74.md) · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b6f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f50.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082d4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d4a0.md#insn-0082d4ac) · [`0082d4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d4a0.md#insn-0082d4bc) · [`0082d4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d4a0.md#insn-0082d4c4)
- 新版 `0082d4ec`（命令位置の公開資料なし） · `0082d4fc`（命令位置の公開資料なし） · `0082d504`（命令位置の公開資料なし）

~~~diff
- 0082d4ac ["INT_ADD", "register:40f0:8", ["const:82d4ac:8", "const:4:8"]]
- 0082d4ac ["CALL", null, ["callee:008514f8:8"]]
+ 0082d4ec ["INT_ADD", "register:40f0:8", ["const:82d4ec:8", "const:4:8"]]
+ 0082d4ec ["CALL", null, ["callee:008514f8:8"]]
- 0082d4ac bytes 03900094
+ 0082d4ec bytes 03900094
- 0082d4bc ["INT_ADD", "register:40f0:8", ["const:82d4bc:8", "const:4:8"]]
- 0082d4bc ["CALL", null, ["callee:008b79c8:8"]]
+ 0082d4fc ["INT_ADD", "register:40f0:8", ["const:82d4fc:8", "const:4:8"]]
+ 0082d4fc ["CALL", null, ["callee:008b79c8:8"]]
- 0082d4bc bytes 32290294
+ 0082d4fc bytes 33290294
- 0082d4c4 ["INT_ADD", "register:40f0:8", ["const:82d4c4:8", "const:4:8"]]
- 0082d4c4 ["CALL", null, ["callee:008514f8:8"]]
+ 0082d504 ["INT_ADD", "register:40f0:8", ["const:82d504:8", "const:4:8"]]
+ 0082d504 ["CALL", null, ["callee:008514f8:8"]]
- 0082d4c4 bytes fd8f0094
+ 0082d504 bytes fd8f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c652b9a8c297dc9107a549729d08d1fd"></a>

### [`0082d718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d718.md) → [`0082d758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d758.md) FUN_0082d758

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082d734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d718.md#insn-0082d734) · [`0082d754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d718.md#insn-0082d754)
- 新版 `0082d774`（命令位置の公開資料なし） · `0082d794`（命令位置の公開資料なし）

~~~diff
- 0082d734 ["INT_ADD", "register:40f0:8", ["const:82d734:8", "const:4:8"]]
- 0082d734 ["CALL", null, ["callee:00c53d00:8"]]
+ 0082d774 ["INT_ADD", "register:40f0:8", ["const:82d774:8", "const:4:8"]]
+ 0082d774 ["CALL", null, ["callee:00c53d00:8"]]
- 0082d734 bytes 6b981094
+ 0082d774 bytes 63991094
- 0082d754 ["COPY", "register:0:8", ["register:4040:8"]]
- 0082d754 ["INT_ADD", "register:40f0:8", ["const:82d754:8", "const:4:8"]]
- 0082d754 ["CALLIND", null, ["register:0:8"]]
+ 0082d794 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0082d794 ["INT_ADD", "register:40f0:8", ["const:82d794:8", "const:4:8"]]
+ 0082d794 ["CALLIND", null, ["register:0:8"]]
- 0082d754 bytes 00013fd6
+ 0082d794 bytes 00013fd6
~~~


<a id="compare-8fce2953e9d8a9703638e5e36875bc70"></a>

### [`0082dce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dce0.md) → [`0082dd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dd20.md) FUN_0082dd20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 1件 [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082dce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dce0.md#insn-0082dce8) · [`0082dcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dce0.md#insn-0082dcf8) · [`0082dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dce0.md#insn-0082dd00)
- 新版 `0082dd28`（命令位置の公開資料なし） · `0082dd38`（命令位置の公開資料なし） · `0082dd40`（命令位置の公開資料なし）

~~~diff
- 0082dce8 ["INT_ADD", "register:40f0:8", ["const:82dce8:8", "const:4:8"]]
- 0082dce8 ["CALL", null, ["callee:008514f8:8"]]
+ 0082dd28 ["INT_ADD", "register:40f0:8", ["const:82dd28:8", "const:4:8"]]
+ 0082dd28 ["CALL", null, ["callee:008514f8:8"]]
- 0082dce8 bytes f48d0094
+ 0082dd28 bytes f48d0094
- 0082dcf8 ["INT_ADD", "register:40f0:8", ["const:82dcf8:8", "const:4:8"]]
- 0082dcf8 ["CALL", null, ["callee:008b79c8:8"]]
+ 0082dd38 ["INT_ADD", "register:40f0:8", ["const:82dd38:8", "const:4:8"]]
+ 0082dd38 ["CALL", null, ["callee:008b79c8:8"]]
- 0082dcf8 bytes 23270294
+ 0082dd38 bytes 24270294
- 0082dd00 ["INT_ADD", "register:40f0:8", ["const:82dd00:8", "const:4:8"]]
- 0082dd00 ["CALL", null, ["callee:008514f8:8"]]
+ 0082dd40 ["INT_ADD", "register:40f0:8", ["const:82dd40:8", "const:4:8"]]
+ 0082dd40 ["CALL", null, ["callee:008514f8:8"]]
- 0082dd00 bytes ee8d0094
+ 0082dd40 bytes ee8d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c72efffa079e659a38c0f599b2dff9d"></a>

### [`0082dd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md) → [`0082dda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md) FUN_0082dda4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) [`00838ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838ad0.md) · 呼出先 3件 [`00829534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829534.md) [`0082a760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082a760.md) [`0082aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082aa38.md)
- 新版 呼出元 2件 [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`00838b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b10.md) · 呼出先 3件 [`00829574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md) [`0082a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082a7a0.md) [`0082aa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082aa78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082ddd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md#insn-0082ddd0) · [`0082de3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md#insn-0082de3c) · [`0082de9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md#insn-0082de9c)
- 新版 `0082de10`（命令位置の公開資料なし） · `0082de7c`（命令位置の公開資料なし） · `0082dedc`（命令位置の公開資料なし）

~~~diff
- 0082ddd0 ["INT_ADD", "register:40f0:8", ["const:82ddd0:8", "const:4:8"]]
- 0082ddd0 ["CALL", null, ["callee:0082aa78:8"]]
+ 0082de10 ["INT_ADD", "register:40f0:8", ["const:82de10:8", "const:4:8"]]
+ 0082de10 ["CALL", null, ["callee:0082aa78:8"]]
- 0082ddd0 bytes 1af3ff97
+ 0082de10 bytes 1af3ff97
- 0082de3c ["INT_ADD", "register:40f0:8", ["const:82de3c:8", "const:4:8"]]
- 0082de3c ["CALL", null, ["callee:00829574:8"]]
+ 0082de7c ["INT_ADD", "register:40f0:8", ["const:82de7c:8", "const:4:8"]]
+ 0082de7c ["CALL", null, ["callee:00829574:8"]]
- 0082de3c bytes beedff97
+ 0082de7c bytes beedff97
- 0082de9c ["INT_ADD", "register:40f0:8", ["const:82de9c:8", "const:4:8"]]
- 0082de9c ["CALL", null, ["callee:0082a7a0:8"]]
+ 0082dedc ["INT_ADD", "register:40f0:8", ["const:82dedc:8", "const:4:8"]]
+ 0082dedc ["CALL", null, ["callee:0082a7a0:8"]]
- 0082de9c bytes 31f2ff97
+ 0082dedc bytes 31f2ff97
~~~


<a id="compare-0fb3de4ca4c0b13f09b9e4f99d785271"></a>

### [`0082dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dec0.md) → [`0082df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df00.md) FUN_0082df00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082ded4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dec0.md#insn-0082ded4) · [`0082dedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dec0.md#insn-0082dedc)
- 新版 `0082df14`（命令位置の公開資料なし） · `0082df1c`（命令位置の公開資料なし）

~~~diff
- 0082ded4 ["INT_ADD", "register:40f0:8", ["const:82ded4:8", "const:4:8"]]
- 0082ded4 ["CALL", null, ["callee:0046eef8:8"]]
+ 0082df14 ["INT_ADD", "register:40f0:8", ["const:82df14:8", "const:4:8"]]
+ 0082df14 ["CALL", null, ["callee:0046eef8:8"]]
- 0082ded4 bytes f903f197
+ 0082df14 bytes f903f197
- 0082dedc ["INT_ADD", "register:40f0:8", ["const:82dedc:8", "const:4:8"]]
- 0082dedc ["CALL", null, ["callee:0046e7c4:8"]]
+ 0082df1c ["INT_ADD", "register:40f0:8", ["const:82df1c:8", "const:4:8"]]
+ 0082df1c ["CALL", null, ["callee:0046e7c4:8"]]
- 0082dedc bytes 2a02f197
+ 0082df1c bytes 2a02f197
~~~


<a id="compare-b18ba7f7b4acc82b49b72b8d85976423"></a>

### [`0082eab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eab8.md) → [`0082eaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eaf8.md) FUN_0082eaf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 21件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`006270cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006adef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006adef0.md) [`006ee700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006ee700.md) · 呼出先 2件 [`00823820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00823/00823820.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 21件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`0062710c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/0062710c.md) [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) [`006adf30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006adf30.md) [`006ee740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006ee740.md) · 呼出先 2件 [`00823860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823860.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082eacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eab8.md#insn-0082eacc)
- 新版 `0082eb0c`（命令位置の公開資料なし）

~~~diff
- 0082eacc ["INT_ADD", "register:40f0:8", ["const:82eacc:8", "const:4:8"]]
- 0082eacc ["CALL", null, ["callee:008514f8:8"]]
+ 0082eb0c ["INT_ADD", "register:40f0:8", ["const:82eb0c:8", "const:4:8"]]
+ 0082eb0c ["CALL", null, ["callee:008514f8:8"]]
- 0082eacc bytes 7b8a0094
+ 0082eb0c bytes 7b8a0094
~~~


<a id="compare-9963d247c3c5ae288e75ae482b003759"></a>

### [`0082eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md) → [`0082eb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md) FUN_0082eb2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`006649ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006a6fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6fcc.md) · 呼出先 5件 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 17件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`006649ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006649ec.md) [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) [`006a700c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a700c.md) · 呼出先 5件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082eb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md#insn-0082eb28) · [`0082eb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md#insn-0082eb34) · [`0082eb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md#insn-0082eb60)
- 新版 `0082eb68`（命令位置の公開資料なし） · `0082eb74`（命令位置の公開資料なし） · `0082eba0`（命令位置の公開資料なし）

~~~diff
- 0082eb28 ["INT_ADD", "register:40f0:8", ["const:82eb28:8", "const:4:8"]]
- 0082eb28 ["CALL", null, ["callee:008514f8:8"]]
+ 0082eb68 ["INT_ADD", "register:40f0:8", ["const:82eb68:8", "const:4:8"]]
+ 0082eb68 ["CALL", null, ["callee:008514f8:8"]]
- 0082eb28 bytes 648a0094
+ 0082eb68 bytes 648a0094
- 0082eb34 ["INT_ADD", "register:40f0:8", ["const:82eb34:8", "const:4:8"]]
- 0082eb34 ["CALL", null, ["callee:00c57e90:8"]]
+ 0082eb74 ["INT_ADD", "register:40f0:8", ["const:82eb74:8", "const:4:8"]]
+ 0082eb74 ["CALL", null, ["callee:00c57e90:8"]]
- 0082eb34 bytes d7a31094
+ 0082eb74 bytes c7a41094
- 0082eb60 ["INT_ADD", "register:40f0:8", ["const:82eb60:8", "const:4:8"]]
- 0082eb60 ["CALL", null, ["callee:00823010:8"]]
+ 0082eba0 ["INT_ADD", "register:40f0:8", ["const:82eba0:8", "const:4:8"]]
+ 0082eba0 ["CALL", null, ["callee:00823010:8"]]
- 0082eb60 bytes 1cd1ff97
+ 0082eba0 bytes 1cd1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26638e3bffe65ac6f04f664e5fe6c670"></a>

### [`0082ebd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ebd4.md) → [`0082ec14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ec14.md) FUN_0082ec14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 7件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 7件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ebd4.md#insn-0082ec08) · [`0082ec2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ebd4.md#insn-0082ec2c) · [`0082ec44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ebd4.md#insn-0082ec44)
- 新版 `0082ec48`（命令位置の公開資料なし） · `0082ec6c`（命令位置の公開資料なし） · `0082ec84`（命令位置の公開資料なし）

~~~diff
- 0082ec08 ["INT_ADD", "register:40f0:8", ["const:82ec08:8", "const:4:8"]]
- 0082ec08 ["CALL", null, ["callee:008514f8:8"]]
+ 0082ec48 ["INT_ADD", "register:40f0:8", ["const:82ec48:8", "const:4:8"]]
+ 0082ec48 ["CALL", null, ["callee:008514f8:8"]]
- 0082ec08 bytes 2c8a0094
+ 0082ec48 bytes 2c8a0094
- 0082ec2c ["INT_ADD", "register:40f0:8", ["const:82ec2c:8", "const:4:8"]]
- 0082ec2c ["CALL", null, ["callee:00c57e90:8"]]
+ 0082ec6c ["INT_ADD", "register:40f0:8", ["const:82ec6c:8", "const:4:8"]]
+ 0082ec6c ["CALL", null, ["callee:00c57e90:8"]]
- 0082ec2c bytes 99a31094
+ 0082ec6c bytes 89a41094
- 0082ec44 ["INT_ADD", "register:40f0:8", ["const:82ec44:8", "const:4:8"]]
- 0082ec44 ["CALL", null, ["callee:00c58000:8"]]
+ 0082ec84 ["INT_ADD", "register:40f0:8", ["const:82ec84:8", "const:4:8"]]
+ 0082ec84 ["CALL", null, ["callee:00c58000:8"]]
- 0082ec44 bytes efa31094
+ 0082ec84 bytes dfa41094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf4b01a232a0e403829bf0b59da943e6"></a>

### [`0082ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ecf8.md) → [`0082ed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ed38.md) FUN_0082ed38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 5件 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) · 呼出先 5件 [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082ed2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ecf8.md#insn-0082ed2c) · [`0082ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ecf8.md#insn-0082ed38) · [`0082ed6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ecf8.md#insn-0082ed6c)
- 新版 `0082ed6c`（命令位置の公開資料なし） · `0082ed78`（命令位置の公開資料なし） · `0082edac`（命令位置の公開資料なし）

~~~diff
- 0082ed2c ["INT_ADD", "register:40f0:8", ["const:82ed2c:8", "const:4:8"]]
- 0082ed2c ["CALL", null, ["callee:008514f8:8"]]
+ 0082ed6c ["INT_ADD", "register:40f0:8", ["const:82ed6c:8", "const:4:8"]]
+ 0082ed6c ["CALL", null, ["callee:008514f8:8"]]
- 0082ed2c bytes e3890094
+ 0082ed6c bytes e3890094
- 0082ed38 ["INT_ADD", "register:40f0:8", ["const:82ed38:8", "const:4:8"]]
- 0082ed38 ["CALL", null, ["callee:00c57e90:8"]]
+ 0082ed78 ["INT_ADD", "register:40f0:8", ["const:82ed78:8", "const:4:8"]]
+ 0082ed78 ["CALL", null, ["callee:00c57e90:8"]]
- 0082ed38 bytes 56a31094
+ 0082ed78 bytes 46a41094
- 0082ed6c ["INT_ADD", "register:40f0:8", ["const:82ed6c:8", "const:4:8"]]
- 0082ed6c ["CALL", null, ["callee:00823010:8"]]
+ 0082edac ["INT_ADD", "register:40f0:8", ["const:82edac:8", "const:4:8"]]
+ 0082edac ["CALL", null, ["callee:00823010:8"]]
- 0082ed6c bytes 99d0ff97
+ 0082edac bytes 99d0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d772ef27a229e8519858bb73ab1d38e9"></a>

### [`0082fd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fd2c.md) → [`0082fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md) FUN_0082fd6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081c510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c510.md) · 呼出先 6件 [`0083000c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083000c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0081c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md) · 呼出先 6件 [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0082fd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fd2c.md#insn-0082fd9c) · [`0082fdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fd2c.md#insn-0082fdb0) · [`0082fdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fd2c.md#insn-0082fdb8)
- 新版 `0082fddc`（命令位置の公開資料なし） · `0082fdf0`（命令位置の公開資料なし） · `0082fdf8`（命令位置の公開資料なし）

~~~diff
- 0082fd9c ["INT_ADD", "register:40f0:8", ["const:82fd9c:8", "const:4:8"]]
- 0082fd9c ["CALL", null, ["callee:00c53d00:8"]]
+ 0082fddc ["INT_ADD", "register:40f0:8", ["const:82fddc:8", "const:4:8"]]
+ 0082fddc ["CALL", null, ["callee:00c53d00:8"]]
- 0082fd9c bytes d18e1094
+ 0082fddc bytes c98f1094
- 0082fdb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0082fdb0 ["INT_ADD", "register:40f0:8", ["const:82fdb0:8", "const:4:8"]]
- 0082fdb0 ["CALLIND", null, ["register:0:8"]]
+ 0082fdf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0082fdf0 ["INT_ADD", "register:40f0:8", ["const:82fdf0:8", "const:4:8"]]
+ 0082fdf0 ["CALLIND", null, ["register:0:8"]]
- 0082fdb0 bytes 00013fd6
+ 0082fdf0 bytes 00013fd6
- 0082fdb8 ["INT_ADD", "register:40f0:8", ["const:82fdb8:8", "const:4:8"]]
- 0082fdb8 ["CALL", null, ["callee:00c57e80:8"]]
+ 0082fdf8 ["INT_ADD", "register:40f0:8", ["const:82fdf8:8", "const:4:8"]]
+ 0082fdf8 ["CALL", null, ["callee:00c57e80:8"]]
- 0082fdb8 bytes 329f1094
+ 0082fdf8 bytes 22a01094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7f5435c6ac348a34fad14a3416160ec"></a>

### [`00830020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md) → [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) FUN_00830060

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d768.md) [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) · 呼出先 7件 [`0081a784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a784.md) [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) [`00830234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830234.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 2件 [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) [`008307f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md) · 呼出先 7件 [`0081a7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a7c4.md) [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) [`00830274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830274.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md#insn-00830064) · [`00830070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md#insn-00830070) · [`008300bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md#insn-008300bc)
- 新版 `008300a4`（命令位置の公開資料なし） · `008300b0`（命令位置の公開資料なし） · `008300fc`（命令位置の公開資料なし）

~~~diff
- 00830064 ["INT_ADD", "register:40f0:8", ["const:830064:8", "const:4:8"]]
- 00830064 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008300a4 ["INT_ADD", "register:40f0:8", ["const:8300a4:8", "const:4:8"]]
+ 008300a4 ["CALL", null, ["callee:00c53cd0:8"]]
- 00830064 bytes 138e1094
+ 008300a4 bytes 0b8f1094
- 00830070 ["INT_ADD", "register:40f0:8", ["const:830070:8", "const:4:8"]]
- 00830070 ["CALL", null, ["callee:0082071c:8"]]
+ 008300b0 ["INT_ADD", "register:40f0:8", ["const:8300b0:8", "const:4:8"]]
+ 008300b0 ["CALL", null, ["callee:0082071c:8"]]
- 00830070 bytes 9bc1ff97
+ 008300b0 bytes 9bc1ff97
- 008300bc ["INT_ADD", "register:40f0:8", ["const:8300bc:8", "const:4:8"]]
- 008300bc ["CALL", null, ["callee:00c57e90:8"]]
+ 008300fc ["INT_ADD", "register:40f0:8", ["const:8300fc:8", "const:4:8"]]
+ 008300fc ["CALL", null, ["callee:00c57e90:8"]]
- 008300bc bytes 759e1094
+ 008300fc bytes 659f1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f83f99dc402fc89836fdf0a806a9d8"></a>

### [`00830130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830130.md) → [`00830170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830170.md) FUN_00830170

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008301a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830130.md#insn-008301a0) · [`008301b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830130.md#insn-008301b4) · [`008301bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830130.md#insn-008301bc)
- 新版 `008301e0`（命令位置の公開資料なし） · `008301f4`（命令位置の公開資料なし） · `008301fc`（命令位置の公開資料なし）

~~~diff
- 008301a0 ["INT_ADD", "register:40f0:8", ["const:8301a0:8", "const:4:8"]]
- 008301a0 ["CALL", null, ["callee:00c53d00:8"]]
+ 008301e0 ["INT_ADD", "register:40f0:8", ["const:8301e0:8", "const:4:8"]]
+ 008301e0 ["CALL", null, ["callee:00c53d00:8"]]
- 008301a0 bytes d08d1094
+ 008301e0 bytes c88e1094
- 008301b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008301b4 ["INT_ADD", "register:40f0:8", ["const:8301b4:8", "const:4:8"]]
- 008301b4 ["CALLIND", null, ["register:0:8"]]
+ 008301f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008301f4 ["INT_ADD", "register:40f0:8", ["const:8301f4:8", "const:4:8"]]
+ 008301f4 ["CALLIND", null, ["register:0:8"]]
- 008301b4 bytes 00013fd6
+ 008301f4 bytes 00013fd6
- 008301bc ["INT_ADD", "register:40f0:8", ["const:8301bc:8", "const:4:8"]]
- 008301bc ["CALL", null, ["callee:00c57e80:8"]]
+ 008301fc ["INT_ADD", "register:40f0:8", ["const:8301fc:8", "const:4:8"]]
+ 008301fc ["CALL", null, ["callee:00c57e80:8"]]
- 008301bc bytes 319e1094
+ 008301fc bytes 219f1094
~~~


<a id="compare-d4f2e700f4587045fd626b9b04a455e8"></a>

### [`008301e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md) → [`00830224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md) FUN_00830224

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00815764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00815/00815764.md) [`008301e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md) [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · 呼出先 2件 [`008301e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`008157a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00815/008157a4.md) [`00830224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 2件 [`00830224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md#insn-00830200) · [`0083020c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md#insn-0083020c) · [`0083021c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md#insn-0083021c)
- 新版 `00830240`（命令位置の公開資料なし） · `0083024c`（命令位置の公開資料なし） · `0083025c`（命令位置の公開資料なし）

~~~diff
- 00830200 ["INT_ADD", "register:40f0:8", ["const:830200:8", "const:4:8"]]
- 00830200 ["CALL", null, ["local:b0:8"]]
+ 00830240 ["INT_ADD", "register:40f0:8", ["const:830240:8", "const:4:8"]]
+ 00830240 ["CALL", null, ["local:b0:8"]]
- 00830200 bytes f9ffff97
+ 00830240 bytes f9ffff97
- 0083020c ["INT_ADD", "register:40f0:8", ["const:83020c:8", "const:4:8"]]
- 0083020c ["CALL", null, ["local:b0:8"]]
+ 0083024c ["INT_ADD", "register:40f0:8", ["const:83024c:8", "const:4:8"]]
+ 0083024c ["CALL", null, ["local:b0:8"]]
- 0083020c bytes f6ffff97
+ 0083024c bytes f6ffff97
- 0083021c ["INT_ADD", "register:40f0:8", ["const:83021c:8", "const:4:8"]]
- 0083021c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0083025c ["INT_ADD", "register:40f0:8", ["const:83025c:8", "const:4:8"]]
+ 0083025c ["CALL", null, ["callee:00c57eb0:8"]]
- 0083021c bytes 259e1094
+ 0083025c bytes 159f1094
~~~


<a id="compare-abaa4792f21efb332821553284882f9e"></a>

### [`00830248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830248.md) → [`00830288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md) FUN_00830288

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`00830248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830248.md) [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · 呼出先 4件 [`00830248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830248.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 4件 [`00830288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830288.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830248.md#insn-00830264) · [`00830270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830248.md#insn-00830270) · [`00830284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830248.md#insn-00830284)
- 新版 `008302a4`（命令位置の公開資料なし） · `008302b0`（命令位置の公開資料なし） · `008302c4`（命令位置の公開資料なし）

~~~diff
- 00830264 ["INT_ADD", "register:40f0:8", ["const:830264:8", "const:4:8"]]
- 00830264 ["CALL", null, ["local:b0:8"]]
+ 008302a4 ["INT_ADD", "register:40f0:8", ["const:8302a4:8", "const:4:8"]]
+ 008302a4 ["CALL", null, ["local:b0:8"]]
- 00830264 bytes f9ffff97
+ 008302a4 bytes f9ffff97
- 00830270 ["INT_ADD", "register:40f0:8", ["const:830270:8", "const:4:8"]]
- 00830270 ["CALL", null, ["local:b0:8"]]
+ 008302b0 ["INT_ADD", "register:40f0:8", ["const:8302b0:8", "const:4:8"]]
+ 008302b0 ["CALL", null, ["local:b0:8"]]
- 00830270 bytes f6ffff97
+ 008302b0 bytes f6ffff97
- 00830284 ["INT_ADD", "register:40f0:8", ["const:830284:8", "const:4:8"]]
- 00830284 ["CALL", null, ["callee:00c53d00:8"]]
+ 008302c4 ["INT_ADD", "register:40f0:8", ["const:8302c4:8", "const:4:8"]]
+ 008302c4 ["CALL", null, ["callee:00c53d00:8"]]
- 00830284 bytes 978d1094
+ 008302c4 bytes 8f8e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02f798e6e9138f2020c4515b8fa99838"></a>

### [`008302f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008302f8.md) → [`00830338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830338.md) FUN_00830338

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008302f8.md#insn-00830314) · [`00830324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008302f8.md#insn-00830324)
- 新版 `00830354`（命令位置の公開資料なし） · `00830364`（命令位置の公開資料なし）

~~~diff
- 00830314 ["INT_ADD", "register:40f0:8", ["const:830314:8", "const:4:8"]]
- 00830314 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00830354 ["INT_ADD", "register:40f0:8", ["const:830354:8", "const:4:8"]]
+ 00830354 ["CALL", null, ["callee:00c57eb0:8"]]
- 00830314 bytes e79d1094
+ 00830354 bytes d79e1094
- 00830324 ["INT_ADD", "register:40f0:8", ["const:830324:8", "const:4:8"]]
- 00830324 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00830364 ["INT_ADD", "register:40f0:8", ["const:830364:8", "const:4:8"]]
+ 00830364 ["CALL", null, ["callee:00c57eb0:8"]]
- 00830324 bytes e39d1094
+ 00830364 bytes d39e1094
~~~


<a id="compare-e30296d18723c7c5a6b59bd2375696b0"></a>

### [`00830350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md) → [`00830390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md) FUN_00830390

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`00830350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md) [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · 呼出先 4件 [`00830350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 4件 [`00830390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830390.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083036c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md#insn-0083036c) · [`00830378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md#insn-00830378) · [`0083038c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md#insn-0083038c)
- 新版 `008303ac`（命令位置の公開資料なし） · `008303b8`（命令位置の公開資料なし） · `008303cc`（命令位置の公開資料なし）

~~~diff
- 0083036c ["INT_ADD", "register:40f0:8", ["const:83036c:8", "const:4:8"]]
- 0083036c ["CALL", null, ["local:b0:8"]]
+ 008303ac ["INT_ADD", "register:40f0:8", ["const:8303ac:8", "const:4:8"]]
+ 008303ac ["CALL", null, ["local:b0:8"]]
- 0083036c bytes f9ffff97
+ 008303ac bytes f9ffff97
- 00830378 ["INT_ADD", "register:40f0:8", ["const:830378:8", "const:4:8"]]
- 00830378 ["CALL", null, ["local:b0:8"]]
+ 008303b8 ["INT_ADD", "register:40f0:8", ["const:8303b8:8", "const:4:8"]]
+ 008303b8 ["CALL", null, ["local:b0:8"]]
- 00830378 bytes f6ffff97
+ 008303b8 bytes f6ffff97
- 0083038c ["INT_ADD", "register:40f0:8", ["const:83038c:8", "const:4:8"]]
- 0083038c ["CALL", null, ["callee:00c53d00:8"]]
+ 008303cc ["INT_ADD", "register:40f0:8", ["const:8303cc:8", "const:4:8"]]
+ 008303cc ["CALL", null, ["callee:00c53d00:8"]]
- 0083038c bytes 558d1094
+ 008303cc bytes 4d8e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b5695eb61cc6a22ea52467c78913fa6"></a>

### [`0083040c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083040c.md) → [`0083044c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083044c.md) FUN_0083044c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00830400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830400.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00830440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830440.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083040c.md#insn-00830428) · [`00830438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083040c.md#insn-00830438) · [`00830448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083040c.md#insn-00830448)
- 新版 `00830468`（命令位置の公開資料なし） · `00830478`（命令位置の公開資料なし） · `00830488`（命令位置の公開資料なし）

~~~diff
- 00830428 ["INT_ADD", "register:40f0:8", ["const:830428:8", "const:4:8"]]
- 00830428 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00830468 ["INT_ADD", "register:40f0:8", ["const:830468:8", "const:4:8"]]
+ 00830468 ["CALL", null, ["callee:00c57eb0:8"]]
- 00830428 bytes a29d1094
+ 00830468 bytes 929e1094
- 00830438 ["INT_ADD", "register:40f0:8", ["const:830438:8", "const:4:8"]]
- 00830438 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00830478 ["INT_ADD", "register:40f0:8", ["const:830478:8", "const:4:8"]]
+ 00830478 ["CALL", null, ["callee:00c57eb0:8"]]
- 00830438 bytes 9e9d1094
+ 00830478 bytes 8e9e1094
- 00830448 ["INT_ADD", "register:40f0:8", ["const:830448:8", "const:4:8"]]
- 00830448 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00830488 ["INT_ADD", "register:40f0:8", ["const:830488:8", "const:4:8"]]
+ 00830488 ["CALL", null, ["callee:00c57eb0:8"]]
- 00830448 bytes 9a9d1094
+ 00830488 bytes 8a9e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55479895b98dff0259dd77819b6ad984"></a>

### [`008304d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008304d0.md) → [`00830510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md) FUN_00830510

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`008304d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008304d0.md) [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · 呼出先 2件 [`008304d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008304d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 2件 [`00830510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830510.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008304f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008304d0.md#insn-008304f0) · [`008304fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008304d0.md#insn-008304fc)
- 新版 `00830530`（命令位置の公開資料なし） · `0083053c`（命令位置の公開資料なし）

~~~diff
- 008304f0 ["INT_ADD", "register:40f0:8", ["const:8304f0:8", "const:4:8"]]
- 008304f0 ["CALL", null, ["local:b0:8"]]
+ 00830530 ["INT_ADD", "register:40f0:8", ["const:830530:8", "const:4:8"]]
+ 00830530 ["CALL", null, ["local:b0:8"]]
- 008304f0 bytes f8ffff97
+ 00830530 bytes f8ffff97
- 008304fc ["INT_ADD", "register:40f0:8", ["const:8304fc:8", "const:4:8"]]
- 008304fc ["CALL", null, ["local:b0:8"]]
+ 0083053c ["INT_ADD", "register:40f0:8", ["const:83053c:8", "const:4:8"]]
+ 0083053c ["CALL", null, ["local:b0:8"]]
- 008304fc bytes f5ffff97
+ 0083053c bytes f5ffff97
~~~


<a id="compare-fbf8746fbe67cc488928ad6ba90ac2a8"></a>

### [`00830514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md) → [`00830554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md) FUN_00830554

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`00830514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md) [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · 呼出先 4件 [`00830514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`00830554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md) [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) · 呼出先 4件 [`00830554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830554.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md#insn-00830530) · [`0083053c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md#insn-0083053c) · [`00830550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md#insn-00830550)
- 新版 `00830570`（命令位置の公開資料なし） · `0083057c`（命令位置の公開資料なし） · `00830590`（命令位置の公開資料なし）

~~~diff
- 00830530 ["INT_ADD", "register:40f0:8", ["const:830530:8", "const:4:8"]]
- 00830530 ["CALL", null, ["local:b0:8"]]
+ 00830570 ["INT_ADD", "register:40f0:8", ["const:830570:8", "const:4:8"]]
+ 00830570 ["CALL", null, ["local:b0:8"]]
- 00830530 bytes f9ffff97
+ 00830570 bytes f9ffff97
- 0083053c ["INT_ADD", "register:40f0:8", ["const:83053c:8", "const:4:8"]]
- 0083053c ["CALL", null, ["local:b0:8"]]
+ 0083057c ["INT_ADD", "register:40f0:8", ["const:83057c:8", "const:4:8"]]
+ 0083057c ["CALL", null, ["local:b0:8"]]
- 0083053c bytes f6ffff97
+ 0083057c bytes f6ffff97
- 00830550 ["INT_ADD", "register:40f0:8", ["const:830550:8", "const:4:8"]]
- 00830550 ["CALL", null, ["callee:00c53d00:8"]]
+ 00830590 ["INT_ADD", "register:40f0:8", ["const:830590:8", "const:4:8"]]
+ 00830590 ["CALL", null, ["callee:00c53d00:8"]]
- 00830550 bytes e48c1094
+ 00830590 bytes dc8d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aae2cc7037752092114248e841a86a3"></a>

### [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md) → [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) FUN_0083060c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`0081c8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c8c4.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`00823820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00823/00823820.md) [`00829354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829354.md) · 呼出先 3件 [`0081c2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md) [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 11件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`0081c904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c904.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`00823860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823860.md) [`00829394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md) · 呼出先 3件 [`0081c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md) [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008305ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md#insn-008305ec) · [`008305f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md#insn-008305f8) · [`00830600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md#insn-00830600)
- 新版 `0083062c`（命令位置の公開資料なし） · `00830638`（命令位置の公開資料なし） · `00830640`（命令位置の公開資料なし）

~~~diff
- 008305ec ["INT_ADD", "register:40f0:8", ["const:8305ec:8", "const:4:8"]]
- 008305ec ["CALL", null, ["local:b0:8"]]
+ 0083062c ["INT_ADD", "register:40f0:8", ["const:83062c:8", "const:4:8"]]
+ 0083062c ["CALL", null, ["local:b0:8"]]
- 008305ec bytes f8ffff97
+ 0083062c bytes f8ffff97
- 008305f8 ["INT_ADD", "register:40f0:8", ["const:8305f8:8", "const:4:8"]]
- 008305f8 ["CALL", null, ["local:b0:8"]]
+ 00830638 ["INT_ADD", "register:40f0:8", ["const:830638:8", "const:4:8"]]
+ 00830638 ["CALL", null, ["local:b0:8"]]
- 008305f8 bytes f5ffff97
+ 00830638 bytes f5ffff97
- 00830600 ["INT_ADD", "register:40f0:8", ["const:830600:8", "const:4:8"]]
- 00830600 ["CALL", null, ["callee:0081c2f4:8"]]
+ 00830640 ["INT_ADD", "register:40f0:8", ["const:830640:8", "const:4:8"]]
+ 00830640 ["CALL", null, ["callee:0081c2f4:8"]]
- 00830600 bytes 2dafff97
+ 00830640 bytes 2dafff97
~~~


<a id="compare-8d9775e0072cc92af2a21f36c5136938"></a>

### [`00830618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830618.md) → [`00830658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830658.md) FUN_00830658

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0081c2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0081c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083063c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830618.md#insn-0083063c)
- 新版 `0083067c`（命令位置の公開資料なし）

~~~diff
- 0083063c ["INT_ADD", "register:40f0:8", ["const:83063c:8", "const:4:8"]]
- 0083063c ["CALL", null, ["callee:0081c2f4:8"]]
+ 0083067c ["INT_ADD", "register:40f0:8", ["const:83067c:8", "const:4:8"]]
+ 0083067c ["CALL", null, ["callee:0081c2f4:8"]]
- 0083063c bytes 1eafff97
+ 0083067c bytes 1eafff97
~~~


<a id="compare-dfb99cb220a81a19cec9fc710629c00d"></a>

### [`0083065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083065c.md) → [`0083069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083069c.md) FUN_0083069c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0083000c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083000c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008306c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083065c.md#insn-008306c8) · [`008306f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083065c.md#insn-008306f4) · [`00830754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083065c.md#insn-00830754)
- 新版 `00830708`（命令位置の公開資料なし） · `00830734`（命令位置の公開資料なし） · `00830794`（命令位置の公開資料なし）

~~~diff
- 008306c8 ["INT_ADD", "register:40f0:8", ["const:8306c8:8", "const:4:8"]]
- 008306c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00830708 ["INT_ADD", "register:40f0:8", ["const:830708:8", "const:4:8"]]
+ 00830708 ["CALL", null, ["callee:00c57e90:8"]]
- 008306c8 bytes f29c1094
+ 00830708 bytes e29d1094
- 008306f4 ["INT_ADD", "register:40f0:8", ["const:8306f4:8", "const:4:8"]]
- 008306f4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00830734 ["INT_ADD", "register:40f0:8", ["const:830734:8", "const:4:8"]]
+ 00830734 ["CALL", null, ["callee:00c53cd0:8"]]
- 008306f4 bytes 6f8c1094
+ 00830734 bytes 678d1094
- 00830754 ["INT_ADD", "register:40f0:8", ["const:830754:8", "const:4:8"]]
- 00830754 ["CALL", null, ["callee:00c53d00:8"]]
+ 00830794 ["INT_ADD", "register:40f0:8", ["const:830794:8", "const:4:8"]]
+ 00830794 ["CALL", null, ["callee:00c53d00:8"]]
- 00830754 bytes 638c1094
+ 00830794 bytes 5b8d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602962841dd40019ee5490d0eb1bf64d"></a>

### [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) → [`008307f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md) FUN_008307f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0081c8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c8c4.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`00823820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00823/00823820.md) [`00829354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829354.md) [`0082c344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c344.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00830020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md) [`008308c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008308c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 8件 [`0081c904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c904.md) [`00823010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823010.md) [`00823860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00823/00823860.md) [`00829394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md) [`0082c384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c384.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00830060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830060.md) [`00830908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830908.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008307f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md#insn-008307f0) · [`00830810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md#insn-00830810) · [`00830830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md#insn-00830830)
- 新版 `00830830`（命令位置の公開資料なし） · `00830850`（命令位置の公開資料なし） · `00830870`（命令位置の公開資料なし）

~~~diff
- 008307f0 ["INT_ADD", "register:40f0:8", ["const:8307f0:8", "const:4:8"]]
- 008307f0 ["CALL", null, ["callee:00830908:8"]]
+ 00830830 ["INT_ADD", "register:40f0:8", ["const:830830:8", "const:4:8"]]
+ 00830830 ["CALL", null, ["callee:00830908:8"]]
- 008307f0 bytes 36000094
+ 00830830 bytes 36000094
- 00830810 ["INT_ADD", "register:40f0:8", ["const:830810:8", "const:4:8"]]
- 00830810 ["CALL", null, ["callee:00c57e90:8"]]
+ 00830850 ["INT_ADD", "register:40f0:8", ["const:830850:8", "const:4:8"]]
+ 00830850 ["CALL", null, ["callee:00c57e90:8"]]
- 00830810 bytes a09c1094
+ 00830850 bytes 909d1094
- 00830830 ["INT_ADD", "register:40f0:8", ["const:830830:8", "const:4:8"]]
- 00830830 ["CALL", null, ["callee:00830060:8"]]
+ 00830870 ["INT_ADD", "register:40f0:8", ["const:830870:8", "const:4:8"]]
+ 00830870 ["CALL", null, ["callee:00830060:8"]]
- 00830830 bytes fcfdff97
+ 00830870 bytes fcfdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b1501d588667db20ebe30c0d24036e5"></a>

### [`00830e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830e0c.md) → [`00830e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e4c.md) FUN_00830e4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00827918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00830e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830e0c.md#insn-00830e48)
- 新版 `00830e88`（命令位置の公開資料なし）

~~~diff
- 00830e48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00830e48 ["INT_ADD", "register:40f0:8", ["const:830e48:8", "const:4:8"]]
- 00830e48 ["CALLIND", null, ["register:0:8"]]
+ 00830e88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00830e88 ["INT_ADD", "register:40f0:8", ["const:830e88:8", "const:4:8"]]
+ 00830e88 ["CALLIND", null, ["register:0:8"]]
- 00830e48 bytes 00013fd6
+ 00830e88 bytes 00013fd6
~~~


<a id="compare-5c7ccefd1d5d3cce1e6029ba1077c157"></a>

### [`008310d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310d8.md) → [`00831118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831118.md) FUN_00831118

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00827918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00831114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310d8.md#insn-00831114)
- 新版 `00831154`（命令位置の公開資料なし）

~~~diff
- 00831114 ["COPY", "register:0:8", ["register:4040:8"]]
- 00831114 ["INT_ADD", "register:40f0:8", ["const:831114:8", "const:4:8"]]
- 00831114 ["CALLIND", null, ["register:0:8"]]
+ 00831154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00831154 ["INT_ADD", "register:40f0:8", ["const:831154:8", "const:4:8"]]
+ 00831154 ["CALLIND", null, ["register:0:8"]]
- 00831114 bytes 00013fd6
+ 00831154 bytes 00013fd6
~~~


<a id="compare-1090833b3a22ed6ea1d5716892d88601"></a>

### [`00831c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md) → [`00831ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md) FUN_00831ca0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) [`00831c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md) · 呼出先 2件 [`00831c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0082ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md) [`00831ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md) · 呼出先 2件 [`00831ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00831c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md#insn-00831c80) · [`00831c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md#insn-00831c8c)
- 新版 `00831cc0`（命令位置の公開資料なし） · `00831ccc`（命令位置の公開資料なし）

~~~diff
- 00831c80 ["INT_ADD", "register:40f0:8", ["const:831c80:8", "const:4:8"]]
- 00831c80 ["CALL", null, ["local:b0:8"]]
+ 00831cc0 ["INT_ADD", "register:40f0:8", ["const:831cc0:8", "const:4:8"]]
+ 00831cc0 ["CALL", null, ["local:b0:8"]]
- 00831c80 bytes f8ffff97
+ 00831cc0 bytes f8ffff97
- 00831c8c ["INT_ADD", "register:40f0:8", ["const:831c8c:8", "const:4:8"]]
- 00831c8c ["CALL", null, ["local:b0:8"]]
+ 00831ccc ["INT_ADD", "register:40f0:8", ["const:831ccc:8", "const:4:8"]]
+ 00831ccc ["CALL", null, ["local:b0:8"]]
- 00831c8c bytes f5ffff97
+ 00831ccc bytes f5ffff97
~~~


<a id="compare-37131bdc2248b5f76ea7361455d83a83"></a>

### [`008345d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00834/008345d0.md) → [`00834610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834610.md) FUN_00834610

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00834108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00834/00834108.md) · 呼出先 1件 [`00834108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00834/00834108.md)
- 新版 呼出元 1件 [`00834148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834148.md) · 呼出先 1件 [`00834148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834148.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008347ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00834/008345d0.md#insn-008347ec) · [`00834804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00834/008345d0.md#insn-00834804)
- 新版 `0083482c`（命令位置の公開資料なし） · `00834844`（命令位置の公開資料なし）

~~~diff
- 008347ec ["INT_ADD", "register:40f0:8", ["const:8347ec:8", "const:4:8"]]
- 008347ec ["CALL", null, ["callee:00834148:8"]]
+ 0083482c ["INT_ADD", "register:40f0:8", ["const:83482c:8", "const:4:8"]]
+ 0083482c ["CALL", null, ["callee:00834148:8"]]
- 008347ec bytes 47feff97
+ 0083482c bytes 47feff97
- 00834804 ["INT_ADD", "register:40f0:8", ["const:834804:8", "const:4:8"]]
- 00834804 ["CALL", null, ["callee:00834148:8"]]
+ 00834844 ["INT_ADD", "register:40f0:8", ["const:834844:8", "const:4:8"]]
+ 00834844 ["CALL", null, ["callee:00834148:8"]]
- 00834804 bytes 41feff97
+ 00834844 bytes 41feff97
~~~


<a id="compare-5db6008ec2908dec35818e177bd1c9e1"></a>

### [`00835330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835330.md) → [`00835370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835370.md) FUN_00835370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00832094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832094.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008320d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00835350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835330.md#insn-00835350)
- 新版 `00835390`（命令位置の公開資料なし）

~~~diff
- 00835350 ["INT_ADD", "register:40f0:8", ["const:835350:8", "const:4:8"]]
- 00835350 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00835390 ["INT_ADD", "register:40f0:8", ["const:835390:8", "const:4:8"]]
+ 00835390 ["CALL", null, ["callee:00c57eb0:8"]]
- 00835350 bytes d8891094
+ 00835390 bytes c88a1094
~~~


<a id="compare-50896aaf97d15e64c391538364c04c41"></a>

### [`008356c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/008356c8.md) → [`00835708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835708.md) FUN_00835708

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00832094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832094.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008320d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008356e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/008356c8.md#insn-008356e8)
- 新版 `00835728`（命令位置の公開資料なし）

~~~diff
- 008356e8 ["INT_ADD", "register:40f0:8", ["const:8356e8:8", "const:4:8"]]
- 008356e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00835728 ["INT_ADD", "register:40f0:8", ["const:835728:8", "const:4:8"]]
+ 00835728 ["CALL", null, ["callee:00c57eb0:8"]]
- 008356e8 bytes f2881094
+ 00835728 bytes e2891094
~~~


<a id="compare-2dcba9721279ca9373279c7e40a7907c"></a>

### [`00835b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835b44.md) → [`00835b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835b84.md) FUN_00835b84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00832094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832094.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008320d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00835b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835b44.md#insn-00835b64)
- 新版 `00835ba4`（命令位置の公開資料なし）

~~~diff
- 00835b64 ["INT_ADD", "register:40f0:8", ["const:835b64:8", "const:4:8"]]
- 00835b64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00835ba4 ["INT_ADD", "register:40f0:8", ["const:835ba4:8", "const:4:8"]]
+ 00835ba4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00835b64 bytes d3871094
+ 00835ba4 bytes c3881094
~~~


<a id="compare-8db32a1e2b63ecc3026d3789f29bf8c8"></a>

### [`00835dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835dd8.md) → [`00835e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835e18.md) FUN_00835e18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00835f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835f8c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00835fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fcc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00835e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835dd8.md#insn-00835e7c) · [`00835f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835dd8.md#insn-00835f28) · [`00835f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835dd8.md#insn-00835f3c)
- 新版 `00835ebc`（命令位置の公開資料なし） · `00835f68`（命令位置の公開資料なし） · `00835f7c`（命令位置の公開資料なし）

~~~diff
- 00835e7c ["INT_ADD", "register:40f0:8", ["const:835e7c:8", "const:4:8"]]
- 00835e7c ["CALL", null, ["callee:00c57e90:8"]]
+ 00835ebc ["INT_ADD", "register:40f0:8", ["const:835ebc:8", "const:4:8"]]
+ 00835ebc ["CALL", null, ["callee:00c57e90:8"]]
- 00835e7c bytes 05871094
+ 00835ebc bytes f5871094
- 00835f28 ["INT_ADD", "register:40f0:8", ["const:835f28:8", "const:4:8"]]
- 00835f28 ["CALL", null, ["callee:00c53d00:8"]]
+ 00835f68 ["INT_ADD", "register:40f0:8", ["const:835f68:8", "const:4:8"]]
+ 00835f68 ["CALL", null, ["callee:00c53d00:8"]]
- 00835f28 bytes 6e761094
+ 00835f68 bytes 66771094
- 00835f3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00835f3c ["INT_ADD", "register:40f0:8", ["const:835f3c:8", "const:4:8"]]
- 00835f3c ["CALLIND", null, ["register:0:8"]]
+ 00835f7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00835f7c ["INT_ADD", "register:40f0:8", ["const:835f7c:8", "const:4:8"]]
+ 00835f7c ["CALLIND", null, ["register:0:8"]]
- 00835f3c bytes 00013fd6
+ 00835f7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013749d1d86cd49e9e162e0236614386"></a>

### [`00835fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md) → [`00835fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fe0.md) FUN_00835fe0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) [`00835fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md) [`008367a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/008367a0.md) · 呼出先 7件 [`00835fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md) [`00836604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836604.md) [`008367a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/008367a0.md) [`00836d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 3件 [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`00835fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fe0.md) [`008367e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/008367e0.md) · 呼出先 7件 [`00835fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fe0.md) [`00836644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836644.md) [`008367e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/008367e0.md) [`00836d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836d70.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083601c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md#insn-0083601c) · [`00836060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md#insn-00836060) · [`00836078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md#insn-00836078)
- 新版 `0083605c`（命令位置の公開資料なし） · `008360a0`（命令位置の公開資料なし） · `008360b8`（命令位置の公開資料なし）

~~~diff
- 0083601c ["INT_ADD", "register:40f0:8", ["const:83601c:8", "const:4:8"]]
- 0083601c ["CALL", null, ["callee:00836644:8"]]
+ 0083605c ["INT_ADD", "register:40f0:8", ["const:83605c:8", "const:4:8"]]
+ 0083605c ["CALL", null, ["callee:00836644:8"]]
- 0083601c bytes 7a010094
+ 0083605c bytes 7a010094
- 00836060 ["INT_ADD", "register:40f0:8", ["const:836060:8", "const:4:8"]]
- 00836060 ["CALL", null, ["callee:00c53d00:8"]]
+ 008360a0 ["INT_ADD", "register:40f0:8", ["const:8360a0:8", "const:4:8"]]
+ 008360a0 ["CALL", null, ["callee:00c53d00:8"]]
- 00836060 bytes 20761094
+ 008360a0 bytes 18771094
- 00836078 ["COPY", "register:0:8", ["register:4040:8"]]
- 00836078 ["INT_ADD", "register:40f0:8", ["const:836078:8", "const:4:8"]]
- 00836078 ["CALLIND", null, ["register:0:8"]]
+ 008360b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008360b8 ["INT_ADD", "register:40f0:8", ["const:8360b8:8", "const:4:8"]]
+ 008360b8 ["CALLIND", null, ["register:0:8"]]
- 00836078 bytes 00013fd6
+ 008360b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-566a997566344826229f0c6202e17fbd"></a>

### [`008367a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/008367a0.md) → [`008367e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/008367e0.md) FUN_008367e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00835fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md) · 呼出先 5件 [`00835fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md) [`00836604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836604.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00835fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fe0.md) · 呼出先 5件 [`00835fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fe0.md) [`00836644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836644.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083683c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/008367a0.md#insn-0083683c) · [`0083693c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/008367a0.md#insn-0083693c) · [`008369c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/008367a0.md#insn-008369c0)
- 新版 `0083687c`（命令位置の公開資料なし） · `0083697c`（命令位置の公開資料なし） · `00836a00`（命令位置の公開資料なし）

~~~diff
- 0083683c ["INT_ADD", "register:40f0:8", ["const:83683c:8", "const:4:8"]]
- 0083683c ["CALL", null, ["callee:00836644:8"]]
+ 0083687c ["INT_ADD", "register:40f0:8", ["const:83687c:8", "const:4:8"]]
+ 0083687c ["CALL", null, ["callee:00836644:8"]]
- 0083683c bytes 72ffff97
+ 0083687c bytes 72ffff97
- 0083693c ["INT_ADD", "register:40f0:8", ["const:83693c:8", "const:4:8"]]
- 0083693c ["CALL", null, ["callee:00836644:8"]]
+ 0083697c ["INT_ADD", "register:40f0:8", ["const:83697c:8", "const:4:8"]]
+ 0083697c ["CALL", null, ["callee:00836644:8"]]
- 0083693c bytes 32ffff97
+ 0083697c bytes 32ffff97
- 008369c0 ["INT_ADD", "register:40f0:8", ["const:8369c0:8", "const:4:8"]]
- 008369c0 ["CALL", null, ["callee:00836644:8"]]
+ 00836a00 ["INT_ADD", "register:40f0:8", ["const:836a00:8", "const:4:8"]]
+ 00836a00 ["CALL", null, ["callee:00836644:8"]]
- 008369c0 bytes 11ffff97
+ 00836a00 bytes 11ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31f62973ab18c74775111ee45bc25c45"></a>

### [`00836ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836ca4.md) → [`00836ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836ce4.md) FUN_00836ce4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00836cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836ca4.md#insn-00836cfc) · [`00836d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836ca4.md#insn-00836d10) · [`00836d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836ca4.md#insn-00836d18)
- 新版 `00836d3c`（命令位置の公開資料なし） · `00836d50`（命令位置の公開資料なし） · `00836d58`（命令位置の公開資料なし）

~~~diff
- 00836cfc ["INT_ADD", "register:40f0:8", ["const:836cfc:8", "const:4:8"]]
- 00836cfc ["CALL", null, ["callee:00c53d00:8"]]
+ 00836d3c ["INT_ADD", "register:40f0:8", ["const:836d3c:8", "const:4:8"]]
+ 00836d3c ["CALL", null, ["callee:00c53d00:8"]]
- 00836cfc bytes f9721094
+ 00836d3c bytes f1731094
- 00836d10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00836d10 ["INT_ADD", "register:40f0:8", ["const:836d10:8", "const:4:8"]]
- 00836d10 ["CALLIND", null, ["register:0:8"]]
+ 00836d50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00836d50 ["INT_ADD", "register:40f0:8", ["const:836d50:8", "const:4:8"]]
+ 00836d50 ["CALLIND", null, ["register:0:8"]]
- 00836d10 bytes 00013fd6
+ 00836d50 bytes 00013fd6
- 00836d18 ["INT_ADD", "register:40f0:8", ["const:836d18:8", "const:4:8"]]
- 00836d18 ["CALL", null, ["callee:00c57e80:8"]]
+ 00836d58 ["INT_ADD", "register:40f0:8", ["const:836d58:8", "const:4:8"]]
+ 00836d58 ["CALL", null, ["callee:00c57e80:8"]]
- 00836d18 bytes 5a831094
+ 00836d58 bytes 4a841094
~~~


<a id="compare-cb9d7380ab6d5d428e6bb31a41ebec95"></a>

### [`00836d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md) → [`00836d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836d70.md) FUN_00836d70

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00835fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835fa0.md) [`00836d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md) · 呼出先 6件 [`00836604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836604.md) [`00836d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md) [`00837548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00837/00837548.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00835fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fe0.md) [`00836d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836d70.md) · 呼出先 6件 [`00836644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836644.md) [`00836d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836d70.md) [`00837588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/00837588.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00836dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md#insn-00836dac) · [`00836e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md#insn-00836e2c) · [`00836e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md#insn-00836e98)
- 新版 `00836dec`（命令位置の公開資料なし） · `00836e6c`（命令位置の公開資料なし） · `00836ed8`（命令位置の公開資料なし）

~~~diff
- 00836dac ["INT_ADD", "register:40f0:8", ["const:836dac:8", "const:4:8"]]
- 00836dac ["CALL", null, ["callee:00836644:8"]]
+ 00836dec ["INT_ADD", "register:40f0:8", ["const:836dec:8", "const:4:8"]]
+ 00836dec ["CALL", null, ["callee:00836644:8"]]
- 00836dac bytes 16feff97
+ 00836dec bytes 16feff97
- 00836e2c ["INT_ADD", "register:40f0:8", ["const:836e2c:8", "const:4:8"]]
- 00836e2c ["CALL", null, ["callee:00836644:8"]]
+ 00836e6c ["INT_ADD", "register:40f0:8", ["const:836e6c:8", "const:4:8"]]
+ 00836e6c ["CALL", null, ["callee:00836644:8"]]
- 00836e2c bytes f6fdff97
+ 00836e6c bytes f6fdff97
- 00836e98 ["INT_ADD", "register:40f0:8", ["const:836e98:8", "const:4:8"]]
- 00836e98 ["CALL", null, ["callee:00837588:8"]]
+ 00836ed8 ["INT_ADD", "register:40f0:8", ["const:836ed8:8", "const:4:8"]]
+ 00836ed8 ["CALL", null, ["callee:00837588:8"]]
- 00836e98 bytes ac010094
+ 00836ed8 bytes ac010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8dedf641b0fec36da59dddd0fe24536"></a>

### [`00837548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00837/00837548.md) → [`00837588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/00837588.md) FUN_00837588

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00836d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836d30.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00836d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00836/00836d70.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008375c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00837/00837548.md#insn-008375c8) · [`008375e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00837/00837548.md#insn-008375e0) · [`008375e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00837/00837548.md#insn-008375e8)
- 新版 `00837608`（命令位置の公開資料なし） · `00837620`（命令位置の公開資料なし） · `00837628`（命令位置の公開資料なし）

~~~diff
- 008375c8 ["INT_ADD", "register:40f0:8", ["const:8375c8:8", "const:4:8"]]
- 008375c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00837608 ["INT_ADD", "register:40f0:8", ["const:837608:8", "const:4:8"]]
+ 00837608 ["CALL", null, ["callee:00c53d00:8"]]
- 008375c8 bytes c6701094
+ 00837608 bytes be711094
- 008375e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008375e0 ["INT_ADD", "register:40f0:8", ["const:8375e0:8", "const:4:8"]]
- 008375e0 ["CALLIND", null, ["register:0:8"]]
+ 00837620 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00837620 ["INT_ADD", "register:40f0:8", ["const:837620:8", "const:4:8"]]
+ 00837620 ["CALLIND", null, ["register:0:8"]]
- 008375e0 bytes 00013fd6
+ 00837620 bytes 00013fd6
- 008375e8 ["INT_ADD", "register:40f0:8", ["const:8375e8:8", "const:4:8"]]
- 008375e8 ["CALL", null, ["callee:00c57e80:8"]]
+ 00837628 ["INT_ADD", "register:40f0:8", ["const:837628:8", "const:4:8"]]
+ 00837628 ["CALL", null, ["callee:00c57e80:8"]]
- 008375e8 bytes 26811094
+ 00837628 bytes 16821094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-966281b4b0ae40eedbc78aa7d6ecb12a"></a>

### [`00838a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md) → [`00838a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a74.md) FUN_00838a74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0082d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d4a0.md) [`00ac948c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac948c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0082d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d4e0.md) [`00ac9688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9688.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00838a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md#insn-00838a48)
- 新版 `00838a88`（命令位置の公開資料なし）

~~~diff
- 00838a48 ["INT_ADD", "register:40f0:8", ["const:838a48:8", "const:4:8"]]
- 00838a48 ["CALL", null, ["callee:00ac9688:8"]]
+ 00838a88 ["INT_ADD", "register:40f0:8", ["const:838a88:8", "const:4:8"]]
+ 00838a88 ["CALL", null, ["callee:00ac9688:8"]]
- 00838a48 bytes 91420a94
+ 00838a88 bytes 00430a94
~~~


<a id="compare-89745baae986688984f59c4c8d4d2a93"></a>

### [`00839524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839524.md) → [`00839564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/00839564.md) FUN_00839564

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083953c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839524.md#insn-0083953c)
- 新版 `0083957c`（命令位置の公開資料なし）

~~~diff
- 0083953c ["INT_ADD", "register:40f0:8", ["const:83953c:8", "const:4:8"]]
- 0083953c ["CALL", null, ["callee:00676a60:8"]]
+ 0083957c ["INT_ADD", "register:40f0:8", ["const:83957c:8", "const:4:8"]]
+ 0083957c ["CALL", null, ["callee:00676a60:8"]]
- 0083953c bytes 39f5f897
+ 0083957c bytes 39f5f897
~~~


<a id="compare-067b7715a09ae01d09fe2948b973dc02"></a>

### [`00839554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839554.md) → [`00839594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/00839594.md) FUN_00839594

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 2件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839554.md#insn-00839570) · [`0083958c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839554.md#insn-0083958c)
- 新版 `008395b0`（命令位置の公開資料なし） · `008395cc`（命令位置の公開資料なし）

~~~diff
- 00839570 ["INT_ADD", "register:40f0:8", ["const:839570:8", "const:4:8"]]
- 00839570 ["CALL", null, ["callee:005c179c:8"]]
+ 008395b0 ["INT_ADD", "register:40f0:8", ["const:8395b0:8", "const:4:8"]]
+ 008395b0 ["CALL", null, ["callee:005c179c:8"]]
- 00839570 bytes 7b20f697
+ 008395b0 bytes 7b20f697
- 0083958c ["INT_ADD", "register:40f0:8", ["const:83958c:8", "const:4:8"]]
- 0083958c ["CALL", null, ["callee:00676a60:8"]]
+ 008395cc ["INT_ADD", "register:40f0:8", ["const:8395cc:8", "const:4:8"]]
+ 008395cc ["CALL", null, ["callee:00676a60:8"]]
- 0083958c bytes 25f5f897
+ 008395cc bytes 25f5f897
~~~


<a id="compare-5051bc15f17df6e6e4729d3966e5f238"></a>

### [`008395ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008395ac.md) → [`008395ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/008395ec.md) FUN_008395ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004804d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004804d8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`00480518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008395d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008395ac.md#insn-008395d4) · [`008395f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008395ac.md#insn-008395f4) · [`00839618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008395ac.md#insn-00839618)
- 新版 `00839614`（命令位置の公開資料なし） · `00839634`（命令位置の公開資料なし） · `00839658`（命令位置の公開資料なし）

~~~diff
- 008395d4 ["INT_ADD", "register:40f0:8", ["const:8395d4:8", "const:4:8"]]
- 008395d4 ["CALL", null, ["callee:00480518:8"]]
+ 00839614 ["INT_ADD", "register:40f0:8", ["const:839614:8", "const:4:8"]]
+ 00839614 ["CALL", null, ["callee:00480518:8"]]
- 008395d4 bytes c11bf197
+ 00839614 bytes c11bf197
- 008395f4 ["INT_ADD", "register:40f0:8", ["const:8395f4:8", "const:4:8"]]
- 008395f4 ["CALL", null, ["callee:0043bba4:8"]]
+ 00839634 ["INT_ADD", "register:40f0:8", ["const:839634:8", "const:4:8"]]
+ 00839634 ["CALL", null, ["callee:0043bba4:8"]]
- 008395f4 bytes 5c09f097
+ 00839634 bytes 5c09f097
- 00839618 ["INT_ADD", "register:40f0:8", ["const:839618:8", "const:4:8"]]
- 00839618 ["CALL", null, ["callee:00480518:8"]]
+ 00839658 ["INT_ADD", "register:40f0:8", ["const:839658:8", "const:4:8"]]
+ 00839658 ["CALL", null, ["callee:00480518:8"]]
- 00839618 bytes b01bf197
+ 00839658 bytes b01bf197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2595ee95b2e6efb9b9494fa3b49ed60"></a>

### [`008397ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008397ac.md) → [`008397ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/008397ec.md) FUN_008397ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 2件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ef8.md)
- 新版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 2件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008397d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008397ac.md#insn-008397d0) · [`008397ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008397ac.md#insn-008397ec) · [`00839824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008397ac.md#insn-00839824)
- 新版 `00839810`（命令位置の公開資料なし） · `0083982c`（命令位置の公開資料なし） · `00839864`（命令位置の公開資料なし）

~~~diff
- 008397d0 ["INT_ADD", "register:40f0:8", ["const:8397d0:8", "const:4:8"]]
- 008397d0 ["CALL", null, ["callee:00480f38:8"]]
+ 00839810 ["INT_ADD", "register:40f0:8", ["const:839810:8", "const:4:8"]]
+ 00839810 ["CALL", null, ["callee:00480f38:8"]]
- 008397d0 bytes ca1df197
+ 00839810 bytes ca1df197
- 008397ec ["INT_ADD", "register:40f0:8", ["const:8397ec:8", "const:4:8"]]
- 008397ec ["CALL", null, ["callee:00480f38:8"]]
+ 0083982c ["INT_ADD", "register:40f0:8", ["const:83982c:8", "const:4:8"]]
+ 0083982c ["CALL", null, ["callee:00480f38:8"]]
- 008397ec bytes c31df197
+ 0083982c bytes c31df197
- 00839824 ["INT_ADD", "register:40f0:8", ["const:839824:8", "const:4:8"]]
- 00839824 ["CALL", null, ["callee:00480f38:8"]]
+ 00839864 ["INT_ADD", "register:40f0:8", ["const:839864:8", "const:4:8"]]
+ 00839864 ["CALL", null, ["callee:00480f38:8"]]
- 00839824 bytes b51df197
+ 00839864 bytes b51df197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3340e1155f4fd14e5f0a9fa0f9676fa5"></a>

### [`008398b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008398b8.md) → [`008398f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/008398f8.md) FUN_008398f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008398b8.md#insn-00839920) · [`00839958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008398b8.md#insn-00839958)
- 新版 `00839960`（命令位置の公開資料なし） · `00839998`（命令位置の公開資料なし）

~~~diff
- 00839920 ["INT_ADD", "register:40f0:8", ["const:839920:8", "const:4:8"]]
- 00839920 ["CALL", null, ["callee:00c57e90:8"]]
+ 00839960 ["INT_ADD", "register:40f0:8", ["const:839960:8", "const:4:8"]]
+ 00839960 ["CALL", null, ["callee:00c57e90:8"]]
- 00839920 bytes 5c781094
+ 00839960 bytes 4c791094
- 00839958 ["INT_ADD", "register:40f0:8", ["const:839958:8", "const:4:8"]]
- 00839958 ["CALL", null, ["callee:0043bba4:8"]]
+ 00839998 ["INT_ADD", "register:40f0:8", ["const:839998:8", "const:4:8"]]
+ 00839998 ["CALL", null, ["callee:0043bba4:8"]]
- 00839958 bytes 8308f097
+ 00839998 bytes 8308f097
~~~


