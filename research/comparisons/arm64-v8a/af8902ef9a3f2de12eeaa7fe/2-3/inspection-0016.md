# v16.0.0 → v16.0.1 · 要調査の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-5d3adcc4db99861c8ff356aef75dad50"></a>

### [`005b74e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b74e0.md) → [`005b7520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7520.md) FUN_005b7520

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b751c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b74e0.md#insn-005b751c)
- 新版 `005b755c`（命令位置の公開資料なし）

~~~diff
- 005b751c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b751c ["INT_ADD", "register:40f0:8", ["const:5b751c:8", "const:4:8"]]
- 005b751c ["CALLIND", null, ["register:0:8"]]
+ 005b755c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b755c ["INT_ADD", "register:40f0:8", ["const:5b755c:8", "const:4:8"]]
+ 005b755c ["CALLIND", null, ["register:0:8"]]
- 005b751c bytes 00013fd6
+ 005b755c bytes 00013fd6
~~~


<a id="compare-63062a088092fe8b19197709a2e9507e"></a>

### [`005b7530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7530.md) → [`005b7570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7570.md) FUN_005b7570

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0059da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059da08.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0059da48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059da48.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b7568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7530.md#insn-005b7568) · [`005b7578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7530.md#insn-005b7578) · [`005b7590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7530.md#insn-005b7590)
- 新版 `005b75a8`（命令位置の公開資料なし） · `005b75b8`（命令位置の公開資料なし） · `005b75d0`（命令位置の公開資料なし）

~~~diff
- 005b7568 ["INT_ADD", "register:40f0:8", ["const:5b7568:8", "const:4:8"]]
- 005b7568 ["CALL", null, ["callee:00c53cd0:8"]]
+ 005b75a8 ["INT_ADD", "register:40f0:8", ["const:5b75a8:8", "const:4:8"]]
+ 005b75a8 ["CALL", null, ["callee:00c53cd0:8"]]
- 005b7568 bytes d2701a94
+ 005b75a8 bytes ca711a94
- 005b7578 ["INT_ADD", "register:40f0:8", ["const:5b7578:8", "const:4:8"]]
- 005b7578 ["CALL", null, ["callee:0059da48:8"]]
+ 005b75b8 ["INT_ADD", "register:40f0:8", ["const:5b75b8:8", "const:4:8"]]
+ 005b75b8 ["CALL", null, ["callee:0059da48:8"]]
- 005b7578 bytes 2499ff97
+ 005b75b8 bytes 2499ff97
- 005b7590 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7590 ["INT_ADD", "register:40f0:8", ["const:5b7590:8", "const:4:8"]]
- 005b7590 ["CALLIND", null, ["register:0:8"]]
+ 005b75d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b75d0 ["INT_ADD", "register:40f0:8", ["const:5b75d0:8", "const:4:8"]]
+ 005b75d0 ["CALLIND", null, ["register:0:8"]]
- 005b7590 bytes 00013fd6
+ 005b75d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cd6863240db33aea5b398f18ee8f584"></a>

### [`005b76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b76a4.md) → [`005b76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b76e4.md) FUN_005b76e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b76c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b76a4.md#insn-005b76c0) · [`005b76e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b76a4.md#insn-005b76e0)
- 新版 `005b7700`（命令位置の公開資料なし） · `005b7720`（命令位置の公開資料なし）

~~~diff
- 005b76c0 ["INT_ADD", "register:40f0:8", ["const:5b76c0:8", "const:4:8"]]
- 005b76c0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b7700 ["INT_ADD", "register:40f0:8", ["const:5b7700:8", "const:4:8"]]
+ 005b7700 ["CALL", null, ["callee:00c53d00:8"]]
- 005b76c0 bytes 88701a94
+ 005b7700 bytes 80711a94
- 005b76e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b76e0 ["INT_ADD", "register:40f0:8", ["const:5b76e0:8", "const:4:8"]]
- 005b76e0 ["CALLIND", null, ["register:0:8"]]
+ 005b7720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7720 ["INT_ADD", "register:40f0:8", ["const:5b7720:8", "const:4:8"]]
+ 005b7720 ["CALLIND", null, ["register:0:8"]]
- 005b76e0 bytes 00013fd6
+ 005b7720 bytes 00013fd6
~~~


<a id="compare-deb3387f78f4fd0830c8d4bb98a89c3a"></a>

### [`005b7ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ab8.md) → [`005b7af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7af8.md) FUN_005b7af8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b7af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ab8.md#insn-005b7af4)
- 新版 `005b7b34`（命令位置の公開資料なし）

~~~diff
- 005b7af4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7af4 ["INT_ADD", "register:40f0:8", ["const:5b7af4:8", "const:4:8"]]
- 005b7af4 ["CALLIND", null, ["register:0:8"]]
+ 005b7b34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7b34 ["INT_ADD", "register:40f0:8", ["const:5b7b34:8", "const:4:8"]]
+ 005b7b34 ["CALLIND", null, ["register:0:8"]]
- 005b7af4 bytes 00013fd6
+ 005b7b34 bytes 00013fd6
~~~


<a id="compare-a29729a977b150f80595a99357c38e6c"></a>

### [`005b7b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7b08.md) → [`005b7b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7b48.md) FUN_005b7b48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b7b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7b08.md#insn-005b7b40) · [`005b7b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7b08.md#insn-005b7b70) · [`005b7b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7b08.md#insn-005b7b88)
- 新版 `005b7b80`（命令位置の公開資料なし） · `005b7bb0`（命令位置の公開資料なし） · `005b7bc8`（命令位置の公開資料なし）

~~~diff
- 005b7b40 ["INT_ADD", "register:40f0:8", ["const:5b7b40:8", "const:4:8"]]
- 005b7b40 ["CALL", null, ["callee:00c53cd0:8"]]
+ 005b7b80 ["INT_ADD", "register:40f0:8", ["const:5b7b80:8", "const:4:8"]]
+ 005b7b80 ["CALL", null, ["callee:00c53cd0:8"]]
- 005b7b40 bytes 5c6f1a94
+ 005b7b80 bytes 54701a94
- 005b7b70 ["INT_ADD", "register:40f0:8", ["const:5b7b70:8", "const:4:8"]]
- 005b7b70 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b7bb0 ["INT_ADD", "register:40f0:8", ["const:5b7bb0:8", "const:4:8"]]
+ 005b7bb0 ["CALL", null, ["callee:0043bb20:8"]]
- 005b7b70 bytes dc0ffa97
+ 005b7bb0 bytes dc0ffa97
- 005b7b88 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7b88 ["INT_ADD", "register:40f0:8", ["const:5b7b88:8", "const:4:8"]]
- 005b7b88 ["CALLIND", null, ["register:0:8"]]
+ 005b7bc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7bc8 ["INT_ADD", "register:40f0:8", ["const:5b7bc8:8", "const:4:8"]]
+ 005b7bc8 ["CALLIND", null, ["register:0:8"]]
- 005b7b88 bytes 00013fd6
+ 005b7bc8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b2679f3943f2ec573f01e6672899da"></a>

### [`005b7c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7c68.md) → [`005b7ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7ca8.md) FUN_005b7ca8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b7c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7c68.md#insn-005b7c84) · [`005b7ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7c68.md#insn-005b7ca4)
- 新版 `005b7cc4`（命令位置の公開資料なし） · `005b7ce4`（命令位置の公開資料なし）

~~~diff
- 005b7c84 ["INT_ADD", "register:40f0:8", ["const:5b7c84:8", "const:4:8"]]
- 005b7c84 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b7cc4 ["INT_ADD", "register:40f0:8", ["const:5b7cc4:8", "const:4:8"]]
+ 005b7cc4 ["CALL", null, ["callee:00c53d00:8"]]
- 005b7c84 bytes 176f1a94
+ 005b7cc4 bytes 0f701a94
- 005b7ca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7ca4 ["INT_ADD", "register:40f0:8", ["const:5b7ca4:8", "const:4:8"]]
- 005b7ca4 ["CALLIND", null, ["register:0:8"]]
+ 005b7ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7ce4 ["INT_ADD", "register:40f0:8", ["const:5b7ce4:8", "const:4:8"]]
+ 005b7ce4 ["CALLIND", null, ["register:0:8"]]
- 005b7ca4 bytes 00013fd6
+ 005b7ce4 bytes 00013fd6
~~~


<a id="compare-8c190c6d7cec3edeaf7aabf60d340fc5"></a>

### [`005b8004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8004.md) → [`005b8044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8044.md) FUN_005b8044

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8004.md#insn-005b8040)
- 新版 `005b8080`（命令位置の公開資料なし）

~~~diff
- 005b8040 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8040 ["INT_ADD", "register:40f0:8", ["const:5b8040:8", "const:4:8"]]
- 005b8040 ["CALLIND", null, ["register:0:8"]]
+ 005b8080 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8080 ["INT_ADD", "register:40f0:8", ["const:5b8080:8", "const:4:8"]]
+ 005b8080 ["CALLIND", null, ["register:0:8"]]
- 005b8040 bytes 00013fd6
+ 005b8080 bytes 00013fd6
~~~


<a id="compare-5da7a9d6dda7085891fb7cb894f79b7b"></a>

### [`005b8054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8054.md) → [`005b8094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8094.md) FUN_005b8094

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8054.md#insn-005b8070)
- 新版 `005b80b0`（命令位置の公開資料なし）

~~~diff
- 005b8070 ["INT_ADD", "register:40f0:8", ["const:5b8070:8", "const:4:8"]]
- 005b8070 ["CALL", null, ["callee:00459d74:8"]]
+ 005b80b0 ["INT_ADD", "register:40f0:8", ["const:5b80b0:8", "const:4:8"]]
+ 005b80b0 ["CALL", null, ["callee:00459d74:8"]]
- 005b8070 bytes 3187fa97
+ 005b80b0 bytes 3187fa97
~~~


<a id="compare-a8efbb0707a5b4c838423e31828e1205"></a>

### [`005b83e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b83e8.md) → [`005b8428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8428.md) FUN_005b8428

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b83e8.md#insn-005b8424)
- 新版 `005b8464`（命令位置の公開資料なし）

~~~diff
- 005b8424 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8424 ["INT_ADD", "register:40f0:8", ["const:5b8424:8", "const:4:8"]]
- 005b8424 ["CALLIND", null, ["register:0:8"]]
+ 005b8464 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8464 ["INT_ADD", "register:40f0:8", ["const:5b8464:8", "const:4:8"]]
+ 005b8464 ["CALLIND", null, ["register:0:8"]]
- 005b8424 bytes 00013fd6
+ 005b8464 bytes 00013fd6
~~~


<a id="compare-d1b595fd23f6a745bc1a4e0f34001ce8"></a>

### [`005b8438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8438.md) → [`005b8478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8478.md) FUN_005b8478

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8438.md#insn-005b8454)
- 新版 `005b8494`（命令位置の公開資料なし）

~~~diff
- 005b8454 ["INT_ADD", "register:40f0:8", ["const:5b8454:8", "const:4:8"]]
- 005b8454 ["CALL", null, ["callee:00459d74:8"]]
+ 005b8494 ["INT_ADD", "register:40f0:8", ["const:5b8494:8", "const:4:8"]]
+ 005b8494 ["CALL", null, ["callee:00459d74:8"]]
- 005b8454 bytes 3886fa97
+ 005b8494 bytes 3886fa97
~~~


<a id="compare-3d6b680a8fdf0c4cf95264646f7c78de"></a>

### [`005b87cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b87cc.md) → [`005b880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b880c.md) FUN_005b880c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b87cc.md#insn-005b8808)
- 新版 `005b8848`（命令位置の公開資料なし）

~~~diff
- 005b8808 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8808 ["INT_ADD", "register:40f0:8", ["const:5b8808:8", "const:4:8"]]
- 005b8808 ["CALLIND", null, ["register:0:8"]]
+ 005b8848 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8848 ["INT_ADD", "register:40f0:8", ["const:5b8848:8", "const:4:8"]]
+ 005b8848 ["CALLIND", null, ["register:0:8"]]
- 005b8808 bytes 00013fd6
+ 005b8848 bytes 00013fd6
~~~


<a id="compare-fc124cb9bd1a44a2b6746645adb9c962"></a>

### [`005b881c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b881c.md) → [`005b885c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b885c.md) FUN_005b885c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b881c.md#insn-005b8854) · [`005b8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b881c.md#insn-005b8884) · [`005b88b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b881c.md#insn-005b88b0)
- 新版 `005b8894`（命令位置の公開資料なし） · `005b88c4`（命令位置の公開資料なし） · `005b88f0`（命令位置の公開資料なし）

~~~diff
- 005b8854 ["INT_ADD", "register:40f0:8", ["const:5b8854:8", "const:4:8"]]
- 005b8854 ["CALL", null, ["callee:00c53cd0:8"]]
+ 005b8894 ["INT_ADD", "register:40f0:8", ["const:5b8894:8", "const:4:8"]]
+ 005b8894 ["CALL", null, ["callee:00c53cd0:8"]]
- 005b8854 bytes 176c1a94
+ 005b8894 bytes 0f6d1a94
- 005b8884 ["INT_ADD", "register:40f0:8", ["const:5b8884:8", "const:4:8"]]
- 005b8884 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b88c4 ["INT_ADD", "register:40f0:8", ["const:5b88c4:8", "const:4:8"]]
+ 005b88c4 ["CALL", null, ["callee:0043bb20:8"]]
- 005b8884 bytes 970cfa97
+ 005b88c4 bytes 970cfa97
- 005b88b0 ["INT_ADD", "register:40f0:8", ["const:5b88b0:8", "const:4:8"]]
- 005b88b0 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b88f0 ["INT_ADD", "register:40f0:8", ["const:5b88f0:8", "const:4:8"]]
+ 005b88f0 ["CALL", null, ["callee:0043bb20:8"]]
- 005b88b0 bytes 8c0cfa97
+ 005b88f0 bytes 8c0cfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32e35565efcb7008bce768356eabeb4d"></a>

### [`005b89d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b89d4.md) → [`005b8a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a14.md) FUN_005b8a14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b89f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b89d4.md#insn-005b89f0) · [`005b8a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b89d4.md#insn-005b8a10)
- 新版 `005b8a30`（命令位置の公開資料なし） · `005b8a50`（命令位置の公開資料なし）

~~~diff
- 005b89f0 ["INT_ADD", "register:40f0:8", ["const:5b89f0:8", "const:4:8"]]
- 005b89f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b8a30 ["INT_ADD", "register:40f0:8", ["const:5b8a30:8", "const:4:8"]]
+ 005b8a30 ["CALL", null, ["callee:00c53d00:8"]]
- 005b89f0 bytes bc6b1a94
+ 005b8a30 bytes b46c1a94
- 005b8a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8a10 ["INT_ADD", "register:40f0:8", ["const:5b8a10:8", "const:4:8"]]
- 005b8a10 ["CALLIND", null, ["register:0:8"]]
+ 005b8a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8a50 ["INT_ADD", "register:40f0:8", ["const:5b8a50:8", "const:4:8"]]
+ 005b8a50 ["CALLIND", null, ["register:0:8"]]
- 005b8a10 bytes 00013fd6
+ 005b8a50 bytes 00013fd6
~~~


<a id="compare-4fbdd39d9a5ee2cc1ef51c67a1c46106"></a>

### [`005b8dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8dc0.md) → [`005b8e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8e00.md) FUN_005b8e00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8dc0.md#insn-005b8dfc)
- 新版 `005b8e3c`（命令位置の公開資料なし）

~~~diff
- 005b8dfc ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8dfc ["INT_ADD", "register:40f0:8", ["const:5b8dfc:8", "const:4:8"]]
- 005b8dfc ["CALLIND", null, ["register:0:8"]]
+ 005b8e3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8e3c ["INT_ADD", "register:40f0:8", ["const:5b8e3c:8", "const:4:8"]]
+ 005b8e3c ["CALLIND", null, ["register:0:8"]]
- 005b8dfc bytes 00013fd6
+ 005b8e3c bytes 00013fd6
~~~


<a id="compare-e4b214a39153e086f83d44d4aa538d0a"></a>

### [`005b8e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8e10.md) → [`005b8e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8e50.md) FUN_005b8e50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8e10.md#insn-005b8e48) · [`005b8e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8e10.md#insn-005b8e6c) · [`005b8e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8e10.md#insn-005b8e7c)
- 新版 `005b8e88`（命令位置の公開資料なし） · `005b8eac`（命令位置の公開資料なし） · `005b8ebc`（命令位置の公開資料なし）

~~~diff
- 005b8e48 ["INT_ADD", "register:40f0:8", ["const:5b8e48:8", "const:4:8"]]
- 005b8e48 ["CALL", null, ["callee:00c53cd0:8"]]
+ 005b8e88 ["INT_ADD", "register:40f0:8", ["const:5b8e88:8", "const:4:8"]]
+ 005b8e88 ["CALL", null, ["callee:00c53cd0:8"]]
- 005b8e48 bytes 9a6a1a94
+ 005b8e88 bytes 926b1a94
- 005b8e6c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8e6c ["INT_ADD", "register:40f0:8", ["const:5b8e6c:8", "const:4:8"]]
- 005b8e6c ["CALLIND", null, ["register:0:8"]]
+ 005b8eac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8eac ["INT_ADD", "register:40f0:8", ["const:5b8eac:8", "const:4:8"]]
+ 005b8eac ["CALLIND", null, ["register:0:8"]]
- 005b8e6c bytes 00013fd6
+ 005b8eac bytes 00013fd6
- 005b8e7c ["INT_ADD", "register:40f0:8", ["const:5b8e7c:8", "const:4:8"]]
- 005b8e7c ["CALL", null, ["callee:00c53d00:8"]]
+ 005b8ebc ["INT_ADD", "register:40f0:8", ["const:5b8ebc:8", "const:4:8"]]
+ 005b8ebc ["CALL", null, ["callee:00c53d00:8"]]
- 005b8e7c bytes 996a1a94
+ 005b8ebc bytes 916b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6418b651e631883808198d06006c279b"></a>

### [`005b8f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f24.md) → [`005b8f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8f64.md) FUN_005b8f64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b8f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f24.md#insn-005b8f40) · [`005b8f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f24.md#insn-005b8f60)
- 新版 `005b8f80`（命令位置の公開資料なし） · `005b8fa0`（命令位置の公開資料なし）

~~~diff
- 005b8f40 ["INT_ADD", "register:40f0:8", ["const:5b8f40:8", "const:4:8"]]
- 005b8f40 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b8f80 ["INT_ADD", "register:40f0:8", ["const:5b8f80:8", "const:4:8"]]
+ 005b8f80 ["CALL", null, ["callee:00c53d00:8"]]
- 005b8f40 bytes 686a1a94
+ 005b8f80 bytes 606b1a94
- 005b8f60 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8f60 ["INT_ADD", "register:40f0:8", ["const:5b8f60:8", "const:4:8"]]
- 005b8f60 ["CALLIND", null, ["register:0:8"]]
+ 005b8fa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8fa0 ["INT_ADD", "register:40f0:8", ["const:5b8fa0:8", "const:4:8"]]
+ 005b8fa0 ["CALLIND", null, ["register:0:8"]]
- 005b8f60 bytes 00013fd6
+ 005b8fa0 bytes 00013fd6
~~~


<a id="compare-ca4e691cde9bf14bba7e126449fd2fde"></a>

### [`005b92c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b92c0.md) → [`005b9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9300.md) FUN_005b9300

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b4a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b4a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b92fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b92c0.md#insn-005b92fc)
- 新版 `005b933c`（命令位置の公開資料なし）

~~~diff
- 005b92fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005b92fc ["INT_ADD", "register:40f0:8", ["const:5b92fc:8", "const:4:8"]]
- 005b92fc ["CALLIND", null, ["register:0:8"]]
+ 005b933c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b933c ["INT_ADD", "register:40f0:8", ["const:5b933c:8", "const:4:8"]]
+ 005b933c ["CALLIND", null, ["register:0:8"]]
- 005b92fc bytes 00013fd6
+ 005b933c bytes 00013fd6
~~~


<a id="compare-2c4129bf43871f942c84d48b77db5b14"></a>

### [`005b9310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9310.md) → [`005b9350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9350.md) FUN_005b9350

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b932c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9310.md#insn-005b932c)
- 新版 `005b936c`（命令位置の公開資料なし）

~~~diff
- 005b932c ["INT_ADD", "register:40f0:8", ["const:5b932c:8", "const:4:8"]]
- 005b932c ["CALL", null, ["callee:00459d74:8"]]
+ 005b936c ["INT_ADD", "register:40f0:8", ["const:5b936c:8", "const:4:8"]]
+ 005b936c ["CALL", null, ["callee:00459d74:8"]]
- 005b932c bytes 8282fa97
+ 005b936c bytes 8282fa97
~~~


