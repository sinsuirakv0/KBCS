# v16.0.0 → v16.0.1 · 要調査の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-8b8547cebe328bcbc86212637c64514e"></a>

### [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) → [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) FUN_00555c94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) [`0055a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md) · 呼出先 8件 [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) [`0058ff68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`0055a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md) · 呼出先 8件 [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) [`0055b248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md) [`0058ffa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00555ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md#insn-00555ca0) · [`00555cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md#insn-00555cbc) · [`00555cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md#insn-00555cf8)
- 新版 `00555ce0`（命令位置の公開資料なし） · `00555cfc`（命令位置の公開資料なし） · `00555d38`（命令位置の公開資料なし）

~~~diff
- 00555ca0 ["INT_ADD", "register:40f0:8", ["const:555ca0:8", "const:4:8"]]
- 00555ca0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00555ce0 ["INT_ADD", "register:40f0:8", ["const:555ce0:8", "const:4:8"]]
+ 00555ce0 ["CALL", null, ["callee:00c57e90:8"]]
- 00555ca0 bytes 7c071c94
+ 00555ce0 bytes 6c081c94
- 00555cbc ["INT_ADD", "register:40f0:8", ["const:555cbc:8", "const:4:8"]]
- 00555cbc ["CALL", null, ["callee:00c58090:8"]]
+ 00555cfc ["INT_ADD", "register:40f0:8", ["const:555cfc:8", "const:4:8"]]
+ 00555cfc ["CALL", null, ["callee:00c58090:8"]]
- 00555cbc bytes f5071c94
+ 00555cfc bytes e5081c94
- 00555cf8 ["INT_ADD", "register:40f0:8", ["const:555cf8:8", "const:4:8"]]
- 00555cf8 ["CALL", null, ["callee:00555e0c:8"]]
+ 00555d38 ["INT_ADD", "register:40f0:8", ["const:555d38:8", "const:4:8"]]
+ 00555d38 ["CALL", null, ["callee:00555e0c:8"]]
- 00555cf8 bytes 35000094
+ 00555d38 bytes 35000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b8a79cee0b0141f93364423e178438"></a>

### [`00559834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md) → [`00559874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559874.md) FUN_00559874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0055b248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005598b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md#insn-005598b4) · [`005598e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md#insn-005598e4) · [`005598f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md#insn-005598f8)
- 新版 `005598f4`（命令位置の公開資料なし） · `00559924`（命令位置の公開資料なし） · `00559938`（命令位置の公開資料なし）

~~~diff
- 005598b4 ["INT_ADD", "register:40f0:8", ["const:5598b4:8", "const:4:8"]]
- 005598b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005598f4 ["INT_ADD", "register:40f0:8", ["const:5598f4:8", "const:4:8"]]
+ 005598f4 ["CALL", null, ["callee:00c57e90:8"]]
- 005598b4 bytes 77f81b94
+ 005598f4 bytes 67f91b94
- 005598e4 ["INT_ADD", "register:40f0:8", ["const:5598e4:8", "const:4:8"]]
- 005598e4 ["CALL", null, ["callee:00c58000:8"]]
+ 00559924 ["INT_ADD", "register:40f0:8", ["const:559924:8", "const:4:8"]]
+ 00559924 ["CALL", null, ["callee:00c58000:8"]]
- 005598e4 bytes c7f81b94
+ 00559924 bytes b7f91b94
- 005598f8 ["INT_ADD", "register:40f0:8", ["const:5598f8:8", "const:4:8"]]
- 005598f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00559938 ["INT_ADD", "register:40f0:8", ["const:559938:8", "const:4:8"]]
+ 00559938 ["CALL", null, ["callee:00c57eb0:8"]]
- 005598f8 bytes 6ef81b94
+ 00559938 bytes 5ef91b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96679d36b02cb75c15acc4ef1ca80cd"></a>

### [`0055a4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md) → [`0055a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md) FUN_0055a53c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00467f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f6c.md) · 呼出先 2件 [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00467fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467fac.md) · 呼出先 2件 [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md#insn-0055a540) · [`0055a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md#insn-0055a564)
- 新版 `0055a580`（命令位置の公開資料なし） · `0055a5a4`（命令位置の公開資料なし）

~~~diff
- 0055a540 ["INT_ADD", "register:40f0:8", ["const:55a540:8", "const:4:8"]]
- 0055a540 ["CALL", null, ["callee:00559964:8"]]
+ 0055a580 ["INT_ADD", "register:40f0:8", ["const:55a580:8", "const:4:8"]]
+ 0055a580 ["CALL", null, ["callee:00559964:8"]]
- 0055a540 bytes f9fcff97
+ 0055a580 bytes f9fcff97
- 0055a564 ["INT_ADD", "register:40f0:8", ["const:55a564:8", "const:4:8"]]
- 0055a564 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0055a5a4 ["INT_ADD", "register:40f0:8", ["const:55a5a4:8", "const:4:8"]]
+ 0055a5a4 ["CALL", null, ["callee:00c57ee0:8"]]
- 0055a564 bytes 5ff51b94
+ 0055a5a4 bytes 4ff61b94
~~~


<a id="compare-de25a9822e8f709c417f0d09cc1dd442"></a>

### [`0055a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a614.md) → [`0055a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a654.md) FUN_0055a654

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00590cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590cd8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00590d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590d18.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a614.md#insn-0055a630) · [`0055a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a614.md#insn-0055a650)
- 新版 `0055a670`（命令位置の公開資料なし） · `0055a690`（命令位置の公開資料なし）

~~~diff
- 0055a630 ["INT_ADD", "register:40f0:8", ["const:55a630:8", "const:4:8"]]
- 0055a630 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055a670 ["INT_ADD", "register:40f0:8", ["const:55a670:8", "const:4:8"]]
+ 0055a670 ["CALL", null, ["callee:00c53d00:8"]]
- 0055a630 bytes ace41b94
+ 0055a670 bytes a4e51b94
- 0055a650 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055a650 ["INT_ADD", "register:40f0:8", ["const:55a650:8", "const:4:8"]]
- 0055a650 ["CALLIND", null, ["register:0:8"]]
+ 0055a690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055a690 ["INT_ADD", "register:40f0:8", ["const:55a690:8", "const:4:8"]]
+ 0055a690 ["CALLIND", null, ["register:0:8"]]
- 0055a650 bytes 00013fd6
+ 0055a690 bytes 00013fd6
~~~


<a id="compare-662c71c3f42509e941df9a578ec32408"></a>

