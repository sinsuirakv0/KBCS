# v15.7.4 → v16.0.0 · 要調査の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-85321e1fa8e6f5ad42efdf575009b5af"></a>

### [`0055d910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d910.md) → [`005807a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807a8.md) FUN_005807a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d910.md#insn-0055d92c) · [`0055d94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d910.md#insn-0055d94c)
- 新版 `005807c4`（命令位置の公開資料なし） · `005807e4`（命令位置の公開資料なし）

~~~diff
- 0055d92c ["INT_ADD", "register:40f0:8", ["const:55d92c:8", "const:4:8"]]
- 0055d92c ["CALL", null, ["callee:00c538e0:8"]]
+ 005807c4 ["INT_ADD", "register:40f0:8", ["const:5807c4:8", "const:4:8"]]
+ 005807c4 ["CALL", null, ["callee:00c538e0:8"]]
- 0055d92c bytes 59e51994
+ 005807c4 bytes 474c1b94
- 0055d94c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d94c ["INT_ADD", "register:40f0:8", ["const:55d94c:8", "const:4:8"]]
- 0055d94c ["CALLIND", null, ["register:0:8"]]
+ 005807e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005807e4 ["INT_ADD", "register:40f0:8", ["const:5807e4:8", "const:4:8"]]
+ 005807e4 ["CALLIND", null, ["register:0:8"]]
- 0055d94c bytes 00013fd6
+ 005807e4 bytes 00013fd6
~~~


<a id="compare-2917fe76a60cb28a69d9cd259b42a8da"></a>

### [`0055d960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d960.md) → [`005807f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807f8.md) FUN_005807f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d960.md#insn-0055d97c) · [`0055d99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d960.md#insn-0055d99c)
- 新版 `00580814`（命令位置の公開資料なし） · `00580834`（命令位置の公開資料なし）

~~~diff
- 0055d97c ["INT_ADD", "register:40f0:8", ["const:55d97c:8", "const:4:8"]]
- 0055d97c ["CALL", null, ["callee:00c538e0:8"]]
+ 00580814 ["INT_ADD", "register:40f0:8", ["const:580814:8", "const:4:8"]]
+ 00580814 ["CALL", null, ["callee:00c538e0:8"]]
- 0055d97c bytes 45e51994
+ 00580814 bytes 334c1b94
- 0055d99c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055d99c ["INT_ADD", "register:40f0:8", ["const:55d99c:8", "const:4:8"]]
- 0055d99c ["CALLIND", null, ["register:0:8"]]
+ 00580834 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580834 ["INT_ADD", "register:40f0:8", ["const:580834:8", "const:4:8"]]
+ 00580834 ["CALLIND", null, ["register:0:8"]]
- 0055d99c bytes 00013fd6
+ 00580834 bytes 00013fd6
~~~


<a id="compare-8d92de002d746e6af6c71c96930de8f7"></a>

