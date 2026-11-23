# v15.7.4 → v16.0.0 · 要調査の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-b996656eb95c93f7e625985c791919a4"></a>

### [`0044e7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e7fc.md) → [`00471694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471694.md) FUN_00471694

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044e818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e7fc.md#insn-0044e818) · [`0044e838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e7fc.md#insn-0044e838)
- 新版 `004716b0`（命令位置の公開資料なし） · `004716d0`（命令位置の公開資料なし）

~~~diff
- 0044e818 ["INT_ADD", "register:40f0:8", ["const:44e818:8", "const:4:8"]]
- 0044e818 ["CALL", null, ["callee:00c538e0:8"]]
+ 004716b0 ["INT_ADD", "register:40f0:8", ["const:4716b0:8", "const:4:8"]]
+ 004716b0 ["CALL", null, ["callee:00c538e0:8"]]
- 0044e818 bytes 9e211e94
+ 004716b0 bytes 8c881f94
- 0044e838 ["COPY", "register:0:8", ["register:4040:8"]]
- 0044e838 ["INT_ADD", "register:40f0:8", ["const:44e838:8", "const:4:8"]]
- 0044e838 ["CALLIND", null, ["register:0:8"]]
+ 004716d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004716d0 ["INT_ADD", "register:40f0:8", ["const:4716d0:8", "const:4:8"]]
+ 004716d0 ["CALLIND", null, ["register:0:8"]]
- 0044e838 bytes 00013fd6
+ 004716d0 bytes 00013fd6
~~~


<a id="compare-e519d290c8469455bd7afaaaa3f01b14"></a>

