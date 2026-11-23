# v15.7.4 → v16.0.0 · 要調査の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-9eeea7dd37f43ece64013fddd4c667e0"></a>

### [`004e6250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6250.md) → [`005090e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005090e8.md) FUN_005090e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6250.md#insn-004e626c)
- 新版 `00509104`（命令位置の公開資料なし）

~~~diff
- 004e626c ["INT_ADD", "register:40f0:8", ["const:4e626c:8", "const:4:8"]]
- 004e626c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00509104 ["INT_ADD", "register:40f0:8", ["const:509104:8", "const:4:8"]]
+ 00509104 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e626c bytes 7dd31b94
+ 00509104 bytes 6b3a1d94
~~~


<a id="compare-89513ab72fe7e0ff652221c4bc94d7e6"></a>

### [`004e68c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e68c8.md) → [`00509760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509760.md) _ZN5BotanneERKNS_7X509_DNES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e68d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e68c8.md#insn-004e68d0)
- 新版 `00509768`（命令位置の公開資料なし）

~~~diff
- 004e68d0 ["INT_ADD", "register:40f0:8", ["const:4e68d0:8", "const:4:8"]]
- 004e68d0 ["CALL", null, ["callee:00c59610:8"]]
+ 00509768 ["INT_ADD", "register:40f0:8", ["const:509768:8", "const:4:8"]]
+ 00509768 ["CALL", null, ["callee:00c59610:8"]]
- 004e68d0 bytes bcd81b94
+ 00509768 bytes aa3f1d94
~~~


<a id="compare-e34aed0bb667a638d596e7545f8215b7"></a>

### [`004e6ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6ca0.md) → [`00509b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509b38.md) _ZNK5Botan4OCSP7Request13base64_encodeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd80.md) [`00bdcd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c587d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587d0.md) [`00c597b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e6cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6ca0.md#insn-004e6cc4) · [`004e6cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6ca0.md#insn-004e6cd4) · [`004e6ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6ca0.md#insn-004e6ce4)
- 新版 `00509b5c`（命令位置の公開資料なし） · `00509b6c`（命令位置の公開資料なし） · `00509b7c`（命令位置の公開資料なし）

~~~diff
- 004e6cc4 ["INT_ADD", "register:40f0:8", ["const:4e6cc4:8", "const:4:8"]]
- 004e6cc4 ["CALL", null, ["callee:00c597b0:8"]]
+ 00509b5c ["INT_ADD", "register:40f0:8", ["const:509b5c:8", "const:4:8"]]
+ 00509b5c ["CALL", null, ["callee:00c597b0:8"]]
- 004e6cc4 bytes 27d81b94
+ 00509b5c bytes 153f1d94
- 004e6cd4 ["INT_ADD", "register:40f0:8", ["const:4e6cd4:8", "const:4:8"]]
- 004e6cd4 ["CALL", null, ["callee:00c587d0:8"]]
+ 00509b6c ["INT_ADD", "register:40f0:8", ["const:509b6c:8", "const:4:8"]]
+ 00509b6c ["CALL", null, ["callee:00c587d0:8"]]
- 004e6cd4 bytes 2bd41b94
+ 00509b6c bytes 193b1d94
- 004e6ce4 ["INT_ADD", "register:40f0:8", ["const:4e6ce4:8", "const:4:8"]]
- 004e6ce4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00509b7c ["INT_ADD", "register:40f0:8", ["const:509b7c:8", "const:4:8"]]
+ 00509b7c ["CALL", null, ["callee:00c57ab0:8"]]
- 004e6ce4 bytes dfd01b94
+ 00509b7c bytes cd371d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07825085fc398fae74f123a43cfe7f1e"></a>

### [`004e8484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8484.md) → [`0050b31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md) FUN_0050b31c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) · 呼出先 2件 [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) · 呼出先 2件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e84a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8484.md#insn-004e84a0) · [`004e84d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8484.md#insn-004e84d8)
- 新版 `0050b338`（命令位置の公開資料なし） · `0050b370`（命令位置の公開資料なし）

~~~diff
- 004e84a0 ["INT_ADD", "register:40f0:8", ["const:4e84a0:8", "const:4:8"]]
- 004e84a0 ["CALL", null, ["callee:0053b3e4:8"]]
+ 0050b338 ["INT_ADD", "register:40f0:8", ["const:50b338:8", "const:4:8"]]
+ 0050b338 ["CALL", null, ["callee:0053b3e4:8"]]
- 004e84a0 bytes 2bc00094
+ 0050b338 bytes 2bc00094
- 004e84d8 ["INT_ADD", "register:40f0:8", ["const:4e84d8:8", "const:4:8"]]
- 004e84d8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0050b370 ["INT_ADD", "register:40f0:8", ["const:50b370:8", "const:4:8"]]
+ 0050b370 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e84d8 bytes e2ca1b94
+ 0050b370 bytes d0311d94
~~~


<a id="compare-1256289e41c1abfd45ce5a923abecbd3"></a>

### [`004e8508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8508.md) → [`0050b3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b3a0.md) FUN_0050b3a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d764.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005405fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e8540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8508.md#insn-004e8540)
- 新版 `0050b3d8`（命令位置の公開資料なし）

~~~diff
- 004e8540 ["INT_ADD", "register:40f0:8", ["const:4e8540:8", "const:4:8"]]
- 004e8540 ["CALL", null, ["callee:005405fc:8"]]
+ 0050b3d8 ["INT_ADD", "register:40f0:8", ["const:50b3d8:8", "const:4:8"]]
+ 0050b3d8 ["CALL", null, ["callee:005405fc:8"]]
- 004e8540 bytes 89d40094
+ 0050b3d8 bytes 89d40094
~~~


<a id="compare-76f303ad63d9f5c6e08ee26d0788729b"></a>

### [`004e8574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8574.md) → [`0050b40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b40c.md) FUN_0050b40c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e85b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8574.md#insn-004e85b4)
- 新版 `0050b44c`（命令位置の公開資料なし）

~~~diff
- 004e85b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e85b4 ["INT_ADD", "register:40f0:8", ["const:4e85b4:8", "const:4:8"]]
- 004e85b4 ["CALLIND", null, ["register:0:8"]]
+ 0050b44c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050b44c ["INT_ADD", "register:40f0:8", ["const:50b44c:8", "const:4:8"]]
+ 0050b44c ["CALLIND", null, ["register:0:8"]]
- 004e85b4 bytes 00013fd6
+ 0050b44c bytes 00013fd6
~~~


<a id="compare-0d29108ccbf381774e082de8c3490835"></a>

### [`004e9100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9100.md) → [`0050bf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bf98.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_15Key_ConstraintsE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e9114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9100.md#insn-004e9114) · [`004e9124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9100.md#insn-004e9124)
- 新版 `0050bfac`（命令位置の公開資料なし） · `0050bfbc`（命令位置の公開資料なし）

~~~diff
- 004e9114 ["INT_ADD", "register:40f0:8", ["const:4e9114:8", "const:4:8"]]
- 004e9114 ["CALL", null, ["callee:00c595f0:8"]]
+ 0050bfac ["INT_ADD", "register:40f0:8", ["const:50bfac:8", "const:4:8"]]
+ 0050bfac ["CALL", null, ["callee:00c595f0:8"]]
- 004e9114 bytes a3ce1b94
+ 0050bfac bytes 91351d94
- 004e9124 ["INT_ADD", "register:40f0:8", ["const:4e9124:8", "const:4:8"]]
- 004e9124 ["CALL", null, ["callee:00c595f0:8"]]
+ 0050bfbc ["INT_ADD", "register:40f0:8", ["const:50bfbc:8", "const:4:8"]]
+ 0050bfbc ["CALL", null, ["callee:00c595f0:8"]]
- 004e9124 bytes 9fce1b94
+ 0050bfbc bytes 8d351d94
~~~


<a id="compare-e3fc162a2c297f951cfddd59347fc595"></a>

### [`004e9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9148.md) → [`0050bfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bfe0.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdf0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 1件 [`00c59840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59840.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e9170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9148.md#insn-004e9170) · [`004e9178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9148.md#insn-004e9178) · [`004e91ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9148.md#insn-004e91ec)
- 新版 `0050c008`（命令位置の公開資料なし） · `0050c010`（命令位置の公開資料なし） · `0050c084`（命令位置の公開資料なし）

~~~diff
- 004e9170 ["INT_ADD", "register:40f0:8", ["const:4e9170:8", "const:4:8"]]
- 004e9170 ["CALL", null, ["callee:00c58280:8"]]
+ 0050c008 ["INT_ADD", "register:40f0:8", ["const:50c008:8", "const:4:8"]]
+ 0050c008 ["CALL", null, ["callee:00c58280:8"]]
- 004e9170 bytes b0c91b94
+ 0050c008 bytes 9e301d94
- 004e9178 ["INT_ADD", "register:40f0:8", ["const:4e9178:8", "const:4:8"]]
- 004e9178 ["CALL", null, ["callee:00c595f0:8"]]
+ 0050c010 ["INT_ADD", "register:40f0:8", ["const:50c010:8", "const:4:8"]]
+ 0050c010 ["CALL", null, ["callee:00c595f0:8"]]
- 004e9178 bytes 8ace1b94
+ 0050c010 bytes 78351d94
- 004e91ec ["INT_ADD", "register:40f0:8", ["const:4e91ec:8", "const:4:8"]]
- 004e91ec ["CALL", null, ["callee:00c57ab0:8"]]
+ 0050c084 ["INT_ADD", "register:40f0:8", ["const:50c084:8", "const:4:8"]]
+ 0050c084 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e91ec bytes 9dc71b94
+ 0050c084 bytes 8b2e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee76f95b8db61888050646a3a8f716c5"></a>

### [`004e9d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9d34.md) → [`0050cbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbcc.md) _ZNK5Botan16X509_Certificate13raw_issuer_dnEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e9d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9d34.md#insn-004e9d3c)
- 新版 `0050cbd4`（命令位置の公開資料なし）

~~~diff
- 004e9d3c ["INT_ADD", "register:40f0:8", ["const:4e9d3c:8", "const:4:8"]]
- 004e9d3c ["CALL", null, ["callee:00c595f0:8"]]
+ 0050cbd4 ["INT_ADD", "register:40f0:8", ["const:50cbd4:8", "const:4:8"]]
+ 0050cbd4 ["CALL", null, ["callee:00c595f0:8"]]
- 004e9d3c bytes 99cb1b94
+ 0050cbd4 bytes 87321d94
~~~


<a id="compare-13c2ff99f3f111da32461796710ef3d3"></a>

### [`004e9d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9d4c.md) → [`0050cbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbe4.md) _ZNK5Botan4OCSP6CertID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md) [`00bdb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb880.md) [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md) [`00bdbcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md) [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md) [`00c58710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e9d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9d4c.md#insn-004e9d6c) · [`004e9d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9d4c.md#insn-004e9d80) · [`004e9d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9d4c.md#insn-004e9d98)
- 新版 `0050cc04`（命令位置の公開資料なし） · `0050cc18`（命令位置の公開資料なし） · `0050cc30`（命令位置の公開資料なし）

~~~diff
- 004e9d6c ["INT_ADD", "register:40f0:8", ["const:4e9d6c:8", "const:4:8"]]
- 004e9d6c ["CALL", null, ["callee:00c582b0:8"]]
+ 0050cc04 ["INT_ADD", "register:40f0:8", ["const:50cc04:8", "const:4:8"]]
+ 0050cc04 ["CALL", null, ["callee:00c582b0:8"]]
- 004e9d6c bytes bdc61b94
+ 0050cc04 bytes ab2d1d94
- 004e9d80 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e9d80 ["INT_ADD", "register:40f0:8", ["const:4e9d80:8", "const:4:8"]]
- 004e9d80 ["CALLIND", null, ["register:0:8"]]
+ 0050cc18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050cc18 ["INT_ADD", "register:40f0:8", ["const:50cc18:8", "const:4:8"]]
+ 0050cc18 ["CALLIND", null, ["register:0:8"]]
- 004e9d80 bytes 00013fd6
+ 0050cc18 bytes 00013fd6
- 004e9d98 ["INT_ADD", "register:40f0:8", ["const:4e9d98:8", "const:4:8"]]
- 004e9d98 ["CALL", null, ["callee:00c58420:8"]]
+ 0050cc30 ["INT_ADD", "register:40f0:8", ["const:50cc30:8", "const:4:8"]]
+ 0050cc30 ["CALL", null, ["callee:00c58420:8"]]
- 004e9d98 bytes 0ec71b94
+ 0050cc30 bytes fc2d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adc60238bc32994f4bede00c3a1ef09c"></a>

### [`004eae78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eae78.md) → [`0050dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd10.md) FUN_0050dd10

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004eae94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eae78.md#insn-004eae94) · [`004eaeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eae78.md#insn-004eaeb4)
- 新版 `0050dd2c`（命令位置の公開資料なし） · `0050dd4c`（命令位置の公開資料なし）

~~~diff
- 004eae94 ["INT_ADD", "register:40f0:8", ["const:4eae94:8", "const:4:8"]]
- 004eae94 ["CALL", null, ["callee:00c538e0:8"]]
+ 0050dd2c ["INT_ADD", "register:40f0:8", ["const:50dd2c:8", "const:4:8"]]
+ 0050dd2c ["CALL", null, ["callee:00c538e0:8"]]
- 004eae94 bytes ffaf1b94
+ 0050dd2c bytes ed161d94
- 004eaeb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004eaeb4 ["INT_ADD", "register:40f0:8", ["const:4eaeb4:8", "const:4:8"]]
- 004eaeb4 ["CALLIND", null, ["register:0:8"]]
+ 0050dd4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050dd4c ["INT_ADD", "register:40f0:8", ["const:50dd4c:8", "const:4:8"]]
+ 0050dd4c ["CALLIND", null, ["register:0:8"]]
- 004eaeb4 bytes 00013fd6
+ 0050dd4c bytes 00013fd6
~~~


<a id="compare-05f887f0dbb5091b95eab52c4d4a5a53"></a>

### [`004ec194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec194.md) → [`0050f02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f02c.md) FUN_0050f02c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00527554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527554.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054a3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec194.md#insn-004ec1b0)
- 新版 `0050f048`（命令位置の公開資料なし）

~~~diff
- 004ec1b0 ["INT_ADD", "register:40f0:8", ["const:4ec1b0:8", "const:4:8"]]
- 004ec1b0 ["CALL", null, ["callee:0054a3ec:8"]]
+ 0050f048 ["INT_ADD", "register:40f0:8", ["const:50f048:8", "const:4:8"]]
+ 0050f048 ["CALL", null, ["callee:0054a3ec:8"]]
- 004ec1b0 bytes e9ec0094
+ 0050f048 bytes e9ec0094
~~~


<a id="compare-356a7ec4e4a43e61db7325c057b553b4"></a>

### [`004ec2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec2cc.md) → [`0050f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f164.md) _ZNK5Botan14PKCS10_Request18challenge_passwordEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec2cc.md#insn-004ec2dc)
- 新版 `0050f174`（命令位置の公開資料なし）

~~~diff
- 004ec2dc ["INT_ADD", "register:40f0:8", ["const:4ec2dc:8", "const:4:8"]]
- 004ec2dc ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f174 ["INT_ADD", "register:40f0:8", ["const:50f174:8", "const:4:8"]]
+ 0050f174 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec2dc bytes e5c21b94
+ 0050f174 bytes d3291d94
~~~


<a id="compare-c3c9d9299f87025b69548955d49c024b"></a>

### [`004ec320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec320.md) → [`0050f1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1b8.md) _ZNK5Botan14PKCS10_Request14raw_public_keyEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec320.md#insn-004ec328)
- 新版 `0050f1c0`（命令位置の公開資料なし）