<a id="compare-f2b57a1b8a1a2f8ab7cfe2f5d43ebd8d"></a>

### [`005b9358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9358.md) → [`005b9398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9398.md) FUN_005b9398

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b2c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b2c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b93c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9358.md#insn-005b93c4) · [`005b93d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9358.md#insn-005b93d4) · [`005b93f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9358.md#insn-005b93f4)
- 新版 `005b9404`（命令位置の公開資料なし） · `005b9414`（命令位置の公開資料なし） · `005b9434`（命令位置の公開資料なし）

~~~diff
- 005b93c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b93c4 ["INT_ADD", "register:40f0:8", ["const:5b93c4:8", "const:4:8"]]
- 005b93c4 ["CALLIND", null, ["register:0:8"]]
+ 005b9404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9404 ["INT_ADD", "register:40f0:8", ["const:5b9404:8", "const:4:8"]]
+ 005b9404 ["CALLIND", null, ["register:0:8"]]
- 005b93c4 bytes 00013fd6
+ 005b9404 bytes 00013fd6
- 005b93d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b93d4 ["INT_ADD", "register:40f0:8", ["const:5b93d4:8", "const:4:8"]]
- 005b93d4 ["CALLIND", null, ["register:0:8"]]
+ 005b9414 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9414 ["INT_ADD", "register:40f0:8", ["const:5b9414:8", "const:4:8"]]
+ 005b9414 ["CALLIND", null, ["register:0:8"]]
- 005b93d4 bytes 00013fd6
+ 005b9414 bytes 00013fd6
- 005b93f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b93f4 ["INT_ADD", "register:40f0:8", ["const:5b93f4:8", "const:4:8"]]
- 005b93f4 ["CALLIND", null, ["register:0:8"]]
+ 005b9434 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9434 ["INT_ADD", "register:40f0:8", ["const:5b9434:8", "const:4:8"]]
+ 005b9434 ["CALLIND", null, ["register:0:8"]]
- 005b93f4 bytes 00013fd6
+ 005b9434 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c7ee05f1e03b44d666091f897fa19c1"></a>

### [`005b94c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b94c0.md) → [`005b9500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9500.md) FUN_005b9500

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ea8.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b2ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b94c0.md#insn-005b952c) · [`005b953c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b94c0.md#insn-005b953c) · [`005b955c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b94c0.md#insn-005b955c)
- 新版 `005b956c`（命令位置の公開資料なし） · `005b957c`（命令位置の公開資料なし） · `005b959c`（命令位置の公開資料なし）

~~~diff
- 005b952c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b952c ["INT_ADD", "register:40f0:8", ["const:5b952c:8", "const:4:8"]]
- 005b952c ["CALLIND", null, ["register:0:8"]]
+ 005b956c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b956c ["INT_ADD", "register:40f0:8", ["const:5b956c:8", "const:4:8"]]
+ 005b956c ["CALLIND", null, ["register:0:8"]]
- 005b952c bytes 00013fd6
+ 005b956c bytes 00013fd6
- 005b953c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b953c ["INT_ADD", "register:40f0:8", ["const:5b953c:8", "const:4:8"]]
- 005b953c ["CALLIND", null, ["register:0:8"]]
+ 005b957c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b957c ["INT_ADD", "register:40f0:8", ["const:5b957c:8", "const:4:8"]]
+ 005b957c ["CALLIND", null, ["register:0:8"]]
- 005b953c bytes 00013fd6
+ 005b957c bytes 00013fd6
- 005b955c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b955c ["INT_ADD", "register:40f0:8", ["const:5b955c:8", "const:4:8"]]
- 005b955c ["CALLIND", null, ["register:0:8"]]
+ 005b959c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b959c ["INT_ADD", "register:40f0:8", ["const:5b959c:8", "const:4:8"]]
+ 005b959c ["CALLIND", null, ["register:0:8"]]
- 005b955c bytes 00013fd6
+ 005b959c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e189f39de4ac752b50e0b56d6decccc"></a>

### [`005b99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md) → [`005b9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a0c.md) FUN_005b9a0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b99ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md#insn-005b99ec) · [`005b99f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md#insn-005b99f8)
- 新版 `005b9a2c`（命令位置の公開資料なし） · `005b9a38`（命令位置の公開資料なし）

~~~diff
- 005b99ec ["INT_ADD", "register:40f0:8", ["const:5b99ec:8", "const:4:8"]]
- 005b99ec ["CALL", null, ["callee:00480d48:8"]]
+ 005b9a2c ["INT_ADD", "register:40f0:8", ["const:5b9a2c:8", "const:4:8"]]
+ 005b9a2c ["CALL", null, ["callee:00480d48:8"]]
- 005b99ec bytes c71cfb97
+ 005b9a2c bytes c71cfb97
- 005b99f8 ["INT_ADD", "register:40f0:8", ["const:5b99f8:8", "const:4:8"]]
- 005b99f8 ["CALL", null, ["callee:00480e28:8"]]
+ 005b9a38 ["INT_ADD", "register:40f0:8", ["const:5b9a38:8", "const:4:8"]]
+ 005b9a38 ["CALL", null, ["callee:00480e28:8"]]
- 005b99f8 bytes fc1cfb97
+ 005b9a38 bytes fc1cfb97
~~~


<a id="compare-e2b5659f0ccd76a498602b2ecb12d13a"></a>

### [`005b9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md) → [`005b9a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a50.md) FUN_005b9a50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b9a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md#insn-005b9a28) · [`005b9a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md#insn-005b9a38) · [`005b9a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md#insn-005b9a44)
- 新版 `005b9a68`（命令位置の公開資料なし） · `005b9a78`（命令位置の公開資料なし） · `005b9a84`（命令位置の公開資料なし）

~~~diff
- 005b9a28 ["INT_ADD", "register:40f0:8", ["const:5b9a28:8", "const:4:8"]]
- 005b9a28 ["CALL", null, ["callee:004802f8:8"]]
+ 005b9a68 ["INT_ADD", "register:40f0:8", ["const:5b9a68:8", "const:4:8"]]
+ 005b9a68 ["CALL", null, ["callee:004802f8:8"]]
- 005b9a28 bytes 241afb97
+ 005b9a68 bytes 241afb97
- 005b9a38 ["INT_ADD", "register:40f0:8", ["const:5b9a38:8", "const:4:8"]]
- 005b9a38 ["CALL", null, ["callee:004803f0:8"]]
+ 005b9a78 ["INT_ADD", "register:40f0:8", ["const:5b9a78:8", "const:4:8"]]
+ 005b9a78 ["CALL", null, ["callee:004803f0:8"]]
- 005b9a38 bytes 5e1afb97
+ 005b9a78 bytes 5e1afb97
- 005b9a44 ["INT_ADD", "register:40f0:8", ["const:5b9a44:8", "const:4:8"]]
- 005b9a44 ["CALL", null, ["callee:00480744:8"]]
+ 005b9a84 ["INT_ADD", "register:40f0:8", ["const:5b9a84:8", "const:4:8"]]
+ 005b9a84 ["CALL", null, ["callee:00480744:8"]]
- 005b9a44 bytes 301bfb97
+ 005b9a84 bytes 301bfb97
~~~


<a id="compare-92ae124ab6df1f723d5df2b87a94f69b"></a>

### [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) → [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) FUN_005b9ee4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 16件 [`005b9b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md) [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) [`005c62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md) [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 16件 [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) [`005c6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6300.md) [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b9ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md#insn-005b9ec0) · [`005b9ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md#insn-005b9ecc) · [`005b9edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md#insn-005b9edc)
- 新版 `005b9f00`（命令位置の公開資料なし） · `005b9f0c`（命令位置の公開資料なし） · `005b9f1c`（命令位置の公開資料なし）

~~~diff
- 005b9ec0 ["INT_ADD", "register:40f0:8", ["const:5b9ec0:8", "const:4:8"]]
- 005b9ec0 ["CALL", null, ["local:b0:8"]]
+ 005b9f00 ["INT_ADD", "register:40f0:8", ["const:5b9f00:8", "const:4:8"]]
+ 005b9f00 ["CALL", null, ["local:b0:8"]]
- 005b9ec0 bytes f9ffff97
+ 005b9f00 bytes f9ffff97
- 005b9ecc ["INT_ADD", "register:40f0:8", ["const:5b9ecc:8", "const:4:8"]]
- 005b9ecc ["CALL", null, ["local:b0:8"]]
+ 005b9f0c ["INT_ADD", "register:40f0:8", ["const:5b9f0c:8", "const:4:8"]]
+ 005b9f0c ["CALL", null, ["local:b0:8"]]
- 005b9ecc bytes f6ffff97
+ 005b9f0c bytes f6ffff97
- 005b9edc ["INT_ADD", "register:40f0:8", ["const:5b9edc:8", "const:4:8"]]
- 005b9edc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b9f1c ["INT_ADD", "register:40f0:8", ["const:5b9f1c:8", "const:4:8"]]
+ 005b9f1c ["CALL", null, ["callee:00c57eb0:8"]]
- 005b9edc bytes f5761a94
+ 005b9f1c bytes e5771a94
~~~


<a id="compare-a6f16d29438ef9d17dd4ac39b085d9a7"></a>

### [`005ba6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md) → [`005ba708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba708.md) FUN_005ba708

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ba6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md#insn-005ba6e8) · [`005ba700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md#insn-005ba700) · [`005ba720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md#insn-005ba720)
- 新版 `005ba728`（命令位置の公開資料なし） · `005ba740`（命令位置の公開資料なし） · `005ba760`（命令位置の公開資料なし）

~~~diff
- 005ba6e8 ["INT_ADD", "register:40f0:8", ["const:5ba6e8:8", "const:4:8"]]
- 005ba6e8 ["CALL", null, ["callee:00c53d00:8"]]
+ 005ba728 ["INT_ADD", "register:40f0:8", ["const:5ba728:8", "const:4:8"]]
+ 005ba728 ["CALL", null, ["callee:00c53d00:8"]]
- 005ba6e8 bytes 7e641a94
+ 005ba728 bytes 76651a94
- 005ba700 ["INT_ADD", "register:40f0:8", ["const:5ba700:8", "const:4:8"]]
- 005ba700 ["CALL", null, ["callee:00c53d00:8"]]
+ 005ba740 ["INT_ADD", "register:40f0:8", ["const:5ba740:8", "const:4:8"]]
+ 005ba740 ["CALL", null, ["callee:00c53d00:8"]]
- 005ba700 bytes 78641a94
+ 005ba740 bytes 70651a94
- 005ba720 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ba720 ["INT_ADD", "register:40f0:8", ["const:5ba720:8", "const:4:8"]]
- 005ba720 ["CALLIND", null, ["register:0:8"]]
+ 005ba760 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ba760 ["INT_ADD", "register:40f0:8", ["const:5ba760:8", "const:4:8"]]
+ 005ba760 ["CALLIND", null, ["register:0:8"]]
- 005ba720 bytes 00013fd6
+ 005ba760 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-599b2b4fa78564c1d099a186b99ab94e"></a>

### [`005bac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bac90.md) → [`005bacd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bacd0.md) FUN_005bacd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b35d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b36164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36164.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005bacbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bac90.md#insn-005bacbc) · [`005bacf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bac90.md#insn-005bacf4) · [`005bad24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bac90.md#insn-005bad24)
- 新版 `005bacfc`（命令位置の公開資料なし） · `005bad34`（命令位置の公開資料なし） · `005bad64`（命令位置の公開資料なし）

~~~diff
- 005bacbc ["INT_ADD", "register:40f0:8", ["const:5bacbc:8", "const:4:8"]]
- 005bacbc ["CALL", null, ["callee:00b36164:8"]]
+ 005bacfc ["INT_ADD", "register:40f0:8", ["const:5bacfc:8", "const:4:8"]]
+ 005bacfc ["CALL", null, ["callee:00b36164:8"]]
- 005bacbc bytes 20ec1594
+ 005bacfc bytes 1aed1594
- 005bacf4 ["INT_ADD", "register:40f0:8", ["const:5bacf4:8", "const:4:8"]]
- 005bacf4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005bad34 ["INT_ADD", "register:40f0:8", ["const:5bad34:8", "const:4:8"]]
+ 005bad34 ["CALL", null, ["callee:00c57eb0:8"]]
- 005bacf4 bytes 6f731a94
+ 005bad34 bytes 5f741a94
- 005bad24 ["INT_ADD", "register:40f0:8", ["const:5bad24:8", "const:4:8"]]
- 005bad24 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005bad64 ["INT_ADD", "register:40f0:8", ["const:5bad64:8", "const:4:8"]]
+ 005bad64 ["CALL", null, ["callee:00c57ee0:8"]]
- 005bad24 bytes 6f731a94
+ 005bad64 bytes 5f741a94
~~~


<a id="compare-fa535daf5b7d44a45d3d715d9f240410"></a>

