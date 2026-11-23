# v15.7.4 → v16.0.0 · 要調査の変更候補 (14)

[一覧の目次](README.md)

<a id="compare-c30ba24aa92a63f4403e3efb2ece4abf"></a>

### [`0066eb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066eb10.md) → [`00694e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694e58.md) FUN_00694e58

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006683dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0066eb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066eb10.md#insn-0066eb30)
- 新版 `00694e78`（命令位置の公開資料なし）

~~~diff
- 0066eb30 ["INT_ADD", "register:40f0:8", ["const:66eb30:8", "const:4:8"]]
- 0066eb30 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00694e78 ["INT_ADD", "register:40f0:8", ["const:694e78:8", "const:4:8"]]
+ 00694e78 ["CALL", null, ["callee:00c57ab0:8"]]
- 0066eb30 bytes 4cb11594
+ 00694e78 bytes 0e0b1794
~~~


<a id="compare-70a413fbdf2f1d98d4ce2ad06c9ba10a"></a>

### [`0066f150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f150.md) → [`00695498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695498.md) FUN_00695498

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006683dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0066f170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f150.md#insn-0066f170)
- 新版 `006954b8`（命令位置の公開資料なし）

~~~diff
- 0066f170 ["INT_ADD", "register:40f0:8", ["const:66f170:8", "const:4:8"]]
- 0066f170 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006954b8 ["INT_ADD", "register:40f0:8", ["const:6954b8:8", "const:4:8"]]
+ 006954b8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0066f170 bytes bcaf1594
+ 006954b8 bytes 7e091794
~~~


<a id="compare-42846ffee535b7adb3bdb9cf89616c4a"></a>

### [`00678554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678554.md) → [`0069e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069e89c.md) FUN_0069e89c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 3件 [`0060ee24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060ee24.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 2件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`0063491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/0063491c.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00678564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678554.md#insn-00678564) · [`00678574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678554.md#insn-00678574)
- 新版 `0069e8ac`（命令位置の公開資料なし） · `0069e8bc`（命令位置の公開資料なし）

~~~diff
- 00678564 ["INT_ADD", "register:40f0:8", ["const:678564:8", "const:4:8"]]
- 00678564 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0069e8ac ["INT_ADD", "register:40f0:8", ["const:69e8ac:8", "const:4:8"]]
+ 0069e8ac ["CALL", null, ["callee:00c57ce0:8"]]
- 00678564 bytes 4b8b1594
+ 0069e8ac bytes 0de51694
- 00678574 ["INT_ADD", "register:40f0:8", ["const:678574:8", "const:4:8"]]
- 00678574 ["CALL", null, ["callee:0063491c:8"]]
+ 0069e8bc ["INT_ADD", "register:40f0:8", ["const:69e8bc:8", "const:4:8"]]
+ 0069e8bc ["CALL", null, ["callee:0063491c:8"]]
- 00678574 bytes 2c5afe97
+ 0069e8bc bytes 1858fe97
~~~


<a id="compare-5ea269cf7ad645838ebe026f0d7bc561"></a>