~~~diff
- 004ec328 ["INT_ADD", "register:40f0:8", ["const:4ec328:8", "const:4:8"]]
- 004ec328 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f1c0 ["INT_ADD", "register:40f0:8", ["const:50f1c0:8", "const:4:8"]]
+ 0050f1c0 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec328 bytes d2c21b94
+ 0050f1c0 bytes c0291d94
~~~


<a id="compare-05d1adf1ec0a5f717874d946b78c200b"></a>

### [`004ec338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec338.md) → [`0050f1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1d0.md) _ZNK5Botan14PKCS10_Request16subject_alt_nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec338.md#insn-004ec340)
- 新版 `0050f1d8`（命令位置の公開資料なし）

~~~diff
- 004ec340 ["INT_ADD", "register:40f0:8", ["const:4ec340:8", "const:4:8"]]
- 004ec340 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f1d8 ["INT_ADD", "register:40f0:8", ["const:50f1d8:8", "const:4:8"]]
+ 0050f1d8 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec340 bytes ccc21b94
+ 0050f1d8 bytes ba291d94
~~~


<a id="compare-b61e945218a1fac2b81b901452d808ca"></a>

### [`004ec350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec350.md) → [`0050f1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1e8.md) _ZNK5Botan14PKCS10_Request10extensionsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec350.md#insn-004ec358)
- 新版 `0050f1f0`（命令位置の公開資料なし）

~~~diff
- 004ec358 ["INT_ADD", "register:40f0:8", ["const:4ec358:8", "const:4:8"]]
- 004ec358 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f1f0 ["INT_ADD", "register:40f0:8", ["const:50f1f0:8", "const:4:8"]]
+ 0050f1f0 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec358 bytes c6c21b94
+ 0050f1f0 bytes b4291d94
~~~


<a id="compare-ea7b61044019041d592711d66df20f18"></a>

### [`004ec4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec4e0.md) → [`0050f378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f378.md) _ZNK5Botan10Extensions3getERKNS_3OIDE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ec4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec4e0.md#insn-004ec4f0) · [`004ec500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec4e0.md#insn-004ec500)
- 新版 `0050f388`（命令位置の公開資料なし） · `0050f398`（命令位置の公開資料なし）

~~~diff
- 004ec4f0 ["INT_ADD", "register:40f0:8", ["const:4ec4f0:8", "const:4:8"]]
- 004ec4f0 ["CALL", null, ["callee:00c596c0:8"]]
+ 0050f388 ["INT_ADD", "register:40f0:8", ["const:50f388:8", "const:4:8"]]
+ 0050f388 ["CALL", null, ["callee:00c596c0:8"]]
- 004ec4f0 bytes e0c11b94
+ 0050f388 bytes ce281d94
- 004ec500 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ec500 ["INT_ADD", "register:40f0:8", ["const:4ec500:8", "const:4:8"]]
- 004ec500 ["CALLIND", null, ["register:0:8"]]
+ 0050f398 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f398 ["INT_ADD", "register:40f0:8", ["const:50f398:8", "const:4:8"]]
+ 0050f398 ["CALLIND", null, ["register:0:8"]]
- 004ec500 bytes 00013fd6
+ 0050f398 bytes 00013fd6
~~~


<a id="compare-67f87b8390f37e377723076fe76c7ec6"></a>

### [`004ed038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed038.md) → [`0050fed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fed0.md) _ZNK5Botan16X509_Certificate10is_CA_certEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ed040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed038.md#insn-004ed040)
- 新版 `0050fed8`（命令位置の公開資料なし）

~~~diff
- 004ed040 ["INT_ADD", "register:40f0:8", ["const:4ed040:8", "const:4:8"]]
- 004ed040 ["CALL", null, ["callee:00c595f0:8"]]
+ 0050fed8 ["INT_ADD", "register:40f0:8", ["const:50fed8:8", "const:4:8"]]
+ 0050fed8 ["CALL", null, ["callee:00c595f0:8"]]
- 004ed040 bytes d8be1b94
+ 0050fed8 bytes c6251d94
~~~


<a id="compare-b2820de1f56ee9a55edddfca26e50c4a"></a>

### [`004ed050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed050.md) → [`0050fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fee8.md) FUN_0050fee8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ecb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`0050fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ed074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed050.md#insn-004ed074) · [`004ed0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed050.md#insn-004ed0bc) · [`004ed0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed050.md#insn-004ed0dc)
- 新版 `0050ff0c`（命令位置の公開資料なし） · `0050ff54`（命令位置の公開資料なし） · `0050ff74`（命令位置の公開資料なし）

~~~diff
- 004ed074 ["INT_ADD", "register:40f0:8", ["const:4ed074:8", "const:4:8"]]
- 004ed074 ["CALL", null, ["callee:00c57be0:8"]]
+ 0050ff0c ["INT_ADD", "register:40f0:8", ["const:50ff0c:8", "const:4:8"]]
+ 0050ff0c ["CALL", null, ["callee:00c57be0:8"]]
- 004ed074 bytes 47b81b94
+ 0050ff0c bytes 351f1d94
- 004ed0bc ["INT_ADD", "register:40f0:8", ["const:4ed0bc:8", "const:4:8"]]
- 004ed0bc ["CALL", null, ["callee:00c57a90:8"]]
+ 0050ff54 ["INT_ADD", "register:40f0:8", ["const:50ff54:8", "const:4:8"]]
+ 0050ff54 ["CALL", null, ["callee:00c57a90:8"]]
- 004ed0bc bytes e1b71b94
+ 0050ff54 bytes cf1e1d94
- 004ed0dc ["INT_ADD", "register:40f0:8", ["const:4ed0dc:8", "const:4:8"]]
- 004ed0dc ["CALL", null, ["callee:00c57b40:8"]]
+ 0050ff74 ["INT_ADD", "register:40f0:8", ["const:50ff74:8", "const:4:8"]]
+ 0050ff74 ["CALL", null, ["callee:00c57b40:8"]]
- 004ed0dc bytes 05b81b94
+ 0050ff74 bytes f31e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee43bb4e11c3289f9c354b2eecabef9"></a>

### [`004ed144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed144.md) → [`0050ffdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050ffdc.md) FUN_0050ffdc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`00713660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00713/00713660.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 9件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`0073d764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073d/0073d764.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ed160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed144.md#insn-004ed160)
- 新版 `0050fff8`（命令位置の公開資料なし）

~~~diff
- 004ed160 ["INT_ADD", "register:40f0:8", ["const:4ed160:8", "const:4:8"]]
- 004ed160 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0050fff8 ["INT_ADD", "register:40f0:8", ["const:50fff8:8", "const:4:8"]]
+ 0050fff8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004ed160 bytes c0b71b94
+ 0050fff8 bytes ae1e1d94
~~~


<a id="compare-84d99123fb9cc8dd1adb79ca13a9ab1b"></a>

### [`004ee760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee760.md) → [`005115f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005115f8.md) FUN_005115f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ee7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee760.md#insn-004ee7a8)
- 新版 `00511640`（命令位置の公開資料なし）

~~~diff
- 004ee7a8 ["INT_ADD", "register:40f0:8", ["const:4ee7a8:8", "const:4:8"]]
- 004ee7a8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00511640 ["INT_ADD", "register:40f0:8", ["const:511640:8", "const:4:8"]]
+ 00511640 ["CALL", null, ["callee:00c57ab0:8"]]
- 004ee7a8 bytes 2eb21b94
+ 00511640 bytes 1c191d94
~~~


<a id="compare-78e24fb8b5ef3cdd4b4a6e0ac0f5d329"></a>

### [`004eedec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eedec.md) → [`00511c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511c84.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md) [`00bdcf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004eee20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eedec.md#insn-004eee20) · [`004eee48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eedec.md#insn-004eee48) · [`004eee98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eedec.md#insn-004eee98)
- 新版 `00511cb8`（命令位置の公開資料なし） · `00511ce0`（命令位置の公開資料なし） · `00511d30`（命令位置の公開資料なし）

~~~diff
- 004eee20 ["INT_ADD", "register:40f0:8", ["const:4eee20:8", "const:4:8"]]
- 004eee20 ["CALL", null, ["callee:00c58180:8"]]
+ 00511cb8 ["INT_ADD", "register:40f0:8", ["const:511cb8:8", "const:4:8"]]
+ 00511cb8 ["CALL", null, ["callee:00c58180:8"]]
- 004eee20 bytes 44b21b94
+ 00511cb8 bytes 32191d94
- 004eee48 ["INT_ADD", "register:40f0:8", ["const:4eee48:8", "const:4:8"]]
- 004eee48 ["CALL", null, ["callee:00c59970:8"]]
+ 00511ce0 ["INT_ADD", "register:40f0:8", ["const:511ce0:8", "const:4:8"]]
+ 00511ce0 ["CALL", null, ["callee:00c59970:8"]]
- 004eee48 bytes 36b81b94
+ 00511ce0 bytes 241f1d94
- 004eee98 ["INT_ADD", "register:40f0:8", ["const:4eee98:8", "const:4:8"]]
- 004eee98 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00511d30 ["INT_ADD", "register:40f0:8", ["const:511d30:8", "const:4:8"]]
+ 00511d30 ["CALL", null, ["callee:00c57ae0:8"]]
- 004eee98 bytes 7eb01b94
+ 00511d30 bytes 6c171d94
~~~


<a id="compare-c80d53c36787ddc7d19d74d7397ab4ca"></a>

### [`004eee9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eee9c.md) → [`00511d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511d34.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorENSt6__ndk16chrono10time_pointINS4_12system_clockENS4_8durationIxNS3_5ratioILl1ELl1000

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004eeed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eee9c.md#insn-004eeed4) · [`004eef20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eee9c.md#insn-004eef20)
- 新版 `00511d6c`（命令位置の公開資料なし） · `00511db8`（命令位置の公開資料なし）

~~~diff
- 004eeed4 ["INT_ADD", "register:40f0:8", ["const:4eeed4:8", "const:4:8"]]
- 004eeed4 ["CALL", null, ["callee:00c59970:8"]]
+ 00511d6c ["INT_ADD", "register:40f0:8", ["const:511d6c:8", "const:4:8"]]
+ 00511d6c ["CALL", null, ["callee:00c59970:8"]]
- 004eeed4 bytes 13b81b94
+ 00511d6c bytes 011f1d94
- 004eef20 ["INT_ADD", "register:40f0:8", ["const:4eef20:8", "const:4:8"]]
- 004eef20 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00511db8 ["INT_ADD", "register:40f0:8", ["const:511db8:8", "const:4:8"]]
+ 00511db8 ["CALL", null, ["callee:00c57ae0:8"]]
- 004eef20 bytes 5cb01b94
+ 00511db8 bytes 4a171d94
~~~


<a id="compare-bf49ab85d2d76c987599bb8c5d8bf9f7"></a>

### [`004eef24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eef24.md) → [`00511dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511dbc.md) _ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md) [`00bdcf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004eef50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eef24.md#insn-004eef50)
- 新版 `00511de8`（命令位置の公開資料なし）

~~~diff
- 004eef50 ["INT_ADD", "register:40f0:8", ["const:4eef50:8", "const:4:8"]]
- 004eef50 ["CALL", null, ["callee:00c58180:8"]]
+ 00511de8 ["INT_ADD", "register:40f0:8", ["const:511de8:8", "const:4:8"]]
+ 00511de8 ["CALL", null, ["callee:00c58180:8"]]
- 004eef50 bytes f8b11b94
+ 00511de8 bytes e6181d94
~~~


<a id="compare-832b569154857bc9e34459b1d4a6da8e"></a>

### [`004ef7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef7b8.md) → [`00512650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512650.md) FUN_00512650

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ef804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef7b8.md#insn-004ef804) · [`004ef818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef7b8.md#insn-004ef818) · [`004ef820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef7b8.md#insn-004ef820)
- 新版 `0051269c`（命令位置の公開資料なし） · `005126b0`（命令位置の公開資料なし） · `005126b8`（命令位置の公開資料なし）

~~~diff
- 004ef804 ["INT_ADD", "register:40f0:8", ["const:4ef804:8", "const:4:8"]]
- 004ef804 ["CALL", null, ["callee:00c538e0:8"]]
+ 0051269c ["INT_ADD", "register:40f0:8", ["const:51269c:8", "const:4:8"]]
+ 0051269c ["CALL", null, ["callee:00c538e0:8"]]
- 004ef804 bytes a39d1b94
+ 0051269c bytes 91041d94
- 004ef818 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ef818 ["INT_ADD", "register:40f0:8", ["const:4ef818:8", "const:4:8"]]
- 004ef818 ["CALLIND", null, ["register:0:8"]]
+ 005126b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005126b0 ["INT_ADD", "register:40f0:8", ["const:5126b0:8", "const:4:8"]]
+ 005126b0 ["CALLIND", null, ["register:0:8"]]
- 004ef818 bytes 00013fd6
+ 005126b0 bytes 00013fd6
- 004ef820 ["INT_ADD", "register:40f0:8", ["const:4ef820:8", "const:4:8"]]
- 004ef820 ["CALL", null, ["callee:00c57a80:8"]]
+ 005126b8 ["INT_ADD", "register:40f0:8", ["const:5126b8:8", "const:4:8"]]
+ 005126b8 ["CALL", null, ["callee:00c57a80:8"]]
- 004ef820 bytes 04ae1b94
+ 005126b8 bytes f2141d94
~~~


<a id="compare-0b271470e18dc1b46381e66424b86ae0"></a>

### [`004ef850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef850.md) → [`005126e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005126e8.md) _ZNK5Botan8X509_CRL11get_revokedEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ef858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef850.md#insn-004ef858)
- 新版 `005126f0`（命令位置の公開資料なし）

~~~diff
- 004ef858 ["INT_ADD", "register:40f0:8", ["const:4ef858:8", "const:4:8"]]
- 004ef858 ["CALL", null, ["callee:00c59650:8"]]
+ 005126f0 ["INT_ADD", "register:40f0:8", ["const:5126f0:8", "const:4:8"]]
+ 005126f0 ["CALL", null, ["callee:00c59650:8"]]
- 004ef858 bytes eab41b94
+ 005126f0 bytes d81b1d94
~~~


<a id="compare-c4e89e627a41eccb9a6f1b12aba55aac"></a>

### [`004ef868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef868.md) → [`00512700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512700.md) _ZNK5Botan8X509_CRL10crl_numberEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ef870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef868.md#insn-004ef870)
- 新版 `00512708`（命令位置の公開資料なし）

~~~diff
- 004ef870 ["INT_ADD", "register:40f0:8", ["const:4ef870:8", "const:4:8"]]
- 004ef870 ["CALL", null, ["callee:00c59650:8"]]
+ 00512708 ["INT_ADD", "register:40f0:8", ["const:512708:8", "const:4:8"]]
+ 00512708 ["CALL", null, ["callee:00c59650:8"]]
- 004ef870 bytes e4b41b94
+ 00512708 bytes d21b1d94
~~~


<a id="compare-d5c698924061ccdea633bc21a45ab1ba"></a>

### [`004ef8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef8d4.md) → [`0051276c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051276c.md) _ZN5Botan17choose_sig_formatERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorI

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ef910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef8d4.md#insn-004ef910) · [`004ef920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef8d4.md#insn-004ef920) · [`004ef970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef8d4.md#insn-004ef970)
- 新版 `005127a8`（命令位置の公開資料なし） · `005127b8`（命令位置の公開資料なし） · `00512808`（命令位置の公開資料なし）