### [`0055dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dbb0.md) → [`00580a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580a48.md) FUN_00580a48

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d580.md) · 呼出先 2件 [`00bdbd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd50.md) [`00bdbd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd80.md)
- 新版 呼出元 1件 [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) · 呼出先 2件 [`00c587a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587a0.md) [`00c587d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055dbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dbb0.md#insn-0055dbdc) · [`0055dbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dbb0.md#insn-0055dbf0) · [`0055dc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dbb0.md#insn-0055dc08)
- 新版 `00580a74`（命令位置の公開資料なし） · `00580a88`（命令位置の公開資料なし） · `00580aa0`（命令位置の公開資料なし）

~~~diff
- 0055dbdc ["COPY", "register:0:8", ["register:4040:8"]]
- 0055dbdc ["INT_ADD", "register:40f0:8", ["const:55dbdc:8", "const:4:8"]]
- 0055dbdc ["CALLIND", null, ["register:0:8"]]
+ 00580a74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580a74 ["INT_ADD", "register:40f0:8", ["const:580a74:8", "const:4:8"]]
+ 00580a74 ["CALLIND", null, ["register:0:8"]]
- 0055dbdc bytes 00013fd6
+ 00580a74 bytes 00013fd6
- 0055dbf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055dbf0 ["INT_ADD", "register:40f0:8", ["const:55dbf0:8", "const:4:8"]]
- 0055dbf0 ["CALLIND", null, ["register:0:8"]]
+ 00580a88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580a88 ["INT_ADD", "register:40f0:8", ["const:580a88:8", "const:4:8"]]
+ 00580a88 ["CALLIND", null, ["register:0:8"]]
- 0055dbf0 bytes 00013fd6
+ 00580a88 bytes 00013fd6
- 0055dc08 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055dc08 ["INT_ADD", "register:40f0:8", ["const:55dc08:8", "const:4:8"]]
- 0055dc08 ["CALLIND", null, ["register:0:8"]]
+ 00580aa0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580aa0 ["INT_ADD", "register:40f0:8", ["const:580aa0:8", "const:4:8"]]
+ 00580aa0 ["CALLIND", null, ["register:0:8"]]
- 0055dc08 bytes 20013fd6
+ 00580aa0 bytes 20013fd6
~~~


<a id="compare-caf931e58b9ef608f9524653cc1ea4a5"></a>

### [`0055e0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e0d0.md) → [`00580f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580f68.md) FUN_00580f68

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e0d0.md#insn-0055e0ec) · [`0055e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e0d0.md#insn-0055e10c)
- 新版 `00580f84`（命令位置の公開資料なし） · `00580fa4`（命令位置の公開資料なし）

~~~diff
- 0055e0ec ["INT_ADD", "register:40f0:8", ["const:55e0ec:8", "const:4:8"]]
- 0055e0ec ["CALL", null, ["callee:00c538e0:8"]]
+ 00580f84 ["INT_ADD", "register:40f0:8", ["const:580f84:8", "const:4:8"]]
+ 00580f84 ["CALL", null, ["callee:00c538e0:8"]]
- 0055e0ec bytes 69e31994
+ 00580f84 bytes 574a1b94
- 0055e10c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055e10c ["INT_ADD", "register:40f0:8", ["const:55e10c:8", "const:4:8"]]
- 0055e10c ["CALLIND", null, ["register:0:8"]]
+ 00580fa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580fa4 ["INT_ADD", "register:40f0:8", ["const:580fa4:8", "const:4:8"]]
+ 00580fa4 ["CALLIND", null, ["register:0:8"]]
- 0055e10c bytes 00013fd6
+ 00580fa4 bytes 00013fd6
~~~


<a id="compare-3d87e2c73d14b190ec38f59c2e729495"></a>

### [`0055e120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e120.md) → [`00580fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580fb8.md) FUN_00580fb8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055e13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e120.md#insn-0055e13c) · [`0055e15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e120.md#insn-0055e15c)
- 新版 `00580fd4`（命令位置の公開資料なし） · `00580ff4`（命令位置の公開資料なし）

~~~diff
- 0055e13c ["INT_ADD", "register:40f0:8", ["const:55e13c:8", "const:4:8"]]
- 0055e13c ["CALL", null, ["callee:00c538e0:8"]]
+ 00580fd4 ["INT_ADD", "register:40f0:8", ["const:580fd4:8", "const:4:8"]]
+ 00580fd4 ["CALL", null, ["callee:00c538e0:8"]]
- 0055e13c bytes 55e31994
+ 00580fd4 bytes 434a1b94
- 0055e15c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055e15c ["INT_ADD", "register:40f0:8", ["const:55e15c:8", "const:4:8"]]
- 0055e15c ["CALLIND", null, ["register:0:8"]]
+ 00580ff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580ff4 ["INT_ADD", "register:40f0:8", ["const:580ff4:8", "const:4:8"]]
+ 00580ff4 ["CALLIND", null, ["register:0:8"]]
- 0055e15c bytes 00013fd6
+ 00580ff4 bytes 00013fd6
~~~


<a id="compare-005bb978a948185bb7a8bfcb8c48eec5"></a>

### [`0055ed20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ed20.md) → [`00581bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581bb8.md) FUN_00581bb8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053d58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d58c.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb210.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00560424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560424.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c60.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ed9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ed20.md#insn-0055ed9c) · [`0055ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ed20.md#insn-0055ee5c) · [`0055ee68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ed20.md#insn-0055ee68)
- 新版 `00581c34`（命令位置の公開資料なし） · `00581cf4`（命令位置の公開資料なし） · `00581d00`（命令位置の公開資料なし）

~~~diff
- 0055ed9c ["INT_ADD", "register:40f0:8", ["const:55ed9c:8", "const:4:8"]]
- 0055ed9c ["CALL", null, ["callee:00c58200:8"]]
+ 00581c34 ["INT_ADD", "register:40f0:8", ["const:581c34:8", "const:4:8"]]
+ 00581c34 ["CALL", null, ["callee:00c58200:8"]]
- 0055ed9c bytes 85f21994
+ 00581c34 bytes 73591b94
- 0055ee5c ["INT_ADD", "register:40f0:8", ["const:55ee5c:8", "const:4:8"]]
- 0055ee5c ["CALL", null, ["callee:00c57c60:8"]]
+ 00581cf4 ["INT_ADD", "register:40f0:8", ["const:581cf4:8", "const:4:8"]]
+ 00581cf4 ["CALL", null, ["callee:00c57c60:8"]]
- 0055ee5c bytes edf01994
+ 00581cf4 bytes db571b94
- 0055ee68 ["INT_ADD", "register:40f0:8", ["const:55ee68:8", "const:4:8"]]
- 0055ee68 ["CALL", null, ["callee:00c58200:8"]]
+ 00581d00 ["INT_ADD", "register:40f0:8", ["const:581d00:8", "const:4:8"]]
+ 00581d00 ["CALL", null, ["callee:00c58200:8"]]
- 0055ee68 bytes 52f21994
+ 00581d00 bytes 40591b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86fc4fb092a41b93b27d815d3178538c"></a>

### [`0055f05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f05c.md) → [`00581ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581ef4.md) FUN_00581ef4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055f07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f05c.md#insn-0055f07c)
- 新版 `00581f14`（命令位置の公開資料なし）

~~~diff
- 0055f07c ["COPY", "register:0:8", ["register:4050:8"]]
- 0055f07c ["INT_ADD", "register:40f0:8", ["const:55f07c:8", "const:4:8"]]
- 0055f07c ["CALLIND", null, ["register:0:8"]]
+ 00581f14 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00581f14 ["INT_ADD", "register:40f0:8", ["const:581f14:8", "const:4:8"]]
+ 00581f14 ["CALLIND", null, ["register:0:8"]]
- 0055f07c bytes 40013fd6
+ 00581f14 bytes 40013fd6
~~~


<a id="compare-3562abd751b9c05fadf345516d074a7c"></a>

### [`0055fc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fc60.md) → [`00582af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582af8.md) FUN_00582af8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00574734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574734.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055fc98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fc60.md#insn-0055fc98) · [`0055fcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fc60.md#insn-0055fcb4) · [`0055fcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fc60.md#insn-0055fcd0)
- 新版 `00582b30`（命令位置の公開資料なし） · `00582b4c`（命令位置の公開資料なし） · `00582b68`（命令位置の公開資料なし）

~~~diff
- 0055fc98 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055fc98 ["INT_ADD", "register:40f0:8", ["const:55fc98:8", "const:4:8"]]
- 0055fc98 ["CALLIND", null, ["register:0:8"]]
+ 00582b30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00582b30 ["INT_ADD", "register:40f0:8", ["const:582b30:8", "const:4:8"]]
+ 00582b30 ["CALLIND", null, ["register:0:8"]]
- 0055fc98 bytes 20013fd6
+ 00582b30 bytes 20013fd6
- 0055fcb4 ["INT_ADD", "register:40f0:8", ["const:55fcb4:8", "const:4:8"]]
- 0055fcb4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00582b4c ["INT_ADD", "register:40f0:8", ["const:582b4c:8", "const:4:8"]]
+ 00582b4c ["CALL", null, ["callee:00c57a90:8"]]
- 0055fcb4 bytes e3ec1994
+ 00582b4c bytes d1531b94
- 0055fcd0 ["INT_ADD", "register:40f0:8", ["const:55fcd0:8", "const:4:8"]]
- 0055fcd0 ["CALL", null, ["callee:00c57c90:8"]]
+ 00582b68 ["INT_ADD", "register:40f0:8", ["const:582b68:8", "const:4:8"]]
+ 00582b68 ["CALL", null, ["callee:00c57c90:8"]]
- 0055fcd0 bytes 5ced1994
+ 00582b68 bytes 4a541b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d1eabd9ae214b91c5bf9ac08b9b6043"></a>

### [`005602ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005602ec.md) → [`00583184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583184.md) FUN_00583184

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00574734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574734.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005602ec.md#insn-00560324) · [`00560340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005602ec.md#insn-00560340) · [`0056035c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005602ec.md#insn-0056035c)
- 新版 `005831bc`（命令位置の公開資料なし） · `005831d8`（命令位置の公開資料なし） · `005831f4`（命令位置の公開資料なし）

~~~diff
- 00560324 ["COPY", "register:0:8", ["register:4048:8"]]
- 00560324 ["INT_ADD", "register:40f0:8", ["const:560324:8", "const:4:8"]]
- 00560324 ["CALLIND", null, ["register:0:8"]]
+ 005831bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005831bc ["INT_ADD", "register:40f0:8", ["const:5831bc:8", "const:4:8"]]
+ 005831bc ["CALLIND", null, ["register:0:8"]]
- 00560324 bytes 20013fd6
+ 005831bc bytes 20013fd6
- 00560340 ["INT_ADD", "register:40f0:8", ["const:560340:8", "const:4:8"]]
- 00560340 ["CALL", null, ["callee:00c57a90:8"]]
+ 005831d8 ["INT_ADD", "register:40f0:8", ["const:5831d8:8", "const:4:8"]]
+ 005831d8 ["CALL", null, ["callee:00c57a90:8"]]
- 00560340 bytes 40eb1994
+ 005831d8 bytes 2e521b94
- 0056035c ["INT_ADD", "register:40f0:8", ["const:56035c:8", "const:4:8"]]
- 0056035c ["CALL", null, ["callee:00c57c90:8"]]
+ 005831f4 ["INT_ADD", "register:40f0:8", ["const:5831f4:8", "const:4:8"]]
+ 005831f4 ["CALL", null, ["callee:00c57c90:8"]]
- 0056035c bytes b9eb1994
+ 005831f4 bytes a7521b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17796811c156368d25dc95591f3a1314"></a>

### [`005604c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604c4.md) → [`0058335c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058335c.md) FUN_0058335c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdd490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c59ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604c4.md#insn-00560514) · [`00560550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604c4.md#insn-00560550)
- 新版 `005833ac`（命令位置の公開資料なし） · `005833e8`（命令位置の公開資料なし）

~~~diff
- 00560514 ["INT_ADD", "register:40f0:8", ["const:560514:8", "const:4:8"]]
- 00560514 ["CALL", null, ["callee:00c59ee0:8"]]
+ 005833ac ["INT_ADD", "register:40f0:8", ["const:5833ac:8", "const:4:8"]]
+ 005833ac ["CALL", null, ["callee:00c59ee0:8"]]
- 00560514 bytes dff31994
+ 005833ac bytes cd5a1b94
- 00560550 ["INT_ADD", "register:40f0:8", ["const:560550:8", "const:4:8"]]
- 00560550 ["CALL", null, ["callee:00c59ee0:8"]]
+ 005833e8 ["INT_ADD", "register:40f0:8", ["const:5833e8:8", "const:4:8"]]
+ 005833e8 ["CALL", null, ["callee:00c59ee0:8"]]
- 00560550 bytes d0f31994
+ 005833e8 bytes be5a1b94
~~~


<a id="compare-355fd39a8f5b3219c563cab1e39b1222"></a>

### [`005607e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005607e4.md) → [`0058367c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058367c.md) FUN_0058367c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005607e4.md#insn-00560800) · [`00560820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005607e4.md#insn-00560820)
- 新版 `00583698`（命令位置の公開資料なし） · `005836b8`（命令位置の公開資料なし）

~~~diff
- 00560800 ["INT_ADD", "register:40f0:8", ["const:560800:8", "const:4:8"]]
- 00560800 ["CALL", null, ["callee:00c538e0:8"]]
+ 00583698 ["INT_ADD", "register:40f0:8", ["const:583698:8", "const:4:8"]]
+ 00583698 ["CALL", null, ["callee:00c538e0:8"]]
- 00560800 bytes a4d91994
+ 00583698 bytes 92401b94
- 00560820 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560820 ["INT_ADD", "register:40f0:8", ["const:560820:8", "const:4:8"]]
- 00560820 ["CALLIND", null, ["register:0:8"]]
+ 005836b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005836b8 ["INT_ADD", "register:40f0:8", ["const:5836b8:8", "const:4:8"]]
+ 005836b8 ["CALLIND", null, ["register:0:8"]]
- 00560820 bytes 00013fd6
+ 005836b8 bytes 00013fd6
~~~


<a id="compare-00fa0bd2d5b388b707756c517e61e266"></a>

### [`00560834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560834.md) → [`005836cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005836cc.md) FUN_005836cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005261fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005261fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560834.md#insn-00560884) · [`005608b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560834.md#insn-005608b0) · [`005608bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560834.md#insn-005608bc)
- 新版 `0058371c`（命令位置の公開資料なし） · `00583748`（命令位置の公開資料なし） · `00583754`（命令位置の公開資料なし）

~~~diff
- 00560884 ["INT_ADD", "register:40f0:8", ["const:560884:8", "const:4:8"]]
- 00560884 ["CALL", null, ["callee:0043bae0:8"]]
+ 0058371c ["INT_ADD", "register:40f0:8", ["const:58371c:8", "const:4:8"]]
+ 0058371c ["CALL", null, ["callee:0043bae0:8"]]
- 00560884 bytes d7e1fa97
+ 0058371c bytes f1e0fa97
- 005608b0 ["INT_ADD", "register:40f0:8", ["const:5608b0:8", "const:4:8"]]
- 005608b0 ["CALL", null, ["callee:0043bae0:8"]]
+ 00583748 ["INT_ADD", "register:40f0:8", ["const:583748:8", "const:4:8"]]
+ 00583748 ["CALL", null, ["callee:0043bae0:8"]]
- 005608b0 bytes cce1fa97
+ 00583748 bytes e6e0fa97
- 005608bc ["INT_ADD", "register:40f0:8", ["const:5608bc:8", "const:4:8"]]
- 005608bc ["CALL", null, ["callee:00549094:8"]]
+ 00583754 ["INT_ADD", "register:40f0:8", ["const:583754:8", "const:4:8"]]
+ 00583754 ["CALL", null, ["callee:00549094:8"]]
- 005608bc bytes 5016ff97
+ 00583754 bytes 5016ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-529eee3227b20892f2a182909fc0bcf1"></a>

### [`00560944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560944.md) → [`005837dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005837dc.md) FUN_005837dc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00560960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560944.md#insn-00560960)
- 新版 `005837f8`（命令位置の公開資料なし）

~~~diff
- 00560960 ["INT_ADD", "register:40f0:8", ["const:560960:8", "const:4:8"]]
- 00560960 ["CALL", null, ["callee:00c538b0:8"]]
+ 005837f8 ["INT_ADD", "register:40f0:8", ["const:5837f8:8", "const:4:8"]]
+ 005837f8 ["CALL", null, ["callee:00c538b0:8"]]
- 00560960 bytes 40d91994
+ 005837f8 bytes 2e401b94
~~~


<a id="compare-678693b21aa9b4e790b179acf872cb05"></a>

### [`005618f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005618f8.md) → [`00584790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584790.md) FUN_00584790

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005618f8.md#insn-00561934) · [`00561968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005618f8.md#insn-00561968)
- 新版 `005847cc`（命令位置の公開資料なし） · `00584800`（命令位置の公開資料なし）

~~~diff
- 00561934 ["COPY", "register:0:8", ["register:4040:8"]]
- 00561934 ["INT_ADD", "register:40f0:8", ["const:561934:8", "const:4:8"]]
- 00561934 ["CALLIND", null, ["register:0:8"]]
+ 005847cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005847cc ["INT_ADD", "register:40f0:8", ["const:5847cc:8", "const:4:8"]]
+ 005847cc ["CALLIND", null, ["register:0:8"]]
- 00561934 bytes 00013fd6
+ 005847cc bytes 00013fd6
- 00561968 ["COPY", "register:0:8", ["register:4040:8"]]
- 00561968 ["INT_ADD", "register:40f0:8", ["const:561968:8", "const:4:8"]]
- 00561968 ["CALLIND", null, ["register:0:8"]]
+ 00584800 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584800 ["INT_ADD", "register:40f0:8", ["const:584800:8", "const:4:8"]]
+ 00584800 ["CALLIND", null, ["register:0:8"]]
- 00561968 bytes 00013fd6
+ 00584800 bytes 00013fd6
~~~


<a id="compare-a6745c32f425721962ab129e9ac3abff"></a>

### [`00561ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ce8.md) → [`00584b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584b80.md) FUN_00584b80

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ce8.md#insn-00561d04) · [`00561d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ce8.md#insn-00561d24)
- 新版 `00584b9c`（命令位置の公開資料なし） · `00584bbc`（命令位置の公開資料なし）

~~~diff
- 00561d04 ["INT_ADD", "register:40f0:8", ["const:561d04:8", "const:4:8"]]
- 00561d04 ["CALL", null, ["callee:00c538e0:8"]]
+ 00584b9c ["INT_ADD", "register:40f0:8", ["const:584b9c:8", "const:4:8"]]
+ 00584b9c ["CALL", null, ["callee:00c538e0:8"]]
- 00561d04 bytes 63d41994
+ 00584b9c bytes 513b1b94
- 00561d24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00561d24 ["INT_ADD", "register:40f0:8", ["const:561d24:8", "const:4:8"]]
- 00561d24 ["CALLIND", null, ["register:0:8"]]
+ 00584bbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584bbc ["INT_ADD", "register:40f0:8", ["const:584bbc:8", "const:4:8"]]
+ 00584bbc ["CALLIND", null, ["register:0:8"]]
- 00561d24 bytes 00013fd6
+ 00584bbc bytes 00013fd6
~~~


<a id="compare-7480740d1235f530c0505dee849742fd"></a>

### [`00561d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d38.md) → [`00584bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584bd0.md) FUN_00584bd0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d38.md#insn-00561d54) · [`00561d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d38.md#insn-00561d74)
- 新版 `00584bec`（命令位置の公開資料なし） · `00584c0c`（命令位置の公開資料なし）

~~~diff
- 00561d54 ["INT_ADD", "register:40f0:8", ["const:561d54:8", "const:4:8"]]
- 00561d54 ["CALL", null, ["callee:00c538e0:8"]]
+ 00584bec ["INT_ADD", "register:40f0:8", ["const:584bec:8", "const:4:8"]]
+ 00584bec ["CALL", null, ["callee:00c538e0:8"]]
- 00561d54 bytes 4fd41994
+ 00584bec bytes 3d3b1b94
- 00561d74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00561d74 ["INT_ADD", "register:40f0:8", ["const:561d74:8", "const:4:8"]]
- 00561d74 ["CALLIND", null, ["register:0:8"]]
+ 00584c0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584c0c ["INT_ADD", "register:40f0:8", ["const:584c0c:8", "const:4:8"]]
+ 00584c0c ["CALLIND", null, ["register:0:8"]]
- 00561d74 bytes 00013fd6
+ 00584c0c bytes 00013fd6
~~~


<a id="compare-9da28747a4e1b6311a4da0ceecbd0987"></a>

### [`00561d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d88.md) → [`00584c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c20.md) FUN_00584c20

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d88.md#insn-00561dac) · [`00561dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d88.md#insn-00561dc4) · [`00561de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d88.md#insn-00561de8)
- 新版 `00584c44`（命令位置の公開資料なし） · `00584c5c`（命令位置の公開資料なし） · `00584c80`（命令位置の公開資料なし）

~~~diff
- 00561dac ["INT_ADD", "register:40f0:8", ["const:561dac:8", "const:4:8"]]
- 00561dac ["CALL", null, ["callee:00c538b0:8"]]
+ 00584c44 ["INT_ADD", "register:40f0:8", ["const:584c44:8", "const:4:8"]]
+ 00584c44 ["CALL", null, ["callee:00c538b0:8"]]
- 00561dac bytes 2dd41994
+ 00584c44 bytes 1b3b1b94
- 00561dc4 ["INT_ADD", "register:40f0:8", ["const:561dc4:8", "const:4:8"]]
- 00561dc4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00584c5c ["INT_ADD", "register:40f0:8", ["const:584c5c:8", "const:4:8"]]
+ 00584c5c ["CALL", null, ["callee:00c538e0:8"]]
- 00561dc4 bytes 33d41994
+ 00584c5c bytes 213b1b94
- 00561de8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00561de8 ["INT_ADD", "register:40f0:8", ["const:561de8:8", "const:4:8"]]
- 00561de8 ["CALLIND", null, ["register:0:8"]]
+ 00584c80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584c80 ["INT_ADD", "register:40f0:8", ["const:584c80:8", "const:4:8"]]
+ 00584c80 ["CALLIND", null, ["register:0:8"]]
- 00561de8 bytes 00013fd6
+ 00584c80 bytes 00013fd6
~~~


<a id="compare-baaf4b26aa6ff6421c455116329f80d1"></a>

### [`00561e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561e00.md) → [`00584c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c98.md) FUN_00584c98

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574730.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561e00.md#insn-00561e2c) · [`00561e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561e00.md#insn-00561e4c) · [`00561e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561e00.md#insn-00561e60)
- 新版 `00584cc4`（命令位置の公開資料なし） · `00584ce4`（命令位置の公開資料なし） · `00584cf8`（命令位置の公開資料なし）

~~~diff
- 00561e2c ["INT_ADD", "register:40f0:8", ["const:561e2c:8", "const:4:8"]]
- 00561e2c ["CALL", null, ["callee:005975c8:8"]]
+ 00584cc4 ["INT_ADD", "register:40f0:8", ["const:584cc4:8", "const:4:8"]]
+ 00584cc4 ["CALL", null, ["callee:005975c8:8"]]
- 00561e2c bytes 414a0094
+ 00584cc4 bytes 414a0094
- 00561e4c ["INT_ADD", "register:40f0:8", ["const:561e4c:8", "const:4:8"]]
- 00561e4c ["CALL", null, ["callee:00c538e0:8"]]
+ 00584ce4 ["INT_ADD", "register:40f0:8", ["const:584ce4:8", "const:4:8"]]
+ 00584ce4 ["CALL", null, ["callee:00c538e0:8"]]
- 00561e4c bytes 11d41994
+ 00584ce4 bytes ff3a1b94
- 00561e60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00561e60 ["INT_ADD", "register:40f0:8", ["const:561e60:8", "const:4:8"]]
- 00561e60 ["CALLIND", null, ["register:0:8"]]
+ 00584cf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584cf8 ["INT_ADD", "register:40f0:8", ["const:584cf8:8", "const:4:8"]]
+ 00584cf8 ["CALLIND", null, ["register:0:8"]]
- 00561e60 bytes 00013fd6
+ 00584cf8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8120edbe2294c223213fd7e760ba6696"></a>

### [`00561ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ec4.md) → [`00584d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584d5c.md) FUN_00584d5c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00567e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567e94.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00561f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ec4.md#insn-00561f08) · [`00561f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ec4.md#insn-00561f20) · [`00561f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ec4.md#insn-00561f30)
- 新版 `00584da0`（命令位置の公開資料なし） · `00584db8`（命令位置の公開資料なし） · `00584dc8`（命令位置の公開資料なし）

~~~diff
- 00561f08 ["INT_ADD", "register:40f0:8", ["const:561f08:8", "const:4:8"]]
- 00561f08 ["CALL", null, ["callee:00c57a90:8"]]
+ 00584da0 ["INT_ADD", "register:40f0:8", ["const:584da0:8", "const:4:8"]]
+ 00584da0 ["CALL", null, ["callee:00c57a90:8"]]
- 00561f08 bytes 4ee41994
+ 00584da0 bytes 3c4b1b94
- 00561f20 ["INT_ADD", "register:40f0:8", ["const:561f20:8", "const:4:8"]]
- 00561f20 ["CALL", null, ["callee:00c57c00:8"]]
+ 00584db8 ["INT_ADD", "register:40f0:8", ["const:584db8:8", "const:4:8"]]
+ 00584db8 ["CALL", null, ["callee:00c57c00:8"]]
- 00561f20 bytes a4e41994
+ 00584db8 bytes 924b1b94
- 00561f30 ["INT_ADD", "register:40f0:8", ["const:561f30:8", "const:4:8"]]
- 00561f30 ["CALL", null, ["callee:0058ad2c:8"]]
+ 00584dc8 ["INT_ADD", "register:40f0:8", ["const:584dc8:8", "const:4:8"]]
+ 00584dc8 ["CALL", null, ["callee:0058ad2c:8"]]
- 00561f30 bytes d9170094
+ 00584dc8 bytes d9170094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0544afe799853a632daf85bbeff0471a"></a>

### [`00562028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562028.md) → [`00584ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) FUN_00584ec0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00524cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524cd8.md) [`005261fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005261fc.md) [`00541408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00547b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`005642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056205c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562028.md#insn-0056205c) · [`00562078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562028.md#insn-00562078) · [`005620ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562028.md#insn-005620ac)
- 新版 `00584ef4`（命令位置の公開資料なし） · `00584f10`（命令位置の公開資料なし） · `00584f44`（命令位置の公開資料なし）

~~~diff
- 0056205c ["INT_ADD", "register:40f0:8", ["const:56205c:8", "const:4:8"]]
- 0056205c ["CALL", null, ["callee:00547b70:8"]]
+ 00584ef4 ["INT_ADD", "register:40f0:8", ["const:584ef4:8", "const:4:8"]]
+ 00584ef4 ["CALL", null, ["callee:00547b70:8"]]
- 0056205c bytes 1f0bff97
+ 00584ef4 bytes 1f0bff97
- 00562078 ["INT_ADD", "register:40f0:8", ["const:562078:8", "const:4:8"]]
- 00562078 ["CALL", null, ["callee:005642a0:8"]]
+ 00584f10 ["INT_ADD", "register:40f0:8", ["const:584f10:8", "const:4:8"]]
+ 00584f10 ["CALL", null, ["callee:005642a0:8"]]
- 00562078 bytes e47cff97
+ 00584f10 bytes e47cff97
- 005620ac ["INT_ADD", "register:40f0:8", ["const:5620ac:8", "const:4:8"]]
- 005620ac ["CALL", null, ["callee:0043bae0:8"]]
+ 00584f44 ["INT_ADD", "register:40f0:8", ["const:584f44:8", "const:4:8"]]
+ 00584f44 ["CALL", null, ["callee:0043bae0:8"]]
- 005620ac bytes cddbfa97
+ 00584f44 bytes e7dafa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bd9877b20222d790eb21a6976ab9a1b"></a>

### [`0056233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056233c.md) → [`005851d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005851d4.md) FUN_005851d4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00562188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00585020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056237c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056233c.md#insn-0056237c) · [`005623c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056233c.md#insn-005623c8) · [`005623dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056233c.md#insn-005623dc)
- 新版 `00585214`（命令位置の公開資料なし） · `00585260`（命令位置の公開資料なし） · `00585274`（命令位置の公開資料なし）

~~~diff
- 0056237c ["INT_ADD", "register:40f0:8", ["const:56237c:8", "const:4:8"]]
- 0056237c ["CALL", null, ["callee:00c57a90:8"]]
+ 00585214 ["INT_ADD", "register:40f0:8", ["const:585214:8", "const:4:8"]]
+ 00585214 ["CALL", null, ["callee:00c57a90:8"]]
- 0056237c bytes 31e31994
+ 00585214 bytes 1f4a1b94
- 005623c8 ["INT_ADD", "register:40f0:8", ["const:5623c8:8", "const:4:8"]]
- 005623c8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00585260 ["INT_ADD", "register:40f0:8", ["const:585260:8", "const:4:8"]]
+ 00585260 ["CALL", null, ["callee:00c538e0:8"]]
- 005623c8 bytes b2d21994
+ 00585260 bytes a0391b94
- 005623dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005623dc ["INT_ADD", "register:40f0:8", ["const:5623dc:8", "const:4:8"]]
- 005623dc ["CALLIND", null, ["register:0:8"]]
+ 00585274 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00585274 ["INT_ADD", "register:40f0:8", ["const:585274:8", "const:4:8"]]
+ 00585274 ["CALLIND", null, ["register:0:8"]]
- 005623dc bytes 00013fd6
+ 00585274 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cef64865b6f390a53d5aa372837f19a"></a>

### [`0056244c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md) → [`005852e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md) FUN_005852e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) · 呼出先 3件 [`00564ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) · 呼出先 3件 [`00587d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d68.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md#insn-00562484) · [`00562498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md#insn-00562498) · [`005624f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md#insn-005624f0)
- 新版 `0058531c`（命令位置の公開資料なし） · `00585330`（命令位置の公開資料なし） · `00585388`（命令位置の公開資料なし）

~~~diff
- 00562484 ["INT_ADD", "register:40f0:8", ["const:562484:8", "const:4:8"]]
- 00562484 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058531c ["INT_ADD", "register:40f0:8", ["const:58531c:8", "const:4:8"]]
+ 0058531c ["CALL", null, ["callee:00c57a90:8"]]
- 00562484 bytes efe21994
+ 0058531c bytes dd491b94
- 00562498 ["INT_ADD", "register:40f0:8", ["const:562498:8", "const:4:8"]]
- 00562498 ["CALL", null, ["callee:00587d68:8"]]
+ 00585330 ["INT_ADD", "register:40f0:8", ["const:585330:8", "const:4:8"]]
+ 00585330 ["CALL", null, ["callee:00587d68:8"]]
- 00562498 bytes 8e0a0094
+ 00585330 bytes 8e0a0094
- 005624f0 ["INT_ADD", "register:40f0:8", ["const:5624f0:8", "const:4:8"]]
- 005624f0 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00585388 ["INT_ADD", "register:40f0:8", ["const:585388:8", "const:4:8"]]
+ 00585388 ["CALL", null, ["callee:00c57ae0:8"]]
- 005624f0 bytes e8e21994
+ 00585388 bytes d6491b94
~~~


<a id="compare-b3f03dc58606b891afbadc24fee7e951"></a>

### [`00562e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562e78.md) → [`00585d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md) FUN_00585d10

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) [`00563038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md) · 呼出先 3件 [`00565334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565334.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`00585ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md) · 呼出先 3件 [`005881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00562ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562e78.md#insn-00562ef4) · [`00562f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562e78.md#insn-00562f50) · [`00562f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562e78.md#insn-00562f80)
- 新版 `00585d8c`（命令位置の公開資料なし） · `00585de8`（命令位置の公開資料なし） · `00585e18`（命令位置の公開資料なし）

~~~diff
- 00562ef4 ["INT_ADD", "register:40f0:8", ["const:562ef4:8", "const:4:8"]]
- 00562ef4 ["CALL", null, ["callee:00c57c50:8"]]
+ 00585d8c ["INT_ADD", "register:40f0:8", ["const:585d8c:8", "const:4:8"]]
+ 00585d8c ["CALL", null, ["callee:00c57c50:8"]]
- 00562ef4 bytes c3e01994
+ 00585d8c bytes b1471b94
- 00562f50 ["INT_ADD", "register:40f0:8", ["const:562f50:8", "const:4:8"]]
- 00562f50 ["CALL", null, ["callee:00c57c50:8"]]
+ 00585de8 ["INT_ADD", "register:40f0:8", ["const:585de8:8", "const:4:8"]]
+ 00585de8 ["CALL", null, ["callee:00c57c50:8"]]
- 00562f50 bytes ace01994
+ 00585de8 bytes 9a471b94
- 00562f80 ["INT_ADD", "register:40f0:8", ["const:562f80:8", "const:4:8"]]
- 00562f80 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00585e18 ["INT_ADD", "register:40f0:8", ["const:585e18:8", "const:4:8"]]
+ 00585e18 ["CALL", null, ["callee:00c57ab0:8"]]
- 00562f80 bytes 38e01994
+ 00585e18 bytes 26471b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aba28e9e0fee67a09d016d1a7c7b4aee"></a>

### [`00562fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562fe8.md) → [`00585e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585e80.md) FUN_00585e80

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562fe8.md#insn-00563004) · [`00563024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562fe8.md#insn-00563024)
- 新版 `00585e9c`（命令位置の公開資料なし） · `00585ebc`（命令位置の公開資料なし）

~~~diff
- 00563004 ["INT_ADD", "register:40f0:8", ["const:563004:8", "const:4:8"]]
- 00563004 ["CALL", null, ["callee:00c538e0:8"]]
+ 00585e9c ["INT_ADD", "register:40f0:8", ["const:585e9c:8", "const:4:8"]]
+ 00585e9c ["CALL", null, ["callee:00c538e0:8"]]
- 00563004 bytes a3cf1994
+ 00585e9c bytes 91361b94
- 00563024 ["COPY", "register:0:8", ["register:4040:8"]]
- 00563024 ["INT_ADD", "register:40f0:8", ["const:563024:8", "const:4:8"]]
- 00563024 ["CALLIND", null, ["register:0:8"]]
+ 00585ebc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00585ebc ["INT_ADD", "register:40f0:8", ["const:585ebc:8", "const:4:8"]]
+ 00585ebc ["CALLIND", null, ["register:0:8"]]
- 00563024 bytes 00013fd6
+ 00585ebc bytes 00013fd6
~~~


<a id="compare-06b2ad2310f22681b3b567a1c7c5ad78"></a>

### [`00563804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563804.md) → [`0058669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058669c.md) FUN_0058669c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00563704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563704.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058659c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058659c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563804.md#insn-00563814)
- 新版 `005866ac`（命令位置の公開資料なし）

~~~diff
- 00563814 ["INT_ADD", "register:40f0:8", ["const:563814:8", "const:4:8"]]
- 00563814 ["CALL", null, ["callee:0058659c:8"]]
+ 005866ac ["INT_ADD", "register:40f0:8", ["const:5866ac:8", "const:4:8"]]
+ 005866ac ["CALL", null, ["callee:0058659c:8"]]
- 00563814 bytes bcffff97
+ 005866ac bytes bcffff97
~~~


<a id="compare-131c25b57dc2b697a011eed4c2788018"></a>

### [`00563938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563938.md) → [`005867d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005867d0.md) FUN_005867d0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563938.md#insn-00563970) · [`00563998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563938.md#insn-00563998) · [`005639b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563938.md#insn-005639b8)
- 新版 `00586808`（命令位置の公開資料なし） · `00586830`（命令位置の公開資料なし） · `00586850`（命令位置の公開資料なし）

~~~diff
- 00563970 ["COPY", "register:0:8", ["register:4048:8"]]
- 00563970 ["INT_ADD", "register:40f0:8", ["const:563970:8", "const:4:8"]]
- 00563970 ["CALLIND", null, ["register:0:8"]]
+ 00586808 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00586808 ["INT_ADD", "register:40f0:8", ["const:586808:8", "const:4:8"]]
+ 00586808 ["CALLIND", null, ["register:0:8"]]
- 00563970 bytes 20013fd6
+ 00586808 bytes 20013fd6
- 00563998 ["COPY", "register:0:8", ["register:4040:8"]]
- 00563998 ["INT_ADD", "register:40f0:8", ["const:563998:8", "const:4:8"]]
- 00563998 ["CALLIND", null, ["register:0:8"]]
+ 00586830 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586830 ["INT_ADD", "register:40f0:8", ["const:586830:8", "const:4:8"]]
+ 00586830 ["CALLIND", null, ["register:0:8"]]
- 00563998 bytes 00013fd6
+ 00586830 bytes 00013fd6
- 005639b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005639b8 ["INT_ADD", "register:40f0:8", ["const:5639b8:8", "const:4:8"]]
- 005639b8 ["CALLIND", null, ["register:0:8"]]
+ 00586850 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586850 ["INT_ADD", "register:40f0:8", ["const:586850:8", "const:4:8"]]
+ 00586850 ["CALLIND", null, ["register:0:8"]]
- 005639b8 bytes 00013fd6
+ 00586850 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6bcac943e5296c44e6335c0b66ef110"></a>

### [`00563a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563a9c.md) → [`00586934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586934.md) FUN_00586934

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563a9c.md#insn-00563ad0) · [`00563af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563a9c.md#insn-00563af8) · [`00563b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563a9c.md#insn-00563b1c)
- 新版 `00586968`（命令位置の公開資料なし） · `00586990`（命令位置の公開資料なし） · `005869b4`（命令位置の公開資料なし）

~~~diff
- 00563ad0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00563ad0 ["INT_ADD", "register:40f0:8", ["const:563ad0:8", "const:4:8"]]
- 00563ad0 ["CALLIND", null, ["register:0:8"]]
+ 00586968 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00586968 ["INT_ADD", "register:40f0:8", ["const:586968:8", "const:4:8"]]
+ 00586968 ["CALLIND", null, ["register:0:8"]]
- 00563ad0 bytes 20013fd6
+ 00586968 bytes 20013fd6
- 00563af8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00563af8 ["INT_ADD", "register:40f0:8", ["const:563af8:8", "const:4:8"]]
- 00563af8 ["CALLIND", null, ["register:0:8"]]
+ 00586990 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586990 ["INT_ADD", "register:40f0:8", ["const:586990:8", "const:4:8"]]
+ 00586990 ["CALLIND", null, ["register:0:8"]]
- 00563af8 bytes 00013fd6
+ 00586990 bytes 00013fd6
- 00563b1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00563b1c ["INT_ADD", "register:40f0:8", ["const:563b1c:8", "const:4:8"]]
- 00563b1c ["CALLIND", null, ["register:0:8"]]
+ 005869b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005869b4 ["INT_ADD", "register:40f0:8", ["const:5869b4:8", "const:4:8"]]
+ 005869b4 ["CALLIND", null, ["register:0:8"]]
- 00563b1c bytes 00013fd6
+ 005869b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37b0f73b4fdc0742269a69a760955c74"></a>

### [`00563c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c04.md) → [`00586a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md) FUN_00586a9c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005604a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604a4.md) [`00563c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c04.md) · 呼出先 2件 [`00563c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c04.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0058333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058333c.md) [`00586a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md) · 呼出先 2件 [`00586a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c04.md#insn-00563c20) · [`00563c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c04.md#insn-00563c2c) · [`00563c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c04.md#insn-00563c60)
- 新版 `00586ab8`（命令位置の公開資料なし） · `00586ac4`（命令位置の公開資料なし） · `00586af8`（命令位置の公開資料なし）

~~~diff
- 00563c20 ["INT_ADD", "register:40f0:8", ["const:563c20:8", "const:4:8"]]
- 00563c20 ["CALL", null, ["local:b0:8"]]
+ 00586ab8 ["INT_ADD", "register:40f0:8", ["const:586ab8:8", "const:4:8"]]
+ 00586ab8 ["CALL", null, ["local:b0:8"]]
- 00563c20 bytes f9ffff97
+ 00586ab8 bytes f9ffff97
- 00563c2c ["INT_ADD", "register:40f0:8", ["const:563c2c:8", "const:4:8"]]
- 00563c2c ["CALL", null, ["local:b0:8"]]
+ 00586ac4 ["INT_ADD", "register:40f0:8", ["const:586ac4:8", "const:4:8"]]
+ 00586ac4 ["CALL", null, ["local:b0:8"]]
- 00563c2c bytes f6ffff97
+ 00586ac4 bytes f6ffff97
- 00563c60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00563c60 ["INT_ADD", "register:40f0:8", ["const:563c60:8", "const:4:8"]]
- 00563c60 ["CALLIND", null, ["register:0:8"]]
+ 00586af8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586af8 ["INT_ADD", "register:40f0:8", ["const:586af8:8", "const:4:8"]]
+ 00586af8 ["CALLIND", null, ["register:0:8"]]
- 00563c60 bytes 00013fd6
+ 00586af8 bytes 00013fd6
~~~


<a id="compare-99231a852bd328998635a004484c6638"></a>

### [`00563c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c74.md) → [`00586b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md) FUN_00586b0c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005604ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604ac.md) [`00563c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c74.md) · 呼出先 2件 [`00563c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c74.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00583344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583344.md) [`00586b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md) · 呼出先 2件 [`00586b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c74.md#insn-00563c90) · [`00563c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c74.md#insn-00563c9c) · [`00563cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563c74.md#insn-00563cd0)
- 新版 `00586b28`（命令位置の公開資料なし） · `00586b34`（命令位置の公開資料なし） · `00586b68`（命令位置の公開資料なし）

~~~diff
- 00563c90 ["INT_ADD", "register:40f0:8", ["const:563c90:8", "const:4:8"]]
- 00563c90 ["CALL", null, ["local:b0:8"]]
+ 00586b28 ["INT_ADD", "register:40f0:8", ["const:586b28:8", "const:4:8"]]
+ 00586b28 ["CALL", null, ["local:b0:8"]]
- 00563c90 bytes f9ffff97
+ 00586b28 bytes f9ffff97
- 00563c9c ["INT_ADD", "register:40f0:8", ["const:563c9c:8", "const:4:8"]]
- 00563c9c ["CALL", null, ["local:b0:8"]]
+ 00586b34 ["INT_ADD", "register:40f0:8", ["const:586b34:8", "const:4:8"]]
+ 00586b34 ["CALL", null, ["local:b0:8"]]
- 00563c9c bytes f6ffff97
+ 00586b34 bytes f6ffff97
- 00563cd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00563cd0 ["INT_ADD", "register:40f0:8", ["const:563cd0:8", "const:4:8"]]
- 00563cd0 ["CALLIND", null, ["register:0:8"]]
+ 00586b68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586b68 ["INT_ADD", "register:40f0:8", ["const:586b68:8", "const:4:8"]]
+ 00586b68 ["CALLIND", null, ["register:0:8"]]
- 00563cd0 bytes 00013fd6
+ 00586b68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71adf4df0bb2a5a0364bd5a3230e63a8"></a>

### [`00563d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md) → [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md) FUN_00586bdc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056547c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00563e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563e60.md) [`005640d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005640d8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00588314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00586cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586cf8.md) [`00586f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586f70.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md#insn-00563da0) · [`00563dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md#insn-00563dc8) · [`00563df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md#insn-00563df4)
- 新版 `00586c38`（命令位置の公開資料なし） · `00586c60`（命令位置の公開資料なし） · `00586c8c`（命令位置の公開資料なし）

~~~diff
- 00563da0 ["INT_ADD", "register:40f0:8", ["const:563da0:8", "const:4:8"]]
- 00563da0 ["CALL", null, ["callee:00586cf8:8"]]
+ 00586c38 ["INT_ADD", "register:40f0:8", ["const:586c38:8", "const:4:8"]]
+ 00586c38 ["CALL", null, ["callee:00586cf8:8"]]
- 00563da0 bytes 30000094
+ 00586c38 bytes 30000094
- 00563dc8 ["INT_ADD", "register:40f0:8", ["const:563dc8:8", "const:4:8"]]
- 00563dc8 ["CALL", null, ["callee:00586f70:8"]]
+ 00586c60 ["INT_ADD", "register:40f0:8", ["const:586c60:8", "const:4:8"]]
+ 00586c60 ["CALL", null, ["callee:00586f70:8"]]
- 00563dc8 bytes c4000094
+ 00586c60 bytes c4000094
- 00563df4 ["INT_ADD", "register:40f0:8", ["const:563df4:8", "const:4:8"]]
- 00563df4 ["CALL", null, ["callee:0043bb64:8"]]
+ 00586c8c ["INT_ADD", "register:40f0:8", ["const:586c8c:8", "const:4:8"]]
+ 00586c8c ["CALL", null, ["callee:0043bb64:8"]]
- 00563df4 bytes 9cd4fa97
+ 00586c8c bytes b6d3fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-567488ea1d28786fc9d082eabfdc5c32"></a>

### [`00563e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563e60.md) → [`00586cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586cf8.md) FUN_00586cf8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00563d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md) · 呼出先 1件 [`00bdd490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd490.md)
- 新版 呼出元 1件 [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md) · 呼出先 1件 [`00c59ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00563ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563e60.md#insn-00563ec4) · [`00563efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563e60.md#insn-00563efc) · [`00563f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563e60.md#insn-00563f6c)
- 新版 `00586d5c`（命令位置の公開資料なし） · `00586d94`（命令位置の公開資料なし） · `00586e04`（命令位置の公開資料なし）

~~~diff
- 00563ec4 ["INT_ADD", "register:40f0:8", ["const:563ec4:8", "const:4:8"]]
- 00563ec4 ["CALL", null, ["callee:00c59ee0:8"]]
+ 00586d5c ["INT_ADD", "register:40f0:8", ["const:586d5c:8", "const:4:8"]]
+ 00586d5c ["CALL", null, ["callee:00c59ee0:8"]]
- 00563ec4 bytes 73e51994
+ 00586d5c bytes 614c1b94
- 00563efc ["INT_ADD", "register:40f0:8", ["const:563efc:8", "const:4:8"]]
- 00563efc ["CALL", null, ["callee:00c59ee0:8"]]
+ 00586d94 ["INT_ADD", "register:40f0:8", ["const:586d94:8", "const:4:8"]]
+ 00586d94 ["CALL", null, ["callee:00c59ee0:8"]]
- 00563efc bytes 65e51994
+ 00586d94 bytes 534c1b94
- 00563f6c ["INT_ADD", "register:40f0:8", ["const:563f6c:8", "const:4:8"]]
- 00563f6c ["CALL", null, ["callee:00c59ee0:8"]]
+ 00586e04 ["INT_ADD", "register:40f0:8", ["const:586e04:8", "const:4:8"]]
+ 00586e04 ["CALL", null, ["callee:00c59ee0:8"]]
- 00563f6c bytes 49e51994
+ 00586e04 bytes 374c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a75dce108f7585dd2debd5d8b01a4240"></a>

### [`005640d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005640d8.md) → [`00586f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586f70.md) FUN_00586f70

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00563d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005640f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005640d8.md#insn-005640f8) · [`0056412c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005640d8.md#insn-0056412c) · [`00564158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005640d8.md#insn-00564158)
- 新版 `00586f90`（命令位置の公開資料なし） · `00586fc4`（命令位置の公開資料なし） · `00586ff0`（命令位置の公開資料なし）

~~~diff
- 005640f8 ["INT_ADD", "register:40f0:8", ["const:5640f8:8", "const:4:8"]]
- 005640f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00586f90 ["INT_ADD", "register:40f0:8", ["const:586f90:8", "const:4:8"]]
+ 00586f90 ["CALL", null, ["callee:00c57a90:8"]]
- 005640f8 bytes d2db1994
+ 00586f90 bytes c0421b94
- 0056412c ["INT_ADD", "register:40f0:8", ["const:56412c:8", "const:4:8"]]
- 0056412c ["CALL", null, ["callee:0043bae0:8"]]
+ 00586fc4 ["INT_ADD", "register:40f0:8", ["const:586fc4:8", "const:4:8"]]
+ 00586fc4 ["CALL", null, ["callee:0043bae0:8"]]
- 0056412c bytes add3fa97
+ 00586fc4 bytes c7d2fa97
- 00564158 ["INT_ADD", "register:40f0:8", ["const:564158:8", "const:4:8"]]
- 00564158 ["CALL", null, ["callee:0043bae0:8"]]
+ 00586ff0 ["INT_ADD", "register:40f0:8", ["const:586ff0:8", "const:4:8"]]
+ 00586ff0 ["CALL", null, ["callee:0043bae0:8"]]
- 00564158 bytes a2d3fa97
+ 00586ff0 bytes bcd2fa97
~~~


<a id="compare-d69b53423bac05547c7c960d312a878f"></a>

### [`005641a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md) → [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) FUN_00587038

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005641a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md) [`0056503c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md) · 呼出先 2件 [`005641a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) [`00587ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md) · 呼出先 2件 [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005641bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md#insn-005641bc) · [`005641c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md#insn-005641c8) · [`005641d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md#insn-005641d8)
- 新版 `00587054`（命令位置の公開資料なし） · `00587060`（命令位置の公開資料なし） · `00587070`（命令位置の公開資料なし）

~~~diff
- 005641bc ["INT_ADD", "register:40f0:8", ["const:5641bc:8", "const:4:8"]]
- 005641bc ["CALL", null, ["local:b0:8"]]
+ 00587054 ["INT_ADD", "register:40f0:8", ["const:587054:8", "const:4:8"]]
+ 00587054 ["CALL", null, ["local:b0:8"]]
- 005641bc bytes f9ffff97
+ 00587054 bytes f9ffff97
- 005641c8 ["INT_ADD", "register:40f0:8", ["const:5641c8:8", "const:4:8"]]
- 005641c8 ["CALL", null, ["local:b0:8"]]
+ 00587060 ["INT_ADD", "register:40f0:8", ["const:587060:8", "const:4:8"]]
+ 00587060 ["CALL", null, ["local:b0:8"]]
- 005641c8 bytes f6ffff97
+ 00587060 bytes f6ffff97
- 005641d8 ["INT_ADD", "register:40f0:8", ["const:5641d8:8", "const:4:8"]]
- 005641d8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00587070 ["INT_ADD", "register:40f0:8", ["const:587070:8", "const:4:8"]]
+ 00587070 ["CALL", null, ["callee:00c57ab0:8"]]
- 005641d8 bytes a2db1994
+ 00587070 bytes 90421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af838d5078c55f7e6833abe8c4d036d6"></a>

### [`00564250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564250.md) → [`005870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005870e8.md) FUN_005870e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005642bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564250.md#insn-005642bc) · [`00564318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564250.md#insn-00564318) · [`00564344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564250.md#insn-00564344)
- 新版 `00587154`（命令位置の公開資料なし） · `005871b0`（命令位置の公開資料なし） · `005871dc`（命令位置の公開資料なし）

~~~diff
- 005642bc ["INT_ADD", "register:40f0:8", ["const:5642bc:8", "const:4:8"]]
- 005642bc ["CALL", null, ["callee:00c57a90:8"]]
+ 00587154 ["INT_ADD", "register:40f0:8", ["const:587154:8", "const:4:8"]]
+ 00587154 ["CALL", null, ["callee:00c57a90:8"]]
- 005642bc bytes 61db1994
+ 00587154 bytes 4f421b94
- 00564318 ["COPY", "register:0:8", ["register:4048:8"]]
- 00564318 ["INT_ADD", "register:40f0:8", ["const:564318:8", "const:4:8"]]
- 00564318 ["CALLIND", null, ["register:0:8"]]
+ 005871b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005871b0 ["INT_ADD", "register:40f0:8", ["const:5871b0:8", "const:4:8"]]
+ 005871b0 ["CALLIND", null, ["register:0:8"]]
- 00564318 bytes 20013fd6
+ 005871b0 bytes 20013fd6
- 00564344 ["INT_ADD", "register:40f0:8", ["const:564344:8", "const:4:8"]]
- 00564344 ["CALL", null, ["callee:0043bb64:8"]]
+ 005871dc ["INT_ADD", "register:40f0:8", ["const:5871dc:8", "const:4:8"]]
+ 005871dc ["CALL", null, ["callee:0043bb64:8"]]
- 00564344 bytes 48d3fa97
+ 005871dc bytes 62d2fa97
~~~


<a id="compare-58553d62b68cc12e7ed59947008aed73"></a>

### [`00564374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564374.md) → [`0058720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md) FUN_0058720c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0056445c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056445c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005872f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005872f4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005643e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564374.md#insn-005643e4) · [`005643fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564374.md#insn-005643fc) · [`00564428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564374.md#insn-00564428)
- 新版 `0058727c`（命令位置の公開資料なし） · `00587294`（命令位置の公開資料なし） · `005872c0`（命令位置の公開資料なし）

~~~diff
- 005643e4 ["INT_ADD", "register:40f0:8", ["const:5643e4:8", "const:4:8"]]
- 005643e4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058727c ["INT_ADD", "register:40f0:8", ["const:58727c:8", "const:4:8"]]
+ 0058727c ["CALL", null, ["callee:00c57a90:8"]]
- 005643e4 bytes 17db1994
+ 0058727c bytes 05421b94
- 005643fc ["INT_ADD", "register:40f0:8", ["const:5643fc:8", "const:4:8"]]
- 005643fc ["CALL", null, ["callee:005872f4:8"]]
+ 00587294 ["INT_ADD", "register:40f0:8", ["const:587294:8", "const:4:8"]]
+ 00587294 ["CALL", null, ["callee:005872f4:8"]]
- 005643fc bytes 18000094
+ 00587294 bytes 18000094
- 00564428 ["INT_ADD", "register:40f0:8", ["const:564428:8", "const:4:8"]]
- 00564428 ["CALL", null, ["callee:0043bb64:8"]]
+ 005872c0 ["INT_ADD", "register:40f0:8", ["const:5872c0:8", "const:4:8"]]
+ 005872c0 ["CALL", null, ["callee:0043bb64:8"]]
- 00564428 bytes 0fd3fa97
+ 005872c0 bytes 29d2fa97
~~~


<a id="compare-92e6c4aa4654193ca05efc59c4c20623"></a>

### [`0056445c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056445c.md) → [`005872f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005872f4.md) FUN_005872f4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00564374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564374.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005644ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056445c.md#insn-005644ac) · [`005644f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056445c.md#insn-005644f0) · [`00564534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056445c.md#insn-00564534)
- 新版 `00587344`（命令位置の公開資料なし） · `00587388`（命令位置の公開資料なし） · `005873cc`（命令位置の公開資料なし）

~~~diff
- 005644ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005644ac ["INT_ADD", "register:40f0:8", ["const:5644ac:8", "const:4:8"]]
- 005644ac ["CALLIND", null, ["register:0:8"]]
+ 00587344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587344 ["INT_ADD", "register:40f0:8", ["const:587344:8", "const:4:8"]]
+ 00587344 ["CALLIND", null, ["register:0:8"]]
- 005644ac bytes 00013fd6
+ 00587344 bytes 00013fd6
- 005644f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005644f0 ["INT_ADD", "register:40f0:8", ["const:5644f0:8", "const:4:8"]]
- 005644f0 ["CALLIND", null, ["register:0:8"]]
+ 00587388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587388 ["INT_ADD", "register:40f0:8", ["const:587388:8", "const:4:8"]]
+ 00587388 ["CALLIND", null, ["register:0:8"]]
- 005644f0 bytes 00013fd6
+ 00587388 bytes 00013fd6
- 00564534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00564534 ["INT_ADD", "register:40f0:8", ["const:564534:8", "const:4:8"]]
- 00564534 ["CALLIND", null, ["register:0:8"]]
+ 005873cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005873cc ["INT_ADD", "register:40f0:8", ["const:5873cc:8", "const:4:8"]]
+ 005873cc ["CALLIND", null, ["register:0:8"]]
- 00564534 bytes 00013fd6
+ 005873cc bytes 00013fd6
~~~


<a id="compare-c3e0cff82eca0e0b1f538fff1c6808be"></a>

### [`005645f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005645f0.md) → [`00587488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587488.md) FUN_00587488

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00564618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005645f0.md#insn-00564618) · [`0056462c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005645f0.md#insn-0056462c) · [`00564634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005645f0.md#insn-00564634)
- 新版 `005874b0`（命令位置の公開資料なし） · `005874c4`（命令位置の公開資料なし） · `005874cc`（命令位置の公開資料なし）

~~~diff
- 00564618 ["INT_ADD", "register:40f0:8", ["const:564618:8", "const:4:8"]]
- 00564618 ["CALL", null, ["callee:00c538e0:8"]]
+ 005874b0 ["INT_ADD", "register:40f0:8", ["const:5874b0:8", "const:4:8"]]
+ 005874b0 ["CALL", null, ["callee:00c538e0:8"]]
- 00564618 bytes 1eca1994
+ 005874b0 bytes 0c311b94
- 0056462c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056462c ["INT_ADD", "register:40f0:8", ["const:56462c:8", "const:4:8"]]
- 0056462c ["CALLIND", null, ["register:0:8"]]
+ 005874c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005874c4 ["INT_ADD", "register:40f0:8", ["const:5874c4:8", "const:4:8"]]
+ 005874c4 ["CALLIND", null, ["register:0:8"]]
- 0056462c bytes 00013fd6
+ 005874c4 bytes 00013fd6
- 00564634 ["INT_ADD", "register:40f0:8", ["const:564634:8", "const:4:8"]]
- 00564634 ["CALL", null, ["callee:00c57a80:8"]]
+ 005874cc ["INT_ADD", "register:40f0:8", ["const:5874cc:8", "const:4:8"]]
+ 005874cc ["CALL", null, ["callee:00c57a80:8"]]
- 00564634 bytes 7fda1994
+ 005874cc bytes 6d411b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27222f6facf86ad0a69ee206b220b8ab"></a>

### [`00564680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564680.md) → [`00587518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587518.md) FUN_00587518

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005646a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564680.md#insn-005646a0) · [`005646b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564680.md#insn-005646b8) · [`005646d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564680.md#insn-005646d8)
- 新版 `00587538`（命令位置の公開資料なし） · `00587550`（命令位置の公開資料なし） · `00587570`（命令位置の公開資料なし）

~~~diff
- 005646a0 ["INT_ADD", "register:40f0:8", ["const:5646a0:8", "const:4:8"]]
- 005646a0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00587538 ["INT_ADD", "register:40f0:8", ["const:587538:8", "const:4:8"]]
+ 00587538 ["CALL", null, ["callee:00c538e0:8"]]
- 005646a0 bytes fcc91994
+ 00587538 bytes ea301b94
- 005646b8 ["INT_ADD", "register:40f0:8", ["const:5646b8:8", "const:4:8"]]
- 005646b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00587550 ["INT_ADD", "register:40f0:8", ["const:587550:8", "const:4:8"]]
+ 00587550 ["CALL", null, ["callee:00c538e0:8"]]
- 005646b8 bytes f6c91994
+ 00587550 bytes e4301b94
- 005646d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005646d8 ["INT_ADD", "register:40f0:8", ["const:5646d8:8", "const:4:8"]]
- 005646d8 ["CALLIND", null, ["register:0:8"]]
+ 00587570 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587570 ["INT_ADD", "register:40f0:8", ["const:587570:8", "const:4:8"]]
+ 00587570 ["CALLIND", null, ["register:0:8"]]
- 005646d8 bytes 00013fd6
+ 00587570 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba544aa3795fa56fd638c280a806437a"></a>

### [`00564974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564974.md) → [`0058780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058780c.md) FUN_0058780c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00564990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564974.md#insn-00564990) · [`005649b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564974.md#insn-005649b0)
- 新版 `00587828`（命令位置の公開資料なし） · `00587848`（命令位置の公開資料なし）

~~~diff
- 00564990 ["INT_ADD", "register:40f0:8", ["const:564990:8", "const:4:8"]]
- 00564990 ["CALL", null, ["callee:00c538e0:8"]]
+ 00587828 ["INT_ADD", "register:40f0:8", ["const:587828:8", "const:4:8"]]
+ 00587828 ["CALL", null, ["callee:00c538e0:8"]]
- 00564990 bytes 40c91994
+ 00587828 bytes 2e301b94
- 005649b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005649b0 ["INT_ADD", "register:40f0:8", ["const:5649b0:8", "const:4:8"]]
- 005649b0 ["CALLIND", null, ["register:0:8"]]
+ 00587848 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587848 ["INT_ADD", "register:40f0:8", ["const:587848:8", "const:4:8"]]
+ 00587848 ["CALLIND", null, ["register:0:8"]]
- 005649b0 bytes 00013fd6
+ 00587848 bytes 00013fd6
~~~


<a id="compare-1a367ac87377f0ca9aa87296ea21a6cc"></a>

### [`005649c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005649c4.md) → [`0058785c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058785c.md) FUN_0058785c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005649e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005649c4.md#insn-005649e4) · [`005649f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005649c4.md#insn-005649f8) · [`00564a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005649c4.md#insn-00564a00)
- 新版 `0058787c`（命令位置の公開資料なし） · `00587890`（命令位置の公開資料なし） · `00587898`（命令位置の公開資料なし）

~~~diff
- 005649e4 ["INT_ADD", "register:40f0:8", ["const:5649e4:8", "const:4:8"]]
- 005649e4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0058787c ["INT_ADD", "register:40f0:8", ["const:58787c:8", "const:4:8"]]
+ 0058787c ["CALL", null, ["callee:00c538e0:8"]]
- 005649e4 bytes 2bc91994
+ 0058787c bytes 19301b94
- 005649f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005649f8 ["INT_ADD", "register:40f0:8", ["const:5649f8:8", "const:4:8"]]
- 005649f8 ["CALLIND", null, ["register:0:8"]]
+ 00587890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587890 ["INT_ADD", "register:40f0:8", ["const:587890:8", "const:4:8"]]
+ 00587890 ["CALLIND", null, ["register:0:8"]]
- 005649f8 bytes 00013fd6
+ 00587890 bytes 00013fd6
- 00564a00 ["INT_ADD", "register:40f0:8", ["const:564a00:8", "const:4:8"]]
- 00564a00 ["CALL", null, ["callee:00c57a80:8"]]
+ 00587898 ["INT_ADD", "register:40f0:8", ["const:587898:8", "const:4:8"]]
+ 00587898 ["CALL", null, ["callee:00c57a80:8"]]
- 00564a00 bytes 8cd91994
+ 00587898 bytes 7a401b94
~~~


<a id="compare-4a99f18d5cbb90044b915fa76f8f0f61"></a>

### [`00564a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564a14.md) → [`005878ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005878ac.md) FUN_005878ac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00564b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564b70.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00587a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587a08.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00564a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564a14.md#insn-00564a54) · [`00564a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564a14.md#insn-00564a6c) · [`00564a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564a14.md#insn-00564a80)
- 新版 `005878ec`（命令位置の公開資料なし） · `00587904`（命令位置の公開資料なし） · `00587918`（命令位置の公開資料なし）

~~~diff
- 00564a54 ["INT_ADD", "register:40f0:8", ["const:564a54:8", "const:4:8"]]
- 00564a54 ["CALL", null, ["callee:00c538b0:8"]]
+ 005878ec ["INT_ADD", "register:40f0:8", ["const:5878ec:8", "const:4:8"]]
+ 005878ec ["CALL", null, ["callee:00c538b0:8"]]
- 00564a54 bytes 03c91994
+ 005878ec bytes f12f1b94
- 00564a6c ["INT_ADD", "register:40f0:8", ["const:564a6c:8", "const:4:8"]]
- 00564a6c ["CALL", null, ["callee:00c538b0:8"]]
+ 00587904 ["INT_ADD", "register:40f0:8", ["const:587904:8", "const:4:8"]]
+ 00587904 ["CALL", null, ["callee:00c538b0:8"]]
- 00564a6c bytes fdc81994
+ 00587904 bytes eb2f1b94
- 00564a80 ["INT_ADD", "register:40f0:8", ["const:564a80:8", "const:4:8"]]
- 00564a80 ["CALL", null, ["callee:00587a08:8"]]
+ 00587918 ["INT_ADD", "register:40f0:8", ["const:587918:8", "const:4:8"]]
+ 00587918 ["CALL", null, ["callee:00587a08:8"]]
- 00564a80 bytes 3c000094
+ 00587918 bytes 3c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a2d06bf5a3e912d5923ed3d400ea894"></a>

### [`00564d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md) → [`00587c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md) FUN_00587c14

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00562188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00564ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ebc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00585020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00587d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d54.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00564de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md#insn-00564de8) · [`00564e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md#insn-00564e58) · [`00564e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md#insn-00564e6c)
- 新版 `00587c80`（命令位置の公開資料なし） · `00587cf0`（命令位置の公開資料なし） · `00587d04`（命令位置の公開資料なし）

~~~diff
- 00564de8 ["INT_ADD", "register:40f0:8", ["const:564de8:8", "const:4:8"]]
- 00564de8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00587c80 ["INT_ADD", "register:40f0:8", ["const:587c80:8", "const:4:8"]]
+ 00587c80 ["CALL", null, ["callee:00c57a90:8"]]
- 00564de8 bytes 96d81994
+ 00587c80 bytes 843f1b94
- 00564e58 ["INT_ADD", "register:40f0:8", ["const:564e58:8", "const:4:8"]]
- 00564e58 ["CALL", null, ["callee:00c538e0:8"]]
+ 00587cf0 ["INT_ADD", "register:40f0:8", ["const:587cf0:8", "const:4:8"]]
+ 00587cf0 ["CALL", null, ["callee:00c538e0:8"]]
- 00564e58 bytes 0ec81994
+ 00587cf0 bytes fc2e1b94
- 00564e6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00564e6c ["INT_ADD", "register:40f0:8", ["const:564e6c:8", "const:4:8"]]
- 00564e6c ["CALLIND", null, ["register:0:8"]]
+ 00587d04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587d04 ["INT_ADD", "register:40f0:8", ["const:587d04:8", "const:4:8"]]
+ 00587d04 ["CALLIND", null, ["register:0:8"]]
- 00564e6c bytes 00013fd6
+ 00587d04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5684664c6333c8107dab93f7303dedaa"></a>

### [`0056521c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056521c.md) → [`005880b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005880b4.md) FUN_005880b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005624f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056521c.md#insn-00565284) · [`005652b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056521c.md#insn-005652b4) · [`005652e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056521c.md#insn-005652e8)
- 新版 `0058811c`（命令位置の公開資料なし） · `0058814c`（命令位置の公開資料なし） · `00588180`（命令位置の公開資料なし）

~~~diff
- 00565284 ["INT_ADD", "register:40f0:8", ["const:565284:8", "const:4:8"]]
- 00565284 ["CALL", null, ["callee:004945d0:8"]]
+ 0058811c ["INT_ADD", "register:40f0:8", ["const:58811c:8", "const:4:8"]]
+ 0058811c ["CALL", null, ["callee:004945d0:8"]]
- 00565284 bytes 2d31fc97
+ 0058811c bytes 2d31fc97
- 005652b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005652b4 ["INT_ADD", "register:40f0:8", ["const:5652b4:8", "const:4:8"]]
- 005652b4 ["CALLIND", null, ["register:0:8"]]
+ 0058814c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058814c ["INT_ADD", "register:40f0:8", ["const:58814c:8", "const:4:8"]]
+ 0058814c ["CALLIND", null, ["register:0:8"]]
- 005652b4 bytes 00013fd6
+ 0058814c bytes 00013fd6
- 005652e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005652e8 ["INT_ADD", "register:40f0:8", ["const:5652e8:8", "const:4:8"]]
- 005652e8 ["CALLIND", null, ["register:0:8"]]
+ 00588180 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588180 ["INT_ADD", "register:40f0:8", ["const:588180:8", "const:4:8"]]
+ 00588180 ["CALLIND", null, ["register:0:8"]]
- 005652e8 bytes 00013fd6
+ 00588180 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9ebdd03f11f6a7710a32372b36596c8"></a>

### [`00565334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565334.md) → [`005881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md) FUN_005881cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00562e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562e78.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0052c2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c2bc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00585d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565334.md#insn-00565374) · [`00565394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565334.md#insn-00565394) · [`005653c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565334.md#insn-005653c8)
- 新版 `0058820c`（命令位置の公開資料なし） · `0058822c`（命令位置の公開資料なし） · `00588260`（命令位置の公開資料なし）

~~~diff
- 00565374 ["INT_ADD", "register:40f0:8", ["const:565374:8", "const:4:8"]]
- 00565374 ["CALL", null, ["callee:0054f154:8"]]
+ 0058820c ["INT_ADD", "register:40f0:8", ["const:58820c:8", "const:4:8"]]
+ 0058820c ["CALL", null, ["callee:0054f154:8"]]
- 00565374 bytes d21bff97
+ 0058820c bytes d21bff97
- 00565394 ["INT_ADD", "register:40f0:8", ["const:565394:8", "const:4:8"]]
- 00565394 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058822c ["INT_ADD", "register:40f0:8", ["const:58822c:8", "const:4:8"]]
+ 0058822c ["CALL", null, ["callee:00c57a90:8"]]
- 00565394 bytes 2bd71994
+ 0058822c bytes 193e1b94
- 005653c8 ["INT_ADD", "register:40f0:8", ["const:5653c8:8", "const:4:8"]]
- 005653c8 ["CALL", null, ["callee:0043bae0:8"]]
+ 00588260 ["INT_ADD", "register:40f0:8", ["const:588260:8", "const:4:8"]]
+ 00588260 ["CALL", null, ["callee:0043bae0:8"]]
- 005653c8 bytes 06cffa97
+ 00588260 bytes 20cefa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28aaa2ccb3cdbcd8934afefb520b3af"></a>

### [`005656d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005656d0.md) → [`00588568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588568.md) FUN_00588568

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005656ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005656d0.md#insn-005656ec) · [`0056570c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005656d0.md#insn-0056570c)
- 新版 `00588584`（命令位置の公開資料なし） · `005885a4`（命令位置の公開資料なし）

~~~diff
- 005656ec ["INT_ADD", "register:40f0:8", ["const:5656ec:8", "const:4:8"]]
- 005656ec ["CALL", null, ["callee:00c538e0:8"]]
+ 00588584 ["INT_ADD", "register:40f0:8", ["const:588584:8", "const:4:8"]]
+ 00588584 ["CALL", null, ["callee:00c538e0:8"]]
- 005656ec bytes e9c51994
+ 00588584 bytes d72c1b94
- 0056570c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056570c ["INT_ADD", "register:40f0:8", ["const:56570c:8", "const:4:8"]]
- 0056570c ["CALLIND", null, ["register:0:8"]]
+ 005885a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005885a4 ["INT_ADD", "register:40f0:8", ["const:5885a4:8", "const:4:8"]]
+ 005885a4 ["CALLIND", null, ["register:0:8"]]
- 0056570c bytes 00013fd6
+ 005885a4 bytes 00013fd6
~~~


<a id="compare-ab959189095f4b93f665715cd2df452f"></a>

### [`00565a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565a1c.md) → [`005888b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005888b4.md) FUN_005888b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565a1c.md#insn-00565a34)
- 新版 `005888cc`（命令位置の公開資料なし）

~~~diff
- 00565a34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00565a34 ["INT_ADD", "register:40f0:8", ["const:565a34:8", "const:4:8"]]
- 00565a34 ["CALLIND", null, ["register:0:8"]]
+ 005888cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005888cc ["INT_ADD", "register:40f0:8", ["const:5888cc:8", "const:4:8"]]
+ 005888cc ["CALLIND", null, ["register:0:8"]]
- 00565a34 bytes 00013fd6
+ 005888cc bytes 00013fd6
~~~


<a id="compare-7accd799a43a02bfec369dfe9cf117dd"></a>

### [`00565a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565a70.md) → [`00588908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588908.md) FUN_00588908

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565a70.md#insn-00565a9c) · [`00565acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565a70.md#insn-00565acc)
- 新版 `00588934`（命令位置の公開資料なし） · `00588964`（命令位置の公開資料なし）

~~~diff
- 00565a9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00565a9c ["INT_ADD", "register:40f0:8", ["const:565a9c:8", "const:4:8"]]
- 00565a9c ["CALLIND", null, ["register:0:8"]]
+ 00588934 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588934 ["INT_ADD", "register:40f0:8", ["const:588934:8", "const:4:8"]]
+ 00588934 ["CALLIND", null, ["register:0:8"]]
- 00565a9c bytes 00013fd6
+ 00588934 bytes 00013fd6
- 00565acc ["COPY", "register:0:8", ["register:4040:8"]]
- 00565acc ["INT_ADD", "register:40f0:8", ["const:565acc:8", "const:4:8"]]
- 00565acc ["CALLIND", null, ["register:0:8"]]
+ 00588964 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588964 ["INT_ADD", "register:40f0:8", ["const:588964:8", "const:4:8"]]
+ 00588964 ["CALLIND", null, ["register:0:8"]]
- 00565acc bytes 00013fd6
+ 00588964 bytes 00013fd6
~~~


<a id="compare-3934a519822502943dd8b5430f593ee7"></a>

### [`00565b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565b20.md) → [`005889b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005889b8.md) FUN_005889b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565b20.md#insn-00565b38)
- 新版 `005889d0`（命令位置の公開資料なし）

~~~diff
- 00565b38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00565b38 ["INT_ADD", "register:40f0:8", ["const:565b38:8", "const:4:8"]]
- 00565b38 ["CALLIND", null, ["register:0:8"]]
+ 005889d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005889d0 ["INT_ADD", "register:40f0:8", ["const:5889d0:8", "const:4:8"]]
+ 005889d0 ["CALLIND", null, ["register:0:8"]]
- 00565b38 bytes 00013fd6
+ 005889d0 bytes 00013fd6
~~~


<a id="compare-3f36dca27e43a6da149baba1e21c3fd8"></a>

### [`00565b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565b70.md) → [`00588a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588a08.md) FUN_00588a08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565b70.md#insn-00565b9c) · [`00565bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565b70.md#insn-00565bcc)
- 新版 `00588a34`（命令位置の公開資料なし） · `00588a64`（命令位置の公開資料なし）

~~~diff
- 00565b9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00565b9c ["INT_ADD", "register:40f0:8", ["const:565b9c:8", "const:4:8"]]
- 00565b9c ["CALLIND", null, ["register:0:8"]]
+ 00588a34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588a34 ["INT_ADD", "register:40f0:8", ["const:588a34:8", "const:4:8"]]
+ 00588a34 ["CALLIND", null, ["register:0:8"]]
- 00565b9c bytes 00013fd6
+ 00588a34 bytes 00013fd6
- 00565bcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00565bcc ["INT_ADD", "register:40f0:8", ["const:565bcc:8", "const:4:8"]]
- 00565bcc ["CALLIND", null, ["register:0:8"]]
+ 00588a64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588a64 ["INT_ADD", "register:40f0:8", ["const:588a64:8", "const:4:8"]]
+ 00588a64 ["CALLIND", null, ["register:0:8"]]
- 00565bcc bytes 00013fd6
+ 00588a64 bytes 00013fd6
~~~


<a id="compare-51132708f3a2989da941f68363efba0d"></a>

### [`00565c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565c20.md) → [`00588ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588ab8.md) FUN_00588ab8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574728.md) · 呼出先 5件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00565ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ce8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005975c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c0.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00588b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565c20.md#insn-00565c48) · [`00565c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565c20.md#insn-00565c5c) · [`00565c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565c20.md#insn-00565c80)
- 新版 `00588ae0`（命令位置の公開資料なし） · `00588af4`（命令位置の公開資料なし） · `00588b18`（命令位置の公開資料なし）

~~~diff
- 00565c48 ["INT_ADD", "register:40f0:8", ["const:565c48:8", "const:4:8"]]
- 00565c48 ["CALL", null, ["callee:00550b64:8"]]
+ 00588ae0 ["INT_ADD", "register:40f0:8", ["const:588ae0:8", "const:4:8"]]
+ 00588ae0 ["CALL", null, ["callee:00550b64:8"]]
- 00565c48 bytes 2120ff97
+ 00588ae0 bytes 2120ff97
- 00565c5c ["INT_ADD", "register:40f0:8", ["const:565c5c:8", "const:4:8"]]
- 00565c5c ["CALL", null, ["callee:00588b80:8"]]
+ 00588af4 ["INT_ADD", "register:40f0:8", ["const:588af4:8", "const:4:8"]]
+ 00588af4 ["CALL", null, ["callee:00588b80:8"]]
- 00565c5c bytes 23000094
+ 00588af4 bytes 23000094
- 00565c80 ["INT_ADD", "register:40f0:8", ["const:565c80:8", "const:4:8"]]
- 00565c80 ["CALL", null, ["callee:00c538e0:8"]]
+ 00588b18 ["INT_ADD", "register:40f0:8", ["const:588b18:8", "const:4:8"]]
+ 00588b18 ["CALL", null, ["callee:00c538e0:8"]]
- 00565c80 bytes 84c41994
+ 00588b18 bytes 722b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-337f2596f156a4eaca0ec1da759815a2"></a>

### [`00565e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md) → [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md) FUN_00588cac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00565720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md) [`00568258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568258.md) [`005682d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005682d8.md) [`00572150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572150.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 4件 [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) [`0058b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md) [`0058b170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b170.md) [`00594fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00565ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md#insn-00565ea8) · [`00565ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md#insn-00565ed4) · [`00565ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md#insn-00565ee8)
- 新版 `00588d40`（命令位置の公開資料なし） · `00588d6c`（命令位置の公開資料なし） · `00588d80`（命令位置の公開資料なし）

~~~diff
- 00565ea8 ["INT_ADD", "register:40f0:8", ["const:565ea8:8", "const:4:8"]]
- 00565ea8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00588d40 ["INT_ADD", "register:40f0:8", ["const:588d40:8", "const:4:8"]]
+ 00588d40 ["CALL", null, ["callee:00c57a90:8"]]
- 00565ea8 bytes 66d41994
+ 00588d40 bytes 543b1b94
- 00565ed4 ["INT_ADD", "register:40f0:8", ["const:565ed4:8", "const:4:8"]]
- 00565ed4 ["CALL", null, ["callee:00c57c00:8"]]
+ 00588d6c ["INT_ADD", "register:40f0:8", ["const:588d6c:8", "const:4:8"]]
+ 00588d6c ["CALL", null, ["callee:00c57c00:8"]]
- 00565ed4 bytes b7d41994
+ 00588d6c bytes a53b1b94
- 00565ee8 ["INT_ADD", "register:40f0:8", ["const:565ee8:8", "const:4:8"]]
- 00565ee8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00588d80 ["INT_ADD", "register:40f0:8", ["const:588d80:8", "const:4:8"]]
+ 00588d80 ["CALL", null, ["callee:00c57ab0:8"]]
- 00565ee8 bytes 5ed41994
+ 00588d80 bytes 4c3b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2c4ae4a3771ba8da3db28e9ba358350"></a>

### [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) → [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) FUN_005896b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 32件 [`005662b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005662b8.md) [`00ae1534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md) [`00ae1b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1b60.md) [`00ae1c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1c64.md) [`00ae2150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 33件 [`00589150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md) [`00b40f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40f0c.md) [`00b41538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41538.md) [`00b4163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b4163c.md) [`00b41b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41b28.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00566890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md#insn-00566890) · [`005668b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md#insn-005668b4)
- 新版 `00589728`（命令位置の公開資料なし） · `0058974c`（命令位置の公開資料なし）

~~~diff
- 00566890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00566890 ["INT_ADD", "register:40f0:8", ["const:566890:8", "const:4:8"]]
- 00566890 ["CALLIND", null, ["register:0:8"]]
+ 00589728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589728 ["INT_ADD", "register:40f0:8", ["const:589728:8", "const:4:8"]]
+ 00589728 ["CALLIND", null, ["register:0:8"]]
- 00566890 bytes 00013fd6
+ 00589728 bytes 00013fd6
- 005668b4 ["INT_ADD", "register:40f0:8", ["const:5668b4:8", "const:4:8"]]
- 005668b4 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0058974c ["INT_ADD", "register:40f0:8", ["const:58974c:8", "const:4:8"]]
+ 0058974c ["CALL", null, ["callee:00c57ae0:8"]]
- 005668b4 bytes f7d11994
+ 0058974c bytes e5381b94
~~~


<a id="compare-140432e030dedf8712382470c68da0dd"></a>

### [`00566988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566988.md) → [`00589820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589820.md) FUN_00589820

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056a298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a298.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md)
- 新版 呼出元 1件 [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005669a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566988.md#insn-005669a0)
- 新版 `00589838`（命令位置の公開資料なし）

~~~diff
- 005669a0 ["INT_ADD", "register:40f0:8", ["const:5669a0:8", "const:4:8"]]
- 005669a0 ["CALL", null, ["callee:00588e8c:8"]]
+ 00589838 ["INT_ADD", "register:40f0:8", ["const:589838:8", "const:4:8"]]
+ 00589838 ["CALL", null, ["callee:00588e8c:8"]]
- 005669a0 bytes 95fdff97
+ 00589838 bytes 95fdff97
~~~


<a id="compare-0b5970b80186140262e6a5ee78da84dd"></a>

### [`005669b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005669b4.md) → [`0058984c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058984c.md) FUN_0058984c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005669d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005669b4.md#insn-005669d0)
- 新版 `00589868`（命令位置の公開資料なし）

~~~diff
- 005669d0 ["INT_ADD", "register:40f0:8", ["const:5669d0:8", "const:4:8"]]
- 005669d0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00589868 ["INT_ADD", "register:40f0:8", ["const:589868:8", "const:4:8"]]
+ 00589868 ["CALL", null, ["callee:00c57ab0:8"]]
- 005669d0 bytes a4d11994
+ 00589868 bytes 92381b94
~~~


<a id="compare-ba9a65873265aac569e9e8f7f926c1eb"></a>

### [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) → [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) FUN_00589914

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 33件 [`004188e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004188e8.md) [`00418a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418a7c.md) [`00418b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b94.md) [`004747cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md) [`00550c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550c88.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 33件 [`0043b3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b3e8.md) [`0043b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b57c.md) [`0043b694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b694.md) [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00573b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573b20.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00566ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md#insn-00566ac0) · [`00566adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md#insn-00566adc) · [`00566ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md#insn-00566ae4)
- 新版 `00589958`（命令位置の公開資料なし） · `00589974`（命令位置の公開資料なし） · `0058997c`（命令位置の公開資料なし）

~~~diff
- 00566ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00566ac0 ["INT_ADD", "register:40f0:8", ["const:566ac0:8", "const:4:8"]]
- 00566ac0 ["CALLIND", null, ["register:0:8"]]
+ 00589958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589958 ["INT_ADD", "register:40f0:8", ["const:589958:8", "const:4:8"]]
+ 00589958 ["CALLIND", null, ["register:0:8"]]
- 00566ac0 bytes 00013fd6
+ 00589958 bytes 00013fd6
- 00566adc ["COPY", "register:0:8", ["register:4040:8"]]
- 00566adc ["INT_ADD", "register:40f0:8", ["const:566adc:8", "const:4:8"]]
- 00566adc ["CALLIND", null, ["register:0:8"]]
+ 00589974 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589974 ["INT_ADD", "register:40f0:8", ["const:589974:8", "const:4:8"]]
+ 00589974 ["CALLIND", null, ["register:0:8"]]
- 00566adc bytes 00013fd6
+ 00589974 bytes 00013fd6
- 00566ae4 ["INT_ADD", "register:40f0:8", ["const:566ae4:8", "const:4:8"]]
- 00566ae4 ["CALL", null, ["callee:00c57be0:8"]]
+ 0058997c ["INT_ADD", "register:40f0:8", ["const:58997c:8", "const:4:8"]]
+ 0058997c ["CALL", null, ["callee:00c57be0:8"]]
- 00566ae4 bytes abd11994
+ 0058997c bytes 99381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-072e2b18add92562751f2882b61b0dd8"></a>

### [`00567170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567170.md) → [`0058a008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a008.md) FUN_0058a008

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00567030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00589ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ec8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567170.md#insn-00567180)
- 新版 `0058a018`（命令位置の公開資料なし）

~~~diff
- 00567180 ["INT_ADD", "register:40f0:8", ["const:567180:8", "const:4:8"]]
- 00567180 ["CALL", null, ["callee:00589ec8:8"]]
+ 0058a018 ["INT_ADD", "register:40f0:8", ["const:58a018:8", "const:4:8"]]
+ 0058a018 ["CALL", null, ["callee:00589ec8:8"]]
- 00567180 bytes acffff97
+ 0058a018 bytes acffff97
~~~


<a id="compare-ce0ead308f366370e521d360c4d91ecb"></a>

### [`005677cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005677cc.md) → [`0058a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a664.md) FUN_0058a664

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0054f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md) [`00555fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555fe4.md) [`0055828c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/0055828c.md) [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005677cc.md#insn-00567804) · [`00567824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005677cc.md#insn-00567824)
- 新版 `0058a69c`（命令位置の公開資料なし） · `0058a6bc`（命令位置の公開資料なし）

~~~diff
- 00567804 ["COPY", "register:0:8", ["register:4040:8"]]
- 00567804 ["INT_ADD", "register:40f0:8", ["const:567804:8", "const:4:8"]]
- 00567804 ["CALLIND", null, ["register:0:8"]]
+ 0058a69c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a69c ["INT_ADD", "register:40f0:8", ["const:58a69c:8", "const:4:8"]]
+ 0058a69c ["CALLIND", null, ["register:0:8"]]
- 00567804 bytes 00013fd6
+ 0058a69c bytes 00013fd6
- 00567824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00567824 ["INT_ADD", "register:40f0:8", ["const:567824:8", "const:4:8"]]
- 00567824 ["CALLIND", null, ["register:0:8"]]
+ 0058a6bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a6bc ["INT_ADD", "register:40f0:8", ["const:58a6bc:8", "const:4:8"]]
+ 0058a6bc ["CALLIND", null, ["register:0:8"]]
- 00567824 bytes 00013fd6
+ 0058a6bc bytes 00013fd6
~~~


<a id="compare-734f095ca2d5f0cedc936faaeb597d77"></a>

### [`00567848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567848.md) → [`0058a6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md) FUN_0058a6e0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) [`00550fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550fa8.md) [`00551208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551208.md) · 呼出先 1件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md)
- 新版 呼出元 3件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) · 呼出先 1件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567848.md#insn-00567870) · [`00567884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567848.md#insn-00567884) · [`0056789c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567848.md#insn-0056789c)
- 新版 `0058a708`（命令位置の公開資料なし） · `0058a71c`（命令位置の公開資料なし） · `0058a734`（命令位置の公開資料なし）

~~~diff
- 00567870 ["COPY", "register:0:8", ["register:4048:8"]]
- 00567870 ["INT_ADD", "register:40f0:8", ["const:567870:8", "const:4:8"]]
- 00567870 ["CALLIND", null, ["register:0:8"]]
+ 0058a708 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058a708 ["INT_ADD", "register:40f0:8", ["const:58a708:8", "const:4:8"]]
+ 0058a708 ["CALLIND", null, ["register:0:8"]]
- 00567870 bytes 20013fd6
+ 0058a708 bytes 20013fd6
- 00567884 ["COPY", "register:0:8", ["register:4040:8"]]
- 00567884 ["INT_ADD", "register:40f0:8", ["const:567884:8", "const:4:8"]]
- 00567884 ["CALLIND", null, ["register:0:8"]]
+ 0058a71c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a71c ["INT_ADD", "register:40f0:8", ["const:58a71c:8", "const:4:8"]]
+ 0058a71c ["CALLIND", null, ["register:0:8"]]
- 00567884 bytes 00013fd6
+ 0058a71c bytes 00013fd6
- 0056789c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056789c ["INT_ADD", "register:40f0:8", ["const:56789c:8", "const:4:8"]]
- 0056789c ["CALLIND", null, ["register:0:8"]]
+ 0058a734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a734 ["INT_ADD", "register:40f0:8", ["const:58a734:8", "const:4:8"]]
+ 0058a734 ["CALLIND", null, ["register:0:8"]]
- 0056789c bytes 00013fd6
+ 0058a734 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f54f1bd70628b165c31d5195c507de92"></a>

### [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) → [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) FUN_0058a90c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`0056691c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056691c.md) [`005673dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005673dc.md) [`0056794c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056794c.md) [`00567998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567998.md) · 呼出先 2件 [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 8件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`005897b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md) [`0058a274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md) [`0058a7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7e4.md) [`0058a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a830.md) · 呼出先 2件 [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md#insn-00567a90) · [`00567a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md#insn-00567a9c) · [`00567aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md#insn-00567aac)
- 新版 `0058a928`（命令位置の公開資料なし） · `0058a934`（命令位置の公開資料なし） · `0058a944`（命令位置の公開資料なし）

~~~diff
- 00567a90 ["INT_ADD", "register:40f0:8", ["const:567a90:8", "const:4:8"]]
- 00567a90 ["CALL", null, ["local:b0:8"]]
+ 0058a928 ["INT_ADD", "register:40f0:8", ["const:58a928:8", "const:4:8"]]
+ 0058a928 ["CALL", null, ["local:b0:8"]]
- 00567a90 bytes f9ffff97
+ 0058a928 bytes f9ffff97
- 00567a9c ["INT_ADD", "register:40f0:8", ["const:567a9c:8", "const:4:8"]]
- 00567a9c ["CALL", null, ["local:b0:8"]]
+ 0058a934 ["INT_ADD", "register:40f0:8", ["const:58a934:8", "const:4:8"]]
+ 0058a934 ["CALL", null, ["local:b0:8"]]
- 00567a9c bytes f6ffff97
+ 0058a934 bytes f6ffff97
- 00567aac ["INT_ADD", "register:40f0:8", ["const:567aac:8", "const:4:8"]]
- 00567aac ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058a944 ["INT_ADD", "register:40f0:8", ["const:58a944:8", "const:4:8"]]
+ 0058a944 ["CALL", null, ["callee:00c57ab0:8"]]
- 00567aac bytes 6dcd1994
+ 0058a944 bytes 5b341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe14f1629dbe0b6f6ce1da60835dc3a2"></a>

### [`00567ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ad4.md) → [`0058a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md) FUN_0058a96c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00567bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567bfc.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`0058aa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ad4.md#insn-00567b38) · [`00567b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ad4.md#insn-00567b68) · [`00567bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ad4.md#insn-00567bcc)
- 新版 `0058a9d0`（命令位置の公開資料なし） · `0058aa00`（命令位置の公開資料なし） · `0058aa64`（命令位置の公開資料なし）

~~~diff
- 00567b38 ["INT_ADD", "register:40f0:8", ["const:567b38:8", "const:4:8"]]
- 00567b38 ["CALL", null, ["callee:00c57c50:8"]]
+ 0058a9d0 ["INT_ADD", "register:40f0:8", ["const:58a9d0:8", "const:4:8"]]
+ 0058a9d0 ["CALL", null, ["callee:00c57c50:8"]]
- 00567b38 bytes b2cd1994
+ 0058a9d0 bytes a0341b94
- 00567b68 ["INT_ADD", "register:40f0:8", ["const:567b68:8", "const:4:8"]]
- 00567b68 ["CALL", null, ["callee:00c57c50:8"]]
+ 0058aa00 ["INT_ADD", "register:40f0:8", ["const:58aa00:8", "const:4:8"]]
+ 0058aa00 ["CALL", null, ["callee:00c57c50:8"]]
- 00567b68 bytes a6cd1994
+ 0058aa00 bytes 94341b94
- 00567bcc ["INT_ADD", "register:40f0:8", ["const:567bcc:8", "const:4:8"]]
- 00567bcc ["CALL", null, ["callee:00c57c50:8"]]
+ 0058aa64 ["INT_ADD", "register:40f0:8", ["const:58aa64:8", "const:4:8"]]
+ 0058aa64 ["CALL", null, ["callee:00c57c50:8"]]
- 00567bcc bytes 8dcd1994
+ 0058aa64 bytes 7b341b94
~~~


<a id="compare-bdb5742c8da57db8cf8fa0c387d55dd5"></a>

### [`00567bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567bfc.md) → [`0058aa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md) FUN_0058aa94

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00567ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ad4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0058a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567bfc.md#insn-00567c44) · [`00567c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567bfc.md#insn-00567c54) · [`00567c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567bfc.md#insn-00567c74)
- 新版 `0058aadc`（命令位置の公開資料なし） · `0058aaec`（命令位置の公開資料なし） · `0058ab0c`（命令位置の公開資料なし）

~~~diff
- 00567c44 ["INT_ADD", "register:40f0:8", ["const:567c44:8", "const:4:8"]]
- 00567c44 ["CALL", null, ["callee:0058a96c:8"]]
+ 0058aadc ["INT_ADD", "register:40f0:8", ["const:58aadc:8", "const:4:8"]]
+ 0058aadc ["CALL", null, ["callee:0058a96c:8"]]
- 00567c44 bytes a4ffff97
+ 0058aadc bytes a4ffff97
- 00567c54 ["INT_ADD", "register:40f0:8", ["const:567c54:8", "const:4:8"]]
- 00567c54 ["CALL", null, ["callee:0058a96c:8"]]
+ 0058aaec ["INT_ADD", "register:40f0:8", ["const:58aaec:8", "const:4:8"]]
+ 0058aaec ["CALL", null, ["callee:0058a96c:8"]]
- 00567c54 bytes a0ffff97
+ 0058aaec bytes a0ffff97
- 00567c74 ["INT_ADD", "register:40f0:8", ["const:567c74:8", "const:4:8"]]
- 00567c74 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058ab0c ["INT_ADD", "register:40f0:8", ["const:58ab0c:8", "const:4:8"]]
+ 0058ab0c ["CALL", null, ["callee:00c57a90:8"]]
- 00567c74 bytes f3cc1994
+ 0058ab0c bytes e1331b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76955629b42a66176de92ef289d19185"></a>

### [`00567df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567df8.md) → [`0058ac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ac90.md) FUN_0058ac90

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567df8.md#insn-00567e54) · [`00567e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567df8.md#insn-00567e74) · [`00567e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567df8.md#insn-00567e90)
- 新版 `0058acec`（命令位置の公開資料なし） · `0058ad0c`（命令位置の公開資料なし） · `0058ad28`（命令位置の公開資料なし）

~~~diff
- 00567e54 ["INT_ADD", "register:40f0:8", ["const:567e54:8", "const:4:8"]]
- 00567e54 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058acec ["INT_ADD", "register:40f0:8", ["const:58acec:8", "const:4:8"]]
+ 0058acec ["CALL", null, ["callee:00c57a90:8"]]
- 00567e54 bytes 7bcc1994
+ 0058acec bytes 69331b94
- 00567e74 ["INT_ADD", "register:40f0:8", ["const:567e74:8", "const:4:8"]]
- 00567e74 ["CALL", null, ["callee:00c57b40:8"]]
+ 0058ad0c ["INT_ADD", "register:40f0:8", ["const:58ad0c:8", "const:4:8"]]
+ 0058ad0c ["CALL", null, ["callee:00c57b40:8"]]
- 00567e74 bytes 9fcc1994
+ 0058ad0c bytes 8d331b94
- 00567e90 ["INT_ADD", "register:40f0:8", ["const:567e90:8", "const:4:8"]]
- 00567e90 ["CALL", null, ["callee:0043b724:8"]]
+ 0058ad28 ["INT_ADD", "register:40f0:8", ["const:58ad28:8", "const:4:8"]]
+ 0058ad28 ["CALL", null, ["callee:0043b724:8"]]
- 00567e90 bytes 65c3fa97
+ 0058ad28 bytes 7fc2fa97
~~~


<a id="compare-7749da87e62fcf5bc1e2feec3187cb2e"></a>

### [`00567e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567e94.md) → [`0058ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md) FUN_0058ad2c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561ec4.md) · 呼出先 2件 [`0056873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056873c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00584d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584d5c.md) · 呼出先 2件 [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567e94.md#insn-00567ec0) · [`00567eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567e94.md#insn-00567eec)
- 新版 `0058ad58`（命令位置の公開資料なし） · `0058ad84`（命令位置の公開資料なし）

~~~diff
- 00567ec0 ["INT_ADD", "register:40f0:8", ["const:567ec0:8", "const:4:8"]]
- 00567ec0 ["CALL", null, ["callee:0058b5d4:8"]]
+ 0058ad58 ["INT_ADD", "register:40f0:8", ["const:58ad58:8", "const:4:8"]]
+ 0058ad58 ["CALL", null, ["callee:0058b5d4:8"]]
- 00567ec0 bytes 1f020094
+ 0058ad58 bytes 1f020094
- 00567eec ["INT_ADD", "register:40f0:8", ["const:567eec:8", "const:4:8"]]
- 00567eec ["CALL", null, ["callee:00c57ae0:8"]]
+ 0058ad84 ["INT_ADD", "register:40f0:8", ["const:58ad84:8", "const:4:8"]]
+ 0058ad84 ["CALL", null, ["callee:00c57ae0:8"]]
- 00567eec bytes 69cc1994
+ 0058ad84 bytes 57331b94
~~~


<a id="compare-033dff48fac0be4d89c0e2b010c3bacc"></a>

### [`00567ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ef0.md) → [`0058ad88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md) FUN_0058ad88

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00574730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574730.md) [`0084a3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a3a8.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`0056873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056873c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`0087d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d340.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00567f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ef0.md#insn-00567f40) · [`00567fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ef0.md#insn-00567fd4) · [`00567fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ef0.md#insn-00567fec)
- 新版 `0058add8`（命令位置の公開資料なし） · `0058ae6c`（命令位置の公開資料なし） · `0058ae84`（命令位置の公開資料なし）

~~~diff
- 00567f40 ["INT_ADD", "register:40f0:8", ["const:567f40:8", "const:4:8"]]
- 00567f40 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058add8 ["INT_ADD", "register:40f0:8", ["const:58add8:8", "const:4:8"]]
+ 0058add8 ["CALL", null, ["callee:00c57a90:8"]]
- 00567f40 bytes 40cc1994
+ 0058add8 bytes 2e331b94
- 00567fd4 ["INT_ADD", "register:40f0:8", ["const:567fd4:8", "const:4:8"]]
- 00567fd4 ["CALL", null, ["callee:0058b5d4:8"]]
+ 0058ae6c ["INT_ADD", "register:40f0:8", ["const:58ae6c:8", "const:4:8"]]
+ 0058ae6c ["CALL", null, ["callee:0058b5d4:8"]]
- 00567fd4 bytes da010094
+ 0058ae6c bytes da010094
- 00567fec ["INT_ADD", "register:40f0:8", ["const:567fec:8", "const:4:8"]]
- 00567fec ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058ae84 ["INT_ADD", "register:40f0:8", ["const:58ae84:8", "const:4:8"]]
+ 0058ae84 ["CALL", null, ["callee:00c57ab0:8"]]
- 00567fec bytes 1dcc1994
+ 0058ae84 bytes 0b331b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0f003070db9b6dad9a95512339c0248"></a>

### [`00568064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568064.md) → [`0058aefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aefc.md) FUN_0058aefc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00574734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574734.md) · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`0056873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056873c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005680a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568064.md#insn-005680a8) · [`005680c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568064.md#insn-005680c0) · [`005680d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568064.md#insn-005680d4)
- 新版 `0058af40`（命令位置の公開資料なし） · `0058af58`（命令位置の公開資料なし） · `0058af6c`（命令位置の公開資料なし）

~~~diff
- 005680a8 ["INT_ADD", "register:40f0:8", ["const:5680a8:8", "const:4:8"]]
- 005680a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058af40 ["INT_ADD", "register:40f0:8", ["const:58af40:8", "const:4:8"]]
+ 0058af40 ["CALL", null, ["callee:00c57a90:8"]]
- 005680a8 bytes e6cb1994
+ 0058af40 bytes d4321b94
- 005680c0 ["INT_ADD", "register:40f0:8", ["const:5680c0:8", "const:4:8"]]
- 005680c0 ["CALL", null, ["callee:00c57c00:8"]]
+ 0058af58 ["INT_ADD", "register:40f0:8", ["const:58af58:8", "const:4:8"]]
+ 0058af58 ["CALL", null, ["callee:00c57c00:8"]]
- 005680c0 bytes 3ccc1994
+ 0058af58 bytes 2a331b94
- 005680d4 ["INT_ADD", "register:40f0:8", ["const:5680d4:8", "const:4:8"]]
- 005680d4 ["CALL", null, ["callee:0058b5d4:8"]]
+ 0058af6c ["INT_ADD", "register:40f0:8", ["const:58af6c:8", "const:4:8"]]
+ 0058af6c ["CALL", null, ["callee:0058b5d4:8"]]
- 005680d4 bytes 9a010094
+ 0058af6c bytes 9a010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91bd23604631c430218caf9a614cd357"></a>

### [`0056817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056817c.md) → [`0058b014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b014.md) FUN_0058b014

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005681d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056817c.md#insn-005681d8) · [`005681f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056817c.md#insn-005681f8) · [`00568214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056817c.md#insn-00568214)
- 新版 `0058b070`（命令位置の公開資料なし） · `0058b090`（命令位置の公開資料なし） · `0058b0ac`（命令位置の公開資料なし）

~~~diff
- 005681d8 ["INT_ADD", "register:40f0:8", ["const:5681d8:8", "const:4:8"]]
- 005681d8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058b070 ["INT_ADD", "register:40f0:8", ["const:58b070:8", "const:4:8"]]
+ 0058b070 ["CALL", null, ["callee:00c57a90:8"]]
- 005681d8 bytes 9acb1994
+ 0058b070 bytes 88321b94
- 005681f8 ["INT_ADD", "register:40f0:8", ["const:5681f8:8", "const:4:8"]]
- 005681f8 ["CALL", null, ["callee:00c57b40:8"]]
+ 0058b090 ["INT_ADD", "register:40f0:8", ["const:58b090:8", "const:4:8"]]
+ 0058b090 ["CALL", null, ["callee:00c57b40:8"]]
- 005681f8 bytes becb1994
+ 0058b090 bytes ac321b94
- 00568214 ["INT_ADD", "register:40f0:8", ["const:568214:8", "const:4:8"]]
- 00568214 ["CALL", null, ["callee:0043b724:8"]]
+ 0058b0ac ["INT_ADD", "register:40f0:8", ["const:58b0ac:8", "const:4:8"]]
+ 0058b0ac ["CALL", null, ["callee:0043b724:8"]]
- 00568214 bytes 84c2fa97
+ 0058b0ac bytes 9ec1fa97
~~~


<a id="compare-542149b23bf01d96483d16c9e9fecbb0"></a>

### [`00568258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568258.md) → [`0058b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md) FUN_0058b0f0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00565e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00568284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568258.md#insn-00568284) · [`0056829c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568258.md#insn-0056829c) · [`005682b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568258.md#insn-005682b4)
- 新版 `0058b11c`（命令位置の公開資料なし） · `0058b134`（命令位置の公開資料なし） · `0058b14c`（命令位置の公開資料なし）

~~~diff
- 00568284 ["COPY", "register:0:8", ["register:4048:8"]]
- 00568284 ["INT_ADD", "register:40f0:8", ["const:568284:8", "const:4:8"]]
- 00568284 ["CALLIND", null, ["register:0:8"]]
+ 0058b11c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b11c ["INT_ADD", "register:40f0:8", ["const:58b11c:8", "const:4:8"]]
+ 0058b11c ["CALLIND", null, ["register:0:8"]]
- 00568284 bytes 20013fd6
+ 0058b11c bytes 20013fd6
- 0056829c ["COPY", "register:0:8", ["register:4048:8"]]
- 0056829c ["INT_ADD", "register:40f0:8", ["const:56829c:8", "const:4:8"]]
- 0056829c ["CALLIND", null, ["register:0:8"]]
+ 0058b134 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b134 ["INT_ADD", "register:40f0:8", ["const:58b134:8", "const:4:8"]]
+ 0058b134 ["CALLIND", null, ["register:0:8"]]
- 0056829c bytes 20013fd6
+ 0058b134 bytes 20013fd6
- 005682b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005682b4 ["INT_ADD", "register:40f0:8", ["const:5682b4:8", "const:4:8"]]
- 005682b4 ["CALLIND", null, ["register:0:8"]]
+ 0058b14c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b14c ["INT_ADD", "register:40f0:8", ["const:58b14c:8", "const:4:8"]]
+ 0058b14c ["CALLIND", null, ["register:0:8"]]
- 005682b4 bytes 20013fd6
+ 0058b14c bytes 20013fd6
~~~


<a id="compare-c1fd8e99b41a7d0e8cd4a28cf84fb5bc"></a>

### [`005682f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005682f8.md) → [`0058b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b190.md) FUN_0058b190

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00574738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574738.md) · 呼出先 3件 [`0056891c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056891c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) · 呼出先 3件 [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056832c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005682f8.md#insn-0056832c) · [`00568344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005682f8.md#insn-00568344) · [`00568398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005682f8.md#insn-00568398)
- 新版 `0058b1c4`（命令位置の公開資料なし） · `0058b1dc`（命令位置の公開資料なし） · `0058b230`（命令位置の公開資料なし）

~~~diff
- 0056832c ["INT_ADD", "register:40f0:8", ["const:56832c:8", "const:4:8"]]
- 0056832c ["CALL", null, ["callee:0058b7b4:8"]]
+ 0058b1c4 ["INT_ADD", "register:40f0:8", ["const:58b1c4:8", "const:4:8"]]
+ 0058b1c4 ["CALL", null, ["callee:0058b7b4:8"]]
- 0056832c bytes 7c010094
+ 0058b1c4 bytes 7c010094
- 00568344 ["INT_ADD", "register:40f0:8", ["const:568344:8", "const:4:8"]]
- 00568344 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058b1dc ["INT_ADD", "register:40f0:8", ["const:58b1dc:8", "const:4:8"]]
+ 0058b1dc ["CALL", null, ["callee:00c57ab0:8"]]
- 00568344 bytes 47cb1994
+ 0058b1dc bytes 35321b94
- 00568398 ["INT_ADD", "register:40f0:8", ["const:568398:8", "const:4:8"]]
- 00568398 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0058b230 ["INT_ADD", "register:40f0:8", ["const:58b230:8", "const:4:8"]]
+ 0058b230 ["CALL", null, ["callee:00c57ae0:8"]]
- 00568398 bytes 3ecb1994
+ 0058b230 bytes 2c321b94
~~~


<a id="compare-b3bd4574202b7c36950646bfcd272851"></a>

### [`0056839c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056839c.md) → [`0058b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b234.md) FUN_0058b234

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0057473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057473c.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`0056891c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056891c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005975d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d4.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005683ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056839c.md#insn-005683ec) · [`00568480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056839c.md#insn-00568480) · [`00568498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056839c.md#insn-00568498)
- 新版 `0058b284`（命令位置の公開資料なし） · `0058b318`（命令位置の公開資料なし） · `0058b330`（命令位置の公開資料なし）

~~~diff
- 005683ec ["INT_ADD", "register:40f0:8", ["const:5683ec:8", "const:4:8"]]
- 005683ec ["CALL", null, ["callee:00c57a90:8"]]
+ 0058b284 ["INT_ADD", "register:40f0:8", ["const:58b284:8", "const:4:8"]]
+ 0058b284 ["CALL", null, ["callee:00c57a90:8"]]
- 005683ec bytes 15cb1994
+ 0058b284 bytes 03321b94
- 00568480 ["INT_ADD", "register:40f0:8", ["const:568480:8", "const:4:8"]]
- 00568480 ["CALL", null, ["callee:0058b7b4:8"]]
+ 0058b318 ["INT_ADD", "register:40f0:8", ["const:58b318:8", "const:4:8"]]
+ 0058b318 ["CALL", null, ["callee:0058b7b4:8"]]
- 00568480 bytes 27010094
+ 0058b318 bytes 27010094
- 00568498 ["INT_ADD", "register:40f0:8", ["const:568498:8", "const:4:8"]]
- 00568498 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058b330 ["INT_ADD", "register:40f0:8", ["const:58b330:8", "const:4:8"]]
+ 0058b330 ["CALL", null, ["callee:00c57ab0:8"]]
- 00568498 bytes f2ca1994
+ 0058b330 bytes e0311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab28b2f30b4e771cd24915102e3345c"></a>

### [`00568510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568510.md) → [`0058b3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b3a8.md) FUN_0058b3a8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574740.md) · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`0056891c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056891c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568510.md#insn-0056854c) · [`00568564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568510.md#insn-00568564) · [`0056857c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568510.md#insn-0056857c)
- 新版 `0058b3e4`（命令位置の公開資料なし） · `0058b3fc`（命令位置の公開資料なし） · `0058b414`（命令位置の公開資料なし）

~~~diff
- 0056854c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056854c ["INT_ADD", "register:40f0:8", ["const:56854c:8", "const:4:8"]]
- 0056854c ["CALLIND", null, ["register:0:8"]]
+ 0058b3e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058b3e4 ["INT_ADD", "register:40f0:8", ["const:58b3e4:8", "const:4:8"]]
+ 0058b3e4 ["CALLIND", null, ["register:0:8"]]
- 0056854c bytes 00013fd6
+ 0058b3e4 bytes 00013fd6
- 00568564 ["COPY", "register:0:8", ["register:4048:8"]]
- 00568564 ["INT_ADD", "register:40f0:8", ["const:568564:8", "const:4:8"]]
- 00568564 ["CALLIND", null, ["register:0:8"]]
+ 0058b3fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b3fc ["INT_ADD", "register:40f0:8", ["const:58b3fc:8", "const:4:8"]]
+ 0058b3fc ["CALLIND", null, ["register:0:8"]]
- 00568564 bytes 20013fd6
+ 0058b3fc bytes 20013fd6
- 0056857c ["COPY", "register:0:8", ["register:4048:8"]]
- 0056857c ["INT_ADD", "register:40f0:8", ["const:56857c:8", "const:4:8"]]
- 0056857c ["CALLIND", null, ["register:0:8"]]
+ 0058b414 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b414 ["INT_ADD", "register:40f0:8", ["const:58b414:8", "const:4:8"]]
+ 0058b414 ["CALLIND", null, ["register:0:8"]]
- 0056857c bytes 20013fd6
+ 0058b414 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d96789efd4ebb505400a493e691e7e"></a>

### [`00568814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568814.md) → [`0058b6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b6ac.md) FUN_0058b6ac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00568220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568220.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0058b0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0b8.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005688a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568814.md#insn-005688a8) · [`005688d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568814.md#insn-005688d0) · [`005688e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568814.md#insn-005688e4)
- 新版 `0058b740`（命令位置の公開資料なし） · `0058b768`（命令位置の公開資料なし） · `0058b77c`（命令位置の公開資料なし）

~~~diff
- 005688a8 ["INT_ADD", "register:40f0:8", ["const:5688a8:8", "const:4:8"]]
- 005688a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058b740 ["INT_ADD", "register:40f0:8", ["const:58b740:8", "const:4:8"]]
+ 0058b740 ["CALL", null, ["callee:00c57a90:8"]]
- 005688a8 bytes e6c91994
+ 0058b740 bytes d4301b94
- 005688d0 ["INT_ADD", "register:40f0:8", ["const:5688d0:8", "const:4:8"]]
- 005688d0 ["CALL", null, ["callee:00c57c00:8"]]
+ 0058b768 ["INT_ADD", "register:40f0:8", ["const:58b768:8", "const:4:8"]]
+ 0058b768 ["CALL", null, ["callee:00c57c00:8"]]
- 005688d0 bytes 38ca1994
+ 0058b768 bytes 26311b94
- 005688e4 ["INT_ADD", "register:40f0:8", ["const:5688e4:8", "const:4:8"]]
- 005688e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058b77c ["INT_ADD", "register:40f0:8", ["const:58b77c:8", "const:4:8"]]
+ 0058b77c ["CALL", null, ["callee:00c57ab0:8"]]
- 005688e4 bytes dfc91994
+ 0058b77c bytes cd301b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba6a34cf672d933af8922f00f0cb7de7"></a>

### [`0056bc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bc6c.md) → [`0058eb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058eb04.md) FUN_0058eb04

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056bc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bc6c.md#insn-0056bc94) · [`0056bc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bc6c.md#insn-0056bc9c) · [`0056bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bc6c.md#insn-0056bce8)
- 新版 `0058eb2c`（命令位置の公開資料なし） · `0058eb34`（命令位置の公開資料なし） · `0058eb80`（命令位置の公開資料なし）

~~~diff
- 0056bc94 ["INT_ADD", "register:40f0:8", ["const:56bc94:8", "const:4:8"]]
- 0056bc94 ["CALL", null, ["callee:00589800:8"]]
+ 0058eb2c ["INT_ADD", "register:40f0:8", ["const:58eb2c:8", "const:4:8"]]
+ 0058eb2c ["CALL", null, ["callee:00589800:8"]]
- 0056bc94 bytes 35ebff97
+ 0058eb2c bytes 35ebff97
- 0056bc9c ["INT_ADD", "register:40f0:8", ["const:56bc9c:8", "const:4:8"]]
- 0056bc9c ["CALL", null, ["callee:00588e2c:8"]]
+ 0058eb34 ["INT_ADD", "register:40f0:8", ["const:58eb34:8", "const:4:8"]]
+ 0058eb34 ["CALL", null, ["callee:00588e2c:8"]]
- 0056bc9c bytes bee8ff97
+ 0058eb34 bytes bee8ff97
- 0056bce8 ["INT_ADD", "register:40f0:8", ["const:56bce8:8", "const:4:8"]]
- 0056bce8 ["CALL", null, ["callee:005892e0:8"]]
+ 0058eb80 ["INT_ADD", "register:40f0:8", ["const:58eb80:8", "const:4:8"]]
+ 0058eb80 ["CALL", null, ["callee:005892e0:8"]]
- 0056bce8 bytes d8e9ff97
+ 0058eb80 bytes d8e9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99e51e39ea596483c33afbab184c3af8"></a>

### [`0056be5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056be5c.md) → [`0058ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ecf4.md) FUN_0058ecf4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe8.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00597e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e80.md) · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056be7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056be5c.md#insn-0056be7c) · [`0056be84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056be5c.md#insn-0056be84) · [`0056bec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056be5c.md#insn-0056bec8)
- 新版 `0058ed14`（命令位置の公開資料なし） · `0058ed1c`（命令位置の公開資料なし） · `0058ed60`（命令位置の公開資料なし）

~~~diff
- 0056be7c ["INT_ADD", "register:40f0:8", ["const:56be7c:8", "const:4:8"]]
- 0056be7c ["CALL", null, ["callee:00588e2c:8"]]
+ 0058ed14 ["INT_ADD", "register:40f0:8", ["const:58ed14:8", "const:4:8"]]
+ 0058ed14 ["CALL", null, ["callee:00588e2c:8"]]
- 0056be7c bytes 46e8ff97
+ 0058ed14 bytes 46e8ff97
- 0056be84 ["INT_ADD", "register:40f0:8", ["const:56be84:8", "const:4:8"]]
- 0056be84 ["CALL", null, ["callee:0058911c:8"]]
+ 0058ed1c ["INT_ADD", "register:40f0:8", ["const:58ed1c:8", "const:4:8"]]
+ 0058ed1c ["CALL", null, ["callee:0058911c:8"]]
- 0056be84 bytes 00e9ff97
+ 0058ed1c bytes 00e9ff97
- 0056bec8 ["INT_ADD", "register:40f0:8", ["const:56bec8:8", "const:4:8"]]
- 0056bec8 ["CALL", null, ["callee:005892e0:8"]]
+ 0058ed60 ["INT_ADD", "register:40f0:8", ["const:58ed60:8", "const:4:8"]]
+ 0058ed60 ["CALL", null, ["callee:005892e0:8"]]
- 0056bec8 bytes 60e9ff97
+ 0058ed60 bytes 60e9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d835f5aa97ab4bcdb919e977b2049ad"></a>

### [`0056c438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c438.md) → [`0058f2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f2d0.md) FUN_0058f2d0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056968c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/0056968c.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058c524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c524.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c438.md#insn-0056c4a4) · [`0056c500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c438.md#insn-0056c500) · [`0056c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c438.md#insn-0056c52c)
- 新版 `0058f33c`（命令位置の公開資料なし） · `0058f398`（命令位置の公開資料なし） · `0058f3c4`（命令位置の公開資料なし）

~~~diff
- 0056c4a4 ["INT_ADD", "register:40f0:8", ["const:56c4a4:8", "const:4:8"]]
- 0056c4a4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058f33c ["INT_ADD", "register:40f0:8", ["const:58f33c:8", "const:4:8"]]
+ 0058f33c ["CALL", null, ["callee:00c57a90:8"]]
- 0056c4a4 bytes e7ba1994
+ 0058f33c bytes d5211b94
- 0056c500 ["COPY", "register:0:8", ["register:4048:8"]]
- 0056c500 ["INT_ADD", "register:40f0:8", ["const:56c500:8", "const:4:8"]]
- 0056c500 ["CALLIND", null, ["register:0:8"]]
+ 0058f398 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058f398 ["INT_ADD", "register:40f0:8", ["const:58f398:8", "const:4:8"]]
+ 0058f398 ["CALLIND", null, ["register:0:8"]]
- 0056c500 bytes 20013fd6
+ 0058f398 bytes 20013fd6
- 0056c52c ["INT_ADD", "register:40f0:8", ["const:56c52c:8", "const:4:8"]]
- 0056c52c ["CALL", null, ["callee:0043bb64:8"]]
+ 0058f3c4 ["INT_ADD", "register:40f0:8", ["const:58f3c4:8", "const:4:8"]]
+ 0058f3c4 ["CALL", null, ["callee:0043bb64:8"]]
- 0056c52c bytes ceb2fa97
+ 0058f3c4 bytes e8b1fa97
~~~


<a id="compare-dfd053b078a9d83cd04cff8cbdaa5d33"></a>

### [`0056c55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md) → [`0058f3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md) FUN_0058f3f4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00569dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569dd8.md) [`0056a080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a080.md) [`00588db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588db4.md) [`00855450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855450.md) [`0085d634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d634.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 7件 [`0058cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc70.md) [`0058cf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cf18.md) [`005ad378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md) [`008883e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md) [`008905cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md#insn-0056c5c8) · [`0056c5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md#insn-0056c5d8) · [`0056c5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md#insn-0056c5f8)
- 新版 `0058f460`（命令位置の公開資料なし） · `0058f470`（命令位置の公開資料なし） · `0058f490`（命令位置の公開資料なし）

~~~diff
- 0056c5c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c5c8 ["INT_ADD", "register:40f0:8", ["const:56c5c8:8", "const:4:8"]]
- 0056c5c8 ["CALLIND", null, ["register:0:8"]]
+ 0058f460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f460 ["INT_ADD", "register:40f0:8", ["const:58f460:8", "const:4:8"]]
+ 0058f460 ["CALLIND", null, ["register:0:8"]]
- 0056c5c8 bytes 00013fd6
+ 0058f460 bytes 00013fd6
- 0056c5d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c5d8 ["INT_ADD", "register:40f0:8", ["const:56c5d8:8", "const:4:8"]]
- 0056c5d8 ["CALLIND", null, ["register:0:8"]]
+ 0058f470 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f470 ["INT_ADD", "register:40f0:8", ["const:58f470:8", "const:4:8"]]
+ 0058f470 ["CALLIND", null, ["register:0:8"]]
- 0056c5d8 bytes 00013fd6
+ 0058f470 bytes 00013fd6
- 0056c5f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c5f8 ["INT_ADD", "register:40f0:8", ["const:56c5f8:8", "const:4:8"]]
- 0056c5f8 ["CALLIND", null, ["register:0:8"]]
+ 0058f490 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f490 ["INT_ADD", "register:40f0:8", ["const:58f490:8", "const:4:8"]]
+ 0058f490 ["CALLIND", null, ["register:0:8"]]
- 0056c5f8 bytes 00013fd6
+ 0058f490 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5859251aaa2d8a072a0977f831d2aea0"></a>

### [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) → [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) FUN_0058f55c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0056acb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056acb4.md) [`00af2808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md) [`00af413c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af413c.md) [`00b55e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md) [`00b56178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56178.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 9件 [`0058db4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058db4c.md) [`00b5258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md) [`00b53ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ec0.md) [`00bc4c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md) [`00bc4f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4f30.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md#insn-0056c738) · [`0056c75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md#insn-0056c75c)
- 新版 `0058f5d0`（命令位置の公開資料なし） · `0058f5f4`（命令位置の公開資料なし）

~~~diff
- 0056c738 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c738 ["INT_ADD", "register:40f0:8", ["const:56c738:8", "const:4:8"]]
- 0056c738 ["CALLIND", null, ["register:0:8"]]
+ 0058f5d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f5d0 ["INT_ADD", "register:40f0:8", ["const:58f5d0:8", "const:4:8"]]
+ 0058f5d0 ["CALLIND", null, ["register:0:8"]]
- 0056c738 bytes 00013fd6
+ 0058f5d0 bytes 00013fd6
- 0056c75c ["INT_ADD", "register:40f0:8", ["const:56c75c:8", "const:4:8"]]
- 0056c75c ["CALL", null, ["callee:00c57ae0:8"]]
+ 0058f5f4 ["INT_ADD", "register:40f0:8", ["const:58f5f4:8", "const:4:8"]]
+ 0058f5f4 ["CALL", null, ["callee:00c57ae0:8"]]
- 0056c75c bytes 4dba1994
+ 0058f5f4 bytes 3b211b94
~~~


<a id="compare-e655c53dba98f13b6188c443997b9e1a"></a>

### [`0056c850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c850.md) → [`0058f6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f6e8.md) FUN_0058f6e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056de40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056de40.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00590cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590cd8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056c86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c850.md#insn-0056c86c) · [`0056c88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c850.md#insn-0056c88c)
- 新版 `0058f704`（命令位置の公開資料なし） · `0058f724`（命令位置の公開資料なし）

~~~diff
- 0056c86c ["INT_ADD", "register:40f0:8", ["const:56c86c:8", "const:4:8"]]
- 0056c86c ["CALL", null, ["callee:00c538e0:8"]]
+ 0058f704 ["INT_ADD", "register:40f0:8", ["const:58f704:8", "const:4:8"]]
+ 0058f704 ["CALL", null, ["callee:00c538e0:8"]]
- 0056c86c bytes 89a91994
+ 0058f704 bytes 77101b94
- 0056c88c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c88c ["INT_ADD", "register:40f0:8", ["const:56c88c:8", "const:4:8"]]
- 0056c88c ["CALLIND", null, ["register:0:8"]]
+ 0058f724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f724 ["INT_ADD", "register:40f0:8", ["const:58f724:8", "const:4:8"]]
+ 0058f724 ["CALLIND", null, ["register:0:8"]]
- 0056c88c bytes 00013fd6
+ 0058f724 bytes 00013fd6
~~~


<a id="compare-0a6ccc3832332eec6b100c7c90542ac1"></a>

### [`0056d410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d410.md) → [`005902a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005902a8.md) FUN_005902a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056c8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8a0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0058f738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f738.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d410.md#insn-0056d440) · [`0056d48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d410.md#insn-0056d48c)
- 新版 `005902d8`（命令位置の公開資料なし） · `00590324`（命令位置の公開資料なし）

~~~diff
- 0056d440 ["INT_ADD", "register:40f0:8", ["const:56d440:8", "const:4:8"]]
- 0056d440 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005902d8 ["INT_ADD", "register:40f0:8", ["const:5902d8:8", "const:4:8"]]
+ 005902d8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0056d440 bytes 08b71994
+ 005902d8 bytes f61d1b94
- 0056d48c ["INT_ADD", "register:40f0:8", ["const:56d48c:8", "const:4:8"]]
- 0056d48c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00590324 ["INT_ADD", "register:40f0:8", ["const:590324:8", "const:4:8"]]
+ 00590324 ["CALL", null, ["callee:00c57ab0:8"]]
- 0056d48c bytes f5b61994
+ 00590324 bytes e31d1b94
~~~


<a id="compare-c6b1424afda36d7ef5575122d567e76e"></a>

### [`0056d4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d4e0.md) → [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) FUN_00590378

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056cec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cec4.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0056d9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d9a0.md) [`0056db28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056db28.md) [`0056dcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dcb4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00590838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590838.md) [`005909c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005909c0.md) [`00590b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590b4c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d4e0.md#insn-0056d578) · [`0056d5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d4e0.md#insn-0056d5bc) · [`0056d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d4e0.md#insn-0056d5cc)
- 新版 `00590410`（命令位置の公開資料なし） · `00590454`（命令位置の公開資料なし） · `00590464`（命令位置の公開資料なし）

~~~diff
- 0056d578 ["INT_ADD", "register:40f0:8", ["const:56d578:8", "const:4:8"]]
- 0056d578 ["CALL", null, ["callee:00c57b40:8"]]
+ 00590410 ["INT_ADD", "register:40f0:8", ["const:590410:8", "const:4:8"]]
+ 00590410 ["CALL", null, ["callee:00c57b40:8"]]
- 0056d578 bytes deb61994
+ 00590410 bytes cc1d1b94
- 0056d5bc ["INT_ADD", "register:40f0:8", ["const:56d5bc:8", "const:4:8"]]
- 0056d5bc ["CALL", null, ["callee:00c57a90:8"]]
+ 00590454 ["INT_ADD", "register:40f0:8", ["const:590454:8", "const:4:8"]]
+ 00590454 ["CALL", null, ["callee:00c57a90:8"]]
- 0056d5bc bytes a1b61994
+ 00590454 bytes 8f1d1b94
- 0056d5cc ["INT_ADD", "register:40f0:8", ["const:56d5cc:8", "const:4:8"]]
- 0056d5cc ["CALL", null, ["callee:00590838:8"]]
+ 00590464 ["INT_ADD", "register:40f0:8", ["const:590464:8", "const:4:8"]]
+ 00590464 ["CALL", null, ["callee:00590838:8"]]
- 0056d5cc bytes f5000094
+ 00590464 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f119c06b23d0a0dfb53dc8e7a0500d2d"></a>

### [`0056d9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d9a0.md) → [`00590838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590838.md) FUN_00590838

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d4e0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056da08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d9a0.md#insn-0056da08) · [`0056da40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d9a0.md#insn-0056da40) · [`0056daf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d9a0.md#insn-0056daf0)
- 新版 `005908a0`（命令位置の公開資料なし） · `005908d8`（命令位置の公開資料なし） · `00590988`（命令位置の公開資料なし）

~~~diff
- 0056da08 ["INT_ADD", "register:40f0:8", ["const:56da08:8", "const:4:8"]]
- 0056da08 ["CALL", null, ["callee:00c57b40:8"]]
+ 005908a0 ["INT_ADD", "register:40f0:8", ["const:5908a0:8", "const:4:8"]]
+ 005908a0 ["CALL", null, ["callee:00c57b40:8"]]
- 0056da08 bytes bab51994
+ 005908a0 bytes a81c1b94
- 0056da40 ["INT_ADD", "register:40f0:8", ["const:56da40:8", "const:4:8"]]
- 0056da40 ["CALL", null, ["callee:00c57a90:8"]]
+ 005908d8 ["INT_ADD", "register:40f0:8", ["const:5908d8:8", "const:4:8"]]
+ 005908d8 ["CALL", null, ["callee:00c57a90:8"]]
- 0056da40 bytes 80b51994
+ 005908d8 bytes 6e1c1b94
- 0056daf0 ["INT_ADD", "register:40f0:8", ["const:56daf0:8", "const:4:8"]]
- 0056daf0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00590988 ["INT_ADD", "register:40f0:8", ["const:590988:8", "const:4:8"]]
+ 00590988 ["CALL", null, ["callee:00c57ab0:8"]]
- 0056daf0 bytes 5cb51994
+ 00590988 bytes 4a1c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ad7aeba83d97a63e7d289097aa5e0a"></a>

### [`0056db28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056db28.md) → [`005909c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005909c0.md) FUN_005909c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d4e0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056db98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056db28.md#insn-0056db98) · [`0056dbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056db28.md#insn-0056dbd0) · [`0056dc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056db28.md#insn-0056dc80)
- 新版 `00590a30`（命令位置の公開資料なし） · `00590a68`（命令位置の公開資料なし） · `00590b18`（命令位置の公開資料なし）

~~~diff
- 0056db98 ["INT_ADD", "register:40f0:8", ["const:56db98:8", "const:4:8"]]
- 0056db98 ["CALL", null, ["callee:00c57b40:8"]]
+ 00590a30 ["INT_ADD", "register:40f0:8", ["const:590a30:8", "const:4:8"]]
+ 00590a30 ["CALL", null, ["callee:00c57b40:8"]]
- 0056db98 bytes 56b51994
+ 00590a30 bytes 441c1b94
- 0056dbd0 ["INT_ADD", "register:40f0:8", ["const:56dbd0:8", "const:4:8"]]
- 0056dbd0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00590a68 ["INT_ADD", "register:40f0:8", ["const:590a68:8", "const:4:8"]]
+ 00590a68 ["CALL", null, ["callee:00c57a90:8"]]
- 0056dbd0 bytes 1cb51994
+ 00590a68 bytes 0a1c1b94
- 0056dc80 ["INT_ADD", "register:40f0:8", ["const:56dc80:8", "const:4:8"]]
- 0056dc80 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00590b18 ["INT_ADD", "register:40f0:8", ["const:590b18:8", "const:4:8"]]
+ 00590b18 ["CALL", null, ["callee:00c57ab0:8"]]
- 0056dc80 bytes f8b41994
+ 00590b18 bytes e61b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9628feab6a2ccfa56471fa4fcf0c049"></a>

### [`0056dcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dcb4.md) → [`00590b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590b4c.md) FUN_00590b4c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d4e0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056dd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dcb4.md#insn-0056dd24) · [`0056dd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dcb4.md#insn-0056dd5c) · [`0056de0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dcb4.md#insn-0056de0c)
- 新版 `00590bbc`（命令位置の公開資料なし） · `00590bf4`（命令位置の公開資料なし） · `00590ca4`（命令位置の公開資料なし）

~~~diff
- 0056dd24 ["INT_ADD", "register:40f0:8", ["const:56dd24:8", "const:4:8"]]
- 0056dd24 ["CALL", null, ["callee:00c57b40:8"]]
+ 00590bbc ["INT_ADD", "register:40f0:8", ["const:590bbc:8", "const:4:8"]]
+ 00590bbc ["CALL", null, ["callee:00c57b40:8"]]
- 0056dd24 bytes f3b41994
+ 00590bbc bytes e11b1b94
- 0056dd5c ["INT_ADD", "register:40f0:8", ["const:56dd5c:8", "const:4:8"]]
- 0056dd5c ["CALL", null, ["callee:00c57a90:8"]]
+ 00590bf4 ["INT_ADD", "register:40f0:8", ["const:590bf4:8", "const:4:8"]]
+ 00590bf4 ["CALL", null, ["callee:00c57a90:8"]]
- 0056dd5c bytes b9b41994
+ 00590bf4 bytes a71b1b94
- 0056de0c ["INT_ADD", "register:40f0:8", ["const:56de0c:8", "const:4:8"]]
- 0056de0c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00590ca4 ["INT_ADD", "register:40f0:8", ["const:590ca4:8", "const:4:8"]]
+ 00590ca4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0056de0c bytes 95b41994
+ 00590ca4 bytes 831b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9903954d069358208dc0ddff9760f02e"></a>

### [`0056e334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e334.md) → [`005911cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005911cc.md) FUN_005911cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056e350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e334.md#insn-0056e350) · [`0056e370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e334.md#insn-0056e370)
- 新版 `005911e8`（命令位置の公開資料なし） · `00591208`（命令位置の公開資料なし）

~~~diff
- 0056e350 ["INT_ADD", "register:40f0:8", ["const:56e350:8", "const:4:8"]]
- 0056e350 ["CALL", null, ["callee:00c538e0:8"]]
+ 005911e8 ["INT_ADD", "register:40f0:8", ["const:5911e8:8", "const:4:8"]]
+ 005911e8 ["CALL", null, ["callee:00c538e0:8"]]
- 0056e350 bytes d0a21994
+ 005911e8 bytes be091b94
- 0056e370 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056e370 ["INT_ADD", "register:40f0:8", ["const:56e370:8", "const:4:8"]]
- 0056e370 ["CALLIND", null, ["register:0:8"]]
+ 00591208 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00591208 ["INT_ADD", "register:40f0:8", ["const:591208:8", "const:4:8"]]
+ 00591208 ["CALLIND", null, ["register:0:8"]]
- 0056e370 bytes 00013fd6
+ 00591208 bytes 00013fd6
~~~


<a id="compare-d53fce813a642890754ed1cbc072d1ad"></a>

### [`0056e384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e384.md) → [`0059121c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md) FUN_0059121c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056dee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md) · 呼出先 2件 [`00570dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) · 呼出先 2件 [`00593c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056e3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e384.md#insn-0056e3b0) · [`0056e3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e384.md#insn-0056e3dc)
- 新版 `00591248`（命令位置の公開資料なし） · `00591274`（命令位置の公開資料なし）

~~~diff
- 0056e3b0 ["INT_ADD", "register:40f0:8", ["const:56e3b0:8", "const:4:8"]]
- 0056e3b0 ["CALL", null, ["callee:00593c64:8"]]
+ 00591248 ["INT_ADD", "register:40f0:8", ["const:591248:8", "const:4:8"]]
+ 00591248 ["CALL", null, ["callee:00593c64:8"]]
- 0056e3b0 bytes 870a0094
+ 00591248 bytes 870a0094
- 0056e3dc ["INT_ADD", "register:40f0:8", ["const:56e3dc:8", "const:4:8"]]
- 0056e3dc ["CALL", null, ["callee:00c57ae0:8"]]
+ 00591274 ["INT_ADD", "register:40f0:8", ["const:591274:8", "const:4:8"]]
+ 00591274 ["CALL", null, ["callee:00c57ae0:8"]]
- 0056e3dc bytes 2db31994
+ 00591274 bytes 1b1a1b94
~~~


<a id="compare-a0f2234b500e4ab7409613198aee6699"></a>

### [`0056e7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e7f4.md) → [`0059168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059168c.md) FUN_0059168c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056fc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fc94.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00592b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b2c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056e81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e7f4.md#insn-0056e81c) · [`0056e848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e7f4.md#insn-0056e848)
- 新版 `005916b4`（命令位置の公開資料なし） · `005916e0`（命令位置の公開資料なし）

~~~diff
- 0056e81c ["INT_ADD", "register:40f0:8", ["const:56e81c:8", "const:4:8"]]
- 0056e81c ["CALL", null, ["callee:00592b2c:8"]]
+ 005916b4 ["INT_ADD", "register:40f0:8", ["const:5916b4:8", "const:4:8"]]
+ 005916b4 ["CALL", null, ["callee:00592b2c:8"]]
- 0056e81c bytes 1e050094
+ 005916b4 bytes 1e050094
- 0056e848 ["INT_ADD", "register:40f0:8", ["const:56e848:8", "const:4:8"]]
- 0056e848 ["CALL", null, ["callee:00c57ae0:8"]]
+ 005916e0 ["INT_ADD", "register:40f0:8", ["const:5916e0:8", "const:4:8"]]
+ 005916e0 ["CALL", null, ["callee:00c57ae0:8"]]
- 0056e848 bytes 12b21994
+ 005916e0 bytes 00191b94
~~~


<a id="compare-90ce9688d0a1ba2b13a4846ca63c6dfd"></a>

### [`0056e8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e8f8.md) → [`00591790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591790.md) FUN_00591790

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd560.md) [`00bdd5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd5c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056e90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e8f8.md#insn-0056e90c)
- 新版 `005917a4`（命令位置の公開資料なし）

~~~diff
- 0056e90c ["INT_ADD", "register:40f0:8", ["const:56e90c:8", "const:4:8"]]
- 0056e90c ["CALL", null, ["callee:00c59fb0:8"]]
+ 005917a4 ["INT_ADD", "register:40f0:8", ["const:5917a4:8", "const:4:8"]]
+ 005917a4 ["CALL", null, ["callee:00c59fb0:8"]]
- 0056e90c bytes 15bb1994
+ 005917a4 bytes 03221b94
~~~


<a id="compare-dabd1a396775040ccbf03989f9ca1b2f"></a>

### [`0056e934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e934.md) → [`005917cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005917cc.md) FUN_005917cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd560.md) [`00bdd5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd5d0.md) [`00bdd600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd600.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a020.md) [`00c5a050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056e94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e934.md#insn-0056e94c)
- 新版 `005917e4`（命令位置の公開資料なし）

~~~diff
- 0056e94c ["INT_ADD", "register:40f0:8", ["const:56e94c:8", "const:4:8"]]
- 0056e94c ["CALL", null, ["callee:00c59fb0:8"]]
+ 005917e4 ["INT_ADD", "register:40f0:8", ["const:5917e4:8", "const:4:8"]]
+ 005917e4 ["CALL", null, ["callee:00c59fb0:8"]]
- 0056e94c bytes 05bb1994
+ 005917e4 bytes f3211b94
~~~


<a id="compare-3d4643fe57cf2b56854f4635284cd375"></a>

### [`0056ea48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ea48.md) → [`005918e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005918e0.md) FUN_005918e0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd560.md) [`00bdd610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd610.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ea48.md#insn-0056ea80) · [`0056ea8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ea48.md#insn-0056ea8c) · [`0056eaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ea48.md#insn-0056eaa8)
- 新版 `00591918`（命令位置の公開資料なし） · `00591924`（命令位置の公開資料なし） · `00591940`（命令位置の公開資料なし）

~~~diff
- 0056ea80 ["INT_ADD", "register:40f0:8", ["const:56ea80:8", "const:4:8"]]
- 0056ea80 ["CALL", null, ["callee:00c59fb0:8"]]
+ 00591918 ["INT_ADD", "register:40f0:8", ["const:591918:8", "const:4:8"]]
+ 00591918 ["CALL", null, ["callee:00c59fb0:8"]]
- 0056ea80 bytes b8ba1994
+ 00591918 bytes a6211b94
- 0056ea8c ["INT_ADD", "register:40f0:8", ["const:56ea8c:8", "const:4:8"]]
- 0056ea8c ["CALL", null, ["callee:00c57ad0:8"]]
+ 00591924 ["INT_ADD", "register:40f0:8", ["const:591924:8", "const:4:8"]]
+ 00591924 ["CALL", null, ["callee:00c57ad0:8"]]
- 0056ea8c bytes 7db11994
+ 00591924 bytes 6b181b94
- 0056eaa8 ["INT_ADD", "register:40f0:8", ["const:56eaa8:8", "const:4:8"]]
- 0056eaa8 ["CALL", null, ["callee:00c5a060:8"]]
+ 00591940 ["INT_ADD", "register:40f0:8", ["const:591940:8", "const:4:8"]]
+ 00591940 ["CALL", null, ["callee:00c5a060:8"]]
- 0056eaa8 bytes daba1994
+ 00591940 bytes c8211b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae21d8439a4a9f93638534fc03e8b7a8"></a>

### [`0056ebe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ebe4.md) → [`00591a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591a7c.md) FUN_00591a7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd560.md) [`00bdd630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd630.md) [`00bdd640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd640.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a080.md) [`00c5a090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ebfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ebe4.md#insn-0056ebfc) · [`0056ec0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ebe4.md#insn-0056ec0c)
- 新版 `00591a94`（命令位置の公開資料なし） · `00591aa4`（命令位置の公開資料なし）

~~~diff
- 0056ebfc ["INT_ADD", "register:40f0:8", ["const:56ebfc:8", "const:4:8"]]
- 0056ebfc ["CALL", null, ["callee:00c59fb0:8"]]
+ 00591a94 ["INT_ADD", "register:40f0:8", ["const:591a94:8", "const:4:8"]]
+ 00591a94 ["CALL", null, ["callee:00c59fb0:8"]]
- 0056ebfc bytes 59ba1994
+ 00591a94 bytes 47211b94
- 0056ec0c ["INT_ADD", "register:40f0:8", ["const:56ec0c:8", "const:4:8"]]
- 0056ec0c ["CALL", null, ["callee:00c5a080:8"]]
+ 00591aa4 ["INT_ADD", "register:40f0:8", ["const:591aa4:8", "const:4:8"]]
+ 00591aa4 ["CALL", null, ["callee:00c5a080:8"]]
- 0056ec0c bytes 89ba1994
+ 00591aa4 bytes 77211b94
~~~


<a id="compare-04e1cc6c3c638f30d0d782982c3e849f"></a>

### [`0056ec44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ec44.md) → [`00591adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591adc.md) FUN_00591adc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd660.md) [`00bdd670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd670.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0b0.md) [`00c5a0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056ec4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ec44.md#insn-0056ec4c)
- 新版 `00591ae4`（命令位置の公開資料なし）

~~~diff
- 0056ec4c ["INT_ADD", "register:40f0:8", ["const:56ec4c:8", "const:4:8"]]
- 0056ec4c ["CALL", null, ["callee:00c5a0b0:8"]]
+ 00591ae4 ["INT_ADD", "register:40f0:8", ["const:591ae4:8", "const:4:8"]]
+ 00591ae4 ["CALL", null, ["callee:00c5a0b0:8"]]
- 0056ec4c bytes 85ba1994
+ 00591ae4 bytes 73211b94
~~~


<a id="compare-2dc960bb8caa2b42b98abaff6c6ed570"></a>

### [`0056f270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f270.md) → [`00592108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592108.md) FUN_00592108

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056f1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f1e8.md) · 呼出先 9件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00592080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592080.md) · 呼出先 9件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f270.md#insn-0056f2b8) · [`0056f2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f270.md#insn-0056f2c4) · [`0056f2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f270.md#insn-0056f2d4)
- 新版 `00592150`（命令位置の公開資料なし） · `0059215c`（命令位置の公開資料なし） · `0059216c`（命令位置の公開資料なし）