### [`0067b120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b120.md) → [`006a1468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1468.md) FUN_006a1468

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`0067b120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b120.md) [`00816bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816bf4.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 2件 [`0067b120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b120.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`006a1468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1468.md) [`008489ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008489ec.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`006a1468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1468.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0067b13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b120.md#insn-0067b13c) · [`0067b148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b120.md#insn-0067b148) · [`0067b158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b120.md#insn-0067b158)
- 新版 `006a1484`（命令位置の公開資料なし） · `006a1490`（命令位置の公開資料なし） · `006a14a0`（命令位置の公開資料なし）

~~~diff
- 0067b13c ["INT_ADD", "register:40f0:8", ["const:67b13c:8", "const:4:8"]]
- 0067b13c ["CALL", null, ["local:b0:8"]]
+ 006a1484 ["INT_ADD", "register:40f0:8", ["const:6a1484:8", "const:4:8"]]
+ 006a1484 ["CALL", null, ["local:b0:8"]]
- 0067b13c bytes f9ffff97
+ 006a1484 bytes f9ffff97
- 0067b148 ["INT_ADD", "register:40f0:8", ["const:67b148:8", "const:4:8"]]
- 0067b148 ["CALL", null, ["local:b0:8"]]
+ 006a1490 ["INT_ADD", "register:40f0:8", ["const:6a1490:8", "const:4:8"]]
+ 006a1490 ["CALL", null, ["local:b0:8"]]
- 0067b148 bytes f6ffff97
+ 006a1490 bytes f6ffff97
- 0067b158 ["INT_ADD", "register:40f0:8", ["const:67b158:8", "const:4:8"]]
- 0067b158 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006a14a0 ["INT_ADD", "register:40f0:8", ["const:6a14a0:8", "const:4:8"]]
+ 006a14a0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0067b158 bytes c27f1594
+ 006a14a0 bytes 84d91694
~~~


<a id="compare-0d95934da5486486bcfc8a669991221a"></a>

### [`0067b1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b1e8.md) → [`006a1530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1530.md) FUN_006a1530

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0067c708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c708.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006a2a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2a50.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0067b214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b1e8.md#insn-0067b214)
- 新版 `006a155c`（命令位置の公開資料なし）

~~~diff
- 0067b214 ["INT_ADD", "register:40f0:8", ["const:67b214:8", "const:4:8"]]
- 0067b214 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006a155c ["INT_ADD", "register:40f0:8", ["const:6a155c:8", "const:4:8"]]
+ 006a155c ["CALL", null, ["callee:00c57ab0:8"]]
- 0067b214 bytes 937f1594
+ 006a155c bytes 55d91694
~~~


<a id="compare-c8881fa827f32c473a10ba9fabc0a541"></a>

### [`0067c444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c444.md) → [`006a278c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a278c.md) FUN_006a278c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00678504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678504.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0067c560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c560.md) [`0067c708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c708.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0069e84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069e84c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`006a28a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a28a8.md) [`006a2a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2a50.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0067c4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c444.md#insn-0067c4a0) · [`0067c4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c444.md#insn-0067c4c8) · [`0067c4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c444.md#insn-0067c4f4)
- 新版 `006a27e8`（命令位置の公開資料なし） · `006a2810`（命令位置の公開資料なし） · `006a283c`（命令位置の公開資料なし）

~~~diff
- 0067c4a0 ["INT_ADD", "register:40f0:8", ["const:67c4a0:8", "const:4:8"]]
- 0067c4a0 ["CALL", null, ["callee:006a28a8:8"]]
+ 006a27e8 ["INT_ADD", "register:40f0:8", ["const:6a27e8:8", "const:4:8"]]
+ 006a27e8 ["CALL", null, ["callee:006a28a8:8"]]
- 0067c4a0 bytes 30000094
+ 006a27e8 bytes 30000094
- 0067c4c8 ["INT_ADD", "register:40f0:8", ["const:67c4c8:8", "const:4:8"]]
- 0067c4c8 ["CALL", null, ["callee:006a2a50:8"]]
+ 006a2810 ["INT_ADD", "register:40f0:8", ["const:6a2810:8", "const:4:8"]]
+ 006a2810 ["CALL", null, ["callee:006a2a50:8"]]
- 0067c4c8 bytes 90000094
+ 006a2810 bytes 90000094
- 0067c4f4 ["INT_ADD", "register:40f0:8", ["const:67c4f4:8", "const:4:8"]]
- 0067c4f4 ["CALL", null, ["callee:0043bb64:8"]]
+ 006a283c ["INT_ADD", "register:40f0:8", ["const:6a283c:8", "const:4:8"]]
+ 006a283c ["CALL", null, ["callee:0043bb64:8"]]
- 0067c4f4 bytes dc72f697
+ 006a283c bytes ca64f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d394fb1af62164b3998ef38fb3479f09"></a>

### [`0067c8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c8ac.md) → [`006a2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2bf4.md) FUN_006a2bf4

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0067c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c8ac.md#insn-0067c8ec)
- 新版 `006a2c34`（命令位置の公開資料なし）

~~~diff
- 0067c8ec ["COPY", "register:0:8", ["register:4040:8"]]
- 0067c8ec ["INT_ADD", "register:40f0:8", ["const:67c8ec:8", "const:4:8"]]
- 0067c8ec ["CALLIND", null, ["register:0:8"]]
+ 006a2c34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006a2c34 ["INT_ADD", "register:40f0:8", ["const:6a2c34:8", "const:4:8"]]
+ 006a2c34 ["CALLIND", null, ["register:0:8"]]
- 0067c8ec bytes 00013fd6
+ 006a2c34 bytes 00013fd6
~~~


<a id="compare-56290009c41684917222fc2a43606190"></a>

### [`006993f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/006993f0.md) → [`006bf754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf754.md) FUN_006bf754

採用 · 移動量 `+0x26364` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00699424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/006993f0.md#insn-00699424) · [`0069942c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/006993f0.md#insn-0069942c)
- 新版 `006bf788`（命令位置の公開資料なし） · `006bf790`（命令位置の公開資料なし）

~~~diff
- 00699424 ["INT_ADD", "register:40f0:8", ["const:699424:8", "const:4:8"]]
- 00699424 ["CALL", null, ["callee:005c175c:8"]]
+ 006bf788 ["INT_ADD", "register:40f0:8", ["const:6bf788:8", "const:4:8"]]
+ 006bf788 ["CALL", null, ["callee:005c175c:8"]]
- 00699424 bytes 420ffc97
+ 006bf788 bytes f507fc97
- 0069942c ["INT_ADD", "register:40f0:8", ["const:69942c:8", "const:4:8"]]
- 0069942c ["CALL", null, ["callee:00c57ab0:8"]]
+ 006bf790 ["INT_ADD", "register:40f0:8", ["const:6bf790:8", "const:4:8"]]
+ 006bf790 ["CALL", null, ["callee:00c57ab0:8"]]
- 0069942c bytes 0d071594
+ 006bf790 bytes c8601694
~~~


<a id="compare-734dc5f5b3af154ade4d925958c71c77"></a>

### [`00699448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699448.md) → [`006bf7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf7ac.md) FUN_006bf7ac

採用 · 移動量 `+0x26364` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00699474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699448.md#insn-00699474)
- 新版 `006bf7d8`（命令位置の公開資料なし）

~~~diff
- 00699474 ["INT_ADD", "register:40f0:8", ["const:699474:8", "const:4:8"]]
- 00699474 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006bf7d8 ["INT_ADD", "register:40f0:8", ["const:6bf7d8:8", "const:4:8"]]
+ 006bf7d8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00699474 bytes fb061594
+ 006bf7d8 bytes b6601694
~~~


<a id="compare-1d829970546004257e7a7a4c5a202b60"></a>

### [`00699490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699490.md) → [`006bf7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf7f4.md) FUN_006bf7f4

採用 · 移動量 `+0x26364` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 2件 [`005d9598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9598.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 2件 [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006994c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699490.md#insn-006994c4) · [`006994cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699490.md#insn-006994cc)
- 新版 `006bf828`（命令位置の公開資料なし） · `006bf830`（命令位置の公開資料なし）

~~~diff
- 006994c4 ["INT_ADD", "register:40f0:8", ["const:6994c4:8", "const:4:8"]]
- 006994c4 ["CALL", null, ["callee:005fe258:8"]]
+ 006bf828 ["INT_ADD", "register:40f0:8", ["const:6bf828:8", "const:4:8"]]
+ 006bf828 ["CALL", null, ["callee:005fe258:8"]]
- 006994c4 bytes 3500fd97
+ 006bf828 bytes 8cfafc97
- 006994cc ["INT_ADD", "register:40f0:8", ["const:6994cc:8", "const:4:8"]]
- 006994cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 006bf830 ["INT_ADD", "register:40f0:8", ["const:6bf830:8", "const:4:8"]]
+ 006bf830 ["CALL", null, ["callee:00c57ab0:8"]]
- 006994cc bytes e5061594
+ 006bf830 bytes a0601694
~~~


<a id="compare-8d0149c3df3ffdd4e5c94a20a92e01b6"></a>

### [`0069aaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069aaf8.md) → [`006c0e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0e5c.md) FUN_006c0e5c

採用 · 移動量 `+0x26364` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 1件 [`0044d208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d208.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069ab28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069aaf8.md#insn-0069ab28) · [`0069ab3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069aaf8.md#insn-0069ab3c)
- 新版 `006c0e8c`（命令位置の公開資料なし） · `006c0ea0`（命令位置の公開資料なし）

~~~diff
- 0069ab28 ["INT_ADD", "register:40f0:8", ["const:69ab28:8", "const:4:8"]]
- 0069ab28 ["CALL", null, ["callee:004700a0:8"]]
+ 006c0e8c ["INT_ADD", "register:40f0:8", ["const:6c0e8c:8", "const:4:8"]]
+ 006c0e8c ["CALL", null, ["callee:004700a0:8"]]
- 0069ab28 bytes b8c9f697
+ 006c0e8c bytes 85bcf697
- 0069ab3c ["INT_ADD", "register:40f0:8", ["const:69ab3c:8", "const:4:8"]]
- 0069ab3c ["CALL", null, ["callee:004700a0:8"]]
+ 006c0ea0 ["INT_ADD", "register:40f0:8", ["const:6c0ea0:8", "const:4:8"]]
+ 006c0ea0 ["CALL", null, ["callee:004700a0:8"]]
- 0069ab3c bytes b3c9f697
+ 006c0ea0 bytes 80bcf697
~~~


<a id="compare-6d3dcf4967e4158e5c40a3d6879a4351"></a>

### [`0069cd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069cd18.md) → [`006c307c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c307c.md) FUN_006c307c

採用 · 移動量 `+0x26364` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 1件 [`0069ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ced4.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069cd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069cd18.md#insn-0069cd3c)
- 新版 `006c30a0`（命令位置の公開資料なし）

~~~diff
- 0069cd3c ["INT_ADD", "register:40f0:8", ["const:69cd3c:8", "const:4:8"]]
- 0069cd3c ["CALL", null, ["callee:006c3238:8"]]
+ 006c30a0 ["INT_ADD", "register:40f0:8", ["const:6c30a0:8", "const:4:8"]]
+ 006c30a0 ["CALL", null, ["callee:006c3238:8"]]
- 0069cd3c bytes 66000094
+ 006c30a0 bytes 66000094
~~~


<a id="compare-6557a3f95e1b00456318a7c09b4f3240"></a>

### [`0069cd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069cd4c.md) → [`006c30b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c30b0.md) FUN_006c30b0

採用 · 移動量 `+0x26364` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00625684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00625/00625684.md) [`006bf5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md) · 呼出先 1件 [`0069ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ced4.md)
- 新版 呼出元 2件 [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) [`006e9364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9364.md) · 呼出先 1件 [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069cd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069cd4c.md#insn-0069cd64)
- 新版 `006c30c8`（命令位置の公開資料なし）

~~~diff
- 0069cd64 ["INT_ADD", "register:40f0:8", ["const:69cd64:8", "const:4:8"]]
- 0069cd64 ["CALL", null, ["callee:006c3238:8"]]
+ 006c30c8 ["INT_ADD", "register:40f0:8", ["const:6c30c8:8", "const:4:8"]]
+ 006c30c8 ["CALL", null, ["callee:006c3238:8"]]
- 0069cd64 bytes 5c000094
+ 006c30c8 bytes 5c000094
~~~


<a id="compare-19e5f012dd1c97b85c8feb11ae839980"></a>

### [`0069ce10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ce10.md) → [`006c3174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3174.md) FUN_006c3174

採用 · 移動量 `+0x26364` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 1件 [`0069ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ced4.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069ce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ce10.md#insn-0069ce40)
- 新版 `006c31a4`（命令位置の公開資料なし）

~~~diff
- 0069ce40 ["INT_ADD", "register:40f0:8", ["const:69ce40:8", "const:4:8"]]
- 0069ce40 ["CALL", null, ["callee:006c3238:8"]]
+ 006c31a4 ["INT_ADD", "register:40f0:8", ["const:6c31a4:8", "const:4:8"]]
+ 006c31a4 ["CALL", null, ["callee:006c3238:8"]]
- 0069ce40 bytes 25000094
+ 006c31a4 bytes 25000094
~~~


<a id="compare-1b86e9a85bed391186712c5b63547dfc"></a>

### [`0069ce5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ce5c.md) → [`006c31c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c31c0.md) FUN_006c31c0

採用 · 移動量 `+0x26364` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006bbf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`008bf94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bf/008bf94c.md) · 呼出先 1件 [`0069ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ced4.md)
- 新版 呼出元 3件 [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`008f380c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f380c.md) · 呼出先 1件 [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069ce78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ce5c.md#insn-0069ce78)
- 新版 `006c31dc`（命令位置の公開資料なし）

~~~diff
- 0069ce78 ["INT_ADD", "register:40f0:8", ["const:69ce78:8", "const:4:8"]]
- 0069ce78 ["CALL", null, ["callee:006c3238:8"]]
+ 006c31dc ["INT_ADD", "register:40f0:8", ["const:6c31dc:8", "const:4:8"]]
+ 006c31dc ["CALL", null, ["callee:006c3238:8"]]
- 0069ce78 bytes 17000094
+ 006c31dc bytes 17000094
~~~


<a id="compare-2194fa5d3fec5b7f680218163fa45a98"></a>

### [`0069ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ce88.md) → [`006c31ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c31ec.md) FUN_006c31ec

採用 · 移動量 `+0x26364` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) · 呼出先 1件 [`0069ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ced4.md)
- 新版 呼出元 1件 [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) · 呼出先 1件 [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069cea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ce88.md#insn-0069cea0)
- 新版 `006c3204`（命令位置の公開資料なし）

~~~diff
- 0069cea0 ["INT_ADD", "register:40f0:8", ["const:69cea0:8", "const:4:8"]]
- 0069cea0 ["CALL", null, ["callee:006c3238:8"]]
+ 006c3204 ["INT_ADD", "register:40f0:8", ["const:6c3204:8", "const:4:8"]]
+ 006c3204 ["CALL", null, ["callee:006c3238:8"]]
- 0069cea0 bytes 0d000094
+ 006c3204 bytes 0d000094
~~~


<a id="compare-2caf51faa228afb148f890a0b5b37e14"></a>

### [`0069ceb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ceb0.md) → [`006c3214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3214.md) FUN_006c3214

採用 · 移動量 `+0x26364` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00625684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00625/00625684.md) [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) [`006bf5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`0069ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ced4.md)
- 新版 呼出元 6件 [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`006e9364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9364.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 1件 [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069cec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ceb0.md#insn-0069cec4)
- 新版 `006c3228`（命令位置の公開資料なし）

~~~diff
- 0069cec4 ["INT_ADD", "register:40f0:8", ["const:69cec4:8", "const:4:8"]]
- 0069cec4 ["CALL", null, ["callee:006c3238:8"]]
+ 006c3228 ["INT_ADD", "register:40f0:8", ["const:6c3228:8", "const:4:8"]]
+ 006c3228 ["CALL", null, ["callee:006c3238:8"]]
- 0069cec4 bytes 04000094
+ 006c3228 bytes 04000094
~~~


<a id="compare-9d41e83942a8e1159602d9edabda4c5a"></a>

### [`0069d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069d8e0.md) → [`006c3c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3c44.md) FUN_006c3c44

採用 · 移動量 `+0x26364` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 2件 [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 2件 [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069d91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069d8e0.md#insn-0069d91c) · [`0069d948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069d8e0.md#insn-0069d948) · [`0069d958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069d8e0.md#insn-0069d958)
- 新版 `006c3c80`（命令位置の公開資料なし） · `006c3cac`（命令位置の公開資料なし） · `006c3cbc`（命令位置の公開資料なし）

~~~diff
- 0069d91c ["COPY", "register:0:8", ["register:4048:8"]]
- 0069d91c ["INT_ADD", "register:40f0:8", ["const:69d91c:8", "const:4:8"]]
- 0069d91c ["CALLIND", null, ["register:0:8"]]
+ 006c3c80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 006c3c80 ["INT_ADD", "register:40f0:8", ["const:6c3c80:8", "const:4:8"]]
+ 006c3c80 ["CALLIND", null, ["register:0:8"]]
- 0069d91c bytes 20013fd6
+ 006c3c80 bytes 20013fd6
- 0069d948 ["COPY", "register:0:8", ["register:4040:8"]]
- 0069d948 ["INT_ADD", "register:40f0:8", ["const:69d948:8", "const:4:8"]]
- 0069d948 ["CALLIND", null, ["register:0:8"]]
+ 006c3cac ["COPY", "register:0:8", ["register:4040:8"]]
+ 006c3cac ["INT_ADD", "register:40f0:8", ["const:6c3cac:8", "const:4:8"]]
+ 006c3cac ["CALLIND", null, ["register:0:8"]]
- 0069d948 bytes 00013fd6
+ 006c3cac bytes 00013fd6
- 0069d958 ["INT_ADD", "register:40f0:8", ["const:69d958:8", "const:4:8"]]
- 0069d958 ["CALL", null, ["callee:0057be68:8"]]
+ 006c3cbc ["INT_ADD", "register:40f0:8", ["const:6c3cbc:8", "const:4:8"]]
+ 006c3cbc ["CALL", null, ["callee:0057be68:8"]]
- 0069d958 bytes 9eedfa97
+ 006c3cbc bytes 6be0fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c6b3053d5502ca9e931a68565f3e686"></a>

### [`0069de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de1c.md) → [`006c4180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4180.md) FUN_006c4180

採用 · 移動量 `+0x26364` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00624e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624e6c.md) [`0069de94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de94.md) [`006bed50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bed50.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 3件 [`0064a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a950.md) [`006c41f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c41f8.md) [`006e8b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8b14.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0069de60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de1c.md#insn-0069de60) · [`0069de74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de1c.md#insn-0069de74) · [`0069de7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de1c.md#insn-0069de7c)
- 新版 `006c41c4`（命令位置の公開資料なし） · `006c41d8`（命令位置の公開資料なし） · `006c41e0`（命令位置の公開資料なし）

~~~diff
- 0069de60 ["INT_ADD", "register:40f0:8", ["const:69de60:8", "const:4:8"]]
- 0069de60 ["CALL", null, ["callee:00c538e0:8"]]
+ 006c41c4 ["INT_ADD", "register:40f0:8", ["const:6c41c4:8", "const:4:8"]]
+ 006c41c4 ["CALL", null, ["callee:00c538e0:8"]]
- 0069de60 bytes 0ce41494
+ 006c41c4 bytes c73d1694
- 0069de74 ["COPY", "register:0:8", ["register:4040:8"]]
- 0069de74 ["INT_ADD", "register:40f0:8", ["const:69de74:8", "const:4:8"]]
- 0069de74 ["CALLIND", null, ["register:0:8"]]
+ 006c41d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006c41d8 ["INT_ADD", "register:40f0:8", ["const:6c41d8:8", "const:4:8"]]
+ 006c41d8 ["CALLIND", null, ["register:0:8"]]
- 0069de74 bytes 00013fd6
+ 006c41d8 bytes 00013fd6
- 0069de7c ["INT_ADD", "register:40f0:8", ["const:69de7c:8", "const:4:8"]]
- 0069de7c ["CALL", null, ["callee:00c57a80:8"]]
+ 006c41e0 ["INT_ADD", "register:40f0:8", ["const:6c41e0:8", "const:4:8"]]
+ 006c41e0 ["CALL", null, ["callee:00c57a80:8"]]
- 0069de7c bytes 6df41494
+ 006c41e0 bytes 284e1694
~~~


<a id="compare-c53f8e4be3285e72b3affab3a510ec83"></a>

### [`006a70c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a70c8.md) → [`006d020c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d020c.md) FUN_006d020c

採用 · 移動量 `+0x29144` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006a70e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a70c8.md#insn-006a70e8) · [`006a70f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a70c8.md#insn-006a70f8)
- 新版 `006d022c`（命令位置の公開資料なし） · `006d023c`（命令位置の公開資料なし）

~~~diff
- 006a70e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 006a70e8 ["INT_ADD", "register:40f0:8", ["const:6a70e8:8", "const:4:8"]]
- 006a70e8 ["CALLIND", null, ["register:0:8"]]
+ 006d022c ["COPY", "register:0:8", ["register:4040:8"]]
+ 006d022c ["INT_ADD", "register:40f0:8", ["const:6d022c:8", "const:4:8"]]
+ 006d022c ["CALLIND", null, ["register:0:8"]]
- 006a70e8 bytes 00013fd6
+ 006d022c bytes 00013fd6
- 006a70f8 ["INT_ADD", "register:40f0:8", ["const:6a70f8:8", "const:4:8"]]
- 006a70f8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006d023c ["INT_ADD", "register:40f0:8", ["const:6d023c:8", "const:4:8"]]
+ 006d023c ["CALL", null, ["callee:00c57ab0:8"]]
- 006a70f8 bytes dacf1494
+ 006d023c bytes 1d1e1694
~~~


<a id="compare-6407f7fb3325781280cc50444e320e34"></a>

### [`006ad268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad268.md) → [`006d7024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7024.md) FUN_006d7024

採用 · 移動量 `+0x29dbc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)
- 新版 呼出元 1件 [`006cfeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ad278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad268.md#insn-006ad278)
- 新版 `006d7034`（命令位置の公開資料なし）

~~~diff
- 006ad278 ["INT_ADD", "register:40f0:8", ["const:6ad278:8", "const:4:8"]]
- 006ad278 ["CALL", null, ["callee:00c5a480:8"]]
+ 006d7034 ["INT_ADD", "register:40f0:8", ["const:6d7034:8", "const:4:8"]]
+ 006d7034 ["CALL", null, ["callee:00c5a480:8"]]
- 006ad278 bytes eec11494
+ 006d7034 bytes 130d1694
~~~


<a id="compare-c4f9fb9be0553acda1d1c2de5b49d685"></a>

### [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) → [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) FUN_006d76a4

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) [`007c1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1c70.md) [`00b75d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75d7c.md) [`00b75dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75dfc.md) [`00b9a790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a790.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 13件 [`006d7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md) [`007f3e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md) [`00bf27c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf27c4.md) [`00bf2844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2844.md) [`00c171d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c171d8.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ad94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md#insn-006ad94c) · [`006ad978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md#insn-006ad978) · [`006ad97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md#insn-006ad97c)
- 新版 `006d7708`（命令位置の公開資料なし） · `006d7734`（命令位置の公開資料なし） · `006d7738`（命令位置の公開資料なし）

~~~diff
- 006ad94c ["INT_ADD", "register:40f0:8", ["const:6ad94c:8", "const:4:8"]]
- 006ad94c ["CALL", null, ["callee:00c57a90:8"]]
+ 006d7708 ["INT_ADD", "register:40f0:8", ["const:6d7708:8", "const:4:8"]]
+ 006d7708 ["CALL", null, ["callee:00c57a90:8"]]
- 006ad94c bytes bdb51494
+ 006d7708 bytes e2001694
- 006ad978 ["INT_ADD", "register:40f0:8", ["const:6ad978:8", "const:4:8"]]
- 006ad978 ["CALL", null, ["callee:006d7660:8"]]
+ 006d7734 ["INT_ADD", "register:40f0:8", ["const:6d7734:8", "const:4:8"]]
+ 006d7734 ["CALL", null, ["callee:006d7660:8"]]
- 006ad978 bytes cbffff97
+ 006d7734 bytes cbffff97
- 006ad97c ["INT_ADD", "register:40f0:8", ["const:6ad97c:8", "const:4:8"]]
- 006ad97c ["CALL", null, ["callee:00440e80:8"]]
+ 006d7738 ["INT_ADD", "register:40f0:8", ["const:6d7738:8", "const:4:8"]]
+ 006d7738 ["CALL", null, ["callee:00440e80:8"]]
- 006ad97c bytes 81c2f597
+ 006d7738 bytes d2a5f597
~~~


<a id="compare-b30daae8a6c242bb90eb7600900318c8"></a>

### [`006b1158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1158.md) → [`006daf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006daf14.md) FUN_006daf14

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 1件 [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b11cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1158.md#insn-006b11cc)
- 新版 `006daf88`（命令位置の公開資料なし）

~~~diff
- 006b11cc ["INT_ADD", "register:40f0:8", ["const:6b11cc:8", "const:4:8"]]
- 006b11cc ["CALL", null, ["callee:0046d770:8"]]
+ 006daf88 ["INT_ADD", "register:40f0:8", ["const:6daf88:8", "const:4:8"]]
+ 006daf88 ["CALL", null, ["callee:0046d770:8"]]
- 006b11cc bytes c365f697
+ 006daf88 bytes fa49f697
~~~


<a id="compare-fb1e3c1cc3d05193270a42974583fd30"></a>

### [`006b1220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1220.md) → [`006dafdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dafdc.md) FUN_006dafdc

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 4件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md) [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 4件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b1240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1220.md#insn-006b1240) · [`006b124c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1220.md#insn-006b124c) · [`006b1258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1220.md#insn-006b1258)
- 新版 `006daffc`（命令位置の公開資料なし） · `006db008`（命令位置の公開資料なし） · `006db014`（命令位置の公開資料なし）

~~~diff
- 006b1240 ["INT_ADD", "register:40f0:8", ["const:6b1240:8", "const:4:8"]]
- 006b1240 ["CALL", null, ["callee:00480b50:8"]]
+ 006daffc ["INT_ADD", "register:40f0:8", ["const:6daffc:8", "const:4:8"]]
+ 006daffc ["CALL", null, ["callee:00480b50:8"]]
- 006b1240 bytes 9eb2f697
+ 006daffc bytes d596f697
- 006b124c ["INT_ADD", "register:40f0:8", ["const:6b124c:8", "const:4:8"]]
- 006b124c ["CALL", null, ["callee:00481058:8"]]
+ 006db008 ["INT_ADD", "register:40f0:8", ["const:6db008:8", "const:4:8"]]
+ 006db008 ["CALL", null, ["callee:00481058:8"]]
- 006b124c bytes ddb3f697
+ 006db008 bytes 1498f697
- 006b1258 ["INT_ADD", "register:40f0:8", ["const:6b1258:8", "const:4:8"]]
- 006b1258 ["CALL", null, ["callee:00480af8:8"]]
+ 006db014 ["INT_ADD", "register:40f0:8", ["const:6db014:8", "const:4:8"]]
+ 006db014 ["CALL", null, ["callee:00480af8:8"]]
- 006b1258 bytes 82b2f697
+ 006db014 bytes b996f697
~~~


<a id="compare-215fd71b65d8be0bef984709a3db4cf6"></a>

### [`006b1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md) → [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) FUN_006db02c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 4件 [`0045d240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md) [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md) [`0045d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md) [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 4件 [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b1288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md#insn-006b1288) · [`006b1298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md#insn-006b1298) · [`006b12a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1270.md#insn-006b12a4)
- 新版 `006db044`（命令位置の公開資料なし） · `006db054`（命令位置の公開資料なし） · `006db060`（命令位置の公開資料なし）

~~~diff
- 006b1288 ["INT_ADD", "register:40f0:8", ["const:6b1288:8", "const:4:8"]]
- 006b1288 ["CALL", null, ["callee:00480138:8"]]
+ 006db044 ["INT_ADD", "register:40f0:8", ["const:6db044:8", "const:4:8"]]
+ 006db044 ["CALL", null, ["callee:00480138:8"]]
- 006b1288 bytes 06b0f697
+ 006db044 bytes 3d94f697
- 006b1298 ["INT_ADD", "register:40f0:8", ["const:6b1298:8", "const:4:8"]]
- 006b1298 ["CALL", null, ["callee:00480704:8"]]
+ 006db054 ["INT_ADD", "register:40f0:8", ["const:6db054:8", "const:4:8"]]
+ 006db054 ["CALL", null, ["callee:00480704:8"]]
- 006b1298 bytes 75b1f697
+ 006db054 bytes ac95f697
- 006b12a4 ["INT_ADD", "register:40f0:8", ["const:6b12a4:8", "const:4:8"]]
- 006b12a4 ["CALL", null, ["callee:004800d8:8"]]
+ 006db060 ["INT_ADD", "register:40f0:8", ["const:6db060:8", "const:4:8"]]
+ 006db060 ["CALL", null, ["callee:004800d8:8"]]
- 006b12a4 bytes e7aff697
+ 006db060 bytes 1e94f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-654b5dbe23f6b1d6ffebaa1afc82cb5b"></a>

### [`006b2880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2880.md) → [`006dc63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc63c.md) FUN_006dc63c

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 1件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b2898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2880.md#insn-006b2898)
- 新版 `006dc654`（命令位置の公開資料なし）

~~~diff
- 006b2898 ["INT_ADD", "register:40f0:8", ["const:6b2898:8", "const:4:8"]]
- 006b2898 ["CALL", null, ["callee:005c175c:8"]]
+ 006dc654 ["INT_ADD", "register:40f0:8", ["const:6dc654:8", "const:4:8"]]
+ 006dc654 ["CALL", null, ["callee:005c175c:8"]]
- 006b2898 bytes 25aafb97
+ 006dc654 bytes 4294fb97
~~~


<a id="compare-d96c65c5be1add6cb8280c71d011dd08"></a>

### [`006b65b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b65b8.md) → [`006e0374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e0374.md) FUN_006e0374

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b65f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b65b8.md#insn-006b65f8) · [`006b6608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b65b8.md#insn-006b6608) · [`006b6618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b65b8.md#insn-006b6618)
- 新版 `006e03b4`（命令位置の公開資料なし） · `006e03c4`（命令位置の公開資料なし） · `006e03d4`（命令位置の公開資料なし）

~~~diff
- 006b65f8 ["INT_ADD", "register:40f0:8", ["const:6b65f8:8", "const:4:8"]]
- 006b65f8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006e03b4 ["INT_ADD", "register:40f0:8", ["const:6e03b4:8", "const:4:8"]]
+ 006e03b4 ["CALL", null, ["callee:00c57ab0:8"]]
- 006b65f8 bytes 9a921494
+ 006e03b4 bytes bfdd1594
- 006b6608 ["INT_ADD", "register:40f0:8", ["const:6b6608:8", "const:4:8"]]
- 006b6608 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006e03c4 ["INT_ADD", "register:40f0:8", ["const:6e03c4:8", "const:4:8"]]
+ 006e03c4 ["CALL", null, ["callee:00c57ab0:8"]]
- 006b6608 bytes 96921494
+ 006e03c4 bytes bbdd1594
- 006b6618 ["INT_ADD", "register:40f0:8", ["const:6b6618:8", "const:4:8"]]
- 006b6618 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006e03d4 ["INT_ADD", "register:40f0:8", ["const:6e03d4:8", "const:4:8"]]
+ 006e03d4 ["CALL", null, ["callee:00c57ab0:8"]]
- 006b6618 bytes 92921494
+ 006e03d4 bytes b7dd1594
~~~


<a id="compare-9eaadba61bcccbb860887c6fcab6957a"></a>

### [`006b6634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6634.md) → [`006e03f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e03f0.md) FUN_006e03f0

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b6674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6634.md#insn-006b6674) · [`006b6684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6634.md#insn-006b6684) · [`006b6694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6634.md#insn-006b6694)
- 新版 `006e0430`（命令位置の公開資料なし） · `006e0440`（命令位置の公開資料なし） · `006e0450`（命令位置の公開資料なし）

~~~diff
- 006b6674 ["INT_ADD", "register:40f0:8", ["const:6b6674:8", "const:4:8"]]
- 006b6674 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006e0430 ["INT_ADD", "register:40f0:8", ["const:6e0430:8", "const:4:8"]]
+ 006e0430 ["CALL", null, ["callee:00c57ab0:8"]]
- 006b6674 bytes 7b921494
+ 006e0430 bytes a0dd1594
- 006b6684 ["INT_ADD", "register:40f0:8", ["const:6b6684:8", "const:4:8"]]
- 006b6684 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006e0440 ["INT_ADD", "register:40f0:8", ["const:6e0440:8", "const:4:8"]]
+ 006e0440 ["CALL", null, ["callee:00c57ab0:8"]]
- 006b6684 bytes 77921494
+ 006e0440 bytes 9cdd1594
- 006b6694 ["INT_ADD", "register:40f0:8", ["const:6b6694:8", "const:4:8"]]
- 006b6694 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006e0450 ["INT_ADD", "register:40f0:8", ["const:6e0450:8", "const:4:8"]]
+ 006e0450 ["CALL", null, ["callee:00c57ab0:8"]]
- 006b6694 bytes 73921494
+ 006e0450 bytes 98dd1594
~~~


<a id="compare-fe0a22d7c5c2887e097feeb81a1d103c"></a>

### [`006b678c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b678c.md) → [`006e0548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e0548.md) FUN_006e0548

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b67bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b678c.md#insn-006b67bc) · [`006b67d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b678c.md#insn-006b67d4) · [`006b67f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b678c.md#insn-006b67f0)
- 新版 `006e0578`（命令位置の公開資料なし） · `006e0590`（命令位置の公開資料なし） · `006e05ac`（命令位置の公開資料なし）

~~~diff
- 006b67bc ["INT_ADD", "register:40f0:8", ["const:6b67bc:8", "const:4:8"]]
- 006b67bc ["CALL", null, ["callee:00c57a90:8"]]
+ 006e0578 ["INT_ADD", "register:40f0:8", ["const:6e0578:8", "const:4:8"]]
+ 006e0578 ["CALL", null, ["callee:00c57a90:8"]]
- 006b67bc bytes 21921494
+ 006e0578 bytes 46dd1594
- 006b67d4 ["INT_ADD", "register:40f0:8", ["const:6b67d4:8", "const:4:8"]]
- 006b67d4 ["CALL", null, ["callee:00c57c00:8"]]
+ 006e0590 ["INT_ADD", "register:40f0:8", ["const:6e0590:8", "const:4:8"]]
+ 006e0590 ["CALL", null, ["callee:00c57c00:8"]]
- 006b67d4 bytes 77921494
+ 006e0590 bytes 9cdd1594
- 006b67f0 ["INT_ADD", "register:40f0:8", ["const:6b67f0:8", "const:4:8"]]
- 006b67f0 ["CALL", null, ["callee:00470800:8"]]
+ 006e05ac ["INT_ADD", "register:40f0:8", ["const:6e05ac:8", "const:4:8"]]
+ 006e05ac ["CALL", null, ["callee:00470800:8"]]
- 006b67f0 bytes 5e5cf697
+ 006e05ac bytes 9540f697
~~~


<a id="compare-147c0cf750f2c09573e3df54bdc3ab6d"></a>

### [`006b7e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7e84.md) → [`006e1c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1c40.md) FUN_006e1c40

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006b77e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`006e15a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e15a0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b7ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7e84.md#insn-006b7ed0) · [`006b7efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7e84.md#insn-006b7efc) · [`006b7f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7e84.md#insn-006b7f28)
- 新版 `006e1c8c`（命令位置の公開資料なし） · `006e1cb8`（命令位置の公開資料なし） · `006e1ce4`（命令位置の公開資料なし）

~~~diff
- 006b7ed0 ["INT_ADD", "register:40f0:8", ["const:6b7ed0:8", "const:4:8"]]
- 006b7ed0 ["CALL", null, ["callee:0043bae0:8"]]
+ 006e1c8c ["INT_ADD", "register:40f0:8", ["const:6e1c8c:8", "const:4:8"]]
+ 006e1c8c ["CALL", null, ["callee:0043bae0:8"]]
- 006b7ed0 bytes 4484f597
+ 006e1c8c bytes 9567f597
- 006b7efc ["INT_ADD", "register:40f0:8", ["const:6b7efc:8", "const:4:8"]]
- 006b7efc ["CALL", null, ["callee:0043bae0:8"]]
+ 006e1cb8 ["INT_ADD", "register:40f0:8", ["const:6e1cb8:8", "const:4:8"]]
+ 006e1cb8 ["CALL", null, ["callee:0043bae0:8"]]
- 006b7efc bytes 3984f597
+ 006e1cb8 bytes 8a67f597
- 006b7f28 ["INT_ADD", "register:40f0:8", ["const:6b7f28:8", "const:4:8"]]
- 006b7f28 ["CALL", null, ["callee:0043bae0:8"]]
+ 006e1ce4 ["INT_ADD", "register:40f0:8", ["const:6e1ce4:8", "const:4:8"]]
+ 006e1ce4 ["CALL", null, ["callee:0043bae0:8"]]
- 006b7f28 bytes 2e84f597
+ 006e1ce4 bytes 7f67f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c18dcf31b7c18d9b2d8dd16b6a86116"></a>

### [`006c0008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0008.md) → [`006e9dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9dcc.md) FUN_006e9dcc

採用 · 移動量 `+0x29dc4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) [`00957320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957320.md) · 呼出先 1件 [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)
- 新版 呼出元 4件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`0098cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md) · 呼出先 1件 [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c0038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0008.md#insn-006c0038)
- 新版 `006e9dfc`（命令位置の公開資料なし）

~~~diff
- 006c0038 ["INT_ADD", "register:40f0:8", ["const:6c0038:8", "const:4:8"]]
- 006c0038 ["CALL", null, ["callee:00c58bd0:8"]]
+ 006e9dfc ["INT_ADD", "register:40f0:8", ["const:6e9dfc:8", "const:4:8"]]
+ 006e9dfc ["CALL", null, ["callee:00c58bd0:8"]]
- 006c0038 bytes 52701494
+ 006e9dfc bytes 75bb1594
~~~


<a id="compare-b52dd029be828d4debabb23c428bb53e"></a>

### [`006c28c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c28c8.md) → [`006ec68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ec/006ec68c.md) FUN_006ec68c

採用 · 移動量 `+0x29dc4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c28f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c28c8.md#insn-006c28f0) · [`006c2904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c28c8.md#insn-006c2904) · [`006c290c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c28c8.md#insn-006c290c)
- 新版 `006ec6b4`（命令位置の公開資料なし） · `006ec6c8`（命令位置の公開資料なし） · `006ec6d0`（命令位置の公開資料なし）

~~~diff
- 006c28f0 ["INT_ADD", "register:40f0:8", ["const:6c28f0:8", "const:4:8"]]
- 006c28f0 ["CALL", null, ["callee:00c538e0:8"]]
+ 006ec6b4 ["INT_ADD", "register:40f0:8", ["const:6ec6b4:8", "const:4:8"]]
+ 006ec6b4 ["CALL", null, ["callee:00c538e0:8"]]
- 006c28f0 bytes 68511494
+ 006ec6b4 bytes 8b9c1594
- 006c2904 ["COPY", "register:0:8", ["register:4040:8"]]
- 006c2904 ["INT_ADD", "register:40f0:8", ["const:6c2904:8", "const:4:8"]]
- 006c2904 ["CALLIND", null, ["register:0:8"]]
+ 006ec6c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006ec6c8 ["INT_ADD", "register:40f0:8", ["const:6ec6c8:8", "const:4:8"]]
+ 006ec6c8 ["CALLIND", null, ["register:0:8"]]
- 006c2904 bytes 00013fd6
+ 006ec6c8 bytes 00013fd6
- 006c290c ["INT_ADD", "register:40f0:8", ["const:6c290c:8", "const:4:8"]]
- 006c290c ["CALL", null, ["callee:00c57a80:8"]]
+ 006ec6d0 ["INT_ADD", "register:40f0:8", ["const:6ec6d0:8", "const:4:8"]]
+ 006ec6d0 ["CALL", null, ["callee:00c57a80:8"]]
- 006c290c bytes c9611494
+ 006ec6d0 bytes ecac1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5420c931a88b58baefeff5ef4f384733"></a>

### [`006c77bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c77bc.md) → [`006f1580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1580.md) FUN_006f1580

採用 · 移動量 `+0x29dc4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 9件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c7824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c77bc.md#insn-006c7824) · [`006c785c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c77bc.md#insn-006c785c)
- 新版 `006f15e8`（命令位置の公開資料なし） · `006f1620`（命令位置の公開資料なし）

~~~diff
- 006c7824 ["INT_ADD", "register:40f0:8", ["const:6c7824:8", "const:4:8"]]
- 006c7824 ["CALL", null, ["callee:00c57a90:8"]]
+ 006f15e8 ["INT_ADD", "register:40f0:8", ["const:6f15e8:8", "const:4:8"]]
+ 006f15e8 ["CALL", null, ["callee:00c57a90:8"]]
- 006c7824 bytes 074e1494
+ 006f15e8 bytes 2a991594
- 006c785c ["INT_ADD", "register:40f0:8", ["const:6c785c:8", "const:4:8"]]
- 006c785c ["CALL", null, ["callee:0043bb64:8"]]
+ 006f1620 ["INT_ADD", "register:40f0:8", ["const:6f1620:8", "const:4:8"]]
+ 006f1620 ["CALL", null, ["callee:0043bb64:8"]]
- 006c785c bytes 0246f597
+ 006f1620 bytes 5129f597
~~~


<a id="compare-20d5b96f348d4d56a4ea2a9001513b12"></a>

### [`006ce860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce860.md) → [`006f8614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f8614.md) FUN_006f8614

採用 · 移動量 `+0x29db4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ce89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce860.md#insn-006ce89c) · [`006ce8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce860.md#insn-006ce8b0)
- 新版 `006f8650`（命令位置の公開資料なし） · `006f8664`（命令位置の公開資料なし）

~~~diff
- 006ce89c ["INT_ADD", "register:40f0:8", ["const:6ce89c:8", "const:4:8"]]
- 006ce89c ["CALL", null, ["callee:00540d3c:8"]]
+ 006f8650 ["INT_ADD", "register:40f0:8", ["const:6f8650:8", "const:4:8"]]
+ 006f8650 ["CALL", null, ["callee:00540d3c:8"]]
- 006ce89c bytes 823df997
+ 006f8650 bytes bb21f997
- 006ce8b0 ["INT_ADD", "register:40f0:8", ["const:6ce8b0:8", "const:4:8"]]
- 006ce8b0 ["CALL", null, ["callee:0043bae0:8"]]
+ 006f8664 ["INT_ADD", "register:40f0:8", ["const:6f8664:8", "const:4:8"]]
+ 006f8664 ["CALL", null, ["callee:0043bae0:8"]]
- 006ce8b0 bytes cc29f597
+ 006f8664 bytes 1f0df597
~~~


<a id="compare-30b69e5c959dab7284d51cfa5ebead83"></a>

### [`006d1280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1280.md) → [`006fb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md) FUN_006fb034

採用 · 移動量 `+0x29db4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`006ba6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba6e4.md) [`006bbf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md) [`006d1280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1280.md) [`006d1b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1b1c.md) [`006d1eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1eb8.md) · 呼出先 4件 [`006d1280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1280.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 10件 [`006e44a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e44a0.md) [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) [`006fb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md) [`006fb8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8d0.md) [`006fbc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md) · 呼出先 4件 [`006fb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d129c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1280.md#insn-006d129c) · [`006d12a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1280.md#insn-006d12a8) · [`006d12bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1280.md#insn-006d12bc)
- 新版 `006fb050`（命令位置の公開資料なし） · `006fb05c`（命令位置の公開資料なし） · `006fb070`（命令位置の公開資料なし）

~~~diff
- 006d129c ["INT_ADD", "register:40f0:8", ["const:6d129c:8", "const:4:8"]]
- 006d129c ["CALL", null, ["local:b0:8"]]
+ 006fb050 ["INT_ADD", "register:40f0:8", ["const:6fb050:8", "const:4:8"]]
+ 006fb050 ["CALL", null, ["local:b0:8"]]
- 006d129c bytes f9ffff97
+ 006fb050 bytes f9ffff97
- 006d12a8 ["INT_ADD", "register:40f0:8", ["const:6d12a8:8", "const:4:8"]]
- 006d12a8 ["CALL", null, ["local:b0:8"]]
+ 006fb05c ["INT_ADD", "register:40f0:8", ["const:6fb05c:8", "const:4:8"]]
+ 006fb05c ["CALL", null, ["local:b0:8"]]
- 006d12a8 bytes f6ffff97
+ 006fb05c bytes f6ffff97
- 006d12bc ["INT_ADD", "register:40f0:8", ["const:6d12bc:8", "const:4:8"]]
- 006d12bc ["CALL", null, ["callee:00c538e0:8"]]
+ 006fb070 ["INT_ADD", "register:40f0:8", ["const:6fb070:8", "const:4:8"]]
+ 006fb070 ["CALL", null, ["callee:00c538e0:8"]]
- 006d12bc bytes f5161494
+ 006fb070 bytes 1c621594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55843ba375aef1a142f69a16cedc09a1"></a>

### [`006d6330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6330.md) → [`007000e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/007000e4.md) FUN_007000e4

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d6350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6330.md#insn-006d6350)
- 新版 `00700104`（命令位置の公開資料なし）

~~~diff
- 006d6350 ["INT_ADD", "register:40f0:8", ["const:6d6350:8", "const:4:8"]]
- 006d6350 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00700104 ["INT_ADD", "register:40f0:8", ["const:700104:8", "const:4:8"]]
+ 00700104 ["CALL", null, ["callee:00c57ab0:8"]]
- 006d6350 bytes 44131494
+ 00700104 bytes 6b5e1594
~~~


<a id="compare-8877c14e129930decbc22545a8af0221"></a>

### [`006d671c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d671c.md) → [`007004d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/007004d0.md) FUN_007004d0

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d673c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d671c.md#insn-006d673c)
- 新版 `007004f0`（命令位置の公開資料なし）

~~~diff
- 006d673c ["INT_ADD", "register:40f0:8", ["const:6d673c:8", "const:4:8"]]
- 006d673c ["CALL", null, ["callee:00c57ab0:8"]]
+ 007004f0 ["INT_ADD", "register:40f0:8", ["const:7004f0:8", "const:4:8"]]
+ 007004f0 ["CALL", null, ["callee:00c57ab0:8"]]
- 006d673c bytes 49121494
+ 007004f0 bytes 705d1594
~~~


<a id="compare-75cbecc97cf51331d475addfb7dd44e6"></a>

### [`006e41d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e41d8.md) → [`0070e108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e108.md) FUN_0070e108

採用 · 移動量 `+0x29f30` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e41fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e41d8.md#insn-006e41fc)
- 新版 `0070e12c`（命令位置の公開資料なし）

~~~diff
- 006e41fc ["INT_ADD", "register:40f0:8", ["const:6e41fc:8", "const:4:8"]]
- 006e41fc ["CALL", null, ["callee:0046ef9c:8"]]
+ 0070e12c ["INT_ADD", "register:40f0:8", ["const:70e12c:8", "const:4:8"]]
+ 0070e12c ["CALL", null, ["callee:0046ef9c:8"]]
- 006e41fc bytes c29ff597
+ 0070e12c bytes 9c83f597
~~~


<a id="compare-fdf62a3606f4c09078114df0a4754a29"></a>

### [`006ea088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea088.md) → [`007140e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007140e4.md) FUN_007140e4

採用 · 移動量 `+0x2a05c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005d955c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d955c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005fe21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe21c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ea108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea088.md#insn-006ea108) · [`006ea144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea088.md#insn-006ea144) · [`006ea158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea088.md#insn-006ea158)
- 新版 `00714164`（命令位置の公開資料なし） · `007141a0`（命令位置の公開資料なし） · `007141b4`（命令位置の公開資料なし）

~~~diff
- 006ea108 ["INT_ADD", "register:40f0:8", ["const:6ea108:8", "const:4:8"]]
- 006ea108 ["CALL", null, ["callee:00c57a90:8"]]
+ 00714164 ["INT_ADD", "register:40f0:8", ["const:714164:8", "const:4:8"]]
+ 00714164 ["CALL", null, ["callee:00c57a90:8"]]
- 006ea108 bytes cec31394
+ 00714164 bytes 4b0e1594
- 006ea144 ["INT_ADD", "register:40f0:8", ["const:6ea144:8", "const:4:8"]]
- 006ea144 ["CALL", null, ["callee:00c57c00:8"]]
+ 007141a0 ["INT_ADD", "register:40f0:8", ["const:7141a0:8", "const:4:8"]]
+ 007141a0 ["CALL", null, ["callee:00c57c00:8"]]
- 006ea144 bytes 1bc41394
+ 007141a0 bytes 980e1594
- 006ea158 ["INT_ADD", "register:40f0:8", ["const:6ea158:8", "const:4:8"]]
- 006ea158 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007141b4 ["INT_ADD", "register:40f0:8", ["const:7141b4:8", "const:4:8"]]
+ 007141b4 ["CALL", null, ["callee:00c57ab0:8"]]
- 006ea158 bytes c2c31394
+ 007141b4 bytes 3f0e1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87fd71778c4c805afeb2652b01a1be46"></a>

### [`006ea180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea180.md) → [`007141dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007141dc.md) FUN_007141dc

採用 · 移動量 `+0x2a05c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005d9598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9598.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ea1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea180.md#insn-006ea1a0)
- 新版 `007141fc`（命令位置の公開資料なし）

~~~diff
- 006ea1a0 ["INT_ADD", "register:40f0:8", ["const:6ea1a0:8", "const:4:8"]]
- 006ea1a0 ["CALL", null, ["callee:005fe258:8"]]
+ 007141fc ["INT_ADD", "register:40f0:8", ["const:7141fc:8", "const:4:8"]]
+ 007141fc ["CALL", null, ["callee:005fe258:8"]]
- 006ea1a0 bytes febcfb97
+ 007141fc bytes 17a8fb97
~~~


<a id="compare-d9a3fbd3176f1381ba8e310ce733a40c"></a>

### [`006fce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fce30.md) → [`00726f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f30.md) FUN_00726f30

採用 · 移動量 `+0x2a100` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`008fbc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbc30.md) · 呼出先 1件 [`0052daf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daf0.md)
- 新版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`009302e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009302e0.md) · 呼出先 1件 [`00550988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550988.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fce30.md#insn-006fce40)
- 新版 `00726f40`（命令位置の公開資料なし）

~~~diff
- 006fce40 ["INT_ADD", "register:40f0:8", ["const:6fce40:8", "const:4:8"]]
- 006fce40 ["CALL", null, ["callee:00550988:8"]]
+ 00726f40 ["INT_ADD", "register:40f0:8", ["const:726f40:8", "const:4:8"]]
+ 00726f40 ["CALL", null, ["callee:00550988:8"]]
- 006fce40 bytes 2cc3f897
+ 00726f40 bytes 92a6f897
~~~


<a id="compare-eb8ddcefac02e9730e6f8acde2e7cbd9"></a>

### [`006fd46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd46c.md) → [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) FUN_0072756c

採用 · 移動量 `+0x2a100` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006fc680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc680.md) [`006fd46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd46c.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 3件 [`006fd46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd46c.md) [`006fd4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd4bc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00726780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726780.md) [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fd48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd46c.md#insn-006fd48c) · [`006fd498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd46c.md#insn-006fd498) · [`006fd4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd46c.md#insn-006fd4a4)
- 新版 `0072758c`（命令位置の公開資料なし） · `00727598`（命令位置の公開資料なし） · `007275a4`（命令位置の公開資料なし）

~~~diff
- 006fd48c ["INT_ADD", "register:40f0:8", ["const:6fd48c:8", "const:4:8"]]
- 006fd48c ["CALL", null, ["local:b0:8"]]
+ 0072758c ["INT_ADD", "register:40f0:8", ["const:72758c:8", "const:4:8"]]
+ 0072758c ["CALL", null, ["local:b0:8"]]
- 006fd48c bytes f8ffff97
+ 0072758c bytes f8ffff97
- 006fd498 ["INT_ADD", "register:40f0:8", ["const:6fd498:8", "const:4:8"]]
- 006fd498 ["CALL", null, ["local:b0:8"]]
+ 00727598 ["INT_ADD", "register:40f0:8", ["const:727598:8", "const:4:8"]]
+ 00727598 ["CALL", null, ["local:b0:8"]]
- 006fd498 bytes f5ffff97
+ 00727598 bytes f5ffff97
- 006fd4a4 ["INT_ADD", "register:40f0:8", ["const:6fd4a4:8", "const:4:8"]]
- 006fd4a4 ["CALL", null, ["callee:007275bc:8"]]
+ 007275a4 ["INT_ADD", "register:40f0:8", ["const:7275a4:8", "const:4:8"]]
+ 007275a4 ["CALL", null, ["callee:007275bc:8"]]
- 006fd4a4 bytes 06000094
+ 007275a4 bytes 06000094
~~~


<a id="compare-ecb44e65fd00646b54a89b0be8bde3ef"></a>

### [`006fd4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd4bc.md) → [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) FUN_007275bc

採用 · 移動量 `+0x2a100` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006fd46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd46c.md) [`006fd4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd4bc.md) · 呼出先 2件 [`006fd4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd4bc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) · 呼出先 2件 [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fd4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd4bc.md#insn-006fd4dc) · [`006fd4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd4bc.md#insn-006fd4e8)
- 新版 `007275dc`（命令位置の公開資料なし） · `007275e8`（命令位置の公開資料なし）

~~~diff
- 006fd4dc ["INT_ADD", "register:40f0:8", ["const:6fd4dc:8", "const:4:8"]]
- 006fd4dc ["CALL", null, ["local:b0:8"]]
+ 007275dc ["INT_ADD", "register:40f0:8", ["const:7275dc:8", "const:4:8"]]
+ 007275dc ["CALL", null, ["local:b0:8"]]
- 006fd4dc bytes f8ffff97
+ 007275dc bytes f8ffff97
- 006fd4e8 ["INT_ADD", "register:40f0:8", ["const:6fd4e8:8", "const:4:8"]]
- 006fd4e8 ["CALL", null, ["local:b0:8"]]
+ 007275e8 ["INT_ADD", "register:40f0:8", ["const:7275e8:8", "const:4:8"]]
+ 007275e8 ["CALL", null, ["local:b0:8"]]
- 006fd4e8 bytes f5ffff97
+ 007275e8 bytes f5ffff97
~~~


<a id="compare-cd87011a7903a971fe08379c19ba5a28"></a>

### [`0070219c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070219c.md) → [`0072c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md) FUN_0072c29c

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`007259f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00725/007259f0.md) [`00726b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00726/00726b58.md) [`00750e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750e68.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`0096b980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096b/0096b980.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00447434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447434.md)
- 新版 呼出元 5件 [`0074fba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074f/0074fba0.md) [`00750d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00750/00750d08.md) [`0077b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`009a1464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a1464.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a2cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007021b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070219c.md#insn-007021b0) · [`007021d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070219c.md#insn-007021d4) · [`00702218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070219c.md#insn-00702218)
- 新版 `0072c2b0`（命令位置の公開資料なし） · `0072c2d4`（命令位置の公開資料なし） · `0072c318`（命令位置の公開資料なし）

~~~diff
- 007021b0 ["INT_ADD", "register:40f0:8", ["const:7021b0:8", "const:4:8"]]
- 007021b0 ["CALL", null, ["callee:00467820:8"]]
+ 0072c2b0 ["INT_ADD", "register:40f0:8", ["const:72c2b0:8", "const:4:8"]]
+ 0072c2b0 ["CALL", null, ["callee:00467820:8"]]
- 007021b0 bytes f609f597
+ 0072c2b0 bytes 5cedf497
- 007021d4 ["INT_ADD", "register:40f0:8", ["const:7021d4:8", "const:4:8"]]
- 007021d4 ["CALL", null, ["callee:0046a2cc:8"]]
+ 0072c2d4 ["INT_ADD", "register:40f0:8", ["const:72c2d4:8", "const:4:8"]]
+ 0072c2d4 ["CALL", null, ["callee:0046a2cc:8"]]
- 007021d4 bytes 9814f597
+ 0072c2d4 bytes fef7f497
- 00702218 ["INT_ADD", "register:40f0:8", ["const:702218:8", "const:4:8"]]
- 00702218 ["CALL", null, ["callee:00469bc4:8"]]
+ 0072c318 ["INT_ADD", "register:40f0:8", ["const:72c318:8", "const:4:8"]]
+ 0072c318 ["CALL", null, ["callee:00469bc4:8"]]
- 00702218 bytes c512f597
+ 0072c318 bytes 2bf6f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f2e3029a8d790c7c191752358e702de"></a>

### [`00702240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702240.md) → [`0072c340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c340.md) FUN_0072c340

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006ff834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ff834.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005f5668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00729934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729934.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0061aeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070229c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702240.md#insn-0070229c) · [`007022ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702240.md#insn-007022ac) · [`007022e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702240.md#insn-007022e0)
- 新版 `0072c39c`（命令位置の公開資料なし） · `0072c3ac`（命令位置の公開資料なし） · `0072c3e0`（命令位置の公開資料なし）

~~~diff
- 0070229c ["INT_ADD", "register:40f0:8", ["const:70229c:8", "const:4:8"]]
- 0070229c ["CALL", null, ["callee:0043bae0:8"]]
+ 0072c39c ["INT_ADD", "register:40f0:8", ["const:72c39c:8", "const:4:8"]]
+ 0072c39c ["CALL", null, ["callee:0043bae0:8"]]
- 0070229c bytes 515bf497
+ 0072c39c bytes d13df497
- 007022ac ["INT_ADD", "register:40f0:8", ["const:7022ac:8", "const:4:8"]]
- 007022ac ["CALL", null, ["callee:0043bae0:8"]]
+ 0072c3ac ["INT_ADD", "register:40f0:8", ["const:72c3ac:8", "const:4:8"]]
+ 0072c3ac ["CALL", null, ["callee:0043bae0:8"]]
- 007022ac bytes 4d5bf497
+ 0072c3ac bytes cd3df497
- 007022e0 ["INT_ADD", "register:40f0:8", ["const:7022e0:8", "const:4:8"]]
- 007022e0 ["CALL", null, ["callee:0061aeb8:8"]]
+ 0072c3e0 ["INT_ADD", "register:40f0:8", ["const:72c3e0:8", "const:4:8"]]
+ 0072c3e0 ["CALL", null, ["callee:0061aeb8:8"]]
- 007022e0 bytes e2ccfb97
+ 0072c3e0 bytes b6bafb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292da6a342d8d1fae309de9985bf0c43"></a>

### [`007027d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007027d4.md) → [`0072c8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8d4.md) FUN_0072c8d4

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · 呼出先 1件 [`007079b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007079b8.md)
- 新版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 1件 [`00731ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ab8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007027f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007027d4.md#insn-007027f8)
- 新版 `0072c8f8`（命令位置の公開資料なし）

~~~diff
- 007027f8 ["INT_ADD", "register:40f0:8", ["const:7027f8:8", "const:4:8"]]
- 007027f8 ["CALL", null, ["callee:00731ab8:8"]]
+ 0072c8f8 ["INT_ADD", "register:40f0:8", ["const:72c8f8:8", "const:4:8"]]
+ 0072c8f8 ["CALL", null, ["callee:00731ab8:8"]]
- 007027f8 bytes 70140094
+ 0072c8f8 bytes 70140094
~~~


<a id="compare-31abb5e222ae896aee660de6af9fc919"></a>

### [`00704a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704a98.md) → [`0072eb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072eb98.md) FUN_0072eb98

採用 · 移動量 `+0x2a100` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00704abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704a98.md#insn-00704abc) · [`00704acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704a98.md#insn-00704acc)
- 新版 `0072ebbc`（命令位置の公開資料なし） · `0072ebcc`（命令位置の公開資料なし）

~~~diff
- 00704abc ["INT_ADD", "register:40f0:8", ["const:704abc:8", "const:4:8"]]
- 00704abc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0072ebbc ["INT_ADD", "register:40f0:8", ["const:72ebbc:8", "const:4:8"]]
+ 0072ebbc ["CALL", null, ["callee:00c57ab0:8"]]
- 00704abc bytes 69591394
+ 0072ebbc bytes bda31494
- 00704acc ["INT_ADD", "register:40f0:8", ["const:704acc:8", "const:4:8"]]
- 00704acc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0072ebcc ["INT_ADD", "register:40f0:8", ["const:72ebcc:8", "const:4:8"]]
+ 0072ebcc ["CALL", null, ["callee:00c57ab0:8"]]
- 00704acc bytes 65591394
+ 0072ebcc bytes b9a31494
~~~


<a id="compare-42491d0b3247b7c13a03f9dc16283bcc"></a>

### [`00704b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704b94.md) → [`0072ec94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ec94.md) FUN_0072ec94

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00704bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704b94.md#insn-00704bb8) · [`00704bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704b94.md#insn-00704bc8)
- 新版 `0072ecb8`（命令位置の公開資料なし） · `0072ecc8`（命令位置の公開資料なし）

~~~diff
- 00704bb8 ["INT_ADD", "register:40f0:8", ["const:704bb8:8", "const:4:8"]]
- 00704bb8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0072ecb8 ["INT_ADD", "register:40f0:8", ["const:72ecb8:8", "const:4:8"]]
+ 0072ecb8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00704bb8 bytes 2a591394
+ 0072ecb8 bytes 7ea31494
- 00704bc8 ["INT_ADD", "register:40f0:8", ["const:704bc8:8", "const:4:8"]]
- 00704bc8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0072ecc8 ["INT_ADD", "register:40f0:8", ["const:72ecc8:8", "const:4:8"]]
+ 0072ecc8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00704bc8 bytes 26591394
+ 0072ecc8 bytes 7aa31494
~~~


<a id="compare-d5dab33c39e22a6b53f8255789fe7028"></a>

### [`00706bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706bbc.md) → [`00730cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730cbc.md) FUN_00730cbc

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) · 呼出先 1件 [`007079a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007079a4.md)
- 新版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 1件 [`00731aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00706be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706bbc.md#insn-00706be0)
- 新版 `00730ce0`（命令位置の公開資料なし）

~~~diff
- 00706be0 ["INT_ADD", "register:40f0:8", ["const:706be0:8", "const:4:8"]]
- 00706be0 ["CALL", null, ["callee:00731aa4:8"]]
+ 00730ce0 ["INT_ADD", "register:40f0:8", ["const:730ce0:8", "const:4:8"]]
+ 00730ce0 ["CALL", null, ["callee:00731aa4:8"]]
- 00706be0 bytes 71030094
+ 00730ce0 bytes 71030094
~~~


<a id="compare-8ea56d1ac38cc4eff08d146869376d70"></a>

### [`00707530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707530.md) → [`00731630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731630.md) FUN_00731630

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · 呼出先 3件 [`007cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd120.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd560.md)
- 新版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 3件 [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070754c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707530.md#insn-0070754c) · [`00707558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707530.md#insn-00707558) · [`0070756c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707530.md#insn-0070756c)
- 新版 `0073164c`（命令位置の公開資料なし） · `00731658`（命令位置の公開資料なし） · `0073166c`（命令位置の公開資料なし）

~~~diff
- 0070754c ["INT_ADD", "register:40f0:8", ["const:70754c:8", "const:4:8"]]
- 0070754c ["CALL", null, ["callee:00800338:8"]]
+ 0073164c ["INT_ADD", "register:40f0:8", ["const:73164c:8", "const:4:8"]]
+ 0073164c ["CALL", null, ["callee:00800338:8"]]
- 0070754c bytes 58170394
+ 0073164c bytes 3b3b0394
- 00707558 ["INT_ADD", "register:40f0:8", ["const:707558:8", "const:4:8"]]
- 00707558 ["CALL", null, ["callee:008005ec:8"]]
+ 00731658 ["INT_ADD", "register:40f0:8", ["const:731658:8", "const:4:8"]]
+ 00731658 ["CALL", null, ["callee:008005ec:8"]]
- 00707558 bytes 02180394
+ 00731658 bytes e53b0394
- 0070756c ["INT_ADD", "register:40f0:8", ["const:70756c:8", "const:4:8"]]
- 0070756c ["CALL", null, ["callee:008001ac:8"]]
+ 0073166c ["INT_ADD", "register:40f0:8", ["const:73166c:8", "const:4:8"]]
+ 0073166c ["CALL", null, ["callee:008001ac:8"]]
- 0070756c bytes ed160394
+ 0073166c bytes d03a0394
~~~


<a id="compare-9aad2ab9da3b7236b5613770b75b3893"></a>

### [`007078b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007078b8.md) → [`007319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md) FUN_007319b8

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00707868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707868.md) [`007078b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007078b8.md) · 呼出先 2件 [`007078b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007078b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00731968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md) [`007319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md) · 呼出先 2件 [`007319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007078d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007078b8.md#insn-007078d4) · [`007078e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007078b8.md#insn-007078e0) · [`007078fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007078b8.md#insn-007078fc)
- 新版 `007319d4`（命令位置の公開資料なし） · `007319e0`（命令位置の公開資料なし） · `007319fc`（命令位置の公開資料なし）

~~~diff
- 007078d4 ["INT_ADD", "register:40f0:8", ["const:7078d4:8", "const:4:8"]]
- 007078d4 ["CALL", null, ["local:b0:8"]]
+ 007319d4 ["INT_ADD", "register:40f0:8", ["const:7319d4:8", "const:4:8"]]
+ 007319d4 ["CALL", null, ["local:b0:8"]]
- 007078d4 bytes f9ffff97
+ 007319d4 bytes f9ffff97
- 007078e0 ["INT_ADD", "register:40f0:8", ["const:7078e0:8", "const:4:8"]]
- 007078e0 ["CALL", null, ["local:b0:8"]]
+ 007319e0 ["INT_ADD", "register:40f0:8", ["const:7319e0:8", "const:4:8"]]
+ 007319e0 ["CALL", null, ["local:b0:8"]]
- 007078e0 bytes f6ffff97
+ 007319e0 bytes f6ffff97
- 007078fc ["INT_ADD", "register:40f0:8", ["const:7078fc:8", "const:4:8"]]
- 007078fc ["CALL", null, ["callee:00c57ab0:8"]]
+ 007319fc ["INT_ADD", "register:40f0:8", ["const:7319fc:8", "const:4:8"]]
+ 007319fc ["CALL", null, ["callee:00c57ab0:8"]]
- 007078fc bytes d94d1394
+ 007319fc bytes 2d981494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89e3b0917db2ab4996aa843ba0e7eadf"></a>

### [`0070b570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b570.md) → [`00735670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735670.md) FUN_00735670

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0070a288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a288.md) [`0070c5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070c5c4.md) [`0070cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070cadc.md) · 呼出先 5件 [`009d8aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d8/009d8aa4.md) [`009d9f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d9/009d9f70.md) [`009da788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009da788.md) [`009dbac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbac8.md) [`009dbae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbae4.md)
- 新版 呼出元 3件 [`00734388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) [`007366c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007366c4.md) [`00736bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/00736bdc.md) · 呼出先 5件 [`00a359a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a359a0.md) [`00a36e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md) [`00a37684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37684.md) [`00a389c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389c4.md) [`00a389e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070b58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b570.md#insn-0070b58c) · [`0070b590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b570.md#insn-0070b590) · [`0070b5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b570.md#insn-0070b5a8)
- 新版 `0073568c`（命令位置の公開資料なし） · `00735690`（命令位置の公開資料なし） · `007356a8`（命令位置の公開資料なし）

~~~diff
- 0070b58c ["INT_ADD", "register:40f0:8", ["const:70b58c:8", "const:4:8"]]
- 0070b58c ["CALL", null, ["callee:00a359a0:8"]]
+ 0073568c ["INT_ADD", "register:40f0:8", ["const:73568c:8", "const:4:8"]]
+ 0073568c ["CALL", null, ["callee:00a359a0:8"]]
- 0070b58c bytes 46350b94
+ 0073568c bytes c5000c94
- 0070b590 ["INT_ADD", "register:40f0:8", ["const:70b590:8", "const:4:8"]]
- 0070b590 ["CALL", null, ["callee:00a389c4:8"]]
+ 00735690 ["INT_ADD", "register:40f0:8", ["const:735690:8", "const:4:8"]]
+ 00735690 ["CALL", null, ["callee:00a389c4:8"]]
- 0070b590 bytes 4e410b94
+ 00735690 bytes cd0c0c94
- 0070b5a8 ["INT_ADD", "register:40f0:8", ["const:70b5a8:8", "const:4:8"]]
- 0070b5a8 ["CALL", null, ["callee:00a359a0:8"]]
+ 007356a8 ["INT_ADD", "register:40f0:8", ["const:7356a8:8", "const:4:8"]]
+ 007356a8 ["CALL", null, ["callee:00a359a0:8"]]
- 0070b5a8 bytes 3f350b94
+ 007356a8 bytes be000c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e99c773471877dc7eb4507f88c5e2c"></a>

### [`0070e1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e1c8.md) → [`007382c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007382c8.md) FUN_007382c8

採用 · 移動量 `+0x2a100` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009b7d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009b7/009b7d00.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070e1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e1c8.md#insn-0070e1e0) · [`0070e1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e1c8.md#insn-0070e1ec)
- 新版 `007382e0`（命令位置の公開資料なし） · `007382ec`（命令位置の公開資料なし）

~~~diff
- 0070e1e0 ["INT_ADD", "register:40f0:8", ["const:70e1e0:8", "const:4:8"]]
- 0070e1e0 ["CALL", null, ["callee:00480de8:8"]]
+ 007382e0 ["INT_ADD", "register:40f0:8", ["const:7382e0:8", "const:4:8"]]
+ 007382e0 ["CALL", null, ["callee:00480de8:8"]]
- 0070e1e0 bytes 5c3ff597
+ 007382e0 bytes c222f597
- 0070e1ec ["INT_ADD", "register:40f0:8", ["const:70e1ec:8", "const:4:8"]]
- 0070e1ec ["CALL", null, ["callee:00480de8:8"]]
+ 007382ec ["INT_ADD", "register:40f0:8", ["const:7382ec:8", "const:4:8"]]
+ 007382ec ["CALL", null, ["callee:00480de8:8"]]
- 0070e1ec bytes 593ff597
+ 007382ec bytes bf22f597
~~~


<a id="compare-283a2cb95e3b67b03b8ac300f8813c29"></a>

### [`0070e204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e204.md) → [`00738304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738304.md) FUN_00738304

採用 · 移動量 `+0x2a100` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070e218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e204.md#insn-0070e218) · [`0070e220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e204.md#insn-0070e220)
- 新版 `00738318`（命令位置の公開資料なし） · `00738320`（命令位置の公開資料なし）

~~~diff
- 0070e218 ["INT_ADD", "register:40f0:8", ["const:70e218:8", "const:4:8"]]
- 0070e218 ["CALL", null, ["callee:004803b0:8"]]
+ 00738318 ["INT_ADD", "register:40f0:8", ["const:738318:8", "const:4:8"]]
+ 00738318 ["CALL", null, ["callee:004803b0:8"]]
- 0070e218 bytes c03cf597
+ 00738318 bytes 2620f597
- 0070e220 ["INT_ADD", "register:40f0:8", ["const:70e220:8", "const:4:8"]]
- 0070e220 ["CALL", null, ["callee:004803b0:8"]]
+ 00738320 ["INT_ADD", "register:40f0:8", ["const:738320:8", "const:4:8"]]
+ 00738320 ["CALL", null, ["callee:004803b0:8"]]
- 0070e220 bytes be3cf597
+ 00738320 bytes 2420f597
~~~


<a id="compare-349560b482fc163c578f770de63a311b"></a>

### [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) → [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) FUN_0073a2c4

採用 · 移動量 `+0x2a100` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`0070dd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070dd4c.md) [`0070ea48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070ea48.md) [`0070f364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f364.md) [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) [`00710d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d08.md) · 呼出先 2件 [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 10件 [`00737e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md) [`00738b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738b48.md) [`00739464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739464.md) [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) · 呼出先 2件 [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007101e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md#insn-007101e0) · [`007101ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md#insn-007101ec) · [`007101fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md#insn-007101fc)
- 新版 `0073a2e0`（命令位置の公開資料なし） · `0073a2ec`（命令位置の公開資料なし） · `0073a2fc`（命令位置の公開資料なし）

~~~diff
- 007101e0 ["INT_ADD", "register:40f0:8", ["const:7101e0:8", "const:4:8"]]
- 007101e0 ["CALL", null, ["local:b0:8"]]
+ 0073a2e0 ["INT_ADD", "register:40f0:8", ["const:73a2e0:8", "const:4:8"]]
+ 0073a2e0 ["CALL", null, ["local:b0:8"]]
- 007101e0 bytes f9ffff97
+ 0073a2e0 bytes f9ffff97
- 007101ec ["INT_ADD", "register:40f0:8", ["const:7101ec:8", "const:4:8"]]
- 007101ec ["CALL", null, ["local:b0:8"]]
+ 0073a2ec ["INT_ADD", "register:40f0:8", ["const:73a2ec:8", "const:4:8"]]
+ 0073a2ec ["CALL", null, ["local:b0:8"]]
- 007101ec bytes f6ffff97
+ 0073a2ec bytes f6ffff97
- 007101fc ["INT_ADD", "register:40f0:8", ["const:7101fc:8", "const:4:8"]]
- 007101fc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0073a2fc ["INT_ADD", "register:40f0:8", ["const:73a2fc:8", "const:4:8"]]
+ 0073a2fc ["CALL", null, ["callee:00c57ab0:8"]]
- 007101fc bytes 992b1394
+ 0073a2fc bytes ed751494
~~~


<a id="compare-250c9cc0bc7702b3a8c1b2296bb0a667"></a>

### [`00710d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d08.md) → [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) FUN_0073ae08

採用 · 移動量 `+0x2a100` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0070a160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a160.md) [`0070dfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070dfa4.md) [`00710d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d08.md) [`0081632c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081632c.md) · 呼出先 3件 [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) [`00710d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00734260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) [`007380a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007380a4.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) [`008480e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md) · 呼出先 3件 [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00710d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d08.md#insn-00710d28) · [`00710d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d08.md#insn-00710d34) · [`00710d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d08.md#insn-00710d40)
- 新版 `0073ae28`（命令位置の公開資料なし） · `0073ae34`（命令位置の公開資料なし） · `0073ae40`（命令位置の公開資料なし）

~~~diff
- 00710d28 ["INT_ADD", "register:40f0:8", ["const:710d28:8", "const:4:8"]]
- 00710d28 ["CALL", null, ["local:b0:8"]]
+ 0073ae28 ["INT_ADD", "register:40f0:8", ["const:73ae28:8", "const:4:8"]]
+ 0073ae28 ["CALL", null, ["local:b0:8"]]
- 00710d28 bytes f8ffff97
+ 0073ae28 bytes f8ffff97
- 00710d34 ["INT_ADD", "register:40f0:8", ["const:710d34:8", "const:4:8"]]
- 00710d34 ["CALL", null, ["local:b0:8"]]
+ 0073ae34 ["INT_ADD", "register:40f0:8", ["const:73ae34:8", "const:4:8"]]
+ 0073ae34 ["CALL", null, ["local:b0:8"]]
- 00710d34 bytes f5ffff97
+ 0073ae34 bytes f5ffff97
- 00710d40 ["INT_ADD", "register:40f0:8", ["const:710d40:8", "const:4:8"]]
- 00710d40 ["CALL", null, ["callee:0073a2c4:8"]]
+ 0073ae40 ["INT_ADD", "register:40f0:8", ["const:73ae40:8", "const:4:8"]]
+ 0073ae40 ["CALL", null, ["callee:0073a2c4:8"]]
- 00710d40 bytes 21fdff97
+ 0073ae40 bytes 21fdff97
~~~


<a id="compare-e2dbe237440739516823df0b0243a50b"></a>

### [`00710d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d58.md) → [`0073ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md) FUN_0073ae58

採用 · 移動量 `+0x2a100` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0070a160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a160.md) [`0070e66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e66c.md) [`00710d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d58.md) [`0081632c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081632c.md) · 呼出先 2件 [`00710d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d58.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00734260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) [`0073876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md) [`0073ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md) [`008480e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md) · 呼出先 2件 [`0073ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00710d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d58.md#insn-00710d78) · [`00710d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d58.md#insn-00710d84)
- 新版 `0073ae78`（命令位置の公開資料なし） · `0073ae84`（命令位置の公開資料なし）

~~~diff
- 00710d78 ["INT_ADD", "register:40f0:8", ["const:710d78:8", "const:4:8"]]
- 00710d78 ["CALL", null, ["local:b0:8"]]
+ 0073ae78 ["INT_ADD", "register:40f0:8", ["const:73ae78:8", "const:4:8"]]
+ 0073ae78 ["CALL", null, ["local:b0:8"]]
- 00710d78 bytes f8ffff97
+ 0073ae78 bytes f8ffff97
- 00710d84 ["INT_ADD", "register:40f0:8", ["const:710d84:8", "const:4:8"]]
- 00710d84 ["CALL", null, ["local:b0:8"]]
+ 0073ae84 ["INT_ADD", "register:40f0:8", ["const:73ae84:8", "const:4:8"]]
+ 0073ae84 ["CALL", null, ["local:b0:8"]]
- 00710d84 bytes f5ffff97
+ 0073ae84 bytes f5ffff97
~~~


<a id="compare-29dc86434fbbfdcb92c9927d498e3282"></a>

### [`00710d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d9c.md) → [`0073ae9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md) FUN_0073ae9c

採用 · 移動量 `+0x2a100` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0070afb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070afb4.md) [`00710d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d9c.md) [`0081632c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081632c.md) · 呼出先 2件 [`00710d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`007350b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/007350b4.md) [`0073ae9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md) [`008480e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md) · 呼出先 2件 [`0073ae9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00710dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d9c.md#insn-00710dbc) · [`00710dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710d9c.md#insn-00710dc8)
- 新版 `0073aebc`（命令位置の公開資料なし） · `0073aec8`（命令位置の公開資料なし）

~~~diff
- 00710dbc ["INT_ADD", "register:40f0:8", ["const:710dbc:8", "const:4:8"]]
- 00710dbc ["CALL", null, ["local:b0:8"]]
+ 0073aebc ["INT_ADD", "register:40f0:8", ["const:73aebc:8", "const:4:8"]]
+ 0073aebc ["CALL", null, ["local:b0:8"]]
- 00710dbc bytes f8ffff97
+ 0073aebc bytes f8ffff97
- 00710dc8 ["INT_ADD", "register:40f0:8", ["const:710dc8:8", "const:4:8"]]
- 00710dc8 ["CALL", null, ["local:b0:8"]]
+ 0073aec8 ["INT_ADD", "register:40f0:8", ["const:73aec8:8", "const:4:8"]]
+ 0073aec8 ["CALL", null, ["local:b0:8"]]
- 00710dc8 bytes f5ffff97
+ 0073aec8 bytes f5ffff97
~~~


<a id="compare-3ddec59a8de93ac26f23eaedcb754f33"></a>

### [`00710e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710e1c.md) → [`0073af1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073af1c.md) FUN_0073af1c

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0070c5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070c5c4.md) [`0070cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070cadc.md) · 呼出先 3件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`007366c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007366c4.md) [`00736bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/00736bdc.md) · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00710ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710e1c.md#insn-00710ecc) · [`00710ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710e1c.md#insn-00710ed8) · [`00710ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710e1c.md#insn-00710ee0)
- 新版 `0073afcc`（命令位置の公開資料なし） · `0073afd8`（命令位置の公開資料なし） · `0073afe0`（命令位置の公開資料なし）

~~~diff
- 00710ecc ["INT_ADD", "register:40f0:8", ["const:710ecc:8", "const:4:8"]]
- 00710ecc ["CALL", null, ["callee:004945d0:8"]]
+ 0073afcc ["INT_ADD", "register:40f0:8", ["const:73afcc:8", "const:4:8"]]
+ 0073afcc ["CALL", null, ["callee:004945d0:8"]]
- 00710ecc bytes 1b82f597
+ 0073afcc bytes 8165f597
- 00710ed8 ["INT_ADD", "register:40f0:8", ["const:710ed8:8", "const:4:8"]]
- 00710ed8 ["CALL", null, ["callee:0073a2c4:8"]]
+ 0073afd8 ["INT_ADD", "register:40f0:8", ["const:73afd8:8", "const:4:8"]]
+ 0073afd8 ["CALL", null, ["callee:0073a2c4:8"]]
- 00710ed8 bytes bbfcff97
+ 0073afd8 bytes bbfcff97
- 00710ee0 ["INT_ADD", "register:40f0:8", ["const:710ee0:8", "const:4:8"]]
- 00710ee0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0073afe0 ["INT_ADD", "register:40f0:8", ["const:73afe0:8", "const:4:8"]]
+ 0073afe0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00710ee0 bytes 60281394
+ 0073afe0 bytes b4721494
~~~


<a id="compare-c1ef5b5f5700a0612e95fbdb45a5f15f"></a>

### [`00710ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710ef4.md) → [`0073aff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aff4.md) FUN_0073aff4

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0070ec20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070ec20.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00711128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711128.md) [`007112e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007112e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00738d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738d20.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0073b228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b228.md) [`0073b3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b3e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00710fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710ef4.md#insn-00710fac) · [`0071105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710ef4.md#insn-0071105c) · [`00711080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710ef4.md#insn-00711080)
- 新版 `0073b0ac`（命令位置の公開資料なし） · `0073b15c`（命令位置の公開資料なし） · `0073b180`（命令位置の公開資料なし）

~~~diff
- 00710fac ["INT_ADD", "register:40f0:8", ["const:710fac:8", "const:4:8"]]
- 00710fac ["CALL", null, ["callee:00c57a90:8"]]
+ 0073b0ac ["INT_ADD", "register:40f0:8", ["const:73b0ac:8", "const:4:8"]]
+ 0073b0ac ["CALL", null, ["callee:00c57a90:8"]]
- 00710fac bytes 25281394
+ 0073b0ac bytes 79721494
- 0071105c ["INT_ADD", "register:40f0:8", ["const:71105c:8", "const:4:8"]]
- 0071105c ["CALL", null, ["callee:0073b228:8"]]
+ 0073b15c ["INT_ADD", "register:40f0:8", ["const:73b15c:8", "const:4:8"]]
+ 0073b15c ["CALL", null, ["callee:0073b228:8"]]
- 0071105c bytes 33000094
+ 0073b15c bytes 33000094
- 00711080 ["INT_ADD", "register:40f0:8", ["const:711080:8", "const:4:8"]]
- 00711080 ["CALL", null, ["callee:005c175c:8"]]
+ 0073b180 ["INT_ADD", "register:40f0:8", ["const:73b180:8", "const:4:8"]]
+ 0073b180 ["CALL", null, ["callee:005c175c:8"]]
- 00711080 bytes 2b30fa97
+ 0073b180 bytes 7719fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dc2be51966d25e6da8acbe616135af9"></a>

### [`00711274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711274.md) → [`0073b374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b374.md) FUN_0073b374

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007112a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711274.md#insn-007112a4) · [`007112b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711274.md#insn-007112b0)
- 新版 `0073b3a4`（命令位置の公開資料なし） · `0073b3b0`（命令位置の公開資料なし）

~~~diff
- 007112a4 ["INT_ADD", "register:40f0:8", ["const:7112a4:8", "const:4:8"]]
- 007112a4 ["CALL", null, ["callee:005c175c:8"]]
+ 0073b3a4 ["INT_ADD", "register:40f0:8", ["const:73b3a4:8", "const:4:8"]]
+ 0073b3a4 ["CALL", null, ["callee:005c175c:8"]]
- 007112a4 bytes a22ffa97
+ 0073b3a4 bytes ee18fa97
- 007112b0 ["INT_ADD", "register:40f0:8", ["const:7112b0:8", "const:4:8"]]
- 007112b0 ["CALL", null, ["callee:005c175c:8"]]
+ 0073b3b0 ["INT_ADD", "register:40f0:8", ["const:73b3b0:8", "const:4:8"]]
+ 0073b3b0 ["CALL", null, ["callee:005c175c:8"]]
- 007112b0 bytes 9f2ffa97
+ 0073b3b0 bytes eb18fa97
~~~


<a id="compare-107dc0d6252e4fd420b0cd59ead2fba0"></a>

### [`00711360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711360.md) → [`0073b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b460.md) FUN_0073b460

採用 · 移動量 `+0x2a100` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0070f0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f0b0.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`007391b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/007391b0.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007113b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711360.md#insn-007113b4) · [`007113c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711360.md#insn-007113c0)
- 新版 `0073b4b4`（命令位置の公開資料なし） · `0073b4c0`（命令位置の公開資料なし）

~~~diff
- 007113b4 ["INT_ADD", "register:40f0:8", ["const:7113b4:8", "const:4:8"]]
- 007113b4 ["CALL", null, ["callee:005c175c:8"]]
+ 0073b4b4 ["INT_ADD", "register:40f0:8", ["const:73b4b4:8", "const:4:8"]]
+ 0073b4b4 ["CALL", null, ["callee:005c175c:8"]]
- 007113b4 bytes 5e2ffa97
+ 0073b4b4 bytes aa18fa97
- 007113c0 ["INT_ADD", "register:40f0:8", ["const:7113c0:8", "const:4:8"]]
- 007113c0 ["CALL", null, ["callee:005c175c:8"]]
+ 0073b4c0 ["INT_ADD", "register:40f0:8", ["const:73b4c0:8", "const:4:8"]]
+ 0073b4c0 ["CALL", null, ["callee:005c175c:8"]]
- 007113c0 bytes 5b2ffa97
+ 0073b4c0 bytes a718fa97
~~~


<a id="compare-0e3eee6a6546144c7fe9fdc26bd562f0"></a>

### [`00716ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00716/00716ebc.md) → [`00740fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740fc0.md) FUN_00740fc0

採用 · 移動量 `+0x2a104` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00716d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00716/00716d24.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00740e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740e28.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00716ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00716/00716ebc.md#insn-00716ecc)
- 新版 `00740fd0`（命令位置の公開資料なし）

~~~diff
- 00716ecc ["INT_ADD", "register:40f0:8", ["const:716ecc:8", "const:4:8"]]
- 00716ecc ["CALL", null, ["callee:00740e28:8"]]
+ 00740fd0 ["INT_ADD", "register:40f0:8", ["const:740fd0:8", "const:4:8"]]
+ 00740fd0 ["CALL", null, ["callee:00740e28:8"]]
- 00716ecc bytes 96ffff97
+ 00740fd0 bytes 96ffff97
~~~


<a id="compare-e6e3fcd293c51f6db8928e427fb6700c"></a>

### [`0071704c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/0071704c.md) → [`00741150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741150.md) FUN_00741150

採用 · 移動量 `+0x2a104` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00717084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/0071704c.md#insn-00717084)
- 新版 `00741188`（命令位置の公開資料なし）

~~~diff
- 00717084 ["INT_ADD", "register:40f0:8", ["const:717084:8", "const:4:8"]]
- 00717084 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00741188 ["INT_ADD", "register:40f0:8", ["const:741188:8", "const:4:8"]]
+ 00741188 ["CALL", null, ["callee:00c57ab0:8"]]
- 00717084 bytes f70f1394
+ 00741188 bytes 4a5a1494
~~~


<a id="compare-1a6bbf8faf5f3491f3fb2edc8188754a"></a>

### [`0071d618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d618.md) → [`007477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md) FUN_007477c4

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00718a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00718/00718a74.md) [`0071d618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d618.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00817538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817538.md) · 呼出先 2件 [`0071d618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d618.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00742b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00742/00742b78.md) [`007477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849330.md) · 呼出先 2件 [`007477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071d634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d618.md#insn-0071d634) · [`0071d640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d618.md#insn-0071d640) · [`0071d650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d618.md#insn-0071d650)
- 新版 `007477e0`（命令位置の公開資料なし） · `007477ec`（命令位置の公開資料なし） · `007477fc`（命令位置の公開資料なし）

~~~diff
- 0071d634 ["INT_ADD", "register:40f0:8", ["const:71d634:8", "const:4:8"]]
- 0071d634 ["CALL", null, ["local:b0:8"]]
+ 007477e0 ["INT_ADD", "register:40f0:8", ["const:7477e0:8", "const:4:8"]]
+ 007477e0 ["CALL", null, ["local:b0:8"]]
- 0071d634 bytes f9ffff97
+ 007477e0 bytes f9ffff97
- 0071d640 ["INT_ADD", "register:40f0:8", ["const:71d640:8", "const:4:8"]]
- 0071d640 ["CALL", null, ["local:b0:8"]]
+ 007477ec ["INT_ADD", "register:40f0:8", ["const:7477ec:8", "const:4:8"]]
+ 007477ec ["CALL", null, ["local:b0:8"]]
- 0071d640 bytes f6ffff97
+ 007477ec bytes f6ffff97
- 0071d650 ["INT_ADD", "register:40f0:8", ["const:71d650:8", "const:4:8"]]
- 0071d650 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007477fc ["INT_ADD", "register:40f0:8", ["const:7477fc:8", "const:4:8"]]
+ 007477fc ["CALL", null, ["callee:00c57ab0:8"]]
- 0071d650 bytes 84f61294
+ 007477fc bytes ad401494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0339becd772a3699adfabb59e26913b"></a>

### [`0071e9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e9f0.md) → [`00748b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748b9c.md) FUN_00748b9c

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071ea10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e9f0.md#insn-0071ea10) · [`0071ea4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e9f0.md#insn-0071ea4c) · [`0071ea5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e9f0.md#insn-0071ea5c)
- 新版 `00748bbc`（命令位置の公開資料なし） · `00748bf8`（命令位置の公開資料なし） · `00748c08`（命令位置の公開資料なし）

~~~diff
- 0071ea10 ["INT_ADD", "register:40f0:8", ["const:71ea10:8", "const:4:8"]]
- 0071ea10 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00748bbc ["INT_ADD", "register:40f0:8", ["const:748bbc:8", "const:4:8"]]
+ 00748bbc ["CALL", null, ["callee:00c57ab0:8"]]
- 0071ea10 bytes 94f11294
+ 00748bbc bytes bd3b1494
- 0071ea4c ["INT_ADD", "register:40f0:8", ["const:71ea4c:8", "const:4:8"]]
- 0071ea4c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00748bf8 ["INT_ADD", "register:40f0:8", ["const:748bf8:8", "const:4:8"]]
+ 00748bf8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0071ea4c bytes 85f11294
+ 00748bf8 bytes ae3b1494
- 0071ea5c ["INT_ADD", "register:40f0:8", ["const:71ea5c:8", "const:4:8"]]
- 0071ea5c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00748c08 ["INT_ADD", "register:40f0:8", ["const:748c08:8", "const:4:8"]]
+ 00748c08 ["CALL", null, ["callee:00c57ab0:8"]]
- 0071ea5c bytes 81f11294
+ 00748c08 bytes aa3b1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53764548361e423e3b0ed71f62c0521f"></a>

### [`0071ed70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed70.md) → [`00748f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f1c.md) FUN_00748f1c

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0071e944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e944.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071edb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed70.md#insn-0071edb0)
- 新版 `00748f5c`（命令位置の公開資料なし）

~~~diff
- 0071edb0 ["INT_ADD", "register:40f0:8", ["const:71edb0:8", "const:4:8"]]
- 0071edb0 ["CALL", null, ["callee:00748af0:8"]]
+ 00748f5c ["INT_ADD", "register:40f0:8", ["const:748f5c:8", "const:4:8"]]
+ 00748f5c ["CALL", null, ["callee:00748af0:8"]]
- 0071edb0 bytes e5feff97
+ 00748f5c bytes e5feff97
~~~


<a id="compare-a17aa2e978946d01e7058754bff1f123"></a>

### [`0071f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f798.md) → [`00749944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749944.md) FUN_00749944

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071cb00.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071f7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f798.md#insn-0071f7d4)
- 新版 `00749980`（命令位置の公開資料なし）

~~~diff
- 0071f7d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071f7d4 ["INT_ADD", "register:40f0:8", ["const:71f7d4:8", "const:4:8"]]
- 0071f7d4 ["CALLIND", null, ["register:0:8"]]
+ 00749980 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00749980 ["INT_ADD", "register:40f0:8", ["const:749980:8", "const:4:8"]]
+ 00749980 ["CALLIND", null, ["register:0:8"]]
- 0071f7d4 bytes 00013fd6
+ 00749980 bytes 00013fd6
~~~


<a id="compare-c9595744cf0c3105c8207fb57917ed2a"></a>

### [`0072012c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072012c.md) → [`0074a2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a2d8.md) FUN_0074a2d8

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009749a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00974/009749a4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009aa488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa488.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00720160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072012c.md#insn-00720160) · [`0072017c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072012c.md#insn-0072017c) · [`0072018c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072012c.md#insn-0072018c)
- 新版 `0074a30c`（命令位置の公開資料なし） · `0074a328`（命令位置の公開資料なし） · `0074a338`（命令位置の公開資料なし）

~~~diff
- 00720160 ["INT_ADD", "register:40f0:8", ["const:720160:8", "const:4:8"]]
- 00720160 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0074a30c ["INT_ADD", "register:40f0:8", ["const:74a30c:8", "const:4:8"]]
+ 0074a30c ["CALL", null, ["callee:00c57ab0:8"]]
- 00720160 bytes c0eb1294
+ 0074a30c bytes e9351494
- 0072017c ["INT_ADD", "register:40f0:8", ["const:72017c:8", "const:4:8"]]
- 0072017c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0074a328 ["INT_ADD", "register:40f0:8", ["const:74a328:8", "const:4:8"]]
+ 0074a328 ["CALL", null, ["callee:00c57ab0:8"]]
- 0072017c bytes b9eb1294
+ 0074a328 bytes e2351494
- 0072018c ["INT_ADD", "register:40f0:8", ["const:72018c:8", "const:4:8"]]
- 0072018c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0074a338 ["INT_ADD", "register:40f0:8", ["const:74a338:8", "const:4:8"]]
+ 0074a338 ["CALL", null, ["callee:00c57ab0:8"]]
- 0072018c bytes b5eb1294
+ 0074a338 bytes de351494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8facbc1ab3e6150c609c2739f354c62"></a>

### [`00720390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720390.md) → [`0074a53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a53c.md) FUN_0074a53c

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071cb00.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007203cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720390.md#insn-007203cc)
- 新版 `0074a578`（命令位置の公開資料なし）

~~~diff
- 007203cc ["COPY", "register:0:8", ["register:4040:8"]]
- 007203cc ["INT_ADD", "register:40f0:8", ["const:7203cc:8", "const:4:8"]]
- 007203cc ["CALLIND", null, ["register:0:8"]]
+ 0074a578 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074a578 ["INT_ADD", "register:40f0:8", ["const:74a578:8", "const:4:8"]]
+ 0074a578 ["CALLIND", null, ["register:0:8"]]
- 007203cc bytes 00013fd6
+ 0074a578 bytes 00013fd6
~~~


<a id="compare-904ff2338ff766479180c8afba94b702"></a>

### [`007204e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007204e8.md) → [`0074a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md) FUN_0074a694

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d070.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`007205e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007205e8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0074721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0074a794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00720568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007204e8.md#insn-00720568) · [`00720580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007204e8.md#insn-00720580) · [`007205e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007204e8.md#insn-007205e4)
- 新版 `0074a714`（命令位置の公開資料なし） · `0074a72c`（命令位置の公開資料なし） · `0074a790`（命令位置の公開資料なし）

~~~diff
- 00720568 ["INT_ADD", "register:40f0:8", ["const:720568:8", "const:4:8"]]
- 00720568 ["CALL", null, ["callee:0074a794:8"]]
+ 0074a714 ["INT_ADD", "register:40f0:8", ["const:74a714:8", "const:4:8"]]
+ 0074a714 ["CALL", null, ["callee:0074a794:8"]]
- 00720568 bytes 20000094
+ 0074a714 bytes 20000094
- 00720580 ["INT_ADD", "register:40f0:8", ["const:720580:8", "const:4:8"]]
- 00720580 ["CALL", null, ["callee:0043bae0:8"]]
+ 0074a72c ["INT_ADD", "register:40f0:8", ["const:74a72c:8", "const:4:8"]]
+ 0074a72c ["CALL", null, ["callee:0043bae0:8"]]
- 00720580 bytes 98e2f397
+ 0074a72c bytes edc4f397
- 007205e4 ["INT_ADD", "register:40f0:8", ["const:7205e4:8", "const:4:8"]]
- 007205e4 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0074a790 ["INT_ADD", "register:40f0:8", ["const:74a790:8", "const:4:8"]]
+ 0074a790 ["CALL", null, ["callee:00c57ae0:8"]]
- 007205e4 bytes abea1294
+ 0074a790 bytes d4341494
~~~


<a id="compare-ca876cc0187dd8d786cbcc2f049f4a4b"></a>

### [`007205e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007205e8.md) → [`0074a794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md) FUN_0074a794

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`007204e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007204e8.md) [`00870ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870ab4.md) [`00975180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975180.md) [`00976638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976638.md) [`0097a22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a22c.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 5件 [`0074a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md) [`008a3c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3c54.md) [`009aac64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aac64.md) [`009ac11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac11c.md) [`009afd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009afd0c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007205e8.md#insn-0072063c) · [`00720668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007205e8.md#insn-00720668) · [`00720680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007205e8.md#insn-00720680)
- 新版 `0074a7e8`（命令位置の公開資料なし） · `0074a814`（命令位置の公開資料なし） · `0074a82c`（命令位置の公開資料なし）

~~~diff
- 0072063c ["INT_ADD", "register:40f0:8", ["const:72063c:8", "const:4:8"]]
- 0072063c ["CALL", null, ["callee:0043bae0:8"]]
+ 0074a7e8 ["INT_ADD", "register:40f0:8", ["const:74a7e8:8", "const:4:8"]]
+ 0074a7e8 ["CALL", null, ["callee:0043bae0:8"]]
- 0072063c bytes 69e2f397
+ 0074a7e8 bytes bec4f397
- 00720668 ["INT_ADD", "register:40f0:8", ["const:720668:8", "const:4:8"]]
- 00720668 ["CALL", null, ["callee:00c57a90:8"]]
+ 0074a814 ["INT_ADD", "register:40f0:8", ["const:74a814:8", "const:4:8"]]
+ 0074a814 ["CALL", null, ["callee:00c57a90:8"]]
- 00720668 bytes 76ea1294
+ 0074a814 bytes 9f341494
- 00720680 ["INT_ADD", "register:40f0:8", ["const:720680:8", "const:4:8"]]
- 00720680 ["CALL", null, ["callee:00c57c00:8"]]
+ 0074a82c ["INT_ADD", "register:40f0:8", ["const:74a82c:8", "const:4:8"]]
+ 0074a82c ["CALL", null, ["callee:00c57c00:8"]]
- 00720680 bytes ccea1294
+ 0074a82c bytes f5341494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c020976c4bd8d82570533419bea71181"></a>

### [`0073f458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f458.md) → [`00769764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769764.md) FUN_00769764

採用 · 移動量 `+0x2a30c` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073f474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f458.md#insn-0073f474) · [`0073f494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f458.md#insn-0073f494)
- 新版 `00769780`（命令位置の公開資料なし） · `007697a0`（命令位置の公開資料なし）

~~~diff
- 0073f474 ["INT_ADD", "register:40f0:8", ["const:73f474:8", "const:4:8"]]
- 0073f474 ["CALL", null, ["callee:00c538e0:8"]]
+ 00769780 ["INT_ADD", "register:40f0:8", ["const:769780:8", "const:4:8"]]
+ 00769780 ["CALL", null, ["callee:00c538e0:8"]]
- 0073f474 bytes 875e1294
+ 00769780 bytes 58a81394
- 0073f494 ["COPY", "register:0:8", ["register:4040:8"]]
- 0073f494 ["INT_ADD", "register:40f0:8", ["const:73f494:8", "const:4:8"]]
- 0073f494 ["CALLIND", null, ["register:0:8"]]
+ 007697a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007697a0 ["INT_ADD", "register:40f0:8", ["const:7697a0:8", "const:4:8"]]
+ 007697a0 ["CALLIND", null, ["register:0:8"]]
- 0073f494 bytes 00013fd6
+ 007697a0 bytes 00013fd6
~~~


<a id="compare-0d5a89d7248d7f2ca753ffb336645cf9"></a>

### [`00750db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750db4.md) → [`0077b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b218.md) FUN_0077b218

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00750dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750db4.md#insn-00750dec) · [`00750df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750db4.md#insn-00750df8)
- 新版 `0077b250`（命令位置の公開資料なし） · `0077b25c`（命令位置の公開資料なし）

~~~diff
- 00750dec ["INT_ADD", "register:40f0:8", ["const:750dec:8", "const:4:8"]]
- 00750dec ["CALL", null, ["callee:005c175c:8"]]
+ 0077b250 ["INT_ADD", "register:40f0:8", ["const:77b250:8", "const:4:8"]]
+ 0077b250 ["CALL", null, ["callee:005c175c:8"]]
- 00750dec bytes d030f997
+ 0077b250 bytes 4319f997
- 00750df8 ["INT_ADD", "register:40f0:8", ["const:750df8:8", "const:4:8"]]
- 00750df8 ["CALL", null, ["callee:005c175c:8"]]
+ 0077b25c ["INT_ADD", "register:40f0:8", ["const:77b25c:8", "const:4:8"]]
+ 0077b25c ["CALL", null, ["callee:005c175c:8"]]
- 00750df8 bytes cd30f997
+ 0077b25c bytes 4019f997
~~~


<a id="compare-824fd80cd019d1644e034ac32857928b"></a>

### [`007520b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007520b8.md) → [`0077c51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md) FUN_0077c51c

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00751cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751cec.md) · 呼出先 5件 [`006fc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc120.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0077c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md) · 呼出先 5件 [`00726220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726220.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075210c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007520b8.md#insn-0075210c) · [`00752170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007520b8.md#insn-00752170) · [`00752198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007520b8.md#insn-00752198)
- 新版 `0077c570`（命令位置の公開資料なし） · `0077c5d4`（命令位置の公開資料なし） · `0077c5fc`（命令位置の公開資料なし）

~~~diff
- 0075210c ["INT_ADD", "register:40f0:8", ["const:75210c:8", "const:4:8"]]
- 0075210c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0077c570 ["INT_ADD", "register:40f0:8", ["const:77c570:8", "const:4:8"]]
+ 0077c570 ["CALL", null, ["callee:00c57ab0:8"]]
- 0075210c bytes d5231294
+ 0077c570 bytes 506d1394
- 00752170 ["INT_ADD", "register:40f0:8", ["const:752170:8", "const:4:8"]]
- 00752170 ["CALL", null, ["callee:00c57a90:8"]]
+ 0077c5d4 ["INT_ADD", "register:40f0:8", ["const:77c5d4:8", "const:4:8"]]
+ 0077c5d4 ["CALL", null, ["callee:00c57a90:8"]]
- 00752170 bytes b4231294
+ 0077c5d4 bytes 2f6d1394
- 00752198 ["INT_ADD", "register:40f0:8", ["const:752198:8", "const:4:8"]]
- 00752198 ["CALL", null, ["callee:00c57c00:8"]]
+ 0077c5fc ["INT_ADD", "register:40f0:8", ["const:77c5fc:8", "const:4:8"]]
+ 0077c5fc ["CALL", null, ["callee:00c57c00:8"]]
- 00752198 bytes 06241294
+ 0077c5fc bytes 816d1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc6a3a2e085a3782a615e3aa4106ee54"></a>

### [`0075867c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075867c.md) → [`00782ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ae0.md) FUN_00782ae0

採用 · 移動量 `+0x2a464` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00758698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075867c.md#insn-00758698) · [`007586b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075867c.md#insn-007586b8)
- 新版 `00782afc`（命令位置の公開資料なし） · `00782b1c`（命令位置の公開資料なし）

~~~diff
- 00758698 ["INT_ADD", "register:40f0:8", ["const:758698:8", "const:4:8"]]
- 00758698 ["CALL", null, ["callee:00c538e0:8"]]
+ 00782afc ["INT_ADD", "register:40f0:8", ["const:782afc:8", "const:4:8"]]
+ 00782afc ["CALL", null, ["callee:00c538e0:8"]]
- 00758698 bytes fef91194
+ 00782afc bytes 79431394
- 007586b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007586b8 ["INT_ADD", "register:40f0:8", ["const:7586b8:8", "const:4:8"]]
- 007586b8 ["CALLIND", null, ["register:0:8"]]
+ 00782b1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00782b1c ["INT_ADD", "register:40f0:8", ["const:782b1c:8", "const:4:8"]]
+ 00782b1c ["CALLIND", null, ["register:0:8"]]
- 007586b8 bytes 00013fd6
+ 00782b1c bytes 00013fd6
~~~


<a id="compare-6082d8ae7bf0569cbed549c180f0a71b"></a>

### [`00759510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759510.md) → [`00783974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783974.md) FUN_00783974

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00759530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759510.md#insn-00759530)
- 新版 `00783994`（命令位置の公開資料なし）

~~~diff
- 00759530 ["INT_ADD", "register:40f0:8", ["const:759530:8", "const:4:8"]]
- 00759530 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00783994 ["INT_ADD", "register:40f0:8", ["const:783994:8", "const:4:8"]]
+ 00783994 ["CALL", null, ["callee:00c57ab0:8"]]
- 00759530 bytes cc061294
+ 00783994 bytes 47501394
~~~


<a id="compare-8f2a3cbc084dab1bc2fb407675989a72"></a>

### [`0075d9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d9f0.md) → [`00787ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787ec4.md) FUN_00787ec4

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`0075d8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d8a0.md) · 呼出先 3件 [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`00787d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787d74.md) · 呼出先 3件 [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0075dafc",
      "incomplete_value": true,
      "site": "0075db04",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0075db04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d9f0.md#insn-0075db04) · [`0075daa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d9f0.md#insn-0075daa0) · [`0075dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d9f0.md#insn-0075dabc)
- 新版 `00787fd8`（命令位置の公開資料なし） · `00787f74`（命令位置の公開資料なし） · `00787f90`（命令位置の公開資料なし）

~~~diff
- 0075db04 ["INT_ADD", "register:40f0:8", ["const:75db04:8", "const:4:8"]]
- 0075db04 ["CALL", null, ["callee:00468b9c:8"]]
+ 00787fd8 ["INT_ADD", "register:40f0:8", ["const:787fd8:8", "const:4:8"]]
+ 00787fd8 ["CALL", null, ["callee:00468b9c:8"]]
- 0075db04 bytes 80a0f397
+ 00787fd8 bytes f182f397
- 0075daa0 ["INT_ADD", "register:40f0:8", ["const:75daa0:8", "const:4:8"]]
- 0075daa0 ["CALL", null, ["callee:00469bc4:8"]]
+ 00787f74 ["INT_ADD", "register:40f0:8", ["const:787f74:8", "const:4:8"]]
+ 00787f74 ["CALL", null, ["callee:00469bc4:8"]]
- 0075daa0 bytes a3a4f397
+ 00787f74 bytes 1487f397
- 0075dabc ["INT_ADD", "register:40f0:8", ["const:75dabc:8", "const:4:8"]]
- 0075dabc ["CALL", null, ["callee:00467ab0:8"]]
+ 00787f90 ["INT_ADD", "register:40f0:8", ["const:787f90:8", "const:4:8"]]
+ 00787f90 ["CALL", null, ["callee:00467ab0:8"]]
- 0075dabc bytes 579cf397
+ 00787f90 bytes c87ef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68061db90f2bb6e71f12092f04b2b6a1"></a>

### [`00765730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765730.md) → [`0078fc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fc04.md) FUN_0078fc04

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 1件 [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md)
- 新版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 1件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00765748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765730.md#insn-00765748)
- 新版 `0078fc1c`（命令位置の公開資料なし）

~~~diff
- 00765748 ["INT_ADD", "register:40f0:8", ["const:765748:8", "const:4:8"]]
- 00765748 ["CALL", null, ["callee:00676a20:8"]]
+ 0078fc1c ["INT_ADD", "register:40f0:8", ["const:78fc1c:8", "const:4:8"]]
+ 0078fc1c ["CALL", null, ["callee:00676a20:8"]]
- 00765748 bytes feabfb97
+ 0078fc1c bytes 819bfb97
~~~


<a id="compare-153152c410b500ab41d18fc280ff9578"></a>

### [`0076c0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c0f0.md) → [`007965c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965c4.md) FUN_007965c4

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00771e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/00771e8c.md) · 呼出先 2件 [`0076c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c120.md) [`0076c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c5e4.md)
- 新版 呼出元 1件 [`0079c360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079c360.md) · 呼出先 2件 [`007965f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965f4.md) [`00796ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796ab8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0076c108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c0f0.md#insn-0076c108)
- 新版 `007965dc`（命令位置の公開資料なし）

~~~diff
- 0076c108 ["INT_ADD", "register:40f0:8", ["const:76c108:8", "const:4:8"]]
- 0076c108 ["CALL", null, ["callee:007965f4:8"]]
+ 007965dc ["INT_ADD", "register:40f0:8", ["const:7965dc:8", "const:4:8"]]
+ 007965dc ["CALL", null, ["callee:007965f4:8"]]
- 0076c108 bytes 06000094
+ 007965dc bytes 06000094
~~~


<a id="compare-0fb9e2d39f2ed7629c8b261da3fc483b"></a>

### [`0076d51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d51c.md) → [`007979f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/007979f0.md) FUN_007979f0

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) · 呼出先 2件 [`0077591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/0077591c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 2件 [`0079fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fdf0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0076d564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d51c.md#insn-0076d564) · [`0076d56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d51c.md#insn-0076d56c)
- 新版 `00797a38`（命令位置の公開資料なし） · `00797a40`（命令位置の公開資料なし）

~~~diff
- 0076d564 ["INT_ADD", "register:40f0:8", ["const:76d564:8", "const:4:8"]]
- 0076d564 ["CALL", null, ["callee:00c57a90:8"]]
+ 00797a38 ["INT_ADD", "register:40f0:8", ["const:797a38:8", "const:4:8"]]
+ 00797a38 ["CALL", null, ["callee:00c57a90:8"]]
- 0076d564 bytes b7b61194
+ 00797a38 bytes 16001394
- 0076d56c ["INT_ADD", "register:40f0:8", ["const:76d56c:8", "const:4:8"]]
- 0076d56c ["CALL", null, ["callee:0079fdf0:8"]]
+ 00797a40 ["INT_ADD", "register:40f0:8", ["const:797a40:8", "const:4:8"]]
+ 00797a40 ["CALL", null, ["callee:0079fdf0:8"]]
- 0076d56c bytes ec200094
+ 00797a40 bytes ec200094
~~~


<a id="compare-3ecf56f51660c4956c4b544a5e0315c2"></a>

### [`0076e8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e8c0.md) → [`00798d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798d94.md) FUN_00798d94

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081e868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081e/0081e868.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0076e8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e8c0.md#insn-0076e8f4)
- 新版 `00798dc8`（命令位置の公開資料なし）

~~~diff
- 0076e8f4 ["INT_ADD", "register:40f0:8", ["const:76e8f4:8", "const:4:8"]]
- 0076e8f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00798dc8 ["INT_ADD", "register:40f0:8", ["const:798dc8:8", "const:4:8"]]
+ 00798dc8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0076e8f4 bytes dbb11194
+ 00798dc8 bytes 3afb1294
~~~


<a id="compare-bd3617fc86a79b5e93d6eaf3366e70ed"></a>

### [`0076e910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e910.md) → [`00798de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798de4.md) FUN_00798de4

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081e868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081e/0081e868.md) · 呼出先 4件 [`00772bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772bc4.md) [`0077591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/0077591c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) · 呼出先 4件 [`0079d098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d098.md) [`0079fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fdf0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0076e934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e910.md#insn-0076e934) · [`0076e93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e910.md#insn-0076e93c) · [`0076e950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e910.md#insn-0076e950)
- 新版 `00798e08`（命令位置の公開資料なし） · `00798e10`（命令位置の公開資料なし） · `00798e24`（命令位置の公開資料なし）

~~~diff
- 0076e934 ["INT_ADD", "register:40f0:8", ["const:76e934:8", "const:4:8"]]
- 0076e934 ["CALL", null, ["callee:00c57a90:8"]]
+ 00798e08 ["INT_ADD", "register:40f0:8", ["const:798e08:8", "const:4:8"]]
+ 00798e08 ["CALL", null, ["callee:00c57a90:8"]]
- 0076e934 bytes c3b11194
+ 00798e08 bytes 22fb1294
- 0076e93c ["INT_ADD", "register:40f0:8", ["const:76e93c:8", "const:4:8"]]
- 0076e93c ["CALL", null, ["callee:0079fdf0:8"]]
+ 00798e10 ["INT_ADD", "register:40f0:8", ["const:798e10:8", "const:4:8"]]
+ 00798e10 ["CALL", null, ["callee:0079fdf0:8"]]
- 0076e93c bytes f81b0094
+ 00798e10 bytes f81b0094
- 0076e950 ["INT_ADD", "register:40f0:8", ["const:76e950:8", "const:4:8"]]
- 0076e950 ["CALL", null, ["callee:0079d098:8"]]
+ 00798e24 ["INT_ADD", "register:40f0:8", ["const:798e24:8", "const:4:8"]]
+ 00798e24 ["CALL", null, ["callee:0079d098:8"]]
- 0076e950 bytes 9d100094
+ 00798e24 bytes 9d100094
~~~


<a id="compare-3b022a4d55e0d9417a26aeb32cd2cbe6"></a>

### [`00772a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772a60.md) → [`0079cf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cf34.md) FUN_0079cf34

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007726fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/007726fc.md) [`00776a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776a8c.md) · 呼出先 5件 [`00581cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cd8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`0079cbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cbd0.md) [`007a0f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a0f60.md) · 呼出先 5件 [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00772ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772a60.md#insn-00772ab4) · [`00772b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772a60.md#insn-00772b18) · [`00772b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772a60.md#insn-00772b40)
- 新版 `0079cf88`（命令位置の公開資料なし） · `0079cfec`（命令位置の公開資料なし） · `0079d014`（命令位置の公開資料なし）

~~~diff
- 00772ab4 ["INT_ADD", "register:40f0:8", ["const:772ab4:8", "const:4:8"]]
- 00772ab4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0079cf88 ["INT_ADD", "register:40f0:8", ["const:79cf88:8", "const:4:8"]]
+ 0079cf88 ["CALL", null, ["callee:00c57ab0:8"]]
- 00772ab4 bytes 6ba11194
+ 0079cf88 bytes caea1294
- 00772b18 ["INT_ADD", "register:40f0:8", ["const:772b18:8", "const:4:8"]]
- 00772b18 ["CALL", null, ["callee:00c57a90:8"]]
+ 0079cfec ["INT_ADD", "register:40f0:8", ["const:79cfec:8", "const:4:8"]]
+ 0079cfec ["CALL", null, ["callee:00c57a90:8"]]
- 00772b18 bytes 4aa11194
+ 0079cfec bytes a9ea1294
- 00772b40 ["INT_ADD", "register:40f0:8", ["const:772b40:8", "const:4:8"]]
- 00772b40 ["CALL", null, ["callee:00c57c00:8"]]
+ 0079d014 ["INT_ADD", "register:40f0:8", ["const:79d014:8", "const:4:8"]]
+ 0079d014 ["CALL", null, ["callee:00c57c00:8"]]
- 00772b40 bytes 9ca11194
+ 0079d014 bytes fbea1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29fcbfc4d08aa6bb4998f169e64ef61b"></a>

### [`00772bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772bc4.md) → [`0079d098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d098.md) FUN_0079d098

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0076d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d5c4.md) [`0076e910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e910.md) · 呼出先 2件 [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00797a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797a98.md) [`00798de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798de4.md) · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00772c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772bc4.md#insn-00772c0c) · [`00772c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772bc4.md#insn-00772c1c) · [`00772c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772bc4.md#insn-00772c2c)
- 新版 `0079d0e0`（命令位置の公開資料なし） · `0079d0f0`（命令位置の公開資料なし） · `0079d100`（命令位置の公開資料なし）

~~~diff
- 00772c0c ["INT_ADD", "register:40f0:8", ["const:772c0c:8", "const:4:8"]]
- 00772c0c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0079d0e0 ["INT_ADD", "register:40f0:8", ["const:79d0e0:8", "const:4:8"]]
+ 0079d0e0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00772c0c bytes 15a11194
+ 0079d0e0 bytes 74ea1294
- 00772c1c ["INT_ADD", "register:40f0:8", ["const:772c1c:8", "const:4:8"]]
- 00772c1c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0079d0f0 ["INT_ADD", "register:40f0:8", ["const:79d0f0:8", "const:4:8"]]
+ 0079d0f0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00772c1c bytes 11a11194
+ 0079d0f0 bytes 70ea1294
- 00772c2c ["INT_ADD", "register:40f0:8", ["const:772c2c:8", "const:4:8"]]
- 00772c2c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0079d100 ["INT_ADD", "register:40f0:8", ["const:79d100:8", "const:4:8"]]
+ 0079d100 ["CALL", null, ["callee:00c57ab0:8"]]
- 00772c2c bytes 0da11194
+ 0079d100 bytes 6cea1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-666cf37741731cc8b3bab22da7083ab6"></a>

### [`00772c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772c64.md) → [`0079d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d138.md) FUN_0079d138

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0076d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d5c4.md) [`00772c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772c64.md) · 呼出先 2件 [`00772c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772c64.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00797a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797a98.md) [`0079d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d138.md) · 呼出先 2件 [`0079d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d138.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00772c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772c64.md#insn-00772c80) · [`00772c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772c64.md#insn-00772c8c) · [`00772cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772c64.md#insn-00772cc0)
- 新版 `0079d154`（命令位置の公開資料なし） · `0079d160`（命令位置の公開資料なし） · `0079d194`（命令位置の公開資料なし）

~~~diff
- 00772c80 ["INT_ADD", "register:40f0:8", ["const:772c80:8", "const:4:8"]]
- 00772c80 ["CALL", null, ["local:b0:8"]]
+ 0079d154 ["INT_ADD", "register:40f0:8", ["const:79d154:8", "const:4:8"]]
+ 0079d154 ["CALL", null, ["local:b0:8"]]
- 00772c80 bytes f9ffff97
+ 0079d154 bytes f9ffff97
- 00772c8c ["INT_ADD", "register:40f0:8", ["const:772c8c:8", "const:4:8"]]
- 00772c8c ["CALL", null, ["local:b0:8"]]
+ 0079d160 ["INT_ADD", "register:40f0:8", ["const:79d160:8", "const:4:8"]]
+ 0079d160 ["CALL", null, ["local:b0:8"]]
- 00772c8c bytes f6ffff97
+ 0079d160 bytes f6ffff97
- 00772cc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00772cc0 ["INT_ADD", "register:40f0:8", ["const:772cc0:8", "const:4:8"]]
- 00772cc0 ["CALLIND", null, ["register:0:8"]]
+ 0079d194 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d194 ["INT_ADD", "register:40f0:8", ["const:79d194:8", "const:4:8"]]
+ 0079d194 ["CALLIND", null, ["register:0:8"]]
- 00772cc0 bytes 00013fd6
+ 0079d194 bytes 00013fd6
~~~


<a id="compare-c593d082e786784eeaacc8d9734bc9bb"></a>

### [`00772cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772cd4.md) → [`0079d1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d1a8.md) FUN_0079d1a8

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0076d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d5c4.md) [`00772cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772cd4.md) · 呼出先 2件 [`00772cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772cd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00797a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797a98.md) [`0079d1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d1a8.md) · 呼出先 2件 [`0079d1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d1a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00772cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772cd4.md#insn-00772cf0) · [`00772cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772cd4.md#insn-00772cfc) · [`00772d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772cd4.md#insn-00772d30)
- 新版 `0079d1c4`（命令位置の公開資料なし） · `0079d1d0`（命令位置の公開資料なし） · `0079d204`（命令位置の公開資料なし）

~~~diff
- 00772cf0 ["INT_ADD", "register:40f0:8", ["const:772cf0:8", "const:4:8"]]
- 00772cf0 ["CALL", null, ["local:b0:8"]]
+ 0079d1c4 ["INT_ADD", "register:40f0:8", ["const:79d1c4:8", "const:4:8"]]
+ 0079d1c4 ["CALL", null, ["local:b0:8"]]
- 00772cf0 bytes f9ffff97
+ 0079d1c4 bytes f9ffff97
- 00772cfc ["INT_ADD", "register:40f0:8", ["const:772cfc:8", "const:4:8"]]
- 00772cfc ["CALL", null, ["local:b0:8"]]
+ 0079d1d0 ["INT_ADD", "register:40f0:8", ["const:79d1d0:8", "const:4:8"]]
+ 0079d1d0 ["CALL", null, ["local:b0:8"]]
- 00772cfc bytes f6ffff97
+ 0079d1d0 bytes f6ffff97
- 00772d30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00772d30 ["INT_ADD", "register:40f0:8", ["const:772d30:8", "const:4:8"]]
- 00772d30 ["CALLIND", null, ["register:0:8"]]
+ 0079d204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d204 ["INT_ADD", "register:40f0:8", ["const:79d204:8", "const:4:8"]]
+ 0079d204 ["CALLIND", null, ["register:0:8"]]
- 00772d30 bytes 00013fd6
+ 0079d204 bytes 00013fd6
~~~


<a id="compare-f742b281d686eec50de4ebe43d75c2b5"></a>

### [`00772d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772d44.md) → [`0079d218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d218.md) FUN_0079d218

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0076d670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d670.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00797b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797b44.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00772db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772d44.md#insn-00772db0) · [`00772dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772d44.md#insn-00772dc0) · [`00772de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772d44.md#insn-00772de0)
- 新版 `0079d284`（命令位置の公開資料なし） · `0079d294`（命令位置の公開資料なし） · `0079d2b4`（命令位置の公開資料なし）

~~~diff
- 00772db0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00772db0 ["INT_ADD", "register:40f0:8", ["const:772db0:8", "const:4:8"]]
- 00772db0 ["CALLIND", null, ["register:0:8"]]
+ 0079d284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d284 ["INT_ADD", "register:40f0:8", ["const:79d284:8", "const:4:8"]]
+ 0079d284 ["CALLIND", null, ["register:0:8"]]
- 00772db0 bytes 00013fd6
+ 0079d284 bytes 00013fd6
- 00772dc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00772dc0 ["INT_ADD", "register:40f0:8", ["const:772dc0:8", "const:4:8"]]
- 00772dc0 ["CALLIND", null, ["register:0:8"]]
+ 0079d294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d294 ["INT_ADD", "register:40f0:8", ["const:79d294:8", "const:4:8"]]
+ 0079d294 ["CALLIND", null, ["register:0:8"]]
- 00772dc0 bytes 00013fd6
+ 0079d294 bytes 00013fd6
- 00772de0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00772de0 ["INT_ADD", "register:40f0:8", ["const:772de0:8", "const:4:8"]]
- 00772de0 ["CALLIND", null, ["register:0:8"]]
+ 0079d2b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d2b4 ["INT_ADD", "register:40f0:8", ["const:79d2b4:8", "const:4:8"]]
+ 0079d2b4 ["CALLIND", null, ["register:0:8"]]
- 00772de0 bytes 00013fd6
+ 0079d2b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f07e2761194c80a5626837b0f5f7515"></a>

### [`007733d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007733d8.md) → [`0079d8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d8ac.md) FUN_0079d8ac

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077344c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007733d8.md#insn-0077344c)
- 新版 `0079d920`（命令位置の公開資料なし）

~~~diff
- 0077344c ["INT_ADD", "register:40f0:8", ["const:77344c:8", "const:4:8"]]
- 0077344c ["CALL", null, ["callee:00459d34:8"]]
+ 0079d920 ["INT_ADD", "register:40f0:8", ["const:79d920:8", "const:4:8"]]
+ 0079d920 ["CALL", null, ["callee:00459d34:8"]]
- 0077344c bytes 940ef397
+ 0079d920 bytes 05f1f297
~~~


<a id="compare-69edbffca4cdfdf20a4d5ce4bdee8a99"></a>

### [`00773684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773684.md) → [`0079db58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db58.md) FUN_0079db58

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007736f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773684.md#insn-007736f8)
- 新版 `0079dbcc`（命令位置の公開資料なし）

~~~diff
- 007736f8 ["INT_ADD", "register:40f0:8", ["const:7736f8:8", "const:4:8"]]
- 007736f8 ["CALL", null, ["callee:00459d34:8"]]
+ 0079dbcc ["INT_ADD", "register:40f0:8", ["const:79dbcc:8", "const:4:8"]]
+ 0079dbcc ["CALL", null, ["callee:00459d34:8"]]
- 007736f8 bytes e90df397
+ 0079dbcc bytes 5af0f297
~~~


<a id="compare-a878a4c54fbb9a08dfe8307bfd141bf7"></a>

### [`00773800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773800.md) → [`0079dcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dcd4.md) FUN_0079dcd4

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00773874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773800.md#insn-00773874)
- 新版 `0079dd48`（命令位置の公開資料なし）

~~~diff
- 00773874 ["INT_ADD", "register:40f0:8", ["const:773874:8", "const:4:8"]]
- 00773874 ["CALL", null, ["callee:00459d34:8"]]
+ 0079dd48 ["INT_ADD", "register:40f0:8", ["const:79dd48:8", "const:4:8"]]
+ 0079dd48 ["CALL", null, ["callee:00459d34:8"]]
- 00773874 bytes 8a0df397
+ 0079dd48 bytes fbeff297
~~~


<a id="compare-9f7b84fb0921ede6993802406d93ed76"></a>

### [`00774204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774204.md) → [`0079e6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e6d8.md) FUN_0079e6d8

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00774220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774204.md#insn-00774220)
- 新版 `0079e6f4`（命令位置の公開資料なし）

~~~diff
- 00774220 ["INT_ADD", "register:40f0:8", ["const:774220:8", "const:4:8"]]
- 00774220 ["CALL", null, ["callee:00459d34:8"]]
+ 0079e6f4 ["INT_ADD", "register:40f0:8", ["const:79e6f4:8", "const:4:8"]]
+ 0079e6f4 ["CALL", null, ["callee:00459d34:8"]]
- 00774220 bytes 1f0bf397
+ 0079e6f4 bytes 90edf297
~~~


<a id="compare-243a8723031fe4983efd48f6d87c789f"></a>

### [`00774778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774778.md) → [`0079ec4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ec4c.md) FUN_0079ec4c

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0077047c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077047c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0079a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a950.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007747b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774778.md#insn-007747b8) · [`007747e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774778.md#insn-007747e4)
- 新版 `0079ec8c`（命令位置の公開資料なし） · `0079ecb8`（命令位置の公開資料なし）

~~~diff
- 007747b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007747b8 ["INT_ADD", "register:40f0:8", ["const:7747b8:8", "const:4:8"]]
- 007747b8 ["CALLIND", null, ["register:0:8"]]
+ 0079ec8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ec8c ["INT_ADD", "register:40f0:8", ["const:79ec8c:8", "const:4:8"]]
+ 0079ec8c ["CALLIND", null, ["register:0:8"]]
- 007747b8 bytes 00013fd6
+ 0079ec8c bytes 00013fd6
- 007747e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 007747e4 ["INT_ADD", "register:40f0:8", ["const:7747e4:8", "const:4:8"]]
- 007747e4 ["CALLIND", null, ["register:0:8"]]
+ 0079ecb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ecb8 ["INT_ADD", "register:40f0:8", ["const:79ecb8:8", "const:4:8"]]
+ 0079ecb8 ["CALLIND", null, ["register:0:8"]]
- 007747e4 bytes 00013fd6
+ 0079ecb8 bytes 00013fd6
~~~


<a id="compare-ed2a2711fc8765d125d410d7816c713e"></a>

### [`007761f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/007761f4.md) → [`007a06c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a06c8.md) FUN_007a06c8

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`00777af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777af0.md) [`007791f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00779/007791f4.md) [`00779cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00779/00779cc8.md) [`0077ad2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0077a/0077ad2c.md) [`0077bc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0077b/0077bc14.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 9件 [`007a1fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1fc4.md) [`007a36c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a3/007a36c8.md) [`007a419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a4/007a419c.md) [`007a5200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5200.md) [`007a60e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a6/007a60e8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00776210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/007761f4.md#insn-00776210)
- 新版 `007a06e4`（命令位置の公開資料なし）

~~~diff
- 00776210 ["INT_ADD", "register:40f0:8", ["const:776210:8", "const:4:8"]]
- 00776210 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a06e4 ["INT_ADD", "register:40f0:8", ["const:7a06e4:8", "const:4:8"]]
+ 007a06e4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00776210 bytes 94931194
+ 007a06e4 bytes f3dc1294
~~~


<a id="compare-006501690f3ed84749d01b03b1ecd618"></a>

### [`007770fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007770fc.md) → [`007a15d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a15d0.md) FUN_007a15d0

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00776bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776bfc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`007a10d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a10d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007771bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007770fc.md#insn-007771bc) · [`007771e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007770fc.md#insn-007771e8) · [`00777224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007770fc.md#insn-00777224)
- 新版 `007a1690`（命令位置の公開資料なし） · `007a16bc`（命令位置の公開資料なし） · `007a16f8`（命令位置の公開資料なし）

~~~diff
- 007771bc ["INT_ADD", "register:40f0:8", ["const:7771bc:8", "const:4:8"]]
- 007771bc ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a1690 ["INT_ADD", "register:40f0:8", ["const:7a1690:8", "const:4:8"]]
+ 007a1690 ["CALL", null, ["callee:00c57ab0:8"]]
- 007771bc bytes a98f1194
+ 007a1690 bytes 08d91294
- 007771e8 ["INT_ADD", "register:40f0:8", ["const:7771e8:8", "const:4:8"]]
- 007771e8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a16bc ["INT_ADD", "register:40f0:8", ["const:7a16bc:8", "const:4:8"]]
+ 007a16bc ["CALL", null, ["callee:00c57ab0:8"]]
- 007771e8 bytes 9e8f1194
+ 007a16bc bytes fdd81294
- 00777224 ["INT_ADD", "register:40f0:8", ["const:777224:8", "const:4:8"]]
- 00777224 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a16f8 ["INT_ADD", "register:40f0:8", ["const:7a16f8:8", "const:4:8"]]
+ 007a16f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00777224 bytes 8f8f1194
+ 007a16f8 bytes eed81294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da72feb912daf34848d9a0776d72b422"></a>

### [`007775b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007775b0.md) → [`007a1a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1a84.md) FUN_007a1a84

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007775f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007775b0.md#insn-007775f0) · [`00777600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007775b0.md#insn-00777600)
- 新版 `007a1ac4`（命令位置の公開資料なし） · `007a1ad4`（命令位置の公開資料なし）

~~~diff
- 007775f0 ["INT_ADD", "register:40f0:8", ["const:7775f0:8", "const:4:8"]]
- 007775f0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a1ac4 ["INT_ADD", "register:40f0:8", ["const:7a1ac4:8", "const:4:8"]]
+ 007a1ac4 ["CALL", null, ["callee:00c57ab0:8"]]
- 007775f0 bytes 9c8e1194
+ 007a1ac4 bytes fbd71294
- 00777600 ["INT_ADD", "register:40f0:8", ["const:777600:8", "const:4:8"]]
- 00777600 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a1ad4 ["INT_ADD", "register:40f0:8", ["const:7a1ad4:8", "const:4:8"]]
+ 007a1ad4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00777600 bytes 988e1194
+ 007a1ad4 bytes f7d71294
~~~


<a id="compare-53359427379d4ba991469f8620c09b06"></a>

### [`00777958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777958.md) → [`007a1e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1e2c.md) FUN_007a1e2c

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00775b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775b20.md) [`00776a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776a8c.md) [`00777730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777730.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00581cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cd8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) [`007a0f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a0f60.md) [`007a1c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1c04.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007779b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777958.md#insn-007779b8) · [`007779fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777958.md#insn-007779fc) · [`00777a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777958.md#insn-00777a14)
- 新版 `007a1e8c`（命令位置の公開資料なし） · `007a1ed0`（命令位置の公開資料なし） · `007a1ee8`（命令位置の公開資料なし）

~~~diff
- 007779b8 ["INT_ADD", "register:40f0:8", ["const:7779b8:8", "const:4:8"]]
- 007779b8 ["CALL", null, ["callee:0043bae0:8"]]
+ 007a1e8c ["INT_ADD", "register:40f0:8", ["const:7a1e8c:8", "const:4:8"]]
+ 007a1e8c ["CALL", null, ["callee:0043bae0:8"]]
- 007779b8 bytes 8a85f297
+ 007a1e8c bytes 1567f297
- 007779fc ["INT_ADD", "register:40f0:8", ["const:7779fc:8", "const:4:8"]]
- 007779fc ["CALL", null, ["callee:00c57a90:8"]]
+ 007a1ed0 ["INT_ADD", "register:40f0:8", ["const:7a1ed0:8", "const:4:8"]]
+ 007a1ed0 ["CALL", null, ["callee:00c57a90:8"]]
- 007779fc bytes 918d1194
+ 007a1ed0 bytes f0d61294
- 00777a14 ["INT_ADD", "register:40f0:8", ["const:777a14:8", "const:4:8"]]
- 00777a14 ["CALL", null, ["callee:00c57c00:8"]]
+ 007a1ee8 ["INT_ADD", "register:40f0:8", ["const:7a1ee8:8", "const:4:8"]]
+ 007a1ee8 ["CALL", null, ["callee:00c57c00:8"]]
- 00777a14 bytes e78d1194
+ 007a1ee8 bytes 46d71294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09b480f552f7835d56cc4854e2d4e866"></a>

### [`00777a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777a74.md) → [`007a1f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1f48.md) FUN_007a1f48

採用 · 移動量 `+0x2a4d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00777ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777a74.md#insn-00777ab0) · [`00777ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777a74.md#insn-00777ac0)
- 新版 `007a1f84`（命令位置の公開資料なし） · `007a1f94`（命令位置の公開資料なし）

~~~diff
- 00777ab0 ["INT_ADD", "register:40f0:8", ["const:777ab0:8", "const:4:8"]]
- 00777ab0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a1f84 ["INT_ADD", "register:40f0:8", ["const:7a1f84:8", "const:4:8"]]
+ 007a1f84 ["CALL", null, ["callee:00c57ab0:8"]]
- 00777ab0 bytes 6c8d1194
+ 007a1f84 bytes cbd61294
- 00777ac0 ["INT_ADD", "register:40f0:8", ["const:777ac0:8", "const:4:8"]]
- 00777ac0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a1f94 ["INT_ADD", "register:40f0:8", ["const:7a1f94:8", "const:4:8"]]
+ 007a1f94 ["CALL", null, ["callee:00c57ab0:8"]]
- 00777ac0 bytes 688d1194
+ 007a1f94 bytes c7d61294
~~~


<a id="compare-47257b4d4616318926af9c6adbf739cc"></a>

### [`0077ba84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0077b/0077ba84.md) → [`007a5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5f58.md) FUN_007a5f58

採用 · 移動量 `+0x2a4d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00777af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777af0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`007a1fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1fc4.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077bb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0077b/0077ba84.md#insn-0077bb48) · [`0077bbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0077b/0077ba84.md#insn-0077bbac) · [`0077bbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0077b/0077ba84.md#insn-0077bbd4)
- 新版 `007a601c`（命令位置の公開資料なし） · `007a6080`（命令位置の公開資料なし） · `007a60a8`（命令位置の公開資料なし）

~~~diff
- 0077bb48 ["INT_ADD", "register:40f0:8", ["const:77bb48:8", "const:4:8"]]
- 0077bb48 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a601c ["INT_ADD", "register:40f0:8", ["const:7a601c:8", "const:4:8"]]
+ 007a601c ["CALL", null, ["callee:00c57ab0:8"]]
- 0077bb48 bytes 467d1194
+ 007a601c bytes a5c61294
- 0077bbac ["INT_ADD", "register:40f0:8", ["const:77bbac:8", "const:4:8"]]
- 0077bbac ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a6080 ["INT_ADD", "register:40f0:8", ["const:7a6080:8", "const:4:8"]]
+ 007a6080 ["CALL", null, ["callee:00c57ab0:8"]]
- 0077bbac bytes 2d7d1194
+ 007a6080 bytes 8cc61294
- 0077bbd4 ["INT_ADD", "register:40f0:8", ["const:77bbd4:8", "const:4:8"]]
- 0077bbd4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 007a60a8 ["INT_ADD", "register:40f0:8", ["const:7a60a8:8", "const:4:8"]]
+ 007a60a8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0077bbd4 bytes 237d1194
+ 007a60a8 bytes 82c61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d58c0e9c7d0ffbc3563528f0f4fffd3"></a>

### [`0078c9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078c9a8.md) → [`007bd698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd698.md) FUN_007bd698

採用 · 移動量 `+0x30cf0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078ca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078c9a8.md#insn-0078ca10) · [`0078ca48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078c9a8.md#insn-0078ca48)
- 新版 `007bd700`（命令位置の公開資料なし） · `007bd738`（命令位置の公開資料なし）

~~~diff
- 0078ca10 ["INT_ADD", "register:40f0:8", ["const:78ca10:8", "const:4:8"]]
- 0078ca10 ["CALL", null, ["callee:00c57a90:8"]]
+ 007bd700 ["INT_ADD", "register:40f0:8", ["const:7bd700:8", "const:4:8"]]
+ 007bd700 ["CALL", null, ["callee:00c57a90:8"]]
- 0078ca10 bytes 8c391194
+ 007bd700 bytes e4681294
- 0078ca48 ["INT_ADD", "register:40f0:8", ["const:78ca48:8", "const:4:8"]]
- 0078ca48 ["CALL", null, ["callee:0043bb64:8"]]
+ 007bd738 ["INT_ADD", "register:40f0:8", ["const:7bd738:8", "const:4:8"]]
+ 007bd738 ["CALL", null, ["callee:0043bb64:8"]]
- 0078ca48 bytes 8731f297
+ 007bd738 bytes 0bf9f197
~~~