### [`0044ed2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed2c.md) → [`00471bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bc4.md) FUN_00471bc4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008f2388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f2/008f2388.md) · 呼出先 1件 [`0044f694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f694.md)
- 新版 呼出元 1件 [`00926414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926414.md) · 呼出先 1件 [`0047252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/0047252c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044ed3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed2c.md#insn-0044ed3c)
- 新版 `00471bd4`（命令位置の公開資料なし）

~~~diff
- 0044ed3c ["INT_ADD", "register:40f0:8", ["const:44ed3c:8", "const:4:8"]]
- 0044ed3c ["CALL", null, ["callee:0047252c:8"]]
+ 00471bd4 ["INT_ADD", "register:40f0:8", ["const:471bd4:8", "const:4:8"]]
+ 00471bd4 ["CALL", null, ["callee:0047252c:8"]]
- 0044ed3c bytes 56020094
+ 00471bd4 bytes 56020094
~~~


<a id="compare-f9c82c4ad03ed4edb916c79294f63540"></a>

### [`0044ed58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed58.md) → [`00471bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md) FUN_00471bf0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0044e018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e018.md) [`0044ed58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed58.md) · 呼出先 4件 [`0044ed58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed58.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00470eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md) [`00471bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md) · 呼出先 4件 [`00471bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044ed74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed58.md#insn-0044ed74) · [`0044ed80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed58.md#insn-0044ed80) · [`0044ed94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed58.md#insn-0044ed94)
- 新版 `00471c0c`（命令位置の公開資料なし） · `00471c18`（命令位置の公開資料なし） · `00471c2c`（命令位置の公開資料なし）

~~~diff
- 0044ed74 ["INT_ADD", "register:40f0:8", ["const:44ed74:8", "const:4:8"]]
- 0044ed74 ["CALL", null, ["local:b0:8"]]
+ 00471c0c ["INT_ADD", "register:40f0:8", ["const:471c0c:8", "const:4:8"]]
+ 00471c0c ["CALL", null, ["local:b0:8"]]
- 0044ed74 bytes f9ffff97
+ 00471c0c bytes f9ffff97
- 0044ed80 ["INT_ADD", "register:40f0:8", ["const:44ed80:8", "const:4:8"]]
- 0044ed80 ["CALL", null, ["local:b0:8"]]
+ 00471c18 ["INT_ADD", "register:40f0:8", ["const:471c18:8", "const:4:8"]]
+ 00471c18 ["CALL", null, ["local:b0:8"]]
- 0044ed80 bytes f6ffff97
+ 00471c18 bytes f6ffff97
- 0044ed94 ["INT_ADD", "register:40f0:8", ["const:44ed94:8", "const:4:8"]]
- 0044ed94 ["CALL", null, ["callee:00c538e0:8"]]
+ 00471c2c ["INT_ADD", "register:40f0:8", ["const:471c2c:8", "const:4:8"]]
+ 00471c2c ["CALL", null, ["callee:00c538e0:8"]]
- 0044ed94 bytes 3f201e94
+ 00471c2c bytes 2d871f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9f5327be9cec0765d534c3f0ea3af3d"></a>

### [`0044ede4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ede4.md) → [`00471c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md) FUN_00471c7c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0044e018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e018.md) [`0044ede4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ede4.md) · 呼出先 2件 [`0044ede4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ede4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00470eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md) [`00471c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md) · 呼出先 2件 [`00471c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044ee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ede4.md#insn-0044ee00) · [`0044ee0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ede4.md#insn-0044ee0c) · [`0044ee1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ede4.md#insn-0044ee1c)
- 新版 `00471c98`（命令位置の公開資料なし） · `00471ca4`（命令位置の公開資料なし） · `00471cb4`（命令位置の公開資料なし）

~~~diff
- 0044ee00 ["INT_ADD", "register:40f0:8", ["const:44ee00:8", "const:4:8"]]
- 0044ee00 ["CALL", null, ["local:b0:8"]]
+ 00471c98 ["INT_ADD", "register:40f0:8", ["const:471c98:8", "const:4:8"]]
+ 00471c98 ["CALL", null, ["local:b0:8"]]
- 0044ee00 bytes f9ffff97
+ 00471c98 bytes f9ffff97
- 0044ee0c ["INT_ADD", "register:40f0:8", ["const:44ee0c:8", "const:4:8"]]
- 0044ee0c ["CALL", null, ["local:b0:8"]]
+ 00471ca4 ["INT_ADD", "register:40f0:8", ["const:471ca4:8", "const:4:8"]]
+ 00471ca4 ["CALL", null, ["local:b0:8"]]
- 0044ee0c bytes f6ffff97
+ 00471ca4 bytes f6ffff97
- 0044ee1c ["INT_ADD", "register:40f0:8", ["const:44ee1c:8", "const:4:8"]]
- 0044ee1c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00471cb4 ["INT_ADD", "register:40f0:8", ["const:471cb4:8", "const:4:8"]]
+ 00471cb4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0044ee1c bytes 91301e94
+ 00471cb4 bytes 7f971f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-101ecabb1dd0136ecf92423e555d1a29"></a>

### [`0044ee44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ee44.md) → [`00471cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md) FUN_00471cdc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0044e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044ef7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ef7c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00471e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471e14.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044ee78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ee44.md#insn-0044ee78) · [`0044ee98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ee44.md#insn-0044ee98) · [`0044eed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ee44.md#insn-0044eed4)
- 新版 `00471d10`（命令位置の公開資料なし） · `00471d30`（命令位置の公開資料なし） · `00471d6c`（命令位置の公開資料なし）

~~~diff
- 0044ee78 ["INT_ADD", "register:40f0:8", ["const:44ee78:8", "const:4:8"]]
- 0044ee78 ["CALL", null, ["callee:00471e14:8"]]
+ 00471d10 ["INT_ADD", "register:40f0:8", ["const:471d10:8", "const:4:8"]]
+ 00471d10 ["CALL", null, ["callee:00471e14:8"]]
- 0044ee78 bytes 41000094
+ 00471d10 bytes 41000094
- 0044ee98 ["INT_ADD", "register:40f0:8", ["const:44ee98:8", "const:4:8"]]
- 0044ee98 ["CALL", null, ["callee:00c57a90:8"]]
+ 00471d30 ["INT_ADD", "register:40f0:8", ["const:471d30:8", "const:4:8"]]
+ 00471d30 ["CALL", null, ["callee:00c57a90:8"]]
- 0044ee98 bytes 6a301e94
+ 00471d30 bytes 58971f94
- 0044eed4 ["INT_ADD", "register:40f0:8", ["const:44eed4:8", "const:4:8"]]
- 0044eed4 ["CALL", null, ["callee:0043bae0:8"]]
+ 00471d6c ["INT_ADD", "register:40f0:8", ["const:471d6c:8", "const:4:8"]]
+ 00471d6c ["CALL", null, ["callee:0043bae0:8"]]
- 0044eed4 bytes 4328ff97
+ 00471d6c bytes 5d27ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85a5b287a2896447a1666a3e2a63259d"></a>

### [`0044ef7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ef7c.md) → [`00471e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471e14.md) FUN_00471e14

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0044ee44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ee44.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00471cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ef7c.md#insn-0044f000) · [`0044f02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ef7c.md#insn-0044f02c)
- 新版 `00471e98`（命令位置の公開資料なし） · `00471ec4`（命令位置の公開資料なし）

~~~diff
- 0044f000 ["INT_ADD", "register:40f0:8", ["const:44f000:8", "const:4:8"]]
- 0044f000 ["CALL", null, ["callee:00c57c50:8"]]
+ 00471e98 ["INT_ADD", "register:40f0:8", ["const:471e98:8", "const:4:8"]]
+ 00471e98 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f000 bytes 80301e94
+ 00471e98 bytes 6e971f94
- 0044f02c ["INT_ADD", "register:40f0:8", ["const:44f02c:8", "const:4:8"]]
- 0044f02c ["CALL", null, ["callee:00c57c50:8"]]
+ 00471ec4 ["INT_ADD", "register:40f0:8", ["const:471ec4:8", "const:4:8"]]
+ 00471ec4 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f02c bytes 75301e94
+ 00471ec4 bytes 63971f94
~~~


<a id="compare-3e2eaa268d7878fca064ac59830aa05a"></a>

### [`0044f080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f080.md) → [`00471f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f18.md) FUN_00471f18

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f080.md#insn-0044f0ac) · [`0044f0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f080.md#insn-0044f0bc)
- 新版 `00471f44`（命令位置の公開資料なし） · `00471f54`（命令位置の公開資料なし）

~~~diff
- 0044f0ac ["INT_ADD", "register:40f0:8", ["const:44f0ac:8", "const:4:8"]]
- 0044f0ac ["CALL", null, ["callee:00c57ab0:8"]]
+ 00471f44 ["INT_ADD", "register:40f0:8", ["const:471f44:8", "const:4:8"]]
+ 00471f44 ["CALL", null, ["callee:00c57ab0:8"]]
- 0044f0ac bytes ed2f1e94
+ 00471f44 bytes db961f94
- 0044f0bc ["INT_ADD", "register:40f0:8", ["const:44f0bc:8", "const:4:8"]]
- 0044f0bc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00471f54 ["INT_ADD", "register:40f0:8", ["const:471f54:8", "const:4:8"]]
+ 00471f54 ["CALL", null, ["callee:00c57ab0:8"]]
- 0044f0bc bytes e92f1e94
+ 00471f54 bytes d7961f94
~~~


<a id="compare-aede6333ec55b0e33561e19af7f279d8"></a>

### [`0044f0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f0dc.md) → [`00471f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md) FUN_00471f74

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0044e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md) [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f0dc.md#insn-0044f148) · [`0044f1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f0dc.md#insn-0044f1a4)
- 新版 `00471fe0`（命令位置の公開資料なし） · `0047203c`（命令位置の公開資料なし）

~~~diff
- 0044f148 ["INT_ADD", "register:40f0:8", ["const:44f148:8", "const:4:8"]]
- 0044f148 ["CALL", null, ["callee:00c57c50:8"]]
+ 00471fe0 ["INT_ADD", "register:40f0:8", ["const:471fe0:8", "const:4:8"]]
+ 00471fe0 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f148 bytes 2e301e94
+ 00471fe0 bytes 1c971f94
- 0044f1a4 ["INT_ADD", "register:40f0:8", ["const:44f1a4:8", "const:4:8"]]
- 0044f1a4 ["CALL", null, ["callee:00c57c50:8"]]
+ 0047203c ["INT_ADD", "register:40f0:8", ["const:47203c:8", "const:4:8"]]
+ 0047203c ["CALL", null, ["callee:00c57c50:8"]]
- 0044f1a4 bytes 17301e94
+ 0047203c bytes 05971f94
~~~


<a id="compare-cc77a91167517700a8d5bef067c0b034"></a>

### [`0044f1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f1e0.md) → [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md) FUN_00472078

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0044e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md) [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044f30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f30c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004721a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004721a4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f1e0.md#insn-0044f214) · [`0044f234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f1e0.md#insn-0044f234) · [`0044f270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f1e0.md#insn-0044f270)
- 新版 `004720ac`（命令位置の公開資料なし） · `004720cc`（命令位置の公開資料なし） · `00472108`（命令位置の公開資料なし）

~~~diff
- 0044f214 ["INT_ADD", "register:40f0:8", ["const:44f214:8", "const:4:8"]]
- 0044f214 ["CALL", null, ["callee:004721a4:8"]]
+ 004720ac ["INT_ADD", "register:40f0:8", ["const:4720ac:8", "const:4:8"]]
+ 004720ac ["CALL", null, ["callee:004721a4:8"]]
- 0044f214 bytes 3e000094
+ 004720ac bytes 3e000094
- 0044f234 ["INT_ADD", "register:40f0:8", ["const:44f234:8", "const:4:8"]]
- 0044f234 ["CALL", null, ["callee:00c57a90:8"]]
+ 004720cc ["INT_ADD", "register:40f0:8", ["const:4720cc:8", "const:4:8"]]
+ 004720cc ["CALL", null, ["callee:00c57a90:8"]]
- 0044f234 bytes 832f1e94
+ 004720cc bytes 71961f94
- 0044f270 ["INT_ADD", "register:40f0:8", ["const:44f270:8", "const:4:8"]]
- 0044f270 ["CALL", null, ["callee:0043bae0:8"]]
+ 00472108 ["INT_ADD", "register:40f0:8", ["const:472108:8", "const:4:8"]]
+ 00472108 ["CALL", null, ["callee:0043bae0:8"]]
- 0044f270 bytes 5c27ff97
+ 00472108 bytes 7626ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3d8043ad0b02ec9d26bcf9d749fd7e"></a>

### [`0044f30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f30c.md) → [`004721a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004721a4.md) FUN_004721a4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0044f1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f1e0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f30c.md#insn-0044f390) · [`0044f3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f30c.md#insn-0044f3bc)
- 新版 `00472228`（命令位置の公開資料なし） · `00472254`（命令位置の公開資料なし）

~~~diff
- 0044f390 ["INT_ADD", "register:40f0:8", ["const:44f390:8", "const:4:8"]]
- 0044f390 ["CALL", null, ["callee:00c57c50:8"]]
+ 00472228 ["INT_ADD", "register:40f0:8", ["const:472228:8", "const:4:8"]]
+ 00472228 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f390 bytes 9c2f1e94
+ 00472228 bytes 8a961f94
- 0044f3bc ["INT_ADD", "register:40f0:8", ["const:44f3bc:8", "const:4:8"]]
- 0044f3bc ["CALL", null, ["callee:00c57c50:8"]]
+ 00472254 ["INT_ADD", "register:40f0:8", ["const:472254:8", "const:4:8"]]
+ 00472254 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f3bc bytes 912f1e94
+ 00472254 bytes 7f961f94
~~~


<a id="compare-8cb8d8233e988f35bf42d46d0be7fb05"></a>

### [`0044f410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f410.md) → [`004722a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004722a8.md) FUN_004722a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f410.md#insn-0044f440) · [`0044f454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f410.md#insn-0044f454) · [`0044f45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f410.md#insn-0044f45c)
- 新版 `004722d8`（命令位置の公開資料なし） · `004722ec`（命令位置の公開資料なし） · `004722f4`（命令位置の公開資料なし）

~~~diff
- 0044f440 ["INT_ADD", "register:40f0:8", ["const:44f440:8", "const:4:8"]]
- 0044f440 ["CALL", null, ["callee:00c538e0:8"]]
+ 004722d8 ["INT_ADD", "register:40f0:8", ["const:4722d8:8", "const:4:8"]]
+ 004722d8 ["CALL", null, ["callee:00c538e0:8"]]
- 0044f440 bytes 941e1e94
+ 004722d8 bytes 82851f94
- 0044f454 ["COPY", "register:0:8", ["register:4040:8"]]
- 0044f454 ["INT_ADD", "register:40f0:8", ["const:44f454:8", "const:4:8"]]
- 0044f454 ["CALLIND", null, ["register:0:8"]]
+ 004722ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004722ec ["INT_ADD", "register:40f0:8", ["const:4722ec:8", "const:4:8"]]
+ 004722ec ["CALLIND", null, ["register:0:8"]]
- 0044f454 bytes 00013fd6
+ 004722ec bytes 00013fd6
- 0044f45c ["INT_ADD", "register:40f0:8", ["const:44f45c:8", "const:4:8"]]
- 0044f45c ["CALL", null, ["callee:00c57a80:8"]]
+ 004722f4 ["INT_ADD", "register:40f0:8", ["const:4722f4:8", "const:4:8"]]
+ 004722f4 ["CALL", null, ["callee:00c57a80:8"]]
- 0044f45c bytes f52e1e94
+ 004722f4 bytes e3951f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a31cdf7d93434f19d54ab5ebccf3a126"></a>

### [`0044f48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f48c.md) → [`00472324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472324.md) FUN_00472324

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0044e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e84c.md) [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f48c.md#insn-0044f4f8) · [`0044f554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f48c.md#insn-0044f554)
- 新版 `00472390`（命令位置の公開資料なし） · `004723ec`（命令位置の公開資料なし）

~~~diff
- 0044f4f8 ["INT_ADD", "register:40f0:8", ["const:44f4f8:8", "const:4:8"]]
- 0044f4f8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00472390 ["INT_ADD", "register:40f0:8", ["const:472390:8", "const:4:8"]]
+ 00472390 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f4f8 bytes 422f1e94
+ 00472390 bytes 30961f94
- 0044f554 ["INT_ADD", "register:40f0:8", ["const:44f554:8", "const:4:8"]]
- 0044f554 ["CALL", null, ["callee:00c57c50:8"]]
+ 004723ec ["INT_ADD", "register:40f0:8", ["const:4723ec:8", "const:4:8"]]
+ 004723ec ["CALL", null, ["callee:00c57c50:8"]]
- 0044f554 bytes 2b2f1e94
+ 004723ec bytes 19961f94
~~~


<a id="compare-867d88e9ba1ca717ae23d2597c7258a8"></a>

### [`0044f590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f590.md) → [`00472428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472428.md) FUN_00472428

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0044e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e84c.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f590.md#insn-0044f5fc) · [`0044f658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f590.md#insn-0044f658)
- 新版 `00472494`（命令位置の公開資料なし） · `004724f0`（命令位置の公開資料なし）

~~~diff
- 0044f5fc ["INT_ADD", "register:40f0:8", ["const:44f5fc:8", "const:4:8"]]
- 0044f5fc ["CALL", null, ["callee:00c57c50:8"]]
+ 00472494 ["INT_ADD", "register:40f0:8", ["const:472494:8", "const:4:8"]]
+ 00472494 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f5fc bytes 012f1e94
+ 00472494 bytes ef951f94
- 0044f658 ["INT_ADD", "register:40f0:8", ["const:44f658:8", "const:4:8"]]
- 0044f658 ["CALL", null, ["callee:00c57c50:8"]]
+ 004724f0 ["INT_ADD", "register:40f0:8", ["const:4724f0:8", "const:4:8"]]
+ 004724f0 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f658 bytes ea2e1e94
+ 004724f0 bytes d8951f94
~~~


<a id="compare-5bcca64b97965ea4bc99f9fb3d5ee8f4"></a>

### [`0044f694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f694.md) → [`0047252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/0047252c.md) FUN_0047252c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0044ed2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ed2c.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00471bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bc4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044f700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f694.md#insn-0044f700) · [`0044f75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f694.md#insn-0044f75c)
- 新版 `00472598`（命令位置の公開資料なし） · `004725f4`（命令位置の公開資料なし）

~~~diff
- 0044f700 ["INT_ADD", "register:40f0:8", ["const:44f700:8", "const:4:8"]]
- 0044f700 ["CALL", null, ["callee:00c57c50:8"]]
+ 00472598 ["INT_ADD", "register:40f0:8", ["const:472598:8", "const:4:8"]]
+ 00472598 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f700 bytes c02e1e94
+ 00472598 bytes ae951f94
- 0044f75c ["INT_ADD", "register:40f0:8", ["const:44f75c:8", "const:4:8"]]
- 0044f75c ["CALL", null, ["callee:00c57c50:8"]]
+ 004725f4 ["INT_ADD", "register:40f0:8", ["const:4725f4:8", "const:4:8"]]
+ 004725f4 ["CALL", null, ["callee:00c57c50:8"]]
- 0044f75c bytes a92e1e94
+ 004725f4 bytes 97951f94
~~~


<a id="compare-dbba4535229dddf0a534fcdf2537430d"></a>

### [`0044fb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fb34.md) → [`004729cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729cc.md) FUN_004729cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044fb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fb34.md#insn-0044fb84) · [`0044fb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fb34.md#insn-0044fb98) · [`0044fba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fb34.md#insn-0044fba0)
- 新版 `00472a1c`（命令位置の公開資料なし） · `00472a30`（命令位置の公開資料なし） · `00472a38`（命令位置の公開資料なし）

~~~diff
- 0044fb84 ["INT_ADD", "register:40f0:8", ["const:44fb84:8", "const:4:8"]]
- 0044fb84 ["CALL", null, ["callee:00c538e0:8"]]
+ 00472a1c ["INT_ADD", "register:40f0:8", ["const:472a1c:8", "const:4:8"]]
+ 00472a1c ["CALL", null, ["callee:00c538e0:8"]]
- 0044fb84 bytes c31c1e94
+ 00472a1c bytes b1831f94
- 0044fb98 ["COPY", "register:0:8", ["register:4040:8"]]
- 0044fb98 ["INT_ADD", "register:40f0:8", ["const:44fb98:8", "const:4:8"]]
- 0044fb98 ["CALLIND", null, ["register:0:8"]]
+ 00472a30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472a30 ["INT_ADD", "register:40f0:8", ["const:472a30:8", "const:4:8"]]
+ 00472a30 ["CALLIND", null, ["register:0:8"]]
- 0044fb98 bytes 00013fd6
+ 00472a30 bytes 00013fd6
- 0044fba0 ["INT_ADD", "register:40f0:8", ["const:44fba0:8", "const:4:8"]]
- 0044fba0 ["CALL", null, ["callee:00c57a80:8"]]
+ 00472a38 ["INT_ADD", "register:40f0:8", ["const:472a38:8", "const:4:8"]]
+ 00472a38 ["CALL", null, ["callee:00c57a80:8"]]
- 0044fba0 bytes 242d1e94
+ 00472a38 bytes 12941f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad1939d801eb39e7b82e2b2c1b706999"></a>

### [`0044fc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fc20.md) → [`00472ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ab8.md) FUN_00472ab8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) [`009b7d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009b7/009b7d00.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044fc68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fc20.md#insn-0044fc68) · [`0044fc7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fc20.md#insn-0044fc7c) · [`0044fc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fc20.md#insn-0044fc84)
- 新版 `00472b00`（命令位置の公開資料なし） · `00472b14`（命令位置の公開資料なし） · `00472b1c`（命令位置の公開資料なし）

~~~diff
- 0044fc68 ["INT_ADD", "register:40f0:8", ["const:44fc68:8", "const:4:8"]]
- 0044fc68 ["CALL", null, ["callee:00c538e0:8"]]
+ 00472b00 ["INT_ADD", "register:40f0:8", ["const:472b00:8", "const:4:8"]]
+ 00472b00 ["CALL", null, ["callee:00c538e0:8"]]
- 0044fc68 bytes 8a1c1e94
+ 00472b00 bytes 78831f94
- 0044fc7c ["COPY", "register:0:8", ["register:4040:8"]]
- 0044fc7c ["INT_ADD", "register:40f0:8", ["const:44fc7c:8", "const:4:8"]]
- 0044fc7c ["CALLIND", null, ["register:0:8"]]
+ 00472b14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472b14 ["INT_ADD", "register:40f0:8", ["const:472b14:8", "const:4:8"]]
+ 00472b14 ["CALLIND", null, ["register:0:8"]]
- 0044fc7c bytes 00013fd6
+ 00472b14 bytes 00013fd6
- 0044fc84 ["INT_ADD", "register:40f0:8", ["const:44fc84:8", "const:4:8"]]
- 0044fc84 ["CALL", null, ["callee:00c57a80:8"]]
+ 00472b1c ["INT_ADD", "register:40f0:8", ["const:472b1c:8", "const:4:8"]]
+ 00472b1c ["CALL", null, ["callee:00c57a80:8"]]
- 0044fc84 bytes eb2c1e94
+ 00472b1c bytes d9931f94
~~~


<a id="compare-d8018836c9ba614ce62ea2197bbf28f2"></a>

### [`0044fce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fce4.md) → [`00472b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b7c.md) FUN_00472b7c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) [`009a6250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6250.md) · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 3件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044fd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fce4.md#insn-0044fd08)
- 新版 `00472ba0`（命令位置の公開資料なし）

~~~diff
- 0044fd08 ["INT_ADD", "register:40f0:8", ["const:44fd08:8", "const:4:8"]]
- 0044fd08 ["CALL", null, ["callee:00c538b0:8"]]
+ 00472ba0 ["INT_ADD", "register:40f0:8", ["const:472ba0:8", "const:4:8"]]
+ 00472ba0 ["CALL", null, ["callee:00c538b0:8"]]
- 0044fd08 bytes 561c1e94
+ 00472ba0 bytes 44831f94
~~~


<a id="compare-0432c41861431d4d0417fcbae7d131a6"></a>

### [`0044fd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fd14.md) → [`00472bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472bac.md) FUN_00472bac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 4件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 4件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0044fd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fd14.md#insn-0044fd68) · [`0044fd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fd14.md#insn-0044fd74) · [`0044fd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fd14.md#insn-0044fd98)
- 新版 `00472c00`（命令位置の公開資料なし） · `00472c0c`（命令位置の公開資料なし） · `00472c30`（命令位置の公開資料なし）

~~~diff
- 0044fd68 ["INT_ADD", "register:40f0:8", ["const:44fd68:8", "const:4:8"]]
- 0044fd68 ["CALL", null, ["callee:00c57c50:8"]]
+ 00472c00 ["INT_ADD", "register:40f0:8", ["const:472c00:8", "const:4:8"]]
+ 00472c00 ["CALL", null, ["callee:00c57c50:8"]]
- 0044fd68 bytes 262d1e94
+ 00472c00 bytes 14941f94
- 0044fd74 ["INT_ADD", "register:40f0:8", ["const:44fd74:8", "const:4:8"]]
- 0044fd74 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00472c0c ["INT_ADD", "register:40f0:8", ["const:472c0c:8", "const:4:8"]]
+ 00472c0c ["CALL", null, ["callee:00c57ab0:8"]]
- 0044fd74 bytes bb2c1e94
+ 00472c0c bytes a9931f94
- 0044fd98 ["COPY", "register:0:8", ["register:4048:8"]]
- 0044fd98 ["INT_ADD", "register:40f0:8", ["const:44fd98:8", "const:4:8"]]
- 0044fd98 ["CALLIND", null, ["register:0:8"]]
+ 00472c30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00472c30 ["INT_ADD", "register:40f0:8", ["const:472c30:8", "const:4:8"]]
+ 00472c30 ["CALLIND", null, ["register:0:8"]]
- 0044fd98 bytes 20013fd6
+ 00472c30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cb7d10d16314369b72aaf04d0151db5"></a>

### [`00450060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450060.md) → [`00472ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ef8.md) FUN_00472ef8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045007c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450060.md#insn-0045007c) · [`0045009c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450060.md#insn-0045009c)
- 新版 `00472f14`（命令位置の公開資料なし） · `00472f34`（命令位置の公開資料なし）

~~~diff
- 0045007c ["INT_ADD", "register:40f0:8", ["const:45007c:8", "const:4:8"]]
- 0045007c ["CALL", null, ["callee:00c538e0:8"]]
+ 00472f14 ["INT_ADD", "register:40f0:8", ["const:472f14:8", "const:4:8"]]
+ 00472f14 ["CALL", null, ["callee:00c538e0:8"]]
- 0045007c bytes 851b1e94
+ 00472f14 bytes 73821f94
- 0045009c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045009c ["INT_ADD", "register:40f0:8", ["const:45009c:8", "const:4:8"]]
- 0045009c ["CALLIND", null, ["register:0:8"]]
+ 00472f34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472f34 ["INT_ADD", "register:40f0:8", ["const:472f34:8", "const:4:8"]]
+ 00472f34 ["CALLIND", null, ["register:0:8"]]
- 0045009c bytes 00013fd6
+ 00472f34 bytes 00013fd6
~~~


<a id="compare-41c097c197874e0e879f3455d05d682a"></a>

### [`004500b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004500b0.md) → [`00472f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f48.md) FUN_00472f48

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004500cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004500b0.md#insn-004500cc) · [`004500ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004500b0.md#insn-004500ec)
- 新版 `00472f64`（命令位置の公開資料なし） · `00472f84`（命令位置の公開資料なし）

~~~diff
- 004500cc ["INT_ADD", "register:40f0:8", ["const:4500cc:8", "const:4:8"]]
- 004500cc ["CALL", null, ["callee:00c538e0:8"]]
+ 00472f64 ["INT_ADD", "register:40f0:8", ["const:472f64:8", "const:4:8"]]
+ 00472f64 ["CALL", null, ["callee:00c538e0:8"]]
- 004500cc bytes 711b1e94
+ 00472f64 bytes 5f821f94
- 004500ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004500ec ["INT_ADD", "register:40f0:8", ["const:4500ec:8", "const:4:8"]]
- 004500ec ["CALLIND", null, ["register:0:8"]]
+ 00472f84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472f84 ["INT_ADD", "register:40f0:8", ["const:472f84:8", "const:4:8"]]
+ 00472f84 ["CALLIND", null, ["register:0:8"]]
- 004500ec bytes 00013fd6
+ 00472f84 bytes 00013fd6
~~~


<a id="compare-a9a411e4d3e1123cbb70958ae1c3a6e8"></a>

### [`00450100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450100.md) → [`00472f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f98.md) FUN_00472f98

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045011c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450100.md#insn-0045011c) · [`0045013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450100.md#insn-0045013c)
- 新版 `00472fb4`（命令位置の公開資料なし） · `00472fd4`（命令位置の公開資料なし）

~~~diff
- 0045011c ["INT_ADD", "register:40f0:8", ["const:45011c:8", "const:4:8"]]
- 0045011c ["CALL", null, ["callee:00c538e0:8"]]
+ 00472fb4 ["INT_ADD", "register:40f0:8", ["const:472fb4:8", "const:4:8"]]
+ 00472fb4 ["CALL", null, ["callee:00c538e0:8"]]
- 0045011c bytes 5d1b1e94
+ 00472fb4 bytes 4b821f94
- 0045013c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045013c ["INT_ADD", "register:40f0:8", ["const:45013c:8", "const:4:8"]]
- 0045013c ["CALLIND", null, ["register:0:8"]]
+ 00472fd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472fd4 ["INT_ADD", "register:40f0:8", ["const:472fd4:8", "const:4:8"]]
+ 00472fd4 ["CALLIND", null, ["register:0:8"]]
- 0045013c bytes 00013fd6
+ 00472fd4 bytes 00013fd6
~~~


<a id="compare-2ba7b2838f8c503be86fa68372f21cc8"></a>

### [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) → [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) FUN_00473500

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 33件 [`004504bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004504bc.md) [`0045e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e588.md) [`00461338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461338.md) [`0049923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md) [`004a0c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0045674c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045674c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 33件 [`00473354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md) [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) [`004841d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md) [`004bc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc0d4.md) [`004c3afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`004795e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004795e4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004506cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md#insn-004506cc) · [`0045072c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md#insn-0045072c) · [`00450778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md#insn-00450778)
- 新版 `00473564`（命令位置の公開資料なし） · `004735c4`（命令位置の公開資料なし） · `00473610`（命令位置の公開資料なし）

~~~diff
- 004506cc ["INT_ADD", "register:40f0:8", ["const:4506cc:8", "const:4:8"]]
- 004506cc ["CALL", null, ["callee:00c57a90:8"]]
+ 00473564 ["INT_ADD", "register:40f0:8", ["const:473564:8", "const:4:8"]]
+ 00473564 ["CALL", null, ["callee:00c57a90:8"]]
- 004506cc bytes 5d2a1e94
+ 00473564 bytes 4b911f94
- 0045072c ["INT_ADD", "register:40f0:8", ["const:45072c:8", "const:4:8"]]
- 0045072c ["CALL", null, ["callee:0043bae0:8"]]
+ 004735c4 ["INT_ADD", "register:40f0:8", ["const:4735c4:8", "const:4:8"]]
+ 004735c4 ["CALL", null, ["callee:0043bae0:8"]]
- 0045072c bytes 2d22ff97
+ 004735c4 bytes 4721ff97
- 00450778 ["INT_ADD", "register:40f0:8", ["const:450778:8", "const:4:8"]]
- 00450778 ["CALL", null, ["callee:00440f1c:8"]]
+ 00473610 ["INT_ADD", "register:40f0:8", ["const:473610:8", "const:4:8"]]
+ 00473610 ["CALL", null, ["callee:00440f1c:8"]]
- 00450778 bytes 2937ff97
+ 00473610 bytes 4336ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac1c5a4ebe575842da3a157d7a4ff43"></a>

### [`00450f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450f94.md) → [`00473e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e2c.md) FUN_00473e2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00450fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450f94.md#insn-00450fb0) · [`00450fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450f94.md#insn-00450fd0)
- 新版 `00473e48`（命令位置の公開資料なし） · `00473e68`（命令位置の公開資料なし）

~~~diff
- 00450fb0 ["INT_ADD", "register:40f0:8", ["const:450fb0:8", "const:4:8"]]
- 00450fb0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00473e48 ["INT_ADD", "register:40f0:8", ["const:473e48:8", "const:4:8"]]
+ 00473e48 ["CALL", null, ["callee:00c538e0:8"]]
- 00450fb0 bytes b8171e94
+ 00473e48 bytes a67e1f94
- 00450fd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00450fd0 ["INT_ADD", "register:40f0:8", ["const:450fd0:8", "const:4:8"]]
- 00450fd0 ["CALLIND", null, ["register:0:8"]]
+ 00473e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473e68 ["INT_ADD", "register:40f0:8", ["const:473e68:8", "const:4:8"]]
+ 00473e68 ["CALLIND", null, ["register:0:8"]]
- 00450fd0 bytes 00013fd6
+ 00473e68 bytes 00013fd6
~~~


<a id="compare-6c6e14df3a3e0b6b16c03f4961645680"></a>

### [`00450fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450fe4.md) → [`00473e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e7c.md) FUN_00473e7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00451000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450fe4.md#insn-00451000) · [`00451014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450fe4.md#insn-00451014) · [`00451034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450fe4.md#insn-00451034)
- 新版 `00473e98`（命令位置の公開資料なし） · `00473eac`（命令位置の公開資料なし） · `00473ecc`（命令位置の公開資料なし）

~~~diff
- 00451000 ["INT_ADD", "register:40f0:8", ["const:451000:8", "const:4:8"]]
- 00451000 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00473e98 ["INT_ADD", "register:40f0:8", ["const:473e98:8", "const:4:8"]]
+ 00473e98 ["CALL", null, ["callee:00c57ab0:8"]]
- 00451000 bytes 18281e94
+ 00473e98 bytes 068f1f94
- 00451014 ["INT_ADD", "register:40f0:8", ["const:451014:8", "const:4:8"]]
- 00451014 ["CALL", null, ["callee:00c538e0:8"]]
+ 00473eac ["INT_ADD", "register:40f0:8", ["const:473eac:8", "const:4:8"]]
+ 00473eac ["CALL", null, ["callee:00c538e0:8"]]
- 00451014 bytes 9f171e94
+ 00473eac bytes 8d7e1f94
- 00451034 ["COPY", "register:0:8", ["register:4040:8"]]
- 00451034 ["INT_ADD", "register:40f0:8", ["const:451034:8", "const:4:8"]]
- 00451034 ["CALLIND", null, ["register:0:8"]]
+ 00473ecc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473ecc ["INT_ADD", "register:40f0:8", ["const:473ecc:8", "const:4:8"]]
+ 00473ecc ["CALLIND", null, ["register:0:8"]]
- 00451034 bytes 00013fd6
+ 00473ecc bytes 00013fd6
~~~


<a id="compare-39c0aa282649a0eb041b58b02e784208"></a>

### [`00451048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451048.md) → [`00473ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473ee0.md) FUN_00473ee0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00451064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451048.md#insn-00451064) · [`00451084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451048.md#insn-00451084)
- 新版 `00473efc`（命令位置の公開資料なし） · `00473f1c`（命令位置の公開資料なし）

~~~diff
- 00451064 ["INT_ADD", "register:40f0:8", ["const:451064:8", "const:4:8"]]
- 00451064 ["CALL", null, ["callee:00c538e0:8"]]
+ 00473efc ["INT_ADD", "register:40f0:8", ["const:473efc:8", "const:4:8"]]
+ 00473efc ["CALL", null, ["callee:00c538e0:8"]]
- 00451064 bytes 8b171e94
+ 00473efc bytes 797e1f94
- 00451084 ["COPY", "register:0:8", ["register:4040:8"]]
- 00451084 ["INT_ADD", "register:40f0:8", ["const:451084:8", "const:4:8"]]
- 00451084 ["CALLIND", null, ["register:0:8"]]
+ 00473f1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473f1c ["INT_ADD", "register:40f0:8", ["const:473f1c:8", "const:4:8"]]
+ 00473f1c ["CALLIND", null, ["register:0:8"]]
- 00451084 bytes 00013fd6
+ 00473f1c bytes 00013fd6
~~~


<a id="compare-22ba01edb2de582f4debd0410eb1eee1"></a>

### [`00451098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451098.md) → [`00473f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f30.md) FUN_00473f30

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004510b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451098.md#insn-004510b4) · [`004510d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451098.md#insn-004510d4)
- 新版 `00473f4c`（命令位置の公開資料なし） · `00473f6c`（命令位置の公開資料なし）

~~~diff
- 004510b4 ["INT_ADD", "register:40f0:8", ["const:4510b4:8", "const:4:8"]]
- 004510b4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00473f4c ["INT_ADD", "register:40f0:8", ["const:473f4c:8", "const:4:8"]]
+ 00473f4c ["CALL", null, ["callee:00c538e0:8"]]
- 004510b4 bytes 77171e94
+ 00473f4c bytes 657e1f94
- 004510d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004510d4 ["INT_ADD", "register:40f0:8", ["const:4510d4:8", "const:4:8"]]
- 004510d4 ["CALLIND", null, ["register:0:8"]]
+ 00473f6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473f6c ["INT_ADD", "register:40f0:8", ["const:473f6c:8", "const:4:8"]]
+ 00473f6c ["CALLIND", null, ["register:0:8"]]
- 004510d4 bytes 00013fd6
+ 00473f6c bytes 00013fd6
~~~


<a id="compare-8501856a746ef6edf911ed91f62c3116"></a>

### [`004510e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004510e8.md) → [`00473f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f80.md) FUN_00473f80

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00451104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004510e8.md#insn-00451104) · [`00451124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004510e8.md#insn-00451124)
- 新版 `00473f9c`（命令位置の公開資料なし） · `00473fbc`（命令位置の公開資料なし）

~~~diff
- 00451104 ["INT_ADD", "register:40f0:8", ["const:451104:8", "const:4:8"]]
- 00451104 ["CALL", null, ["callee:00c538e0:8"]]
+ 00473f9c ["INT_ADD", "register:40f0:8", ["const:473f9c:8", "const:4:8"]]
+ 00473f9c ["CALL", null, ["callee:00c538e0:8"]]
- 00451104 bytes 63171e94
+ 00473f9c bytes 517e1f94
- 00451124 ["COPY", "register:0:8", ["register:4040:8"]]
- 00451124 ["INT_ADD", "register:40f0:8", ["const:451124:8", "const:4:8"]]
- 00451124 ["CALLIND", null, ["register:0:8"]]
+ 00473fbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473fbc ["INT_ADD", "register:40f0:8", ["const:473fbc:8", "const:4:8"]]
+ 00473fbc ["CALLIND", null, ["register:0:8"]]
- 00451124 bytes 00013fd6
+ 00473fbc bytes 00013fd6
~~~


<a id="compare-f4aad67e173bedafa4dfe3b3350c1705"></a>

### [`00451138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451138.md) → [`00473fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473fd0.md) FUN_00473fd0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 6件 [`00457938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457938.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 6件 [`0047a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a7d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00451170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451138.md#insn-00451170) · [`0045117c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451138.md#insn-0045117c) · [`00451188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451138.md#insn-00451188)
- 新版 `00474008`（命令位置の公開資料なし） · `00474014`（命令位置の公開資料なし） · `00474020`（命令位置の公開資料なし）

~~~diff
- 00451170 ["INT_ADD", "register:40f0:8", ["const:451170:8", "const:4:8"]]
- 00451170 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00474008 ["INT_ADD", "register:40f0:8", ["const:474008:8", "const:4:8"]]
+ 00474008 ["CALL", null, ["callee:00c57ce0:8"]]
- 00451170 bytes 48281e94
+ 00474008 bytes 368f1f94
- 0045117c ["INT_ADD", "register:40f0:8", ["const:45117c:8", "const:4:8"]]
- 0045117c ["CALL", null, ["callee:0047a7d0:8"]]
+ 00474014 ["INT_ADD", "register:40f0:8", ["const:474014:8", "const:4:8"]]
+ 00474014 ["CALL", null, ["callee:0047a7d0:8"]]
- 0045117c bytes ef190094
+ 00474014 bytes ef190094
- 00451188 ["INT_ADD", "register:40f0:8", ["const:451188:8", "const:4:8"]]
- 00451188 ["CALL", null, ["callee:00c57cf0:8"]]
+ 00474020 ["INT_ADD", "register:40f0:8", ["const:474020:8", "const:4:8"]]
+ 00474020 ["CALL", null, ["callee:00c57cf0:8"]]
- 00451188 bytes 46281e94
+ 00474020 bytes 348f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8c01e690feb75beb04cc05cd90ba6b"></a>

### [`00451270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451270.md) → [`00474108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474108.md) FUN_00474108

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045128c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451270.md#insn-0045128c) · [`004512ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451270.md#insn-004512ac)
- 新版 `00474124`（命令位置の公開資料なし） · `00474144`（命令位置の公開資料なし）

~~~diff
- 0045128c ["INT_ADD", "register:40f0:8", ["const:45128c:8", "const:4:8"]]
- 0045128c ["CALL", null, ["callee:00c538e0:8"]]
+ 00474124 ["INT_ADD", "register:40f0:8", ["const:474124:8", "const:4:8"]]
+ 00474124 ["CALL", null, ["callee:00c538e0:8"]]
- 0045128c bytes 01171e94
+ 00474124 bytes ef7d1f94
- 004512ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004512ac ["INT_ADD", "register:40f0:8", ["const:4512ac:8", "const:4:8"]]
- 004512ac ["CALLIND", null, ["register:0:8"]]
+ 00474144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474144 ["INT_ADD", "register:40f0:8", ["const:474144:8", "const:4:8"]]
+ 00474144 ["CALLIND", null, ["register:0:8"]]
- 004512ac bytes 00013fd6
+ 00474144 bytes 00013fd6
~~~


<a id="compare-796317145054f8df1cdc6e14223d5277"></a>

### [`00451c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451c54.md) → [`00474aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474aec.md) FUN_00474aec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00451c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451c20.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00474ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474ab8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00451cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451c54.md#insn-00451cd0) · [`00451ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451c54.md#insn-00451ce4) · [`00451cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451c54.md#insn-00451cec)
- 新版 `00474b68`（命令位置の公開資料なし） · `00474b7c`（命令位置の公開資料なし） · `00474b84`（命令位置の公開資料なし）

~~~diff
- 00451cd0 ["INT_ADD", "register:40f0:8", ["const:451cd0:8", "const:4:8"]]
- 00451cd0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00474b68 ["INT_ADD", "register:40f0:8", ["const:474b68:8", "const:4:8"]]
+ 00474b68 ["CALL", null, ["callee:00c538e0:8"]]
- 00451cd0 bytes 70141e94
+ 00474b68 bytes 5e7b1f94
- 00451ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00451ce4 ["INT_ADD", "register:40f0:8", ["const:451ce4:8", "const:4:8"]]
- 00451ce4 ["CALLIND", null, ["register:0:8"]]
+ 00474b7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474b7c ["INT_ADD", "register:40f0:8", ["const:474b7c:8", "const:4:8"]]
+ 00474b7c ["CALLIND", null, ["register:0:8"]]
- 00451ce4 bytes 00013fd6
+ 00474b7c bytes 00013fd6
- 00451cec ["INT_ADD", "register:40f0:8", ["const:451cec:8", "const:4:8"]]
- 00451cec ["CALL", null, ["callee:00c57a80:8"]]
+ 00474b84 ["INT_ADD", "register:40f0:8", ["const:474b84:8", "const:4:8"]]
+ 00474b84 ["CALL", null, ["callee:00c57a80:8"]]
- 00451cec bytes d1241e94
+ 00474b84 bytes bf8b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fad611cc78b89dd9d49f2f05cbc6488"></a>

### [`00451e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451e58.md) → [`00474cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cf0.md) FUN_00474cf0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00451e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451e24.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00474cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cbc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00451edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451e58.md#insn-00451edc) · [`00451ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451e58.md#insn-00451ef0) · [`00451ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451e58.md#insn-00451ef8)
- 新版 `00474d74`（命令位置の公開資料なし） · `00474d88`（命令位置の公開資料なし） · `00474d90`（命令位置の公開資料なし）

~~~diff
- 00451edc ["INT_ADD", "register:40f0:8", ["const:451edc:8", "const:4:8"]]
- 00451edc ["CALL", null, ["callee:00c538e0:8"]]
+ 00474d74 ["INT_ADD", "register:40f0:8", ["const:474d74:8", "const:4:8"]]
+ 00474d74 ["CALL", null, ["callee:00c538e0:8"]]
- 00451edc bytes ed131e94
+ 00474d74 bytes db7a1f94
- 00451ef0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00451ef0 ["INT_ADD", "register:40f0:8", ["const:451ef0:8", "const:4:8"]]
- 00451ef0 ["CALLIND", null, ["register:0:8"]]
+ 00474d88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474d88 ["INT_ADD", "register:40f0:8", ["const:474d88:8", "const:4:8"]]
+ 00474d88 ["CALLIND", null, ["register:0:8"]]
- 00451ef0 bytes 00013fd6
+ 00474d88 bytes 00013fd6
- 00451ef8 ["INT_ADD", "register:40f0:8", ["const:451ef8:8", "const:4:8"]]
- 00451ef8 ["CALL", null, ["callee:00c57a80:8"]]
+ 00474d90 ["INT_ADD", "register:40f0:8", ["const:474d90:8", "const:4:8"]]
+ 00474d90 ["CALL", null, ["callee:00c57a80:8"]]
- 00451ef8 bytes 4e241e94
+ 00474d90 bytes 3c8b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5595531679e80801338da6cf395c9e86"></a>

### [`00451ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md) → [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) FUN_00474e88

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00450150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md) [`004529a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a8.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004524b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004524b0.md) [`00452638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452638.md) [`004527c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004527c4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00475840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00475348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475348.md) [`004754d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004754d0.md) [`0047565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047565c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00452088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md#insn-00452088) · [`004520cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md#insn-004520cc) · [`004520dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md#insn-004520dc)
- 新版 `00474f20`（命令位置の公開資料なし） · `00474f64`（命令位置の公開資料なし） · `00474f74`（命令位置の公開資料なし）

~~~diff
- 00452088 ["INT_ADD", "register:40f0:8", ["const:452088:8", "const:4:8"]]
- 00452088 ["CALL", null, ["callee:00c57b40:8"]]
+ 00474f20 ["INT_ADD", "register:40f0:8", ["const:474f20:8", "const:4:8"]]
+ 00474f20 ["CALL", null, ["callee:00c57b40:8"]]
- 00452088 bytes 1a241e94
+ 00474f20 bytes 088b1f94
- 004520cc ["INT_ADD", "register:40f0:8", ["const:4520cc:8", "const:4:8"]]
- 004520cc ["CALL", null, ["callee:00c57a90:8"]]
+ 00474f64 ["INT_ADD", "register:40f0:8", ["const:474f64:8", "const:4:8"]]
+ 00474f64 ["CALL", null, ["callee:00c57a90:8"]]
- 004520cc bytes dd231e94
+ 00474f64 bytes cb8a1f94
- 004520dc ["INT_ADD", "register:40f0:8", ["const:4520dc:8", "const:4:8"]]
- 004520dc ["CALL", null, ["callee:00475348:8"]]
+ 00474f74 ["INT_ADD", "register:40f0:8", ["const:474f74:8", "const:4:8"]]
+ 00474f74 ["CALL", null, ["callee:00475348:8"]]
- 004520dc bytes f5000094
+ 00474f74 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b891409a82451a447f3bfb0fcee4a82e"></a>

### [`004524b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004524b0.md) → [`00475348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475348.md) FUN_00475348

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00451ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00452518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004524b0.md#insn-00452518) · [`00452550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004524b0.md#insn-00452550) · [`00452600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004524b0.md#insn-00452600)
- 新版 `004753b0`（命令位置の公開資料なし） · `004753e8`（命令位置の公開資料なし） · `00475498`（命令位置の公開資料なし）

~~~diff
- 00452518 ["INT_ADD", "register:40f0:8", ["const:452518:8", "const:4:8"]]
- 00452518 ["CALL", null, ["callee:00c57b40:8"]]
+ 004753b0 ["INT_ADD", "register:40f0:8", ["const:4753b0:8", "const:4:8"]]
+ 004753b0 ["CALL", null, ["callee:00c57b40:8"]]
- 00452518 bytes f6221e94
+ 004753b0 bytes e4891f94
- 00452550 ["INT_ADD", "register:40f0:8", ["const:452550:8", "const:4:8"]]
- 00452550 ["CALL", null, ["callee:00c57a90:8"]]
+ 004753e8 ["INT_ADD", "register:40f0:8", ["const:4753e8:8", "const:4:8"]]
+ 004753e8 ["CALL", null, ["callee:00c57a90:8"]]
- 00452550 bytes bc221e94
+ 004753e8 bytes aa891f94
- 00452600 ["INT_ADD", "register:40f0:8", ["const:452600:8", "const:4:8"]]
- 00452600 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00475498 ["INT_ADD", "register:40f0:8", ["const:475498:8", "const:4:8"]]
+ 00475498 ["CALL", null, ["callee:00c57ab0:8"]]
- 00452600 bytes 98221e94
+ 00475498 bytes 86891f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d96b5719d8c497feb7b510b5d2e1ce2a"></a>

### [`00452638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452638.md) → [`004754d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004754d0.md) FUN_004754d0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00451ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004526a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452638.md#insn-004526a8) · [`004526e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452638.md#insn-004526e0) · [`00452790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452638.md#insn-00452790)
- 新版 `00475540`（命令位置の公開資料なし） · `00475578`（命令位置の公開資料なし） · `00475628`（命令位置の公開資料なし）

~~~diff
- 004526a8 ["INT_ADD", "register:40f0:8", ["const:4526a8:8", "const:4:8"]]
- 004526a8 ["CALL", null, ["callee:00c57b40:8"]]
+ 00475540 ["INT_ADD", "register:40f0:8", ["const:475540:8", "const:4:8"]]
+ 00475540 ["CALL", null, ["callee:00c57b40:8"]]
- 004526a8 bytes 92221e94
+ 00475540 bytes 80891f94
- 004526e0 ["INT_ADD", "register:40f0:8", ["const:4526e0:8", "const:4:8"]]
- 004526e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00475578 ["INT_ADD", "register:40f0:8", ["const:475578:8", "const:4:8"]]
+ 00475578 ["CALL", null, ["callee:00c57a90:8"]]
- 004526e0 bytes 58221e94
+ 00475578 bytes 46891f94
- 00452790 ["INT_ADD", "register:40f0:8", ["const:452790:8", "const:4:8"]]
- 00452790 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00475628 ["INT_ADD", "register:40f0:8", ["const:475628:8", "const:4:8"]]
+ 00475628 ["CALL", null, ["callee:00c57ab0:8"]]
- 00452790 bytes 34221e94
+ 00475628 bytes 22891f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e4e8130ea3d3aedf714b21fd2db36be"></a>

### [`004527c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004527c4.md) → [`0047565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047565c.md) FUN_0047565c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00451ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00452834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004527c4.md#insn-00452834) · [`0045286c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004527c4.md#insn-0045286c) · [`0045291c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004527c4.md#insn-0045291c)
- 新版 `004756cc`（命令位置の公開資料なし） · `00475704`（命令位置の公開資料なし） · `004757b4`（命令位置の公開資料なし）

~~~diff
- 00452834 ["INT_ADD", "register:40f0:8", ["const:452834:8", "const:4:8"]]
- 00452834 ["CALL", null, ["callee:00c57b40:8"]]
+ 004756cc ["INT_ADD", "register:40f0:8", ["const:4756cc:8", "const:4:8"]]
+ 004756cc ["CALL", null, ["callee:00c57b40:8"]]
- 00452834 bytes 2f221e94
+ 004756cc bytes 1d891f94
- 0045286c ["INT_ADD", "register:40f0:8", ["const:45286c:8", "const:4:8"]]
- 0045286c ["CALL", null, ["callee:00c57a90:8"]]
+ 00475704 ["INT_ADD", "register:40f0:8", ["const:475704:8", "const:4:8"]]
+ 00475704 ["CALL", null, ["callee:00c57a90:8"]]
- 0045286c bytes f5211e94
+ 00475704 bytes e3881f94
- 0045291c ["INT_ADD", "register:40f0:8", ["const:45291c:8", "const:4:8"]]
- 0045291c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004757b4 ["INT_ADD", "register:40f0:8", ["const:4757b4:8", "const:4:8"]]
+ 004757b4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0045291c bytes d1211e94
+ 004757b4 bytes bf881f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c8024143991a4e255fd4bd1b7f6516c"></a>

### [`004529a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a8.md) → [`00475840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md) FUN_00475840

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00451ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md) [`00452c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452c50.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) [`00475ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ae8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004529e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a8.md#insn-004529e8) · [`00452a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a8.md#insn-00452a08) · [`00452a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a8.md#insn-00452a1c)
- 新版 `00475880`（命令位置の公開資料なし） · `004758a0`（命令位置の公開資料なし） · `004758b4`（命令位置の公開資料なし）

~~~diff
- 004529e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004529e8 ["INT_ADD", "register:40f0:8", ["const:4529e8:8", "const:4:8"]]
- 004529e8 ["CALLIND", null, ["register:0:8"]]
+ 00475880 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00475880 ["INT_ADD", "register:40f0:8", ["const:475880:8", "const:4:8"]]
+ 00475880 ["CALLIND", null, ["register:0:8"]]
- 004529e8 bytes 00013fd6
+ 00475880 bytes 00013fd6
- 00452a08 ["COPY", "register:0:8", ["register:4048:8"]]
- 00452a08 ["INT_ADD", "register:40f0:8", ["const:452a08:8", "const:4:8"]]
- 00452a08 ["CALLIND", null, ["register:0:8"]]
+ 004758a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004758a0 ["INT_ADD", "register:40f0:8", ["const:4758a0:8", "const:4:8"]]
+ 004758a0 ["CALLIND", null, ["register:0:8"]]
- 00452a08 bytes 20013fd6
+ 004758a0 bytes 20013fd6
- 00452a1c ["COPY", "register:0:8", ["register:4048:8"]]
- 00452a1c ["INT_ADD", "register:40f0:8", ["const:452a1c:8", "const:4:8"]]
- 00452a1c ["CALLIND", null, ["register:0:8"]]
+ 004758b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004758b4 ["INT_ADD", "register:40f0:8", ["const:4758b4:8", "const:4:8"]]
+ 004758b4 ["CALLIND", null, ["register:0:8"]]
- 00452a1c bytes 20013fd6
+ 004758b4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bca0aaa3c519a580ee0aff43ffbcac1"></a>

### [`00452c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452c50.md) → [`00475ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ae8.md) FUN_00475ae8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004529a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a8.md) · 呼出先 8件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00475840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md) · 呼出先 8件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00452c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452c50.md#insn-00452c9c) · [`00452ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452c50.md#insn-00452ca8) · [`00452cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452c50.md#insn-00452cbc)
- 新版 `00475b34`（命令位置の公開資料なし） · `00475b40`（命令位置の公開資料なし） · `00475b54`（命令位置の公開資料なし）

~~~diff
- 00452c9c ["INT_ADD", "register:40f0:8", ["const:452c9c:8", "const:4:8"]]
- 00452c9c ["CALL", null, ["callee:00c538b0:8"]]
+ 00475b34 ["INT_ADD", "register:40f0:8", ["const:475b34:8", "const:4:8"]]
+ 00475b34 ["CALL", null, ["callee:00c538b0:8"]]
- 00452c9c bytes 71101e94
+ 00475b34 bytes 5f771f94
- 00452ca8 ["INT_ADD", "register:40f0:8", ["const:452ca8:8", "const:4:8"]]
- 00452ca8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00475b40 ["INT_ADD", "register:40f0:8", ["const:475b40:8", "const:4:8"]]
+ 00475b40 ["CALL", null, ["callee:00c538e0:8"]]
- 00452ca8 bytes 7a101e94
+ 00475b40 bytes 68771f94
- 00452cbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00452cbc ["INT_ADD", "register:40f0:8", ["const:452cbc:8", "const:4:8"]]
- 00452cbc ["CALLIND", null, ["register:0:8"]]
+ 00475b54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00475b54 ["INT_ADD", "register:40f0:8", ["const:475b54:8", "const:4:8"]]
+ 00475b54 ["CALLIND", null, ["register:0:8"]]
- 00452cbc bytes 00013fd6
+ 00475b54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34a427bc42065f971acaa2aa43c58b7b"></a>

### [`00453660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453660.md) → [`004764f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/004764f8.md) FUN_004764f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045367c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453660.md#insn-0045367c) · [`0045369c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453660.md#insn-0045369c)
- 新版 `00476514`（命令位置の公開資料なし） · `00476534`（命令位置の公開資料なし）

~~~diff
- 0045367c ["INT_ADD", "register:40f0:8", ["const:45367c:8", "const:4:8"]]
- 0045367c ["CALL", null, ["callee:00c538e0:8"]]
+ 00476514 ["INT_ADD", "register:40f0:8", ["const:476514:8", "const:4:8"]]
+ 00476514 ["CALL", null, ["callee:00c538e0:8"]]
- 0045367c bytes 050e1e94
+ 00476514 bytes f3741f94
- 0045369c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045369c ["INT_ADD", "register:40f0:8", ["const:45369c:8", "const:4:8"]]
- 0045369c ["CALLIND", null, ["register:0:8"]]
+ 00476534 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00476534 ["INT_ADD", "register:40f0:8", ["const:476534:8", "const:4:8"]]
+ 00476534 ["CALLIND", null, ["register:0:8"]]
- 0045369c bytes 00013fd6
+ 00476534 bytes 00013fd6
~~~


<a id="compare-b5b063842e828d8f1ee73cbe6e0be513"></a>

### [`0045539c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045539c.md) → [`00478234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478234.md) FUN_00478234

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004553b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045539c.md#insn-004553b8) · [`004553d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045539c.md#insn-004553d8)
- 新版 `00478250`（命令位置の公開資料なし） · `00478270`（命令位置の公開資料なし）

~~~diff
- 004553b8 ["INT_ADD", "register:40f0:8", ["const:4553b8:8", "const:4:8"]]
- 004553b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00478250 ["INT_ADD", "register:40f0:8", ["const:478250:8", "const:4:8"]]
+ 00478250 ["CALL", null, ["callee:00c538e0:8"]]
- 004553b8 bytes b6061e94
+ 00478250 bytes a46d1f94
- 004553d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004553d8 ["INT_ADD", "register:40f0:8", ["const:4553d8:8", "const:4:8"]]
- 004553d8 ["CALLIND", null, ["register:0:8"]]
+ 00478270 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00478270 ["INT_ADD", "register:40f0:8", ["const:478270:8", "const:4:8"]]
+ 00478270 ["CALLIND", null, ["register:0:8"]]
- 004553d8 bytes 00013fd6
+ 00478270 bytes 00013fd6
~~~


<a id="compare-6321d5fd3137bb61f0a975becaa4556f"></a>

### [`004553ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/004553ec.md) → [`00478284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478284.md) FUN_00478284

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00455408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/004553ec.md#insn-00455408) · [`00455428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/004553ec.md#insn-00455428)
- 新版 `004782a0`（命令位置の公開資料なし） · `004782c0`（命令位置の公開資料なし）

~~~diff
- 00455408 ["INT_ADD", "register:40f0:8", ["const:455408:8", "const:4:8"]]
- 00455408 ["CALL", null, ["callee:00c538e0:8"]]
+ 004782a0 ["INT_ADD", "register:40f0:8", ["const:4782a0:8", "const:4:8"]]
+ 004782a0 ["CALL", null, ["callee:00c538e0:8"]]
- 00455408 bytes a2061e94
+ 004782a0 bytes 906d1f94
- 00455428 ["COPY", "register:0:8", ["register:4040:8"]]
- 00455428 ["INT_ADD", "register:40f0:8", ["const:455428:8", "const:4:8"]]
- 00455428 ["CALLIND", null, ["register:0:8"]]
+ 004782c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004782c0 ["INT_ADD", "register:40f0:8", ["const:4782c0:8", "const:4:8"]]
+ 004782c0 ["CALLIND", null, ["register:0:8"]]
- 00455428 bytes 00013fd6
+ 004782c0 bytes 00013fd6
~~~


<a id="compare-1d6df116a9ca01879f07cd178ed0cd0d"></a>

### [`00455d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d3c.md) → [`00478bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md) FUN_00478bd4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`00455cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455cb8.md) [`00455d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d3c.md) [`00469fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fe0.md) · 呼出先 2件 [`00455d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d3c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`00478b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b50.md) [`00478bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md) [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) · 呼出先 2件 [`00478bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00455d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d3c.md#insn-00455d5c) · [`00455d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d3c.md#insn-00455d68)
- 新版 `00478bf4`（命令位置の公開資料なし） · `00478c00`（命令位置の公開資料なし）

~~~diff
- 00455d5c ["INT_ADD", "register:40f0:8", ["const:455d5c:8", "const:4:8"]]
- 00455d5c ["CALL", null, ["local:b0:8"]]
+ 00478bf4 ["INT_ADD", "register:40f0:8", ["const:478bf4:8", "const:4:8"]]
+ 00478bf4 ["CALL", null, ["local:b0:8"]]
- 00455d5c bytes f8ffff97
+ 00478bf4 bytes f8ffff97
- 00455d68 ["INT_ADD", "register:40f0:8", ["const:455d68:8", "const:4:8"]]
- 00455d68 ["CALL", null, ["local:b0:8"]]
+ 00478c00 ["INT_ADD", "register:40f0:8", ["const:478c00:8", "const:4:8"]]
+ 00478c00 ["CALL", null, ["local:b0:8"]]
- 00455d68 bytes f5ffff97
+ 00478c00 bytes f5ffff97
~~~


<a id="compare-6e4e4e7c7638080d1ea7eb7dbeaad702"></a>

### [`00455dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md) → [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) FUN_00478c84

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00452ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md) [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004562ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004562ac.md) [`00456434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456434.md) [`004565c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004565c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00479144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479144.md) [`004792cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004792cc.md) [`00479458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479458.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00455e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md#insn-00455e84) · [`00455ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md#insn-00455ec8) · [`00455ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md#insn-00455ed8)
- 新版 `00478d1c`（命令位置の公開資料なし） · `00478d60`（命令位置の公開資料なし） · `00478d70`（命令位置の公開資料なし）

~~~diff
- 00455e84 ["INT_ADD", "register:40f0:8", ["const:455e84:8", "const:4:8"]]
- 00455e84 ["CALL", null, ["callee:00c57b40:8"]]
+ 00478d1c ["INT_ADD", "register:40f0:8", ["const:478d1c:8", "const:4:8"]]
+ 00478d1c ["CALL", null, ["callee:00c57b40:8"]]
- 00455e84 bytes 9b141e94
+ 00478d1c bytes 897b1f94
- 00455ec8 ["INT_ADD", "register:40f0:8", ["const:455ec8:8", "const:4:8"]]
- 00455ec8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00478d60 ["INT_ADD", "register:40f0:8", ["const:478d60:8", "const:4:8"]]
+ 00478d60 ["CALL", null, ["callee:00c57a90:8"]]
- 00455ec8 bytes 5e141e94
+ 00478d60 bytes 4c7b1f94
- 00455ed8 ["INT_ADD", "register:40f0:8", ["const:455ed8:8", "const:4:8"]]
- 00455ed8 ["CALL", null, ["callee:00479144:8"]]
+ 00478d70 ["INT_ADD", "register:40f0:8", ["const:478d70:8", "const:4:8"]]
+ 00478d70 ["CALL", null, ["callee:00479144:8"]]
- 00455ed8 bytes f5000094
+ 00478d70 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e059180ee802589a9ccdd6ecdc6be6f"></a>

### [`004562ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004562ac.md) → [`00479144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479144.md) FUN_00479144

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00455dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00456314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004562ac.md#insn-00456314) · [`0045634c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004562ac.md#insn-0045634c) · [`004563fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004562ac.md#insn-004563fc)
- 新版 `004791ac`（命令位置の公開資料なし） · `004791e4`（命令位置の公開資料なし） · `00479294`（命令位置の公開資料なし）

~~~diff
- 00456314 ["INT_ADD", "register:40f0:8", ["const:456314:8", "const:4:8"]]
- 00456314 ["CALL", null, ["callee:00c57b40:8"]]
+ 004791ac ["INT_ADD", "register:40f0:8", ["const:4791ac:8", "const:4:8"]]
+ 004791ac ["CALL", null, ["callee:00c57b40:8"]]
- 00456314 bytes 77131e94
+ 004791ac bytes 657a1f94
- 0045634c ["INT_ADD", "register:40f0:8", ["const:45634c:8", "const:4:8"]]
- 0045634c ["CALL", null, ["callee:00c57a90:8"]]
+ 004791e4 ["INT_ADD", "register:40f0:8", ["const:4791e4:8", "const:4:8"]]
+ 004791e4 ["CALL", null, ["callee:00c57a90:8"]]
- 0045634c bytes 3d131e94
+ 004791e4 bytes 2b7a1f94
- 004563fc ["INT_ADD", "register:40f0:8", ["const:4563fc:8", "const:4:8"]]
- 004563fc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00479294 ["INT_ADD", "register:40f0:8", ["const:479294:8", "const:4:8"]]
+ 00479294 ["CALL", null, ["callee:00c57ab0:8"]]
- 004563fc bytes 19131e94
+ 00479294 bytes 077a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5512589b371bfeffc205afcb4bda3b60"></a>

### [`00456434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456434.md) → [`004792cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004792cc.md) FUN_004792cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00455dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004564a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456434.md#insn-004564a4) · [`004564dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456434.md#insn-004564dc) · [`0045658c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456434.md#insn-0045658c)
- 新版 `0047933c`（命令位置の公開資料なし） · `00479374`（命令位置の公開資料なし） · `00479424`（命令位置の公開資料なし）

~~~diff
- 004564a4 ["INT_ADD", "register:40f0:8", ["const:4564a4:8", "const:4:8"]]
- 004564a4 ["CALL", null, ["callee:00c57b40:8"]]
+ 0047933c ["INT_ADD", "register:40f0:8", ["const:47933c:8", "const:4:8"]]
+ 0047933c ["CALL", null, ["callee:00c57b40:8"]]
- 004564a4 bytes 13131e94
+ 0047933c bytes 017a1f94
- 004564dc ["INT_ADD", "register:40f0:8", ["const:4564dc:8", "const:4:8"]]
- 004564dc ["CALL", null, ["callee:00c57a90:8"]]
+ 00479374 ["INT_ADD", "register:40f0:8", ["const:479374:8", "const:4:8"]]
+ 00479374 ["CALL", null, ["callee:00c57a90:8"]]
- 004564dc bytes d9121e94
+ 00479374 bytes c7791f94
- 0045658c ["INT_ADD", "register:40f0:8", ["const:45658c:8", "const:4:8"]]
- 0045658c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00479424 ["INT_ADD", "register:40f0:8", ["const:479424:8", "const:4:8"]]
+ 00479424 ["CALL", null, ["callee:00c57ab0:8"]]
- 0045658c bytes b5121e94
+ 00479424 bytes a3791f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4196d564724f7a92d1793b4e5d45e3da"></a>

### [`004565c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004565c0.md) → [`00479458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479458.md) FUN_00479458

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00455dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00456630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004565c0.md#insn-00456630) · [`00456668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004565c0.md#insn-00456668) · [`00456718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004565c0.md#insn-00456718)
- 新版 `004794c8`（命令位置の公開資料なし） · `00479500`（命令位置の公開資料なし） · `004795b0`（命令位置の公開資料なし）

~~~diff
- 00456630 ["INT_ADD", "register:40f0:8", ["const:456630:8", "const:4:8"]]
- 00456630 ["CALL", null, ["callee:00c57b40:8"]]
+ 004794c8 ["INT_ADD", "register:40f0:8", ["const:4794c8:8", "const:4:8"]]
+ 004794c8 ["CALL", null, ["callee:00c57b40:8"]]
- 00456630 bytes b0121e94
+ 004794c8 bytes 9e791f94
- 00456668 ["INT_ADD", "register:40f0:8", ["const:456668:8", "const:4:8"]]
- 00456668 ["CALL", null, ["callee:00c57a90:8"]]
+ 00479500 ["INT_ADD", "register:40f0:8", ["const:479500:8", "const:4:8"]]
+ 00479500 ["CALL", null, ["callee:00c57a90:8"]]
- 00456668 bytes 76121e94
+ 00479500 bytes 64791f94
- 00456718 ["INT_ADD", "register:40f0:8", ["const:456718:8", "const:4:8"]]
- 00456718 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004795b0 ["INT_ADD", "register:40f0:8", ["const:4795b0:8", "const:4:8"]]
+ 004795b0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00456718 bytes 52121e94
+ 004795b0 bytes 40791f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a79a050d55e05455e8f8da71145a1f54"></a>

### [`0045674c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045674c.md) → [`004795e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004795e4.md) FUN_004795e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004567b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045674c.md#insn-004567b4)
- 新版 `0047964c`（命令位置の公開資料なし）

~~~diff
- 004567b4 ["INT_ADD", "register:40f0:8", ["const:4567b4:8", "const:4:8"]]
- 004567b4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047964c ["INT_ADD", "register:40f0:8", ["const:47964c:8", "const:4:8"]]
+ 0047964c ["CALL", null, ["callee:00c57ab0:8"]]
- 004567b4 bytes 2b121e94
+ 0047964c bytes 19791f94
~~~


<a id="compare-5b4886569721cc27d29f511e9ae6ed97"></a>

### [`004567d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004567d8.md) → [`00479670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479670.md) FUN_00479670

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051c140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c140.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0053efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efd8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00456824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004567d8.md#insn-00456824)
- 新版 `004796bc`（命令位置の公開資料なし）

~~~diff
- 00456824 ["INT_ADD", "register:40f0:8", ["const:456824:8", "const:4:8"]]
- 00456824 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004796bc ["INT_ADD", "register:40f0:8", ["const:4796bc:8", "const:4:8"]]
+ 004796bc ["CALL", null, ["callee:00c57ab0:8"]]
- 00456824 bytes 0f121e94
+ 004796bc bytes fd781f94
~~~


<a id="compare-ec88564caaf7b6913a55adf03315caaa"></a>

### [`00456bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456bac.md) → [`00479a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479a44.md) FUN_00479a44

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00456bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456bac.md#insn-00456bc8) · [`00456bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456bac.md#insn-00456bdc) · [`00456bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456bac.md#insn-00456bfc)
- 新版 `00479a60`（命令位置の公開資料なし） · `00479a74`（命令位置の公開資料なし） · `00479a94`（命令位置の公開資料なし）

~~~diff
- 00456bc8 ["INT_ADD", "register:40f0:8", ["const:456bc8:8", "const:4:8"]]
- 00456bc8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00479a60 ["INT_ADD", "register:40f0:8", ["const:479a60:8", "const:4:8"]]
+ 00479a60 ["CALL", null, ["callee:00c57ab0:8"]]
- 00456bc8 bytes 26111e94
+ 00479a60 bytes 14781f94
- 00456bdc ["INT_ADD", "register:40f0:8", ["const:456bdc:8", "const:4:8"]]
- 00456bdc ["CALL", null, ["callee:00c538e0:8"]]
+ 00479a74 ["INT_ADD", "register:40f0:8", ["const:479a74:8", "const:4:8"]]
+ 00479a74 ["CALL", null, ["callee:00c538e0:8"]]
- 00456bdc bytes ad001e94
+ 00479a74 bytes 9b671f94
- 00456bfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00456bfc ["INT_ADD", "register:40f0:8", ["const:456bfc:8", "const:4:8"]]
- 00456bfc ["CALLIND", null, ["register:0:8"]]
+ 00479a94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479a94 ["INT_ADD", "register:40f0:8", ["const:479a94:8", "const:4:8"]]
+ 00479a94 ["CALLIND", null, ["register:0:8"]]
- 00456bfc bytes 00013fd6
+ 00479a94 bytes 00013fd6
~~~


<a id="compare-044fd36dcd290093671a0f7b6b2118d0"></a>

### [`00456c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c10.md) → [`00479aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479aa8.md) FUN_00479aa8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00456c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c10.md#insn-00456c2c) · [`00456c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c10.md#insn-00456c40) · [`00456c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c10.md#insn-00456c54)
- 新版 `00479ac4`（命令位置の公開資料なし） · `00479ad8`（命令位置の公開資料なし） · `00479aec`（命令位置の公開資料なし）

~~~diff
- 00456c2c ["INT_ADD", "register:40f0:8", ["const:456c2c:8", "const:4:8"]]
- 00456c2c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00479ac4 ["INT_ADD", "register:40f0:8", ["const:479ac4:8", "const:4:8"]]
+ 00479ac4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00456c2c bytes 0d111e94
+ 00479ac4 bytes fb771f94
- 00456c40 ["INT_ADD", "register:40f0:8", ["const:456c40:8", "const:4:8"]]
- 00456c40 ["CALL", null, ["callee:00c538e0:8"]]
+ 00479ad8 ["INT_ADD", "register:40f0:8", ["const:479ad8:8", "const:4:8"]]
+ 00479ad8 ["CALL", null, ["callee:00c538e0:8"]]
- 00456c40 bytes 94001e94
+ 00479ad8 bytes 82671f94
- 00456c54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00456c54 ["INT_ADD", "register:40f0:8", ["const:456c54:8", "const:4:8"]]
- 00456c54 ["CALLIND", null, ["register:0:8"]]
+ 00479aec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479aec ["INT_ADD", "register:40f0:8", ["const:479aec:8", "const:4:8"]]
+ 00479aec ["CALLIND", null, ["register:0:8"]]
- 00456c54 bytes 00013fd6
+ 00479aec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a54fd9b5bf218869cf916a3878ae7c0e"></a>

### [`00456e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456e40.md) → [`00479cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479cd8.md) FUN_00479cd8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00456e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456e40.md#insn-00456e5c) · [`00456e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456e40.md#insn-00456e7c)
- 新版 `00479cf4`（命令位置の公開資料なし） · `00479d14`（命令位置の公開資料なし）

~~~diff
- 00456e5c ["INT_ADD", "register:40f0:8", ["const:456e5c:8", "const:4:8"]]
- 00456e5c ["CALL", null, ["callee:00c538e0:8"]]
+ 00479cf4 ["INT_ADD", "register:40f0:8", ["const:479cf4:8", "const:4:8"]]
+ 00479cf4 ["CALL", null, ["callee:00c538e0:8"]]
- 00456e5c bytes 0d001e94
+ 00479cf4 bytes fb661f94
- 00456e7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00456e7c ["INT_ADD", "register:40f0:8", ["const:456e7c:8", "const:4:8"]]
- 00456e7c ["CALLIND", null, ["register:0:8"]]
+ 00479d14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479d14 ["INT_ADD", "register:40f0:8", ["const:479d14:8", "const:4:8"]]
+ 00479d14 ["CALLIND", null, ["register:0:8"]]
- 00456e7c bytes 00013fd6
+ 00479d14 bytes 00013fd6
~~~


<a id="compare-5db3e3e41ea96c170687fddf8af28028"></a>

### [`00457074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457074.md) → [`00479f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f0c.md) FUN_00479f0c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00457090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457074.md#insn-00457090) · [`004570b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457074.md#insn-004570b0)
- 新版 `00479f28`（命令位置の公開資料なし） · `00479f48`（命令位置の公開資料なし）

~~~diff
- 00457090 ["INT_ADD", "register:40f0:8", ["const:457090:8", "const:4:8"]]
- 00457090 ["CALL", null, ["callee:00c538e0:8"]]
+ 00479f28 ["INT_ADD", "register:40f0:8", ["const:479f28:8", "const:4:8"]]
+ 00479f28 ["CALL", null, ["callee:00c538e0:8"]]
- 00457090 bytes 80ff1d94
+ 00479f28 bytes 6e661f94
- 004570b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004570b0 ["INT_ADD", "register:40f0:8", ["const:4570b0:8", "const:4:8"]]
- 004570b0 ["CALLIND", null, ["register:0:8"]]
+ 00479f48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479f48 ["INT_ADD", "register:40f0:8", ["const:479f48:8", "const:4:8"]]
+ 00479f48 ["CALLIND", null, ["register:0:8"]]
- 004570b0 bytes 00013fd6
+ 00479f48 bytes 00013fd6
~~~


<a id="compare-d59270ec751c17b6f0bb0d8ac0240087"></a>

### [`004570c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004570c4.md) → [`00479f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f5c.md) FUN_00479f5c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004570e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004570c4.md#insn-004570e4) · [`004570f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004570c4.md#insn-004570f8) · [`00457100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004570c4.md#insn-00457100)
- 新版 `00479f7c`（命令位置の公開資料なし） · `00479f90`（命令位置の公開資料なし） · `00479f98`（命令位置の公開資料なし）

~~~diff
- 004570e4 ["INT_ADD", "register:40f0:8", ["const:4570e4:8", "const:4:8"]]
- 004570e4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00479f7c ["INT_ADD", "register:40f0:8", ["const:479f7c:8", "const:4:8"]]
+ 00479f7c ["CALL", null, ["callee:00c538e0:8"]]
- 004570e4 bytes 6bff1d94
+ 00479f7c bytes 59661f94
- 004570f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004570f8 ["INT_ADD", "register:40f0:8", ["const:4570f8:8", "const:4:8"]]
- 004570f8 ["CALLIND", null, ["register:0:8"]]
+ 00479f90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479f90 ["INT_ADD", "register:40f0:8", ["const:479f90:8", "const:4:8"]]
+ 00479f90 ["CALLIND", null, ["register:0:8"]]
- 004570f8 bytes 00013fd6
+ 00479f90 bytes 00013fd6
- 00457100 ["INT_ADD", "register:40f0:8", ["const:457100:8", "const:4:8"]]
- 00457100 ["CALL", null, ["callee:00c57a80:8"]]
+ 00479f98 ["INT_ADD", "register:40f0:8", ["const:479f98:8", "const:4:8"]]
+ 00479f98 ["CALL", null, ["callee:00c57a80:8"]]
- 00457100 bytes cc0f1e94
+ 00479f98 bytes ba761f94
~~~


<a id="compare-2e1a95e4ca73de33bc2304056a475b32"></a>

### [`00457690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457690.md) → [`0047a528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a528.md) FUN_0047a528

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004576ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457690.md#insn-004576ac) · [`004576cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457690.md#insn-004576cc)
- 新版 `0047a544`（命令位置の公開資料なし） · `0047a564`（命令位置の公開資料なし）

~~~diff
- 004576ac ["INT_ADD", "register:40f0:8", ["const:4576ac:8", "const:4:8"]]
- 004576ac ["CALL", null, ["callee:00c538e0:8"]]
+ 0047a544 ["INT_ADD", "register:40f0:8", ["const:47a544:8", "const:4:8"]]
+ 0047a544 ["CALL", null, ["callee:00c538e0:8"]]
- 004576ac bytes f9fd1d94
+ 0047a544 bytes e7641f94
- 004576cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004576cc ["INT_ADD", "register:40f0:8", ["const:4576cc:8", "const:4:8"]]
- 004576cc ["CALLIND", null, ["register:0:8"]]
+ 0047a564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a564 ["INT_ADD", "register:40f0:8", ["const:47a564:8", "const:4:8"]]
+ 0047a564 ["CALLIND", null, ["register:0:8"]]
- 004576cc bytes 00013fd6
+ 0047a564 bytes 00013fd6
~~~


<a id="compare-10facf887834b0dd45f2db7ed913938c"></a>

### [`004576e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004576e0.md) → [`0047a578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a578.md) FUN_0047a578

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004576fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004576e0.md#insn-004576fc) · [`0045771c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004576e0.md#insn-0045771c)
- 新版 `0047a594`（命令位置の公開資料なし） · `0047a5b4`（命令位置の公開資料なし）

~~~diff
- 004576fc ["INT_ADD", "register:40f0:8", ["const:4576fc:8", "const:4:8"]]
- 004576fc ["CALL", null, ["callee:00c538e0:8"]]
+ 0047a594 ["INT_ADD", "register:40f0:8", ["const:47a594:8", "const:4:8"]]
+ 0047a594 ["CALL", null, ["callee:00c538e0:8"]]
- 004576fc bytes e5fd1d94
+ 0047a594 bytes d3641f94
- 0045771c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045771c ["INT_ADD", "register:40f0:8", ["const:45771c:8", "const:4:8"]]
- 0045771c ["CALLIND", null, ["register:0:8"]]
+ 0047a5b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a5b4 ["INT_ADD", "register:40f0:8", ["const:47a5b4:8", "const:4:8"]]
+ 0047a5b4 ["CALLIND", null, ["register:0:8"]]
- 0045771c bytes 00013fd6
+ 0047a5b4 bytes 00013fd6
~~~


<a id="compare-8eac874559ddafed94ac4479a754b6c4"></a>

### [`0045786c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045786c.md) → [`0047a704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a704.md) FUN_0047a704

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004572a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a8.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0047a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00457888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045786c.md#insn-00457888) · [`004578a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045786c.md#insn-004578a8)
- 新版 `0047a720`（命令位置の公開資料なし） · `0047a740`（命令位置の公開資料なし）

~~~diff
- 00457888 ["INT_ADD", "register:40f0:8", ["const:457888:8", "const:4:8"]]
- 00457888 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047a720 ["INT_ADD", "register:40f0:8", ["const:47a720:8", "const:4:8"]]
+ 0047a720 ["CALL", null, ["callee:00c538e0:8"]]
- 00457888 bytes 82fd1d94
+ 0047a720 bytes 70641f94
- 004578a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004578a8 ["INT_ADD", "register:40f0:8", ["const:4578a8:8", "const:4:8"]]
- 004578a8 ["CALLIND", null, ["register:0:8"]]
+ 0047a740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a740 ["INT_ADD", "register:40f0:8", ["const:47a740:8", "const:4:8"]]
+ 0047a740 ["CALLIND", null, ["register:0:8"]]
- 004578a8 bytes 00013fd6
+ 0047a740 bytes 00013fd6
~~~


<a id="compare-e387f217d02f6e65e9887fa8e1a3965a"></a>

### [`004578bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004578bc.md) → [`0047a754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a754.md) FUN_0047a754

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004572a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a8.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0047a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004578dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004578bc.md#insn-004578dc) · [`004578f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004578bc.md#insn-004578f0) · [`004578f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004578bc.md#insn-004578f8)
- 新版 `0047a774`（命令位置の公開資料なし） · `0047a788`（命令位置の公開資料なし） · `0047a790`（命令位置の公開資料なし）

~~~diff
- 004578dc ["INT_ADD", "register:40f0:8", ["const:4578dc:8", "const:4:8"]]
- 004578dc ["CALL", null, ["callee:00c538e0:8"]]
+ 0047a774 ["INT_ADD", "register:40f0:8", ["const:47a774:8", "const:4:8"]]
+ 0047a774 ["CALL", null, ["callee:00c538e0:8"]]
- 004578dc bytes 6dfd1d94
+ 0047a774 bytes 5b641f94
- 004578f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004578f0 ["INT_ADD", "register:40f0:8", ["const:4578f0:8", "const:4:8"]]
- 004578f0 ["CALLIND", null, ["register:0:8"]]
+ 0047a788 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a788 ["INT_ADD", "register:40f0:8", ["const:47a788:8", "const:4:8"]]
+ 0047a788 ["CALLIND", null, ["register:0:8"]]
- 004578f0 bytes 00013fd6
+ 0047a788 bytes 00013fd6
- 004578f8 ["INT_ADD", "register:40f0:8", ["const:4578f8:8", "const:4:8"]]
- 004578f8 ["CALL", null, ["callee:00c57a80:8"]]
+ 0047a790 ["INT_ADD", "register:40f0:8", ["const:47a790:8", "const:4:8"]]
+ 0047a790 ["CALL", null, ["callee:00c57a80:8"]]
- 004578f8 bytes ce0d1e94
+ 0047a790 bytes bc741f94
~~~


<a id="compare-a25a0ce0bf1a25d2c0b70ddb14efa1a3"></a>

### [`00457ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457ecc.md) → [`0047ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047ad64.md) FUN_0047ad64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`0045cb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cb74.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00457eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457ecc.md#insn-00457eec) · [`00457ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457ecc.md#insn-00457ef8) · [`00457f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457ecc.md#insn-00457f0c)
- 新版 `0047ad84`（命令位置の公開資料なし） · `0047ad90`（命令位置の公開資料なし） · `0047ada4`（命令位置の公開資料なし）

~~~diff
- 00457eec ["INT_ADD", "register:40f0:8", ["const:457eec:8", "const:4:8"]]
- 00457eec ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047ad84 ["INT_ADD", "register:40f0:8", ["const:47ad84:8", "const:4:8"]]
+ 0047ad84 ["CALL", null, ["callee:00c57ab0:8"]]
- 00457eec bytes 5d0c1e94
+ 0047ad84 bytes 4b731f94
- 00457ef8 ["INT_ADD", "register:40f0:8", ["const:457ef8:8", "const:4:8"]]
- 00457ef8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047ad90 ["INT_ADD", "register:40f0:8", ["const:47ad90:8", "const:4:8"]]
+ 0047ad90 ["CALL", null, ["callee:00c57ab0:8"]]
- 00457ef8 bytes 5a0c1e94
+ 0047ad90 bytes 48731f94
- 00457f0c ["INT_ADD", "register:40f0:8", ["const:457f0c:8", "const:4:8"]]
- 00457f0c ["CALL", null, ["callee:00c538e0:8"]]
+ 0047ada4 ["INT_ADD", "register:40f0:8", ["const:47ada4:8", "const:4:8"]]
+ 0047ada4 ["CALL", null, ["callee:00c538e0:8"]]
- 00457f0c bytes e1fb1d94
+ 0047ada4 bytes cf621f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0363b25c322ea3de7f806ac4f1c8a029"></a>

### [`00458634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458634.md) → [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) FUN_0047b4cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00458038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md) [`007d8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d8/007d8824.md) [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 7件 [`0045a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) [`007c7938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md) [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 7件 [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004586e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458634.md#insn-004586e0) · [`00458714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458634.md#insn-00458714) · [`00458778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458634.md#insn-00458778)
- 新版 `0047b578`（命令位置の公開資料なし） · `0047b5ac`（命令位置の公開資料なし） · `0047b610`（命令位置の公開資料なし）

~~~diff
- 004586e0 ["INT_ADD", "register:40f0:8", ["const:4586e0:8", "const:4:8"]]
- 004586e0 ["CALL", null, ["callee:0047d574:8"]]
+ 0047b578 ["INT_ADD", "register:40f0:8", ["const:47b578:8", "const:4:8"]]
+ 0047b578 ["CALL", null, ["callee:0047d574:8"]]
- 004586e0 bytes ff070094
+ 0047b578 bytes ff070094
- 00458714 ["INT_ADD", "register:40f0:8", ["const:458714:8", "const:4:8"]]
- 00458714 ["CALL", null, ["callee:00c57b40:8"]]
+ 0047b5ac ["INT_ADD", "register:40f0:8", ["const:47b5ac:8", "const:4:8"]]
+ 0047b5ac ["CALL", null, ["callee:00c57b40:8"]]
- 00458714 bytes 770a1e94
+ 0047b5ac bytes 65711f94
- 00458778 ["INT_ADD", "register:40f0:8", ["const:458778:8", "const:4:8"]]
- 00458778 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047b610 ["INT_ADD", "register:40f0:8", ["const:47b610:8", "const:4:8"]]
+ 0047b610 ["CALL", null, ["callee:00c57ab0:8"]]
- 00458778 bytes 3a0a1e94
+ 0047b610 bytes 28711f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06cc0bdb19e717f2695c3e108dd438db"></a>

### [`004588f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588f4.md) → [`0047b78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b78c.md) FUN_0047b78c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00acc56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00b2bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045892c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588f4.md#insn-0045892c) · [`00458940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588f4.md#insn-00458940) · [`00458948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588f4.md#insn-00458948)
- 新版 `0047b7c4`（命令位置の公開資料なし） · `0047b7d8`（命令位置の公開資料なし） · `0047b7e0`（命令位置の公開資料なし）

~~~diff
- 0045892c ["INT_ADD", "register:40f0:8", ["const:45892c:8", "const:4:8"]]
- 0045892c ["CALL", null, ["callee:00c538e0:8"]]
+ 0047b7c4 ["INT_ADD", "register:40f0:8", ["const:47b7c4:8", "const:4:8"]]
+ 0047b7c4 ["CALL", null, ["callee:00c538e0:8"]]
- 0045892c bytes 59f91d94
+ 0047b7c4 bytes 47601f94
- 00458940 ["COPY", "register:0:8", ["register:4040:8"]]
- 00458940 ["INT_ADD", "register:40f0:8", ["const:458940:8", "const:4:8"]]
- 00458940 ["CALLIND", null, ["register:0:8"]]
+ 0047b7d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047b7d8 ["INT_ADD", "register:40f0:8", ["const:47b7d8:8", "const:4:8"]]
+ 0047b7d8 ["CALLIND", null, ["register:0:8"]]
- 00458940 bytes 00013fd6
+ 0047b7d8 bytes 00013fd6
- 00458948 ["INT_ADD", "register:40f0:8", ["const:458948:8", "const:4:8"]]
- 00458948 ["CALL", null, ["callee:00c57a80:8"]]
+ 0047b7e0 ["INT_ADD", "register:40f0:8", ["const:47b7e0:8", "const:4:8"]]
+ 0047b7e0 ["CALL", null, ["callee:00c57a80:8"]]
- 00458948 bytes ba091e94
+ 0047b7e0 bytes a8701f94
~~~


<a id="compare-45d5bfb2e501045094ec25cd95f02ebd"></a>

### [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) → [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) FUN_0047c928

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 27件 [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005edb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ed/005edb40.md) [`0060b7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b7bc.md) [`0060d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d1dc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0045a988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 27件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`00632cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0047d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md#insn-00459ae4) · [`00459af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md#insn-00459af4) · [`00459b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md#insn-00459b24)
- 新版 `0047c97c`（命令位置の公開資料なし） · `0047c98c`（命令位置の公開資料なし） · `0047c9bc`（命令位置の公開資料なし）

~~~diff
- 00459ae4 ["INT_ADD", "register:40f0:8", ["const:459ae4:8", "const:4:8"]]
- 00459ae4 ["CALL", null, ["callee:0043bae0:8"]]
+ 0047c97c ["INT_ADD", "register:40f0:8", ["const:47c97c:8", "const:4:8"]]
+ 0047c97c ["CALL", null, ["callee:0043bae0:8"]]
- 00459ae4 bytes 3ffdfe97
+ 0047c97c bytes 59fcfe97
- 00459af4 ["INT_ADD", "register:40f0:8", ["const:459af4:8", "const:4:8"]]
- 00459af4 ["CALL", null, ["callee:0043bae0:8"]]
+ 0047c98c ["INT_ADD", "register:40f0:8", ["const:47c98c:8", "const:4:8"]]
+ 0047c98c ["CALL", null, ["callee:0043bae0:8"]]
- 00459af4 bytes 3bfdfe97
+ 0047c98c bytes 55fcfe97
- 00459b24 ["INT_ADD", "register:40f0:8", ["const:459b24:8", "const:4:8"]]
- 00459b24 ["CALL", null, ["callee:0047d820:8"]]
+ 0047c9bc ["INT_ADD", "register:40f0:8", ["const:47c9bc:8", "const:4:8"]]
+ 0047c9bc ["CALL", null, ["callee:0047d820:8"]]
- 00459b24 bytes 99030094
+ 0047c9bc bytes 99030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-590945f4eaee8c38c5974aa61390e36a"></a>

### [`00459bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md) → [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md) FUN_0047ca4c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md) [`005c20ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c20ec.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`00628858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/00628858.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 27件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) [`005e6dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6dbc.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`0064e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md#insn-00459ce4) · [`00459d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md#insn-00459d04) · [`00459d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md#insn-00459d18)
- 新版 `0047cb7c`（命令位置の公開資料なし） · `0047cb9c`（命令位置の公開資料なし） · `0047cbb0`（命令位置の公開資料なし）

~~~diff
- 00459ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459ce4 ["INT_ADD", "register:40f0:8", ["const:459ce4:8", "const:4:8"]]
- 00459ce4 ["CALLIND", null, ["register:0:8"]]
+ 0047cb7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cb7c ["INT_ADD", "register:40f0:8", ["const:47cb7c:8", "const:4:8"]]
+ 0047cb7c ["CALLIND", null, ["register:0:8"]]
- 00459ce4 bytes 00013fd6
+ 0047cb7c bytes 00013fd6
- 00459d04 ["INT_ADD", "register:40f0:8", ["const:459d04:8", "const:4:8"]]
- 00459d04 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047cb9c ["INT_ADD", "register:40f0:8", ["const:47cb9c:8", "const:4:8"]]
+ 0047cb9c ["CALL", null, ["callee:00c538e0:8"]]
- 00459d04 bytes 63f41d94
+ 0047cb9c bytes 515b1f94
- 00459d18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459d18 ["INT_ADD", "register:40f0:8", ["const:459d18:8", "const:4:8"]]
- 00459d18 ["CALLIND", null, ["register:0:8"]]
+ 0047cbb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cbb0 ["INT_ADD", "register:40f0:8", ["const:47cbb0:8", "const:4:8"]]
+ 0047cbb0 ["CALLIND", null, ["register:0:8"]]
- 00459d18 bytes 00013fd6
+ 0047cbb0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e1125e3788cdd26b1353a1e5f0165cb"></a>

### [`00459e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459e50.md) → [`0047cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cce8.md) FUN_0047cce8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459e50.md#insn-00459e7c) · [`00459e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459e50.md#insn-00459e90) · [`00459e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459e50.md#insn-00459e98)
- 新版 `0047cd14`（命令位置の公開資料なし） · `0047cd28`（命令位置の公開資料なし） · `0047cd30`（命令位置の公開資料なし）

~~~diff
- 00459e7c ["INT_ADD", "register:40f0:8", ["const:459e7c:8", "const:4:8"]]
- 00459e7c ["CALL", null, ["callee:00c538e0:8"]]
+ 0047cd14 ["INT_ADD", "register:40f0:8", ["const:47cd14:8", "const:4:8"]]
+ 0047cd14 ["CALL", null, ["callee:00c538e0:8"]]
- 00459e7c bytes 05f41d94
+ 0047cd14 bytes f35a1f94
- 00459e90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459e90 ["INT_ADD", "register:40f0:8", ["const:459e90:8", "const:4:8"]]
- 00459e90 ["CALLIND", null, ["register:0:8"]]
+ 0047cd28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cd28 ["INT_ADD", "register:40f0:8", ["const:47cd28:8", "const:4:8"]]
+ 0047cd28 ["CALLIND", null, ["register:0:8"]]
- 00459e90 bytes 00013fd6
+ 0047cd28 bytes 00013fd6
- 00459e98 ["INT_ADD", "register:40f0:8", ["const:459e98:8", "const:4:8"]]
- 00459e98 ["CALL", null, ["callee:00c57a80:8"]]
+ 0047cd30 ["INT_ADD", "register:40f0:8", ["const:47cd30:8", "const:4:8"]]
+ 0047cd30 ["CALL", null, ["callee:00c57a80:8"]]
- 00459e98 bytes 66041e94
+ 0047cd30 bytes 546b1f94
~~~


<a id="compare-d6438cce45a899c17c77945a91161958"></a>

### [`00459eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459eac.md) → [`0047cd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd44.md) FUN_0047cd44

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459eac.md#insn-00459ec8) · [`00459ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459eac.md#insn-00459ee8)
- 新版 `0047cd60`（命令位置の公開資料なし） · `0047cd80`（命令位置の公開資料なし）

~~~diff
- 00459ec8 ["INT_ADD", "register:40f0:8", ["const:459ec8:8", "const:4:8"]]
- 00459ec8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047cd60 ["INT_ADD", "register:40f0:8", ["const:47cd60:8", "const:4:8"]]
+ 0047cd60 ["CALL", null, ["callee:00c538e0:8"]]
- 00459ec8 bytes f2f31d94
+ 0047cd60 bytes e05a1f94
- 00459ee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459ee8 ["INT_ADD", "register:40f0:8", ["const:459ee8:8", "const:4:8"]]
- 00459ee8 ["CALLIND", null, ["register:0:8"]]
+ 0047cd80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cd80 ["INT_ADD", "register:40f0:8", ["const:47cd80:8", "const:4:8"]]
+ 0047cd80 ["CALLIND", null, ["register:0:8"]]
- 00459ee8 bytes 00013fd6
+ 0047cd80 bytes 00013fd6
~~~


<a id="compare-026570dc176e4199b1b4430bb8a31c6f"></a>

### [`00459f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md) → [`0047cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md) FUN_0047cde8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`005f0e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e9c.md) [`006d5524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5524.md) [`007ca13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca13c.md) [`00822650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/00822650.md) [`0085ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 6件 [`006166dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166dc.md) [`006ff2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md) [`007fd33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md) [`008545cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008545cc.md) [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00459f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md#insn-00459f80) · [`00459fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md#insn-00459fd8) · [`00459ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md#insn-00459ff8)
- 新版 `0047ce18`（命令位置の公開資料なし） · `0047ce70`（命令位置の公開資料なし） · `0047ce90`（命令位置の公開資料なし）

~~~diff
- 00459f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459f80 ["INT_ADD", "register:40f0:8", ["const:459f80:8", "const:4:8"]]
- 00459f80 ["CALLIND", null, ["register:0:8"]]
+ 0047ce18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047ce18 ["INT_ADD", "register:40f0:8", ["const:47ce18:8", "const:4:8"]]
+ 0047ce18 ["CALLIND", null, ["register:0:8"]]
- 00459f80 bytes 00013fd6
+ 0047ce18 bytes 00013fd6
- 00459fd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459fd8 ["INT_ADD", "register:40f0:8", ["const:459fd8:8", "const:4:8"]]
- 00459fd8 ["CALLIND", null, ["register:0:8"]]
+ 0047ce70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047ce70 ["INT_ADD", "register:40f0:8", ["const:47ce70:8", "const:4:8"]]
+ 0047ce70 ["CALLIND", null, ["register:0:8"]]
- 00459fd8 bytes 00013fd6
+ 0047ce70 bytes 00013fd6
- 00459ff8 ["INT_ADD", "register:40f0:8", ["const:459ff8:8", "const:4:8"]]
- 00459ff8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047ce90 ["INT_ADD", "register:40f0:8", ["const:47ce90:8", "const:4:8"]]
+ 0047ce90 ["CALL", null, ["callee:00c538e0:8"]]
- 00459ff8 bytes a6f31d94
+ 0047ce90 bytes 945a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d037ecc9bb67093aff3cb85a43434148"></a>

### [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) → [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) FUN_0047cec8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`005f10d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10d0.md) [`006d584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d584c.md) [`007ca3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3b0.md) [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) · 呼出先 1件 [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md)
- 新版 呼出元 7件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00616910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md) [`006ff600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff600.md) [`007fd5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5b0.md) [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) · 呼出先 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045a098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md#insn-0045a098)
- 新版 `0047cf30`（命令位置の公開資料なし）

~~~diff
- 0045a098 ["INT_ADD", "register:40f0:8", ["const:45a098:8", "const:4:8"]]
- 0045a098 ["CALL", null, ["callee:0047c008:8"]]
+ 0047cf30 ["INT_ADD", "register:40f0:8", ["const:47cf30:8", "const:4:8"]]
+ 0047cf30 ["CALL", null, ["callee:0047c008:8"]]
- 0045a098 bytes 36fcff97
+ 0047cf30 bytes 36fcff97
~~~


<a id="compare-0a3255337496662d6d9dfff7190cf77e"></a>

### [`0045a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0e0.md) → [`0047cf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf78.md) FUN_0047cf78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0084d464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d464.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 3件 [`008803fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045a154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0e0.md#insn-0045a154) · [`0045a174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0e0.md#insn-0045a174) · [`0045a188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0e0.md#insn-0045a188)
- 新版 `0047cfec`（命令位置の公開資料なし） · `0047d00c`（命令位置の公開資料なし） · `0047d020`（命令位置の公開資料なし）

~~~diff
- 0045a154 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a154 ["INT_ADD", "register:40f0:8", ["const:45a154:8", "const:4:8"]]
- 0045a154 ["CALLIND", null, ["register:0:8"]]
+ 0047cfec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cfec ["INT_ADD", "register:40f0:8", ["const:47cfec:8", "const:4:8"]]
+ 0047cfec ["CALLIND", null, ["register:0:8"]]
- 0045a154 bytes 00013fd6
+ 0047cfec bytes 00013fd6
- 0045a174 ["INT_ADD", "register:40f0:8", ["const:45a174:8", "const:4:8"]]
- 0045a174 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047d00c ["INT_ADD", "register:40f0:8", ["const:47d00c:8", "const:4:8"]]
+ 0047d00c ["CALL", null, ["callee:00c538e0:8"]]
- 0045a174 bytes 47f31d94
+ 0047d00c bytes 355a1f94
- 0045a188 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a188 ["INT_ADD", "register:40f0:8", ["const:45a188:8", "const:4:8"]]
- 0045a188 ["CALLIND", null, ["register:0:8"]]
+ 0047d020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d020 ["INT_ADD", "register:40f0:8", ["const:47d020:8", "const:4:8"]]
+ 0047d020 ["CALLIND", null, ["register:0:8"]]
- 0045a188 bytes 00013fd6
+ 0047d020 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bed3509ecde1965203981cf166dce8ec"></a>

### [`0045a244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a244.md) → [`0047d0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d0dc.md) FUN_0047d0dc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008feab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008feab4.md) [`008ff388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff388.md) [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 0件 
- 新版 呼出元 3件 [`009334e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/009334e8.md) [`00933dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933dbc.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045a2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a244.md#insn-0045a2c8)
- 新版 `0047d160`（命令位置の公開資料なし）

~~~diff
- 0045a2c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a2c8 ["INT_ADD", "register:40f0:8", ["const:45a2c8:8", "const:4:8"]]
- 0045a2c8 ["CALLIND", null, ["register:0:8"]]
+ 0047d160 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d160 ["INT_ADD", "register:40f0:8", ["const:47d160:8", "const:4:8"]]
+ 0047d160 ["CALLIND", null, ["register:0:8"]]
- 0045a2c8 bytes 00013fd6
+ 0047d160 bytes 00013fd6
~~~


<a id="compare-ec0fdba943fbf4948b2a164782da4671"></a>

### [`0045a3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a3a4.md) → [`0047d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md) FUN_0047d23c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00458038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0045a52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a52c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0047d3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045a41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a3a4.md#insn-0045a41c) · [`0045a440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a3a4.md#insn-0045a440) · [`0045a46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a3a4.md#insn-0045a46c)
- 新版 `0047d2b4`（命令位置の公開資料なし） · `0047d2d8`（命令位置の公開資料なし） · `0047d304`（命令位置の公開資料なし）

~~~diff
- 0045a41c ["INT_ADD", "register:40f0:8", ["const:45a41c:8", "const:4:8"]]
- 0045a41c ["CALL", null, ["callee:00c57a90:8"]]
+ 0047d2b4 ["INT_ADD", "register:40f0:8", ["const:47d2b4:8", "const:4:8"]]
+ 0047d2b4 ["CALL", null, ["callee:00c57a90:8"]]
- 0045a41c bytes 09031e94
+ 0047d2b4 bytes f7691f94
- 0045a440 ["INT_ADD", "register:40f0:8", ["const:45a440:8", "const:4:8"]]
- 0045a440 ["CALL", null, ["callee:00c57c90:8"]]
+ 0047d2d8 ["INT_ADD", "register:40f0:8", ["const:47d2d8:8", "const:4:8"]]
+ 0047d2d8 ["CALL", null, ["callee:00c57c90:8"]]
- 0045a440 bytes 80031e94
+ 0047d2d8 bytes 6e6a1f94
- 0045a46c ["INT_ADD", "register:40f0:8", ["const:45a46c:8", "const:4:8"]]
- 0045a46c ["CALL", null, ["callee:00c57c90:8"]]
+ 0047d304 ["INT_ADD", "register:40f0:8", ["const:47d304:8", "const:4:8"]]
+ 0047d304 ["CALL", null, ["callee:00c57c90:8"]]
- 0045a46c bytes 75031e94
+ 0047d304 bytes 636a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7a5613f92ad8be0089dd95d010bf895"></a>

### [`0045a540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a540.md) → [`0047d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3d8.md) FUN_0047d3d8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00458038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0045a6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6c8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0047d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a540.md#insn-0045a5b8) · [`0045a5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a540.md#insn-0045a5dc) · [`0045a608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a540.md#insn-0045a608)
- 新版 `0047d450`（命令位置の公開資料なし） · `0047d474`（命令位置の公開資料なし） · `0047d4a0`（命令位置の公開資料なし）

~~~diff
- 0045a5b8 ["INT_ADD", "register:40f0:8", ["const:45a5b8:8", "const:4:8"]]
- 0045a5b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0047d450 ["INT_ADD", "register:40f0:8", ["const:47d450:8", "const:4:8"]]
+ 0047d450 ["CALL", null, ["callee:00c57a90:8"]]
- 0045a5b8 bytes a2021e94
+ 0047d450 bytes 90691f94
- 0045a5dc ["INT_ADD", "register:40f0:8", ["const:45a5dc:8", "const:4:8"]]
- 0045a5dc ["CALL", null, ["callee:00c57c90:8"]]
+ 0047d474 ["INT_ADD", "register:40f0:8", ["const:47d474:8", "const:4:8"]]
+ 0047d474 ["CALL", null, ["callee:00c57c90:8"]]
- 0045a5dc bytes 19031e94
+ 0047d474 bytes 076a1f94
- 0045a608 ["INT_ADD", "register:40f0:8", ["const:45a608:8", "const:4:8"]]
- 0045a608 ["CALL", null, ["callee:00c57c90:8"]]
+ 0047d4a0 ["INT_ADD", "register:40f0:8", ["const:47d4a0:8", "const:4:8"]]
+ 0047d4a0 ["CALL", null, ["callee:00c57c90:8"]]
- 0045a608 bytes 0e031e94
+ 0047d4a0 bytes fc691f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f76e4f7126da0d8feaf76daac6eaaf"></a>

### [`0045a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md) → [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) FUN_0047d574

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00458634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458634.md) [`004785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md) [`0047bdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bdcc.md) [`007da86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da86c.md) [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 3件 [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 5件 [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`0049ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md) [`0080f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080f0e8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045a70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md#insn-0045a70c) · [`0045a7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md#insn-0045a7dc)
- 新版 `0047d5a4`（命令位置の公開資料なし） · `0047d674`（命令位置の公開資料なし）

~~~diff
- 0045a70c ["INT_ADD", "register:40f0:8", ["const:45a70c:8", "const:4:8"]]
- 0045a70c ["CALL", null, ["callee:00c57a90:8"]]
+ 0047d5a4 ["INT_ADD", "register:40f0:8", ["const:47d5a4:8", "const:4:8"]]
+ 0047d5a4 ["CALL", null, ["callee:00c57a90:8"]]
- 0045a70c bytes 4d021e94
+ 0047d5a4 bytes 3b691f94
- 0045a7dc ["INT_ADD", "register:40f0:8", ["const:45a7dc:8", "const:4:8"]]
- 0045a7dc ["CALL", null, ["callee:0047d678:8"]]
+ 0047d674 ["INT_ADD", "register:40f0:8", ["const:47d674:8", "const:4:8"]]
+ 0047d674 ["CALL", null, ["callee:0047d678:8"]]
- 0045a7dc bytes 01000094
+ 0047d674 bytes 01000094
~~~


<a id="compare-e2cb04d74c9d83be0a089d1e38595ce6"></a>

### [`0045a84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a84c.md) → [`0047d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e4.md) FUN_0047d6e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00458f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045a8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a84c.md#insn-0045a8a4) · [`0045a8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a84c.md#insn-0045a8c0) · [`0045a8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a84c.md#insn-0045a8d4)
- 新版 `0047d73c`（命令位置の公開資料なし） · `0047d758`（命令位置の公開資料なし） · `0047d76c`（命令位置の公開資料なし）

~~~diff
- 0045a8a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a8a4 ["INT_ADD", "register:40f0:8", ["const:45a8a4:8", "const:4:8"]]
- 0045a8a4 ["CALLIND", null, ["register:0:8"]]
+ 0047d73c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d73c ["INT_ADD", "register:40f0:8", ["const:47d73c:8", "const:4:8"]]
+ 0047d73c ["CALLIND", null, ["register:0:8"]]
- 0045a8a4 bytes 00013fd6
+ 0047d73c bytes 00013fd6
- 0045a8c0 ["INT_ADD", "register:40f0:8", ["const:45a8c0:8", "const:4:8"]]
- 0045a8c0 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047d758 ["INT_ADD", "register:40f0:8", ["const:47d758:8", "const:4:8"]]
+ 0047d758 ["CALL", null, ["callee:00c538e0:8"]]
- 0045a8c0 bytes 74f11d94
+ 0047d758 bytes 62581f94
- 0045a8d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a8d4 ["INT_ADD", "register:40f0:8", ["const:45a8d4:8", "const:4:8"]]
- 0045a8d4 ["CALLIND", null, ["register:0:8"]]
+ 0047d76c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d76c ["INT_ADD", "register:40f0:8", ["const:47d76c:8", "const:4:8"]]
+ 0047d76c ["CALLIND", null, ["register:0:8"]]
- 0045a8d4 bytes 00013fd6
+ 0047d76c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024ebe3724d433be1f01cf7af4f450c7"></a>

### [`0045be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045be0c.md) → [`0047eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eca4.md) FUN_0047eca4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0045c7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045be38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045be0c.md#insn-0045be38) · [`0045be50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045be0c.md#insn-0045be50) · [`0045be58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045be0c.md#insn-0045be58)
- 新版 `0047ecd0`（命令位置の公開資料なし） · `0047ece8`（命令位置の公開資料なし） · `0047ecf0`（命令位置の公開資料なし）

~~~diff
- 0045be38 ["INT_ADD", "register:40f0:8", ["const:45be38:8", "const:4:8"]]
- 0045be38 ["CALL", null, ["callee:0047f694:8"]]
+ 0047ecd0 ["INT_ADD", "register:40f0:8", ["const:47ecd0:8", "const:4:8"]]
+ 0047ecd0 ["CALL", null, ["callee:0047f694:8"]]
- 0045be38 bytes 71020094
+ 0047ecd0 bytes 71020094
- 0045be50 ["INT_ADD", "register:40f0:8", ["const:45be50:8", "const:4:8"]]
- 0045be50 ["CALL", null, ["callee:00c580e0:8"]]
+ 0047ece8 ["INT_ADD", "register:40f0:8", ["const:47ece8:8", "const:4:8"]]
+ 0047ece8 ["CALL", null, ["callee:00c580e0:8"]]
- 0045be50 bytes 10fe1d94
+ 0047ece8 bytes fe641f94
- 0045be58 ["INT_ADD", "register:40f0:8", ["const:45be58:8", "const:4:8"]]
- 0045be58 ["CALL", null, ["callee:00c580e0:8"]]
+ 0047ecf0 ["INT_ADD", "register:40f0:8", ["const:47ecf0:8", "const:4:8"]]
+ 0047ecf0 ["CALL", null, ["callee:00c580e0:8"]]
- 0045be58 bytes 0efe1d94
+ 0047ecf0 bytes fc641f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c06f9c99e3109cd86643cdca0507fa1"></a>

### [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) → [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) FUN_0047ed74

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 216件 [`0045b334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md) [`00595ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md) [`0059fbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md) [`005a74e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a74e4.md) [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) · 呼出先 4件 [`0045bf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf28.md) [`0045bfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bfd8.md) [`00474da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 207件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`005ba2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md) [`005c421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) [`005cc174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md) [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) · 呼出先 4件 [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045befc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md#insn-0045befc) · [`0045bf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md#insn-0045bf04) · [`0045bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md#insn-0045bf10)
- 新版 `0047ed94`（命令位置の公開資料なし） · `0047ed9c`（命令位置の公開資料なし） · `0047eda8`（命令位置の公開資料なし）

~~~diff
- 0045befc ["INT_ADD", "register:40f0:8", ["const:45befc:8", "const:4:8"]]
- 0045befc ["CALL", null, ["callee:00497c3c:8"]]
+ 0047ed94 ["INT_ADD", "register:40f0:8", ["const:47ed94:8", "const:4:8"]]
+ 0047ed94 ["CALL", null, ["callee:00497c3c:8"]]
- 0045befc bytes aa630094
+ 0047ed94 bytes aa630094
- 0045bf04 ["INT_ADD", "register:40f0:8", ["const:45bf04:8", "const:4:8"]]
- 0045bf04 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047ed9c ["INT_ADD", "register:40f0:8", ["const:47ed9c:8", "const:4:8"]]
+ 0047ed9c ["CALL", null, ["callee:00c57ab0:8"]]
- 0045bf04 bytes 57fc1d94
+ 0047ed9c bytes 45631f94
- 0045bf10 ["INT_ADD", "register:40f0:8", ["const:45bf10:8", "const:4:8"]]
- 0045bf10 ["CALL", null, ["callee:0047edc0:8"]]
+ 0047eda8 ["INT_ADD", "register:40f0:8", ["const:47eda8:8", "const:4:8"]]
+ 0047eda8 ["CALL", null, ["callee:0047edc0:8"]]
- 0045bf10 bytes 06000094
+ 0047eda8 bytes 06000094
~~~


<a id="compare-549b5ae0f720805004afd3f00ba2239f"></a>

### [`0045bf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf28.md) → [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) FUN_0047edc0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0045bf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf28.md) · 呼出先 3件 [`0045bf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf28.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) · 呼出先 3件 [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045bf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf28.md#insn-0045bf44) · [`0045bf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf28.md#insn-0045bf50) · [`0045bf5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf28.md#insn-0045bf5c)
- 新版 `0047eddc`（命令位置の公開資料なし） · `0047ede8`（命令位置の公開資料なし） · `0047edf4`（命令位置の公開資料なし）

~~~diff
- 0045bf44 ["INT_ADD", "register:40f0:8", ["const:45bf44:8", "const:4:8"]]
- 0045bf44 ["CALL", null, ["local:b0:8"]]
+ 0047eddc ["INT_ADD", "register:40f0:8", ["const:47eddc:8", "const:4:8"]]
+ 0047eddc ["CALL", null, ["local:b0:8"]]
- 0045bf44 bytes f9ffff97
+ 0047eddc bytes f9ffff97
- 0045bf50 ["INT_ADD", "register:40f0:8", ["const:45bf50:8", "const:4:8"]]
- 0045bf50 ["CALL", null, ["local:b0:8"]]
+ 0047ede8 ["INT_ADD", "register:40f0:8", ["const:47ede8:8", "const:4:8"]]
+ 0047ede8 ["CALL", null, ["local:b0:8"]]
- 0045bf50 bytes f6ffff97
+ 0047ede8 bytes f6ffff97
- 0045bf5c ["INT_ADD", "register:40f0:8", ["const:45bf5c:8", "const:4:8"]]
- 0045bf5c ["CALL", null, ["callee:00c57a80:8"]]
+ 0047edf4 ["INT_ADD", "register:40f0:8", ["const:47edf4:8", "const:4:8"]]
+ 0047edf4 ["CALL", null, ["callee:00c57a80:8"]]
- 0045bf5c bytes 35fc1d94
+ 0047edf4 bytes 23631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29c724d8476a6a935bfb17c09911f03b"></a>

### [`0045bf94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf94.md) → [`0047ee2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee2c.md) FUN_0047ee2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045bfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bf94.md#insn-0045bfb0)
- 新版 `0047ee48`（命令位置の公開資料なし）

~~~diff
- 0045bfb0 ["INT_ADD", "register:40f0:8", ["const:45bfb0:8", "const:4:8"]]
- 0045bfb0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047ee48 ["INT_ADD", "register:40f0:8", ["const:47ee48:8", "const:4:8"]]
+ 0047ee48 ["CALL", null, ["callee:00c57ab0:8"]]
- 0045bfb0 bytes 2cfc1d94
+ 0047ee48 bytes 1a631f94
~~~


<a id="compare-370ff54887fdaa065a23b3d36c3491b4"></a>

### [`0045bfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bfd8.md) → [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) FUN_0047ee70

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0045bfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bfd8.md) · 呼出先 3件 [`0045bfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bfd8.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) · 呼出先 3件 [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bfd8.md#insn-0045bff4) · [`0045c000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bfd8.md#insn-0045c000) · [`0045c00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bfd8.md#insn-0045c00c)
- 新版 `0047ee8c`（命令位置の公開資料なし） · `0047ee98`（命令位置の公開資料なし） · `0047eea4`（命令位置の公開資料なし）

~~~diff
- 0045bff4 ["INT_ADD", "register:40f0:8", ["const:45bff4:8", "const:4:8"]]
- 0045bff4 ["CALL", null, ["local:b0:8"]]
+ 0047ee8c ["INT_ADD", "register:40f0:8", ["const:47ee8c:8", "const:4:8"]]
+ 0047ee8c ["CALL", null, ["local:b0:8"]]
- 0045bff4 bytes f9ffff97
+ 0047ee8c bytes f9ffff97
- 0045c000 ["INT_ADD", "register:40f0:8", ["const:45c000:8", "const:4:8"]]
- 0045c000 ["CALL", null, ["local:b0:8"]]
+ 0047ee98 ["INT_ADD", "register:40f0:8", ["const:47ee98:8", "const:4:8"]]
+ 0047ee98 ["CALL", null, ["local:b0:8"]]
- 0045c000 bytes f6ffff97
+ 0047ee98 bytes f6ffff97
- 0045c00c ["INT_ADD", "register:40f0:8", ["const:45c00c:8", "const:4:8"]]
- 0045c00c ["CALL", null, ["callee:00c57a80:8"]]
+ 0047eea4 ["INT_ADD", "register:40f0:8", ["const:47eea4:8", "const:4:8"]]
+ 0047eea4 ["CALL", null, ["callee:00c57a80:8"]]
- 0045c00c bytes 09fc1d94
+ 0047eea4 bytes f7621f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fc7109cb0521b6923209b36e53637d4"></a>

### [`0045c034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c034.md) → [`0047eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eecc.md) FUN_0047eecc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c034.md#insn-0045c0a0) · [`0045c0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c034.md#insn-0045c0fc)
- 新版 `0047ef38`（命令位置の公開資料なし） · `0047ef94`（命令位置の公開資料なし）

~~~diff
- 0045c0a0 ["INT_ADD", "register:40f0:8", ["const:45c0a0:8", "const:4:8"]]
- 0045c0a0 ["CALL", null, ["callee:00c57c50:8"]]
+ 0047ef38 ["INT_ADD", "register:40f0:8", ["const:47ef38:8", "const:4:8"]]
+ 0047ef38 ["CALL", null, ["callee:00c57c50:8"]]
- 0045c0a0 bytes 58fc1d94
+ 0047ef38 bytes 46631f94
- 0045c0fc ["INT_ADD", "register:40f0:8", ["const:45c0fc:8", "const:4:8"]]
- 0045c0fc ["CALL", null, ["callee:00c57c50:8"]]
+ 0047ef94 ["INT_ADD", "register:40f0:8", ["const:47ef94:8", "const:4:8"]]
+ 0047ef94 ["CALL", null, ["callee:00c57c50:8"]]
- 0045c0fc bytes 41fc1d94
+ 0047ef94 bytes 2f631f94
~~~


<a id="compare-78dde56e16da91b11a4b59713f848fe7"></a>

### [`0045c184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c184.md) → [`0047f01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f01c.md) FUN_0047f01c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c178.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0047f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f010.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c184.md#insn-0045c1a4) · [`0045c1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c184.md#insn-0045c1b8) · [`0045c1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c184.md#insn-0045c1c0)
- 新版 `0047f03c`（命令位置の公開資料なし） · `0047f050`（命令位置の公開資料なし） · `0047f058`（命令位置の公開資料なし）

~~~diff
- 0045c1a4 ["INT_ADD", "register:40f0:8", ["const:45c1a4:8", "const:4:8"]]
- 0045c1a4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047f03c ["INT_ADD", "register:40f0:8", ["const:47f03c:8", "const:4:8"]]
+ 0047f03c ["CALL", null, ["callee:00c538e0:8"]]
- 0045c1a4 bytes 3beb1d94
+ 0047f03c bytes 29521f94
- 0045c1b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c1b8 ["INT_ADD", "register:40f0:8", ["const:45c1b8:8", "const:4:8"]]
- 0045c1b8 ["CALLIND", null, ["register:0:8"]]
+ 0047f050 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047f050 ["INT_ADD", "register:40f0:8", ["const:47f050:8", "const:4:8"]]
+ 0047f050 ["CALLIND", null, ["register:0:8"]]
- 0045c1b8 bytes 00013fd6
+ 0047f050 bytes 00013fd6
- 0045c1c0 ["INT_ADD", "register:40f0:8", ["const:45c1c0:8", "const:4:8"]]
- 0045c1c0 ["CALL", null, ["callee:00c57a80:8"]]
+ 0047f058 ["INT_ADD", "register:40f0:8", ["const:47f058:8", "const:4:8"]]
+ 0047f058 ["CALL", null, ["callee:00c57a80:8"]]
- 0045c1c0 bytes 9cfb1d94
+ 0047f058 bytes 8a621f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f17dbfb064f43b9c8b69b6032a0e202b"></a>

### [`0045c274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c274.md) → [`0047f10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f10c.md) FUN_0047f10c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c274.md#insn-0045c2f8) · [`0045c324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c274.md#insn-0045c324)
- 新版 `0047f190`（命令位置の公開資料なし） · `0047f1bc`（命令位置の公開資料なし）

~~~diff
- 0045c2f8 ["INT_ADD", "register:40f0:8", ["const:45c2f8:8", "const:4:8"]]
- 0045c2f8 ["CALL", null, ["callee:00c57c50:8"]]
+ 0047f190 ["INT_ADD", "register:40f0:8", ["const:47f190:8", "const:4:8"]]
+ 0047f190 ["CALL", null, ["callee:00c57c50:8"]]
- 0045c2f8 bytes c2fb1d94
+ 0047f190 bytes b0621f94
- 0045c324 ["INT_ADD", "register:40f0:8", ["const:45c324:8", "const:4:8"]]
- 0045c324 ["CALL", null, ["callee:00c57c50:8"]]
+ 0047f1bc ["INT_ADD", "register:40f0:8", ["const:47f1bc:8", "const:4:8"]]
+ 0047f1bc ["CALL", null, ["callee:00c57c50:8"]]
- 0045c324 bytes b7fb1d94
+ 0047f1bc bytes a5621f94
~~~


<a id="compare-8487f97a9640e50b9502c723ff74a096"></a>

### [`0045c378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md) → [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) FUN_0047f210

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045c584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) · 呼出先 3件 [`0045c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c484.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 3件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) · 呼出先 3件 [`0047f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f31c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md#insn-0045c3ec) · [`0045c41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md#insn-0045c41c) · [`0045c44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md#insn-0045c44c)
- 新版 `0047f284`（命令位置の公開資料なし） · `0047f2b4`（命令位置の公開資料なし） · `0047f2e4`（命令位置の公開資料なし）

~~~diff
- 0045c3ec ["INT_ADD", "register:40f0:8", ["const:45c3ec:8", "const:4:8"]]
- 0045c3ec ["CALL", null, ["callee:00c57c50:8"]]
+ 0047f284 ["INT_ADD", "register:40f0:8", ["const:47f284:8", "const:4:8"]]
+ 0047f284 ["CALL", null, ["callee:00c57c50:8"]]
- 0045c3ec bytes 85fb1d94
+ 0047f284 bytes 73621f94
- 0045c41c ["INT_ADD", "register:40f0:8", ["const:45c41c:8", "const:4:8"]]
- 0045c41c ["CALL", null, ["callee:00c57c50:8"]]
+ 0047f2b4 ["INT_ADD", "register:40f0:8", ["const:47f2b4:8", "const:4:8"]]
+ 0047f2b4 ["CALL", null, ["callee:00c57c50:8"]]
- 0045c41c bytes 79fb1d94
+ 0047f2b4 bytes 67621f94
- 0045c44c ["INT_ADD", "register:40f0:8", ["const:45c44c:8", "const:4:8"]]
- 0045c44c ["CALL", null, ["callee:0047f31c:8"]]
+ 0047f2e4 ["INT_ADD", "register:40f0:8", ["const:47f2e4:8", "const:4:8"]]
+ 0047f2e4 ["CALL", null, ["callee:0047f31c:8"]]
- 0045c44c bytes 0e000094
+ 0047f2e4 bytes 0e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfab3ec96fe6e25119fb256296927356"></a>

### [`0045c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c484.md) → [`0047f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f31c.md) FUN_0047f31c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0045c378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c484.md#insn-0045c4f0) · [`0045c520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c484.md#insn-0045c520)
- 新版 `0047f388`（命令位置の公開資料なし） · `0047f3b8`（命令位置の公開資料なし）

~~~diff
- 0045c4f0 ["INT_ADD", "register:40f0:8", ["const:45c4f0:8", "const:4:8"]]
- 0045c4f0 ["CALL", null, ["callee:00c57c50:8"]]
+ 0047f388 ["INT_ADD", "register:40f0:8", ["const:47f388:8", "const:4:8"]]
+ 0047f388 ["CALL", null, ["callee:00c57c50:8"]]
- 0045c4f0 bytes 44fb1d94
+ 0047f388 bytes 32621f94
- 0045c520 ["INT_ADD", "register:40f0:8", ["const:45c520:8", "const:4:8"]]
- 0045c520 ["CALL", null, ["callee:00c57c50:8"]]
+ 0047f3b8 ["INT_ADD", "register:40f0:8", ["const:47f3b8:8", "const:4:8"]]
+ 0047f3b8 ["CALL", null, ["callee:00c57c50:8"]]
- 0045c520 bytes 38fb1d94
+ 0047f3b8 bytes 26621f94
~~~


<a id="compare-08bb94a51dacf6c251f4e9a2fb024263"></a>

### [`0045c584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md) → [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) FUN_0047f41c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045c378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md) [`0045c6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c6b4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) [`0047f54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f54c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md#insn-0045c5ec) · [`0045c600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md#insn-0045c600) · [`0045c630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md#insn-0045c630)
- 新版 `0047f484`（命令位置の公開資料なし） · `0047f498`（命令位置の公開資料なし） · `0047f4c8`（命令位置の公開資料なし）

~~~diff
- 0045c5ec ["INT_ADD", "register:40f0:8", ["const:45c5ec:8", "const:4:8"]]
- 0045c5ec ["CALL", null, ["callee:0047f210:8"]]
+ 0047f484 ["INT_ADD", "register:40f0:8", ["const:47f484:8", "const:4:8"]]
+ 0047f484 ["CALL", null, ["callee:0047f210:8"]]
- 0045c5ec bytes 63ffff97
+ 0047f484 bytes 63ffff97
- 0045c600 ["INT_ADD", "register:40f0:8", ["const:45c600:8", "const:4:8"]]
- 0045c600 ["CALL", null, ["callee:0047f210:8"]]
+ 0047f498 ["INT_ADD", "register:40f0:8", ["const:47f498:8", "const:4:8"]]
+ 0047f498 ["CALL", null, ["callee:0047f210:8"]]
- 0045c600 bytes 5effff97
+ 0047f498 bytes 5effff97
- 0045c630 ["INT_ADD", "register:40f0:8", ["const:45c630:8", "const:4:8"]]
- 0045c630 ["CALL", null, ["callee:0047f54c:8"]]
+ 0047f4c8 ["INT_ADD", "register:40f0:8", ["const:47f4c8:8", "const:4:8"]]
+ 0047f4c8 ["CALL", null, ["callee:0047f54c:8"]]
- 0045c630 bytes 21000094
+ 0047f4c8 bytes 21000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec0e48bd2567299e09e7d7492ad2d97c"></a>

### [`0045c6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c6b4.md) → [`0047f54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f54c.md) FUN_0047f54c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0045c584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c6b4.md#insn-0045c6d4) · [`0045c70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c6b4.md#insn-0045c70c) · [`0045c738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c6b4.md#insn-0045c738)
- 新版 `0047f56c`（命令位置の公開資料なし） · `0047f5a4`（命令位置の公開資料なし） · `0047f5d0`（命令位置の公開資料なし）

~~~diff
- 0045c6d4 ["INT_ADD", "register:40f0:8", ["const:45c6d4:8", "const:4:8"]]
- 0045c6d4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0047f56c ["INT_ADD", "register:40f0:8", ["const:47f56c:8", "const:4:8"]]
+ 0047f56c ["CALL", null, ["callee:00c57a90:8"]]
- 0045c6d4 bytes 5bfa1d94
+ 0047f56c bytes 49611f94
- 0045c70c ["INT_ADD", "register:40f0:8", ["const:45c70c:8", "const:4:8"]]
- 0045c70c ["CALL", null, ["callee:0043bae0:8"]]
+ 0047f5a4 ["INT_ADD", "register:40f0:8", ["const:47f5a4:8", "const:4:8"]]
+ 0047f5a4 ["CALL", null, ["callee:0043bae0:8"]]
- 0045c70c bytes 35f2fe97
+ 0047f5a4 bytes 4ff1fe97
- 0045c738 ["INT_ADD", "register:40f0:8", ["const:45c738:8", "const:4:8"]]
- 0045c738 ["CALL", null, ["callee:0043bae0:8"]]
+ 0047f5d0 ["INT_ADD", "register:40f0:8", ["const:47f5d0:8", "const:4:8"]]
+ 0047f5d0 ["CALL", null, ["callee:0043bae0:8"]]
- 0045c738 bytes 2af2fe97
+ 0047f5d0 bytes 44f1fe97
~~~


<a id="compare-be9d2081accbe198367146c0489922df"></a>

### [`0045c794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c794.md) → [`0047f62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f62c.md) FUN_0047f62c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045c7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c794.md#insn-0045c7bc) · [`0045c7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c794.md#insn-0045c7cc) · [`0045c7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c794.md#insn-0045c7dc)
- 新版 `0047f654`（命令位置の公開資料なし） · `0047f664`（命令位置の公開資料なし） · `0047f674`（命令位置の公開資料なし）

~~~diff
- 0045c7bc ["INT_ADD", "register:40f0:8", ["const:45c7bc:8", "const:4:8"]]
- 0045c7bc ["CALL", null, ["callee:00c57a80:8"]]
+ 0047f654 ["INT_ADD", "register:40f0:8", ["const:47f654:8", "const:4:8"]]
+ 0047f654 ["CALL", null, ["callee:00c57a80:8"]]
- 0045c7bc bytes 1dfa1d94
+ 0047f654 bytes 0b611f94
- 0045c7cc ["INT_ADD", "register:40f0:8", ["const:45c7cc:8", "const:4:8"]]
- 0045c7cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047f664 ["INT_ADD", "register:40f0:8", ["const:47f664:8", "const:4:8"]]
+ 0047f664 ["CALL", null, ["callee:00c57ab0:8"]]
- 0045c7cc bytes 25fa1d94
+ 0047f664 bytes 13611f94
- 0045c7dc ["INT_ADD", "register:40f0:8", ["const:45c7dc:8", "const:4:8"]]
- 0045c7dc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047f674 ["INT_ADD", "register:40f0:8", ["const:47f674:8", "const:4:8"]]
+ 0047f674 ["CALL", null, ["callee:00c57ab0:8"]]
- 0045c7dc bytes 21fa1d94
+ 0047f674 bytes 0f611f94
~~~


<a id="compare-e642511bc6002c19764159bc892f07c2"></a>

### [`0045caa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045caa4.md) → [`0047f93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f93c.md) FUN_0047f93c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0045c7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md) · 呼出先 2件 [`00bdb6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6e0.md) [`00bdb6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6f0.md)
- 新版 呼出元 1件 [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) · 呼出先 2件 [`00c58130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045cab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045caa4.md#insn-0045cab4)
- 新版 `0047f94c`（命令位置の公開資料なし）

~~~diff
- 0045cab4 ["INT_ADD", "register:40f0:8", ["const:45cab4:8", "const:4:8"]]
- 0045cab4 ["CALL", null, ["callee:00c58130:8"]]
+ 0047f94c ["INT_ADD", "register:40f0:8", ["const:47f94c:8", "const:4:8"]]
+ 0047f94c ["CALL", null, ["callee:00c58130:8"]]
- 0045cab4 bytes 0bfb1d94
+ 0047f94c bytes f9611f94
~~~


<a id="compare-972e8218ea30ec3caffd8ae253a9ebee"></a>

### [`0045d240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md) → [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) FUN_004800d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 19件 [`0059c528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c528.md) [`0064504c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064504c.md) [`006b1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md) [`00704be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704be8.md) [`00708804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708804.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 23件 [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) [`0066b324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b324.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0072ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) [`00732904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md#insn-0045d26c) · [`0045d29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md#insn-0045d29c)
- 新版 `00480104`（命令位置の公開資料なし） · `00480134`（命令位置の公開資料なし）

~~~diff
- 0045d26c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d26c ["INT_ADD", "register:40f0:8", ["const:45d26c:8", "const:4:8"]]
- 0045d26c ["CALLIND", null, ["register:0:8"]]
+ 00480104 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480104 ["INT_ADD", "register:40f0:8", ["const:480104:8", "const:4:8"]]
+ 00480104 ["CALLIND", null, ["register:0:8"]]
- 0045d26c bytes 00013fd6
+ 00480104 bytes 00013fd6
- 0045d29c ["INT_ADD", "register:40f0:8", ["const:45d29c:8", "const:4:8"]]
- 0045d29c ["CALL", null, ["callee:00c57ae0:8"]]
+ 00480134 ["INT_ADD", "register:40f0:8", ["const:480134:8", "const:4:8"]]
+ 00480134 ["CALL", null, ["callee:00c57ae0:8"]]
- 0045d29c bytes 7df71d94
+ 00480134 bytes 6b5e1f94
~~~


<a id="compare-9e9ea58d39008142e3e0cac6ce9aa869"></a>

### [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md) → [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) FUN_00480138

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 22件 [`0059c528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c528.md) [`0064f874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f874.md) [`0067e574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067e/0067e574.md) [`006b1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md) [`0070e66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e66c.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 26件 [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) [`00675b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b54.md) [`006a48bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a4/006a48bc.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0073876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md#insn-0045d2cc) · [`0045d2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md#insn-0045d2fc)
- 新版 `00480164`（命令位置の公開資料なし） · `00480194`（命令位置の公開資料なし）

~~~diff
- 0045d2cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d2cc ["INT_ADD", "register:40f0:8", ["const:45d2cc:8", "const:4:8"]]
- 0045d2cc ["CALLIND", null, ["register:0:8"]]
+ 00480164 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480164 ["INT_ADD", "register:40f0:8", ["const:480164:8", "const:4:8"]]
+ 00480164 ["CALLIND", null, ["register:0:8"]]
- 0045d2cc bytes 00013fd6
+ 00480164 bytes 00013fd6
- 0045d2fc ["INT_ADD", "register:40f0:8", ["const:45d2fc:8", "const:4:8"]]
- 0045d2fc ["CALL", null, ["callee:00c57ae0:8"]]
+ 00480194 ["INT_ADD", "register:40f0:8", ["const:480194:8", "const:4:8"]]
+ 00480194 ["CALL", null, ["callee:00c57ae0:8"]]
- 0045d2fc bytes 65f71d94
+ 00480194 bytes 535e1f94
~~~


<a id="compare-d0c308e7250473e0b125ba8957067dd5"></a>

### [`0045d300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d300.md) → [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) FUN_00480198

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 17件 [`00645654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/00645654.md) [`0067e574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067e/0067e574.md) [`006b294c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b294c.md) [`0070e66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e66c.md) [`0071ada0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071ada0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 19件 [`0066b92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b92c.md) [`006a48bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a4/006a48bc.md) [`006dc708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc708.md) [`0073876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md) [`00744f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744f4c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d300.md#insn-0045d32c) · [`0045d35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d300.md#insn-0045d35c)
- 新版 `004801c4`（命令位置の公開資料なし） · `004801f4`（命令位置の公開資料なし）

~~~diff
- 0045d32c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d32c ["INT_ADD", "register:40f0:8", ["const:45d32c:8", "const:4:8"]]
- 0045d32c ["CALLIND", null, ["register:0:8"]]
+ 004801c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004801c4 ["INT_ADD", "register:40f0:8", ["const:4801c4:8", "const:4:8"]]
+ 004801c4 ["CALLIND", null, ["register:0:8"]]
- 0045d32c bytes 00013fd6
+ 004801c4 bytes 00013fd6
- 0045d35c ["INT_ADD", "register:40f0:8", ["const:45d35c:8", "const:4:8"]]
- 0045d35c ["CALL", null, ["callee:00c57ae0:8"]]
+ 004801f4 ["INT_ADD", "register:40f0:8", ["const:4801f4:8", "const:4:8"]]
+ 004801f4 ["CALL", null, ["callee:00c57ae0:8"]]
- 0045d35c bytes 4df71d94
+ 004801f4 bytes 3b5e1f94
~~~


<a id="compare-fcc0904bb7ea178049b0093e758b52e8"></a>

### [`0045d360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d360.md) → [`004801f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004801f8.md) FUN_004801f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d360.md#insn-0045d38c) · [`0045d3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d360.md#insn-0045d3bc)
- 新版 `00480224`（命令位置の公開資料なし） · `00480254`（命令位置の公開資料なし）

~~~diff
- 0045d38c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d38c ["INT_ADD", "register:40f0:8", ["const:45d38c:8", "const:4:8"]]
- 0045d38c ["CALLIND", null, ["register:0:8"]]
+ 00480224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480224 ["INT_ADD", "register:40f0:8", ["const:480224:8", "const:4:8"]]
+ 00480224 ["CALLIND", null, ["register:0:8"]]
- 0045d38c bytes 00013fd6
+ 00480224 bytes 00013fd6
- 0045d3bc ["INT_ADD", "register:40f0:8", ["const:45d3bc:8", "const:4:8"]]
- 0045d3bc ["CALL", null, ["callee:00c57ae0:8"]]
+ 00480254 ["INT_ADD", "register:40f0:8", ["const:480254:8", "const:4:8"]]
+ 00480254 ["CALL", null, ["callee:00c57ae0:8"]]
- 0045d3bc bytes 35f71d94
+ 00480254 bytes 235e1f94
~~~


<a id="compare-e40529a19744948b01ea668d4a1a0558"></a>

### [`0045d3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d3c0.md) → [`00480258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480258.md) FUN_00480258

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d3c0.md#insn-0045d3ec) · [`0045d41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d3c0.md#insn-0045d41c)
- 新版 `00480284`（命令位置の公開資料なし） · `004802b4`（命令位置の公開資料なし）

~~~diff
- 0045d3ec ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d3ec ["INT_ADD", "register:40f0:8", ["const:45d3ec:8", "const:4:8"]]
- 0045d3ec ["CALLIND", null, ["register:0:8"]]
+ 00480284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480284 ["INT_ADD", "register:40f0:8", ["const:480284:8", "const:4:8"]]
+ 00480284 ["CALLIND", null, ["register:0:8"]]
- 0045d3ec bytes 00013fd6
+ 00480284 bytes 00013fd6
- 0045d41c ["INT_ADD", "register:40f0:8", ["const:45d41c:8", "const:4:8"]]
- 0045d41c ["CALL", null, ["callee:00c57ae0:8"]]
+ 004802b4 ["INT_ADD", "register:40f0:8", ["const:4802b4:8", "const:4:8"]]
+ 004802b4 ["CALL", null, ["callee:00c57ae0:8"]]
- 0045d41c bytes 1df71d94
+ 004802b4 bytes 0b5e1f94
~~~


<a id="compare-4a80aa12d9f284420fe26cc0c9b4a882"></a>

### [`0045d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md) → [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) FUN_004802b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 29件 [`005953e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/005953e0.md) [`0064504c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064504c.md) [`006b1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md) [`00704be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704be8.md) [`00708804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708804.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 32件 [`005b9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md) [`0066b324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b324.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0072ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) [`00732904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md#insn-0045d44c) · [`0045d480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md#insn-0045d480)
- 新版 `004802e4`（命令位置の公開資料なし） · `00480318`（命令位置の公開資料なし）

~~~diff
- 0045d44c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d44c ["INT_ADD", "register:40f0:8", ["const:45d44c:8", "const:4:8"]]
- 0045d44c ["CALLIND", null, ["register:0:8"]]
+ 004802e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004802e4 ["INT_ADD", "register:40f0:8", ["const:4802e4:8", "const:4:8"]]
+ 004802e4 ["CALLIND", null, ["register:0:8"]]
- 0045d44c bytes 00013fd6
+ 004802e4 bytes 00013fd6
- 0045d480 ["INT_ADD", "register:40f0:8", ["const:45d480:8", "const:4:8"]]
- 0045d480 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00480318 ["INT_ADD", "register:40f0:8", ["const:480318:8", "const:4:8"]]
+ 00480318 ["CALL", null, ["callee:00c57ae0:8"]]
- 0045d480 bytes 04f71d94
+ 00480318 bytes f25d1f94
~~~


<a id="compare-f39abf6d28cf4b3c27b251079d9b5cd2"></a>

### [`0045d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d484.md) → [`0048031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048031c.md) FUN_0048031c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 3件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c644.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4dc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d484.md#insn-0045d4b8) · [`0045d4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d484.md#insn-0045d4cc) · [`0045d4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d484.md#insn-0045d4ec)
- 新版 `00480350`（命令位置の公開資料なし） · `00480364`（命令位置の公開資料なし） · `00480384`（命令位置の公開資料なし）

~~~diff
- 0045d4b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d4b8 ["INT_ADD", "register:40f0:8", ["const:45d4b8:8", "const:4:8"]]
- 0045d4b8 ["CALLIND", null, ["register:0:8"]]
+ 00480350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480350 ["INT_ADD", "register:40f0:8", ["const:480350:8", "const:4:8"]]
+ 00480350 ["CALLIND", null, ["register:0:8"]]
- 0045d4b8 bytes 00013fd6
+ 00480350 bytes 00013fd6
- 0045d4cc ["INT_ADD", "register:40f0:8", ["const:45d4cc:8", "const:4:8"]]
- 0045d4cc ["CALL", null, ["callee:0055f484:8"]]
+ 00480364 ["INT_ADD", "register:40f0:8", ["const:480364:8", "const:4:8"]]
+ 00480364 ["CALL", null, ["callee:0055f484:8"]]
- 0045d4cc bytes 487c0394
+ 00480364 bytes 487c0394
- 0045d4ec ["INT_ADD", "register:40f0:8", ["const:45d4ec:8", "const:4:8"]]
- 0045d4ec ["CALL", null, ["callee:0055f4dc:8"]]
+ 00480384 ["INT_ADD", "register:40f0:8", ["const:480384:8", "const:4:8"]]
+ 00480384 ["CALL", null, ["callee:0055f4dc:8"]]
- 0045d4ec bytes 567c0394
+ 00480384 bytes 567c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75c309a98a2e8abe391ea65400883233"></a>

### [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md) → [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) FUN_004803b0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 36件 [`005953e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/005953e0.md) [`005bb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb364.md) [`005bb3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3a8.md) [`005bb454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb454.md) [`005bb4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb4ec.md) · 呼出先 3件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c660.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 36件 [`005b9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md) [`005e0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md) [`005e0078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md) [`005e0124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0124.md) [`005e01bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md#insn-0045d54c) · [`0045d560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md#insn-0045d560) · [`0045d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md#insn-0045d580)
- 新版 `004803e4`（命令位置の公開資料なし） · `004803f8`（命令位置の公開資料なし） · `00480418`（命令位置の公開資料なし）

~~~diff
- 0045d54c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d54c ["INT_ADD", "register:40f0:8", ["const:45d54c:8", "const:4:8"]]
- 0045d54c ["CALLIND", null, ["register:0:8"]]
+ 004803e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004803e4 ["INT_ADD", "register:40f0:8", ["const:4803e4:8", "const:4:8"]]
+ 004803e4 ["CALLIND", null, ["register:0:8"]]
- 0045d54c bytes 00013fd6
+ 004803e4 bytes 00013fd6
- 0045d560 ["INT_ADD", "register:40f0:8", ["const:45d560:8", "const:4:8"]]
- 0045d560 ["CALL", null, ["callee:0055f484:8"]]
+ 004803f8 ["INT_ADD", "register:40f0:8", ["const:4803f8:8", "const:4:8"]]
+ 004803f8 ["CALL", null, ["callee:0055f484:8"]]
- 0045d560 bytes 237c0394
+ 004803f8 bytes 237c0394
- 0045d580 ["INT_ADD", "register:40f0:8", ["const:45d580:8", "const:4:8"]]
- 0045d580 ["CALL", null, ["callee:0055f4f8:8"]]
+ 00480418 ["INT_ADD", "register:40f0:8", ["const:480418:8", "const:4:8"]]
+ 00480418 ["CALL", null, ["callee:0055f4f8:8"]]
- 0045d580 bytes 387c0394
+ 00480418 bytes 387c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6ecce04ada364b694120a625d0665c3"></a>

### [`0045d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d5ac.md) → [`00480444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480444.md) FUN_00480444

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 3件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c660.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d5ac.md#insn-0045d5e0) · [`0045d5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d5ac.md#insn-0045d5f4) · [`0045d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d5ac.md#insn-0045d614)
- 新版 `00480478`（命令位置の公開資料なし） · `0048048c`（命令位置の公開資料なし） · `004804ac`（命令位置の公開資料なし）

~~~diff
- 0045d5e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d5e0 ["INT_ADD", "register:40f0:8", ["const:45d5e0:8", "const:4:8"]]
- 0045d5e0 ["CALLIND", null, ["register:0:8"]]
+ 00480478 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480478 ["INT_ADD", "register:40f0:8", ["const:480478:8", "const:4:8"]]
+ 00480478 ["CALLIND", null, ["register:0:8"]]
- 0045d5e0 bytes 00013fd6
+ 00480478 bytes 00013fd6
- 0045d5f4 ["INT_ADD", "register:40f0:8", ["const:45d5f4:8", "const:4:8"]]
- 0045d5f4 ["CALL", null, ["callee:0055f484:8"]]
+ 0048048c ["INT_ADD", "register:40f0:8", ["const:48048c:8", "const:4:8"]]
+ 0048048c ["CALL", null, ["callee:0055f484:8"]]
- 0045d5f4 bytes fe7b0394
+ 0048048c bytes fe7b0394
- 0045d614 ["INT_ADD", "register:40f0:8", ["const:45d614:8", "const:4:8"]]
- 0045d614 ["CALL", null, ["callee:0055f4f8:8"]]
+ 004804ac ["INT_ADD", "register:40f0:8", ["const:4804ac:8", "const:4:8"]]
+ 004804ac ["CALL", null, ["callee:0055f4f8:8"]]
- 0045d614 bytes 137c0394
+ 004804ac bytes 137c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c70d4438a4d6fa34b95d18086afae8c"></a>

### [`0045d640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d640.md) → [`004804d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004804d8.md) FUN_004804d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00807c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807c40.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`008395ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008395ac.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d640.md#insn-0045d674) · [`0045d6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d640.md#insn-0045d6a4) · [`0045d6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d640.md#insn-0045d6d8)
- 新版 `0048050c`（命令位置の公開資料なし） · `0048053c`（命令位置の公開資料なし） · `00480570`（命令位置の公開資料なし）

~~~diff
- 0045d674 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d674 ["INT_ADD", "register:40f0:8", ["const:45d674:8", "const:4:8"]]
- 0045d674 ["CALLIND", null, ["register:0:8"]]
+ 0048050c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048050c ["INT_ADD", "register:40f0:8", ["const:48050c:8", "const:4:8"]]
+ 0048050c ["CALLIND", null, ["register:0:8"]]
- 0045d674 bytes 00013fd6
+ 0048050c bytes 00013fd6
- 0045d6a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d6a4 ["INT_ADD", "register:40f0:8", ["const:45d6a4:8", "const:4:8"]]
- 0045d6a4 ["CALLIND", null, ["register:0:8"]]
+ 0048053c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048053c ["INT_ADD", "register:40f0:8", ["const:48053c:8", "const:4:8"]]
+ 0048053c ["CALLIND", null, ["register:0:8"]]
- 0045d6a4 bytes 00013fd6
+ 0048053c bytes 00013fd6
- 0045d6d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d6d8 ["INT_ADD", "register:40f0:8", ["const:45d6d8:8", "const:4:8"]]
- 0045d6d8 ["CALLIND", null, ["register:0:8"]]
+ 00480570 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480570 ["INT_ADD", "register:40f0:8", ["const:480570:8", "const:4:8"]]
+ 00480570 ["CALLIND", null, ["register:0:8"]]
- 0045d6d8 bytes 00013fd6
+ 00480570 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4efa436eb7d94a3a823e7aa7006b32"></a>

### [`0045d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d750.md) → [`004805e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004805e8.md) FUN_004805e8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 3件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c680.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f518.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d750.md#insn-0045d784) · [`0045d798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d750.md#insn-0045d798) · [`0045d7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d750.md#insn-0045d7b8)
- 新版 `0048061c`（命令位置の公開資料なし） · `00480630`（命令位置の公開資料なし） · `00480650`（命令位置の公開資料なし）

~~~diff
- 0045d784 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d784 ["INT_ADD", "register:40f0:8", ["const:45d784:8", "const:4:8"]]
- 0045d784 ["CALLIND", null, ["register:0:8"]]
+ 0048061c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048061c ["INT_ADD", "register:40f0:8", ["const:48061c:8", "const:4:8"]]
+ 0048061c ["CALLIND", null, ["register:0:8"]]
- 0045d784 bytes 00013fd6
+ 0048061c bytes 00013fd6
- 0045d798 ["INT_ADD", "register:40f0:8", ["const:45d798:8", "const:4:8"]]
- 0045d798 ["CALL", null, ["callee:0055f484:8"]]
+ 00480630 ["INT_ADD", "register:40f0:8", ["const:480630:8", "const:4:8"]]
+ 00480630 ["CALL", null, ["callee:0055f484:8"]]
- 0045d798 bytes 957b0394
+ 00480630 bytes 957b0394
- 0045d7b8 ["INT_ADD", "register:40f0:8", ["const:45d7b8:8", "const:4:8"]]
- 0045d7b8 ["CALL", null, ["callee:0055f518:8"]]
+ 00480650 ["INT_ADD", "register:40f0:8", ["const:480650:8", "const:4:8"]]
+ 00480650 ["CALL", null, ["callee:0055f518:8"]]
- 0045d7b8 bytes b27b0394
+ 00480650 bytes b27b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd20c49a8b9a5c9c4ce219ed7e7cde05"></a>

### [`0045d7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d7e4.md) → [`0048067c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048067c.md) FUN_0048067c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 3件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c670.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f508.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d7e4.md#insn-0045d818) · [`0045d830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d7e4.md#insn-0045d830) · [`0045d840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d7e4.md#insn-0045d840)
- 新版 `004806b0`（命令位置の公開資料なし） · `004806c8`（命令位置の公開資料なし） · `004806d8`（命令位置の公開資料なし）

~~~diff
- 0045d818 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d818 ["INT_ADD", "register:40f0:8", ["const:45d818:8", "const:4:8"]]
- 0045d818 ["CALLIND", null, ["register:0:8"]]
+ 004806b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004806b0 ["INT_ADD", "register:40f0:8", ["const:4806b0:8", "const:4:8"]]
+ 004806b0 ["CALLIND", null, ["register:0:8"]]
- 0045d818 bytes 00013fd6
+ 004806b0 bytes 00013fd6
- 0045d830 ["INT_ADD", "register:40f0:8", ["const:45d830:8", "const:4:8"]]
- 0045d830 ["CALL", null, ["callee:0055f484:8"]]
+ 004806c8 ["INT_ADD", "register:40f0:8", ["const:4806c8:8", "const:4:8"]]
+ 004806c8 ["CALL", null, ["callee:0055f484:8"]]
- 0045d830 bytes 6f7b0394
+ 004806c8 bytes 6f7b0394
- 0045d840 ["INT_ADD", "register:40f0:8", ["const:45d840:8", "const:4:8"]]
- 0045d840 ["CALL", null, ["callee:0055f508:8"]]
+ 004806d8 ["INT_ADD", "register:40f0:8", ["const:4806d8:8", "const:4:8"]]
+ 004806d8 ["CALL", null, ["callee:0055f508:8"]]
- 0045d840 bytes 8c7b0394
+ 004806d8 bytes 8c7b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b05848dd4d8c8079433135e01fb782c9"></a>

### [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md) → [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md) FUN_00480704

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 27件 [`005953e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/005953e0.md) [`0064f874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f874.md) [`006b1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md) [`00704be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704be8.md) [`00708804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708804.md) · 呼出先 3件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c690.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 27件 [`005b9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md) [`00675b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b54.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0072ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) [`00732904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f528.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md#insn-0045d8a0) · [`0045d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md#insn-0045d8b8) · [`0045d8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md#insn-0045d8c8)
- 新版 `00480738`（命令位置の公開資料なし） · `00480750`（命令位置の公開資料なし） · `00480760`（命令位置の公開資料なし）

~~~diff
- 0045d8a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d8a0 ["INT_ADD", "register:40f0:8", ["const:45d8a0:8", "const:4:8"]]
- 0045d8a0 ["CALLIND", null, ["register:0:8"]]
+ 00480738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480738 ["INT_ADD", "register:40f0:8", ["const:480738:8", "const:4:8"]]
+ 00480738 ["CALLIND", null, ["register:0:8"]]
- 0045d8a0 bytes 00013fd6
+ 00480738 bytes 00013fd6
- 0045d8b8 ["INT_ADD", "register:40f0:8", ["const:45d8b8:8", "const:4:8"]]
- 0045d8b8 ["CALL", null, ["callee:0055f484:8"]]
+ 00480750 ["INT_ADD", "register:40f0:8", ["const:480750:8", "const:4:8"]]
+ 00480750 ["CALL", null, ["callee:0055f484:8"]]
- 0045d8b8 bytes 4d7b0394
+ 00480750 bytes 4d7b0394
- 0045d8c8 ["INT_ADD", "register:40f0:8", ["const:45d8c8:8", "const:4:8"]]
- 0045d8c8 ["CALL", null, ["callee:0055f528:8"]]
+ 00480760 ["INT_ADD", "register:40f0:8", ["const:480760:8", "const:4:8"]]
+ 00480760 ["CALL", null, ["callee:0055f528:8"]]
- 0045d8c8 bytes 727b0394
+ 00480760 bytes 727b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a12da35972fa2d9cdb0ba5a81d6bc47"></a>

### [`0045d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d8f4.md) → [`0048078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048078c.md) FUN_0048078c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0070dfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070dfa4.md) [`00775b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775b20.md) [`0094b7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094b/0094b7f8.md) [`009737c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/009737c4.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 5件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c660.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 6件 [`007380a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007380a4.md) [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) [`009812a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md) [`009a92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a92a8.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 5件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045d930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d8f4.md#insn-0045d930) · [`0045d944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d8f4.md#insn-0045d944) · [`0045d954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d8f4.md#insn-0045d954)
- 新版 `004807c8`（命令位置の公開資料なし） · `004807dc`（命令位置の公開資料なし） · `004807ec`（命令位置の公開資料なし）

~~~diff
- 0045d930 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045d930 ["INT_ADD", "register:40f0:8", ["const:45d930:8", "const:4:8"]]
- 0045d930 ["CALLIND", null, ["register:0:8"]]
+ 004807c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004807c8 ["INT_ADD", "register:40f0:8", ["const:4807c8:8", "const:4:8"]]
+ 004807c8 ["CALLIND", null, ["register:0:8"]]
- 0045d930 bytes 20013fd6
+ 004807c8 bytes 20013fd6
- 0045d944 ["INT_ADD", "register:40f0:8", ["const:45d944:8", "const:4:8"]]
- 0045d944 ["CALL", null, ["callee:0055f484:8"]]
+ 004807dc ["INT_ADD", "register:40f0:8", ["const:4807dc:8", "const:4:8"]]
+ 004807dc ["CALL", null, ["callee:0055f484:8"]]
- 0045d944 bytes 2a7b0394
+ 004807dc bytes 2a7b0394
- 0045d954 ["INT_ADD", "register:40f0:8", ["const:45d954:8", "const:4:8"]]
- 0045d954 ["CALL", null, ["callee:0055f4f8:8"]]
+ 004807ec ["INT_ADD", "register:40f0:8", ["const:4807ec:8", "const:4:8"]]
+ 004807ec ["CALL", null, ["callee:0055f4f8:8"]]
- 0045d954 bytes 437b0394
+ 004807ec bytes 437b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97234c437cc1d9edacc94e1168e8b9c2"></a>

### [`0045da24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045da24.md) → [`004808bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004808bc.md) FUN_004808bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00775b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775b20.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 4件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c660.md) [`005748a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748a0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 4件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0045da6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045da24.md#insn-0045da6c) · [`0045da80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045da24.md#insn-0045da80) · [`0045da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045da24.md#insn-0045da90)
- 新版 `00480904`（命令位置の公開資料なし） · `00480918`（命令位置の公開資料なし） · `00480928`（命令位置の公開資料なし）

~~~diff
- 0045da6c ["COPY", "register:0:8", ["register:4048:8"]]
- 0045da6c ["INT_ADD", "register:40f0:8", ["const:45da6c:8", "const:4:8"]]
- 0045da6c ["CALLIND", null, ["register:0:8"]]
+ 00480904 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00480904 ["INT_ADD", "register:40f0:8", ["const:480904:8", "const:4:8"]]
+ 00480904 ["CALLIND", null, ["register:0:8"]]
- 0045da6c bytes 20013fd6
+ 00480904 bytes 20013fd6
- 0045da80 ["INT_ADD", "register:40f0:8", ["const:45da80:8", "const:4:8"]]
- 0045da80 ["CALL", null, ["callee:0055f484:8"]]
+ 00480918 ["INT_ADD", "register:40f0:8", ["const:480918:8", "const:4:8"]]
+ 00480918 ["CALL", null, ["callee:0055f484:8"]]
- 0045da80 bytes db7a0394
+ 00480918 bytes db7a0394
- 0045da90 ["INT_ADD", "register:40f0:8", ["const:45da90:8", "const:4:8"]]
- 0045da90 ["CALL", null, ["callee:0055f4f8:8"]]
+ 00480928 ["INT_ADD", "register:40f0:8", ["const:480928:8", "const:4:8"]]
+ 00480928 ["CALL", null, ["callee:0055f4f8:8"]]
- 0045da90 bytes f47a0394
+ 00480928 bytes f47a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