~~~diff
- 0056f2b8 ["INT_ADD", "register:40f0:8", ["const:56f2b8:8", "const:4:8"]]
- 0056f2b8 ["CALL", null, ["callee:00c57ad0:8"]]
+ 00592150 ["INT_ADD", "register:40f0:8", ["const:592150:8", "const:4:8"]]
+ 00592150 ["CALL", null, ["callee:00c57ad0:8"]]
- 0056f2b8 bytes 72af1994
+ 00592150 bytes 60161b94
- 0056f2c4 ["INT_ADD", "register:40f0:8", ["const:56f2c4:8", "const:4:8"]]
- 0056f2c4 ["CALL", null, ["callee:00c5a120:8"]]
+ 0059215c ["INT_ADD", "register:40f0:8", ["const:59215c:8", "const:4:8"]]
+ 0059215c ["CALL", null, ["callee:00c5a120:8"]]
- 0056f2c4 bytes 03b91994
+ 0059215c bytes f11f1b94
- 0056f2d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056f2d4 ["INT_ADD", "register:40f0:8", ["const:56f2d4:8", "const:4:8"]]
- 0056f2d4 ["CALLIND", null, ["register:0:8"]]
+ 0059216c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059216c ["INT_ADD", "register:40f0:8", ["const:59216c:8", "const:4:8"]]
+ 0059216c ["CALLIND", null, ["register:0:8"]]
- 0056f2d4 bytes 00013fd6
+ 0059216c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18993a9869b382843b30c83839366dbd"></a>