### [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) → [`0055a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md) FUN_0055a6f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0055af38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md) [`0055b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md) [`0055b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md) [`0055b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b120.md)
- 新版 呼出元 2件 [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) [`00559f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559f40.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0055af78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055af78.md) [`0055b138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b138.md) [`0055b14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b14c.md) [`0055b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md#insn-0055a76c) · [`0055a788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md#insn-0055a788) · [`0055a798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md#insn-0055a798)
- 新版 `0055a7ac`（命令位置の公開資料なし） · `0055a7c8`（命令位置の公開資料なし） · `0055a7d8`（命令位置の公開資料なし）

~~~diff
- 0055a76c ["INT_ADD", "register:40f0:8", ["const:55a76c:8", "const:4:8"]]
- 0055a76c ["CALL", null, ["callee:00c57e90:8"]]
+ 0055a7ac ["INT_ADD", "register:40f0:8", ["const:55a7ac:8", "const:4:8"]]
+ 0055a7ac ["CALL", null, ["callee:00c57e90:8"]]
- 0055a76c bytes c9f41b94
+ 0055a7ac bytes b9f51b94
- 0055a788 ["INT_ADD", "register:40f0:8", ["const:55a788:8", "const:4:8"]]
- 0055a788 ["CALL", null, ["callee:00c58090:8"]]
+ 0055a7c8 ["INT_ADD", "register:40f0:8", ["const:55a7c8:8", "const:4:8"]]
+ 0055a7c8 ["CALL", null, ["callee:00c58090:8"]]
- 0055a788 bytes 42f51b94
+ 0055a7c8 bytes 32f61b94
- 0055a798 ["INT_ADD", "register:40f0:8", ["const:55a798:8", "const:4:8"]]
- 0055a798 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055a7d8 ["INT_ADD", "register:40f0:8", ["const:55a7d8:8", "const:4:8"]]
+ 0055a7d8 ["CALL", null, ["callee:00c57e90:8"]]
- 0055a798 bytes bef41b94
+ 0055a7d8 bytes aef51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f4ed192813d7bc46dad1b11510df928"></a>

### [`0055af38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md) → [`0055af78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055af78.md) FUN_0055af78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0055a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md#insn-0055b064) · [`0055b098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md#insn-0055b098)
- 新版 `0055b0a4`（命令位置の公開資料なし） · `0055b0d8`（命令位置の公開資料なし）

~~~diff
- 0055b064 ["INT_ADD", "register:40f0:8", ["const:55b064:8", "const:4:8"]]
- 0055b064 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0055b0a4 ["INT_ADD", "register:40f0:8", ["const:55b0a4:8", "const:4:8"]]
+ 0055b0a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0055b064 bytes 93f21b94
+ 0055b0a4 bytes 83f31b94
- 0055b098 ["INT_ADD", "register:40f0:8", ["const:55b098:8", "const:4:8"]]
- 0055b098 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0055b0d8 ["INT_ADD", "register:40f0:8", ["const:55b0d8:8", "const:4:8"]]
+ 0055b0d8 ["CALL", null, ["callee:00c57ee0:8"]]
- 0055b098 bytes 92f21b94
+ 0055b0d8 bytes 82f31b94
~~~


<a id="compare-dc632e4b43f60975d2861fad190632af"></a>

### [`0055b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b09c.md) → [`0055b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b0dc.md) FUN_0055b0dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b09c.md#insn-0055b0dc)
- 新版 `0055b11c`（命令位置の公開資料なし）

~~~diff
- 0055b0dc ["INT_ADD", "register:40f0:8", ["const:55b0dc:8", "const:4:8"]]
- 0055b0dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0055b11c ["INT_ADD", "register:40f0:8", ["const:55b11c:8", "const:4:8"]]
+ 0055b11c ["CALL", null, ["callee:00c57eb0:8"]]
- 0055b0dc bytes 75f21b94
+ 0055b11c bytes 65f31b94
~~~


<a id="compare-327f4009356c50363f81458ad5d9e4fc"></a>

### [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) → [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) FUN_0055b380

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0055b21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md) [`0055c2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md) [`0055c2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md) · 呼出先 5件 [`0055b478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md) [`0058ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff18.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0055b25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b25c.md) [`0055c2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c2e4.md) [`0055c324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c324.md) · 呼出先 5件 [`0055b4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md) [`0058ff58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff58.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md#insn-0055b374) · [`0055b394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md#insn-0055b394) · [`0055b3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md#insn-0055b3a8)
- 新版 `0055b3b4`（命令位置の公開資料なし） · `0055b3d4`（命令位置の公開資料なし） · `0055b3e8`（命令位置の公開資料なし）

~~~diff
- 0055b374 ["INT_ADD", "register:40f0:8", ["const:55b374:8", "const:4:8"]]
- 0055b374 ["CALL", null, ["callee:0058ff58:8"]]
+ 0055b3b4 ["INT_ADD", "register:40f0:8", ["const:55b3b4:8", "const:4:8"]]
+ 0055b3b4 ["CALL", null, ["callee:0058ff58:8"]]
- 0055b374 bytes e9d20094
+ 0055b3b4 bytes e9d20094
- 0055b394 ["INT_ADD", "register:40f0:8", ["const:55b394:8", "const:4:8"]]
- 0055b394 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055b3d4 ["INT_ADD", "register:40f0:8", ["const:55b3d4:8", "const:4:8"]]
+ 0055b3d4 ["CALL", null, ["callee:00c53d00:8"]]
- 0055b394 bytes 53e11b94
+ 0055b3d4 bytes 4be21b94
- 0055b3a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055b3a8 ["INT_ADD", "register:40f0:8", ["const:55b3a8:8", "const:4:8"]]
- 0055b3a8 ["CALLIND", null, ["register:0:8"]]
+ 0055b3e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055b3e8 ["INT_ADD", "register:40f0:8", ["const:55b3e8:8", "const:4:8"]]
+ 0055b3e8 ["CALLIND", null, ["register:0:8"]]
- 0055b3a8 bytes 00013fd6
+ 0055b3e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf519218590b4fc218552e0dc2f52ca9"></a>

### [`0055b478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md) → [`0055b4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md) FUN_0055b4b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) · 呼出先 6件 [`0055c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c69c.md) [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) · 呼出先 6件 [`0055c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6dc.md) [`0055c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md#insn-0055b4c4) · [`0055b4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md#insn-0055b4e4) · [`0055b500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md#insn-0055b500)
- 新版 `0055b504`（命令位置の公開資料なし） · `0055b524`（命令位置の公開資料なし） · `0055b540`（命令位置の公開資料なし）

~~~diff
- 0055b4c4 ["INT_ADD", "register:40f0:8", ["const:55b4c4:8", "const:4:8"]]
- 0055b4c4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0055b504 ["INT_ADD", "register:40f0:8", ["const:55b504:8", "const:4:8"]]
+ 0055b504 ["CALL", null, ["callee:00c53cd0:8"]]
- 0055b4c4 bytes fbe01b94
+ 0055b504 bytes f3e11b94
- 0055b4e4 ["INT_ADD", "register:40f0:8", ["const:55b4e4:8", "const:4:8"]]
- 0055b4e4 ["CALL", null, ["callee:0055c6dc:8"]]
+ 0055b524 ["INT_ADD", "register:40f0:8", ["const:55b524:8", "const:4:8"]]
+ 0055b524 ["CALL", null, ["callee:0055c6dc:8"]]
- 0055b4e4 bytes 6e040094
+ 0055b524 bytes 6e040094
- 0055b500 ["INT_ADD", "register:40f0:8", ["const:55b500:8", "const:4:8"]]
- 0055b500 ["CALL", null, ["callee:0055c6e4:8"]]
+ 0055b540 ["INT_ADD", "register:40f0:8", ["const:55b540:8", "const:4:8"]]
+ 0055b540 ["CALL", null, ["callee:0055c6e4:8"]]
- 0055b500 bytes 69040094
+ 0055b540 bytes 69040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1855f8273c5ab02ba813b11791d043dc"></a>

### [`0055b7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b7d0.md) → [`0055b810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b810.md) FUN_0055b810

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0055e680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e680.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0055e6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b7d0.md#insn-0055b7f0)
- 新版 `0055b830`（命令位置の公開資料なし）

~~~diff
- 0055b7f0 ["INT_ADD", "register:40f0:8", ["const:55b7f0:8", "const:4:8"]]
- 0055b7f0 ["CALL", null, ["callee:0055e6c0:8"]]
+ 0055b830 ["INT_ADD", "register:40f0:8", ["const:55b830:8", "const:4:8"]]
+ 0055b830 ["CALL", null, ["callee:0055e6c0:8"]]
- 0055b7f0 bytes a40b0094
+ 0055b830 bytes a40b0094
~~~


<a id="compare-a5847d890833406ca96e1e798e36b7fc"></a>

### [`0055b834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b834.md) → [`0055b874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b874.md) FUN_0055b874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0055e680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e680.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0055e6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b834.md#insn-0055b850)
- 新版 `0055b890`（命令位置の公開資料なし）

~~~diff
- 0055b850 ["INT_ADD", "register:40f0:8", ["const:55b850:8", "const:4:8"]]
- 0055b850 ["CALL", null, ["callee:0055e6c0:8"]]
+ 0055b890 ["INT_ADD", "register:40f0:8", ["const:55b890:8", "const:4:8"]]
+ 0055b890 ["CALL", null, ["callee:0055e6c0:8"]]
- 0055b850 bytes 8c0b0094
+ 0055b890 bytes 8c0b0094
~~~


<a id="compare-c3e1729ba443d30b0566e61784fde809"></a>

### [`0055c2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md) → [`0055c2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c2e4.md) FUN_0055c2e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) [`0055e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) [`0055e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e624.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md#insn-0055c2c0) · [`0055c2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md#insn-0055c2cc)
- 新版 `0055c300`（命令位置の公開資料なし） · `0055c30c`（命令位置の公開資料なし）

~~~diff
- 0055c2c0 ["INT_ADD", "register:40f0:8", ["const:55c2c0:8", "const:4:8"]]
- 0055c2c0 ["CALL", null, ["callee:0055e624:8"]]
+ 0055c300 ["INT_ADD", "register:40f0:8", ["const:55c300:8", "const:4:8"]]
+ 0055c300 ["CALL", null, ["callee:0055e624:8"]]
- 0055c2c0 bytes c9080094
+ 0055c300 bytes c9080094
- 0055c2cc ["INT_ADD", "register:40f0:8", ["const:55c2cc:8", "const:4:8"]]
- 0055c2cc ["CALL", null, ["callee:0055b380:8"]]
+ 0055c30c ["INT_ADD", "register:40f0:8", ["const:55c30c:8", "const:4:8"]]
+ 0055c30c ["CALL", null, ["callee:0055b380:8"]]
- 0055c2cc bytes 1dfcff97
+ 0055c30c bytes 1dfcff97
~~~


<a id="compare-1afb9df7a2217196c4fccd270b71deb7"></a>

### [`0055c2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md) → [`0055c324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c324.md) FUN_0055c324

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) [`0055e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) [`0055e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e624.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md#insn-0055c2fc) · [`0055c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md#insn-0055c308)
- 新版 `0055c33c`（命令位置の公開資料なし） · `0055c348`（命令位置の公開資料なし）

~~~diff
- 0055c2fc ["INT_ADD", "register:40f0:8", ["const:55c2fc:8", "const:4:8"]]
- 0055c2fc ["CALL", null, ["callee:0055e624:8"]]
+ 0055c33c ["INT_ADD", "register:40f0:8", ["const:55c33c:8", "const:4:8"]]
+ 0055c33c ["CALL", null, ["callee:0055e624:8"]]
- 0055c2fc bytes ba080094
+ 0055c33c bytes ba080094
- 0055c308 ["INT_ADD", "register:40f0:8", ["const:55c308:8", "const:4:8"]]
- 0055c308 ["CALL", null, ["callee:0055b380:8"]]
+ 0055c348 ["INT_ADD", "register:40f0:8", ["const:55c348:8", "const:4:8"]]
+ 0055c348 ["CALL", null, ["callee:0055b380:8"]]
- 0055c308 bytes 0efcff97
+ 0055c348 bytes 0efcff97
~~~


<a id="compare-69845a7536cc9980f1efcf41b3d25663"></a>

### [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) → [`0055c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md) FUN_0055c7c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0057f82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md) [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) · 呼出先 2件 [`0055c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0057f86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md) [`005804a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md) · 呼出先 2件 [`0055ca04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md#insn-0055c7b8) · [`0055c7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md#insn-0055c7dc)
- 新版 `0055c7f8`（命令位置の公開資料なし） · `0055c81c`（命令位置の公開資料なし）

~~~diff
- 0055c7b8 ["INT_ADD", "register:40f0:8", ["const:55c7b8:8", "const:4:8"]]
- 0055c7b8 ["CALL", null, ["callee:0055ca04:8"]]
+ 0055c7f8 ["INT_ADD", "register:40f0:8", ["const:55c7f8:8", "const:4:8"]]
+ 0055c7f8 ["CALL", null, ["callee:0055ca04:8"]]
- 0055c7b8 bytes 83000094
+ 0055c7f8 bytes 83000094
- 0055c7dc ["INT_ADD", "register:40f0:8", ["const:55c7dc:8", "const:4:8"]]
- 0055c7dc ["CALL", null, ["callee:00c57ee0:8"]]
+ 0055c81c ["INT_ADD", "register:40f0:8", ["const:55c81c:8", "const:4:8"]]
+ 0055c81c ["CALL", null, ["callee:00c57ee0:8"]]
- 0055c7dc bytes c1ec1b94
+ 0055c81c bytes b1ed1b94
~~~


<a id="compare-4b5819d3387f4e3d42d0d1389f65bfa7"></a>

### [`0055c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md) → [`0055c888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c888.md) FUN_0055c888

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) [`0055c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`0055c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md) [`0055ca04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055c8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md#insn-0055c8c0) · [`0055c8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md#insn-0055c8e4) · [`0055c910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md#insn-0055c910)
- 新版 `0055c900`（命令位置の公開資料なし） · `0055c924`（命令位置の公開資料なし） · `0055c950`（命令位置の公開資料なし）

~~~diff
- 0055c8c0 ["INT_ADD", "register:40f0:8", ["const:55c8c0:8", "const:4:8"]]
- 0055c8c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055c900 ["INT_ADD", "register:40f0:8", ["const:55c900:8", "const:4:8"]]
+ 0055c900 ["CALL", null, ["callee:00c57e90:8"]]
- 0055c8c0 bytes 74ec1b94
+ 0055c900 bytes 64ed1b94
- 0055c8e4 ["INT_ADD", "register:40f0:8", ["const:55c8e4:8", "const:4:8"]]
- 0055c8e4 ["CALL", null, ["callee:00c58090:8"]]
+ 0055c924 ["INT_ADD", "register:40f0:8", ["const:55c924:8", "const:4:8"]]
+ 0055c924 ["CALL", null, ["callee:00c58090:8"]]
- 0055c8e4 bytes ebec1b94
+ 0055c924 bytes dbed1b94
- 0055c910 ["INT_ADD", "register:40f0:8", ["const:55c910:8", "const:4:8"]]
- 0055c910 ["CALL", null, ["callee:00c58090:8"]]
+ 0055c950 ["INT_ADD", "register:40f0:8", ["const:55c950:8", "const:4:8"]]
+ 0055c950 ["CALL", null, ["callee:00c58090:8"]]
- 0055c910 bytes e0ec1b94
+ 0055c950 bytes d0ed1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4034812e489ea7f4ba746fd65f97cd"></a>

### [`0055ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ccf0.md) → [`0055cd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd30.md) FUN_0055cd30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055cd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ccf0.md#insn-0055cd0c) · [`0055cd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ccf0.md#insn-0055cd2c)
- 新版 `0055cd4c`（命令位置の公開資料なし） · `0055cd6c`（命令位置の公開資料なし）

~~~diff
- 0055cd0c ["INT_ADD", "register:40f0:8", ["const:55cd0c:8", "const:4:8"]]
- 0055cd0c ["CALL", null, ["callee:00c53d00:8"]]
+ 0055cd4c ["INT_ADD", "register:40f0:8", ["const:55cd4c:8", "const:4:8"]]
+ 0055cd4c ["CALL", null, ["callee:00c53d00:8"]]
- 0055cd0c bytes f5da1b94
+ 0055cd4c bytes eddb1b94
- 0055cd2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055cd2c ["INT_ADD", "register:40f0:8", ["const:55cd2c:8", "const:4:8"]]
- 0055cd2c ["CALLIND", null, ["register:0:8"]]
+ 0055cd6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055cd6c ["INT_ADD", "register:40f0:8", ["const:55cd6c:8", "const:4:8"]]
+ 0055cd6c ["CALLIND", null, ["register:0:8"]]
- 0055cd2c bytes 00013fd6
+ 0055cd6c bytes 00013fd6
~~~


<a id="compare-201f3a5496ff02bbd0c4897317b727fe"></a>

### [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) → [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) FUN_0055ce68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0055cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md) [`0055d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md) [`0055d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md) · 呼出先 2件 [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`0055dd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md)
- 新版 呼出元 3件 [`0055d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d030.md) [`0055d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d190.md) [`0055d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d2f0.md) · 呼出先 2件 [`0053c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c178.md) [`0055ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055ddd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ce60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md#insn-0055ce60) · [`0055ceb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md#insn-0055ceb4)
- 新版 `0055cea0`（命令位置の公開資料なし） · `0055cef4`（命令位置の公開資料なし）

~~~diff
- 0055ce60 ["INT_ADD", "register:40f0:8", ["const:55ce60:8", "const:4:8"]]
- 0055ce60 ["CALL", null, ["callee:0055ddd0:8"]]
+ 0055cea0 ["INT_ADD", "register:40f0:8", ["const:55cea0:8", "const:4:8"]]
+ 0055cea0 ["CALL", null, ["callee:0055ddd0:8"]]
- 0055ce60 bytes cc030094
+ 0055cea0 bytes cc030094
- 0055ceb4 ["INT_ADD", "register:40f0:8", ["const:55ceb4:8", "const:4:8"]]
- 0055ceb4 ["CALL", null, ["callee:0053c178:8"]]
+ 0055cef4 ["INT_ADD", "register:40f0:8", ["const:55cef4:8", "const:4:8"]]
+ 0055cef4 ["CALL", null, ["callee:0053c178:8"]]
- 0055ceb4 bytes a17cff97
+ 0055cef4 bytes a17cff97
~~~


<a id="compare-7434ceaf5f172d41340d7922bc65f301"></a>

### [`0055cf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md) → [`0055cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cfb8.md) FUN_0055cfb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055cf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md#insn-0055cf9c) · [`0055cfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md#insn-0055cfb4) · [`0055cfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md#insn-0055cfd8)
- 新版 `0055cfdc`（命令位置の公開資料なし） · `0055cff4`（命令位置の公開資料なし） · `0055d018`（命令位置の公開資料なし）

~~~diff
- 0055cf9c ["INT_ADD", "register:40f0:8", ["const:55cf9c:8", "const:4:8"]]
- 0055cf9c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0055cfdc ["INT_ADD", "register:40f0:8", ["const:55cfdc:8", "const:4:8"]]
+ 0055cfdc ["CALL", null, ["callee:00c53cd0:8"]]
- 0055cf9c bytes 45da1b94
+ 0055cfdc bytes 3ddb1b94
- 0055cfb4 ["INT_ADD", "register:40f0:8", ["const:55cfb4:8", "const:4:8"]]
- 0055cfb4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055cff4 ["INT_ADD", "register:40f0:8", ["const:55cff4:8", "const:4:8"]]
+ 0055cff4 ["CALL", null, ["callee:00c53d00:8"]]
- 0055cfb4 bytes 4bda1b94
+ 0055cff4 bytes 43db1b94
- 0055cfd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055cfd8 ["INT_ADD", "register:40f0:8", ["const:55cfd8:8", "const:4:8"]]
- 0055cfd8 ["CALLIND", null, ["register:0:8"]]
+ 0055d018 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d018 ["INT_ADD", "register:40f0:8", ["const:55d018:8", "const:4:8"]]
+ 0055d018 ["CALLIND", null, ["register:0:8"]]
- 0055cfd8 bytes 00013fd6
+ 0055d018 bytes 00013fd6
~~~


<a id="compare-49a9f51eee8dedd17b5c82c6a66ce011"></a>

### [`0055cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md) → [`0055d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d030.md) FUN_0055d030

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md#insn-0055d038) · [`0055d05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md#insn-0055d05c) · [`0055d080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md#insn-0055d080)
- 新版 `0055d078`（命令位置の公開資料なし） · `0055d09c`（命令位置の公開資料なし） · `0055d0c0`（命令位置の公開資料なし）

~~~diff
- 0055d038 ["INT_ADD", "register:40f0:8", ["const:55d038:8", "const:4:8"]]
- 0055d038 ["CALL", null, ["callee:0055ce68:8"]]
+ 0055d078 ["INT_ADD", "register:40f0:8", ["const:55d078:8", "const:4:8"]]
+ 0055d078 ["CALL", null, ["callee:0055ce68:8"]]
- 0055d038 bytes 7cffff97
+ 0055d078 bytes 7cffff97
- 0055d05c ["INT_ADD", "register:40f0:8", ["const:55d05c:8", "const:4:8"]]
- 0055d05c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0055d09c ["INT_ADD", "register:40f0:8", ["const:55d09c:8", "const:4:8"]]
+ 0055d09c ["CALL", null, ["callee:00c53cd0:8"]]
- 0055d05c bytes 15da1b94
+ 0055d09c bytes 0ddb1b94
- 0055d080 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d080 ["INT_ADD", "register:40f0:8", ["const:55d080:8", "const:4:8"]]
- 0055d080 ["CALLIND", null, ["register:0:8"]]
+ 0055d0c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d0c0 ["INT_ADD", "register:40f0:8", ["const:55d0c0:8", "const:4:8"]]
+ 0055d0c0 ["CALLIND", null, ["register:0:8"]]
- 0055d080 bytes 00013fd6
+ 0055d0c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-291509f1b2afd6cab758ad222a52ea6e"></a>

### [`0055d100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d100.md) → [`0055d140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d140.md) FUN_0055d140

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d100.md#insn-0055d11c) · [`0055d13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d100.md#insn-0055d13c)
- 新版 `0055d15c`（命令位置の公開資料なし） · `0055d17c`（命令位置の公開資料なし）

~~~diff
- 0055d11c ["INT_ADD", "register:40f0:8", ["const:55d11c:8", "const:4:8"]]
- 0055d11c ["CALL", null, ["callee:00c53d00:8"]]
+ 0055d15c ["INT_ADD", "register:40f0:8", ["const:55d15c:8", "const:4:8"]]
+ 0055d15c ["CALL", null, ["callee:00c53d00:8"]]
- 0055d11c bytes f1d91b94
+ 0055d15c bytes e9da1b94
- 0055d13c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d13c ["INT_ADD", "register:40f0:8", ["const:55d13c:8", "const:4:8"]]
- 0055d13c ["CALLIND", null, ["register:0:8"]]
+ 0055d17c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d17c ["INT_ADD", "register:40f0:8", ["const:55d17c:8", "const:4:8"]]
+ 0055d17c ["CALLIND", null, ["register:0:8"]]
- 0055d13c bytes 00013fd6
+ 0055d17c bytes 00013fd6
~~~


<a id="compare-07db30c8f74c6be7295b118debd007c2"></a>

### [`0055d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md) → [`0055d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d190.md) FUN_0055d190

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md#insn-0055d1bc) · [`0055d1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md#insn-0055d1e4) · [`0055d224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md#insn-0055d224)
- 新版 `0055d1fc`（命令位置の公開資料なし） · `0055d224`（命令位置の公開資料なし） · `0055d264`（命令位置の公開資料なし）

~~~diff
- 0055d1bc ["INT_ADD", "register:40f0:8", ["const:55d1bc:8", "const:4:8"]]
- 0055d1bc ["CALL", null, ["callee:0055ce68:8"]]
+ 0055d1fc ["INT_ADD", "register:40f0:8", ["const:55d1fc:8", "const:4:8"]]
+ 0055d1fc ["CALL", null, ["callee:0055ce68:8"]]
- 0055d1bc bytes 1bffff97
+ 0055d1fc bytes 1bffff97
- 0055d1e4 ["INT_ADD", "register:40f0:8", ["const:55d1e4:8", "const:4:8"]]
- 0055d1e4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0055d224 ["INT_ADD", "register:40f0:8", ["const:55d224:8", "const:4:8"]]
+ 0055d224 ["CALL", null, ["callee:00c53cd0:8"]]
- 0055d1e4 bytes b3d91b94
+ 0055d224 bytes abda1b94
- 0055d224 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d224 ["INT_ADD", "register:40f0:8", ["const:55d224:8", "const:4:8"]]
- 0055d224 ["CALLIND", null, ["register:0:8"]]
+ 0055d264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d264 ["INT_ADD", "register:40f0:8", ["const:55d264:8", "const:4:8"]]
+ 0055d264 ["CALLIND", null, ["register:0:8"]]
- 0055d224 bytes 00013fd6
+ 0055d264 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e266dc4aa0a530cbbcaa62241af9307e"></a>

### [`0055d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md) → [`0055d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d2f0.md) FUN_0055d2f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md#insn-0055d2f0) · [`0055d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md#insn-0055d314) · [`0055d334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md#insn-0055d334)
- 新版 `0055d330`（命令位置の公開資料なし） · `0055d354`（命令位置の公開資料なし） · `0055d374`（命令位置の公開資料なし）

~~~diff
- 0055d2f0 ["INT_ADD", "register:40f0:8", ["const:55d2f0:8", "const:4:8"]]
- 0055d2f0 ["CALL", null, ["callee:0055ce68:8"]]
+ 0055d330 ["INT_ADD", "register:40f0:8", ["const:55d330:8", "const:4:8"]]
+ 0055d330 ["CALL", null, ["callee:0055ce68:8"]]
- 0055d2f0 bytes cefeff97
+ 0055d330 bytes cefeff97
- 0055d314 ["INT_ADD", "register:40f0:8", ["const:55d314:8", "const:4:8"]]
- 0055d314 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0055d354 ["INT_ADD", "register:40f0:8", ["const:55d354:8", "const:4:8"]]
+ 0055d354 ["CALL", null, ["callee:00c53cd0:8"]]
- 0055d314 bytes 67d91b94
+ 0055d354 bytes 5fda1b94
- 0055d334 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d334 ["INT_ADD", "register:40f0:8", ["const:55d334:8", "const:4:8"]]
- 0055d334 ["CALLIND", null, ["register:0:8"]]
+ 0055d374 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d374 ["INT_ADD", "register:40f0:8", ["const:55d374:8", "const:4:8"]]
+ 0055d374 ["CALLIND", null, ["register:0:8"]]
- 0055d334 bytes 00013fd6
+ 0055d374 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c94b03198650a8de0a8502c3e791c139"></a>

### [`0055d558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d558.md) → [`0055d598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d598.md) FUN_0055d598

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d558.md#insn-0055d574) · [`0055d594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d558.md#insn-0055d594)
- 新版 `0055d5b4`（命令位置の公開資料なし） · `0055d5d4`（命令位置の公開資料なし）

~~~diff
- 0055d574 ["INT_ADD", "register:40f0:8", ["const:55d574:8", "const:4:8"]]
- 0055d574 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055d5b4 ["INT_ADD", "register:40f0:8", ["const:55d5b4:8", "const:4:8"]]
+ 0055d5b4 ["CALL", null, ["callee:00c53d00:8"]]
- 0055d574 bytes dbd81b94
+ 0055d5b4 bytes d3d91b94
- 0055d594 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d594 ["INT_ADD", "register:40f0:8", ["const:55d594:8", "const:4:8"]]
- 0055d594 ["CALLIND", null, ["register:0:8"]]
+ 0055d5d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d5d4 ["INT_ADD", "register:40f0:8", ["const:55d5d4:8", "const:4:8"]]
+ 0055d5d4 ["CALLIND", null, ["register:0:8"]]
- 0055d594 bytes 00013fd6
+ 0055d5d4 bytes 00013fd6
~~~


<a id="compare-d1f3a9a889ad892b98c2256f4232cfbc"></a>

### [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) → [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) FUN_0055d5e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md) [`0058fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fee8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) [`0058ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md#insn-0055d5f0) · [`0055d620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md#insn-0055d620) · [`0055d638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md#insn-0055d638)
- 新版 `0055d630`（命令位置の公開資料なし） · `0055d660`（命令位置の公開資料なし） · `0055d678`（命令位置の公開資料なし）

~~~diff
- 0055d5f0 ["INT_ADD", "register:40f0:8", ["const:55d5f0:8", "const:4:8"]]
- 0055d5f0 ["CALL", null, ["callee:0055db5c:8"]]
+ 0055d630 ["INT_ADD", "register:40f0:8", ["const:55d630:8", "const:4:8"]]
+ 0055d630 ["CALL", null, ["callee:0055db5c:8"]]
- 0055d5f0 bytes 4b010094
+ 0055d630 bytes 4b010094
- 0055d620 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d620 ["INT_ADD", "register:40f0:8", ["const:55d620:8", "const:4:8"]]
- 0055d620 ["CALLIND", null, ["register:0:8"]]
+ 0055d660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d660 ["INT_ADD", "register:40f0:8", ["const:55d660:8", "const:4:8"]]
+ 0055d660 ["CALLIND", null, ["register:0:8"]]
- 0055d620 bytes 00013fd6
+ 0055d660 bytes 00013fd6
- 0055d638 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d638 ["INT_ADD", "register:40f0:8", ["const:55d638:8", "const:4:8"]]
- 0055d638 ["CALLIND", null, ["register:0:8"]]
+ 0055d678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d678 ["INT_ADD", "register:40f0:8", ["const:55d678:8", "const:4:8"]]
+ 0055d678 ["CALLIND", null, ["register:0:8"]]
- 0055d638 bytes 00013fd6
+ 0055d678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e893ac64b0453158ad450f1780846946"></a>

### [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) → [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) FUN_0055d7c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md) [`0058fe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fe20.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) [`0058fe60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md#insn-0055d7e0) · [`0055d834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md#insn-0055d834) · [`0055d840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md#insn-0055d840)
- 新版 `0055d820`（命令位置の公開資料なし） · `0055d874`（命令位置の公開資料なし） · `0055d880`（命令位置の公開資料なし）

~~~diff
- 0055d7e0 ["INT_ADD", "register:40f0:8", ["const:55d7e0:8", "const:4:8"]]
- 0055d7e0 ["CALL", null, ["callee:0055db5c:8"]]
+ 0055d820 ["INT_ADD", "register:40f0:8", ["const:55d820:8", "const:4:8"]]
+ 0055d820 ["CALL", null, ["callee:0055db5c:8"]]
- 0055d7e0 bytes cf000094
+ 0055d820 bytes cf000094
- 0055d834 ["INT_ADD", "register:40f0:8", ["const:55d834:8", "const:4:8"]]
- 0055d834 ["CALL", null, ["callee:0058fd9c:8"]]
+ 0055d874 ["INT_ADD", "register:40f0:8", ["const:55d874:8", "const:4:8"]]
+ 0055d874 ["CALL", null, ["callee:0058fd9c:8"]]
- 0055d834 bytes 4ac90094
+ 0055d874 bytes 4ac90094
- 0055d840 ["INT_ADD", "register:40f0:8", ["const:55d840:8", "const:4:8"]]
- 0055d840 ["CALL", null, ["callee:0058ff28:8"]]
+ 0055d880 ["INT_ADD", "register:40f0:8", ["const:55d880:8", "const:4:8"]]
+ 0055d880 ["CALL", null, ["callee:0058ff28:8"]]
- 0055d840 bytes aac90094
+ 0055d880 bytes aac90094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014617a49039a5e492043a69fc541526"></a>

### [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) → [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) FUN_0055d99c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) [`0058fc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc00.md) [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) [`0058fc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fc40.md) [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md#insn-0055d994) · [`0055d9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md#insn-0055d9dc) · [`0055d9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md#insn-0055d9e4)
- 新版 `0055d9d4`（命令位置の公開資料なし） · `0055da1c`（命令位置の公開資料なし） · `0055da24`（命令位置の公開資料なし）

~~~diff
- 0055d994 ["INT_ADD", "register:40f0:8", ["const:55d994:8", "const:4:8"]]
- 0055d994 ["CALL", null, ["callee:0055db5c:8"]]
+ 0055d9d4 ["INT_ADD", "register:40f0:8", ["const:55d9d4:8", "const:4:8"]]
+ 0055d9d4 ["CALL", null, ["callee:0055db5c:8"]]
- 0055d994 bytes 62000094
+ 0055d9d4 bytes 62000094
- 0055d9dc ["INT_ADD", "register:40f0:8", ["const:55d9dc:8", "const:4:8"]]
- 0055d9dc ["CALL", null, ["callee:0058fd9c:8"]]
+ 0055da1c ["INT_ADD", "register:40f0:8", ["const:55da1c:8", "const:4:8"]]
+ 0055da1c ["CALL", null, ["callee:0058fd9c:8"]]
- 0055d9dc bytes e0c80094
+ 0055da1c bytes e0c80094
- 0055d9e4 ["INT_ADD", "register:40f0:8", ["const:55d9e4:8", "const:4:8"]]
- 0055d9e4 ["CALL", null, ["callee:0058fc40:8"]]
+ 0055da24 ["INT_ADD", "register:40f0:8", ["const:55da24:8", "const:4:8"]]
+ 0055da24 ["CALL", null, ["callee:0058fc40:8"]]
- 0055d9e4 bytes 87c80094
+ 0055da24 bytes 87c80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-596ef8e9a31bd431d48ceff81a572684"></a>

### [`0055dacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dacc.md) → [`0055db0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db0c.md) FUN_0055db0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055dae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dacc.md#insn-0055dae8) · [`0055db08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dacc.md#insn-0055db08)
- 新版 `0055db28`（命令位置の公開資料なし） · `0055db48`（命令位置の公開資料なし）

~~~diff
- 0055dae8 ["INT_ADD", "register:40f0:8", ["const:55dae8:8", "const:4:8"]]
- 0055dae8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055db28 ["INT_ADD", "register:40f0:8", ["const:55db28:8", "const:4:8"]]
+ 0055db28 ["CALL", null, ["callee:00c53d00:8"]]
- 0055dae8 bytes 7ed71b94
+ 0055db28 bytes 76d81b94
- 0055db08 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055db08 ["INT_ADD", "register:40f0:8", ["const:55db08:8", "const:4:8"]]
- 0055db08 ["CALLIND", null, ["register:0:8"]]
+ 0055db48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055db48 ["INT_ADD", "register:40f0:8", ["const:55db48:8", "const:4:8"]]
+ 0055db48 ["CALLIND", null, ["register:0:8"]]
- 0055db08 bytes 00013fd6
+ 0055db48 bytes 00013fd6
~~~


<a id="compare-b58093397861495e25d58d546ca0c89a"></a>

### [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) → [`0055db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055db5c.md) FUN_0055db5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 4件 [`0058ff4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff4c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 4件 [`0058ff8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff8c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md#insn-0055db54) · [`0055db74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md#insn-0055db74) · [`0055db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md#insn-0055db88)
- 新版 `0055db94`（命令位置の公開資料なし） · `0055dbb4`（命令位置の公開資料なし） · `0055dbc8`（命令位置の公開資料なし）

~~~diff
- 0055db54 ["INT_ADD", "register:40f0:8", ["const:55db54:8", "const:4:8"]]
- 0055db54 ["CALL", null, ["callee:0058ff8c:8"]]
+ 0055db94 ["INT_ADD", "register:40f0:8", ["const:55db94:8", "const:4:8"]]
+ 0055db94 ["CALL", null, ["callee:0058ff8c:8"]]
- 0055db54 bytes fec80094
+ 0055db94 bytes fec80094
- 0055db74 ["INT_ADD", "register:40f0:8", ["const:55db74:8", "const:4:8"]]
- 0055db74 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055dbb4 ["INT_ADD", "register:40f0:8", ["const:55dbb4:8", "const:4:8"]]
+ 0055dbb4 ["CALL", null, ["callee:00c53d00:8"]]
- 0055db74 bytes 5bd71b94
+ 0055dbb4 bytes 53d81b94
- 0055db88 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055db88 ["INT_ADD", "register:40f0:8", ["const:55db88:8", "const:4:8"]]
- 0055db88 ["CALLIND", null, ["register:0:8"]]
+ 0055dbc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055dbc8 ["INT_ADD", "register:40f0:8", ["const:55dbc8:8", "const:4:8"]]
+ 0055dbc8 ["CALLIND", null, ["register:0:8"]]
- 0055db88 bytes 00013fd6
+ 0055dbc8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79576276af67a9d5dc93c58c3833282b"></a>

### [`0055dd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md) → [`0055ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055ddd0.md) FUN_0055ddd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) · 呼出先 5件 [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) · 呼出先 5件 [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ddd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md#insn-0055ddd4) · [`0055de1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md#insn-0055de1c) · [`0055de44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md#insn-0055de44)
- 新版 `0055de14`（命令位置の公開資料なし） · `0055de5c`（命令位置の公開資料なし） · `0055de84`（命令位置の公開資料なし）

~~~diff
- 0055ddd4 ["INT_ADD", "register:40f0:8", ["const:55ddd4:8", "const:4:8"]]
- 0055ddd4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0055de14 ["INT_ADD", "register:40f0:8", ["const:55de14:8", "const:4:8"]]
+ 0055de14 ["CALL", null, ["callee:00c57eb0:8"]]
- 0055ddd4 bytes 37e71b94
+ 0055de14 bytes 27e81b94
- 0055de1c ["INT_ADD", "register:40f0:8", ["const:55de1c:8", "const:4:8"]]
- 0055de1c ["CALL", null, ["callee:00c57e90:8"]]
+ 0055de5c ["INT_ADD", "register:40f0:8", ["const:55de5c:8", "const:4:8"]]
+ 0055de5c ["CALL", null, ["callee:00c57e90:8"]]
- 0055de1c bytes 1de71b94
+ 0055de5c bytes 0de81b94
- 0055de44 ["INT_ADD", "register:40f0:8", ["const:55de44:8", "const:4:8"]]
- 0055de44 ["CALL", null, ["callee:00c58000:8"]]
+ 0055de84 ["INT_ADD", "register:40f0:8", ["const:55de84:8", "const:4:8"]]
+ 0055de84 ["CALL", null, ["callee:00c58000:8"]]
- 0055de44 bytes 6fe71b94
+ 0055de84 bytes 5fe81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c50ed036dd664fbe484e6e8b21f4b57"></a>

### [`0055dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md) → [`0055df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055df00.md) FUN_0055df00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0055d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d4c8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055df34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md#insn-0055df34) · [`0055dfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md#insn-0055dfac) · [`0055dfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md#insn-0055dfec)
- 新版 `0055df74`（命令位置の公開資料なし） · `0055dfec`（命令位置の公開資料なし） · `0055e02c`（命令位置の公開資料なし）

~~~diff
- 0055df34 ["INT_ADD", "register:40f0:8", ["const:55df34:8", "const:4:8"]]
- 0055df34 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055df74 ["INT_ADD", "register:40f0:8", ["const:55df74:8", "const:4:8"]]
+ 0055df74 ["CALL", null, ["callee:00c57e90:8"]]
- 0055df34 bytes d7e61b94
+ 0055df74 bytes c7e71b94
- 0055dfac ["INT_ADD", "register:40f0:8", ["const:55dfac:8", "const:4:8"]]
- 0055dfac ["CALL", null, ["callee:00c58000:8"]]
+ 0055dfec ["INT_ADD", "register:40f0:8", ["const:55dfec:8", "const:4:8"]]
+ 0055dfec ["CALL", null, ["callee:00c58000:8"]]
- 0055dfac bytes 15e71b94
+ 0055dfec bytes 05e81b94
- 0055dfec ["INT_ADD", "register:40f0:8", ["const:55dfec:8", "const:4:8"]]
- 0055dfec ["CALL", null, ["callee:0046c44c:8"]]
+ 0055e02c ["INT_ADD", "register:40f0:8", ["const:55e02c:8", "const:4:8"]]
+ 0055e02c ["CALL", null, ["callee:0046c44c:8"]]
- 0055dfec bytes 0839fc97
+ 0055e02c bytes 0839fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e39273ef41580bf5e802048c747a780f"></a>

### [`0055dff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md) → [`0055e034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e034.md) FUN_0055e034

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cd40.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0055cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd80.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md#insn-0055e078) · [`0055e0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md#insn-0055e0b0) · [`0055e118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md#insn-0055e118)
- 新版 `0055e0b8`（命令位置の公開資料なし） · `0055e0f0`（命令位置の公開資料なし） · `0055e158`（命令位置の公開資料なし）

~~~diff
- 0055e078 ["INT_ADD", "register:40f0:8", ["const:55e078:8", "const:4:8"]]
- 0055e078 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055e0b8 ["INT_ADD", "register:40f0:8", ["const:55e0b8:8", "const:4:8"]]
+ 0055e0b8 ["CALL", null, ["callee:00c57e90:8"]]
- 0055e078 bytes 86e61b94
+ 0055e0b8 bytes 76e71b94
- 0055e0b0 ["INT_ADD", "register:40f0:8", ["const:55e0b0:8", "const:4:8"]]
- 0055e0b0 ["CALL", null, ["callee:00c57f40:8"]]
+ 0055e0f0 ["INT_ADD", "register:40f0:8", ["const:55e0f0:8", "const:4:8"]]
+ 0055e0f0 ["CALL", null, ["callee:00c57f40:8"]]
- 0055e0b0 bytes a4e61b94
+ 0055e0f0 bytes 94e71b94
- 0055e118 ["INT_ADD", "register:40f0:8", ["const:55e118:8", "const:4:8"]]
- 0055e118 ["CALL", null, ["callee:00c57f40:8"]]
+ 0055e158 ["INT_ADD", "register:40f0:8", ["const:55e158:8", "const:4:8"]]
+ 0055e158 ["CALL", null, ["callee:00c57f40:8"]]
- 0055e118 bytes 8ae61b94
+ 0055e158 bytes 7ae71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0895642908c933ea5fe83d906c6d6d1c"></a>

### [`0055e1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md) → [`0055e218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e218.md) FUN_0055e218

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cd40.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0055cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd80.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md#insn-0055e260) · [`0055e29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md#insn-0055e29c) · [`0055e324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md#insn-0055e324)
- 新版 `0055e2a0`（命令位置の公開資料なし） · `0055e2dc`（命令位置の公開資料なし） · `0055e364`（命令位置の公開資料なし）

~~~diff
- 0055e260 ["INT_ADD", "register:40f0:8", ["const:55e260:8", "const:4:8"]]
- 0055e260 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055e2a0 ["INT_ADD", "register:40f0:8", ["const:55e2a0:8", "const:4:8"]]
+ 0055e2a0 ["CALL", null, ["callee:00c57e90:8"]]
- 0055e260 bytes 0ce61b94
+ 0055e2a0 bytes fce61b94
- 0055e29c ["INT_ADD", "register:40f0:8", ["const:55e29c:8", "const:4:8"]]
- 0055e29c ["CALL", null, ["callee:00c57f40:8"]]
+ 0055e2dc ["INT_ADD", "register:40f0:8", ["const:55e2dc:8", "const:4:8"]]
+ 0055e2dc ["CALL", null, ["callee:00c57f40:8"]]
- 0055e29c bytes 29e61b94
+ 0055e2dc bytes 19e71b94
- 0055e324 ["INT_ADD", "register:40f0:8", ["const:55e324:8", "const:4:8"]]
- 0055e324 ["CALL", null, ["callee:00c58000:8"]]
+ 0055e364 ["INT_ADD", "register:40f0:8", ["const:55e364:8", "const:4:8"]]
+ 0055e364 ["CALL", null, ["callee:00c58000:8"]]
- 0055e324 bytes 37e61b94
+ 0055e364 bytes 27e71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6794e690cb8f669539576db081df5a4f"></a>

### [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) → [`0055e6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e6f4.md) FUN_0055e6f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md#insn-0055e6d8) · [`0055e6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md#insn-0055e6f8)
- 新版 `0055e718`（命令位置の公開資料なし） · `0055e738`（命令位置の公開資料なし）

~~~diff
- 0055e6d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055e6d8 ["INT_ADD", "register:40f0:8", ["const:55e6d8:8", "const:4:8"]]
- 0055e6d8 ["CALLIND", null, ["register:0:8"]]
+ 0055e718 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055e718 ["INT_ADD", "register:40f0:8", ["const:55e718:8", "const:4:8"]]
+ 0055e718 ["CALLIND", null, ["register:0:8"]]
- 0055e6d8 bytes 00013fd6
+ 0055e718 bytes 00013fd6
- 0055e6f8 ["INT_ADD", "register:40f0:8", ["const:55e6f8:8", "const:4:8"]]
- 0055e6f8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0055e738 ["INT_ADD", "register:40f0:8", ["const:55e738:8", "const:4:8"]]
+ 0055e738 ["CALL", null, ["callee:00c53cd0:8"]]
- 0055e6f8 bytes 6ed41b94
+ 0055e738 bytes 66d51b94
~~~


<a id="compare-1a97131400b455687b49f78a81fb58d3"></a>

### [`0055e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md) → [`0055e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md) FUN_0055e750

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d330.md) · 呼出先 4件 [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0048d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md) · 呼出先 4件 [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md#insn-0055e740) · [`0055e75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md#insn-0055e75c) · [`0055e770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md#insn-0055e770)
- 新版 `0055e780`（命令位置の公開資料なし） · `0055e79c`（命令位置の公開資料なし） · `0055e7b0`（命令位置の公開資料なし）

~~~diff
- 0055e740 ["INT_ADD", "register:40f0:8", ["const:55e740:8", "const:4:8"]]
- 0055e740 ["CALL", null, ["callee:00581a34:8"]]
+ 0055e780 ["INT_ADD", "register:40f0:8", ["const:55e780:8", "const:4:8"]]
+ 0055e780 ["CALL", null, ["callee:00581a34:8"]]
- 0055e740 bytes ad8c0094
+ 0055e780 bytes ad8c0094
- 0055e75c ["COPY", "register:0:8", ["register:4048:8"]]
- 0055e75c ["INT_ADD", "register:40f0:8", ["const:55e75c:8", "const:4:8"]]
- 0055e75c ["CALLIND", null, ["register:0:8"]]
+ 0055e79c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055e79c ["INT_ADD", "register:40f0:8", ["const:55e79c:8", "const:4:8"]]
+ 0055e79c ["CALLIND", null, ["register:0:8"]]
- 0055e75c bytes 20013fd6
+ 0055e79c bytes 20013fd6
- 0055e770 ["INT_ADD", "register:40f0:8", ["const:55e770:8", "const:4:8"]]
- 0055e770 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055e7b0 ["INT_ADD", "register:40f0:8", ["const:55e7b0:8", "const:4:8"]]
+ 0055e7b0 ["CALL", null, ["callee:00c53d00:8"]]
- 0055e770 bytes 5cd41b94
+ 0055e7b0 bytes 54d51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-835c03237faa8784bb947912200b50c3"></a>

### [`0055e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md) → [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md) FUN_0055e874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) [`0048d27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d27c.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 4件 [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`0048d2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 4件 [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md#insn-0055e870) · [`0055e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md#insn-0055e880) · [`0055e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md#insn-0055e89c)
- 新版 `0055e8b0`（命令位置の公開資料なし） · `0055e8c0`（命令位置の公開資料なし） · `0055e8dc`（命令位置の公開資料なし）

~~~diff
- 0055e870 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055e870 ["INT_ADD", "register:40f0:8", ["const:55e870:8", "const:4:8"]]
- 0055e870 ["CALLIND", null, ["register:0:8"]]
+ 0055e8b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055e8b0 ["INT_ADD", "register:40f0:8", ["const:55e8b0:8", "const:4:8"]]
+ 0055e8b0 ["CALLIND", null, ["register:0:8"]]
- 0055e870 bytes 00013fd6
+ 0055e8b0 bytes 00013fd6
- 0055e880 ["INT_ADD", "register:40f0:8", ["const:55e880:8", "const:4:8"]]
- 0055e880 ["CALL", null, ["callee:00581a34:8"]]
+ 0055e8c0 ["INT_ADD", "register:40f0:8", ["const:55e8c0:8", "const:4:8"]]
+ 0055e8c0 ["CALL", null, ["callee:00581a34:8"]]
- 0055e880 bytes 5d8c0094
+ 0055e8c0 bytes 5d8c0094
- 0055e89c ["COPY", "register:0:8", ["register:4048:8"]]
- 0055e89c ["INT_ADD", "register:40f0:8", ["const:55e89c:8", "const:4:8"]]
- 0055e89c ["CALLIND", null, ["register:0:8"]]
+ 0055e8dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055e8dc ["INT_ADD", "register:40f0:8", ["const:55e8dc:8", "const:4:8"]]
+ 0055e8dc ["CALLIND", null, ["register:0:8"]]
- 0055e89c bytes 20013fd6
+ 0055e8dc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6bba3e15aabde0097c120019da58751"></a>

### [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md) → [`0055e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md) FUN_0055e9c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`007650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007650e8.md) [`007656e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`00765128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765128.md) [`00765728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765728.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md#insn-0055e9d4) · [`0055e9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md#insn-0055e9f0) · [`0055ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md#insn-0055ea04)
- 新版 `0055ea14`（命令位置の公開資料なし） · `0055ea30`（命令位置の公開資料なし） · `0055ea44`（命令位置の公開資料なし）

~~~diff
- 0055e9d4 ["INT_ADD", "register:40f0:8", ["const:55e9d4:8", "const:4:8"]]
- 0055e9d4 ["CALL", null, ["callee:00581aa8:8"]]
+ 0055ea14 ["INT_ADD", "register:40f0:8", ["const:55ea14:8", "const:4:8"]]
+ 0055ea14 ["CALL", null, ["callee:00581aa8:8"]]
- 0055e9d4 bytes 258c0094
+ 0055ea14 bytes 258c0094
- 0055e9f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055e9f0 ["INT_ADD", "register:40f0:8", ["const:55e9f0:8", "const:4:8"]]
- 0055e9f0 ["CALLIND", null, ["register:0:8"]]
+ 0055ea30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055ea30 ["INT_ADD", "register:40f0:8", ["const:55ea30:8", "const:4:8"]]
+ 0055ea30 ["CALLIND", null, ["register:0:8"]]
- 0055e9f0 bytes 20013fd6
+ 0055ea30 bytes 20013fd6
- 0055ea04 ["INT_ADD", "register:40f0:8", ["const:55ea04:8", "const:4:8"]]
- 0055ea04 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055ea44 ["INT_ADD", "register:40f0:8", ["const:55ea44:8", "const:4:8"]]
+ 0055ea44 ["CALL", null, ["callee:00c53d00:8"]]
- 0055ea04 bytes b7d31b94
+ 0055ea44 bytes afd41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80b06d4061f374a486576ca668984759"></a>

### [`0055eadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md) → [`0055eb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md) FUN_0055eb1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044ff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044ff1c.md) · 呼出先 4件 [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0044ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md) · 呼出先 4件 [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md#insn-0055eb20) · [`0055eb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md#insn-0055eb34) · [`0055eb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md#insn-0055eb50)
- 新版 `0055eb60`（命令位置の公開資料なし） · `0055eb74`（命令位置の公開資料なし） · `0055eb90`（命令位置の公開資料なし）

~~~diff
- 0055eb20 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055eb20 ["INT_ADD", "register:40f0:8", ["const:55eb20:8", "const:4:8"]]
- 0055eb20 ["CALLIND", null, ["register:0:8"]]
+ 0055eb60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055eb60 ["INT_ADD", "register:40f0:8", ["const:55eb60:8", "const:4:8"]]
+ 0055eb60 ["CALLIND", null, ["register:0:8"]]
- 0055eb20 bytes 00013fd6
+ 0055eb60 bytes 00013fd6
- 0055eb34 ["INT_ADD", "register:40f0:8", ["const:55eb34:8", "const:4:8"]]
- 0055eb34 ["CALL", null, ["callee:00581aa8:8"]]
+ 0055eb74 ["INT_ADD", "register:40f0:8", ["const:55eb74:8", "const:4:8"]]
+ 0055eb74 ["CALL", null, ["callee:00581aa8:8"]]
- 0055eb34 bytes cd8b0094
+ 0055eb74 bytes cd8b0094
- 0055eb50 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055eb50 ["INT_ADD", "register:40f0:8", ["const:55eb50:8", "const:4:8"]]
- 0055eb50 ["CALLIND", null, ["register:0:8"]]
+ 0055eb90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055eb90 ["INT_ADD", "register:40f0:8", ["const:55eb90:8", "const:4:8"]]
+ 0055eb90 ["CALLIND", null, ["register:0:8"]]
- 0055eb50 bytes 20013fd6
+ 0055eb90 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55792decc473d6fb06c10829d496a3c8"></a>

### [`0055eca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eca0.md) → [`0055ece0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ece0.md) FUN_0055ece0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eca0.md#insn-0055ecbc)
- 新版 `0055ecfc`（命令位置の公開資料なし）

~~~diff
- 0055ecbc ["INT_ADD", "register:40f0:8", ["const:55ecbc:8", "const:4:8"]]
- 0055ecbc ["CALL", null, ["callee:00c53cd0:8"]]
+ 0055ecfc ["INT_ADD", "register:40f0:8", ["const:55ecfc:8", "const:4:8"]]
+ 0055ecfc ["CALL", null, ["callee:00c53cd0:8"]]
- 0055ecbc bytes fdd21b94
+ 0055ecfc bytes f5d31b94
~~~


<a id="compare-4167f9c61a5258505420096573296035"></a>

### [`0055f058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md) → [`0055f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md) FUN_0055f098

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0048d7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d7dc.md) [`0048d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d8dc.md) · 呼出先 5件 [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0048d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md) [`0048d91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d91c.md) · 呼出先 5件 [`00581764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md) [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055f0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md#insn-0055f0a0) · [`0055f0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md#insn-0055f0b8) · [`0055f0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md#insn-0055f0d4)
- 新版 `0055f0e0`（命令位置の公開資料なし） · `0055f0f8`（命令位置の公開資料なし） · `0055f114`（命令位置の公開資料なし）

~~~diff
- 0055f0a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055f0a0 ["INT_ADD", "register:40f0:8", ["const:55f0a0:8", "const:4:8"]]
- 0055f0a0 ["CALLIND", null, ["register:0:8"]]
+ 0055f0e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055f0e0 ["INT_ADD", "register:40f0:8", ["const:55f0e0:8", "const:4:8"]]
+ 0055f0e0 ["CALLIND", null, ["register:0:8"]]
- 0055f0a0 bytes 00013fd6
+ 0055f0e0 bytes 00013fd6
- 0055f0b8 ["INT_ADD", "register:40f0:8", ["const:55f0b8:8", "const:4:8"]]
- 0055f0b8 ["CALL", null, ["callee:00581764:8"]]
+ 0055f0f8 ["INT_ADD", "register:40f0:8", ["const:55f0f8:8", "const:4:8"]]
+ 0055f0f8 ["CALL", null, ["callee:00581764:8"]]
- 0055f0b8 bytes 9b890094
+ 0055f0f8 bytes 9b890094
- 0055f0d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055f0d4 ["INT_ADD", "register:40f0:8", ["const:55f0d4:8", "const:4:8"]]
- 0055f0d4 ["CALLIND", null, ["register:0:8"]]
+ 0055f114 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055f114 ["INT_ADD", "register:40f0:8", ["const:55f114:8", "const:4:8"]]
+ 0055f114 ["CALLIND", null, ["register:0:8"]]
- 0055f0d4 bytes 20013fd6
+ 0055f114 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d33d7ffb332694e3d771ff49f04b9fb"></a>

### [`0055fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md) → [`0055febc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055febc.md) FUN_0055febc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056052c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056056c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056056c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055feb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md#insn-0055feb0) · [`0055fed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md#insn-0055fed4)
- 新版 `0055fef0`（命令位置の公開資料なし） · `0055ff14`（命令位置の公開資料なし）

~~~diff
- 0055feb0 ["INT_ADD", "register:40f0:8", ["const:55feb0:8", "const:4:8"]]
- 0055feb0 ["CALL", null, ["callee:0056056c:8"]]
+ 0055fef0 ["INT_ADD", "register:40f0:8", ["const:55fef0:8", "const:4:8"]]
+ 0055fef0 ["CALL", null, ["callee:0056056c:8"]]
- 0055feb0 bytes 9f010094
+ 0055fef0 bytes 9f010094
- 0055fed4 ["INT_ADD", "register:40f0:8", ["const:55fed4:8", "const:4:8"]]
- 0055fed4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0055ff14 ["INT_ADD", "register:40f0:8", ["const:55ff14:8", "const:4:8"]]
+ 0055ff14 ["CALL", null, ["callee:00c57ee0:8"]]
- 0055fed4 bytes 03df1b94
+ 0055ff14 bytes f3df1b94
~~~


<a id="compare-5e3e1119c0f4ca0ac43965832de4038a"></a>

### [`00560428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md) → [`00560468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560468.md) FUN_00560468

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) [`0055f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`0055f578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md) [`0055f618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f618.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md#insn-00560444) · [`00560464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md#insn-00560464)
- 新版 `00560484`（命令位置の公開資料なし） · `005604a4`（命令位置の公開資料なし）

~~~diff
- 00560444 ["INT_ADD", "register:40f0:8", ["const:560444:8", "const:4:8"]]
- 00560444 ["CALL", null, ["callee:00c53d00:8"]]
+ 00560484 ["INT_ADD", "register:40f0:8", ["const:560484:8", "const:4:8"]]
+ 00560484 ["CALL", null, ["callee:00c53d00:8"]]
- 00560444 bytes 27cd1b94
+ 00560484 bytes 1fce1b94
- 00560464 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560464 ["INT_ADD", "register:40f0:8", ["const:560464:8", "const:4:8"]]
- 00560464 ["CALLIND", null, ["register:0:8"]]
+ 005604a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005604a4 ["INT_ADD", "register:40f0:8", ["const:5604a4:8", "const:4:8"]]
+ 005604a4 ["CALLIND", null, ["register:0:8"]]
- 00560464 bytes 00013fd6
+ 005604a4 bytes 00013fd6
~~~


<a id="compare-708fae36e49ec563636f5b0365115e72"></a>

### [`0056052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056052c.md) → [`0056056c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056056c.md) FUN_0056056c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md) · 呼出先 1件 [`00c59be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59be0.md)
- 新版 呼出元 1件 [`0055febc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055febc.md) · 呼出先 1件 [`00c59fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005606c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056052c.md#insn-005606c0)
- 新版 `00560700`（命令位置の公開資料なし）

~~~diff
- 005606c0 ["INT_ADD", "register:40f0:8", ["const:5606c0:8", "const:4:8"]]
- 005606c0 ["CALL", null, ["callee:00c59fe0:8"]]
+ 00560700 ["INT_ADD", "register:40f0:8", ["const:560700:8", "const:4:8"]]
+ 00560700 ["CALL", null, ["callee:00c59fe0:8"]]
- 005606c0 bytes 48e51b94
+ 00560700 bytes 38e61b94
~~~


<a id="compare-3723def4db371d796fcdc74b53db57e6"></a>

### [`00560ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md) → [`00560b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md) FUN_00560b08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) · 呼出先 2件 [`00560ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) · 呼出先 2件 [`00560ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md#insn-00560ae8) · [`00560af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md#insn-00560af8)
- 新版 `00560b28`（命令位置の公開資料なし） · `00560b38`（命令位置の公開資料なし）

~~~diff
- 00560ae8 ["INT_ADD", "register:40f0:8", ["const:560ae8:8", "const:4:8"]]
- 00560ae8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00560b28 ["INT_ADD", "register:40f0:8", ["const:560b28:8", "const:4:8"]]
+ 00560b28 ["CALL", null, ["callee:00c57e90:8"]]
- 00560ae8 bytes eadb1b94
+ 00560b28 bytes dadc1b94
- 00560af8 ["INT_ADD", "register:40f0:8", ["const:560af8:8", "const:4:8"]]
- 00560af8 ["CALL", null, ["callee:00560ee0:8"]]
+ 00560b38 ["INT_ADD", "register:40f0:8", ["const:560b38:8", "const:4:8"]]
+ 00560b38 ["CALL", null, ["callee:00560ee0:8"]]
- 00560af8 bytes ea000094
+ 00560b38 bytes ea000094
~~~


<a id="compare-36c8a992e29fbafd9cda901cb3e1ca1d"></a>

### [`00560e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e08.md) → [`00560e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e48.md) FUN_00560e48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00560864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005608a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e08.md#insn-00560e44)
- 新版 `00560e84`（命令位置の公開資料なし）

~~~diff
- 00560e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560e44 ["INT_ADD", "register:40f0:8", ["const:560e44:8", "const:4:8"]]
- 00560e44 ["CALLIND", null, ["register:0:8"]]
+ 00560e84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560e84 ["INT_ADD", "register:40f0:8", ["const:560e84:8", "const:4:8"]]
+ 00560e84 ["CALLIND", null, ["register:0:8"]]
- 00560e44 bytes 00013fd6
+ 00560e84 bytes 00013fd6
~~~


<a id="compare-b9163dbde636a383f4035ffe5e027562"></a>

### [`00560e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e58.md) → [`00560e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e98.md) FUN_00560e98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e58.md#insn-00560e74)
- 新版 `00560eb4`（命令位置の公開資料なし）

~~~diff
- 00560e74 ["INT_ADD", "register:40f0:8", ["const:560e74:8", "const:4:8"]]
- 00560e74 ["CALL", null, ["callee:00459d74:8"]]
+ 00560eb4 ["INT_ADD", "register:40f0:8", ["const:560eb4:8", "const:4:8"]]
+ 00560eb4 ["CALL", null, ["callee:00459d74:8"]]
- 00560e74 bytes b0e3fb97
+ 00560eb4 bytes b0e3fb97
~~~


<a id="compare-361cc0108a1188578c6c6efe81cbaa10"></a>

### [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) → [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) FUN_00561014

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 2件 [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) [`00562f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md)
- 新版 呼出元 1件 [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 2件 [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) [`00562fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md#insn-00560ff4) · [`00561008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md#insn-00561008)
- 新版 `00561034`（命令位置の公開資料なし） · `00561048`（命令位置の公開資料なし）

~~~diff
- 00560ff4 ["INT_ADD", "register:40f0:8", ["const:560ff4:8", "const:4:8"]]
- 00560ff4 ["CALL", null, ["callee:00562fc8:8"]]
+ 00561034 ["INT_ADD", "register:40f0:8", ["const:561034:8", "const:4:8"]]
+ 00561034 ["CALL", null, ["callee:00562fc8:8"]]
- 00560ff4 bytes e5070094
+ 00561034 bytes e5070094
- 00561008 ["INT_ADD", "register:40f0:8", ["const:561008:8", "const:4:8"]]
- 00561008 ["CALL", null, ["callee:00562d90:8"]]
+ 00561048 ["INT_ADD", "register:40f0:8", ["const:561048:8", "const:4:8"]]
+ 00561048 ["CALL", null, ["callee:00562d90:8"]]
- 00561008 bytes 52070094
+ 00561048 bytes 52070094
~~~


<a id="compare-4c46a07fc4ae1da763ec87f81a372b53"></a>

### [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) → [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) FUN_00561064

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 2件 [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) [`005632a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md)
- 新版 呼出元 2件 [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 2件 [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) [`005632e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md#insn-00561044) · [`00561058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md#insn-00561058)
- 新版 `00561084`（命令位置の公開資料なし） · `00561098`（命令位置の公開資料なし）

~~~diff
- 00561044 ["INT_ADD", "register:40f0:8", ["const:561044:8", "const:4:8"]]
- 00561044 ["CALL", null, ["callee:005632e0:8"]]
+ 00561084 ["INT_ADD", "register:40f0:8", ["const:561084:8", "const:4:8"]]
+ 00561084 ["CALL", null, ["callee:005632e0:8"]]
- 00561044 bytes 97080094
+ 00561084 bytes 97080094
- 00561058 ["INT_ADD", "register:40f0:8", ["const:561058:8", "const:4:8"]]
- 00561058 ["CALL", null, ["callee:00563098:8"]]
+ 00561098 ["INT_ADD", "register:40f0:8", ["const:561098:8", "const:4:8"]]
+ 00561098 ["CALL", null, ["callee:00563098:8"]]
- 00561058 bytes 00080094
+ 00561098 bytes 00080094
~~~


<a id="compare-f8a815db7fa3f7a439e130af7aae8b1b"></a>

### [`00561f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f4c.md) → [`00561f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561f8c.md) FUN_00561f8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f4c.md#insn-00561f68)
- 新版 `00561fa8`（命令位置の公開資料なし）

~~~diff
- 00561f68 ["INT_ADD", "register:40f0:8", ["const:561f68:8", "const:4:8"]]
- 00561f68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00561fa8 ["INT_ADD", "register:40f0:8", ["const:561fa8:8", "const:4:8"]]
+ 00561fa8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00561f68 bytes d2d61b94
+ 00561fa8 bytes c2d71b94
~~~


<a id="compare-230ed8c49f16e9db1e9ca022a5c6e1b5"></a>

### [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) → [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) FUN_005626f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`00561f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md) [`0056385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md) [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006d0264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0264.md) · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 20件 [`00561fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md) [`0056389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006d02a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d0/006d02a4.md) · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md#insn-00562794) · [`005627a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md#insn-005627a8) · [`00562844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md#insn-00562844)
- 新版 `005627d4`（命令位置の公開資料なし） · `005627e8`（命令位置の公開資料なし） · `00562884`（命令位置の公開資料なし）

~~~diff
- 00562794 ["INT_ADD", "register:40f0:8", ["const:562794:8", "const:4:8"]]
- 00562794 ["CALL", null, ["callee:00c57fd0:8"]]
+ 005627d4 ["INT_ADD", "register:40f0:8", ["const:5627d4:8", "const:4:8"]]
+ 005627d4 ["CALL", null, ["callee:00c57fd0:8"]]
- 00562794 bytes 0fd51b94
+ 005627d4 bytes ffd51b94
- 005627a8 ["INT_ADD", "register:40f0:8", ["const:5627a8:8", "const:4:8"]]
- 005627a8 ["CALL", null, ["callee:00c58050:8"]]
+ 005627e8 ["INT_ADD", "register:40f0:8", ["const:5627e8:8", "const:4:8"]]
+ 005627e8 ["CALL", null, ["callee:00c58050:8"]]
- 005627a8 bytes 2ad51b94
+ 005627e8 bytes 1ad61b94
- 00562844 ["INT_ADD", "register:40f0:8", ["const:562844:8", "const:4:8"]]
- 00562844 ["CALL", null, ["callee:00c57e90:8"]]
+ 00562884 ["INT_ADD", "register:40f0:8", ["const:562884:8", "const:4:8"]]
+ 00562884 ["CALL", null, ["callee:00c57e90:8"]]
- 00562844 bytes 93d41b94
+ 00562884 bytes 83d51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d4428713ddc859c1c148b822f4455d5"></a>

### [`00562c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c44.md) → [`00562c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562c84.md) FUN_00562c84

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c44.md#insn-00562c6c)
- 新版 `00562cac`（命令位置の公開資料なし）

~~~diff
- 00562c6c ["INT_ADD", "register:40f0:8", ["const:562c6c:8", "const:4:8"]]
- 00562c6c ["CALL", null, ["callee:00562cf0:8"]]
+ 00562cac ["INT_ADD", "register:40f0:8", ["const:562cac:8", "const:4:8"]]
+ 00562cac ["CALL", null, ["callee:00562cf0:8"]]
- 00562c6c bytes 11000094
+ 00562cac bytes 11000094
~~~


<a id="compare-a239d9d03d07c9a6e68a04b4101cbfba"></a>

### [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) → [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) FUN_00562cf0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00562c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c44.md) [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) [`005633e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633e4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`00562c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562c84.md) [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) [`00563424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563424.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md#insn-00562ce8) · [`00562cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md#insn-00562cf8) · [`00562d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md#insn-00562d08)
- 新版 `00562d28`（命令位置の公開資料なし） · `00562d38`（命令位置の公開資料なし） · `00562d48`（命令位置の公開資料なし）

~~~diff
- 00562ce8 ["INT_ADD", "register:40f0:8", ["const:562ce8:8", "const:4:8"]]
- 00562ce8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00562d28 ["INT_ADD", "register:40f0:8", ["const:562d28:8", "const:4:8"]]
+ 00562d28 ["CALL", null, ["callee:00c57eb0:8"]]
- 00562ce8 bytes 72d31b94
+ 00562d28 bytes 62d41b94
- 00562cf8 ["INT_ADD", "register:40f0:8", ["const:562cf8:8", "const:4:8"]]
- 00562cf8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00562d38 ["INT_ADD", "register:40f0:8", ["const:562d38:8", "const:4:8"]]
+ 00562d38 ["CALL", null, ["callee:00c57eb0:8"]]
- 00562cf8 bytes 6ed31b94
+ 00562d38 bytes 5ed41b94
- 00562d08 ["INT_ADD", "register:40f0:8", ["const:562d08:8", "const:4:8"]]
- 00562d08 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00562d48 ["INT_ADD", "register:40f0:8", ["const:562d48:8", "const:4:8"]]
+ 00562d48 ["CALL", null, ["callee:00c57eb0:8"]]
- 00562d08 bytes 6ad31b94
+ 00562d48 bytes 5ad41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5a64f70a10720cb3656f94709de9a51"></a>

### [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) → [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) FUN_00562d90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00562c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md) [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`00562f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00562cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md) [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`00562fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md#insn-00562e14) · [`00562e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md#insn-00562e44) · [`00562ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md#insn-00562ed8)
- 新版 `00562e54`（命令位置の公開資料なし） · `00562e84`（命令位置の公開資料なし） · `00562f18`（命令位置の公開資料なし）

~~~diff
- 00562e14 ["INT_ADD", "register:40f0:8", ["const:562e14:8", "const:4:8"]]
- 00562e14 ["CALL", null, ["callee:00c57e90:8"]]
+ 00562e54 ["INT_ADD", "register:40f0:8", ["const:562e54:8", "const:4:8"]]
+ 00562e54 ["CALL", null, ["callee:00c57e90:8"]]
- 00562e14 bytes 1fd31b94
+ 00562e54 bytes 0fd41b94
- 00562e44 ["INT_ADD", "register:40f0:8", ["const:562e44:8", "const:4:8"]]
- 00562e44 ["CALL", null, ["callee:00562fc8:8"]]
+ 00562e84 ["INT_ADD", "register:40f0:8", ["const:562e84:8", "const:4:8"]]
+ 00562e84 ["CALL", null, ["callee:00562fc8:8"]]
- 00562e44 bytes 51000094
+ 00562e84 bytes 51000094
- 00562ed8 ["INT_ADD", "register:40f0:8", ["const:562ed8:8", "const:4:8"]]
- 00562ed8 ["CALL", null, ["callee:00562cf0:8"]]
+ 00562f18 ["INT_ADD", "register:40f0:8", ["const:562f18:8", "const:4:8"]]
+ 00562f18 ["CALL", null, ["callee:00562cf0:8"]]
- 00562ed8 bytes 76ffff97
+ 00562f18 bytes 76ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0da60665e987c80cd137e06622c8570"></a>

### [`00562f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md) → [`00562fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562fc8.md) FUN_00562fc8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md)
- 新版 呼出元 2件 [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md#insn-00562fac) · [`00562fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md#insn-00562fd4) · [`00563008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md#insn-00563008)
- 新版 `00562fec`（命令位置の公開資料なし） · `00563014`（命令位置の公開資料なし） · `00563048`（命令位置の公開資料なし）

~~~diff
- 00562fac ["INT_ADD", "register:40f0:8", ["const:562fac:8", "const:4:8"]]
- 00562fac ["CALL", null, ["callee:00597608:8"]]
+ 00562fec ["INT_ADD", "register:40f0:8", ["const:562fec:8", "const:4:8"]]
+ 00562fec ["CALL", null, ["callee:00597608:8"]]
- 00562fac bytes 87d10094
+ 00562fec bytes 87d10094
- 00562fd4 ["INT_ADD", "register:40f0:8", ["const:562fd4:8", "const:4:8"]]
- 00562fd4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00563014 ["INT_ADD", "register:40f0:8", ["const:563014:8", "const:4:8"]]
+ 00563014 ["CALL", null, ["callee:0043bb20:8"]]
- 00562fd4 bytes c362fb97
+ 00563014 bytes c362fb97
- 00563008 ["INT_ADD", "register:40f0:8", ["const:563008:8", "const:4:8"]]
- 00563008 ["CALL", null, ["callee:0043bb20:8"]]
+ 00563048 ["INT_ADD", "register:40f0:8", ["const:563048:8", "const:4:8"]]
+ 00563048 ["CALL", null, ["callee:0043bb20:8"]]
- 00563008 bytes b662fb97
+ 00563048 bytes b662fb97
~~~


<a id="compare-bb0c4bd8a30cbdd3caf198d3ea143eb1"></a>

### [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) → [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) FUN_00563098

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00562c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md) [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`005632a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00562cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md) [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`005632e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md#insn-00563124) · [`00563158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md#insn-00563158) · [`005631ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md#insn-005631ec)
- 新版 `00563164`（命令位置の公開資料なし） · `00563198`（命令位置の公開資料なし） · `0056322c`（命令位置の公開資料なし）

~~~diff
- 00563124 ["INT_ADD", "register:40f0:8", ["const:563124:8", "const:4:8"]]
- 00563124 ["CALL", null, ["callee:00c57e90:8"]]
+ 00563164 ["INT_ADD", "register:40f0:8", ["const:563164:8", "const:4:8"]]
+ 00563164 ["CALL", null, ["callee:00c57e90:8"]]
- 00563124 bytes 5bd21b94
+ 00563164 bytes 4bd31b94
- 00563158 ["INT_ADD", "register:40f0:8", ["const:563158:8", "const:4:8"]]
- 00563158 ["CALL", null, ["callee:005632e0:8"]]
+ 00563198 ["INT_ADD", "register:40f0:8", ["const:563198:8", "const:4:8"]]
+ 00563198 ["CALL", null, ["callee:005632e0:8"]]
- 00563158 bytes 52000094
+ 00563198 bytes 52000094
- 005631ec ["INT_ADD", "register:40f0:8", ["const:5631ec:8", "const:4:8"]]
- 005631ec ["CALL", null, ["callee:00562cf0:8"]]
+ 0056322c ["INT_ADD", "register:40f0:8", ["const:56322c:8", "const:4:8"]]
+ 0056322c ["CALL", null, ["callee:00562cf0:8"]]
- 005631ec bytes b1feff97
+ 0056322c bytes b1feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d69b24eb7f58ed168da3401843d4daec"></a>

### [`005632a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md) → [`005632e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005632e0.md) FUN_005632e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 2件 [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005632d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md#insn-005632d4) · [`005632fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md#insn-005632fc) · [`00563324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md#insn-00563324)
- 新版 `00563314`（命令位置の公開資料なし） · `0056333c`（命令位置の公開資料なし） · `00563364`（命令位置の公開資料なし）

~~~diff
- 005632d4 ["INT_ADD", "register:40f0:8", ["const:5632d4:8", "const:4:8"]]
- 005632d4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00563314 ["INT_ADD", "register:40f0:8", ["const:563314:8", "const:4:8"]]
+ 00563314 ["CALL", null, ["callee:00c53cd0:8"]]
- 005632d4 bytes 77c11b94
+ 00563314 bytes 6fc21b94
- 005632fc ["INT_ADD", "register:40f0:8", ["const:5632fc:8", "const:4:8"]]
- 005632fc ["CALL", null, ["callee:0043bb20:8"]]
+ 0056333c ["INT_ADD", "register:40f0:8", ["const:56333c:8", "const:4:8"]]
+ 0056333c ["CALL", null, ["callee:0043bb20:8"]]
- 005632fc bytes f961fb97
+ 0056333c bytes f961fb97
- 00563324 ["INT_ADD", "register:40f0:8", ["const:563324:8", "const:4:8"]]
- 00563324 ["CALL", null, ["callee:0043bb20:8"]]
+ 00563364 ["INT_ADD", "register:40f0:8", ["const:563364:8", "const:4:8"]]
+ 00563364 ["CALL", null, ["callee:0043bb20:8"]]
- 00563324 bytes ef61fb97
+ 00563364 bytes ef61fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46e368c3a97bf66f03b25f423607dfda"></a>

### [`005633e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633e4.md) → [`00563424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563424.md) FUN_00563424

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00562cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cf0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056341c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633e4.md#insn-0056341c)
- 新版 `0056345c`（命令位置の公開資料なし）

~~~diff
- 0056341c ["INT_ADD", "register:40f0:8", ["const:56341c:8", "const:4:8"]]
- 0056341c ["CALL", null, ["callee:00562cf0:8"]]
+ 0056345c ["INT_ADD", "register:40f0:8", ["const:56345c:8", "const:4:8"]]
+ 0056345c ["CALL", null, ["callee:00562cf0:8"]]
- 0056341c bytes 25feff97
+ 0056345c bytes 25feff97
~~~


<a id="compare-59962231ae4c266a2740d3fe902e5c73"></a>

### [`005636cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005636cc.md) → [`0056370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056370c.md) FUN_0056370c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005636e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005636cc.md#insn-005636e8)
- 新版 `00563728`（命令位置の公開資料なし）

~~~diff
- 005636e8 ["INT_ADD", "register:40f0:8", ["const:5636e8:8", "const:4:8"]]
- 005636e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00563728 ["INT_ADD", "register:40f0:8", ["const:563728:8", "const:4:8"]]
+ 00563728 ["CALL", null, ["callee:00c57eb0:8"]]
- 005636e8 bytes f2d01b94
+ 00563728 bytes e2d11b94
~~~


<a id="compare-fce3b044908c071d74f5258fe91e0599"></a>

### [`00563710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md) → [`00563750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563750.md) FUN_00563750

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md#insn-0056372c) · [`0056373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md#insn-0056373c)
- 新版 `0056376c`（命令位置の公開資料なし） · `0056377c`（命令位置の公開資料なし）

~~~diff
- 0056372c ["INT_ADD", "register:40f0:8", ["const:56372c:8", "const:4:8"]]
- 0056372c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0056376c ["INT_ADD", "register:40f0:8", ["const:56376c:8", "const:4:8"]]
+ 0056376c ["CALL", null, ["callee:00c57eb0:8"]]
- 0056372c bytes e1d01b94
+ 0056376c bytes d1d11b94
- 0056373c ["INT_ADD", "register:40f0:8", ["const:56373c:8", "const:4:8"]]
- 0056373c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0056377c ["INT_ADD", "register:40f0:8", ["const:56377c:8", "const:4:8"]]
+ 0056377c ["CALL", null, ["callee:00c57eb0:8"]]
- 0056373c bytes ddd01b94
+ 0056377c bytes cdd11b94
~~~


<a id="compare-4d6d19c8f14957b3c76bb293a653a04b"></a>

### [`00563ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md) → [`00563b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md) FUN_00563b04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0056389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md#insn-00563b14) · [`00563b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md#insn-00563b40) · [`00563b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md#insn-00563b4c)
- 新版 `00563b54`（命令位置の公開資料なし） · `00563b80`（命令位置の公開資料なし） · `00563b8c`（命令位置の公開資料なし）

~~~diff
- 00563b14 ["INT_ADD", "register:40f0:8", ["const:563b14:8", "const:4:8"]]
- 00563b14 ["CALL", null, ["callee:0043bb20:8"]]
+ 00563b54 ["INT_ADD", "register:40f0:8", ["const:563b54:8", "const:4:8"]]
+ 00563b54 ["CALL", null, ["callee:0043bb20:8"]]
- 00563b14 bytes f35ffb97
+ 00563b54 bytes f35ffb97
- 00563b40 ["INT_ADD", "register:40f0:8", ["const:563b40:8", "const:4:8"]]
- 00563b40 ["CALL", null, ["callee:0043bb20:8"]]
+ 00563b80 ["INT_ADD", "register:40f0:8", ["const:563b80:8", "const:4:8"]]
+ 00563b80 ["CALL", null, ["callee:0043bb20:8"]]
- 00563b40 bytes e85ffb97
+ 00563b80 bytes e85ffb97
- 00563b4c ["INT_ADD", "register:40f0:8", ["const:563b4c:8", "const:4:8"]]
- 00563b4c ["CALL", null, ["callee:005490d4:8"]]
+ 00563b8c ["INT_ADD", "register:40f0:8", ["const:563b8c:8", "const:4:8"]]
+ 00563b8c ["CALL", null, ["callee:005490d4:8"]]
- 00563b4c bytes 5295ff97
+ 00563b8c bytes 5295ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f1836ea13a08d6aaf8fed6b7c52786"></a>

### [`00563bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md) → [`00563c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c14.md) FUN_00563c14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00547b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) [`005642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00547bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md) [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md#insn-00563be8) · [`00563c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md#insn-00563c04)
- 新版 `00563c28`（命令位置の公開資料なし） · `00563c44`（命令位置の公開資料なし）

~~~diff
- 00563be8 ["INT_ADD", "register:40f0:8", ["const:563be8:8", "const:4:8"]]
- 00563be8 ["CALL", null, ["callee:00547bb0:8"]]
+ 00563c28 ["INT_ADD", "register:40f0:8", ["const:563c28:8", "const:4:8"]]
+ 00563c28 ["CALL", null, ["callee:00547bb0:8"]]
- 00563be8 bytes e28fff97
+ 00563c28 bytes e28fff97
- 00563c04 ["INT_ADD", "register:40f0:8", ["const:563c04:8", "const:4:8"]]
- 00563c04 ["CALL", null, ["callee:005642e0:8"]]
+ 00563c44 ["INT_ADD", "register:40f0:8", ["const:563c44:8", "const:4:8"]]
+ 00563c44 ["CALL", null, ["callee:005642e0:8"]]
- 00563c04 bytes a7010094
+ 00563c44 bytes a7010094
~~~


<a id="compare-40b8a4de29470c7e7730db3f9b9cd170"></a>

### [`00563c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c20.md) → [`00563c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c60.md) FUN_00563c60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c20.md#insn-00563c38)
- 新版 `00563c78`（命令位置の公開資料なし）

~~~diff
- 00563c38 ["INT_ADD", "register:40f0:8", ["const:563c38:8", "const:4:8"]]
- 00563c38 ["CALL", null, ["callee:00493dc8:8"]]
+ 00563c78 ["INT_ADD", "register:40f0:8", ["const:563c78:8", "const:4:8"]]
+ 00563c78 ["CALL", null, ["callee:00493dc8:8"]]
- 00563c38 bytes 54c0fc97
+ 00563c78 bytes 54c0fc97
~~~


<a id="compare-1836a3a0319394aaa4d5b2b348545448"></a>

### [`00563c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md) → [`00563ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563ccc.md) FUN_00563ccc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md#insn-00563ca4) · [`00563d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md#insn-00563d04) · [`00563d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md#insn-00563d18)
- 新版 `00563ce4`（命令位置の公開資料なし） · `00563d44`（命令位置の公開資料なし） · `00563d58`（命令位置の公開資料なし）

~~~diff
- 00563ca4 ["INT_ADD", "register:40f0:8", ["const:563ca4:8", "const:4:8"]]
- 00563ca4 ["CALL", null, ["callee:00548098:8"]]
+ 00563ce4 ["INT_ADD", "register:40f0:8", ["const:563ce4:8", "const:4:8"]]
+ 00563ce4 ["CALL", null, ["callee:00548098:8"]]
- 00563ca4 bytes ed90ff97
+ 00563ce4 bytes ed90ff97
- 00563d04 ["INT_ADD", "register:40f0:8", ["const:563d04:8", "const:4:8"]]
- 00563d04 ["CALL", null, ["callee:00540d7c:8"]]
+ 00563d44 ["INT_ADD", "register:40f0:8", ["const:563d44:8", "const:4:8"]]
+ 00563d44 ["CALL", null, ["callee:00540d7c:8"]]
- 00563d04 bytes 0e74ff97
+ 00563d44 bytes 0e74ff97
- 00563d18 ["INT_ADD", "register:40f0:8", ["const:563d18:8", "const:4:8"]]
- 00563d18 ["CALL", null, ["callee:0043bb20:8"]]
+ 00563d58 ["INT_ADD", "register:40f0:8", ["const:563d58:8", "const:4:8"]]
+ 00563d58 ["CALL", null, ["callee:0043bb20:8"]]
- 00563d18 bytes 725ffb97
+ 00563d58 bytes 725ffb97
~~~


<a id="compare-02aeedc3c000ad43491ddbfd7754ec0e"></a>

### [`00563d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563d84.md) → [`00563dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563dc4.md) FUN_00563dc4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00564340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00564380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563d84.md#insn-00563d90)
- 新版 `00563dd0`（命令位置の公開資料なし）

~~~diff
- 00563d90 ["INT_ADD", "register:40f0:8", ["const:563d90:8", "const:4:8"]]
- 00563d90 ["CALL", null, ["callee:00564380:8"]]
+ 00563dd0 ["INT_ADD", "register:40f0:8", ["const:563dd0:8", "const:4:8"]]
+ 00563dd0 ["CALL", null, ["callee:00564380:8"]]
- 00563d90 bytes 6c010094
+ 00563dd0 bytes 6c010094
~~~


<a id="compare-48e8c51705b3a5ed01af9196841f9e1f"></a>

### [`00563df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md) → [`00563e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563e30.md) FUN_00563e30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00564548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00564588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md#insn-00563e98) · [`00563ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md#insn-00563ecc) · [`00563f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md#insn-00563f30)
- 新版 `00563ed8`（命令位置の公開資料なし） · `00563f0c`（命令位置の公開資料なし） · `00563f70`（命令位置の公開資料なし）

~~~diff
- 00563e98 ["INT_ADD", "register:40f0:8", ["const:563e98:8", "const:4:8"]]
- 00563e98 ["CALL", null, ["callee:0043bb20:8"]]
+ 00563ed8 ["INT_ADD", "register:40f0:8", ["const:563ed8:8", "const:4:8"]]
+ 00563ed8 ["CALL", null, ["callee:0043bb20:8"]]
- 00563e98 bytes 125ffb97
+ 00563ed8 bytes 125ffb97
- 00563ecc ["INT_ADD", "register:40f0:8", ["const:563ecc:8", "const:4:8"]]
- 00563ecc ["CALL", null, ["callee:0043bb20:8"]]
+ 00563f0c ["INT_ADD", "register:40f0:8", ["const:563f0c:8", "const:4:8"]]
+ 00563f0c ["CALL", null, ["callee:0043bb20:8"]]
- 00563ecc bytes 055ffb97
+ 00563f0c bytes 055ffb97
- 00563f30 ["INT_ADD", "register:40f0:8", ["const:563f30:8", "const:4:8"]]
- 00563f30 ["CALL", null, ["callee:00c57e90:8"]]
+ 00563f70 ["INT_ADD", "register:40f0:8", ["const:563f70:8", "const:4:8"]]
+ 00563f70 ["CALL", null, ["callee:00c57e90:8"]]
- 00563f30 bytes d8ce1b94
+ 00563f70 bytes c8cf1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb1477c863a20c839552a121bf091260"></a>

### [`005642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md) → [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md) FUN_005642e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00563bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md) [`00584ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) [`0088f2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2b4.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`00563c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c14.md) [`00584f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`0088f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00564304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md#insn-00564304) · [`00564314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md#insn-00564314) · [`00564324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md#insn-00564324)
- 新版 `00564344`（命令位置の公開資料なし） · `00564354`（命令位置の公開資料なし） · `00564364`（命令位置の公開資料なし）

~~~diff
- 00564304 ["INT_ADD", "register:40f0:8", ["const:564304:8", "const:4:8"]]
- 00564304 ["CALL", null, ["callee:00494610:8"]]
+ 00564344 ["INT_ADD", "register:40f0:8", ["const:564344:8", "const:4:8"]]
+ 00564344 ["CALL", null, ["callee:00494610:8"]]
- 00564304 bytes b3c0fc97
+ 00564344 bytes b3c0fc97
- 00564314 ["INT_ADD", "register:40f0:8", ["const:564314:8", "const:4:8"]]
- 00564314 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00564354 ["INT_ADD", "register:40f0:8", ["const:564354:8", "const:4:8"]]
+ 00564354 ["CALL", null, ["callee:00c57eb0:8"]]
- 00564314 bytes e7cd1b94
+ 00564354 bytes d7ce1b94
- 00564324 ["INT_ADD", "register:40f0:8", ["const:564324:8", "const:4:8"]]
- 00564324 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00564364 ["INT_ADD", "register:40f0:8", ["const:564364:8", "const:4:8"]]
+ 00564364 ["CALL", null, ["callee:00c57eb0:8"]]
- 00564324 bytes e3cd1b94
+ 00564364 bytes d3ce1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10cb0750e480934c3462cfa1e7cfa40e"></a>

### [`00564340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md) → [`00564380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564380.md) FUN_00564380

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00563d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563d84.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00563dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563dc4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005643bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md#insn-005643bc) · [`005643e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md#insn-005643e4) · [`00564450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md#insn-00564450)
- 新版 `005643fc`（命令位置の公開資料なし） · `00564424`（命令位置の公開資料なし） · `00564490`（命令位置の公開資料なし）

~~~diff
- 005643bc ["INT_ADD", "register:40f0:8", ["const:5643bc:8", "const:4:8"]]
- 005643bc ["CALL", null, ["callee:00c58050:8"]]
+ 005643fc ["INT_ADD", "register:40f0:8", ["const:5643fc:8", "const:4:8"]]
+ 005643fc ["CALL", null, ["callee:00c58050:8"]]
- 005643bc bytes 25ce1b94
+ 005643fc bytes 15cf1b94
- 005643e4 ["INT_ADD", "register:40f0:8", ["const:5643e4:8", "const:4:8"]]
- 005643e4 ["CALL", null, ["callee:00c58050:8"]]
+ 00564424 ["INT_ADD", "register:40f0:8", ["const:564424:8", "const:4:8"]]
+ 00564424 ["CALL", null, ["callee:00c58050:8"]]
- 005643e4 bytes 1bce1b94
+ 00564424 bytes 0bcf1b94
- 00564450 ["INT_ADD", "register:40f0:8", ["const:564450:8", "const:4:8"]]
- 00564450 ["CALL", null, ["callee:00c58050:8"]]
+ 00564490 ["INT_ADD", "register:40f0:8", ["const:564490:8", "const:4:8"]]
+ 00564490 ["CALL", null, ["callee:00c58050:8"]]
- 00564450 bytes 00ce1b94
+ 00564490 bytes f0ce1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25b2766651fc548db1b132d4dc8c7df7"></a>

### [`00564994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md) → [`005649d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005649d4.md) FUN_005649d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005649d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md#insn-005649d0) · [`005649f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md#insn-005649f4) · [`00564a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md#insn-00564a40)
- 新版 `00564a10`（命令位置の公開資料なし） · `00564a34`（命令位置の公開資料なし） · `00564a80`（命令位置の公開資料なし）

~~~diff
- 005649d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005649d0 ["INT_ADD", "register:40f0:8", ["const:5649d0:8", "const:4:8"]]
- 005649d0 ["CALLIND", null, ["register:0:8"]]
+ 00564a10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00564a10 ["INT_ADD", "register:40f0:8", ["const:564a10:8", "const:4:8"]]
+ 00564a10 ["CALLIND", null, ["register:0:8"]]
- 005649d0 bytes 20013fd6
+ 00564a10 bytes 20013fd6
- 005649f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005649f4 ["INT_ADD", "register:40f0:8", ["const:5649f4:8", "const:4:8"]]
- 005649f4 ["CALLIND", null, ["register:0:8"]]
+ 00564a34 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00564a34 ["INT_ADD", "register:40f0:8", ["const:564a34:8", "const:4:8"]]
+ 00564a34 ["CALLIND", null, ["register:0:8"]]
- 005649f4 bytes 20013fd6
+ 00564a34 bytes 20013fd6
- 00564a40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00564a40 ["INT_ADD", "register:40f0:8", ["const:564a40:8", "const:4:8"]]
- 00564a40 ["CALLIND", null, ["register:0:8"]]
+ 00564a80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00564a80 ["INT_ADD", "register:40f0:8", ["const:564a80:8", "const:4:8"]]
+ 00564a80 ["CALLIND", null, ["register:0:8"]]
- 00564a40 bytes 00013fd6
+ 00564a80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70f5fcd4a23fd2c1831b04fd9954a8af"></a>

### [`00565104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md) → [`00565144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565144.md) FUN_00565144

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md#insn-00565140) · [`00565190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md#insn-00565190) · [`00565200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md#insn-00565200)
- 新版 `00565180`（命令位置の公開資料なし） · `005651d0`（命令位置の公開資料なし） · `00565240`（命令位置の公開資料なし）

~~~diff
- 00565140 ["COPY", "register:0:8", ["register:4048:8"]]
- 00565140 ["INT_ADD", "register:40f0:8", ["const:565140:8", "const:4:8"]]
- 00565140 ["CALLIND", null, ["register:0:8"]]
+ 00565180 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00565180 ["INT_ADD", "register:40f0:8", ["const:565180:8", "const:4:8"]]
+ 00565180 ["CALLIND", null, ["register:0:8"]]
- 00565140 bytes 20013fd6
+ 00565180 bytes 20013fd6
- 00565190 ["COPY", "register:0:8", ["register:4048:8"]]
- 00565190 ["INT_ADD", "register:40f0:8", ["const:565190:8", "const:4:8"]]
- 00565190 ["CALLIND", null, ["register:0:8"]]
+ 005651d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005651d0 ["INT_ADD", "register:40f0:8", ["const:5651d0:8", "const:4:8"]]
+ 005651d0 ["CALLIND", null, ["register:0:8"]]
- 00565190 bytes 20013fd6
+ 005651d0 bytes 20013fd6
- 00565200 ["INT_ADD", "register:40f0:8", ["const:565200:8", "const:4:8"]]
- 00565200 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00565240 ["INT_ADD", "register:40f0:8", ["const:565240:8", "const:4:8"]]
+ 00565240 ["CALL", null, ["callee:00c57eb0:8"]]
- 00565200 bytes 2cca1b94
+ 00565240 bytes 1ccb1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cb3a223526f254868d2c1439bb3d1a3"></a>

### [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) → [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) FUN_00565584

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`0056b75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md)
- 新版 呼出元 4件 [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) [`0056b79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md) [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md#insn-00565568) · [`0056559c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md#insn-0056559c) · [`005655b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md#insn-005655b4)
- 新版 `005655a8`（命令位置の公開資料なし） · `005655dc`（命令位置の公開資料なし） · `005655f4`（命令位置の公開資料なし）

~~~diff
- 00565568 ["INT_ADD", "register:40f0:8", ["const:565568:8", "const:4:8"]]
- 00565568 ["CALL", null, ["callee:00c58660:8"]]
+ 005655a8 ["INT_ADD", "register:40f0:8", ["const:5655a8:8", "const:4:8"]]
+ 005655a8 ["CALL", null, ["callee:00c58660:8"]]
- 00565568 bytes 3ecb1b94
+ 005655a8 bytes 2ecc1b94
- 0056559c ["INT_ADD", "register:40f0:8", ["const:56559c:8", "const:4:8"]]
- 0056559c ["CALL", null, ["callee:00c58660:8"]]
+ 005655dc ["INT_ADD", "register:40f0:8", ["const:5655dc:8", "const:4:8"]]
+ 005655dc ["CALL", null, ["callee:00c58660:8"]]
- 0056559c bytes 31cb1b94
+ 005655dc bytes 21cc1b94
- 005655b4 ["INT_ADD", "register:40f0:8", ["const:5655b4:8", "const:4:8"]]
- 005655b4 ["CALL", null, ["callee:00c58660:8"]]
+ 005655f4 ["INT_ADD", "register:40f0:8", ["const:5655f4:8", "const:4:8"]]
+ 005655f4 ["CALL", null, ["callee:00c58660:8"]]
- 005655b4 bytes 2bcb1b94
+ 005655f4 bytes 1bcc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60faff7788d6123cd4c3e54abbb769a4"></a>

### [`005688e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/005688e8.md) → [`00568928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/00568928.md) FUN_00568928

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`00569aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569aac.md) · 呼出先 1件 [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md)
- 新版 呼出元 2件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`00569aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569aec.md) · 呼出先 1件 [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00568924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/005688e8.md#insn-00568924)
- 新版 `00568964`（命令位置の公開資料なし）

~~~diff
- 00568924 ["INT_ADD", "register:40f0:8", ["const:568924:8", "const:4:8"]]
- 00568924 ["CALL", null, ["callee:00c5a050:8"]]
+ 00568964 ["INT_ADD", "register:40f0:8", ["const:568964:8", "const:4:8"]]
+ 00568964 ["CALL", null, ["callee:00c5a050:8"]]
- 00568924 bytes cbc41b94
+ 00568964 bytes bbc51b94
~~~


<a id="compare-8a47644c5422edc6aef4f1b1b52ac64c"></a>

### [`0056927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md) → [`005692bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005692bc.md) FUN_005692bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) · 呼出先 3件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) · 呼出先 3件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005692ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md#insn-005692ac) · [`005692c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md#insn-005692c4) · [`005692f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md#insn-005692f0)
- 新版 `005692ec`（命令位置の公開資料なし） · `00569304`（命令位置の公開資料なし） · `00569330`（命令位置の公開資料なし）

~~~diff
- 005692ac ["INT_ADD", "register:40f0:8", ["const:5692ac:8", "const:4:8"]]
- 005692ac ["CALL", null, ["callee:00565a58:8"]]
+ 005692ec ["INT_ADD", "register:40f0:8", ["const:5692ec:8", "const:4:8"]]
+ 005692ec ["CALL", null, ["callee:00565a58:8"]]
- 005692ac bytes dbf1ff97
+ 005692ec bytes dbf1ff97
- 005692c4 ["INT_ADD", "register:40f0:8", ["const:5692c4:8", "const:4:8"]]
- 005692c4 ["CALL", null, ["callee:00566918:8"]]
+ 00569304 ["INT_ADD", "register:40f0:8", ["const:569304:8", "const:4:8"]]
+ 00569304 ["CALL", null, ["callee:00566918:8"]]
- 005692c4 bytes 85f5ff97
+ 00569304 bytes 85f5ff97
- 005692f0 ["INT_ADD", "register:40f0:8", ["const:5692f0:8", "const:4:8"]]
- 005692f0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00569330 ["INT_ADD", "register:40f0:8", ["const:569330:8", "const:4:8"]]
+ 00569330 ["CALL", null, ["callee:00c57ee0:8"]]
- 005692f0 bytes fcb91b94
+ 00569330 bytes ecba1b94
~~~


<a id="compare-667022c78cb440b8ed03499beb86593f"></a>

### [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) → [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) FUN_00569334

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) · 呼出先 4件 [`0056d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d230.md) [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)
- 新版 呼出元 2件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) · 呼出先 4件 [`0056d270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d270.md) [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00569320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md#insn-00569320) · [`005693b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md#insn-005693b4) · [`005693f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md#insn-005693f0)
- 新版 `00569360`（命令位置の公開資料なし） · `005693f4`（命令位置の公開資料なし） · `00569430`（命令位置の公開資料なし）

~~~diff
- 00569320 ["INT_ADD", "register:40f0:8", ["const:569320:8", "const:4:8"]]
- 00569320 ["CALL", null, ["callee:0056d2e0:8"]]
+ 00569360 ["INT_ADD", "register:40f0:8", ["const:569360:8", "const:4:8"]]
+ 00569360 ["CALL", null, ["callee:0056d2e0:8"]]
- 00569320 bytes e00f0094
+ 00569360 bytes e00f0094
- 005693b4 ["INT_ADD", "register:40f0:8", ["const:5693b4:8", "const:4:8"]]
- 005693b4 ["CALL", null, ["callee:00c5a070:8"]]
+ 005693f4 ["INT_ADD", "register:40f0:8", ["const:5693f4:8", "const:4:8"]]
+ 005693f4 ["CALL", null, ["callee:00c5a070:8"]]
- 005693b4 bytes 2fc21b94
+ 005693f4 bytes 1fc31b94
- 005693f0 ["INT_ADD", "register:40f0:8", ["const:5693f0:8", "const:4:8"]]
- 005693f0 ["CALL", null, ["callee:00c5a070:8"]]
+ 00569430 ["INT_ADD", "register:40f0:8", ["const:569430:8", "const:4:8"]]
+ 00569430 ["CALL", null, ["callee:00c5a070:8"]]
- 005693f0 bytes 20c21b94
+ 00569430 bytes 10c31b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5848407bb810e58af8429ec342e1cbfa"></a>

### [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) → [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) FUN_005694e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) · 呼出先 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)
- 新版 呼出元 3件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) [`0056c23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md) · 呼出先 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md#insn-0056952c) · [`00569548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md#insn-00569548) · [`00569580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md#insn-00569580)
- 新版 `0056956c`（命令位置の公開資料なし） · `00569588`（命令位置の公開資料なし） · `005695c0`（命令位置の公開資料なし）

~~~diff
- 0056952c ["INT_ADD", "register:40f0:8", ["const:56952c:8", "const:4:8"]]
- 0056952c ["CALL", null, ["callee:00c5a060:8"]]
+ 0056956c ["INT_ADD", "register:40f0:8", ["const:56956c:8", "const:4:8"]]
+ 0056956c ["CALL", null, ["callee:00c5a060:8"]]
- 0056952c bytes cdc11b94
+ 0056956c bytes bdc21b94
- 00569548 ["INT_ADD", "register:40f0:8", ["const:569548:8", "const:4:8"]]
- 00569548 ["CALL", null, ["callee:00c5a060:8"]]
+ 00569588 ["INT_ADD", "register:40f0:8", ["const:569588:8", "const:4:8"]]
+ 00569588 ["CALL", null, ["callee:00c5a060:8"]]
- 00569548 bytes c6c11b94
+ 00569588 bytes b6c21b94
- 00569580 ["INT_ADD", "register:40f0:8", ["const:569580:8", "const:4:8"]]
- 00569580 ["CALL", null, ["callee:00565a58:8"]]
+ 005695c0 ["INT_ADD", "register:40f0:8", ["const:5695c0:8", "const:4:8"]]
+ 005695c0 ["CALL", null, ["callee:00565a58:8"]]
- 00569580 bytes 26f1ff97
+ 005695c0 bytes 26f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d27994d5ad26d859bc63c327f9e4d59"></a>

### [`005695c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005695c8.md) → [`00569608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569608.md) FUN_00569608

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`00569aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569aac.md) · 呼出先 1件 [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)
- 新版 呼出元 2件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`00569aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569aec.md) · 呼出先 1件 [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00569640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005695c8.md#insn-00569640)
- 新版 `00569680`（命令位置の公開資料なし）

~~~diff
- 00569640 ["INT_ADD", "register:40f0:8", ["const:569640:8", "const:4:8"]]
- 00569640 ["CALL", null, ["callee:00c5a060:8"]]
+ 00569680 ["INT_ADD", "register:40f0:8", ["const:569680:8", "const:4:8"]]
+ 00569680 ["CALL", null, ["callee:00c5a060:8"]]
- 00569640 bytes 88c11b94
+ 00569680 bytes 78c21b94
~~~


<a id="compare-d97dbc6e92f3b7385bde1e1ce3f06578"></a>

### [`00569678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md) → [`005696b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md) FUN_005696b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) · 呼出先 6件 [`00569aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569aac.md) [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)
- 新版 呼出元 2件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) · 呼出先 6件 [`00569aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569aec.md) [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005696d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md#insn-005696d8) · [`00569764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md#insn-00569764) · [`00569780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md#insn-00569780)
- 新版 `00569718`（命令位置の公開資料なし） · `005697a4`（命令位置の公開資料なし） · `005697c0`（命令位置の公開資料なし）

~~~diff
- 005696d8 ["INT_ADD", "register:40f0:8", ["const:5696d8:8", "const:4:8"]]
- 005696d8 ["CALL", null, ["callee:00c5a050:8"]]
+ 00569718 ["INT_ADD", "register:40f0:8", ["const:569718:8", "const:4:8"]]
+ 00569718 ["CALL", null, ["callee:00c5a050:8"]]
- 005696d8 bytes 5ec11b94
+ 00569718 bytes 4ec21b94
- 00569764 ["INT_ADD", "register:40f0:8", ["const:569764:8", "const:4:8"]]
- 00569764 ["CALL", null, ["callee:00c5a060:8"]]
+ 005697a4 ["INT_ADD", "register:40f0:8", ["const:5697a4:8", "const:4:8"]]
+ 005697a4 ["CALL", null, ["callee:00c5a060:8"]]
- 00569764 bytes 3fc11b94
+ 005697a4 bytes 2fc21b94
- 00569780 ["INT_ADD", "register:40f0:8", ["const:569780:8", "const:4:8"]]
- 00569780 ["CALL", null, ["callee:00c5a060:8"]]
+ 005697c0 ["INT_ADD", "register:40f0:8", ["const:5697c0:8", "const:4:8"]]
+ 005697c0 ["CALL", null, ["callee:00c5a060:8"]]
- 00569780 bytes 38c11b94
+ 005697c0 bytes 28c21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0740ed6a753c8dee3a4cfde7b66393e"></a>

### [`00569f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md) → [`00569f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569f74.md) FUN_00569f74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 2件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c80.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 2件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00569f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md#insn-00569f88) · [`00569fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md#insn-00569fac)
- 新版 `00569fc8`（命令位置の公開資料なし） · `00569fec`（命令位置の公開資料なし）

~~~diff
- 00569f88 ["INT_ADD", "register:40f0:8", ["const:569f88:8", "const:4:8"]]
- 00569f88 ["CALL", null, ["callee:00c5a080:8"]]
+ 00569fc8 ["INT_ADD", "register:40f0:8", ["const:569fc8:8", "const:4:8"]]
+ 00569fc8 ["CALL", null, ["callee:00c5a080:8"]]
- 00569f88 bytes 3ebf1b94
+ 00569fc8 bytes 2ec01b94
- 00569fac ["INT_ADD", "register:40f0:8", ["const:569fac:8", "const:4:8"]]
- 00569fac ["CALL", null, ["callee:00c58000:8"]]
+ 00569fec ["INT_ADD", "register:40f0:8", ["const:569fec:8", "const:4:8"]]
+ 00569fec ["CALL", null, ["callee:00c58000:8"]]
- 00569fac bytes 15b71b94
+ 00569fec bytes 05b81b94
~~~


<a id="compare-dea6a048f248a0a7f28ae8a1f2202006"></a>

### [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) → [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) FUN_0056a010

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`00569678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md) [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) · 呼出先 1件 [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)
- 新版 呼出元 3件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`005696b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md) [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) · 呼出先 1件 [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md#insn-0056a010) · [`0056a02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md#insn-0056a02c) · [`0056a0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md#insn-0056a0c0)
- 新版 `0056a050`（命令位置の公開資料なし） · `0056a06c`（命令位置の公開資料なし） · `0056a100`（命令位置の公開資料なし）

~~~diff
- 0056a010 ["INT_ADD", "register:40f0:8", ["const:56a010:8", "const:4:8"]]
- 0056a010 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056a050 ["INT_ADD", "register:40f0:8", ["const:56a050:8", "const:4:8"]]
+ 0056a050 ["CALL", null, ["callee:00c5a070:8"]]
- 0056a010 bytes 18bf1b94
+ 0056a050 bytes 08c01b94
- 0056a02c ["INT_ADD", "register:40f0:8", ["const:56a02c:8", "const:4:8"]]
- 0056a02c ["CALL", null, ["callee:00c5a070:8"]]
+ 0056a06c ["INT_ADD", "register:40f0:8", ["const:56a06c:8", "const:4:8"]]
+ 0056a06c ["CALL", null, ["callee:00c5a070:8"]]
- 0056a02c bytes 11bf1b94
+ 0056a06c bytes 01c01b94
- 0056a0c0 ["INT_ADD", "register:40f0:8", ["const:56a0c0:8", "const:4:8"]]
- 0056a0c0 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056a100 ["INT_ADD", "register:40f0:8", ["const:56a100:8", "const:4:8"]]
+ 0056a100 ["CALL", null, ["callee:00c5a070:8"]]
- 0056a0c0 bytes ecbe1b94
+ 0056a100 bytes dcbf1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-283a284bc35980589258c6796dd2bce2"></a>

### [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) → [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) FUN_0056a174

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) · 呼出先 8件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) · 呼出先 8件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056a180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md#insn-0056a180) · [`0056a1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md#insn-0056a1d0) · [`0056a21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md#insn-0056a21c)
- 新版 `0056a1c0`（命令位置の公開資料なし） · `0056a210`（命令位置の公開資料なし） · `0056a25c`（命令位置の公開資料なし）

~~~diff
- 0056a180 ["INT_ADD", "register:40f0:8", ["const:56a180:8", "const:4:8"]]
- 0056a180 ["CALL", null, ["callee:00c58090:8"]]
+ 0056a1c0 ["INT_ADD", "register:40f0:8", ["const:56a1c0:8", "const:4:8"]]
+ 0056a1c0 ["CALL", null, ["callee:00c58090:8"]]
- 0056a180 bytes c4b61b94
+ 0056a1c0 bytes b4b71b94
- 0056a1d0 ["INT_ADD", "register:40f0:8", ["const:56a1d0:8", "const:4:8"]]
- 0056a1d0 ["CALL", null, ["callee:00566c00:8"]]
+ 0056a210 ["INT_ADD", "register:40f0:8", ["const:56a210:8", "const:4:8"]]
+ 0056a210 ["CALL", null, ["callee:00566c00:8"]]
- 0056a1d0 bytes 7cf2ff97
+ 0056a210 bytes 7cf2ff97
- 0056a21c ["INT_ADD", "register:40f0:8", ["const:56a21c:8", "const:4:8"]]
- 0056a21c ["CALL", null, ["callee:00565584:8"]]
+ 0056a25c ["INT_ADD", "register:40f0:8", ["const:56a25c:8", "const:4:8"]]
+ 0056a25c ["CALL", null, ["callee:00565584:8"]]
- 0056a21c bytes caecff97
+ 0056a25c bytes caecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9aab4a2b9a02da1a533f8ae6cb3e323"></a>

### [`0056a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md) → [`0056a914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md) FUN_0056a914

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) · 呼出先 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`0056a2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a2c8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) · 呼出先 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566918.md) [`0056a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a308.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056a978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md#insn-0056a978) · [`0056a9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md#insn-0056a9ac) · [`0056a9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md#insn-0056a9c4)
- 新版 `0056a9b8`（命令位置の公開資料なし） · `0056a9ec`（命令位置の公開資料なし） · `0056aa04`（命令位置の公開資料なし）

~~~diff
- 0056a978 ["INT_ADD", "register:40f0:8", ["const:56a978:8", "const:4:8"]]
- 0056a978 ["CALL", null, ["callee:0056a308:8"]]
+ 0056a9b8 ["INT_ADD", "register:40f0:8", ["const:56a9b8:8", "const:4:8"]]
+ 0056a9b8 ["CALL", null, ["callee:0056a308:8"]]
- 0056a978 bytes 54feff97
+ 0056a9b8 bytes 54feff97
- 0056a9ac ["INT_ADD", "register:40f0:8", ["const:56a9ac:8", "const:4:8"]]
- 0056a9ac ["CALL", null, ["callee:00565a58:8"]]
+ 0056a9ec ["INT_ADD", "register:40f0:8", ["const:56a9ec:8", "const:4:8"]]
+ 0056a9ec ["CALL", null, ["callee:00565a58:8"]]
- 0056a9ac bytes 1becff97
+ 0056a9ec bytes 1becff97
- 0056a9c4 ["INT_ADD", "register:40f0:8", ["const:56a9c4:8", "const:4:8"]]
- 0056a9c4 ["CALL", null, ["callee:00566918:8"]]
+ 0056aa04 ["INT_ADD", "register:40f0:8", ["const:56aa04:8", "const:4:8"]]
+ 0056aa04 ["CALL", null, ["callee:00566918:8"]]
- 0056a9c4 bytes c5efff97
+ 0056aa04 bytes c5efff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4db46c8aed825b6587c7770eb399f4ed"></a>

### [`0056aa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md) → [`0056aad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056aad0.md) FUN_0056aad0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00571244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571244.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00571284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056aadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md#insn-0056aadc) · [`0056aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md#insn-0056aaf0) · [`0056aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md#insn-0056aaf8)
- 新版 `0056ab1c`（命令位置の公開資料なし） · `0056ab30`（命令位置の公開資料なし） · `0056ab38`（命令位置の公開資料なし）

~~~diff
- 0056aadc ["INT_ADD", "register:40f0:8", ["const:56aadc:8", "const:4:8"]]
- 0056aadc ["CALL", null, ["callee:00c53d00:8"]]
+ 0056ab1c ["INT_ADD", "register:40f0:8", ["const:56ab1c:8", "const:4:8"]]
+ 0056ab1c ["CALL", null, ["callee:00c53d00:8"]]
- 0056aadc bytes 81a31b94
+ 0056ab1c bytes 79a41b94
- 0056aaf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056aaf0 ["INT_ADD", "register:40f0:8", ["const:56aaf0:8", "const:4:8"]]
- 0056aaf0 ["CALLIND", null, ["register:0:8"]]
+ 0056ab30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056ab30 ["INT_ADD", "register:40f0:8", ["const:56ab30:8", "const:4:8"]]
+ 0056ab30 ["CALLIND", null, ["register:0:8"]]
- 0056aaf0 bytes 00013fd6
+ 0056ab30 bytes 00013fd6
- 0056aaf8 ["INT_ADD", "register:40f0:8", ["const:56aaf8:8", "const:4:8"]]
- 0056aaf8 ["CALL", null, ["callee:00c57e80:8"]]
+ 0056ab38 ["INT_ADD", "register:40f0:8", ["const:56ab38:8", "const:4:8"]]
+ 0056ab38 ["CALL", null, ["callee:00c57e80:8"]]
- 0056aaf8 bytes e2b31b94
+ 0056ab38 bytes d2b41b94
~~~


<a id="compare-5fdf270c778d63b7afbce2e667590f9d"></a>

### [`0056af2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md) → [`0056af6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056af6c.md) FUN_0056af6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056af64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md#insn-0056af64) · [`0056af78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md#insn-0056af78) · [`0056af80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md#insn-0056af80)
- 新版 `0056afa4`（命令位置の公開資料なし） · `0056afb8`（命令位置の公開資料なし） · `0056afc0`（命令位置の公開資料なし）

~~~diff
- 0056af64 ["INT_ADD", "register:40f0:8", ["const:56af64:8", "const:4:8"]]
- 0056af64 ["CALL", null, ["callee:00c53d00:8"]]
+ 0056afa4 ["INT_ADD", "register:40f0:8", ["const:56afa4:8", "const:4:8"]]
+ 0056afa4 ["CALL", null, ["callee:00c53d00:8"]]
- 0056af64 bytes 5fa21b94
+ 0056afa4 bytes 57a31b94
- 0056af78 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056af78 ["INT_ADD", "register:40f0:8", ["const:56af78:8", "const:4:8"]]
- 0056af78 ["CALLIND", null, ["register:0:8"]]
+ 0056afb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056afb8 ["INT_ADD", "register:40f0:8", ["const:56afb8:8", "const:4:8"]]
+ 0056afb8 ["CALLIND", null, ["register:0:8"]]
- 0056af78 bytes 00013fd6
+ 0056afb8 bytes 00013fd6
- 0056af80 ["INT_ADD", "register:40f0:8", ["const:56af80:8", "const:4:8"]]
- 0056af80 ["CALL", null, ["callee:00c57e80:8"]]
+ 0056afc0 ["INT_ADD", "register:40f0:8", ["const:56afc0:8", "const:4:8"]]
+ 0056afc0 ["CALL", null, ["callee:00c57e80:8"]]
- 0056af80 bytes c0b21b94
+ 0056afc0 bytes b0b31b94
~~~


<a id="compare-336285e913d181eaa514207f8b8646e9"></a>

### [`0056af9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md) → [`0056afdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056afdc.md) FUN_0056afdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056afb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md#insn-0056afb8) · [`0056afd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md#insn-0056afd8)
- 新版 `0056aff8`（命令位置の公開資料なし） · `0056b018`（命令位置の公開資料なし）

~~~diff
- 0056afb8 ["INT_ADD", "register:40f0:8", ["const:56afb8:8", "const:4:8"]]
- 0056afb8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0056aff8 ["INT_ADD", "register:40f0:8", ["const:56aff8:8", "const:4:8"]]
+ 0056aff8 ["CALL", null, ["callee:00c53d00:8"]]
- 0056afb8 bytes 4aa21b94
+ 0056aff8 bytes 42a31b94
- 0056afd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056afd8 ["INT_ADD", "register:40f0:8", ["const:56afd8:8", "const:4:8"]]
- 0056afd8 ["CALLIND", null, ["register:0:8"]]
+ 0056b018 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b018 ["INT_ADD", "register:40f0:8", ["const:56b018:8", "const:4:8"]]
+ 0056b018 ["CALLIND", null, ["register:0:8"]]
- 0056afd8 bytes 00013fd6
+ 0056b018 bytes 00013fd6
~~~


<a id="compare-4971b29d4ab3703acafc230b4088ca29"></a>

### [`0056b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b640.md) → [`0056b680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b680.md) FUN_0056b680

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056b65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b640.md#insn-0056b65c) · [`0056b67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b640.md#insn-0056b67c)
- 新版 `0056b69c`（命令位置の公開資料なし） · `0056b6bc`（命令位置の公開資料なし）

~~~diff
- 0056b65c ["INT_ADD", "register:40f0:8", ["const:56b65c:8", "const:4:8"]]
- 0056b65c ["CALL", null, ["callee:00c53d00:8"]]
+ 0056b69c ["INT_ADD", "register:40f0:8", ["const:56b69c:8", "const:4:8"]]
+ 0056b69c ["CALL", null, ["callee:00c53d00:8"]]
- 0056b65c bytes a1a01b94
+ 0056b69c bytes 99a11b94
- 0056b67c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b67c ["INT_ADD", "register:40f0:8", ["const:56b67c:8", "const:4:8"]]
- 0056b67c ["CALLIND", null, ["register:0:8"]]
+ 0056b6bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b6bc ["INT_ADD", "register:40f0:8", ["const:56b6bc:8", "const:4:8"]]
+ 0056b6bc ["CALLIND", null, ["register:0:8"]]
- 0056b67c bytes 00013fd6
+ 0056b6bc bytes 00013fd6
~~~


<a id="compare-2c18502541d5fffa139f5635dbf70395"></a>

### [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) → [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) FUN_0056b6d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00571034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md) [`00571174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md) · 呼出先 4件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)
- 新版 呼出元 2件 [`00571074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md) [`005711b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md) · 呼出先 4件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056b6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md#insn-0056b6bc) · [`0056b6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md#insn-0056b6d0) · [`0056b6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md#insn-0056b6e0)
- 新版 `0056b6fc`（命令位置の公開資料なし） · `0056b710`（命令位置の公開資料なし） · `0056b720`（命令位置の公開資料なし）

~~~diff
- 0056b6bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b6bc ["INT_ADD", "register:40f0:8", ["const:56b6bc:8", "const:4:8"]]
- 0056b6bc ["CALLIND", null, ["register:0:8"]]
+ 0056b6fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b6fc ["INT_ADD", "register:40f0:8", ["const:56b6fc:8", "const:4:8"]]
+ 0056b6fc ["CALLIND", null, ["register:0:8"]]
- 0056b6bc bytes 00013fd6
+ 0056b6fc bytes 00013fd6
- 0056b6d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b6d0 ["INT_ADD", "register:40f0:8", ["const:56b6d0:8", "const:4:8"]]
- 0056b6d0 ["CALLIND", null, ["register:0:8"]]
+ 0056b710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b710 ["INT_ADD", "register:40f0:8", ["const:56b710:8", "const:4:8"]]
+ 0056b710 ["CALLIND", null, ["register:0:8"]]
- 0056b6d0 bytes 00013fd6
+ 0056b710 bytes 00013fd6
- 0056b6e0 ["INT_ADD", "register:40f0:8", ["const:56b6e0:8", "const:4:8"]]
- 0056b6e0 ["CALL", null, ["callee:00c5a0e0:8"]]
+ 0056b720 ["INT_ADD", "register:40f0:8", ["const:56b720:8", "const:4:8"]]
+ 0056b720 ["CALL", null, ["callee:00c5a0e0:8"]]
- 0056b6e0 bytes 80b91b94
+ 0056b720 bytes 70ba1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4a77cb1f91ee1a5bab2f566a751069"></a>

### [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) → [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) FUN_0056b90c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0056b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b5d4.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) · 呼出先 5件 [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) [`0056a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md) [`00c53850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53850.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)
- 新版 呼出元 3件 [`0056b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b614.md) [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) [`0056c23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md) · 呼出先 5件 [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) [`0056a914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md) [`00c53c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53c70.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md#insn-0056b8e4) · [`0056b918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md#insn-0056b918) · [`0056b92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md#insn-0056b92c)
- 新版 `0056b924`（命令位置の公開資料なし） · `0056b958`（命令位置の公開資料なし） · `0056b96c`（命令位置の公開資料なし）

~~~diff
- 0056b8e4 ["INT_ADD", "register:40f0:8", ["const:56b8e4:8", "const:4:8"]]
- 0056b8e4 ["CALL", null, ["callee:00c5a0e0:8"]]
+ 0056b924 ["INT_ADD", "register:40f0:8", ["const:56b924:8", "const:4:8"]]
+ 0056b924 ["CALL", null, ["callee:00c5a0e0:8"]]
- 0056b8e4 bytes ffb81b94
+ 0056b924 bytes efb91b94
- 0056b918 ["INT_ADD", "register:40f0:8", ["const:56b918:8", "const:4:8"]]
- 0056b918 ["CALL", null, ["callee:0056a914:8"]]
+ 0056b958 ["INT_ADD", "register:40f0:8", ["const:56b958:8", "const:4:8"]]
+ 0056b958 ["CALL", null, ["callee:0056a914:8"]]
- 0056b918 bytes effbff97
+ 0056b958 bytes effbff97
- 0056b92c ["INT_ADD", "register:40f0:8", ["const:56b92c:8", "const:4:8"]]
- 0056b92c ["CALL", null, ["callee:00c53c70:8"]]
+ 0056b96c ["INT_ADD", "register:40f0:8", ["const:56b96c:8", "const:4:8"]]
+ 0056b96c ["CALL", null, ["callee:00c53c70:8"]]
- 0056b92c bytes c99f1b94
+ 0056b96c bytes c1a01b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d19a04505d34344c30b3ad7e480d0b85"></a>

### [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) → [`0056ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056ba24.md) FUN_0056ba24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c700.md) · 呼出先 12件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00569678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md) [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`0056c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c740.md) · 呼出先 12件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`005696b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005696b8.md) [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md#insn-0056ba14) · [`0056ba2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md#insn-0056ba2c) · [`0056ba3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md#insn-0056ba3c)
- 新版 `0056ba54`（命令位置の公開資料なし） · `0056ba6c`（命令位置の公開資料なし） · `0056ba7c`（命令位置の公開資料なし）

~~~diff
- 0056ba14 ["INT_ADD", "register:40f0:8", ["const:56ba14:8", "const:4:8"]]
- 0056ba14 ["CALL", null, ["callee:00c5a0e0:8"]]
+ 0056ba54 ["INT_ADD", "register:40f0:8", ["const:56ba54:8", "const:4:8"]]
+ 0056ba54 ["CALL", null, ["callee:00c5a0e0:8"]]
- 0056ba14 bytes b3b81b94
+ 0056ba54 bytes a3b91b94
- 0056ba2c ["INT_ADD", "register:40f0:8", ["const:56ba2c:8", "const:4:8"]]
- 0056ba2c ["CALL", null, ["callee:00565584:8"]]
+ 0056ba6c ["INT_ADD", "register:40f0:8", ["const:56ba6c:8", "const:4:8"]]
+ 0056ba6c ["CALL", null, ["callee:00565584:8"]]
- 0056ba2c bytes c6e6ff97
+ 0056ba6c bytes c6e6ff97
- 0056ba3c ["INT_ADD", "register:40f0:8", ["const:56ba3c:8", "const:4:8"]]
- 0056ba3c ["CALL", null, ["callee:00c58660:8"]]
+ 0056ba7c ["INT_ADD", "register:40f0:8", ["const:56ba7c:8", "const:4:8"]]
+ 0056ba7c ["CALL", null, ["callee:00c58660:8"]]
- 0056ba3c bytes 09b21b94
+ 0056ba7c bytes f9b21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27c7663dbe05c2a626309f8e429a283f"></a>

### [`0056bcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md) → [`0056bcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056bcf4.md) FUN_0056bcf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056c4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c4bc.md) · 呼出先 5件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`0056c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md) · 呼出先 5件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md#insn-0056bcec) · [`0056bd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md#insn-0056bd04) · [`0056bd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md#insn-0056bd18)
- 新版 `0056bd2c`（命令位置の公開資料なし） · `0056bd44`（命令位置の公開資料なし） · `0056bd58`（命令位置の公開資料なし）

~~~diff
- 0056bcec ["INT_ADD", "register:40f0:8", ["const:56bcec:8", "const:4:8"]]
- 0056bcec ["CALL", null, ["callee:00c53cd0:8"]]
+ 0056bd2c ["INT_ADD", "register:40f0:8", ["const:56bd2c:8", "const:4:8"]]
+ 0056bd2c ["CALL", null, ["callee:00c53cd0:8"]]
- 0056bcec bytes f19e1b94
+ 0056bd2c bytes e99f1b94
- 0056bd04 ["INT_ADD", "register:40f0:8", ["const:56bd04:8", "const:4:8"]]
- 0056bd04 ["CALL", null, ["callee:00c53d00:8"]]
+ 0056bd44 ["INT_ADD", "register:40f0:8", ["const:56bd44:8", "const:4:8"]]
+ 0056bd44 ["CALL", null, ["callee:00c53d00:8"]]
- 0056bd04 bytes f79e1b94
+ 0056bd44 bytes ef9f1b94
- 0056bd18 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056bd18 ["INT_ADD", "register:40f0:8", ["const:56bd18:8", "const:4:8"]]
- 0056bd18 ["CALLIND", null, ["register:0:8"]]
+ 0056bd58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056bd58 ["INT_ADD", "register:40f0:8", ["const:56bd58:8", "const:4:8"]]
+ 0056bd58 ["CALLIND", null, ["register:0:8"]]
- 0056bd18 bytes 00013fd6
+ 0056bd58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad04df3c228bf94099738a3f1c879b16"></a>

### [`0056bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md) → [`0056c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c000.md) FUN_0056c000

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md#insn-0056bff4) · [`0056c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md#insn-0056c018) · [`0056c03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md#insn-0056c03c)
- 新版 `0056c034`（命令位置の公開資料なし） · `0056c058`（命令位置の公開資料なし） · `0056c07c`（命令位置の公開資料なし）

~~~diff
- 0056bff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056bff4 ["INT_ADD", "register:40f0:8", ["const:56bff4:8", "const:4:8"]]
- 0056bff4 ["CALLIND", null, ["register:0:8"]]
+ 0056c034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c034 ["INT_ADD", "register:40f0:8", ["const:56c034:8", "const:4:8"]]
+ 0056c034 ["CALLIND", null, ["register:0:8"]]
- 0056bff4 bytes 00013fd6
+ 0056c034 bytes 00013fd6
- 0056c018 ["INT_ADD", "register:40f0:8", ["const:56c018:8", "const:4:8"]]
- 0056c018 ["CALL", null, ["callee:00c58420:8"]]
+ 0056c058 ["INT_ADD", "register:40f0:8", ["const:56c058:8", "const:4:8"]]
+ 0056c058 ["CALL", null, ["callee:00c58420:8"]]
- 0056c018 bytes 02b01b94
+ 0056c058 bytes f2b01b94
- 0056c03c ["INT_ADD", "register:40f0:8", ["const:56c03c:8", "const:4:8"]]
- 0056c03c ["CALL", null, ["callee:00c57ee0:8"]]
+ 0056c07c ["INT_ADD", "register:40f0:8", ["const:56c07c:8", "const:4:8"]]
+ 0056c07c ["CALL", null, ["callee:00c57ee0:8"]]
- 0056c03c bytes a9ae1b94
+ 0056c07c bytes 99af1b94
~~~


<a id="compare-eb996f19adc787a310edec99efd6e954"></a>

### [`0056c05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c05c.md) → [`0056c09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c09c.md) FUN_0056c09c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c05c.md#insn-0056c0a0) · [`0056c0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c05c.md#insn-0056c0d0)
- 新版 `0056c0e0`（命令位置の公開資料なし） · `0056c110`（命令位置の公開資料なし）

~~~diff
- 0056c0a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0056c0a0 ["INT_ADD", "register:40f0:8", ["const:56c0a0:8", "const:4:8"]]
- 0056c0a0 ["CALLIND", null, ["register:0:8"]]
+ 0056c0e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0056c0e0 ["INT_ADD", "register:40f0:8", ["const:56c0e0:8", "const:4:8"]]
+ 0056c0e0 ["CALLIND", null, ["register:0:8"]]
- 0056c0a0 bytes 20013fd6
+ 0056c0e0 bytes 20013fd6
- 0056c0d0 ["INT_ADD", "register:40f0:8", ["const:56c0d0:8", "const:4:8"]]
- 0056c0d0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0056c110 ["INT_ADD", "register:40f0:8", ["const:56c110:8", "const:4:8"]]
+ 0056c110 ["CALL", null, ["callee:00c57ee0:8"]]
- 0056c0d0 bytes 84ae1b94
+ 0056c110 bytes 74af1b94
~~~


<a id="compare-6b68b4809ac44db3036c1aeabfce7f51"></a>

### [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) → [`0056c23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c23c.md) FUN_0056c23c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056c41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c41c.md) · 呼出先 4件 [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)
- 新版 呼出元 1件 [`0056c45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c45c.md) · 呼出先 4件 [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) [`0056b90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b90c.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md#insn-0056c228) · [`0056c23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md#insn-0056c23c) · [`0056c24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md#insn-0056c24c)
- 新版 `0056c268`（命令位置の公開資料なし） · `0056c27c`（命令位置の公開資料なし） · `0056c28c`（命令位置の公開資料なし）

~~~diff
- 0056c228 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c228 ["INT_ADD", "register:40f0:8", ["const:56c228:8", "const:4:8"]]
- 0056c228 ["CALLIND", null, ["register:0:8"]]
+ 0056c268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c268 ["INT_ADD", "register:40f0:8", ["const:56c268:8", "const:4:8"]]
+ 0056c268 ["CALLIND", null, ["register:0:8"]]
- 0056c228 bytes 00013fd6
+ 0056c268 bytes 00013fd6
- 0056c23c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c23c ["INT_ADD", "register:40f0:8", ["const:56c23c:8", "const:4:8"]]
- 0056c23c ["CALLIND", null, ["register:0:8"]]
+ 0056c27c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c27c ["INT_ADD", "register:40f0:8", ["const:56c27c:8", "const:4:8"]]
+ 0056c27c ["CALLIND", null, ["register:0:8"]]
- 0056c23c bytes 00013fd6
+ 0056c27c bytes 00013fd6
- 0056c24c ["INT_ADD", "register:40f0:8", ["const:56c24c:8", "const:4:8"]]
- 0056c24c ["CALL", null, ["callee:00c5a0e0:8"]]
+ 0056c28c ["INT_ADD", "register:40f0:8", ["const:56c28c:8", "const:4:8"]]
+ 0056c28c ["CALL", null, ["callee:00c5a0e0:8"]]
- 0056c24c bytes a5b61b94
+ 0056c28c bytes 95b71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7647de446b797b6b03ec01e3cd980cb1"></a>

### [`0056c2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c2bc.md) → [`0056c2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c2fc.md) FUN_0056c2fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c2bc.md#insn-0056c2e0) · [`0056c2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c2bc.md#insn-0056c2fc)
- 新版 `0056c320`（命令位置の公開資料なし） · `0056c33c`（命令位置の公開資料なし）

~~~diff
- 0056c2e0 ["INT_ADD", "register:40f0:8", ["const:56c2e0:8", "const:4:8"]]
- 0056c2e0 ["CALL", null, ["callee:00c5a0e0:8"]]
+ 0056c320 ["INT_ADD", "register:40f0:8", ["const:56c320:8", "const:4:8"]]
+ 0056c320 ["CALL", null, ["callee:00c5a0e0:8"]]
- 0056c2e0 bytes 80b61b94
+ 0056c320 bytes 70b71b94
- 0056c2fc ["INT_ADD", "register:40f0:8", ["const:56c2fc:8", "const:4:8"]]
- 0056c2fc ["CALL", null, ["callee:0056897c:8"]]
+ 0056c33c ["INT_ADD", "register:40f0:8", ["const:56c33c:8", "const:4:8"]]
+ 0056c33c ["CALL", null, ["callee:0056897c:8"]]
- 0056c2fc bytes 90f1ff97
+ 0056c33c bytes 90f1ff97
~~~


<a id="compare-2711298e49ab3f3b34f6e92450282c15"></a>

### [`0056c39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c39c.md) → [`0056c3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c3dc.md) FUN_0056c3dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c39c.md#insn-0056c3d0)
- 新版 `0056c410`（命令位置の公開資料なし）

~~~diff
- 0056c3d0 ["INT_ADD", "register:40f0:8", ["const:56c3d0:8", "const:4:8"]]
- 0056c3d0 ["CALL", null, ["callee:00c5a100:8"]]
+ 0056c410 ["INT_ADD", "register:40f0:8", ["const:56c410:8", "const:4:8"]]
+ 0056c410 ["CALL", null, ["callee:00c5a100:8"]]
- 0056c3d0 bytes 4cb61b94
+ 0056c410 bytes 3cb71b94
~~~


<a id="compare-2f91972094cdff1396c6edb438287a08"></a>

### [`0056c428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c428.md) → [`0056c468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c468.md) FUN_0056c468

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c428.md#insn-0056c478) · [`0056c4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c428.md#insn-0056c4b8)
- 新版 `0056c4b8`（命令位置の公開資料なし） · `0056c4f8`（命令位置の公開資料なし）

~~~diff
- 0056c478 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c478 ["INT_ADD", "register:40f0:8", ["const:56c478:8", "const:4:8"]]
- 0056c478 ["CALLIND", null, ["register:0:8"]]
+ 0056c4b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c4b8 ["INT_ADD", "register:40f0:8", ["const:56c4b8:8", "const:4:8"]]
+ 0056c4b8 ["CALLIND", null, ["register:0:8"]]
- 0056c478 bytes 00013fd6
+ 0056c4b8 bytes 00013fd6
- 0056c4b8 ["INT_ADD", "register:40f0:8", ["const:56c4b8:8", "const:4:8"]]
- 0056c4b8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0056c4f8 ["INT_ADD", "register:40f0:8", ["const:56c4f8:8", "const:4:8"]]
+ 0056c4f8 ["CALL", null, ["callee:00c57ee0:8"]]
- 0056c4b8 bytes 8aad1b94
+ 0056c4f8 bytes 7aae1b94
~~~


<a id="compare-0c58a48167065b7acfd76c404d364abc"></a>

### [`0056c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6ac.md) → [`0056c6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c6ec.md) FUN_0056c6ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6ac.md#insn-0056c6c8) · [`0056c6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6ac.md#insn-0056c6e8)
- 新版 `0056c708`（命令位置の公開資料なし） · `0056c728`（命令位置の公開資料なし）

~~~diff
- 0056c6c8 ["INT_ADD", "register:40f0:8", ["const:56c6c8:8", "const:4:8"]]
- 0056c6c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0056c708 ["INT_ADD", "register:40f0:8", ["const:56c708:8", "const:4:8"]]
+ 0056c708 ["CALL", null, ["callee:00c53d00:8"]]
- 0056c6c8 bytes 869c1b94
+ 0056c708 bytes 7e9d1b94
- 0056c6e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c6e8 ["INT_ADD", "register:40f0:8", ["const:56c6e8:8", "const:4:8"]]
- 0056c6e8 ["CALLIND", null, ["register:0:8"]]
+ 0056c728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c728 ["INT_ADD", "register:40f0:8", ["const:56c728:8", "const:4:8"]]
+ 0056c728 ["CALLIND", null, ["register:0:8"]]
- 0056c6e8 bytes 00013fd6
+ 0056c728 bytes 00013fd6
~~~


<a id="compare-31c3a304412f80f023d72f13aa03a79a"></a>

### [`0056c8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c8c0.md) → [`0056c900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c900.md) FUN_0056c900

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c8c0.md#insn-0056c8dc) · [`0056c8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c8c0.md#insn-0056c8fc)
- 新版 `0056c91c`（命令位置の公開資料なし） · `0056c93c`（命令位置の公開資料なし）

~~~diff
- 0056c8dc ["INT_ADD", "register:40f0:8", ["const:56c8dc:8", "const:4:8"]]
- 0056c8dc ["CALL", null, ["callee:00c53d00:8"]]
+ 0056c91c ["INT_ADD", "register:40f0:8", ["const:56c91c:8", "const:4:8"]]
+ 0056c91c ["CALL", null, ["callee:00c53d00:8"]]
- 0056c8dc bytes 019c1b94
+ 0056c91c bytes f99c1b94
- 0056c8fc ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c8fc ["INT_ADD", "register:40f0:8", ["const:56c8fc:8", "const:4:8"]]
- 0056c8fc ["CALLIND", null, ["register:0:8"]]
+ 0056c93c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c93c ["INT_ADD", "register:40f0:8", ["const:56c93c:8", "const:4:8"]]
+ 0056c93c ["CALLIND", null, ["register:0:8"]]
- 0056c8fc bytes 00013fd6
+ 0056c93c bytes 00013fd6
~~~


<a id="compare-760def082c1ce6ca14c14e9eca048595"></a>

### [`0056c910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c910.md) → [`0056c950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c950.md) FUN_0056c950

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c910.md#insn-0056c92c) · [`0056c94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c910.md#insn-0056c94c)
- 新版 `0056c96c`（命令位置の公開資料なし） · `0056c98c`（命令位置の公開資料なし）

~~~diff
- 0056c92c ["INT_ADD", "register:40f0:8", ["const:56c92c:8", "const:4:8"]]
- 0056c92c ["CALL", null, ["callee:00c53d00:8"]]
+ 0056c96c ["INT_ADD", "register:40f0:8", ["const:56c96c:8", "const:4:8"]]
+ 0056c96c ["CALL", null, ["callee:00c53d00:8"]]
- 0056c92c bytes ed9b1b94
+ 0056c96c bytes e59c1b94
- 0056c94c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c94c ["INT_ADD", "register:40f0:8", ["const:56c94c:8", "const:4:8"]]
- 0056c94c ["CALLIND", null, ["register:0:8"]]
+ 0056c98c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c98c ["INT_ADD", "register:40f0:8", ["const:56c98c:8", "const:4:8"]]
+ 0056c98c ["CALLIND", null, ["register:0:8"]]
- 0056c94c bytes 00013fd6
+ 0056c98c bytes 00013fd6
~~~


<a id="compare-6a5d8dcd67e2fcce1b8eaa0ed6bdcaa4"></a>

### [`0056c960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md) → [`0056c9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c9a0.md) FUN_0056c9a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550944.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`0056c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c700.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00550984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550984.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`0056c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c740.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md#insn-0056c990) · [`0056c9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md#insn-0056c9a0) · [`0056c9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md#insn-0056c9b4)
- 新版 `0056c9d0`（命令位置の公開資料なし） · `0056c9e0`（命令位置の公開資料なし） · `0056c9f4`（命令位置の公開資料なし）

~~~diff
- 0056c990 ["INT_ADD", "register:40f0:8", ["const:56c990:8", "const:4:8"]]
- 0056c990 ["CALL", null, ["callee:00550ba4:8"]]
+ 0056c9d0 ["INT_ADD", "register:40f0:8", ["const:56c9d0:8", "const:4:8"]]
+ 0056c9d0 ["CALL", null, ["callee:00550ba4:8"]]
- 0056c990 bytes 7590ff97
+ 0056c9d0 bytes 7590ff97
- 0056c9a0 ["INT_ADD", "register:40f0:8", ["const:56c9a0:8", "const:4:8"]]
- 0056c9a0 ["CALL", null, ["callee:0056c740:8"]]
+ 0056c9e0 ["INT_ADD", "register:40f0:8", ["const:56c9e0:8", "const:4:8"]]
+ 0056c9e0 ["CALL", null, ["callee:0056c740:8"]]
- 0056c9a0 bytes 58ffff97
+ 0056c9e0 bytes 58ffff97
- 0056c9b4 ["INT_ADD", "register:40f0:8", ["const:56c9b4:8", "const:4:8"]]
- 0056c9b4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0056c9f4 ["INT_ADD", "register:40f0:8", ["const:56c9f4:8", "const:4:8"]]
+ 0056c9f4 ["CALL", null, ["callee:00c53d00:8"]]
- 0056c9b4 bytes cb9b1b94
+ 0056c9f4 bytes c39c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88bd8c7d5dd5d01450bf04ca05d517d9"></a>

### [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) → [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) FUN_0056ce4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) · 呼出先 2件 [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md)
- 新版 呼出元 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) · 呼出先 2件 [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md#insn-0056ce50) · [`0056ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md#insn-0056ceac) · [`0056cf20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md#insn-0056cf20)
- 新版 `0056ce90`（命令位置の公開資料なし） · `0056ceec`（命令位置の公開資料なし） · `0056cf60`（命令位置の公開資料なし）

~~~diff
- 0056ce50 ["INT_ADD", "register:40f0:8", ["const:56ce50:8", "const:4:8"]]
- 0056ce50 ["CALL", null, ["callee:0056d06c:8"]]
+ 0056ce90 ["INT_ADD", "register:40f0:8", ["const:56ce90:8", "const:4:8"]]
+ 0056ce90 ["CALL", null, ["callee:0056d06c:8"]]
- 0056ce50 bytes 77000094
+ 0056ce90 bytes 77000094
- 0056ceac ["INT_ADD", "register:40f0:8", ["const:56ceac:8", "const:4:8"]]
- 0056ceac ["CALL", null, ["callee:0056d06c:8"]]
+ 0056ceec ["INT_ADD", "register:40f0:8", ["const:56ceec:8", "const:4:8"]]
+ 0056ceec ["CALL", null, ["callee:0056d06c:8"]]
- 0056ceac bytes 60000094
+ 0056ceec bytes 60000094
- 0056cf20 ["INT_ADD", "register:40f0:8", ["const:56cf20:8", "const:4:8"]]
- 0056cf20 ["CALL", null, ["local:b0:8"]]
+ 0056cf60 ["INT_ADD", "register:40f0:8", ["const:56cf60:8", "const:4:8"]]
+ 0056cf60 ["CALL", null, ["local:b0:8"]]
- 0056cf20 bytes bbffff97
+ 0056cf60 bytes bbffff97
~~~


<a id="compare-5a31770a1fdec72b544eb5612b9f2251"></a>

### [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) → [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) FUN_0056d06c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) · 呼出先 2件 [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)
- 新版 呼出元 10件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) · 呼出先 2件 [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md#insn-0056d090) · [`0056d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md#insn-0056d130)
- 新版 `0056d0d0`（命令位置の公開資料なし） · `0056d170`（命令位置の公開資料なし）

~~~diff
- 0056d090 ["INT_ADD", "register:40f0:8", ["const:56d090:8", "const:4:8"]]
- 0056d090 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056d0d0 ["INT_ADD", "register:40f0:8", ["const:56d0d0:8", "const:4:8"]]
+ 0056d0d0 ["CALL", null, ["callee:00c5a070:8"]]
- 0056d090 bytes f8b21b94
+ 0056d0d0 bytes e8b31b94
- 0056d130 ["INT_ADD", "register:40f0:8", ["const:56d130:8", "const:4:8"]]
- 0056d130 ["CALL", null, ["callee:0056d2e0:8"]]
+ 0056d170 ["INT_ADD", "register:40f0:8", ["const:56d170:8", "const:4:8"]]
+ 0056d170 ["CALL", null, ["callee:0056d2e0:8"]]
- 0056d130 bytes 5c000094
+ 0056d170 bytes 5c000094
~~~


<a id="compare-69da5b04e44ff8e6c12c2eee01940215"></a>

### [`0056d16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d16c.md) → [`0056d1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d1ac.md) FUN_0056d1ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d16c.md#insn-0056d1f4)
- 新版 `0056d234`（命令位置の公開資料なし）

~~~diff
- 0056d1f4 ["INT_ADD", "register:40f0:8", ["const:56d1f4:8", "const:4:8"]]
- 0056d1f4 ["CALL", null, ["callee:0056d2e0:8"]]
+ 0056d234 ["INT_ADD", "register:40f0:8", ["const:56d234:8", "const:4:8"]]
+ 0056d234 ["CALL", null, ["callee:0056d2e0:8"]]
- 0056d1f4 bytes 2b000094
+ 0056d234 bytes 2b000094
~~~