~~~diff
- 004ef910 ["INT_ADD", "register:40f0:8", ["const:4ef910:8", "const:4:8"]]
- 004ef910 ["CALL", null, ["callee:00510020:8"]]
+ 005127a8 ["INT_ADD", "register:40f0:8", ["const:5127a8:8", "const:4:8"]]
+ 005127a8 ["CALL", null, ["callee:00510020:8"]]
- 004ef910 bytes 1ef6ff97
+ 005127a8 bytes 1ef6ff97
- 004ef920 ["INT_ADD", "register:40f0:8", ["const:4ef920:8", "const:4:8"]]
- 004ef920 ["CALL", null, ["callee:0046d450:8"]]
+ 005127b8 ["INT_ADD", "register:40f0:8", ["const:5127b8:8", "const:4:8"]]
+ 005127b8 ["CALL", null, ["callee:0046d450:8"]]
- 004ef920 bytes 266bfd97
+ 005127b8 bytes 266bfd97
- 004ef970 ["INT_ADD", "register:40f0:8", ["const:4ef970:8", "const:4:8"]]
- 004ef970 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00512808 ["INT_ADD", "register:40f0:8", ["const:512808:8", "const:4:8"]]
+ 00512808 ["CALL", null, ["callee:00c57ae0:8"]]
- 004ef970 bytes c8ad1b94
+ 00512808 bytes b6141d94
~~~


<a id="compare-a95737dfe8fae51d8f46179d13e5f224"></a>

### [`004ef998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef998.md) → [`00512830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512830.md) _ZNK5Botan8X509_CRL20alternate_PEM_labelsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ef9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef998.md#insn-004ef9d4) · [`004ef9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef998.md#insn-004ef9e4) · [`004efa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef998.md#insn-004efa34)
- 新版 `0051286c`（命令位置の公開資料なし） · `0051287c`（命令位置の公開資料なし） · `005128cc`（命令位置の公開資料なし）

~~~diff
- 004ef9d4 ["INT_ADD", "register:40f0:8", ["const:4ef9d4:8", "const:4:8"]]
- 004ef9d4 ["CALL", null, ["callee:00473500:8"]]
+ 0051286c ["INT_ADD", "register:40f0:8", ["const:51286c:8", "const:4:8"]]
+ 0051286c ["CALL", null, ["callee:00473500:8"]]
- 004ef9d4 bytes 2583fd97
+ 0051286c bytes 2583fd97
- 004ef9e4 ["INT_ADD", "register:40f0:8", ["const:4ef9e4:8", "const:4:8"]]
- 004ef9e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051287c ["INT_ADD", "register:40f0:8", ["const:51287c:8", "const:4:8"]]
+ 0051287c ["CALL", null, ["callee:00c57ab0:8"]]
- 004ef9e4 bytes 9fad1b94
+ 0051287c bytes 8d141d94
- 004efa34 ["INT_ADD", "register:40f0:8", ["const:4efa34:8", "const:4:8"]]
- 004efa34 ["CALL", null, ["callee:00c57ae0:8"]]
+ 005128cc ["INT_ADD", "register:40f0:8", ["const:5128cc:8", "const:4:8"]]
+ 005128cc ["CALL", null, ["callee:00c57ae0:8"]]
- 004efa34 bytes 97ad1b94
+ 005128cc bytes 85141d94
~~~


<a id="compare-a7db0ecc566ec11ba0f3493a221c90de"></a>

### [`004efb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb3c.md) → [`005129d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005129d4.md) FUN_005129d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004efb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb3c.md#insn-004efb58) · [`004efb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb3c.md#insn-004efb78)
- 新版 `005129f0`（命令位置の公開資料なし） · `00512a10`（命令位置の公開資料なし）

~~~diff
- 004efb58 ["INT_ADD", "register:40f0:8", ["const:4efb58:8", "const:4:8"]]
- 004efb58 ["CALL", null, ["callee:00c538e0:8"]]
+ 005129f0 ["INT_ADD", "register:40f0:8", ["const:5129f0:8", "const:4:8"]]
+ 005129f0 ["CALL", null, ["callee:00c538e0:8"]]
- 004efb58 bytes ce9c1b94
+ 005129f0 bytes bc031d94
- 004efb78 ["COPY", "register:0:8", ["register:4040:8"]]
- 004efb78 ["INT_ADD", "register:40f0:8", ["const:4efb78:8", "const:4:8"]]
- 004efb78 ["CALLIND", null, ["register:0:8"]]
+ 00512a10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00512a10 ["INT_ADD", "register:40f0:8", ["const:512a10:8", "const:4:8"]]
+ 00512a10 ["CALLIND", null, ["register:0:8"]]
- 004efb78 bytes 00013fd6
+ 00512a10 bytes 00013fd6
~~~


<a id="compare-59ac728b90b23ec0b6dcb34f6ce79f02"></a>

### [`004f00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f00b0.md) → [`00512f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512f48.md) _ZNK5Botan8X509_CRL10is_revokedERKNS_16X509_CertificateE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf50.md) · 呼出先 10件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c599a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599a0.md) · 呼出先 10件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f00e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f00b0.md#insn-004f00e8) · [`004f00f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f00b0.md#insn-004f00f4) · [`004f0100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f00b0.md#insn-004f0100)
- 新版 `00512f80`（命令位置の公開資料なし） · `00512f8c`（命令位置の公開資料なし） · `00512f98`（命令位置の公開資料なし）

~~~diff
- 004f00e8 ["INT_ADD", "register:40f0:8", ["const:4f00e8:8", "const:4:8"]]
- 004f00e8 ["CALL", null, ["callee:00c595f0:8"]]
+ 00512f80 ["INT_ADD", "register:40f0:8", ["const:512f80:8", "const:4:8"]]
+ 00512f80 ["CALL", null, ["callee:00c595f0:8"]]
- 004f00e8 bytes aeb21b94
+ 00512f80 bytes 9c191d94
- 004f00f4 ["INT_ADD", "register:40f0:8", ["const:4f00f4:8", "const:4:8"]]
- 004f00f4 ["CALL", null, ["callee:00c59650:8"]]
+ 00512f8c ["INT_ADD", "register:40f0:8", ["const:512f8c:8", "const:4:8"]]
+ 00512f8c ["CALL", null, ["callee:00c59650:8"]]
- 004f00f4 bytes c3b21b94
+ 00512f8c bytes b1191d94
- 004f0100 ["INT_ADD", "register:40f0:8", ["const:4f0100:8", "const:4:8"]]
- 004f0100 ["CALL", null, ["callee:00c59610:8"]]
+ 00512f98 ["INT_ADD", "register:40f0:8", ["const:512f98:8", "const:4:8"]]
+ 00512f98 ["CALL", null, ["callee:00c59610:8"]]
- 004f0100 bytes b0b21b94
+ 00512f98 bytes 9e191d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e51e6fce6479be6c3562dbd8d0bfd9ea"></a>

### [`004f0f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f3c.md) → [`00513dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513dd4.md) FUN_00513dd4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00527b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527b74.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054aa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f0f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f3c.md#insn-004f0f58)
- 新版 `00513df0`（命令位置の公開資料なし）

~~~diff
- 004f0f58 ["INT_ADD", "register:40f0:8", ["const:4f0f58:8", "const:4:8"]]
- 004f0f58 ["CALL", null, ["callee:0054aa0c:8"]]
+ 00513df0 ["INT_ADD", "register:40f0:8", ["const:513df0:8", "const:4:8"]]
+ 00513df0 ["CALL", null, ["callee:0054aa0c:8"]]
- 004f0f58 bytes 07db0094
+ 00513df0 bytes 07db0094
~~~


<a id="compare-99bccca6248fdec8355604a2b506dafa"></a>

### [`004f1074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1074.md) → [`00513f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f0c.md) _ZNK5Botan8X509_CRL10extensionsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f107c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1074.md#insn-004f107c)
- 新版 `00513f14`（命令位置の公開資料なし）

~~~diff
- 004f107c ["INT_ADD", "register:40f0:8", ["const:4f107c:8", "const:4:8"]]
- 004f107c ["CALL", null, ["callee:00c59650:8"]]
+ 00513f14 ["INT_ADD", "register:40f0:8", ["const:513f14:8", "const:4:8"]]
+ 00513f14 ["CALL", null, ["callee:00c59650:8"]]
- 004f107c bytes e1ae1b94
+ 00513f14 bytes cf151d94
~~~


<a id="compare-ca4077a1ac6c0195db2a6cc5f9f55ded"></a>

### [`004f108c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f108c.md) → [`00513f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f24.md) _ZNK5Botan8X509_CRL11next_updateEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f108c.md#insn-004f1094)
- 新版 `00513f2c`（命令位置の公開資料なし）

~~~diff
- 004f1094 ["INT_ADD", "register:40f0:8", ["const:4f1094:8", "const:4:8"]]
- 004f1094 ["CALL", null, ["callee:00c59650:8"]]
+ 00513f2c ["INT_ADD", "register:40f0:8", ["const:513f2c:8", "const:4:8"]]
+ 00513f2c ["CALL", null, ["callee:00c59650:8"]]
- 004f1094 bytes dbae1b94
+ 00513f2c bytes c9151d94
~~~


<a id="compare-1e46b9d1d256f32b2acabad35e56e277"></a>

### [`004f10a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10a4.md) → [`00513f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f3c.md) _ZNK5Botan8X509_CRL30crl_issuing_distribution_pointEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f10b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10a4.md#insn-004f10b4)
- 新版 `00513f4c`（命令位置の公開資料なし）

~~~diff
- 004f10b4 ["INT_ADD", "register:40f0:8", ["const:4f10b4:8", "const:4:8"]]
- 004f10b4 ["CALL", null, ["callee:00c59650:8"]]
+ 00513f4c ["INT_ADD", "register:40f0:8", ["const:513f4c:8", "const:4:8"]]
+ 00513f4c ["CALL", null, ["callee:00c59650:8"]]
- 004f10b4 bytes d3ae1b94
+ 00513f4c bytes c1151d94
~~~


<a id="compare-debeb8389564d356dc44bd88a64637fd"></a>

### [`004f11e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md) → [`00514078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md) _ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdccb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccb0.md) · 呼出先 6件 [`004dc4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md) [`00527fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527fd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md) · 呼出先 6件 [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) [`0054ae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ae6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md#insn-004f1230) · [`004f12c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md#insn-004f12c4) · [`004f1304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md#insn-004f1304)
- 新版 `005140c8`（命令位置の公開資料なし） · `0051415c`（命令位置の公開資料なし） · `0051419c`（命令位置の公開資料なし）

~~~diff
- 004f1230 ["INT_ADD", "register:40f0:8", ["const:4f1230:8", "const:4:8"]]
- 004f1230 ["CALL", null, ["callee:0054ae6c:8"]]
+ 005140c8 ["INT_ADD", "register:40f0:8", ["const:5140c8:8", "const:4:8"]]
+ 005140c8 ["CALL", null, ["callee:0054ae6c:8"]]
- 004f1230 bytes 69db0094
+ 005140c8 bytes 69db0094
- 004f12c4 ["INT_ADD", "register:40f0:8", ["const:4f12c4:8", "const:4:8"]]
- 004f12c4 ["CALL", null, ["callee:00c57c50:8"]]
+ 0051415c ["INT_ADD", "register:40f0:8", ["const:51415c:8", "const:4:8"]]
+ 0051415c ["CALL", null, ["callee:00c57c50:8"]]
- 004f12c4 bytes cfa71b94
+ 0051415c bytes bd0e1d94
- 004f1304 ["INT_ADD", "register:40f0:8", ["const:4f1304:8", "const:4:8"]]
- 004f1304 ["CALL", null, ["callee:00c584f0:8"]]
+ 0051419c ["INT_ADD", "register:40f0:8", ["const:51419c:8", "const:4:8"]]
+ 0051419c ["CALL", null, ["callee:00c584f0:8"]]
- 004f1304 bytes e7a91b94
+ 0051419c bytes d5101d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb321ecf06a2c1be2b50e64484d7f630"></a>