### [`0056f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f6a0.md) → [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md) FUN_00592538

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0056dee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md) [`0056e8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e8b0.md) [`0056e968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e968.md) [`0056e9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e9b0.md) [`0056ea00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ea00.md) · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f6a0.md)
- 新版 呼出元 7件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) [`00591748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591748.md) [`00591800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591800.md) [`00591848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591848.md) [`00591898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591898.md) · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f6a0.md#insn-0056f6cc)
- 新版 `00592564`（命令位置の公開資料なし）

~~~diff
- 0056f6cc ["INT_ADD", "register:40f0:8", ["const:56f6cc:8", "const:4:8"]]
- 0056f6cc ["CALL", null, ["local:b0:8"]]
+ 00592564 ["INT_ADD", "register:40f0:8", ["const:592564:8", "const:4:8"]]
+ 00592564 ["CALL", null, ["local:b0:8"]]
- 0056f6cc bytes f5ffff97
+ 00592564 bytes f5ffff97
~~~


<a id="compare-6950a0a4fccd5d016429589eb94f373e"></a>

### [`0056f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f7d0.md) → [`00592668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592668.md) FUN_00592668

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f7d0.md#insn-0056f7e0)
- 新版 `00592678`（命令位置の公開資料なし）

~~~diff
- 0056f7e0 ["INT_ADD", "register:40f0:8", ["const:56f7e0:8", "const:4:8"]]
- 0056f7e0 ["CALL", null, ["callee:00555248:8"]]
+ 00592678 ["INT_ADD", "register:40f0:8", ["const:592678:8", "const:4:8"]]
+ 00592678 ["CALL", null, ["callee:00555248:8"]]
- 0056f7e0 bytes f40aff97
+ 00592678 bytes f40aff97
~~~


