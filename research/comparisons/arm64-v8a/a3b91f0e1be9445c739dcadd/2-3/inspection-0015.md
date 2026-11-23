# v15.7.4 → v16.0.0 · 要調査の変更候補 (15)

[一覧の目次](README.md)

<a id="compare-6d4835dd97cea7f5b2ec2a4ccb9fefc4"></a>

### [`0078ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078ca70.md) → [`007bd760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd760.md) FUN_007bd760

採用 · 移動量 `+0x30cf0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078caa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078ca70.md#insn-0078caa4)
- 新版 `007bd794`（命令位置の公開資料なし）

~~~diff
- 0078caa4 ["INT_ADD", "register:40f0:8", ["const:78caa4:8", "const:4:8"]]
- 0078caa4 ["CALL", null, ["callee:0046e864:8"]]
+ 007bd794 ["INT_ADD", "register:40f0:8", ["const:7bd794:8", "const:4:8"]]
+ 007bd794 ["CALL", null, ["callee:0046e864:8"]]
- 0078caa4 bytes cafbf297
+ 007bd794 bytes 34c4f297
~~~


<a id="compare-6bc35b2c7e6228629dc5951bc64cf687"></a>

### [`0078cad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cad8.md) → [`007bd7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd7c8.md) FUN_007bd7c8

採用 · 移動量 `+0x30cf0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078cb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cad8.md#insn-0078cb10) · [`0078cb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cad8.md#insn-0078cb24) · [`0078cb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cad8.md#insn-0078cb2c)
- 新版 `007bd800`（命令位置の公開資料なし） · `007bd814`（命令位置の公開資料なし） · `007bd81c`（命令位置の公開資料なし）

~~~diff
- 0078cb10 ["INT_ADD", "register:40f0:8", ["const:78cb10:8", "const:4:8"]]
- 0078cb10 ["CALL", null, ["callee:00c538e0:8"]]
+ 007bd800 ["INT_ADD", "register:40f0:8", ["const:7bd800:8", "const:4:8"]]
+ 007bd800 ["CALL", null, ["callee:00c538e0:8"]]
- 0078cb10 bytes e0281194
+ 007bd800 bytes 38581294
- 0078cb24 ["COPY", "register:0:8", ["register:4040:8"]]
- 0078cb24 ["INT_ADD", "register:40f0:8", ["const:78cb24:8", "const:4:8"]]
- 0078cb24 ["CALLIND", null, ["register:0:8"]]
+ 007bd814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd814 ["INT_ADD", "register:40f0:8", ["const:7bd814:8", "const:4:8"]]
+ 007bd814 ["CALLIND", null, ["register:0:8"]]
- 0078cb24 bytes 00013fd6
+ 007bd814 bytes 00013fd6
- 0078cb2c ["INT_ADD", "register:40f0:8", ["const:78cb2c:8", "const:4:8"]]
- 0078cb2c ["CALL", null, ["callee:00c57a80:8"]]
+ 007bd81c ["INT_ADD", "register:40f0:8", ["const:7bd81c:8", "const:4:8"]]
+ 007bd81c ["CALL", null, ["callee:00c57a80:8"]]
- 0078cb2c bytes 41391194
+ 007bd81c bytes 99681294
~~~


<a id="compare-8b376c1e6473001580971bfe38da1b2a"></a>

### [`0078cb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cb44.md) → [`007bd834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd834.md) FUN_007bd834

採用 · 移動量 `+0x30cf0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078cb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cb44.md#insn-0078cb7c) · [`0078cb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cb44.md#insn-0078cb90) · [`0078cb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cb44.md#insn-0078cb98)
- 新版 `007bd86c`（命令位置の公開資料なし） · `007bd880`（命令位置の公開資料なし） · `007bd888`（命令位置の公開資料なし）

~~~diff
- 0078cb7c ["INT_ADD", "register:40f0:8", ["const:78cb7c:8", "const:4:8"]]
- 0078cb7c ["CALL", null, ["callee:00c538e0:8"]]
+ 007bd86c ["INT_ADD", "register:40f0:8", ["const:7bd86c:8", "const:4:8"]]
+ 007bd86c ["CALL", null, ["callee:00c538e0:8"]]
- 0078cb7c bytes c5281194
+ 007bd86c bytes 1d581294
- 0078cb90 ["COPY", "register:0:8", ["register:4040:8"]]
- 0078cb90 ["INT_ADD", "register:40f0:8", ["const:78cb90:8", "const:4:8"]]
- 0078cb90 ["CALLIND", null, ["register:0:8"]]
+ 007bd880 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd880 ["INT_ADD", "register:40f0:8", ["const:7bd880:8", "const:4:8"]]
+ 007bd880 ["CALLIND", null, ["register:0:8"]]
- 0078cb90 bytes 00013fd6
+ 007bd880 bytes 00013fd6
- 0078cb98 ["INT_ADD", "register:40f0:8", ["const:78cb98:8", "const:4:8"]]
- 0078cb98 ["CALL", null, ["callee:00c57a80:8"]]
+ 007bd888 ["INT_ADD", "register:40f0:8", ["const:7bd888:8", "const:4:8"]]
+ 007bd888 ["CALL", null, ["callee:00c57a80:8"]]
- 0078cb98 bytes 26391194
+ 007bd888 bytes 7e681294
~~~


<a id="compare-fb1342264227d63969298485ccb0d27b"></a>

### [`0078cbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cbb0.md) → [`007bd8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8a0.md) FUN_007bd8a0

採用 · 移動量 `+0x30cf0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078cbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cbb0.md#insn-0078cbcc) · [`0078cbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cbb0.md#insn-0078cbec)
- 新版 `007bd8bc`（命令位置の公開資料なし） · `007bd8dc`（命令位置の公開資料なし）

~~~diff
- 0078cbcc ["INT_ADD", "register:40f0:8", ["const:78cbcc:8", "const:4:8"]]
- 0078cbcc ["CALL", null, ["callee:00c538e0:8"]]
+ 007bd8bc ["INT_ADD", "register:40f0:8", ["const:7bd8bc:8", "const:4:8"]]
+ 007bd8bc ["CALL", null, ["callee:00c538e0:8"]]
- 0078cbcc bytes b1281194
+ 007bd8bc bytes 09581294
- 0078cbec ["COPY", "register:0:8", ["register:4040:8"]]
- 0078cbec ["INT_ADD", "register:40f0:8", ["const:78cbec:8", "const:4:8"]]
- 0078cbec ["CALLIND", null, ["register:0:8"]]
+ 007bd8dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd8dc ["INT_ADD", "register:40f0:8", ["const:7bd8dc:8", "const:4:8"]]
+ 007bd8dc ["CALLIND", null, ["register:0:8"]]
- 0078cbec bytes 00013fd6
+ 007bd8dc bytes 00013fd6
~~~


<a id="compare-2c6134637d3b2d3fd62b3bede2fd8977"></a>

### [`0078cc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cc00.md) → [`007bd8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8f0.md) FUN_007bd8f0

採用 · 移動量 `+0x30cf0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078cc68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cc00.md#insn-0078cc68) · [`0078ccec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cc00.md#insn-0078ccec)
- 新版 `007bd958`（命令位置の公開資料なし） · `007bd9dc`（命令位置の公開資料なし）

~~~diff
- 0078cc68 ["INT_ADD", "register:40f0:8", ["const:78cc68:8", "const:4:8"]]
- 0078cc68 ["CALL", null, ["callee:00c57a90:8"]]
+ 007bd958 ["INT_ADD", "register:40f0:8", ["const:7bd958:8", "const:4:8"]]
+ 007bd958 ["CALL", null, ["callee:00c57a90:8"]]
- 0078cc68 bytes f6381194
+ 007bd958 bytes 4e681294
- 0078ccec ["INT_ADD", "register:40f0:8", ["const:78ccec:8", "const:4:8"]]
- 0078ccec ["CALL", null, ["callee:0043bb64:8"]]
+ 007bd9dc ["INT_ADD", "register:40f0:8", ["const:7bd9dc:8", "const:4:8"]]
+ 007bd9dc ["CALL", null, ["callee:0043bb64:8"]]
- 0078ccec bytes de30f297
+ 007bd9dc bytes 62f8f197
~~~


<a id="compare-53dc369ff9140f356b06fcef659f4d98"></a>

### [`007ab188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab188.md) → [`007dd248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd248.md) FUN_007dd248

採用 · 移動量 `+0x320c0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ab1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab188.md#insn-007ab1f0) · [`007ab23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab188.md#insn-007ab23c)
- 新版 `007dd2b0`（命令位置の公開資料なし） · `007dd2fc`（命令位置の公開資料なし）

~~~diff
- 007ab1f0 ["INT_ADD", "register:40f0:8", ["const:7ab1f0:8", "const:4:8"]]
- 007ab1f0 ["CALL", null, ["callee:00c57a90:8"]]
+ 007dd2b0 ["INT_ADD", "register:40f0:8", ["const:7dd2b0:8", "const:4:8"]]
+ 007dd2b0 ["CALL", null, ["callee:00c57a90:8"]]
- 007ab1f0 bytes 94bf1094
+ 007dd2b0 bytes f8e91194
- 007ab23c ["INT_ADD", "register:40f0:8", ["const:7ab23c:8", "const:4:8"]]
- 007ab23c ["CALL", null, ["callee:0043bb64:8"]]
+ 007dd2fc ["INT_ADD", "register:40f0:8", ["const:7dd2fc:8", "const:4:8"]]
+ 007dd2fc ["CALL", null, ["callee:0043bb64:8"]]
- 007ab23c bytes 8ab7f197
+ 007dd2fc bytes 1a7af197
~~~


<a id="compare-2cd9fffad96ba86d46b72da89314c954"></a>

### [`007bd430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd430.md) → [`007ef59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef59c.md) FUN_007ef59c

採用 · 移動量 `+0x3216c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 5件 [`007292d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292d8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 5件 [`00753490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753490.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd430.md#insn-007bd480) · [`007bd498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd430.md#insn-007bd498) · [`007bd4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd430.md#insn-007bd4b4)
- 新版 `007ef5ec`（命令位置の公開資料なし） · `007ef604`（命令位置の公開資料なし） · `007ef620`（命令位置の公開資料なし）

~~~diff
- 007bd480 ["INT_ADD", "register:40f0:8", ["const:7bd480:8", "const:4:8"]]
- 007bd480 ["CALL", null, ["callee:00c57a90:8"]]
+ 007ef5ec ["INT_ADD", "register:40f0:8", ["const:7ef5ec:8", "const:4:8"]]
+ 007ef5ec ["CALL", null, ["callee:00c57a90:8"]]
- 007bd480 bytes f0761094
+ 007ef5ec bytes 29a11194
- 007bd498 ["INT_ADD", "register:40f0:8", ["const:7bd498:8", "const:4:8"]]
- 007bd498 ["CALL", null, ["callee:00c57c00:8"]]
+ 007ef604 ["INT_ADD", "register:40f0:8", ["const:7ef604:8", "const:4:8"]]
+ 007ef604 ["CALL", null, ["callee:00c57c00:8"]]
- 007bd498 bytes 46771094
+ 007ef604 bytes 7fa11194
- 007bd4b4 ["INT_ADD", "register:40f0:8", ["const:7bd4b4:8", "const:4:8"]]
- 007bd4b4 ["CALL", null, ["callee:00753490:8"]]
+ 007ef620 ["INT_ADD", "register:40f0:8", ["const:7ef620:8", "const:4:8"]]
+ 007ef620 ["CALL", null, ["callee:00753490:8"]]
- 007bd4b4 bytes 89affd97
+ 007ef620 bytes 9c8ffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7656ede189cd4f128be71fa7eab87669"></a>

### [`007bf6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf6b8.md) → [`007f1854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1854.md) FUN_007f1854

採用 · 移動量 `+0x3219c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0078b0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078b/0078b0ec.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`007bf8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf8dc.md) [`007bfcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfcb4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) [`007f1e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e50.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bf778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf6b8.md#insn-007bf778) · [`007bf7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf6b8.md#insn-007bf7a0) · [`007bf7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf6b8.md#insn-007bf7e8)
- 新版 `007f1914`（命令位置の公開資料なし） · `007f193c`（命令位置の公開資料なし） · `007f1984`（命令位置の公開資料なし）

~~~diff
- 007bf778 ["INT_ADD", "register:40f0:8", ["const:7bf778:8", "const:4:8"]]
- 007bf778 ["CALL", null, ["callee:00c57a90:8"]]
+ 007f1914 ["INT_ADD", "register:40f0:8", ["const:7f1914:8", "const:4:8"]]
+ 007f1914 ["CALL", null, ["callee:00c57a90:8"]]
- 007bf778 bytes 326e1094
+ 007f1914 bytes 5f981194
- 007bf7a0 ["INT_ADD", "register:40f0:8", ["const:7bf7a0:8", "const:4:8"]]
- 007bf7a0 ["CALL", null, ["callee:007f1a78:8"]]
+ 007f193c ["INT_ADD", "register:40f0:8", ["const:7f193c:8", "const:4:8"]]
+ 007f193c ["CALL", null, ["callee:007f1a78:8"]]
- 007bf7a0 bytes 4f000094
+ 007f193c bytes 4f000094
- 007bf7e8 ["INT_ADD", "register:40f0:8", ["const:7bf7e8:8", "const:4:8"]]
- 007bf7e8 ["CALL", null, ["callee:007f1a78:8"]]
+ 007f1984 ["INT_ADD", "register:40f0:8", ["const:7f1984:8", "const:4:8"]]
+ 007f1984 ["CALL", null, ["callee:007f1a78:8"]]
- 007bf7e8 bytes 3d000094
+ 007f1984 bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e80e1c4ca718e3f55deada294e0343"></a>

### [`007ceacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007ceacc.md) → [`00801c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801c50.md) FUN_00801c50

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`0075bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bc70.md) [`007e9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e9/007e9118.md) [`007ef4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef4ec.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 8件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`0081de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081de40.md) [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ceb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007ceacc.md#insn-007ceb64) · [`007ceb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007ceacc.md#insn-007ceb98)
- 新版 `00801ce8`（命令位置の公開資料なし） · `00801d1c`（命令位置の公開資料なし）

~~~diff
- 007ceb64 ["INT_ADD", "register:40f0:8", ["const:7ceb64:8", "const:4:8"]]
- 007ceb64 ["CALL", null, ["callee:00c57a90:8"]]
+ 00801ce8 ["INT_ADD", "register:40f0:8", ["const:801ce8:8", "const:4:8"]]
+ 00801ce8 ["CALL", null, ["callee:00c57a90:8"]]
- 007ceb64 bytes 37311094
+ 00801ce8 bytes 6a571194
- 007ceb98 ["INT_ADD", "register:40f0:8", ["const:7ceb98:8", "const:4:8"]]
- 007ceb98 ["CALL", null, ["callee:0043bb64:8"]]
+ 00801d1c ["INT_ADD", "register:40f0:8", ["const:801d1c:8", "const:4:8"]]
+ 00801d1c ["CALL", null, ["callee:0043bb64:8"]]
- 007ceb98 bytes 3329f197
+ 00801d1c bytes 92e7f097
~~~


<a id="compare-1528c8e2a16f13ed03f70501c423ed6c"></a>

### [`007cec1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cec1c.md) → [`00801da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801da0.md) FUN_00801da0

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007e9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e9/007e9118.md) [`007ef4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef4ec.md) [`00a3e5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3e/00a3e5f8.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`0081de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081de40.md) [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) [`00a9c4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9c/00a9c4f4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cec1c.md#insn-007cec80) · [`007cecbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cec1c.md#insn-007cecbc)
- 新版 `00801e04`（命令位置の公開資料なし） · `00801e40`（命令位置の公開資料なし）

~~~diff
- 007cec80 ["INT_ADD", "register:40f0:8", ["const:7cec80:8", "const:4:8"]]
- 007cec80 ["CALL", null, ["callee:00c57a90:8"]]
+ 00801e04 ["INT_ADD", "register:40f0:8", ["const:801e04:8", "const:4:8"]]
+ 00801e04 ["CALL", null, ["callee:00c57a90:8"]]
- 007cec80 bytes f0301094
+ 00801e04 bytes 23571194
- 007cecbc ["INT_ADD", "register:40f0:8", ["const:7cecbc:8", "const:4:8"]]
- 007cecbc ["CALL", null, ["callee:0043bb64:8"]]
+ 00801e40 ["INT_ADD", "register:40f0:8", ["const:801e40:8", "const:4:8"]]
+ 00801e40 ["CALL", null, ["callee:0043bb64:8"]]
- 007cecbc bytes ea28f197
+ 00801e40 bytes 49e7f097
~~~


<a id="compare-3e063c9e4422fadf0d9b2122f573b1ce"></a>

### [`007cf14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf14c.md) → [`008022d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008022d0.md) FUN_008022d0

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cf16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf14c.md#insn-007cf16c)
- 新版 `008022f0`（命令位置の公開資料なし）

~~~diff
- 007cf16c ["INT_ADD", "register:40f0:8", ["const:7cf16c:8", "const:4:8"]]
- 007cf16c ["CALL", null, ["callee:00c58050:8"]]
+ 008022f0 ["INT_ADD", "register:40f0:8", ["const:8022f0:8", "const:4:8"]]
+ 008022f0 ["CALL", null, ["callee:00c58050:8"]]
- 007cf16c bytes 25311094
+ 008022f0 bytes 58571194
~~~


<a id="compare-bb1a7140479c6d427c15565d07fced34"></a>

### [`007cf1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf1c8.md) → [`0080234c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md) FUN_0080234c

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`007ef1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef1a0.md) [`007ef34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef34c.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 6件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`008242f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md) [`0082449c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cf278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf1c8.md#insn-007cf278) · [`007cf2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf1c8.md#insn-007cf2ac)
- 新版 `008023fc`（命令位置の公開資料なし） · `00802430`（命令位置の公開資料なし）

~~~diff
- 007cf278 ["INT_ADD", "register:40f0:8", ["const:7cf278:8", "const:4:8"]]
- 007cf278 ["CALL", null, ["callee:00c57a90:8"]]
+ 008023fc ["INT_ADD", "register:40f0:8", ["const:8023fc:8", "const:4:8"]]
+ 008023fc ["CALL", null, ["callee:00c57a90:8"]]
- 007cf278 bytes 722f1094
+ 008023fc bytes a5551194
- 007cf2ac ["INT_ADD", "register:40f0:8", ["const:7cf2ac:8", "const:4:8"]]
- 007cf2ac ["CALL", null, ["callee:0043bb64:8"]]
+ 00802430 ["INT_ADD", "register:40f0:8", ["const:802430:8", "const:4:8"]]
+ 00802430 ["CALL", null, ["callee:0043bb64:8"]]
- 007cf2ac bytes 6e27f197
+ 00802430 bytes cde5f097
~~~


<a id="compare-f92389d8e98626ffad3ca9a32f867789"></a>

### [`007cf2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf2e8.md) → [`0080246c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080246c.md) FUN_0080246c

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005e8d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8d4c.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) [`00a52298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52298.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 5件 [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`00ab0300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0300.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cf308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf2e8.md#insn-007cf308)
- 新版 `0080248c`（命令位置の公開資料なし）

~~~diff
- 007cf308 ["INT_ADD", "register:40f0:8", ["const:7cf308:8", "const:4:8"]]
- 007cf308 ["CALL", null, ["callee:00c58050:8"]]
+ 0080248c ["INT_ADD", "register:40f0:8", ["const:80248c:8", "const:4:8"]]
+ 0080248c ["CALL", null, ["callee:00c58050:8"]]
- 007cf308 bytes be301094
+ 0080248c bytes f1561194
~~~


<a id="compare-53a2813b45427951091343115c44aab5"></a>

### [`007cf32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf32c.md) → [`008024b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008024b0.md) FUN_008024b0

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cf34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf32c.md#insn-007cf34c)
- 新版 `008024d0`（命令位置の公開資料なし）

~~~diff
- 007cf34c ["INT_ADD", "register:40f0:8", ["const:7cf34c:8", "const:4:8"]]
- 007cf34c ["CALL", null, ["callee:00c58050:8"]]
+ 008024d0 ["INT_ADD", "register:40f0:8", ["const:8024d0:8", "const:4:8"]]
+ 008024d0 ["CALL", null, ["callee:00c58050:8"]]
- 007cf34c bytes ad301094
+ 008024d0 bytes e0561194
~~~


<a id="compare-86643ef01792d8e7d73ddd8948985e61"></a>

### [`007cf370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf370.md) → [`008024f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008024f4.md) FUN_008024f4

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aa05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa05ac.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cf408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf370.md#insn-007cf408) · [`007cf43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf370.md#insn-007cf43c)
- 新版 `0080258c`（命令位置の公開資料なし） · `008025c0`（命令位置の公開資料なし）

~~~diff
- 007cf408 ["INT_ADD", "register:40f0:8", ["const:7cf408:8", "const:4:8"]]
- 007cf408 ["CALL", null, ["callee:00c57a90:8"]]
+ 0080258c ["INT_ADD", "register:40f0:8", ["const:80258c:8", "const:4:8"]]
+ 0080258c ["CALL", null, ["callee:00c57a90:8"]]
- 007cf408 bytes 0e2f1094
+ 0080258c bytes 41551194
- 007cf43c ["INT_ADD", "register:40f0:8", ["const:7cf43c:8", "const:4:8"]]
- 007cf43c ["CALL", null, ["callee:0043bb64:8"]]
+ 008025c0 ["INT_ADD", "register:40f0:8", ["const:8025c0:8", "const:4:8"]]
+ 008025c0 ["CALL", null, ["callee:0043bb64:8"]]
- 007cf43c bytes 0a27f197
+ 008025c0 bytes 69e5f097
~~~


<a id="compare-aafa185211eb5f8c54df049242a87790"></a>

### [`007cf46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf46c.md) → [`008025f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008025f0.md) FUN_008025f0

採用 · 移動量 `+0x33184` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005f00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f00b0.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 9件 [`006158d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006158d0.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0078597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md) [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cf48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf46c.md#insn-007cf48c)
- 新版 `00802610`（命令位置の公開資料なし）

~~~diff
- 007cf48c ["INT_ADD", "register:40f0:8", ["const:7cf48c:8", "const:4:8"]]
- 007cf48c ["CALL", null, ["callee:00c58050:8"]]
+ 00802610 ["INT_ADD", "register:40f0:8", ["const:802610:8", "const:4:8"]]
+ 00802610 ["CALL", null, ["callee:00c58050:8"]]
- 007cf48c bytes 5d301094
+ 00802610 bytes 90561194
~~~


<a id="compare-cf16b337fa07088b97b8d0c0285938f8"></a>

### [`007d48ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48ac.md) → [`00807d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d20.md) FUN_00807d20

採用 · 移動量 `+0x33474` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`007d7e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7e70.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d48c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48ac.md#insn-007d48c8) · [`007d48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48ac.md#insn-007d48e0)
- 新版 `00807d3c`（命令位置の公開資料なし） · `00807d54`（命令位置の公開資料なし）

~~~diff
- 007d48c8 ["INT_ADD", "register:40f0:8", ["const:7d48c8:8", "const:4:8"]]
- 007d48c8 ["CALL", null, ["callee:005c175c:8"]]
+ 00807d3c ["INT_ADD", "register:40f0:8", ["const:807d3c:8", "const:4:8"]]
+ 00807d3c ["CALL", null, ["callee:005c175c:8"]]
- 007d48c8 bytes 1922f797
+ 00807d3c bytes 88e6f697
- 007d48e0 ["INT_ADD", "register:40f0:8", ["const:7d48e0:8", "const:4:8"]]
- 007d48e0 ["CALL", null, ["callee:0080b2e4:8"]]
+ 00807d54 ["INT_ADD", "register:40f0:8", ["const:807d54:8", "const:4:8"]]
+ 00807d54 ["CALL", null, ["callee:0080b2e4:8"]]
- 007d48e0 bytes 640d0094
+ 00807d54 bytes 640d0094
~~~


<a id="compare-b64d3c5e6606c2f3d2514ec7f05117d5"></a>

### [`007d7a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7a48.md) → [`0080aebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aebc.md) FUN_0080aebc

採用 · 移動量 `+0x33474` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a29a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29a48.md) · 呼出先 1件 [`007d7e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7e70.md)
- 新版 呼出元 1件 [`00a878d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a878d8.md) · 呼出先 1件 [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d7a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7a48.md#insn-007d7a60)
- 新版 `0080aed4`（命令位置の公開資料なし）

~~~diff
- 007d7a60 ["INT_ADD", "register:40f0:8", ["const:7d7a60:8", "const:4:8"]]
- 007d7a60 ["CALL", null, ["callee:0080b2e4:8"]]
+ 0080aed4 ["INT_ADD", "register:40f0:8", ["const:80aed4:8", "const:4:8"]]
+ 0080aed4 ["CALL", null, ["callee:0080b2e4:8"]]
- 007d7a60 bytes 04010094
+ 0080aed4 bytes 04010094
~~~


<a id="compare-8fc46890ca51fcca1b82c5c73623cf3c"></a>

### [`007d7a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7a78.md) → [`0080aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aeec.md) FUN_0080aeec

採用 · 移動量 `+0x33474` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0079653c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00796/0079653c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`007c7938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d7b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7a78.md#insn-007d7b10) · [`007d7b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7a78.md#insn-007d7b5c)
- 新版 `0080af84`（命令位置の公開資料なし） · `0080afd0`（命令位置の公開資料なし）

~~~diff
- 007d7b10 ["INT_ADD", "register:40f0:8", ["const:7d7b10:8", "const:4:8"]]
- 007d7b10 ["CALL", null, ["callee:00c57a90:8"]]
+ 0080af84 ["INT_ADD", "register:40f0:8", ["const:80af84:8", "const:4:8"]]
+ 0080af84 ["CALL", null, ["callee:00c57a90:8"]]
- 007d7b10 bytes 4c0d1094
+ 0080af84 bytes c3321194
- 007d7b5c ["INT_ADD", "register:40f0:8", ["const:7d7b5c:8", "const:4:8"]]
- 007d7b5c ["CALL", null, ["callee:0043bb64:8"]]
+ 0080afd0 ["INT_ADD", "register:40f0:8", ["const:80afd0:8", "const:4:8"]]
+ 0080afd0 ["CALL", null, ["callee:0043bb64:8"]]
- 007d7b5c bytes 4205f197
+ 0080afd0 bytes e5c2f097
~~~


<a id="compare-39625288f78af0027a597195ed393c43"></a>

### [`007d7b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7b8c.md) → [`0080b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b000.md) FUN_0080b000

採用 · 移動量 `+0x33474` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00902ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00902/00902ef0.md) [`009034dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00903/009034dc.md) [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 4件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00937924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md) [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d7c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7b8c.md#insn-007d7c24) · [`007d7c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7b8c.md#insn-007d7c60)
- 新版 `0080b098`（命令位置の公開資料なし） · `0080b0d4`（命令位置の公開資料なし）

~~~diff
- 007d7c24 ["INT_ADD", "register:40f0:8", ["const:7d7c24:8", "const:4:8"]]
- 007d7c24 ["CALL", null, ["callee:00c57a90:8"]]
+ 0080b098 ["INT_ADD", "register:40f0:8", ["const:80b098:8", "const:4:8"]]
+ 0080b098 ["CALL", null, ["callee:00c57a90:8"]]
- 007d7c24 bytes 070d1094
+ 0080b098 bytes 7e321194
- 007d7c60 ["INT_ADD", "register:40f0:8", ["const:7d7c60:8", "const:4:8"]]
- 007d7c60 ["CALL", null, ["callee:0043bb64:8"]]
+ 0080b0d4 ["INT_ADD", "register:40f0:8", ["const:80b0d4:8", "const:4:8"]]
+ 0080b0d4 ["CALL", null, ["callee:0043bb64:8"]]
- 007d7c60 bytes 0105f197
+ 0080b0d4 bytes a4c2f097
~~~


<a id="compare-1e57a054fddcf836e3167e75d70ea1e7"></a>

### [`007d7c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7c90.md) → [`0080b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b104.md) FUN_0080b104

採用 · 移動量 `+0x33474` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045d300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d300.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d7cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7c90.md#insn-007d7cbc) · [`007d7cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7c90.md#insn-007d7cd4) · [`007d7cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7c90.md#insn-007d7cf8)
- 新版 `0080b130`（命令位置の公開資料なし） · `0080b148`（命令位置の公開資料なし） · `0080b16c`（命令位置の公開資料なし）

~~~diff
- 007d7cbc ["INT_ADD", "register:40f0:8", ["const:7d7cbc:8", "const:4:8"]]
- 007d7cbc ["CALL", null, ["callee:00480198:8"]]
+ 0080b130 ["INT_ADD", "register:40f0:8", ["const:80b130:8", "const:4:8"]]
+ 0080b130 ["CALL", null, ["callee:00480198:8"]]
- 007d7cbc bytes 9115f297
+ 0080b130 bytes 1ad4f197
- 007d7cd4 ["INT_ADD", "register:40f0:8", ["const:7d7cd4:8", "const:4:8"]]
- 007d7cd4 ["CALL", null, ["callee:005c175c:8"]]
+ 0080b148 ["INT_ADD", "register:40f0:8", ["const:80b148:8", "const:4:8"]]
+ 0080b148 ["CALL", null, ["callee:005c175c:8"]]
- 007d7cd4 bytes 1615f797
+ 0080b148 bytes 85d9f697
- 007d7cf8 ["INT_ADD", "register:40f0:8", ["const:7d7cf8:8", "const:4:8"]]
- 007d7cf8 ["CALL", null, ["callee:0043bb64:8"]]
+ 0080b16c ["INT_ADD", "register:40f0:8", ["const:80b16c:8", "const:4:8"]]
+ 0080b16c ["CALL", null, ["callee:0043bb64:8"]]
- 007d7cf8 bytes db04f197
+ 0080b16c bytes 7ec2f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e74450097ed91c3e4f8db7a16d9e10e"></a>

### [`007d7dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7dd4.md) → [`0080b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b248.md) FUN_0080b248

採用 · 移動量 `+0x33474` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 1件 [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 1件 [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7dd4.md#insn-007d7df8) · [`007d7e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7dd4.md#insn-007d7e30) · [`007d7e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7dd4.md#insn-007d7e3c)
- 新版 `0080b26c`（命令位置の公開資料なし） · `0080b2a4`（命令位置の公開資料なし） · `0080b2b0`（命令位置の公開資料なし）

~~~diff
- 007d7df8 ["INT_ADD", "register:40f0:8", ["const:7d7df8:8", "const:4:8"]]
- 007d7df8 ["CALL", null, ["callee:00480ba8:8"]]
+ 0080b26c ["INT_ADD", "register:40f0:8", ["const:80b26c:8", "const:4:8"]]
+ 0080b26c ["CALL", null, ["callee:00480ba8:8"]]
- 007d7df8 bytes c617f297
+ 0080b26c bytes 4fd6f197
- 007d7e30 ["INT_ADD", "register:40f0:8", ["const:7d7e30:8", "const:4:8"]]
- 007d7e30 ["CALL", null, ["callee:00480ba8:8"]]
+ 0080b2a4 ["INT_ADD", "register:40f0:8", ["const:80b2a4:8", "const:4:8"]]
+ 0080b2a4 ["CALL", null, ["callee:00480ba8:8"]]
- 007d7e30 bytes b817f297
+ 0080b2a4 bytes 41d6f197
- 007d7e3c ["INT_ADD", "register:40f0:8", ["const:7d7e3c:8", "const:4:8"]]
- 007d7e3c ["CALL", null, ["callee:00480ba8:8"]]
+ 0080b2b0 ["INT_ADD", "register:40f0:8", ["const:80b2b0:8", "const:4:8"]]
+ 0080b2b0 ["CALL", null, ["callee:00480ba8:8"]]
- 007d7e3c bytes b517f297
+ 0080b2b0 bytes 3ed6f197
~~~


<a id="compare-78d64fd2d1a99cde821e404b60953085"></a>

### [`007d7e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7e70.md) → [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md) FUN_0080b2e4

採用 · 移動量 `+0x33474` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`007d48ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48ac.md) [`007d6524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d6/007d6524.md) [`007d7a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7a48.md) [`007d7e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7e70.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 2件 [`007d7e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7e70.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`00807d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d20.md) [`00809998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00809/00809998.md) [`0080aebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aebc.md) [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d7e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7e70.md#insn-007d7e90) · [`007d7e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7e70.md#insn-007d7e9c)
- 新版 `0080b304`（命令位置の公開資料なし） · `0080b310`（命令位置の公開資料なし）

~~~diff
- 007d7e90 ["INT_ADD", "register:40f0:8", ["const:7d7e90:8", "const:4:8"]]
- 007d7e90 ["CALL", null, ["local:b0:8"]]
+ 0080b304 ["INT_ADD", "register:40f0:8", ["const:80b304:8", "const:4:8"]]
+ 0080b304 ["CALL", null, ["local:b0:8"]]
- 007d7e90 bytes f8ffff97
+ 0080b304 bytes f8ffff97
- 007d7e9c ["INT_ADD", "register:40f0:8", ["const:7d7e9c:8", "const:4:8"]]
- 007d7e9c ["CALL", null, ["local:b0:8"]]
+ 0080b310 ["INT_ADD", "register:40f0:8", ["const:80b310:8", "const:4:8"]]
+ 0080b310 ["CALL", null, ["local:b0:8"]]
- 007d7e9c bytes f5ffff97
+ 0080b310 bytes f5ffff97
~~~


<a id="compare-670950cc8f1e9d0afc5baf173bfb983d"></a>

### [`007d7eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7eb4.md) → [`0080b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md) FUN_0080b328

採用 · 移動量 `+0x33474` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007d48f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48f8.md) [`007d7eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7eb4.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081736c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081736c.md) · 呼出先 2件 [`007d7eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7eb4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00807d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d6c.md) [`0080b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849164.md) · 呼出先 2件 [`0080b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d7ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7eb4.md#insn-007d7ed0) · [`007d7edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7eb4.md#insn-007d7edc) · [`007d7eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7eb4.md#insn-007d7eec)
- 新版 `0080b344`（命令位置の公開資料なし） · `0080b350`（命令位置の公開資料なし） · `0080b360`（命令位置の公開資料なし）

~~~diff
- 007d7ed0 ["INT_ADD", "register:40f0:8", ["const:7d7ed0:8", "const:4:8"]]
- 007d7ed0 ["CALL", null, ["local:b0:8"]]
+ 0080b344 ["INT_ADD", "register:40f0:8", ["const:80b344:8", "const:4:8"]]
+ 0080b344 ["CALL", null, ["local:b0:8"]]
- 007d7ed0 bytes f9ffff97
+ 0080b344 bytes f9ffff97
- 007d7edc ["INT_ADD", "register:40f0:8", ["const:7d7edc:8", "const:4:8"]]
- 007d7edc ["CALL", null, ["local:b0:8"]]
+ 0080b350 ["INT_ADD", "register:40f0:8", ["const:80b350:8", "const:4:8"]]
+ 0080b350 ["CALL", null, ["local:b0:8"]]
- 007d7edc bytes f6ffff97
+ 0080b350 bytes f6ffff97
- 007d7eec ["INT_ADD", "register:40f0:8", ["const:7d7eec:8", "const:4:8"]]
- 007d7eec ["CALL", null, ["callee:00c57ab0:8"]]
+ 0080b360 ["INT_ADD", "register:40f0:8", ["const:80b360:8", "const:4:8"]]
+ 0080b360 ["CALL", null, ["callee:00c57ab0:8"]]
- 007d7eec bytes 5d0c1094
+ 0080b360 bytes d4311194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-177b9cae5dd2ddb021f4e527e0e56b36"></a>

### [`007d9274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9274.md) → [`0080c6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c6e8.md) FUN_0080c6e8

採用 · 移動量 `+0x33474` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 2件 [`0045d240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md) [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007d92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9274.md#insn-007d92a0) · [`007d92d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9274.md#insn-007d92d4) · [`007d92e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9274.md#insn-007d92e4)
- 新版 `0080c714`（命令位置の公開資料なし） · `0080c748`（命令位置の公開資料なし） · `0080c758`（命令位置の公開資料なし）

~~~diff
- 007d92a0 ["INT_ADD", "register:40f0:8", ["const:7d92a0:8", "const:4:8"]]
- 007d92a0 ["CALL", null, ["callee:00480138:8"]]
+ 0080c714 ["INT_ADD", "register:40f0:8", ["const:80c714:8", "const:4:8"]]
+ 0080c714 ["CALL", null, ["callee:00480138:8"]]
- 007d92a0 bytes 0010f297
+ 0080c714 bytes 89cef197
- 007d92d4 ["INT_ADD", "register:40f0:8", ["const:7d92d4:8", "const:4:8"]]
- 007d92d4 ["CALL", null, ["callee:004800d8:8"]]
+ 0080c748 ["INT_ADD", "register:40f0:8", ["const:80c748:8", "const:4:8"]]
+ 0080c748 ["CALL", null, ["callee:004800d8:8"]]
- 007d92d4 bytes db0ff297
+ 0080c748 bytes 64cef197
- 007d92e4 ["INT_ADD", "register:40f0:8", ["const:7d92e4:8", "const:4:8"]]
- 007d92e4 ["CALL", null, ["callee:004800d8:8"]]
+ 0080c758 ["INT_ADD", "register:40f0:8", ["const:80c758:8", "const:4:8"]]
+ 0080c758 ["CALL", null, ["callee:004800d8:8"]]
- 007d92e4 bytes d70ff297
+ 0080c758 bytes 60cef197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9abd8ea9dbd3d303572045770d5b2a"></a>

### [`007db210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db210.md) → [`0080fa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fa8c.md) FUN_0080fa8c

採用 · 移動量 `+0x3487c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`0075b518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b518.md) [`0075d03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d03c.md) · 呼出先 1件 [`007dbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbf90.md)
- 新版 呼出元 9件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0078597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md) [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) · 呼出先 1件 [`0081080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/0081080c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007db254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db210.md#insn-007db254)
- 新版 `0080fad0`（命令位置の公開資料なし）

~~~diff
- 007db254 ["INT_ADD", "register:40f0:8", ["const:7db254:8", "const:4:8"]]
- 007db254 ["CALL", null, ["callee:0081080c:8"]]
+ 0080fad0 ["INT_ADD", "register:40f0:8", ["const:80fad0:8", "const:4:8"]]
+ 0080fad0 ["CALL", null, ["callee:0081080c:8"]]
- 007db254 bytes 4f030094
+ 0080fad0 bytes 4f030094
~~~


<a id="compare-3b15ff10947c5a6ce0e21ff285833774"></a>

### [`007df0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df0b0.md) → [`00813914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813914.md) FUN_00813914

採用 · 移動量 `+0x34864` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007df0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df0b0.md#insn-007df0cc) · [`007df0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df0b0.md#insn-007df0dc)
- 新版 `00813930`（命令位置の公開資料なし） · `00813940`（命令位置の公開資料なし）

~~~diff
- 007df0cc ["INT_ADD", "register:40f0:8", ["const:7df0cc:8", "const:4:8"]]
- 007df0cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00813930 ["INT_ADD", "register:40f0:8", ["const:813930:8", "const:4:8"]]
+ 00813930 ["CALL", null, ["callee:00c57ab0:8"]]
- 007df0cc bytes e5ef0f94
+ 00813930 bytes 60101194
- 007df0dc ["INT_ADD", "register:40f0:8", ["const:7df0dc:8", "const:4:8"]]
- 007df0dc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00813940 ["INT_ADD", "register:40f0:8", ["const:813940:8", "const:4:8"]]
+ 00813940 ["CALL", null, ["callee:00c57ab0:8"]]
- 007df0dc bytes e1ef0f94
+ 00813940 bytes 5c101194
~~~


<a id="compare-0db4c5d635b72de08fe1dd58a47ad683"></a>

### [`007df558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df558.md) → [`00813dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813dbc.md) FUN_00813dbc

採用 · 移動量 `+0x34864` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007df574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df558.md#insn-007df574) · [`007df584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df558.md#insn-007df584)
- 新版 `00813dd8`（命令位置の公開資料なし） · `00813de8`（命令位置の公開資料なし）

~~~diff
- 007df574 ["INT_ADD", "register:40f0:8", ["const:7df574:8", "const:4:8"]]
- 007df574 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00813dd8 ["INT_ADD", "register:40f0:8", ["const:813dd8:8", "const:4:8"]]
+ 00813dd8 ["CALL", null, ["callee:00c57ab0:8"]]
- 007df574 bytes bbee0f94
+ 00813dd8 bytes 360f1194
- 007df584 ["INT_ADD", "register:40f0:8", ["const:7df584:8", "const:4:8"]]
- 007df584 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00813de8 ["INT_ADD", "register:40f0:8", ["const:813de8:8", "const:4:8"]]
+ 00813de8 ["CALL", null, ["callee:00c57ab0:8"]]
- 007df584 bytes b7ee0f94
+ 00813de8 bytes 320f1194
~~~


<a id="compare-b97017986d3f7c093f86c5cfc375d119"></a>

### [`007df5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df5ac.md) → [`00813e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md) FUN_00813e10

採用 · 移動量 `+0x34864` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df104.md) · 呼出先 4件 [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00813968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md) · 呼出先 4件 [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007df5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df5ac.md#insn-007df5f4) · [`007df60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df5ac.md#insn-007df60c) · [`007df634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df5ac.md#insn-007df634)
- 新版 `00813e58`（命令位置の公開資料なし） · `00813e70`（命令位置の公開資料なし） · `00813e98`（命令位置の公開資料なし）

~~~diff
- 007df5f4 ["INT_ADD", "register:40f0:8", ["const:7df5f4:8", "const:4:8"]]
- 007df5f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00813e58 ["INT_ADD", "register:40f0:8", ["const:813e58:8", "const:4:8"]]
+ 00813e58 ["CALL", null, ["callee:00c57a90:8"]]
- 007df5f4 bytes 93ee0f94
+ 00813e58 bytes 0e0f1194
- 007df60c ["INT_ADD", "register:40f0:8", ["const:7df60c:8", "const:4:8"]]
- 007df60c ["CALL", null, ["callee:00c57c00:8"]]
+ 00813e70 ["INT_ADD", "register:40f0:8", ["const:813e70:8", "const:4:8"]]
+ 00813e70 ["CALL", null, ["callee:00c57c00:8"]]
- 007df60c bytes e9ee0f94
+ 00813e70 bytes 640f1194
- 007df634 ["INT_ADD", "register:40f0:8", ["const:7df634:8", "const:4:8"]]
- 007df634 ["CALL", null, ["callee:00c57a90:8"]]
+ 00813e98 ["INT_ADD", "register:40f0:8", ["const:813e98:8", "const:4:8"]]
+ 00813e98 ["CALL", null, ["callee:00c57a90:8"]]
- 007df634 bytes 83ee0f94
+ 00813e98 bytes fe0e1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-072c50d231c11f7297630ba04ac5b5d4"></a>

### [`007df734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df734.md) → [`00813f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813f98.md) FUN_00813f98

採用 · 移動量 `+0x34864` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007df104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df104.md) [`00883ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883ce0.md) · 呼出先 5件 [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00813968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813968.md) [`008b6e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e80.md) · 呼出先 5件 [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007df778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df734.md#insn-007df778) · [`007df7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df734.md#insn-007df7c0) · [`007df7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df734.md#insn-007df7e8)
- 新版 `00813fdc`（命令位置の公開資料なし） · `00814024`（命令位置の公開資料なし） · `0081404c`（命令位置の公開資料なし）

~~~diff
- 007df778 ["INT_ADD", "register:40f0:8", ["const:7df778:8", "const:4:8"]]
- 007df778 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00813fdc ["INT_ADD", "register:40f0:8", ["const:813fdc:8", "const:4:8"]]
+ 00813fdc ["CALL", null, ["callee:00c57ab0:8"]]
- 007df778 bytes 3aee0f94
+ 00813fdc bytes b50e1194
- 007df7c0 ["INT_ADD", "register:40f0:8", ["const:7df7c0:8", "const:4:8"]]
- 007df7c0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00814024 ["INT_ADD", "register:40f0:8", ["const:814024:8", "const:4:8"]]
+ 00814024 ["CALL", null, ["callee:00c57a90:8"]]
- 007df7c0 bytes 20ee0f94
+ 00814024 bytes 9b0e1194
- 007df7e8 ["INT_ADD", "register:40f0:8", ["const:7df7e8:8", "const:4:8"]]
- 007df7e8 ["CALL", null, ["callee:00c57c00:8"]]
+ 0081404c ["INT_ADD", "register:40f0:8", ["const:81404c:8", "const:4:8"]]
+ 0081404c ["CALL", null, ["callee:00c57c00:8"]]
- 007df7e8 bytes 72ee0f94
+ 0081404c bytes ed0e1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1baadc0ba10b593c74d9d838d5eb03e"></a>

### [`007df864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df864.md) → [`008140c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md) FUN_008140c8

採用 · 移動量 `+0x34864` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007de628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007de/007de628.md) [`007df864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df864.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 2件 [`007df864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df864.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00812e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00812/00812e8c.md) [`008140c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`008140c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008140c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007df880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df864.md#insn-007df880) · [`007df88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df864.md#insn-007df88c) · [`007df89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df864.md#insn-007df89c)
- 新版 `008140e4`（命令位置の公開資料なし） · `008140f0`（命令位置の公開資料なし） · `00814100`（命令位置の公開資料なし）

~~~diff
- 007df880 ["INT_ADD", "register:40f0:8", ["const:7df880:8", "const:4:8"]]
- 007df880 ["CALL", null, ["local:b0:8"]]
+ 008140e4 ["INT_ADD", "register:40f0:8", ["const:8140e4:8", "const:4:8"]]
+ 008140e4 ["CALL", null, ["local:b0:8"]]
- 007df880 bytes f9ffff97
+ 008140e4 bytes f9ffff97
- 007df88c ["INT_ADD", "register:40f0:8", ["const:7df88c:8", "const:4:8"]]
- 007df88c ["CALL", null, ["local:b0:8"]]
+ 008140f0 ["INT_ADD", "register:40f0:8", ["const:8140f0:8", "const:4:8"]]
+ 008140f0 ["CALL", null, ["local:b0:8"]]
- 007df88c bytes f6ffff97
+ 008140f0 bytes f6ffff97
- 007df89c ["INT_ADD", "register:40f0:8", ["const:7df89c:8", "const:4:8"]]
- 007df89c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00814100 ["INT_ADD", "register:40f0:8", ["const:814100:8", "const:4:8"]]
+ 00814100 ["CALL", null, ["callee:00c57ab0:8"]]
- 007df89c bytes f1ed0f94
+ 00814100 bytes 6c0e1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c87c2c03e9bb4e03d028f850466b1c2"></a>

### [`007eb8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb8f8.md) → [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) FUN_008206dc

採用 · 移動量 `+0x34de4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007eb474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb474.md) [`007edc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007edc9c.md) [`007edf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007edf34.md) [`007fac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fac0c.md) · 呼出先 10件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`007e550c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e550c.md) [`007fabf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fabf8.md) [`007fad1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fad1c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 4件 [`00820258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/00820258.md) [`00822c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822c58.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`00830020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md) · 呼出先 10件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00819d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d34.md) [`0083000c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/0083000c.md) [`00830130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830130.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007eb950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb8f8.md#insn-007eb950) · [`007eb968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb8f8.md#insn-007eb968) · [`007eb994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb8f8.md#insn-007eb994)
- 新版 `00820734`（命令位置の公開資料なし） · `0082074c`（命令位置の公開資料なし） · `00820778`（命令位置の公開資料なし）

~~~diff
- 007eb950 ["INT_ADD", "register:40f0:8", ["const:7eb950:8", "const:4:8"]]
- 007eb950 ["CALL", null, ["callee:00c57a90:8"]]
+ 00820734 ["INT_ADD", "register:40f0:8", ["const:820734:8", "const:4:8"]]
+ 00820734 ["CALL", null, ["callee:00c57a90:8"]]
- 007eb950 bytes bcbd0f94
+ 00820734 bytes d7dc1094
- 007eb968 ["INT_ADD", "register:40f0:8", ["const:7eb968:8", "const:4:8"]]
- 007eb968 ["CALL", null, ["callee:00c57c00:8"]]
+ 0082074c ["INT_ADD", "register:40f0:8", ["const:82074c:8", "const:4:8"]]
+ 0082074c ["CALL", null, ["callee:00c57c00:8"]]
- 007eb968 bytes 12be0f94
+ 0082074c bytes 2ddd1094
- 007eb994 ["INT_ADD", "register:40f0:8", ["const:7eb994:8", "const:4:8"]]
- 007eb994 ["CALL", null, ["callee:00c538b0:8"]]
+ 00820778 ["INT_ADD", "register:40f0:8", ["const:820778:8", "const:4:8"]]
+ 00820778 ["CALL", null, ["callee:00c538b0:8"]]
- 007eb994 bytes 33ad0f94
+ 00820778 bytes 4ecc1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f0beaf2414994d78b7dfe56dadc8772"></a>

### [`007f8304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8304.md) → [`0082d718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d718.md) FUN_0082d718

採用 · 移動量 `+0x35414` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f8320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8304.md#insn-007f8320) · [`007f8340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8304.md#insn-007f8340)
- 新版 `0082d734`（命令位置の公開資料なし） · `0082d754`（命令位置の公開資料なし）

~~~diff
- 007f8320 ["INT_ADD", "register:40f0:8", ["const:7f8320:8", "const:4:8"]]
- 007f8320 ["CALL", null, ["callee:00c538e0:8"]]
+ 0082d734 ["INT_ADD", "register:40f0:8", ["const:82d734:8", "const:4:8"]]
+ 0082d734 ["CALL", null, ["callee:00c538e0:8"]]
- 007f8320 bytes dc7a0f94
+ 0082d734 bytes 6b981094
- 007f8340 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f8340 ["INT_ADD", "register:40f0:8", ["const:7f8340:8", "const:4:8"]]
- 007f8340 ["CALLIND", null, ["register:0:8"]]
+ 0082d754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0082d754 ["INT_ADD", "register:40f0:8", ["const:82d754:8", "const:4:8"]]
+ 0082d754 ["CALLIND", null, ["register:0:8"]]
- 007f8340 bytes 00013fd6
+ 0082d754 bytes 00013fd6
~~~


<a id="compare-fed2528686521676f587643fa3bf4c9f"></a>

### [`007f8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8aac.md) → [`0082dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dec0.md) FUN_0082dec0

採用 · 移動量 `+0x35414` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 2件 [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f8ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8aac.md#insn-007f8ac0) · [`007f8ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8aac.md#insn-007f8ac8)
- 新版 `0082ded4`（命令位置の公開資料なし） · `0082dedc`（命令位置の公開資料なし）

~~~diff
- 007f8ac0 ["INT_ADD", "register:40f0:8", ["const:7f8ac0:8", "const:4:8"]]
- 007f8ac0 ["CALL", null, ["callee:0046eeb8:8"]]
+ 0082ded4 ["INT_ADD", "register:40f0:8", ["const:82ded4:8", "const:4:8"]]
+ 0082ded4 ["CALL", null, ["callee:0046eeb8:8"]]
- 007f8ac0 bytes 584df197
+ 0082ded4 bytes f903f197
- 007f8ac8 ["INT_ADD", "register:40f0:8", ["const:7f8ac8:8", "const:4:8"]]
- 007f8ac8 ["CALL", null, ["callee:0046e784:8"]]
+ 0082dedc ["INT_ADD", "register:40f0:8", ["const:82dedc:8", "const:4:8"]]
+ 0082dedc ["CALL", null, ["callee:0046e784:8"]]
- 007f8ac8 bytes 894bf197
+ 0082dedc bytes 2a02f197
~~~


<a id="compare-a0c115d49ac55995474c82d7ac3685d4"></a>

### [`007fad1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fad1c.md) → [`00830130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830130.md) FUN_00830130

採用 · 移動量 `+0x35414` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007eb8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb8f8.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007fad8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fad1c.md#insn-007fad8c) · [`007fada0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fad1c.md#insn-007fada0) · [`007fada8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fad1c.md#insn-007fada8)
- 新版 `008301a0`（命令位置の公開資料なし） · `008301b4`（命令位置の公開資料なし） · `008301bc`（命令位置の公開資料なし）

~~~diff
- 007fad8c ["INT_ADD", "register:40f0:8", ["const:7fad8c:8", "const:4:8"]]
- 007fad8c ["CALL", null, ["callee:00c538e0:8"]]
+ 008301a0 ["INT_ADD", "register:40f0:8", ["const:8301a0:8", "const:4:8"]]
+ 008301a0 ["CALL", null, ["callee:00c538e0:8"]]
- 007fad8c bytes 41700f94
+ 008301a0 bytes d08d1094
- 007fada0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007fada0 ["INT_ADD", "register:40f0:8", ["const:7fada0:8", "const:4:8"]]
- 007fada0 ["CALLIND", null, ["register:0:8"]]
+ 008301b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008301b4 ["INT_ADD", "register:40f0:8", ["const:8301b4:8", "const:4:8"]]
+ 008301b4 ["CALLIND", null, ["register:0:8"]]
- 007fada0 bytes 00013fd6
+ 008301b4 bytes 00013fd6
- 007fada8 ["INT_ADD", "register:40f0:8", ["const:7fada8:8", "const:4:8"]]
- 007fada8 ["CALL", null, ["callee:00c57a80:8"]]
+ 008301bc ["INT_ADD", "register:40f0:8", ["const:8301bc:8", "const:4:8"]]
+ 008301bc ["CALL", null, ["callee:00c57a80:8"]]
- 007fada8 bytes a2800f94
+ 008301bc bytes 319e1094
~~~


<a id="compare-1d617c7be88c5eda19649ec4929c3614"></a>

### [`007faf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faf3c.md) → [`00830350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md) FUN_00830350

採用 · 移動量 `+0x35414` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) [`007faf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faf3c.md) [`00815a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815a74.md) · 呼出先 4件 [`007faf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faf3c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`00830350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md) [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · 呼出先 4件 [`00830350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830350.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007faf58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faf3c.md#insn-007faf58) · [`007faf64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faf3c.md#insn-007faf64) · [`007faf78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faf3c.md#insn-007faf78)
- 新版 `0083036c`（命令位置の公開資料なし） · `00830378`（命令位置の公開資料なし） · `0083038c`（命令位置の公開資料なし）

~~~diff
- 007faf58 ["INT_ADD", "register:40f0:8", ["const:7faf58:8", "const:4:8"]]
- 007faf58 ["CALL", null, ["local:b0:8"]]
+ 0083036c ["INT_ADD", "register:40f0:8", ["const:83036c:8", "const:4:8"]]
+ 0083036c ["CALL", null, ["local:b0:8"]]
- 007faf58 bytes f9ffff97
+ 0083036c bytes f9ffff97
- 007faf64 ["INT_ADD", "register:40f0:8", ["const:7faf64:8", "const:4:8"]]
- 007faf64 ["CALL", null, ["local:b0:8"]]
+ 00830378 ["INT_ADD", "register:40f0:8", ["const:830378:8", "const:4:8"]]
+ 00830378 ["CALL", null, ["local:b0:8"]]
- 007faf64 bytes f6ffff97
+ 00830378 bytes f6ffff97
- 007faf78 ["INT_ADD", "register:40f0:8", ["const:7faf78:8", "const:4:8"]]
- 007faf78 ["CALL", null, ["callee:00c538e0:8"]]
+ 0083038c ["INT_ADD", "register:40f0:8", ["const:83038c:8", "const:4:8"]]
+ 0083038c ["CALL", null, ["callee:00c538e0:8"]]
- 007faf78 bytes c66f0f94
+ 0083038c bytes 558d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4334c6601feb4e7706b63468323752e"></a>

### [`007fb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb100.md) → [`00830514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md) FUN_00830514

採用 · 移動量 `+0x35414` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) [`007fb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb100.md) [`00815a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815a74.md) · 呼出先 4件 [`007fb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb100.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`00830514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md) [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · 呼出先 4件 [`00830514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830514.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007fb11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb100.md#insn-007fb11c) · [`007fb128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb100.md#insn-007fb128) · [`007fb13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb100.md#insn-007fb13c)
- 新版 `00830530`（命令位置の公開資料なし） · `0083053c`（命令位置の公開資料なし） · `00830550`（命令位置の公開資料なし）

~~~diff
- 007fb11c ["INT_ADD", "register:40f0:8", ["const:7fb11c:8", "const:4:8"]]
- 007fb11c ["CALL", null, ["local:b0:8"]]
+ 00830530 ["INT_ADD", "register:40f0:8", ["const:830530:8", "const:4:8"]]
+ 00830530 ["CALL", null, ["local:b0:8"]]
- 007fb11c bytes f9ffff97
+ 00830530 bytes f9ffff97
- 007fb128 ["INT_ADD", "register:40f0:8", ["const:7fb128:8", "const:4:8"]]
- 007fb128 ["CALL", null, ["local:b0:8"]]
+ 0083053c ["INT_ADD", "register:40f0:8", ["const:83053c:8", "const:4:8"]]
+ 0083053c ["CALL", null, ["local:b0:8"]]
- 007fb128 bytes f6ffff97
+ 0083053c bytes f6ffff97
- 007fb13c ["INT_ADD", "register:40f0:8", ["const:7fb13c:8", "const:4:8"]]
- 007fb13c ["CALL", null, ["callee:00c538e0:8"]]
+ 00830550 ["INT_ADD", "register:40f0:8", ["const:830550:8", "const:4:8"]]
+ 00830550 ["CALL", null, ["callee:00c538e0:8"]]
- 007fb13c bytes 556f0f94
+ 00830550 bytes e48c1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ece6d7a963292fea562bf5426e6299"></a>

### [`008002f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008002f4.md) → [`00831c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md) FUN_00831c60

採用 · 移動量 `+0x3196c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) [`008002f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008002f4.md) · 呼出先 2件 [`008002f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008002f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) [`00831c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md) · 呼出先 2件 [`00831c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831c60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00800314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008002f4.md#insn-00800314) · [`00800320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008002f4.md#insn-00800320)
- 新版 `00831c80`（命令位置の公開資料なし） · `00831c8c`（命令位置の公開資料なし）

~~~diff
- 00800314 ["INT_ADD", "register:40f0:8", ["const:800314:8", "const:4:8"]]
- 00800314 ["CALL", null, ["local:b0:8"]]
+ 00831c80 ["INT_ADD", "register:40f0:8", ["const:831c80:8", "const:4:8"]]
+ 00831c80 ["CALL", null, ["local:b0:8"]]
- 00800314 bytes f8ffff97
+ 00831c80 bytes f8ffff97
- 00800320 ["INT_ADD", "register:40f0:8", ["const:800320:8", "const:4:8"]]
- 00800320 ["CALL", null, ["local:b0:8"]]
+ 00831c8c ["INT_ADD", "register:40f0:8", ["const:831c8c:8", "const:4:8"]]
+ 00831c8c ["CALL", null, ["local:b0:8"]]
- 00800320 bytes f5ffff97
+ 00831c8c bytes f5ffff97
~~~


<a id="compare-92c698040b9404c0d455bd544a47a9ba"></a>

### [`00803d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803d5c.md) → [`008356c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/008356c8.md) FUN_008356c8

採用 · 移動量 `+0x3196c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00800728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800728.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00832094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832094.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00803d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803d5c.md#insn-00803d7c)
- 新版 `008356e8`（命令位置の公開資料なし）

~~~diff
- 00803d7c ["INT_ADD", "register:40f0:8", ["const:803d7c:8", "const:4:8"]]
- 00803d7c ["CALL", null, ["callee:00c57ab0:8"]]
+ 008356e8 ["INT_ADD", "register:40f0:8", ["const:8356e8:8", "const:4:8"]]
+ 008356e8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00803d7c bytes b95c0f94
+ 008356e8 bytes f2881094
~~~


<a id="compare-0b819d36776a77f331bf4e13d09f910a"></a>

### [`00807be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807be8.md) → [`00839554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839554.md) FUN_00839554

採用 · 移動量 `+0x3196c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md)
- 新版 呼出元 2件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00807c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807be8.md#insn-00807c04) · [`00807c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807be8.md#insn-00807c20)
- 新版 `00839570`（命令位置の公開資料なし） · `0083958c`（命令位置の公開資料なし）

~~~diff
- 00807c04 ["INT_ADD", "register:40f0:8", ["const:807c04:8", "const:4:8"]]
- 00807c04 ["CALL", null, ["callee:005c175c:8"]]
+ 00839570 ["INT_ADD", "register:40f0:8", ["const:839570:8", "const:4:8"]]
+ 00839570 ["CALL", null, ["callee:005c175c:8"]]
- 00807c04 bytes 4a55f697
+ 00839570 bytes 7b20f697
- 00807c20 ["INT_ADD", "register:40f0:8", ["const:807c20:8", "const:4:8"]]
- 00807c20 ["CALL", null, ["callee:00676a20:8"]]
+ 0083958c ["INT_ADD", "register:40f0:8", ["const:83958c:8", "const:4:8"]]
+ 0083958c ["CALL", null, ["callee:00676a20:8"]]
- 00807c20 bytes c822f997
+ 0083958c bytes 25f5f897
~~~


<a id="compare-d4518264ac1540bbb58a795ab6698d66"></a>

### [`00808060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808060.md) → [`008399cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008399cc.md) FUN_008399cc

採用 · 移動量 `+0x3196c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00606588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/00606588.md) [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008080c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808060.md#insn-008080c8) · [`008080fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808060.md#insn-008080fc)
- 新版 `00839a34`（命令位置の公開資料なし） · `00839a68`（命令位置の公開資料なし）

~~~diff
- 008080c8 ["INT_ADD", "register:40f0:8", ["const:8080c8:8", "const:4:8"]]
- 008080c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00839a34 ["INT_ADD", "register:40f0:8", ["const:839a34:8", "const:4:8"]]
+ 00839a34 ["CALL", null, ["callee:00c57a90:8"]]
- 008080c8 bytes de4b0f94
+ 00839a34 bytes 17781094
- 008080fc ["INT_ADD", "register:40f0:8", ["const:8080fc:8", "const:4:8"]]
- 008080fc ["CALL", null, ["callee:0043bb64:8"]]
+ 00839a68 ["INT_ADD", "register:40f0:8", ["const:839a68:8", "const:4:8"]]
+ 00839a68 ["CALL", null, ["callee:0043bb64:8"]]
- 008080fc bytes da43f097
+ 00839a68 bytes 3f08f097
~~~


<a id="compare-b0ee393d91dcaa4a6123e2016c09a459"></a>

### [`008147e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00814/008147e8.md) → [`00846488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846488.md) FUN_00846488

採用 · 移動量 `+0x31ca0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00814800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00814/008147e8.md#insn-00814800)
- 新版 `008464a0`（命令位置の公開資料なし）

~~~diff
- 00814800 ["INT_ADD", "register:40f0:8", ["const:814800:8", "const:4:8"]]
- 00814800 ["CALL", null, ["callee:005c3e3c:8"]]
+ 008464a0 ["INT_ADD", "register:40f0:8", ["const:8464a0:8", "const:4:8"]]
+ 008464a0 ["CALL", null, ["callee:005c3e3c:8"]]
- 00814800 bytes 032cf697
+ 008464a0 bytes 67f6f597
~~~


<a id="compare-770b92a1439e502a30c3bf536e74a383"></a>

### [`008155a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008155a8.md) → [`00847354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847354.md) FUN_00847354

採用 · 移動量 `+0x31dac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008155c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008155a8.md#insn-008155c4) · [`008155e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008155a8.md#insn-008155e4)
- 新版 `00847370`（命令位置の公開資料なし） · `00847390`（命令位置の公開資料なし）

~~~diff
- 008155c4 ["INT_ADD", "register:40f0:8", ["const:8155c4:8", "const:4:8"]]
- 008155c4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00847370 ["INT_ADD", "register:40f0:8", ["const:847370:8", "const:4:8"]]
+ 00847370 ["CALL", null, ["callee:00c538e0:8"]]
- 008155c4 bytes 33060f94
+ 00847370 bytes 5c311094
- 008155e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008155e4 ["INT_ADD", "register:40f0:8", ["const:8155e4:8", "const:4:8"]]
- 008155e4 ["CALLIND", null, ["register:0:8"]]
+ 00847390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847390 ["INT_ADD", "register:40f0:8", ["const:847390:8", "const:4:8"]]
+ 00847390 ["CALLIND", null, ["register:0:8"]]
- 008155e4 bytes 00013fd6
+ 00847390 bytes 00013fd6
~~~


<a id="compare-9499efdf7b76b3cc367ff19f0dd53c46"></a>

### [`008155f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008155f8.md) → [`008473a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md) FUN_008473a4

採用 · 移動量 `+0x31dac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 4件 [`008371d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008371d0.md) [`00837270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837270.md) [`00837354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837354.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 4件 [`00869148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md) [`008691e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md) [`008692cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008692cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00815618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008155f8.md#insn-00815618) · [`00815640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008155f8.md#insn-00815640) · [`00815654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008155f8.md#insn-00815654)
- 新版 `008473c4`（命令位置の公開資料なし） · `008473ec`（命令位置の公開資料なし） · `00847400`（命令位置の公開資料なし）

~~~diff
- 00815618 ["INT_ADD", "register:40f0:8", ["const:815618:8", "const:4:8"]]
- 00815618 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008473c4 ["INT_ADD", "register:40f0:8", ["const:8473c4:8", "const:4:8"]]
+ 008473c4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00815618 bytes 92160f94
+ 008473c4 bytes bb411094
- 00815640 ["INT_ADD", "register:40f0:8", ["const:815640:8", "const:4:8"]]
- 00815640 ["CALL", null, ["callee:00869148:8"]]
+ 008473ec ["INT_ADD", "register:40f0:8", ["const:8473ec:8", "const:4:8"]]
+ 008473ec ["CALL", null, ["callee:00869148:8"]]
- 00815640 bytes e4860094
+ 008473ec bytes 57870094
- 00815654 ["INT_ADD", "register:40f0:8", ["const:815654:8", "const:4:8"]]
- 00815654 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00847400 ["INT_ADD", "register:40f0:8", ["const:847400:8", "const:4:8"]]
+ 00847400 ["CALL", null, ["callee:00c57ab0:8"]]
- 00815654 bytes 83160f94
+ 00847400 bytes ac411094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9110e20d190a0937ccf54e5ddb0d6e4f"></a>

### [`008156c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008156c4.md) → [`00847470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847470.md) FUN_00847470

採用 · 移動量 `+0x31dac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00837408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837408.md) [`00837468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837468.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md) [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008156dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008156c4.md#insn-008156dc)
- 新版 `00847488`（命令位置の公開資料なし）

~~~diff
- 008156dc ["INT_ADD", "register:40f0:8", ["const:8156dc:8", "const:4:8"]]
- 008156dc ["CALL", null, ["callee:00869380:8"]]
+ 00847488 ["INT_ADD", "register:40f0:8", ["const:847488:8", "const:4:8"]]
+ 00847488 ["CALL", null, ["callee:00869380:8"]]
- 008156dc bytes 4b870094
+ 00847488 bytes be870094
~~~


<a id="compare-db808f9b27d5161ed186fd7054f83142"></a>

### [`008156f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008156f4.md) → [`008474a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008474a0.md) FUN_008474a0

採用 · 移動量 `+0x31dac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005d9598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9598.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00815740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008156f4.md#insn-00815740) · [`00815748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008156f4.md#insn-00815748)
- 新版 `008474ec`（命令位置の公開資料なし） · `008474f4`（命令位置の公開資料なし）

~~~diff
- 00815740 ["INT_ADD", "register:40f0:8", ["const:815740:8", "const:4:8"]]
- 00815740 ["CALL", null, ["callee:005fe258:8"]]
+ 008474ec ["INT_ADD", "register:40f0:8", ["const:8474ec:8", "const:4:8"]]
+ 008474ec ["CALL", null, ["callee:005fe258:8"]]
- 00815740 bytes 960ff797
+ 008474ec bytes 5bdbf697
- 00815748 ["INT_ADD", "register:40f0:8", ["const:815748:8", "const:4:8"]]
- 00815748 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008474f4 ["INT_ADD", "register:40f0:8", ["const:8474f4:8", "const:4:8"]]
+ 008474f4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00815748 bytes 46160f94
+ 008474f4 bytes 6f411094
~~~


<a id="compare-e870f4815b94e609819f49f054a956c3"></a>

### [`00815778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815778.md) → [`00847524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847524.md) FUN_00847524

採用 · 移動量 `+0x31dac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008157bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815778.md#insn-008157bc)
- 新版 `00847568`（命令位置の公開資料なし）

~~~diff
- 008157bc ["INT_ADD", "register:40f0:8", ["const:8157bc:8", "const:4:8"]]
- 008157bc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00847568 ["INT_ADD", "register:40f0:8", ["const:847568:8", "const:4:8"]]
+ 00847568 ["CALL", null, ["callee:00c57ab0:8"]]
- 008157bc bytes 29160f94
+ 00847568 bytes 52411094
~~~


<a id="compare-8a5bc086cde09e22fce888c8e61ec1ff"></a>

### [`008157ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008157ec.md) → [`00847598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847598.md) FUN_00847598

採用 · 移動量 `+0x31dac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00815838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008157ec.md#insn-00815838) · [`00815840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008157ec.md#insn-00815840)
- 新版 `008475e4`（命令位置の公開資料なし） · `008475ec`（命令位置の公開資料なし）

~~~diff
- 00815838 ["INT_ADD", "register:40f0:8", ["const:815838:8", "const:4:8"]]
- 00815838 ["CALL", null, ["callee:005c175c:8"]]
+ 008475e4 ["INT_ADD", "register:40f0:8", ["const:8475e4:8", "const:4:8"]]
+ 008475e4 ["CALL", null, ["callee:005c175c:8"]]
- 00815838 bytes 3d1ef697
+ 008475e4 bytes 5ee8f597
- 00815840 ["INT_ADD", "register:40f0:8", ["const:815840:8", "const:4:8"]]
- 00815840 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008475ec ["INT_ADD", "register:40f0:8", ["const:8475ec:8", "const:4:8"]]
+ 008475ec ["CALL", null, ["callee:00c57ab0:8"]]
- 00815840 bytes 08160f94
+ 008475ec bytes 31411094
~~~


<a id="compare-62bbdb0215d7073c711a5c96203c9269"></a>

### [`00815870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815870.md) → [`0084761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084761c.md) FUN_0084761c

採用 · 移動量 `+0x31dac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081588c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815870.md#insn-0081588c) · [`008158ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815870.md#insn-008158ac)
- 新版 `00847638`（命令位置の公開資料なし） · `00847658`（命令位置の公開資料なし）

~~~diff
- 0081588c ["INT_ADD", "register:40f0:8", ["const:81588c:8", "const:4:8"]]
- 0081588c ["CALL", null, ["callee:00c538e0:8"]]
+ 00847638 ["INT_ADD", "register:40f0:8", ["const:847638:8", "const:4:8"]]
+ 00847638 ["CALL", null, ["callee:00c538e0:8"]]
- 0081588c bytes 81050f94
+ 00847638 bytes aa301094
- 008158ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008158ac ["INT_ADD", "register:40f0:8", ["const:8158ac:8", "const:4:8"]]
- 008158ac ["CALLIND", null, ["register:0:8"]]
+ 00847658 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847658 ["INT_ADD", "register:40f0:8", ["const:847658:8", "const:4:8"]]
+ 00847658 ["CALLIND", null, ["register:0:8"]]
- 008158ac bytes 00013fd6
+ 00847658 bytes 00013fd6
~~~


<a id="compare-4bf8488c2193affbd4d5caa913b1d2bc"></a>

### [`008158c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008158c0.md) → [`0084766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084766c.md) FUN_0084766c

採用 · 移動量 `+0x31dac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`008374fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008158d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008158c0.md#insn-008158d8)
- 新版 `00847684`（命令位置の公開資料なし）

~~~diff
- 008158d8 ["INT_ADD", "register:40f0:8", ["const:8158d8:8", "const:4:8"]]
- 008158d8 ["CALL", null, ["callee:00869474:8"]]
+ 00847684 ["INT_ADD", "register:40f0:8", ["const:847684:8", "const:4:8"]]
+ 00847684 ["CALL", null, ["callee:00869474:8"]]
- 008158d8 bytes 09870094
+ 00847684 bytes 7c870094
~~~


<a id="compare-b1bf23c8979f4a1508d87b1c6d10cacc"></a>

### [`008158f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008158f0.md) → [`0084769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084769c.md) FUN_0084769c

採用 · 移動量 `+0x31dac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00815030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815030.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00846cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008158f0.md#insn-0081592c) · [`0081595c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008158f0.md#insn-0081595c) · [`0081598c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008158f0.md#insn-0081598c)
- 新版 `008476d8`（命令位置の公開資料なし） · `00847708`（命令位置の公開資料なし） · `00847738`（命令位置の公開資料なし）

~~~diff
- 0081592c ["COPY", "register:0:8", ["register:4040:8"]]
- 0081592c ["INT_ADD", "register:40f0:8", ["const:81592c:8", "const:4:8"]]
- 0081592c ["CALLIND", null, ["register:0:8"]]
+ 008476d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008476d8 ["INT_ADD", "register:40f0:8", ["const:8476d8:8", "const:4:8"]]
+ 008476d8 ["CALLIND", null, ["register:0:8"]]
- 0081592c bytes 00013fd6
+ 008476d8 bytes 00013fd6
- 0081595c ["COPY", "register:0:8", ["register:4040:8"]]
- 0081595c ["INT_ADD", "register:40f0:8", ["const:81595c:8", "const:4:8"]]
- 0081595c ["CALLIND", null, ["register:0:8"]]
+ 00847708 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847708 ["INT_ADD", "register:40f0:8", ["const:847708:8", "const:4:8"]]
+ 00847708 ["CALLIND", null, ["register:0:8"]]
- 0081595c bytes 00013fd6
+ 00847708 bytes 00013fd6
- 0081598c ["COPY", "register:0:8", ["register:4040:8"]]
- 0081598c ["INT_ADD", "register:40f0:8", ["const:81598c:8", "const:4:8"]]
- 0081598c ["CALLIND", null, ["register:0:8"]]
+ 00847738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847738 ["INT_ADD", "register:40f0:8", ["const:847738:8", "const:4:8"]]
+ 00847738 ["CALLIND", null, ["register:0:8"]]
- 0081598c bytes 00013fd6
+ 00847738 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf95c86a1c83c02982e290b4329382b0"></a>

### [`00815a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815a74.md) → [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) FUN_00847820

採用 · 移動量 `+0x31dac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 11件 [`00595874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595874.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`007fadd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fadd0.md)
- 新版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 11件 [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`008301e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00815a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815a74.md#insn-00815a8c) · [`00815a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815a74.md#insn-00815a98) · [`00815aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815a74.md#insn-00815aa4)
- 新版 `00847838`（命令位置の公開資料なし） · `00847844`（命令位置の公開資料なし） · `00847850`（命令位置の公開資料なし）

~~~diff
- 00815a8c ["INT_ADD", "register:40f0:8", ["const:815a8c:8", "const:4:8"]]
- 00815a8c ["CALL", null, ["callee:00830514:8"]]
+ 00847838 ["INT_ADD", "register:40f0:8", ["const:847838:8", "const:4:8"]]
+ 00847838 ["CALL", null, ["callee:00830514:8"]]
- 00815a8c bytes 9d95ff97
+ 00847838 bytes 37a3ff97
- 00815a98 ["INT_ADD", "register:40f0:8", ["const:815a98:8", "const:4:8"]]
- 00815a98 ["CALL", null, ["callee:005c3e3c:8"]]
+ 00847844 ["INT_ADD", "register:40f0:8", ["const:847844:8", "const:4:8"]]
+ 00847844 ["CALL", null, ["callee:005c3e3c:8"]]
- 00815a98 bytes 5d27f697
+ 00847844 bytes 7ef1f597
- 00815aa4 ["INT_ADD", "register:40f0:8", ["const:815aa4:8", "const:4:8"]]
- 00815aa4 ["CALL", null, ["callee:005c3e3c:8"]]
+ 00847850 ["INT_ADD", "register:40f0:8", ["const:847850:8", "const:4:8"]]
+ 00847850 ["CALL", null, ["callee:005c3e3c:8"]]
- 00815aa4 bytes 5a27f697
+ 00847850 bytes 7bf1f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa090ffa7f2ab3ea4e31568312349b7a"></a>

### [`00815c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815c14.md) → [`008479c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479c0.md) FUN_008479c0

採用 · 移動量 `+0x31dac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00815c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815c14.md#insn-00815c30) · [`00815c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815c14.md#insn-00815c38)
- 新版 `008479dc`（命令位置の公開資料なし） · `008479e4`（命令位置の公開資料なし）

~~~diff
- 00815c30 ["INT_ADD", "register:40f0:8", ["const:815c30:8", "const:4:8"]]
- 00815c30 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008479dc ["INT_ADD", "register:40f0:8", ["const:8479dc:8", "const:4:8"]]
+ 008479dc ["CALL", null, ["callee:00c57ab0:8"]]
- 00815c30 bytes 0c150f94
+ 008479dc bytes 35401094
- 00815c38 ["INT_ADD", "register:40f0:8", ["const:815c38:8", "const:4:8"]]
- 00815c38 ["CALL", null, ["callee:0046e864:8"]]
+ 008479e4 ["INT_ADD", "register:40f0:8", ["const:8479e4:8", "const:4:8"]]
+ 008479e4 ["CALL", null, ["callee:0046e864:8"]]
- 00815c38 bytes 65d7f097
+ 008479e4 bytes a09bf097
~~~


<a id="compare-3a9749c0cff48cac4367b4ee8565e012"></a>

### [`00816068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816068.md) → [`00847e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847e24.md) FUN_00847e24

採用 · 移動量 `+0x31dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008160ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816068.md#insn-008160ac)
- 新版 `00847e68`（命令位置の公開資料なし）

~~~diff
- 008160ac ["INT_ADD", "register:40f0:8", ["const:8160ac:8", "const:4:8"]]
- 008160ac ["CALL", null, ["callee:00c57ab0:8"]]
+ 00847e68 ["INT_ADD", "register:40f0:8", ["const:847e68:8", "const:4:8"]]
+ 00847e68 ["CALL", null, ["callee:00c57ab0:8"]]
- 008160ac bytes ed130f94
+ 00847e68 bytes 123f1094
~~~


<a id="compare-7dcce1ef40f6ba81249438d68c55f576"></a>

### [`008160dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008160dc.md) → [`00847e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847e98.md) FUN_00847e98

採用 · 移動量 `+0x31dbc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0064c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c428.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008160f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008160dc.md#insn-008160f0) · [`008160fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008160dc.md#insn-008160fc)
- 新版 `00847eac`（命令位置の公開資料なし） · `00847eb8`（命令位置の公開資料なし）

~~~diff
- 008160f0 ["INT_ADD", "register:40f0:8", ["const:8160f0:8", "const:4:8"]]
- 008160f0 ["CALL", null, ["callee:00672708:8"]]
+ 00847eac ["INT_ADD", "register:40f0:8", ["const:847eac:8", "const:4:8"]]
+ 00847eac ["CALL", null, ["callee:00672708:8"]]
- 008160f0 bytes ced8f897
+ 00847eac bytes 17aaf897
- 008160fc ["INT_ADD", "register:40f0:8", ["const:8160fc:8", "const:4:8"]]
- 008160fc ["CALL", null, ["callee:00676a20:8"]]
+ 00847eb8 ["INT_ADD", "register:40f0:8", ["const:847eb8:8", "const:4:8"]]
+ 00847eb8 ["CALL", null, ["callee:00676a20:8"]]
- 008160fc bytes 91e9f897
+ 00847eb8 bytes dabaf897
~~~


<a id="compare-6954b6dc600f8255dcc9b77151b3131c"></a>

### [`00816114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816114.md) → [`00847ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ed0.md) FUN_00847ed0

採用 · 移動量 `+0x31dbc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d580.md) [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081612c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816114.md#insn-0081612c)
- 新版 `00847ee8`（命令位置の公開資料なし）

~~~diff
- 0081612c ["INT_ADD", "register:40f0:8", ["const:81612c:8", "const:4:8"]]
- 0081612c ["CALL", null, ["callee:005c1bb0:8"]]
+ 00847ee8 ["INT_ADD", "register:40f0:8", ["const:847ee8:8", "const:4:8"]]
+ 00847ee8 ["CALL", null, ["callee:005c1bb0:8"]]
- 0081612c bytes 151df697
+ 00847ee8 bytes 32e7f597
~~~


<a id="compare-71668028f4aa23015223f1d0c678d77d"></a>

### [`00816140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816140.md) → [`00847efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847efc.md) FUN_00847efc

採用 · 移動量 `+0x31dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816140.md#insn-00816178) · [`0081618c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816140.md#insn-0081618c) · [`00816194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816140.md#insn-00816194)
- 新版 `00847f34`（命令位置の公開資料なし） · `00847f48`（命令位置の公開資料なし） · `00847f50`（命令位置の公開資料なし）

~~~diff
- 00816178 ["INT_ADD", "register:40f0:8", ["const:816178:8", "const:4:8"]]
- 00816178 ["CALL", null, ["callee:00c538e0:8"]]
+ 00847f34 ["INT_ADD", "register:40f0:8", ["const:847f34:8", "const:4:8"]]
+ 00847f34 ["CALL", null, ["callee:00c538e0:8"]]
- 00816178 bytes 46030f94
+ 00847f34 bytes 6b2e1094
- 0081618c ["COPY", "register:0:8", ["register:4040:8"]]
- 0081618c ["INT_ADD", "register:40f0:8", ["const:81618c:8", "const:4:8"]]
- 0081618c ["CALLIND", null, ["register:0:8"]]
+ 00847f48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847f48 ["INT_ADD", "register:40f0:8", ["const:847f48:8", "const:4:8"]]
+ 00847f48 ["CALLIND", null, ["register:0:8"]]
- 0081618c bytes 00013fd6
+ 00847f48 bytes 00013fd6
- 00816194 ["INT_ADD", "register:40f0:8", ["const:816194:8", "const:4:8"]]
- 00816194 ["CALL", null, ["callee:00c57a80:8"]]
+ 00847f50 ["INT_ADD", "register:40f0:8", ["const:847f50:8", "const:4:8"]]
+ 00847f50 ["CALL", null, ["callee:00c57a80:8"]]
- 00816194 bytes a7130f94
+ 00847f50 bytes cc3e1094
~~~


<a id="compare-dc712c27975dc01ccdce0e6cf44f2404"></a>

### [`00816524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816524.md) → [`008482e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008482e0.md) FUN_008482e0

採用 · 移動量 `+0x31dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816524.md#insn-00816538) · [`00816540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816524.md#insn-00816540) · [`00816548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816524.md#insn-00816548)
- 新版 `008482f4`（命令位置の公開資料なし） · `008482fc`（命令位置の公開資料なし） · `00848304`（命令位置の公開資料なし）

~~~diff
- 00816538 ["INT_ADD", "register:40f0:8", ["const:816538:8", "const:4:8"]]
- 00816538 ["CALL", null, ["callee:0046e864:8"]]
+ 008482f4 ["INT_ADD", "register:40f0:8", ["const:8482f4:8", "const:4:8"]]
+ 008482f4 ["CALL", null, ["callee:0046e864:8"]]
- 00816538 bytes 25d5f097
+ 008482f4 bytes 5c99f097
- 00816540 ["INT_ADD", "register:40f0:8", ["const:816540:8", "const:4:8"]]
- 00816540 ["CALL", null, ["callee:0046e864:8"]]
+ 008482fc ["INT_ADD", "register:40f0:8", ["const:8482fc:8", "const:4:8"]]
+ 008482fc ["CALL", null, ["callee:0046e864:8"]]
- 00816540 bytes 23d5f097
+ 008482fc bytes 5a99f097
- 00816548 ["INT_ADD", "register:40f0:8", ["const:816548:8", "const:4:8"]]
- 00816548 ["CALL", null, ["callee:0046e864:8"]]
+ 00848304 ["INT_ADD", "register:40f0:8", ["const:848304:8", "const:4:8"]]
+ 00848304 ["CALL", null, ["callee:0046e864:8"]]
- 00816548 bytes 21d5f097
+ 00848304 bytes 5899f097
~~~


<a id="compare-85c4eab0acf7db5283573406514d05ba"></a>

### [`0081655c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081655c.md) → [`00848318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848318.md) FUN_00848318

採用 · 移動量 `+0x31dbc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081655c.md#insn-00816570) · [`00816578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081655c.md#insn-00816578) · [`00816580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081655c.md#insn-00816580)
- 新版 `0084832c`（命令位置の公開資料なし） · `00848334`（命令位置の公開資料なし） · `0084833c`（命令位置の公開資料なし）

~~~diff
- 00816570 ["INT_ADD", "register:40f0:8", ["const:816570:8", "const:4:8"]]
- 00816570 ["CALL", null, ["callee:0046ef9c:8"]]
+ 0084832c ["INT_ADD", "register:40f0:8", ["const:84832c:8", "const:4:8"]]
+ 0084832c ["CALL", null, ["callee:0046ef9c:8"]]
- 00816570 bytes e5d6f097
+ 0084832c bytes 1c9bf097
- 00816578 ["INT_ADD", "register:40f0:8", ["const:816578:8", "const:4:8"]]
- 00816578 ["CALL", null, ["callee:0046ef9c:8"]]
+ 00848334 ["INT_ADD", "register:40f0:8", ["const:848334:8", "const:4:8"]]
+ 00848334 ["CALL", null, ["callee:0046ef9c:8"]]
- 00816578 bytes e3d6f097
+ 00848334 bytes 1a9bf097
- 00816580 ["INT_ADD", "register:40f0:8", ["const:816580:8", "const:4:8"]]
- 00816580 ["CALL", null, ["callee:0046ef9c:8"]]
+ 0084833c ["INT_ADD", "register:40f0:8", ["const:84833c:8", "const:4:8"]]
+ 0084833c ["CALL", null, ["callee:0046ef9c:8"]]
- 00816580 bytes e1d6f097
+ 0084833c bytes 189bf097
~~~


<a id="compare-9eae5c27e585d1abfcbec7032be63b06"></a>

### [`00816594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816594.md) → [`00848350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848350.md) FUN_00848350

採用 · 移動量 `+0x31dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`007dc22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc22c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00810aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008165ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816594.md#insn-008165ac) · [`008165bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816594.md#insn-008165bc)
- 新版 `00848368`（命令位置の公開資料なし） · `00848378`（命令位置の公開資料なし）

~~~diff
- 008165ac ["INT_ADD", "register:40f0:8", ["const:8165ac:8", "const:4:8"]]
- 008165ac ["CALL", null, ["callee:00810aa8:8"]]
+ 00848368 ["INT_ADD", "register:40f0:8", ["const:848368:8", "const:4:8"]]
+ 00848368 ["CALL", null, ["callee:00810aa8:8"]]
- 008165ac bytes 2017ff97
+ 00848368 bytes d021ff97
- 008165bc ["INT_ADD", "register:40f0:8", ["const:8165bc:8", "const:4:8"]]
- 008165bc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848378 ["INT_ADD", "register:40f0:8", ["const:848378:8", "const:4:8"]]
+ 00848378 ["CALL", null, ["callee:00c57ab0:8"]]
- 008165bc bytes a9120f94
+ 00848378 bytes ce3d1094
~~~


<a id="compare-403a5bcefd8a1c3760f3dc45dad3fa6f"></a>

### [`00816674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816674.md) → [`00848430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848430.md) FUN_00848430

採用 · 移動量 `+0x31dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008166bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816674.md#insn-008166bc) · [`008166cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816674.md#insn-008166cc)
- 新版 `00848478`（命令位置の公開資料なし） · `00848488`（命令位置の公開資料なし）

~~~diff
- 008166bc ["INT_ADD", "register:40f0:8", ["const:8166bc:8", "const:4:8"]]
- 008166bc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848478 ["INT_ADD", "register:40f0:8", ["const:848478:8", "const:4:8"]]
+ 00848478 ["CALL", null, ["callee:00c57ab0:8"]]
- 008166bc bytes 69120f94
+ 00848478 bytes 8e3d1094
- 008166cc ["INT_ADD", "register:40f0:8", ["const:8166cc:8", "const:4:8"]]
- 008166cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848488 ["INT_ADD", "register:40f0:8", ["const:848488:8", "const:4:8"]]
+ 00848488 ["CALL", null, ["callee:00c57ab0:8"]]
- 008166cc bytes 65120f94
+ 00848488 bytes 8a3d1094
~~~


<a id="compare-641099dbfa35c79acbdbb1ebe4830064"></a>

### [`00816778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816778.md) → [`00848570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848570.md) FUN_00848570

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0076d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d5c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00797a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797a98.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816778.md#insn-00816794)
- 新版 `0084858c`（命令位置の公開資料なし）

~~~diff
- 00816794 ["INT_ADD", "register:40f0:8", ["const:816794:8", "const:4:8"]]
- 00816794 ["CALL", null, ["callee:00797a98:8"]]
+ 0084858c ["INT_ADD", "register:40f0:8", ["const:84858c:8", "const:4:8"]]
+ 0084858c ["CALL", null, ["callee:00797a98:8"]]
- 00816794 bytes 8c5bfd97
+ 0084858c bytes 433dfd97
~~~


<a id="compare-fd908a279e2a4ec35da46934f9f9e427"></a>

### [`008167b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008167b4.md) → [`008485ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485ac.md) FUN_008485ac

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cd38.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008167d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008167b4.md#insn-008167d0)
- 新版 `008485c8`（命令位置の公開資料なし）

~~~diff
- 008167d0 ["INT_ADD", "register:40f0:8", ["const:8167d0:8", "const:4:8"]]
- 008167d0 ["CALL", null, ["callee:005b1368:8"]]
+ 008485c8 ["INT_ADD", "register:40f0:8", ["const:8485c8:8", "const:4:8"]]
+ 008485c8 ["CALL", null, ["callee:005b1368:8"]]
- 008167d0 bytes 5ad9f597
+ 008485c8 bytes 68a3f597
~~~


<a id="compare-a77d9bbafc51f542e61255f2cf6ecf99"></a>

### [`008167f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008167f0.md) → [`008485e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485e8.md) FUN_008485e8

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0063c684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c684.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0066295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/0066295c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008167f0.md#insn-00816810)
- 新版 `00848608`（命令位置の公開資料なし）

~~~diff
- 00816810 ["INT_ADD", "register:40f0:8", ["const:816810:8", "const:4:8"]]
- 00816810 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848608 ["INT_ADD", "register:40f0:8", ["const:848608:8", "const:4:8"]]
+ 00848608 ["CALL", null, ["callee:00c57ab0:8"]]
- 00816810 bytes 14120f94
+ 00848608 bytes 2a3d1094
~~~


<a id="compare-40448b159e1f3b1619abb7e5ad4dba2d"></a>

### [`00816828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816828.md) → [`00848620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848620.md) FUN_00848620

採用 · 移動量 `+0x31df8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0084b6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b6f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0087e690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e690.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816828.md#insn-00816844)
- 新版 `0084863c`（命令位置の公開資料なし）

~~~diff
- 00816844 ["INT_ADD", "register:40f0:8", ["const:816844:8", "const:4:8"]]
- 00816844 ["CALL", null, ["callee:0087e690:8"]]
+ 0084863c ["INT_ADD", "register:40f0:8", ["const:84863c:8", "const:4:8"]]
+ 0084863c ["CALL", null, ["callee:0087e690:8"]]
- 00816844 bytes add30094
+ 0084863c bytes 15d80094
~~~


<a id="compare-600c915efad6464d6d0c56a649bb0f8a"></a>

### [`00816864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816864.md) → [`0084865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084865c.md) FUN_0084865c

採用 · 移動量 `+0x31df8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0084a530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a530.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0087d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d4c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816864.md#insn-00816880)
- 新版 `00848678`（命令位置の公開資料なし）

~~~diff
- 00816880 ["INT_ADD", "register:40f0:8", ["const:816880:8", "const:4:8"]]
- 00816880 ["CALL", null, ["callee:0087d4c8:8"]]
+ 00848678 ["INT_ADD", "register:40f0:8", ["const:848678:8", "const:4:8"]]
+ 00848678 ["CALL", null, ["callee:0087d4c8:8"]]
- 00816880 bytes 2ccf0094
+ 00848678 bytes 94d30094
~~~


<a id="compare-b0a758f4e5ef8e8be1d3b2e6513ec339"></a>

### [`008168a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008168a0.md) → [`00848698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848698.md) FUN_00848698

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00845f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f00.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008781ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008781ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008168bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008168a0.md#insn-008168bc)
- 新版 `008486b4`（命令位置の公開資料なし）

~~~diff
- 008168bc ["INT_ADD", "register:40f0:8", ["const:8168bc:8", "const:4:8"]]
- 008168bc ["CALL", null, ["callee:008781ec:8"]]
+ 008486b4 ["INT_ADD", "register:40f0:8", ["const:8486b4:8", "const:4:8"]]
+ 008486b4 ["CALL", null, ["callee:008781ec:8"]]
- 008168bc bytes 91bd0094
+ 008486b4 bytes cebe0094
~~~


<a id="compare-1f446739aa9e6b75bad8c932a6547465"></a>

### [`00816918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816918.md) → [`00848710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848710.md) FUN_00848710

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0085474c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/0085474c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008876e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816918.md#insn-00816934)
- 新版 `0084872c`（命令位置の公開資料なし）

~~~diff
- 00816934 ["INT_ADD", "register:40f0:8", ["const:816934:8", "const:4:8"]]
- 00816934 ["CALL", null, ["callee:008876e4:8"]]
+ 0084872c ["INT_ADD", "register:40f0:8", ["const:84872c:8", "const:4:8"]]
+ 0084872c ["CALL", null, ["callee:008876e4:8"]]
- 00816934 bytes 86f70094
+ 0084872c bytes eefb0094
~~~


<a id="compare-f5e38a5fed3db4ab5fa05b189235d3d0"></a>

### [`00816954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816954.md) → [`0084874c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084874c.md) FUN_0084874c

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00982bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982bf0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009b86d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816954.md#insn-00816970)
- 新版 `00848768`（命令位置の公開資料なし）

~~~diff
- 00816970 ["INT_ADD", "register:40f0:8", ["const:816970:8", "const:4:8"]]
- 00816970 ["CALL", null, ["callee:009b86d0:8"]]
+ 00848768 ["INT_ADD", "register:40f0:8", ["const:848768:8", "const:4:8"]]
+ 00848768 ["CALL", null, ["callee:009b86d0:8"]]
- 00816970 bytes a0b00594
+ 00848768 bytes dabf0594
~~~


<a id="compare-a763190faf8f665ddedcebb4118770c4"></a>

### [`00816990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816990.md) → [`00848788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848788.md) FUN_00848788

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00837f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837f3c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008169b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816990.md#insn-008169b0) · [`008169b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816990.md#insn-008169b8)
- 新版 `008487a8`（命令位置の公開資料なし） · `008487b0`（命令位置の公開資料なし）

~~~diff
- 008169b0 ["INT_ADD", "register:40f0:8", ["const:8169b0:8", "const:4:8"]]
- 008169b0 ["CALL", null, ["callee:00869eb4:8"]]
+ 008487a8 ["INT_ADD", "register:40f0:8", ["const:8487a8:8", "const:4:8"]]
+ 008487a8 ["CALL", null, ["callee:00869eb4:8"]]
- 008169b0 bytes 63850094
+ 008487a8 bytes c3850094
- 008169b8 ["INT_ADD", "register:40f0:8", ["const:8169b8:8", "const:4:8"]]
- 008169b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008487b0 ["INT_ADD", "register:40f0:8", ["const:8487b0:8", "const:4:8"]]
+ 008487b0 ["CALL", null, ["callee:00c57ab0:8"]]
- 008169b8 bytes aa110f94
+ 008487b0 bytes c03c1094
~~~


<a id="compare-76bbab7146ccb5eb50188ae2c47a3313"></a>

### [`00816aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816aa4.md) → [`0084889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084889c.md) FUN_0084889c

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`008380ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008380ac.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816aa4.md#insn-00816abc)
- 新版 `008488b4`（命令位置の公開資料なし）

~~~diff
- 00816abc ["INT_ADD", "register:40f0:8", ["const:816abc:8", "const:4:8"]]
- 00816abc ["CALL", null, ["callee:005c175c:8"]]
+ 008488b4 ["INT_ADD", "register:40f0:8", ["const:8488b4:8", "const:4:8"]]
+ 008488b4 ["CALL", null, ["callee:005c175c:8"]]
- 00816abc bytes 9c19f697
+ 008488b4 bytes aae3f597
~~~


<a id="compare-dfa44afa0bfa6e7916315b59187dc336"></a>

### [`00816d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816d24.md) → [`00848b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b1c.md) FUN_00848b1c

採用 · 移動量 `+0x31df8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0059d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d170.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816d24.md#insn-00816d3c) · [`00816d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816d24.md#insn-00816d48)
- 新版 `00848b34`（命令位置の公開資料なし） · `00848b40`（命令位置の公開資料なし）

~~~diff
- 00816d3c ["INT_ADD", "register:40f0:8", ["const:816d3c:8", "const:4:8"]]
- 00816d3c ["CALL", null, ["callee:005c17a0:8"]]
+ 00848b34 ["INT_ADD", "register:40f0:8", ["const:848b34:8", "const:4:8"]]
+ 00848b34 ["CALL", null, ["callee:005c17a0:8"]]
- 00816d3c bytes 0d19f697
+ 00848b34 bytes 1be3f597
- 00816d48 ["INT_ADD", "register:40f0:8", ["const:816d48:8", "const:4:8"]]
- 00816d48 ["CALL", null, ["callee:00676a20:8"]]
+ 00848b40 ["INT_ADD", "register:40f0:8", ["const:848b40:8", "const:4:8"]]
+ 00848b40 ["CALL", null, ["callee:00676a20:8"]]
- 00816d48 bytes 7ee6f897
+ 00848b40 bytes b8b7f897
~~~


<a id="compare-d3000c759ce6c45d79c96c137ada755b"></a>

### [`00816d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816d60.md) → [`00848b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b58.md) FUN_00848b58

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`008381f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008381f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a168.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816d60.md#insn-00816d78) · [`00816d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816d60.md#insn-00816d84) · [`00816d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816d60.md#insn-00816d94)
- 新版 `00848b70`（命令位置の公開資料なし） · `00848b7c`（命令位置の公開資料なし） · `00848b8c`（命令位置の公開資料なし）

~~~diff
- 00816d78 ["INT_ADD", "register:40f0:8", ["const:816d78:8", "const:4:8"]]
- 00816d78 ["CALL", null, ["callee:005c175c:8"]]
+ 00848b70 ["INT_ADD", "register:40f0:8", ["const:848b70:8", "const:4:8"]]
+ 00848b70 ["CALL", null, ["callee:005c175c:8"]]
- 00816d78 bytes ed18f697
+ 00848b70 bytes fbe2f597
- 00816d84 ["INT_ADD", "register:40f0:8", ["const:816d84:8", "const:4:8"]]
- 00816d84 ["CALL", null, ["callee:005c175c:8"]]
+ 00848b7c ["INT_ADD", "register:40f0:8", ["const:848b7c:8", "const:4:8"]]
+ 00848b7c ["CALL", null, ["callee:005c175c:8"]]
- 00816d84 bytes ea18f697
+ 00848b7c bytes f8e2f597
- 00816d94 ["INT_ADD", "register:40f0:8", ["const:816d94:8", "const:4:8"]]
- 00816d94 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848b8c ["INT_ADD", "register:40f0:8", ["const:848b8c:8", "const:4:8"]]
+ 00848b8c ["CALL", null, ["callee:00c57ab0:8"]]
- 00816d94 bytes b3100f94
+ 00848b8c bytes c93b1094
~~~


<a id="compare-09cc6bbef5e9fcd4f58be46edd054d97"></a>

### [`00816dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816dac.md) → [`00848ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ba4.md) FUN_00848ba4

採用 · 移動量 `+0x31df8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0059d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d170.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816dac.md#insn-00816dc4) · [`00816dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816dac.md#insn-00816dd0)
- 新版 `00848bbc`（命令位置の公開資料なし） · `00848bc8`（命令位置の公開資料なし）

~~~diff
- 00816dc4 ["INT_ADD", "register:40f0:8", ["const:816dc4:8", "const:4:8"]]
- 00816dc4 ["CALL", null, ["callee:005c17a0:8"]]
+ 00848bbc ["INT_ADD", "register:40f0:8", ["const:848bbc:8", "const:4:8"]]
+ 00848bbc ["CALL", null, ["callee:005c17a0:8"]]
- 00816dc4 bytes eb18f697
+ 00848bbc bytes f9e2f597
- 00816dd0 ["INT_ADD", "register:40f0:8", ["const:816dd0:8", "const:4:8"]]
- 00816dd0 ["CALL", null, ["callee:00676a20:8"]]
+ 00848bc8 ["INT_ADD", "register:40f0:8", ["const:848bc8:8", "const:4:8"]]
+ 00848bc8 ["CALL", null, ["callee:00676a20:8"]]
- 00816dd0 bytes 5ce6f897
+ 00848bc8 bytes 96b7f897
~~~


<a id="compare-6937fd73cd8ec6969f925421f24b6ca7"></a>

### [`00816de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816de8.md) → [`00848be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848be0.md) FUN_00848be0

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 5件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00838234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838234.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 5件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a1ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816de8.md#insn-00816e00) · [`00816e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816de8.md#insn-00816e08) · [`00816e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816de8.md#insn-00816e18)
- 新版 `00848bf8`（命令位置の公開資料なし） · `00848c00`（命令位置の公開資料なし） · `00848c10`（命令位置の公開資料なし）

~~~diff
- 00816e00 ["INT_ADD", "register:40f0:8", ["const:816e00:8", "const:4:8"]]
- 00816e00 ["CALL", null, ["callee:0046e864:8"]]
+ 00848bf8 ["INT_ADD", "register:40f0:8", ["const:848bf8:8", "const:4:8"]]
+ 00848bf8 ["CALL", null, ["callee:0046e864:8"]]
- 00816e00 bytes f3d2f097
+ 00848bf8 bytes 1b97f097
- 00816e08 ["INT_ADD", "register:40f0:8", ["const:816e08:8", "const:4:8"]]
- 00816e08 ["CALL", null, ["callee:0046ef9c:8"]]
+ 00848c00 ["INT_ADD", "register:40f0:8", ["const:848c00:8", "const:4:8"]]
+ 00848c00 ["CALL", null, ["callee:0046ef9c:8"]]
- 00816e08 bytes bfd4f097
+ 00848c00 bytes e798f097
- 00816e18 ["INT_ADD", "register:40f0:8", ["const:816e18:8", "const:4:8"]]
- 00816e18 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848c10 ["INT_ADD", "register:40f0:8", ["const:848c10:8", "const:4:8"]]
+ 00848c10 ["CALL", null, ["callee:00c57ab0:8"]]
- 00816e18 bytes 92100f94
+ 00848c10 bytes a83b1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baa8f9f481327684fd6f50986c65ed57"></a>

### [`00816ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816ec4.md) → [`00848cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848cbc.md) FUN_00848cbc

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0067c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c7f0.md) [`008382c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008382c0.md) [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`0086a238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00816ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816ec4.md#insn-00816ee4) · [`00816eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816ec4.md#insn-00816eec) · [`00816ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816ec4.md#insn-00816ef4)
- 新版 `00848cdc`（命令位置の公開資料なし） · `00848ce4`（命令位置の公開資料なし） · `00848cec`（命令位置の公開資料なし）

~~~diff
- 00816ee4 ["INT_ADD", "register:40f0:8", ["const:816ee4:8", "const:4:8"]]
- 00816ee4 ["CALL", null, ["callee:006a2b38:8"]]
+ 00848cdc ["INT_ADD", "register:40f0:8", ["const:848cdc:8", "const:4:8"]]
+ 00848cdc ["CALL", null, ["callee:006a2b38:8"]]
- 00816ee4 bytes 4396f997
+ 00848cdc bytes 9767f997
- 00816eec ["INT_ADD", "register:40f0:8", ["const:816eec:8", "const:4:8"]]
- 00816eec ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848ce4 ["INT_ADD", "register:40f0:8", ["const:848ce4:8", "const:4:8"]]
+ 00848ce4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00816eec bytes 5d100f94
+ 00848ce4 bytes 733b1094
- 00816ef4 ["INT_ADD", "register:40f0:8", ["const:816ef4:8", "const:4:8"]]
- 00816ef4 ["CALL", null, ["callee:00c57a60:8"]]
+ 00848cec ["INT_ADD", "register:40f0:8", ["const:848cec:8", "const:4:8"]]
+ 00848cec ["CALL", null, ["callee:00c57a60:8"]]
- 00816ef4 bytes 47100f94
+ 00848cec bytes 5d3b1094
~~~


<a id="compare-a8a0885f1cf2192e3b1417d7ab8feed1"></a>

### [`008170f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008170f0.md) → [`00848ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ee8.md) FUN_00848ee8

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00763798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763798.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0081710c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008170f0.md#insn-0081710c) · [`0081711c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008170f0.md#insn-0081711c) · [`0081712c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008170f0.md#insn-0081712c)
- 新版 `00848f04`（命令位置の公開資料なし） · `00848f14`（命令位置の公開資料なし） · `00848f24`（命令位置の公開資料なし）

~~~diff
- 0081710c ["INT_ADD", "register:40f0:8", ["const:81710c:8", "const:4:8"]]
- 0081710c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848f04 ["INT_ADD", "register:40f0:8", ["const:848f04:8", "const:4:8"]]
+ 00848f04 ["CALL", null, ["callee:00c57ab0:8"]]
- 0081710c bytes d50f0f94
+ 00848f04 bytes eb3a1094
- 0081711c ["INT_ADD", "register:40f0:8", ["const:81711c:8", "const:4:8"]]
- 0081711c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848f14 ["INT_ADD", "register:40f0:8", ["const:848f14:8", "const:4:8"]]
+ 00848f14 ["CALL", null, ["callee:00c57ab0:8"]]
- 0081711c bytes d10f0f94
+ 00848f14 bytes e73a1094
- 0081712c ["INT_ADD", "register:40f0:8", ["const:81712c:8", "const:4:8"]]
- 0081712c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00848f24 ["INT_ADD", "register:40f0:8", ["const:848f24:8", "const:4:8"]]
+ 00848f24 ["CALL", null, ["callee:00c57ab0:8"]]
- 0081712c bytes cd0f0f94
+ 00848f24 bytes e33a1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f27b92e8bec3c8fb49eed78a5d306fbd"></a>

### [`008173e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008173e4.md) → [`008491dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491dc.md) FUN_008491dc

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`0065134c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/0065134c.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0067762c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/0067762c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008173fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008173e4.md#insn-008173fc) · [`00817408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008173e4.md#insn-00817408) · [`00817414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008173e4.md#insn-00817414)
- 新版 `008491f4`（命令位置の公開資料なし） · `00849200`（命令位置の公開資料なし） · `0084920c`（命令位置の公開資料なし）

~~~diff
- 008173fc ["INT_ADD", "register:40f0:8", ["const:8173fc:8", "const:4:8"]]
- 008173fc ["CALL", null, ["callee:00676a20:8"]]
+ 008491f4 ["INT_ADD", "register:40f0:8", ["const:8491f4:8", "const:4:8"]]
+ 008491f4 ["CALL", null, ["callee:00676a20:8"]]
- 008173fc bytes d1e4f897
+ 008491f4 bytes 0bb6f897
- 00817408 ["INT_ADD", "register:40f0:8", ["const:817408:8", "const:4:8"]]
- 00817408 ["CALL", null, ["callee:005c175c:8"]]
+ 00849200 ["INT_ADD", "register:40f0:8", ["const:849200:8", "const:4:8"]]
+ 00849200 ["CALL", null, ["callee:005c175c:8"]]
- 00817408 bytes 4917f697
+ 00849200 bytes 57e1f597
- 00817414 ["INT_ADD", "register:40f0:8", ["const:817414:8", "const:4:8"]]
- 00817414 ["CALL", null, ["callee:005c175c:8"]]
+ 0084920c ["INT_ADD", "register:40f0:8", ["const:84920c:8", "const:4:8"]]
+ 0084920c ["CALL", null, ["callee:005c175c:8"]]
- 00817414 bytes 4617f697
+ 0084920c bytes 54e1f597
~~~


<a id="compare-0b8dc20a7275d7f957b8754bc53aceb8"></a>

### [`0081742c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081742c.md) → [`00849224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849224.md) FUN_00849224

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00656480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656480.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0067c760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c760.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081742c.md#insn-00817470) · [`00817480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081742c.md#insn-00817480)
- 新版 `00849268`（命令位置の公開資料なし） · `00849278`（命令位置の公開資料なし）

~~~diff
- 00817470 ["INT_ADD", "register:40f0:8", ["const:817470:8", "const:4:8"]]
- 00817470 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00849268 ["INT_ADD", "register:40f0:8", ["const:849268:8", "const:4:8"]]
+ 00849268 ["CALL", null, ["callee:00c57ab0:8"]]
- 00817470 bytes fc0e0f94
+ 00849268 bytes 123a1094
- 00817480 ["INT_ADD", "register:40f0:8", ["const:817480:8", "const:4:8"]]
- 00817480 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00849278 ["INT_ADD", "register:40f0:8", ["const:849278:8", "const:4:8"]]
+ 00849278 ["CALL", null, ["callee:00c57ab0:8"]]
- 00817480 bytes f80e0f94
+ 00849278 bytes 0e3a1094
~~~


<a id="compare-63aa6d59798c45af2de0ef1434d06526"></a>

### [`00817940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817940.md) → [`00849738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849738.md) FUN_00849738

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) [`008385ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008385ec.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`0086a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a564.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817940.md#insn-00817968) · [`00817974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817940.md#insn-00817974) · [`00817998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817940.md#insn-00817998)
- 新版 `00849760`（命令位置の公開資料なし） · `0084976c`（命令位置の公開資料なし） · `00849790`（命令位置の公開資料なし）

~~~diff
- 00817968 ["INT_ADD", "register:40f0:8", ["const:817968:8", "const:4:8"]]
- 00817968 ["CALL", null, ["callee:0073a2c4:8"]]
+ 00849760 ["INT_ADD", "register:40f0:8", ["const:849760:8", "const:4:8"]]
+ 00849760 ["CALL", null, ["callee:0073a2c4:8"]]
- 00817968 bytes 17e2fb97
+ 00849760 bytes d9c2fb97
- 00817974 ["INT_ADD", "register:40f0:8", ["const:817974:8", "const:4:8"]]
- 00817974 ["CALL", null, ["callee:0086a564:8"]]
+ 0084976c ["INT_ADD", "register:40f0:8", ["const:84976c:8", "const:4:8"]]
+ 0084976c ["CALL", null, ["callee:0086a564:8"]]
- 00817974 bytes 1e830094
+ 0084976c bytes 7e830094
- 00817998 ["INT_ADD", "register:40f0:8", ["const:817998:8", "const:4:8"]]
- 00817998 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00849790 ["INT_ADD", "register:40f0:8", ["const:849790:8", "const:4:8"]]
+ 00849790 ["CALL", null, ["callee:00c57ae0:8"]]
- 00817998 bytes be0d0f94
+ 00849790 bytes d4381094
~~~


<a id="compare-6f7fd8f5b7d0cdb787dfe6163a7da12a"></a>

### [`00817a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817a90.md) → [`00849888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849888.md) FUN_00849888

採用 · 移動量 `+0x31df8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0067fd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067f/0067fd50.md) [`0067fda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067f/0067fda0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006a6098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6098.md) [`006a60e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a60e8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817a90.md#insn-00817aa8)
- 新版 `008498a0`（命令位置の公開資料なし）

~~~diff
- 00817aa8 ["INT_ADD", "register:40f0:8", ["const:817aa8:8", "const:4:8"]]
- 00817aa8 ["CALL", null, ["callee:006a6098:8"]]
+ 008498a0 ["INT_ADD", "register:40f0:8", ["const:8498a0:8", "const:4:8"]]
+ 008498a0 ["CALL", null, ["callee:006a6098:8"]]
- 00817aa8 bytes aaa0f997
+ 008498a0 bytes fe71f997
~~~


<a id="compare-85bb596ff10e663da5ed2f21ccce8199"></a>

### [`00817ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817ba8.md) → [`008499a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008499a0.md) FUN_008499a0

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817ba8.md#insn-00817bc0)
- 新版 `008499b8`（命令位置の公開資料なし）

~~~diff
- 00817bc0 ["INT_ADD", "register:40f0:8", ["const:817bc0:8", "const:4:8"]]
- 00817bc0 ["CALL", null, ["callee:005c3e3c:8"]]
+ 008499b8 ["INT_ADD", "register:40f0:8", ["const:8499b8:8", "const:4:8"]]
+ 008499b8 ["CALL", null, ["callee:005c3e3c:8"]]
- 00817bc0 bytes 131ff697
+ 008499b8 bytes 21e9f597
~~~


<a id="compare-9d57ce4b04d91822a8b3c17019e4d995"></a>

### [`00817bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817bd8.md) → [`008499d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008499d0.md) FUN_008499d0

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817bd8.md#insn-00817bf8)
- 新版 `008499f0`（命令位置の公開資料なし）

~~~diff
- 00817bf8 ["INT_ADD", "register:40f0:8", ["const:817bf8:8", "const:4:8"]]
- 00817bf8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008499f0 ["INT_ADD", "register:40f0:8", ["const:8499f0:8", "const:4:8"]]
+ 008499f0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00817bf8 bytes 1a0d0f94
+ 008499f0 bytes 30381094
~~~


<a id="compare-7ac8d1a35a9cb911b5c21f8a12b6791c"></a>

### [`00817c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817c10.md) → [`00849a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a08.md) FUN_00849a08

採用 · 移動量 `+0x31df8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0059d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d170.md) [`008387a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008387a8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`0086a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a720.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817c10.md#insn-00817c28) · [`00817c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817c10.md#insn-00817c38) · [`00817c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817c10.md#insn-00817c48)
- 新版 `00849a20`（命令位置の公開資料なし） · `00849a30`（命令位置の公開資料なし） · `00849a40`（命令位置の公開資料なし）

~~~diff
- 00817c28 ["INT_ADD", "register:40f0:8", ["const:817c28:8", "const:4:8"]]
- 00817c28 ["CALL", null, ["callee:005c175c:8"]]
+ 00849a20 ["INT_ADD", "register:40f0:8", ["const:849a20:8", "const:4:8"]]
+ 00849a20 ["CALL", null, ["callee:005c175c:8"]]
- 00817c28 bytes 4115f697
+ 00849a20 bytes 4fdff597
- 00817c38 ["INT_ADD", "register:40f0:8", ["const:817c38:8", "const:4:8"]]
- 00817c38 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00849a30 ["INT_ADD", "register:40f0:8", ["const:849a30:8", "const:4:8"]]
+ 00849a30 ["CALL", null, ["callee:00c57ab0:8"]]
- 00817c38 bytes 0a0d0f94
+ 00849a30 bytes 20381094
- 00817c48 ["INT_ADD", "register:40f0:8", ["const:817c48:8", "const:4:8"]]
- 00817c48 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00849a40 ["INT_ADD", "register:40f0:8", ["const:849a40:8", "const:4:8"]]
+ 00849a40 ["CALL", null, ["callee:00c57ab0:8"]]
- 00817c48 bytes 060d0f94
+ 00849a40 bytes 1c381094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fdc5e1f6513ca773431291ebb05b9e5"></a>

### [`00817d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817d60.md) → [`00849b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b58.md) FUN_00849b58

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`00838a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838a40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0086a9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817d60.md#insn-00817d78) · [`00817d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817d60.md#insn-00817d84)
- 新版 `00849b70`（命令位置の公開資料なし） · `00849b7c`（命令位置の公開資料なし）

~~~diff
- 00817d78 ["INT_ADD", "register:40f0:8", ["const:817d78:8", "const:4:8"]]
- 00817d78 ["CALL", null, ["callee:00676a20:8"]]
+ 00849b70 ["INT_ADD", "register:40f0:8", ["const:849b70:8", "const:4:8"]]
+ 00849b70 ["CALL", null, ["callee:00676a20:8"]]
- 00817d78 bytes 72e2f897
+ 00849b70 bytes acb3f897
- 00817d84 ["INT_ADD", "register:40f0:8", ["const:817d84:8", "const:4:8"]]
- 00817d84 ["CALL", null, ["callee:005c3e3c:8"]]
+ 00849b7c ["INT_ADD", "register:40f0:8", ["const:849b7c:8", "const:4:8"]]
+ 00849b7c ["CALL", null, ["callee:005c3e3c:8"]]
- 00817d84 bytes a21ef697
+ 00849b7c bytes b0e8f597
~~~


<a id="compare-cf3c01bd3befe40b5923adc371db6938"></a>

### [`00817d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817d9c.md) → [`00849b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b94.md) FUN_00849b94

採用 · 移動量 `+0x31df8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`006fc250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc250.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00726350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00817db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817d9c.md#insn-00817db4) · [`00817dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817d9c.md#insn-00817dc0)
- 新版 `00849bac`（命令位置の公開資料なし） · `00849bb8`（命令位置の公開資料なし）

~~~diff
- 00817db4 ["INT_ADD", "register:40f0:8", ["const:817db4:8", "const:4:8"]]
- 00817db4 ["CALL", null, ["callee:00676a20:8"]]
+ 00849bac ["INT_ADD", "register:40f0:8", ["const:849bac:8", "const:4:8"]]
+ 00849bac ["CALL", null, ["callee:00676a20:8"]]
- 00817db4 bytes 63e2f897
+ 00849bac bytes 9db3f897
- 00817dc0 ["INT_ADD", "register:40f0:8", ["const:817dc0:8", "const:4:8"]]
- 00817dc0 ["CALL", null, ["callee:005c175c:8"]]
+ 00849bb8 ["INT_ADD", "register:40f0:8", ["const:849bb8:8", "const:4:8"]]
+ 00849bb8 ["CALL", null, ["callee:005c175c:8"]]
- 00817dc0 bytes db14f697
+ 00849bb8 bytes e9def597
~~~


<a id="compare-daeef5e6785d2cf544321a9b347207b2"></a>

### [`00836888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/00836888.md) → [`00868800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md) FUN_00868800

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00834d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00834/00834d90.md) [`00836888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/00836888.md) · 呼出先 2件 [`00836888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/00836888.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) [`00868800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md) · 呼出先 2件 [`00868800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008368a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/00836888.md#insn-008368a8) · [`008368b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/00836888.md#insn-008368b4)
- 新版 `00868820`（命令位置の公開資料なし） · `0086882c`（命令位置の公開資料なし）

~~~diff
- 008368a8 ["INT_ADD", "register:40f0:8", ["const:8368a8:8", "const:4:8"]]
- 008368a8 ["CALL", null, ["local:b0:8"]]
+ 00868820 ["INT_ADD", "register:40f0:8", ["const:868820:8", "const:4:8"]]
+ 00868820 ["CALL", null, ["local:b0:8"]]
- 008368a8 bytes f8ffff97
+ 00868820 bytes f8ffff97
- 008368b4 ["INT_ADD", "register:40f0:8", ["const:8368b4:8", "const:4:8"]]
- 008368b4 ["CALL", null, ["local:b0:8"]]
+ 0086882c ["INT_ADD", "register:40f0:8", ["const:86882c:8", "const:4:8"]]
+ 0086882c ["CALL", null, ["local:b0:8"]]
- 008368b4 bytes f5ffff97
+ 0086882c bytes f5ffff97
~~~


<a id="compare-c2e2280a687f3399ae85cc1d405e1ee1"></a>

### [`008368cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/008368cc.md) → [`00868844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md) FUN_00868844

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008350b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00835/008350b0.md) [`008368cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/008368cc.md) · 呼出先 2件 [`008368cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/008368cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) [`00868844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md) · 呼出先 2件 [`00868844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008368ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/008368cc.md#insn-008368ec) · [`008368f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/008368cc.md#insn-008368f8)
- 新版 `00868864`（命令位置の公開資料なし） · `00868870`（命令位置の公開資料なし）

~~~diff
- 008368ec ["INT_ADD", "register:40f0:8", ["const:8368ec:8", "const:4:8"]]
- 008368ec ["CALL", null, ["local:b0:8"]]
+ 00868864 ["INT_ADD", "register:40f0:8", ["const:868864:8", "const:4:8"]]
+ 00868864 ["CALL", null, ["local:b0:8"]]
- 008368ec bytes f8ffff97
+ 00868864 bytes f8ffff97
- 008368f8 ["INT_ADD", "register:40f0:8", ["const:8368f8:8", "const:4:8"]]
- 008368f8 ["CALL", null, ["local:b0:8"]]
+ 00868870 ["INT_ADD", "register:40f0:8", ["const:868870:8", "const:4:8"]]
+ 00868870 ["CALL", null, ["local:b0:8"]]
- 008368f8 bytes f5ffff97
+ 00868870 bytes f5ffff97
~~~


<a id="compare-d80467f410167f1bec4c8f332f1f45bd"></a>

### [`00837180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md) → [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) FUN_008690f8

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00837130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837130.md) [`00837180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md) [`00a076f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a076f4.md) [`00a09db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md) [`00a0a14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a14c.md) · 呼出先 2件 [`00837180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 5件 [`008690a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md) [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) [`00a64d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md) [`00a67a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67a88.md) [`00a67e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67e1c.md) · 呼出先 2件 [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083719c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md#insn-0083719c) · [`008371a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md#insn-008371a8) · [`008371b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md#insn-008371b8)
- 新版 `00869114`（命令位置の公開資料なし） · `00869120`（命令位置の公開資料なし） · `00869130`（命令位置の公開資料なし）

~~~diff
- 0083719c ["INT_ADD", "register:40f0:8", ["const:83719c:8", "const:4:8"]]
- 0083719c ["CALL", null, ["local:b0:8"]]
+ 00869114 ["INT_ADD", "register:40f0:8", ["const:869114:8", "const:4:8"]]
+ 00869114 ["CALL", null, ["local:b0:8"]]
- 0083719c bytes f9ffff97
+ 00869114 bytes f9ffff97
- 008371a8 ["INT_ADD", "register:40f0:8", ["const:8371a8:8", "const:4:8"]]
- 008371a8 ["CALL", null, ["local:b0:8"]]
+ 00869120 ["INT_ADD", "register:40f0:8", ["const:869120:8", "const:4:8"]]
+ 00869120 ["CALL", null, ["local:b0:8"]]
- 008371a8 bytes f6ffff97
+ 00869120 bytes f6ffff97
- 008371b8 ["INT_ADD", "register:40f0:8", ["const:8371b8:8", "const:4:8"]]
- 008371b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00869130 ["INT_ADD", "register:40f0:8", ["const:869130:8", "const:4:8"]]
+ 00869130 ["CALL", null, ["callee:00c57ab0:8"]]
- 008371b8 bytes aa8f0e94
+ 00869130 bytes 60ba0f94
~~~


<a id="compare-08d06d834ae4cacf8d104c0bac5df74c"></a>

### [`00837468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837468.md) → [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md) FUN_008693e0

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008156c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008156c4.md) [`00837468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837468.md) · 呼出先 2件 [`00837468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837468.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847470.md) [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md) · 呼出先 2件 [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00837488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837468.md#insn-00837488) · [`00837494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837468.md#insn-00837494)
- 新版 `00869400`（命令位置の公開資料なし） · `0086940c`（命令位置の公開資料なし）

~~~diff
- 00837488 ["INT_ADD", "register:40f0:8", ["const:837488:8", "const:4:8"]]
- 00837488 ["CALL", null, ["local:b0:8"]]
+ 00869400 ["INT_ADD", "register:40f0:8", ["const:869400:8", "const:4:8"]]
+ 00869400 ["CALL", null, ["local:b0:8"]]
- 00837488 bytes f8ffff97
+ 00869400 bytes f8ffff97
- 00837494 ["INT_ADD", "register:40f0:8", ["const:837494:8", "const:4:8"]]
- 00837494 ["CALL", null, ["local:b0:8"]]
+ 0086940c ["INT_ADD", "register:40f0:8", ["const:86940c:8", "const:4:8"]]
+ 0086940c ["CALL", null, ["local:b0:8"]]
- 00837494 bytes f5ffff97
+ 0086940c bytes f5ffff97
~~~


<a id="compare-03cc12a5c32a2e790a1981e998590ada"></a>

### [`008374ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374ac.md) → [`00869424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md) FUN_00869424

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008374ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374ac.md) · 呼出先 2件 [`008374ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374ac.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md) · 呼出先 2件 [`00869424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008374c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374ac.md#insn-008374c8) · [`008374d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374ac.md#insn-008374d4) · [`008374e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374ac.md#insn-008374e4)
- 新版 `00869440`（命令位置の公開資料なし） · `0086944c`（命令位置の公開資料なし） · `0086945c`（命令位置の公開資料なし）

~~~diff
- 008374c8 ["INT_ADD", "register:40f0:8", ["const:8374c8:8", "const:4:8"]]
- 008374c8 ["CALL", null, ["local:b0:8"]]
+ 00869440 ["INT_ADD", "register:40f0:8", ["const:869440:8", "const:4:8"]]
+ 00869440 ["CALL", null, ["local:b0:8"]]
- 008374c8 bytes f9ffff97
+ 00869440 bytes f9ffff97
- 008374d4 ["INT_ADD", "register:40f0:8", ["const:8374d4:8", "const:4:8"]]
- 008374d4 ["CALL", null, ["local:b0:8"]]
+ 0086944c ["INT_ADD", "register:40f0:8", ["const:86944c:8", "const:4:8"]]
+ 0086944c ["CALL", null, ["local:b0:8"]]
- 008374d4 bytes f6ffff97
+ 0086944c bytes f6ffff97
- 008374e4 ["INT_ADD", "register:40f0:8", ["const:8374e4:8", "const:4:8"]]
- 008374e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086945c ["INT_ADD", "register:40f0:8", ["const:86945c:8", "const:4:8"]]
+ 0086945c ["CALL", null, ["callee:00c57ab0:8"]]
- 008374e4 bytes df8e0e94
+ 0086945c bytes 95b90f94
~~~


<a id="compare-35633a74701a2d5d5959faf6e93c237a"></a>

### [`008374fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374fc.md) → [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md) FUN_00869474

採用 · 移動量 `+0x31f78` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008158c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/008158c0.md) [`008374fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374fc.md) [`00a517d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a517d0.md) [`00a52754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52754.md) · 呼出先 2件 [`008374fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084766c.md) [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md) [`00aaf838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aaf/00aaf838.md) [`00ab07f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab07f8.md) · 呼出先 2件 [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00837518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374fc.md#insn-00837518) · [`00837524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374fc.md#insn-00837524) · [`00837534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008374fc.md#insn-00837534)
- 新版 `00869490`（命令位置の公開資料なし） · `0086949c`（命令位置の公開資料なし） · `008694ac`（命令位置の公開資料なし）

~~~diff
- 00837518 ["INT_ADD", "register:40f0:8", ["const:837518:8", "const:4:8"]]
- 00837518 ["CALL", null, ["local:b0:8"]]
+ 00869490 ["INT_ADD", "register:40f0:8", ["const:869490:8", "const:4:8"]]
+ 00869490 ["CALL", null, ["local:b0:8"]]
- 00837518 bytes f9ffff97
+ 00869490 bytes f9ffff97
- 00837524 ["INT_ADD", "register:40f0:8", ["const:837524:8", "const:4:8"]]
- 00837524 ["CALL", null, ["local:b0:8"]]
+ 0086949c ["INT_ADD", "register:40f0:8", ["const:86949c:8", "const:4:8"]]
+ 0086949c ["CALL", null, ["local:b0:8"]]
- 00837524 bytes f6ffff97
+ 0086949c bytes f6ffff97
- 00837534 ["INT_ADD", "register:40f0:8", ["const:837534:8", "const:4:8"]]
- 00837534 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008694ac ["INT_ADD", "register:40f0:8", ["const:8694ac:8", "const:4:8"]]
+ 008694ac ["CALL", null, ["callee:00c57ab0:8"]]
- 00837534 bytes cb8e0e94
+ 008694ac bytes 81b90f94
~~~


<a id="compare-3464d977b6a11f1b2d4aea2b677a33c4"></a>

### [`008377cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008377cc.md) → [`00869744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md) FUN_00869744

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00815d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815d0c.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`008377cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008377cc.md) · 呼出先 2件 [`008377cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008377cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`00869744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md) · 呼出先 2件 [`00869744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008377ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008377cc.md#insn-008377ec) · [`008377f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008377cc.md#insn-008377f8)
- 新版 `00869764`（命令位置の公開資料なし） · `00869770`（命令位置の公開資料なし）

~~~diff
- 008377ec ["INT_ADD", "register:40f0:8", ["const:8377ec:8", "const:4:8"]]
- 008377ec ["CALL", null, ["local:b0:8"]]
+ 00869764 ["INT_ADD", "register:40f0:8", ["const:869764:8", "const:4:8"]]
+ 00869764 ["CALL", null, ["local:b0:8"]]
- 008377ec bytes f8ffff97
+ 00869764 bytes f8ffff97
- 008377f8 ["INT_ADD", "register:40f0:8", ["const:8377f8:8", "const:4:8"]]
- 008377f8 ["CALL", null, ["local:b0:8"]]
+ 00869770 ["INT_ADD", "register:40f0:8", ["const:869770:8", "const:4:8"]]
+ 00869770 ["CALL", null, ["local:b0:8"]]
- 008377f8 bytes f5ffff97
+ 00869770 bytes f5ffff97
~~~


<a id="compare-1523542018d7712af3baa206d7f4eefc"></a>

### [`00837e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837e08.md) → [`00869d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md) FUN_00869d80

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00837e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837e08.md) · 呼出先 3件 [`00837e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837e08.md) [`00837e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837e58.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md) · 呼出先 3件 [`00869d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md) [`00869dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869dd0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00837e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837e08.md#insn-00837e28) · [`00837e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837e08.md#insn-00837e34) · [`00837e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837e08.md#insn-00837e40)
- 新版 `00869da0`（命令位置の公開資料なし） · `00869dac`（命令位置の公開資料なし） · `00869db8`（命令位置の公開資料なし）

~~~diff
- 00837e28 ["INT_ADD", "register:40f0:8", ["const:837e28:8", "const:4:8"]]
- 00837e28 ["CALL", null, ["local:b0:8"]]
+ 00869da0 ["INT_ADD", "register:40f0:8", ["const:869da0:8", "const:4:8"]]
+ 00869da0 ["CALL", null, ["local:b0:8"]]
- 00837e28 bytes f8ffff97
+ 00869da0 bytes f8ffff97
- 00837e34 ["INT_ADD", "register:40f0:8", ["const:837e34:8", "const:4:8"]]
- 00837e34 ["CALL", null, ["local:b0:8"]]
+ 00869dac ["INT_ADD", "register:40f0:8", ["const:869dac:8", "const:4:8"]]
+ 00869dac ["CALL", null, ["local:b0:8"]]
- 00837e34 bytes f5ffff97
+ 00869dac bytes f5ffff97
- 00837e40 ["INT_ADD", "register:40f0:8", ["const:837e40:8", "const:4:8"]]
- 00837e40 ["CALL", null, ["callee:00869dd0:8"]]
+ 00869db8 ["INT_ADD", "register:40f0:8", ["const:869db8:8", "const:4:8"]]
+ 00869db8 ["CALL", null, ["callee:00869dd0:8"]]
- 00837e40 bytes 06000094
+ 00869db8 bytes 06000094
~~~


<a id="compare-f5aa4ec8178bd0e861fdf2dd6a92587d"></a>

### [`00837eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837eec.md) → [`00869e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md) FUN_00869e64

採用 · 移動量 `+0x31f78` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00837eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837eec.md) [`00a05768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05768.md) · 呼出先 3件 [`0059d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d170.md) [`00837eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837eec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md) [`00a62d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62d54.md) · 呼出先 3件 [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00869e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00837f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837eec.md#insn-00837f0c) · [`00837f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837eec.md#insn-00837f18) · [`00837f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837eec.md#insn-00837f24)
- 新版 `00869e84`（命令位置の公開資料なし） · `00869e90`（命令位置の公開資料なし） · `00869e9c`（命令位置の公開資料なし）

~~~diff
- 00837f0c ["INT_ADD", "register:40f0:8", ["const:837f0c:8", "const:4:8"]]
- 00837f0c ["CALL", null, ["local:b0:8"]]
+ 00869e84 ["INT_ADD", "register:40f0:8", ["const:869e84:8", "const:4:8"]]
+ 00869e84 ["CALL", null, ["local:b0:8"]]
- 00837f0c bytes f8ffff97
+ 00869e84 bytes f8ffff97
- 00837f18 ["INT_ADD", "register:40f0:8", ["const:837f18:8", "const:4:8"]]
- 00837f18 ["CALL", null, ["local:b0:8"]]
+ 00869e90 ["INT_ADD", "register:40f0:8", ["const:869e90:8", "const:4:8"]]
+ 00869e90 ["CALL", null, ["local:b0:8"]]
- 00837f18 bytes f5ffff97
+ 00869e90 bytes f5ffff97
- 00837f24 ["INT_ADD", "register:40f0:8", ["const:837f24:8", "const:4:8"]]
- 00837f24 ["CALL", null, ["callee:005c17a0:8"]]
+ 00869e9c ["INT_ADD", "register:40f0:8", ["const:869e9c:8", "const:4:8"]]
+ 00869e9c ["CALL", null, ["callee:005c17a0:8"]]
- 00837f24 bytes 9394f597
+ 00869e9c bytes 415ef597
~~~


<a id="compare-c5eeaf8a1d2b0164db453a891243a38e"></a>

### [`00837ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837ff8.md) → [`00869f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md) FUN_00869f70

採用 · 移動量 `+0x31f78` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008169e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008169e0.md) [`008a90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a90c0.md) [`008ac5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md) [`008ac998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac998.md) · 呼出先 3件 [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008487d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008487d8.md) [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) [`008e0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0458.md) [`008e083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e083c.md) · 呼出先 3件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00838010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837ff8.md#insn-00838010) · [`0083801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837ff8.md#insn-0083801c) · [`00838028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837ff8.md#insn-00838028)
- 新版 `00869f88`（命令位置の公開資料なし） · `00869f94`（命令位置の公開資料なし） · `00869fa0`（命令位置の公開資料なし）

~~~diff
- 00838010 ["INT_ADD", "register:40f0:8", ["const:838010:8", "const:4:8"]]
- 00838010 ["CALL", null, ["callee:00676a20:8"]]
+ 00869f88 ["INT_ADD", "register:40f0:8", ["const:869f88:8", "const:4:8"]]
+ 00869f88 ["CALL", null, ["callee:00676a20:8"]]
- 00838010 bytes cc61f897
+ 00869f88 bytes a632f897
- 0083801c ["INT_ADD", "register:40f0:8", ["const:83801c:8", "const:4:8"]]
- 0083801c ["CALL", null, ["callee:00676a20:8"]]
+ 00869f94 ["INT_ADD", "register:40f0:8", ["const:869f94:8", "const:4:8"]]
+ 00869f94 ["CALL", null, ["callee:00676a20:8"]]
- 0083801c bytes c961f897
+ 00869f94 bytes a332f897
- 00838028 ["INT_ADD", "register:40f0:8", ["const:838028:8", "const:4:8"]]
- 00838028 ["CALL", null, ["callee:00676a20:8"]]
+ 00869fa0 ["INT_ADD", "register:40f0:8", ["const:869fa0:8", "const:4:8"]]
+ 00869fa0 ["CALL", null, ["callee:00676a20:8"]]
- 00838028 bytes c661f897
+ 00869fa0 bytes a032f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc3e03f2d8061b92e7d797111ea5795"></a>

### [`008380ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008380ac.md) → [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md) FUN_0086a024

採用 · 移動量 `+0x31f78` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00816aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816aa4.md) [`008380ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008380ac.md) [`008a31c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a3/008a31c0.md) · 呼出先 2件 [`008380ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008380ac.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084889c.md) [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md) [`008d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md) · 呼出先 2件 [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008380c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008380ac.md#insn-008380c8) · [`008380d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008380ac.md#insn-008380d4) · [`008380e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008380ac.md#insn-008380e4)
- 新版 `0086a040`（命令位置の公開資料なし） · `0086a04c`（命令位置の公開資料なし） · `0086a05c`（命令位置の公開資料なし）

~~~diff
- 008380c8 ["INT_ADD", "register:40f0:8", ["const:8380c8:8", "const:4:8"]]
- 008380c8 ["CALL", null, ["local:b0:8"]]
+ 0086a040 ["INT_ADD", "register:40f0:8", ["const:86a040:8", "const:4:8"]]
+ 0086a040 ["CALL", null, ["local:b0:8"]]
- 008380c8 bytes f9ffff97
+ 0086a040 bytes f9ffff97
- 008380d4 ["INT_ADD", "register:40f0:8", ["const:8380d4:8", "const:4:8"]]
- 008380d4 ["CALL", null, ["local:b0:8"]]
+ 0086a04c ["INT_ADD", "register:40f0:8", ["const:86a04c:8", "const:4:8"]]
+ 0086a04c ["CALL", null, ["local:b0:8"]]
- 008380d4 bytes f6ffff97
+ 0086a04c bytes f6ffff97
- 008380e4 ["INT_ADD", "register:40f0:8", ["const:8380e4:8", "const:4:8"]]
- 008380e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086a05c ["INT_ADD", "register:40f0:8", ["const:86a05c:8", "const:4:8"]]
+ 0086a05c ["CALL", null, ["callee:00c57ab0:8"]]
- 008380e4 bytes df8b0e94
+ 0086a05c bytes 95b60f94
~~~


<a id="compare-c20565a4f57b23db5306ad39e4e03bf1"></a>

### [`008384f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008384f8.md) → [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md) FUN_0086a470

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008175c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008175c8.md) [`008384f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008384f8.md) [`0094ba84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094b/0094ba84.md) · 呼出先 2件 [`008384f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008384f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008493c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md) [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md) [`00981530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981530.md) · 呼出先 2件 [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00838518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008384f8.md#insn-00838518) · [`00838524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008384f8.md#insn-00838524)
- 新版 `0086a490`（命令位置の公開資料なし） · `0086a49c`（命令位置の公開資料なし）

~~~diff
- 00838518 ["INT_ADD", "register:40f0:8", ["const:838518:8", "const:4:8"]]
- 00838518 ["CALL", null, ["local:b0:8"]]
+ 0086a490 ["INT_ADD", "register:40f0:8", ["const:86a490:8", "const:4:8"]]
+ 0086a490 ["CALL", null, ["local:b0:8"]]
- 00838518 bytes f8ffff97
+ 0086a490 bytes f8ffff97
- 00838524 ["INT_ADD", "register:40f0:8", ["const:838524:8", "const:4:8"]]
- 00838524 ["CALL", null, ["local:b0:8"]]
+ 0086a49c ["INT_ADD", "register:40f0:8", ["const:86a49c:8", "const:4:8"]]
+ 0086a49c ["CALL", null, ["local:b0:8"]]
- 00838524 bytes f5ffff97
+ 0086a49c bytes f5ffff97
~~~


<a id="compare-7887672927c61b4da822b8b87e36b5f8"></a>

### [`0083869c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/0083869c.md) → [`0086a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md) FUN_0086a614

採用 · 移動量 `+0x31f78` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00817a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817a44.md) [`0083869c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/0083869c.md) · 呼出先 2件 [`0083869c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/0083869c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/0084983c.md) [`0086a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md) · 呼出先 2件 [`0086a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008386b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/0083869c.md#insn-008386b8) · [`008386c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/0083869c.md#insn-008386c4) · [`008386d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/0083869c.md#insn-008386d4)
- 新版 `0086a630`（命令位置の公開資料なし） · `0086a63c`（命令位置の公開資料なし） · `0086a64c`（命令位置の公開資料なし）

~~~diff
- 008386b8 ["INT_ADD", "register:40f0:8", ["const:8386b8:8", "const:4:8"]]
- 008386b8 ["CALL", null, ["local:b0:8"]]
+ 0086a630 ["INT_ADD", "register:40f0:8", ["const:86a630:8", "const:4:8"]]
+ 0086a630 ["CALL", null, ["local:b0:8"]]
- 008386b8 bytes f9ffff97
+ 0086a630 bytes f9ffff97
- 008386c4 ["INT_ADD", "register:40f0:8", ["const:8386c4:8", "const:4:8"]]
- 008386c4 ["CALL", null, ["local:b0:8"]]
+ 0086a63c ["INT_ADD", "register:40f0:8", ["const:86a63c:8", "const:4:8"]]
+ 0086a63c ["CALL", null, ["local:b0:8"]]
- 008386c4 bytes f6ffff97
+ 0086a63c bytes f6ffff97
- 008386d4 ["INT_ADD", "register:40f0:8", ["const:8386d4:8", "const:4:8"]]
- 008386d4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086a64c ["INT_ADD", "register:40f0:8", ["const:86a64c:8", "const:4:8"]]
+ 0086a64c ["CALL", null, ["callee:00c57ab0:8"]]
- 008386d4 bytes 638a0e94
+ 0086a64c bytes 19b50f94
~~~


<a id="compare-58d1c04e77186f59fa1f7f2aa676fbf0"></a>

### [`00838920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838920.md) → [`0086a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md) FUN_0086a898

採用 · 移動量 `+0x31f78` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00817cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817cac.md) [`00838920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838920.md) [`0098d74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098d/0098d74c.md) · 呼出先 2件 [`00838920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838920.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md) [`0086a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md) [`009c3240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c3240.md) · 呼出先 2件 [`0086a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00838940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838920.md#insn-00838940) · [`0083894c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838920.md#insn-0083894c)
- 新版 `0086a8b8`（命令位置の公開資料なし） · `0086a8c4`（命令位置の公開資料なし）

~~~diff
- 00838940 ["INT_ADD", "register:40f0:8", ["const:838940:8", "const:4:8"]]
- 00838940 ["CALL", null, ["local:b0:8"]]
+ 0086a8b8 ["INT_ADD", "register:40f0:8", ["const:86a8b8:8", "const:4:8"]]
+ 0086a8b8 ["CALL", null, ["local:b0:8"]]
- 00838940 bytes f8ffff97
+ 0086a8b8 bytes f8ffff97
- 0083894c ["INT_ADD", "register:40f0:8", ["const:83894c:8", "const:4:8"]]
- 0083894c ["CALL", null, ["local:b0:8"]]
+ 0086a8c4 ["INT_ADD", "register:40f0:8", ["const:86a8c4:8", "const:4:8"]]
+ 0086a8c4 ["CALL", null, ["local:b0:8"]]
- 0083894c bytes f5ffff97
+ 0086a8c4 bytes f5ffff97
~~~


