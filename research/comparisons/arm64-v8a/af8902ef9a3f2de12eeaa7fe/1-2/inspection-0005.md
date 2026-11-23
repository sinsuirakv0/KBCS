# v15.7.4 → v16.0.0 · 要調査の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-6581cbc3908521936dc7bd7c8967d89f"></a>

### [`004714e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004714e4.md) → [`0049437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md) FUN_0049437c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004703fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004703fc.md) [`004714e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004714e4.md) · 呼出先 4件 [`004714e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004714e4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00493294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493294.md) [`0049437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md) · 呼出先 4件 [`0049437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004714e4.md#insn-00471500) · [`0047150c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004714e4.md#insn-0047150c) · [`00471520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004714e4.md#insn-00471520)
- 新版 [`00494398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md#insn-00494398) · [`004943a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md#insn-004943a4) · [`004943b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md#insn-004943b8)

~~~diff
- 00471500 ["INT_ADD", "register:40f0:8", ["const:471500:8", "const:4:8"]]
- 00471500 ["CALL", null, ["local:b0:8"]]
+ 00494398 ["INT_ADD", "register:40f0:8", ["const:494398:8", "const:4:8"]]
+ 00494398 ["CALL", null, ["local:b0:8"]]
- 00471500 bytes f9ffff97
+ 00494398 bytes f9ffff97
- 0047150c ["INT_ADD", "register:40f0:8", ["const:47150c:8", "const:4:8"]]
- 0047150c ["CALL", null, ["local:b0:8"]]
+ 004943a4 ["INT_ADD", "register:40f0:8", ["const:4943a4:8", "const:4:8"]]
+ 004943a4 ["CALL", null, ["local:b0:8"]]
- 0047150c bytes f6ffff97
+ 004943a4 bytes f6ffff97
- 00471520 ["INT_ADD", "register:40f0:8", ["const:471520:8", "const:4:8"]]
- 00471520 ["CALL", null, ["callee:00c538e0:8"]]
+ 004943b8 ["INT_ADD", "register:40f0:8", ["const:4943b8:8", "const:4:8"]]
+ 004943b8 ["CALL", null, ["callee:00c538e0:8"]]
- 00471520 bytes 5c961d94
+ 004943b8 bytes 4afd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b72f95a0737d5ae1a0d50b936b23264"></a>

### [`0047163c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047163c.md) → [`004944d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md) FUN_004944d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004715b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004715b4.md) [`00471cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471cf4.md) · 呼出先 4件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0049444c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049444c.md) [`00494b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md) · 呼出先 4件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004716ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047163c.md#insn-004716ec) · [`00471700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047163c.md#insn-00471700) · [`00471714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047163c.md#insn-00471714)
- 新版 [`00494584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md#insn-00494584) · [`00494598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md#insn-00494598) · [`004945ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md#insn-004945ac)

~~~diff
- 004716ec ["INT_ADD", "register:40f0:8", ["const:4716ec:8", "const:4:8"]]
- 004716ec ["CALL", null, ["callee:004945d0:8"]]
+ 00494584 ["INT_ADD", "register:40f0:8", ["const:494584:8", "const:4:8"]]
+ 00494584 ["CALL", null, ["callee:004945d0:8"]]
- 004716ec bytes 13000094
+ 00494584 bytes 13000094
- 00471700 ["INT_ADD", "register:40f0:8", ["const:471700:8", "const:4:8"]]
- 00471700 ["CALL", null, ["callee:00c538e0:8"]]
+ 00494598 ["INT_ADD", "register:40f0:8", ["const:494598:8", "const:4:8"]]
+ 00494598 ["CALL", null, ["callee:00c538e0:8"]]
- 00471700 bytes e4951d94
+ 00494598 bytes d2fc1e94
- 00471714 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471714 ["INT_ADD", "register:40f0:8", ["const:471714:8", "const:4:8"]]
- 00471714 ["CALLIND", null, ["register:0:8"]]
+ 004945ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004945ac ["INT_ADD", "register:40f0:8", ["const:4945ac:8", "const:4:8"]]
+ 004945ac ["CALLIND", null, ["register:0:8"]]
- 00471714 bytes 00013fd6
+ 004945ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11797ff30d5b49dbcf9ae749147c3532"></a>

### [`00471ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ca4.md) → [`00494b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b3c.md) FUN_00494b3c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00470404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ca4.md#insn-00471ce0)
- 新版 [`00494b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b3c.md#insn-00494b78)

~~~diff
- 00471ce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471ce0 ["INT_ADD", "register:40f0:8", ["const:471ce0:8", "const:4:8"]]
- 00471ce0 ["CALLIND", null, ["register:0:8"]]
+ 00494b78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494b78 ["INT_ADD", "register:40f0:8", ["const:494b78:8", "const:4:8"]]
+ 00494b78 ["CALLIND", null, ["register:0:8"]]
- 00471ce0 bytes 00013fd6
+ 00494b78 bytes 00013fd6
~~~


<a id="compare-630b99a3da494fc94813ac444509ee84"></a>

### [`00471da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471da4.md) → [`00494c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md) FUN_00494c3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0046b2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b2bc.md) [`004db550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db550.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`0076cab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cab8.md) [`00832958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832958.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 8件 [`0048e154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e154.md) [`004fe3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md) [`00796f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796f8c.md) [`007aa9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md) [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471da4.md#insn-00471dd8) · [`00471df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471da4.md#insn-00471df8) · [`00471e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471da4.md#insn-00471e34)
- 新版 [`00494c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md#insn-00494c70) · [`00494c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md#insn-00494c90) · [`00494ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md#insn-00494ccc)

~~~diff
- 00471dd8 ["INT_ADD", "register:40f0:8", ["const:471dd8:8", "const:4:8"]]
- 00471dd8 ["CALL", null, ["callee:0046d568:8"]]
+ 00494c70 ["INT_ADD", "register:40f0:8", ["const:494c70:8", "const:4:8"]]
+ 00494c70 ["CALL", null, ["callee:0046d568:8"]]
- 00471dd8 bytes 3e62ff97
+ 00494c70 bytes 3e62ff97
- 00471df8 ["INT_ADD", "register:40f0:8", ["const:471df8:8", "const:4:8"]]
- 00471df8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00494c90 ["INT_ADD", "register:40f0:8", ["const:494c90:8", "const:4:8"]]
+ 00494c90 ["CALL", null, ["callee:00c57a90:8"]]
- 00471df8 bytes 92a41d94
+ 00494c90 bytes 800b1f94
- 00471e34 ["INT_ADD", "register:40f0:8", ["const:471e34:8", "const:4:8"]]
- 00471e34 ["CALL", null, ["callee:0043bae0:8"]]
+ 00494ccc ["INT_ADD", "register:40f0:8", ["const:494ccc:8", "const:4:8"]]
+ 00494ccc ["CALL", null, ["callee:0043bae0:8"]]
- 00471e34 bytes 6b9cfe97
+ 00494ccc bytes 859bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4ca585c218e8f301b1054ef3ff167aa"></a>

### [`00471ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ed4.md) → [`00494d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494d6c.md) FUN_00494d6c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ed4.md#insn-00471f00) · [`00471f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ed4.md#insn-00471f10)
- 新版 [`00494d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494d6c.md#insn-00494d98) · [`00494da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494d6c.md#insn-00494da8)

~~~diff
- 00471f00 ["INT_ADD", "register:40f0:8", ["const:471f00:8", "const:4:8"]]
- 00471f00 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00494d98 ["INT_ADD", "register:40f0:8", ["const:494d98:8", "const:4:8"]]
+ 00494d98 ["CALL", null, ["callee:00c57ab0:8"]]
- 00471f00 bytes 58a41d94
+ 00494d98 bytes 460b1f94
- 00471f10 ["INT_ADD", "register:40f0:8", ["const:471f10:8", "const:4:8"]]
- 00471f10 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00494da8 ["INT_ADD", "register:40f0:8", ["const:494da8:8", "const:4:8"]]
+ 00494da8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00471f10 bytes 54a41d94
+ 00494da8 bytes 420b1f94
~~~


<a id="compare-a22b03ed13fa05172b9331ca95369a2a"></a>

### [`00472c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472c8c.md) → [`00495b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b24.md) FUN_00495b24

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472c8c.md#insn-00472ca8) · [`00472cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472c8c.md#insn-00472cc8)
- 新版 [`00495b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b24.md#insn-00495b40) · [`00495b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b24.md#insn-00495b60)

~~~diff
- 00472ca8 ["INT_ADD", "register:40f0:8", ["const:472ca8:8", "const:4:8"]]
- 00472ca8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00495b40 ["INT_ADD", "register:40f0:8", ["const:495b40:8", "const:4:8"]]
+ 00495b40 ["CALL", null, ["callee:00c538e0:8"]]
- 00472ca8 bytes 7a901d94
+ 00495b40 bytes 68f71e94
- 00472cc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472cc8 ["INT_ADD", "register:40f0:8", ["const:472cc8:8", "const:4:8"]]
- 00472cc8 ["CALLIND", null, ["register:0:8"]]
+ 00495b60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495b60 ["INT_ADD", "register:40f0:8", ["const:495b60:8", "const:4:8"]]
+ 00495b60 ["CALLIND", null, ["register:0:8"]]
- 00472cc8 bytes 00013fd6
+ 00495b60 bytes 00013fd6
~~~


<a id="compare-51fca906e5afb7de98c56970e6392083"></a>

### [`00472cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472cdc.md) → [`00495b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md) FUN_00495b74

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004723a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004723a4.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049523c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/0049523c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472cdc.md#insn-00472d58) · [`00472d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472cdc.md#insn-00472d6c) · [`00472d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472cdc.md#insn-00472d74)
- 新版 [`00495bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md#insn-00495bf0) · [`00495c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md#insn-00495c04) · [`00495c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md#insn-00495c0c)

~~~diff
- 00472d58 ["INT_ADD", "register:40f0:8", ["const:472d58:8", "const:4:8"]]
- 00472d58 ["CALL", null, ["callee:00c538e0:8"]]
+ 00495bf0 ["INT_ADD", "register:40f0:8", ["const:495bf0:8", "const:4:8"]]
+ 00495bf0 ["CALL", null, ["callee:00c538e0:8"]]
- 00472d58 bytes 4e901d94
+ 00495bf0 bytes 3cf71e94
- 00472d6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00472d6c ["INT_ADD", "register:40f0:8", ["const:472d6c:8", "const:4:8"]]
- 00472d6c ["CALLIND", null, ["register:0:8"]]
+ 00495c04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495c04 ["INT_ADD", "register:40f0:8", ["const:495c04:8", "const:4:8"]]
+ 00495c04 ["CALLIND", null, ["register:0:8"]]
- 00472d6c bytes 00013fd6
+ 00495c04 bytes 00013fd6
- 00472d74 ["INT_ADD", "register:40f0:8", ["const:472d74:8", "const:4:8"]]
- 00472d74 ["CALL", null, ["callee:00c57a80:8"]]
+ 00495c0c ["INT_ADD", "register:40f0:8", ["const:495c0c:8", "const:4:8"]]
+ 00495c0c ["CALL", null, ["callee:00c57a80:8"]]
- 00472d74 bytes afa01d94
+ 00495c0c bytes 9d071f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d31e2d1d5cc804be535d7f035eb7b10"></a>

### [`00472e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md) → [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) FUN_00495d04

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004724fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0047332c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/0047332c.md) [`004734b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004734b4.md) [`00473640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473640.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00495394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004961c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md) [`0049634c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md) [`004964d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md#insn-00472f04) · [`00472f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md#insn-00472f48) · [`00472f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md#insn-00472f58)
- 新版 [`00495d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md#insn-00495d9c) · [`00495de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md#insn-00495de0) · [`00495df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md#insn-00495df0)

~~~diff
- 00472f04 ["INT_ADD", "register:40f0:8", ["const:472f04:8", "const:4:8"]]
- 00472f04 ["CALL", null, ["callee:00c57b40:8"]]
+ 00495d9c ["INT_ADD", "register:40f0:8", ["const:495d9c:8", "const:4:8"]]
+ 00495d9c ["CALL", null, ["callee:00c57b40:8"]]
- 00472f04 bytes 7ba01d94
+ 00495d9c bytes 69071f94
- 00472f48 ["INT_ADD", "register:40f0:8", ["const:472f48:8", "const:4:8"]]
- 00472f48 ["CALL", null, ["callee:00c57a90:8"]]
+ 00495de0 ["INT_ADD", "register:40f0:8", ["const:495de0:8", "const:4:8"]]
+ 00495de0 ["CALL", null, ["callee:00c57a90:8"]]
- 00472f48 bytes 3ea01d94
+ 00495de0 bytes 2c071f94
- 00472f58 ["INT_ADD", "register:40f0:8", ["const:472f58:8", "const:4:8"]]
- 00472f58 ["CALL", null, ["callee:004961c4:8"]]
+ 00495df0 ["INT_ADD", "register:40f0:8", ["const:495df0:8", "const:4:8"]]
+ 00495df0 ["CALL", null, ["callee:004961c4:8"]]
- 00472f58 bytes f5000094
+ 00495df0 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5f361d89e1174489f5511cd7c32b5f3"></a>

### [`0047332c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/0047332c.md) → [`004961c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md) FUN_004961c4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00472e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/0047332c.md#insn-00473394) · [`004733cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/0047332c.md#insn-004733cc) · [`0047347c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/0047332c.md#insn-0047347c)
- 新版 [`0049622c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md#insn-0049622c) · [`00496264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md#insn-00496264) · [`00496314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md#insn-00496314)

~~~diff
- 00473394 ["INT_ADD", "register:40f0:8", ["const:473394:8", "const:4:8"]]
- 00473394 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049622c ["INT_ADD", "register:40f0:8", ["const:49622c:8", "const:4:8"]]
+ 0049622c ["CALL", null, ["callee:00c57b40:8"]]
- 00473394 bytes 579f1d94
+ 0049622c bytes 45061f94
- 004733cc ["INT_ADD", "register:40f0:8", ["const:4733cc:8", "const:4:8"]]
- 004733cc ["CALL", null, ["callee:00c57a90:8"]]
+ 00496264 ["INT_ADD", "register:40f0:8", ["const:496264:8", "const:4:8"]]
+ 00496264 ["CALL", null, ["callee:00c57a90:8"]]
- 004733cc bytes 1d9f1d94
+ 00496264 bytes 0b061f94
- 0047347c ["INT_ADD", "register:40f0:8", ["const:47347c:8", "const:4:8"]]
- 0047347c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00496314 ["INT_ADD", "register:40f0:8", ["const:496314:8", "const:4:8"]]
+ 00496314 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047347c bytes f99e1d94
+ 00496314 bytes e7051f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a21a6432fc67f671faa872c0c289f18"></a>

### [`004734b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004734b4.md) → [`0049634c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md) FUN_0049634c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00472e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md) [`009b7d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009b7/009b7d00.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004734b4.md#insn-00473524) · [`0047355c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004734b4.md#insn-0047355c) · [`0047360c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004734b4.md#insn-0047360c)
- 新版 [`004963bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md#insn-004963bc) · [`004963f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md#insn-004963f4) · [`004964a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md#insn-004964a4)

~~~diff
- 00473524 ["INT_ADD", "register:40f0:8", ["const:473524:8", "const:4:8"]]
- 00473524 ["CALL", null, ["callee:00c57b40:8"]]
+ 004963bc ["INT_ADD", "register:40f0:8", ["const:4963bc:8", "const:4:8"]]
+ 004963bc ["CALL", null, ["callee:00c57b40:8"]]
- 00473524 bytes f39e1d94
+ 004963bc bytes e1051f94
- 0047355c ["INT_ADD", "register:40f0:8", ["const:47355c:8", "const:4:8"]]
- 0047355c ["CALL", null, ["callee:00c57a90:8"]]
+ 004963f4 ["INT_ADD", "register:40f0:8", ["const:4963f4:8", "const:4:8"]]
+ 004963f4 ["CALL", null, ["callee:00c57a90:8"]]
- 0047355c bytes b99e1d94
+ 004963f4 bytes a7051f94
- 0047360c ["INT_ADD", "register:40f0:8", ["const:47360c:8", "const:4:8"]]
- 0047360c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004964a4 ["INT_ADD", "register:40f0:8", ["const:4964a4:8", "const:4:8"]]
+ 004964a4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047360c bytes 959e1d94
+ 004964a4 bytes 83051f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b868bcfcbb6011fb2a4e88b28ce8821c"></a>

### [`00473640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473640.md) → [`004964d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md) FUN_004964d8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00472e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004736b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473640.md#insn-004736b0) · [`004736e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473640.md#insn-004736e8) · [`00473798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473640.md#insn-00473798)
- 新版 [`00496548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md#insn-00496548) · [`00496580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md#insn-00496580) · [`00496630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md#insn-00496630)

~~~diff
- 004736b0 ["INT_ADD", "register:40f0:8", ["const:4736b0:8", "const:4:8"]]
- 004736b0 ["CALL", null, ["callee:00c57b40:8"]]
+ 00496548 ["INT_ADD", "register:40f0:8", ["const:496548:8", "const:4:8"]]
+ 00496548 ["CALL", null, ["callee:00c57b40:8"]]
- 004736b0 bytes 909e1d94
+ 00496548 bytes 7e051f94
- 004736e8 ["INT_ADD", "register:40f0:8", ["const:4736e8:8", "const:4:8"]]
- 004736e8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00496580 ["INT_ADD", "register:40f0:8", ["const:496580:8", "const:4:8"]]
+ 00496580 ["CALL", null, ["callee:00c57a90:8"]]
- 004736e8 bytes 569e1d94
+ 00496580 bytes 44051f94
- 00473798 ["INT_ADD", "register:40f0:8", ["const:473798:8", "const:4:8"]]
- 00473798 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00496630 ["INT_ADD", "register:40f0:8", ["const:496630:8", "const:4:8"]]
+ 00496630 ["CALL", null, ["callee:00c57ab0:8"]]
- 00473798 bytes 329e1d94
+ 00496630 bytes 20051f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a087197a39e906befbd4f57f5af887"></a>

### [`00473f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f9c.md) → [`00496e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md) FUN_00496e34

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474620.md) [`00474724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474724.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004974b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md) [`004975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f9c.md#insn-00473fb0)
- 新版 [`00496e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md#insn-00496e48)

~~~diff
- 00473fb0 ["INT_ADD", "register:40f0:8", ["const:473fb0:8", "const:4:8"]]
- 00473fb0 ["CALL", null, ["callee:004974b8:8"]]
+ 00496e48 ["INT_ADD", "register:40f0:8", ["const:496e48:8", "const:4:8"]]
+ 00496e48 ["CALL", null, ["callee:004974b8:8"]]
- 00473fb0 bytes 9c010094
+ 00496e48 bytes 9c010094
~~~


<a id="compare-6863918ff6b7635f4180a8b77800c043"></a>

### [`00473fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473fe0.md) → [`00496e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e78.md) FUN_00496e78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473fe0.md#insn-00473ff4)
- 新版 [`00496e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e78.md#insn-00496e8c)

~~~diff
- 00473ff4 ["INT_ADD", "register:40f0:8", ["const:473ff4:8", "const:4:8"]]
- 00473ff4 ["CALL", null, ["callee:0044104c:8"]]
+ 00496e8c ["INT_ADD", "register:40f0:8", ["const:496e8c:8", "const:4:8"]]
+ 00496e8c ["CALL", null, ["callee:0044104c:8"]]
- 00473ff4 bytes 56a9fe97
+ 00496e8c bytes 70a8fe97
~~~


<a id="compare-44f6e69f1fa9d747cb77a3cfad801186"></a>

### [`0047402c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047402c.md) → [`00496ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ec4.md) FUN_00496ec4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047402c.md#insn-00474040)
- 新版 [`00496ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ec4.md#insn-00496ed8)

~~~diff
- 00474040 ["INT_ADD", "register:40f0:8", ["const:474040:8", "const:4:8"]]
- 00474040 ["CALL", null, ["callee:0044104c:8"]]
+ 00496ed8 ["INT_ADD", "register:40f0:8", ["const:496ed8:8", "const:4:8"]]
+ 00496ed8 ["CALL", null, ["callee:0044104c:8"]]
- 00474040 bytes 43a9fe97
+ 00496ed8 bytes 5da8fe97
~~~


<a id="compare-b7490a020d1ebddb0dc88f0368a31463"></a>

### [`00474078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474078.md) → [`00496f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f10.md) FUN_00496f10

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047408c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474078.md#insn-0047408c)
- 新版 [`00496f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f10.md#insn-00496f24)

~~~diff
- 0047408c ["INT_ADD", "register:40f0:8", ["const:47408c:8", "const:4:8"]]
- 0047408c ["CALL", null, ["callee:0044104c:8"]]
+ 00496f24 ["INT_ADD", "register:40f0:8", ["const:496f24:8", "const:4:8"]]
+ 00496f24 ["CALL", null, ["callee:0044104c:8"]]
- 0047408c bytes 30a9fe97
+ 00496f24 bytes 4aa8fe97
~~~


<a id="compare-d95c1a9c1093abfb0677c0a2b3caba55"></a>

### [`004740c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004740c4.md) → [`00496f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f5c.md) FUN_00496f5c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004740d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004740c4.md#insn-004740d8) · [`004740f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004740c4.md#insn-004740f4)
- 新版 [`00496f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f5c.md#insn-00496f70) · [`00496f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f5c.md#insn-00496f8c)

~~~diff
- 004740d8 ["INT_ADD", "register:40f0:8", ["const:4740d8:8", "const:4:8"]]
- 004740d8 ["CALL", null, ["callee:0044104c:8"]]
+ 00496f70 ["INT_ADD", "register:40f0:8", ["const:496f70:8", "const:4:8"]]
+ 00496f70 ["CALL", null, ["callee:0044104c:8"]]
- 004740d8 bytes 1da9fe97
+ 00496f70 bytes 37a8fe97
- 004740f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004740f4 ["INT_ADD", "register:40f0:8", ["const:4740f4:8", "const:4:8"]]
- 004740f4 ["CALLIND", null, ["register:0:8"]]
+ 00496f8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00496f8c ["INT_ADD", "register:40f0:8", ["const:496f8c:8", "const:4:8"]]
+ 00496f8c ["CALLIND", null, ["register:0:8"]]
- 004740f4 bytes 00013fd6
+ 00496f8c bytes 00013fd6
~~~


<a id="compare-88049bc343621728d0e59840a66dbfe1"></a>

### [`0047410c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047410c.md) → [`00496fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496fa4.md) FUN_00496fa4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047410c.md#insn-00474124)
- 新版 [`00496fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496fa4.md#insn-00496fbc)

~~~diff
- 00474124 ["INT_ADD", "register:40f0:8", ["const:474124:8", "const:4:8"]]
- 00474124 ["CALL", null, ["callee:0044104c:8"]]
+ 00496fbc ["INT_ADD", "register:40f0:8", ["const:496fbc:8", "const:4:8"]]
+ 00496fbc ["CALL", null, ["callee:0044104c:8"]]
- 00474124 bytes 0aa9fe97
+ 00496fbc bytes 24a8fe97
~~~


<a id="compare-f70137900c40b7bc0c3514c1323a7b0f"></a>

### [`00474620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474620.md) → [`004974b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md) FUN_004974b8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00473f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f9c.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00496e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047468c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474620.md#insn-0047468c) · [`004746e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474620.md#insn-004746e8)
- 新版 [`00497524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md#insn-00497524) · [`00497580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md#insn-00497580)

~~~diff
- 0047468c ["INT_ADD", "register:40f0:8", ["const:47468c:8", "const:4:8"]]
- 0047468c ["CALL", null, ["callee:00c57c50:8"]]
+ 00497524 ["INT_ADD", "register:40f0:8", ["const:497524:8", "const:4:8"]]
+ 00497524 ["CALL", null, ["callee:00c57c50:8"]]
- 0047468c bytes dd9a1d94
+ 00497524 bytes cb011f94
- 004746e8 ["INT_ADD", "register:40f0:8", ["const:4746e8:8", "const:4:8"]]
- 004746e8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00497580 ["INT_ADD", "register:40f0:8", ["const:497580:8", "const:4:8"]]
+ 00497580 ["CALL", null, ["callee:00c57c50:8"]]
- 004746e8 bytes c69a1d94
+ 00497580 bytes b4011f94
~~~


<a id="compare-0683c604367f6939c79c3b92952c0733"></a>

### [`00474724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474724.md) → [`004975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md) FUN_004975bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00473f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f9c.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00496e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474724.md#insn-00474788) · [`004747a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474724.md#insn-004747a0) · [`004747b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474724.md#insn-004747b0)
- 新版 [`00497620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md#insn-00497620) · [`00497638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md#insn-00497638) · [`00497648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md#insn-00497648)

~~~diff
- 00474788 ["INT_ADD", "register:40f0:8", ["const:474788:8", "const:4:8"]]
- 00474788 ["CALL", null, ["callee:004945d0:8"]]
+ 00497620 ["INT_ADD", "register:40f0:8", ["const:497620:8", "const:4:8"]]
+ 00497620 ["CALL", null, ["callee:004945d0:8"]]
- 00474788 bytes ecf3ff97
+ 00497620 bytes ecf3ff97
- 004747a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004747a0 ["INT_ADD", "register:40f0:8", ["const:4747a0:8", "const:4:8"]]
- 004747a0 ["CALLIND", null, ["register:0:8"]]
+ 00497638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497638 ["INT_ADD", "register:40f0:8", ["const:497638:8", "const:4:8"]]
+ 00497638 ["CALLIND", null, ["register:0:8"]]
- 004747a0 bytes 00013fd6
+ 00497638 bytes 00013fd6
- 004747b0 ["INT_ADD", "register:40f0:8", ["const:4747b0:8", "const:4:8"]]
- 004747b0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00497648 ["INT_ADD", "register:40f0:8", ["const:497648:8", "const:4:8"]]
+ 00497648 ["CALL", null, ["callee:00c57ab0:8"]]
- 004747b0 bytes 2c9a1d94
+ 00497648 bytes 1a011f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-485bf574bee8d2becb958f9a4c642cbd"></a>

### [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) → [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) FUN_004977f4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 132件 [`004747cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md) [`00555a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555a38.md) [`0055b604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md) [`0055b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md) [`0055c754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 135件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`005788d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md) [`0057e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md) [`0057e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md) [`0057f5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f5ec.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004749d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md#insn-004749d0) · [`004749f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md#insn-004749f4)
- 新版 [`00497868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md#insn-00497868) · [`0049788c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md#insn-0049788c)

~~~diff
- 004749d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004749d0 ["INT_ADD", "register:40f0:8", ["const:4749d0:8", "const:4:8"]]
- 004749d0 ["CALLIND", null, ["register:0:8"]]
+ 00497868 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497868 ["INT_ADD", "register:40f0:8", ["const:497868:8", "const:4:8"]]
+ 00497868 ["CALLIND", null, ["register:0:8"]]
- 004749d0 bytes 00013fd6
+ 00497868 bytes 00013fd6
- 004749f4 ["INT_ADD", "register:40f0:8", ["const:4749f4:8", "const:4:8"]]
- 004749f4 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0049788c ["INT_ADD", "register:40f0:8", ["const:49788c:8", "const:4:8"]]
+ 0049788c ["CALL", null, ["callee:00c57ae0:8"]]
- 004749f4 bytes a7991d94
+ 0049788c bytes 95001f94
~~~


<a id="compare-e65f5f51a60e6c25bc2a5b9be792f413"></a>

### [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) → [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) FUN_00497a08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 45件 [`004749f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ea94.md) [`0054fb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fb0c.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 46件 [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) [`005729a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005729a4.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md#insn-00474be4) · [`00474c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md#insn-00474c08)
- 新版 [`00497a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md#insn-00497a7c) · [`00497aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md#insn-00497aa0)

~~~diff
- 00474be4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00474be4 ["INT_ADD", "register:40f0:8", ["const:474be4:8", "const:4:8"]]
- 00474be4 ["CALLIND", null, ["register:0:8"]]
+ 00497a7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497a7c ["INT_ADD", "register:40f0:8", ["const:497a7c:8", "const:4:8"]]
+ 00497a7c ["CALLIND", null, ["register:0:8"]]
- 00474be4 bytes 00013fd6
+ 00497a7c bytes 00013fd6
- 00474c08 ["INT_ADD", "register:40f0:8", ["const:474c08:8", "const:4:8"]]
- 00474c08 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00497aa0 ["INT_ADD", "register:40f0:8", ["const:497aa0:8", "const:4:8"]]
+ 00497aa0 ["CALL", null, ["callee:00c57ae0:8"]]
- 00474c08 bytes 22991d94
+ 00497aa0 bytes 10001f94
~~~


<a id="compare-d1a672a7e3347665f59b8332f3e8a463"></a>

### [`00474d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474d04.md) → [`00497b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497b9c.md) FUN_00497b9c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474d04.md#insn-00474d20) · [`00474d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474d04.md#insn-00474d40)
- 新版 [`00497bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497b9c.md#insn-00497bb8) · [`00497bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497b9c.md#insn-00497bd8)

~~~diff
- 00474d20 ["INT_ADD", "register:40f0:8", ["const:474d20:8", "const:4:8"]]
- 00474d20 ["CALL", null, ["callee:00c538e0:8"]]
+ 00497bb8 ["INT_ADD", "register:40f0:8", ["const:497bb8:8", "const:4:8"]]
+ 00497bb8 ["CALL", null, ["callee:00c538e0:8"]]
- 00474d20 bytes 5c881d94
+ 00497bb8 bytes 4aef1e94
- 00474d40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00474d40 ["INT_ADD", "register:40f0:8", ["const:474d40:8", "const:4:8"]]
- 00474d40 ["CALLIND", null, ["register:0:8"]]
+ 00497bd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497bd8 ["INT_ADD", "register:40f0:8", ["const:497bd8:8", "const:4:8"]]
+ 00497bd8 ["CALLIND", null, ["register:0:8"]]
- 00474d40 bytes 00013fd6
+ 00497bd8 bytes 00013fd6
~~~


<a id="compare-29f14f38373afb9fe74a0c1c7b663cdf"></a>

### [`00474d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474d54.md) → [`00497bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497bec.md) FUN_00497bec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474d54.md#insn-00474d70) · [`00474d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474d54.md#insn-00474d90)
- 新版 [`00497c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497bec.md#insn-00497c08) · [`00497c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497bec.md#insn-00497c28)

~~~diff
- 00474d70 ["INT_ADD", "register:40f0:8", ["const:474d70:8", "const:4:8"]]
- 00474d70 ["CALL", null, ["callee:00c538e0:8"]]
+ 00497c08 ["INT_ADD", "register:40f0:8", ["const:497c08:8", "const:4:8"]]
+ 00497c08 ["CALL", null, ["callee:00c538e0:8"]]
- 00474d70 bytes 48881d94
+ 00497c08 bytes 36ef1e94
- 00474d90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00474d90 ["INT_ADD", "register:40f0:8", ["const:474d90:8", "const:4:8"]]
- 00474d90 ["CALLIND", null, ["register:0:8"]]
+ 00497c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497c28 ["INT_ADD", "register:40f0:8", ["const:497c28:8", "const:4:8"]]
+ 00497c28 ["CALLIND", null, ["register:0:8"]]
- 00474d90 bytes 00013fd6
+ 00497c28 bytes 00013fd6
~~~


<a id="compare-95085f713930bfb21ac9187b1dbe303c"></a>

### [`004751fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md) → [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) FUN_00498094

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00474da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md) [`00474f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474f1c.md) [`00475470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md) · 呼出先 4件 [`004768c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)
- 新版 呼出元 3件 [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) [`00497db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md) [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) · 呼出先 4件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md#insn-00475218) · [`00475250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md#insn-00475250) · [`0047529c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md#insn-0047529c)
- 新版 [`004980b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md#insn-004980b0) · [`004980e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md#insn-004980e8) · [`00498134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md#insn-00498134)

~~~diff
- 00475218 ["INT_ADD", "register:40f0:8", ["const:475218:8", "const:4:8"]]
- 00475218 ["CALL", null, ["callee:00c57ce0:8"]]
+ 004980b0 ["INT_ADD", "register:40f0:8", ["const:4980b0:8", "const:4:8"]]
+ 004980b0 ["CALL", null, ["callee:00c57ce0:8"]]
- 00475218 bytes 1e981d94
+ 004980b0 bytes 0cff1e94
- 00475250 ["INT_ADD", "register:40f0:8", ["const:475250:8", "const:4:8"]]
- 00475250 ["CALL", null, ["callee:0049975c:8"]]
+ 004980e8 ["INT_ADD", "register:40f0:8", ["const:4980e8:8", "const:4:8"]]
+ 004980e8 ["CALL", null, ["callee:0049975c:8"]]
- 00475250 bytes 9d050094
+ 004980e8 bytes 9d050094
- 0047529c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047529c ["INT_ADD", "register:40f0:8", ["const:47529c:8", "const:4:8"]]
- 0047529c ["CALLIND", null, ["register:0:8"]]
+ 00498134 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498134 ["INT_ADD", "register:40f0:8", ["const:498134:8", "const:4:8"]]
+ 00498134 ["CALLIND", null, ["register:0:8"]]
- 0047529c bytes 00013fd6
+ 00498134 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84b85aa76c60285899e6eb57f8bbb3c"></a>

### [`00475708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475708.md) → [`004985a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md) FUN_004985a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00475470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md) · 呼出先 4件 [`004773cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) · 呼出先 4件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475708.md#insn-00475724) · [`0047575c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475708.md#insn-0047575c) · [`004757ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475708.md#insn-004757ac)
- 新版 [`004985bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md#insn-004985bc) · [`004985f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md#insn-004985f4) · [`00498644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md#insn-00498644)

~~~diff
- 00475724 ["INT_ADD", "register:40f0:8", ["const:475724:8", "const:4:8"]]
- 00475724 ["CALL", null, ["callee:00c57ce0:8"]]
+ 004985bc ["INT_ADD", "register:40f0:8", ["const:4985bc:8", "const:4:8"]]
+ 004985bc ["CALL", null, ["callee:00c57ce0:8"]]
- 00475724 bytes db961d94
+ 004985bc bytes c9fd1e94
- 0047575c ["INT_ADD", "register:40f0:8", ["const:47575c:8", "const:4:8"]]
- 0047575c ["CALL", null, ["callee:0049a264:8"]]
+ 004985f4 ["INT_ADD", "register:40f0:8", ["const:4985f4:8", "const:4:8"]]
+ 004985f4 ["CALL", null, ["callee:0049a264:8"]]
- 0047575c bytes 1c070094
+ 004985f4 bytes 1c070094
- 004757ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004757ac ["INT_ADD", "register:40f0:8", ["const:4757ac:8", "const:4:8"]]
- 004757ac ["CALLIND", null, ["register:0:8"]]
+ 00498644 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498644 ["INT_ADD", "register:40f0:8", ["const:498644:8", "const:4:8"]]
+ 00498644 ["CALLIND", null, ["register:0:8"]]
- 004757ac bytes 00013fd6
+ 00498644 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3571c153d20bc9b43b1d7c45158df1b7"></a>

### [`0047592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047592c.md) → [`004987c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md) FUN_004987c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 22件 [`00659a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md) [`0065aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md) [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) [`0068f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068f070.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 22件 [`0067fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md) [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`006b53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b5/006b53c4.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047592c.md#insn-00475958) · [`00475964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047592c.md#insn-00475964) · [`0047597c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047592c.md#insn-0047597c)
- 新版 [`004987f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md#insn-004987f0) · [`004987fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md#insn-004987fc) · [`00498814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md#insn-00498814)

~~~diff
- 00475958 ["INT_ADD", "register:40f0:8", ["const:475958:8", "const:4:8"]]
- 00475958 ["CALL", null, ["callee:00c57ce0:8"]]
+ 004987f0 ["INT_ADD", "register:40f0:8", ["const:4987f0:8", "const:4:8"]]
+ 004987f0 ["CALL", null, ["callee:00c57ce0:8"]]
- 00475958 bytes 4e961d94
+ 004987f0 bytes 3cfd1e94
- 00475964 ["INT_ADD", "register:40f0:8", ["const:475964:8", "const:4:8"]]
- 00475964 ["CALL", null, ["callee:00c57cf0:8"]]
+ 004987fc ["INT_ADD", "register:40f0:8", ["const:4987fc:8", "const:4:8"]]
+ 004987fc ["CALL", null, ["callee:00c57cf0:8"]]
- 00475964 bytes 4f961d94
+ 004987fc bytes 3dfd1e94
- 0047597c ["INT_ADD", "register:40f0:8", ["const:47597c:8", "const:4:8"]]
- 0047597c ["CALL", null, ["callee:00c57ce0:8"]]
+ 00498814 ["INT_ADD", "register:40f0:8", ["const:498814:8", "const:4:8"]]
+ 00498814 ["CALL", null, ["callee:00c57ce0:8"]]
- 0047597c bytes 45961d94
+ 00498814 bytes 33fd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9bbae80c79f1d3225733f53ece7c765"></a>

### [`004759a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004759a4.md) → [`0049883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md) FUN_0049883c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00839074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839074.md) [`0083928c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/0083928c.md) · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 2件 [`0086b314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b314.md) [`0086b52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b52c.md) · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004759c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004759a4.md#insn-004759c4) · [`004759d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004759a4.md#insn-004759d0) · [`004759e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004759a4.md#insn-004759e0)
- 新版 [`0049885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md#insn-0049885c) · [`00498868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md#insn-00498868) · [`00498878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md#insn-00498878)

~~~diff
- 004759c4 ["INT_ADD", "register:40f0:8", ["const:4759c4:8", "const:4:8"]]
- 004759c4 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0049885c ["INT_ADD", "register:40f0:8", ["const:49885c:8", "const:4:8"]]
+ 0049885c ["CALL", null, ["callee:00c57ce0:8"]]
- 004759c4 bytes 33961d94
+ 0049885c bytes 21fd1e94
- 004759d0 ["INT_ADD", "register:40f0:8", ["const:4759d0:8", "const:4:8"]]
- 004759d0 ["CALL", null, ["callee:00c57cf0:8"]]
+ 00498868 ["INT_ADD", "register:40f0:8", ["const:498868:8", "const:4:8"]]
+ 00498868 ["CALL", null, ["callee:00c57cf0:8"]]
- 004759d0 bytes 34961d94
+ 00498868 bytes 22fd1e94
- 004759e0 ["INT_ADD", "register:40f0:8", ["const:4759e0:8", "const:4:8"]]
- 004759e0 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00498878 ["INT_ADD", "register:40f0:8", ["const:498878:8", "const:4:8"]]
+ 00498878 ["CALL", null, ["callee:00c57ce0:8"]]
- 004759e0 bytes 2c961d94
+ 00498878 bytes 1afd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1054017bd83deb5a76dbd00ad3a0500"></a>

### [`00475a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475a78.md) → [`00498910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md) FUN_00498910

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00475a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475a44.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004988dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988dc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475a78.md#insn-00475b18) · [`00475b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475a78.md#insn-00475b64) · [`00475bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475a78.md#insn-00475bb0)
- 新版 [`004989b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md#insn-004989b0) · [`004989fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md#insn-004989fc) · [`00498a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md#insn-00498a48)

~~~diff
- 00475b18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00475b18 ["INT_ADD", "register:40f0:8", ["const:475b18:8", "const:4:8"]]
- 00475b18 ["CALLIND", null, ["register:0:8"]]
+ 004989b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004989b0 ["INT_ADD", "register:40f0:8", ["const:4989b0:8", "const:4:8"]]
+ 004989b0 ["CALLIND", null, ["register:0:8"]]
- 00475b18 bytes 00013fd6
+ 004989b0 bytes 00013fd6
- 00475b64 ["INT_ADD", "register:40f0:8", ["const:475b64:8", "const:4:8"]]
- 00475b64 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004989fc ["INT_ADD", "register:40f0:8", ["const:4989fc:8", "const:4:8"]]
+ 004989fc ["CALL", null, ["callee:00c57ab0:8"]]
- 00475b64 bytes 3f951d94
+ 004989fc bytes 2dfc1e94
- 00475bb0 ["INT_ADD", "register:40f0:8", ["const:475bb0:8", "const:4:8"]]
- 00475bb0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00498a48 ["INT_ADD", "register:40f0:8", ["const:498a48:8", "const:4:8"]]
+ 00498a48 ["CALL", null, ["callee:00c57ab0:8"]]
- 00475bb0 bytes 2c951d94
+ 00498a48 bytes 1afc1e94
~~~


<a id="compare-f1b098db4c93747fd2a1cef26cb926e0"></a>

### [`00475c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475c88.md) → [`00498b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md) FUN_00498b20

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00475c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475c54.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00498aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498aec.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475c88.md#insn-00475d28) · [`00475d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475c88.md#insn-00475d74) · [`00475dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475c88.md#insn-00475dc0)
- 新版 [`00498bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md#insn-00498bc0) · [`00498c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md#insn-00498c0c) · [`00498c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md#insn-00498c58)

~~~diff
- 00475d28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00475d28 ["INT_ADD", "register:40f0:8", ["const:475d28:8", "const:4:8"]]
- 00475d28 ["CALLIND", null, ["register:0:8"]]
+ 00498bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498bc0 ["INT_ADD", "register:40f0:8", ["const:498bc0:8", "const:4:8"]]
+ 00498bc0 ["CALLIND", null, ["register:0:8"]]
- 00475d28 bytes 00013fd6
+ 00498bc0 bytes 00013fd6
- 00475d74 ["INT_ADD", "register:40f0:8", ["const:475d74:8", "const:4:8"]]
- 00475d74 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00498c0c ["INT_ADD", "register:40f0:8", ["const:498c0c:8", "const:4:8"]]
+ 00498c0c ["CALL", null, ["callee:00c57ab0:8"]]
- 00475d74 bytes bb941d94
+ 00498c0c bytes a9fb1e94
- 00475dc0 ["INT_ADD", "register:40f0:8", ["const:475dc0:8", "const:4:8"]]
- 00475dc0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00498c58 ["INT_ADD", "register:40f0:8", ["const:498c58:8", "const:4:8"]]
+ 00498c58 ["CALL", null, ["callee:00c57ab0:8"]]
- 00475dc0 bytes a8941d94
+ 00498c58 bytes 96fb1e94
~~~


<a id="compare-42b4b6c7748725df444e466e8987165f"></a>

### [`004763f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004763f8.md) → [`00499290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md) FUN_00499290

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00475e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475e24.md) · 呼出先 4件 [`00476598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476598.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) · 呼出先 4件 [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047646c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004763f8.md#insn-0047646c) · [`00476494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004763f8.md#insn-00476494) · [`004764a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004763f8.md#insn-004764a4)
- 新版 [`00499304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md#insn-00499304) · [`0049932c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md#insn-0049932c) · [`0049933c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md#insn-0049933c)

~~~diff
- 0047646c ["COPY", "register:0:8", ["register:4048:8"]]
- 0047646c ["INT_ADD", "register:40f0:8", ["const:47646c:8", "const:4:8"]]
- 0047646c ["CALLIND", null, ["register:0:8"]]
+ 00499304 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00499304 ["INT_ADD", "register:40f0:8", ["const:499304:8", "const:4:8"]]
+ 00499304 ["CALLIND", null, ["register:0:8"]]
- 0047646c bytes 20013fd6
+ 00499304 bytes 20013fd6
- 00476494 ["COPY", "register:0:8", ["register:4040:8"]]
- 00476494 ["INT_ADD", "register:40f0:8", ["const:476494:8", "const:4:8"]]
- 00476494 ["CALLIND", null, ["register:0:8"]]
+ 0049932c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049932c ["INT_ADD", "register:40f0:8", ["const:49932c:8", "const:4:8"]]
+ 0049932c ["CALLIND", null, ["register:0:8"]]
- 00476494 bytes 00013fd6
+ 0049932c bytes 00013fd6
- 004764a4 ["INT_ADD", "register:40f0:8", ["const:4764a4:8", "const:4:8"]]
- 004764a4 ["CALL", null, ["callee:00499430:8"]]
+ 0049933c ["INT_ADD", "register:40f0:8", ["const:49933c:8", "const:4:8"]]
+ 0049933c ["CALL", null, ["callee:00499430:8"]]
- 004764a4 bytes 3d000094
+ 0049933c bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b269a9142f12e67827e77fa3b8da83e3"></a>

### [`00476598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476598.md) → [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) FUN_00499430

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00475e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475e24.md) [`004763f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004763f8.md) [`00477224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477224.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) [`00499290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md) [`0049a0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00476604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476598.md#insn-00476604) · [`00476614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476598.md#insn-00476614) · [`00476634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476598.md#insn-00476634)
- 新版 [`0049949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md#insn-0049949c) · [`004994ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md#insn-004994ac) · [`004994cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md#insn-004994cc)

~~~diff
- 00476604 ["COPY", "register:0:8", ["register:4040:8"]]
- 00476604 ["INT_ADD", "register:40f0:8", ["const:476604:8", "const:4:8"]]
- 00476604 ["CALLIND", null, ["register:0:8"]]
+ 0049949c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049949c ["INT_ADD", "register:40f0:8", ["const:49949c:8", "const:4:8"]]
+ 0049949c ["CALLIND", null, ["register:0:8"]]
- 00476604 bytes 00013fd6
+ 0049949c bytes 00013fd6
- 00476614 ["COPY", "register:0:8", ["register:4040:8"]]
- 00476614 ["INT_ADD", "register:40f0:8", ["const:476614:8", "const:4:8"]]
- 00476614 ["CALLIND", null, ["register:0:8"]]
+ 004994ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004994ac ["INT_ADD", "register:40f0:8", ["const:4994ac:8", "const:4:8"]]
+ 004994ac ["CALLIND", null, ["register:0:8"]]
- 00476614 bytes 00013fd6
+ 004994ac bytes 00013fd6
- 00476634 ["COPY", "register:0:8", ["register:4040:8"]]
- 00476634 ["INT_ADD", "register:40f0:8", ["const:476634:8", "const:4:8"]]
- 00476634 ["CALLIND", null, ["register:0:8"]]
+ 004994cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004994cc ["INT_ADD", "register:40f0:8", ["const:4994cc:8", "const:4:8"]]
+ 004994cc ["CALLIND", null, ["register:0:8"]]
- 00476634 bytes 00013fd6
+ 004994cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fbdc1a494e832b925fb337277b1ba74"></a>

### [`0047676c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/0047676c.md) → [`00499604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md) FUN_00499604

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004767b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/0047676c.md#insn-004767b0) · [`004767e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/0047676c.md#insn-004767e4) · [`004767e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/0047676c.md#insn-004767e8)
- 新版 [`00499648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md#insn-00499648) · [`0049967c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md#insn-0049967c) · [`00499680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md#insn-00499680)

~~~diff
- 004767b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004767b0 ["INT_ADD", "register:40f0:8", ["const:4767b0:8", "const:4:8"]]
- 004767b0 ["CALLIND", null, ["register:0:8"]]
+ 00499648 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00499648 ["INT_ADD", "register:40f0:8", ["const:499648:8", "const:4:8"]]
+ 00499648 ["CALLIND", null, ["register:0:8"]]
- 004767b0 bytes 00013fd6
+ 00499648 bytes 00013fd6
- 004767e4 ["INT_ADD", "register:40f0:8", ["const:4767e4:8", "const:4:8"]]
- 004767e4 ["CALL", null, ["callee:00459d34:8"]]
+ 0049967c ["INT_ADD", "register:40f0:8", ["const:49967c:8", "const:4:8"]]
+ 0049967c ["CALL", null, ["callee:00459d34:8"]]
- 004767e4 bytes ae01ff97
+ 0049967c bytes ae01ff97
- 004767e8 ["INT_ADD", "register:40f0:8", ["const:4767e8:8", "const:4:8"]]
- 004767e8 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00499680 ["INT_ADD", "register:40f0:8", ["const:499680:8", "const:4:8"]]
+ 00499680 ["CALL", null, ["callee:00c57ae0:8"]]
- 004767e8 bytes 2a921d94
+ 00499680 bytes 18f91e94
~~~


<a id="compare-ad7160eea90e443d8fdc2633290ea2c2"></a>

### [`00476870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476870.md) → [`00499708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499708.md) FUN_00499708

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00476898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476870.md#insn-00476898)
- 新版 [`00499730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499708.md#insn-00499730)

~~~diff
- 00476898 ["INT_ADD", "register:40f0:8", ["const:476898:8", "const:4:8"]]
- 00476898 ["CALL", null, ["callee:00459d34:8"]]
+ 00499730 ["INT_ADD", "register:40f0:8", ["const:499730:8", "const:4:8"]]
+ 00499730 ["CALL", null, ["callee:00459d34:8"]]
- 00476898 bytes 8101ff97
+ 00499730 bytes 8101ff97
~~~


<a id="compare-7465dbd5afb3fb918139b5be9649dec9"></a>

### [`004768c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md) → [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) FUN_0049975c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004751fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00476d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476d84.md) [`00476f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476f0c.md) [`00477098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477098.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00499c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md) [`00499da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md) [`00499f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047695c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md#insn-0047695c) · [`004769a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md#insn-004769a0) · [`004769b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md#insn-004769b0)
- 新版 [`004997f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md#insn-004997f4) · [`00499838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md#insn-00499838) · [`00499848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md#insn-00499848)

~~~diff
- 0047695c ["INT_ADD", "register:40f0:8", ["const:47695c:8", "const:4:8"]]
- 0047695c ["CALL", null, ["callee:00c57b40:8"]]
+ 004997f4 ["INT_ADD", "register:40f0:8", ["const:4997f4:8", "const:4:8"]]
+ 004997f4 ["CALL", null, ["callee:00c57b40:8"]]
- 0047695c bytes e5911d94
+ 004997f4 bytes d3f81e94
- 004769a0 ["INT_ADD", "register:40f0:8", ["const:4769a0:8", "const:4:8"]]
- 004769a0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00499838 ["INT_ADD", "register:40f0:8", ["const:499838:8", "const:4:8"]]
+ 00499838 ["CALL", null, ["callee:00c57a90:8"]]
- 004769a0 bytes a8911d94
+ 00499838 bytes 96f81e94
- 004769b0 ["INT_ADD", "register:40f0:8", ["const:4769b0:8", "const:4:8"]]
- 004769b0 ["CALL", null, ["callee:00499c1c:8"]]
+ 00499848 ["INT_ADD", "register:40f0:8", ["const:499848:8", "const:4:8"]]
+ 00499848 ["CALL", null, ["callee:00499c1c:8"]]
- 004769b0 bytes f5000094
+ 00499848 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5204e19aea2d33f314c772ae31805a58"></a>

### [`00476d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476d84.md) → [`00499c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md) FUN_00499c1c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004768c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00476dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476d84.md#insn-00476dec) · [`00476e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476d84.md#insn-00476e24) · [`00476ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476d84.md#insn-00476ed4)
- 新版 [`00499c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md#insn-00499c84) · [`00499cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md#insn-00499cbc) · [`00499d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md#insn-00499d6c)

~~~diff
- 00476dec ["INT_ADD", "register:40f0:8", ["const:476dec:8", "const:4:8"]]
- 00476dec ["CALL", null, ["callee:00c57b40:8"]]
+ 00499c84 ["INT_ADD", "register:40f0:8", ["const:499c84:8", "const:4:8"]]
+ 00499c84 ["CALL", null, ["callee:00c57b40:8"]]
- 00476dec bytes c1901d94
+ 00499c84 bytes aff71e94
- 00476e24 ["INT_ADD", "register:40f0:8", ["const:476e24:8", "const:4:8"]]
- 00476e24 ["CALL", null, ["callee:00c57a90:8"]]
+ 00499cbc ["INT_ADD", "register:40f0:8", ["const:499cbc:8", "const:4:8"]]
+ 00499cbc ["CALL", null, ["callee:00c57a90:8"]]
- 00476e24 bytes 87901d94
+ 00499cbc bytes 75f71e94
- 00476ed4 ["INT_ADD", "register:40f0:8", ["const:476ed4:8", "const:4:8"]]
- 00476ed4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00499d6c ["INT_ADD", "register:40f0:8", ["const:499d6c:8", "const:4:8"]]
+ 00499d6c ["CALL", null, ["callee:00c57ab0:8"]]
- 00476ed4 bytes 63901d94
+ 00499d6c bytes 51f71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a7b8faaea24b2a2a9eac0538fa03292"></a>

### [`00476f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476f0c.md) → [`00499da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md) FUN_00499da4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004768c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00476f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476f0c.md#insn-00476f7c) · [`00476fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476f0c.md#insn-00476fb4) · [`00477064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476f0c.md#insn-00477064)
- 新版 [`00499e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md#insn-00499e14) · [`00499e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md#insn-00499e4c) · [`00499efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md#insn-00499efc)

~~~diff
- 00476f7c ["INT_ADD", "register:40f0:8", ["const:476f7c:8", "const:4:8"]]
- 00476f7c ["CALL", null, ["callee:00c57b40:8"]]
+ 00499e14 ["INT_ADD", "register:40f0:8", ["const:499e14:8", "const:4:8"]]
+ 00499e14 ["CALL", null, ["callee:00c57b40:8"]]
- 00476f7c bytes 5d901d94
+ 00499e14 bytes 4bf71e94
- 00476fb4 ["INT_ADD", "register:40f0:8", ["const:476fb4:8", "const:4:8"]]
- 00476fb4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00499e4c ["INT_ADD", "register:40f0:8", ["const:499e4c:8", "const:4:8"]]
+ 00499e4c ["CALL", null, ["callee:00c57a90:8"]]
- 00476fb4 bytes 23901d94
+ 00499e4c bytes 11f71e94
- 00477064 ["INT_ADD", "register:40f0:8", ["const:477064:8", "const:4:8"]]
- 00477064 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00499efc ["INT_ADD", "register:40f0:8", ["const:499efc:8", "const:4:8"]]
+ 00499efc ["CALL", null, ["callee:00c57ab0:8"]]
- 00477064 bytes ff8f1d94
+ 00499efc bytes edf61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb62648d3c541527892e1fca87848d3"></a>

### [`00477098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477098.md) → [`00499f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md) FUN_00499f30

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004768c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004768c4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00477108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477098.md#insn-00477108) · [`00477140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477098.md#insn-00477140) · [`004771f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477098.md#insn-004771f0)
- 新版 [`00499fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md#insn-00499fa0) · [`00499fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md#insn-00499fd8) · [`0049a088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md#insn-0049a088)

~~~diff
- 00477108 ["INT_ADD", "register:40f0:8", ["const:477108:8", "const:4:8"]]
- 00477108 ["CALL", null, ["callee:00c57b40:8"]]
+ 00499fa0 ["INT_ADD", "register:40f0:8", ["const:499fa0:8", "const:4:8"]]
+ 00499fa0 ["CALL", null, ["callee:00c57b40:8"]]
- 00477108 bytes fa8f1d94
+ 00499fa0 bytes e8f61e94
- 00477140 ["INT_ADD", "register:40f0:8", ["const:477140:8", "const:4:8"]]
- 00477140 ["CALL", null, ["callee:00c57a90:8"]]
+ 00499fd8 ["INT_ADD", "register:40f0:8", ["const:499fd8:8", "const:4:8"]]
+ 00499fd8 ["CALL", null, ["callee:00c57a90:8"]]
- 00477140 bytes c08f1d94
+ 00499fd8 bytes aef61e94
- 004771f0 ["INT_ADD", "register:40f0:8", ["const:4771f0:8", "const:4:8"]]
- 004771f0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049a088 ["INT_ADD", "register:40f0:8", ["const:49a088:8", "const:4:8"]]
+ 0049a088 ["CALL", null, ["callee:00c57ab0:8"]]
- 004771f0 bytes 9c8f1d94
+ 0049a088 bytes 8af61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a471c4baeb95723ab33461b56479b225"></a>

### [`00477224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477224.md) → [`0049a0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md) FUN_0049a0bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md) · 呼出先 4件 [`00476598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476598.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) · 呼出先 4件 [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004772a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477224.md#insn-004772a0) · [`004772c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477224.md#insn-004772c8) · [`004772d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477224.md#insn-004772d8)
- 新版 [`0049a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md#insn-0049a138) · [`0049a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md#insn-0049a160) · [`0049a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md#insn-0049a170)

~~~diff
- 004772a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004772a0 ["INT_ADD", "register:40f0:8", ["const:4772a0:8", "const:4:8"]]
- 004772a0 ["CALLIND", null, ["register:0:8"]]
+ 0049a138 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0049a138 ["INT_ADD", "register:40f0:8", ["const:49a138:8", "const:4:8"]]
+ 0049a138 ["CALLIND", null, ["register:0:8"]]
- 004772a0 bytes 20013fd6
+ 0049a138 bytes 20013fd6
- 004772c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004772c8 ["INT_ADD", "register:40f0:8", ["const:4772c8:8", "const:4:8"]]
- 004772c8 ["CALLIND", null, ["register:0:8"]]
+ 0049a160 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049a160 ["INT_ADD", "register:40f0:8", ["const:49a160:8", "const:4:8"]]
+ 0049a160 ["CALLIND", null, ["register:0:8"]]
- 004772c8 bytes 00013fd6
+ 0049a160 bytes 00013fd6
- 004772d8 ["INT_ADD", "register:40f0:8", ["const:4772d8:8", "const:4:8"]]
- 004772d8 ["CALL", null, ["callee:00499430:8"]]
+ 0049a170 ["INT_ADD", "register:40f0:8", ["const:49a170:8", "const:4:8"]]
+ 0049a170 ["CALL", null, ["callee:00499430:8"]]
- 004772d8 bytes b0fcff97
+ 0049a170 bytes b0fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c17f6668de047662d85a6d363b612d64"></a>

### [`004773cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md) → [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) FUN_0049a264

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00475708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475708.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0047788c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/0047788c.md) [`00477a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477a14.md) [`00477ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477ba0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`004985a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0049a724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md) [`0049a8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md) [`0049aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00477464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md#insn-00477464) · [`004774a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md#insn-004774a8) · [`004774b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md#insn-004774b8)
- 新版 [`0049a2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md#insn-0049a2fc) · [`0049a340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md#insn-0049a340) · [`0049a350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md#insn-0049a350)

~~~diff
- 00477464 ["INT_ADD", "register:40f0:8", ["const:477464:8", "const:4:8"]]
- 00477464 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049a2fc ["INT_ADD", "register:40f0:8", ["const:49a2fc:8", "const:4:8"]]
+ 0049a2fc ["CALL", null, ["callee:00c57b40:8"]]
- 00477464 bytes 238f1d94
+ 0049a2fc bytes 11f61e94
- 004774a8 ["INT_ADD", "register:40f0:8", ["const:4774a8:8", "const:4:8"]]
- 004774a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049a340 ["INT_ADD", "register:40f0:8", ["const:49a340:8", "const:4:8"]]
+ 0049a340 ["CALL", null, ["callee:00c57a90:8"]]
- 004774a8 bytes e68e1d94
+ 0049a340 bytes d4f51e94
- 004774b8 ["INT_ADD", "register:40f0:8", ["const:4774b8:8", "const:4:8"]]
- 004774b8 ["CALL", null, ["callee:0049a724:8"]]
+ 0049a350 ["INT_ADD", "register:40f0:8", ["const:49a350:8", "const:4:8"]]
+ 0049a350 ["CALL", null, ["callee:0049a724:8"]]
- 004774b8 bytes f5000094
+ 0049a350 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35c2085e277a151afcd037a4c8d6fa00"></a>

### [`0047788c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/0047788c.md) → [`0049a724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md) FUN_0049a724

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004773cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004778f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/0047788c.md#insn-004778f4) · [`0047792c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/0047788c.md#insn-0047792c) · [`004779dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/0047788c.md#insn-004779dc)
- 新版 [`0049a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md#insn-0049a78c) · [`0049a7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md#insn-0049a7c4) · [`0049a874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md#insn-0049a874)

~~~diff
- 004778f4 ["INT_ADD", "register:40f0:8", ["const:4778f4:8", "const:4:8"]]
- 004778f4 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049a78c ["INT_ADD", "register:40f0:8", ["const:49a78c:8", "const:4:8"]]
+ 0049a78c ["CALL", null, ["callee:00c57b40:8"]]
- 004778f4 bytes ff8d1d94
+ 0049a78c bytes edf41e94
- 0047792c ["INT_ADD", "register:40f0:8", ["const:47792c:8", "const:4:8"]]
- 0047792c ["CALL", null, ["callee:00c57a90:8"]]
+ 0049a7c4 ["INT_ADD", "register:40f0:8", ["const:49a7c4:8", "const:4:8"]]
+ 0049a7c4 ["CALL", null, ["callee:00c57a90:8"]]
- 0047792c bytes c58d1d94
+ 0049a7c4 bytes b3f41e94
- 004779dc ["INT_ADD", "register:40f0:8", ["const:4779dc:8", "const:4:8"]]
- 004779dc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049a874 ["INT_ADD", "register:40f0:8", ["const:49a874:8", "const:4:8"]]
+ 0049a874 ["CALL", null, ["callee:00c57ab0:8"]]
- 004779dc bytes a18d1d94
+ 0049a874 bytes 8ff41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd6b5dfce6d64c379f16d4fba376d5f"></a>

### [`00477a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477a14.md) → [`0049a8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md) FUN_0049a8ac

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004773cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00477a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477a14.md#insn-00477a84) · [`00477abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477a14.md#insn-00477abc) · [`00477b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477a14.md#insn-00477b6c)
- 新版 [`0049a91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md#insn-0049a91c) · [`0049a954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md#insn-0049a954) · [`0049aa04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md#insn-0049aa04)

~~~diff
- 00477a84 ["INT_ADD", "register:40f0:8", ["const:477a84:8", "const:4:8"]]
- 00477a84 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049a91c ["INT_ADD", "register:40f0:8", ["const:49a91c:8", "const:4:8"]]
+ 0049a91c ["CALL", null, ["callee:00c57b40:8"]]
- 00477a84 bytes 9b8d1d94
+ 0049a91c bytes 89f41e94
- 00477abc ["INT_ADD", "register:40f0:8", ["const:477abc:8", "const:4:8"]]
- 00477abc ["CALL", null, ["callee:00c57a90:8"]]
+ 0049a954 ["INT_ADD", "register:40f0:8", ["const:49a954:8", "const:4:8"]]
+ 0049a954 ["CALL", null, ["callee:00c57a90:8"]]
- 00477abc bytes 618d1d94
+ 0049a954 bytes 4ff41e94
- 00477b6c ["INT_ADD", "register:40f0:8", ["const:477b6c:8", "const:4:8"]]
- 00477b6c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049aa04 ["INT_ADD", "register:40f0:8", ["const:49aa04:8", "const:4:8"]]
+ 0049aa04 ["CALL", null, ["callee:00c57ab0:8"]]
- 00477b6c bytes 3d8d1d94
+ 0049aa04 bytes 2bf41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47fac38160ee81dcb3b105029b2550b8"></a>

### [`00477ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477ba0.md) → [`0049aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md) FUN_0049aa38

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004773cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/004773cc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00477c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477ba0.md#insn-00477c10) · [`00477c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477ba0.md#insn-00477c48) · [`00477cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477ba0.md#insn-00477cf8)
- 新版 [`0049aaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md#insn-0049aaa8) · [`0049aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md#insn-0049aae0) · [`0049ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md#insn-0049ab90)

~~~diff
- 00477c10 ["INT_ADD", "register:40f0:8", ["const:477c10:8", "const:4:8"]]
- 00477c10 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049aaa8 ["INT_ADD", "register:40f0:8", ["const:49aaa8:8", "const:4:8"]]
+ 0049aaa8 ["CALL", null, ["callee:00c57b40:8"]]
- 00477c10 bytes 388d1d94
+ 0049aaa8 bytes 26f41e94
- 00477c48 ["INT_ADD", "register:40f0:8", ["const:477c48:8", "const:4:8"]]
- 00477c48 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049aae0 ["INT_ADD", "register:40f0:8", ["const:49aae0:8", "const:4:8"]]
+ 0049aae0 ["CALL", null, ["callee:00c57a90:8"]]
- 00477c48 bytes fe8c1d94
+ 0049aae0 bytes ecf31e94
- 00477cf8 ["INT_ADD", "register:40f0:8", ["const:477cf8:8", "const:4:8"]]
- 00477cf8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049ab90 ["INT_ADD", "register:40f0:8", ["const:49ab90:8", "const:4:8"]]
+ 0049ab90 ["CALL", null, ["callee:00c57ab0:8"]]
- 00477cf8 bytes da8c1d94
+ 0049ab90 bytes c8f31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f8bd03fde429c1eb7b1160362795c9b"></a>

### [`00477e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e1c.md) → [`0049acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049acb4.md) FUN_0049acb4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047580c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047580c.md) · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00477e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e1c.md#insn-00477e38)
- 新版 [`0049acd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049acb4.md#insn-0049acd0)

~~~diff
- 00477e38 ["INT_ADD", "register:40f0:8", ["const:477e38:8", "const:4:8"]]
- 00477e38 ["CALL", null, ["callee:00c57a80:8"]]
+ 0049acd0 ["INT_ADD", "register:40f0:8", ["const:49acd0:8", "const:4:8"]]
+ 0049acd0 ["CALL", null, ["callee:00c57a80:8"]]
- 00477e38 bytes 7e8c1d94
+ 0049acd0 bytes 6cf31e94
~~~


<a id="compare-4b431d2f55493c8828dd26e0708d5da7"></a>

### [`00477e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e4c.md) → [`0049ace4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md) FUN_0049ace4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004665d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004665d0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c580f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00477e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e4c.md#insn-00477e78) · [`00477e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e4c.md#insn-00477e94) · [`00477ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e4c.md#insn-00477ea0)
- 新版 [`0049ad10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md#insn-0049ad10) · [`0049ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md#insn-0049ad2c) · [`0049ad38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md#insn-0049ad38)

~~~diff
- 00477e78 ["INT_ADD", "register:40f0:8", ["const:477e78:8", "const:4:8"]]
- 00477e78 ["CALL", null, ["callee:00c580f0:8"]]
+ 0049ad10 ["INT_ADD", "register:40f0:8", ["const:49ad10:8", "const:4:8"]]
+ 0049ad10 ["CALL", null, ["callee:00c580f0:8"]]
- 00477e78 bytes 0a8e1d94
+ 0049ad10 bytes f8f41e94
- 00477e94 ["INT_ADD", "register:40f0:8", ["const:477e94:8", "const:4:8"]]
- 00477e94 ["CALL", null, ["callee:00489468:8"]]
+ 0049ad2c ["INT_ADD", "register:40f0:8", ["const:49ad2c:8", "const:4:8"]]
+ 0049ad2c ["CALL", null, ["callee:00489468:8"]]
- 00477e94 bytes cfb9ff97
+ 0049ad2c bytes cfb9ff97
- 00477ea0 ["INT_ADD", "register:40f0:8", ["const:477ea0:8", "const:4:8"]]
- 00477ea0 ["CALL", null, ["callee:00c538e0:8"]]
+ 0049ad38 ["INT_ADD", "register:40f0:8", ["const:49ad38:8", "const:4:8"]]
+ 0049ad38 ["CALL", null, ["callee:00c538e0:8"]]
- 00477ea0 bytes fc7b1d94
+ 0049ad38 bytes eae21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c531185155dcb3f041860cc33766f2f7"></a>

### [`004784fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784fc.md) → [`0049b394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md) FUN_0049b394

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784fc.md#insn-00478538) · [`00478554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784fc.md#insn-00478554)
- 新版 [`0049b3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md#insn-0049b3d0) · [`0049b3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md#insn-0049b3ec)

~~~diff
- 00478538 ["INT_ADD", "register:40f0:8", ["const:478538:8", "const:4:8"]]
- 00478538 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049b3d0 ["INT_ADD", "register:40f0:8", ["const:49b3d0:8", "const:4:8"]]
+ 0049b3d0 ["CALL", null, ["callee:00c57a90:8"]]
- 00478538 bytes c28a1d94
+ 0049b3d0 bytes b0f11e94
- 00478554 ["INT_ADD", "register:40f0:8", ["const:478554:8", "const:4:8"]]
- 00478554 ["CALL", null, ["callee:00c57c90:8"]]
+ 0049b3ec ["INT_ADD", "register:40f0:8", ["const:49b3ec:8", "const:4:8"]]
+ 0049b3ec ["CALL", null, ["callee:00c57c90:8"]]
- 00478554 bytes 3b8b1d94
+ 0049b3ec bytes 29f21e94
~~~


<a id="compare-6a1c29b6fa8d59cbb36873cc70fb1187"></a>

### [`004786d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004786d4.md) → [`0049b56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md) FUN_0049b56c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) · 呼出先 4件 [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) [`0047d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d078.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 4件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004786d4.md#insn-00478700) · [`00478720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004786d4.md#insn-00478720) · [`00478754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004786d4.md#insn-00478754)
- 新版 [`0049b598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md#insn-0049b598) · [`0049b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md#insn-0049b5b8) · [`0049b5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md#insn-0049b5ec)

~~~diff
- 00478700 ["INT_ADD", "register:40f0:8", ["const:478700:8", "const:4:8"]]
- 00478700 ["CALL", null, ["callee:0049ff10:8"]]
+ 0049b598 ["INT_ADD", "register:40f0:8", ["const:49b598:8", "const:4:8"]]
+ 0049b598 ["CALL", null, ["callee:0049ff10:8"]]
- 00478700 bytes 5e120094
+ 0049b598 bytes 5e120094
- 00478720 ["INT_ADD", "register:40f0:8", ["const:478720:8", "const:4:8"]]
- 00478720 ["CALL", null, ["callee:0049b64c:8"]]
+ 0049b5b8 ["INT_ADD", "register:40f0:8", ["const:49b5b8:8", "const:4:8"]]
+ 0049b5b8 ["CALL", null, ["callee:0049b64c:8"]]
- 00478720 bytes 25000094
+ 0049b5b8 bytes 25000094
- 00478754 ["INT_ADD", "register:40f0:8", ["const:478754:8", "const:4:8"]]
- 00478754 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049b5ec ["INT_ADD", "register:40f0:8", ["const:49b5ec:8", "const:4:8"]]
+ 0049b5ec ["CALL", null, ["callee:00c57ab0:8"]]
- 00478754 bytes 438a1d94
+ 0049b5ec bytes 31f11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-880c29d53299fcdc4c3bc9caab90bcf7"></a>

### [`00478d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d10.md) → [`0049bba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bba8.md) FUN_0049bba8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d10.md#insn-00478d54)
- 新版 [`0049bbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bba8.md#insn-0049bbec)

~~~diff
- 00478d54 ["INT_ADD", "register:40f0:8", ["const:478d54:8", "const:4:8"]]
- 00478d54 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049bbec ["INT_ADD", "register:40f0:8", ["const:49bbec:8", "const:4:8"]]
+ 0049bbec ["CALL", null, ["callee:00c57ab0:8"]]
- 00478d54 bytes c3881d94
+ 0049bbec bytes b1ef1e94
~~~


<a id="compare-bfd3b61b97be0231c35824f83a61fa49"></a>

### [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) → [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) FUN_0049bfe4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) · 呼出先 8件 [`0047a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md) [`0047a39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a39c.md) [`0047a520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a520.md) [`0047a5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md) [`0047a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a9e0.md)
- 新版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 8件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) [`0049d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md) [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) [`0049d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004791a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md#insn-004791a0) · [`004791b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md#insn-004791b4) · [`00479240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md#insn-00479240)
- 新版 [`0049c038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md#insn-0049c038) · [`0049c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md#insn-0049c04c) · [`0049c0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md#insn-0049c0d8)

~~~diff
- 004791a0 ["INT_ADD", "register:40f0:8", ["const:4791a0:8", "const:4:8"]]
- 004791a0 ["CALL", null, ["callee:0049d158:8"]]
+ 0049c038 ["INT_ADD", "register:40f0:8", ["const:49c038:8", "const:4:8"]]
+ 0049c038 ["CALL", null, ["callee:0049d158:8"]]
- 004791a0 bytes 48040094
+ 0049c038 bytes 48040094
- 004791b4 ["INT_ADD", "register:40f0:8", ["const:4791b4:8", "const:4:8"]]
- 004791b4 ["CALL", null, ["callee:0049d158:8"]]
+ 0049c04c ["INT_ADD", "register:40f0:8", ["const:49c04c:8", "const:4:8"]]
+ 0049c04c ["CALL", null, ["callee:0049d158:8"]]
- 004791b4 bytes 43040094
+ 0049c04c bytes 43040094
- 00479240 ["INT_ADD", "register:40f0:8", ["const:479240:8", "const:4:8"]]
- 00479240 ["CALL", null, ["callee:0049d158:8"]]
+ 0049c0d8 ["INT_ADD", "register:40f0:8", ["const:49c0d8:8", "const:4:8"]]
+ 0049c0d8 ["CALL", null, ["callee:0049d158:8"]]
- 00479240 bytes 20040094
+ 0049c0d8 bytes 20040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54a8d5257003e32d3587d00a3887d5fb"></a>

### [`0047a1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a1b0.md) → [`0049d048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d048.md) FUN_0049d048

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a1b0.md#insn-0047a1f0)
- 新版 [`0049d088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d048.md#insn-0049d088)

~~~diff
- 0047a1f0 ["INT_ADD", "register:40f0:8", ["const:47a1f0:8", "const:4:8"]]
- 0047a1f0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049d088 ["INT_ADD", "register:40f0:8", ["const:49d088:8", "const:4:8"]]
+ 0049d088 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047a1f0 bytes 9c831d94
+ 0049d088 bytes 8aea1e94
~~~


<a id="compare-f36df6e2b53fc60502ac163854a1573c"></a>

### [`0047a228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a228.md) → [`0049d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md) FUN_0049d0c0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) · 呼出先 2件 [`0047c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md)
- 新版 呼出元 1件 [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 2件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a228.md#insn-0047a2b8) · [`0047a2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a228.md#insn-0047a2bc)
- 新版 [`0049d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md#insn-0049d150) · [`0049d154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md#insn-0049d154)

~~~diff
- 0047a2b8 ["INT_ADD", "register:40f0:8", ["const:47a2b8:8", "const:4:8"]]
- 0047a2b8 ["CALL", null, ["callee:0049f3c4:8"]]
+ 0049d150 ["INT_ADD", "register:40f0:8", ["const:49d150:8", "const:4:8"]]
+ 0049d150 ["CALL", null, ["callee:0049f3c4:8"]]
- 0047a2b8 bytes 9d080094
+ 0049d150 bytes 9d080094
- 0047a2bc ["INT_ADD", "register:40f0:8", ["const:47a2bc:8", "const:4:8"]]
- 0047a2bc ["CALL", null, ["callee:0049f3d8:8"]]
+ 0049d154 ["INT_ADD", "register:40f0:8", ["const:49d154:8", "const:4:8"]]
+ 0049d154 ["CALL", null, ["callee:0049f3d8:8"]]
- 0047a2bc bytes a1080094
+ 0049d154 bytes a1080094
~~~


<a id="compare-8e170dc9f0d0af1cc4e7abbf2f4c3fe7"></a>

### [`0047a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md) → [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) FUN_0049d158

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) [`0047a520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a520.md) [`0047a5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md) [`0047a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a9e0.md) · 呼出先 2件 [`0047c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md)
- 新版 呼出元 4件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`0049d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md) [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) [`0049d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md) · 呼出先 2件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md#insn-0047a388) · [`0047a390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md#insn-0047a390) · [`0047a394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md#insn-0047a394)
- 新版 [`0049d220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md#insn-0049d220) · [`0049d228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md#insn-0049d228) · [`0049d22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md#insn-0049d22c)

~~~diff
- 0047a388 ["INT_ADD", "register:40f0:8", ["const:47a388:8", "const:4:8"]]
- 0047a388 ["CALL", null, ["callee:0049f3c4:8"]]
+ 0049d220 ["INT_ADD", "register:40f0:8", ["const:49d220:8", "const:4:8"]]
+ 0049d220 ["CALL", null, ["callee:0049f3c4:8"]]
- 0047a388 bytes 69080094
+ 0049d220 bytes 69080094
- 0047a390 ["INT_ADD", "register:40f0:8", ["const:47a390:8", "const:4:8"]]
- 0047a390 ["CALL", null, ["callee:0049f3d8:8"]]
+ 0049d228 ["INT_ADD", "register:40f0:8", ["const:49d228:8", "const:4:8"]]
+ 0049d228 ["CALL", null, ["callee:0049f3d8:8"]]
- 0047a390 bytes 6c080094
+ 0049d228 bytes 6c080094
- 0047a394 ["INT_ADD", "register:40f0:8", ["const:47a394:8", "const:4:8"]]
- 0047a394 ["CALL", null, ["callee:0049f3c4:8"]]
+ 0049d22c ["INT_ADD", "register:40f0:8", ["const:49d22c:8", "const:4:8"]]
+ 0049d22c ["CALL", null, ["callee:0049f3c4:8"]]
- 0047a394 bytes 66080094
+ 0049d22c bytes 66080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12fe9bd3613ced2b7a72303afb4b0cee"></a>

### [`0047a520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a520.md) → [`0049d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md) FUN_0049d3b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) · 呼出先 1件 [`0047a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md)
- 新版 呼出元 1件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) · 呼出先 1件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a520.md#insn-0047a568) · [`0047a588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a520.md#insn-0047a588) · [`0047a59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a520.md#insn-0047a59c)
- 新版 [`0049d400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md#insn-0049d400) · [`0049d420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md#insn-0049d420) · [`0049d434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md#insn-0049d434)

~~~diff
- 0047a568 ["INT_ADD", "register:40f0:8", ["const:47a568:8", "const:4:8"]]
- 0047a568 ["CALL", null, ["callee:0049d158:8"]]
+ 0049d400 ["INT_ADD", "register:40f0:8", ["const:49d400:8", "const:4:8"]]
+ 0049d400 ["CALL", null, ["callee:0049d158:8"]]
- 0047a568 bytes 56ffff97
+ 0049d400 bytes 56ffff97
- 0047a588 ["INT_ADD", "register:40f0:8", ["const:47a588:8", "const:4:8"]]
- 0047a588 ["CALL", null, ["callee:0049d158:8"]]
+ 0049d420 ["INT_ADD", "register:40f0:8", ["const:49d420:8", "const:4:8"]]
+ 0049d420 ["CALL", null, ["callee:0049d158:8"]]
- 0047a588 bytes 4effff97
+ 0049d420 bytes 4effff97
- 0047a59c ["INT_ADD", "register:40f0:8", ["const:47a59c:8", "const:4:8"]]
- 0047a59c ["CALL", null, ["callee:0049d158:8"]]
+ 0049d434 ["INT_ADD", "register:40f0:8", ["const:49d434:8", "const:4:8"]]
+ 0049d434 ["CALL", null, ["callee:0049d158:8"]]
- 0047a59c bytes 49ffff97
+ 0049d434 bytes 49ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14397b34de52595cf848a45d38c4355f"></a>

### [`0047ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md) → [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) FUN_0049d9e0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) · 呼出先 8件 [`0047bbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bbd4.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`0047ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 8件 [`0049ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ab90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md#insn-0047ab90) · [`0047abac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md#insn-0047abac) · [`0047ac04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md#insn-0047ac04)
- 新版 [`0049da28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md#insn-0049da28) · [`0049da44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md#insn-0049da44) · [`0049da9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md#insn-0049da9c)

~~~diff
- 0047ab90 ["INT_ADD", "register:40f0:8", ["const:47ab90:8", "const:4:8"]]
- 0047ab90 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049da28 ["INT_ADD", "register:40f0:8", ["const:49da28:8", "const:4:8"]]
+ 0049da28 ["CALL", null, ["callee:00c57a90:8"]]
- 0047ab90 bytes 2c811d94
+ 0049da28 bytes 1ae81e94
- 0047abac ["INT_ADD", "register:40f0:8", ["const:47abac:8", "const:4:8"]]
- 0047abac ["CALL", null, ["callee:00c57c90:8"]]
+ 0049da44 ["INT_ADD", "register:40f0:8", ["const:49da44:8", "const:4:8"]]
+ 0049da44 ["CALL", null, ["callee:00c57c90:8"]]
- 0047abac bytes a5811d94
+ 0049da44 bytes 93e81e94
- 0047ac04 ["INT_ADD", "register:40f0:8", ["const:47ac04:8", "const:4:8"]]
- 0047ac04 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049da9c ["INT_ADD", "register:40f0:8", ["const:49da9c:8", "const:4:8"]]
+ 0049da9c ["CALL", null, ["callee:00c57b40:8"]]
- 0047ac04 bytes 3b811d94
+ 0049da9c bytes 29e81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a01a552804d433a0aa56a385005920c4"></a>

### [`0047ad80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ad80.md) → [`0049dc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc18.md) FUN_0049dc18

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047adcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ad80.md#insn-0047adcc)
- 新版 [`0049dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc18.md#insn-0049dc64)

~~~diff
- 0047adcc ["INT_ADD", "register:40f0:8", ["const:47adcc:8", "const:4:8"]]
- 0047adcc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049dc64 ["INT_ADD", "register:40f0:8", ["const:49dc64:8", "const:4:8"]]
+ 0049dc64 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047adcc bytes a5801d94
+ 0049dc64 bytes 93e71e94
~~~


<a id="compare-23df3048a3147e3d2a6831cd482e293a"></a>

### [`0047b068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b068.md) → [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) FUN_0049df00

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00479f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md) · 呼出先 2件 [`0047c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md)
- 新版 呼出元 1件 [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) · 呼出先 2件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047b390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b068.md#insn-0047b390) · [`0047b5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b068.md#insn-0047b5bc) · [`0047b5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b068.md#insn-0047b5c4)
- 新版 [`0049e228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md#insn-0049e228) · [`0049e454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md#insn-0049e454) · [`0049e45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md#insn-0049e45c)

~~~diff
- 0047b390 ["INT_ADD", "register:40f0:8", ["const:47b390:8", "const:4:8"]]
- 0047b390 ["CALL", null, ["callee:0049f3d8:8"]]
+ 0049e228 ["INT_ADD", "register:40f0:8", ["const:49e228:8", "const:4:8"]]
+ 0049e228 ["CALL", null, ["callee:0049f3d8:8"]]
- 0047b390 bytes 6c040094
+ 0049e228 bytes 6c040094
- 0047b5bc ["INT_ADD", "register:40f0:8", ["const:47b5bc:8", "const:4:8"]]
- 0047b5bc ["CALL", null, ["callee:0049f3d8:8"]]
+ 0049e454 ["INT_ADD", "register:40f0:8", ["const:49e454:8", "const:4:8"]]
+ 0049e454 ["CALL", null, ["callee:0049f3d8:8"]]
- 0047b5bc bytes e1030094
+ 0049e454 bytes e1030094
- 0047b5c4 ["INT_ADD", "register:40f0:8", ["const:47b5c4:8", "const:4:8"]]
- 0047b5c4 ["CALL", null, ["callee:0049f3c4:8"]]
+ 0049e45c ["INT_ADD", "register:40f0:8", ["const:49e45c:8", "const:4:8"]]
+ 0049e45c ["CALL", null, ["callee:0049f3c4:8"]]
- 0047b5c4 bytes da030094
+ 0049e45c bytes da030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6a3ce374b8b6d049d97c37c4f6518c0"></a>

### [`0047b5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b5ec.md) → [`0049e484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md) FUN_0049e484

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0047a39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a39c.md) [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`00893ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00893/00893ea0.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 4件 [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) [`008c79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c7/008c79a4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047b690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b5ec.md#insn-0047b690) · [`0047b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b5ec.md#insn-0047b704) · [`0047b740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b5ec.md#insn-0047b740)
- 新版 [`0049e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md#insn-0049e528) · [`0049e59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md#insn-0049e59c) · [`0049e5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md#insn-0049e5d8)

~~~diff
- 0047b690 ["INT_ADD", "register:40f0:8", ["const:47b690:8", "const:4:8"]]
- 0047b690 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049e528 ["INT_ADD", "register:40f0:8", ["const:49e528:8", "const:4:8"]]
+ 0049e528 ["CALL", null, ["callee:00c57a90:8"]]
- 0047b690 bytes 6c7e1d94
+ 0049e528 bytes 5ae51e94
- 0047b704 ["INT_ADD", "register:40f0:8", ["const:47b704:8", "const:4:8"]]
- 0047b704 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049e59c ["INT_ADD", "register:40f0:8", ["const:49e59c:8", "const:4:8"]]
+ 0049e59c ["CALL", null, ["callee:00c57b40:8"]]
- 0047b704 bytes 7b7e1d94
+ 0049e59c bytes 69e51e94
- 0047b740 ["INT_ADD", "register:40f0:8", ["const:47b740:8", "const:4:8"]]
- 0047b740 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049e5d8 ["INT_ADD", "register:40f0:8", ["const:49e5d8:8", "const:4:8"]]
+ 0049e5d8 ["CALL", null, ["callee:00c57a90:8"]]
- 0047b740 bytes 407e1d94
+ 0049e5d8 bytes 2ee51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12111de723175a91f5a7f3e1930ab9cb"></a>

### [`0047b7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b7fc.md) → [`0049e694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md) FUN_0049e694

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0047a39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a39c.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0047ca1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca1c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0049f8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047b8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b7fc.md#insn-0047b8b4) · [`0047b8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b7fc.md#insn-0047b8f4) · [`0047b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b7fc.md#insn-0047b908)
- 新版 [`0049e74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md#insn-0049e74c) · [`0049e78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md#insn-0049e78c) · [`0049e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md#insn-0049e7a0)

~~~diff
- 0047b8b4 ["INT_ADD", "register:40f0:8", ["const:47b8b4:8", "const:4:8"]]
- 0047b8b4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049e74c ["INT_ADD", "register:40f0:8", ["const:49e74c:8", "const:4:8"]]
+ 0049e74c ["CALL", null, ["callee:00c57a90:8"]]
- 0047b8b4 bytes e37d1d94
+ 0049e74c bytes d1e41e94
- 0047b8f4 ["INT_ADD", "register:40f0:8", ["const:47b8f4:8", "const:4:8"]]
- 0047b8f4 ["CALL", null, ["callee:0049f8b4:8"]]
+ 0049e78c ["INT_ADD", "register:40f0:8", ["const:49e78c:8", "const:4:8"]]
+ 0049e78c ["CALL", null, ["callee:0049f8b4:8"]]
- 0047b8f4 bytes 4a040094
+ 0049e78c bytes 4a040094
- 0047b908 ["INT_ADD", "register:40f0:8", ["const:47b908:8", "const:4:8"]]
- 0047b908 ["CALL", null, ["callee:00c57c00:8"]]
+ 0049e7a0 ["INT_ADD", "register:40f0:8", ["const:49e7a0:8", "const:4:8"]]
+ 0049e7a0 ["CALL", null, ["callee:00c57c00:8"]]
- 0047b908 bytes 2a7e1d94
+ 0049e7a0 bytes 18e51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f848b01a7a23bb0c93d045fd1222f347"></a>

### [`0047bcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bcc8.md) → [`0049eb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md) FUN_0049eb60

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 2件 [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047bd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bcc8.md#insn-0047bd04) · [`0047bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bcc8.md#insn-0047bdc8)
- 新版 [`0049eb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md#insn-0049eb9c) · [`0049ec60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md#insn-0049ec60)

~~~diff
- 0047bd04 ["INT_ADD", "register:40f0:8", ["const:47bd04:8", "const:4:8"]]
- 0047bd04 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049eb9c ["INT_ADD", "register:40f0:8", ["const:49eb9c:8", "const:4:8"]]
+ 0049eb9c ["CALL", null, ["callee:00c57a90:8"]]
- 0047bd04 bytes cf7c1d94
+ 0049eb9c bytes bde31e94
- 0047bdc8 ["INT_ADD", "register:40f0:8", ["const:47bdc8:8", "const:4:8"]]
- 0047bdc8 ["CALL", null, ["callee:0047d678:8"]]
+ 0049ec60 ["INT_ADD", "register:40f0:8", ["const:49ec60:8", "const:4:8"]]
+ 0049ec60 ["CALL", null, ["callee:0047d678:8"]]
- 0047bdc8 bytes 867aff97
+ 0049ec60 bytes 867aff97
~~~


<a id="compare-c1bfc456b1b93c3a5a0eb2fd20e7a99c"></a>

### [`0047bdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bdcc.md) → [`0049ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md) FUN_0049ec64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) · 呼出先 7件 [`0045a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md) [`0047c2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c2a4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 7件 [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`0049f13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f13c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047bf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bdcc.md#insn-0047bf34) · [`0047bf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bdcc.md#insn-0047bf8c) · [`0047bfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bdcc.md#insn-0047bfa4)
- 新版 [`0049edcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md#insn-0049edcc) · [`0049ee24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md#insn-0049ee24) · [`0049ee3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md#insn-0049ee3c)

~~~diff
- 0047bf34 ["INT_ADD", "register:40f0:8", ["const:47bf34:8", "const:4:8"]]
- 0047bf34 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049edcc ["INT_ADD", "register:40f0:8", ["const:49edcc:8", "const:4:8"]]
+ 0049edcc ["CALL", null, ["callee:00c57b40:8"]]
- 0047bf34 bytes 6f7c1d94
+ 0049edcc bytes 5de31e94
- 0047bf8c ["INT_ADD", "register:40f0:8", ["const:47bf8c:8", "const:4:8"]]
- 0047bf8c ["CALL", null, ["callee:0049f13c:8"]]
+ 0049ee24 ["INT_ADD", "register:40f0:8", ["const:49ee24:8", "const:4:8"]]
+ 0049ee24 ["CALL", null, ["callee:0049f13c:8"]]
- 0047bf8c bytes c6000094
+ 0049ee24 bytes c6000094
- 0047bfa4 ["INT_ADD", "register:40f0:8", ["const:47bfa4:8", "const:4:8"]]
- 0047bfa4 ["CALL", null, ["callee:0047d574:8"]]
+ 0049ee3c ["INT_ADD", "register:40f0:8", ["const:49ee3c:8", "const:4:8"]]
+ 0049ee3c ["CALL", null, ["callee:0047d574:8"]]
- 0047bfa4 bytes ce79ff97
+ 0049ee3c bytes ce79ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed52f9d588ce5e94e7ac4327748c97c"></a>

### [`0047c498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c498.md) → [`0049f330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f330.md) FUN_0049f330

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047c4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c498.md#insn-0047c4f4)
- 新版 [`0049f38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f330.md#insn-0049f38c)

~~~diff
- 0047c4f4 ["INT_ADD", "register:40f0:8", ["const:47c4f4:8", "const:4:8"]]
- 0047c4f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049f38c ["INT_ADD", "register:40f0:8", ["const:49f38c:8", "const:4:8"]]
+ 0049f38c ["CALL", null, ["callee:00c57ab0:8"]]
- 0047c4f4 bytes db7a1d94
+ 0049f38c bytes c9e11e94
~~~


<a id="compare-bc1fc14552eb68ce62e811f8b10115ec"></a>

### [`0047c568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c568.md) → [`0049f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md) FUN_0049f400

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047c5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c568.md#insn-0047c5e8) · [`0047c61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c568.md#insn-0047c61c) · [`0047c72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c568.md#insn-0047c72c)
- 新版 [`0049f480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md#insn-0049f480) · [`0049f4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md#insn-0049f4b4) · [`0049f5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md#insn-0049f5c4)

~~~diff
- 0047c5e8 ["INT_ADD", "register:40f0:8", ["const:47c5e8:8", "const:4:8"]]
- 0047c5e8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049f480 ["INT_ADD", "register:40f0:8", ["const:49f480:8", "const:4:8"]]
+ 0049f480 ["CALL", null, ["callee:00c57a90:8"]]
- 0047c5e8 bytes 967a1d94
+ 0049f480 bytes 84e11e94
- 0047c61c ["INT_ADD", "register:40f0:8", ["const:47c61c:8", "const:4:8"]]
- 0047c61c ["CALL", null, ["callee:00c57b40:8"]]
+ 0049f4b4 ["INT_ADD", "register:40f0:8", ["const:49f4b4:8", "const:4:8"]]
+ 0049f4b4 ["CALL", null, ["callee:00c57b40:8"]]
- 0047c61c bytes b57a1d94
+ 0049f4b4 bytes a3e11e94
- 0047c72c ["INT_ADD", "register:40f0:8", ["const:47c72c:8", "const:4:8"]]
- 0047c72c ["CALL", null, ["callee:00c57b40:8"]]
+ 0049f5c4 ["INT_ADD", "register:40f0:8", ["const:49f5c4:8", "const:4:8"]]
+ 0049f5c4 ["CALL", null, ["callee:00c57b40:8"]]
- 0047c72c bytes 717a1d94
+ 0049f5c4 bytes 5fe11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f1d7b259482019b5b2ce24773c46a3"></a>

### [`0047c854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c854.md) → [`0049f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md) FUN_0049f6ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0047c9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9e0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0049f878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047c8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c854.md#insn-0047c8e0) · [`0047c998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c854.md#insn-0047c998) · [`0047c9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c854.md#insn-0047c9b4)
- 新版 [`0049f778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md#insn-0049f778) · [`0049f830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md#insn-0049f830) · [`0049f84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md#insn-0049f84c)

~~~diff
- 0047c8e0 ["INT_ADD", "register:40f0:8", ["const:47c8e0:8", "const:4:8"]]
- 0047c8e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049f778 ["INT_ADD", "register:40f0:8", ["const:49f778:8", "const:4:8"]]
+ 0049f778 ["CALL", null, ["callee:00c57a90:8"]]
- 0047c8e0 bytes d8791d94
+ 0049f778 bytes c6e01e94
- 0047c998 ["INT_ADD", "register:40f0:8", ["const:47c998:8", "const:4:8"]]
- 0047c998 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049f830 ["INT_ADD", "register:40f0:8", ["const:49f830:8", "const:4:8"]]
+ 0049f830 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047c998 bytes b2791d94
+ 0049f830 bytes a0e01e94
- 0047c9b4 ["INT_ADD", "register:40f0:8", ["const:47c9b4:8", "const:4:8"]]
- 0047c9b4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049f84c ["INT_ADD", "register:40f0:8", ["const:49f84c:8", "const:4:8"]]
+ 0049f84c ["CALL", null, ["callee:00c57ab0:8"]]
- 0047c9b4 bytes ab791d94
+ 0049f84c bytes 99e01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7615715c9b82db55f8a5cfb8ff8186fb"></a>

### [`0047ca1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca1c.md) → [`0049f8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md) FUN_0049f8b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047b7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b7fc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0049e694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ca84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca1c.md#insn-0047ca84) · [`0047cabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca1c.md#insn-0047cabc) · [`0047cb6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca1c.md#insn-0047cb6c)
- 新版 [`0049f91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md#insn-0049f91c) · [`0049f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md#insn-0049f954) · [`0049fa04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md#insn-0049fa04)

~~~diff
- 0047ca84 ["INT_ADD", "register:40f0:8", ["const:47ca84:8", "const:4:8"]]
- 0047ca84 ["CALL", null, ["callee:00c57b40:8"]]
+ 0049f91c ["INT_ADD", "register:40f0:8", ["const:49f91c:8", "const:4:8"]]
+ 0049f91c ["CALL", null, ["callee:00c57b40:8"]]
- 0047ca84 bytes 9b791d94
+ 0049f91c bytes 89e01e94
- 0047cabc ["INT_ADD", "register:40f0:8", ["const:47cabc:8", "const:4:8"]]
- 0047cabc ["CALL", null, ["callee:00c57a90:8"]]
+ 0049f954 ["INT_ADD", "register:40f0:8", ["const:49f954:8", "const:4:8"]]
+ 0049f954 ["CALL", null, ["callee:00c57a90:8"]]
- 0047cabc bytes 61791d94
+ 0049f954 bytes 4fe01e94
- 0047cb6c ["INT_ADD", "register:40f0:8", ["const:47cb6c:8", "const:4:8"]]
- 0047cb6c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0049fa04 ["INT_ADD", "register:40f0:8", ["const:49fa04:8", "const:4:8"]]
+ 0049fa04 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047cb6c bytes 3d791d94
+ 0049fa04 bytes 2be01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc5c7525554a9a6bd4ccea7a8ed79875"></a>

### [`0047d490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d490.md) → [`004a0328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md) FUN_004a0328

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d078.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0047d610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d610.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004a04a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d490.md#insn-0047d518) · [`0047d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d490.md#insn-0047d5cc) · [`0047d5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d490.md#insn-0047d5e8)
- 新版 [`004a03b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md#insn-004a03b0) · [`004a0464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md#insn-004a0464) · [`004a0480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md#insn-004a0480)

~~~diff
- 0047d518 ["INT_ADD", "register:40f0:8", ["const:47d518:8", "const:4:8"]]
- 0047d518 ["CALL", null, ["callee:00c57a90:8"]]
+ 004a03b0 ["INT_ADD", "register:40f0:8", ["const:4a03b0:8", "const:4:8"]]
+ 004a03b0 ["CALL", null, ["callee:00c57a90:8"]]
- 0047d518 bytes ca761d94
+ 004a03b0 bytes b8dd1e94
- 0047d5cc ["INT_ADD", "register:40f0:8", ["const:47d5cc:8", "const:4:8"]]
- 0047d5cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 004a0464 ["INT_ADD", "register:40f0:8", ["const:4a0464:8", "const:4:8"]]
+ 004a0464 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047d5cc bytes a5761d94
+ 004a0464 bytes 93dd1e94
- 0047d5e8 ["INT_ADD", "register:40f0:8", ["const:47d5e8:8", "const:4:8"]]
- 0047d5e8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004a0480 ["INT_ADD", "register:40f0:8", ["const:4a0480:8", "const:4:8"]]
+ 004a0480 ["CALL", null, ["callee:00c57ab0:8"]]
- 0047d5e8 bytes 9e761d94
+ 004a0480 bytes 8cdd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffa94ba461cffa89fb27c34a03167b0f"></a>

### [`0047ebdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ebdc.md) → [`004a1a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md) _ZN5Botan7AES_1285clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dbb0.md) [`0051dca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dca0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540a48.md) [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ebdc.md#insn-0047ec00) · [`0047ec10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ebdc.md#insn-0047ec10) · [`0047ec28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ebdc.md#insn-0047ec28)
- 新版 [`004a1a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md#insn-004a1a98) · [`004a1aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md#insn-004a1aa8) · [`004a1ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md#insn-004a1ac0)

~~~diff
- 0047ec00 ["INT_ADD", "register:40f0:8", ["const:47ec00:8", "const:4:8"]]
- 0047ec00 ["CALL", null, ["callee:00c57c90:8"]]
+ 004a1a98 ["INT_ADD", "register:40f0:8", ["const:4a1a98:8", "const:4:8"]]
+ 004a1a98 ["CALL", null, ["callee:00c57c90:8"]]
- 0047ec00 bytes 90711d94
+ 004a1a98 bytes 7ed81e94
- 0047ec10 ["INT_ADD", "register:40f0:8", ["const:47ec10:8", "const:4:8"]]
- 0047ec10 ["CALL", null, ["callee:00540a48:8"]]
+ 004a1aa8 ["INT_ADD", "register:40f0:8", ["const:4a1aa8:8", "const:4:8"]]
+ 004a1aa8 ["CALL", null, ["callee:00540a48:8"]]
- 0047ec10 bytes e87b0294
+ 004a1aa8 bytes e87b0294
- 0047ec28 ["INT_ADD", "register:40f0:8", ["const:47ec28:8", "const:4:8"]]
- 0047ec28 ["CALL", null, ["callee:00c57c90:8"]]
+ 004a1ac0 ["INT_ADD", "register:40f0:8", ["const:4a1ac0:8", "const:4:8"]]
+ 004a1ac0 ["CALL", null, ["callee:00c57c90:8"]]
- 0047ec28 bytes 86711d94
+ 004a1ac0 bytes 74d81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1eb8db0d50cb909632794d656e7bfd"></a>

### [`0047eef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047eef8.md) → [`004a1d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md) _ZN5Botan7AES_1925clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dbb0.md) [`0051dca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dca0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540a48.md) [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ef1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047eef8.md#insn-0047ef1c) · [`0047ef2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047eef8.md#insn-0047ef2c) · [`0047ef44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047eef8.md#insn-0047ef44)
- 新版 [`004a1db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md#insn-004a1db4) · [`004a1dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md#insn-004a1dc4) · [`004a1ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md#insn-004a1ddc)

~~~diff
- 0047ef1c ["INT_ADD", "register:40f0:8", ["const:47ef1c:8", "const:4:8"]]
- 0047ef1c ["CALL", null, ["callee:00c57c90:8"]]
+ 004a1db4 ["INT_ADD", "register:40f0:8", ["const:4a1db4:8", "const:4:8"]]
+ 004a1db4 ["CALL", null, ["callee:00c57c90:8"]]
- 0047ef1c bytes c9701d94
+ 004a1db4 bytes b7d71e94
- 0047ef2c ["INT_ADD", "register:40f0:8", ["const:47ef2c:8", "const:4:8"]]
- 0047ef2c ["CALL", null, ["callee:00540a48:8"]]
+ 004a1dc4 ["INT_ADD", "register:40f0:8", ["const:4a1dc4:8", "const:4:8"]]
+ 004a1dc4 ["CALL", null, ["callee:00540a48:8"]]
- 0047ef2c bytes 217b0294
+ 004a1dc4 bytes 217b0294
- 0047ef44 ["INT_ADD", "register:40f0:8", ["const:47ef44:8", "const:4:8"]]
- 0047ef44 ["CALL", null, ["callee:00c57c90:8"]]
+ 004a1ddc ["INT_ADD", "register:40f0:8", ["const:4a1ddc:8", "const:4:8"]]
+ 004a1ddc ["CALL", null, ["callee:00c57c90:8"]]
- 0047ef44 bytes bf701d94
+ 004a1ddc bytes add71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c76981fd26e694fa757f447199a3e9bb"></a>

### [`0047f214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f214.md) → [`004a20ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md) _ZN5Botan7AES_2565clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dbb0.md) [`0051dca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dca0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540a48.md) [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f214.md#insn-0047f238) · [`0047f248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f214.md#insn-0047f248) · [`0047f260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f214.md#insn-0047f260)
- 新版 [`004a20d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md#insn-004a20d0) · [`004a20e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md#insn-004a20e0) · [`004a20f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md#insn-004a20f8)

~~~diff
- 0047f238 ["INT_ADD", "register:40f0:8", ["const:47f238:8", "const:4:8"]]
- 0047f238 ["CALL", null, ["callee:00c57c90:8"]]
+ 004a20d0 ["INT_ADD", "register:40f0:8", ["const:4a20d0:8", "const:4:8"]]
+ 004a20d0 ["CALL", null, ["callee:00c57c90:8"]]
- 0047f238 bytes 02701d94
+ 004a20d0 bytes f0d61e94
- 0047f248 ["INT_ADD", "register:40f0:8", ["const:47f248:8", "const:4:8"]]
- 0047f248 ["CALL", null, ["callee:00540a48:8"]]
+ 004a20e0 ["INT_ADD", "register:40f0:8", ["const:4a20e0:8", "const:4:8"]]
+ 004a20e0 ["CALL", null, ["callee:00540a48:8"]]
- 0047f248 bytes 5a7a0294
+ 004a20e0 bytes 5a7a0294
- 0047f260 ["INT_ADD", "register:40f0:8", ["const:47f260:8", "const:4:8"]]
- 0047f260 ["CALL", null, ["callee:00c57c90:8"]]
+ 004a20f8 ["INT_ADD", "register:40f0:8", ["const:4a20f8:8", "const:4:8"]]
+ 004a20f8 ["CALL", null, ["callee:00c57c90:8"]]
- 0047f260 bytes f86f1d94
+ 004a20f8 bytes e6d61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89dae0a62e941b8fcbd8b6189cd18603"></a>

### [`004822c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004822c0.md) → [`004a5158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5158.md) _ZN5BotaneqERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb850.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004822c0.md#insn-00482390)
- 新版 [`004a5228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5158.md#insn-004a5228)

~~~diff
- 00482390 ["INT_ADD", "register:40f0:8", ["const:482390:8", "const:4:8"]]
- 00482390 ["CALL", null, ["callee:00c57c50:8"]]
+ 004a5228 ["INT_ADD", "register:40f0:8", ["const:4a5228:8", "const:4:8"]]
+ 004a5228 ["CALL", null, ["callee:00c57c50:8"]]
- 00482390 bytes 9c631d94
+ 004a5228 bytes 8aca1e94
~~~


<a id="compare-edd9c741acf5dc11c436d195bfb5e2f5"></a>

### [`00482414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482414.md) → [`004a52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52ac.md) _ZN5BotanneERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb850.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048241c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482414.md#insn-0048241c)
- 新版 [`004a52b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52ac.md#insn-004a52b4)

~~~diff
- 0048241c ["INT_ADD", "register:40f0:8", ["const:48241c:8", "const:4:8"]]
- 0048241c ["CALL", null, ["callee:00c582a0:8"]]
+ 004a52b4 ["INT_ADD", "register:40f0:8", ["const:4a52b4:8", "const:4:8"]]
+ 004a52b4 ["CALL", null, ["callee:00c582a0:8"]]
- 0048241c bytes 0d651d94
+ 004a52b4 bytes fbcb1e94
~~~


<a id="compare-0defff85ccdafb79964c25e999dba78a"></a>

### [`00482430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482430.md) → [`004a52c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md) _ZNK5Botan19AlgorithmIdentifier11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb870.md) [`00bdb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb880.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582c0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482430.md#insn-00482458) · [`0048246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482430.md#insn-0048246c) · [`00482488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482430.md#insn-00482488)
- 新版 [`004a52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md#insn-004a52f0) · [`004a5304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md#insn-004a5304) · [`004a5320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md#insn-004a5320)

~~~diff
- 00482458 ["INT_ADD", "register:40f0:8", ["const:482458:8", "const:4:8"]]
- 00482458 ["CALL", null, ["callee:00c582b0:8"]]
+ 004a52f0 ["INT_ADD", "register:40f0:8", ["const:4a52f0:8", "const:4:8"]]
+ 004a52f0 ["CALL", null, ["callee:00c582b0:8"]]
- 00482458 bytes 02651d94
+ 004a52f0 bytes f0cb1e94
- 0048246c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048246c ["INT_ADD", "register:40f0:8", ["const:48246c:8", "const:4:8"]]
- 0048246c ["CALLIND", null, ["register:0:8"]]
+ 004a5304 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5304 ["INT_ADD", "register:40f0:8", ["const:4a5304:8", "const:4:8"]]
+ 004a5304 ["CALLIND", null, ["register:0:8"]]
- 0048246c bytes 00013fd6
+ 004a5304 bytes 00013fd6
- 00482488 ["INT_ADD", "register:40f0:8", ["const:482488:8", "const:4:8"]]
- 00482488 ["CALL", null, ["callee:00c582c0:8"]]
+ 004a5320 ["INT_ADD", "register:40f0:8", ["const:4a5320:8", "const:4:8"]]
+ 004a5320 ["CALL", null, ["callee:00c582c0:8"]]
- 00482488 bytes fa641d94
+ 004a5320 bytes e8cb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d4ed225de78b615a8ecc55e10fdcf5"></a>

### [`00482690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482690.md) → [`004a5528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5528.md) _ZN5Botan11DER_Encoder6encodeERKNS_11ASN1_ObjectE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004826b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482690.md#insn-004826b0)
- 新版 [`004a5548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5528.md#insn-004a5548)

~~~diff
- 004826b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004826b0 ["INT_ADD", "register:40f0:8", ["const:4826b0:8", "const:4:8"]]
- 004826b0 ["CALLIND", null, ["register:0:8"]]
+ 004a5548 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5548 ["INT_ADD", "register:40f0:8", ["const:4a5548:8", "const:4:8"]]
+ 004a5548 ["CALLIND", null, ["register:0:8"]]
- 004826b0 bytes 00013fd6
+ 004a5548 bytes 00013fd6
~~~


<a id="compare-6b8be3d6b3ca8808addb25db04653f4a"></a>

### [`00482a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482a74.md) → [`004a590c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a590c.md) _ZN5Botan11BER_Decoder6decodeERNS_11ASN1_ObjectENS_8ASN1_TagES3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482a74.md#insn-00482a94)
- 新版 [`004a592c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a590c.md#insn-004a592c)

~~~diff
- 00482a94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482a94 ["INT_ADD", "register:40f0:8", ["const:482a94:8", "const:4:8"]]
- 00482a94 ["CALLIND", null, ["register:0:8"]]
+ 004a592c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a592c ["INT_ADD", "register:40f0:8", ["const:4a592c:8", "const:4:8"]]
+ 004a592c ["CALLIND", null, ["register:0:8"]]
- 00482a94 bytes 00013fd6
+ 004a592c bytes 00013fd6
~~~


<a id="compare-e826f0740710a1fb4103fafd4446c2ac"></a>

### [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) → [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) FUN_004a5940

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`004830c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md) [`004e40b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md) [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) [`004fc31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc31c.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 5件 [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a5f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md) [`00506f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md) [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) [`0051f1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f1b4.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md#insn-00482af8) · [`00482b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md#insn-00482b2c) · [`00482b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md#insn-00482b70)
- 新版 [`004a5990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md#insn-004a5990) · [`004a59c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md#insn-004a59c4) · [`004a5a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md#insn-004a5a08)

~~~diff
- 00482af8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482af8 ["INT_ADD", "register:40f0:8", ["const:482af8:8", "const:4:8"]]
- 00482af8 ["CALLIND", null, ["register:0:8"]]
+ 004a5990 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5990 ["INT_ADD", "register:40f0:8", ["const:4a5990:8", "const:4:8"]]
+ 004a5990 ["CALLIND", null, ["register:0:8"]]
- 00482af8 bytes 00013fd6
+ 004a5990 bytes 00013fd6
- 00482b2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00482b2c ["INT_ADD", "register:40f0:8", ["const:482b2c:8", "const:4:8"]]
- 00482b2c ["CALLIND", null, ["register:0:8"]]
+ 004a59c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a59c4 ["INT_ADD", "register:40f0:8", ["const:4a59c4:8", "const:4:8"]]
+ 004a59c4 ["CALLIND", null, ["register:0:8"]]
- 00482b2c bytes 00013fd6
+ 004a59c4 bytes 00013fd6
- 00482b70 ["INT_ADD", "register:40f0:8", ["const:482b70:8", "const:4:8"]]
- 00482b70 ["CALL", null, ["callee:00c57a90:8"]]
+ 004a5a08 ["INT_ADD", "register:40f0:8", ["const:4a5a08:8", "const:4:8"]]
+ 004a5a08 ["CALL", null, ["callee:00c57a90:8"]]
- 00482b70 bytes 34611d94
+ 004a5a08 bytes 22c81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a742cdae60394d414b23206f6b61fd5f"></a>

### [`00482fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482fe4.md) → [`004a5e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md) _ZNK5Botan9Attribute11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb870.md) [`00bdb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb880.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582c0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048300c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482fe4.md#insn-0048300c) · [`00483020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482fe4.md#insn-00483020) · [`00483030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482fe4.md#insn-00483030)
- 新版 [`004a5ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md#insn-004a5ea4) · [`004a5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md#insn-004a5eb8) · [`004a5ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md#insn-004a5ec8)

~~~diff
- 0048300c ["INT_ADD", "register:40f0:8", ["const:48300c:8", "const:4:8"]]
- 0048300c ["CALL", null, ["callee:00c582b0:8"]]
+ 004a5ea4 ["INT_ADD", "register:40f0:8", ["const:4a5ea4:8", "const:4:8"]]
+ 004a5ea4 ["CALL", null, ["callee:00c582b0:8"]]
- 0048300c bytes 15621d94
+ 004a5ea4 bytes 03c91e94
- 00483020 ["COPY", "register:0:8", ["register:4040:8"]]
- 00483020 ["INT_ADD", "register:40f0:8", ["const:483020:8", "const:4:8"]]
- 00483020 ["CALLIND", null, ["register:0:8"]]
+ 004a5eb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5eb8 ["INT_ADD", "register:40f0:8", ["const:4a5eb8:8", "const:4:8"]]
+ 004a5eb8 ["CALLIND", null, ["register:0:8"]]
- 00483020 bytes 00013fd6
+ 004a5eb8 bytes 00013fd6
- 00483030 ["INT_ADD", "register:40f0:8", ["const:483030:8", "const:4:8"]]
- 00483030 ["CALL", null, ["callee:00c582b0:8"]]
+ 004a5ec8 ["INT_ADD", "register:40f0:8", ["const:4a5ec8:8", "const:4:8"]]
+ 004a5ec8 ["CALL", null, ["callee:00c582b0:8"]]
- 00483030 bytes 0c621d94
+ 004a5ec8 bytes fac81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57b3b33ba352ba2f28928b00c2879927"></a>

### [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) → [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) FUN_004a680c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`0048c5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c5ac.md) [`004994e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004994e0.md) [`0049c054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c054.md) [`004b5004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5004.md) [`004c5f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5f28.md) · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 11件 [`004af444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md) [`004bc378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md) [`004beeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beeec.md) [`004d7e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md) [`004e8dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md) · 呼出先 1件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048399c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md#insn-0048399c)
- 新版 [`004a6834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md#insn-004a6834)

~~~diff
- 0048399c ["INT_ADD", "register:40f0:8", ["const:48399c:8", "const:4:8"]]
- 0048399c ["CALL", null, ["callee:00c57b80:8"]]
+ 004a6834 ["INT_ADD", "register:40f0:8", ["const:4a6834:8", "const:4:8"]]
+ 004a6834 ["CALL", null, ["callee:00c57b80:8"]]
- 0048399c bytes e55d1d94
+ 004a6834 bytes d3c41e94
~~~


<a id="compare-731f9569a30a013383e86b2faa6f17f9"></a>

### [`00484d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484d30.md) → [`004a7bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md) _ZN5Botan3OIDpLEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9c0.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c58410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58410.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484d30.md#insn-00484dac) · [`00484dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484d30.md#insn-00484dd8) · [`00484dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484d30.md#insn-00484dec)
- 新版 [`004a7c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md#insn-004a7c44) · [`004a7c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md#insn-004a7c70) · [`004a7c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md#insn-004a7c84)

~~~diff
- 00484dac ["INT_ADD", "register:40f0:8", ["const:484dac:8", "const:4:8"]]
- 00484dac ["CALL", null, ["callee:00c57a90:8"]]
+ 004a7c44 ["INT_ADD", "register:40f0:8", ["const:4a7c44:8", "const:4:8"]]
+ 004a7c44 ["CALL", null, ["callee:00c57a90:8"]]
- 00484dac bytes a5581d94
+ 004a7c44 bytes 93bf1e94
- 00484dd8 ["INT_ADD", "register:40f0:8", ["const:484dd8:8", "const:4:8"]]
- 00484dd8 ["CALL", null, ["callee:00c57c00:8"]]
+ 004a7c70 ["INT_ADD", "register:40f0:8", ["const:4a7c70:8", "const:4:8"]]
+ 004a7c70 ["CALL", null, ["callee:00c57c00:8"]]
- 00484dd8 bytes f6581d94
+ 004a7c70 bytes e4bf1e94
- 00484dec ["INT_ADD", "register:40f0:8", ["const:484dec:8", "const:4:8"]]
- 00484dec ["CALL", null, ["callee:00c57ab0:8"]]
+ 004a7c84 ["INT_ADD", "register:40f0:8", ["const:4a7c84:8", "const:4:8"]]
+ 004a7c84 ["CALL", null, ["callee:00c57ab0:8"]]
- 00484dec bytes 9d581d94
+ 004a7c84 bytes 8bbf1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-662e809eb69deec1b19dd719db30f554"></a>

### [`00489150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489150.md) → [`004abfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md) _ZN5Botan6BigInt6encodeERKS0_NS0_4BaseE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdba80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba80.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdbaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbaf0.md) [`00bdbb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb00.md)
- 新版 呼出元 1件 [`00c584d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584d0.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58540.md) [`00c58550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489150.md#insn-00489170) · [`0048918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489150.md#insn-0048918c) · [`004891a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489150.md#insn-004891a8)
- 新版 [`004ac008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md#insn-004ac008) · [`004ac024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md#insn-004ac024) · [`004ac040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md#insn-004ac040)

~~~diff
- 00489170 ["INT_ADD", "register:40f0:8", ["const:489170:8", "const:4:8"]]
- 00489170 ["CALL", null, ["callee:00c58540:8"]]
+ 004ac008 ["INT_ADD", "register:40f0:8", ["const:4ac008:8", "const:4:8"]]
+ 004ac008 ["CALL", null, ["callee:00c58540:8"]]
- 00489170 bytes 604a1d94
+ 004ac008 bytes 4eb11e94
- 0048918c ["INT_ADD", "register:40f0:8", ["const:48918c:8", "const:4:8"]]
- 0048918c ["CALL", null, ["callee:00c57a90:8"]]
+ 004ac024 ["INT_ADD", "register:40f0:8", ["const:4ac024:8", "const:4:8"]]
+ 004ac024 ["CALL", null, ["callee:00c57a90:8"]]
- 0048918c bytes ad471d94
+ 004ac024 bytes 9bae1e94
- 004891a8 ["INT_ADD", "register:40f0:8", ["const:4891a8:8", "const:4:8"]]
- 004891a8 ["CALL", null, ["callee:00c57c90:8"]]
+ 004ac040 ["INT_ADD", "register:40f0:8", ["const:4ac040:8", "const:4:8"]]
+ 004ac040 ["CALL", null, ["callee:00c57c90:8"]]
- 004891a8 bytes 26481d94
+ 004ac040 bytes 14af1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4bb7d558fc0ef5ece3b45780698118b"></a>

### [`004892c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/004892c8.md) → [`004ac160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac160.md) FUN_004ac160

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004892e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/004892c8.md#insn-004892e4)
- 新版 [`004ac17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac160.md#insn-004ac17c)

~~~diff
- 004892e4 ["INT_ADD", "register:40f0:8", ["const:4892e4:8", "const:4:8"]]
- 004892e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ac17c ["INT_ADD", "register:40f0:8", ["const:4ac17c:8", "const:4:8"]]
+ 004ac17c ["CALL", null, ["callee:00c57ab0:8"]]
- 004892e4 bytes 5f471d94
+ 004ac17c bytes 4dae1e94
~~~


<a id="compare-020396150a8c130466f13ed4a1c6af98"></a>

### [`00489d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489d4c.md) → [`004acbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md) FUN_004acbe4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004fd178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd178.md) [`006bbf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md) · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00520010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520010.md) [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489d4c.md#insn-00489d64) · [`00489da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489d4c.md#insn-00489da0) · [`00489dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489d4c.md#insn-00489dc4)
- 新版 [`004acbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md#insn-004acbfc) · [`004acc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md#insn-004acc38) · [`004acc5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md#insn-004acc5c)

~~~diff
- 00489d64 ["INT_ADD", "register:40f0:8", ["const:489d64:8", "const:4:8"]]
- 00489d64 ["CALL", null, ["callee:00c57be0:8"]]
+ 004acbfc ["INT_ADD", "register:40f0:8", ["const:4acbfc:8", "const:4:8"]]
+ 004acbfc ["CALL", null, ["callee:00c57be0:8"]]
- 00489d64 bytes 0b451d94
+ 004acbfc bytes f9ab1e94
- 00489da0 ["INT_ADD", "register:40f0:8", ["const:489da0:8", "const:4:8"]]
- 00489da0 ["CALL", null, ["callee:00c57c50:8"]]
+ 004acc38 ["INT_ADD", "register:40f0:8", ["const:4acc38:8", "const:4:8"]]
+ 004acc38 ["CALL", null, ["callee:00c57c50:8"]]
- 00489da0 bytes 18451d94
+ 004acc38 bytes 06ac1e94
- 00489dc4 ["INT_ADD", "register:40f0:8", ["const:489dc4:8", "const:4:8"]]
- 00489dc4 ["CALL", null, ["callee:004428dc:8"]]
+ 004acc5c ["INT_ADD", "register:40f0:8", ["const:4acc5c:8", "const:4:8"]]
+ 004acc5c ["CALL", null, ["callee:004428dc:8"]]
- 00489dc4 bytes 0658fe97
+ 004acc5c bytes 2057fe97
~~~


<a id="compare-62e7e4835121c3f4babcc03d9a569739"></a>

### [`0048c288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c288.md) → [`004af120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af120.md) _ZNK5Botan9X509_Time16to_std_timepointEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c288.md#insn-0048c2b8) · [`0048c2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c288.md#insn-0048c2dc)
- 新版 [`004af150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af120.md#insn-004af150) · [`004af174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af120.md#insn-004af174)

~~~diff
- 0048c2b8 ["INT_ADD", "register:40f0:8", ["const:48c2b8:8", "const:4:8"]]
- 0048c2b8 ["CALL", null, ["callee:00c58600:8"]]
+ 004af150 ["INT_ADD", "register:40f0:8", ["const:4af150:8", "const:4:8"]]
+ 004af150 ["CALL", null, ["callee:00c58600:8"]]
- 0048c2b8 bytes 3e3e1d94
+ 004af150 bytes 2ca51e94
- 0048c2dc ["INT_ADD", "register:40f0:8", ["const:48c2dc:8", "const:4:8"]]
- 0048c2dc ["CALL", null, ["callee:00c57ae0:8"]]
+ 004af174 ["INT_ADD", "register:40f0:8", ["const:4af174:8", "const:4:8"]]
+ 004af174 ["CALL", null, ["callee:00c57ae0:8"]]
- 0048c2dc bytes 6d3b1d94
+ 004af174 bytes 5ba21e94
~~~


<a id="compare-2f9ddbcbd6ecd0c0ef193c14dfefde26"></a>

### [`0048c508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c508.md) → [`004af3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3a0.md) _ZN5BotaneqERKNS_9X509_TimeES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c508.md#insn-0048c510)
- 新版 [`004af3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3a0.md#insn-004af3a8)

~~~diff
- 0048c510 ["INT_ADD", "register:40f0:8", ["const:48c510:8", "const:4:8"]]
- 0048c510 ["CALL", null, ["callee:00c585e0:8"]]
+ 004af3a8 ["INT_ADD", "register:40f0:8", ["const:4af3a8:8", "const:4:8"]]
+ 004af3a8 ["CALL", null, ["callee:00c585e0:8"]]
- 0048c510 bytes a03d1d94
+ 004af3a8 bytes 8ea41e94
~~~


<a id="compare-5bac1b8e6ad29865e72425f3d89fd9af"></a>

### [`0048c524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c524.md) → [`004af3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3bc.md) _ZN5BotanneERKNS_9X509_TimeES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c524.md#insn-0048c52c)
- 新版 [`004af3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3bc.md#insn-004af3c4)

~~~diff
- 0048c52c ["INT_ADD", "register:40f0:8", ["const:48c52c:8", "const:4:8"]]
- 0048c52c ["CALL", null, ["callee:00c585e0:8"]]
+ 004af3c4 ["INT_ADD", "register:40f0:8", ["const:4af3c4:8", "const:4:8"]]
+ 004af3c4 ["CALL", null, ["callee:00c585e0:8"]]
- 0048c52c bytes 993d1d94
+ 004af3c4 bytes 87a41e94
~~~


<a id="compare-4599e20798831a4fc31d3a75905b8230"></a>

### [`0048c540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c540.md) → [`004af3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3d8.md) _ZN5BotanleERKNS_9X509_TimeES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c540.md#insn-0048c548)
- 新版 [`004af3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3d8.md#insn-004af3e0)

~~~diff
- 0048c548 ["INT_ADD", "register:40f0:8", ["const:48c548:8", "const:4:8"]]
- 0048c548 ["CALL", null, ["callee:00c585e0:8"]]
+ 004af3e0 ["INT_ADD", "register:40f0:8", ["const:4af3e0:8", "const:4:8"]]
+ 004af3e0 ["CALL", null, ["callee:00c585e0:8"]]
- 0048c548 bytes 923d1d94
+ 004af3e0 bytes 80a41e94
~~~


<a id="compare-91e623bc71bc46c2d99ec530caa7144a"></a>

### [`0048c55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c55c.md) → [`004af3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3f4.md) _ZN5BotangeERKNS_9X509_TimeES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c55c.md#insn-0048c564)
- 新版 [`004af3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3f4.md#insn-004af3fc)

~~~diff
- 0048c564 ["INT_ADD", "register:40f0:8", ["const:48c564:8", "const:4:8"]]
- 0048c564 ["CALL", null, ["callee:00c585e0:8"]]
+ 004af3fc ["INT_ADD", "register:40f0:8", ["const:4af3fc:8", "const:4:8"]]
+ 004af3fc ["CALL", null, ["callee:00c585e0:8"]]
- 0048c564 bytes 8b3d1d94
+ 004af3fc bytes 79a41e94
~~~


<a id="compare-73a44cbb10434df35803ebf99cfbd962"></a>

### [`0048c578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c578.md) → [`004af410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af410.md) _ZN5BotanltERKNS_9X509_TimeES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c578.md#insn-0048c580)
- 新版 [`004af418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af410.md#insn-004af418)

~~~diff
- 0048c580 ["INT_ADD", "register:40f0:8", ["const:48c580:8", "const:4:8"]]
- 0048c580 ["CALL", null, ["callee:00c585e0:8"]]
+ 004af418 ["INT_ADD", "register:40f0:8", ["const:4af418:8", "const:4:8"]]
+ 004af418 ["CALL", null, ["callee:00c585e0:8"]]
- 0048c580 bytes 843d1d94
+ 004af418 bytes 72a41e94
~~~


<a id="compare-aee7bb091b3df546c47c749c5d176904"></a>

### [`0048c590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c590.md) → [`004af428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af428.md) _ZN5BotangtERKNS_9X509_TimeES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c590.md#insn-0048c598)
- 新版 [`004af430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af428.md#insn-004af430)

~~~diff
- 0048c598 ["INT_ADD", "register:40f0:8", ["const:48c598:8", "const:4:8"]]
- 0048c598 ["CALL", null, ["callee:00c585e0:8"]]
+ 004af430 ["INT_ADD", "register:40f0:8", ["const:4af430:8", "const:4:8"]]
+ 004af430 ["CALL", null, ["callee:00c585e0:8"]]
- 0048c598 bytes 7e3d1d94
+ 004af430 bytes 6ca41e94
~~~


<a id="compare-3bd76253fe058d86e731ec6c5fc27248"></a>

### [`0048c978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c978.md) → [`004af810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af810.md) _ZNK5Botan11BER_Decoder10more_itemsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048c994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c978.md#insn-0048c994)
- 新版 [`004af82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af810.md#insn-004af82c)

~~~diff
- 0048c994 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048c994 ["INT_ADD", "register:40f0:8", ["const:48c994:8", "const:4:8"]]
- 0048c994 ["CALLIND", null, ["register:0:8"]]
+ 004af82c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004af82c ["INT_ADD", "register:40f0:8", ["const:4af82c:8", "const:4:8"]]
+ 004af82c ["CALLIND", null, ["register:0:8"]]
- 0048c994 bytes 00013fd6
+ 004af82c bytes 00013fd6
~~~


<a id="compare-9fc02b96aecdff00213b3a87fece2368"></a>

### [`0048cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cadc.md) → [`004af974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af974.md) _ZN5Botan11BER_Decoder17discard_remainingEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048cb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cadc.md#insn-0048cb10) · [`0048cb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cadc.md#insn-0048cb3c)
- 新版 [`004af9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af974.md#insn-004af9a8) · [`004af9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af974.md#insn-004af9d4)

~~~diff
- 0048cb10 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048cb10 ["INT_ADD", "register:40f0:8", ["const:48cb10:8", "const:4:8"]]
- 0048cb10 ["CALLIND", null, ["register:0:8"]]
+ 004af9a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004af9a8 ["INT_ADD", "register:40f0:8", ["const:4af9a8:8", "const:4:8"]]
+ 004af9a8 ["CALLIND", null, ["register:0:8"]]
- 0048cb10 bytes 00013fd6
+ 004af9a8 bytes 00013fd6
- 0048cb3c ["INT_ADD", "register:40f0:8", ["const:48cb3c:8", "const:4:8"]]
- 0048cb3c ["CALL", null, ["callee:00c57ae0:8"]]
+ 004af9d4 ["INT_ADD", "register:40f0:8", ["const:4af9d4:8", "const:4:8"]]
+ 004af9d4 ["CALL", null, ["callee:00c57ae0:8"]]
- 0048cb3c bytes 55391d94
+ 004af9d4 bytes 43a01e94
~~~


<a id="compare-fe87d3ad0afb7c9ebdf4f4d438e84043"></a>

### [`0048e570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e570.md) → [`004b1408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1408.md) _ZN5Botan11BER_Decoder21get_next_octet_stringEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c584a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048e598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e570.md#insn-0048e598)
- 新版 [`004b1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1408.md#insn-004b1430)

~~~diff
- 0048e598 ["INT_ADD", "register:40f0:8", ["const:48e598:8", "const:4:8"]]
- 0048e598 ["CALL", null, ["callee:00c584a0:8"]]
+ 004b1430 ["INT_ADD", "register:40f0:8", ["const:4b1430:8", "const:4:8"]]
+ 004b1430 ["CALL", null, ["callee:00c584a0:8"]]
- 0048e598 bytes 2e351d94
+ 004b1430 bytes 1c9c1e94
~~~


<a id="compare-72eb9dadc82bf889241d95d24753101c"></a>

### [`0048f6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md) → [`004b2580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md) FUN_004b2580

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0048a5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md) [`0048f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md) · 呼出先 2件 [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`004ad470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md) [`004b1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md) · 呼出先 2件 [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048f730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md#insn-0048f730) · [`0048f7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md#insn-0048f7dc) · [`0048f824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md#insn-0048f824)
- 新版 [`004b25c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md#insn-004b25c8) · [`004b2674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md#insn-004b2674) · [`004b26bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md#insn-004b26bc)

~~~diff
- 0048f730 ["INT_ADD", "register:40f0:8", ["const:48f730:8", "const:4:8"]]
- 0048f730 ["CALL", null, ["callee:00541164:8"]]
+ 004b25c8 ["INT_ADD", "register:40f0:8", ["const:4b25c8:8", "const:4:8"]]
+ 004b25c8 ["CALL", null, ["callee:00541164:8"]]
- 0048f730 bytes e73a0294
+ 004b25c8 bytes e73a0294
- 0048f7dc ["INT_ADD", "register:40f0:8", ["const:48f7dc:8", "const:4:8"]]
- 0048f7dc ["CALL", null, ["callee:00541164:8"]]
+ 004b2674 ["INT_ADD", "register:40f0:8", ["const:4b2674:8", "const:4:8"]]
+ 004b2674 ["CALL", null, ["callee:00541164:8"]]
- 0048f7dc bytes bc3a0294
+ 004b2674 bytes bc3a0294
- 0048f824 ["INT_ADD", "register:40f0:8", ["const:48f824:8", "const:4:8"]]
- 0048f824 ["CALL", null, ["callee:00541164:8"]]
+ 004b26bc ["INT_ADD", "register:40f0:8", ["const:4b26bc:8", "const:4:8"]]
+ 004b26bc ["CALL", null, ["callee:00541164:8"]]
- 0048f824 bytes aa3a0294
+ 004b26bc bytes aa3a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b07bbe31b86296a6ad51f4b764d436c7"></a>

### [`0048fd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fd08.md) → [`004b2ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2ba0.md) _ZN5Botan11DER_Encoder9raw_bytesEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb870.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c582c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048fd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fd08.md#insn-0048fd2c) · [`0048fd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fd08.md#insn-0048fd58) · [`0048fd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fd08.md#insn-0048fd80)
- 新版 [`004b2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2ba0.md#insn-004b2bc4) · [`004b2bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2ba0.md#insn-004b2bf0) · [`004b2c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2ba0.md#insn-004b2c18)

~~~diff
- 0048fd2c ["INT_ADD", "register:40f0:8", ["const:48fd2c:8", "const:4:8"]]
- 0048fd2c ["CALL", null, ["callee:00c582c0:8"]]
+ 004b2bc4 ["INT_ADD", "register:40f0:8", ["const:4b2bc4:8", "const:4:8"]]
+ 004b2bc4 ["CALL", null, ["callee:00c582c0:8"]]
- 0048fd2c bytes d12e1d94
+ 004b2bc4 bytes bf951e94
- 0048fd58 ["INT_ADD", "register:40f0:8", ["const:48fd58:8", "const:4:8"]]
- 0048fd58 ["CALL", null, ["callee:005404ac:8"]]
+ 004b2bf0 ["INT_ADD", "register:40f0:8", ["const:4b2bf0:8", "const:4:8"]]
+ 004b2bf0 ["CALL", null, ["callee:005404ac:8"]]
- 0048fd58 bytes 2f360294
+ 004b2bf0 bytes 2f360294
- 0048fd80 ["INT_ADD", "register:40f0:8", ["const:48fd80:8", "const:4:8"]]
- 0048fd80 ["CALL", null, ["callee:00c57b40:8"]]
+ 004b2c18 ["INT_ADD", "register:40f0:8", ["const:4b2c18:8", "const:4:8"]]
+ 004b2c18 ["CALL", null, ["callee:00c57b40:8"]]
- 0048fd80 bytes dc2c1d94
+ 004b2c18 bytes ca931e94
~~~


<a id="compare-9dcd1974f78d774ca164bc13421a0583"></a>

### [`0048fdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fdac.md) → [`004b2c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2c44.md) _ZN5Botan11DER_Encoder6encodeEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048fde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fdac.md#insn-0048fde0) · [`0048fe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fdac.md#insn-0048fe04)
- 新版 [`004b2c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2c44.md#insn-004b2c78) · [`004b2c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2c44.md#insn-004b2c9c)

~~~diff
- 0048fde0 ["INT_ADD", "register:40f0:8", ["const:48fde0:8", "const:4:8"]]
- 0048fde0 ["CALL", null, ["callee:00c58420:8"]]
+ 004b2c78 ["INT_ADD", "register:40f0:8", ["const:4b2c78:8", "const:4:8"]]
+ 004b2c78 ["CALL", null, ["callee:00c58420:8"]]
- 0048fde0 bytes fc2e1d94
+ 004b2c78 bytes ea951e94
- 0048fe04 ["INT_ADD", "register:40f0:8", ["const:48fe04:8", "const:4:8"]]
- 0048fe04 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004b2c9c ["INT_ADD", "register:40f0:8", ["const:4b2c9c:8", "const:4:8"]]
+ 004b2c9c ["CALL", null, ["callee:00c57ae0:8"]]
- 0048fe04 bytes a32c1d94
+ 004b2c9c bytes 91931e94
~~~


<a id="compare-e94328b9a481a8f85ec637833d2a3304"></a>

### [`0048fe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fe08.md) → [`004b2ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2ca0.md) _ZN5Botan11DER_Encoder6encodeEbNS_8ASN1_TagES1_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048fe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fe08.md#insn-0048fe40) · [`0048fe64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fe08.md#insn-0048fe64)
- 新版 [`004b2cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2ca0.md#insn-004b2cd8) · [`004b2cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2ca0.md#insn-004b2cfc)

~~~diff
- 0048fe40 ["INT_ADD", "register:40f0:8", ["const:48fe40:8", "const:4:8"]]
- 0048fe40 ["CALL", null, ["callee:00c58420:8"]]
+ 004b2cd8 ["INT_ADD", "register:40f0:8", ["const:4b2cd8:8", "const:4:8"]]
+ 004b2cd8 ["CALL", null, ["callee:00c58420:8"]]
- 0048fe40 bytes e42e1d94
+ 004b2cd8 bytes d2951e94
- 0048fe64 ["INT_ADD", "register:40f0:8", ["const:48fe64:8", "const:4:8"]]
- 0048fe64 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004b2cfc ["INT_ADD", "register:40f0:8", ["const:4b2cfc:8", "const:4:8"]]
+ 004b2cfc ["CALL", null, ["callee:00c57ae0:8"]]
- 0048fe64 bytes 8b2c1d94
+ 004b2cfc bytes 79931e94
~~~


<a id="compare-7aa08a4d6e0ba3da63510f287ece8a5a"></a>

### [`0049054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/0049054c.md) → [`004b33e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b33e4.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_h

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00490574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/0049054c.md#insn-00490574) · [`00490598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/0049054c.md#insn-00490598)
- 新版 [`004b340c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b33e4.md#insn-004b340c) · [`004b3430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b33e4.md#insn-004b3430)

~~~diff
- 00490574 ["INT_ADD", "register:40f0:8", ["const:490574:8", "const:4:8"]]
- 00490574 ["CALL", null, ["callee:00c58420:8"]]
+ 004b340c ["INT_ADD", "register:40f0:8", ["const:4b340c:8", "const:4:8"]]
+ 004b340c ["CALL", null, ["callee:00c58420:8"]]
- 00490574 bytes 172d1d94
+ 004b340c bytes 05941e94
- 00490598 ["INT_ADD", "register:40f0:8", ["const:490598:8", "const:4:8"]]
- 00490598 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004b3430 ["INT_ADD", "register:40f0:8", ["const:4b3430:8", "const:4:8"]]
+ 004b3430 ["CALL", null, ["callee:00c57ae0:8"]]
- 00490598 bytes be2a1d94
+ 004b3430 bytes ac911e94
~~~


<a id="compare-06df2f4433539c3fb4f4ff267ce37645"></a>

### [`00490ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490ea4.md) → [`004b3d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3d3c.md) _ZN5Botan11DER_Encoder9encode_ifEbRKNS_11ASN1_ObjectE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00490ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490ea4.md#insn-00490ec8)
- 新版 [`004b3d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3d3c.md#insn-004b3d60)

~~~diff
- 00490ec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00490ec8 ["INT_ADD", "register:40f0:8", ["const:490ec8:8", "const:4:8"]]
- 00490ec8 ["CALLIND", null, ["register:0:8"]]
+ 004b3d60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004b3d60 ["INT_ADD", "register:40f0:8", ["const:4b3d60:8", "const:4:8"]]
+ 004b3d60 ["CALLIND", null, ["register:0:8"]]
- 00490ec8 bytes 00013fd6
+ 004b3d60 bytes 00013fd6
~~~


<a id="compare-45e3cee2a9c11ebb7b73ab376d826f6a"></a>

### [`00490edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490edc.md) → [`004b3d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3d74.md) _ZN5Botan9SCAN_NameC1EPKc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00490f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490edc.md#insn-00490f0c) · [`00490f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490edc.md#insn-00490f58) · [`00490f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490edc.md#insn-00490f78)
- 新版 [`004b3da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3d74.md#insn-004b3da4) · [`004b3df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3d74.md#insn-004b3df0) · [`004b3e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3d74.md#insn-004b3e10)

~~~diff
- 00490f0c ["INT_ADD", "register:40f0:8", ["const:490f0c:8", "const:4:8"]]
- 00490f0c ["CALL", null, ["callee:00c57be0:8"]]
+ 004b3da4 ["INT_ADD", "register:40f0:8", ["const:4b3da4:8", "const:4:8"]]
+ 004b3da4 ["CALL", null, ["callee:00c57be0:8"]]
- 00490f0c bytes a1281d94
+ 004b3da4 bytes 8f8f1e94
- 00490f58 ["INT_ADD", "register:40f0:8", ["const:490f58:8", "const:4:8"]]
- 00490f58 ["CALL", null, ["callee:00c57a90:8"]]
+ 004b3df0 ["INT_ADD", "register:40f0:8", ["const:4b3df0:8", "const:4:8"]]
+ 004b3df0 ["CALL", null, ["callee:00c57a90:8"]]
- 00490f58 bytes 3a281d94
+ 004b3df0 bytes 288f1e94
- 00490f78 ["INT_ADD", "register:40f0:8", ["const:490f78:8", "const:4:8"]]
- 00490f78 ["CALL", null, ["callee:00c57c00:8"]]
+ 004b3e10 ["INT_ADD", "register:40f0:8", ["const:4b3e10:8", "const:4:8"]]
+ 004b3e10 ["CALL", null, ["callee:00c57c00:8"]]
- 00490f78 bytes 8e281d94
+ 004b3e10 bytes 7c8f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef668376b182e8592fc41ca3249f971e"></a>

### [`00491b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491b68.md) → [`004b4a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a00.md) FUN_004b4a00

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00491bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491b68.md#insn-00491bb0)
- 新版 [`004b4a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a00.md#insn-004b4a48)

~~~diff
- 00491bb0 ["INT_ADD", "register:40f0:8", ["const:491bb0:8", "const:4:8"]]
- 00491bb0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004b4a48 ["INT_ADD", "register:40f0:8", ["const:4b4a48:8", "const:4:8"]]
+ 004b4a48 ["CALL", null, ["callee:00c57ab0:8"]]
- 00491bb0 bytes 2c251d94
+ 004b4a48 bytes 1a8c1e94
~~~


<a id="compare-cd0e4f2eb6ddbe376a3f26a1be1dd286"></a>

### [`00491ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491ef0.md) → [`004b4d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4d88.md) _ZNK5Botan9SCAN_Name14arg_as_integerEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c583f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00491f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491ef0.md#insn-00491f24)
- 新版 [`004b4dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4d88.md#insn-004b4dbc)

~~~diff
- 00491f24 ["INT_ADD", "register:40f0:8", ["const:491f24:8", "const:4:8"]]
- 00491f24 ["CALL", null, ["callee:00c583f0:8"]]
+ 004b4dbc ["INT_ADD", "register:40f0:8", ["const:4b4dbc:8", "const:4:8"]]
+ 004b4dbc ["CALL", null, ["callee:00c583f0:8"]]
- 00491f24 bytes 9f261d94
+ 004b4dbc bytes 8d8d1e94
~~~


<a id="compare-72a4d436522f92ba1e6e310b3d2a9b7a"></a>

### [`00492030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492030.md) → [`004b4ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4ec8.md) _ZN5Botan11OctetStringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c586e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492030.md#insn-00492068) · [`0049208c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492030.md#insn-0049208c) · [`004920a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492030.md#insn-004920a4)
- 新版 [`004b4f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4ec8.md#insn-004b4f00) · [`004b4f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4ec8.md#insn-004b4f24) · [`004b4f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4ec8.md#insn-004b4f3c)

~~~diff
- 00492068 ["INT_ADD", "register:40f0:8", ["const:492068:8", "const:4:8"]]
- 00492068 ["CALL", null, ["callee:005404ac:8"]]
+ 004b4f00 ["INT_ADD", "register:40f0:8", ["const:4b4f00:8", "const:4:8"]]
+ 004b4f00 ["CALL", null, ["callee:005404ac:8"]]
- 00492068 bytes 6b2d0294
+ 004b4f00 bytes 6b2d0294
- 0049208c ["INT_ADD", "register:40f0:8", ["const:49208c:8", "const:4:8"]]
- 0049208c ["CALL", null, ["callee:00c586e0:8"]]
+ 004b4f24 ["INT_ADD", "register:40f0:8", ["const:4b4f24:8", "const:4:8"]]
+ 004b4f24 ["CALL", null, ["callee:00c586e0:8"]]
- 0049208c bytes 01271d94
+ 004b4f24 bytes ef8d1e94
- 004920a4 ["INT_ADD", "register:40f0:8", ["const:4920a4:8", "const:4:8"]]
- 004920a4 ["CALL", null, ["callee:005404ac:8"]]
+ 004b4f3c ["INT_ADD", "register:40f0:8", ["const:4b4f3c:8", "const:4:8"]]
+ 004b4f3c ["CALL", null, ["callee:005404ac:8"]]
- 004920a4 bytes 5c2d0294
+ 004b4f3c bytes 5c2d0294
~~~


<a id="compare-fec7df09d080549c51ea7917bce39cda"></a>

### [`004920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004920f8.md) → [`004b4f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4f90.md) _ZN5Botan11OctetStringC1EPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005204e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204e8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004920f8.md#insn-00492118)
- 新版 [`004b4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4f90.md#insn-004b4fb0)

~~~diff
- 00492118 ["INT_ADD", "register:40f0:8", ["const:492118:8", "const:4:8"]]
- 00492118 ["CALL", null, ["callee:00543380:8"]]
+ 004b4fb0 ["INT_ADD", "register:40f0:8", ["const:4b4fb0:8", "const:4:8"]]
+ 004b4fb0 ["CALL", null, ["callee:00543380:8"]]
- 00492118 bytes f4380294
+ 004b4fb0 bytes f4380294
~~~