<a id="compare-c4642727c8762596bc05e3b35cddb61b"></a>

### [`0056f7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f7f8.md) → [`00592690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592690.md) FUN_00592690

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md) [`00bdd540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd540.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f7f8.md#insn-0056f83c) · [`0056f848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f7f8.md#insn-0056f848) · [`0056f870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f7f8.md#insn-0056f870)
- 新版 `005926d4`（命令位置の公開資料なし） · `005926e0`（命令位置の公開資料なし） · `00592708`（命令位置の公開資料なし）

~~~diff
- 0056f83c ["INT_ADD", "register:40f0:8", ["const:56f83c:8", "const:4:8"]]
- 0056f83c ["CALL", null, ["callee:00c57ad0:8"]]
+ 005926d4 ["INT_ADD", "register:40f0:8", ["const:5926d4:8", "const:4:8"]]
+ 005926d4 ["CALL", null, ["callee:00c57ad0:8"]]
- 0056f83c bytes 11ae1994
+ 005926d4 bytes ff141b94
- 0056f848 ["INT_ADD", "register:40f0:8", ["const:56f848:8", "const:4:8"]]
- 0056f848 ["CALL", null, ["callee:00c59f70:8"]]
+ 005926e0 ["INT_ADD", "register:40f0:8", ["const:5926e0:8", "const:4:8"]]
+ 005926e0 ["CALL", null, ["callee:00c59f70:8"]]
- 0056f848 bytes 36b71994
+ 005926e0 bytes 241e1b94
- 0056f870 ["INT_ADD", "register:40f0:8", ["const:56f870:8", "const:4:8"]]
- 0056f870 ["CALL", null, ["callee:00c59f90:8"]]
+ 00592708 ["INT_ADD", "register:40f0:8", ["const:592708:8", "const:4:8"]]
+ 00592708 ["CALL", null, ["callee:00c59f90:8"]]
- 0056f870 bytes 34b71994
+ 00592708 bytes 221e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57fb32fab695a0269f9e037644d417a7"></a>

### [`0056f8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f8ac.md) → [`00592744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592744.md) FUN_00592744

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md) [`00bdd530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd530.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f8ac.md#insn-0056f8dc) · [`0056f8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f8ac.md#insn-0056f8e8) · [`0056f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f8ac.md#insn-0056f8f8)
- 新版 `00592774`（命令位置の公開資料なし） · `00592780`（命令位置の公開資料なし） · `00592790`（命令位置の公開資料なし）

~~~diff
- 0056f8dc ["INT_ADD", "register:40f0:8", ["const:56f8dc:8", "const:4:8"]]
- 0056f8dc ["CALL", null, ["callee:00c57ad0:8"]]
+ 00592774 ["INT_ADD", "register:40f0:8", ["const:592774:8", "const:4:8"]]
+ 00592774 ["CALL", null, ["callee:00c57ad0:8"]]
- 0056f8dc bytes e9ad1994
+ 00592774 bytes d7141b94
- 0056f8e8 ["INT_ADD", "register:40f0:8", ["const:56f8e8:8", "const:4:8"]]
- 0056f8e8 ["CALL", null, ["callee:00c59f70:8"]]
+ 00592780 ["INT_ADD", "register:40f0:8", ["const:592780:8", "const:4:8"]]
+ 00592780 ["CALL", null, ["callee:00c59f70:8"]]
- 0056f8e8 bytes 0eb71994
+ 00592780 bytes fc1d1b94
- 0056f8f8 ["INT_ADD", "register:40f0:8", ["const:56f8f8:8", "const:4:8"]]
- 0056f8f8 ["CALL", null, ["callee:00c59f80:8"]]
+ 00592790 ["INT_ADD", "register:40f0:8", ["const:592790:8", "const:4:8"]]
+ 00592790 ["CALL", null, ["callee:00c59f80:8"]]
- 0056f8f8 bytes 0eb71994
+ 00592790 bytes fc1d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa2cb62c3475cc31c71615ebf2f72236"></a>

### [`0056fa58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fa58.md) → [`005928f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928f0.md) FUN_005928f0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fa58.md#insn-0056fa68)
- 新版 `00592900`（命令位置の公開資料なし）

~~~diff
- 0056fa68 ["INT_ADD", "register:40f0:8", ["const:56fa68:8", "const:4:8"]]
- 0056fa68 ["CALL", null, ["callee:00555248:8"]]
+ 00592900 ["INT_ADD", "register:40f0:8", ["const:592900:8", "const:4:8"]]
+ 00592900 ["CALL", null, ["callee:00555248:8"]]
- 0056fa68 bytes 520aff97
+ 00592900 bytes 520aff97
~~~


<a id="compare-17cda4fc9e85a066cb1111d3e203e29d"></a>

### [`0056fb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb84.md) → [`00592a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a1c.md) FUN_00592a1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdd6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd6b0.md) [`00bdd730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd730.md) [`00bdd740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a100.md) [`00c5a180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a180.md) [`00c5a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb84.md#insn-0056fbb0) · [`0056fbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb84.md#insn-0056fbc8) · [`0056fbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb84.md#insn-0056fbdc)
- 新版 `00592a48`（命令位置の公開資料なし） · `00592a60`（命令位置の公開資料なし） · `00592a74`（命令位置の公開資料なし）

~~~diff
- 0056fbb0 ["INT_ADD", "register:40f0:8", ["const:56fbb0:8", "const:4:8"]]
- 0056fbb0 ["CALL", null, ["callee:00c5a100:8"]]
+ 00592a48 ["INT_ADD", "register:40f0:8", ["const:592a48:8", "const:4:8"]]
+ 00592a48 ["CALL", null, ["callee:00c5a100:8"]]
- 0056fbb0 bytes c0b61994
+ 00592a48 bytes ae1d1b94
- 0056fbc8 ["INT_ADD", "register:40f0:8", ["const:56fbc8:8", "const:4:8"]]
- 0056fbc8 ["CALL", null, ["callee:00c5a180:8"]]
+ 00592a60 ["INT_ADD", "register:40f0:8", ["const:592a60:8", "const:4:8"]]
+ 00592a60 ["CALL", null, ["callee:00c5a180:8"]]
- 0056fbc8 bytes dab61994
+ 00592a60 bytes c81d1b94
- 0056fbdc ["INT_ADD", "register:40f0:8", ["const:56fbdc:8", "const:4:8"]]
- 0056fbdc ["CALL", null, ["callee:00c5a190:8"]]
+ 00592a74 ["INT_ADD", "register:40f0:8", ["const:592a74:8", "const:4:8"]]
+ 00592a74 ["CALL", null, ["callee:00c5a190:8"]]
- 0056fbdc bytes d9b61994
+ 00592a74 bytes c71d1b94
~~~


<a id="compare-85cf7985ccd50a61192b7e2f4ea6b444"></a>

### [`0056fbf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fbf8.md) → [`00592a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a90.md) FUN_00592a90

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd6b0.md) [`00bdd750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd750.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a100.md) [`00c5a1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a1a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fbf8.md#insn-0056fc20) · [`0056fc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fbf8.md#insn-0056fc30) · [`0056fc3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fbf8.md#insn-0056fc3c)
- 新版 `00592ab8`（命令位置の公開資料なし） · `00592ac8`（命令位置の公開資料なし） · `00592ad4`（命令位置の公開資料なし）

~~~diff
- 0056fc20 ["INT_ADD", "register:40f0:8", ["const:56fc20:8", "const:4:8"]]
- 0056fc20 ["CALL", null, ["callee:00c5a100:8"]]
+ 00592ab8 ["INT_ADD", "register:40f0:8", ["const:592ab8:8", "const:4:8"]]
+ 00592ab8 ["CALL", null, ["callee:00c5a100:8"]]
- 0056fc20 bytes a4b61994
+ 00592ab8 bytes 921d1b94
- 0056fc30 ["INT_ADD", "register:40f0:8", ["const:56fc30:8", "const:4:8"]]
- 0056fc30 ["CALL", null, ["callee:00c5a1a0:8"]]
+ 00592ac8 ["INT_ADD", "register:40f0:8", ["const:592ac8:8", "const:4:8"]]
+ 00592ac8 ["CALL", null, ["callee:00c5a1a0:8"]]
- 0056fc30 bytes c8b61994
+ 00592ac8 bytes b61d1b94
- 0056fc3c ["INT_ADD", "register:40f0:8", ["const:56fc3c:8", "const:4:8"]]
- 0056fc3c ["CALL", null, ["callee:00c5a100:8"]]
+ 00592ad4 ["INT_ADD", "register:40f0:8", ["const:592ad4:8", "const:4:8"]]
+ 00592ad4 ["CALL", null, ["callee:00c5a100:8"]]
- 0056fc3c bytes 9db61994
+ 00592ad4 bytes 8b1d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-938cd90827098392bfc3eed1409212db"></a>

### [`0056fc68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fc68.md) → [`00592b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b00.md) FUN_00592b00

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fc68.md#insn-0056fc78)
- 新版 `00592b10`（命令位置の公開資料なし）

~~~diff
- 0056fc78 ["INT_ADD", "register:40f0:8", ["const:56fc78:8", "const:4:8"]]
- 0056fc78 ["CALL", null, ["callee:00555248:8"]]
+ 00592b10 ["INT_ADD", "register:40f0:8", ["const:592b10:8", "const:4:8"]]
+ 00592b10 ["CALL", null, ["callee:00555248:8"]]
- 0056fc78 bytes ce09ff97
+ 00592b10 bytes ce09ff97
~~~


<a id="compare-40cbd6973d96e7bfc3bfeceb96a6f8ee"></a>

### [`0056fd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fd8c.md) → [`00592c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c24.md) FUN_00592c24

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fd8c.md#insn-0056fda8) · [`0056fdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fd8c.md#insn-0056fdc8)
- 新版 `00592c40`（命令位置の公開資料なし） · `00592c60`（命令位置の公開資料なし）

~~~diff
- 0056fda8 ["INT_ADD", "register:40f0:8", ["const:56fda8:8", "const:4:8"]]
- 0056fda8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00592c40 ["INT_ADD", "register:40f0:8", ["const:592c40:8", "const:4:8"]]
+ 00592c40 ["CALL", null, ["callee:00c538e0:8"]]
- 0056fda8 bytes 3a9c1994
+ 00592c40 bytes 28031b94
- 0056fdc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056fdc8 ["INT_ADD", "register:40f0:8", ["const:56fdc8:8", "const:4:8"]]
- 0056fdc8 ["CALLIND", null, ["register:0:8"]]
+ 00592c60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00592c60 ["INT_ADD", "register:40f0:8", ["const:592c60:8", "const:4:8"]]
+ 00592c60 ["CALLIND", null, ["register:0:8"]]
- 0056fdc8 bytes 00013fd6
+ 00592c60 bytes 00013fd6
~~~


