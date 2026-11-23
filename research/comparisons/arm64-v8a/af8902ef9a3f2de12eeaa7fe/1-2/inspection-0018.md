# v15.7.4 → v16.0.0 · 要調査の変更候補 (18)

[一覧の目次](README.md)

<a id="compare-94369fbbd2b5b6494dbd912e26456ea3"></a>

### [`00a20954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20954.md) → [`00a7e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md) FUN_00a7e7e4

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) [`00a20954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20954.md) · 呼出先 2件 [`00a20954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20954.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) [`00a7e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md) · 呼出先 2件 [`00a7e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a20974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20954.md#insn-00a20974) · [`00a20980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20954.md#insn-00a20980)
- 新版 [`00a7e804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md#insn-00a7e804) · [`00a7e810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e7e4.md#insn-00a7e810)

~~~diff
- 00a20974 ["INT_ADD", "register:40f0:8", ["const:a20974:8", "const:4:8"]]
- 00a20974 ["CALL", null, ["local:b0:8"]]
+ 00a7e804 ["INT_ADD", "register:40f0:8", ["const:a7e804:8", "const:4:8"]]
+ 00a7e804 ["CALL", null, ["local:b0:8"]]
- 00a20974 bytes f8ffff97
+ 00a7e804 bytes f8ffff97
- 00a20980 ["INT_ADD", "register:40f0:8", ["const:a20980:8", "const:4:8"]]
- 00a20980 ["CALL", null, ["local:b0:8"]]
+ 00a7e810 ["INT_ADD", "register:40f0:8", ["const:a7e810:8", "const:4:8"]]
+ 00a7e810 ["CALL", null, ["local:b0:8"]]
- 00a20980 bytes f5ffff97
+ 00a7e810 bytes f5ffff97
~~~


<a id="compare-4ea89f85ac159c0449f342f7967b7ae0"></a>

### [`00a262b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a262b0.md) → [`00a84140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84140.md) FUN_00a84140

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a24a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a24/00a24a78.md) [`00a26364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26364.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00a82908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82908.md) [`00a841f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a841f4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a26320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a262b0.md#insn-00a26320) · [`00a26334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a262b0.md#insn-00a26334) · [`00a2633c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a262b0.md#insn-00a2633c)
- 新版 [`00a841b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84140.md#insn-00a841b0) · [`00a841c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84140.md#insn-00a841c4) · [`00a841cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84140.md#insn-00a841cc)

~~~diff
- 00a26320 ["INT_ADD", "register:40f0:8", ["const:a26320:8", "const:4:8"]]
- 00a26320 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a841b0 ["INT_ADD", "register:40f0:8", ["const:a841b0:8", "const:4:8"]]
+ 00a841b0 ["CALL", null, ["callee:00c538e0:8"]]
- 00a26320 bytes dcc20694
+ 00a841b0 bytes cc3d0794
- 00a26334 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a26334 ["INT_ADD", "register:40f0:8", ["const:a26334:8", "const:4:8"]]
- 00a26334 ["CALLIND", null, ["register:0:8"]]
+ 00a841c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a841c4 ["INT_ADD", "register:40f0:8", ["const:a841c4:8", "const:4:8"]]
+ 00a841c4 ["CALLIND", null, ["register:0:8"]]
- 00a26334 bytes 00013fd6
+ 00a841c4 bytes 00013fd6
- 00a2633c ["INT_ADD", "register:40f0:8", ["const:a2633c:8", "const:4:8"]]
- 00a2633c ["CALL", null, ["callee:00c57a80:8"]]
+ 00a841cc ["INT_ADD", "register:40f0:8", ["const:a841cc:8", "const:4:8"]]
+ 00a841cc ["CALL", null, ["callee:00c57a80:8"]]
- 00a2633c bytes 3dd30694
+ 00a841cc bytes 2d4e0794
~~~


<a id="compare-7748a6c92a6f61e8c07230a125b316db"></a>

### [`00a26500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26500.md) → [`00a84390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84390.md) FUN_00a84390

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a26364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26364.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00a841f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a841f4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a26538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26500.md#insn-00a26538) · [`00a26580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26500.md#insn-00a26580) · [`00a26594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26500.md#insn-00a26594)
- 新版 [`00a843c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84390.md#insn-00a843c8) · [`00a84410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84390.md#insn-00a84410) · [`00a84424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84390.md#insn-00a84424)

~~~diff
- 00a26538 ["INT_ADD", "register:40f0:8", ["const:a26538:8", "const:4:8"]]
- 00a26538 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a843c8 ["INT_ADD", "register:40f0:8", ["const:a843c8:8", "const:4:8"]]
+ 00a843c8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a26538 bytes cad20694
+ 00a843c8 bytes ba4d0794
- 00a26580 ["INT_ADD", "register:40f0:8", ["const:a26580:8", "const:4:8"]]
- 00a26580 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a84410 ["INT_ADD", "register:40f0:8", ["const:a84410:8", "const:4:8"]]
+ 00a84410 ["CALL", null, ["callee:00c538e0:8"]]
- 00a26580 bytes 44c20694
+ 00a84410 bytes 343d0794
- 00a26594 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a26594 ["INT_ADD", "register:40f0:8", ["const:a26594:8", "const:4:8"]]
- 00a26594 ["CALLIND", null, ["register:0:8"]]
+ 00a84424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a84424 ["INT_ADD", "register:40f0:8", ["const:a84424:8", "const:4:8"]]
+ 00a84424 ["CALLIND", null, ["register:0:8"]]
- 00a26594 bytes 00013fd6
+ 00a84424 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb9adab855c4579da4b248749d5983ac"></a>

### [`00a26df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26df8.md) → [`00a84c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84c88.md) FUN_00a84c88

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 1件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a26e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26df8.md#insn-00a26e08)
- 新版 [`00a84c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84c88.md#insn-00a84c98)

~~~diff
- 00a26e08 ["INT_ADD", "register:40f0:8", ["const:a26e08:8", "const:4:8"]]
- 00a26e08 ["CALL", null, ["callee:0048ce44:8"]]
+ 00a84c98 ["INT_ADD", "register:40f0:8", ["const:a84c98:8", "const:4:8"]]
+ 00a84c98 ["CALL", null, ["callee:0048ce44:8"]]
- 00a26e08 bytes 690ce997
+ 00a84c98 bytes 6b20e897
~~~


<a id="compare-67d83c815a07936d9caacc26e941da34"></a>

### [`00a288c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a288c0.md) → [`00a86750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86750.md) FUN_00a86750

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009b7d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009b7/009b7d00.md) · 呼出先 1件 [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 1件 [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a288dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a288c0.md#insn-00a288dc) · [`00a288e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a288c0.md#insn-00a288e8) · [`00a288f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a288c0.md#insn-00a288f8)
- 新版 [`00a8676c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86750.md#insn-00a8676c) · [`00a86778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86750.md#insn-00a86778) · [`00a86788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86750.md#insn-00a86788)

~~~diff
- 00a288dc ["INT_ADD", "register:40f0:8", ["const:a288dc:8", "const:4:8"]]
- 00a288dc ["CALL", null, ["callee:00481058:8"]]
+ 00a8676c ["INT_ADD", "register:40f0:8", ["const:a8676c:8", "const:4:8"]]
+ 00a8676c ["CALL", null, ["callee:00481058:8"]]
- 00a288dc bytes 39d6e897
+ 00a8676c bytes 3beae797
- 00a288e8 ["INT_ADD", "register:40f0:8", ["const:a288e8:8", "const:4:8"]]
- 00a288e8 ["CALL", null, ["callee:00481058:8"]]
+ 00a86778 ["INT_ADD", "register:40f0:8", ["const:a86778:8", "const:4:8"]]
+ 00a86778 ["CALL", null, ["callee:00481058:8"]]
- 00a288e8 bytes 36d6e897
+ 00a86778 bytes 38eae797
- 00a288f8 ["INT_ADD", "register:40f0:8", ["const:a288f8:8", "const:4:8"]]
- 00a288f8 ["CALL", null, ["callee:00481058:8"]]
+ 00a86788 ["INT_ADD", "register:40f0:8", ["const:a86788:8", "const:4:8"]]
+ 00a86788 ["CALL", null, ["callee:00481058:8"]]
- 00a288f8 bytes 32d6e897
+ 00a86788 bytes 34eae797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66432d7a2a77e726c494f3e81f9dbb6f"></a>

### [`00a28924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28924.md) → [`00a867b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a867b4.md) FUN_00a867b4

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2893c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28924.md#insn-00a2893c) · [`00a28948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28924.md#insn-00a28948) · [`00a28954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28924.md#insn-00a28954)
- 新版 [`00a867cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a867b4.md#insn-00a867cc) · [`00a867d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a867b4.md#insn-00a867d8) · [`00a867e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a867b4.md#insn-00a867e4)

~~~diff
- 00a2893c ["INT_ADD", "register:40f0:8", ["const:a2893c:8", "const:4:8"]]
- 00a2893c ["CALL", null, ["callee:00480704:8"]]
+ 00a867cc ["INT_ADD", "register:40f0:8", ["const:a867cc:8", "const:4:8"]]
+ 00a867cc ["CALL", null, ["callee:00480704:8"]]
- 00a2893c bytes ccd3e897
+ 00a867cc bytes cee7e797
- 00a28948 ["INT_ADD", "register:40f0:8", ["const:a28948:8", "const:4:8"]]
- 00a28948 ["CALL", null, ["callee:00480704:8"]]
+ 00a867d8 ["INT_ADD", "register:40f0:8", ["const:a867d8:8", "const:4:8"]]
+ 00a867d8 ["CALL", null, ["callee:00480704:8"]]
- 00a28948 bytes c9d3e897
+ 00a867d8 bytes cbe7e797
- 00a28954 ["INT_ADD", "register:40f0:8", ["const:a28954:8", "const:4:8"]]
- 00a28954 ["CALL", null, ["callee:00480704:8"]]
+ 00a867e4 ["INT_ADD", "register:40f0:8", ["const:a867e4:8", "const:4:8"]]
+ 00a867e4 ["CALL", null, ["callee:00480704:8"]]
- 00a28954 bytes c6d3e897
+ 00a867e4 bytes c8e7e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79e3ac59d824254f24c20dbeb15944de"></a>

### [`00a289b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a289b4.md) → [`00a86844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86844.md) FUN_00a86844

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a289c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a289b4.md#insn-00a289c8)
- 新版 [`00a86858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86844.md#insn-00a86858)

~~~diff
- 00a289c8 ["INT_ADD", "register:40f0:8", ["const:a289c8:8", "const:4:8"]]
- 00a289c8 ["CALL", null, ["callee:00480704:8"]]
+ 00a86858 ["INT_ADD", "register:40f0:8", ["const:a86858:8", "const:4:8"]]
+ 00a86858 ["CALL", null, ["callee:00480704:8"]]
- 00a289c8 bytes a9d3e897
+ 00a86858 bytes abe7e797
~~~


<a id="compare-0ff638713fae16047bc1b1e53426ccda"></a>

### [`00a28a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a00.md) → [`00a86890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86890.md) FUN_00a86890

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a00.md#insn-00a28a14)
- 新版 [`00a868a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86890.md#insn-00a868a4)

~~~diff
- 00a28a14 ["INT_ADD", "register:40f0:8", ["const:a28a14:8", "const:4:8"]]
- 00a28a14 ["CALL", null, ["callee:00480704:8"]]
+ 00a868a4 ["INT_ADD", "register:40f0:8", ["const:a868a4:8", "const:4:8"]]
+ 00a868a4 ["CALL", null, ["callee:00480704:8"]]
- 00a28a14 bytes 96d3e897
+ 00a868a4 bytes 98e7e797
~~~


<a id="compare-de0d5c7408ffda77518bad75a6f1afbf"></a>

### [`00a28a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a44.md) → [`00a868d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a868d4.md) FUN_00a868d4

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a44.md#insn-00a28a58)
- 新版 [`00a868e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a868d4.md#insn-00a868e8)

~~~diff
- 00a28a58 ["INT_ADD", "register:40f0:8", ["const:a28a58:8", "const:4:8"]]
- 00a28a58 ["CALL", null, ["callee:00480704:8"]]
+ 00a868e8 ["INT_ADD", "register:40f0:8", ["const:a868e8:8", "const:4:8"]]
+ 00a868e8 ["CALL", null, ["callee:00480704:8"]]
- 00a28a58 bytes 85d3e897
+ 00a868e8 bytes 87e7e797
~~~


<a id="compare-d200d7560afc8e4b5d405559f2ce615e"></a>

### [`00a28a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a80.md) → [`00a86910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86910.md) FUN_00a86910

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a80.md#insn-00a28a94)
- 新版 [`00a86924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86910.md#insn-00a86924)

~~~diff
- 00a28a94 ["INT_ADD", "register:40f0:8", ["const:a28a94:8", "const:4:8"]]
- 00a28a94 ["CALL", null, ["callee:00480704:8"]]
+ 00a86924 ["INT_ADD", "register:40f0:8", ["const:a86924:8", "const:4:8"]]
+ 00a86924 ["CALL", null, ["callee:00480704:8"]]
- 00a28a94 bytes 76d3e897
+ 00a86924 bytes 78e7e797
~~~


<a id="compare-209ba96413f2d9d6c7e254bdc40ed05f"></a>

### [`00a28ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ab8.md) → [`00a86948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86948.md) FUN_00a86948

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 1件 [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 1件 [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ab8.md#insn-00a28adc)
- 新版 [`00a8696c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86948.md#insn-00a8696c)

~~~diff
- 00a28adc ["INT_ADD", "register:40f0:8", ["const:a28adc:8", "const:4:8"]]
- 00a28adc ["CALL", null, ["callee:00481058:8"]]
+ 00a8696c ["INT_ADD", "register:40f0:8", ["const:a8696c:8", "const:4:8"]]
+ 00a8696c ["CALL", null, ["callee:00481058:8"]]
- 00a28adc bytes b9d5e897
+ 00a8696c bytes bbe9e797
~~~


<a id="compare-5730704eb51196da80a56d6c405cf4f4"></a>

### [`00a28afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28afc.md) → [`00a8698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a8698c.md) FUN_00a8698c

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28afc.md#insn-00a28b14) · [`00a28b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28afc.md#insn-00a28b30)
- 新版 [`00a869a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a8698c.md#insn-00a869a4) · [`00a869c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a8698c.md#insn-00a869c0)

~~~diff
- 00a28b14 ["INT_ADD", "register:40f0:8", ["const:a28b14:8", "const:4:8"]]
- 00a28b14 ["CALL", null, ["callee:00480704:8"]]
+ 00a869a4 ["INT_ADD", "register:40f0:8", ["const:a869a4:8", "const:4:8"]]
+ 00a869a4 ["CALL", null, ["callee:00480704:8"]]
- 00a28b14 bytes 56d3e897
+ 00a869a4 bytes 58e7e797
- 00a28b30 ["INT_ADD", "register:40f0:8", ["const:a28b30:8", "const:4:8"]]
- 00a28b30 ["CALL", null, ["callee:00480704:8"]]
+ 00a869c0 ["INT_ADD", "register:40f0:8", ["const:a869c0:8", "const:4:8"]]
+ 00a869c0 ["CALL", null, ["callee:00480704:8"]]
- 00a28b30 bytes 4fd3e897
+ 00a869c0 bytes 51e7e797
~~~


<a id="compare-54e9502123ce1c1b21458e307eb4f9fb"></a>

### [`00a28b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28b68.md) → [`00a869f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a869f8.md) FUN_00a869f8

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28b68.md#insn-00a28b7c)
- 新版 [`00a86a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a869f8.md#insn-00a86a0c)

~~~diff
- 00a28b7c ["INT_ADD", "register:40f0:8", ["const:a28b7c:8", "const:4:8"]]
- 00a28b7c ["CALL", null, ["callee:00480704:8"]]
+ 00a86a0c ["INT_ADD", "register:40f0:8", ["const:a86a0c:8", "const:4:8"]]
+ 00a86a0c ["CALL", null, ["callee:00480704:8"]]
- 00a28b7c bytes 3cd3e897
+ 00a86a0c bytes 3ee7e797
~~~


<a id="compare-84203dbe51d8397b20a0a5f4e208cecc"></a>

### [`00a28ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md) → [`00a86a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86a30.md) FUN_00a86a30

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 2件 [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md#insn-00a28bc8) · [`00a28c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md#insn-00a28c08) · [`00a28c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md#insn-00a28c18)
- 新版 [`00a86a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86a30.md#insn-00a86a58) · [`00a86a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86a30.md#insn-00a86a98) · [`00a86aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86a30.md#insn-00a86aa8)

~~~diff
- 00a28bc8 ["INT_ADD", "register:40f0:8", ["const:a28bc8:8", "const:4:8"]]
- 00a28bc8 ["CALL", null, ["callee:00480b50:8"]]
+ 00a86a58 ["INT_ADD", "register:40f0:8", ["const:a86a58:8", "const:4:8"]]
+ 00a86a58 ["CALL", null, ["callee:00480b50:8"]]
- 00a28bc8 bytes 3cd4e897
+ 00a86a58 bytes 3ee8e797
- 00a28c08 ["INT_ADD", "register:40f0:8", ["const:a28c08:8", "const:4:8"]]
- 00a28c08 ["CALL", null, ["callee:00480b50:8"]]
+ 00a86a98 ["INT_ADD", "register:40f0:8", ["const:a86a98:8", "const:4:8"]]
+ 00a86a98 ["CALL", null, ["callee:00480b50:8"]]
- 00a28c08 bytes 2cd4e897
+ 00a86a98 bytes 2ee8e797
- 00a28c18 ["INT_ADD", "register:40f0:8", ["const:a28c18:8", "const:4:8"]]
- 00a28c18 ["CALL", null, ["callee:00481058:8"]]
+ 00a86aa8 ["INT_ADD", "register:40f0:8", ["const:a86aa8:8", "const:4:8"]]
+ 00a86aa8 ["CALL", null, ["callee:00481058:8"]]
- 00a28c18 bytes 6ad5e897
+ 00a86aa8 bytes 6ce9e797
~~~


<a id="compare-2f0376d315d31b92c1e589797c56e22a"></a>

### [`00a28c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md) → [`00a86adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86adc.md) FUN_00a86adc

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md) [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md#insn-00a28c78) · [`00a28c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md#insn-00a28c98) · [`00a28cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md#insn-00a28cc0)
- 新版 [`00a86b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86adc.md#insn-00a86b08) · [`00a86b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86adc.md#insn-00a86b28) · [`00a86b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86adc.md#insn-00a86b50)

~~~diff
- 00a28c78 ["INT_ADD", "register:40f0:8", ["const:a28c78:8", "const:4:8"]]
- 00a28c78 ["CALL", null, ["callee:00480138:8"]]
+ 00a86b08 ["INT_ADD", "register:40f0:8", ["const:a86b08:8", "const:4:8"]]
+ 00a86b08 ["CALL", null, ["callee:00480138:8"]]
- 00a28c78 bytes 8ad1e897
+ 00a86b08 bytes 8ce5e797
- 00a28c98 ["INT_ADD", "register:40f0:8", ["const:a28c98:8", "const:4:8"]]
- 00a28c98 ["CALL", null, ["callee:0043bb64:8"]]
+ 00a86b28 ["INT_ADD", "register:40f0:8", ["const:a86b28:8", "const:4:8"]]
+ 00a86b28 ["CALL", null, ["callee:0043bb64:8"]]
- 00a28c98 bytes f3c0e797
+ 00a86b28 bytes 0fd4e697
- 00a28cc0 ["INT_ADD", "register:40f0:8", ["const:a28cc0:8", "const:4:8"]]
- 00a28cc0 ["CALL", null, ["callee:00480138:8"]]
+ 00a86b50 ["INT_ADD", "register:40f0:8", ["const:a86b50:8", "const:4:8"]]
+ 00a86b50 ["CALL", null, ["callee:00480138:8"]]
- 00a28cc0 bytes 78d1e897
+ 00a86b50 bytes 7ae5e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f884039ccb71489cfc371398272194ac"></a>

### [`00a28d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28d90.md) → [`00a86c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c20.md) FUN_00a86c20

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28d90.md#insn-00a28da4)
- 新版 [`00a86c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c20.md#insn-00a86c34)

~~~diff
- 00a28da4 ["INT_ADD", "register:40f0:8", ["const:a28da4:8", "const:4:8"]]
- 00a28da4 ["CALL", null, ["callee:00480704:8"]]
+ 00a86c34 ["INT_ADD", "register:40f0:8", ["const:a86c34:8", "const:4:8"]]
+ 00a86c34 ["CALL", null, ["callee:00480704:8"]]
- 00a28da4 bytes b2d2e897
+ 00a86c34 bytes b4e6e797
~~~


<a id="compare-85369613d6f5df49cb9cbad8a4b7dd9f"></a>

### [`00a290f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a290f0.md) → [`00a86f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86f80.md) FUN_00a86f80

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 1件 [`00a26e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26e20.md)
- 新版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 1件 [`00a84cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84cb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2910c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a290f0.md#insn-00a2910c)
- 新版 [`00a86f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86f80.md#insn-00a86f9c)

~~~diff
- 00a2910c ["INT_ADD", "register:40f0:8", ["const:a2910c:8", "const:4:8"]]
- 00a2910c ["CALL", null, ["callee:00a84cb0:8"]]
+ 00a86f9c ["INT_ADD", "register:40f0:8", ["const:a86f9c:8", "const:4:8"]]
+ 00a86f9c ["CALL", null, ["callee:00a84cb0:8"]]
- 00a2910c bytes 45f7ff97
+ 00a86f9c bytes 45f7ff97
~~~


<a id="compare-b51f23d02b8b897644661f22da36c45c"></a>

### [`00a29130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md) → [`00a86fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86fc0.md) FUN_00a86fc0

採用 · 移動量 `+0x5de90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a26e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26e20.md) [`00a2720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a27/00a2720c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a2924c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a2924c.md) [`00a293f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00a84cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84cb0.md) [`00a8509c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a85/00a8509c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00a870dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a870dc.md) [`00a87284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87284.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md#insn-00a2918c) · [`00a291b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md#insn-00a291b4) · [`00a291e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md#insn-00a291e0)
- 新版 [`00a8701c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86fc0.md#insn-00a8701c) · [`00a87044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86fc0.md#insn-00a87044) · [`00a87070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86fc0.md#insn-00a87070)

~~~diff
- 00a2918c ["INT_ADD", "register:40f0:8", ["const:a2918c:8", "const:4:8"]]
- 00a2918c ["CALL", null, ["callee:00a870dc:8"]]
+ 00a8701c ["INT_ADD", "register:40f0:8", ["const:a8701c:8", "const:4:8"]]
+ 00a8701c ["CALL", null, ["callee:00a870dc:8"]]
- 00a2918c bytes 30000094
+ 00a8701c bytes 30000094
- 00a291b4 ["INT_ADD", "register:40f0:8", ["const:a291b4:8", "const:4:8"]]
- 00a291b4 ["CALL", null, ["callee:00a87284:8"]]
+ 00a87044 ["INT_ADD", "register:40f0:8", ["const:a87044:8", "const:4:8"]]
+ 00a87044 ["CALL", null, ["callee:00a87284:8"]]
- 00a291b4 bytes 90000094
+ 00a87044 bytes 90000094
- 00a291e0 ["INT_ADD", "register:40f0:8", ["const:a291e0:8", "const:4:8"]]
- 00a291e0 ["CALL", null, ["callee:0043bb64:8"]]
+ 00a87070 ["INT_ADD", "register:40f0:8", ["const:a87070:8", "const:4:8"]]
+ 00a87070 ["CALL", null, ["callee:0043bb64:8"]]
- 00a291e0 bytes a1bfe797
+ 00a87070 bytes bdd2e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cefcf9fe0462d56c7b2a5fb918096fd"></a>

### [`00a293f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md) → [`00a87284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87284.md) FUN_00a87284

採用 · 移動量 `+0x5de90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a29130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md) · 呼出先 6件 [`00650784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650784.md) [`00a294e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a294e4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00a86fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86fc0.md) · 呼出先 6件 [`00676a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a64.md) [`00a87374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87374.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a29418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md#insn-00a29418) · [`00a29470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md#insn-00a29470) · [`00a29488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md#insn-00a29488)
- 新版 [`00a872a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87284.md#insn-00a872a8) · [`00a87300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87284.md#insn-00a87300) · [`00a87318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87284.md#insn-00a87318)

~~~diff
- 00a29418 ["INT_ADD", "register:40f0:8", ["const:a29418:8", "const:4:8"]]
- 00a29418 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a872a8 ["INT_ADD", "register:40f0:8", ["const:a872a8:8", "const:4:8"]]
+ 00a872a8 ["CALL", null, ["callee:00c57a90:8"]]
- 00a29418 bytes 0ac70694
+ 00a872a8 bytes fa410794
- 00a29470 ["INT_ADD", "register:40f0:8", ["const:a29470:8", "const:4:8"]]
- 00a29470 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a87300 ["INT_ADD", "register:40f0:8", ["const:a87300:8", "const:4:8"]]
+ 00a87300 ["CALL", null, ["callee:00c57a90:8"]]
- 00a29470 bytes f4c60694
+ 00a87300 bytes e4410794
- 00a29488 ["INT_ADD", "register:40f0:8", ["const:a29488:8", "const:4:8"]]
- 00a29488 ["CALL", null, ["callee:00c57c00:8"]]
+ 00a87318 ["INT_ADD", "register:40f0:8", ["const:a87318:8", "const:4:8"]]
+ 00a87318 ["CALL", null, ["callee:00c57c00:8"]]
- 00a29488 bytes 4ac70694
+ 00a87318 bytes 3a420794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d12c966728a4f49c5584f8a17dcaae73"></a>

### [`00a3a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md) → [`00a97f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a97/00a97f2c.md) FUN_00a97f2c

採用 · 移動量 `+0x5def4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a37f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37f10.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00882a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/00882a18.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a95e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a95e04.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008b5bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b5/008b5bb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md#insn-00a3a08c) · [`00a3a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md#insn-00a3a0a0) · [`00a3a0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md#insn-00a3a0d0)
- 新版 [`00a97f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a97/00a97f2c.md#insn-00a97f80) · [`00a97f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a97/00a97f2c.md#insn-00a97f94) · [`00a97fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a97/00a97f2c.md#insn-00a97fc4)

~~~diff
- 00a3a08c ["INT_ADD", "register:40f0:8", ["const:a3a08c:8", "const:4:8"]]
- 00a3a08c ["CALL", null, ["callee:0043bae0:8"]]
+ 00a97f80 ["INT_ADD", "register:40f0:8", ["const:a97f80:8", "const:4:8"]]
+ 00a97f80 ["CALL", null, ["callee:0043bae0:8"]]
- 00a3a08c bytes d57be797
+ 00a97f80 bytes d88ee697
- 00a3a0a0 ["INT_ADD", "register:40f0:8", ["const:a3a0a0:8", "const:4:8"]]
- 00a3a0a0 ["CALL", null, ["callee:0043bae0:8"]]
+ 00a97f94 ["INT_ADD", "register:40f0:8", ["const:a97f94:8", "const:4:8"]]
+ 00a97f94 ["CALL", null, ["callee:0043bae0:8"]]
- 00a3a0a0 bytes d07be797
+ 00a97f94 bytes d38ee697
- 00a3a0d0 ["INT_ADD", "register:40f0:8", ["const:a3a0d0:8", "const:4:8"]]
- 00a3a0d0 ["CALL", null, ["callee:008b5bb8:8"]]
+ 00a97fc4 ["INT_ADD", "register:40f0:8", ["const:a97fc4:8", "const:4:8"]]
+ 00a97fc4 ["CALL", null, ["callee:008b5bb8:8"]]
- 00a3a0d0 bytes 5222f997
+ 00a97fc4 bytes fd76f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bdece2e5de6c896f5c03d77a3b09b97"></a>

### [`00a3a328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a328.md) → [`00a9821c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a98/00a9821c.md) FUN_00a9821c

採用 · 移動量 `+0x5def4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a3a160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a160.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a98054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a98/00a98054.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a328.md#insn-00a3a338)
- 新版 [`00a9822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a98/00a9821c.md#insn-00a9822c)

~~~diff
- 00a3a338 ["INT_ADD", "register:40f0:8", ["const:a3a338:8", "const:4:8"]]
- 00a3a338 ["CALL", null, ["callee:00a98054:8"]]
+ 00a9822c ["INT_ADD", "register:40f0:8", ["const:a9822c:8", "const:4:8"]]
+ 00a9822c ["CALL", null, ["callee:00a98054:8"]]
- 00a3a338 bytes 8affff97
+ 00a9822c bytes 8affff97
~~~


<a id="compare-1a6f4a49ceb257fbb8d22bc173af0cd3"></a>

### [`00a41098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md) → [`00a9ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9e/00a9ef9c.md) FUN_00a9ef9c

採用 · 移動量 `+0x5df04` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00739a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00739/00739a10.md) [`00761d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md) [`00a3d70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d70c.md) [`00a41924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41924.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00763d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763d18.md) [`0078c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md) [`00a9b600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9b600.md) [`00a9f828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f828.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4118c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md#insn-00a4118c) · [`00a411b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md#insn-00a411b4) · [`00a411c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md#insn-00a411c0)
- 新版 [`00a9f090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9e/00a9ef9c.md#insn-00a9f090) · [`00a9f0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9e/00a9ef9c.md#insn-00a9f0b8) · [`00a9f0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9e/00a9ef9c.md#insn-00a9f0c4)

~~~diff
- 00a4118c ["INT_ADD", "register:40f0:8", ["const:a4118c:8", "const:4:8"]]
- 00a4118c ["CALL", null, ["callee:00c57a90:8"]]
+ 00a9f090 ["INT_ADD", "register:40f0:8", ["const:a9f090:8", "const:4:8"]]
+ 00a9f090 ["CALL", null, ["callee:00c57a90:8"]]
- 00a4118c bytes ad670694
+ 00a9f090 bytes 80e20694
- 00a411b4 ["INT_ADD", "register:40f0:8", ["const:a411b4:8", "const:4:8"]]
- 00a411b4 ["CALL", null, ["callee:00c57c00:8"]]
+ 00a9f0b8 ["INT_ADD", "register:40f0:8", ["const:a9f0b8:8", "const:4:8"]]
+ 00a9f0b8 ["CALL", null, ["callee:00c57c00:8"]]
- 00a411b4 bytes ff670694
+ 00a9f0b8 bytes d2e20694
- 00a411c0 ["INT_ADD", "register:40f0:8", ["const:a411c0:8", "const:4:8"]]
- 00a411c0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a9f0c4 ["INT_ADD", "register:40f0:8", ["const:a9f0c4:8", "const:4:8"]]
+ 00a9f0c4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a411c0 bytes a8670694
+ 00a9f0c4 bytes 7be20694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-593f2740885919dafb4b9f7e677193c1"></a>

### [`00a43c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c10.md) → [`00aa1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1b14.md) FUN_00aa1b14

採用 · 移動量 `+0x5df04` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a43c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c10.md#insn-00a43c3c)
- 新版 [`00aa1b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1b14.md#insn-00aa1b40)

~~~diff
- 00a43c3c ["INT_ADD", "register:40f0:8", ["const:a43c3c:8", "const:4:8"]]
- 00a43c3c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00aa1b40 ["INT_ADD", "register:40f0:8", ["const:aa1b40:8", "const:4:8"]]
+ 00aa1b40 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a43c3c bytes 095d0694
+ 00aa1b40 bytes dcd70694
~~~


<a id="compare-7c545081ee04569b400d23fa6acb01af"></a>

### [`00a4fd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fd84.md) → [`00aadda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadda8.md) FUN_00aadda8

採用 · 移動量 `+0x5e024` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4fdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fd84.md#insn-00a4fdd0)
- 新版 [`00aaddf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadda8.md#insn-00aaddf4)

~~~diff
- 00a4fdd0 ["INT_ADD", "register:40f0:8", ["const:a4fdd0:8", "const:4:8"]]
- 00a4fdd0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00aaddf4 ["INT_ADD", "register:40f0:8", ["const:aaddf4:8", "const:4:8"]]
+ 00aaddf4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a4fdd0 bytes a42c0694
+ 00aaddf4 bytes 2fa70694
~~~


<a id="compare-48ab7177b6994fe19881b663d9e563f1"></a>

### [`00a53498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53498.md) → [`00ab153c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab153c.md) FUN_00ab153c

採用 · 移動量 `+0x5e0a4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00ab1860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1860.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a534c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53498.md#insn-00a534c4)
- 新版 [`00ab1568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab153c.md#insn-00ab1568)

~~~diff
- 00a534c4 ["INT_ADD", "register:40f0:8", ["const:a534c4:8", "const:4:8"]]
- 00a534c4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00ab1568 ["INT_ADD", "register:40f0:8", ["const:ab1568:8", "const:4:8"]]
+ 00ab1568 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a534c4 bytes e71e0694
+ 00ab1568 bytes 52990694
~~~


<a id="compare-8ed2bb70674400b77000c26d0b9aa8dc"></a>

### [`00a534f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md) → [`00ab159c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab159c.md) FUN_00ab159c

採用 · 移動量 `+0x5e0a4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a52754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52754.md) [`00a52948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52948.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a53614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53614.md) [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00ab07f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab07f8.md) [`00ab09ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab09ec.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00ab16b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab16b8.md) [`00ab1860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1860.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a53554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md#insn-00a53554) · [`00a5357c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md#insn-00a5357c) · [`00a535a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md#insn-00a535a8)
- 新版 [`00ab15f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab159c.md#insn-00ab15f8) · [`00ab1620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab159c.md#insn-00ab1620) · [`00ab164c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab159c.md#insn-00ab164c)

~~~diff
- 00a53554 ["INT_ADD", "register:40f0:8", ["const:a53554:8", "const:4:8"]]
- 00a53554 ["CALL", null, ["callee:00ab16b8:8"]]
+ 00ab15f8 ["INT_ADD", "register:40f0:8", ["const:ab15f8:8", "const:4:8"]]
+ 00ab15f8 ["CALL", null, ["callee:00ab16b8:8"]]
- 00a53554 bytes 30000094
+ 00ab15f8 bytes 30000094
- 00a5357c ["INT_ADD", "register:40f0:8", ["const:a5357c:8", "const:4:8"]]
- 00a5357c ["CALL", null, ["callee:00ab1860:8"]]
+ 00ab1620 ["INT_ADD", "register:40f0:8", ["const:ab1620:8", "const:4:8"]]
+ 00ab1620 ["CALL", null, ["callee:00ab1860:8"]]
- 00a5357c bytes 90000094
+ 00ab1620 bytes 90000094
- 00a535a8 ["INT_ADD", "register:40f0:8", ["const:a535a8:8", "const:4:8"]]
- 00a535a8 ["CALL", null, ["callee:0043bb64:8"]]
+ 00ab164c ["INT_ADD", "register:40f0:8", ["const:ab164c:8", "const:4:8"]]
+ 00ab164c ["CALL", null, ["callee:0043bb64:8"]]
- 00a535a8 bytes af16e797
+ 00ab164c bytes 4629e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4bb9742bd2573e8dda52719803b675"></a>

### [`00a5c5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5ac.md) → [`00aba564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba564.md) FUN_00aba564

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5c5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5ac.md#insn-00a5c5c4) · [`00a5c5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5ac.md#insn-00a5c5d0)
- 新版 [`00aba57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba564.md#insn-00aba57c) · [`00aba588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba564.md#insn-00aba588)

~~~diff
- 00a5c5c4 ["INT_ADD", "register:40f0:8", ["const:a5c5c4:8", "const:4:8"]]
- 00a5c5c4 ["CALL", null, ["callee:004803b0:8"]]
+ 00aba57c ["INT_ADD", "register:40f0:8", ["const:aba57c:8", "const:4:8"]]
+ 00aba57c ["CALL", null, ["callee:004803b0:8"]]
- 00a5c5c4 bytes d503e897
+ 00aba57c bytes 8d17e797
- 00a5c5d0 ["INT_ADD", "register:40f0:8", ["const:a5c5d0:8", "const:4:8"]]
- 00a5c5d0 ["CALL", null, ["callee:004803b0:8"]]
+ 00aba588 ["INT_ADD", "register:40f0:8", ["const:aba588:8", "const:4:8"]]
+ 00aba588 ["CALL", null, ["callee:004803b0:8"]]
- 00a5c5d0 bytes d203e897
+ 00aba588 bytes 8a17e797
~~~


<a id="compare-8de44a157e4cf640e59a0b7ef08ec4b3"></a>

### [`00a5c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5e4.md) → [`00aba59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba59c.md) FUN_00aba59c

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5c604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5e4.md#insn-00a5c604)
- 新版 [`00aba5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba59c.md#insn-00aba5bc)

~~~diff
- 00a5c604 ["INT_ADD", "register:40f0:8", ["const:a5c604:8", "const:4:8"]]
- 00a5c604 ["CALL", null, ["callee:00480de8:8"]]
+ 00aba5bc ["INT_ADD", "register:40f0:8", ["const:aba5bc:8", "const:4:8"]]
+ 00aba5bc ["CALL", null, ["callee:00480de8:8"]]
- 00a5c604 bytes 5306e897
+ 00aba5bc bytes 0b1ae797
~~~


<a id="compare-edc2129c97c67f271ea235212d1795e3"></a>

### [`00a5f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f0e4.md) → [`00abd09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd09c.md) FUN_00abd09c

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00704f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704f50.md) [`00705000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00705/00705000.md) [`00706234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706234.md) [`007072cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007072cc.md) [`007073e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007073e8.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 5件 [`0072f050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f050.md) [`0072f100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f100.md) [`00730334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md) [`007313cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007313cc.md) [`007314e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007314e8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5f104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f0e4.md#insn-00a5f104)
- 新版 [`00abd0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd09c.md#insn-00abd0bc)

~~~diff
- 00a5f104 ["INT_ADD", "register:40f0:8", ["const:a5f104:8", "const:4:8"]]
- 00a5f104 ["CALL", null, ["callee:00c58050:8"]]
+ 00abd0bc ["INT_ADD", "register:40f0:8", ["const:abd0bc:8", "const:4:8"]]
+ 00abd0bc ["CALL", null, ["callee:00c58050:8"]]
- 00a5f104 bytes 3ff10594
+ 00abd0bc bytes e56b0694
~~~


<a id="compare-1837511e0a39ad9254c0dd433abe5e59"></a>

### [`00a61450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a61450.md) → [`00abf408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf408.md) FUN_00abf408

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0089f868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089f/0089f868.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a8e58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e58c.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 3件 [`008d3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) [`00aed9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed9b8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6148c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a61450.md#insn-00a6148c)
- 新版 [`00abf444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf408.md#insn-00abf444)

~~~diff
- 00a6148c ["INT_ADD", "register:40f0:8", ["const:a6148c:8", "const:4:8"]]
- 00a6148c ["CALL", null, ["callee:00c58050:8"]]
+ 00abf444 ["INT_ADD", "register:40f0:8", ["const:abf444:8", "const:4:8"]]
+ 00abf444 ["CALL", null, ["callee:00c58050:8"]]
- 00a6148c bytes 5de80594
+ 00abf444 bytes 03630694
~~~


<a id="compare-e10c14584deb977a234b5df9c2f71070"></a>

### [`00a69974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69974.md) → [`00ac7908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7908.md) FUN_00ac7908

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`0089dc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089dc0c.md) · 呼出先 0件 
- 新版 呼出元 11件 [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`008d1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1aa4.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a699c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69974.md#insn-00a699c8)
- 新版 [`00ac795c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7908.md#insn-00ac795c)

~~~diff
- 00a699c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a699c8 ["INT_ADD", "register:40f0:8", ["const:a699c8:8", "const:4:8"]]
- 00a699c8 ["CALLIND", null, ["register:0:8"]]
+ 00ac795c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac795c ["INT_ADD", "register:40f0:8", ["const:ac795c:8", "const:4:8"]]
+ 00ac795c ["CALLIND", null, ["register:0:8"]]
- 00a699c8 bytes 00013fd6
+ 00ac795c bytes 00013fd6
~~~


<a id="compare-a7b3be450521870161f8e8607b8f2a1e"></a>

### [`00a6ced8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md) → [`00acae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acae6c.md) FUN_00acae6c

採用 · 移動量 `+0x5df94` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a6a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md) [`00a6b2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b2a8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00ac87ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md) [`00ac923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac923c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6cf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md#insn-00a6cf44) · [`00a6cf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md#insn-00a6cf54) · [`00a6cf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md#insn-00a6cf74)
- 新版 [`00acaed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acae6c.md#insn-00acaed8) · [`00acaee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acae6c.md#insn-00acaee8) · [`00acaf08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acae6c.md#insn-00acaf08)

~~~diff
- 00a6cf44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6cf44 ["INT_ADD", "register:40f0:8", ["const:a6cf44:8", "const:4:8"]]
- 00a6cf44 ["CALLIND", null, ["register:0:8"]]
+ 00acaed8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acaed8 ["INT_ADD", "register:40f0:8", ["const:acaed8:8", "const:4:8"]]
+ 00acaed8 ["CALLIND", null, ["register:0:8"]]
- 00a6cf44 bytes 00013fd6
+ 00acaed8 bytes 00013fd6
- 00a6cf54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6cf54 ["INT_ADD", "register:40f0:8", ["const:a6cf54:8", "const:4:8"]]
- 00a6cf54 ["CALLIND", null, ["register:0:8"]]
+ 00acaee8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acaee8 ["INT_ADD", "register:40f0:8", ["const:acaee8:8", "const:4:8"]]
+ 00acaee8 ["CALLIND", null, ["register:0:8"]]
- 00a6cf54 bytes 00013fd6
+ 00acaee8 bytes 00013fd6
- 00a6cf74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6cf74 ["INT_ADD", "register:40f0:8", ["const:a6cf74:8", "const:4:8"]]
- 00a6cf74 ["CALLIND", null, ["register:0:8"]]
+ 00acaf08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acaf08 ["INT_ADD", "register:40f0:8", ["const:acaf08:8", "const:4:8"]]
+ 00acaf08 ["CALLIND", null, ["register:0:8"]]
- 00a6cf74 bytes 00013fd6
+ 00acaf08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c3267629cb5c13dcced991c0c43020e"></a>

### [`00a6d9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md) → [`00acb960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb960.md) FUN_00acb960

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00900f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900f40.md) · 呼出先 4件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00935974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935974.md) · 呼出先 4件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6da2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md#insn-00a6da2c) · [`00a6da40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md#insn-00a6da40) · [`00a6da50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md#insn-00a6da50)
- 新版 [`00acb9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb960.md#insn-00acb9c0) · [`00acb9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb960.md#insn-00acb9d4) · [`00acb9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb960.md#insn-00acb9e4)

~~~diff
- 00a6da2c ["INT_ADD", "register:40f0:8", ["const:a6da2c:8", "const:4:8"]]
- 00a6da2c ["CALL", null, ["callee:00c538b0:8"]]
+ 00acb9c0 ["INT_ADD", "register:40f0:8", ["const:acb9c0:8", "const:4:8"]]
+ 00acb9c0 ["CALL", null, ["callee:00c538b0:8"]]
- 00a6da2c bytes 0da50594
+ 00acb9c0 bytes bc1f0694
- 00a6da40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6da40 ["INT_ADD", "register:40f0:8", ["const:a6da40:8", "const:4:8"]]
- 00a6da40 ["CALLIND", null, ["register:0:8"]]
+ 00acb9d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acb9d4 ["INT_ADD", "register:40f0:8", ["const:acb9d4:8", "const:4:8"]]
+ 00acb9d4 ["CALLIND", null, ["register:0:8"]]
- 00a6da40 bytes 00013fd6
+ 00acb9d4 bytes 00013fd6
- 00a6da50 ["INT_ADD", "register:40f0:8", ["const:a6da50:8", "const:4:8"]]
- 00a6da50 ["CALL", null, ["callee:00c538e0:8"]]
+ 00acb9e4 ["INT_ADD", "register:40f0:8", ["const:acb9e4:8", "const:4:8"]]
+ 00acb9e4 ["CALL", null, ["callee:00c538e0:8"]]
- 00a6da50 bytes 10a50594
+ 00acb9e4 bytes bf1f0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5612e52d8a59ac09277383013ad7ab"></a>

### [`00a6dac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md) → [`00acba58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acba58.md) FUN_00acba58

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6db24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md#insn-00a6db24) · [`00a6db38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md#insn-00a6db38) · [`00a6db48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md#insn-00a6db48)
- 新版 [`00acbab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acba58.md#insn-00acbab8) · [`00acbacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acba58.md#insn-00acbacc) · [`00acbadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acba58.md#insn-00acbadc)

~~~diff
- 00a6db24 ["INT_ADD", "register:40f0:8", ["const:a6db24:8", "const:4:8"]]
- 00a6db24 ["CALL", null, ["callee:00c538b0:8"]]
+ 00acbab8 ["INT_ADD", "register:40f0:8", ["const:acbab8:8", "const:4:8"]]
+ 00acbab8 ["CALL", null, ["callee:00c538b0:8"]]
- 00a6db24 bytes cfa40594
+ 00acbab8 bytes 7e1f0694
- 00a6db38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6db38 ["INT_ADD", "register:40f0:8", ["const:a6db38:8", "const:4:8"]]
- 00a6db38 ["CALLIND", null, ["register:0:8"]]
+ 00acbacc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acbacc ["INT_ADD", "register:40f0:8", ["const:acbacc:8", "const:4:8"]]
+ 00acbacc ["CALLIND", null, ["register:0:8"]]
- 00a6db38 bytes 00013fd6
+ 00acbacc bytes 00013fd6
- 00a6db48 ["INT_ADD", "register:40f0:8", ["const:a6db48:8", "const:4:8"]]
- 00a6db48 ["CALL", null, ["callee:00c538e0:8"]]
+ 00acbadc ["INT_ADD", "register:40f0:8", ["const:acbadc:8", "const:4:8"]]
+ 00acbadc ["CALL", null, ["callee:00c538e0:8"]]
- 00a6db48 bytes d2a40594
+ 00acbadc bytes 811f0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97cc5b80ebdad1c372866650c458361f"></a>

### [`00a6dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md) → [`00acbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md) FUN_00acbd30

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00983a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983a68.md) [`00a6dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md) · 呼出先 5件 [`00a6dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`009b9548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9548.md) [`00acbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md) · 呼出先 5件 [`00acbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6ddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md#insn-00a6ddf8) · [`00a6de04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md#insn-00a6de04) · [`00a6de14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md#insn-00a6de14)
- 新版 [`00acbd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md#insn-00acbd8c) · [`00acbd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md#insn-00acbd98) · [`00acbda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md#insn-00acbda8)

~~~diff
- 00a6ddf8 ["INT_ADD", "register:40f0:8", ["const:a6ddf8:8", "const:4:8"]]
- 00a6ddf8 ["CALL", null, ["callee:00c538b0:8"]]
+ 00acbd8c ["INT_ADD", "register:40f0:8", ["const:acbd8c:8", "const:4:8"]]
+ 00acbd8c ["CALL", null, ["callee:00c538b0:8"]]
- 00a6ddf8 bytes 1aa40594
+ 00acbd8c bytes c91e0694
- 00a6de04 ["INT_ADD", "register:40f0:8", ["const:a6de04:8", "const:4:8"]]
- 00a6de04 ["CALL", null, ["local:b0:8"]]
+ 00acbd98 ["INT_ADD", "register:40f0:8", ["const:acbd98:8", "const:4:8"]]
+ 00acbd98 ["CALL", null, ["local:b0:8"]]
- 00a6de04 bytes e6ffff97
+ 00acbd98 bytes e6ffff97
- 00a6de14 ["INT_ADD", "register:40f0:8", ["const:a6de14:8", "const:4:8"]]
- 00a6de14 ["CALL", null, ["callee:00c538e0:8"]]
+ 00acbda8 ["INT_ADD", "register:40f0:8", ["const:acbda8:8", "const:4:8"]]
+ 00acbda8 ["CALL", null, ["callee:00c538e0:8"]]
- 00a6de14 bytes 1fa40594
+ 00acbda8 bytes ce1e0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-851cb12d642b8958945865c7e02aa1c5"></a>

### [`00a6de88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6de88.md) → [`00acbe1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbe1c.md) FUN_00acbe1c

採用 · 移動量 `+0x5df94` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00acb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6de88.md#insn-00a6dea4)
- 新版 [`00acbe38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbe1c.md#insn-00acbe38)

~~~diff
- 00a6dea4 ["INT_ADD", "register:40f0:8", ["const:a6dea4:8", "const:4:8"]]
- 00a6dea4 ["CALL", null, ["callee:00acb88c:8"]]
+ 00acbe38 ["INT_ADD", "register:40f0:8", ["const:acbe38:8", "const:4:8"]]
+ 00acbe38 ["CALL", null, ["callee:00acb88c:8"]]
- 00a6dea4 bytes 95feff97
+ 00acbe38 bytes 95feff97
~~~


<a id="compare-e0c99f67cc80cb14c82fa0c19097556d"></a>

### [`00a6dee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dee8.md) → [`00acbe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbe7c.md) FUN_00acbe7c

採用 · 移動量 `+0x5df94` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a6dbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dbbc.md) · 呼出先 2件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00acbb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md) · 呼出先 2件 [`00acb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6df00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dee8.md#insn-00a6df00)
- 新版 [`00acbe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbe7c.md#insn-00acbe94)

~~~diff
- 00a6df00 ["INT_ADD", "register:40f0:8", ["const:a6df00:8", "const:4:8"]]
- 00a6df00 ["CALL", null, ["callee:00acb88c:8"]]
+ 00acbe94 ["INT_ADD", "register:40f0:8", ["const:acbe94:8", "const:4:8"]]
+ 00acbe94 ["CALL", null, ["callee:00acb88c:8"]]
- 00a6df00 bytes 7efeff97
+ 00acbe94 bytes 7efeff97
~~~


<a id="compare-33c0b47e4191a0178ee7179f55982b2e"></a>

### [`00a8cd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cd88.md) → [`00aec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec104.md) FUN_00aec104

採用 · 移動量 `+0x5f37c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a8cb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cb08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00aebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a8cd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cd88.md#insn-00a8cd98)
- 新版 [`00aec114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec104.md#insn-00aec114)

~~~diff
- 00a8cd98 ["INT_ADD", "register:40f0:8", ["const:a8cd98:8", "const:4:8"]]
- 00a8cd98 ["CALL", null, ["callee:00aebe84:8"]]
+ 00aec114 ["INT_ADD", "register:40f0:8", ["const:aec114:8", "const:4:8"]]
+ 00aec114 ["CALL", null, ["callee:00aebe84:8"]]
- 00a8cd98 bytes 5cffff97
+ 00aec114 bytes 5cffff97
~~~


<a id="compare-e2300daf2d25f0775a75cb50894fa9e8"></a>

### [`00aa9764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9764.md) → [`00b091dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md) FUN_00b091dc

採用 · 移動量 `+0x5fa78` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 2件 [`008387ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008387ec.md) [`00838880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838880.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`0086a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md) [`0086a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa9780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9764.md#insn-00aa9780) · [`00aa979c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9764.md#insn-00aa979c)
- 新版 [`00b091f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md#insn-00b091f8) · [`00b09214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md#insn-00b09214)

~~~diff
- 00aa9780 ["INT_ADD", "register:40f0:8", ["const:aa9780:8", "const:4:8"]]
- 00aa9780 ["CALL", null, ["callee:0086a7f8:8"]]
+ 00b091f8 ["INT_ADD", "register:40f0:8", ["const:b091f8:8", "const:4:8"]]
+ 00b091f8 ["CALL", null, ["callee:0086a7f8:8"]]
- 00aa9780 bytes 403cf697
+ 00b091f8 bytes 8085f597
- 00aa979c ["INT_ADD", "register:40f0:8", ["const:aa979c:8", "const:4:8"]]
- 00aa979c ["CALL", null, ["callee:0086a764:8"]]
+ 00b09214 ["INT_ADD", "register:40f0:8", ["const:b09214:8", "const:4:8"]]
+ 00b09214 ["CALL", null, ["callee:0086a764:8"]]
- 00aa979c bytes 143cf697
+ 00b09214 bytes 5485f597
~~~


<a id="compare-874af1b43c76d5df1d6cde347f0cc1c4"></a>

### [`00aa9ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md) → [`00b09a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md) FUN_00b09a84

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 3件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaa020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md#insn-00aaa020) · [`00aaa03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md#insn-00aaa03c) · [`00aaa070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md#insn-00aaa070)
- 新版 [`00b09ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md#insn-00b09ab0) · [`00b09acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md#insn-00b09acc) · [`00b09b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md#insn-00b09b00)

~~~diff
- 00aaa020 ["INT_ADD", "register:40f0:8", ["const:aaa020:8", "const:4:8"]]
- 00aaa020 ["CALL", null, ["callee:00480b50:8"]]
+ 00b09ab0 ["INT_ADD", "register:40f0:8", ["const:b09ab0:8", "const:4:8"]]
+ 00b09ab0 ["CALL", null, ["callee:00480b50:8"]]
- 00aaa020 bytes 26cfe697
+ 00b09ab0 bytes 28dce597
- 00aaa03c ["INT_ADD", "register:40f0:8", ["const:aaa03c:8", "const:4:8"]]
- 00aaa03c ["CALL", null, ["callee:00480b50:8"]]
+ 00b09acc ["INT_ADD", "register:40f0:8", ["const:b09acc:8", "const:4:8"]]
+ 00b09acc ["CALL", null, ["callee:00480b50:8"]]
- 00aaa03c bytes 1fcfe697
+ 00b09acc bytes 21dce597
- 00aaa070 ["INT_ADD", "register:40f0:8", ["const:aaa070:8", "const:4:8"]]
- 00aaa070 ["CALL", null, ["callee:00480ba8:8"]]
+ 00b09b00 ["INT_ADD", "register:40f0:8", ["const:b09b00:8", "const:4:8"]]
+ 00b09b00 ["CALL", null, ["callee:00480ba8:8"]]
- 00aaa070 bytes 28cfe697
+ 00b09b00 bytes 2adce597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58bbff65914774f49b0f6d2fe3404a82"></a>

### [`00aaae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaae5c.md) → [`00b0a8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a8ec.md) FUN_00b0a8ec

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) [`00a7840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a7840c.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a80570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a80/00a80570.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 8件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00adee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ade/00adee94.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaae7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaae5c.md#insn-00aaae7c)
- 新版 [`00b0a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a8ec.md#insn-00b0a90c)

~~~diff
- 00aaae7c ["INT_ADD", "register:40f0:8", ["const:aaae7c:8", "const:4:8"]]
- 00aaae7c ["CALL", null, ["callee:00c58050:8"]]
+ 00b0a90c ["INT_ADD", "register:40f0:8", ["const:b0a90c:8", "const:4:8"]]
+ 00b0a90c ["CALL", null, ["callee:00c58050:8"]]
- 00aaae7c bytes e1c10494
+ 00b0a90c bytes d1350594
~~~


<a id="compare-c268622534bf1d7865eba1df507da371"></a>

### [`00aac964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md) → [`00b0c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md) FUN_00b0c3f4

採用 · 移動量 `+0x5fa90` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aa9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9850.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aacb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00b092e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b0c600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c600.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md#insn-00aaca10) · [`00aaca54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md#insn-00aaca54) · [`00aaca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md#insn-00aaca98)
- 新版 [`00b0c4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md#insn-00b0c4a0) · [`00b0c4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md#insn-00b0c4e4) · [`00b0c528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md#insn-00b0c528)

~~~diff
- 00aaca10 ["INT_ADD", "register:40f0:8", ["const:aaca10:8", "const:4:8"]]
- 00aaca10 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b0c4a0 ["INT_ADD", "register:40f0:8", ["const:b0c4a0:8", "const:4:8"]]
+ 00b0c4a0 ["CALL", null, ["callee:00c57a90:8"]]
- 00aaca10 bytes 8cb90494
+ 00b0c4a0 bytes 7c2d0594
- 00aaca54 ["INT_ADD", "register:40f0:8", ["const:aaca54:8", "const:4:8"]]
- 00aaca54 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b0c4e4 ["INT_ADD", "register:40f0:8", ["const:b0c4e4:8", "const:4:8"]]
+ 00b0c4e4 ["CALL", null, ["callee:00c57c90:8"]]
- 00aaca54 bytes fbb90494
+ 00b0c4e4 bytes eb2d0594
- 00aaca98 ["INT_ADD", "register:40f0:8", ["const:aaca98:8", "const:4:8"]]
- 00aaca98 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b0c528 ["INT_ADD", "register:40f0:8", ["const:b0c528:8", "const:4:8"]]
+ 00b0c528 ["CALL", null, ["callee:00c57c90:8"]]
- 00aaca98 bytes eab90494
+ 00b0c528 bytes da2d0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5ff3b61288b3bbda5fcd2ee29d4cb23"></a>

### [`00aacb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md) → [`00b0c628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md) FUN_00b0c628

採用 · 移動量 `+0x5fa90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aaafe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aacb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b0aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b0c600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c600.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aacc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md#insn-00aacc24) · [`00aaccdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md#insn-00aaccdc) · [`00aaccf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md#insn-00aaccf8)
- 新版 [`00b0c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md#insn-00b0c6b4) · [`00b0c76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md#insn-00b0c76c) · [`00b0c788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md#insn-00b0c788)

~~~diff
- 00aacc24 ["INT_ADD", "register:40f0:8", ["const:aacc24:8", "const:4:8"]]
- 00aacc24 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b0c6b4 ["INT_ADD", "register:40f0:8", ["const:b0c6b4:8", "const:4:8"]]
+ 00b0c6b4 ["CALL", null, ["callee:00c57a90:8"]]
- 00aacc24 bytes 07b90494
+ 00b0c6b4 bytes f72c0594
- 00aaccdc ["INT_ADD", "register:40f0:8", ["const:aaccdc:8", "const:4:8"]]
- 00aaccdc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b0c76c ["INT_ADD", "register:40f0:8", ["const:b0c76c:8", "const:4:8"]]
+ 00b0c76c ["CALL", null, ["callee:00c57ab0:8"]]
- 00aaccdc bytes e1b80494
+ 00b0c76c bytes d12c0594
- 00aaccf8 ["INT_ADD", "register:40f0:8", ["const:aaccf8:8", "const:4:8"]]
- 00aaccf8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b0c788 ["INT_ADD", "register:40f0:8", ["const:b0c788:8", "const:4:8"]]
+ 00b0c788 ["CALL", null, ["callee:00c57ab0:8"]]
- 00aaccf8 bytes dab80494
+ 00b0c788 bytes ca2c0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be935cae2bfc2b5b509a70e51ceefb5"></a>

### [`00aadbe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md) → [`00b0d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md) FUN_00b0d678

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aac39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b0be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0be2c.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aadc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md#insn-00aadc50) · [`00aadc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md#insn-00aadc8c) · [`00aadc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md#insn-00aadc9c)
- 新版 [`00b0d6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md#insn-00b0d6e0) · [`00b0d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md#insn-00b0d71c) · [`00b0d72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md#insn-00b0d72c)

~~~diff
- 00aadc50 ["INT_ADD", "register:40f0:8", ["const:aadc50:8", "const:4:8"]]
- 00aadc50 ["CALL", null, ["callee:004945d0:8"]]
+ 00b0d6e0 ["INT_ADD", "register:40f0:8", ["const:b0d6e0:8", "const:4:8"]]
+ 00b0d6e0 ["CALL", null, ["callee:004945d0:8"]]
- 00aadc50 bytes ba0ee797
+ 00b0d6e0 bytes bc1be697
- 00aadc8c ["INT_ADD", "register:40f0:8", ["const:aadc8c:8", "const:4:8"]]
- 00aadc8c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b0d71c ["INT_ADD", "register:40f0:8", ["const:b0d71c:8", "const:4:8"]]
+ 00b0d71c ["CALL", null, ["callee:00c57ab0:8"]]
- 00aadc8c bytes f5b40494
+ 00b0d71c bytes e5280594
- 00aadc9c ["INT_ADD", "register:40f0:8", ["const:aadc9c:8", "const:4:8"]]
- 00aadc9c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b0d72c ["INT_ADD", "register:40f0:8", ["const:b0d72c:8", "const:4:8"]]
+ 00b0d72c ["CALL", null, ["callee:00c57ab0:8"]]
- 00aadc9c bytes f1b40494
+ 00b0d72c bytes e1280594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c0a8d7c2d587711323612c12719e8f7"></a>

### [`00aaef04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md) → [`00b0e994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md) FUN_00b0e994

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 2件 [`0045d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 2件 [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaef24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md#insn-00aaef24) · [`00aaef30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md#insn-00aaef30) · [`00aaef3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md#insn-00aaef3c)
- 新版 [`00b0e9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md#insn-00b0e9b4) · [`00b0e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md#insn-00b0e9c0) · [`00b0e9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md#insn-00b0e9cc)

~~~diff
- 00aaef24 ["INT_ADD", "register:40f0:8", ["const:aaef24:8", "const:4:8"]]
- 00aaef24 ["CALL", null, ["callee:004803b0:8"]]
+ 00b0e9b4 ["INT_ADD", "register:40f0:8", ["const:b0e9b4:8", "const:4:8"]]
+ 00b0e9b4 ["CALL", null, ["callee:004803b0:8"]]
- 00aaef24 bytes 7db9e697
+ 00b0e9b4 bytes 7fc6e597
- 00aaef30 ["INT_ADD", "register:40f0:8", ["const:aaef30:8", "const:4:8"]]
- 00aaef30 ["CALL", null, ["callee:004803b0:8"]]
+ 00b0e9c0 ["INT_ADD", "register:40f0:8", ["const:b0e9c0:8", "const:4:8"]]
+ 00b0e9c0 ["CALL", null, ["callee:004803b0:8"]]
- 00aaef30 bytes 7ab9e697
+ 00b0e9c0 bytes 7cc6e597
- 00aaef3c ["INT_ADD", "register:40f0:8", ["const:aaef3c:8", "const:4:8"]]
- 00aaef3c ["CALL", null, ["callee:004803b0:8"]]
+ 00b0e9cc ["INT_ADD", "register:40f0:8", ["const:b0e9cc:8", "const:4:8"]]
+ 00b0e9cc ["CALL", null, ["callee:004803b0:8"]]
- 00aaef3c bytes 77b9e697
+ 00b0e9cc bytes 79c6e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3376b650397caa583be4275003cf4f57"></a>

### [`00aaf024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md) → [`00b0eab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md) FUN_00b0eab4

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 2件 [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md) [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 2件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md#insn-00aaf044) · [`00aaf050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md#insn-00aaf050) · [`00aaf05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md#insn-00aaf05c)
- 新版 [`00b0ead4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md#insn-00b0ead4) · [`00b0eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md#insn-00b0eae0) · [`00b0eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md#insn-00b0eaec)

~~~diff
- 00aaf044 ["INT_ADD", "register:40f0:8", ["const:aaf044:8", "const:4:8"]]
- 00aaf044 ["CALL", null, ["callee:00480de8:8"]]
+ 00b0ead4 ["INT_ADD", "register:40f0:8", ["const:b0ead4:8", "const:4:8"]]
+ 00b0ead4 ["CALL", null, ["callee:00480de8:8"]]
- 00aaf044 bytes c3bbe697
+ 00b0ead4 bytes c5c8e597
- 00aaf050 ["INT_ADD", "register:40f0:8", ["const:aaf050:8", "const:4:8"]]
- 00aaf050 ["CALL", null, ["callee:00480de8:8"]]
+ 00b0eae0 ["INT_ADD", "register:40f0:8", ["const:b0eae0:8", "const:4:8"]]
+ 00b0eae0 ["CALL", null, ["callee:00480de8:8"]]
- 00aaf050 bytes c0bbe697
+ 00b0eae0 bytes c2c8e597
- 00aaf05c ["INT_ADD", "register:40f0:8", ["const:aaf05c:8", "const:4:8"]]
- 00aaf05c ["CALL", null, ["callee:00480de8:8"]]
+ 00b0eaec ["INT_ADD", "register:40f0:8", ["const:b0eaec:8", "const:4:8"]]
+ 00b0eaec ["CALL", null, ["callee:00480de8:8"]]
- 00aaf05c bytes bdbbe697
+ 00b0eaec bytes bfc8e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9bb97443d0e4072797d3efacd0dcf6a"></a>

### [`00aaf0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf0e8.md) → [`00b0eb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eb78.md) FUN_00b0eb78

採用 · 移動量 `+0x5fa90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf0e8.md#insn-00aaf100) · [`00aaf10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf0e8.md#insn-00aaf10c)
- 新版 [`00b0eb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eb78.md#insn-00b0eb90) · [`00b0eb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eb78.md#insn-00b0eb9c)

~~~diff
- 00aaf100 ["INT_ADD", "register:40f0:8", ["const:aaf100:8", "const:4:8"]]
- 00aaf100 ["CALL", null, ["callee:004803b0:8"]]
+ 00b0eb90 ["INT_ADD", "register:40f0:8", ["const:b0eb90:8", "const:4:8"]]
+ 00b0eb90 ["CALL", null, ["callee:004803b0:8"]]
- 00aaf100 bytes 06b9e697
+ 00b0eb90 bytes 08c6e597
- 00aaf10c ["INT_ADD", "register:40f0:8", ["const:aaf10c:8", "const:4:8"]]
- 00aaf10c ["CALL", null, ["callee:004803b0:8"]]
+ 00b0eb9c ["INT_ADD", "register:40f0:8", ["const:b0eb9c:8", "const:4:8"]]
+ 00b0eb9c ["CALL", null, ["callee:004803b0:8"]]
- 00aaf10c bytes 03b9e697
+ 00b0eb9c bytes 05c6e597
~~~


<a id="compare-cba7daf9b87d2a63476898cffebcb40e"></a>

### [`00aaf120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf120.md) → [`00b0ebb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ebb0.md) FUN_00b0ebb0

採用 · 移動量 `+0x5fa90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf120.md#insn-00aaf140)
- 新版 [`00b0ebd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ebb0.md#insn-00b0ebd0)

~~~diff
- 00aaf140 ["INT_ADD", "register:40f0:8", ["const:aaf140:8", "const:4:8"]]
- 00aaf140 ["CALL", null, ["callee:00480de8:8"]]
+ 00b0ebd0 ["INT_ADD", "register:40f0:8", ["const:b0ebd0:8", "const:4:8"]]
+ 00b0ebd0 ["CALL", null, ["callee:00480de8:8"]]
- 00aaf140 bytes 84bbe697
+ 00b0ebd0 bytes 86c8e597
~~~


<a id="compare-5b40b2ce2a46444fd128d7c222a024d7"></a>

### [`00aaf554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md) → [`00b0efe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md) FUN_00b0efe4

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00aaf73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf73c.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00ab0e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab0/00ab0e7c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00b0f1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f1cc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00b1090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b1090c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md#insn-00aaf594) · [`00aaf5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md#insn-00aaf5a4) · [`00aaf5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md#insn-00aaf5cc)
- 新版 [`00b0f024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md#insn-00b0f024) · [`00b0f034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md#insn-00b0f034) · [`00b0f05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md#insn-00b0f05c)

~~~diff
- 00aaf594 ["INT_ADD", "register:40f0:8", ["const:aaf594:8", "const:4:8"]]
- 00aaf594 ["CALL", null, ["callee:004878fc:8"]]
+ 00b0f024 ["INT_ADD", "register:40f0:8", ["const:b0f024:8", "const:4:8"]]
+ 00b0f024 ["CALL", null, ["callee:004878fc:8"]]
- 00aaf594 bytes 34d5e697
+ 00b0f024 bytes 36e2e597
- 00aaf5a4 ["INT_ADD", "register:40f0:8", ["const:aaf5a4:8", "const:4:8"]]
- 00aaf5a4 ["CALL", null, ["callee:004878fc:8"]]
+ 00b0f034 ["INT_ADD", "register:40f0:8", ["const:b0f034:8", "const:4:8"]]
+ 00b0f034 ["CALL", null, ["callee:004878fc:8"]]
- 00aaf5a4 bytes 30d5e697
+ 00b0f034 bytes 32e2e597
- 00aaf5cc ["INT_ADD", "register:40f0:8", ["const:aaf5cc:8", "const:4:8"]]
- 00aaf5cc ["CALL", null, ["callee:004878dc:8"]]
+ 00b0f05c ["INT_ADD", "register:40f0:8", ["const:b0f05c:8", "const:4:8"]]
+ 00b0f05c ["CALL", null, ["callee:004878dc:8"]]
- 00aaf5cc bytes 1ed5e697
+ 00b0f05c bytes 20e2e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e4ea2c5b8a9118a553a8d6670ee7612"></a>

### [`00ac9b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9b30.md) → [`00b295c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md) FUN_00b295c0

採用 · 移動量 `+0x5fa90` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00729118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729118.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`007532d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/007532d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9b30.md#insn-00ac9ba8) · [`00ac9bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9b30.md#insn-00ac9bcc) · [`00ac9bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9b30.md#insn-00ac9bf8)
- 新版 [`00b29638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md#insn-00b29638) · [`00b2965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md#insn-00b2965c) · [`00b29688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md#insn-00b29688)

~~~diff
- 00ac9ba8 ["INT_ADD", "register:40f0:8", ["const:ac9ba8:8", "const:4:8"]]
- 00ac9ba8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b29638 ["INT_ADD", "register:40f0:8", ["const:b29638:8", "const:4:8"]]
+ 00b29638 ["CALL", null, ["callee:00c57a90:8"]]
- 00ac9ba8 bytes 26450494
+ 00b29638 bytes 16b90494
- 00ac9bcc ["INT_ADD", "register:40f0:8", ["const:ac9bcc:8", "const:4:8"]]
- 00ac9bcc ["CALL", null, ["callee:00c57c90:8"]]
+ 00b2965c ["INT_ADD", "register:40f0:8", ["const:b2965c:8", "const:4:8"]]
+ 00b2965c ["CALL", null, ["callee:00c57c90:8"]]
- 00ac9bcc bytes 9d450494
+ 00b2965c bytes 8db90494
- 00ac9bf8 ["INT_ADD", "register:40f0:8", ["const:ac9bf8:8", "const:4:8"]]
- 00ac9bf8 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b29688 ["INT_ADD", "register:40f0:8", ["const:b29688:8", "const:4:8"]]
+ 00b29688 ["CALL", null, ["callee:00c57c90:8"]]
- 00ac9bf8 bytes 92450494
+ 00b29688 bytes 82b90494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8ca26f6ff965d0dfda0bab75c237f59"></a>

### [`00ac9c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9c5c.md) → [`00b296ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md) FUN_00b296ec

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00ac9e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9e0c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2989c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b2989c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9c5c.md#insn-00ac9d10) · [`00ac9d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9c5c.md#insn-00ac9d58) · [`00ac9dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9c5c.md#insn-00ac9dac)
- 新版 [`00b297a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md#insn-00b297a0) · [`00b297e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md#insn-00b297e8) · [`00b2983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b296ec.md#insn-00b2983c)

~~~diff
- 00ac9d10 ["INT_ADD", "register:40f0:8", ["const:ac9d10:8", "const:4:8"]]
- 00ac9d10 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b297a0 ["INT_ADD", "register:40f0:8", ["const:b297a0:8", "const:4:8"]]
+ 00b297a0 ["CALL", null, ["callee:00c57a90:8"]]
- 00ac9d10 bytes cc440494
+ 00b297a0 bytes bcb80494
- 00ac9d58 ["INT_ADD", "register:40f0:8", ["const:ac9d58:8", "const:4:8"]]
- 00ac9d58 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b297e8 ["INT_ADD", "register:40f0:8", ["const:b297e8:8", "const:4:8"]]
+ 00b297e8 ["CALL", null, ["callee:00c57c90:8"]]
- 00ac9d58 bytes 3a450494
+ 00b297e8 bytes 2ab90494
- 00ac9dac ["INT_ADD", "register:40f0:8", ["const:ac9dac:8", "const:4:8"]]
- 00ac9dac ["CALL", null, ["callee:00c57c90:8"]]
+ 00b2983c ["INT_ADD", "register:40f0:8", ["const:b2983c:8", "const:4:8"]]
+ 00b2983c ["CALL", null, ["callee:00c57c90:8"]]
- 00ac9dac bytes 25450494
+ 00b2983c bytes 15b90494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b8e53084caaf2031effda7c7773249c"></a>

### [`00aca16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca16c.md) → [`00b29bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md) FUN_00b29bfc

採用 · 移動量 `+0x5fa90` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca298.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b29d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca16c.md#insn-00aca1e4) · [`00aca208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca16c.md#insn-00aca208) · [`00aca234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca16c.md#insn-00aca234)
- 新版 [`00b29c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md#insn-00b29c74) · [`00b29c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md#insn-00b29c98) · [`00b29cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md#insn-00b29cc4)

~~~diff
- 00aca1e4 ["INT_ADD", "register:40f0:8", ["const:aca1e4:8", "const:4:8"]]
- 00aca1e4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b29c74 ["INT_ADD", "register:40f0:8", ["const:b29c74:8", "const:4:8"]]
+ 00b29c74 ["CALL", null, ["callee:00c57a90:8"]]
- 00aca1e4 bytes 97430494
+ 00b29c74 bytes 87b70494
- 00aca208 ["INT_ADD", "register:40f0:8", ["const:aca208:8", "const:4:8"]]
- 00aca208 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b29c98 ["INT_ADD", "register:40f0:8", ["const:b29c98:8", "const:4:8"]]
+ 00b29c98 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca208 bytes 0e440494
+ 00b29c98 bytes feb70494
- 00aca234 ["INT_ADD", "register:40f0:8", ["const:aca234:8", "const:4:8"]]
- 00aca234 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b29cc4 ["INT_ADD", "register:40f0:8", ["const:b29cc4:8", "const:4:8"]]
+ 00b29cc4 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca234 bytes 03440494
+ 00b29cc4 bytes f3b70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b199e2c03f42cb328deb3c94a3310e0b"></a>

### [`00aca2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca2ac.md) → [`00b29d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md) FUN_00b29d3c

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca440.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b29ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ed0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca2ac.md#insn-00aca354) · [`00aca394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca2ac.md#insn-00aca394) · [`00aca3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca2ac.md#insn-00aca3d8)
- 新版 [`00b29de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md#insn-00b29de4) · [`00b29e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md#insn-00b29e24) · [`00b29e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md#insn-00b29e68)

~~~diff
- 00aca354 ["INT_ADD", "register:40f0:8", ["const:aca354:8", "const:4:8"]]
- 00aca354 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b29de4 ["INT_ADD", "register:40f0:8", ["const:b29de4:8", "const:4:8"]]
+ 00b29de4 ["CALL", null, ["callee:00c57a90:8"]]
- 00aca354 bytes 3b430494
+ 00b29de4 bytes 2bb70494
- 00aca394 ["INT_ADD", "register:40f0:8", ["const:aca394:8", "const:4:8"]]
- 00aca394 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b29e24 ["INT_ADD", "register:40f0:8", ["const:b29e24:8", "const:4:8"]]
+ 00b29e24 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca394 bytes ab430494
+ 00b29e24 bytes 9bb70494
- 00aca3d8 ["INT_ADD", "register:40f0:8", ["const:aca3d8:8", "const:4:8"]]
- 00aca3d8 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b29e68 ["INT_ADD", "register:40f0:8", ["const:b29e68:8", "const:4:8"]]
+ 00b29e68 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca3d8 bytes 9a430494
+ 00b29e68 bytes 8ab70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e85fc0bb2e6d4a1f8e1eebf8a68ed1c"></a>

### [`00aca454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca454.md) → [`00b29ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md) FUN_00b29ee4

採用 · 移動量 `+0x5fa90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca5e4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a074.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca454.md#insn-00aca4f8) · [`00aca538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca454.md#insn-00aca538) · [`00aca584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca454.md#insn-00aca584)
- 新版 [`00b29f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md#insn-00b29f88) · [`00b29fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md#insn-00b29fc8) · [`00b2a014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md#insn-00b2a014)

~~~diff
- 00aca4f8 ["INT_ADD", "register:40f0:8", ["const:aca4f8:8", "const:4:8"]]
- 00aca4f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b29f88 ["INT_ADD", "register:40f0:8", ["const:b29f88:8", "const:4:8"]]
+ 00b29f88 ["CALL", null, ["callee:00c57a90:8"]]
- 00aca4f8 bytes d2420494
+ 00b29f88 bytes c2b60494
- 00aca538 ["INT_ADD", "register:40f0:8", ["const:aca538:8", "const:4:8"]]
- 00aca538 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b29fc8 ["INT_ADD", "register:40f0:8", ["const:b29fc8:8", "const:4:8"]]
+ 00b29fc8 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca538 bytes 42430494
+ 00b29fc8 bytes 32b70494
- 00aca584 ["INT_ADD", "register:40f0:8", ["const:aca584:8", "const:4:8"]]
- 00aca584 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b2a014 ["INT_ADD", "register:40f0:8", ["const:b2a014:8", "const:4:8"]]
+ 00b2a014 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca584 bytes 2f430494
+ 00b2a014 bytes 1fb70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c2f589d01570c293bcf4b71e4231f07"></a>

### [`00aca60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca60c.md) → [`00b2a09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md) FUN_00b2a09c

採用 · 移動量 `+0x5fa90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca738.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2a1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca60c.md#insn-00aca684) · [`00aca6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca60c.md#insn-00aca6a8) · [`00aca6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca60c.md#insn-00aca6d4)
- 新版 [`00b2a114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md#insn-00b2a114) · [`00b2a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md#insn-00b2a138) · [`00b2a164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md#insn-00b2a164)

~~~diff
- 00aca684 ["INT_ADD", "register:40f0:8", ["const:aca684:8", "const:4:8"]]
- 00aca684 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b2a114 ["INT_ADD", "register:40f0:8", ["const:b2a114:8", "const:4:8"]]
+ 00b2a114 ["CALL", null, ["callee:00c57a90:8"]]
- 00aca684 bytes 6f420494
+ 00b2a114 bytes 5fb60494
- 00aca6a8 ["INT_ADD", "register:40f0:8", ["const:aca6a8:8", "const:4:8"]]
- 00aca6a8 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b2a138 ["INT_ADD", "register:40f0:8", ["const:b2a138:8", "const:4:8"]]
+ 00b2a138 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca6a8 bytes e6420494
+ 00b2a138 bytes d6b60494
- 00aca6d4 ["INT_ADD", "register:40f0:8", ["const:aca6d4:8", "const:4:8"]]
- 00aca6d4 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b2a164 ["INT_ADD", "register:40f0:8", ["const:b2a164:8", "const:4:8"]]
+ 00b2a164 ["CALL", null, ["callee:00c57c90:8"]]
- 00aca6d4 bytes db420494
+ 00b2a164 bytes cbb60494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b39ee74a5459ab246e7c51c43f6a93f7"></a>

### [`00acad14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad14.md) → [`00b2a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md) FUN_00b2a7a4

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`0076a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a658.md) [`007d95c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d95c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00794b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794b2c.md) [`0080da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080da1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acadb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad14.md#insn-00acadb8) · [`00acae00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad14.md#insn-00acae00) · [`00acae18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad14.md#insn-00acae18)
- 新版 [`00b2a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md#insn-00b2a848) · [`00b2a890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md#insn-00b2a890) · [`00b2a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md#insn-00b2a8a8)

~~~diff
- 00acadb8 ["INT_ADD", "register:40f0:8", ["const:acadb8:8", "const:4:8"]]
- 00acadb8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b2a848 ["INT_ADD", "register:40f0:8", ["const:b2a848:8", "const:4:8"]]
+ 00b2a848 ["CALL", null, ["callee:00c57a90:8"]]
- 00acadb8 bytes a2400494
+ 00b2a848 bytes 92b40494
- 00acae00 ["INT_ADD", "register:40f0:8", ["const:acae00:8", "const:4:8"]]
- 00acae00 ["CALL", null, ["callee:0054071c:8"]]
+ 00b2a890 ["INT_ADD", "register:40f0:8", ["const:b2a890:8", "const:4:8"]]
+ 00b2a890 ["CALL", null, ["callee:0054071c:8"]]
- 00acae00 bytes a14ae997
+ 00b2a890 bytes a357e897
- 00acae18 ["INT_ADD", "register:40f0:8", ["const:acae18:8", "const:4:8"]]
- 00acae18 ["CALL", null, ["callee:0080da1c:8"]]
+ 00b2a8a8 ["INT_ADD", "register:40f0:8", ["const:b2a8a8:8", "const:4:8"]]
+ 00b2a8a8 ["CALL", null, ["callee:0080da1c:8"]]
- 00acae18 bytes ea39f497
+ 00b2a8a8 bytes 5d8cf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f6ffd148b22f9c9624457f0ed8e0946"></a>

### [`00acb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb090.md) → [`00b2ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md) FUN_00b2ab20

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 6件 [`005f064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062ca28.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 6件 [`00615e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md) [`00652480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652480.md) [`0065250c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/0065250c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb090.md#insn-00acb108) · [`00acb12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb090.md#insn-00acb12c) · [`00acb17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb090.md#insn-00acb17c)
- 新版 [`00b2ab98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md#insn-00b2ab98) · [`00b2abbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md#insn-00b2abbc) · [`00b2ac0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md#insn-00b2ac0c)

~~~diff
- 00acb108 ["INT_ADD", "register:40f0:8", ["const:acb108:8", "const:4:8"]]
- 00acb108 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b2ab98 ["INT_ADD", "register:40f0:8", ["const:b2ab98:8", "const:4:8"]]
+ 00b2ab98 ["CALL", null, ["callee:00c57a90:8"]]
- 00acb108 bytes ce3f0494
+ 00b2ab98 bytes beb30494
- 00acb12c ["INT_ADD", "register:40f0:8", ["const:acb12c:8", "const:4:8"]]
- 00acb12c ["CALL", null, ["callee:0065250c:8"]]
+ 00b2abbc ["INT_ADD", "register:40f0:8", ["const:b2abbc:8", "const:4:8"]]
+ 00b2abbc ["CALL", null, ["callee:0065250c:8"]]
- 00acb12c bytes 3f86ed97
+ 00b2abbc bytes 549eec97
- 00acb17c ["INT_ADD", "register:40f0:8", ["const:acb17c:8", "const:4:8"]]
- 00acb17c ["CALL", null, ["callee:00615e8c:8"]]
+ 00b2ac0c ["INT_ADD", "register:40f0:8", ["const:b2ac0c:8", "const:4:8"]]
+ 00b2ac0c ["CALL", null, ["callee:00615e8c:8"]]
- 00acb17c bytes 3495ec97
+ 00b2ac0c bytes a0aceb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0cb9ff489555e274dd196284c590687"></a>

### [`00acb1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md) → [`00b2ac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md) FUN_00b2ac48

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 11件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005f064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062ca28.md) [`00acb43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb43c.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 11件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00615e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md) [`00652480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652480.md) [`0065250c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/0065250c.md) [`00b2aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md#insn-00acb25c) · [`00acb2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md#insn-00acb2bc) · [`00acb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md#insn-00acb2e0)
- 新版 [`00b2acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md#insn-00b2acec) · [`00b2ad4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md#insn-00b2ad4c) · [`00b2ad70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md#insn-00b2ad70)

~~~diff
- 00acb25c ["INT_ADD", "register:40f0:8", ["const:acb25c:8", "const:4:8"]]
- 00acb25c ["CALL", null, ["callee:00c57a90:8"]]
+ 00b2acec ["INT_ADD", "register:40f0:8", ["const:b2acec:8", "const:4:8"]]
+ 00b2acec ["CALL", null, ["callee:00c57a90:8"]]
- 00acb25c bytes 793f0494
+ 00b2acec bytes 69b30494
- 00acb2bc ["INT_ADD", "register:40f0:8", ["const:acb2bc:8", "const:4:8"]]
- 00acb2bc ["CALL", null, ["callee:00c57a90:8"]]
+ 00b2ad4c ["INT_ADD", "register:40f0:8", ["const:b2ad4c:8", "const:4:8"]]
+ 00b2ad4c ["CALL", null, ["callee:00c57a90:8"]]
- 00acb2bc bytes 613f0494
+ 00b2ad4c bytes 51b30494
- 00acb2e0 ["INT_ADD", "register:40f0:8", ["const:acb2e0:8", "const:4:8"]]
- 00acb2e0 ["CALL", null, ["callee:0065250c:8"]]
+ 00b2ad70 ["INT_ADD", "register:40f0:8", ["const:b2ad70:8", "const:4:8"]]
+ 00b2ad70 ["CALL", null, ["callee:0065250c:8"]]
- 00acb2e0 bytes d285ed97
+ 00b2ad70 bytes e79dec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7098324038ac03b4b70c6a6345c39533"></a>

### [`00acb43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb43c.md) → [`00b2aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md) FUN_00b2aecc

採用 · 移動量 `+0x5fa90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acb1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b2ac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb43c.md#insn-00acb4b8) · [`00acb500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb43c.md#insn-00acb500)
- 新版 [`00b2af48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md#insn-00b2af48) · [`00b2af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md#insn-00b2af90)

~~~diff
- 00acb4b8 ["INT_ADD", "register:40f0:8", ["const:acb4b8:8", "const:4:8"]]
- 00acb4b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b2af48 ["INT_ADD", "register:40f0:8", ["const:b2af48:8", "const:4:8"]]
+ 00b2af48 ["CALL", null, ["callee:00c57ab0:8"]]
- 00acb4b8 bytes ea3e0494
+ 00b2af48 bytes dab20494
- 00acb500 ["INT_ADD", "register:40f0:8", ["const:acb500:8", "const:4:8"]]
- 00acb500 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b2af90 ["INT_ADD", "register:40f0:8", ["const:b2af90:8", "const:4:8"]]
+ 00b2af90 ["CALL", null, ["callee:00c57ab0:8"]]
- 00acb500 bytes d83e0494
+ 00b2af90 bytes c8b20494
~~~


<a id="compare-fb5225f2adace74648ac95035b3fe2b7"></a>

### [`00acb558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb558.md) → [`00b2afe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2afe8.md) FUN_00b2afe8

採用 · 移動量 `+0x5fa90` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acb1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b2ac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb558.md#insn-00acb58c) · [`00acb5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb558.md#insn-00acb5dc)
- 新版 [`00b2b01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2afe8.md#insn-00b2b01c) · [`00b2b06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2afe8.md#insn-00b2b06c)

~~~diff
- 00acb58c ["INT_ADD", "register:40f0:8", ["const:acb58c:8", "const:4:8"]]
- 00acb58c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b2b01c ["INT_ADD", "register:40f0:8", ["const:b2b01c:8", "const:4:8"]]
+ 00b2b01c ["CALL", null, ["callee:00c57ab0:8"]]
- 00acb58c bytes b53e0494
+ 00b2b01c bytes a5b20494
- 00acb5dc ["INT_ADD", "register:40f0:8", ["const:acb5dc:8", "const:4:8"]]
- 00acb5dc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b2b06c ["INT_ADD", "register:40f0:8", ["const:b2b06c:8", "const:4:8"]]
+ 00b2b06c ["CALL", null, ["callee:00c57ab0:8"]]
- 00acb5dc bytes a13e0494
+ 00b2b06c bytes 91b20494
~~~


<a id="compare-e78a61ee65276312e289a4d7d4f39528"></a>

### [`00acbd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md) → [`00b2b7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) FUN_00b2b7a4

採用 · 移動量 `+0x5fa90` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00418a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418a68.md) [`00418b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) · 呼出先 4件 [`00449bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bcc.md) [`00449be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449be4.md) [`00449bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bf0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`0043b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b568.md) [`0043b618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b618.md) · 呼出先 4件 [`0046ca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca64.md) [`0046ca7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca7c.md) [`0046ca88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acbd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md#insn-00acbd24) · [`00acbd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md#insn-00acbd2c) · [`00acbd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md#insn-00acbd34)
- 新版 [`00b2b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md#insn-00b2b7b4) · [`00b2b7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md#insn-00b2b7bc) · [`00b2b7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md#insn-00b2b7c4)

~~~diff
- 00acbd24 ["INT_ADD", "register:40f0:8", ["const:acbd24:8", "const:4:8"]]
- 00acbd24 ["CALL", null, ["callee:008514b8:8"]]
+ 00b2b7b4 ["INT_ADD", "register:40f0:8", ["const:b2b7b4:8", "const:4:8"]]
+ 00b2b7b4 ["CALL", null, ["callee:008514b8:8"]]
- 00acbd24 bytes 174ef597
+ 00b2b7b4 bytes 4197f497
- 00acbd2c ["INT_ADD", "register:40f0:8", ["const:acbd2c:8", "const:4:8"]]
- 00acbd2c ["CALL", null, ["callee:0046ca7c:8"]]
+ 00b2b7bc ["INT_ADD", "register:40f0:8", ["const:b2b7bc:8", "const:4:8"]]
+ 00b2b7bc ["CALL", null, ["callee:0046ca7c:8"]]
- 00acbd2c bytes aef7e597
+ 00b2b7bc bytes b004e597
- 00acbd34 ["INT_ADD", "register:40f0:8", ["const:acbd34:8", "const:4:8"]]
- 00acbd34 ["CALL", null, ["callee:008514b8:8"]]
+ 00b2b7c4 ["INT_ADD", "register:40f0:8", ["const:b2b7c4:8", "const:4:8"]]
+ 00b2b7c4 ["CALL", null, ["callee:008514b8:8"]]
- 00acbd34 bytes 134ef597
+ 00b2b7c4 bytes 3d97f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2169968127f3efc1e4f1f1147407597"></a>

### [`00acd390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd390.md) → [`00b2ce34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce34.md) FUN_00b2ce34

採用 · 移動量 `+0x5faa4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0043b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd390.md#insn-00acd3ac)
- 新版 [`00b2ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce34.md#insn-00b2ce50)

~~~diff
- 00acd3ac ["INT_ADD", "register:40f0:8", ["const:acd3ac:8", "const:4:8"]]
- 00acd3ac ["CALL", null, ["callee:008514b8:8"]]
+ 00b2ce50 ["INT_ADD", "register:40f0:8", ["const:b2ce50:8", "const:4:8"]]
+ 00b2ce50 ["CALL", null, ["callee:008514b8:8"]]
- 00acd3ac bytes 7548f597
+ 00b2ce50 bytes 9a91f497
~~~


<a id="compare-5cbd78b0bf34b8a07a7e44d4eacbf9c8"></a>

### [`00acd3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd3d8.md) → [`00b2ce7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce7c.md) FUN_00b2ce7c

採用 · 移動量 `+0x5faa4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0043b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd3d8.md#insn-00acd3f4)
- 新版 [`00b2ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce7c.md#insn-00b2ce98)

~~~diff
- 00acd3f4 ["INT_ADD", "register:40f0:8", ["const:acd3f4:8", "const:4:8"]]
- 00acd3f4 ["CALL", null, ["callee:008514b8:8"]]
+ 00b2ce98 ["INT_ADD", "register:40f0:8", ["const:b2ce98:8", "const:4:8"]]
+ 00b2ce98 ["CALL", null, ["callee:008514b8:8"]]
- 00acd3f4 bytes 6348f597
+ 00b2ce98 bytes 8891f497
~~~


<a id="compare-2f7b2f540fe286a56899f0556e085c43"></a>

### [`00acd420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd420.md) → [`00b2cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cec4.md) FUN_00b2cec4

採用 · 移動量 `+0x5faa4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0043b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd420.md#insn-00acd43c)
- 新版 [`00b2cee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cec4.md#insn-00b2cee0)

~~~diff
- 00acd43c ["INT_ADD", "register:40f0:8", ["const:acd43c:8", "const:4:8"]]
- 00acd43c ["CALL", null, ["callee:008514b8:8"]]
+ 00b2cee0 ["INT_ADD", "register:40f0:8", ["const:b2cee0:8", "const:4:8"]]
+ 00b2cee0 ["CALL", null, ["callee:008514b8:8"]]
- 00acd43c bytes 5148f597
+ 00b2cee0 bytes 7691f497
~~~


<a id="compare-1a7ae287dc005eaa3b646de5dee58fad"></a>

### [`00acd534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd534.md) → [`00b2cfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfec.md) FUN_00b2cfec

採用 · 移動量 `+0x5fab8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd534.md#insn-00acd53c)
- 新版 [`00b2cff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfec.md#insn-00b2cff4)

~~~diff
- 00acd53c ["INT_ADD", "register:40f0:8", ["const:acd53c:8", "const:4:8"]]
- 00acd53c ["CALL", null, ["callee:008514b8:8"]]
+ 00b2cff4 ["INT_ADD", "register:40f0:8", ["const:b2cff4:8", "const:4:8"]]
+ 00b2cff4 ["CALL", null, ["callee:008514b8:8"]]
- 00acd53c bytes 1148f597
+ 00b2cff4 bytes 3191f497
~~~


<a id="compare-c8c2f6ea0889eb059b491ea8f47b178d"></a>

### [`00acd5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd5b8.md) → [`00b2d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d070.md) FUN_00b2d070

採用 · 移動量 `+0x5fab8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd5b8.md#insn-00acd5c0)
- 新版 [`00b2d078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d070.md#insn-00b2d078)

~~~diff
- 00acd5c0 ["INT_ADD", "register:40f0:8", ["const:acd5c0:8", "const:4:8"]]
- 00acd5c0 ["CALL", null, ["callee:008514b8:8"]]
+ 00b2d078 ["INT_ADD", "register:40f0:8", ["const:b2d078:8", "const:4:8"]]
+ 00b2d078 ["CALL", null, ["callee:008514b8:8"]]
- 00acd5c0 bytes f047f597
+ 00b2d078 bytes 1091f497
~~~


<a id="compare-5fd34675f6acfa948537de07dc6fd87b"></a>

### [`00acd944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd944.md) → [`00b2d3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d3fc.md) FUN_00b2d3fc

採用 · 移動量 `+0x5fab8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acc598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc598.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b2c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd944.md#insn-00acd964)
- 新版 [`00b2d41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d3fc.md#insn-00b2d41c)

~~~diff
- 00acd964 ["INT_ADD", "register:40f0:8", ["const:acd964:8", "const:4:8"]]
- 00acd964 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b2d41c ["INT_ADD", "register:40f0:8", ["const:b2d41c:8", "const:4:8"]]
+ 00b2d41c ["CALL", null, ["callee:00c57ab0:8"]]
- 00acd964 bytes bf350494
+ 00b2d41c bytes a5a90494
~~~


<a id="compare-a916f28371dafcd9ca7bf60cd6864e57"></a>

### [`00acf910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf910.md) → [`00b2f3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md) FUN_00b2f3c8

採用 · 移動量 `+0x5fab8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e5/005e53dc.md) [`0063e818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e818.md) [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) [`0063ea04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063ea04.md) [`006e34b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e3/006e34b0.md) · 呼出先 1件 [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)
- 新版 呼出元 18件 [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`00664af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664af0.md) [`00664b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b8c.md) [`00664cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664cdc.md) [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) · 呼出先 1件 [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf910.md#insn-00acf918)
- 新版 [`00b2f3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md#insn-00b2f3d0)

~~~diff
- 00acf918 ["INT_ADD", "register:40f0:8", ["const:acf918:8", "const:4:8"]]
- 00acf918 ["CALL", null, ["callee:00b3ba6c:8"]]
+ 00b2f3d0 ["INT_ADD", "register:40f0:8", ["const:b2f3d0:8", "const:4:8"]]
+ 00b2f3d0 ["CALL", null, ["callee:00b3ba6c:8"]]
- 00acf918 bytes df310094
+ 00b2f3d0 bytes a7310094
~~~


<a id="compare-ad87a5482497b3da9b937fb2f9b7a19c"></a>

### [`00acf9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9a0.md) → [`00b2f458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f458.md) FUN_00b2f458

採用 · 移動量 `+0x5fab8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e5/005e53dc.md) [`0063e774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e774.md) [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) [`0063e910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e910.md) [`0063edf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063edf8.md) · 呼出先 1件 [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)
- 新版 呼出元 19件 [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`00664a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664a4c.md) [`00664b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b8c.md) [`00664be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664be8.md) [`006650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006650d0.md) · 呼出先 1件 [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9a0.md#insn-00acf9a8)
- 新版 [`00b2f460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f458.md#insn-00b2f460)

~~~diff
- 00acf9a8 ["INT_ADD", "register:40f0:8", ["const:acf9a8:8", "const:4:8"]]
- 00acf9a8 ["CALL", null, ["callee:00b3ba6c:8"]]
+ 00b2f460 ["INT_ADD", "register:40f0:8", ["const:b2f460:8", "const:4:8"]]
+ 00b2f460 ["CALL", null, ["callee:00b3ba6c:8"]]
- 00acf9a8 bytes bb310094
+ 00b2f460 bytes 83310094
~~~


<a id="compare-c604b4db26450fca8672e677e2fc1210"></a>

### [`00acfad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md) → [`00b2f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md) FUN_00b2f590

採用 · 移動量 `+0x5fab8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 33件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`005d8f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d8/005d8f58.md) [`00617dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00617/00617dec.md) [`00624a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624a0c.md) [`0062da7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da7c.md) · 呼出先 1件 [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)
- 新版 呼出元 32件 [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) [`005fdc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fd/005fdc18.md) [`0063d8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d8d4.md) [`0064a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) · 呼出先 1件 [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acfaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md#insn-00acfaec) · [`00acfb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md#insn-00acfb08)
- 新版 [`00b2f5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md#insn-00b2f5a4) · [`00b2f5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md#insn-00b2f5c0)

~~~diff
- 00acfaec ["INT_ADD", "register:40f0:8", ["const:acfaec:8", "const:4:8"]]
- 00acfaec ["CALL", null, ["callee:00b3ba6c:8"]]
+ 00b2f5a4 ["INT_ADD", "register:40f0:8", ["const:b2f5a4:8", "const:4:8"]]
+ 00b2f5a4 ["CALL", null, ["callee:00b3ba6c:8"]]
- 00acfaec bytes 6a310094
+ 00b2f5a4 bytes 32310094
- 00acfb08 ["INT_ADD", "register:40f0:8", ["const:acfb08:8", "const:4:8"]]
- 00acfb08 ["CALL", null, ["callee:00b3ba6c:8"]]
+ 00b2f5c0 ["INT_ADD", "register:40f0:8", ["const:b2f5c0:8", "const:4:8"]]
+ 00b2f5c0 ["CALL", null, ["callee:00b3ba6c:8"]]
- 00acfb08 bytes 63310094
+ 00b2f5c0 bytes 2b310094
~~~


<a id="compare-7bfc23cc0fde5b29315e07a81f98ca3f"></a>

### [`00acfe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfe60.md) → [`00b2f918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md) FUN_00b2f918

採用 · 移動量 `+0x5fab8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acfb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00ad0938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00b2f5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00b303f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b30/00b303f0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acfebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfe60.md#insn-00acfebc) · [`00acfed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfe60.md#insn-00acfed0) · [`00acff04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfe60.md#insn-00acff04)
- 新版 [`00b2f974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md#insn-00b2f974) · [`00b2f988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md#insn-00b2f988) · [`00b2f9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f918.md#insn-00b2f9bc)

~~~diff
- 00acfebc ["INT_ADD", "register:40f0:8", ["const:acfebc:8", "const:4:8"]]
- 00acfebc ["CALL", null, ["callee:0043bae0:8"]]
+ 00b2f974 ["INT_ADD", "register:40f0:8", ["const:b2f974:8", "const:4:8"]]
+ 00b2f974 ["CALL", null, ["callee:0043bae0:8"]]
- 00acfebc bytes 4924e597
+ 00b2f974 bytes 5b30e497
- 00acfed0 ["INT_ADD", "register:40f0:8", ["const:acfed0:8", "const:4:8"]]
- 00acfed0 ["CALL", null, ["callee:0043bae0:8"]]
+ 00b2f988 ["INT_ADD", "register:40f0:8", ["const:b2f988:8", "const:4:8"]]
+ 00b2f988 ["CALL", null, ["callee:0043bae0:8"]]
- 00acfed0 bytes 4424e597
+ 00b2f988 bytes 5630e497
- 00acff04 ["INT_ADD", "register:40f0:8", ["const:acff04:8", "const:4:8"]]
- 00acff04 ["CALL", null, ["callee:00b303f0:8"]]
+ 00b2f9bc ["INT_ADD", "register:40f0:8", ["const:b2f9bc:8", "const:4:8"]]
+ 00b2f9bc ["CALL", null, ["callee:00b303f0:8"]]
- 00acff04 bytes 8d020094
+ 00b2f9bc bytes 8d020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb33c0fcdf00fcdd5c6f6e2ae866d31"></a>

### [`00ad4a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4a94.md) → [`00b344d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md) FUN_00b344d8

採用 · 移動量 `+0x5fa44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad4468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4468.md) [`00ad6cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6cbc.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00b33f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33f20.md) [`00b36694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36694.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4a94.md#insn-00ad4b00) · [`00ad4b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4a94.md#insn-00ad4b10) · [`00ad4b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4a94.md#insn-00ad4b30)
- 新版 [`00b34544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md#insn-00b34544) · [`00b34554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md#insn-00b34554) · [`00b34574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md#insn-00b34574)

~~~diff
- 00ad4b00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4b00 ["INT_ADD", "register:40f0:8", ["const:ad4b00:8", "const:4:8"]]
- 00ad4b00 ["CALLIND", null, ["register:0:8"]]
+ 00b34544 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34544 ["INT_ADD", "register:40f0:8", ["const:b34544:8", "const:4:8"]]
+ 00b34544 ["CALLIND", null, ["register:0:8"]]
- 00ad4b00 bytes 00013fd6
+ 00b34544 bytes 00013fd6
- 00ad4b10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4b10 ["INT_ADD", "register:40f0:8", ["const:ad4b10:8", "const:4:8"]]
- 00ad4b10 ["CALLIND", null, ["register:0:8"]]
+ 00b34554 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34554 ["INT_ADD", "register:40f0:8", ["const:b34554:8", "const:4:8"]]
+ 00b34554 ["CALLIND", null, ["register:0:8"]]
- 00ad4b10 bytes 00013fd6
+ 00b34554 bytes 00013fd6
- 00ad4b30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4b30 ["INT_ADD", "register:40f0:8", ["const:ad4b30:8", "const:4:8"]]
- 00ad4b30 ["CALLIND", null, ["register:0:8"]]
+ 00b34574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34574 ["INT_ADD", "register:40f0:8", ["const:b34574:8", "const:4:8"]]
+ 00b34574 ["CALLIND", null, ["register:0:8"]]
- 00ad4b30 bytes 00013fd6
+ 00b34574 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bffd83f57d54d40a4c21482ca95e0ed"></a>

### [`00ad4bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4bfc.md) → [`00b34640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md) FUN_00b34640

採用 · 移動量 `+0x5fa44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad4530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b33fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4bfc.md#insn-00ad4c9c) · [`00ad4cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4bfc.md#insn-00ad4cc0) · [`00ad4d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4bfc.md#insn-00ad4d04)
- 新版 [`00b346e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md#insn-00b346e0) · [`00b34704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md#insn-00b34704) · [`00b34748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md#insn-00b34748)

~~~diff
- 00ad4c9c ["INT_ADD", "register:40f0:8", ["const:ad4c9c:8", "const:4:8"]]
- 00ad4c9c ["CALL", null, ["callee:00c57a90:8"]]
+ 00b346e0 ["INT_ADD", "register:40f0:8", ["const:b346e0:8", "const:4:8"]]
+ 00b346e0 ["CALL", null, ["callee:00c57a90:8"]]
- 00ad4c9c bytes e9180494
+ 00b346e0 bytes ec8c0494
- 00ad4cc0 ["INT_ADD", "register:40f0:8", ["const:ad4cc0:8", "const:4:8"]]
- 00ad4cc0 ["CALL", null, ["callee:00c57be0:8"]]
+ 00b34704 ["INT_ADD", "register:40f0:8", ["const:b34704:8", "const:4:8"]]
+ 00b34704 ["CALL", null, ["callee:00c57be0:8"]]
- 00ad4cc0 bytes 34190494
+ 00b34704 bytes 378d0494
- 00ad4d04 ["INT_ADD", "register:40f0:8", ["const:ad4d04:8", "const:4:8"]]
- 00ad4d04 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b34748 ["INT_ADD", "register:40f0:8", ["const:b34748:8", "const:4:8"]]
+ 00b34748 ["CALL", null, ["callee:00c57a90:8"]]
- 00ad4d04 bytes cf180494
+ 00b34748 bytes d28c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-248ca7db1d36444b34a2cef4bb0e5a85"></a>

### [`00ad4df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4df8.md) → [`00b3483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md) FUN_00b3483c

採用 · 移動量 `+0x5fa44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad4530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b33fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4df8.md#insn-00ad4e98) · [`00ad4ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4df8.md#insn-00ad4ebc) · [`00ad4f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4df8.md#insn-00ad4f00)
- 新版 [`00b348dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md#insn-00b348dc) · [`00b34900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md#insn-00b34900) · [`00b34944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md#insn-00b34944)

~~~diff
- 00ad4e98 ["INT_ADD", "register:40f0:8", ["const:ad4e98:8", "const:4:8"]]
- 00ad4e98 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b348dc ["INT_ADD", "register:40f0:8", ["const:b348dc:8", "const:4:8"]]
+ 00b348dc ["CALL", null, ["callee:00c57a90:8"]]
- 00ad4e98 bytes 6a180494
+ 00b348dc bytes 6d8c0494
- 00ad4ebc ["INT_ADD", "register:40f0:8", ["const:ad4ebc:8", "const:4:8"]]
- 00ad4ebc ["CALL", null, ["callee:00c57be0:8"]]
+ 00b34900 ["INT_ADD", "register:40f0:8", ["const:b34900:8", "const:4:8"]]
+ 00b34900 ["CALL", null, ["callee:00c57be0:8"]]
- 00ad4ebc bytes b5180494
+ 00b34900 bytes b88c0494
- 00ad4f00 ["INT_ADD", "register:40f0:8", ["const:ad4f00:8", "const:4:8"]]
- 00ad4f00 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b34944 ["INT_ADD", "register:40f0:8", ["const:b34944:8", "const:4:8"]]
+ 00b34944 ["CALL", null, ["callee:00c57a90:8"]]
- 00ad4f00 bytes 50180494
+ 00b34944 bytes 538c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8c4d867cff62a7f54200b78ec19bfe1"></a>

### [`00ad6078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md) → [`00b35a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md) FUN_00b35a50

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad5f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f04.md) [`00ad6078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md) · 呼出先 2件 [`00ad6078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00b358dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358dc.md) [`00b35a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md) · 呼出先 2件 [`00b35a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad6094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md#insn-00ad6094) · [`00ad60a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md#insn-00ad60a0) · [`00ad60d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md#insn-00ad60d4)
- 新版 [`00b35a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md#insn-00b35a6c) · [`00b35a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md#insn-00b35a78) · [`00b35aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md#insn-00b35aac)

~~~diff
- 00ad6094 ["INT_ADD", "register:40f0:8", ["const:ad6094:8", "const:4:8"]]
- 00ad6094 ["CALL", null, ["local:b0:8"]]
+ 00b35a6c ["INT_ADD", "register:40f0:8", ["const:b35a6c:8", "const:4:8"]]
+ 00b35a6c ["CALL", null, ["local:b0:8"]]
- 00ad6094 bytes f9ffff97
+ 00b35a6c bytes f9ffff97
- 00ad60a0 ["INT_ADD", "register:40f0:8", ["const:ad60a0:8", "const:4:8"]]
- 00ad60a0 ["CALL", null, ["local:b0:8"]]
+ 00b35a78 ["INT_ADD", "register:40f0:8", ["const:b35a78:8", "const:4:8"]]
+ 00b35a78 ["CALL", null, ["local:b0:8"]]
- 00ad60a0 bytes f6ffff97
+ 00b35a78 bytes f6ffff97
- 00ad60d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad60d4 ["INT_ADD", "register:40f0:8", ["const:ad60d4:8", "const:4:8"]]
- 00ad60d4 ["CALLIND", null, ["register:0:8"]]
+ 00b35aac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b35aac ["INT_ADD", "register:40f0:8", ["const:b35aac:8", "const:4:8"]]
+ 00b35aac ["CALLIND", null, ["register:0:8"]]
- 00ad60d4 bytes 00013fd6
+ 00b35aac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30635bbad568e2577da091d2f682b6e6"></a>

### [`00ad74f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad74f8.md) → [`00b36ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md) FUN_00b36ed0

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad9088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9088.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b38a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38a60.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad7534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad74f8.md#insn-00ad7534) · [`00ad7564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad74f8.md#insn-00ad7564) · [`00ad7594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad74f8.md#insn-00ad7594)
- 新版 [`00b36f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md#insn-00b36f0c) · [`00b36f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md#insn-00b36f3c) · [`00b36f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md#insn-00b36f6c)

~~~diff
- 00ad7534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7534 ["INT_ADD", "register:40f0:8", ["const:ad7534:8", "const:4:8"]]
- 00ad7534 ["CALLIND", null, ["register:0:8"]]
+ 00b36f0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b36f0c ["INT_ADD", "register:40f0:8", ["const:b36f0c:8", "const:4:8"]]
+ 00b36f0c ["CALLIND", null, ["register:0:8"]]
- 00ad7534 bytes 00013fd6
+ 00b36f0c bytes 00013fd6
- 00ad7564 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7564 ["INT_ADD", "register:40f0:8", ["const:ad7564:8", "const:4:8"]]
- 00ad7564 ["CALLIND", null, ["register:0:8"]]
+ 00b36f3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b36f3c ["INT_ADD", "register:40f0:8", ["const:b36f3c:8", "const:4:8"]]
+ 00b36f3c ["CALLIND", null, ["register:0:8"]]
- 00ad7564 bytes 00013fd6
+ 00b36f3c bytes 00013fd6
- 00ad7594 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7594 ["INT_ADD", "register:40f0:8", ["const:ad7594:8", "const:4:8"]]
- 00ad7594 ["CALLIND", null, ["register:0:8"]]
+ 00b36f6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b36f6c ["INT_ADD", "register:40f0:8", ["const:b36f6c:8", "const:4:8"]]
+ 00b36f6c ["CALLIND", null, ["register:0:8"]]
- 00ad7594 bytes 00013fd6
+ 00b36f6c bytes 00013fd6
~~~


<a id="compare-d0dfde535f39acf6a63d0149510fbeda"></a>

### [`00adb80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb80c.md) → [`00b3b1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b1e4.md) FUN_00b3b1e4

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb80c.md#insn-00adb868) · [`00adb894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb80c.md#insn-00adb894) · [`00adb8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb80c.md#insn-00adb8a4)
- 新版 [`00b3b240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b1e4.md#insn-00b3b240) · [`00b3b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b1e4.md#insn-00b3b26c) · [`00b3b27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b1e4.md#insn-00b3b27c)

~~~diff
- 00adb868 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb868 ["INT_ADD", "register:40f0:8", ["const:adb868:8", "const:4:8"]]
- 00adb868 ["CALLIND", null, ["register:0:8"]]
+ 00b3b240 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3b240 ["INT_ADD", "register:40f0:8", ["const:b3b240:8", "const:4:8"]]
+ 00b3b240 ["CALLIND", null, ["register:0:8"]]
- 00adb868 bytes 00013fd6
+ 00b3b240 bytes 00013fd6
- 00adb894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb894 ["INT_ADD", "register:40f0:8", ["const:adb894:8", "const:4:8"]]
- 00adb894 ["CALLIND", null, ["register:0:8"]]
+ 00b3b26c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3b26c ["INT_ADD", "register:40f0:8", ["const:b3b26c:8", "const:4:8"]]
+ 00b3b26c ["CALLIND", null, ["register:0:8"]]
- 00adb894 bytes 00013fd6
+ 00b3b26c bytes 00013fd6
- 00adb8a4 ["INT_ADD", "register:40f0:8", ["const:adb8a4:8", "const:4:8"]]
- 00adb8a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b3b27c ["INT_ADD", "register:40f0:8", ["const:b3b27c:8", "const:4:8"]]
+ 00b3b27c ["CALL", null, ["callee:00c57ab0:8"]]
- 00adb8a4 bytes effd0394
+ 00b3b27c bytes 0d720494
~~~


<a id="compare-5e1212b41f167cef24ee8bc40341658e"></a>

### [`00ae0070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0070.md) → [`00b3fa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md) FUN_00b3fa48

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ae05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md) · 呼出先 2件 [`00bddb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb10.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)
- 新版 呼出元 1件 [`00b3ff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md) · 呼出先 2件 [`00c5a560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a560.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0070.md#insn-00ae0080) · [`00ae0090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0070.md#insn-00ae0090)
- 新版 [`00b3fa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md#insn-00b3fa58) · [`00b3fa68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md#insn-00b3fa68)

~~~diff
- 00ae0080 ["INT_ADD", "register:40f0:8", ["const:ae0080:8", "const:4:8"]]
- 00ae0080 ["CALL", null, ["callee:00c5a860:8"]]
+ 00b3fa58 ["INT_ADD", "register:40f0:8", ["const:b3fa58:8", "const:4:8"]]
+ 00b3fa58 ["CALL", null, ["callee:00c5a860:8"]]
- 00ae0080 bytes 60f70394
+ 00b3fa58 bytes 826b0494
- 00ae0090 ["INT_ADD", "register:40f0:8", ["const:ae0090:8", "const:4:8"]]
- 00ae0090 ["CALL", null, ["callee:00c5a560:8"]]
+ 00b3fa68 ["INT_ADD", "register:40f0:8", ["const:b3fa68:8", "const:4:8"]]
+ 00b3fa68 ["CALL", null, ["callee:00c5a560:8"]]
- 00ae0090 bytes a0f60394
+ 00b3fa68 bytes be6a0494
~~~


<a id="compare-eadaccab84f14db82af9bddd961ec93e"></a>

### [`00ae00a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00a4.md) → [`00b3fa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa7c.md) FUN_00b3fa7c

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ae05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md) · 呼出先 2件 [`00bddaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaf0.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)
- 新版 呼出元 1件 [`00b3ff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md) · 呼出先 2件 [`00c5a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a540.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae00b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00a4.md#insn-00ae00b4)
- 新版 [`00b3fa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa7c.md#insn-00b3fa8c)

~~~diff
- 00ae00b4 ["INT_ADD", "register:40f0:8", ["const:ae00b4:8", "const:4:8"]]
- 00ae00b4 ["CALL", null, ["callee:00c5a860:8"]]
+ 00b3fa8c ["INT_ADD", "register:40f0:8", ["const:b3fa8c:8", "const:4:8"]]
+ 00b3fa8c ["CALL", null, ["callee:00c5a860:8"]]
- 00ae00b4 bytes 53f70394
+ 00b3fa8c bytes 756b0494
~~~


<a id="compare-eb009ac2c665ec2b64406d4ffeb22e21"></a>

### [`00ae3e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e0c.md) → [`00b43b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `reordered`

- 旧版 呼出元 3件 [`00ae2c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md) [`00b4de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4de48.md) [`00b6eef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eef0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00b42888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42888.md) [`00bbc3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc3b0.md) [`00bde3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde3f0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e0c.md#insn-00ae3e2c)
- 新版 [`00b43bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md#insn-00b43bb0)

~~~diff
- 00ae3e2c ["INT_ADD", "register:40f0:8", ["const:ae3e2c:8", "const:4:8"]]
- 00ae3e2c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b43bb0 ["INT_ADD", "register:40f0:8", ["const:b43bb0:8", "const:4:8"]]
+ 00b43bb0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00ae3e2c bytes 8ddc0394
+ 00b43bb0 bytes c04f0494
~~~


<a id="compare-95bdc9d4d4a2613267265c98d60f3a6b"></a>

### [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) → [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) FUN_00b43cf8

採用 · 移動量 `+0x5fd84` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00ae3fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md) [`00ae44a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44a0.md) [`00ae44cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md) · 呼出先 2件 [`00ae4514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 3件 [`00b43d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md) [`00b44224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44224.md) [`00b44250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md) · 呼出先 2件 [`00b44298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44298.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md#insn-00ae3f88) · [`00ae3fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md#insn-00ae3fa0)
- 新版 [`00b43d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md#insn-00b43d0c) · [`00b43d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md#insn-00b43d24)

~~~diff
- 00ae3f88 ["INT_ADD", "register:40f0:8", ["const:ae3f88:8", "const:4:8"]]
- 00ae3f88 ["CALL", null, ["callee:00b44298:8"]]
+ 00b43d0c ["INT_ADD", "register:40f0:8", ["const:b43d0c:8", "const:4:8"]]
+ 00b43d0c ["CALL", null, ["callee:00b44298:8"]]
- 00ae3f88 bytes 63010094
+ 00b43d0c bytes 63010094
- 00ae3fa0 ["INT_ADD", "register:40f0:8", ["const:ae3fa0:8", "const:4:8"]]
- 00ae3fa0 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b43d24 ["INT_ADD", "register:40f0:8", ["const:b43d24:8", "const:4:8"]]
+ 00b43d24 ["CALL", null, ["callee:00c5ad40:8"]]
- 00ae3fa0 bytes c8e80394
+ 00b43d24 bytes 075c0494
~~~


<a id="compare-89177399c1a8e1cebdffd7abd8c8421f"></a>

### [`00ae45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae45f4.md) → [`00b44378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44378.md) _ZN8firebase18AndroidLogMessageVEiPKcS1_St9__va_list

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde370.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5adf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae461c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae45f4.md#insn-00ae461c) · [`00ae4640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae45f4.md#insn-00ae4640)
- 新版 [`00b443a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44378.md#insn-00b443a0) · [`00b443c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44378.md#insn-00b443c4)

~~~diff
- 00ae461c ["INT_ADD", "register:40f0:8", ["const:ae461c:8", "const:4:8"]]
- 00ae461c ["CALL", null, ["callee:00c5adf0:8"]]
+ 00b443a0 ["INT_ADD", "register:40f0:8", ["const:b443a0:8", "const:4:8"]]
+ 00b443a0 ["CALL", null, ["callee:00c5adf0:8"]]
- 00ae461c bytes 55e70394
+ 00b443a0 bytes 945a0494
- 00ae4640 ["INT_ADD", "register:40f0:8", ["const:ae4640:8", "const:4:8"]]
- 00ae4640 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00b443c4 ["INT_ADD", "register:40f0:8", ["const:b443c4:8", "const:4:8"]]
+ 00b443c4 ["CALL", null, ["callee:00c57ae0:8"]]
- 00ae4640 bytes 94da0394
+ 00b443c4 bytes c74d0494
~~~


<a id="compare-a2213c6a7c3ca68a3b7240bf0332dd8f"></a>

### [`00af1558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1558.md) → [`00b512dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b512dc.md) _ZN7_JNIEnv20CallStaticVoidMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af15cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1558.md#insn-00af15cc) · [`00af15f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1558.md#insn-00af15f0)
- 新版 [`00b51350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b512dc.md#insn-00b51350) · [`00b51374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b512dc.md#insn-00b51374)

~~~diff
- 00af15cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00af15cc ["INT_ADD", "register:40f0:8", ["const:af15cc:8", "const:4:8"]]
- 00af15cc ["CALLIND", null, ["register:0:8"]]
+ 00b51350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b51350 ["INT_ADD", "register:40f0:8", ["const:b51350:8", "const:4:8"]]
+ 00b51350 ["CALLIND", null, ["register:0:8"]]
- 00af15cc bytes 00013fd6
+ 00b51350 bytes 00013fd6
- 00af15f0 ["INT_ADD", "register:40f0:8", ["const:af15f0:8", "const:4:8"]]
- 00af15f0 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00b51374 ["INT_ADD", "register:40f0:8", ["const:b51374:8", "const:4:8"]]
+ 00b51374 ["CALL", null, ["callee:00c57ae0:8"]]
- 00af15f0 bytes a8a60394
+ 00b51374 bytes db190494
~~~


<a id="compare-68966228caecc139903baa3de95d0173"></a>

### [`00afddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md) → [`00b5db7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md) _ZN8firebase4Path11GetRelativeERKS0_S2_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bded20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded20.md) · 呼出先 6件 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)
- 新版 呼出元 1件 [`00c5b7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7e0.md) · 呼出先 6件 [`00b5d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d030.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afde2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md#insn-00afde2c) · [`00afde38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md#insn-00afde38) · [`00afdef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md#insn-00afdef4)
- 新版 [`00b5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md#insn-00b5dbb0) · [`00b5dbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md#insn-00b5dbbc) · [`00b5dc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md#insn-00b5dc78)

~~~diff
- 00afde2c ["INT_ADD", "register:40f0:8", ["const:afde2c:8", "const:4:8"]]
- 00afde2c ["CALL", null, ["callee:00c5b800:8"]]
+ 00b5dbb0 ["INT_ADD", "register:40f0:8", ["const:b5dbb0:8", "const:4:8"]]
+ 00b5dbb0 ["CALL", null, ["callee:00c5b800:8"]]
- 00afde2c bytes c5830394
+ 00b5dbb0 bytes 14f70394
- 00afde38 ["INT_ADD", "register:40f0:8", ["const:afde38:8", "const:4:8"]]
- 00afde38 ["CALL", null, ["callee:00c5b800:8"]]
+ 00b5dbbc ["INT_ADD", "register:40f0:8", ["const:b5dbbc:8", "const:4:8"]]
+ 00b5dbbc ["CALL", null, ["callee:00c5b800:8"]]
- 00afde38 bytes c2830394
+ 00b5dbbc bytes 11f70394
- 00afdef4 ["INT_ADD", "register:40f0:8", ["const:afdef4:8", "const:4:8"]]
- 00afdef4 ["CALL", null, ["callee:00c57c50:8"]]
+ 00b5dc78 ["INT_ADD", "register:40f0:8", ["const:b5dc78:8", "const:4:8"]]
+ 00b5dc78 ["CALL", null, ["callee:00c57c50:8"]]
- 00afdef4 bytes c3740394
+ 00b5dc78 bytes f6e70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc065ee0ce54b69e97c362dad3b314d"></a>

### [`00afe05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe05c.md) → [`00b5dde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iterator

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bded50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded50.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)
- 新版 呼出元 1件 [`00c5b810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b810.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe05c.md#insn-00afe16c) · [`00afe198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe05c.md#insn-00afe198) · [`00afe1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe05c.md#insn-00afe1e8)
- 新版 [`00b5def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md#insn-00b5def0) · [`00b5df1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md#insn-00b5df1c) · [`00b5df6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md#insn-00b5df6c)

~~~diff
- 00afe16c ["INT_ADD", "register:40f0:8", ["const:afe16c:8", "const:4:8"]]
- 00afe16c ["CALL", null, ["callee:00c5a4e0:8"]]
+ 00b5def0 ["INT_ADD", "register:40f0:8", ["const:b5def0:8", "const:4:8"]]
+ 00b5def0 ["CALL", null, ["callee:00c5a4e0:8"]]
- 00afe16c bytes 497e0394
+ 00b5def0 bytes 7cf10394
- 00afe198 ["INT_ADD", "register:40f0:8", ["const:afe198:8", "const:4:8"]]
- 00afe198 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b5df1c ["INT_ADD", "register:40f0:8", ["const:b5df1c:8", "const:4:8"]]
+ 00b5df1c ["CALL", null, ["callee:00c57a90:8"]]
- 00afe198 bytes aa730394
+ 00b5df1c bytes dde60394
- 00afe1e8 ["INT_ADD", "register:40f0:8", ["const:afe1e8:8", "const:4:8"]]
- 00afe1e8 ["CALL", null, ["callee:00c57b40:8"]]
+ 00b5df6c ["INT_ADD", "register:40f0:8", ["const:b5df6c:8", "const:4:8"]]
+ 00b5df6c ["CALL", null, ["callee:00c57b40:8"]]
- 00afe1e8 bytes c2730394
+ 00b5df6c bytes f5e60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ef24c6f8d0b1424ce6c1cd5b9fa4e4d"></a>

### [`00afea28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afea28.md) → [`00b5e7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md) _ZN8firebase17FutureBackingData22ClearExistingCallbacksEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdedc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdedc0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5b880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b880.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afea54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afea28.md#insn-00afea54) · [`00afea70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afea28.md#insn-00afea70) · [`00afeacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afea28.md#insn-00afeacc)
- 新版 [`00b5e7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md#insn-00b5e7d8) · [`00b5e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md#insn-00b5e7f4) · [`00b5e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e7ac.md#insn-00b5e850)

~~~diff
- 00afea54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afea54 ["INT_ADD", "register:40f0:8", ["const:afea54:8", "const:4:8"]]
- 00afea54 ["CALLIND", null, ["register:0:8"]]
+ 00b5e7d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5e7d8 ["INT_ADD", "register:40f0:8", ["const:b5e7d8:8", "const:4:8"]]
+ 00b5e7d8 ["CALLIND", null, ["register:0:8"]]
- 00afea54 bytes 00013fd6
+ 00b5e7d8 bytes 00013fd6
- 00afea70 ["INT_ADD", "register:40f0:8", ["const:afea70:8", "const:4:8"]]
- 00afea70 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b5e7f4 ["INT_ADD", "register:40f0:8", ["const:b5e7f4:8", "const:4:8"]]
+ 00b5e7f4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00afea70 bytes 7c710394
+ 00b5e7f4 bytes afe40394
- 00afeacc ["COPY", "register:0:8", ["register:4040:8"]]
- 00afeacc ["INT_ADD", "register:40f0:8", ["const:afeacc:8", "const:4:8"]]
- 00afeacc ["CALLIND", null, ["register:0:8"]]
+ 00b5e850 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5e850 ["INT_ADD", "register:40f0:8", ["const:b5e850:8", "const:4:8"]]
+ 00b5e850 ["CALLIND", null, ["register:0:8"]]
- 00afeacc bytes 00013fd6
+ 00b5e850 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-878b8cd0cf71560794aec82b8b4b27b4"></a>

### [`00b00c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00c6c.md) → [`00b609f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b609f0.md) _ZN8firebase26ReferenceCountedFutureImpl12MarkOrphanedEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00c6c.md#insn-00b00c84)
- 新版 [`00b60a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b609f0.md#insn-00b60a08)

~~~diff
- 00b00c84 ["INT_ADD", "register:40f0:8", ["const:b00c84:8", "const:4:8"]]
- 00b00c84 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b60a08 ["INT_ADD", "register:40f0:8", ["const:b60a08:8", "const:4:8"]]
+ 00b60a08 ["CALL", null, ["callee:00c5a600:8"]]
- 00b00c84 bytes e7730394
+ 00b60a08 bytes fee60394
~~~


<a id="compare-040d08974449317c1871b9e932804c07"></a>

### [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md) → [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md) FUN_00b60d04

採用 · 移動量 `+0x5fc18` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `reordered`

- 旧版 呼出元 6件 [`00b002e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b002e8.md) [`00b081c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md) [`00b59b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59b68.md) [`00b59d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59d2c.md) [`00b5aaac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aaac.md) · 呼出先 1件 [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 7件 [`00b6006c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b6006c.md) [`00b67e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md) [`00bb3be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3be8.md) [`00bc9068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9068.md) [`00bc922c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md) · 呼出先 1件 [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b010f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md#insn-00b010f4)
- 新版 [`00b60d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md#insn-00b60d0c)

~~~diff
- 00b010f4 ["INT_ADD", "register:40f0:8", ["const:b010f4:8", "const:4:8"]]
- 00b010f4 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b60d0c ["INT_ADD", "register:40f0:8", ["const:b60d0c:8", "const:4:8"]]
+ 00b60d0c ["CALL", null, ["callee:00c5ad40:8"]]
- 00b010f4 bytes 73740394
+ 00b60d0c bytes 0de80394
~~~


<a id="compare-51d6fe95157e17b16f2f0762c5d4121e"></a>

### [`00b02510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02510.md) → [`00b62144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62144.md) _ZN8firebase16StaticFutureData13CreateNewDataEPKvi

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddde0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02510.md#insn-00b02524) · [`00b02530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02510.md#insn-00b02530)
- 新版 [`00b62158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62144.md#insn-00b62158) · [`00b62164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62144.md#insn-00b62164)

~~~diff
- 00b02524 ["INT_ADD", "register:40f0:8", ["const:b02524:8", "const:4:8"]]
- 00b02524 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b62158 ["INT_ADD", "register:40f0:8", ["const:b62158:8", "const:4:8"]]
+ 00b62158 ["CALL", null, ["callee:00c57a90:8"]]
- 00b02524 bytes c7620394
+ 00b62158 bytes 4ed60394
- 00b02530 ["INT_ADD", "register:40f0:8", ["const:b02530:8", "const:4:8"]]
- 00b02530 ["CALL", null, ["callee:00c5a840:8"]]
+ 00b62164 ["INT_ADD", "register:40f0:8", ["const:b62164:8", "const:4:8"]]
+ 00b62164 ["CALL", null, ["callee:00c5a840:8"]]
- 00b02530 bytes 2c6e0394
+ 00b62164 bytes b7e10394
~~~


<a id="compare-3340297525dad77f8412e078ee9da89a"></a>

### [`00b029dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b029dc.md) → [`00b62634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md) _ZNSt6__ndk16vectorIPFN8firebase10InitResultEPNS1_3AppEPvENS_9allocatorIS7_EEE21__push_back_slow_pathIRKS7_EEvOT_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdef00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef00.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9b0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b029dc.md#insn-00b02a40) · [`00b02a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b029dc.md#insn-00b02a4c) · [`00b02a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b029dc.md#insn-00b02a78)
- 新版 [`00b62698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md#insn-00b62698) · [`00b626a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md#insn-00b626a4) · [`00b626d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62634.md#insn-00b626d0)

~~~diff
- 00b02a40 ["INT_ADD", "register:40f0:8", ["const:b02a40:8", "const:4:8"]]
- 00b02a40 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b62698 ["INT_ADD", "register:40f0:8", ["const:b62698:8", "const:4:8"]]
+ 00b62698 ["CALL", null, ["callee:00c5ad40:8"]]
- 00b02a40 bytes 206e0394
+ 00b62698 bytes aae10394
- 00b02a4c ["INT_ADD", "register:40f0:8", ["const:b02a4c:8", "const:4:8"]]
- 00b02a4c ["CALL", null, ["callee:00c57a90:8"]]
+ 00b626a4 ["INT_ADD", "register:40f0:8", ["const:b626a4:8", "const:4:8"]]
+ 00b626a4 ["CALL", null, ["callee:00c57a90:8"]]
- 00b02a4c bytes 7d610394
+ 00b626a4 bytes fbd40394
- 00b02a78 ["INT_ADD", "register:40f0:8", ["const:b02a78:8", "const:4:8"]]
- 00b02a78 ["CALL", null, ["callee:00c57c00:8"]]
+ 00b626d0 ["INT_ADD", "register:40f0:8", ["const:b626d0:8", "const:4:8"]]
+ 00b626d0 ["CALL", null, ["callee:00c57c00:8"]]
- 00b02a78 bytes ce610394
+ 00b626d0 bytes 4cd50394
~~~


<a id="compare-8bbd5ca2d4d9a2fe32c9845ac55f45de"></a>

### [`00b02ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ac4.md) → [`00b6271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeed0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeed0.md)
- 新版 呼出元 1件 [`00c5b980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b980.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ac4.md#insn-00b02ae0) · [`00b02aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ac4.md#insn-00b02aec) · [`00b02afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ac4.md#insn-00b02afc)
- 新版 [`00b62738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md#insn-00b62738) · [`00b62744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md#insn-00b62744) · [`00b62754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6271c.md#insn-00b62754)

~~~diff
- 00b02ae0 ["INT_ADD", "register:40f0:8", ["const:b02ae0:8", "const:4:8"]]
- 00b02ae0 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b62738 ["INT_ADD", "register:40f0:8", ["const:b62738:8", "const:4:8"]]
+ 00b62738 ["CALL", null, ["callee:00c5b980:8"]]
- 00b02ae0 bytes fc700394
+ 00b62738 bytes 92e40394
- 00b02aec ["INT_ADD", "register:40f0:8", ["const:b02aec:8", "const:4:8"]]
- 00b02aec ["CALL", null, ["callee:00c5b980:8"]]
+ 00b62744 ["INT_ADD", "register:40f0:8", ["const:b62744:8", "const:4:8"]]
+ 00b62744 ["CALL", null, ["callee:00c5b980:8"]]
- 00b02aec bytes f9700394
+ 00b62744 bytes 8fe40394
- 00b02afc ["INT_ADD", "register:40f0:8", ["const:b02afc:8", "const:4:8"]]
- 00b02afc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b62754 ["INT_ADD", "register:40f0:8", ["const:b62754:8", "const:4:8"]]
+ 00b62754 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b02afc bytes 59610394
+ 00b62754 bytes d7d40394
~~~


<a id="compare-931c2da4cbc31e244b6edf609922aea2"></a>

### [`00b02b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02b14.md) → [`00b6276c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6276c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeec0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5b970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b970.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02b14.md#insn-00b02bb0) · [`00b02bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02b14.md#insn-00b02bf0)
- 新版 [`00b62808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6276c.md#insn-00b62808) · [`00b62848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6276c.md#insn-00b62848)

~~~diff
- 00b02bb0 ["INT_ADD", "register:40f0:8", ["const:b02bb0:8", "const:4:8"]]
- 00b02bb0 ["CALL", null, ["callee:00c57c50:8"]]
+ 00b62808 ["INT_ADD", "register:40f0:8", ["const:b62808:8", "const:4:8"]]
+ 00b62808 ["CALL", null, ["callee:00c57c50:8"]]
- 00b02bb0 bytes 94610394
+ 00b62808 bytes 12d50394
- 00b02bf0 ["INT_ADD", "register:40f0:8", ["const:b02bf0:8", "const:4:8"]]
- 00b02bf0 ["CALL", null, ["callee:00c57c50:8"]]
+ 00b62848 ["INT_ADD", "register:40f0:8", ["const:b62848:8", "const:4:8"]]
+ 00b62848 ["CALL", null, ["callee:00c57c50:8"]]
- 00b02bf0 bytes 84610394
+ 00b62848 bytes 02d50394
~~~


<a id="compare-936d77c5030af98bcd2a70ac66b3b1d4"></a>

### [`00b02c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02c34.md) → [`00b6288c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6288c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeef0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5b9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9a0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02c34.md#insn-00b02ccc) · [`00b02d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02c34.md#insn-00b02d14)
- 新版 [`00b62924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6288c.md#insn-00b62924) · [`00b6296c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b6288c.md#insn-00b6296c)

~~~diff
- 00b02ccc ["INT_ADD", "register:40f0:8", ["const:b02ccc:8", "const:4:8"]]
- 00b02ccc ["CALL", null, ["callee:00c57c50:8"]]
+ 00b62924 ["INT_ADD", "register:40f0:8", ["const:b62924:8", "const:4:8"]]
+ 00b62924 ["CALL", null, ["callee:00c57c50:8"]]
- 00b02ccc bytes 4d610394
+ 00b62924 bytes cbd40394
- 00b02d14 ["INT_ADD", "register:40f0:8", ["const:b02d14:8", "const:4:8"]]
- 00b02d14 ["CALL", null, ["callee:00c57c50:8"]]
+ 00b6296c ["INT_ADD", "register:40f0:8", ["const:b6296c:8", "const:4:8"]]
+ 00b6296c ["CALL", null, ["callee:00c57c50:8"]]
- 00b02d14 bytes 3b610394
+ 00b6296c bytes b9d40394
~~~


<a id="compare-35bab6e82e5bc65b9a7e0bdd225776d3"></a>

### [`00b06b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md) → [`00b667d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md) _ZN8firebase3AppD2Ev

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde940.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde340.md) [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)
- 新版 呼出元 1件 [`00c5b3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3c0.md) · 呼出先 7件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5adc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5adc0.md) [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md#insn-00b06b8c) · [`00b06b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md#insn-00b06b98) · [`00b06bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md#insn-00b06bac)
- 新版 [`00b667e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md#insn-00b667e4) · [`00b667f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md#insn-00b667f0) · [`00b66804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md#insn-00b66804)

~~~diff
- 00b06b8c ["INT_ADD", "register:40f0:8", ["const:b06b8c:8", "const:4:8"]]
- 00b06b8c ["CALL", null, ["callee:00c5b360:8"]]
+ 00b667e4 ["INT_ADD", "register:40f0:8", ["const:b667e4:8", "const:4:8"]]
+ 00b667e4 ["CALL", null, ["callee:00c5b360:8"]]
- 00b06b8c bytes 555f0394
+ 00b667e4 bytes dfd20394
- 00b06b98 ["INT_ADD", "register:40f0:8", ["const:b06b98:8", "const:4:8"]]
- 00b06b98 ["CALL", null, ["callee:00c5afc0:8"]]
+ 00b667f0 ["INT_ADD", "register:40f0:8", ["const:b667f0:8", "const:4:8"]]
+ 00b667f0 ["CALL", null, ["callee:00c5afc0:8"]]
- 00b06b98 bytes 6a5e0394
+ 00b667f0 bytes f4d10394
- 00b06bac ["INT_ADD", "register:40f0:8", ["const:b06bac:8", "const:4:8"]]
- 00b06bac ["CALL", null, ["callee:00c5adc0:8"]]
+ 00b66804 ["INT_ADD", "register:40f0:8", ["const:b66804:8", "const:4:8"]]
+ 00b66804 ["CALL", null, ["callee:00c5adc0:8"]]
- 00b06bac bytes e55d0394
+ 00b66804 bytes 6fd10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e67a4aeb3df0fbad5ce6be07d170312"></a>

### [`00b081c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md) → [`00b67e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md) _ZN8firebase28CallAfterEnsureMethodsCachedEP7_JNIEnvP8_jobjectNSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b081d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md#insn-00b081d4) · [`00b081ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md#insn-00b081ec) · [`00b0820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md#insn-00b0820c)
- 新版 [`00b67e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md#insn-00b67e2c) · [`00b67e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md#insn-00b67e44) · [`00b67e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md#insn-00b67e64)

~~~diff
- 00b081d4 ["INT_ADD", "register:40f0:8", ["const:b081d4:8", "const:4:8"]]
- 00b081d4 ["CALL", null, ["callee:00b6602c:8"]]
+ 00b67e2c ["INT_ADD", "register:40f0:8", ["const:b67e2c:8", "const:4:8"]]
+ 00b67e2c ["CALL", null, ["callee:00b6602c:8"]]
- 00b081d4 bytes 80f8ff97
+ 00b67e2c bytes 80f8ff97
- 00b081ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b081ec ["INT_ADD", "register:40f0:8", ["const:b081ec:8", "const:4:8"]]
- 00b081ec ["CALLIND", null, ["register:0:8"]]
+ 00b67e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67e44 ["INT_ADD", "register:40f0:8", ["const:b67e44:8", "const:4:8"]]
+ 00b67e44 ["CALLIND", null, ["register:0:8"]]
- 00b081ec bytes 00013fd6
+ 00b67e44 bytes 00013fd6
- 00b0820c ["INT_ADD", "register:40f0:8", ["const:b0820c:8", "const:4:8"]]
- 00b0820c ["CALL", null, ["callee:00b60d04:8"]]
+ 00b67e64 ["INT_ADD", "register:40f0:8", ["const:b67e64:8", "const:4:8"]]
+ 00b67e64 ["CALL", null, ["callee:00b60d04:8"]]
- 00b0820c bytes b8e3ff97
+ 00b67e64 bytes a8e3ff97
~~~


<a id="compare-793ff34f00627ab4b047e3c79cdf817a"></a>

### [`00b0d1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1bc.md) → [`00b6d4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d4d8.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0x6031c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec00.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec00.md)
- 新版 呼出元 1件 [`00c5b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6c0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1bc.md#insn-00b0d1d8) · [`00b0d1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1bc.md#insn-00b0d1e4)
- 新版 [`00b6d4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d4d8.md#insn-00b6d4f4) · [`00b6d500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d4d8.md#insn-00b6d500)

~~~diff
- 00b0d1d8 ["INT_ADD", "register:40f0:8", ["const:b0d1d8:8", "const:4:8"]]
- 00b0d1d8 ["CALL", null, ["callee:00c5b6c0:8"]]
+ 00b6d4f4 ["INT_ADD", "register:40f0:8", ["const:b6d4f4:8", "const:4:8"]]
+ 00b6d4f4 ["CALL", null, ["callee:00c5b6c0:8"]]
- 00b0d1d8 bytes 8a460394
+ 00b6d4f4 bytes 73b80394
- 00b0d1e4 ["INT_ADD", "register:40f0:8", ["const:b0d1e4:8", "const:4:8"]]
- 00b0d1e4 ["CALL", null, ["callee:00c5b6c0:8"]]
+ 00b6d500 ["INT_ADD", "register:40f0:8", ["const:b6d500:8", "const:4:8"]]
+ 00b6d500 ["CALL", null, ["callee:00c5b6c0:8"]]
- 00b0d1e4 bytes 87460394
+ 00b6d500 bytes 70b80394
~~~


<a id="compare-e1cbed1b68f210d82934a6e43f2e21c8"></a>

### [`00b0d1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1fc.md) → [`00b6d518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d518.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE

採用 · 移動量 `+0x6031c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdec10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec10.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdec10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec10.md)
- 新版 呼出元 1件 [`00c5b6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6d0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1fc.md#insn-00b0d218) · [`00b0d224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1fc.md#insn-00b0d224)
- 新版 [`00b6d534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d518.md#insn-00b6d534) · [`00b6d540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d518.md#insn-00b6d540)

~~~diff
- 00b0d218 ["INT_ADD", "register:40f0:8", ["const:b0d218:8", "const:4:8"]]
- 00b0d218 ["CALL", null, ["callee:00c5b6d0:8"]]
+ 00b6d534 ["INT_ADD", "register:40f0:8", ["const:b6d534:8", "const:4:8"]]
+ 00b6d534 ["CALL", null, ["callee:00c5b6d0:8"]]
- 00b0d218 bytes 7e460394
+ 00b6d534 bytes 67b80394
- 00b0d224 ["INT_ADD", "register:40f0:8", ["const:b0d224:8", "const:4:8"]]
- 00b0d224 ["CALL", null, ["callee:00c5b6d0:8"]]
+ 00b6d540 ["INT_ADD", "register:40f0:8", ["const:b6d540:8", "const:4:8"]]
+ 00b6d540 ["CALL", null, ["callee:00c5b6d0:8"]]
- 00b0d224 bytes 7b460394
+ 00b6d540 bytes 64b80394
~~~


<a id="compare-38b2e06136000bbcc68122256b2459d7"></a>

### [`00b0d390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d390.md) → [`00b6d6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x6031c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebd0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebd0.md)
- 新版 呼出元 1件 [`00c5b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b680.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d390.md#insn-00b0d3ac) · [`00b0d3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d390.md#insn-00b0d3b8) · [`00b0d3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d390.md#insn-00b0d3c8)
- 新版 [`00b6d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md#insn-00b6d6c8) · [`00b6d6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md#insn-00b6d6d4) · [`00b6d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6ac.md#insn-00b6d6e4)

~~~diff
- 00b0d3ac ["INT_ADD", "register:40f0:8", ["const:b0d3ac:8", "const:4:8"]]
- 00b0d3ac ["CALL", null, ["callee:00c5b680:8"]]
+ 00b6d6c8 ["INT_ADD", "register:40f0:8", ["const:b6d6c8:8", "const:4:8"]]
+ 00b6d6c8 ["CALL", null, ["callee:00c5b680:8"]]
- 00b0d3ac bytes 09460394
+ 00b6d6c8 bytes eeb70394
- 00b0d3b8 ["INT_ADD", "register:40f0:8", ["const:b0d3b8:8", "const:4:8"]]
- 00b0d3b8 ["CALL", null, ["callee:00c5b680:8"]]
+ 00b6d6d4 ["INT_ADD", "register:40f0:8", ["const:b6d6d4:8", "const:4:8"]]
+ 00b6d6d4 ["CALL", null, ["callee:00c5b680:8"]]
- 00b0d3b8 bytes 06460394
+ 00b6d6d4 bytes ebb70394
- 00b0d3c8 ["INT_ADD", "register:40f0:8", ["const:b0d3c8:8", "const:4:8"]]
- 00b0d3c8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b6d6e4 ["INT_ADD", "register:40f0:8", ["const:b6d6e4:8", "const:4:8"]]
+ 00b6d6e4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b0d3c8 bytes 26370394
+ 00b6d6e4 bytes f3a80394
~~~


<a id="compare-712e393af7365f9baae761d5dfb12c9b"></a>

### [`00b0d430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d430.md) → [`00b6d74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x6031c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb80.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb80.md)
- 新版 呼出元 1件 [`00c5b630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b630.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d430.md#insn-00b0d44c) · [`00b0d458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d430.md#insn-00b0d458) · [`00b0d468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d430.md#insn-00b0d468)
- 新版 [`00b6d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md#insn-00b6d768) · [`00b6d774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md#insn-00b6d774) · [`00b6d784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md#insn-00b6d784)

~~~diff
- 00b0d44c ["INT_ADD", "register:40f0:8", ["const:b0d44c:8", "const:4:8"]]
- 00b0d44c ["CALL", null, ["callee:00c5b630:8"]]
+ 00b6d768 ["INT_ADD", "register:40f0:8", ["const:b6d768:8", "const:4:8"]]
+ 00b6d768 ["CALL", null, ["callee:00c5b630:8"]]
- 00b0d44c bytes cd450394
+ 00b6d768 bytes b2b70394
- 00b0d458 ["INT_ADD", "register:40f0:8", ["const:b0d458:8", "const:4:8"]]
- 00b0d458 ["CALL", null, ["callee:00c5b630:8"]]
+ 00b6d774 ["INT_ADD", "register:40f0:8", ["const:b6d774:8", "const:4:8"]]
+ 00b6d774 ["CALL", null, ["callee:00c5b630:8"]]
- 00b0d458 bytes ca450394
+ 00b6d774 bytes afb70394
- 00b0d468 ["INT_ADD", "register:40f0:8", ["const:b0d468:8", "const:4:8"]]
- 00b0d468 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b6d784 ["INT_ADD", "register:40f0:8", ["const:b6d784:8", "const:4:8"]]
+ 00b6d784 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b0d468 bytes fe360394
+ 00b6d784 bytes cba80394
~~~


<a id="compare-0b25097587fa5194f73dd8c7946d1ddf"></a>

### [`00b0d564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d564.md) → [`00b6d898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdebc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebc0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebc0.md)
- 新版 呼出元 1件 [`00c5b670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b670.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d564.md#insn-00b0d580) · [`00b0d58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d564.md#insn-00b0d58c) · [`00b0d59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d564.md#insn-00b0d59c)
- 新版 [`00b6d8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md#insn-00b6d8b4) · [`00b6d8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md#insn-00b6d8c0) · [`00b6d8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md#insn-00b6d8d0)

~~~diff
- 00b0d580 ["INT_ADD", "register:40f0:8", ["const:b0d580:8", "const:4:8"]]
- 00b0d580 ["CALL", null, ["callee:00c5b670:8"]]
+ 00b6d8b4 ["INT_ADD", "register:40f0:8", ["const:b6d8b4:8", "const:4:8"]]
+ 00b6d8b4 ["CALL", null, ["callee:00c5b670:8"]]
- 00b0d580 bytes 90450394
+ 00b6d8b4 bytes 6fb70394
- 00b0d58c ["INT_ADD", "register:40f0:8", ["const:b0d58c:8", "const:4:8"]]
- 00b0d58c ["CALL", null, ["callee:00c5b670:8"]]
+ 00b6d8c0 ["INT_ADD", "register:40f0:8", ["const:b6d8c0:8", "const:4:8"]]
+ 00b6d8c0 ["CALL", null, ["callee:00c5b670:8"]]
- 00b0d58c bytes 8d450394
+ 00b6d8c0 bytes 6cb70394
- 00b0d59c ["INT_ADD", "register:40f0:8", ["const:b0d59c:8", "const:4:8"]]
- 00b0d59c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b6d8d0 ["INT_ADD", "register:40f0:8", ["const:b6d8d0:8", "const:4:8"]]
+ 00b6d8d0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b0d59c bytes b1360394
+ 00b6d8d0 bytes 78a80394
~~~