### [`005bad8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad8c.md) → [`005badcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005badcc.md) FUN_005badcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005ba918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba918.md) · 呼出先 2件 [`00c58130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58140.md)
- 新版 呼出元 1件 [`005ba958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba958.md) · 呼出先 2件 [`00c58530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58530.md) [`00c58540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005bad9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad8c.md#insn-005bad9c)
- 新版 `005baddc`（命令位置の公開資料なし）

~~~diff
- 005bad9c ["INT_ADD", "register:40f0:8", ["const:5bad9c:8", "const:4:8"]]
- 005bad9c ["CALL", null, ["callee:00c58530:8"]]
+ 005baddc ["INT_ADD", "register:40f0:8", ["const:5baddc:8", "const:4:8"]]
+ 005baddc ["CALL", null, ["callee:00c58530:8"]]
- 005bad9c bytes e5741a94
+ 005baddc bytes d5751a94
~~~


<a id="compare-a6b6aa0358313f23b5e563c38e89ea2d"></a>

### [`005badb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005badb4.md) → [`005badf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005badf4.md) FUN_005badf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005badd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005badb4.md#insn-005badd8) · [`005bade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005badb4.md#insn-005bade0) · [`005bae54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005badb4.md#insn-005bae54)
- 新版 `005bae18`（命令位置の公開資料なし） · `005bae20`（命令位置の公開資料なし） · `005bae94`（命令位置の公開資料なし）

~~~diff
- 005badd8 ["INT_ADD", "register:40f0:8", ["const:5badd8:8", "const:4:8"]]
- 005badd8 ["CALL", null, ["callee:005ba798:8"]]
+ 005bae18 ["INT_ADD", "register:40f0:8", ["const:5bae18:8", "const:4:8"]]
+ 005bae18 ["CALL", null, ["callee:005ba798:8"]]
- 005badd8 bytes 60feff97
+ 005bae18 bytes 60feff97
- 005bade0 ["INT_ADD", "register:40f0:8", ["const:5bade0:8", "const:4:8"]]
- 005bade0 ["CALL", null, ["callee:00c58550:8"]]
+ 005bae20 ["INT_ADD", "register:40f0:8", ["const:5bae20:8", "const:4:8"]]
+ 005bae20 ["CALL", null, ["callee:00c58550:8"]]
- 005bade0 bytes dc741a94
+ 005bae20 bytes cc751a94
- 005bae54 ["INT_ADD", "register:40f0:8", ["const:5bae54:8", "const:4:8"]]
- 005bae54 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005bae94 ["INT_ADD", "register:40f0:8", ["const:5bae94:8", "const:4:8"]]
+ 005bae94 ["CALL", null, ["callee:00c57ee0:8"]]
- 005bae54 bytes 23731a94
+ 005bae94 bytes 13741a94
~~~


<a id="compare-e99d9348da05e81d1b39ba8403c0d8fb"></a>

### [`005bae5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bae5c.md) → [`005bae9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bae9c.md) FUN_005bae9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ba918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba918.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 1件 [`005ba958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba958.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005bae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bae5c.md#insn-005bae84) · [`005bae94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bae5c.md#insn-005bae94) · [`005baeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bae5c.md#insn-005baeb0)
- 新版 `005baec4`（命令位置の公開資料なし） · `005baed4`（命令位置の公開資料なし） · `005baef0`（命令位置の公開資料なし）

~~~diff
- 005bae84 ["INT_ADD", "register:40f0:8", ["const:5bae84:8", "const:4:8"]]
- 005bae84 ["CALL", null, ["callee:00c58130:8"]]
+ 005baec4 ["INT_ADD", "register:40f0:8", ["const:5baec4:8", "const:4:8"]]
+ 005baec4 ["CALL", null, ["callee:00c58130:8"]]
- 005bae84 bytes ab731a94
+ 005baec4 bytes 9b741a94
- 005bae94 ["INT_ADD", "register:40f0:8", ["const:5bae94:8", "const:4:8"]]
- 005bae94 ["CALL", null, ["callee:00c58140:8"]]
+ 005baed4 ["INT_ADD", "register:40f0:8", ["const:5baed4:8", "const:4:8"]]
+ 005baed4 ["CALL", null, ["callee:00c58140:8"]]
- 005bae94 bytes ab731a94
+ 005baed4 bytes 9b741a94
- 005baeb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005baeb0 ["INT_ADD", "register:40f0:8", ["const:5baeb0:8", "const:4:8"]]
- 005baeb0 ["CALLIND", null, ["register:0:8"]]
+ 005baef0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005baef0 ["INT_ADD", "register:40f0:8", ["const:5baef0:8", "const:4:8"]]
+ 005baef0 ["CALLIND", null, ["register:0:8"]]
- 005baeb0 bytes 00013fd6
+ 005baef0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f355ba5cc63f3bfd6464c7d3227cfde"></a>

### [`005baf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005baf28.md) → [`005baf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005baf68.md) FUN_005baf68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005baf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005baf28.md#insn-005baf50) · [`005baf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005baf28.md#insn-005baf58)
- 新版 `005baf90`（命令位置の公開資料なし） · `005baf98`（命令位置の公開資料なし）

~~~diff
- 005baf50 ["INT_ADD", "register:40f0:8", ["const:5baf50:8", "const:4:8"]]
- 005baf50 ["CALL", null, ["callee:00c58150:8"]]
+ 005baf90 ["INT_ADD", "register:40f0:8", ["const:5baf90:8", "const:4:8"]]
+ 005baf90 ["CALL", null, ["callee:00c58150:8"]]
- 005baf50 bytes 80731a94
+ 005baf90 bytes 70741a94
- 005baf58 ["INT_ADD", "register:40f0:8", ["const:5baf58:8", "const:4:8"]]
- 005baf58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005baf98 ["INT_ADD", "register:40f0:8", ["const:5baf98:8", "const:4:8"]]
+ 005baf98 ["CALL", null, ["callee:00c57eb0:8"]]
- 005baf58 bytes d6721a94
+ 005baf98 bytes c6731a94
~~~


<a id="compare-db4b07bb10f570f5a216e446d468ecfd"></a>

### [`005bb308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md) → [`005bb348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb348.md) FUN_005bb348

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 5件 [`005bb344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb344.md) [`005bb6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb6b8.md) [`005bbed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bbed4.md) [`005bc1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc1f8.md) [`005bc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 5件 [`005bb384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb384.md) [`005bb6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb6f8.md) [`005bbf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bbf14.md) [`005bc238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc238.md) [`005bc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc518.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005bb318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md#insn-005bb318) · [`005bb320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md#insn-005bb320) · [`005bb328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md#insn-005bb328)
- 新版 `005bb358`（命令位置の公開資料なし） · `005bb360`（命令位置の公開資料なし） · `005bb368`（命令位置の公開資料なし）

~~~diff
- 005bb318 ["INT_ADD", "register:40f0:8", ["const:5bb318:8", "const:4:8"]]
- 005bb318 ["CALL", null, ["callee:005bb384:8"]]
+ 005bb358 ["INT_ADD", "register:40f0:8", ["const:5bb358:8", "const:4:8"]]
+ 005bb358 ["CALL", null, ["callee:005bb384:8"]]
- 005bb318 bytes 0b000094
+ 005bb358 bytes 0b000094
- 005bb320 ["INT_ADD", "register:40f0:8", ["const:5bb320:8", "const:4:8"]]
- 005bb320 ["CALL", null, ["callee:005bb6f8:8"]]
+ 005bb360 ["INT_ADD", "register:40f0:8", ["const:5bb360:8", "const:4:8"]]
+ 005bb360 ["CALL", null, ["callee:005bb6f8:8"]]
- 005bb320 bytes e6000094
+ 005bb360 bytes e6000094
- 005bb328 ["INT_ADD", "register:40f0:8", ["const:5bb328:8", "const:4:8"]]
- 005bb328 ["CALL", null, ["callee:005bbf14:8"]]
+ 005bb368 ["INT_ADD", "register:40f0:8", ["const:5bb368:8", "const:4:8"]]
+ 005bb368 ["CALL", null, ["callee:005bbf14:8"]]
- 005bb328 bytes eb020094
+ 005bb368 bytes eb020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02386dc8d9055ab9595edf26bff96d26"></a>

### [`005c04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md) → [`005c04f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c04f0.md) FUN_005c04f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) [`008c79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c7/008c79a4.md) [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 10件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`008c5da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5da4.md) [`008c7b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c7/008c7b40.md) [`00ad6a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a88.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c055c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md#insn-005c055c) · [`005c0598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md#insn-005c0598) · [`005c0604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md#insn-005c0604)
- 新版 `005c059c`（命令位置の公開資料なし） · `005c05d8`（命令位置の公開資料なし） · `005c0644`（命令位置の公開資料なし）

~~~diff
- 005c055c ["INT_ADD", "register:40f0:8", ["const:5c055c:8", "const:4:8"]]
- 005c055c ["CALL", null, ["callee:00c57e90:8"]]
+ 005c059c ["INT_ADD", "register:40f0:8", ["const:5c059c:8", "const:4:8"]]
+ 005c059c ["CALL", null, ["callee:00c57e90:8"]]
- 005c055c bytes 4d5d1a94
+ 005c059c bytes 3d5e1a94
- 005c0598 ["INT_ADD", "register:40f0:8", ["const:5c0598:8", "const:4:8"]]
- 005c0598 ["CALL", null, ["callee:0043bba4:8"]]
+ 005c05d8 ["INT_ADD", "register:40f0:8", ["const:5c05d8:8", "const:4:8"]]
+ 005c05d8 ["CALL", null, ["callee:0043bba4:8"]]
- 005c0598 bytes 73edf997
+ 005c05d8 bytes 73edf997
- 005c0604 ["INT_ADD", "register:40f0:8", ["const:5c0604:8", "const:4:8"]]
- 005c0604 ["CALL", null, ["callee:00c57e90:8"]]
+ 005c0644 ["INT_ADD", "register:40f0:8", ["const:5c0644:8", "const:4:8"]]
+ 005c0644 ["CALL", null, ["callee:00c57e90:8"]]
- 005c0604 bytes 235d1a94
+ 005c0644 bytes 135e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf2788491c9b26b7abe0b9312ff596c"></a>

### [`005c0b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b24.md) → [`005c0b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b64.md) FUN_005c0b64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c0b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b24.md#insn-005c0b3c)
- 新版 `005c0b7c`（命令位置の公開資料なし）

~~~diff
- 005c0b3c ["INT_ADD", "register:40f0:8", ["const:5c0b3c:8", "const:4:8"]]
- 005c0b3c ["CALL", null, ["callee:005c3e7c:8"]]
+ 005c0b7c ["INT_ADD", "register:40f0:8", ["const:5c0b7c:8", "const:4:8"]]
+ 005c0b7c ["CALL", null, ["callee:005c3e7c:8"]]
- 005c0b3c bytes c00c0094
+ 005c0b7c bytes c00c0094
~~~


<a id="compare-0f79c8c12292f1f7f78f1f8e5287fa68"></a>

### [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) → [`005c0b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b98.md) FUN_005c0b98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c0b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md#insn-005c0b8c) · [`005c0ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md#insn-005c0ba0) · [`005c0bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md#insn-005c0bd8)
- 新版 `005c0bcc`（命令位置の公開資料なし） · `005c0be0`（命令位置の公開資料なし） · `005c0c18`（命令位置の公開資料なし）

~~~diff
- 005c0b8c ["INT_ADD", "register:40f0:8", ["const:5c0b8c:8", "const:4:8"]]
- 005c0b8c ["CALL", null, ["callee:005c3e7c:8"]]
+ 005c0bcc ["INT_ADD", "register:40f0:8", ["const:5c0bcc:8", "const:4:8"]]
+ 005c0bcc ["CALL", null, ["callee:005c3e7c:8"]]
- 005c0b8c bytes ac0c0094
+ 005c0bcc bytes ac0c0094
- 005c0ba0 ["INT_ADD", "register:40f0:8", ["const:5c0ba0:8", "const:4:8"]]
- 005c0ba0 ["CALL", null, ["callee:00480118:8"]]
+ 005c0be0 ["INT_ADD", "register:40f0:8", ["const:5c0be0:8", "const:4:8"]]
+ 005c0be0 ["CALL", null, ["callee:00480118:8"]]
- 005c0ba0 bytes 4efdfa97
+ 005c0be0 bytes 4efdfa97
- 005c0bd8 ["INT_ADD", "register:40f0:8", ["const:5c0bd8:8", "const:4:8"]]
- 005c0bd8 ["CALL", null, ["callee:00480118:8"]]
+ 005c0c18 ["INT_ADD", "register:40f0:8", ["const:5c0c18:8", "const:4:8"]]
+ 005c0c18 ["CALL", null, ["callee:00480118:8"]]
- 005c0bd8 bytes 40fdfa97
+ 005c0c18 bytes 40fdfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9c5a3c6436f9a747b0c0bf388daa65a"></a>

### [`005c0d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md) → [`005c0dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0dc4.md) FUN_005c0dc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c0dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md#insn-005c0dac) · [`005c0de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md#insn-005c0de4) · [`005c0df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md#insn-005c0df8)
- 新版 `005c0dec`（命令位置の公開資料なし） · `005c0e24`（命令位置の公開資料なし） · `005c0e38`（命令位置の公開資料なし）

~~~diff
- 005c0dac ["INT_ADD", "register:40f0:8", ["const:5c0dac:8", "const:4:8"]]
- 005c0dac ["CALL", null, ["callee:00480b38:8"]]
+ 005c0dec ["INT_ADD", "register:40f0:8", ["const:5c0dec:8", "const:4:8"]]
+ 005c0dec ["CALL", null, ["callee:00480b38:8"]]
- 005c0dac bytes 53fffa97
+ 005c0dec bytes 53fffa97
- 005c0de4 ["INT_ADD", "register:40f0:8", ["const:5c0de4:8", "const:4:8"]]
- 005c0de4 ["CALL", null, ["callee:00480b38:8"]]
+ 005c0e24 ["INT_ADD", "register:40f0:8", ["const:5c0e24:8", "const:4:8"]]
+ 005c0e24 ["CALL", null, ["callee:00480b38:8"]]
- 005c0de4 bytes 45fffa97
+ 005c0e24 bytes 45fffa97
- 005c0df8 ["INT_ADD", "register:40f0:8", ["const:5c0df8:8", "const:4:8"]]
- 005c0df8 ["CALL", null, ["callee:00480b38:8"]]
+ 005c0e38 ["INT_ADD", "register:40f0:8", ["const:5c0e38:8", "const:4:8"]]
+ 005c0e38 ["CALL", null, ["callee:00480b38:8"]]
- 005c0df8 bytes 40fffa97
+ 005c0e38 bytes 40fffa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77a23837e3422b4364539e5dbbb4c23f"></a>

### [`005c0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md) → [`005c0e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0e8c.md) FUN_005c0e8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005c1310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1310.md) [`00743d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743d50.md)
- 新版 呼出元 1件 [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005c1350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1350.md) [`00743d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c0f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md#insn-005c0f00) · [`005c0fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md#insn-005c0fb0) · [`005c0fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md#insn-005c0fd8)
- 新版 `005c0f40`（命令位置の公開資料なし） · `005c0ff0`（命令位置の公開資料なし） · `005c1018`（命令位置の公開資料なし）

~~~diff
- 005c0f00 ["INT_ADD", "register:40f0:8", ["const:5c0f00:8", "const:4:8"]]
- 005c0f00 ["CALL", null, ["callee:008514f8:8"]]
+ 005c0f40 ["INT_ADD", "register:40f0:8", ["const:5c0f40:8", "const:4:8"]]
+ 005c0f40 ["CALL", null, ["callee:008514f8:8"]]
- 005c0f00 bytes 6e410a94
+ 005c0f40 bytes 6e410a94
- 005c0fb0 ["INT_ADD", "register:40f0:8", ["const:5c0fb0:8", "const:4:8"]]
- 005c0fb0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005c0ff0 ["INT_ADD", "register:40f0:8", ["const:5c0ff0:8", "const:4:8"]]
+ 005c0ff0 ["CALL", null, ["callee:00c57e90:8"]]
- 005c0fb0 bytes b85a1a94
+ 005c0ff0 bytes a85b1a94
- 005c0fd8 ["INT_ADD", "register:40f0:8", ["const:5c0fd8:8", "const:4:8"]]
- 005c0fd8 ["CALL", null, ["callee:00c58000:8"]]
+ 005c1018 ["INT_ADD", "register:40f0:8", ["const:5c1018:8", "const:4:8"]]
+ 005c1018 ["CALL", null, ["callee:00c58000:8"]]
- 005c0fd8 bytes 0a5b1a94
+ 005c1018 bytes fa5b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9c0bd2577d94c60629d7524ccdac15f"></a>

### [`005c1310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1310.md) → [`005c1350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1350.md) FUN_005c1350

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005c0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005c0e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0e8c.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) [`00aec960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec960.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c1394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1310.md#insn-005c1394) · [`005c13d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1310.md#insn-005c13d0) · [`005c142c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1310.md#insn-005c142c)
- 新版 `005c13d4`（命令位置の公開資料なし） · `005c1410`（命令位置の公開資料なし） · `005c146c`（命令位置の公開資料なし）

~~~diff
- 005c1394 ["INT_ADD", "register:40f0:8", ["const:5c1394:8", "const:4:8"]]
- 005c1394 ["CALL", null, ["callee:00c57e90:8"]]
+ 005c13d4 ["INT_ADD", "register:40f0:8", ["const:5c13d4:8", "const:4:8"]]
+ 005c13d4 ["CALL", null, ["callee:00c57e90:8"]]
- 005c1394 bytes bf591a94
+ 005c13d4 bytes af5a1a94
- 005c13d0 ["INT_ADD", "register:40f0:8", ["const:5c13d0:8", "const:4:8"]]
- 005c13d0 ["CALL", null, ["callee:0043bba4:8"]]
+ 005c1410 ["INT_ADD", "register:40f0:8", ["const:5c1410:8", "const:4:8"]]
+ 005c1410 ["CALL", null, ["callee:0043bba4:8"]]
- 005c13d0 bytes e5e9f997
+ 005c1410 bytes e5e9f997
- 005c142c ["INT_ADD", "register:40f0:8", ["const:5c142c:8", "const:4:8"]]
- 005c142c ["CALL", null, ["callee:00c57e90:8"]]
+ 005c146c ["INT_ADD", "register:40f0:8", ["const:5c146c:8", "const:4:8"]]
+ 005c146c ["CALL", null, ["callee:00c57e90:8"]]
- 005c142c bytes 99591a94
+ 005c146c bytes 895a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd3cabb633fe73b4a034f048aab5abc7"></a>

### [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) → [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) FUN_005c179c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 154件 [`005bb6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb6b8.md) [`005bc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md) [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 155件 [`005bb6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb6f8.md) [`005bc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc518.md) [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c177c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md#insn-005c177c) · [`005c1788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md#insn-005c1788)
- 新版 `005c17bc`（命令位置の公開資料なし） · `005c17c8`（命令位置の公開資料なし）

~~~diff
- 005c177c ["INT_ADD", "register:40f0:8", ["const:5c177c:8", "const:4:8"]]
- 005c177c ["CALL", null, ["local:b0:8"]]
+ 005c17bc ["INT_ADD", "register:40f0:8", ["const:5c17bc:8", "const:4:8"]]
+ 005c17bc ["CALL", null, ["local:b0:8"]]
- 005c177c bytes f8ffff97
+ 005c17bc bytes f8ffff97
- 005c1788 ["INT_ADD", "register:40f0:8", ["const:5c1788:8", "const:4:8"]]
- 005c1788 ["CALL", null, ["local:b0:8"]]
+ 005c17c8 ["INT_ADD", "register:40f0:8", ["const:5c17c8:8", "const:4:8"]]
+ 005c17c8 ["CALL", null, ["local:b0:8"]]
- 005c1788 bytes f5ffff97
+ 005c17c8 bytes f5ffff97
~~~


<a id="compare-a41c9cb4712b4541aee8cbee7653898f"></a>

### [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) → [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) FUN_005c17e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 15件 [`005bb344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb344.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 15件 [`005bb384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb384.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c17c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md#insn-005c17c0) · [`005c17cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md#insn-005c17cc) · [`005c17d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md#insn-005c17d8)
- 新版 `005c1800`（命令位置の公開資料なし） · `005c180c`（命令位置の公開資料なし） · `005c1818`（命令位置の公開資料なし）

~~~diff
- 005c17c0 ["INT_ADD", "register:40f0:8", ["const:5c17c0:8", "const:4:8"]]
- 005c17c0 ["CALL", null, ["local:b0:8"]]
+ 005c1800 ["INT_ADD", "register:40f0:8", ["const:5c1800:8", "const:4:8"]]
+ 005c1800 ["CALL", null, ["local:b0:8"]]
- 005c17c0 bytes f8ffff97
+ 005c1800 bytes f8ffff97
- 005c17cc ["INT_ADD", "register:40f0:8", ["const:5c17cc:8", "const:4:8"]]
- 005c17cc ["CALL", null, ["local:b0:8"]]
+ 005c180c ["INT_ADD", "register:40f0:8", ["const:5c180c:8", "const:4:8"]]
+ 005c180c ["CALL", null, ["local:b0:8"]]
- 005c17cc bytes f5ffff97
+ 005c180c bytes f5ffff97
- 005c17d8 ["INT_ADD", "register:40f0:8", ["const:5c17d8:8", "const:4:8"]]
- 005c17d8 ["CALL", null, ["callee:005c179c:8"]]
+ 005c1818 ["INT_ADD", "register:40f0:8", ["const:5c1818:8", "const:4:8"]]
+ 005c1818 ["CALL", null, ["callee:005c179c:8"]]
- 005c17d8 bytes e1ffff97
+ 005c1818 bytes e1ffff97
~~~


<a id="compare-dea19ffd5a2a965b1e1092b09217d52c"></a>

### [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) → [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) FUN_005c1bf0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00675b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b08.md) [`00675b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b54.md) [`00734260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) · 呼出先 2件 [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 19件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00675b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b48.md) [`00675b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b94.md) [`007342a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) · 呼出先 2件 [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c1bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md#insn-005c1bd0) · [`005c1bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md#insn-005c1bdc)
- 新版 `005c1c10`（命令位置の公開資料なし） · `005c1c1c`（命令位置の公開資料なし）

~~~diff
- 005c1bd0 ["INT_ADD", "register:40f0:8", ["const:5c1bd0:8", "const:4:8"]]
- 005c1bd0 ["CALL", null, ["local:b0:8"]]
+ 005c1c10 ["INT_ADD", "register:40f0:8", ["const:5c1c10:8", "const:4:8"]]
+ 005c1c10 ["CALL", null, ["local:b0:8"]]
- 005c1bd0 bytes f8ffff97
+ 005c1c10 bytes f8ffff97
- 005c1bdc ["INT_ADD", "register:40f0:8", ["const:5c1bdc:8", "const:4:8"]]
- 005c1bdc ["CALL", null, ["local:b0:8"]]
+ 005c1c1c ["INT_ADD", "register:40f0:8", ["const:5c1c1c:8", "const:4:8"]]
+ 005c1c1c ["CALL", null, ["local:b0:8"]]
- 005c1bdc bytes f5ffff97
+ 005c1c1c bytes f5ffff97
~~~


<a id="compare-9871b1ccac1dd006913d03cdc1d43099"></a>

### [`005c1bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bf4.md) → [`005c1c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1c34.md) FUN_005c1c34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c1bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bf4.md) · 呼出先 2件 [`005c1bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bf4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c1c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1c34.md) · 呼出先 2件 [`005c1c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1c34.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c1c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bf4.md#insn-005c1c10) · [`005c1c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bf4.md#insn-005c1c1c) · [`005c1c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bf4.md#insn-005c1c2c)
- 新版 `005c1c50`（命令位置の公開資料なし） · `005c1c5c`（命令位置の公開資料なし） · `005c1c6c`（命令位置の公開資料なし）

~~~diff
- 005c1c10 ["INT_ADD", "register:40f0:8", ["const:5c1c10:8", "const:4:8"]]
- 005c1c10 ["CALL", null, ["local:b0:8"]]
+ 005c1c50 ["INT_ADD", "register:40f0:8", ["const:5c1c50:8", "const:4:8"]]
+ 005c1c50 ["CALL", null, ["local:b0:8"]]
- 005c1c10 bytes f9ffff97
+ 005c1c50 bytes f9ffff97
- 005c1c1c ["INT_ADD", "register:40f0:8", ["const:5c1c1c:8", "const:4:8"]]
- 005c1c1c ["CALL", null, ["local:b0:8"]]
+ 005c1c5c ["INT_ADD", "register:40f0:8", ["const:5c1c5c:8", "const:4:8"]]
+ 005c1c5c ["CALL", null, ["local:b0:8"]]
- 005c1c1c bytes f6ffff97
+ 005c1c5c bytes f6ffff97
- 005c1c2c ["INT_ADD", "register:40f0:8", ["const:5c1c2c:8", "const:4:8"]]
- 005c1c2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005c1c6c ["INT_ADD", "register:40f0:8", ["const:5c1c6c:8", "const:4:8"]]
+ 005c1c6c ["CALL", null, ["callee:00c57eb0:8"]]
- 005c1c2c bytes a1571a94
+ 005c1c6c bytes 91581a94
~~~


<a id="compare-065e56726d653a3902cca20304d47dab"></a>

### [`005c1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md) → [`005c1c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1c84.md) FUN_005c1c84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md) · 呼出先 2件 [`005c1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c1c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1c84.md) · 呼出先 2件 [`005c1c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1c84.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c1c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md#insn-005c1c64) · [`005c1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md#insn-005c1c70)
- 新版 `005c1ca4`（命令位置の公開資料なし） · `005c1cb0`（命令位置の公開資料なし）

~~~diff
- 005c1c64 ["INT_ADD", "register:40f0:8", ["const:5c1c64:8", "const:4:8"]]
- 005c1c64 ["CALL", null, ["local:b0:8"]]
+ 005c1ca4 ["INT_ADD", "register:40f0:8", ["const:5c1ca4:8", "const:4:8"]]
+ 005c1ca4 ["CALL", null, ["local:b0:8"]]
- 005c1c64 bytes f8ffff97
+ 005c1ca4 bytes f8ffff97
- 005c1c70 ["INT_ADD", "register:40f0:8", ["const:5c1c70:8", "const:4:8"]]
- 005c1c70 ["CALL", null, ["local:b0:8"]]
+ 005c1cb0 ["INT_ADD", "register:40f0:8", ["const:5c1cb0:8", "const:4:8"]]
+ 005c1cb0 ["CALL", null, ["local:b0:8"]]
- 005c1c70 bytes f5ffff97
+ 005c1cb0 bytes f5ffff97
~~~


<a id="compare-29a06d330b4137ecf5238bc76126c4a8"></a>

### [`005c1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md) → [`005c1cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1cf0.md) FUN_005c1cf0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md) · 呼出先 5件 [`005c1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md) [`005c2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2550.md) [`005c2674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md) [`005c28cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c1cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1cf0.md) · 呼出先 5件 [`005c1cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1cf0.md) [`005c2590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2590.md) [`005c26b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c26b4.md) [`005c290c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c290c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c1d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md#insn-005c1d78) · [`005c1d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md#insn-005c1d9c) · [`005c1dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md#insn-005c1dac)
- 新版 `005c1db8`（命令位置の公開資料なし） · `005c1ddc`（命令位置の公開資料なし） · `005c1dec`（命令位置の公開資料なし）

~~~diff
- 005c1d78 ["INT_ADD", "register:40f0:8", ["const:5c1d78:8", "const:4:8"]]
- 005c1d78 ["CALL", null, ["callee:005c2590:8"]]
+ 005c1db8 ["INT_ADD", "register:40f0:8", ["const:5c1db8:8", "const:4:8"]]
+ 005c1db8 ["CALL", null, ["callee:005c2590:8"]]
- 005c1d78 bytes f6010094
+ 005c1db8 bytes f6010094
- 005c1d9c ["INT_ADD", "register:40f0:8", ["const:5c1d9c:8", "const:4:8"]]
- 005c1d9c ["CALL", null, ["callee:005c2590:8"]]
+ 005c1ddc ["INT_ADD", "register:40f0:8", ["const:5c1ddc:8", "const:4:8"]]
+ 005c1ddc ["CALL", null, ["callee:005c2590:8"]]
- 005c1d9c bytes ed010094
+ 005c1ddc bytes ed010094
- 005c1dac ["INT_ADD", "register:40f0:8", ["const:5c1dac:8", "const:4:8"]]
- 005c1dac ["CALL", null, ["callee:005c2590:8"]]
+ 005c1dec ["INT_ADD", "register:40f0:8", ["const:5c1dec:8", "const:4:8"]]
+ 005c1dec ["CALL", null, ["callee:005c2590:8"]]
- 005c1dac bytes e9010094
+ 005c1dec bytes e9010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-341072cfe72fe27704e0f341b7ac8132"></a>

### [`005c2674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md) → [`005c26b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c26b4.md) FUN_005c26b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005c1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md) · 呼出先 2件 [`005c2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2550.md) [`005c28cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md)
- 新版 呼出元 1件 [`005c1cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1cf0.md) · 呼出先 2件 [`005c2590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2590.md) [`005c290c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c290c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md#insn-005c271c) · [`005c27dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md#insn-005c27dc) · [`005c27f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md#insn-005c27f8)
- 新版 `005c275c`（命令位置の公開資料なし） · `005c281c`（命令位置の公開資料なし） · `005c2838`（命令位置の公開資料なし）

~~~diff
- 005c271c ["INT_ADD", "register:40f0:8", ["const:5c271c:8", "const:4:8"]]
- 005c271c ["CALL", null, ["callee:005c290c:8"]]
+ 005c275c ["INT_ADD", "register:40f0:8", ["const:5c275c:8", "const:4:8"]]
+ 005c275c ["CALL", null, ["callee:005c290c:8"]]
- 005c271c bytes 6c000094
+ 005c275c bytes 6c000094
- 005c27dc ["INT_ADD", "register:40f0:8", ["const:5c27dc:8", "const:4:8"]]
- 005c27dc ["CALL", null, ["callee:005c2590:8"]]
+ 005c281c ["INT_ADD", "register:40f0:8", ["const:5c281c:8", "const:4:8"]]
+ 005c281c ["CALL", null, ["callee:005c2590:8"]]
- 005c27dc bytes 5dffff97
+ 005c281c bytes 5dffff97
- 005c27f8 ["INT_ADD", "register:40f0:8", ["const:5c27f8:8", "const:4:8"]]
- 005c27f8 ["CALL", null, ["callee:005c2590:8"]]
+ 005c2838 ["INT_ADD", "register:40f0:8", ["const:5c2838:8", "const:4:8"]]
+ 005c2838 ["CALL", null, ["callee:005c2590:8"]]
- 005c27f8 bytes 56ffff97
+ 005c2838 bytes 56ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9adcc2c40ad73a856cb31c1ed7291ee"></a>

### [`005c28cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md) → [`005c290c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c290c.md) FUN_005c290c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005c1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md) [`005c2674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md) · 呼出先 1件 [`005c2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2550.md)
- 新版 呼出元 2件 [`005c1cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1cf0.md) [`005c26b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c26b4.md) · 呼出先 1件 [`005c2590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c28ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md#insn-005c28ec)
- 新版 `005c292c`（命令位置の公開資料なし）

~~~diff
- 005c28ec ["INT_ADD", "register:40f0:8", ["const:5c28ec:8", "const:4:8"]]
- 005c28ec ["CALL", null, ["callee:005c2590:8"]]
+ 005c292c ["INT_ADD", "register:40f0:8", ["const:5c292c:8", "const:4:8"]]
+ 005c292c ["CALL", null, ["callee:005c2590:8"]]
- 005c28ec bytes 19ffff97
+ 005c292c bytes 19ffff97
~~~


<a id="compare-a07f7861ec3962bd68931ad1291c37b4"></a>

### [`005c29c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c29c0.md) → [`005c2a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a00.md) FUN_005c2a00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c29c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c29c0.md) · 呼出先 2件 [`005c29c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c29c0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c2a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a00.md) · 呼出先 2件 [`005c2a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c29dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c29c0.md#insn-005c29dc) · [`005c29e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c29c0.md#insn-005c29e8) · [`005c29f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c29c0.md#insn-005c29f8)
- 新版 `005c2a1c`（命令位置の公開資料なし） · `005c2a28`（命令位置の公開資料なし） · `005c2a38`（命令位置の公開資料なし）

~~~diff
- 005c29dc ["INT_ADD", "register:40f0:8", ["const:5c29dc:8", "const:4:8"]]
- 005c29dc ["CALL", null, ["local:b0:8"]]
+ 005c2a1c ["INT_ADD", "register:40f0:8", ["const:5c2a1c:8", "const:4:8"]]
+ 005c2a1c ["CALL", null, ["local:b0:8"]]
- 005c29dc bytes f9ffff97
+ 005c2a1c bytes f9ffff97
- 005c29e8 ["INT_ADD", "register:40f0:8", ["const:5c29e8:8", "const:4:8"]]
- 005c29e8 ["CALL", null, ["local:b0:8"]]
+ 005c2a28 ["INT_ADD", "register:40f0:8", ["const:5c2a28:8", "const:4:8"]]
+ 005c2a28 ["CALL", null, ["local:b0:8"]]
- 005c29e8 bytes f6ffff97
+ 005c2a28 bytes f6ffff97
- 005c29f8 ["INT_ADD", "register:40f0:8", ["const:5c29f8:8", "const:4:8"]]
- 005c29f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005c2a38 ["INT_ADD", "register:40f0:8", ["const:5c2a38:8", "const:4:8"]]
+ 005c2a38 ["CALL", null, ["callee:00c57eb0:8"]]
- 005c29f8 bytes 2e541a94
+ 005c2a38 bytes 1e551a94
~~~


<a id="compare-0c42c4f5197cd21da95c9dedbc8f56d8"></a>

### [`005c2a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md) → [`005c2a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a50.md) FUN_005c2a50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c2a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md) · 呼出先 2件 [`005c2a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c2a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a50.md) · 呼出先 2件 [`005c2a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c2a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md#insn-005c2a30) · [`005c2a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md#insn-005c2a3c)
- 新版 `005c2a70`（命令位置の公開資料なし） · `005c2a7c`（命令位置の公開資料なし）

~~~diff
- 005c2a30 ["INT_ADD", "register:40f0:8", ["const:5c2a30:8", "const:4:8"]]
- 005c2a30 ["CALL", null, ["local:b0:8"]]
+ 005c2a70 ["INT_ADD", "register:40f0:8", ["const:5c2a70:8", "const:4:8"]]
+ 005c2a70 ["CALL", null, ["local:b0:8"]]
- 005c2a30 bytes f8ffff97
+ 005c2a70 bytes f8ffff97
- 005c2a3c ["INT_ADD", "register:40f0:8", ["const:5c2a3c:8", "const:4:8"]]
- 005c2a3c ["CALL", null, ["local:b0:8"]]
+ 005c2a7c ["INT_ADD", "register:40f0:8", ["const:5c2a7c:8", "const:4:8"]]
+ 005c2a7c ["CALL", null, ["local:b0:8"]]
- 005c2a3c bytes f5ffff97
+ 005c2a7c bytes f5ffff97
~~~


<a id="compare-9acfa517905881d8e695998f93d20f3d"></a>

### [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) → [`005c2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a94.md) FUN_005c2a94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) · 呼出先 7件 [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) [`005c36f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c36f8.md) [`005c38b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md) [`005c3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md) [`005c3cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md)
- 新版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a94.md) · 呼出先 7件 [`005c2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a94.md) [`005c3738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3738.md) [`005c38f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c38f8.md) [`005c3ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3ac4.md) [`005c3d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3d1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c2b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md#insn-005c2b08) · [`005c2b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md#insn-005c2b2c) · [`005c2b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md#insn-005c2b44)
- 新版 `005c2b48`（命令位置の公開資料なし） · `005c2b6c`（命令位置の公開資料なし） · `005c2b84`（命令位置の公開資料なし）

~~~diff
- 005c2b08 ["INT_ADD", "register:40f0:8", ["const:5c2b08:8", "const:4:8"]]
- 005c2b08 ["CALL", null, ["callee:005c38f8:8"]]
+ 005c2b48 ["INT_ADD", "register:40f0:8", ["const:5c2b48:8", "const:4:8"]]
+ 005c2b48 ["CALL", null, ["callee:005c38f8:8"]]
- 005c2b08 bytes 6c030094
+ 005c2b48 bytes 6c030094
- 005c2b2c ["INT_ADD", "register:40f0:8", ["const:5c2b2c:8", "const:4:8"]]
- 005c2b2c ["CALL", null, ["callee:005c38f8:8"]]
+ 005c2b6c ["INT_ADD", "register:40f0:8", ["const:5c2b6c:8", "const:4:8"]]
+ 005c2b6c ["CALL", null, ["callee:005c38f8:8"]]
- 005c2b2c bytes 63030094
+ 005c2b6c bytes 63030094
- 005c2b44 ["INT_ADD", "register:40f0:8", ["const:5c2b44:8", "const:4:8"]]
- 005c2b44 ["CALL", null, ["callee:005c38f8:8"]]
+ 005c2b84 ["INT_ADD", "register:40f0:8", ["const:5c2b84:8", "const:4:8"]]
+ 005c2b84 ["CALL", null, ["callee:005c38f8:8"]]
- 005c2b44 bytes 5d030094
+ 005c2b84 bytes 5d030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6d63807bc380a2e065ed1e6c43f47a"></a>

### [`005c36f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c36f8.md) → [`005c3738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3738.md) FUN_005c3738

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) [`005c3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md) · 呼出先 3件 [`005c3cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md) [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md)
- 新版 呼出元 2件 [`005c2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a94.md) [`005c3ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3ac4.md) · 呼出先 3件 [`005c3d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3d1c.md) [`00664e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e10.md) [`00b00054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c36f8.md#insn-005c372c) · [`005c373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c36f8.md#insn-005c373c) · [`005c3750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c36f8.md#insn-005c3750)
- 新版 `005c376c`（命令位置の公開資料なし） · `005c377c`（命令位置の公開資料なし） · `005c3790`（命令位置の公開資料なし）

~~~diff
- 005c372c ["INT_ADD", "register:40f0:8", ["const:5c372c:8", "const:4:8"]]
- 005c372c ["CALL", null, ["callee:005c3d1c:8"]]
+ 005c376c ["INT_ADD", "register:40f0:8", ["const:5c376c:8", "const:4:8"]]
+ 005c376c ["CALL", null, ["callee:005c3d1c:8"]]
- 005c372c bytes 6c010094
+ 005c376c bytes 6c010094
- 005c373c ["INT_ADD", "register:40f0:8", ["const:5c373c:8", "const:4:8"]]
- 005c373c ["CALL", null, ["callee:00664e10:8"]]
+ 005c377c ["INT_ADD", "register:40f0:8", ["const:5c377c:8", "const:4:8"]]
+ 005c377c ["CALL", null, ["callee:00664e10:8"]]
- 005c373c bytes a5850294
+ 005c377c bytes a5850294
- 005c3750 ["INT_ADD", "register:40f0:8", ["const:5c3750:8", "const:4:8"]]
- 005c3750 ["CALL", null, ["callee:00b00054:8"]]
+ 005c3790 ["INT_ADD", "register:40f0:8", ["const:5c3790:8", "const:4:8"]]
+ 005c3790 ["CALL", null, ["callee:00b00054:8"]]
- 005c3750 bytes 37f11494
+ 005c3790 bytes 31f21494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-889b3f3367dd90298feb27cd93315fea"></a>

### [`005c38b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md) → [`005c38f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c38f8.md) FUN_005c38f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) [`005c3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md) [`005c3cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md) · 呼出先 2件 [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md)
- 新版 呼出元 3件 [`005c2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a94.md) [`005c3ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3ac4.md) [`005c3d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3d1c.md) · 呼出先 2件 [`00664e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e10.md) [`00b00054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c38ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md#insn-005c38ec) · [`005c3900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md#insn-005c3900) · [`005c390c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md#insn-005c390c)
- 新版 `005c392c`（命令位置の公開資料なし） · `005c3940`（命令位置の公開資料なし） · `005c394c`（命令位置の公開資料なし）

~~~diff
- 005c38ec ["INT_ADD", "register:40f0:8", ["const:5c38ec:8", "const:4:8"]]
- 005c38ec ["CALL", null, ["callee:00664e10:8"]]
+ 005c392c ["INT_ADD", "register:40f0:8", ["const:5c392c:8", "const:4:8"]]
+ 005c392c ["CALL", null, ["callee:00664e10:8"]]
- 005c38ec bytes 39850294
+ 005c392c bytes 39850294
- 005c3900 ["INT_ADD", "register:40f0:8", ["const:5c3900:8", "const:4:8"]]
- 005c3900 ["CALL", null, ["callee:00b00054:8"]]
+ 005c3940 ["INT_ADD", "register:40f0:8", ["const:5c3940:8", "const:4:8"]]
+ 005c3940 ["CALL", null, ["callee:00b00054:8"]]
- 005c3900 bytes cbf01494
+ 005c3940 bytes c5f11494
- 005c390c ["INT_ADD", "register:40f0:8", ["const:5c390c:8", "const:4:8"]]
- 005c390c ["CALL", null, ["callee:00664e10:8"]]
+ 005c394c ["INT_ADD", "register:40f0:8", ["const:5c394c:8", "const:4:8"]]
+ 005c394c ["CALL", null, ["callee:00664e10:8"]]
- 005c390c bytes 31850294
+ 005c394c bytes 31850294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01d124b7c851f37dca50880648c45307"></a>

### [`005c3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md) → [`005c3ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3ac4.md) FUN_005c3ac4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) · 呼出先 5件 [`005c36f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c36f8.md) [`005c38b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md) [`005c3cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md) [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md)
- 新版 呼出元 1件 [`005c2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a94.md) · 呼出先 5件 [`005c3738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3738.md) [`005c38f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c38f8.md) [`005c3d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3d1c.md) [`00664e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e10.md) [`00b00054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c3ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md#insn-005c3ad4) · [`005c3ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md#insn-005c3ae8) · [`005c3af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md#insn-005c3af4)
- 新版 `005c3b14`（命令位置の公開資料なし） · `005c3b28`（命令位置の公開資料なし） · `005c3b34`（命令位置の公開資料なし）

~~~diff
- 005c3ad4 ["INT_ADD", "register:40f0:8", ["const:5c3ad4:8", "const:4:8"]]
- 005c3ad4 ["CALL", null, ["callee:00664e10:8"]]
+ 005c3b14 ["INT_ADD", "register:40f0:8", ["const:5c3b14:8", "const:4:8"]]
+ 005c3b14 ["CALL", null, ["callee:00664e10:8"]]
- 005c3ad4 bytes bf840294
+ 005c3b14 bytes bf840294
- 005c3ae8 ["INT_ADD", "register:40f0:8", ["const:5c3ae8:8", "const:4:8"]]
- 005c3ae8 ["CALL", null, ["callee:00b00054:8"]]
+ 005c3b28 ["INT_ADD", "register:40f0:8", ["const:5c3b28:8", "const:4:8"]]
+ 005c3b28 ["CALL", null, ["callee:00b00054:8"]]
- 005c3ae8 bytes 51f01494
+ 005c3b28 bytes 4bf11494
- 005c3af4 ["INT_ADD", "register:40f0:8", ["const:5c3af4:8", "const:4:8"]]
- 005c3af4 ["CALL", null, ["callee:00664e10:8"]]
+ 005c3b34 ["INT_ADD", "register:40f0:8", ["const:5c3b34:8", "const:4:8"]]
+ 005c3b34 ["CALL", null, ["callee:00664e10:8"]]
- 005c3af4 bytes b7840294
+ 005c3b34 bytes b7840294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236f8c743a77412139e222e79a0fbf0e"></a>

### [`005c3cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md) → [`005c3d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3d1c.md) FUN_005c3d1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) [`005c36f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c36f8.md) [`005c3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md) · 呼出先 3件 [`005c38b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md) [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md)
- 新版 呼出元 3件 [`005c2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c2/005c2a94.md) [`005c3738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3738.md) [`005c3ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3ac4.md) · 呼出先 3件 [`005c38f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c38f8.md) [`00664e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e10.md) [`00b00054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c3d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md#insn-005c3d0c) · [`005c3d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md#insn-005c3d1c) · [`005c3d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md#insn-005c3d30)
- 新版 `005c3d4c`（命令位置の公開資料なし） · `005c3d5c`（命令位置の公開資料なし） · `005c3d70`（命令位置の公開資料なし）

~~~diff
- 005c3d0c ["INT_ADD", "register:40f0:8", ["const:5c3d0c:8", "const:4:8"]]
- 005c3d0c ["CALL", null, ["callee:005c38f8:8"]]
+ 005c3d4c ["INT_ADD", "register:40f0:8", ["const:5c3d4c:8", "const:4:8"]]
+ 005c3d4c ["CALL", null, ["callee:005c38f8:8"]]
- 005c3d0c bytes ebfeff97
+ 005c3d4c bytes ebfeff97
- 005c3d1c ["INT_ADD", "register:40f0:8", ["const:5c3d1c:8", "const:4:8"]]
- 005c3d1c ["CALL", null, ["callee:00664e10:8"]]
+ 005c3d5c ["INT_ADD", "register:40f0:8", ["const:5c3d5c:8", "const:4:8"]]
+ 005c3d5c ["CALL", null, ["callee:00664e10:8"]]
- 005c3d1c bytes 2d840294
+ 005c3d5c bytes 2d840294
- 005c3d30 ["INT_ADD", "register:40f0:8", ["const:5c3d30:8", "const:4:8"]]
- 005c3d30 ["CALL", null, ["callee:00b00054:8"]]
+ 005c3d70 ["INT_ADD", "register:40f0:8", ["const:5c3d70:8", "const:4:8"]]
+ 005c3d70 ["CALL", null, ["callee:00b00054:8"]]
- 005c3d30 bytes bfef1494
+ 005c3d70 bytes b9f01494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b41e6f6fd91ae06a7dafb4106b81c5d6"></a>

### [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) → [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) FUN_005c3e7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`005c0b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b24.md) [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`005c62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md) [`0063dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md) · 呼出先 2件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 54件 [`005c0b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b64.md) [`005c0b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b98.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`005c6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6300.md) [`0063dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063dd10.md) · 呼出先 2件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c3e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md#insn-005c3e58) · [`005c3e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md#insn-005c3e64) · [`005c3e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md#insn-005c3e74)
- 新版 `005c3e98`（命令位置の公開資料なし） · `005c3ea4`（命令位置の公開資料なし） · `005c3eb4`（命令位置の公開資料なし）

~~~diff
- 005c3e58 ["INT_ADD", "register:40f0:8", ["const:5c3e58:8", "const:4:8"]]
- 005c3e58 ["CALL", null, ["local:b0:8"]]
+ 005c3e98 ["INT_ADD", "register:40f0:8", ["const:5c3e98:8", "const:4:8"]]
+ 005c3e98 ["CALL", null, ["local:b0:8"]]
- 005c3e58 bytes f9ffff97
+ 005c3e98 bytes f9ffff97
- 005c3e64 ["INT_ADD", "register:40f0:8", ["const:5c3e64:8", "const:4:8"]]
- 005c3e64 ["CALL", null, ["local:b0:8"]]
+ 005c3ea4 ["INT_ADD", "register:40f0:8", ["const:5c3ea4:8", "const:4:8"]]
+ 005c3ea4 ["CALL", null, ["local:b0:8"]]
- 005c3e64 bytes f6ffff97
+ 005c3ea4 bytes f6ffff97
- 005c3e74 ["INT_ADD", "register:40f0:8", ["const:5c3e74:8", "const:4:8"]]
- 005c3e74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005c3eb4 ["INT_ADD", "register:40f0:8", ["const:5c3eb4:8", "const:4:8"]]
+ 005c3eb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005c3e74 bytes 0f4f1a94
+ 005c3eb4 bytes ff4f1a94
~~~


<a id="compare-2d00f097f0283edbc5ae6f41885e47ca"></a>

### [`005c61ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c61ec.md) → [`005c622c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c622c.md) FUN_005c622c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00adf01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00adf/00adf01c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00adf218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00adf/00adf218.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c6254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c61ec.md#insn-005c6254) · [`005c6298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c61ec.md#insn-005c6298)
- 新版 `005c6294`（命令位置の公開資料なし） · `005c62d8`（命令位置の公開資料なし）

~~~diff
- 005c6254 ["INT_ADD", "register:40f0:8", ["const:5c6254:8", "const:4:8"]]
- 005c6254 ["CALL", null, ["callee:00c57e90:8"]]
+ 005c6294 ["INT_ADD", "register:40f0:8", ["const:5c6294:8", "const:4:8"]]
+ 005c6294 ["CALL", null, ["callee:00c57e90:8"]]
- 005c6254 bytes 0f461a94
+ 005c6294 bytes ff461a94
- 005c6298 ["INT_ADD", "register:40f0:8", ["const:5c6298:8", "const:4:8"]]
- 005c6298 ["CALL", null, ["callee:0043bba4:8"]]
+ 005c62d8 ["INT_ADD", "register:40f0:8", ["const:5c62d8:8", "const:4:8"]]
+ 005c62d8 ["CALL", null, ["callee:0043bba4:8"]]
- 005c6298 bytes 33d6f997
+ 005c62d8 bytes 33d6f997
~~~


<a id="compare-2ba05fa9f4e3fa02100f2854a36eff29"></a>

### [`005c75b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c75b8.md) → [`005c75f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c75f8.md) FUN_005c75f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`00b3d1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3d1f0.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0060a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060a/0060a8a0.md) [`00b3d618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3d/00b3d618.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c7620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c75b8.md#insn-005c7620) · [`005c7654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c75b8.md#insn-005c7654)
- 新版 `005c7660`（命令位置の公開資料なし） · `005c7694`（命令位置の公開資料なし）

~~~diff
- 005c7620 ["INT_ADD", "register:40f0:8", ["const:5c7620:8", "const:4:8"]]
- 005c7620 ["CALL", null, ["callee:00c57e90:8"]]
+ 005c7660 ["INT_ADD", "register:40f0:8", ["const:5c7660:8", "const:4:8"]]
+ 005c7660 ["CALL", null, ["callee:00c57e90:8"]]
- 005c7620 bytes 1c411a94
+ 005c7660 bytes 0c421a94
- 005c7654 ["INT_ADD", "register:40f0:8", ["const:5c7654:8", "const:4:8"]]
- 005c7654 ["CALL", null, ["callee:0043bba4:8"]]
+ 005c7694 ["INT_ADD", "register:40f0:8", ["const:5c7694:8", "const:4:8"]]
+ 005c7694 ["CALL", null, ["callee:0043bba4:8"]]
- 005c7654 bytes 44d1f997
+ 005c7694 bytes 44d1f997
~~~


<a id="compare-ef9b8c501d28bbbbf6dc10f2e419da03"></a>

### [`005c84b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c84b4.md) → [`005c84f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c84f4.md) FUN_005c84f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c84d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c84b4.md#insn-005c84d0) · [`005c84e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c84b4.md#insn-005c84e4) · [`005c84f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c84b4.md#insn-005c84f8)
- 新版 `005c8510`（命令位置の公開資料なし） · `005c8524`（命令位置の公開資料なし） · `005c8538`（命令位置の公開資料なし）

~~~diff
- 005c84d0 ["INT_ADD", "register:40f0:8", ["const:5c84d0:8", "const:4:8"]]
- 005c84d0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005c8510 ["INT_ADD", "register:40f0:8", ["const:5c8510:8", "const:4:8"]]
+ 005c8510 ["CALL", null, ["callee:00c57eb0:8"]]
- 005c84d0 bytes 783d1a94
+ 005c8510 bytes 683e1a94
- 005c84e4 ["INT_ADD", "register:40f0:8", ["const:5c84e4:8", "const:4:8"]]
- 005c84e4 ["CALL", null, ["callee:00c53d00:8"]]
+ 005c8524 ["INT_ADD", "register:40f0:8", ["const:5c8524:8", "const:4:8"]]
+ 005c8524 ["CALL", null, ["callee:00c53d00:8"]]
- 005c84e4 bytes ff2c1a94
+ 005c8524 bytes f72d1a94
- 005c84f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005c84f8 ["INT_ADD", "register:40f0:8", ["const:5c84f8:8", "const:4:8"]]
- 005c84f8 ["CALLIND", null, ["register:0:8"]]
+ 005c8538 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005c8538 ["INT_ADD", "register:40f0:8", ["const:5c8538:8", "const:4:8"]]
+ 005c8538 ["CALLIND", null, ["register:0:8"]]
- 005c84f8 bytes 00013fd6
+ 005c8538 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fc0eb08489202afec7927c72422d367"></a>

### [`005cc960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc960.md) → [`005cc9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc9a0.md) FUN_005cc9a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006a6fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6fcc.md) [`00922c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/00922c2c.md) [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) [`00962d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00962/00962d80.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005cc6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc6a4.md) [`005ccac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005ccac8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 6件 [`006a700c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a700c.md) [`00922dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922dc8.md) [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) [`00962f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00962/00962f1c.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005cc6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc6e4.md) [`005ccb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccb08.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cc994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc960.md#insn-005cc994) · [`005cca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc960.md#insn-005cca04) · [`005cca30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc960.md#insn-005cca30)
- 新版 `005cc9d4`（命令位置の公開資料なし） · `005cca44`（命令位置の公開資料なし） · `005cca70`（命令位置の公開資料なし）

~~~diff
- 005cc994 ["INT_ADD", "register:40f0:8", ["const:5cc994:8", "const:4:8"]]
- 005cc994 ["CALL", null, ["callee:005cc6e4:8"]]
+ 005cc9d4 ["INT_ADD", "register:40f0:8", ["const:5cc9d4:8", "const:4:8"]]
+ 005cc9d4 ["CALL", null, ["callee:005cc6e4:8"]]
- 005cc994 bytes 44ffff97
+ 005cc9d4 bytes 44ffff97
- 005cca04 ["INT_ADD", "register:40f0:8", ["const:5cca04:8", "const:4:8"]]
- 005cca04 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cca44 ["INT_ADD", "register:40f0:8", ["const:5cca44:8", "const:4:8"]]
+ 005cca44 ["CALL", null, ["callee:00c57e90:8"]]
- 005cca04 bytes 232c1a94
+ 005cca44 bytes 132d1a94
- 005cca30 ["INT_ADD", "register:40f0:8", ["const:5cca30:8", "const:4:8"]]
- 005cca30 ["CALL", null, ["callee:00c58000:8"]]
+ 005cca70 ["INT_ADD", "register:40f0:8", ["const:5cca70:8", "const:4:8"]]
+ 005cca70 ["CALL", null, ["callee:00c58000:8"]]
- 005cca30 bytes 742c1a94
+ 005cca70 bytes 642d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20a7e572c8f8bf4c9b793407a7d5bc32"></a>

### [`005ccac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005ccac8.md) → [`005ccb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccb08.md) FUN_005ccb08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005cc960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc960.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005dc2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc2c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`005cc9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc9a0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005dc300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dc/005dc300.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ccb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005ccac8.md#insn-005ccb6c) · [`005ccbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005ccac8.md#insn-005ccbe0) · [`005ccc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005ccac8.md#insn-005ccc08)
- 新版 `005ccbac`（命令位置の公開資料なし） · `005ccc20`（命令位置の公開資料なし） · `005ccc48`（命令位置の公開資料なし）

~~~diff
- 005ccb6c ["INT_ADD", "register:40f0:8", ["const:5ccb6c:8", "const:4:8"]]
- 005ccb6c ["CALL", null, ["callee:00c57e90:8"]]
+ 005ccbac ["INT_ADD", "register:40f0:8", ["const:5ccbac:8", "const:4:8"]]
+ 005ccbac ["CALL", null, ["callee:00c57e90:8"]]
- 005ccb6c bytes c92b1a94
+ 005ccbac bytes b92c1a94
- 005ccbe0 ["INT_ADD", "register:40f0:8", ["const:5ccbe0:8", "const:4:8"]]
- 005ccbe0 ["CALL", null, ["callee:00c57f40:8"]]
+ 005ccc20 ["INT_ADD", "register:40f0:8", ["const:5ccc20:8", "const:4:8"]]
+ 005ccc20 ["CALL", null, ["callee:00c57f40:8"]]
- 005ccbe0 bytes d82b1a94
+ 005ccc20 bytes c82c1a94
- 005ccc08 ["INT_ADD", "register:40f0:8", ["const:5ccc08:8", "const:4:8"]]
- 005ccc08 ["CALL", null, ["callee:00c57e90:8"]]
+ 005ccc48 ["INT_ADD", "register:40f0:8", ["const:5ccc48:8", "const:4:8"]]
+ 005ccc48 ["CALL", null, ["callee:00c57e90:8"]]
- 005ccc08 bytes a22b1a94
+ 005ccc48 bytes 922c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cff88b25a4594a3cb1f16c1d0e912c4"></a>

### [`005cd4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd4d8.md) → [`005cd518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd518.md) FUN_005cd518

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005cccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md) [`005db448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db448.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 2件 [`005ccd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccd04.md) [`005db488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005db488.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cd4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd4d8.md#insn-005cd4fc) · [`005cd544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd4d8.md#insn-005cd544) · [`005cd564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd4d8.md#insn-005cd564)
- 新版 `005cd53c`（命令位置の公開資料なし） · `005cd584`（命令位置の公開資料なし） · `005cd5a4`（命令位置の公開資料なし）

~~~diff
- 005cd4fc ["INT_ADD", "register:40f0:8", ["const:5cd4fc:8", "const:4:8"]]
- 005cd4fc ["CALL", null, ["callee:00c57fe0:8"]]
+ 005cd53c ["INT_ADD", "register:40f0:8", ["const:5cd53c:8", "const:4:8"]]
+ 005cd53c ["CALL", null, ["callee:00c57fe0:8"]]
- 005cd4fc bytes b9291a94
+ 005cd53c bytes a92a1a94
- 005cd544 ["INT_ADD", "register:40f0:8", ["const:5cd544:8", "const:4:8"]]
- 005cd544 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cd584 ["INT_ADD", "register:40f0:8", ["const:5cd584:8", "const:4:8"]]
+ 005cd584 ["CALL", null, ["callee:00c57e90:8"]]
- 005cd544 bytes 53291a94
+ 005cd584 bytes 432a1a94
- 005cd564 ["INT_ADD", "register:40f0:8", ["const:5cd564:8", "const:4:8"]]
- 005cd564 ["CALL", null, ["callee:00c57f40:8"]]
+ 005cd5a4 ["INT_ADD", "register:40f0:8", ["const:5cd5a4:8", "const:4:8"]]
+ 005cd5a4 ["CALL", null, ["callee:00c57f40:8"]]
- 005cd564 bytes 77291a94
+ 005cd5a4 bytes 672a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da247d60686ed7ebb976196a19a8f76f"></a>

### [`005cd6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md) → [`005cd718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd718.md) FUN_005cd718

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cd6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md#insn-005cd6f8) · [`005cd70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md#insn-005cd70c) · [`005cd714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md#insn-005cd714)
- 新版 `005cd738`（命令位置の公開資料なし） · `005cd74c`（命令位置の公開資料なし） · `005cd754`（命令位置の公開資料なし）

~~~diff
- 005cd6f8 ["INT_ADD", "register:40f0:8", ["const:5cd6f8:8", "const:4:8"]]
- 005cd6f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 005cd738 ["INT_ADD", "register:40f0:8", ["const:5cd738:8", "const:4:8"]]
+ 005cd738 ["CALL", null, ["callee:00c53d00:8"]]
- 005cd6f8 bytes 7a181a94
+ 005cd738 bytes 72191a94
- 005cd70c ["COPY", "register:0:8", ["register:4040:8"]]
- 005cd70c ["INT_ADD", "register:40f0:8", ["const:5cd70c:8", "const:4:8"]]
- 005cd70c ["CALLIND", null, ["register:0:8"]]
+ 005cd74c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005cd74c ["INT_ADD", "register:40f0:8", ["const:5cd74c:8", "const:4:8"]]
+ 005cd74c ["CALLIND", null, ["register:0:8"]]
- 005cd70c bytes 00013fd6
+ 005cd74c bytes 00013fd6
- 005cd714 ["INT_ADD", "register:40f0:8", ["const:5cd714:8", "const:4:8"]]
- 005cd714 ["CALL", null, ["callee:00c57e80:8"]]
+ 005cd754 ["INT_ADD", "register:40f0:8", ["const:5cd754:8", "const:4:8"]]
+ 005cd754 ["CALL", null, ["callee:00c57e80:8"]]
- 005cd714 bytes db281a94
+ 005cd754 bytes cb291a94
~~~


<a id="compare-a4bb09707ecea4c98a314e4a589a8a14"></a>

### [`005cd728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd728.md) → [`005cd768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd768.md) FUN_005cd768

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005cd620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005cd660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd660.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cd744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd728.md#insn-005cd744) · [`005cd764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd728.md#insn-005cd764)
- 新版 `005cd784`（命令位置の公開資料なし） · `005cd7a4`（命令位置の公開資料なし）

~~~diff
- 005cd744 ["INT_ADD", "register:40f0:8", ["const:5cd744:8", "const:4:8"]]
- 005cd744 ["CALL", null, ["callee:00c53d00:8"]]
+ 005cd784 ["INT_ADD", "register:40f0:8", ["const:5cd784:8", "const:4:8"]]
+ 005cd784 ["CALL", null, ["callee:00c53d00:8"]]
- 005cd744 bytes 67181a94
+ 005cd784 bytes 5f191a94
- 005cd764 ["COPY", "register:0:8", ["register:4040:8"]]
- 005cd764 ["INT_ADD", "register:40f0:8", ["const:5cd764:8", "const:4:8"]]
- 005cd764 ["CALLIND", null, ["register:0:8"]]
+ 005cd7a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005cd7a4 ["INT_ADD", "register:40f0:8", ["const:5cd7a4:8", "const:4:8"]]
+ 005cd7a4 ["CALLIND", null, ["register:0:8"]]
- 005cd764 bytes 00013fd6
+ 005cd7a4 bytes 00013fd6
~~~


<a id="compare-ab1e4a022a97db8cc00c56414aa24b62"></a>

### [`005ce38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce38c.md) → [`005ce3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce3cc.md) FUN_005ce3cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ce39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce38c.md#insn-005ce39c)
- 新版 `005ce3dc`（命令位置の公開資料なし）

~~~diff
- 005ce39c ["INT_ADD", "register:40f0:8", ["const:5ce39c:8", "const:4:8"]]
- 005ce39c ["CALL", null, ["callee:00c57ea0:8"]]
+ 005ce3dc ["INT_ADD", "register:40f0:8", ["const:5ce3dc:8", "const:4:8"]]
+ 005ce3dc ["CALL", null, ["callee:00c57ea0:8"]]
- 005ce39c bytes c1251a94
+ 005ce3dc bytes b1261a94
~~~


<a id="compare-64fb0308d3736d227efc6a79d2d34524"></a>

### [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) → [`005ce4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce4cc.md) FUN_005ce4cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) · 呼出先 3件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md)
- 新版 呼出元 1件 [`005cd7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd7b8.md) · 呼出先 3件 [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) [`005cec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cec1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ce4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md#insn-005ce4c8) · [`005ce4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md#insn-005ce4e4) · [`005ce508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md#insn-005ce508)
- 新版 `005ce508`（命令位置の公開資料なし） · `005ce524`（命令位置の公開資料なし） · `005ce548`（命令位置の公開資料なし）

~~~diff
- 005ce4c8 ["INT_ADD", "register:40f0:8", ["const:5ce4c8:8", "const:4:8"]]
- 005ce4c8 ["CALL", null, ["callee:005cec1c:8"]]
+ 005ce508 ["INT_ADD", "register:40f0:8", ["const:5ce508:8", "const:4:8"]]
+ 005ce508 ["CALL", null, ["callee:005cec1c:8"]]
- 005ce4c8 bytes c5010094
+ 005ce508 bytes c5010094
- 005ce4e4 ["INT_ADD", "register:40f0:8", ["const:5ce4e4:8", "const:4:8"]]
- 005ce4e4 ["CALL", null, ["callee:005ce600:8"]]
+ 005ce524 ["INT_ADD", "register:40f0:8", ["const:5ce524:8", "const:4:8"]]
+ 005ce524 ["CALL", null, ["callee:005ce600:8"]]
- 005ce4e4 bytes 37000094
+ 005ce524 bytes 37000094
- 005ce508 ["INT_ADD", "register:40f0:8", ["const:5ce508:8", "const:4:8"]]
- 005ce508 ["CALL", null, ["callee:005ce964:8"]]
+ 005ce548 ["INT_ADD", "register:40f0:8", ["const:5ce548:8", "const:4:8"]]
+ 005ce548 ["CALL", null, ["callee:005ce964:8"]]
- 005ce508 bytes 07010094
+ 005ce548 bytes 07010094
~~~


<a id="compare-1fa8a6f28a829bc6c0079a66b7d40650"></a>

### [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) → [`005ce56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce56c.md) FUN_005ce56c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005cdb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdb08.md) · 呼出先 3件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md)
- 新版 呼出元 1件 [`005cdb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdb48.md) · 呼出先 3件 [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) [`005cec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cec1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ce54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md#insn-005ce54c) · [`005ce580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md#insn-005ce580)
- 新版 `005ce58c`（命令位置の公開資料なし） · `005ce5c0`（命令位置の公開資料なし）

~~~diff
- 005ce54c ["INT_ADD", "register:40f0:8", ["const:5ce54c:8", "const:4:8"]]
- 005ce54c ["CALL", null, ["callee:005ce600:8"]]
+ 005ce58c ["INT_ADD", "register:40f0:8", ["const:5ce58c:8", "const:4:8"]]
+ 005ce58c ["CALL", null, ["callee:005ce600:8"]]
- 005ce54c bytes 1d000094
+ 005ce58c bytes 1d000094
- 005ce580 ["INT_ADD", "register:40f0:8", ["const:5ce580:8", "const:4:8"]]
- 005ce580 ["CALL", null, ["callee:005ce964:8"]]
+ 005ce5c0 ["INT_ADD", "register:40f0:8", ["const:5ce5c0:8", "const:4:8"]]
+ 005ce5c0 ["CALL", null, ["callee:005ce964:8"]]
- 005ce580 bytes e9000094
+ 005ce5c0 bytes e9000094
~~~


<a id="compare-8f96e0c6ad2f1215db44a2679f47fa25"></a>

### [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md) → [`005cec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cec1c.md) FUN_005cec1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) [`005d582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md) · 呼出先 3件 [`005d4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md) [`005d4c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md) [`005d4c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md)
- 新版 呼出元 3件 [`005ce4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce4cc.md) [`005ce56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce56c.md) [`005d586c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d586c.md) · 呼出先 3件 [`005d4b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4b48.md) [`005d4c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4c88.md) [`005d4cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4cd4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cef20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md#insn-005cef20) · [`005cef34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md#insn-005cef34) · [`005cef38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md#insn-005cef38)
- 新版 `005cef60`（命令位置の公開資料なし） · `005cef74`（命令位置の公開資料なし） · `005cef78`（命令位置の公開資料なし）

~~~diff
- 005cef20 ["INT_ADD", "register:40f0:8", ["const:5cef20:8", "const:4:8"]]
- 005cef20 ["CALL", null, ["callee:005d4b48:8"]]
+ 005cef60 ["INT_ADD", "register:40f0:8", ["const:5cef60:8", "const:4:8"]]
+ 005cef60 ["CALL", null, ["callee:005d4b48:8"]]
- 005cef20 bytes fa160094
+ 005cef60 bytes fa160094
- 005cef34 ["INT_ADD", "register:40f0:8", ["const:5cef34:8", "const:4:8"]]
- 005cef34 ["CALL", null, ["callee:005d4c88:8"]]
+ 005cef74 ["INT_ADD", "register:40f0:8", ["const:5cef74:8", "const:4:8"]]
+ 005cef74 ["CALL", null, ["callee:005d4c88:8"]]
- 005cef34 bytes 45170094
+ 005cef74 bytes 45170094
- 005cef38 ["INT_ADD", "register:40f0:8", ["const:5cef38:8", "const:4:8"]]
- 005cef38 ["CALL", null, ["callee:005d4cd4:8"]]
+ 005cef78 ["INT_ADD", "register:40f0:8", ["const:5cef78:8", "const:4:8"]]
+ 005cef78 ["CALL", null, ["callee:005d4cd4:8"]]
- 005cef38 bytes 57170094
+ 005cef78 bytes 57170094
~~~


<a id="compare-398187c1d04359f592b35d63e01a555b"></a>

### [`005cf4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md) → [`005cf508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf508.md) FUN_005cf508

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005cfb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfb34.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cf530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md#insn-005cf530) · [`005cf580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md#insn-005cf580) · [`005cf624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md#insn-005cf624)
- 新版 `005cf570`（命令位置の公開資料なし） · `005cf5c0`（命令位置の公開資料なし） · `005cf664`（命令位置の公開資料なし）

~~~diff
- 005cf530 ["INT_ADD", "register:40f0:8", ["const:5cf530:8", "const:4:8"]]
- 005cf530 ["CALL", null, ["callee:005cfb34:8"]]
+ 005cf570 ["INT_ADD", "register:40f0:8", ["const:5cf570:8", "const:4:8"]]
+ 005cf570 ["CALL", null, ["callee:005cfb34:8"]]
- 005cf530 bytes 71010094
+ 005cf570 bytes 71010094
- 005cf580 ["INT_ADD", "register:40f0:8", ["const:5cf580:8", "const:4:8"]]
- 005cf580 ["CALL", null, ["callee:005cf6c0:8"]]
+ 005cf5c0 ["INT_ADD", "register:40f0:8", ["const:5cf5c0:8", "const:4:8"]]
+ 005cf5c0 ["CALL", null, ["callee:005cf6c0:8"]]
- 005cf580 bytes 40000094
+ 005cf5c0 bytes 40000094
- 005cf624 ["INT_ADD", "register:40f0:8", ["const:5cf624:8", "const:4:8"]]
- 005cf624 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005cf664 ["INT_ADD", "register:40f0:8", ["const:5cf664:8", "const:4:8"]]
+ 005cf664 ["CALL", null, ["callee:00c57eb0:8"]]
- 005cf624 bytes 23211a94
+ 005cf664 bytes 13221a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b1d1c847ac44e35e85d58d11a762383"></a>

### [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) → [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) FUN_005cf6c0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005cf4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md) [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 10件 [`005cfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005cfed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md) [`005cff24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md) [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md)
- 新版 呼出元 2件 [`005cf508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf508.md) [`005d5c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5c60.md) · 呼出先 10件 [`005cfd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfd54.md) [`005cfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfda0.md) [`005cff18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cff18.md) [`005cff64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cff64.md) [`005cffec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cffec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cf704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md#insn-005cf704) · [`005cf71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md#insn-005cf71c) · [`005cf72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md#insn-005cf72c)
- 新版 `005cf744`（命令位置の公開資料なし） · `005cf75c`（命令位置の公開資料なし） · `005cf76c`（命令位置の公開資料なし）

~~~diff
- 005cf704 ["INT_ADD", "register:40f0:8", ["const:5cf704:8", "const:4:8"]]
- 005cf704 ["CALL", null, ["callee:005cffec:8"]]
+ 005cf744 ["INT_ADD", "register:40f0:8", ["const:5cf744:8", "const:4:8"]]
+ 005cf744 ["CALL", null, ["callee:005cffec:8"]]
- 005cf704 bytes 2a020094
+ 005cf744 bytes 2a020094
- 005cf71c ["INT_ADD", "register:40f0:8", ["const:5cf71c:8", "const:4:8"]]
- 005cf71c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005cf75c ["INT_ADD", "register:40f0:8", ["const:5cf75c:8", "const:4:8"]]
+ 005cf75c ["CALL", null, ["callee:00c57eb0:8"]]
- 005cf71c bytes e5201a94
+ 005cf75c bytes d5211a94
- 005cf72c ["INT_ADD", "register:40f0:8", ["const:5cf72c:8", "const:4:8"]]
- 005cf72c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005cf76c ["INT_ADD", "register:40f0:8", ["const:5cf76c:8", "const:4:8"]]
+ 005cf76c ["CALL", null, ["callee:00c57eb0:8"]]
- 005cf72c bytes e1201a94
+ 005cf76c bytes d1211a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8b8ad39b240630ab02d018f29e23ff"></a>

### [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) → [`005cfb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfb34.md) FUN_005cfb34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005cf4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md) [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 3件 [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005cf508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf508.md) [`005d5c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5c60.md) · 呼出先 3件 [`005cfcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfcfc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cfb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md#insn-005cfb40) · [`005cfba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md#insn-005cfba0) · [`005cfcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md#insn-005cfcb8)
- 新版 `005cfb80`（命令位置の公開資料なし） · `005cfbe0`（命令位置の公開資料なし） · `005cfcf8`（命令位置の公開資料なし）

~~~diff
- 005cfb40 ["INT_ADD", "register:40f0:8", ["const:5cfb40:8", "const:4:8"]]
- 005cfb40 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005cfb80 ["INT_ADD", "register:40f0:8", ["const:5cfb80:8", "const:4:8"]]
+ 005cfb80 ["CALL", null, ["callee:00c57eb0:8"]]
- 005cfb40 bytes dc1f1a94
+ 005cfb80 bytes cc201a94
- 005cfba0 ["INT_ADD", "register:40f0:8", ["const:5cfba0:8", "const:4:8"]]
- 005cfba0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cfbe0 ["INT_ADD", "register:40f0:8", ["const:5cfbe0:8", "const:4:8"]]
+ 005cfbe0 ["CALL", null, ["callee:00c57e90:8"]]
- 005cfba0 bytes bc1f1a94
+ 005cfbe0 bytes ac201a94
- 005cfcb8 ["INT_ADD", "register:40f0:8", ["const:5cfcb8:8", "const:4:8"]]
- 005cfcb8 ["CALL", null, ["callee:005cfcfc:8"]]
+ 005cfcf8 ["INT_ADD", "register:40f0:8", ["const:5cfcf8:8", "const:4:8"]]
+ 005cfcf8 ["CALL", null, ["callee:005cfcfc:8"]]
- 005cfcb8 bytes 01000094
+ 005cfcf8 bytes 01000094
~~~


<a id="compare-45d9c9aa70b830da84ade1061ae3cc24"></a>

### [`005cfcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcd0.md) → [`005cfd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfd10.md) FUN_005cfd10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cfcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcd0.md#insn-005cfcec)
- 新版 `005cfd2c`（命令位置の公開資料なし）

~~~diff
- 005cfcec ["INT_ADD", "register:40f0:8", ["const:5cfcec:8", "const:4:8"]]
- 005cfcec ["CALL", null, ["callee:00c57eb0:8"]]
+ 005cfd2c ["INT_ADD", "register:40f0:8", ["const:5cfd2c:8", "const:4:8"]]
+ 005cfd2c ["CALL", null, ["callee:00c57eb0:8"]]
- 005cfcec bytes 711f1a94
+ 005cfd2c bytes 61201a94
~~~


<a id="compare-87072b5addf20c234a1bbd76b8dac320"></a>

### [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) → [`005cfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfda0.md) FUN_005cfda0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 6件 [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 6件 [`005cfcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfcfc.md) [`005d063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d063c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cfdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md#insn-005cfdc8) · [`005cfe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md#insn-005cfe04) · [`005cfe30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md#insn-005cfe30)
- 新版 `005cfe08`（命令位置の公開資料なし） · `005cfe44`（命令位置の公開資料なし） · `005cfe70`（命令位置の公開資料なし）

~~~diff
- 005cfdc8 ["INT_ADD", "register:40f0:8", ["const:5cfdc8:8", "const:4:8"]]
- 005cfdc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cfe08 ["INT_ADD", "register:40f0:8", ["const:5cfe08:8", "const:4:8"]]
+ 005cfe08 ["CALL", null, ["callee:00c57e90:8"]]
- 005cfdc8 bytes 321f1a94
+ 005cfe08 bytes 22201a94
- 005cfe04 ["INT_ADD", "register:40f0:8", ["const:5cfe04:8", "const:4:8"]]
- 005cfe04 ["CALL", null, ["callee:00c58000:8"]]
+ 005cfe44 ["INT_ADD", "register:40f0:8", ["const:5cfe44:8", "const:4:8"]]
+ 005cfe44 ["CALL", null, ["callee:00c58000:8"]]
- 005cfe04 bytes 7f1f1a94
+ 005cfe44 bytes 6f201a94
- 005cfe30 ["INT_ADD", "register:40f0:8", ["const:5cfe30:8", "const:4:8"]]
- 005cfe30 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cfe70 ["INT_ADD", "register:40f0:8", ["const:5cfe70:8", "const:4:8"]]
+ 005cfe70 ["CALL", null, ["callee:00c57e90:8"]]
- 005cfe30 bytes 181f1a94
+ 005cfe70 bytes 08201a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-930297378ad21a8ee1615484b0390778"></a>

### [`005cff24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md) → [`005cff64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cff64.md) FUN_005cff64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cff6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md#insn-005cff6c) · [`005cff7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md#insn-005cff7c)
- 新版 `005cffac`（命令位置の公開資料なし） · `005cffbc`（命令位置の公開資料なし）

~~~diff
- 005cff6c ["INT_ADD", "register:40f0:8", ["const:5cff6c:8", "const:4:8"]]
- 005cff6c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005cffac ["INT_ADD", "register:40f0:8", ["const:5cffac:8", "const:4:8"]]
+ 005cffac ["CALL", null, ["callee:00c57eb0:8"]]
- 005cff6c bytes d11e1a94
+ 005cffac bytes c11f1a94
- 005cff7c ["INT_ADD", "register:40f0:8", ["const:5cff7c:8", "const:4:8"]]
- 005cff7c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005cffbc ["INT_ADD", "register:40f0:8", ["const:5cffbc:8", "const:4:8"]]
+ 005cffbc ["CALL", null, ["callee:00c57eb0:8"]]
- 005cff7c bytes cd1e1a94
+ 005cffbc bytes bd1f1a94
~~~


<a id="compare-008b366c3523f9475ab4ff8a3793725b"></a>

### [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md) → [`005cffec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cffec.md) FUN_005cffec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d0190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0190.md) [`005d0330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0330.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d01d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d01d0.md) [`005d0370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0370.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d004c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md#insn-005d004c) · [`005d00bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md#insn-005d00bc) · [`005d00ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md#insn-005d00ec)
- 新版 `005d008c`（命令位置の公開資料なし） · `005d00fc`（命令位置の公開資料なし） · `005d012c`（命令位置の公開資料なし）

~~~diff
- 005d004c ["INT_ADD", "register:40f0:8", ["const:5d004c:8", "const:4:8"]]
- 005d004c ["CALL", null, ["callee:00c57e90:8"]]
+ 005d008c ["INT_ADD", "register:40f0:8", ["const:5d008c:8", "const:4:8"]]
+ 005d008c ["CALL", null, ["callee:00c57e90:8"]]
- 005d004c bytes 911e1a94
+ 005d008c bytes 811f1a94
- 005d00bc ["INT_ADD", "register:40f0:8", ["const:5d00bc:8", "const:4:8"]]
- 005d00bc ["CALL", null, ["callee:005d01d0:8"]]
+ 005d00fc ["INT_ADD", "register:40f0:8", ["const:5d00fc:8", "const:4:8"]]
+ 005d00fc ["CALL", null, ["callee:005d01d0:8"]]
- 005d00bc bytes 35000094
+ 005d00fc bytes 35000094
- 005d00ec ["INT_ADD", "register:40f0:8", ["const:5d00ec:8", "const:4:8"]]
- 005d00ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d012c ["INT_ADD", "register:40f0:8", ["const:5d012c:8", "const:4:8"]]
+ 005d012c ["CALL", null, ["callee:00c57eb0:8"]]
- 005d00ec bytes 711e1a94
+ 005d012c bytes 611f1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5635ff5a908af623961f45da9a8f04f3"></a>

### [`005d0190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0190.md) → [`005d01d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d01d0.md) FUN_005d01d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005cffec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cffec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d0250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0190.md#insn-005d0250) · [`005d0260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0190.md#insn-005d0260)
- 新版 `005d0290`（命令位置の公開資料なし） · `005d02a0`（命令位置の公開資料なし）

~~~diff
- 005d0250 ["INT_ADD", "register:40f0:8", ["const:5d0250:8", "const:4:8"]]
- 005d0250 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d0290 ["INT_ADD", "register:40f0:8", ["const:5d0290:8", "const:4:8"]]
+ 005d0290 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d0250 bytes 181e1a94
+ 005d0290 bytes 081f1a94
- 005d0260 ["INT_ADD", "register:40f0:8", ["const:5d0260:8", "const:4:8"]]
- 005d0260 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d02a0 ["INT_ADD", "register:40f0:8", ["const:5d02a0:8", "const:4:8"]]
+ 005d02a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d0260 bytes 141e1a94
+ 005d02a0 bytes 041f1a94
~~~


<a id="compare-a2ad34d5f7de9834292d2ee119ab25a2"></a>

### [`005d02b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d02b4.md) → [`005d02f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d02f4.md) FUN_005d02f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d02f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d02b4.md#insn-005d02f0) · [`005d0300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d02b4.md#insn-005d0300)
- 新版 `005d0330`（命令位置の公開資料なし） · `005d0340`（命令位置の公開資料なし）

~~~diff
- 005d02f0 ["INT_ADD", "register:40f0:8", ["const:5d02f0:8", "const:4:8"]]
- 005d02f0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d0330 ["INT_ADD", "register:40f0:8", ["const:5d0330:8", "const:4:8"]]
+ 005d0330 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d02f0 bytes f01d1a94
+ 005d0330 bytes e01e1a94
- 005d0300 ["INT_ADD", "register:40f0:8", ["const:5d0300:8", "const:4:8"]]
- 005d0300 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d0340 ["INT_ADD", "register:40f0:8", ["const:5d0340:8", "const:4:8"]]
+ 005d0340 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d0300 bytes ec1d1a94
+ 005d0340 bytes dc1e1a94
~~~


<a id="compare-24d159d49b049f759e1b538165108b9b"></a>

### [`005d0344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0344.md) → [`005d0384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0384.md) FUN_005d0384

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005cfcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfcfc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d03ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0344.md#insn-005d03ec) · [`005d0488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0344.md#insn-005d0488) · [`005d04c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0344.md#insn-005d04c8)
- 新版 `005d042c`（命令位置の公開資料なし） · `005d04c8`（命令位置の公開資料なし） · `005d0508`（命令位置の公開資料なし）

~~~diff
- 005d03ec ["INT_ADD", "register:40f0:8", ["const:5d03ec:8", "const:4:8"]]
- 005d03ec ["CALL", null, ["callee:00c57e90:8"]]
+ 005d042c ["INT_ADD", "register:40f0:8", ["const:5d042c:8", "const:4:8"]]
+ 005d042c ["CALL", null, ["callee:00c57e90:8"]]
- 005d03ec bytes a91d1a94
+ 005d042c bytes 991e1a94
- 005d0488 ["INT_ADD", "register:40f0:8", ["const:5d0488:8", "const:4:8"]]
- 005d0488 ["CALL", null, ["callee:00c58000:8"]]
+ 005d04c8 ["INT_ADD", "register:40f0:8", ["const:5d04c8:8", "const:4:8"]]
+ 005d04c8 ["CALL", null, ["callee:00c58000:8"]]
- 005d0488 bytes de1d1a94
+ 005d04c8 bytes ce1e1a94
- 005d04c8 ["INT_ADD", "register:40f0:8", ["const:5d04c8:8", "const:4:8"]]
- 005d04c8 ["CALL", null, ["callee:005cfcfc:8"]]
+ 005d0508 ["INT_ADD", "register:40f0:8", ["const:5d0508:8", "const:4:8"]]
+ 005d0508 ["CALL", null, ["callee:005cfcfc:8"]]
- 005d04c8 bytes fdfdff97
+ 005d0508 bytes fdfdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4810782dcc866154e5378260e05af6c"></a>

### [`005d04d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md) → [`005d0510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0510.md) FUN_005d0510

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 3件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d063c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d0548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md#insn-005d0548) · [`005d056c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md#insn-005d056c) · [`005d0598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md#insn-005d0598)
- 新版 `005d0588`（命令位置の公開資料なし） · `005d05ac`（命令位置の公開資料なし） · `005d05d8`（命令位置の公開資料なし）

~~~diff
- 005d0548 ["INT_ADD", "register:40f0:8", ["const:5d0548:8", "const:4:8"]]
- 005d0548 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d0588 ["INT_ADD", "register:40f0:8", ["const:5d0588:8", "const:4:8"]]
+ 005d0588 ["CALL", null, ["callee:00c57e90:8"]]
- 005d0548 bytes 521d1a94
+ 005d0588 bytes 421e1a94
- 005d056c ["INT_ADD", "register:40f0:8", ["const:5d056c:8", "const:4:8"]]
- 005d056c ["CALL", null, ["callee:00c58090:8"]]
+ 005d05ac ["INT_ADD", "register:40f0:8", ["const:5d05ac:8", "const:4:8"]]
+ 005d05ac ["CALL", null, ["callee:00c58090:8"]]
- 005d056c bytes c91d1a94
+ 005d05ac bytes b91e1a94
- 005d0598 ["INT_ADD", "register:40f0:8", ["const:5d0598:8", "const:4:8"]]
- 005d0598 ["CALL", null, ["callee:00c58090:8"]]
+ 005d05d8 ["INT_ADD", "register:40f0:8", ["const:5d05d8:8", "const:4:8"]]
+ 005d05d8 ["CALL", null, ["callee:00c58090:8"]]
- 005d0598 bytes be1d1a94
+ 005d05d8 bytes ae1e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74700876d06a568709adf4e584076c5a"></a>

### [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) → [`005d0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0650.md) FUN_005d0650

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005d5608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5608.md) [`005d5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5a28.md) · 呼出先 7件 [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md) [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 3件 [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) [`005d5648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5648.md) [`005d5a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5a68.md) · 呼出先 7件 [`005d17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d17a4.md) [`005d1900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1900.md) [`005d2bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2bb8.md) [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d0664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md#insn-005d0664) · [`005d0688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md#insn-005d0688) · [`005d06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md#insn-005d06c4)
- 新版 `005d06a4`（命令位置の公開資料なし） · `005d06c8`（命令位置の公開資料なし） · `005d0704`（命令位置の公開資料なし）

~~~diff
- 005d0664 ["INT_ADD", "register:40f0:8", ["const:5d0664:8", "const:4:8"]]
- 005d0664 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d06a4 ["INT_ADD", "register:40f0:8", ["const:5d06a4:8", "const:4:8"]]
+ 005d06a4 ["CALL", null, ["callee:00c57e90:8"]]
- 005d0664 bytes 0b1d1a94
+ 005d06a4 bytes fb1d1a94
- 005d0688 ["INT_ADD", "register:40f0:8", ["const:5d0688:8", "const:4:8"]]
- 005d0688 ["CALL", null, ["callee:005d1900:8"]]
+ 005d06c8 ["INT_ADD", "register:40f0:8", ["const:5d06c8:8", "const:4:8"]]
+ 005d06c8 ["CALL", null, ["callee:005d1900:8"]]
- 005d0688 bytes 8e040094
+ 005d06c8 bytes 8e040094
- 005d06c4 ["INT_ADD", "register:40f0:8", ["const:5d06c4:8", "const:4:8"]]
- 005d06c4 ["CALL", null, ["callee:005d17a4:8"]]
+ 005d0704 ["INT_ADD", "register:40f0:8", ["const:5d0704:8", "const:4:8"]]
+ 005d0704 ["CALL", null, ["callee:005d17a4:8"]]
- 005d06c4 bytes 28040094
+ 005d0704 bytes 28040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-208806d40e87c891835b8c0a642a738c"></a>

### [`005d07b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md) → [`005d07f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d07f0.md) FUN_005d07f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) · 呼出先 1件 [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md)
- 新版 呼出元 1件 [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) · 呼出先 1件 [`005d0eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0eb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d0800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md#insn-005d0800)
- 新版 `005d0840`（命令位置の公開資料なし）

~~~diff
- 005d0800 ["INT_ADD", "register:40f0:8", ["const:5d0800:8", "const:4:8"]]
- 005d0800 ["CALL", null, ["callee:005d0eb8:8"]]
+ 005d0840 ["INT_ADD", "register:40f0:8", ["const:5d0840:8", "const:4:8"]]
+ 005d0840 ["CALL", null, ["callee:005d0eb8:8"]]
- 005d0800 bytes 9e010094
+ 005d0840 bytes 9e010094
~~~


<a id="compare-4321176917bd4978ae5fa15506a0fea6"></a>

### [`005d08ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md) → [`005d08ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d08ec.md) FUN_005d08ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) · 呼出先 3件 [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md)
- 新版 呼出元 1件 [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) · 呼出先 3件 [`005d0eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0eb8.md) [`005d0ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0ff8.md) [`005d1044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1044.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d08d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md#insn-005d08d0) · [`005d095c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md#insn-005d095c) · [`005d0970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md#insn-005d0970)
- 新版 `005d0910`（命令位置の公開資料なし） · `005d099c`（命令位置の公開資料なし） · `005d09b0`（命令位置の公開資料なし）

~~~diff
- 005d08d0 ["INT_ADD", "register:40f0:8", ["const:5d08d0:8", "const:4:8"]]
- 005d08d0 ["CALL", null, ["callee:005d0eb8:8"]]
+ 005d0910 ["INT_ADD", "register:40f0:8", ["const:5d0910:8", "const:4:8"]]
+ 005d0910 ["CALL", null, ["callee:005d0eb8:8"]]
- 005d08d0 bytes 6a010094
+ 005d0910 bytes 6a010094
- 005d095c ["INT_ADD", "register:40f0:8", ["const:5d095c:8", "const:4:8"]]
- 005d095c ["CALL", null, ["callee:005d1044:8"]]
+ 005d099c ["INT_ADD", "register:40f0:8", ["const:5d099c:8", "const:4:8"]]
+ 005d099c ["CALL", null, ["callee:005d1044:8"]]
- 005d095c bytes aa010094
+ 005d099c bytes aa010094
- 005d0970 ["INT_ADD", "register:40f0:8", ["const:5d0970:8", "const:4:8"]]
- 005d0970 ["CALL", null, ["callee:005d0ff8:8"]]
+ 005d09b0 ["INT_ADD", "register:40f0:8", ["const:5d09b0:8", "const:4:8"]]
+ 005d09b0 ["CALL", null, ["callee:005d0ff8:8"]]
- 005d0970 bytes 92010094
+ 005d09b0 bytes 92010094
~~~


<a id="compare-4c31edb1c32adfb657e57ad9964fec61"></a>

### [`005d0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md) → [`005d09b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d09b4.md) FUN_005d09b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) · 呼出先 3件 [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) · 呼出先 3件 [`005d17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d17a4.md) [`005d1900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1900.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d09bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md#insn-005d09bc) · [`005d09e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md#insn-005d09e0) · [`005d0a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md#insn-005d0a04)
- 新版 `005d09fc`（命令位置の公開資料なし） · `005d0a20`（命令位置の公開資料なし） · `005d0a44`（命令位置の公開資料なし）

~~~diff
- 005d09bc ["INT_ADD", "register:40f0:8", ["const:5d09bc:8", "const:4:8"]]
- 005d09bc ["CALL", null, ["callee:00c57e90:8"]]
+ 005d09fc ["INT_ADD", "register:40f0:8", ["const:5d09fc:8", "const:4:8"]]
+ 005d09fc ["CALL", null, ["callee:00c57e90:8"]]
- 005d09bc bytes 351c1a94
+ 005d09fc bytes 251d1a94
- 005d09e0 ["INT_ADD", "register:40f0:8", ["const:5d09e0:8", "const:4:8"]]
- 005d09e0 ["CALL", null, ["callee:005d1900:8"]]
+ 005d0a20 ["INT_ADD", "register:40f0:8", ["const:5d0a20:8", "const:4:8"]]
+ 005d0a20 ["CALL", null, ["callee:005d1900:8"]]
- 005d09e0 bytes b8030094
+ 005d0a20 bytes b8030094
- 005d0a04 ["INT_ADD", "register:40f0:8", ["const:5d0a04:8", "const:4:8"]]
- 005d0a04 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d0a44 ["INT_ADD", "register:40f0:8", ["const:5d0a44:8", "const:4:8"]]
+ 005d0a44 ["CALL", null, ["callee:00c57e90:8"]]
- 005d0a04 bytes 231c1a94
+ 005d0a44 bytes 131d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c793a9d271557be45ea3106e39097aff"></a>

### [`005d0b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md) → [`005d0bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0bb8.md) FUN_005d0bb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) · 呼出先 3件 [`005d0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md) [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`00c5a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3e0.md)
- 新版 呼出元 2件 [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) [`005d347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d347c.md) · 呼出先 3件 [`005d08a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d08a0.md) [`005d0eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0eb8.md) [`00c5a7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d0c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md#insn-005d0c0c) · [`005d0c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md#insn-005d0c34) · [`005d0c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md#insn-005d0c58)
- 新版 `005d0c4c`（命令位置の公開資料なし） · `005d0c74`（命令位置の公開資料なし） · `005d0c98`（命令位置の公開資料なし）

~~~diff
- 005d0c0c ["INT_ADD", "register:40f0:8", ["const:5d0c0c:8", "const:4:8"]]
- 005d0c0c ["CALL", null, ["callee:00c5a7e0:8"]]
+ 005d0c4c ["INT_ADD", "register:40f0:8", ["const:5d0c4c:8", "const:4:8"]]
+ 005d0c4c ["CALL", null, ["callee:00c5a7e0:8"]]
- 005d0c0c bytes f5251a94
+ 005d0c4c bytes e5261a94
- 005d0c34 ["INT_ADD", "register:40f0:8", ["const:5d0c34:8", "const:4:8"]]
- 005d0c34 ["CALL", null, ["callee:00c5a7e0:8"]]
+ 005d0c74 ["INT_ADD", "register:40f0:8", ["const:5d0c74:8", "const:4:8"]]
+ 005d0c74 ["CALL", null, ["callee:00c5a7e0:8"]]
- 005d0c34 bytes eb251a94
+ 005d0c74 bytes db261a94
- 005d0c58 ["INT_ADD", "register:40f0:8", ["const:5d0c58:8", "const:4:8"]]
- 005d0c58 ["CALL", null, ["callee:00c5a7e0:8"]]
+ 005d0c98 ["INT_ADD", "register:40f0:8", ["const:5d0c98:8", "const:4:8"]]
+ 005d0c98 ["CALL", null, ["callee:00c5a7e0:8"]]
- 005d0c58 bytes e2251a94
+ 005d0c98 bytes d2261a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6390ba56c2c91bdd65478275a1a0233d"></a>

### [`005d1180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1180.md) → [`005d11c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d11c0.md) FUN_005d11c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d11b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1180.md#insn-005d11b0)
- 新版 `005d11f0`（命令位置の公開資料なし）

~~~diff
- 005d11b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005d11b0 ["INT_ADD", "register:40f0:8", ["const:5d11b0:8", "const:4:8"]]
- 005d11b0 ["CALLIND", null, ["register:0:8"]]
+ 005d11f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d11f0 ["INT_ADD", "register:40f0:8", ["const:5d11f0:8", "const:4:8"]]
+ 005d11f0 ["CALLIND", null, ["register:0:8"]]
- 005d11b0 bytes 20013fd6
+ 005d11f0 bytes 20013fd6
~~~


<a id="compare-5aaa576ea238ce9004a57f22183c4135"></a>

### [`005d1438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1438.md) → [`005d1478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1478.md) FUN_005d1478

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d14b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1438.md#insn-005d14b8) · [`005d14d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1438.md#insn-005d14d8)
- 新版 `005d14f8`（命令位置の公開資料なし） · `005d1518`（命令位置の公開資料なし）

~~~diff
- 005d14b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005d14b8 ["INT_ADD", "register:40f0:8", ["const:5d14b8:8", "const:4:8"]]
- 005d14b8 ["CALLIND", null, ["register:0:8"]]
+ 005d14f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d14f8 ["INT_ADD", "register:40f0:8", ["const:5d14f8:8", "const:4:8"]]
+ 005d14f8 ["CALLIND", null, ["register:0:8"]]
- 005d14b8 bytes 20013fd6
+ 005d14f8 bytes 20013fd6
- 005d14d8 ["COPY", "register:0:8", ["register:4050:8"]]
- 005d14d8 ["INT_ADD", "register:40f0:8", ["const:5d14d8:8", "const:4:8"]]
- 005d14d8 ["CALLIND", null, ["register:0:8"]]
+ 005d1518 ["COPY", "register:0:8", ["register:4050:8"]]
+ 005d1518 ["INT_ADD", "register:40f0:8", ["const:5d1518:8", "const:4:8"]]
+ 005d1518 ["CALLIND", null, ["register:0:8"]]
- 005d14d8 bytes 40013fd6
+ 005d1518 bytes 40013fd6
~~~


<a id="compare-2f2bd2e85caa38ca86f1078814dd21ab"></a>

### [`005d16a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d16a4.md) → [`005d16e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d16e4.md) FUN_005d16e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005d0ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0ff8.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d1718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d16a4.md#insn-005d1718) · [`005d1760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d16a4.md#insn-005d1760)
- 新版 `005d1758`（命令位置の公開資料なし） · `005d17a0`（命令位置の公開資料なし）

~~~diff
- 005d1718 ["INT_ADD", "register:40f0:8", ["const:5d1718:8", "const:4:8"]]
- 005d1718 ["CALL", null, ["callee:00c58050:8"]]
+ 005d1758 ["INT_ADD", "register:40f0:8", ["const:5d1758:8", "const:4:8"]]
+ 005d1758 ["CALL", null, ["callee:00c58050:8"]]
- 005d1718 bytes 4e191a94
+ 005d1758 bytes 3e1a1a94
- 005d1760 ["INT_ADD", "register:40f0:8", ["const:5d1760:8", "const:4:8"]]
- 005d1760 ["CALL", null, ["callee:005d0ff8:8"]]
+ 005d17a0 ["INT_ADD", "register:40f0:8", ["const:5d17a0:8", "const:4:8"]]
+ 005d17a0 ["CALL", null, ["callee:005d0ff8:8"]]
- 005d1760 bytes 16feff97
+ 005d17a0 bytes 16feff97
~~~


<a id="compare-f625db42d58946edcee0314f512171ae"></a>

### [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) → [`005d17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d17a4.md) FUN_005d17a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) [`005d0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md) [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) · 呼出先 4件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`005d0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0650.md) [`005d09b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d09b4.md) [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) [`005d347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d347c.md) · 呼出先 4件 [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d1790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md#insn-005d1790) · [`005d17fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md#insn-005d17fc) · [`005d1848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md#insn-005d1848)
- 新版 `005d17d0`（命令位置の公開資料なし） · `005d183c`（命令位置の公開資料なし） · `005d1888`（命令位置の公開資料なし）

~~~diff
- 005d1790 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d1790 ["INT_ADD", "register:40f0:8", ["const:5d1790:8", "const:4:8"]]
- 005d1790 ["CALLIND", null, ["register:0:8"]]
+ 005d17d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d17d0 ["INT_ADD", "register:40f0:8", ["const:5d17d0:8", "const:4:8"]]
+ 005d17d0 ["CALLIND", null, ["register:0:8"]]
- 005d1790 bytes 00013fd6
+ 005d17d0 bytes 00013fd6
- 005d17fc ["INT_ADD", "register:40f0:8", ["const:5d17fc:8", "const:4:8"]]
- 005d17fc ["CALL", null, ["callee:00c57e90:8"]]
+ 005d183c ["INT_ADD", "register:40f0:8", ["const:5d183c:8", "const:4:8"]]
+ 005d183c ["CALL", null, ["callee:00c57e90:8"]]
- 005d17fc bytes a5181a94
+ 005d183c bytes 95191a94
- 005d1848 ["INT_ADD", "register:40f0:8", ["const:5d1848:8", "const:4:8"]]
- 005d1848 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d1888 ["INT_ADD", "register:40f0:8", ["const:5d1888:8", "const:4:8"]]
+ 005d1888 ["CALL", null, ["callee:00c57e90:8"]]
- 005d1848 bytes 92181a94
+ 005d1888 bytes 82191a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54fb6c57d4cbe41597ffb4122975698f"></a>

### [`005d1a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1a7c.md) → [`005d1abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1abc.md) FUN_005d1abc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d1ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1a7c.md#insn-005d1ac4) · [`005d1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1a7c.md#insn-005d1ad8)
- 新版 `005d1b04`（命令位置の公開資料なし） · `005d1b18`（命令位置の公開資料なし）

~~~diff
- 005d1ac4 ["INT_ADD", "register:40f0:8", ["const:5d1ac4:8", "const:4:8"]]
- 005d1ac4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d1b04 ["INT_ADD", "register:40f0:8", ["const:5d1b04:8", "const:4:8"]]
+ 005d1b04 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d1ac4 bytes fb171a94
+ 005d1b04 bytes eb181a94
- 005d1ad8 ["INT_ADD", "register:40f0:8", ["const:5d1ad8:8", "const:4:8"]]
- 005d1ad8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d1b18 ["INT_ADD", "register:40f0:8", ["const:5d1b18:8", "const:4:8"]]
+ 005d1b18 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d1ad8 bytes f6171a94
+ 005d1b18 bytes e6181a94
~~~


<a id="compare-be50b8087a65bdf7fb0dc7b7e1d04861"></a>

### [`005d1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c4c.md) → [`005d1c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1c8c.md) FUN_005d1c8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005d1b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1b08.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005d1b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1b48.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d1c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c4c.md#insn-005d1c5c)
- 新版 `005d1c9c`（命令位置の公開資料なし）

~~~diff
- 005d1c5c ["INT_ADD", "register:40f0:8", ["const:5d1c5c:8", "const:4:8"]]
- 005d1c5c ["CALL", null, ["callee:005d1b48:8"]]
+ 005d1c9c ["INT_ADD", "register:40f0:8", ["const:5d1c9c:8", "const:4:8"]]
+ 005d1c9c ["CALL", null, ["callee:005d1b48:8"]]
- 005d1c5c bytes abffff97
+ 005d1c9c bytes abffff97
~~~


<a id="compare-c13853f9d773d1a96d86d170696c44bd"></a>

### [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) → [`005d1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1cb0.md) FUN_005d1cb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`005d25d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md) [`005d2740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md) [`005d29a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005d2610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2610.md) [`005d2780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2780.md) [`005d29e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d29e4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d1ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md#insn-005d1ce8) · [`005d1d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md#insn-005d1d04) · [`005d1d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md#insn-005d1d24)
- 新版 `005d1d28`（命令位置の公開資料なし） · `005d1d44`（命令位置の公開資料なし） · `005d1d64`（命令位置の公開資料なし）

~~~diff
- 005d1ce8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d1ce8 ["INT_ADD", "register:40f0:8", ["const:5d1ce8:8", "const:4:8"]]
- 005d1ce8 ["CALLIND", null, ["register:0:8"]]
+ 005d1d28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d1d28 ["INT_ADD", "register:40f0:8", ["const:5d1d28:8", "const:4:8"]]
+ 005d1d28 ["CALLIND", null, ["register:0:8"]]
- 005d1ce8 bytes 00013fd6
+ 005d1d28 bytes 00013fd6
- 005d1d04 ["COPY", "register:0:8", ["register:4048:8"]]
- 005d1d04 ["INT_ADD", "register:40f0:8", ["const:5d1d04:8", "const:4:8"]]
- 005d1d04 ["CALLIND", null, ["register:0:8"]]
+ 005d1d44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d1d44 ["INT_ADD", "register:40f0:8", ["const:5d1d44:8", "const:4:8"]]
+ 005d1d44 ["CALLIND", null, ["register:0:8"]]
- 005d1d04 bytes 20013fd6
+ 005d1d44 bytes 20013fd6
- 005d1d24 ["INT_ADD", "register:40f0:8", ["const:5d1d24:8", "const:4:8"]]
- 005d1d24 ["CALL", null, ["callee:005d2780:8"]]
+ 005d1d64 ["INT_ADD", "register:40f0:8", ["const:5d1d64:8", "const:4:8"]]
+ 005d1d64 ["CALL", null, ["callee:005d2780:8"]]
- 005d1d24 bytes 87020094
+ 005d1d64 bytes 87020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-614ec9bc8bf9d4004694d597bcd41ab2"></a>

### [`005d25d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md) → [`005d2610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2610.md) FUN_005d2610

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1cb0.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d2654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md#insn-005d2654) · [`005d267c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md#insn-005d267c) · [`005d26b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md#insn-005d26b8)
- 新版 `005d2694`（命令位置の公開資料なし） · `005d26bc`（命令位置の公開資料なし） · `005d26f8`（命令位置の公開資料なし）

~~~diff
- 005d2654 ["INT_ADD", "register:40f0:8", ["const:5d2654:8", "const:4:8"]]
- 005d2654 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d2694 ["INT_ADD", "register:40f0:8", ["const:5d2694:8", "const:4:8"]]
+ 005d2694 ["CALL", null, ["callee:00c57e90:8"]]
- 005d2654 bytes 0f151a94
+ 005d2694 bytes ff151a94
- 005d267c ["INT_ADD", "register:40f0:8", ["const:5d267c:8", "const:4:8"]]
- 005d267c ["CALL", null, ["callee:00c58000:8"]]
+ 005d26bc ["INT_ADD", "register:40f0:8", ["const:5d26bc:8", "const:4:8"]]
+ 005d26bc ["CALL", null, ["callee:00c58000:8"]]
- 005d267c bytes 61151a94
+ 005d26bc bytes 51161a94
- 005d26b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005d26b8 ["INT_ADD", "register:40f0:8", ["const:5d26b8:8", "const:4:8"]]
- 005d26b8 ["CALLIND", null, ["register:0:8"]]
+ 005d26f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d26f8 ["INT_ADD", "register:40f0:8", ["const:5d26f8:8", "const:4:8"]]
+ 005d26f8 ["CALLIND", null, ["register:0:8"]]
- 005d26b8 bytes 20013fd6
+ 005d26f8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f90883b0292871322140437c34f05b7"></a>

### [`005d2740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md) → [`005d2780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2780.md) FUN_005d2780

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1cb0.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d27c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md#insn-005d27c4) · [`005d27ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md#insn-005d27ec) · [`005d282c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md#insn-005d282c)
- 新版 `005d2804`（命令位置の公開資料なし） · `005d282c`（命令位置の公開資料なし） · `005d286c`（命令位置の公開資料なし）

~~~diff
- 005d27c4 ["INT_ADD", "register:40f0:8", ["const:5d27c4:8", "const:4:8"]]
- 005d27c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d2804 ["INT_ADD", "register:40f0:8", ["const:5d2804:8", "const:4:8"]]
+ 005d2804 ["CALL", null, ["callee:00c57e90:8"]]
- 005d27c4 bytes b3141a94
+ 005d2804 bytes a3151a94
- 005d27ec ["INT_ADD", "register:40f0:8", ["const:5d27ec:8", "const:4:8"]]
- 005d27ec ["CALL", null, ["callee:00c58000:8"]]
+ 005d282c ["INT_ADD", "register:40f0:8", ["const:5d282c:8", "const:4:8"]]
+ 005d282c ["CALL", null, ["callee:00c58000:8"]]
- 005d27ec bytes 05151a94
+ 005d282c bytes f5151a94
- 005d282c ["INT_ADD", "register:40f0:8", ["const:5d282c:8", "const:4:8"]]
- 005d282c ["CALL", null, ["callee:00c5a800:8"]]
+ 005d286c ["INT_ADD", "register:40f0:8", ["const:5d286c:8", "const:4:8"]]
+ 005d286c ["CALL", null, ["callee:00c5a800:8"]]
- 005d282c bytes f51e1a94
+ 005d286c bytes e51f1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b1c539748eda683cfd2518fac27ec6a"></a>

### [`005d29a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md) → [`005d29e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d29e4.md) FUN_005d29e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1cb0.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d2a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md#insn-005d2a28) · [`005d2a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md#insn-005d2a50) · [`005d2a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md#insn-005d2a8c)
- 新版 `005d2a68`（命令位置の公開資料なし） · `005d2a90`（命令位置の公開資料なし） · `005d2acc`（命令位置の公開資料なし）

~~~diff
- 005d2a28 ["INT_ADD", "register:40f0:8", ["const:5d2a28:8", "const:4:8"]]
- 005d2a28 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d2a68 ["INT_ADD", "register:40f0:8", ["const:5d2a68:8", "const:4:8"]]
+ 005d2a68 ["CALL", null, ["callee:00c57e90:8"]]
- 005d2a28 bytes 1a141a94
+ 005d2a68 bytes 0a151a94
- 005d2a50 ["INT_ADD", "register:40f0:8", ["const:5d2a50:8", "const:4:8"]]
- 005d2a50 ["CALL", null, ["callee:00c58000:8"]]
+ 005d2a90 ["INT_ADD", "register:40f0:8", ["const:5d2a90:8", "const:4:8"]]
+ 005d2a90 ["CALL", null, ["callee:00c58000:8"]]
- 005d2a50 bytes 6c141a94
+ 005d2a90 bytes 5c151a94
- 005d2a8c ["COPY", "register:0:8", ["register:4048:8"]]
- 005d2a8c ["INT_ADD", "register:40f0:8", ["const:5d2a8c:8", "const:4:8"]]
- 005d2a8c ["CALLIND", null, ["register:0:8"]]
+ 005d2acc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d2acc ["INT_ADD", "register:40f0:8", ["const:5d2acc:8", "const:4:8"]]
+ 005d2acc ["CALLIND", null, ["register:0:8"]]
- 005d2a8c bytes 20013fd6
+ 005d2acc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ada2850bd81d7ec578dc71110069608"></a>

### [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) → [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) FUN_005d2c04

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) · 呼出先 14件 [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md)
- 新版 呼出元 1件 [`005d0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0650.md) · 呼出先 14件 [`005d17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d17a4.md) [`005d2bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2bb8.md) [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) [`005d3360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3360.md) [`005d347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d347c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d2c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md#insn-005d2c60) · [`005d2ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md#insn-005d2ccc) · [`005d2d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md#insn-005d2d2c)
- 新版 `005d2ca0`（命令位置の公開資料なし） · `005d2d0c`（命令位置の公開資料なし） · `005d2d6c`（命令位置の公開資料なし）

~~~diff
- 005d2c60 ["INT_ADD", "register:40f0:8", ["const:5d2c60:8", "const:4:8"]]
- 005d2c60 ["CALL", null, ["callee:005d30d4:8"]]
+ 005d2ca0 ["INT_ADD", "register:40f0:8", ["const:5d2ca0:8", "const:4:8"]]
+ 005d2ca0 ["CALL", null, ["callee:005d30d4:8"]]
- 005d2c60 bytes 0d010094
+ 005d2ca0 bytes 0d010094
- 005d2ccc ["INT_ADD", "register:40f0:8", ["const:5d2ccc:8", "const:4:8"]]
- 005d2ccc ["CALL", null, ["callee:005d3360:8"]]
+ 005d2d0c ["INT_ADD", "register:40f0:8", ["const:5d2d0c:8", "const:4:8"]]
+ 005d2d0c ["CALL", null, ["callee:005d3360:8"]]
- 005d2ccc bytes 95010094
+ 005d2d0c bytes 95010094
- 005d2d2c ["INT_ADD", "register:40f0:8", ["const:5d2d2c:8", "const:4:8"]]
- 005d2d2c ["CALL", null, ["callee:005d35a0:8"]]
+ 005d2d6c ["INT_ADD", "register:40f0:8", ["const:5d2d6c:8", "const:4:8"]]
+ 005d2d6c ["CALL", null, ["callee:005d35a0:8"]]
- 005d2d2c bytes 0d020094
+ 005d2d6c bytes 0d020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-472cd984f31cbbb39277af68ce32c781"></a>

### [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) → [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) FUN_005d30d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d3c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md)
- 新版 呼出元 1件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`005d17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d17a4.md) [`005d2bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2bb8.md) [`005d3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3c58.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d3124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md#insn-005d3124) · [`005d315c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md#insn-005d315c) · [`005d31d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md#insn-005d31d8)
- 新版 `005d3164`（命令位置の公開資料なし） · `005d319c`（命令位置の公開資料なし） · `005d3218`（命令位置の公開資料なし）

~~~diff
- 005d3124 ["INT_ADD", "register:40f0:8", ["const:5d3124:8", "const:4:8"]]
- 005d3124 ["CALL", null, ["callee:005d3eb0:8"]]
+ 005d3164 ["INT_ADD", "register:40f0:8", ["const:5d3164:8", "const:4:8"]]
+ 005d3164 ["CALL", null, ["callee:005d3eb0:8"]]
- 005d3124 bytes 53030094
+ 005d3164 bytes 53030094
- 005d315c ["INT_ADD", "register:40f0:8", ["const:5d315c:8", "const:4:8"]]
- 005d315c ["CALL", null, ["callee:005d4114:8"]]
+ 005d319c ["INT_ADD", "register:40f0:8", ["const:5d319c:8", "const:4:8"]]
+ 005d319c ["CALL", null, ["callee:005d4114:8"]]
- 005d315c bytes de030094
+ 005d319c bytes de030094
- 005d31d8 ["INT_ADD", "register:40f0:8", ["const:5d31d8:8", "const:4:8"]]
- 005d31d8 ["CALL", null, ["callee:005d17a4:8"]]
+ 005d3218 ["INT_ADD", "register:40f0:8", ["const:5d3218:8", "const:4:8"]]
+ 005d3218 ["CALL", null, ["callee:005d17a4:8"]]
- 005d31d8 bytes 63f9ff97
+ 005d3218 bytes 63f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b8969f2c4f964ce3d81f739d428789a"></a>

### [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) → [`005d3360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3360.md) FUN_005d3360

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 5件 [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d3e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e24.md) [`005d3e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) · 呼出先 5件 [`005d2bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2bb8.md) [`005d3e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3e64.md) [`005d3eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3eb0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d33a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md#insn-005d33a0) · [`005d33b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md#insn-005d33b0) · [`005d3420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md#insn-005d3420)
- 新版 `005d33e0`（命令位置の公開資料なし） · `005d33f0`（命令位置の公開資料なし） · `005d3460`（命令位置の公開資料なし）

~~~diff
- 005d33a0 ["INT_ADD", "register:40f0:8", ["const:5d33a0:8", "const:4:8"]]
- 005d33a0 ["CALL", null, ["callee:005d3eb0:8"]]
+ 005d33e0 ["INT_ADD", "register:40f0:8", ["const:5d33e0:8", "const:4:8"]]
+ 005d33e0 ["CALL", null, ["callee:005d3eb0:8"]]
- 005d33a0 bytes b4020094
+ 005d33e0 bytes b4020094
- 005d33b0 ["INT_ADD", "register:40f0:8", ["const:5d33b0:8", "const:4:8"]]
- 005d33b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d33f0 ["INT_ADD", "register:40f0:8", ["const:5d33f0:8", "const:4:8"]]
+ 005d33f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d33b0 bytes c0111a94
+ 005d33f0 bytes b0121a94
- 005d3420 ["INT_ADD", "register:40f0:8", ["const:5d3420:8", "const:4:8"]]
- 005d3420 ["CALL", null, ["callee:005d2bb8:8"]]
+ 005d3460 ["INT_ADD", "register:40f0:8", ["const:5d3460:8", "const:4:8"]]
+ 005d3460 ["CALL", null, ["callee:005d2bb8:8"]]
- 005d3420 bytes d6fdff97
+ 005d3460 bytes d6fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac4d76fe58d54086722360fc171741c4"></a>

### [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) → [`005d347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d347c.md) FUN_005d347c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 5件 [`005d0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md) [`005d0b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md) [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d44dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md) [`00c5a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3e0.md)
- 新版 呼出元 1件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) · 呼出先 5件 [`005d08a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d08a0.md) [`005d0bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0bb8.md) [`005d17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d17a4.md) [`005d451c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d451c.md) [`00c5a7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d34cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md#insn-005d34cc) · [`005d34f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md#insn-005d34f8) · [`005d3508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md#insn-005d3508)
- 新版 `005d350c`（命令位置の公開資料なし） · `005d3538`（命令位置の公開資料なし） · `005d3548`（命令位置の公開資料なし）

~~~diff
- 005d34cc ["INT_ADD", "register:40f0:8", ["const:5d34cc:8", "const:4:8"]]
- 005d34cc ["CALL", null, ["callee:005d451c:8"]]
+ 005d350c ["INT_ADD", "register:40f0:8", ["const:5d350c:8", "const:4:8"]]
+ 005d350c ["CALL", null, ["callee:005d451c:8"]]
- 005d34cc bytes 04040094
+ 005d350c bytes 04040094
- 005d34f8 ["INT_ADD", "register:40f0:8", ["const:5d34f8:8", "const:4:8"]]
- 005d34f8 ["CALL", null, ["callee:005d17a4:8"]]
+ 005d3538 ["INT_ADD", "register:40f0:8", ["const:5d3538:8", "const:4:8"]]
+ 005d3538 ["CALL", null, ["callee:005d17a4:8"]]
- 005d34f8 bytes 9bf8ff97
+ 005d3538 bytes 9bf8ff97
- 005d3508 ["INT_ADD", "register:40f0:8", ["const:5d3508:8", "const:4:8"]]
- 005d3508 ["CALL", null, ["callee:00c5a7e0:8"]]
+ 005d3548 ["INT_ADD", "register:40f0:8", ["const:5d3548:8", "const:4:8"]]
+ 005d3548 ["CALL", null, ["callee:00c5a7e0:8"]]
- 005d3508 bytes b61b1a94
+ 005d3548 bytes a61c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-942b9ec7a63e7d4d5225aed93cb4c935"></a>

### [`005d3560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md) → [`005d35a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d35a0.md) FUN_005d35a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`005d5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md) · 呼出先 3件 [`005d0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md) [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`00c5a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3e0.md)
- 新版 呼出元 2件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) [`005d5b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5b90.md) · 呼出先 3件 [`005d08a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d08a0.md) [`005d0eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0eb8.md) [`00c5a7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d365c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md#insn-005d365c) · [`005d3708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md#insn-005d3708) · [`005d3720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md#insn-005d3720)
- 新版 `005d369c`（命令位置の公開資料なし） · `005d3748`（命令位置の公開資料なし） · `005d3760`（命令位置の公開資料なし）

~~~diff
- 005d365c ["INT_ADD", "register:40f0:8", ["const:5d365c:8", "const:4:8"]]
- 005d365c ["CALL", null, ["callee:00c5a7e0:8"]]
+ 005d369c ["INT_ADD", "register:40f0:8", ["const:5d369c:8", "const:4:8"]]
+ 005d369c ["CALL", null, ["callee:00c5a7e0:8"]]
- 005d365c bytes 611b1a94
+ 005d369c bytes 511c1a94
- 005d3708 ["INT_ADD", "register:40f0:8", ["const:5d3708:8", "const:4:8"]]
- 005d3708 ["CALL", null, ["callee:005d0eb8:8"]]
+ 005d3748 ["INT_ADD", "register:40f0:8", ["const:5d3748:8", "const:4:8"]]
+ 005d3748 ["CALL", null, ["callee:005d0eb8:8"]]
- 005d3708 bytes dcf5ff97
+ 005d3748 bytes dcf5ff97
- 005d3720 ["INT_ADD", "register:40f0:8", ["const:5d3720:8", "const:4:8"]]
- 005d3720 ["CALL", null, ["callee:00c5a7e0:8"]]
+ 005d3760 ["INT_ADD", "register:40f0:8", ["const:5d3760:8", "const:4:8"]]
+ 005d3760 ["CALL", null, ["callee:00c5a7e0:8"]]
- 005d3720 bytes 301b1a94
+ 005d3760 bytes 201c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d051e32fc8daa6e5149163ae15752a8"></a>

### [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) → [`005d3788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3788.md) FUN_005d3788

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 7件 [`004ec218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec218.md) [`005d4638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md) [`005d47fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d47fc.md) [`005d4848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) · 呼出先 7件 [`004ec258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec258.md) [`005d4678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4678.md) [`005d483c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d483c.md) [`005d4888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4888.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d37c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md#insn-005d37c8) · [`005d3844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md#insn-005d3844) · [`005d38e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md#insn-005d38e0)
- 新版 `005d3808`（命令位置の公開資料なし） · `005d3884`（命令位置の公開資料なし） · `005d3920`（命令位置の公開資料なし）

~~~diff
- 005d37c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d37c8 ["INT_ADD", "register:40f0:8", ["const:5d37c8:8", "const:4:8"]]
- 005d37c8 ["CALLIND", null, ["register:0:8"]]
+ 005d3808 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d3808 ["INT_ADD", "register:40f0:8", ["const:5d3808:8", "const:4:8"]]
+ 005d3808 ["CALLIND", null, ["register:0:8"]]
- 005d37c8 bytes 00013fd6
+ 005d3808 bytes 00013fd6
- 005d3844 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d3844 ["INT_ADD", "register:40f0:8", ["const:5d3844:8", "const:4:8"]]
- 005d3844 ["CALLIND", null, ["register:0:8"]]
+ 005d3884 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d3884 ["INT_ADD", "register:40f0:8", ["const:5d3884:8", "const:4:8"]]
+ 005d3884 ["CALLIND", null, ["register:0:8"]]
- 005d3844 bytes 00013fd6
+ 005d3884 bytes 00013fd6
- 005d38e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d38e0 ["INT_ADD", "register:40f0:8", ["const:5d38e0:8", "const:4:8"]]
- 005d38e0 ["CALLIND", null, ["register:0:8"]]
+ 005d3920 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d3920 ["INT_ADD", "register:40f0:8", ["const:5d3920:8", "const:4:8"]]
+ 005d3920 ["CALLIND", null, ["register:0:8"]]
- 005d38e0 bytes 00013fd6
+ 005d3920 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-218811b8e6b9dc3af5c3feed50053331"></a>

### [`005d3c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md) → [`005d3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3c58.md) FUN_005d3c58

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d4a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4a3c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d3c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md#insn-005d3c4c) · [`005d3c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md#insn-005d3c68) · [`005d3d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md#insn-005d3d20)
- 新版 `005d3c8c`（命令位置の公開資料なし） · `005d3ca8`（命令位置の公開資料なし） · `005d3d60`（命令位置の公開資料なし）

~~~diff
- 005d3c4c ["COPY", "register:0:8", ["register:4040:8"]]
- 005d3c4c ["INT_ADD", "register:40f0:8", ["const:5d3c4c:8", "const:4:8"]]
- 005d3c4c ["CALLIND", null, ["register:0:8"]]
+ 005d3c8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d3c8c ["INT_ADD", "register:40f0:8", ["const:5d3c8c:8", "const:4:8"]]
+ 005d3c8c ["CALLIND", null, ["register:0:8"]]
- 005d3c4c bytes 00013fd6
+ 005d3c8c bytes 00013fd6
- 005d3c68 ["COPY", "register:0:8", ["register:4048:8"]]
- 005d3c68 ["INT_ADD", "register:40f0:8", ["const:5d3c68:8", "const:4:8"]]
- 005d3c68 ["CALLIND", null, ["register:0:8"]]
+ 005d3ca8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d3ca8 ["INT_ADD", "register:40f0:8", ["const:5d3ca8:8", "const:4:8"]]
+ 005d3ca8 ["CALLIND", null, ["register:0:8"]]
- 005d3c68 bytes 20013fd6
+ 005d3ca8 bytes 20013fd6
- 005d3d20 ["INT_ADD", "register:40f0:8", ["const:5d3d20:8", "const:4:8"]]
- 005d3d20 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d3d60 ["INT_ADD", "register:40f0:8", ["const:5d3d60:8", "const:4:8"]]
+ 005d3d60 ["CALL", null, ["callee:00c57e90:8"]]
- 005d3d20 bytes 5c0f1a94
+ 005d3d60 bytes 4c101a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62d589932e3037564689b0e828af3586"></a>

### [`005d3e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md) → [`005d3eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3eb0.md) FUN_005d3eb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) [`005d3360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3360.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d3ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md#insn-005d3ef4) · [`005d3f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md#insn-005d3f1c) · [`005d3f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md#insn-005d3f5c)
- 新版 `005d3f34`（命令位置の公開資料なし） · `005d3f5c`（命令位置の公開資料なし） · `005d3f9c`（命令位置の公開資料なし）

~~~diff
- 005d3ef4 ["INT_ADD", "register:40f0:8", ["const:5d3ef4:8", "const:4:8"]]
- 005d3ef4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d3f34 ["INT_ADD", "register:40f0:8", ["const:5d3f34:8", "const:4:8"]]
+ 005d3f34 ["CALL", null, ["callee:00c57e90:8"]]
- 005d3ef4 bytes e70e1a94
+ 005d3f34 bytes d70f1a94
- 005d3f1c ["INT_ADD", "register:40f0:8", ["const:5d3f1c:8", "const:4:8"]]
- 005d3f1c ["CALL", null, ["callee:00c58000:8"]]
+ 005d3f5c ["INT_ADD", "register:40f0:8", ["const:5d3f5c:8", "const:4:8"]]
+ 005d3f5c ["CALL", null, ["callee:00c58000:8"]]
- 005d3f1c bytes 390f1a94
+ 005d3f5c bytes 29101a94
- 005d3f5c ["INT_ADD", "register:40f0:8", ["const:5d3f5c:8", "const:4:8"]]
- 005d3f5c ["CALL", null, ["callee:00c5a800:8"]]
+ 005d3f9c ["INT_ADD", "register:40f0:8", ["const:5d3f9c:8", "const:4:8"]]
+ 005d3f9c ["CALL", null, ["callee:00c5a800:8"]]
- 005d3f5c bytes 29191a94
+ 005d3f9c bytes 191a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27696ae3344e2e2bb4e50bb1f554218b"></a>

### [`005d40d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md) → [`005d4114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4114.md) FUN_005d4114

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d41a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md#insn-005d41a4) · [`005d4210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md#insn-005d4210) · [`005d426c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md#insn-005d426c)
- 新版 `005d41e4`（命令位置の公開資料なし） · `005d4250`（命令位置の公開資料なし） · `005d42ac`（命令位置の公開資料なし）

~~~diff
- 005d41a4 ["INT_ADD", "register:40f0:8", ["const:5d41a4:8", "const:4:8"]]
- 005d41a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d41e4 ["INT_ADD", "register:40f0:8", ["const:5d41e4:8", "const:4:8"]]
+ 005d41e4 ["CALL", null, ["callee:00c57e90:8"]]
- 005d41a4 bytes 3b0e1a94
+ 005d41e4 bytes 2b0f1a94
- 005d4210 ["COPY", "register:0:8", ["register:4048:8"]]
- 005d4210 ["INT_ADD", "register:40f0:8", ["const:5d4210:8", "const:4:8"]]
- 005d4210 ["CALLIND", null, ["register:0:8"]]
+ 005d4250 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d4250 ["INT_ADD", "register:40f0:8", ["const:5d4250:8", "const:4:8"]]
+ 005d4250 ["CALLIND", null, ["register:0:8"]]
- 005d4210 bytes 20013fd6
+ 005d4250 bytes 20013fd6
- 005d426c ["INT_ADD", "register:40f0:8", ["const:5d426c:8", "const:4:8"]]
- 005d426c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d42ac ["INT_ADD", "register:40f0:8", ["const:5d42ac:8", "const:4:8"]]
+ 005d42ac ["CALL", null, ["callee:00c57eb0:8"]]
- 005d426c bytes 110e1a94
+ 005d42ac bytes 010f1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec39138a67af32172da0c565aa608e5a"></a>

### [`005d4348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md) → [`005d4388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4388.md) FUN_005d4388

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d43cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md#insn-005d43cc) · [`005d43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md#insn-005d43f4) · [`005d442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md#insn-005d442c)
- 新版 `005d440c`（命令位置の公開資料なし） · `005d4434`（命令位置の公開資料なし） · `005d446c`（命令位置の公開資料なし）

~~~diff
- 005d43cc ["INT_ADD", "register:40f0:8", ["const:5d43cc:8", "const:4:8"]]
- 005d43cc ["CALL", null, ["callee:00c57e90:8"]]
+ 005d440c ["INT_ADD", "register:40f0:8", ["const:5d440c:8", "const:4:8"]]
+ 005d440c ["CALL", null, ["callee:00c57e90:8"]]
- 005d43cc bytes b10d1a94
+ 005d440c bytes a10e1a94
- 005d43f4 ["INT_ADD", "register:40f0:8", ["const:5d43f4:8", "const:4:8"]]
- 005d43f4 ["CALL", null, ["callee:00c58000:8"]]
+ 005d4434 ["INT_ADD", "register:40f0:8", ["const:5d4434:8", "const:4:8"]]
+ 005d4434 ["CALL", null, ["callee:00c58000:8"]]
- 005d43f4 bytes 030e1a94
+ 005d4434 bytes f30e1a94
- 005d442c ["COPY", "register:0:8", ["register:4040:8"]]
- 005d442c ["INT_ADD", "register:40f0:8", ["const:5d442c:8", "const:4:8"]]
- 005d442c ["CALLIND", null, ["register:0:8"]]
+ 005d446c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d446c ["INT_ADD", "register:40f0:8", ["const:5d446c:8", "const:4:8"]]
+ 005d446c ["CALLIND", null, ["register:0:8"]]
- 005d442c bytes 00013fd6
+ 005d446c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