### [`004f14f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f14f4.md) → [`0051438c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051438c.md) _ZNK5Botan7X509_DN8contentsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb60.md) · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md) [`00bdba60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba60.md)
- 新版 呼出元 1件 [`00c595b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595b0.md) · 呼出先 5件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58400.md) [`00c584b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f14f4.md#insn-004f1570) · [`004f1594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f14f4.md#insn-004f1594) · [`004f15a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f14f4.md#insn-004f15a4)
- 新版 `00514408`（命令位置の公開資料なし） · `0051442c`（命令位置の公開資料なし） · `0051443c`（命令位置の公開資料なし）

~~~diff
- 004f1570 ["INT_ADD", "register:40f0:8", ["const:4f1570:8", "const:4:8"]]
- 004f1570 ["CALL", null, ["callee:00c584b0:8"]]
+ 00514408 ["INT_ADD", "register:40f0:8", ["const:514408:8", "const:4:8"]]
+ 00514408 ["CALL", null, ["callee:00c584b0:8"]]
- 004f1570 bytes 3ca91b94
+ 00514408 bytes 2a101d94
- 004f1594 ["INT_ADD", "register:40f0:8", ["const:4f1594:8", "const:4:8"]]
- 004f1594 ["CALL", null, ["callee:00c58400:8"]]
+ 0051442c ["INT_ADD", "register:40f0:8", ["const:51442c:8", "const:4:8"]]
+ 0051442c ["CALL", null, ["callee:00c58400:8"]]
- 004f1594 bytes 07a91b94
+ 0051442c bytes f50f1d94
- 004f15a4 ["INT_ADD", "register:40f0:8", ["const:4f15a4:8", "const:4:8"]]
- 004f15a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051443c ["INT_ADD", "register:40f0:8", ["const:51443c:8", "const:4:8"]]
+ 0051443c ["CALL", null, ["callee:00c57ab0:8"]]
- 004f15a4 bytes afa61b94
+ 0051443c bytes 9d0d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba0f4bb8fcdf471d571c318ce43aeb6"></a>

### [`004f1650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1650.md) → [`005144e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005144e8.md) _ZNK5Botan7X509_DN9has_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf70.md) · 呼出先 5件 [`0052839c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052839c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd20.md)
- 新版 呼出元 1件 [`00c599c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599c0.md) · 呼出先 5件 [`0054b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b234.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f167c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1650.md#insn-004f167c) · [`004f1688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1650.md#insn-004f1688) · [`004f1698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1650.md#insn-004f1698)
- 新版 `00514514`（命令位置の公開資料なし） · `00514520`（命令位置の公開資料なし） · `00514530`（命令位置の公開資料なし）

~~~diff
- 004f167c ["INT_ADD", "register:40f0:8", ["const:4f167c:8", "const:4:8"]]
- 004f167c ["CALL", null, ["callee:00c59770:8"]]
+ 00514514 ["INT_ADD", "register:40f0:8", ["const:514514:8", "const:4:8"]]
+ 00514514 ["CALL", null, ["callee:00c59770:8"]]
- 004f167c bytes a9ad1b94
+ 00514514 bytes 97141d94
- 004f1688 ["INT_ADD", "register:40f0:8", ["const:4f1688:8", "const:4:8"]]
- 004f1688 ["CALL", null, ["callee:00c58280:8"]]
+ 00514520 ["INT_ADD", "register:40f0:8", ["const:514520:8", "const:4:8"]]
+ 00514520 ["CALL", null, ["callee:00c58280:8"]]
- 004f1688 bytes 6aa81b94
+ 00514520 bytes 580f1d94
- 004f1698 ["INT_ADD", "register:40f0:8", ["const:4f1698:8", "const:4:8"]]
- 004f1698 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00514530 ["INT_ADD", "register:40f0:8", ["const:514530:8", "const:4:8"]]
+ 00514530 ["CALL", null, ["callee:00c57ab0:8"]]
- 004f1698 bytes 72a61b94
+ 00514530 bytes 600d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c997914533288dd3c2aaf8b9ba10d64"></a>

### [`004f1a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1a6c.md) → [`00514904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514904.md) _ZNK5Botan7X509_DN19get_first_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd20.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1a6c.md#insn-004f1a9c) · [`004f1aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1a6c.md#insn-004f1aa8) · [`004f1ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1a6c.md#insn-004f1ab8)
- 新版 `00514934`（命令位置の公開資料なし） · `00514940`（命令位置の公開資料なし） · `00514950`（命令位置の公開資料なし）

~~~diff
- 004f1a9c ["INT_ADD", "register:40f0:8", ["const:4f1a9c:8", "const:4:8"]]
- 004f1a9c ["CALL", null, ["callee:00c59770:8"]]
+ 00514934 ["INT_ADD", "register:40f0:8", ["const:514934:8", "const:4:8"]]
+ 00514934 ["CALL", null, ["callee:00c59770:8"]]
- 004f1a9c bytes a1ac1b94
+ 00514934 bytes 8f131d94
- 004f1aa8 ["INT_ADD", "register:40f0:8", ["const:4f1aa8:8", "const:4:8"]]
- 004f1aa8 ["CALL", null, ["callee:00c58280:8"]]
+ 00514940 ["INT_ADD", "register:40f0:8", ["const:514940:8", "const:4:8"]]
+ 00514940 ["CALL", null, ["callee:00c58280:8"]]
- 004f1aa8 bytes 62a71b94
+ 00514940 bytes 500e1d94
- 004f1ab8 ["INT_ADD", "register:40f0:8", ["const:4f1ab8:8", "const:4:8"]]
- 004f1ab8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00514950 ["INT_ADD", "register:40f0:8", ["const:514950:8", "const:4:8"]]
+ 00514950 ["CALL", null, ["callee:00c57ab0:8"]]
- 004f1ab8 bytes 6aa51b94
+ 00514950 bytes 580c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b65c24e34000636654cba679ec68dcab"></a>

### [`004f1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1c30.md) → [`00514ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514ac8.md) _ZN5BotanltERKNS_7X509_DNES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00526790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdcbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c59620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f1c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1c30.md#insn-004f1c64) · [`004f1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1c30.md#insn-004f1c70) · [`004f1dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1c30.md#insn-004f1dcc)
- 新版 `00514afc`（命令位置の公開資料なし） · `00514b08`（命令位置の公開資料なし） · `00514c64`（命令位置の公開資料なし）

~~~diff
- 004f1c64 ["INT_ADD", "register:40f0:8", ["const:4f1c64:8", "const:4:8"]]
- 004f1c64 ["CALL", null, ["callee:00c59620:8"]]
+ 00514afc ["INT_ADD", "register:40f0:8", ["const:514afc:8", "const:4:8"]]
+ 00514afc ["CALL", null, ["callee:00c59620:8"]]
- 004f1c64 bytes dbab1b94
+ 00514afc bytes c9121d94
- 004f1c70 ["INT_ADD", "register:40f0:8", ["const:4f1c70:8", "const:4:8"]]
- 004f1c70 ["CALL", null, ["callee:00c59620:8"]]
+ 00514b08 ["INT_ADD", "register:40f0:8", ["const:514b08:8", "const:4:8"]]
+ 00514b08 ["CALL", null, ["callee:00c59620:8"]]
- 004f1c70 bytes d8ab1b94
+ 00514b08 bytes c6121d94
- 004f1dcc ["INT_ADD", "register:40f0:8", ["const:4f1dcc:8", "const:4:8"]]
- 004f1dcc ["CALL", null, ["callee:00c57c50:8"]]
+ 00514c64 ["INT_ADD", "register:40f0:8", ["const:514c64:8", "const:4:8"]]
+ 00514c64 ["CALL", null, ["callee:00c57c50:8"]]
- 004f1dcc bytes 0da51b94
+ 00514c64 bytes fb0b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-065fa5ada00aa767107a57169595fe5f"></a>

### [`004f25dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md) → [`00515474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) FUN_00515474

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052c558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0052855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052855c.md) [`005288f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005288f8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0054f3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054b3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b3f4.md) [`0054b790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f262c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md#insn-004f262c) · [`004f265c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md#insn-004f265c) · [`004f2678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md#insn-004f2678)
- 新版 `005154c4`（命令位置の公開資料なし） · `005154f4`（命令位置の公開資料なし） · `00515510`（命令位置の公開資料なし）

~~~diff
- 004f262c ["INT_ADD", "register:40f0:8", ["const:4f262c:8", "const:4:8"]]
- 004f262c ["CALL", null, ["callee:0043bb64:8"]]
+ 005154c4 ["INT_ADD", "register:40f0:8", ["const:5154c4:8", "const:4:8"]]
+ 005154c4 ["CALL", null, ["callee:0043bb64:8"]]
- 004f262c bytes 8e9afc97
+ 005154c4 bytes a899fc97
- 004f265c ["INT_ADD", "register:40f0:8", ["const:4f265c:8", "const:4:8"]]
- 004f265c ["CALL", null, ["callee:0054b3f4:8"]]
+ 005154f4 ["INT_ADD", "register:40f0:8", ["const:5154f4:8", "const:4:8"]]
+ 005154f4 ["CALL", null, ["callee:0054b3f4:8"]]
- 004f265c bytes c0d70094
+ 005154f4 bytes c0d70094
- 004f2678 ["INT_ADD", "register:40f0:8", ["const:4f2678:8", "const:4:8"]]
- 004f2678 ["CALL", null, ["callee:0054b790:8"]]
+ 00515510 ["INT_ADD", "register:40f0:8", ["const:515510:8", "const:4:8"]]
+ 00515510 ["CALL", null, ["callee:0054b790:8"]]
- 004f2678 bytes a0d80094
+ 00515510 bytes a0d80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10c6002be5b7cbc18da55306e244d72e"></a>

### [`004f3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3cec.md) → [`00516b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md) FUN_00516b84

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004e01ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md) [`004ee4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00503084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f3d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3cec.md#insn-004f3d08) · [`004f3d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3cec.md#insn-004f3d1c) · [`004f3d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3cec.md#insn-004f3d3c)
- 新版 `00516ba0`（命令位置の公開資料なし） · `00516bb4`（命令位置の公開資料なし） · `00516bd4`（命令位置の公開資料なし）

~~~diff
- 004f3d08 ["INT_ADD", "register:40f0:8", ["const:4f3d08:8", "const:4:8"]]
- 004f3d08 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00516ba0 ["INT_ADD", "register:40f0:8", ["const:516ba0:8", "const:4:8"]]
+ 00516ba0 ["CALL", null, ["callee:00c57ab0:8"]]
- 004f3d08 bytes d69c1b94
+ 00516ba0 bytes c4031d94
- 004f3d1c ["INT_ADD", "register:40f0:8", ["const:4f3d1c:8", "const:4:8"]]
- 004f3d1c ["CALL", null, ["callee:00c538e0:8"]]
+ 00516bb4 ["INT_ADD", "register:40f0:8", ["const:516bb4:8", "const:4:8"]]
+ 00516bb4 ["CALL", null, ["callee:00c538e0:8"]]
- 004f3d1c bytes 5d8c1b94
+ 00516bb4 bytes 4bf31c94
- 004f3d3c ["COPY", "register:0:8", ["register:4040:8"]]
- 004f3d3c ["INT_ADD", "register:40f0:8", ["const:4f3d3c:8", "const:4:8"]]
- 004f3d3c ["CALLIND", null, ["register:0:8"]]
+ 00516bd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00516bd4 ["INT_ADD", "register:40f0:8", ["const:516bd4:8", "const:4:8"]]
+ 00516bd4 ["CALLIND", null, ["register:0:8"]]
- 004f3d3c bytes 00013fd6
+ 00516bd4 bytes 00013fd6
~~~


<a id="compare-c13288a2fe2c03321258c8f24498be96"></a>

### [`004f41bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f41bc.md) → [`00517054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517054.md) FUN_00517054

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f4208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f41bc.md#insn-004f4208)
- 新版 `005170a0`（命令位置の公開資料なし）

~~~diff
- 004f4208 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f4208 ["INT_ADD", "register:40f0:8", ["const:4f4208:8", "const:4:8"]]
- 004f4208 ["CALLIND", null, ["register:0:8"]]
+ 005170a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005170a0 ["INT_ADD", "register:40f0:8", ["const:5170a0:8", "const:4:8"]]
+ 005170a0 ["CALLIND", null, ["register:0:8"]]
- 004f4208 bytes 00013fd6
+ 005170a0 bytes 00013fd6
~~~


<a id="compare-c24486776c0c67a991f74d095af5483d"></a>

### [`004f4238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4238.md) → [`005170d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md) _ZNK5Botan10Extensions14extensions_rawEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`005293c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/005293c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0054c258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c258.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f42dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4238.md#insn-004f42dc) · [`004f42f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4238.md#insn-004f42f4) · [`004f4310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4238.md#insn-004f4310)
- 新版 `00517174`（命令位置の公開資料なし） · `0051718c`（命令位置の公開資料なし） · `005171a8`（命令位置の公開資料なし）

~~~diff
- 004f42dc ["INT_ADD", "register:40f0:8", ["const:4f42dc:8", "const:4:8"]]
- 004f42dc ["CALL", null, ["callee:00c57a90:8"]]
+ 00517174 ["INT_ADD", "register:40f0:8", ["const:517174:8", "const:4:8"]]
+ 00517174 ["CALL", null, ["callee:00c57a90:8"]]
- 004f42dc bytes 599b1b94
+ 00517174 bytes 47021d94
- 004f42f4 ["INT_ADD", "register:40f0:8", ["const:4f42f4:8", "const:4:8"]]
- 004f42f4 ["CALL", null, ["callee:00c57c00:8"]]
+ 0051718c ["INT_ADD", "register:40f0:8", ["const:51718c:8", "const:4:8"]]
+ 0051718c ["CALL", null, ["callee:00c57c00:8"]]
- 004f42f4 bytes af9b1b94
+ 0051718c bytes 9d021d94
- 004f4310 ["INT_ADD", "register:40f0:8", ["const:4f4310:8", "const:4:8"]]
- 004f4310 ["CALL", null, ["callee:0054c258:8"]]
+ 005171a8 ["INT_ADD", "register:40f0:8", ["const:5171a8:8", "const:4:8"]]
+ 005171a8 ["CALL", null, ["callee:0054c258:8"]]
- 004f4310 bytes 2cd40094
+ 005171a8 bytes 2cd40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cae886d87190d35abab91be3dcb53fc"></a>

### [`004f46fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f46fc.md) → [`00517594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517594.md) FUN_00517594

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f4718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f46fc.md#insn-004f4718) · [`004f472c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f46fc.md#insn-004f472c) · [`004f4758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f46fc.md#insn-004f4758)
- 新版 `005175b0`（命令位置の公開資料なし） · `005175c4`（命令位置の公開資料なし） · `005175f0`（命令位置の公開資料なし）

~~~diff
- 004f4718 ["INT_ADD", "register:40f0:8", ["const:4f4718:8", "const:4:8"]]
- 004f4718 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005175b0 ["INT_ADD", "register:40f0:8", ["const:5175b0:8", "const:4:8"]]
+ 005175b0 ["CALL", null, ["callee:00c57ab0:8"]]
- 004f4718 bytes 529a1b94
+ 005175b0 bytes 40011d94
- 004f472c ["INT_ADD", "register:40f0:8", ["const:4f472c:8", "const:4:8"]]
- 004f472c ["CALL", null, ["callee:00c538e0:8"]]
+ 005175c4 ["INT_ADD", "register:40f0:8", ["const:5175c4:8", "const:4:8"]]
+ 005175c4 ["CALL", null, ["callee:00c538e0:8"]]
- 004f472c bytes d9891b94
+ 005175c4 bytes c7f01c94
- 004f4758 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f4758 ["INT_ADD", "register:40f0:8", ["const:4f4758:8", "const:4:8"]]
- 004f4758 ["CALLIND", null, ["register:0:8"]]
+ 005175f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005175f0 ["INT_ADD", "register:40f0:8", ["const:5175f0:8", "const:4:8"]]
+ 005175f0 ["CALLIND", null, ["register:0:8"]]
- 004f4758 bytes 00013fd6
+ 005175f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff5567777f9125b8eb5318877ee8a9b2"></a>

### [`004f6b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6b24.md) → [`005199bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005199bc.md) _ZNK5Botan14Cert_Extension24Subject_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00518c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59570.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f6b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6b24.md#insn-004f6b54) · [`004f6b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6b24.md#insn-004f6b70) · [`004f6bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6b24.md#insn-004f6bac)
- 新版 `005199ec`（命令位置の公開資料なし） · `00519a08`（命令位置の公開資料なし） · `00519a44`（命令位置の公開資料なし）

~~~diff
- 004f6b54 ["INT_ADD", "register:40f0:8", ["const:4f6b54:8", "const:4:8"]]
- 004f6b54 ["CALL", null, ["callee:00c59570:8"]]
+ 005199ec ["INT_ADD", "register:40f0:8", ["const:5199ec:8", "const:4:8"]]
+ 005199ec ["CALL", null, ["callee:00c59570:8"]]
- 004f6b54 bytes f3971b94
+ 005199ec bytes e1fe1c94
- 004f6b70 ["INT_ADD", "register:40f0:8", ["const:4f6b70:8", "const:4:8"]]
- 004f6b70 ["CALL", null, ["callee:0046d450:8"]]
+ 00519a08 ["INT_ADD", "register:40f0:8", ["const:519a08:8", "const:4:8"]]
+ 00519a08 ["CALL", null, ["callee:0046d450:8"]]
- 004f6b70 bytes 924efd97
+ 00519a08 bytes 924efd97
- 004f6bac ["INT_ADD", "register:40f0:8", ["const:4f6bac:8", "const:4:8"]]
- 004f6bac ["CALL", null, ["callee:0053bb30:8"]]
+ 00519a44 ["INT_ADD", "register:40f0:8", ["const:519a44:8", "const:4:8"]]
+ 00519a44 ["CALL", null, ["callee:0053bb30:8"]]
- 004f6bac bytes 3b880094
+ 00519a44 bytes 3b880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0d3cfa04a3156ef90dec77304716f08"></a>

### [`004f6c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6c0c.md) → [`00519aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519aa4.md) _ZNK5Botan14Cert_Extension23Issuer_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00518c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59570.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6c0c.md#insn-004f6c3c) · [`004f6c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6c0c.md#insn-004f6c58) · [`004f6c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6c0c.md#insn-004f6c94)
- 新版 `00519ad4`（命令位置の公開資料なし） · `00519af0`（命令位置の公開資料なし） · `00519b2c`（命令位置の公開資料なし）

~~~diff
- 004f6c3c ["INT_ADD", "register:40f0:8", ["const:4f6c3c:8", "const:4:8"]]
- 004f6c3c ["CALL", null, ["callee:00c59570:8"]]
+ 00519ad4 ["INT_ADD", "register:40f0:8", ["const:519ad4:8", "const:4:8"]]
+ 00519ad4 ["CALL", null, ["callee:00c59570:8"]]
- 004f6c3c bytes b9971b94
+ 00519ad4 bytes a7fe1c94
- 004f6c58 ["INT_ADD", "register:40f0:8", ["const:4f6c58:8", "const:4:8"]]
- 004f6c58 ["CALL", null, ["callee:0046d450:8"]]
+ 00519af0 ["INT_ADD", "register:40f0:8", ["const:519af0:8", "const:4:8"]]
+ 00519af0 ["CALL", null, ["callee:0046d450:8"]]
- 004f6c58 bytes 584efd97
+ 00519af0 bytes 584efd97
- 004f6c94 ["INT_ADD", "register:40f0:8", ["const:4f6c94:8", "const:4:8"]]
- 004f6c94 ["CALL", null, ["callee:0053bb30:8"]]
+ 00519b2c ["INT_ADD", "register:40f0:8", ["const:519b2c:8", "const:4:8"]]
+ 00519b2c ["CALL", null, ["callee:0053bb30:8"]]
- 004f6c94 bytes 01880094
+ 00519b2c bytes 01880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52252c157974bffd9a639e5468734804"></a>

### [`004f7afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md) → [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) FUN_0051a994

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004f73a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f73a8.md) · 呼出先 7件 [`004f7ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7ecc.md) [`0051a888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a888.md) [`0051a920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a920.md) [`0051a934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a934.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 1件 [`0051a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md) · 呼出先 7件 [`0051ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ad64.md) [`0053d720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d720.md) [`0053d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md) [`0053d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7cc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f7b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md#insn-004f7b74) · [`004f7b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md#insn-004f7b98) · [`004f7be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md#insn-004f7be4)
- 新版 `0051aa0c`（命令位置の公開資料なし） · `0051aa30`（命令位置の公開資料なし） · `0051aa7c`（命令位置の公開資料なし）

~~~diff
- 004f7b74 ["INT_ADD", "register:40f0:8", ["const:4f7b74:8", "const:4:8"]]
- 004f7b74 ["CALL", null, ["callee:00c57a90:8"]]
+ 0051aa0c ["INT_ADD", "register:40f0:8", ["const:51aa0c:8", "const:4:8"]]
+ 0051aa0c ["CALL", null, ["callee:00c57a90:8"]]
- 004f7b74 bytes 338d1b94
+ 0051aa0c bytes 21f41c94
- 004f7b98 ["INT_ADD", "register:40f0:8", ["const:4f7b98:8", "const:4:8"]]
- 004f7b98 ["CALL", null, ["callee:0053d7cc:8"]]
+ 0051aa30 ["INT_ADD", "register:40f0:8", ["const:51aa30:8", "const:4:8"]]
+ 0051aa30 ["CALL", null, ["callee:0053d7cc:8"]]
- 004f7b98 bytes 678b0094
+ 0051aa30 bytes 678b0094
- 004f7be4 ["INT_ADD", "register:40f0:8", ["const:4f7be4:8", "const:4:8"]]
- 004f7be4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0051aa7c ["INT_ADD", "register:40f0:8", ["const:51aa7c:8", "const:4:8"]]
+ 0051aa7c ["CALL", null, ["callee:00c57a90:8"]]
- 004f7be4 bytes 178d1b94
+ 0051aa7c bytes 05f41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af09a56f9b38054df539f98c7f4af5fb"></a>

### [`004f7cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7cc4.md) → [`0051ab5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ab5c.md) FUN_0051ab5c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004f73a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f73a8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0051a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f7d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7cc4.md#insn-004f7d14) · [`004f7d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7cc4.md#insn-004f7d24) · [`004f7d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7cc4.md#insn-004f7d34)
- 新版 `0051abac`（命令位置の公開資料なし） · `0051abbc`（命令位置の公開資料なし） · `0051abcc`（命令位置の公開資料なし）

~~~diff
- 004f7d14 ["INT_ADD", "register:40f0:8", ["const:4f7d14:8", "const:4:8"]]
- 004f7d14 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051abac ["INT_ADD", "register:40f0:8", ["const:51abac:8", "const:4:8"]]
+ 0051abac ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7d14 bytes d38c1b94
+ 0051abac bytes c1f31c94
- 004f7d24 ["INT_ADD", "register:40f0:8", ["const:4f7d24:8", "const:4:8"]]
- 004f7d24 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051abbc ["INT_ADD", "register:40f0:8", ["const:51abbc:8", "const:4:8"]]
+ 0051abbc ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7d24 bytes cf8c1b94
+ 0051abbc bytes bdf31c94
- 004f7d34 ["INT_ADD", "register:40f0:8", ["const:4f7d34:8", "const:4:8"]]
- 004f7d34 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051abcc ["INT_ADD", "register:40f0:8", ["const:51abcc:8", "const:4:8"]]
+ 0051abcc ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7d34 bytes cb8c1b94
+ 0051abcc bytes b9f31c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b6c5dc987196ac2d65713922a5a6030"></a>

### [`004f7dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md) → [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) FUN_0051ac84

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004f73a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f73a8.md) [`0050ee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee54.md) [`0050ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee5c.md) [`0052a5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0051a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md) [`00531cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531cec.md) [`00531cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531cf4.md) [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f7e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md#insn-004f7e34) · [`004f7e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md#insn-004f7e44) · [`004f7e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md#insn-004f7e54)
- 新版 `0051accc`（命令位置の公開資料なし） · `0051acdc`（命令位置の公開資料なし） · `0051acec`（命令位置の公開資料なし）

~~~diff
- 004f7e34 ["INT_ADD", "register:40f0:8", ["const:4f7e34:8", "const:4:8"]]
- 004f7e34 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051accc ["INT_ADD", "register:40f0:8", ["const:51accc:8", "const:4:8"]]
+ 0051accc ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7e34 bytes 8b8c1b94
+ 0051accc bytes 79f31c94
- 004f7e44 ["INT_ADD", "register:40f0:8", ["const:4f7e44:8", "const:4:8"]]
- 004f7e44 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051acdc ["INT_ADD", "register:40f0:8", ["const:51acdc:8", "const:4:8"]]
+ 0051acdc ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7e44 bytes 878c1b94
+ 0051acdc bytes 75f31c94
- 004f7e54 ["INT_ADD", "register:40f0:8", ["const:4f7e54:8", "const:4:8"]]
- 004f7e54 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051acec ["INT_ADD", "register:40f0:8", ["const:51acec:8", "const:4:8"]]
+ 0051acec ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7e54 bytes 838c1b94
+ 0051acec bytes 71f31c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7c9d1cb2e07f0957ae520008773e4f"></a>

### [`004f7ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7ecc.md) → [`0051ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ad64.md) FUN_0051ad64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004f7afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md) [`0051ca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ca38.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f7f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7ecc.md#insn-004f7f14) · [`004f7f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7ecc.md#insn-004f7f24)
- 新版 `0051adac`（命令位置の公開資料なし） · `0051adbc`（命令位置の公開資料なし）

~~~diff
- 004f7f14 ["INT_ADD", "register:40f0:8", ["const:4f7f14:8", "const:4:8"]]
- 004f7f14 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051adac ["INT_ADD", "register:40f0:8", ["const:51adac:8", "const:4:8"]]
+ 0051adac ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7f14 bytes 538c1b94
+ 0051adac bytes 41f31c94
- 004f7f24 ["INT_ADD", "register:40f0:8", ["const:4f7f24:8", "const:4:8"]]
- 004f7f24 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051adbc ["INT_ADD", "register:40f0:8", ["const:51adbc:8", "const:4:8"]]
+ 0051adbc ["CALL", null, ["callee:00c57ab0:8"]]
- 004f7f24 bytes 4f8c1b94
+ 0051adbc bytes 3df31c94
~~~


<a id="compare-b79e17749212301923e6ef8121c7b322"></a>

### [`004f8990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8990.md) → [`0051b828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b828.md) _ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd000.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 1件 [`00c59a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a50.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f89b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8990.md#insn-004f89b4) · [`004f89c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8990.md#insn-004f89c4) · [`004f8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8990.md#insn-004f8ac4)
- 新版 `0051b84c`（命令位置の公開資料なし） · `0051b85c`（命令位置の公開資料なし） · `0051b95c`（命令位置の公開資料なし）

~~~diff
- 004f89b4 ["INT_ADD", "register:40f0:8", ["const:4f89b4:8", "const:4:8"]]
- 004f89b4 ["CALL", null, ["callee:00c595f0:8"]]
+ 0051b84c ["INT_ADD", "register:40f0:8", ["const:51b84c:8", "const:4:8"]]
+ 0051b84c ["CALL", null, ["callee:00c595f0:8"]]
- 004f89b4 bytes 7b901b94
+ 0051b84c bytes 69f71c94
- 004f89c4 ["INT_ADD", "register:40f0:8", ["const:4f89c4:8", "const:4:8"]]
- 004f89c4 ["CALL", null, ["callee:00c58280:8"]]
+ 0051b85c ["INT_ADD", "register:40f0:8", ["const:51b85c:8", "const:4:8"]]
+ 0051b85c ["CALL", null, ["callee:00c58280:8"]]
- 004f89c4 bytes 9b8b1b94
+ 0051b85c bytes 89f21c94
- 004f8ac4 ["INT_ADD", "register:40f0:8", ["const:4f8ac4:8", "const:4:8"]]
- 004f8ac4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051b95c ["INT_ADD", "register:40f0:8", ["const:51b95c:8", "const:4:8"]]
+ 0051b95c ["CALL", null, ["callee:00c57ab0:8"]]
- 004f8ac4 bytes 67891b94
+ 0051b95c bytes 55f01c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0912852d102f49644fd26a7741b7ddc"></a>

### [`004f8afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8afc.md) → [`0051b994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b994.md) FUN_0051b994

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8afc.md#insn-004f8b64) · [`004f8b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8afc.md#insn-004f8b98)
- 新版 `0051b9fc`（命令位置の公開資料なし） · `0051ba30`（命令位置の公開資料なし）

~~~diff
- 004f8b64 ["INT_ADD", "register:40f0:8", ["const:4f8b64:8", "const:4:8"]]
- 004f8b64 ["CALL", null, ["callee:00c57a90:8"]]
+ 0051b9fc ["INT_ADD", "register:40f0:8", ["const:51b9fc:8", "const:4:8"]]
+ 0051b9fc ["CALL", null, ["callee:00c57a90:8"]]
- 004f8b64 bytes 37891b94
+ 0051b9fc bytes 25f01c94
- 004f8b98 ["INT_ADD", "register:40f0:8", ["const:4f8b98:8", "const:4:8"]]
- 004f8b98 ["CALL", null, ["callee:0043bb64:8"]]
+ 0051ba30 ["INT_ADD", "register:40f0:8", ["const:51ba30:8", "const:4:8"]]
+ 0051ba30 ["CALL", null, ["callee:0043bb64:8"]]
- 004f8b98 bytes 3381fc97
+ 0051ba30 bytes 4d80fc97
~~~


<a id="compare-6a91581f48711882ce07d035c44d8eee"></a>

### [`004f8bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8bcc.md) → [`0051ba64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051ba64.md) FUN_0051ba64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f8be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8bcc.md#insn-004f8be8)
- 新版 `0051ba80`（命令位置の公開資料なし）

~~~diff
- 004f8be8 ["INT_ADD", "register:40f0:8", ["const:4f8be8:8", "const:4:8"]]
- 004f8be8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051ba80 ["INT_ADD", "register:40f0:8", ["const:51ba80:8", "const:4:8"]]
+ 0051ba80 ["CALL", null, ["callee:00c57ab0:8"]]
- 004f8be8 bytes 1e891b94
+ 0051ba80 bytes 0cf01c94
~~~


<a id="compare-4ef29bb4892bfdcaecc8e7f124270971"></a>

### [`004f9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9118.md) → [`0051bfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051bfb0.md) FUN_0051bfb0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9118.md#insn-004f9160)
- 新版 `0051bff8`（命令位置の公開資料なし）

~~~diff
- 004f9160 ["INT_ADD", "register:40f0:8", ["const:4f9160:8", "const:4:8"]]
- 004f9160 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051bff8 ["INT_ADD", "register:40f0:8", ["const:51bff8:8", "const:4:8"]]
+ 0051bff8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004f9160 bytes c0871b94
+ 0051bff8 bytes aeee1c94
~~~


<a id="compare-d0009f0c7cf93154afe7b5014cb5ad67"></a>

### [`004f9934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9934.md) → [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) _ZN5Botan14Cert_Extension20Certificate_Policies8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocator

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004f9abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md) [`0051d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9e4.md) [`0052a214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a214.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0051c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) [`0054087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054087c.md) [`0054d0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9934.md#insn-004f996c) · [`004f9a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9934.md#insn-004f9a00) · [`004f9a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9934.md#insn-004f9a34)
- 新版 `0051c804`（命令位置の公開資料なし） · `0051c898`（命令位置の公開資料なし） · `0051c8cc`（命令位置の公開資料なし）

~~~diff
- 004f996c ["INT_ADD", "register:40f0:8", ["const:4f996c:8", "const:4:8"]]
- 004f996c ["CALL", null, ["callee:0051c954:8"]]
+ 0051c804 ["INT_ADD", "register:40f0:8", ["const:51c804:8", "const:4:8"]]
+ 0051c804 ["CALL", null, ["callee:0051c954:8"]]
- 004f996c bytes 54000094
+ 0051c804 bytes 54000094
- 004f9a00 ["INT_ADD", "register:40f0:8", ["const:4f9a00:8", "const:4:8"]]
- 004f9a00 ["CALL", null, ["callee:00c57a90:8"]]
+ 0051c898 ["INT_ADD", "register:40f0:8", ["const:51c898:8", "const:4:8"]]
+ 0051c898 ["CALL", null, ["callee:00c57a90:8"]]
- 004f9a00 bytes 90851b94
+ 0051c898 bytes 7eec1c94
- 004f9a34 ["INT_ADD", "register:40f0:8", ["const:4f9a34:8", "const:4:8"]]
- 004f9a34 ["CALL", null, ["callee:0043bb64:8"]]
+ 0051c8cc ["INT_ADD", "register:40f0:8", ["const:51c8cc:8", "const:4:8"]]
+ 0051c8cc ["CALL", null, ["callee:0043bb64:8"]]
- 004f9a34 bytes 8c7dfc97
+ 0051c8cc bytes a67cfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9be2c32468b360d758575bca2c0c01"></a>

### [`004f9abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md) → [`0051c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) FUN_0051c954

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004f9934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9934.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00529d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d5c.md) [`0052a0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054cbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbf4.md) [`0054cf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cf90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004f9b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md#insn-004f9b0c) · [`004f9b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md#insn-004f9b3c) · [`004f9b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md#insn-004f9b58)
- 新版 `0051c9a4`（命令位置の公開資料なし） · `0051c9d4`（命令位置の公開資料なし） · `0051c9f0`（命令位置の公開資料なし）

~~~diff
- 004f9b0c ["INT_ADD", "register:40f0:8", ["const:4f9b0c:8", "const:4:8"]]
- 004f9b0c ["CALL", null, ["callee:0043bb64:8"]]
+ 0051c9a4 ["INT_ADD", "register:40f0:8", ["const:51c9a4:8", "const:4:8"]]
+ 0051c9a4 ["CALL", null, ["callee:0043bb64:8"]]
- 004f9b0c bytes 567dfc97
+ 0051c9a4 bytes 707cfc97
- 004f9b3c ["INT_ADD", "register:40f0:8", ["const:4f9b3c:8", "const:4:8"]]
- 004f9b3c ["CALL", null, ["callee:0054cbf4:8"]]
+ 0051c9d4 ["INT_ADD", "register:40f0:8", ["const:51c9d4:8", "const:4:8"]]
+ 0051c9d4 ["CALL", null, ["callee:0054cbf4:8"]]
- 004f9b3c bytes 88c00094
+ 0051c9d4 bytes 88c00094
- 004f9b58 ["INT_ADD", "register:40f0:8", ["const:4f9b58:8", "const:4:8"]]
- 004f9b58 ["CALL", null, ["callee:0054cf90:8"]]
+ 0051c9f0 ["INT_ADD", "register:40f0:8", ["const:51c9f0:8", "const:4:8"]]
+ 0051c9f0 ["CALL", null, ["callee:0054cf90:8"]]
- 004f9b58 bytes 68c10094
+ 0051c9f0 bytes 68c10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90c625d50bc017d65d5b1ff6cac8976"></a>

### [`004fc170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc170.md) → [`0051f008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f008.md) _ZNK5Botan14Cert_Extension17Unknown_Extension12encode_innerEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fc1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc170.md#insn-004fc1a0) · [`004fc1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc170.md#insn-004fc1b8) · [`004fc1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc170.md#insn-004fc1d4)
- 新版 `0051f038`（命令位置の公開資料なし） · `0051f050`（命令位置の公開資料なし） · `0051f06c`（命令位置の公開資料なし）

~~~diff
- 004fc1a0 ["INT_ADD", "register:40f0:8", ["const:4fc1a0:8", "const:4:8"]]
- 004fc1a0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0051f038 ["INT_ADD", "register:40f0:8", ["const:51f038:8", "const:4:8"]]
+ 0051f038 ["CALL", null, ["callee:00c57a90:8"]]
- 004fc1a0 bytes a87b1b94
+ 0051f038 bytes 96e21c94
- 004fc1b8 ["INT_ADD", "register:40f0:8", ["const:4fc1b8:8", "const:4:8"]]
- 004fc1b8 ["CALL", null, ["callee:00c57c00:8"]]
+ 0051f050 ["INT_ADD", "register:40f0:8", ["const:51f050:8", "const:4:8"]]
+ 0051f050 ["CALL", null, ["callee:00c57c00:8"]]
- 004fc1b8 bytes fe7b1b94
+ 0051f050 bytes ece21c94
- 004fc1d4 ["INT_ADD", "register:40f0:8", ["const:4fc1d4:8", "const:4:8"]]
- 004fc1d4 ["CALL", null, ["callee:0049f3ec:8"]]
+ 0051f06c ["INT_ADD", "register:40f0:8", ["const:51f06c:8", "const:4:8"]]
+ 0051f06c ["CALL", null, ["callee:0049f3ec:8"]]
- 004fc1d4 bytes e000fe97
+ 0051f06c bytes e000fe97
~~~


<a id="compare-a26ab20d156e543a419e29321b65fdc7"></a>

### [`004fc21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc21c.md) → [`0051f0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f0b4.md) _ZNK5Botan11X509_Object11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb870.md) [`00bdb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb880.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582c0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fc244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc21c.md#insn-004fc244) · [`004fc254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc21c.md#insn-004fc254) · [`004fc270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc21c.md#insn-004fc270)
- 新版 `0051f0dc`（命令位置の公開資料なし） · `0051f0ec`（命令位置の公開資料なし） · `0051f108`（命令位置の公開資料なし）

~~~diff
- 004fc244 ["INT_ADD", "register:40f0:8", ["const:4fc244:8", "const:4:8"]]
- 004fc244 ["CALL", null, ["callee:00c582b0:8"]]
+ 0051f0dc ["INT_ADD", "register:40f0:8", ["const:51f0dc:8", "const:4:8"]]
+ 0051f0dc ["CALL", null, ["callee:00c582b0:8"]]
- 004fc244 bytes 877d1b94
+ 0051f0dc bytes 75e41c94
- 004fc254 ["INT_ADD", "register:40f0:8", ["const:4fc254:8", "const:4:8"]]
- 004fc254 ["CALL", null, ["callee:00c582b0:8"]]
+ 0051f0ec ["INT_ADD", "register:40f0:8", ["const:51f0ec:8", "const:4:8"]]
+ 0051f0ec ["CALL", null, ["callee:00c582b0:8"]]
- 004fc254 bytes 837d1b94
+ 0051f0ec bytes 71e41c94
- 004fc270 ["INT_ADD", "register:40f0:8", ["const:4fc270:8", "const:4:8"]]
- 004fc270 ["CALL", null, ["callee:00c582c0:8"]]
+ 0051f108 ["INT_ADD", "register:40f0:8", ["const:51f108:8", "const:4:8"]]
+ 0051f108 ["CALL", null, ["callee:00c582c0:8"]]
- 004fc270 bytes 807d1b94
+ 0051f108 bytes 6ee41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c02d6f84df1eda5d449cfcc0d34b91"></a>

### [`004fc5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc5bc.md) → [`0051f454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f454.md) _ZNK5Botan11X509_Object10PEM_encodeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdd030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c59a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fc5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc5bc.md#insn-004fc5e8) · [`004fc5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc5bc.md#insn-004fc5fc) · [`004fc614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc5bc.md#insn-004fc614)
- 新版 `0051f480`（命令位置の公開資料なし） · `0051f494`（命令位置の公開資料なし） · `0051f4ac`（命令位置の公開資料なし）

~~~diff
- 004fc5e8 ["INT_ADD", "register:40f0:8", ["const:4fc5e8:8", "const:4:8"]]
- 004fc5e8 ["CALL", null, ["callee:00c59a80:8"]]
+ 0051f480 ["INT_ADD", "register:40f0:8", ["const:51f480:8", "const:4:8"]]
+ 0051f480 ["CALL", null, ["callee:00c59a80:8"]]
- 004fc5e8 bytes 92821b94
+ 0051f480 bytes 80e91c94
- 004fc5fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004fc5fc ["INT_ADD", "register:40f0:8", ["const:4fc5fc:8", "const:4:8"]]
- 004fc5fc ["CALLIND", null, ["register:0:8"]]
+ 0051f494 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f494 ["INT_ADD", "register:40f0:8", ["const:51f494:8", "const:4:8"]]
+ 0051f494 ["CALLIND", null, ["register:0:8"]]
- 004fc5fc bytes 20013fd6
+ 0051f494 bytes 20013fd6
- 004fc614 ["INT_ADD", "register:40f0:8", ["const:4fc614:8", "const:4:8"]]
- 004fc614 ["CALL", null, ["callee:00c59090:8"]]
+ 0051f4ac ["INT_ADD", "register:40f0:8", ["const:51f4ac:8", "const:4:8"]]
+ 0051f4ac ["CALL", null, ["callee:00c59090:8"]]
- 004fc614 bytes 0b801b94
+ 0051f4ac bytes f9e61c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-affe585438c58ac360ca70aab1ca6894"></a>

### [`004fd0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd0d8.md) → [`0051ff70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051ff70.md) FUN_0051ff70

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd0d8.md#insn-004fd0f4) · [`004fd104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd0d8.md#insn-004fd104) · [`004fd114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd0d8.md#insn-004fd114)
- 新版 `0051ff8c`（命令位置の公開資料なし） · `0051ff9c`（命令位置の公開資料なし） · `0051ffac`（命令位置の公開資料なし）

~~~diff
- 004fd0f4 ["INT_ADD", "register:40f0:8", ["const:4fd0f4:8", "const:4:8"]]
- 004fd0f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051ff8c ["INT_ADD", "register:40f0:8", ["const:51ff8c:8", "const:4:8"]]
+ 0051ff8c ["CALL", null, ["callee:00c57ab0:8"]]
- 004fd0f4 bytes db771b94
+ 0051ff8c bytes c9de1c94
- 004fd104 ["INT_ADD", "register:40f0:8", ["const:4fd104:8", "const:4:8"]]
- 004fd104 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051ff9c ["INT_ADD", "register:40f0:8", ["const:51ff9c:8", "const:4:8"]]
+ 0051ff9c ["CALL", null, ["callee:00c57ab0:8"]]
- 004fd104 bytes d7771b94
+ 0051ff9c bytes c5de1c94
- 004fd114 ["INT_ADD", "register:40f0:8", ["const:4fd114:8", "const:4:8"]]
- 004fd114 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0051ffac ["INT_ADD", "register:40f0:8", ["const:51ffac:8", "const:4:8"]]
+ 0051ffac ["CALL", null, ["callee:00c57ab0:8"]]
- 004fd114 bytes d3771b94
+ 0051ffac bytes c1de1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81263b645d16c8c0b886d4ef653be86c"></a>

### [`004fd15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd15c.md) → [`0051fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051fff4.md) _ZNK5Botan11X509_Object15check_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdce60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c598b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fd164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd15c.md#insn-004fd164)
- 新版 `0051fffc`（命令位置の公開資料なし）

~~~diff
- 004fd164 ["INT_ADD", "register:40f0:8", ["const:4fd164:8", "const:4:8"]]
- 004fd164 ["CALL", null, ["callee:00c598b0:8"]]
+ 0051fffc ["INT_ADD", "register:40f0:8", ["const:51fffc:8", "const:4:8"]]
+ 0051fffc ["CALL", null, ["callee:00c598b0:8"]]
- 004fd164 bytes 3f7f1b94
+ 0051fffc bytes 2de61c94
~~~


<a id="compare-29d24c470f781a4ffd647676d2fe8418"></a>

### [`004fdce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdce4.md) → [`00520b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520b7c.md) FUN_00520b7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fdd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdce4.md#insn-004fdd00) · [`004fdd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdce4.md#insn-004fdd20)
- 新版 `00520b98`（命令位置の公開資料なし） · `00520bb8`（命令位置の公開資料なし）

~~~diff
- 004fdd00 ["INT_ADD", "register:40f0:8", ["const:4fdd00:8", "const:4:8"]]
- 004fdd00 ["CALL", null, ["callee:00c538e0:8"]]
+ 00520b98 ["INT_ADD", "register:40f0:8", ["const:520b98:8", "const:4:8"]]
+ 00520b98 ["CALL", null, ["callee:00c538e0:8"]]
- 004fdd00 bytes 64641b94
+ 00520b98 bytes 52cb1c94
- 004fdd20 ["COPY", "register:0:8", ["register:4040:8"]]
- 004fdd20 ["INT_ADD", "register:40f0:8", ["const:4fdd20:8", "const:4:8"]]
- 004fdd20 ["CALLIND", null, ["register:0:8"]]
+ 00520bb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00520bb8 ["INT_ADD", "register:40f0:8", ["const:520bb8:8", "const:4:8"]]
+ 00520bb8 ["CALLIND", null, ["register:0:8"]]
- 004fdd20 bytes 00013fd6
+ 00520bb8 bytes 00013fd6
~~~


<a id="compare-0e36351e4cf8be53110a968d59fba14f"></a>

### [`004ff950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ff950.md) → [`005227e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005227e8.md) FUN_005227e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052a5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ff96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ff950.md#insn-004ff96c)
- 新版 `00522804`（命令位置の公開資料なし）

~~~diff
- 004ff96c ["INT_ADD", "register:40f0:8", ["const:4ff96c:8", "const:4:8"]]
- 004ff96c ["CALL", null, ["callee:0054d464:8"]]
+ 00522804 ["INT_ADD", "register:40f0:8", ["const:522804:8", "const:4:8"]]
+ 00522804 ["CALL", null, ["callee:0054d464:8"]]
- 004ff96c bytes 18ab0094
+ 00522804 bytes 18ab0094
~~~


<a id="compare-2dbe464ef03d86f77919ae48a9470119"></a>

### [`004ffa88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffa88.md) → [`00522920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522920.md) _ZNK5Botan16X509_Certificate12x509_versionEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffa90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffa88.md#insn-004ffa90)
- 新版 `00522928`（命令位置の公開資料なし）

~~~diff
- 004ffa90 ["INT_ADD", "register:40f0:8", ["const:4ffa90:8", "const:4:8"]]
- 004ffa90 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522928 ["INT_ADD", "register:40f0:8", ["const:522928:8", "const:4:8"]]
+ 00522928 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffa90 bytes 44741b94
+ 00522928 bytes 32db1c94
~~~


<a id="compare-a04e02a6dd460db4481a01944cd3fcc4"></a>

### [`004ffaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffaa0.md) → [`00522938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522938.md) _ZNK5Botan16X509_Certificate14is_self_signedEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffaa0.md#insn-004ffaa8)
- 新版 `00522940`（命令位置の公開資料なし）

~~~diff
- 004ffaa8 ["INT_ADD", "register:40f0:8", ["const:4ffaa8:8", "const:4:8"]]
- 004ffaa8 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522940 ["INT_ADD", "register:40f0:8", ["const:522940:8", "const:4:8"]]
+ 00522940 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffaa8 bytes 3e741b94
+ 00522940 bytes 2cdb1c94
~~~


<a id="compare-4f10ce62f0999fc0935cacd9c96f49c0"></a>

### [`004ffab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffab8.md) → [`00522950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522950.md) _ZNK5Botan16X509_Certificate10not_beforeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffab8.md#insn-004ffac0)
- 新版 `00522958`（命令位置の公開資料なし）

~~~diff
- 004ffac0 ["INT_ADD", "register:40f0:8", ["const:4ffac0:8", "const:4:8"]]
- 004ffac0 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522958 ["INT_ADD", "register:40f0:8", ["const:522958:8", "const:4:8"]]
+ 00522958 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffac0 bytes 38741b94
+ 00522958 bytes 26db1c94
~~~


<a id="compare-10c7c7a0272ced9b9a22afaf28d49871"></a>

### [`004ffad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffad0.md) → [`00522968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522968.md) _ZNK5Botan16X509_Certificate9not_afterEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffad0.md#insn-004ffad8)
- 新版 `00522970`（命令位置の公開資料なし）

~~~diff
- 004ffad8 ["INT_ADD", "register:40f0:8", ["const:4ffad8:8", "const:4:8"]]
- 004ffad8 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522970 ["INT_ADD", "register:40f0:8", ["const:522970:8", "const:4:8"]]
+ 00522970 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffad8 bytes 32741b94
+ 00522970 bytes 20db1c94
~~~


<a id="compare-8d4953b2f8b519676542d5da1173955a"></a>

### [`004ffae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffae8.md) → [`00522980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522980.md) _ZNK5Botan16X509_Certificate23subject_public_key_algoEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffae8.md#insn-004ffaf0)
- 新版 `00522988`（命令位置の公開資料なし）

~~~diff
- 004ffaf0 ["INT_ADD", "register:40f0:8", ["const:4ffaf0:8", "const:4:8"]]
- 004ffaf0 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522988 ["INT_ADD", "register:40f0:8", ["const:522988:8", "const:4:8"]]
+ 00522988 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffaf0 bytes 2c741b94
+ 00522988 bytes 1adb1c94
~~~


<a id="compare-49a2a62b2ea260788af14935ad3b715e"></a>

### [`004ffb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb00.md) → [`00522998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522998.md) _ZNK5Botan16X509_Certificate16v2_issuer_key_idEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb00.md#insn-004ffb08)
- 新版 `005229a0`（命令位置の公開資料なし）

~~~diff
- 004ffb08 ["INT_ADD", "register:40f0:8", ["const:4ffb08:8", "const:4:8"]]
- 004ffb08 ["CALL", null, ["callee:00c595f0:8"]]
+ 005229a0 ["INT_ADD", "register:40f0:8", ["const:5229a0:8", "const:4:8"]]
+ 005229a0 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffb08 bytes 26741b94
+ 005229a0 bytes 14db1c94
~~~


<a id="compare-5bc2d8d8e940295bd9674b3853d8217d"></a>

### [`004ffb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb18.md) → [`005229b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229b0.md) _ZNK5Botan16X509_Certificate17v2_subject_key_idEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb18.md#insn-004ffb20)
- 新版 `005229b8`（命令位置の公開資料なし）

~~~diff
- 004ffb20 ["INT_ADD", "register:40f0:8", ["const:4ffb20:8", "const:4:8"]]
- 004ffb20 ["CALL", null, ["callee:00c595f0:8"]]
+ 005229b8 ["INT_ADD", "register:40f0:8", ["const:5229b8:8", "const:4:8"]]
+ 005229b8 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffb20 bytes 20741b94
+ 005229b8 bytes 0edb1c94
~~~


<a id="compare-7f9249e4d77477eb7031a3502f822039"></a>

### [`004ffb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb30.md) → [`005229c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229c8.md) _ZNK5Botan16X509_Certificate23subject_public_key_bitsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb30.md#insn-004ffb38)
- 新版 `005229d0`（命令位置の公開資料なし）

~~~diff
- 004ffb38 ["INT_ADD", "register:40f0:8", ["const:4ffb38:8", "const:4:8"]]
- 004ffb38 ["CALL", null, ["callee:00c595f0:8"]]
+ 005229d0 ["INT_ADD", "register:40f0:8", ["const:5229d0:8", "const:4:8"]]
+ 005229d0 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffb38 bytes 1a741b94
+ 005229d0 bytes 08db1c94
~~~


<a id="compare-b94a39283f3ad17baa4fbf3432359cbe"></a>

### [`004ffb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb48.md) → [`005229e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229e0.md) _ZNK5Botan16X509_Certificate18is_serial_negativeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb48.md#insn-004ffb50)
- 新版 `005229e8`（命令位置の公開資料なし）

~~~diff
- 004ffb50 ["INT_ADD", "register:40f0:8", ["const:4ffb50:8", "const:4:8"]]
- 004ffb50 ["CALL", null, ["callee:00c595f0:8"]]
+ 005229e8 ["INT_ADD", "register:40f0:8", ["const:5229e8:8", "const:4:8"]]
+ 005229e8 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffb50 bytes 14741b94
+ 005229e8 bytes 02db1c94
~~~


<a id="compare-16ea32d667b0f6fa5b3454a3ef1a487d"></a>

### [`004ffb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb60.md) → [`005229f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229f8.md) _ZNK5Botan16X509_Certificate10path_limitEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffb68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb60.md#insn-004ffb68)
- 新版 `00522a00`（命令位置の公開資料なし）

~~~diff
- 004ffb68 ["INT_ADD", "register:40f0:8", ["const:4ffb68:8", "const:4:8"]]
- 004ffb68 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522a00 ["INT_ADD", "register:40f0:8", ["const:522a00:8", "const:4:8"]]
+ 00522a00 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffb68 bytes 0e741b94
+ 00522a00 bytes fcda1c94
~~~


<a id="compare-8337597f1506fd424b8e5bf6266f7b80"></a>

### [`004ffb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb78.md) → [`00522a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a10.md) _ZNK5Botan16X509_Certificate11constraintsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb78.md#insn-004ffb80)
- 新版 `00522a18`（命令位置の公開資料なし）

~~~diff
- 004ffb80 ["INT_ADD", "register:40f0:8", ["const:4ffb80:8", "const:4:8"]]
- 004ffb80 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522a18 ["INT_ADD", "register:40f0:8", ["const:522a18:8", "const:4:8"]]
+ 00522a18 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffb80 bytes 08741b94
+ 00522a18 bytes f6da1c94
~~~


<a id="compare-16f5352e033349be5803eb17c46ba08b"></a>

### [`004ffb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb90.md) → [`00522a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a28.md) _ZNK5Botan16X509_Certificate18extended_key_usageEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffb90.md#insn-004ffb98)
- 新版 `00522a30`（命令位置の公開資料なし）

~~~diff
- 004ffb98 ["INT_ADD", "register:40f0:8", ["const:4ffb98:8", "const:4:8"]]
- 004ffb98 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522a30 ["INT_ADD", "register:40f0:8", ["const:522a30:8", "const:4:8"]]
+ 00522a30 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffb98 bytes 02741b94
+ 00522a30 bytes f0da1c94
~~~


<a id="compare-460baed3b86ce822040ee36e112a76ce"></a>

### [`004ffba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffba8.md) → [`00522a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a40.md) _ZNK5Botan16X509_Certificate23certificate_policy_oidsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffba8.md#insn-004ffbb0)
- 新版 `00522a48`（命令位置の公開資料なし）

~~~diff
- 004ffbb0 ["INT_ADD", "register:40f0:8", ["const:4ffbb0:8", "const:4:8"]]
- 004ffbb0 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522a48 ["INT_ADD", "register:40f0:8", ["const:522a48:8", "const:4:8"]]
+ 00522a48 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffbb0 bytes fc731b94
+ 00522a48 bytes eada1c94
~~~


<a id="compare-398b88b13daf1714d91fe36de7b3bef0"></a>

### [`004ffbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffbc0.md) → [`00522a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a58.md) _ZNK5Botan16X509_Certificate16name_constraintsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffbc0.md#insn-004ffbc8)
- 新版 `00522a60`（命令位置の公開資料なし）

~~~diff
- 004ffbc8 ["INT_ADD", "register:40f0:8", ["const:4ffbc8:8", "const:4:8"]]
- 004ffbc8 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522a60 ["INT_ADD", "register:40f0:8", ["const:522a60:8", "const:4:8"]]
+ 00522a60 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffbc8 bytes f6731b94
+ 00522a60 bytes e4da1c94
~~~


<a id="compare-d111906d751ce932c08e44b893b0be2b"></a>

### [`004ffbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffbd8.md) → [`00522a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a70.md) _ZNK5Botan16X509_Certificate13v3_extensionsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffbd8.md#insn-004ffbe0)
- 新版 `00522a78`（命令位置の公開資料なし）

~~~diff
- 004ffbe0 ["INT_ADD", "register:40f0:8", ["const:4ffbe0:8", "const:4:8"]]
- 004ffbe0 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522a78 ["INT_ADD", "register:40f0:8", ["const:522a78:8", "const:4:8"]]
+ 00522a78 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffbe0 bytes f0731b94
+ 00522a78 bytes deda1c94
~~~


<a id="compare-1af65c5c25fdf0f6eda62f4b926e8491"></a>

### [`004ffbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffbf0.md) → [`00522a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a88.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNS_3OIDE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffbf0.md#insn-004ffc00)
- 新版 `00522a98`（命令位置の公開資料なし）

~~~diff
- 004ffc00 ["INT_ADD", "register:40f0:8", ["const:4ffc00:8", "const:4:8"]]
- 004ffc00 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522a98 ["INT_ADD", "register:40f0:8", ["const:522a98:8", "const:4:8"]]
+ 00522a98 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffc00 bytes e8731b94
+ 00522a98 bytes d6da1c94
~~~


<a id="compare-0ca586ee69a6507a3fea1b9b3ebac969"></a>

### [`004ffed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffed4.md) → [`00522d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522d6c.md) _ZNK5Botan16X509_Certificate15has_constraintsENS_15Key_ConstraintsE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ffee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffed4.md#insn-004ffee8) · [`004ffef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffed4.md#insn-004ffef8)
- 新版 `00522d80`（命令位置の公開資料なし） · `00522d90`（命令位置の公開資料なし）

~~~diff
- 004ffee8 ["INT_ADD", "register:40f0:8", ["const:4ffee8:8", "const:4:8"]]
- 004ffee8 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522d80 ["INT_ADD", "register:40f0:8", ["const:522d80:8", "const:4:8"]]
+ 00522d80 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffee8 bytes 2e731b94
+ 00522d80 bytes 1cda1c94
- 004ffef8 ["INT_ADD", "register:40f0:8", ["const:4ffef8:8", "const:4:8"]]
- 004ffef8 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522d90 ["INT_ADD", "register:40f0:8", ["const:522d90:8", "const:4:8"]]
+ 00522d90 ["CALL", null, ["callee:00c595f0:8"]]
- 004ffef8 bytes 2a731b94
+ 00522d90 bytes 18da1c94
~~~


<a id="compare-6c527abfc536de6e5dfa22ca22728472"></a>

### [`004fff1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004fff1c.md) → [`00522db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522db4.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004fff48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004fff1c.md#insn-004fff48) · [`004fff50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004fff1c.md#insn-004fff50) · [`004fffcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004fff1c.md#insn-004fffcc)
- 新版 `00522de0`（命令位置の公開資料なし） · `00522de8`（命令位置の公開資料なし） · `00522e64`（命令位置の公開資料なし）

~~~diff
- 004fff48 ["INT_ADD", "register:40f0:8", ["const:4fff48:8", "const:4:8"]]
- 004fff48 ["CALL", null, ["callee:00c58280:8"]]
+ 00522de0 ["INT_ADD", "register:40f0:8", ["const:522de0:8", "const:4:8"]]
+ 00522de0 ["CALL", null, ["callee:00c58280:8"]]
- 004fff48 bytes 3a6e1b94
+ 00522de0 bytes 28d51c94
- 004fff50 ["INT_ADD", "register:40f0:8", ["const:4fff50:8", "const:4:8"]]
- 004fff50 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522de8 ["INT_ADD", "register:40f0:8", ["const:522de8:8", "const:4:8"]]
+ 00522de8 ["CALL", null, ["callee:00c595f0:8"]]
- 004fff50 bytes 14731b94
+ 00522de8 bytes 02da1c94
- 004fffcc ["INT_ADD", "register:40f0:8", ["const:4fffcc:8", "const:4:8"]]
- 004fffcc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00522e64 ["INT_ADD", "register:40f0:8", ["const:522e64:8", "const:4:8"]]
+ 00522e64 ["CALL", null, ["callee:00c57ab0:8"]]
- 004fffcc bytes 256c1b94
+ 00522e64 bytes 13d31c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb38020626c56d4df4235bb24cc23983"></a>

### [`0050003c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/0050003c.md) → [`00522ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522ed4.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/0050003c.md#insn-0050004c)
- 新版 `00522ee4`（命令位置の公開資料なし）

~~~diff
- 0050004c ["INT_ADD", "register:40f0:8", ["const:50004c:8", "const:4:8"]]
- 0050004c ["CALL", null, ["callee:00c595f0:8"]]
+ 00522ee4 ["INT_ADD", "register:40f0:8", ["const:522ee4:8", "const:4:8"]]
+ 00522ee4 ["CALL", null, ["callee:00c595f0:8"]]
- 0050004c bytes d5721b94
+ 00522ee4 bytes c3d91c94
~~~


<a id="compare-8d18682dc201d0098b9a985692c7ed55"></a>

### [`005000cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/005000cc.md) → [`00522f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522f64.md) _ZNK5Botan16X509_Certificate14ocsp_responderEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005000dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/005000cc.md#insn-005000dc)
- 新版 `00522f74`（命令位置の公開資料なし）

~~~diff
- 005000dc ["INT_ADD", "register:40f0:8", ["const:5000dc:8", "const:4:8"]]
- 005000dc ["CALL", null, ["callee:00c595f0:8"]]
+ 00522f74 ["INT_ADD", "register:40f0:8", ["const:522f74:8", "const:4:8"]]
+ 00522f74 ["CALL", null, ["callee:00c595f0:8"]]
- 005000dc bytes b1721b94
+ 00522f74 bytes 9fd91c94
~~~


<a id="compare-207121af5a724f83fc01576494200dd8"></a>

### [`00500120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500120.md) → [`00522fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522fb8.md) _ZNK5Botan16X509_Certificate10ca_issuersEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00500130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500120.md#insn-00500130)
- 新版 `00522fc8`（命令位置の公開資料なし）

~~~diff
- 00500130 ["INT_ADD", "register:40f0:8", ["const:500130:8", "const:4:8"]]
- 00500130 ["CALL", null, ["callee:00c595f0:8"]]
+ 00522fc8 ["INT_ADD", "register:40f0:8", ["const:522fc8:8", "const:4:8"]]
+ 00522fc8 ["CALL", null, ["callee:00c595f0:8"]]
- 00500130 bytes 9c721b94
+ 00522fc8 bytes 8ad91c94
~~~


<a id="compare-430d16d9a0f24182eeec4c12891be1d0"></a>

### [`00500168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500168.md) → [`00523000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523000.md) _ZNK5Botan16X509_Certificate22crl_distribution_pointEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050017c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500168.md#insn-0050017c) · [`00500194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500168.md#insn-00500194)
- 新版 `00523014`（命令位置の公開資料なし） · `0052302c`（命令位置の公開資料なし）

~~~diff
- 0050017c ["INT_ADD", "register:40f0:8", ["const:50017c:8", "const:4:8"]]
- 0050017c ["CALL", null, ["callee:00c595f0:8"]]
+ 00523014 ["INT_ADD", "register:40f0:8", ["const:523014:8", "const:4:8"]]
+ 00523014 ["CALL", null, ["callee:00c595f0:8"]]
- 0050017c bytes 89721b94
+ 00523014 bytes 77d91c94
- 00500194 ["INT_ADD", "register:40f0:8", ["const:500194:8", "const:4:8"]]
- 00500194 ["CALL", null, ["callee:00c595f0:8"]]
+ 0052302c ["INT_ADD", "register:40f0:8", ["const:52302c:8", "const:4:8"]]
+ 0052302c ["CALL", null, ["callee:00c595f0:8"]]
- 00500194 bytes 83721b94
+ 0052302c bytes 71d91c94
~~~


<a id="compare-80c00bd265c667d59ed211389e4ffee5"></a>

### [`005001dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/005001dc.md) → [`00523074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523074.md) _ZNK5Botan16X509_Certificate15issuer_alt_nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005001e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/005001dc.md#insn-005001e4)
- 新版 `0052307c`（命令位置の公開資料なし）

~~~diff
- 005001e4 ["INT_ADD", "register:40f0:8", ["const:5001e4:8", "const:4:8"]]
- 005001e4 ["CALL", null, ["callee:00c595f0:8"]]
+ 0052307c ["INT_ADD", "register:40f0:8", ["const:52307c:8", "const:4:8"]]
+ 0052307c ["CALL", null, ["callee:00c595f0:8"]]
- 005001e4 bytes 6f721b94
+ 0052307c bytes 5dd91c94
~~~


<a id="compare-cc9d2d3d9af53c600072e52511df0915"></a>

### [`00500f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500f10.md) → [`00523da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523da8.md) _ZNK5Botan16X509_Certificate23load_subject_public_keyEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdc0.md) · 呼出先 5件 [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8a0.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 1件 [`00c59810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59810.md) · 呼出先 5件 [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c592f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592f0.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00500f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500f10.md#insn-00500f34) · [`00500f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500f10.md#insn-00500f40) · [`00500f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500f10.md#insn-00500f48)
- 新版 `00523dcc`（命令位置の公開資料なし） · `00523dd8`（命令位置の公開資料なし） · `00523de0`（命令位置の公開資料なし）

~~~diff
- 00500f34 ["INT_ADD", "register:40f0:8", ["const:500f34:8", "const:4:8"]]
- 00500f34 ["CALL", null, ["callee:00c595f0:8"]]
+ 00523dcc ["INT_ADD", "register:40f0:8", ["const:523dcc:8", "const:4:8"]]
+ 00523dcc ["CALL", null, ["callee:00c595f0:8"]]
- 00500f34 bytes 1b6f1b94
+ 00523dcc bytes 09d61c94
- 00500f40 ["INT_ADD", "register:40f0:8", ["const:500f40:8", "const:4:8"]]
- 00500f40 ["CALL", null, ["callee:004a6bdc:8"]]
+ 00523dd8 ["INT_ADD", "register:40f0:8", ["const:523dd8:8", "const:4:8"]]
+ 00523dd8 ["CALL", null, ["callee:004a6bdc:8"]]
- 00500f40 bytes 810bfe97
+ 00523dd8 bytes 810bfe97
- 00500f48 ["INT_ADD", "register:40f0:8", ["const:500f48:8", "const:4:8"]]
- 00500f48 ["CALL", null, ["callee:00c592f0:8"]]
+ 00523de0 ["INT_ADD", "register:40f0:8", ["const:523de0:8", "const:4:8"]]
+ 00523de0 ["CALL", null, ["callee:00c592f0:8"]]
- 00500f48 bytes 566e1b94
+ 00523de0 bytes 44d51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e276b9cc8478c1b16db61155e3bf16fb"></a>

### [`00501084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501084.md) → [`00523f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523f1c.md) _ZNK5Botan16X509_Certificate20raw_issuer_dn_sha256Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005010e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501084.md#insn-005010e4) · [`005010f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501084.md#insn-005010f4) · [`00501104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501084.md#insn-00501104)
- 新版 `00523f7c`（命令位置の公開資料なし） · `00523f8c`（命令位置の公開資料なし） · `00523f9c`（命令位置の公開資料なし）

~~~diff
- 005010e4 ["INT_ADD", "register:40f0:8", ["const:5010e4:8", "const:4:8"]]
- 005010e4 ["CALL", null, ["callee:00c58a70:8"]]
+ 00523f7c ["INT_ADD", "register:40f0:8", ["const:523f7c:8", "const:4:8"]]
+ 00523f7c ["CALL", null, ["callee:00c58a70:8"]]
- 005010e4 bytes cf6b1b94
+ 00523f7c bytes bdd21c94
- 005010f4 ["INT_ADD", "register:40f0:8", ["const:5010f4:8", "const:4:8"]]
- 005010f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00523f8c ["INT_ADD", "register:40f0:8", ["const:523f8c:8", "const:4:8"]]
+ 00523f8c ["CALL", null, ["callee:00c57ab0:8"]]
- 005010f4 bytes db671b94
+ 00523f8c bytes c9ce1c94
- 00501104 ["INT_ADD", "register:40f0:8", ["const:501104:8", "const:4:8"]]
- 00501104 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00523f9c ["INT_ADD", "register:40f0:8", ["const:523f9c:8", "const:4:8"]]
+ 00523f9c ["CALL", null, ["callee:00c57ab0:8"]]
- 00501104 bytes d7671b94
+ 00523f9c bytes c5ce1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e538855ff51fde69093cda8721b60f"></a>

### [`00501274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501274.md) → [`0052410c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/0052410c.md) _ZNK5Botan16X509_Certificate21raw_subject_dn_sha256Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005012d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501274.md#insn-005012d4) · [`005012e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501274.md#insn-005012e0) · [`005012f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501274.md#insn-005012f8)
- 新版 `0052416c`（命令位置の公開資料なし） · `00524178`（命令位置の公開資料なし） · `00524190`（命令位置の公開資料なし）

~~~diff
- 005012d4 ["INT_ADD", "register:40f0:8", ["const:5012d4:8", "const:4:8"]]
- 005012d4 ["CALL", null, ["callee:00c589f0:8"]]
+ 0052416c ["INT_ADD", "register:40f0:8", ["const:52416c:8", "const:4:8"]]
+ 0052416c ["CALL", null, ["callee:00c589f0:8"]]
- 005012d4 bytes 336b1b94
+ 0052416c bytes 21d21c94
- 005012e0 ["INT_ADD", "register:40f0:8", ["const:5012e0:8", "const:4:8"]]
- 005012e0 ["CALL", null, ["callee:00c595f0:8"]]
+ 00524178 ["INT_ADD", "register:40f0:8", ["const:524178:8", "const:4:8"]]
+ 00524178 ["CALL", null, ["callee:00c595f0:8"]]
- 005012e0 bytes 306e1b94
+ 00524178 bytes 1ed51c94
- 005012f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005012f8 ["INT_ADD", "register:40f0:8", ["const:5012f8:8", "const:4:8"]]
- 005012f8 ["CALLIND", null, ["register:0:8"]]
+ 00524190 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00524190 ["INT_ADD", "register:40f0:8", ["const:524190:8", "const:4:8"]]
+ 00524190 ["CALLIND", null, ["register:0:8"]]
- 005012f8 bytes 00013fd6
+ 00524190 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2a84c808de4e7320d55a992113ecf13"></a>

### [`0050140c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050140c.md) → [`005242a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242a4.md) _ZNK5Botan16X509_Certificate14ex_constraintsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00501434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501434.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005242cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050141c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050140c.md#insn-0050141c)
- 新版 `005242b4`（命令位置の公開資料なし）

~~~diff
- 0050141c ["INT_ADD", "register:40f0:8", ["const:50141c:8", "const:4:8"]]
- 0050141c ["CALL", null, ["callee:00c595f0:8"]]
+ 005242b4 ["INT_ADD", "register:40f0:8", ["const:5242b4:8", "const:4:8"]]
+ 005242b4 ["CALL", null, ["callee:00c595f0:8"]]
- 0050141c bytes e16d1b94
+ 005242b4 bytes cfd41c94
~~~


<a id="compare-4ff8d300fa91301308aa625acb2ed620"></a>

### [`00501434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501434.md) → [`005242cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md) FUN_005242cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050140c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050140c.md) [`00501664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501664.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`005242a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242a4.md) [`005244fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005244fc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005014c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501434.md#insn-005014c0) · [`00501528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501434.md#insn-00501528) · [`0050156c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501434.md#insn-0050156c)
- 新版 `00524358`（命令位置の公開資料なし） · `005243c0`（命令位置の公開資料なし） · `00524404`（命令位置の公開資料なし）

~~~diff
- 005014c0 ["INT_ADD", "register:40f0:8", ["const:5014c0:8", "const:4:8"]]
- 005014c0 ["CALL", null, ["callee:00c584b0:8"]]
+ 00524358 ["INT_ADD", "register:40f0:8", ["const:524358:8", "const:4:8"]]
+ 00524358 ["CALL", null, ["callee:00c584b0:8"]]
- 005014c0 bytes 68691b94
+ 00524358 bytes 56d01c94
- 00501528 ["INT_ADD", "register:40f0:8", ["const:501528:8", "const:4:8"]]
- 00501528 ["CALL", null, ["callee:00c57a90:8"]]
+ 005243c0 ["INT_ADD", "register:40f0:8", ["const:5243c0:8", "const:4:8"]]
+ 005243c0 ["CALL", null, ["callee:00c57a90:8"]]
- 00501528 bytes c6661b94
+ 005243c0 bytes b4cd1c94
- 0050156c ["INT_ADD", "register:40f0:8", ["const:50156c:8", "const:4:8"]]
- 0050156c ["CALL", null, ["callee:00c57c00:8"]]
+ 00524404 ["INT_ADD", "register:40f0:8", ["const:524404:8", "const:4:8"]]
+ 00524404 ["CALL", null, ["callee:00c57c00:8"]]
- 0050156c bytes 11671b94
+ 00524404 bytes ffcd1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e57972524a5a166104a9096eb0e97be8"></a>

### [`00501664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501664.md) → [`005244fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005244fc.md) _ZNK5Botan16X509_Certificate8policiesEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00501434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501434.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005242cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501664.md#insn-00501674)
- 新版 `0052450c`（命令位置の公開資料なし）

~~~diff
- 00501674 ["INT_ADD", "register:40f0:8", ["const:501674:8", "const:4:8"]]
- 00501674 ["CALL", null, ["callee:00c595f0:8"]]
+ 0052450c ["INT_ADD", "register:40f0:8", ["const:52450c:8", "const:4:8"]]
+ 0052450c ["CALL", null, ["callee:00c595f0:8"]]
- 00501674 bytes 4b6d1b94
+ 0052450c bytes 39d41c94
~~~


<a id="compare-e0ce2c11a4c4788855d9c27351181dcb"></a>

### [`0050168c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050168c.md) → [`00524524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524524.md) _ZNK5Botan16X509_Certificate11fingerprintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc770.md) [`00bdd030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c591c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591c0.md) [`00c59a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005016b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050168c.md#insn-005016b8) · [`005016cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050168c.md#insn-005016cc) · [`005016dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050168c.md#insn-005016dc)
- 新版 `00524550`（命令位置の公開資料なし） · `00524564`（命令位置の公開資料なし） · `00524574`（命令位置の公開資料なし）

~~~diff
- 005016b8 ["INT_ADD", "register:40f0:8", ["const:5016b8:8", "const:4:8"]]
- 005016b8 ["CALL", null, ["callee:00c59a80:8"]]
+ 00524550 ["INT_ADD", "register:40f0:8", ["const:524550:8", "const:4:8"]]
+ 00524550 ["CALL", null, ["callee:00c59a80:8"]]
- 005016b8 bytes 5e6e1b94
+ 00524550 bytes 4cd51c94
- 005016cc ["INT_ADD", "register:40f0:8", ["const:5016cc:8", "const:4:8"]]
- 005016cc ["CALL", null, ["callee:00c591c0:8"]]
+ 00524564 ["INT_ADD", "register:40f0:8", ["const:524564:8", "const:4:8"]]
+ 00524564 ["CALL", null, ["callee:00c591c0:8"]]
- 005016cc bytes 296c1b94
+ 00524564 bytes 17d31c94
- 005016dc ["INT_ADD", "register:40f0:8", ["const:5016dc:8", "const:4:8"]]
- 005016dc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00524574 ["INT_ADD", "register:40f0:8", ["const:524574:8", "const:4:8"]]
+ 00524574 ["CALL", null, ["callee:00c57ab0:8"]]
- 005016dc bytes 61661b94
+ 00524574 bytes 4fcd1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da17d1f3001cb8eafe6fe2054102b8cc"></a>

### [`00501738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501738.md) → [`005245d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005245d0.md) _ZNK5Botan16X509_Certificate16matches_dns_nameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd070.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcad0.md) [`00bdd060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd060.md)
- 新版 呼出元 1件 [`00c59ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ac0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59520.md) [`00c59ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501738.md#insn-00501798) · [`005017a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501738.md#insn-005017a8) · [`005017dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501738.md#insn-005017dc)
- 新版 `00524630`（命令位置の公開資料なし） · `00524640`（命令位置の公開資料なし） · `00524674`（命令位置の公開資料なし）

~~~diff
- 00501798 ["INT_ADD", "register:40f0:8", ["const:501798:8", "const:4:8"]]
- 00501798 ["CALL", null, ["callee:00c59ab0:8"]]
+ 00524630 ["INT_ADD", "register:40f0:8", ["const:524630:8", "const:4:8"]]
+ 00524630 ["CALL", null, ["callee:00c59ab0:8"]]
- 00501798 bytes 326e1b94
+ 00524630 bytes 20d51c94
- 005017a8 ["INT_ADD", "register:40f0:8", ["const:5017a8:8", "const:4:8"]]
- 005017a8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00524640 ["INT_ADD", "register:40f0:8", ["const:524640:8", "const:4:8"]]
+ 00524640 ["CALL", null, ["callee:00c57ab0:8"]]
- 005017a8 bytes 2e661b94
+ 00524640 bytes 1ccd1c94
- 005017dc ["INT_ADD", "register:40f0:8", ["const:5017dc:8", "const:4:8"]]
- 005017dc ["CALL", null, ["callee:00c59ab0:8"]]
+ 00524674 ["INT_ADD", "register:40f0:8", ["const:524674:8", "const:4:8"]]
+ 00524674 ["CALL", null, ["callee:00c59ab0:8"]]
- 005017dc bytes 216e1b94
+ 00524674 bytes 0fd51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e305d20739d7467bff9cb0827244b1f8"></a>

### [`00501998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501998.md) → [`00524830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524830.md) _ZNK5Botan16X509_CertificateltERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005019d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501998.md#insn-005019d4)
- 新版 `0052486c`（命令位置の公開資料なし）

~~~diff
- 005019d4 ["INT_ADD", "register:40f0:8", ["const:5019d4:8", "const:4:8"]]
- 005019d4 ["CALL", null, ["callee:00c57c50:8"]]
+ 0052486c ["INT_ADD", "register:40f0:8", ["const:52486c:8", "const:4:8"]]
+ 0052486c ["CALL", null, ["callee:00c57c50:8"]]
- 005019d4 bytes 0b661b94
+ 0052486c bytes f9cc1c94
~~~


<a id="compare-416c9a1d302abb78215219dd2873896c"></a>

### [`00501a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501a8c.md) → [`00524924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524924.md) _ZN5BotanneERKNS_16X509_CertificateES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501a8c.md#insn-00501ab8) · [`00501ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501a8c.md#insn-00501ac8) · [`00501ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501a8c.md#insn-00501ae8)
- 新版 `00524950`（命令位置の公開資料なし） · `00524960`（命令位置の公開資料なし） · `00524980`（命令位置の公開資料なし）

~~~diff
- 00501ab8 ["INT_ADD", "register:40f0:8", ["const:501ab8:8", "const:4:8"]]
- 00501ab8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00524950 ["INT_ADD", "register:40f0:8", ["const:524950:8", "const:4:8"]]
+ 00524950 ["CALL", null, ["callee:00c57c50:8"]]
- 00501ab8 bytes d2651b94
+ 00524950 bytes c0cc1c94
- 00501ac8 ["INT_ADD", "register:40f0:8", ["const:501ac8:8", "const:4:8"]]
- 00501ac8 ["CALL", null, ["callee:00c582a0:8"]]
+ 00524960 ["INT_ADD", "register:40f0:8", ["const:524960:8", "const:4:8"]]
+ 00524960 ["CALL", null, ["callee:00c582a0:8"]]
- 00501ac8 bytes 62671b94
+ 00524960 bytes 50ce1c94
- 00501ae8 ["INT_ADD", "register:40f0:8", ["const:501ae8:8", "const:4:8"]]
- 00501ae8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00524980 ["INT_ADD", "register:40f0:8", ["const:524980:8", "const:4:8"]]
+ 00524980 ["CALL", null, ["callee:00c57c50:8"]]
- 00501ae8 bytes c6651b94
+ 00524980 bytes b4cc1c94
~~~


<a id="compare-71e4b6bbd7fc04f2a05f30f97482c99c"></a>

### [`00503338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503338.md) → [`005261d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005261d0.md) _ZN5Botan17X509_Cert_Options10not_beforeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503338.md#insn-00503360) · [`00503398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503338.md#insn-00503398)
- 新版 `005261f8`（命令位置の公開資料なし） · `00526230`（命令位置の公開資料なし）

~~~diff
- 00503360 ["INT_ADD", "register:40f0:8", ["const:503360:8", "const:4:8"]]
- 00503360 ["CALL", null, ["callee:00c59ad0:8"]]
+ 005261f8 ["INT_ADD", "register:40f0:8", ["const:5261f8:8", "const:4:8"]]
+ 005261f8 ["CALL", null, ["callee:00c59ad0:8"]]
- 00503360 bytes 48671b94
+ 005261f8 bytes 36ce1c94
- 00503398 ["INT_ADD", "register:40f0:8", ["const:503398:8", "const:4:8"]]
- 00503398 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00526230 ["INT_ADD", "register:40f0:8", ["const:526230:8", "const:4:8"]]
+ 00526230 ["CALL", null, ["callee:00c57ae0:8"]]
- 00503398 bytes 3e5f1b94
+ 00526230 bytes 2cc61c94
~~~


<a id="compare-67b7b5649f7500bdff53396ec7f2f8cf"></a>

### [`0050339c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/0050339c.md) → [`00526234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526234.md) _ZN5Botan17X509_Cert_Options9not_afterERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005033c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/0050339c.md#insn-005033c4) · [`005033fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/0050339c.md#insn-005033fc)
- 新版 `0052625c`（命令位置の公開資料なし） · `00526294`（命令位置の公開資料なし）

~~~diff
- 005033c4 ["INT_ADD", "register:40f0:8", ["const:5033c4:8", "const:4:8"]]
- 005033c4 ["CALL", null, ["callee:00c59ad0:8"]]
+ 0052625c ["INT_ADD", "register:40f0:8", ["const:52625c:8", "const:4:8"]]
+ 0052625c ["CALL", null, ["callee:00c59ad0:8"]]
- 005033c4 bytes 2f671b94
+ 0052625c bytes 1dce1c94
- 005033fc ["INT_ADD", "register:40f0:8", ["const:5033fc:8", "const:4:8"]]
- 005033fc ["CALL", null, ["callee:00c57ae0:8"]]
+ 00526294 ["INT_ADD", "register:40f0:8", ["const:526294:8", "const:4:8"]]
+ 00526294 ["CALL", null, ["callee:00c57ae0:8"]]
- 005033fc bytes 255f1b94
+ 00526294 bytes 13c61c94
~~~


<a id="compare-9d4c524d90bce9a7c88a7f822f1c19a9"></a>

### [`00504ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504ee4.md) → [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) FUN_00527d7c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) [`00504f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) [`0050947c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md) [`00509f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) · 呼出先 2件 [`0051c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c938.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) · 呼出先 2件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00504f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504ee4.md#insn-00504f1c)
- 新版 `00527db4`（命令位置の公開資料なし）

~~~diff
- 00504f1c ["INT_ADD", "register:40f0:8", ["const:504f1c:8", "const:4:8"]]
- 00504f1c ["CALL", null, ["callee:0053f7d0:8"]]
+ 00527db4 ["INT_ADD", "register:40f0:8", ["const:527db4:8", "const:4:8"]]
+ 00527db4 ["CALL", null, ["callee:0053f7d0:8"]]
- 00504f1c bytes 875e0094
+ 00527db4 bytes 875e0094
~~~


