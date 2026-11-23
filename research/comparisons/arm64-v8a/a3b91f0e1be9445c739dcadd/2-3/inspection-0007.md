# v15.7.4 → v16.0.0 · 要調査の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-7330955ec708d0588ea92db29afd6385"></a>

### [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) → [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) FUN_004d78c8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004b47ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) · 呼出先 11件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) [`00495c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) [`004af240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af240.md) [`004af83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af83c.md)
- 新版 呼出元 2件 [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 11件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004d20d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d20d8.md) [`004d26d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d26d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md#insn-004b4a84) · [`004b4a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md#insn-004b4a9c) · [`004b4b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md#insn-004b4b0c)
- 新版 `004d791c`（命令位置の公開資料なし） · `004d7934`（命令位置の公開資料なし） · `004d79a4`（命令位置の公開資料なし）

~~~diff
- 004b4a84 ["INT_ADD", "register:40f0:8", ["const:4b4a84:8", "const:4:8"]]
- 004b4a84 ["CALL", null, ["callee:004b8774:8"]]
+ 004d791c ["INT_ADD", "register:40f0:8", ["const:4d791c:8", "const:4:8"]]
+ 004d791c ["CALL", null, ["callee:004b8774:8"]]
- 004b4a84 bytes 9683ff97
+ 004d791c bytes 9683ff97
- 004b4a9c ["INT_ADD", "register:40f0:8", ["const:4b4a9c:8", "const:4:8"]]
- 004b4a9c ["CALL", null, ["callee:00c57c90:8"]]
+ 004d7934 ["INT_ADD", "register:40f0:8", ["const:4d7934:8", "const:4:8"]]
+ 004d7934 ["CALL", null, ["callee:00c57c90:8"]]
- 004b4a9c bytes e9991c94
+ 004d7934 bytes d7001e94
- 004b4b0c ["INT_ADD", "register:40f0:8", ["const:4b4b0c:8", "const:4:8"]]
- 004b4b0c ["CALL", null, ["callee:004b890c:8"]]
+ 004d79a4 ["INT_ADD", "register:40f0:8", ["const:4d79a4:8", "const:4:8"]]
+ 004d79a4 ["CALL", null, ["callee:004b890c:8"]]
- 004b4b0c bytes da83ff97
+ 004d79a4 bytes da83ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747091a423d666e9849e92c28800fbdd"></a>

### [`004b4c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4c94.md) → [`004d7b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7b2c.md) FUN_004d7b2c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004bc804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md) [`004bd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 2件 [`004df69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4c94.md#insn-004b4ef4)
- 新版 `004d7d8c`（命令位置の公開資料なし）

~~~diff
- 004b4ef4 ["INT_ADD", "register:40f0:8", ["const:4b4ef4:8", "const:4:8"]]
- 004b4ef4 ["CALL", null, ["callee:00c57b40:8"]]
+ 004d7d8c ["INT_ADD", "register:40f0:8", ["const:4d7d8c:8", "const:4:8"]]
+ 004d7d8c ["CALL", null, ["callee:00c57b40:8"]]
- 004b4ef4 bytes 7f981c94
+ 004d7d8c bytes 6dff1d94
~~~


<a id="compare-5440eea162f6041dc81ae82e04c822cc"></a>

### [`004b6540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6540.md) → [`004d93d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d93d8.md) _ZN5Botan19generate_dsa_primesERNS_21RandomNumberGeneratorERNS_6BigIntES3_mm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdc460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc460.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b6594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6540.md#insn-004b6594) · [`004b65b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6540.md#insn-004b65b0) · [`004b65cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6540.md#insn-004b65cc)
- 新版 `004d942c`（命令位置の公開資料なし） · `004d9448`（命令位置の公開資料なし） · `004d9464`（命令位置の公開資料なし）

~~~diff
- 004b6594 ["INT_ADD", "register:40f0:8", ["const:4b6594:8", "const:4:8"]]
- 004b6594 ["CALL", null, ["callee:00c57a90:8"]]
+ 004d942c ["INT_ADD", "register:40f0:8", ["const:4d942c:8", "const:4:8"]]
+ 004d942c ["CALL", null, ["callee:00c57a90:8"]]
- 004b6594 bytes ab921c94
+ 004d942c bytes 99f91d94
- 004b65b0 ["INT_ADD", "register:40f0:8", ["const:4b65b0:8", "const:4:8"]]
- 004b65b0 ["CALL", null, ["callee:00c57c90:8"]]
+ 004d9448 ["INT_ADD", "register:40f0:8", ["const:4d9448:8", "const:4:8"]]
+ 004d9448 ["CALL", null, ["callee:00c57c90:8"]]
- 004b65b0 bytes 24931c94
+ 004d9448 bytes 12fa1d94
- 004b65cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004b65cc ["INT_ADD", "register:40f0:8", ["const:4b65cc:8", "const:4:8"]]
- 004b65cc ["CALLIND", null, ["register:0:8"]]
+ 004d9464 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004d9464 ["INT_ADD", "register:40f0:8", ["const:4d9464:8", "const:4:8"]]
+ 004d9464 ["CALLIND", null, ["register:0:8"]]
- 004b65cc bytes 00013fd6
+ 004d9464 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e9cea344cbbc1c4408c83f7639f8eab"></a>

### [`004b97b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b97b0.md) → [`004dc648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc648.md) _ZN5Botan29normalized_montgomery_inverseERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdbc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc80.md) [`00bdc550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc550.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c586d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586d0.md) [`00c58fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b97e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b97b0.md#insn-004b97e8) · [`004b9830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b97b0.md#insn-004b9830)
- 新版 `004dc680`（命令位置の公開資料なし） · `004dc6c8`（命令位置の公開資料なし）

~~~diff
- 004b97e8 ["INT_ADD", "register:40f0:8", ["const:4b97e8:8", "const:4:8"]]
- 004b97e8 ["CALL", null, ["callee:00c58fa0:8"]]
+ 004dc680 ["INT_ADD", "register:40f0:8", ["const:4dc680:8", "const:4:8"]]
+ 004dc680 ["CALL", null, ["callee:00c58fa0:8"]]
- 004b97e8 bytes 5a8b1c94
+ 004dc680 bytes 48f21d94
- 004b9830 ["INT_ADD", "register:40f0:8", ["const:4b9830:8", "const:4:8"]]
- 004b9830 ["CALL", null, ["callee:00c586d0:8"]]
+ 004dc6c8 ["INT_ADD", "register:40f0:8", ["const:4dc6c8:8", "const:4:8"]]
+ 004dc6c8 ["CALL", null, ["callee:00c586d0:8"]]
- 004b9830 bytes 14891c94
+ 004dc6c8 bytes 02f01d94
~~~


<a id="compare-9fad2bbbb4c873ed63782d22656dad4d"></a>

### [`004bbb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbb44.md) → [`004de9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de9dc.md) _ZN5Botan9Power_ModaSERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bbb6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbb44.md#insn-004bbb6c) · [`004bbb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbb44.md#insn-004bbb88)
- 新版 `004dea04`（命令位置の公開資料なし） · `004dea20`（命令位置の公開資料なし）

~~~diff
- 004bbb6c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bbb6c ["INT_ADD", "register:40f0:8", ["const:4bbb6c:8", "const:4:8"]]
- 004bbb6c ["CALLIND", null, ["register:0:8"]]
+ 004dea04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004dea04 ["INT_ADD", "register:40f0:8", ["const:4dea04:8", "const:4:8"]]
+ 004dea04 ["CALLIND", null, ["register:0:8"]]
- 004bbb6c bytes 00013fd6
+ 004dea04 bytes 00013fd6
- 004bbb88 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bbb88 ["INT_ADD", "register:40f0:8", ["const:4bbb88:8", "const:4:8"]]
- 004bbb88 ["CALLIND", null, ["register:0:8"]]
+ 004dea20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dea20 ["INT_ADD", "register:40f0:8", ["const:4dea20:8", "const:4:8"]]
+ 004dea20 ["CALLIND", null, ["register:0:8"]]
- 004bbb88 bytes 20013fd6
+ 004dea20 bytes 20013fd6
~~~


<a id="compare-0d6ff56de51a740c58955106b7f56c81"></a>

### [`004bc02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc02c.md) → [`004deec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004deec4.md) FUN_004deec4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc02c.md#insn-004bc058)
- 新版 `004deef0`（命令位置の公開資料なし）

~~~diff
- 004bc058 ["INT_ADD", "register:40f0:8", ["const:4bc058:8", "const:4:8"]]
- 004bc058 ["CALL", null, ["callee:0054369c:8"]]
+ 004deef0 ["INT_ADD", "register:40f0:8", ["const:4deef0:8", "const:4:8"]]
+ 004deef0 ["CALL", null, ["callee:0054369c:8"]]
- 004bc058 bytes eb910194
+ 004deef0 bytes eb910194
~~~


<a id="compare-94245d66a17459eacd0afbb8b9879aae"></a>

### [`004bc748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc748.md) → [`004df5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df5e0.md) FUN_004df5e0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc748.md#insn-004bc774)
- 新版 `004df60c`（命令位置の公開資料なし）

~~~diff
- 004bc774 ["INT_ADD", "register:40f0:8", ["const:4bc774:8", "const:4:8"]]
- 004bc774 ["CALL", null, ["callee:0054369c:8"]]
+ 004df60c ["INT_ADD", "register:40f0:8", ["const:4df60c:8", "const:4:8"]]
+ 004df60c ["CALL", null, ["callee:0054369c:8"]]
- 004bc774 bytes 24900194
+ 004df60c bytes 24900194
~~~


<a id="compare-79227eb5defc013fdce7e27bb24d15f0"></a>

### [`004bf520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf520.md) → [`004e23b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e23b8.md) _ZN5Botan13pbes2_encryptERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bf554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf520.md#insn-004bf554) · [`004bf578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf520.md#insn-004bf578)
- 新版 `004e23ec`（命令位置の公開資料なし） · `004e2410`（命令位置の公開資料なし）

~~~diff
- 004bf554 ["INT_ADD", "register:40f0:8", ["const:4bf554:8", "const:4:8"]]
- 004bf554 ["CALL", null, ["callee:004e2414:8"]]
+ 004e23ec ["INT_ADD", "register:40f0:8", ["const:4e23ec:8", "const:4:8"]]
+ 004e23ec ["CALL", null, ["callee:004e2414:8"]]
- 004bf554 bytes 0a000094
+ 004e23ec bytes 0a000094
- 004bf578 ["INT_ADD", "register:40f0:8", ["const:4bf578:8", "const:4:8"]]
- 004bf578 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004e2410 ["INT_ADD", "register:40f0:8", ["const:4e2410:8", "const:4:8"]]
+ 004e2410 ["CALL", null, ["callee:00c57ae0:8"]]
- 004bf578 bytes c66e1c94
+ 004e2410 bytes b4d51d94
~~~


<a id="compare-ea4d720f0fd87a0303c8acb24afac077"></a>

### [`004c0520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0520.md) → [`004e33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e33b8.md) _ZN5Botan18pbes2_encrypt_msecERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0520.md#insn-004c054c) · [`004c057c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0520.md#insn-004c057c)
- 新版 `004e33e4`（命令位置の公開資料なし） · `004e3414`（命令位置の公開資料なし）

~~~diff
- 004c054c ["INT_ADD", "register:40f0:8", ["const:4c054c:8", "const:4:8"]]
- 004c054c ["CALL", null, ["callee:004e2414:8"]]
+ 004e33e4 ["INT_ADD", "register:40f0:8", ["const:4e33e4:8", "const:4:8"]]
+ 004e33e4 ["CALL", null, ["callee:004e2414:8"]]
- 004c054c bytes 0cfcff97
+ 004e33e4 bytes 0cfcff97
- 004c057c ["INT_ADD", "register:40f0:8", ["const:4c057c:8", "const:4:8"]]
- 004c057c ["CALL", null, ["callee:00c57ae0:8"]]
+ 004e3414 ["INT_ADD", "register:40f0:8", ["const:4e3414:8", "const:4:8"]]
+ 004e3414 ["CALL", null, ["callee:00c57ae0:8"]]
- 004c057c bytes c56a1c94
+ 004e3414 bytes b3d11d94
~~~


<a id="compare-b50d68b22eb9ae5fe375b913fd0c3f62"></a>

### [`004c0580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0580.md) → [`004e3418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3418.md) FUN_004e3418

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c059c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0580.md#insn-004c059c) · [`004c05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0580.md#insn-004c05ac)
- 新版 `004e3434`（命令位置の公開資料なし） · `004e3444`（命令位置の公開資料なし）

~~~diff
- 004c059c ["INT_ADD", "register:40f0:8", ["const:4c059c:8", "const:4:8"]]
- 004c059c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004e3434 ["INT_ADD", "register:40f0:8", ["const:4e3434:8", "const:4:8"]]
+ 004e3434 ["CALL", null, ["callee:00c57ab0:8"]]
- 004c059c bytes b16a1c94
+ 004e3434 bytes 9fd11d94
- 004c05ac ["INT_ADD", "register:40f0:8", ["const:4c05ac:8", "const:4:8"]]
- 004c05ac ["CALL", null, ["callee:00c57ab0:8"]]
+ 004e3444 ["INT_ADD", "register:40f0:8", ["const:4e3444:8", "const:4:8"]]
+ 004e3444 ["CALL", null, ["callee:00c57ab0:8"]]
- 004c05ac bytes ad6a1c94
+ 004e3444 bytes 9bd11d94
~~~


<a id="compare-de2adf98e95d9c4cf32367ab3a1c8f59"></a>

### [`004c177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c177c.md) → [`004e4614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4614.md) _ZNK5Botan5PBKDF16pbkdf_iterationsEmRKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKhmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdc5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c59030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c17b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c177c.md#insn-004c17b4) · [`004c17d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c177c.md#insn-004c17d4)
- 新版 `004e464c`（命令位置の公開資料なし） · `004e466c`（命令位置の公開資料なし）

~~~diff
- 004c17b4 ["INT_ADD", "register:40f0:8", ["const:4c17b4:8", "const:4:8"]]
- 004c17b4 ["CALL", null, ["callee:004b34c8:8"]]
+ 004e464c ["INT_ADD", "register:40f0:8", ["const:4e464c:8", "const:4:8"]]
+ 004e464c ["CALL", null, ["callee:004b34c8:8"]]
- 004c17b4 bytes 9f3bff97
+ 004e464c bytes 9f3bff97
- 004c17d4 ["INT_ADD", "register:40f0:8", ["const:4c17d4:8", "const:4:8"]]
- 004c17d4 ["CALL", null, ["callee:00c59030:8"]]
+ 004e466c ["INT_ADD", "register:40f0:8", ["const:4e466c:8", "const:4:8"]]
+ 004e466c ["CALL", null, ["callee:00c59030:8"]]
- 004c17d4 bytes 836b1c94
+ 004e466c bytes 71d21d94
~~~


<a id="compare-8174127be5f0602389dcda0ab17fd702"></a>

### [`004c1d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1d14.md) → [`004e4bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4bac.md) _ZN5Botan5PBKDF9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004c1e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1e78.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004e4d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4d10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c1d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1d14.md#insn-004c1d84) · [`004c1d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1d14.md#insn-004c1d94) · [`004c1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1d14.md#insn-004c1dd0)
- 新版 `004e4c1c`（命令位置の公開資料なし） · `004e4c2c`（命令位置の公開資料なし） · `004e4c68`（命令位置の公開資料なし）

~~~diff
- 004c1d84 ["INT_ADD", "register:40f0:8", ["const:4c1d84:8", "const:4:8"]]
- 004c1d84 ["CALL", null, ["callee:00473500:8"]]
+ 004e4c1c ["INT_ADD", "register:40f0:8", ["const:4e4c1c:8", "const:4:8"]]
+ 004e4c1c ["CALL", null, ["callee:00473500:8"]]
- 004c1d84 bytes 393afe97
+ 004e4c1c bytes 393afe97
- 004c1d94 ["INT_ADD", "register:40f0:8", ["const:4c1d94:8", "const:4:8"]]
- 004c1d94 ["CALL", null, ["callee:004e4d10:8"]]
+ 004e4c2c ["INT_ADD", "register:40f0:8", ["const:4e4c2c:8", "const:4:8"]]
+ 004e4c2c ["CALL", null, ["callee:004e4d10:8"]]
- 004c1d94 bytes 39000094
+ 004e4c2c bytes 39000094
- 004c1dd0 ["INT_ADD", "register:40f0:8", ["const:4c1dd0:8", "const:4:8"]]
- 004c1dd0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004e4c68 ["INT_ADD", "register:40f0:8", ["const:4e4c68:8", "const:4:8"]]
+ 004e4c68 ["CALL", null, ["callee:00c57ab0:8"]]
- 004c1dd0 bytes a4641c94
+ 004e4c68 bytes 92cb1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b15142f888d34b3c9a036d7d43e17bd"></a>

### [`004c1e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1e78.md) → [`004e4d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4d10.md) FUN_004e4d10

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c1d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1d14.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5d0.md)
- 新版 呼出元 1件 [`004e4bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4bac.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c1ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1e78.md#insn-004c1ec8) · [`004c1edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1e78.md#insn-004c1edc) · [`004c1ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1e78.md#insn-004c1ef8)
- 新版 `004e4d60`（命令位置の公開資料なし） · `004e4d74`（命令位置の公開資料なし） · `004e4d90`（命令位置の公開資料なし）

~~~diff
- 004c1ec8 ["INT_ADD", "register:40f0:8", ["const:4c1ec8:8", "const:4:8"]]
- 004c1ec8 ["CALL", null, ["callee:00540d3c:8"]]
+ 004e4d60 ["INT_ADD", "register:40f0:8", ["const:4e4d60:8", "const:4:8"]]
+ 004e4d60 ["CALL", null, ["callee:00540d3c:8"]]
- 004c1ec8 bytes f76f0194
+ 004e4d60 bytes f76f0194
- 004c1edc ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1edc ["INT_ADD", "register:40f0:8", ["const:4c1edc:8", "const:4:8"]]
- 004c1edc ["CALLIND", null, ["register:0:8"]]
+ 004e4d74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e4d74 ["INT_ADD", "register:40f0:8", ["const:4e4d74:8", "const:4:8"]]
+ 004e4d74 ["CALLIND", null, ["register:0:8"]]
- 004c1edc bytes 00013fd6
+ 004e4d74 bytes 00013fd6
- 004c1ef8 ["INT_ADD", "register:40f0:8", ["const:4c1ef8:8", "const:4:8"]]
- 004c1ef8 ["CALL", null, ["callee:00c59020:8"]]
+ 004e4d90 ["INT_ADD", "register:40f0:8", ["const:4e4d90:8", "const:4:8"]]
+ 004e4d90 ["CALL", null, ["callee:00c59020:8"]]
- 004c1ef8 bytes b6691c94
+ 004e4d90 bytes a4d01d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e043086fd8220fd110f865d9497311c"></a>

### [`004c1fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1fb8.md) → [`004e4e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e50.md) _ZNK5Botan5PBKDF11pbkdf_timedEPhmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKhmNS2_6chrono8durationIxNS2_5ratioIL

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c1fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1fb8.md#insn-004c1fd8)
- 新版 `004e4e70`（命令位置の公開資料なし）

~~~diff
- 004c1fd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1fd8 ["INT_ADD", "register:40f0:8", ["const:4c1fd8:8", "const:4:8"]]
- 004c1fd8 ["CALLIND", null, ["register:0:8"]]
+ 004e4e70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e4e70 ["INT_ADD", "register:40f0:8", ["const:4e4e70:8", "const:4:8"]]
+ 004e4e70 ["CALLIND", null, ["register:0:8"]]
- 004c1fd8 bytes 00013fd6
+ 004e4e70 bytes 00013fd6
~~~


<a id="compare-fa11a27381b74d9089520232284a5725"></a>

### [`004c2190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2190.md) → [`004e5028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5028.md) _ZNK5Botan5PBKDF11pbkdf_timedEmRKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKhmNS1_6chrono8durationIxNS1_5ratioILl1

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c21cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2190.md#insn-004c21cc) · [`004c21f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2190.md#insn-004c21f8)
- 新版 `004e5064`（命令位置の公開資料なし） · `004e5090`（命令位置の公開資料なし）

~~~diff
- 004c21cc ["INT_ADD", "register:40f0:8", ["const:4c21cc:8", "const:4:8"]]
- 004c21cc ["CALL", null, ["callee:004b34c8:8"]]
+ 004e5064 ["INT_ADD", "register:40f0:8", ["const:4e5064:8", "const:4:8"]]
+ 004e5064 ["CALL", null, ["callee:004b34c8:8"]]
- 004c21cc bytes 1939ff97
+ 004e5064 bytes 1939ff97
- 004c21f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c21f8 ["INT_ADD", "register:40f0:8", ["const:4c21f8:8", "const:4:8"]]
- 004c21f8 ["CALLIND", null, ["register:0:8"]]
+ 004e5090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004e5090 ["INT_ADD", "register:40f0:8", ["const:4e5090:8", "const:4:8"]]
+ 004e5090 ["CALLIND", null, ["register:0:8"]]
- 004c21f8 bytes 00013fd6
+ 004e5090 bytes 00013fd6
~~~


<a id="compare-7ade825464bf986f7cdc09362d359df6"></a>

### [`004c43dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c43dc.md) → [`004e7274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7274.md) _ZN5Botan13hash_for_emsaERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6f0.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd40.md) [`00bdbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbef0.md)
- 新版 呼出元 1件 [`00c59140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59140.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58790.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c4424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c43dc.md#insn-004c4424) · [`004c4430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c43dc.md#insn-004c4430) · [`004c4440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c43dc.md#insn-004c4440)
- 新版 `004e72bc`（命令位置の公開資料なし） · `004e72c8`（命令位置の公開資料なし） · `004e72d8`（命令位置の公開資料なし）

~~~diff
- 004c4424 ["INT_ADD", "register:40f0:8", ["const:4c4424:8", "const:4:8"]]
- 004c4424 ["CALL", null, ["callee:0043bae0:8"]]
+ 004e72bc ["INT_ADD", "register:40f0:8", ["const:4e72bc:8", "const:4:8"]]
+ 004e72bc ["CALL", null, ["callee:0043bae0:8"]]
- 004c4424 bytes ef52fd97
+ 004e72bc bytes 0952fd97
- 004c4430 ["INT_ADD", "register:40f0:8", ["const:4c4430:8", "const:4:8"]]
- 004c4430 ["CALL", null, ["callee:00c58940:8"]]
+ 004e72c8 ["INT_ADD", "register:40f0:8", ["const:4e72c8:8", "const:4:8"]]
+ 004e72c8 ["CALL", null, ["callee:00c58940:8"]]
- 004c4430 bytes b05e1c94
+ 004e72c8 bytes 9ec51d94
- 004c4440 ["INT_ADD", "register:40f0:8", ["const:4c4440:8", "const:4:8"]]
- 004c4440 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004e72d8 ["INT_ADD", "register:40f0:8", ["const:4e72d8:8", "const:4:8"]]
+ 004e72d8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004c4440 bytes 085b1c94
+ 004e72d8 bytes f6c11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc06dd2aa527f5773d8679dd822bef4f"></a>

### [`004c45bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md) → [`004e7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) FUN_004e7454

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052c558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00522300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522300.md) [`0052259c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/0052259c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0054f3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00545198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md) [`00545434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545434.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c460c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md#insn-004c460c) · [`004c463c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md#insn-004c463c) · [`004c4658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md#insn-004c4658)
- 新版 `004e74a4`（命令位置の公開資料なし） · `004e74d4`（命令位置の公開資料なし） · `004e74f0`（命令位置の公開資料なし）

~~~diff
- 004c460c ["INT_ADD", "register:40f0:8", ["const:4c460c:8", "const:4:8"]]
- 004c460c ["CALL", null, ["callee:0043bb64:8"]]
+ 004e74a4 ["INT_ADD", "register:40f0:8", ["const:4e74a4:8", "const:4:8"]]
+ 004e74a4 ["CALL", null, ["callee:0043bb64:8"]]
- 004c460c bytes 9652fd97
+ 004e74a4 bytes b051fd97
- 004c463c ["INT_ADD", "register:40f0:8", ["const:4c463c:8", "const:4:8"]]
- 004c463c ["CALL", null, ["callee:00545198:8"]]
+ 004e74d4 ["INT_ADD", "register:40f0:8", ["const:4e74d4:8", "const:4:8"]]
+ 004e74d4 ["CALL", null, ["callee:00545198:8"]]
- 004c463c bytes 31770194
+ 004e74d4 bytes 31770194
- 004c4658 ["INT_ADD", "register:40f0:8", ["const:4c4658:8", "const:4:8"]]
- 004c4658 ["CALL", null, ["callee:00545434:8"]]
+ 004e74f0 ["INT_ADD", "register:40f0:8", ["const:4e74f0:8", "const:4:8"]]
+ 004e74f0 ["CALL", null, ["callee:00545434:8"]]
- 004c4658 bytes d1770194
+ 004e74f0 bytes d1770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08a7374030f216a117965493fa0435f5"></a>

### [`004c46d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c46d8.md) → [`004e7570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7570.md) FUN_004e7570

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c4724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c46d8.md#insn-004c4724) · [`004c4734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c46d8.md#insn-004c4734)
- 新版 `004e75bc`（命令位置の公開資料なし） · `004e75cc`（命令位置の公開資料なし）

~~~diff
- 004c4724 ["INT_ADD", "register:40f0:8", ["const:4c4724:8", "const:4:8"]]
- 004c4724 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004e75bc ["INT_ADD", "register:40f0:8", ["const:4e75bc:8", "const:4:8"]]
+ 004e75bc ["CALL", null, ["callee:00c57ab0:8"]]
- 004c4724 bytes 4f5a1c94
+ 004e75bc bytes 3dc11d94
- 004c4734 ["INT_ADD", "register:40f0:8", ["const:4c4734:8", "const:4:8"]]
- 004c4734 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004e75cc ["INT_ADD", "register:40f0:8", ["const:4e75cc:8", "const:4:8"]]
+ 004e75cc ["CALL", null, ["callee:00c57ab0:8"]]
- 004c4734 bytes 4b5a1c94
+ 004e75cc bytes 39c11d94
~~~


<a id="compare-cf0fbcd7983b61de5724df85ebd22f48"></a>

### [`004c5e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5e50.md) → [`004e8ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8ce8.md) _ZN5Botan18create_private_keyERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS_21RandomNumberGeneratorES8_S8_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md) [`00bdc760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c583f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583f0.md) [`00c591b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c5ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5e50.md#insn-004c5ee0) · [`004c5ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5e50.md#insn-004c5ef4) · [`004c5f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5e50.md#insn-004c5f08)
- 新版 `004e8d78`（命令位置の公開資料なし） · `004e8d8c`（命令位置の公開資料なし） · `004e8da0`（命令位置の公開資料なし）

~~~diff
- 004c5ee0 ["INT_ADD", "register:40f0:8", ["const:4c5ee0:8", "const:4:8"]]
- 004c5ee0 ["CALL", null, ["callee:00c583f0:8"]]
+ 004e8d78 ["INT_ADD", "register:40f0:8", ["const:4e8d78:8", "const:4:8"]]
+ 004e8d78 ["CALL", null, ["callee:00c583f0:8"]]
- 004c5ee0 bytes b0561c94
+ 004e8d78 bytes 9ebd1d94
- 004c5ef4 ["INT_ADD", "register:40f0:8", ["const:4c5ef4:8", "const:4:8"]]
- 004c5ef4 ["CALL", null, ["callee:00c57a90:8"]]
+ 004e8d8c ["INT_ADD", "register:40f0:8", ["const:4e8d8c:8", "const:4:8"]]
+ 004e8d8c ["CALL", null, ["callee:00c57a90:8"]]
- 004c5ef4 bytes 53541c94
+ 004e8d8c bytes 41bb1d94
- 004c5f08 ["INT_ADD", "register:40f0:8", ["const:4c5f08:8", "const:4:8"]]
- 004c5f08 ["CALL", null, ["callee:00c591b0:8"]]
+ 004e8da0 ["INT_ADD", "register:40f0:8", ["const:4e8da0:8", "const:4:8"]]
+ 004e8da0 ["CALL", null, ["callee:00c591b0:8"]]
- 004c5f08 bytes 165a1c94
+ 004e8da0 bytes 04c11d94
~~~


<a id="compare-3f6a318b78a37759afae8508f7e2e888"></a>

### [`004c6b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c6/004c6b50.md) → [`004e99e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e99e8.md) _ZN5Botan26probe_provider_private_keyERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_6vectorIS6_NS4_IS6_EEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c6bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c6/004c6b50.md#insn-004c6bf4) · [`004c6c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c6/004c6b50.md#insn-004c6c08)
- 新版 `004e9a8c`（命令位置の公開資料なし） · `004e9aa0`（命令位置の公開資料なし）

~~~diff
- 004c6bf4 ["INT_ADD", "register:40f0:8", ["const:4c6bf4:8", "const:4:8"]]
- 004c6bf4 ["CALL", null, ["callee:0043bae0:8"]]
+ 004e9a8c ["INT_ADD", "register:40f0:8", ["const:4e9a8c:8", "const:4:8"]]
+ 004e9a8c ["CALL", null, ["callee:0043bae0:8"]]
- 004c6bf4 bytes fb48fd97
+ 004e9a8c bytes 1548fd97
- 004c6c08 ["INT_ADD", "register:40f0:8", ["const:4c6c08:8", "const:4:8"]]
- 004c6c08 ["CALL", null, ["callee:00540d3c:8"]]
+ 004e9aa0 ["INT_ADD", "register:40f0:8", ["const:4e9aa0:8", "const:4:8"]]
+ 004e9aa0 ["CALL", null, ["callee:00540d3c:8"]]
- 004c6c08 bytes a75c0194
+ 004e9aa0 bytes a75c0194
~~~


<a id="compare-b9c83f85964a51ed38cb42ab0d622f53"></a>

### [`004c7138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7138.md) → [`004e9fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e9/004e9fd0.md) _ZNK5Botan10Public_Key7get_oidEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c716c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7138.md#insn-004c716c) · [`004c7178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7138.md#insn-004c7178) · [`004c7188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7138.md#insn-004c7188)
- 新版 `004ea004`（命令位置の公開資料なし） · `004ea010`（命令位置の公開資料なし） · `004ea020`（命令位置の公開資料なし）

~~~diff
- 004c716c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c716c ["INT_ADD", "register:40f0:8", ["const:4c716c:8", "const:4:8"]]
- 004c716c ["CALLIND", null, ["register:0:8"]]
+ 004ea004 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea004 ["INT_ADD", "register:40f0:8", ["const:4ea004:8", "const:4:8"]]
+ 004ea004 ["CALLIND", null, ["register:0:8"]]
- 004c716c bytes 20013fd6
+ 004ea004 bytes 20013fd6
- 004c7178 ["INT_ADD", "register:40f0:8", ["const:4c7178:8", "const:4:8"]]
- 004c7178 ["CALL", null, ["callee:00c58280:8"]]
+ 004ea010 ["INT_ADD", "register:40f0:8", ["const:4ea010:8", "const:4:8"]]
+ 004ea010 ["CALL", null, ["callee:00c58280:8"]]
- 004c7178 bytes ae511c94
+ 004ea010 bytes 9cb81d94
- 004c7188 ["INT_ADD", "register:40f0:8", ["const:4c7188:8", "const:4:8"]]
- 004c7188 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ea020 ["INT_ADD", "register:40f0:8", ["const:4ea020:8", "const:4:8"]]
+ 004ea020 ["CALL", null, ["callee:00c57ab0:8"]]
- 004c7188 bytes b64f1c94
+ 004ea020 bytes a4b61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a322de29ddb77be15ed3defa4f007a88"></a>

### [`004c7618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7618.md) → [`004ea4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea4b0.md) _ZNK5Botan10Public_Key18fingerprint_publicERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc770.md) [`00bdc780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc780.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c591c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591c0.md) [`00c591d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7618.md#insn-004c7644) · [`004c7658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7618.md#insn-004c7658) · [`004c7668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7618.md#insn-004c7668)
- 新版 `004ea4dc`（命令位置の公開資料なし） · `004ea4f0`（命令位置の公開資料なし） · `004ea500`（命令位置の公開資料なし）

~~~diff
- 004c7644 ["INT_ADD", "register:40f0:8", ["const:4c7644:8", "const:4:8"]]
- 004c7644 ["CALL", null, ["callee:00c591d0:8"]]
+ 004ea4dc ["INT_ADD", "register:40f0:8", ["const:4ea4dc:8", "const:4:8"]]
+ 004ea4dc ["CALL", null, ["callee:00c591d0:8"]]
- 004c7644 bytes 4f541c94
+ 004ea4dc bytes 3dbb1d94
- 004c7658 ["INT_ADD", "register:40f0:8", ["const:4c7658:8", "const:4:8"]]
- 004c7658 ["CALL", null, ["callee:00c591c0:8"]]
+ 004ea4f0 ["INT_ADD", "register:40f0:8", ["const:4ea4f0:8", "const:4:8"]]
+ 004ea4f0 ["CALL", null, ["callee:00c591c0:8"]]
- 004c7658 bytes 46541c94
+ 004ea4f0 bytes 34bb1d94
- 004c7668 ["INT_ADD", "register:40f0:8", ["const:4c7668:8", "const:4:8"]]
- 004c7668 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ea500 ["INT_ADD", "register:40f0:8", ["const:4ea500:8", "const:4:8"]]
+ 004ea500 ["CALL", null, ["callee:00c57ab0:8"]]
- 004c7668 bytes 7e4e1c94
+ 004ea500 bytes 6cb51d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b53072e7954d892081c5b771ec392d72"></a>

### [`004c9380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9380.md) → [`004ec218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec218.md) FUN_004ec218

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005aea7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c939c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9380.md#insn-004c939c)
- 新版 `004ec234`（命令位置の公開資料なし）

~~~diff
- 004c939c ["INT_ADD", "register:40f0:8", ["const:4c939c:8", "const:4:8"]]
- 004c939c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ec234 ["INT_ADD", "register:40f0:8", ["const:4ec234:8", "const:4:8"]]
+ 004ec234 ["CALL", null, ["callee:00c57ab0:8"]]
- 004c939c bytes 31471c94
+ 004ec234 bytes 1fae1d94
~~~


<a id="compare-15cb3e2d635b9f3b78703e91b3afbf30"></a>

### [`004c9d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9d0c.md) → [`004ecba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecba4.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceENSt6__ndk18functionIFNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEvEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9d0c.md#insn-004c9d50) · [`004c9d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9d0c.md#insn-004c9d7c) · [`004c9d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9d0c.md#insn-004c9d94)
- 新版 `004ecbe8`（命令位置の公開資料なし） · `004ecc14`（命令位置の公開資料なし） · `004ecc2c`（命令位置の公開資料なし）

~~~diff
- 004c9d50 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c9d50 ["INT_ADD", "register:40f0:8", ["const:4c9d50:8", "const:4:8"]]
- 004c9d50 ["CALLIND", null, ["register:0:8"]]
+ 004ecbe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ecbe8 ["INT_ADD", "register:40f0:8", ["const:4ecbe8:8", "const:4:8"]]
+ 004ecbe8 ["CALLIND", null, ["register:0:8"]]
- 004c9d50 bytes 00013fd6
+ 004ecbe8 bytes 00013fd6
- 004c9d7c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c9d7c ["INT_ADD", "register:40f0:8", ["const:4c9d7c:8", "const:4:8"]]
- 004c9d7c ["CALLIND", null, ["register:0:8"]]
+ 004ecc14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ecc14 ["INT_ADD", "register:40f0:8", ["const:4ecc14:8", "const:4:8"]]
+ 004ecc14 ["CALLIND", null, ["register:0:8"]]
- 004c9d7c bytes 00013fd6
+ 004ecc14 bytes 00013fd6
- 004c9d94 ["INT_ADD", "register:40f0:8", ["const:4c9d94:8", "const:4:8"]]
- 004c9d94 ["CALL", null, ["callee:004eccd0:8"]]
+ 004ecc2c ["INT_ADD", "register:40f0:8", ["const:4ecc2c:8", "const:4:8"]]
+ 004ecc2c ["CALL", null, ["callee:004eccd0:8"]]
- 004c9d94 bytes 29000094
+ 004ecc2c bytes 29000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b737e87bf1064f000f138cb1fb16a94"></a>

### [`004cb140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb140.md) → [`004edfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorENSt6__ndk18functionIFNS5_12basic_stringIcNS5_11char_traitsIcEENS5_9all

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb140.md#insn-004cb17c) · [`004cb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb140.md#insn-004cb19c) · [`004cb1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb140.md#insn-004cb1cc)
- 新版 `004ee014`（命令位置の公開資料なし） · `004ee034`（命令位置の公開資料なし） · `004ee064`（命令位置の公開資料なし）

~~~diff
- 004cb17c ["COPY", "register:0:8", ["register:4048:8"]]
- 004cb17c ["INT_ADD", "register:40f0:8", ["const:4cb17c:8", "const:4:8"]]
- 004cb17c ["CALLIND", null, ["register:0:8"]]
+ 004ee014 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ee014 ["INT_ADD", "register:40f0:8", ["const:4ee014:8", "const:4:8"]]
+ 004ee014 ["CALLIND", null, ["register:0:8"]]
- 004cb17c bytes 20013fd6
+ 004ee014 bytes 20013fd6
- 004cb19c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cb19c ["INT_ADD", "register:40f0:8", ["const:4cb19c:8", "const:4:8"]]
- 004cb19c ["CALLIND", null, ["register:0:8"]]
+ 004ee034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee034 ["INT_ADD", "register:40f0:8", ["const:4ee034:8", "const:4:8"]]
+ 004ee034 ["CALLIND", null, ["register:0:8"]]
- 004cb19c bytes 00013fd6
+ 004ee034 bytes 00013fd6
- 004cb1cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004cb1cc ["INT_ADD", "register:40f0:8", ["const:4cb1cc:8", "const:4:8"]]
- 004cb1cc ["CALLIND", null, ["register:0:8"]]
+ 004ee064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee064 ["INT_ADD", "register:40f0:8", ["const:4ee064:8", "const:4:8"]]
+ 004ee064 ["CALLIND", null, ["register:0:8"]]
- 004cb1cc bytes 00013fd6
+ 004ee064 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a059d8b74a54b9981765d6784b81180"></a>

### [`004cb32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb32c.md) → [`004ee1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee1c4.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb32c.md#insn-004cb350) · [`004cb378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb32c.md#insn-004cb378)
- 新版 `004ee1e8`（命令位置の公開資料なし） · `004ee210`（命令位置の公開資料なし）

~~~diff
- 004cb350 ["INT_ADD", "register:40f0:8", ["const:4cb350:8", "const:4:8"]]
- 004cb350 ["CALL", null, ["callee:00c59230:8"]]
+ 004ee1e8 ["INT_ADD", "register:40f0:8", ["const:4ee1e8:8", "const:4:8"]]
+ 004ee1e8 ["CALL", null, ["callee:00c59230:8"]]
- 004cb350 bytes 24451c94
+ 004ee1e8 bytes 12ac1d94
- 004cb378 ["INT_ADD", "register:40f0:8", ["const:4cb378:8", "const:4:8"]]
- 004cb378 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004ee210 ["INT_ADD", "register:40f0:8", ["const:4ee210:8", "const:4:8"]]
+ 004ee210 ["CALL", null, ["callee:00c57ae0:8"]]
- 004cb378 bytes 463f1c94
+ 004ee210 bytes 34a61d94
~~~


<a id="compare-99a3b6cd8739689d03f0cd3db17eb2ce"></a>

### [`004cb970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb970.md) → [`004ee808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee808.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc800.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb970.md#insn-004cb990) · [`004cb9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb970.md#insn-004cb9b8)
- 新版 `004ee828`（命令位置の公開資料なし） · `004ee850`（命令位置の公開資料なし）

~~~diff
- 004cb990 ["INT_ADD", "register:40f0:8", ["const:4cb990:8", "const:4:8"]]
- 004cb990 ["CALL", null, ["callee:00c59250:8"]]
+ 004ee828 ["INT_ADD", "register:40f0:8", ["const:4ee828:8", "const:4:8"]]
+ 004ee828 ["CALL", null, ["callee:00c59250:8"]]
- 004cb990 bytes 9c431c94
+ 004ee828 bytes 8aaa1d94
- 004cb9b8 ["INT_ADD", "register:40f0:8", ["const:4cb9b8:8", "const:4:8"]]
- 004cb9b8 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004ee850 ["INT_ADD", "register:40f0:8", ["const:4ee850:8", "const:4:8"]]
+ 004ee850 ["CALL", null, ["callee:00c57ae0:8"]]
- 004cb9b8 bytes b63d1c94
+ 004ee850 bytes a4a41d94
~~~


<a id="compare-d54beed540ec06127185886641d9ee6c"></a>

### [`004cc064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc064.md) → [`004eeefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeefc.md) _ZN5Botan16PK_Encryptor_EMED0Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cc074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc064.md#insn-004cc074)
- 新版 `004eef0c`（命令位置の公開資料なし）

~~~diff
- 004cc074 ["INT_ADD", "register:40f0:8", ["const:4cc074:8", "const:4:8"]]
- 004cc074 ["CALL", null, ["callee:00c58e10:8"]]
+ 004eef0c ["INT_ADD", "register:40f0:8", ["const:4eef0c:8", "const:4:8"]]
+ 004eef0c ["CALL", null, ["callee:00c58e10:8"]]
- 004cc074 bytes d3401c94
+ 004eef0c bytes c1a71d94
~~~


<a id="compare-790955ddecc81fa98377ef1d745e5a89"></a>

### [`004ccb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccb7c.md) → [`004efa14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efa14.md) _ZN5Botan16PK_Key_AgreementaSEOS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ccbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccb7c.md#insn-004ccbb4)
- 新版 `004efa4c`（命令位置の公開資料なし）

~~~diff
- 004ccbb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ccbb4 ["INT_ADD", "register:40f0:8", ["const:4ccbb4:8", "const:4:8"]]
- 004ccbb4 ["CALLIND", null, ["register:0:8"]]
+ 004efa4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004efa4c ["INT_ADD", "register:40f0:8", ["const:4efa4c:8", "const:4:8"]]
+ 004efa4c ["CALLIND", null, ["register:0:8"]]
- 004ccbb4 bytes 20013fd6
+ 004efa4c bytes 20013fd6
~~~


<a id="compare-9c002beed1927ed221df5b5d7583936f"></a>

### [`004cd814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd814.md) → [`004f06ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f06ac.md) _ZN5Botan11PK_Verifier14verify_messageEPKhmS2_m

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc850.md) · 呼出先 1件 [`00bdc410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc410.md)
- 新版 呼出元 1件 [`00c592a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592a0.md) · 呼出先 1件 [`00c58e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cd83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd814.md#insn-004cd83c)
- 新版 `004f06d4`（命令位置の公開資料なし）

~~~diff
- 004cd83c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cd83c ["INT_ADD", "register:40f0:8", ["const:4cd83c:8", "const:4:8"]]
- 004cd83c ["CALLIND", null, ["register:0:8"]]
+ 004f06d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f06d4 ["INT_ADD", "register:40f0:8", ["const:4f06d4:8", "const:4:8"]]
+ 004f06d4 ["CALLIND", null, ["register:0:8"]]
- 004cd83c bytes 00013fd6
+ 004f06d4 bytes 00013fd6
~~~


<a id="compare-f166c6c8022103ffcd764e9dfef7e1b6"></a>

### [`004cdca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdca8.md) → [`004f0b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md) FUN_004f0b40

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004cd86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd86c.md) · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`004f0704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cdd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdca8.md#insn-004cdd20) · [`004cdd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdca8.md#insn-004cdd3c) · [`004cdd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdca8.md#insn-004cdd4c)
- 新版 `004f0bb8`（命令位置の公開資料なし） · `004f0bd4`（命令位置の公開資料なし） · `004f0be4`（命令位置の公開資料なし）

~~~diff
- 004cdd20 ["INT_ADD", "register:40f0:8", ["const:4cdd20:8", "const:4:8"]]
- 004cdd20 ["CALL", null, ["callee:00c57a90:8"]]
+ 004f0bb8 ["INT_ADD", "register:40f0:8", ["const:4f0bb8:8", "const:4:8"]]
+ 004f0bb8 ["CALL", null, ["callee:00c57a90:8"]]
- 004cdd20 bytes c8341c94
+ 004f0bb8 bytes b69b1d94
- 004cdd3c ["INT_ADD", "register:40f0:8", ["const:4cdd3c:8", "const:4:8"]]
- 004cdd3c ["CALL", null, ["callee:00c57c90:8"]]
+ 004f0bd4 ["INT_ADD", "register:40f0:8", ["const:4f0bd4:8", "const:4:8"]]
+ 004f0bd4 ["CALL", null, ["callee:00c57c90:8"]]
- 004cdd3c bytes 41351c94
+ 004f0bd4 bytes 2f9c1d94
- 004cdd4c ["INT_ADD", "register:40f0:8", ["const:4cdd4c:8", "const:4:8"]]
- 004cdd4c ["CALL", null, ["callee:00c57c00:8"]]
+ 004f0be4 ["INT_ADD", "register:40f0:8", ["const:4f0be4:8", "const:4:8"]]
+ 004f0be4 ["CALL", null, ["callee:00c57c00:8"]]
- 004cdd4c bytes 19351c94
+ 004f0be4 bytes 079c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16cf2ab2c1e58209602d2456f27adefe"></a>

### [`004ce8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce8c4.md) → [`004f175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f175c.md) _ZN5Botan21RandomNumberGenerator23randomize_with_ts_inputEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md) [`00bdc8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8b0.md) [`00bdc8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md) [`00c59310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce8c4.md#insn-004ce8f8) · [`004ce900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce8c4.md#insn-004ce900) · [`004ce924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce8c4.md#insn-004ce924)
- 新版 `004f1790`（命令位置の公開資料なし） · `004f1798`（命令位置の公開資料なし） · `004f17bc`（命令位置の公開資料なし）

~~~diff
- 004ce8f8 ["INT_ADD", "register:40f0:8", ["const:4ce8f8:8", "const:4:8"]]
- 004ce8f8 ["CALL", null, ["callee:00c59300:8"]]
+ 004f1790 ["INT_ADD", "register:40f0:8", ["const:4f1790:8", "const:4:8"]]
+ 004f1790 ["CALL", null, ["callee:00c59300:8"]]
- 004ce8f8 bytes ee371c94
+ 004f1790 bytes dc9e1d94
- 004ce900 ["INT_ADD", "register:40f0:8", ["const:4ce900:8", "const:4:8"]]
- 004ce900 ["CALL", null, ["callee:00c58180:8"]]
+ 004f1798 ["INT_ADD", "register:40f0:8", ["const:4f1798:8", "const:4:8"]]
+ 004f1798 ["CALL", null, ["callee:00c58180:8"]]
- 004ce900 bytes 8c331c94
+ 004f1798 bytes 7a9a1d94
- 004ce924 ["INT_ADD", "register:40f0:8", ["const:4ce924:8", "const:4:8"]]
- 004ce924 ["CALL", null, ["callee:00c59310:8"]]
+ 004f17bc ["INT_ADD", "register:40f0:8", ["const:4f17bc:8", "const:4:8"]]
+ 004f17bc ["CALL", null, ["callee:00c59310:8"]]
- 004ce924 bytes e7371c94
+ 004f17bc bytes d59e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5836a66fab7b0e6e7478f7999c352133"></a>

### [`004ce974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce974.md) → [`004f180c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f180c.md) _ZN5Botan2OS23get_system_timestamp_nsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md) [`00bdc8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ce998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce974.md#insn-004ce998) · [`004ce9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce974.md#insn-004ce9a0) · [`004ce9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce974.md#insn-004ce9e0)
- 新版 `004f1830`（命令位置の公開資料なし） · `004f1838`（命令位置の公開資料なし） · `004f1878`（命令位置の公開資料なし）

~~~diff
- 004ce998 ["INT_ADD", "register:40f0:8", ["const:4ce998:8", "const:4:8"]]
- 004ce998 ["CALL", null, ["callee:00c59300:8"]]
+ 004f1830 ["INT_ADD", "register:40f0:8", ["const:4f1830:8", "const:4:8"]]
+ 004f1830 ["CALL", null, ["callee:00c59300:8"]]
- 004ce998 bytes c6371c94
+ 004f1830 bytes b49e1d94
- 004ce9a0 ["INT_ADD", "register:40f0:8", ["const:4ce9a0:8", "const:4:8"]]
- 004ce9a0 ["CALL", null, ["callee:00c58180:8"]]
+ 004f1838 ["INT_ADD", "register:40f0:8", ["const:4f1838:8", "const:4:8"]]
+ 004f1838 ["CALL", null, ["callee:00c58180:8"]]
- 004ce9a0 bytes 64331c94
+ 004f1838 bytes 529a1d94
- 004ce9e0 ["INT_ADD", "register:40f0:8", ["const:4ce9e0:8", "const:4:8"]]
- 004ce9e0 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004f1878 ["INT_ADD", "register:40f0:8", ["const:4f1878:8", "const:4:8"]]
+ 004f1878 ["CALL", null, ["callee:00c57ae0:8"]]
- 004ce9e0 bytes ac311c94
+ 004f1878 bytes 9a981d94
~~~


<a id="compare-6c2a6b094e61099ce1ded8270675f587"></a>

### [`004ce9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce9e4.md) → [`004f187c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f187c.md) _ZN5Botan2OS25get_high_resolution_clockEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8c0.md) · 呼出先 3件 [`00bdb070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb070.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8b0.md)
- 新版 呼出元 1件 [`00c59310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59310.md) · 呼出先 3件 [`00c57ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cea08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce9e4.md#insn-004cea08) · [`004cea18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce9e4.md#insn-004cea18) · [`004cea28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce9e4.md#insn-004cea28)
- 新版 `004f18a0`（命令位置の公開資料なし） · `004f18b0`（命令位置の公開資料なし） · `004f18c0`（命令位置の公開資料なし）

~~~diff
- 004cea08 ["INT_ADD", "register:40f0:8", ["const:4cea08:8", "const:4:8"]]
- 004cea08 ["CALL", null, ["callee:00c59300:8"]]
+ 004f18a0 ["INT_ADD", "register:40f0:8", ["const:4f18a0:8", "const:4:8"]]
+ 004f18a0 ["CALL", null, ["callee:00c59300:8"]]
- 004cea08 bytes aa371c94
+ 004f18a0 bytes 989e1d94
- 004cea18 ["INT_ADD", "register:40f0:8", ["const:4cea18:8", "const:4:8"]]
- 004cea18 ["CALL", null, ["callee:00c59300:8"]]
+ 004f18b0 ["INT_ADD", "register:40f0:8", ["const:4f18b0:8", "const:4:8"]]
+ 004f18b0 ["CALL", null, ["callee:00c59300:8"]]
- 004cea18 bytes a6371c94
+ 004f18b0 bytes 949e1d94
- 004cea28 ["INT_ADD", "register:40f0:8", ["const:4cea28:8", "const:4:8"]]
- 004cea28 ["CALL", null, ["callee:00c59300:8"]]
+ 004f18c0 ["INT_ADD", "register:40f0:8", ["const:4f18c0:8", "const:4:8"]]
+ 004f18c0 ["CALL", null, ["callee:00c59300:8"]]
- 004cea28 bytes a2371c94
+ 004f18c0 bytes 909e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4009ab6d30393542c1bf6f1c075bb297"></a>

### [`004cea84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cea84.md) → [`004f191c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f191c.md) _ZN5Botan21RandomNumberGenerator20randomize_with_inputEPhmPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ceab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cea84.md#insn-004ceab0)
- 新版 `004f1948`（命令位置の公開資料なし）

~~~diff
- 004ceab0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ceab0 ["INT_ADD", "register:40f0:8", ["const:4ceab0:8", "const:4:8"]]
- 004ceab0 ["CALLIND", null, ["register:0:8"]]
+ 004f1948 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f1948 ["INT_ADD", "register:40f0:8", ["const:4f1948:8", "const:4:8"]]
+ 004f1948 ["CALLIND", null, ["register:0:8"]]
- 004ceab0 bytes 00013fd6
+ 004f1948 bytes 00013fd6
~~~


<a id="compare-6bff2ed1767944e067a01abff99616c3"></a>

### [`004cead8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cead8.md) → [`004f1970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1970.md) _ZN5Botan21RandomNumberGenerator6reseedERNS_15Entropy_SourcesEmNSt6__ndk16chrono8durationIxNS3_5ratioILl1ELl1000EEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ceafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cead8.md#insn-004ceafc) · [`004ceb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cead8.md#insn-004ceb2c) · [`004ceb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cead8.md#insn-004ceb3c)
- 新版 `004f1994`（命令位置の公開資料なし） · `004f19c4`（命令位置の公開資料なし） · `004f19d4`（命令位置の公開資料なし）

~~~diff
- 004ceafc ["INT_ADD", "register:40f0:8", ["const:4ceafc:8", "const:4:8"]]
- 004ceafc ["CALL", null, ["callee:00c58180:8"]]
+ 004f1994 ["INT_ADD", "register:40f0:8", ["const:4f1994:8", "const:4:8"]]
+ 004f1994 ["CALL", null, ["callee:00c58180:8"]]
- 004ceafc bytes 0d331c94
+ 004f1994 bytes fb991d94
- 004ceb2c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ceb2c ["INT_ADD", "register:40f0:8", ["const:4ceb2c:8", "const:4:8"]]
- 004ceb2c ["CALLIND", null, ["register:0:8"]]
+ 004f19c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f19c4 ["INT_ADD", "register:40f0:8", ["const:4f19c4:8", "const:4:8"]]
+ 004f19c4 ["CALLIND", null, ["register:0:8"]]
- 004ceb2c bytes 00013fd6
+ 004f19c4 bytes 00013fd6
- 004ceb3c ["INT_ADD", "register:40f0:8", ["const:4ceb3c:8", "const:4:8"]]
- 004ceb3c ["CALL", null, ["callee:00c58180:8"]]
+ 004f19d4 ["INT_ADD", "register:40f0:8", ["const:4f19d4:8", "const:4:8"]]
+ 004f19d4 ["CALL", null, ["callee:00c58180:8"]]
- 004ceb3c bytes fd321c94
+ 004f19d4 bytes eb991d94
~~~


<a id="compare-cece24bc9c3e8a6347f22c86a8c1352a"></a>

### [`004d2330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2330.md) → [`004f51c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51c8.md) _ZTv0_n104_NK5Botan13RSA_PublicKey20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9a

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc910.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d2344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2330.md#insn-004d2344)
- 新版 `004f51dc`（命令位置の公開資料なし）

~~~diff
- 004d2344 ["INT_ADD", "register:40f0:8", ["const:4d2344:8", "const:4:8"]]
- 004d2344 ["CALL", null, ["callee:00c59360:8"]]
+ 004f51dc ["INT_ADD", "register:40f0:8", ["const:4f51dc:8", "const:4:8"]]
+ 004f51dc ["CALL", null, ["callee:00c59360:8"]]
- 004d2344 bytes 73291c94
+ 004f51dc bytes 61901d94
~~~


<a id="compare-01a6bfd4c520dc489e46c37c6284702c"></a>

### [`004d2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2c70.md) → [`004f5b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5b08.md) _ZN5Botan7SHA_16010compress_nEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d2cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2c70.md#insn-004d2cd0)
- 新版 `004f5b68`（命令位置の公開資料なし）

~~~diff
- 004d2cd0 ["INT_ADD", "register:40f0:8", ["const:4d2cd0:8", "const:4:8"]]
- 004d2cd0 ["CALL", null, ["callee:005408e0:8"]]
+ 004f5b68 ["INT_ADD", "register:40f0:8", ["const:4f5b68:8", "const:4:8"]]
+ 004f5b68 ["CALL", null, ["callee:005408e0:8"]]
- 004d2cd0 bytes 5e2b0194
+ 004f5b68 bytes 5e2b0194
~~~


<a id="compare-a0fdac9315fb4023fb3478ed6b6ed8ac"></a>

### [`004d5c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5c30.md) → [`004f8ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8ac8.md) _ZN5Botan12StreamCipher9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004d5d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5d94.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004f8c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8c2c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d5ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5c30.md#insn-004d5ca0) · [`004d5cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5c30.md#insn-004d5cb0) · [`004d5cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5c30.md#insn-004d5cec)
- 新版 `004f8b38`（命令位置の公開資料なし） · `004f8b48`（命令位置の公開資料なし） · `004f8b84`（命令位置の公開資料なし）

~~~diff
- 004d5ca0 ["INT_ADD", "register:40f0:8", ["const:4d5ca0:8", "const:4:8"]]
- 004d5ca0 ["CALL", null, ["callee:00473500:8"]]
+ 004f8b38 ["INT_ADD", "register:40f0:8", ["const:4f8b38:8", "const:4:8"]]
+ 004f8b38 ["CALL", null, ["callee:00473500:8"]]
- 004d5ca0 bytes 72eafd97
+ 004f8b38 bytes 72eafd97
- 004d5cb0 ["INT_ADD", "register:40f0:8", ["const:4d5cb0:8", "const:4:8"]]
- 004d5cb0 ["CALL", null, ["callee:004f8c2c:8"]]
+ 004f8b48 ["INT_ADD", "register:40f0:8", ["const:4f8b48:8", "const:4:8"]]
+ 004f8b48 ["CALL", null, ["callee:004f8c2c:8"]]
- 004d5cb0 bytes 39000094
+ 004f8b48 bytes 39000094
- 004d5cec ["INT_ADD", "register:40f0:8", ["const:4d5cec:8", "const:4:8"]]
- 004d5cec ["CALL", null, ["callee:00c57ab0:8"]]
+ 004f8b84 ["INT_ADD", "register:40f0:8", ["const:4f8b84:8", "const:4:8"]]
+ 004f8b84 ["CALL", null, ["callee:00c57ab0:8"]]
- 004d5cec bytes dd141c94
+ 004f8b84 bytes cb7b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73ca506229eeda35b21db36f910dbdf5"></a>

### [`004d5d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5d94.md) → [`004f8c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8c2c.md) FUN_004f8c2c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004d5c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5c30.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc010.md)
- 新版 呼出元 1件 [`004f8ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8ac8.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d5de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5d94.md#insn-004d5de4) · [`004d5df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5d94.md#insn-004d5df8) · [`004d5e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5d94.md#insn-004d5e10)
- 新版 `004f8c7c`（命令位置の公開資料なし） · `004f8c90`（命令位置の公開資料なし） · `004f8ca8`（命令位置の公開資料なし）

~~~diff
- 004d5de4 ["INT_ADD", "register:40f0:8", ["const:4d5de4:8", "const:4:8"]]
- 004d5de4 ["CALL", null, ["callee:00540d3c:8"]]
+ 004f8c7c ["INT_ADD", "register:40f0:8", ["const:4f8c7c:8", "const:4:8"]]
+ 004f8c7c ["CALL", null, ["callee:00540d3c:8"]]
- 004d5de4 bytes 30200194
+ 004f8c7c bytes 30200194
- 004d5df8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004d5df8 ["INT_ADD", "register:40f0:8", ["const:4d5df8:8", "const:4:8"]]
- 004d5df8 ["CALLIND", null, ["register:0:8"]]
+ 004f8c90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f8c90 ["INT_ADD", "register:40f0:8", ["const:4f8c90:8", "const:4:8"]]
+ 004f8c90 ["CALLIND", null, ["register:0:8"]]
- 004d5df8 bytes 00013fd6
+ 004f8c90 bytes 00013fd6
- 004d5e10 ["INT_ADD", "register:40f0:8", ["const:4d5e10:8", "const:4:8"]]
- 004d5e10 ["CALL", null, ["callee:00c58a60:8"]]
+ 004f8ca8 ["INT_ADD", "register:40f0:8", ["const:4f8ca8:8", "const:4:8"]]
+ 004f8ca8 ["CALL", null, ["callee:00c58a60:8"]]
- 004d5e10 bytes 80181c94
+ 004f8ca8 bytes 6e7f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c19ac1ee7b84159c9bc248ceb5d90b18"></a>

### [`004d6094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6094.md) → [`004f8f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) FUN_004f8f2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004d5ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md) [`0051308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md) · 呼出先 1件 [`00bdc980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc980.md)
- 新版 呼出元 2件 [`004f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) [`00535f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) · 呼出先 1件 [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d60a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6094.md#insn-004d60a8)
- 新版 `004f8f40`（命令位置の公開資料なし）

~~~diff
- 004d60a8 ["INT_ADD", "register:40f0:8", ["const:4d60a8:8", "const:4:8"]]
- 004d60a8 ["CALL", null, ["callee:00c593d0:8"]]
+ 004f8f40 ["INT_ADD", "register:40f0:8", ["const:4f8f40:8", "const:4:8"]]
+ 004f8f40 ["CALL", null, ["callee:00c593d0:8"]]
- 004d60a8 bytes 361a1c94
+ 004f8f40 bytes 24811d94
~~~


<a id="compare-1d72826e492af85e5b9fc758d25e23d8"></a>

### [`004d6aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6aac.md) → [`004f9944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9944.md) _ZN5Botan10DataSource12discard_nextEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d6b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6aac.md#insn-004d6b08) · [`004d6b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6aac.md#insn-004d6b44)
- 新版 `004f99a0`（命令位置の公開資料なし） · `004f99dc`（命令位置の公開資料なし）

~~~diff
- 004d6b08 ["COPY", "register:0:8", ["register:4040:8"]]
- 004d6b08 ["INT_ADD", "register:40f0:8", ["const:4d6b08:8", "const:4:8"]]
- 004d6b08 ["CALLIND", null, ["register:0:8"]]
+ 004f99a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f99a0 ["INT_ADD", "register:40f0:8", ["const:4f99a0:8", "const:4:8"]]
+ 004f99a0 ["CALLIND", null, ["register:0:8"]]
- 004d6b08 bytes 00013fd6
+ 004f99a0 bytes 00013fd6
- 004d6b44 ["INT_ADD", "register:40f0:8", ["const:4d6b44:8", "const:4:8"]]
- 004d6b44 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004f99dc ["INT_ADD", "register:40f0:8", ["const:4f99dc:8", "const:4:8"]]
+ 004f99dc ["CALL", null, ["callee:00c57ae0:8"]]
- 004d6b44 bytes 53111c94
+ 004f99dc bytes 41781d94
~~~


<a id="compare-65fc008a2ec1ec8150b19be9941202db"></a>

### [`004d6b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6b48.md) → [`004f99e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f99e0.md) _ZN5Botan17DataSource_Memory4readEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d6b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6b48.md#insn-004d6b80)
- 新版 `004f9a18`（命令位置の公開資料なし）

~~~diff
- 004d6b80 ["INT_ADD", "register:40f0:8", ["const:4d6b80:8", "const:4:8"]]
- 004d6b80 ["CALL", null, ["callee:00c57b40:8"]]
+ 004f9a18 ["INT_ADD", "register:40f0:8", ["const:4f9a18:8", "const:4:8"]]
+ 004f9a18 ["CALL", null, ["callee:00c57b40:8"]]
- 004d6b80 bytes 5c111c94
+ 004f9a18 bytes 4a781d94
~~~


<a id="compare-da1ea1433226b6288fa8370b24056277"></a>

### [`004d6bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6bbc.md) → [`004f9a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9a54.md) _ZNK5Botan17DataSource_Memory4peekEPhmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d6bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6bbc.md#insn-004d6bfc)
- 新版 `004f9a94`（命令位置の公開資料なし）

~~~diff
- 004d6bfc ["INT_ADD", "register:40f0:8", ["const:4d6bfc:8", "const:4:8"]]
- 004d6bfc ["CALL", null, ["callee:00c57b40:8"]]
+ 004f9a94 ["INT_ADD", "register:40f0:8", ["const:4f9a94:8", "const:4:8"]]
+ 004f9a94 ["CALL", null, ["callee:00c57b40:8"]]
- 004d6bfc bytes 3d111c94
+ 004f9a94 bytes 2b781d94
~~~


<a id="compare-dc9f6c4ade0cdba246dd4605c47dd4b7"></a>

### [`004d6db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6db4.md) → [`004f9c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9c4c.md) _ZN5Botan17DataSource_Stream15check_availableEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc990.md) [`00bdc9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9a0.md) [`00bdc9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c593e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593e0.md) [`00c593f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593f0.md) [`00c59400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d6dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6db4.md#insn-004d6dd0) · [`004d6de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6db4.md#insn-004d6de8) · [`004d6df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6db4.md#insn-004d6df0)
- 新版 `004f9c68`（命令位置の公開資料なし） · `004f9c80`（命令位置の公開資料なし） · `004f9c88`（命令位置の公開資料なし）

~~~diff
- 004d6dd0 ["INT_ADD", "register:40f0:8", ["const:4d6dd0:8", "const:4:8"]]
- 004d6dd0 ["CALL", null, ["callee:00c593e0:8"]]
+ 004f9c68 ["INT_ADD", "register:40f0:8", ["const:4f9c68:8", "const:4:8"]]
+ 004f9c68 ["CALL", null, ["callee:00c593e0:8"]]
- 004d6dd0 bytes f0161c94
+ 004f9c68 bytes de7d1d94
- 004d6de8 ["INT_ADD", "register:40f0:8", ["const:4d6de8:8", "const:4:8"]]
- 004d6de8 ["CALL", null, ["callee:00c593f0:8"]]
+ 004f9c80 ["INT_ADD", "register:40f0:8", ["const:4f9c80:8", "const:4:8"]]
+ 004f9c80 ["CALL", null, ["callee:00c593f0:8"]]
- 004d6de8 bytes ee161c94
+ 004f9c80 bytes dc7d1d94
- 004d6df0 ["INT_ADD", "register:40f0:8", ["const:4d6df0:8", "const:4:8"]]
- 004d6df0 ["CALL", null, ["callee:00c593e0:8"]]
+ 004f9c88 ["INT_ADD", "register:40f0:8", ["const:4f9c88:8", "const:4:8"]]
+ 004f9c88 ["CALL", null, ["callee:00c593e0:8"]]
- 004d6df0 bytes e8161c94
+ 004f9c88 bytes d67d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313fa434a5c2622773b153c1ae9e6734"></a>

### [`004d74ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d74ac.md) → [`004fa344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa344.md) _ZN5Botan17DataSource_StreamD1Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d74d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d74ac.md#insn-004d74d0)
- 新版 `004fa368`（命令位置の公開資料なし）

~~~diff
- 004d74d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004d74d0 ["INT_ADD", "register:40f0:8", ["const:4d74d0:8", "const:4:8"]]
- 004d74d0 ["CALLIND", null, ["register:0:8"]]
+ 004fa368 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fa368 ["INT_ADD", "register:40f0:8", ["const:4fa368:8", "const:4:8"]]
+ 004fa368 ["CALLIND", null, ["register:0:8"]]
- 004d74d0 bytes 00013fd6
+ 004fa368 bytes 00013fd6
~~~


<a id="compare-40819a5c0d5e67a7f768a6dd0a02ad88"></a>

### [`004d9804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9804.md) → [`004fc69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc69c.md) FUN_004fc69c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004daaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004fd93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004d9854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9804.md#insn-004d9854) · [`004d9864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9804.md#insn-004d9864)
- 新版 `004fc6ec`（命令位置の公開資料なし） · `004fc6fc`（命令位置の公開資料なし）

~~~diff
- 004d9854 ["INT_ADD", "register:40f0:8", ["const:4d9854:8", "const:4:8"]]
- 004d9854 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004fc6ec ["INT_ADD", "register:40f0:8", ["const:4fc6ec:8", "const:4:8"]]
+ 004fc6ec ["CALL", null, ["callee:00c57ab0:8"]]
- 004d9854 bytes 03061c94
+ 004fc6ec bytes f16c1d94
- 004d9864 ["INT_ADD", "register:40f0:8", ["const:4d9864:8", "const:4:8"]]
- 004d9864 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004fc6fc ["INT_ADD", "register:40f0:8", ["const:4fc6fc:8", "const:4:8"]]
+ 004fc6fc ["CALL", null, ["callee:00c57ab0:8"]]
- 004d9864 bytes ff051c94
+ 004fc6fc bytes ed6c1d94
~~~


<a id="compare-ec03ef8f03e7b07255c70afa3c9b2e7a"></a>

### [`004da844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da844.md) → [`004fd6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd6dc.md) _ZN5Botan11erase_charsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_3setIcNS0_4lessIcEES5_EE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004da88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da844.md#insn-004da88c)
- 新版 `004fd724`（命令位置の公開資料なし）

~~~diff
- 004da88c ["INT_ADD", "register:40f0:8", ["const:4da88c:8", "const:4:8"]]
- 004da88c ["CALL", null, ["callee:00c58200:8"]]
+ 004fd724 ["INT_ADD", "register:40f0:8", ["const:4fd724:8", "const:4:8"]]
+ 004fd724 ["CALL", null, ["callee:00c58200:8"]]
- 004da88c bytes c9031c94
+ 004fd724 bytes b76a1d94
~~~


<a id="compare-ff734d3db3d40e2c9db50a1745d4ad26"></a>

### [`004da8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da8fc.md) → [`004fd794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd794.md) _ZN5Botan13replace_charsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_3setIcNS0_4lessIcEES5_EEc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004da93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da8fc.md#insn-004da93c)
- 新版 `004fd7d4`（命令位置の公開資料なし）

~~~diff
- 004da93c ["INT_ADD", "register:40f0:8", ["const:4da93c:8", "const:4:8"]]
- 004da93c ["CALL", null, ["callee:0043bae0:8"]]
+ 004fd7d4 ["INT_ADD", "register:40f0:8", ["const:4fd7d4:8", "const:4:8"]]
+ 004fd7d4 ["CALL", null, ["callee:0043bae0:8"]]
- 004da93c bytes a9f9fc97
+ 004fd7d4 bytes c3f8fc97
~~~


<a id="compare-bdf11cdc58d2a06de8e548429f46b536"></a>

### [`004da9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da9e0.md) → [`004fd878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd878.md) _ZN5Botan12replace_charERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEcc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004daa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da9e0.md#insn-004daa20)
- 新版 `004fd8b8`（命令位置の公開資料なし）

~~~diff
- 004daa20 ["INT_ADD", "register:40f0:8", ["const:4daa20:8", "const:4:8"]]
- 004daa20 ["CALL", null, ["callee:0043bae0:8"]]
+ 004fd8b8 ["INT_ADD", "register:40f0:8", ["const:4fd8b8:8", "const:4:8"]]
+ 004fd8b8 ["CALL", null, ["callee:0043bae0:8"]]
- 004daa20 bytes 70f9fc97
+ 004fd8b8 bytes 8af8fc97
~~~


<a id="compare-31321c5519d5bdafa5c44b2e7275d7b3"></a>

### [`004db3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db3c8.md) → [`004fe260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe260.md) _ZN5Botan8clean_wsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcaf0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c59540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59540.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004db500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db3c8.md#insn-004db500) · [`004db520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db3c8.md#insn-004db520) · [`004db544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db3c8.md#insn-004db544)
- 新版 `004fe398`（命令位置の公開資料なし） · `004fe3b8`（命令位置の公開資料なし） · `004fe3dc`（命令位置の公開資料なし）

~~~diff
- 004db500 ["INT_ADD", "register:40f0:8", ["const:4db500:8", "const:4:8"]]
- 004db500 ["CALL", null, ["callee:00c57a90:8"]]
+ 004fe398 ["INT_ADD", "register:40f0:8", ["const:4fe398:8", "const:4:8"]]
+ 004fe398 ["CALL", null, ["callee:00c57a90:8"]]
- 004db500 bytes d0fe1b94
+ 004fe398 bytes be651d94
- 004db520 ["INT_ADD", "register:40f0:8", ["const:4db520:8", "const:4:8"]]
- 004db520 ["CALL", null, ["callee:00c57b40:8"]]
+ 004fe3b8 ["INT_ADD", "register:40f0:8", ["const:4fe3b8:8", "const:4:8"]]
+ 004fe3b8 ["CALL", null, ["callee:00c57b40:8"]]
- 004db520 bytes f4fe1b94
+ 004fe3b8 bytes e2651d94
- 004db544 ["INT_ADD", "register:40f0:8", ["const:4db544:8", "const:4:8"]]
- 004db544 ["CALL", null, ["callee:004428dc:8"]]
+ 004fe3dc ["INT_ADD", "register:40f0:8", ["const:4fe3dc:8", "const:4:8"]]
+ 004fe3dc ["CALL", null, ["callee:004428dc:8"]]
- 004db544 bytes 2612fd97
+ 004fe3dc bytes 4011fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93514faaa46b2baa05aa95c9afd8ee90"></a>

### [`004dc168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc168.md) → [`004ff000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md) _ZN5Botan15AlternativeName13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb00.md) · 呼出先 3件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00524cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524cd8.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c59550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59550.md) · 呼出先 3件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00547b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc168.md#insn-004dc1c0) · [`004dc254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc168.md#insn-004dc254)
- 新版 `004ff058`（命令位置の公開資料なし） · `004ff0ec`（命令位置の公開資料なし）

~~~diff
- 004dc1c0 ["INT_ADD", "register:40f0:8", ["const:4dc1c0:8", "const:4:8"]]
- 004dc1c0 ["CALL", null, ["callee:00547b70:8"]]
+ 004ff058 ["INT_ADD", "register:40f0:8", ["const:4ff058:8", "const:4:8"]]
+ 004ff058 ["CALL", null, ["callee:00547b70:8"]]
- 004dc1c0 bytes c6220194
+ 004ff058 bytes c6220194
- 004dc254 ["INT_ADD", "register:40f0:8", ["const:4dc254:8", "const:4:8"]]
- 004dc254 ["CALL", null, ["callee:00c57c50:8"]]
+ 004ff0ec ["INT_ADD", "register:40f0:8", ["const:4ff0ec:8", "const:4:8"]]
+ 004ff0ec ["CALL", null, ["callee:00c57c50:8"]]
- 004dc254 bytes ebfb1b94
+ 004ff0ec bytes d9621d94
~~~


<a id="compare-e089baa6a2db730fe30c8ea07214db38"></a>

### [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) → [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) FUN_004ff160

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`004dc168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc168.md) [`004dc550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc550.md) [`004e1aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1aec.md) [`004e1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1af0.md) [`004e1b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1b98.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005261fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005261fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 18件 [`004ff000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md) [`004ff3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff3e8.md) [`00504984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504984.md) [`00504988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504988.md) [`00504a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504a30.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md#insn-004dc318) · [`004dc344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md#insn-004dc344) · [`004dc350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md#insn-004dc350)
- 新版 `004ff1b0`（命令位置の公開資料なし） · `004ff1dc`（命令位置の公開資料なし） · `004ff1e8`（命令位置の公開資料なし）

~~~diff
- 004dc318 ["INT_ADD", "register:40f0:8", ["const:4dc318:8", "const:4:8"]]
- 004dc318 ["CALL", null, ["callee:0043bae0:8"]]
+ 004ff1b0 ["INT_ADD", "register:40f0:8", ["const:4ff1b0:8", "const:4:8"]]
+ 004ff1b0 ["CALL", null, ["callee:0043bae0:8"]]
- 004dc318 bytes 32f3fc97
+ 004ff1b0 bytes 4cf2fc97
- 004dc344 ["INT_ADD", "register:40f0:8", ["const:4dc344:8", "const:4:8"]]
- 004dc344 ["CALL", null, ["callee:0043bae0:8"]]
+ 004ff1dc ["INT_ADD", "register:40f0:8", ["const:4ff1dc:8", "const:4:8"]]
+ 004ff1dc ["CALL", null, ["callee:0043bae0:8"]]
- 004dc344 bytes 27f3fc97
+ 004ff1dc bytes 41f2fc97
- 004dc350 ["INT_ADD", "register:40f0:8", ["const:4dc350:8", "const:4:8"]]
- 004dc350 ["CALL", null, ["callee:00549094:8"]]
+ 004ff1e8 ["INT_ADD", "register:40f0:8", ["const:4ff1e8:8", "const:4:8"]]
+ 004ff1e8 ["CALL", null, ["callee:00549094:8"]]
- 004dc350 bytes ab270194
+ 004ff1e8 bytes ab270194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02de301eff05a963790a095e530d281c"></a>

### [`004dc4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md) → [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) FUN_004ff33c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004dc3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc3d8.md) [`004dcf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcf48.md) [`004f11e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md) [`0050af44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050af44.md) · 呼出先 4件 [`00524eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524eec.md) [`00525054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525054.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`004ff270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md) [`004ffde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md) [`00514078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md) [`0052e00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e00c.md) · 呼出先 4件 [`00547d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d84.md) [`00547eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547eec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md#insn-004dc4c8) · [`004dc4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md#insn-004dc4d4) · [`004dc4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md#insn-004dc4e4)
- 新版 `004ff360`（命令位置の公開資料なし） · `004ff36c`（命令位置の公開資料なし） · `004ff37c`（命令位置の公開資料なし）

~~~diff
- 004dc4c8 ["INT_ADD", "register:40f0:8", ["const:4dc4c8:8", "const:4:8"]]
- 004dc4c8 ["CALL", null, ["callee:00547eec:8"]]
+ 004ff360 ["INT_ADD", "register:40f0:8", ["const:4ff360:8", "const:4:8"]]
+ 004ff360 ["CALL", null, ["callee:00547eec:8"]]
- 004dc4c8 bytes e3220194
+ 004ff360 bytes e3220194
- 004dc4d4 ["INT_ADD", "register:40f0:8", ["const:4dc4d4:8", "const:4:8"]]
- 004dc4d4 ["CALL", null, ["callee:00547d84:8"]]
+ 004ff36c ["INT_ADD", "register:40f0:8", ["const:4ff36c:8", "const:4:8"]]
+ 004ff36c ["CALL", null, ["callee:00547d84:8"]]
- 004dc4d4 bytes 86220194
+ 004ff36c bytes 86220194
- 004dc4e4 ["INT_ADD", "register:40f0:8", ["const:4dc4e4:8", "const:4:8"]]
- 004dc4e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ff37c ["INT_ADD", "register:40f0:8", ["const:4ff37c:8", "const:4:8"]]
+ 004ff37c ["CALL", null, ["callee:00c57ab0:8"]]
- 004dc4e4 bytes dffa1b94
+ 004ff37c bytes cd611d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0cc3eedbd341b2cb02bfe55df7a0f0f"></a>

### [`004dc550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc550.md) → [`004ff3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff3e8.md) _ZNK5Botan15AlternativeName8contentsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb20.md) · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdba60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba60.md)
- 新版 呼出元 1件 [`00c59570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59570.md) · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c584b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc550.md#insn-004dc5ec) · [`004dc634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc550.md#insn-004dc634) · [`004dc644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc550.md#insn-004dc644)
- 新版 `004ff484`（命令位置の公開資料なし） · `004ff4cc`（命令位置の公開資料なし） · `004ff4dc`（命令位置の公開資料なし）

~~~diff
- 004dc5ec ["INT_ADD", "register:40f0:8", ["const:4dc5ec:8", "const:4:8"]]
- 004dc5ec ["CALL", null, ["callee:004ff160:8"]]
+ 004ff484 ["INT_ADD", "register:40f0:8", ["const:4ff484:8", "const:4:8"]]
+ 004ff484 ["CALL", null, ["callee:004ff160:8"]]
- 004dc5ec bytes 37ffff97
+ 004ff484 bytes 37ffff97
- 004dc634 ["INT_ADD", "register:40f0:8", ["const:4dc634:8", "const:4:8"]]
- 004dc634 ["CALL", null, ["callee:00c584b0:8"]]
+ 004ff4cc ["INT_ADD", "register:40f0:8", ["const:4ff4cc:8", "const:4:8"]]
+ 004ff4cc ["CALL", null, ["callee:00c584b0:8"]]
- 004dc634 bytes 0bfd1b94
+ 004ff4cc bytes f9631d94
- 004dc644 ["INT_ADD", "register:40f0:8", ["const:4dc644:8", "const:4:8"]]
- 004dc644 ["CALL", null, ["callee:004ff160:8"]]
+ 004ff4dc ["INT_ADD", "register:40f0:8", ["const:4ff4dc:8", "const:4:8"]]
+ 004ff4dc ["CALL", null, ["callee:004ff160:8"]]
- 004dc644 bytes 21ffff97
+ 004ff4dc bytes 21ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02818237973da09b237dc57d63883ee8"></a>

### [`004dc6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc6d0.md) → [`004ff568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff568.md) _ZNK5Botan15AlternativeName9has_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005251c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005251c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc6d0.md#insn-004dc6dc)
- 新版 `004ff574`（命令位置の公開資料なし）

~~~diff
- 004dc6dc ["INT_ADD", "register:40f0:8", ["const:4dc6dc:8", "const:4:8"]]
- 004dc6dc ["CALL", null, ["callee:00548058:8"]]
+ 004ff574 ["INT_ADD", "register:40f0:8", ["const:4ff574:8", "const:4:8"]]
+ 004ff574 ["CALL", null, ["callee:00548058:8"]]
- 004dc6dc bytes b9220194
+ 004ff574 bytes b9220194
~~~


<a id="compare-a40837ecef8df43ba94511660984c3fa"></a>

### [`004dc6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc6f0.md) → [`004ff588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff588.md) _ZNK5Botan15AlternativeName19get_first_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc6f0.md#insn-004dc760) · [`004dc7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc6f0.md#insn-004dc7e8)
- 新版 `004ff5f8`（命令位置の公開資料なし） · `004ff680`（命令位置の公開資料なし）

~~~diff
- 004dc760 ["INT_ADD", "register:40f0:8", ["const:4dc760:8", "const:4:8"]]
- 004dc760 ["CALL", null, ["callee:00c57c50:8"]]
+ 004ff5f8 ["INT_ADD", "register:40f0:8", ["const:4ff5f8:8", "const:4:8"]]
+ 004ff5f8 ["CALL", null, ["callee:00c57c50:8"]]
- 004dc760 bytes a8fa1b94
+ 004ff5f8 bytes 96611d94
- 004dc7e8 ["INT_ADD", "register:40f0:8", ["const:4dc7e8:8", "const:4:8"]]
- 004dc7e8 ["CALL", null, ["callee:00c57c50:8"]]
+ 004ff680 ["INT_ADD", "register:40f0:8", ["const:4ff680:8", "const:4:8"]]
+ 004ff680 ["CALL", null, ["callee:00c57c50:8"]]
- 004dc7e8 bytes 86fa1b94
+ 004ff680 bytes 74611d94
~~~


<a id="compare-d5975fff80bd35b2f90d4efaa9afdd00"></a>

### [`004dc84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc84c.md) → [`004ff6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff6e4.md) _ZNK5Botan15AlternativeName13get_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb30.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`005251c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005251c0.md)
- 新版 呼出元 1件 [`00c59580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59580.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc84c.md#insn-004dc86c) · [`004dc8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc84c.md#insn-004dc8c4) · [`004dc8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc84c.md#insn-004dc8d8)
- 新版 `004ff704`（命令位置の公開資料なし） · `004ff75c`（命令位置の公開資料なし） · `004ff770`（命令位置の公開資料なし）

~~~diff
- 004dc86c ["INT_ADD", "register:40f0:8", ["const:4dc86c:8", "const:4:8"]]
- 004dc86c ["CALL", null, ["callee:00548058:8"]]
+ 004ff704 ["INT_ADD", "register:40f0:8", ["const:4ff704:8", "const:4:8"]]
+ 004ff704 ["CALL", null, ["callee:00548058:8"]]
- 004dc86c bytes 55220194
+ 004ff704 bytes 55220194
- 004dc8c4 ["INT_ADD", "register:40f0:8", ["const:4dc8c4:8", "const:4:8"]]
- 004dc8c4 ["CALL", null, ["callee:00540d3c:8"]]
+ 004ff75c ["INT_ADD", "register:40f0:8", ["const:4ff75c:8", "const:4:8"]]
+ 004ff75c ["CALL", null, ["callee:00540d3c:8"]]
- 004dc8c4 bytes 78050194
+ 004ff75c bytes 78050194
- 004dc8d8 ["INT_ADD", "register:40f0:8", ["const:4dc8d8:8", "const:4:8"]]
- 004dc8d8 ["CALL", null, ["callee:0043bae0:8"]]
+ 004ff770 ["INT_ADD", "register:40f0:8", ["const:4ff770:8", "const:4:8"]]
+ 004ff770 ["CALL", null, ["callee:0043bae0:8"]]
- 004dc8d8 bytes c2f1fc97
+ 004ff770 bytes dcf0fc97
~~~


<a id="compare-59cc926054fcdbd862964318a24410e4"></a>

### [`004dc960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc960.md) → [`004ff7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff7f8.md) _ZNK5Botan15AlternativeName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004dcbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md) [`00bdb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb880.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dc998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc960.md#insn-004dc998) · [`004dc9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc960.md#insn-004dc9cc) · [`004dc9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc960.md#insn-004dc9dc)
- 新版 `004ff830`（命令位置の公開資料なし） · `004ff864`（命令位置の公開資料なし） · `004ff874`（命令位置の公開資料なし）

~~~diff
- 004dc998 ["INT_ADD", "register:40f0:8", ["const:4dc998:8", "const:4:8"]]
- 004dc998 ["CALL", null, ["callee:00c582b0:8"]]
+ 004ff830 ["INT_ADD", "register:40f0:8", ["const:4ff830:8", "const:4:8"]]
+ 004ff830 ["CALL", null, ["callee:00c582b0:8"]]
- 004dc998 bytes b2fb1b94
+ 004ff830 bytes a0621d94
- 004dc9cc ["INT_ADD", "register:40f0:8", ["const:4dc9cc:8", "const:4:8"]]
- 004dc9cc ["CALL", null, ["callee:004ffa6c:8"]]
+ 004ff864 ["INT_ADD", "register:40f0:8", ["const:4ff864:8", "const:4:8"]]
+ 004ff864 ["CALL", null, ["callee:004ffa6c:8"]]
- 004dc9cc bytes 82000094
+ 004ff864 bytes 82000094
- 004dc9dc ["INT_ADD", "register:40f0:8", ["const:4dc9dc:8", "const:4:8"]]
- 004dc9dc ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ff874 ["INT_ADD", "register:40f0:8", ["const:4ff874:8", "const:4:8"]]
+ 004ff874 ["CALL", null, ["callee:00c57ab0:8"]]
- 004dc9dc bytes a1f91b94
+ 004ff874 bytes 8f601d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b44bd51c46452af0e4117cf9fa3c56d"></a>

### [`004de034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de034.md) → [`00500ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500ecc.md) FUN_00500ecc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 2件 [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de034.md#insn-004de050)
- 新版 `00500ee8`（命令位置の公開資料なし）

~~~diff
- 004de050 ["INT_ADD", "register:40f0:8", ["const:4de050:8", "const:4:8"]]
- 004de050 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00500ee8 ["INT_ADD", "register:40f0:8", ["const:500ee8:8", "const:4:8"]]
+ 00500ee8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004de050 bytes 04f41b94
+ 00500ee8 bytes f25a1d94
~~~


<a id="compare-045615be3c5357c216dcb7337c1839eb"></a>

### [`004de69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de69c.md) → [`00501534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501534.md) _ZNK5Botan16X509_CertificateeqERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de69c.md#insn-004de6c8) · [`004de6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de69c.md#insn-004de6d8) · [`004de6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de69c.md#insn-004de6f8)
- 新版 `00501560`（命令位置の公開資料なし） · `00501570`（命令位置の公開資料なし） · `00501590`（命令位置の公開資料なし）

~~~diff
- 004de6c8 ["INT_ADD", "register:40f0:8", ["const:4de6c8:8", "const:4:8"]]
- 004de6c8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00501560 ["INT_ADD", "register:40f0:8", ["const:501560:8", "const:4:8"]]
+ 00501560 ["CALL", null, ["callee:00c57c50:8"]]
- 004de6c8 bytes cef21b94
+ 00501560 bytes bc591d94
- 004de6d8 ["INT_ADD", "register:40f0:8", ["const:4de6d8:8", "const:4:8"]]
- 004de6d8 ["CALL", null, ["callee:00c582a0:8"]]
+ 00501570 ["INT_ADD", "register:40f0:8", ["const:501570:8", "const:4:8"]]
+ 00501570 ["CALL", null, ["callee:00c582a0:8"]]
- 004de6d8 bytes 5ef41b94
+ 00501570 bytes 4c5b1d94
- 004de6f8 ["INT_ADD", "register:40f0:8", ["const:4de6f8:8", "const:4:8"]]
- 004de6f8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00501590 ["INT_ADD", "register:40f0:8", ["const:501590:8", "const:4:8"]]
+ 00501590 ["CALL", null, ["callee:00c57c50:8"]]
- 004de6f8 bytes c2f21b94
+ 00501590 bytes b0591d94
~~~


<a id="compare-f9cebf2df79a613008e8aff0013156dc"></a>

### [`004de718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de718.md) → [`005015b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005015b0.md) FUN_005015b0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00504f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de718.md#insn-004de734) · [`004de754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de718.md#insn-004de754)
- 新版 `005015cc`（命令位置の公開資料なし） · `005015ec`（命令位置の公開資料なし）

~~~diff
- 004de734 ["INT_ADD", "register:40f0:8", ["const:4de734:8", "const:4:8"]]
- 004de734 ["CALL", null, ["callee:00c538e0:8"]]
+ 005015cc ["INT_ADD", "register:40f0:8", ["const:5015cc:8", "const:4:8"]]
+ 005015cc ["CALL", null, ["callee:00c538e0:8"]]
- 004de734 bytes d7e11b94
+ 005015cc bytes c5481d94
- 004de754 ["COPY", "register:0:8", ["register:4040:8"]]
- 004de754 ["INT_ADD", "register:40f0:8", ["const:4de754:8", "const:4:8"]]
- 004de754 ["CALLIND", null, ["register:0:8"]]
+ 005015ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005015ec ["INT_ADD", "register:40f0:8", ["const:5015ec:8", "const:4:8"]]
+ 005015ec ["CALLIND", null, ["register:0:8"]]
- 004de754 bytes 00013fd6
+ 005015ec bytes 00013fd6
~~~


<a id="compare-58aa9da074ddd32dce5a1be8faf9688c"></a>

### [`004de768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de768.md) → [`00501600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501600.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateENSt6__ndk110shared_ptrIKNS_16X509_CertificateEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb90.md) · 呼出先 4件 [`005256c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256c0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb850.md)
- 新版 呼出元 1件 [`00c595e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595e0.md) · 呼出先 4件 [`00548558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de768.md#insn-004de7d4) · [`004de7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de768.md#insn-004de7e4) · [`004de804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de768.md#insn-004de804)
- 新版 `0050166c`（命令位置の公開資料なし） · `0050167c`（命令位置の公開資料なし） · `0050169c`（命令位置の公開資料なし）

~~~diff
- 004de7d4 ["INT_ADD", "register:40f0:8", ["const:4de7d4:8", "const:4:8"]]
- 004de7d4 ["CALL", null, ["callee:00c57c50:8"]]
+ 0050166c ["INT_ADD", "register:40f0:8", ["const:50166c:8", "const:4:8"]]
+ 0050166c ["CALL", null, ["callee:00c57c50:8"]]
- 004de7d4 bytes 8bf21b94
+ 0050166c bytes 79591d94
- 004de7e4 ["INT_ADD", "register:40f0:8", ["const:4de7e4:8", "const:4:8"]]
- 004de7e4 ["CALL", null, ["callee:00c582a0:8"]]
+ 0050167c ["INT_ADD", "register:40f0:8", ["const:50167c:8", "const:4:8"]]
+ 0050167c ["CALL", null, ["callee:00c582a0:8"]]
- 004de7e4 bytes 1bf41b94
+ 0050167c bytes 095b1d94
- 004de804 ["INT_ADD", "register:40f0:8", ["const:4de804:8", "const:4:8"]]
- 004de804 ["CALL", null, ["callee:00c57c50:8"]]
+ 0050169c ["INT_ADD", "register:40f0:8", ["const:50169c:8", "const:4:8"]]
+ 0050169c ["CALL", null, ["callee:00c57c50:8"]]
- 004de804 bytes 7ff21b94
+ 0050169c bytes 6d591d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1df274d590b7618e73c12518965cb43"></a>

### [`004de868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de868.md) → [`00501700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md) _ZNK5Botan27Certificate_Store_In_Memory12all_subjectsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004df920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md) [`0052581c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/0052581c.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de868.md#insn-004de89c) · [`004de8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de868.md#insn-004de8b4) · [`004de8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de868.md#insn-004de8cc)
- 新版 `00501734`（命令位置の公開資料なし） · `0050174c`（命令位置の公開資料なし） · `00501764`（命令位置の公開資料なし）

~~~diff
- 004de89c ["INT_ADD", "register:40f0:8", ["const:4de89c:8", "const:4:8"]]
- 004de89c ["CALL", null, ["callee:005486b4:8"]]
+ 00501734 ["INT_ADD", "register:40f0:8", ["const:501734:8", "const:4:8"]]
+ 00501734 ["CALL", null, ["callee:005486b4:8"]]
- 004de89c bytes e01b0194
+ 00501734 bytes e01b0194
- 004de8b4 ["INT_ADD", "register:40f0:8", ["const:4de8b4:8", "const:4:8"]]
- 004de8b4 ["CALL", null, ["callee:00c595f0:8"]]
+ 0050174c ["INT_ADD", "register:40f0:8", ["const:50174c:8", "const:4:8"]]
+ 0050174c ["CALL", null, ["callee:00c595f0:8"]]
- 004de8b4 bytes bbf81b94
+ 0050174c bytes a95f1d94
- 004de8cc ["INT_ADD", "register:40f0:8", ["const:4de8cc:8", "const:4:8"]]
- 004de8cc ["CALL", null, ["callee:005027b8:8"]]
+ 00501764 ["INT_ADD", "register:40f0:8", ["const:501764:8", "const:4:8"]]
+ 00501764 ["CALL", null, ["callee:005027b8:8"]]
- 004de8cc bytes 15040094
+ 00501764 bytes 15040094
~~~


<a id="compare-2e17c43ed5dd64a9c174d35be1ece4bc"></a>

### [`004de908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de908.md) → [`005017a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017a0.md) _ZNK5Botan16X509_Certificate10subject_dnEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de908.md#insn-004de910)
- 新版 `005017a8`（命令位置の公開資料なし）

~~~diff
- 004de910 ["INT_ADD", "register:40f0:8", ["const:4de910:8", "const:4:8"]]
- 004de910 ["CALL", null, ["callee:00c595f0:8"]]
+ 005017a8 ["INT_ADD", "register:40f0:8", ["const:5017a8:8", "const:4:8"]]
+ 005017a8 ["CALL", null, ["callee:00c595f0:8"]]
- 004de910 bytes a4f81b94
+ 005017a8 bytes 925f1d94
~~~


<a id="compare-c15fc1cd482f8675273b0e28302c3ad9"></a>

### [`004de920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de920.md) → [`005017b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017b8.md) FUN_005017b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de920.md#insn-004de95c) · [`004de978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de920.md#insn-004de978)
- 新版 `005017f4`（命令位置の公開資料なし） · `00501810`（命令位置の公開資料なし）

~~~diff
- 004de95c ["INT_ADD", "register:40f0:8", ["const:4de95c:8", "const:4:8"]]
- 004de95c ["CALL", null, ["callee:0053af50:8"]]
+ 005017f4 ["INT_ADD", "register:40f0:8", ["const:5017f4:8", "const:4:8"]]
+ 005017f4 ["CALL", null, ["callee:0053af50:8"]]
- 004de95c bytes d7e50094
+ 005017f4 bytes d7e50094
- 004de978 ["INT_ADD", "register:40f0:8", ["const:4de978:8", "const:4:8"]]
- 004de978 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00501810 ["INT_ADD", "register:40f0:8", ["const:501810:8", "const:4:8"]]
+ 00501810 ["CALL", null, ["callee:00c57ab0:8"]]
- 004de978 bytes baf11b94
+ 00501810 bytes a8581d94
~~~


<a id="compare-dacb4f438c234acb71b397212220c4bc"></a>

### [`004de9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de9a8.md) → [`00501840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501840.md) _ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbb0.md) · 呼出先 9件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59600.md) · 呼出先 9件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004de9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de9a8.md#insn-004de9f4) · [`004de9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de9a8.md#insn-004de9fc) · [`004dea08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de9a8.md#insn-004dea08)
- 新版 `0050188c`（命令位置の公開資料なし） · `00501894`（命令位置の公開資料なし） · `005018a0`（命令位置の公開資料なし）

~~~diff
- 004de9f4 ["INT_ADD", "register:40f0:8", ["const:4de9f4:8", "const:4:8"]]
- 004de9f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0050188c ["INT_ADD", "register:40f0:8", ["const:50188c:8", "const:4:8"]]
+ 0050188c ["CALL", null, ["callee:00c57ab0:8"]]
- 004de9f4 bytes 9bf11b94
+ 0050188c bytes 89581d94
- 004de9fc ["INT_ADD", "register:40f0:8", ["const:4de9fc:8", "const:4:8"]]
- 004de9fc ["CALL", null, ["callee:00c595f0:8"]]
+ 00501894 ["INT_ADD", "register:40f0:8", ["const:501894:8", "const:4:8"]]
+ 00501894 ["CALL", null, ["callee:00c595f0:8"]]
- 004de9fc bytes 69f81b94
+ 00501894 bytes 575f1d94
- 004dea08 ["INT_ADD", "register:40f0:8", ["const:4dea08:8", "const:4:8"]]
- 004dea08 ["CALL", null, ["callee:00c59610:8"]]
+ 005018a0 ["INT_ADD", "register:40f0:8", ["const:5018a0:8", "const:4:8"]]
+ 005018a0 ["CALL", null, ["callee:00c59610:8"]]
- 004dea08 bytes 6ef81b94
+ 005018a0 bytes 5c5f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c0dd34125952b174952af965781885"></a>

### [`004deb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deb44.md) → [`005019dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019dc.md) _ZNK5Botan16X509_Certificate14subject_key_idEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004deb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deb44.md#insn-004deb4c)
- 新版 `005019e4`（命令位置の公開資料なし）

~~~diff
- 004deb4c ["INT_ADD", "register:40f0:8", ["const:4deb4c:8", "const:4:8"]]
- 004deb4c ["CALL", null, ["callee:00c595f0:8"]]
+ 005019e4 ["INT_ADD", "register:40f0:8", ["const:5019e4:8", "const:4:8"]]
+ 005019e4 ["CALL", null, ["callee:00c595f0:8"]]
- 004deb4c bytes 15f81b94
+ 005019e4 bytes 035f1d94
~~~


<a id="compare-43eac057a8647672638b189da3b24d20"></a>

### [`004deb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deb5c.md) → [`005019f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019f4.md) _ZN5BotaneqERKNS_7X509_DNES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbc0.md) · 呼出先 4件 [`00526790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcaa0.md) [`00bdcbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbd0.md)
- 新版 呼出元 1件 [`00c59610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59610.md) · 呼出先 4件 [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c594f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594f0.md) [`00c59620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004deb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deb5c.md#insn-004deb88) · [`004deb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deb5c.md#insn-004deb94) · [`004dec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deb5c.md#insn-004dec14)
- 新版 `00501a20`（命令位置の公開資料なし） · `00501a2c`（命令位置の公開資料なし） · `00501aac`（命令位置の公開資料なし）

~~~diff
- 004deb88 ["INT_ADD", "register:40f0:8", ["const:4deb88:8", "const:4:8"]]
- 004deb88 ["CALL", null, ["callee:00c59620:8"]]
+ 00501a20 ["INT_ADD", "register:40f0:8", ["const:501a20:8", "const:4:8"]]
+ 00501a20 ["CALL", null, ["callee:00c59620:8"]]
- 004deb88 bytes 12f81b94
+ 00501a20 bytes 005f1d94
- 004deb94 ["INT_ADD", "register:40f0:8", ["const:4deb94:8", "const:4:8"]]
- 004deb94 ["CALL", null, ["callee:00c59620:8"]]
+ 00501a2c ["INT_ADD", "register:40f0:8", ["const:501a2c:8", "const:4:8"]]
+ 00501a2c ["CALL", null, ["callee:00c59620:8"]]
- 004deb94 bytes 0ff81b94
+ 00501a2c bytes fd5e1d94
- 004dec14 ["INT_ADD", "register:40f0:8", ["const:4dec14:8", "const:4:8"]]
- 004dec14 ["CALL", null, ["callee:00c594f0:8"]]
+ 00501aac ["INT_ADD", "register:40f0:8", ["const:501aac:8", "const:4:8"]]
+ 00501aac ["CALL", null, ["callee:00c594f0:8"]]
- 004dec14 bytes a3f71b94
+ 00501aac bytes 915e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-050a1364cbe949350e5c7a9703382e9b"></a>

### [`004ded14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004ded14.md) → [`00501bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501bac.md) _ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbe0.md) · 呼出先 10件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`005256c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256c0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c59630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59630.md) · 呼出先 10件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00548558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ded68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004ded14.md#insn-004ded68) · [`004ded88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004ded14.md#insn-004ded88) · [`004dedac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004ded14.md#insn-004dedac)
- 新版 `00501c00`（命令位置の公開資料なし） · `00501c20`（命令位置の公開資料なし） · `00501c44`（命令位置の公開資料なし）

~~~diff
- 004ded68 ["INT_ADD", "register:40f0:8", ["const:4ded68:8", "const:4:8"]]
- 004ded68 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00501c00 ["INT_ADD", "register:40f0:8", ["const:501c00:8", "const:4:8"]]
+ 00501c00 ["CALL", null, ["callee:00c57ab0:8"]]
- 004ded68 bytes bef01b94
+ 00501c00 bytes ac571d94
- 004ded88 ["INT_ADD", "register:40f0:8", ["const:4ded88:8", "const:4:8"]]
- 004ded88 ["CALL", null, ["callee:00c595f0:8"]]
+ 00501c20 ["INT_ADD", "register:40f0:8", ["const:501c20:8", "const:4:8"]]
+ 00501c20 ["CALL", null, ["callee:00c595f0:8"]]
- 004ded88 bytes 86f71b94
+ 00501c20 bytes 745e1d94
- 004dedac ["INT_ADD", "register:40f0:8", ["const:4dedac:8", "const:4:8"]]
- 004dedac ["CALL", null, ["callee:00c57a90:8"]]
+ 00501c44 ["INT_ADD", "register:40f0:8", ["const:501c44:8", "const:4:8"]]
+ 00501c44 ["CALL", null, ["callee:00c57a90:8"]]
- 004dedac bytes a5f01b94
+ 00501c44 bytes 93571d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c2c7bccaccf9e5143f9c04ca0378384"></a>

### [`004deee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deee0.md) → [`00501d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501d78.md) FUN_00501d78

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00509f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004def2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deee0.md#insn-004def2c) · [`004def40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deee0.md#insn-004def40) · [`004def48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deee0.md#insn-004def48)
- 新版 `00501dc4`（命令位置の公開資料なし） · `00501dd8`（命令位置の公開資料なし） · `00501de0`（命令位置の公開資料なし）

~~~diff
- 004def2c ["INT_ADD", "register:40f0:8", ["const:4def2c:8", "const:4:8"]]
- 004def2c ["CALL", null, ["callee:00c538e0:8"]]
+ 00501dc4 ["INT_ADD", "register:40f0:8", ["const:501dc4:8", "const:4:8"]]
+ 00501dc4 ["CALL", null, ["callee:00c538e0:8"]]
- 004def2c bytes d9df1b94
+ 00501dc4 bytes c7461d94
- 004def40 ["COPY", "register:0:8", ["register:4040:8"]]
- 004def40 ["INT_ADD", "register:40f0:8", ["const:4def40:8", "const:4:8"]]
- 004def40 ["CALLIND", null, ["register:0:8"]]
+ 00501dd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00501dd8 ["INT_ADD", "register:40f0:8", ["const:501dd8:8", "const:4:8"]]
+ 00501dd8 ["CALLIND", null, ["register:0:8"]]
- 004def40 bytes 00013fd6
+ 00501dd8 bytes 00013fd6
- 004def48 ["INT_ADD", "register:40f0:8", ["const:4def48:8", "const:4:8"]]
- 004def48 ["CALL", null, ["callee:00c57a80:8"]]
+ 00501de0 ["INT_ADD", "register:40f0:8", ["const:501de0:8", "const:4:8"]]
+ 00501de0 ["CALL", null, ["callee:00c57a80:8"]]
- 004def48 bytes 3af01b94
+ 00501de0 bytes 28571d94
~~~


<a id="compare-1b6ed050bc97e787f00ef83c1719a34c"></a>

### [`004df278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df278.md) → [`00502110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502110.md) _ZNK5Botan16X509_Certificate28subject_public_key_bitstringEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004df280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df278.md#insn-004df280)
- 新版 `00502118`（命令位置の公開資料なし）

~~~diff
- 004df280 ["INT_ADD", "register:40f0:8", ["const:4df280:8", "const:4:8"]]
- 004df280 ["CALL", null, ["callee:00c595f0:8"]]
+ 00502118 ["INT_ADD", "register:40f0:8", ["const:502118:8", "const:4:8"]]
+ 00502118 ["CALL", null, ["callee:00c595f0:8"]]
- 004df280 bytes 48f61b94
+ 00502118 bytes 365d1d94
~~~


<a id="compare-eff9970a14797c55a187c6db3e4067f0"></a>

### [`004df598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df598.md) → [`00502430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502430.md) _ZNK5Botan16X509_Certificate14raw_subject_dnEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004df5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df598.md#insn-004df5a0)
- 新版 `00502438`（命令位置の公開資料なし）

~~~diff
- 004df5a0 ["INT_ADD", "register:40f0:8", ["const:4df5a0:8", "const:4:8"]]
- 004df5a0 ["CALL", null, ["callee:00c595f0:8"]]
+ 00502438 ["INT_ADD", "register:40f0:8", ["const:502438:8", "const:4:8"]]
+ 00502438 ["CALL", null, ["callee:00c595f0:8"]]
- 004df5a0 bytes 80f51b94
+ 00502438 bytes 6e5c1d94
~~~


<a id="compare-193526cff188f88e687ccb9b0251b3c8"></a>

### [`004df724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df724.md) → [`005025bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbf0.md) · 呼出先 11件 [`004df920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00525ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ce8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c59640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59640.md) · 呼出先 11件 [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00548b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004df758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df724.md#insn-004df758) · [`004df764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df724.md#insn-004df764) · [`004df77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df724.md#insn-004df77c)
- 新版 `005025f0`（命令位置の公開資料なし） · `005025fc`（命令位置の公開資料なし） · `00502614`（命令位置の公開資料なし）

~~~diff
- 004df758 ["INT_ADD", "register:40f0:8", ["const:4df758:8", "const:4:8"]]
- 004df758 ["CALL", null, ["callee:00c59650:8"]]
+ 005025f0 ["INT_ADD", "register:40f0:8", ["const:5025f0:8", "const:4:8"]]
+ 005025f0 ["CALL", null, ["callee:00c59650:8"]]
- 004df758 bytes 2af51b94
+ 005025f0 bytes 185c1d94
- 004df764 ["INT_ADD", "register:40f0:8", ["const:4df764:8", "const:4:8"]]
- 004df764 ["CALL", null, ["callee:005027b8:8"]]
+ 005025fc ["INT_ADD", "register:40f0:8", ["const:5025fc:8", "const:4:8"]]
+ 005025fc ["CALL", null, ["callee:005027b8:8"]]
- 004df764 bytes 6f000094
+ 005025fc bytes 6f000094
- 004df77c ["INT_ADD", "register:40f0:8", ["const:4df77c:8", "const:4:8"]]
- 004df77c ["CALL", null, ["callee:00c59650:8"]]
+ 00502614 ["INT_ADD", "register:40f0:8", ["const:502614:8", "const:4:8"]]
+ 00502614 ["CALL", null, ["callee:00c59650:8"]]
- 004df77c bytes 21f51b94
+ 00502614 bytes 0f5c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2878d85ef53c95af63b1491f9f011ce"></a>

### [`004df8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df8cc.md) → [`00502764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502764.md) FUN_00502764

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004df8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df8cc.md#insn-004df8e8) · [`004df908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df8cc.md#insn-004df908)
- 新版 `00502780`（命令位置の公開資料なし） · `005027a0`（命令位置の公開資料なし）

~~~diff
- 004df8e8 ["INT_ADD", "register:40f0:8", ["const:4df8e8:8", "const:4:8"]]
- 004df8e8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00502780 ["INT_ADD", "register:40f0:8", ["const:502780:8", "const:4:8"]]
+ 00502780 ["CALL", null, ["callee:00c538e0:8"]]
- 004df8e8 bytes 6add1b94
+ 00502780 bytes 58441d94
- 004df908 ["COPY", "register:0:8", ["register:4040:8"]]
- 004df908 ["INT_ADD", "register:40f0:8", ["const:4df908:8", "const:4:8"]]
- 004df908 ["CALLIND", null, ["register:0:8"]]
+ 005027a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005027a0 ["INT_ADD", "register:40f0:8", ["const:5027a0:8", "const:4:8"]]
+ 005027a0 ["CALLIND", null, ["register:0:8"]]
- 004df908 bytes 00013fd6
+ 005027a0 bytes 00013fd6
~~~


<a id="compare-7b715fb039fea53698d8b68f8be4c3a7"></a>

### [`004dfa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfa4c.md) → [`005028e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028e4.md) _ZNK5Botan8X509_CRL11this_updateEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dfa54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfa4c.md#insn-004dfa54)
- 新版 `005028ec`（命令位置の公開資料なし）

~~~diff
- 004dfa54 ["INT_ADD", "register:40f0:8", ["const:4dfa54:8", "const:4:8"]]
- 004dfa54 ["CALL", null, ["callee:00c59650:8"]]
+ 005028ec ["INT_ADD", "register:40f0:8", ["const:5028ec:8", "const:4:8"]]
+ 005028ec ["CALL", null, ["callee:00c59650:8"]]
- 004dfa54 bytes 6bf41b94
+ 005028ec bytes 595b1d94
~~~


<a id="compare-0caeb021fd1dc9d233508d3490ed8d6b"></a>

### [`004dfa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfa64.md) → [`005028fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028fc.md) _ZNK5Botan27Certificate_Store_In_Memory12find_crl_forERKNS_16X509_CertificateE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfa64.md#insn-004dfaa0) · [`004dfabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfa64.md#insn-004dfabc) · [`004dfac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfa64.md#insn-004dfac4)
- 新版 `00502938`（命令位置の公開資料なし） · `00502954`（命令位置の公開資料なし） · `0050295c`（命令位置の公開資料なし）

~~~diff
- 004dfaa0 ["INT_ADD", "register:40f0:8", ["const:4dfaa0:8", "const:4:8"]]
- 004dfaa0 ["CALL", null, ["callee:00c595f0:8"]]
+ 00502938 ["INT_ADD", "register:40f0:8", ["const:502938:8", "const:4:8"]]
+ 00502938 ["CALL", null, ["callee:00c595f0:8"]]
- 004dfaa0 bytes 40f41b94
+ 00502938 bytes 2e5b1d94
- 004dfabc ["INT_ADD", "register:40f0:8", ["const:4dfabc:8", "const:4:8"]]
- 004dfabc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00502954 ["INT_ADD", "register:40f0:8", ["const:502954:8", "const:4:8"]]
+ 00502954 ["CALL", null, ["callee:00c57ab0:8"]]
- 004dfabc bytes 69ed1b94
+ 00502954 bytes 57541d94
- 004dfac4 ["INT_ADD", "register:40f0:8", ["const:4dfac4:8", "const:4:8"]]
- 004dfac4 ["CALL", null, ["callee:00c59650:8"]]
+ 0050295c ["INT_ADD", "register:40f0:8", ["const:50295c:8", "const:4:8"]]
+ 0050295c ["CALL", null, ["callee:00c59650:8"]]
- 004dfac4 bytes 4ff41b94
+ 0050295c bytes 3d5b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a65d9d41de5bf3c7b9e78b67016c4326"></a>

### [`004dfc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc1c.md) → [`00502ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ab4.md) _ZNK5Botan16X509_Certificate16authority_key_idEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dfc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc1c.md#insn-004dfc24)
- 新版 `00502abc`（命令位置の公開資料なし）

~~~diff
- 004dfc24 ["INT_ADD", "register:40f0:8", ["const:4dfc24:8", "const:4:8"]]
- 004dfc24 ["CALL", null, ["callee:00c595f0:8"]]
+ 00502abc ["INT_ADD", "register:40f0:8", ["const:502abc:8", "const:4:8"]]
+ 00502abc ["CALL", null, ["callee:00c595f0:8"]]
- 004dfc24 bytes dff31b94
+ 00502abc bytes cd5a1d94
~~~


<a id="compare-08130ff64e873d12c0b07f14b28142d5"></a>

### [`004dfc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc34.md) → [`00502acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502acc.md) _ZNK5Botan8X509_CRL16authority_key_idEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dfc3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc34.md#insn-004dfc3c)
- 新版 `00502ad4`（命令位置の公開資料なし）

~~~diff
- 004dfc3c ["INT_ADD", "register:40f0:8", ["const:4dfc3c:8", "const:4:8"]]
- 004dfc3c ["CALL", null, ["callee:00c59650:8"]]
+ 00502ad4 ["INT_ADD", "register:40f0:8", ["const:502ad4:8", "const:4:8"]]
+ 00502ad4 ["CALL", null, ["callee:00c59650:8"]]
- 004dfc3c bytes f1f31b94
+ 00502ad4 bytes df5a1d94
~~~


<a id="compare-33b5ced2eab31601c0ca1fae4ef9698b"></a>

### [`004dfc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc4c.md) → [`00502ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ae4.md) _ZNK5Botan16X509_Certificate9issuer_dnEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dfc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc4c.md#insn-004dfc54)
- 新版 `00502aec`（命令位置の公開資料なし）

~~~diff
- 004dfc54 ["INT_ADD", "register:40f0:8", ["const:4dfc54:8", "const:4:8"]]
- 004dfc54 ["CALL", null, ["callee:00c595f0:8"]]
+ 00502aec ["INT_ADD", "register:40f0:8", ["const:502aec:8", "const:4:8"]]
+ 00502aec ["CALL", null, ["callee:00c595f0:8"]]
- 004dfc54 bytes d3f31b94
+ 00502aec bytes c15a1d94
~~~


<a id="compare-9addedb8a15098798160b558c1bf22aa"></a>

### [`004dfccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfccc.md) → [`00502b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502b64.md) FUN_00502b64

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004dfd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfccc.md#insn-004dfd18) · [`004dfd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfccc.md#insn-004dfd2c) · [`004dfd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfccc.md#insn-004dfd34)
- 新版 `00502bb0`（命令位置の公開資料なし） · `00502bc4`（命令位置の公開資料なし） · `00502bcc`（命令位置の公開資料なし）

~~~diff
- 004dfd18 ["INT_ADD", "register:40f0:8", ["const:4dfd18:8", "const:4:8"]]
- 004dfd18 ["CALL", null, ["callee:00c538e0:8"]]
+ 00502bb0 ["INT_ADD", "register:40f0:8", ["const:502bb0:8", "const:4:8"]]
+ 00502bb0 ["CALL", null, ["callee:00c538e0:8"]]
- 004dfd18 bytes 5edc1b94
+ 00502bb0 bytes 4c431d94
- 004dfd2c ["COPY", "register:0:8", ["register:4040:8"]]
- 004dfd2c ["INT_ADD", "register:40f0:8", ["const:4dfd2c:8", "const:4:8"]]
- 004dfd2c ["CALLIND", null, ["register:0:8"]]
+ 00502bc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502bc4 ["INT_ADD", "register:40f0:8", ["const:502bc4:8", "const:4:8"]]
+ 00502bc4 ["CALLIND", null, ["register:0:8"]]
- 004dfd2c bytes 00013fd6
+ 00502bc4 bytes 00013fd6
- 004dfd34 ["INT_ADD", "register:40f0:8", ["const:4dfd34:8", "const:4:8"]]
- 004dfd34 ["CALL", null, ["callee:00c57a80:8"]]
+ 00502bcc ["INT_ADD", "register:40f0:8", ["const:502bcc:8", "const:4:8"]]
+ 00502bcc ["CALL", null, ["callee:00c57a80:8"]]
- 004dfd34 bytes bfec1b94
+ 00502bcc bytes ad531d94
~~~


<a id="compare-12e42cecf557980db43b979f67ef10a3"></a>

### [`004dffe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dffe8.md) → [`00502e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502e80.md) FUN_00502e80

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dffe8.md#insn-004e0004) · [`004e0024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dffe8.md#insn-004e0024)
- 新版 `00502e9c`（命令位置の公開資料なし） · `00502ebc`（命令位置の公開資料なし）

~~~diff
- 004e0004 ["INT_ADD", "register:40f0:8", ["const:4e0004:8", "const:4:8"]]
- 004e0004 ["CALL", null, ["callee:00c538e0:8"]]
+ 00502e9c ["INT_ADD", "register:40f0:8", ["const:502e9c:8", "const:4:8"]]
+ 00502e9c ["CALL", null, ["callee:00c538e0:8"]]
- 004e0004 bytes a3db1b94
+ 00502e9c bytes 91421d94
- 004e0024 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e0024 ["INT_ADD", "register:40f0:8", ["const:4e0024:8", "const:4:8"]]
- 004e0024 ["CALLIND", null, ["register:0:8"]]
+ 00502ebc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502ebc ["INT_ADD", "register:40f0:8", ["const:502ebc:8", "const:4:8"]]
+ 00502ebc ["CALLIND", null, ["register:0:8"]]
- 004e0024 bytes 00013fd6
+ 00502ebc bytes 00013fd6
~~~


<a id="compare-d8dba5cc63d2f561d6b90b96fa9fd64c"></a>

### [`004e05e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e05e8.md) → [`00503480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503480.md) FUN_00503480

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e0604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e05e8.md#insn-004e0604) · [`004e0624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e05e8.md#insn-004e0624)
- 新版 `0050349c`（命令位置の公開資料なし） · `005034bc`（命令位置の公開資料なし）

~~~diff
- 004e0604 ["INT_ADD", "register:40f0:8", ["const:4e0604:8", "const:4:8"]]
- 004e0604 ["CALL", null, ["callee:00c538e0:8"]]
+ 0050349c ["INT_ADD", "register:40f0:8", ["const:50349c:8", "const:4:8"]]
+ 0050349c ["CALL", null, ["callee:00c538e0:8"]]
- 004e0604 bytes 23da1b94
+ 0050349c bytes 11411d94
- 004e0624 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e0624 ["INT_ADD", "register:40f0:8", ["const:4e0624:8", "const:4:8"]]
- 004e0624 ["CALLIND", null, ["register:0:8"]]
+ 005034bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005034bc ["INT_ADD", "register:40f0:8", ["const:5034bc:8", "const:4:8"]]
+ 005034bc ["CALLIND", null, ["register:0:8"]]
- 004e0624 bytes 00013fd6
+ 005034bc bytes 00013fd6
~~~


<a id="compare-5e83139fc8ee786d215c9c67c5e15d64"></a>

### [`004e0638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0638.md) → [`005034d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005034d0.md) _ZN5BotaneqERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc40.md) · 呼出先 3件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md) [`00bdcc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc50.md)
- 新版 呼出元 1件 [`00c59690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59690.md) · 呼出先 3件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md) [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e0650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0638.md#insn-004e0650) · [`004e065c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0638.md#insn-004e065c) · [`004e067c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0638.md#insn-004e067c)
- 新版 `005034e8`（命令位置の公開資料なし） · `005034f4`（命令位置の公開資料なし） · `00503514`（命令位置の公開資料なし）

~~~diff
- 004e0650 ["INT_ADD", "register:40f0:8", ["const:4e0650:8", "const:4:8"]]
- 004e0650 ["CALL", null, ["callee:00c596a0:8"]]
+ 005034e8 ["INT_ADD", "register:40f0:8", ["const:5034e8:8", "const:4:8"]]
+ 005034e8 ["CALL", null, ["callee:00c596a0:8"]]
- 004e0650 bytes 80f11b94
+ 005034e8 bytes 6e581d94
- 004e065c ["INT_ADD", "register:40f0:8", ["const:4e065c:8", "const:4:8"]]
- 004e065c ["CALL", null, ["callee:00c596a0:8"]]
+ 005034f4 ["INT_ADD", "register:40f0:8", ["const:5034f4:8", "const:4:8"]]
+ 005034f4 ["CALL", null, ["callee:00c596a0:8"]]
- 004e065c bytes 7df11b94
+ 005034f4 bytes 6b581d94
- 004e067c ["INT_ADD", "register:40f0:8", ["const:4e067c:8", "const:4:8"]]
- 004e067c ["CALL", null, ["callee:00c57c50:8"]]
+ 00503514 ["INT_ADD", "register:40f0:8", ["const:503514:8", "const:4:8"]]
+ 00503514 ["CALL", null, ["callee:00c57c50:8"]]
- 004e067c bytes e1ea1b94
+ 00503514 bytes cf511d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2e4bc99d61ae70d7d3cea43cfeb2396"></a>

### [`004e06e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e06e8.md) → [`00503580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503580.md) _ZNK5Botan9CRL_Entry11expire_timeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e06e8.md#insn-004e06f0)
- 新版 `00503588`（命令位置の公開資料なし）

~~~diff
- 004e06f0 ["INT_ADD", "register:40f0:8", ["const:4e06f0:8", "const:4:8"]]
- 004e06f0 ["CALL", null, ["callee:00c596a0:8"]]
+ 00503588 ["INT_ADD", "register:40f0:8", ["const:503588:8", "const:4:8"]]
+ 00503588 ["CALL", null, ["callee:00c596a0:8"]]
- 004e06f0 bytes 58f11b94
+ 00503588 bytes 46581d94
~~~


<a id="compare-a9cfcd167f0c83d21a088abd132b094c"></a>

### [`004e0700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0700.md) → [`00503598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503598.md) _ZNK5Botan9CRL_Entry11reason_codeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e0708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0700.md#insn-004e0708)
- 新版 `005035a0`（命令位置の公開資料なし）

~~~diff
- 004e0708 ["INT_ADD", "register:40f0:8", ["const:4e0708:8", "const:4:8"]]
- 004e0708 ["CALL", null, ["callee:00c596a0:8"]]
+ 005035a0 ["INT_ADD", "register:40f0:8", ["const:5035a0:8", "const:4:8"]]
+ 005035a0 ["CALL", null, ["callee:00c596a0:8"]]
- 004e0708 bytes 52f11b94
+ 005035a0 bytes 40581d94
~~~


<a id="compare-ae72b435bd2bd90fb3a13a462710e032"></a>

### [`004e0718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0718.md) → [`005035b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005035b0.md) _ZN5BotanneERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59690.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e0720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0718.md#insn-004e0720)
- 新版 `005035b8`（命令位置の公開資料なし）

~~~diff
- 004e0720 ["INT_ADD", "register:40f0:8", ["const:4e0720:8", "const:4:8"]]
- 004e0720 ["CALL", null, ["callee:00c59690:8"]]
+ 005035b8 ["INT_ADD", "register:40f0:8", ["const:5035b8:8", "const:4:8"]]
+ 005035b8 ["CALL", null, ["callee:00c59690:8"]]
- 004e0720 bytes 48f11b94
+ 005035b8 bytes 36581d94
~~~


<a id="compare-92cc5e3fe74f474849cd824bddd52c79"></a>

### [`004e087c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e087c.md) → [`00503714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503714.md) _ZNK5Botan9CRL_Entry10extensionsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e0884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e087c.md#insn-004e0884)
- 新版 `0050371c`（命令位置の公開資料なし）

~~~diff
- 004e0884 ["INT_ADD", "register:40f0:8", ["const:4e0884:8", "const:4:8"]]
- 004e0884 ["CALL", null, ["callee:00c596a0:8"]]
+ 0050371c ["INT_ADD", "register:40f0:8", ["const:50371c:8", "const:4:8"]]
+ 0050371c ["CALL", null, ["callee:00c596a0:8"]]
- 004e0884 bytes f3f01b94
+ 0050371c bytes e1571d94
~~~


<a id="compare-e46d2af122cf3894dbfd3b22f8c9e8f4"></a>

### [`004e0ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0ec0.md) → [`00503d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503d58.md) _ZNK5Botan10Data_StoreeqERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005260b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005260b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00548f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548f48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e0f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0ec0.md#insn-004e0f0c)
- 新版 `00503da4`（命令位置の公開資料なし）

~~~diff
- 004e0f0c ["INT_ADD", "register:40f0:8", ["const:4e0f0c:8", "const:4:8"]]
- 004e0f0c ["CALL", null, ["callee:00548f48:8"]]
+ 00503da4 ["INT_ADD", "register:40f0:8", ["const:503da4:8", "const:4:8"]]
+ 00503da4 ["CALL", null, ["callee:00548f48:8"]]
- 004e0f0c bytes 69140194
+ 00503da4 bytes 69140194
~~~


<a id="compare-b6249b800e4a781b98fe5c5dc779b98f"></a>

### [`004e0f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0f9c.md) → [`00503e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503e34.md) _ZNK5Botan10Data_Store9has_valueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e1008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0f9c.md#insn-004e1008)
- 新版 `00503ea0`（命令位置の公開資料なし）

~~~diff
- 004e1008 ["INT_ADD", "register:40f0:8", ["const:4e1008:8", "const:4:8"]]
- 004e1008 ["CALL", null, ["callee:00c57c50:8"]]
+ 00503ea0 ["INT_ADD", "register:40f0:8", ["const:503ea0:8", "const:4:8"]]
+ 00503ea0 ["CALL", null, ["callee:00c57c50:8"]]
- 004e1008 bytes 7ee81b94
+ 00503ea0 bytes 6c4f1d94
~~~


<a id="compare-bcf9f055877c777c75747d2814222791"></a>

### [`004e105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e105c.md) → [`00503ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503ef4.md) _ZNK5Botan10Data_Store10search_forENSt6__ndk18functionIFbNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_EEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc80.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`005261fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005261fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c596d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596d0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e10ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e105c.md#insn-004e10ec) · [`004e1118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e105c.md#insn-004e1118) · [`004e1134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e105c.md#insn-004e1134)
- 新版 `00503f84`（命令位置の公開資料なし） · `00503fb0`（命令位置の公開資料なし） · `00503fcc`（命令位置の公開資料なし）

~~~diff
- 004e10ec ["INT_ADD", "register:40f0:8", ["const:4e10ec:8", "const:4:8"]]
- 004e10ec ["CALL", null, ["callee:0043bae0:8"]]
+ 00503f84 ["INT_ADD", "register:40f0:8", ["const:503f84:8", "const:4:8"]]
+ 00503f84 ["CALL", null, ["callee:0043bae0:8"]]
- 004e10ec bytes bddffc97
+ 00503f84 bytes d7defc97
- 004e1118 ["INT_ADD", "register:40f0:8", ["const:4e1118:8", "const:4:8"]]
- 004e1118 ["CALL", null, ["callee:0043bae0:8"]]
+ 00503fb0 ["INT_ADD", "register:40f0:8", ["const:503fb0:8", "const:4:8"]]
+ 00503fb0 ["CALL", null, ["callee:0043bae0:8"]]
- 004e1118 bytes b2dffc97
+ 00503fb0 bytes ccdefc97
- 004e1134 ["COPY", "register:0:8", ["register:4040:8"]]
- 004e1134 ["INT_ADD", "register:40f0:8", ["const:4e1134:8", "const:4:8"]]
- 004e1134 ["CALLIND", null, ["register:0:8"]]
+ 00503fcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00503fcc ["INT_ADD", "register:40f0:8", ["const:503fcc:8", "const:4:8"]]
+ 00503fcc ["CALLIND", null, ["register:0:8"]]
- 004e1134 bytes 00013fd6
+ 00503fcc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cf067314fdac1c0a7bbf2141e67de7f"></a>

### [`004e12e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e12e8.md) → [`00504180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504180.md) _ZNK5Botan10Data_Store3getERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc90.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`005251c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005251c0.md)
- 新版 呼出元 1件 [`00c596e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596e0.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e1304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e12e8.md#insn-004e1304) · [`004e135c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e12e8.md#insn-004e135c) · [`004e1370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e12e8.md#insn-004e1370)
- 新版 `0050419c`（命令位置の公開資料なし） · `005041f4`（命令位置の公開資料なし） · `00504208`（命令位置の公開資料なし）

~~~diff
- 004e1304 ["INT_ADD", "register:40f0:8", ["const:4e1304:8", "const:4:8"]]
- 004e1304 ["CALL", null, ["callee:00548058:8"]]
+ 0050419c ["INT_ADD", "register:40f0:8", ["const:50419c:8", "const:4:8"]]
+ 0050419c ["CALL", null, ["callee:00548058:8"]]
- 004e1304 bytes af0f0194
+ 0050419c bytes af0f0194
- 004e135c ["INT_ADD", "register:40f0:8", ["const:4e135c:8", "const:4:8"]]
- 004e135c ["CALL", null, ["callee:00540d3c:8"]]
+ 005041f4 ["INT_ADD", "register:40f0:8", ["const:5041f4:8", "const:4:8"]]
+ 005041f4 ["CALL", null, ["callee:00540d3c:8"]]
- 004e135c bytes d2f20094
+ 005041f4 bytes d2f20094
- 004e1370 ["INT_ADD", "register:40f0:8", ["const:4e1370:8", "const:4:8"]]
- 004e1370 ["CALL", null, ["callee:0043bae0:8"]]
+ 00504208 ["INT_ADD", "register:40f0:8", ["const:504208:8", "const:4:8"]]
+ 00504208 ["CALL", null, ["callee:0043bae0:8"]]
- 004e1370 bytes 1cdffc97
+ 00504208 bytes 36defc97
~~~


<a id="compare-dffe8e3eb212d62446a5a4561eed116c"></a>

### [`004e1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1af0.md) → [`00504988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504988.md) _ZN5Botan10Data_Store3addERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e1b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1af0.md#insn-004e1b20) · [`004e1b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1af0.md#insn-004e1b30) · [`004e1b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1af0.md#insn-004e1b40)
- 新版 `005049b8`（命令位置の公開資料なし） · `005049c8`（命令位置の公開資料なし） · `005049d8`（命令位置の公開資料なし）

~~~diff
- 004e1b20 ["INT_ADD", "register:40f0:8", ["const:4e1b20:8", "const:4:8"]]
- 004e1b20 ["CALL", null, ["callee:00c58390:8"]]
+ 005049b8 ["INT_ADD", "register:40f0:8", ["const:5049b8:8", "const:4:8"]]
+ 005049b8 ["CALL", null, ["callee:00c58390:8"]]
- 004e1b20 bytes 88e71b94
+ 005049b8 bytes 764e1d94
- 004e1b30 ["INT_ADD", "register:40f0:8", ["const:4e1b30:8", "const:4:8"]]
- 004e1b30 ["CALL", null, ["callee:004ff160:8"]]
+ 005049c8 ["INT_ADD", "register:40f0:8", ["const:5049c8:8", "const:4:8"]]
+ 005049c8 ["CALL", null, ["callee:004ff160:8"]]
- 004e1b30 bytes e6e9ff97
+ 005049c8 bytes e6e9ff97
- 004e1b40 ["INT_ADD", "register:40f0:8", ["const:4e1b40:8", "const:4:8"]]
- 004e1b40 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005049d8 ["INT_ADD", "register:40f0:8", ["const:5049d8:8", "const:4:8"]]
+ 005049d8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e1b40 bytes 48e51b94
+ 005049d8 bytes 364c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a06db59516ce978d9c3107f8cbaf299"></a>

### [`004e1eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1eb8.md) → [`00504d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504d50.md) _ZN5Botan10Data_Store3addERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pai

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00518c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e1ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1eb8.md#insn-004e1ef4)
- 新版 `00504d8c`（命令位置の公開資料なし）

~~~diff
- 004e1ef4 ["INT_ADD", "register:40f0:8", ["const:4e1ef4:8", "const:4:8"]]
- 004e1ef4 ["CALL", null, ["callee:0053bb30:8"]]
+ 00504d8c ["INT_ADD", "register:40f0:8", ["const:504d8c:8", "const:4:8"]]
+ 00504d8c ["CALL", null, ["callee:0053bb30:8"]]
- 004e1ef4 bytes 69db0094
+ 00504d8c bytes 69db0094
~~~


<a id="compare-2d0762374417e156420ac175d2d608fd"></a>

### [`004e20fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e20fc.md) → [`00504f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504f94.md) _ZN5Botan7X509_DN13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdccb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e212c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e20fc.md#insn-004e212c) · [`004e213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e20fc.md#insn-004e213c) · [`004e214c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e20fc.md#insn-004e214c)
- 新版 `00504fc4`（命令位置の公開資料なし） · `00504fd4`（命令位置の公開資料なし） · `00504fe4`（命令位置の公開資料なし）

~~~diff
- 004e212c ["INT_ADD", "register:40f0:8", ["const:4e212c:8", "const:4:8"]]
- 004e212c ["CALL", null, ["callee:00c58280:8"]]
+ 00504fc4 ["INT_ADD", "register:40f0:8", ["const:504fc4:8", "const:4:8"]]
+ 00504fc4 ["CALL", null, ["callee:00c58280:8"]]
- 004e212c bytes c1e51b94
+ 00504fc4 bytes af4c1d94
- 004e213c ["INT_ADD", "register:40f0:8", ["const:4e213c:8", "const:4:8"]]
- 004e213c ["CALL", null, ["callee:00c59700:8"]]
+ 00504fd4 ["INT_ADD", "register:40f0:8", ["const:504fd4:8", "const:4:8"]]
+ 00504fd4 ["CALL", null, ["callee:00c59700:8"]]
- 004e213c bytes ddea1b94
+ 00504fd4 bytes cb511d94
- 004e214c ["INT_ADD", "register:40f0:8", ["const:4e214c:8", "const:4:8"]]
- 004e214c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00504fe4 ["INT_ADD", "register:40f0:8", ["const:504fe4:8", "const:4:8"]]
+ 00504fe4 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e214c bytes c5e31b94
+ 00504fe4 bytes b34a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38d2b2dc675b0a1eddfc623373394b6d"></a>

### [`004e23fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e23fc.md) → [`00505294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505294.md) FUN_00505294

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 2件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e2414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e23fc.md#insn-004e2414)
- 新版 `005052ac`（命令位置の公開資料なし）

~~~diff
- 004e2414 ["INT_ADD", "register:40f0:8", ["const:4e2414:8", "const:4:8"]]
- 004e2414 ["CALL", null, ["callee:0053af50:8"]]
+ 005052ac ["INT_ADD", "register:40f0:8", ["const:5052ac:8", "const:4:8"]]
+ 005052ac ["CALL", null, ["callee:0053af50:8"]]
- 004e2414 bytes 29d70094
+ 005052ac bytes 29d70094
~~~


<a id="compare-a70730fe46b74ceef6bc949cb1b5924c"></a>

### [`004e4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bdc.md) → [`00507a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a74.md) _ZNK5Botan16X509_Certificate16subject_alt_nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bdc.md#insn-004e4be4)
- 新版 `00507a7c`（命令位置の公開資料なし）

~~~diff
- 004e4be4 ["INT_ADD", "register:40f0:8", ["const:4e4be4:8", "const:4:8"]]
- 004e4be4 ["CALL", null, ["callee:00c595f0:8"]]
+ 00507a7c ["INT_ADD", "register:40f0:8", ["const:507a7c:8", "const:4:8"]]
+ 00507a7c ["CALL", null, ["callee:00c595f0:8"]]
- 004e4be4 bytes efdf1b94
+ 00507a7c bytes dd461d94
~~~


<a id="compare-cf166648778c0dd0586911edb099fd3b"></a>

### [`004e4f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4f2c.md) → [`00507dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507dc4.md) _ZNK5Botan7X509_DN13get_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd10.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`0052839c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052839c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59760.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`0054b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b234.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e4f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4f2c.md#insn-004e4f60) · [`004e4f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4f2c.md#insn-004e4f6c) · [`004e4f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4f2c.md#insn-004e4f7c)
- 新版 `00507df8`（命令位置の公開資料なし） · `00507e04`（命令位置の公開資料なし） · `00507e14`（命令位置の公開資料なし）

~~~diff
- 004e4f60 ["INT_ADD", "register:40f0:8", ["const:4e4f60:8", "const:4:8"]]
- 004e4f60 ["CALL", null, ["callee:00c59770:8"]]
+ 00507df8 ["INT_ADD", "register:40f0:8", ["const:507df8:8", "const:4:8"]]
+ 00507df8 ["CALL", null, ["callee:00c59770:8"]]
- 004e4f60 bytes 70df1b94
+ 00507df8 bytes 5e461d94
- 004e4f6c ["INT_ADD", "register:40f0:8", ["const:4e4f6c:8", "const:4:8"]]
- 004e4f6c ["CALL", null, ["callee:00c58280:8"]]
+ 00507e04 ["INT_ADD", "register:40f0:8", ["const:507e04:8", "const:4:8"]]
+ 00507e04 ["CALL", null, ["callee:00c58280:8"]]
- 004e4f6c bytes 31da1b94
+ 00507e04 bytes 1f411d94
- 004e4f7c ["INT_ADD", "register:40f0:8", ["const:4e4f7c:8", "const:4:8"]]
- 004e4f7c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00507e14 ["INT_ADD", "register:40f0:8", ["const:507e14:8", "const:4:8"]]
+ 00507e14 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e4f7c bytes 39d81b94
+ 00507e14 bytes 273f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0cce7b246a2901bd36712e5d26b2eb7"></a>

### [`004e5c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5c34.md) → [`00508acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md) _ZNK5Botan7X509_DN14get_attributesEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdcbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbd0.md) · 呼出先 4件 [`00528194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528194.md) [`005282c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005282c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59620.md) · 呼出先 4件 [`0054b02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b02c.md) [`0054b15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b15c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e5cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5c34.md#insn-004e5cb4) · [`004e5cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5c34.md#insn-004e5cc0) · [`004e5cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5c34.md#insn-004e5cd0)
- 新版 `00508b4c`（命令位置の公開資料なし） · `00508b58`（命令位置の公開資料なし） · `00508b68`（命令位置の公開資料なし）

~~~diff
- 004e5cb4 ["INT_ADD", "register:40f0:8", ["const:4e5cb4:8", "const:4:8"]]
- 004e5cb4 ["CALL", null, ["callee:0054b15c:8"]]
+ 00508b4c ["INT_ADD", "register:40f0:8", ["const:508b4c:8", "const:4:8"]]
+ 00508b4c ["CALL", null, ["callee:0054b15c:8"]]
- 004e5cb4 bytes 84090194
+ 00508b4c bytes 84090194
- 004e5cc0 ["INT_ADD", "register:40f0:8", ["const:4e5cc0:8", "const:4:8"]]
- 004e5cc0 ["CALL", null, ["callee:0054b02c:8"]]
+ 00508b58 ["INT_ADD", "register:40f0:8", ["const:508b58:8", "const:4:8"]]
+ 00508b58 ["CALL", null, ["callee:0054b02c:8"]]
- 004e5cc0 bytes 35090194
+ 00508b58 bytes 35090194
- 004e5cd0 ["INT_ADD", "register:40f0:8", ["const:4e5cd0:8", "const:4:8"]]
- 004e5cd0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00508b68 ["INT_ADD", "register:40f0:8", ["const:508b68:8", "const:4:8"]]
+ 00508b68 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e5cd0 bytes e4d41b94
+ 00508b68 bytes d23b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50cdef9c9b7c9830e64a9f02ebac68fe"></a>

### [`004e5e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e2c.md) → [`00508cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508cc4.md) FUN_00508cc4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004e5e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e2c.md#insn-004e5e48)
- 新版 `00508ce0`（命令位置の公開資料なし）

~~~diff
- 004e5e48 ["INT_ADD", "register:40f0:8", ["const:4e5e48:8", "const:4:8"]]
- 004e5e48 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00508ce0 ["INT_ADD", "register:40f0:8", ["const:508ce0:8", "const:4:8"]]
+ 00508ce0 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e5e48 bytes 86d41b94
+ 00508ce0 bytes 743b1d94
~~~


