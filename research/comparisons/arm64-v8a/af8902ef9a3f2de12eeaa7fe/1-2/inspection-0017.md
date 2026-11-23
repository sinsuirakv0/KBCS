# v15.7.4 → v16.0.0 · 要調査の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-fc62e83d58391f96f968fea3d9e677b6"></a>

### [`008b4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4778.md) → [`008e861c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e861c.md) FUN_008e861c

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b4610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e84b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84b4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b47b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4778.md#insn-008b47b8)
- 新版 [`008e865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e861c.md#insn-008e865c)

~~~diff
- 008b47b8 ["INT_ADD", "register:40f0:8", ["const:8b47b8:8", "const:4:8"]]
- 008b47b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e865c ["INT_ADD", "register:40f0:8", ["const:8e865c:8", "const:4:8"]]
+ 008e865c ["CALL", null, ["callee:00c57ab0:8"]]
- 008b47b8 bytes 2a9a0c94
+ 008e865c bytes 15bd0d94
~~~


<a id="compare-9b370f63adb98f5c00fdd8e4ab9af311"></a>

### [`008b47e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47e0.md) → [`008e8684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8684.md) FUN_008e8684

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`008b493c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b493c.md) [`008b49c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008e87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e87e0.md) [`008e8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b482c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47e0.md#insn-008b482c) · [`008b48ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47e0.md#insn-008b48ac) · [`008b48fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47e0.md#insn-008b48fc)
- 新版 [`008e86d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8684.md#insn-008e86d0) · [`008e8750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8684.md#insn-008e8750) · [`008e87a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8684.md#insn-008e87a0)

~~~diff
- 008b482c ["INT_ADD", "register:40f0:8", ["const:8b482c:8", "const:4:8"]]
- 008b482c ["CALL", null, ["callee:00c57a90:8"]]
+ 008e86d0 ["INT_ADD", "register:40f0:8", ["const:8e86d0:8", "const:4:8"]]
+ 008e86d0 ["CALL", null, ["callee:00c57a90:8"]]
- 008b482c bytes 059a0c94
+ 008e86d0 bytes f0bc0d94
- 008b48ac ["INT_ADD", "register:40f0:8", ["const:8b48ac:8", "const:4:8"]]
- 008b48ac ["CALL", null, ["callee:0043bae0:8"]]
+ 008e8750 ["INT_ADD", "register:40f0:8", ["const:8e8750:8", "const:4:8"]]
+ 008e8750 ["CALL", null, ["callee:0043bae0:8"]]
- 008b48ac bytes cd91ed97
+ 008e8750 bytes e44ced97
- 008b48fc ["INT_ADD", "register:40f0:8", ["const:8b48fc:8", "const:4:8"]]
- 008b48fc ["CALL", null, ["callee:008e8868:8"]]
+ 008e87a0 ["INT_ADD", "register:40f0:8", ["const:8e87a0:8", "const:4:8"]]
+ 008e87a0 ["CALL", null, ["callee:008e8868:8"]]
- 008b48fc bytes 32000094
+ 008e87a0 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b3a157c02444ff6eed823d50b1cc7b1"></a>

### [`008b493c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b493c.md) → [`008e87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e87e0.md) FUN_008e87e0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b47e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47e0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e8684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8684.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b49a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b493c.md#insn-008b49a0)
- 新版 [`008e8844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e87e0.md#insn-008e8844)

~~~diff
- 008b49a0 ["INT_ADD", "register:40f0:8", ["const:8b49a0:8", "const:4:8"]]
- 008b49a0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8844 ["INT_ADD", "register:40f0:8", ["const:8e8844:8", "const:4:8"]]
+ 008e8844 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b49a0 bytes b0990c94
+ 008e8844 bytes 9bbc0d94
~~~


<a id="compare-99b806c5e01553721645f19d90dafe0d"></a>

### [`008b49d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49d8.md) → [`008e887c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e887c.md) FUN_008e887c

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49d8.md#insn-008b4a18)
- 新版 [`008e88bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e887c.md#insn-008e88bc)

~~~diff
- 008b4a18 ["INT_ADD", "register:40f0:8", ["const:8b4a18:8", "const:4:8"]]
- 008b4a18 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e88bc ["INT_ADD", "register:40f0:8", ["const:8e88bc:8", "const:4:8"]]
+ 008e88bc ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4a18 bytes 92990c94
+ 008e88bc bytes 7dbc0d94
~~~


<a id="compare-d1756d98dd3157c64e5e96f7a347c44d"></a>

### [`008b4a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4a2c.md) → [`008e88d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e88d0.md) FUN_008e88d0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`008b4b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4b88.md) [`008b4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008e8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8a2c.md) [`008e8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4a2c.md#insn-008b4a78) · [`008b4af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4a2c.md#insn-008b4af8) · [`008b4b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4a2c.md#insn-008b4b48)
- 新版 [`008e891c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e88d0.md#insn-008e891c) · [`008e899c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e88d0.md#insn-008e899c) · [`008e89ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e88d0.md#insn-008e89ec)

~~~diff
- 008b4a78 ["INT_ADD", "register:40f0:8", ["const:8b4a78:8", "const:4:8"]]
- 008b4a78 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e891c ["INT_ADD", "register:40f0:8", ["const:8e891c:8", "const:4:8"]]
+ 008e891c ["CALL", null, ["callee:00c57a90:8"]]
- 008b4a78 bytes 72990c94
+ 008e891c bytes 5dbc0d94
- 008b4af8 ["INT_ADD", "register:40f0:8", ["const:8b4af8:8", "const:4:8"]]
- 008b4af8 ["CALL", null, ["callee:0043bae0:8"]]
+ 008e899c ["INT_ADD", "register:40f0:8", ["const:8e899c:8", "const:4:8"]]
+ 008e899c ["CALL", null, ["callee:0043bae0:8"]]
- 008b4af8 bytes 3a91ed97
+ 008e899c bytes 514ced97
- 008b4b48 ["INT_ADD", "register:40f0:8", ["const:8b4b48:8", "const:4:8"]]
- 008b4b48 ["CALL", null, ["callee:008e8ab4:8"]]
+ 008e89ec ["INT_ADD", "register:40f0:8", ["const:8e89ec:8", "const:4:8"]]
+ 008e89ec ["CALL", null, ["callee:008e8ab4:8"]]
- 008b4b48 bytes 32000094
+ 008e89ec bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f7630828706dc6a5b4dfba37e0e9ac2"></a>

### [`008b4b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4b88.md) → [`008e8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8a2c.md) FUN_008e8a2c

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b4a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4a2c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e88d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e88d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4b88.md#insn-008b4bec)
- 新版 [`008e8a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8a2c.md#insn-008e8a90)

~~~diff
- 008b4bec ["INT_ADD", "register:40f0:8", ["const:8b4bec:8", "const:4:8"]]
- 008b4bec ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8a90 ["INT_ADD", "register:40f0:8", ["const:8e8a90:8", "const:4:8"]]
+ 008e8a90 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4bec bytes 1d990c94
+ 008e8a90 bytes 08bc0d94
~~~


<a id="compare-58806937b1a071a164103249109f2ba8"></a>

### [`008b4c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c24.md) → [`008e8ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ac8.md) FUN_008e8ac8

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c24.md#insn-008b4c64)
- 新版 [`008e8b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ac8.md#insn-008e8b08)

~~~diff
- 008b4c64 ["INT_ADD", "register:40f0:8", ["const:8b4c64:8", "const:4:8"]]
- 008b4c64 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8b08 ["INT_ADD", "register:40f0:8", ["const:8e8b08:8", "const:4:8"]]
+ 008e8b08 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4c64 bytes ff980c94
+ 008e8b08 bytes eabb0d94
~~~


<a id="compare-58f941586ac87785546893d9a926b502"></a>

### [`008b4c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c78.md) → [`008e8b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8b1c.md) FUN_008e8b1c

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008b45fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b45fc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e84a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c78.md#insn-008b4d00) · [`008b4dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c78.md#insn-008b4dbc) · [`008b4dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c78.md#insn-008b4dd8)
- 新版 [`008e8ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8b1c.md#insn-008e8ba4) · [`008e8c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8b1c.md#insn-008e8c60) · [`008e8c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8b1c.md#insn-008e8c7c)

~~~diff
- 008b4d00 ["INT_ADD", "register:40f0:8", ["const:8b4d00:8", "const:4:8"]]
- 008b4d00 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e8ba4 ["INT_ADD", "register:40f0:8", ["const:8e8ba4:8", "const:4:8"]]
+ 008e8ba4 ["CALL", null, ["callee:00c57a90:8"]]
- 008b4d00 bytes d0980c94
+ 008e8ba4 bytes bbbb0d94
- 008b4dbc ["INT_ADD", "register:40f0:8", ["const:8b4dbc:8", "const:4:8"]]
- 008b4dbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8c60 ["INT_ADD", "register:40f0:8", ["const:8e8c60:8", "const:4:8"]]
+ 008e8c60 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4dbc bytes a9980c94
+ 008e8c60 bytes 94bb0d94
- 008b4dd8 ["INT_ADD", "register:40f0:8", ["const:8b4dd8:8", "const:4:8"]]
- 008b4dd8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8c7c ["INT_ADD", "register:40f0:8", ["const:8e8c7c:8", "const:4:8"]]
+ 008e8c7c ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4dd8 bytes a2980c94
+ 008e8c7c bytes 8dbb0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-802b6f9073ceea7b9878498fa7c0fa62"></a>

### [`008b4e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4e00.md) → [`008e8ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ca4.md) FUN_008e8ca4

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008b450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b450c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e83b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4e00.md#insn-008b4e68) · [`008b4f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4e00.md#insn-008b4f04) · [`008b4f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4e00.md#insn-008b4f20)
- 新版 [`008e8d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ca4.md#insn-008e8d0c) · [`008e8da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ca4.md#insn-008e8da8) · [`008e8dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ca4.md#insn-008e8dc4)

~~~diff
- 008b4e68 ["INT_ADD", "register:40f0:8", ["const:8b4e68:8", "const:4:8"]]
- 008b4e68 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e8d0c ["INT_ADD", "register:40f0:8", ["const:8e8d0c:8", "const:4:8"]]
+ 008e8d0c ["CALL", null, ["callee:00c57a90:8"]]
- 008b4e68 bytes 76980c94
+ 008e8d0c bytes 61bb0d94
- 008b4f04 ["INT_ADD", "register:40f0:8", ["const:8b4f04:8", "const:4:8"]]
- 008b4f04 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8da8 ["INT_ADD", "register:40f0:8", ["const:8e8da8:8", "const:4:8"]]
+ 008e8da8 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4f04 bytes 57980c94
+ 008e8da8 bytes 42bb0d94
- 008b4f20 ["INT_ADD", "register:40f0:8", ["const:8b4f20:8", "const:4:8"]]
- 008b4f20 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8dc4 ["INT_ADD", "register:40f0:8", ["const:8e8dc4:8", "const:4:8"]]
+ 008e8dc4 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4f20 bytes 50980c94
+ 008e8dc4 bytes 3bbb0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7870b556d903d2bd88f9ebc5ceebe4cd"></a>

### [`008b4f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4f48.md) → [`008e8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md) FUN_008e8dec

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008b49c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4f48.md#insn-008b4fb0) · [`008b504c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4f48.md#insn-008b504c) · [`008b5068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4f48.md#insn-008b5068)
- 新版 [`008e8e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md#insn-008e8e54) · [`008e8ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md#insn-008e8ef0) · [`008e8f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md#insn-008e8f0c)

~~~diff
- 008b4fb0 ["INT_ADD", "register:40f0:8", ["const:8b4fb0:8", "const:4:8"]]
- 008b4fb0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e8e54 ["INT_ADD", "register:40f0:8", ["const:8e8e54:8", "const:4:8"]]
+ 008e8e54 ["CALL", null, ["callee:00c57a90:8"]]
- 008b4fb0 bytes 24980c94
+ 008e8e54 bytes 0fbb0d94
- 008b504c ["INT_ADD", "register:40f0:8", ["const:8b504c:8", "const:4:8"]]
- 008b504c ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8ef0 ["INT_ADD", "register:40f0:8", ["const:8e8ef0:8", "const:4:8"]]
+ 008e8ef0 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b504c bytes 05980c94
+ 008e8ef0 bytes f0ba0d94
- 008b5068 ["INT_ADD", "register:40f0:8", ["const:8b5068:8", "const:4:8"]]
- 008b5068 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8f0c ["INT_ADD", "register:40f0:8", ["const:8e8f0c:8", "const:4:8"]]
+ 008e8f0c ["CALL", null, ["callee:00c57ab0:8"]]
- 008b5068 bytes fe970c94
+ 008e8f0c bytes e9ba0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ace99a890e77f11e7d488c3f25a9d54"></a>

### [`008b5090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5090.md) → [`008e8f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f34.md) FUN_008e8f34

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b50e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5090.md#insn-008b50e0)
- 新版 [`008e8f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f34.md#insn-008e8f84)

~~~diff
- 008b50e0 ["INT_ADD", "register:40f0:8", ["const:8b50e0:8", "const:4:8"]]
- 008b50e0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8f84 ["INT_ADD", "register:40f0:8", ["const:8e8f84:8", "const:4:8"]]
+ 008e8f84 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b50e0 bytes e0970c94
+ 008e8f84 bytes cbba0d94
~~~


<a id="compare-883836e16483cb47581104d401053ae7"></a>

### [`008b5240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5240.md) → [`008e90e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e90e4.md) FUN_008e90e4

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5240.md#insn-008b5290)
- 新版 [`008e9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e90e4.md#insn-008e9134)

~~~diff
- 008b5290 ["INT_ADD", "register:40f0:8", ["const:8b5290:8", "const:4:8"]]
- 008b5290 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e9134 ["INT_ADD", "register:40f0:8", ["const:8e9134:8", "const:4:8"]]
+ 008e9134 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b5290 bytes 74970c94
+ 008e9134 bytes 5fba0d94
~~~


<a id="compare-c409f83fe7540f7997c8190d47b2d530"></a>

### [`008b635c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b635c.md) → [`008ea200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea200.md) FUN_008ea200

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b11a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008b4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b63e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b635c.md#insn-008b63e0) · [`008b6430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b635c.md#insn-008b6430) · [`008b64ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b635c.md#insn-008b64ac)
- 新版 [`008ea284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea200.md#insn-008ea284) · [`008ea2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea200.md#insn-008ea2d4) · [`008ea350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea200.md#insn-008ea350)

~~~diff
- 008b63e0 ["INT_ADD", "register:40f0:8", ["const:8b63e0:8", "const:4:8"]]
- 008b63e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea284 ["INT_ADD", "register:40f0:8", ["const:8ea284:8", "const:4:8"]]
+ 008ea284 ["CALL", null, ["callee:00c57a90:8"]]
- 008b63e0 bytes 18930c94
+ 008ea284 bytes 03b60d94
- 008b6430 ["INT_ADD", "register:40f0:8", ["const:8b6430:8", "const:4:8"]]
- 008b6430 ["CALL", null, ["callee:0043bae0:8"]]
+ 008ea2d4 ["INT_ADD", "register:40f0:8", ["const:8ea2d4:8", "const:4:8"]]
+ 008ea2d4 ["CALL", null, ["callee:0043bae0:8"]]
- 008b6430 bytes ec8aed97
+ 008ea2d4 bytes 0346ed97
- 008b64ac ["INT_ADD", "register:40f0:8", ["const:8b64ac:8", "const:4:8"]]
- 008b64ac ["CALL", null, ["callee:00c57ab0:8"]]
+ 008ea350 ["INT_ADD", "register:40f0:8", ["const:8ea350:8", "const:4:8"]]
+ 008ea350 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b64ac bytes ed920c94
+ 008ea350 bytes d8b50d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf72765496b05eceec7ae2d117a03ae"></a>

### [`008b6558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6558.md) → [`008ea3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea3fc.md) FUN_008ea3fc

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b11a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008b49c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b65dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6558.md#insn-008b65dc) · [`008b662c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6558.md#insn-008b662c) · [`008b66a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6558.md#insn-008b66a4)
- 新版 [`008ea480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea3fc.md#insn-008ea480) · [`008ea4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea3fc.md#insn-008ea4d0) · [`008ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea3fc.md#insn-008ea548)

~~~diff
- 008b65dc ["INT_ADD", "register:40f0:8", ["const:8b65dc:8", "const:4:8"]]
- 008b65dc ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea480 ["INT_ADD", "register:40f0:8", ["const:8ea480:8", "const:4:8"]]
+ 008ea480 ["CALL", null, ["callee:00c57a90:8"]]
- 008b65dc bytes 99920c94
+ 008ea480 bytes 84b50d94
- 008b662c ["INT_ADD", "register:40f0:8", ["const:8b662c:8", "const:4:8"]]
- 008b662c ["CALL", null, ["callee:0043bae0:8"]]
+ 008ea4d0 ["INT_ADD", "register:40f0:8", ["const:8ea4d0:8", "const:4:8"]]
+ 008ea4d0 ["CALL", null, ["callee:0043bae0:8"]]
- 008b662c bytes 6d8aed97
+ 008ea4d0 bytes 8445ed97
- 008b66a4 ["INT_ADD", "register:40f0:8", ["const:8b66a4:8", "const:4:8"]]
- 008b66a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008ea548 ["INT_ADD", "register:40f0:8", ["const:8ea548:8", "const:4:8"]]
+ 008ea548 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b66a4 bytes 6f920c94
+ 008ea548 bytes 5ab50d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad3e24873344155cbe5e4cd6048c685c"></a>

### [`008b818c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b818c.md) → [`008ec030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec030.md) FUN_008ec030

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b818c.md#insn-008b81bc) · [`008b81d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b818c.md#insn-008b81d0) · [`008b81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b818c.md#insn-008b81d8)
- 新版 [`008ec060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec030.md#insn-008ec060) · [`008ec074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec030.md#insn-008ec074) · [`008ec07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec030.md#insn-008ec07c)

~~~diff
- 008b81bc ["INT_ADD", "register:40f0:8", ["const:8b81bc:8", "const:4:8"]]
- 008b81bc ["CALL", null, ["callee:00c538e0:8"]]
+ 008ec060 ["INT_ADD", "register:40f0:8", ["const:8ec060:8", "const:4:8"]]
+ 008ec060 ["CALL", null, ["callee:00c538e0:8"]]
- 008b81bc bytes 357b0c94
+ 008ec060 bytes 209e0d94
- 008b81d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b81d0 ["INT_ADD", "register:40f0:8", ["const:8b81d0:8", "const:4:8"]]
- 008b81d0 ["CALLIND", null, ["register:0:8"]]
+ 008ec074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008ec074 ["INT_ADD", "register:40f0:8", ["const:8ec074:8", "const:4:8"]]
+ 008ec074 ["CALLIND", null, ["register:0:8"]]
- 008b81d0 bytes 00013fd6
+ 008ec074 bytes 00013fd6
- 008b81d8 ["INT_ADD", "register:40f0:8", ["const:8b81d8:8", "const:4:8"]]
- 008b81d8 ["CALL", null, ["callee:00c57a80:8"]]
+ 008ec07c ["INT_ADD", "register:40f0:8", ["const:8ec07c:8", "const:4:8"]]
+ 008ec07c ["CALL", null, ["callee:00c57a80:8"]]
- 008b81d8 bytes 968b0c94
+ 008ec07c bytes 81ae0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-503ef482b39623a1f71fc264e2a7d866"></a>

### [`008c82bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c82bc.md) → [`008fc190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc190.md) FUN_008fc190

採用 · 移動量 `+0x33ed4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`008c83f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c83f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008fc2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc2c4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c8364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c82bc.md#insn-008c8364) · [`008c8398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c82bc.md#insn-008c8398) · [`008c83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c82bc.md#insn-008c83e4)
- 新版 [`008fc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc190.md#insn-008fc238) · [`008fc26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc190.md#insn-008fc26c) · [`008fc2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc190.md#insn-008fc2b8)

~~~diff
- 008c8364 ["INT_ADD", "register:40f0:8", ["const:8c8364:8", "const:4:8"]]
- 008c8364 ["CALL", null, ["callee:00c57a90:8"]]
+ 008fc238 ["INT_ADD", "register:40f0:8", ["const:8fc238:8", "const:4:8"]]
+ 008fc238 ["CALL", null, ["callee:00c57a90:8"]]
- 008c8364 bytes 374b0c94
+ 008fc238 bytes 166e0d94
- 008c8398 ["INT_ADD", "register:40f0:8", ["const:8c8398:8", "const:4:8"]]
- 008c8398 ["CALL", null, ["callee:0043bb64:8"]]
+ 008fc26c ["INT_ADD", "register:40f0:8", ["const:8fc26c:8", "const:4:8"]]
+ 008fc26c ["CALL", null, ["callee:0043bb64:8"]]
- 008c8398 bytes 3343ed97
+ 008fc26c bytes 3efeec97
- 008c83e4 ["INT_ADD", "register:40f0:8", ["const:8c83e4:8", "const:4:8"]]
- 008c83e4 ["CALL", null, ["callee:008fc2c4:8"]]
+ 008fc2b8 ["INT_ADD", "register:40f0:8", ["const:8fc2b8:8", "const:4:8"]]
+ 008fc2b8 ["CALL", null, ["callee:008fc2c4:8"]]
- 008c83e4 bytes 03000094
+ 008fc2b8 bytes 03000094
~~~


<a id="compare-c2316d49e0541ad7ca7667ad6b9dfb67"></a>

### [`008c83f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c83f0.md) → [`008fc2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc2c4.md) FUN_008fc2c4

採用 · 移動量 `+0x33ed4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008c82bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c82bc.md) · 呼出先 3件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008fc190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc190.md) · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c84a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c83f0.md#insn-008c84a0) · [`008c84a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c83f0.md#insn-008c84a8) · [`008c855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c83f0.md#insn-008c855c)
- 新版 [`008fc374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc2c4.md#insn-008fc374) · [`008fc37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc2c4.md#insn-008fc37c) · [`008fc430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc2c4.md#insn-008fc430)

~~~diff
- 008c84a0 ["INT_ADD", "register:40f0:8", ["const:8c84a0:8", "const:4:8"]]
- 008c84a0 ["CALL", null, ["callee:004945d0:8"]]
+ 008fc374 ["INT_ADD", "register:40f0:8", ["const:8fc374:8", "const:4:8"]]
+ 008fc374 ["CALL", null, ["callee:004945d0:8"]]
- 008c84a0 bytes a6a4ee97
+ 008fc374 bytes 9760ee97
- 008c84a8 ["INT_ADD", "register:40f0:8", ["const:8c84a8:8", "const:4:8"]]
- 008c84a8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008fc37c ["INT_ADD", "register:40f0:8", ["const:8fc37c:8", "const:4:8"]]
+ 008fc37c ["CALL", null, ["callee:00c57ab0:8"]]
- 008c84a8 bytes ee4a0c94
+ 008fc37c bytes cd6d0d94
- 008c855c ["INT_ADD", "register:40f0:8", ["const:8c855c:8", "const:4:8"]]
- 008c855c ["CALL", null, ["callee:004945d0:8"]]
+ 008fc430 ["INT_ADD", "register:40f0:8", ["const:8fc430:8", "const:4:8"]]
+ 008fc430 ["CALL", null, ["callee:004945d0:8"]]
- 008c855c bytes 77a4ee97
+ 008fc430 bytes 6860ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10baedca321b1f92c1c7cb1d008e7924"></a>

### [`008c8fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8fe4.md) → [`008fceb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fceb8.md) FUN_008fceb8

採用 · 移動量 `+0x33ed4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`008381ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008381ac.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a124.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c8ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8fe4.md#insn-008c8ffc)
- 新版 [`008fced0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fceb8.md#insn-008fced0)

~~~diff
- 008c8ffc ["INT_ADD", "register:40f0:8", ["const:8c8ffc:8", "const:4:8"]]
- 008c8ffc ["CALL", null, ["callee:005c175c:8"]]
+ 008fced0 ["INT_ADD", "register:40f0:8", ["const:8fced0:8", "const:4:8"]]
+ 008fced0 ["CALL", null, ["callee:005c175c:8"]]
- 008c8ffc bytes 4c50f397
+ 008fced0 bytes 2312f397
~~~


<a id="compare-de5690ad605c49814193149de2e58c03"></a>

### [`008c9014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9014.md) → [`008fcee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fcee8.md) FUN_008fcee8

採用 · 移動量 `+0x33ed4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008c8580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8580.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008fc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc454.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008c9068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9014.md#insn-008c9068) · [`008c90bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9014.md#insn-008c90bc) · [`008c90f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9014.md#insn-008c90f0)
- 新版 [`008fcf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fcee8.md#insn-008fcf3c) · [`008fcf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fcee8.md#insn-008fcf90) · [`008fcfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fcee8.md#insn-008fcfc4)

~~~diff
- 008c9068 ["INT_ADD", "register:40f0:8", ["const:8c9068:8", "const:4:8"]]
- 008c9068 ["CALL", null, ["callee:0046d770:8"]]
+ 008fcf3c ["INT_ADD", "register:40f0:8", ["const:8fcf3c:8", "const:4:8"]]
+ 008fcf3c ["CALL", null, ["callee:0046d770:8"]]
- 008c9068 bytes 1c06ee97
+ 008fcf3c bytes 0dc2ed97
- 008c90bc ["INT_ADD", "register:40f0:8", ["const:8c90bc:8", "const:4:8"]]
- 008c90bc ["CALL", null, ["callee:00c57a90:8"]]
+ 008fcf90 ["INT_ADD", "register:40f0:8", ["const:8fcf90:8", "const:4:8"]]
+ 008fcf90 ["CALL", null, ["callee:00c57a90:8"]]
- 008c90bc bytes e1470c94
+ 008fcf90 bytes c06a0d94
- 008c90f0 ["INT_ADD", "register:40f0:8", ["const:8c90f0:8", "const:4:8"]]
- 008c90f0 ["CALL", null, ["callee:0043bb64:8"]]
+ 008fcfc4 ["INT_ADD", "register:40f0:8", ["const:8fcfc4:8", "const:4:8"]]
+ 008fcfc4 ["CALL", null, ["callee:0043bb64:8"]]
- 008c90f0 bytes dd3fed97
+ 008fcfc4 bytes e8faec97
~~~


<a id="compare-9f88d4a7c29895c36e227322a024f67e"></a>

### [`008cb36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb36c.md) → [`008ff23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff23c.md) FUN_008ff23c

採用 · 移動量 `+0x33ed0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008cb384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb36c.md#insn-008cb384) · [`008cb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb36c.md#insn-008cb390)
- 新版 [`008ff254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff23c.md#insn-008ff254) · [`008ff260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff23c.md#insn-008ff260)

~~~diff
- 008cb384 ["INT_ADD", "register:40f0:8", ["const:8cb384:8", "const:4:8"]]
- 008cb384 ["CALL", null, ["callee:005c175c:8"]]
+ 008ff254 ["INT_ADD", "register:40f0:8", ["const:8ff254:8", "const:4:8"]]
+ 008ff254 ["CALL", null, ["callee:005c175c:8"]]
- 008cb384 bytes 6a47f397
+ 008ff254 bytes 4209f397
- 008cb390 ["INT_ADD", "register:40f0:8", ["const:8cb390:8", "const:4:8"]]
- 008cb390 ["CALL", null, ["callee:005c175c:8"]]
+ 008ff260 ["INT_ADD", "register:40f0:8", ["const:8ff260:8", "const:4:8"]]
+ 008ff260 ["CALL", null, ["callee:005c175c:8"]]
- 008cb390 bytes 6747f397
+ 008ff260 bytes 3f09f397
~~~


<a id="compare-3bd93bc1aec24dc14cd41fc18b30dc0c"></a>

### [`008cd248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd248.md) → [`00901118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901118.md) FUN_00901118

採用 · 移動量 `+0x33ed0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd120.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00900ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00900/00900ff0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008cd258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd248.md#insn-008cd258)
- 新版 [`00901128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901118.md#insn-00901128)

~~~diff
- 008cd258 ["INT_ADD", "register:40f0:8", ["const:8cd258:8", "const:4:8"]]
- 008cd258 ["CALL", null, ["callee:00900ff0:8"]]
+ 00901128 ["INT_ADD", "register:40f0:8", ["const:901128:8", "const:4:8"]]
+ 00901128 ["CALL", null, ["callee:00900ff0:8"]]
- 008cd258 bytes b2ffff97
+ 00901128 bytes b2ffff97
~~~


<a id="compare-a8ea0203b3ce045bece3096714ee18b1"></a>

### [`008cd26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd26c.md) → [`0090113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/0090113c.md) FUN_0090113c

採用 · 移動量 `+0x33ed0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008cb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb860.md) [`009e2258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2258.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`007bf8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf8dc.md) [`007bfcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfcb4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`008ff730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff730.md) [`00a3f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f154.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) [`007f1e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e50.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008cd32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd26c.md#insn-008cd32c) · [`008cd354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd26c.md#insn-008cd354) · [`008cd39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd26c.md#insn-008cd39c)
- 新版 [`009011fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/0090113c.md#insn-009011fc) · [`00901224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/0090113c.md#insn-00901224) · [`0090126c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/0090113c.md#insn-0090126c)

~~~diff
- 008cd32c ["INT_ADD", "register:40f0:8", ["const:8cd32c:8", "const:4:8"]]
- 008cd32c ["CALL", null, ["callee:00c57a90:8"]]
+ 009011fc ["INT_ADD", "register:40f0:8", ["const:9011fc:8", "const:4:8"]]
+ 009011fc ["CALL", null, ["callee:00c57a90:8"]]
- 008cd32c bytes 45370c94
+ 009011fc bytes 255a0d94
- 008cd354 ["INT_ADD", "register:40f0:8", ["const:8cd354:8", "const:4:8"]]
- 008cd354 ["CALL", null, ["callee:007f1a78:8"]]
+ 00901224 ["INT_ADD", "register:40f0:8", ["const:901224:8", "const:4:8"]]
+ 00901224 ["CALL", null, ["callee:007f1a78:8"]]
- 008cd354 bytes 62c9fb97
+ 00901224 bytes 15c2fb97
- 008cd39c ["INT_ADD", "register:40f0:8", ["const:8cd39c:8", "const:4:8"]]
- 008cd39c ["CALL", null, ["callee:007f1a78:8"]]
+ 0090126c ["INT_ADD", "register:40f0:8", ["const:90126c:8", "const:4:8"]]
+ 0090126c ["CALL", null, ["callee:007f1a78:8"]]
- 008cd39c bytes 50c9fb97
+ 0090126c bytes 03c2fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38fc96bf164a326655851fda9d8feaf2"></a>

### [`008cf728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cf728.md) → [`009037e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/009037e0.md) FUN_009037e0

採用 · 移動量 `+0x340b8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 2件 [`008cf74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cf74c.md) [`008cfa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cfa1c.md)
- 新版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 2件 [`00903804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903804.md) [`00903ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903ad4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008cf738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cf728.md#insn-008cf738)
- 新版 [`009037f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/009037e0.md#insn-009037f0)

~~~diff
- 008cf738 ["INT_ADD", "register:40f0:8", ["const:8cf738:8", "const:4:8"]]
- 008cf738 ["CALL", null, ["callee:00903804:8"]]
+ 009037f0 ["INT_ADD", "register:40f0:8", ["const:9037f0:8", "const:4:8"]]
+ 009037f0 ["CALL", null, ["callee:00903804:8"]]
- 008cf738 bytes 05000094
+ 009037f0 bytes 05000094
~~~


<a id="compare-fa193326ce16645ed4c4d2d32e86e72b"></a>

### [`008d0050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0050.md) → [`00904108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904108.md) FUN_00904108

採用 · 移動量 `+0x340b8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d0064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0050.md#insn-008d0064)
- 新版 [`0090411c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904108.md#insn-0090411c)

~~~diff
- 008d0064 ["INT_ADD", "register:40f0:8", ["const:8d0064:8", "const:4:8"]]
- 008d0064 ["CALL", null, ["callee:004802b8:8"]]
+ 0090411c ["INT_ADD", "register:40f0:8", ["const:90411c:8", "const:4:8"]]
+ 0090411c ["CALL", null, ["callee:004802b8:8"]]
- 008d0064 bytes ef34ee97
+ 0090411c bytes 67f0ed97
~~~


<a id="compare-6d3fb9403836d3e5c357e68a9a3e148c"></a>

### [`008d00a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d00a0.md) → [`00904158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904158.md) FUN_00904158

採用 · 移動量 `+0x340b8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008cf74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cf74c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008d0224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0224.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00903804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903804.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`009042dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/009042dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d0128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d00a0.md#insn-008d0128) · [`008d01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d00a0.md#insn-008d01e0) · [`008d01fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d00a0.md#insn-008d01fc)
- 新版 [`009041e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904158.md#insn-009041e0) · [`00904298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904158.md#insn-00904298) · [`009042b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904158.md#insn-009042b4)

~~~diff
- 008d0128 ["INT_ADD", "register:40f0:8", ["const:8d0128:8", "const:4:8"]]
- 008d0128 ["CALL", null, ["callee:00c57a90:8"]]
+ 009041e0 ["INT_ADD", "register:40f0:8", ["const:9041e0:8", "const:4:8"]]
+ 009041e0 ["CALL", null, ["callee:00c57a90:8"]]
- 008d0128 bytes c62b0c94
+ 009041e0 bytes 2c4e0d94
- 008d01e0 ["INT_ADD", "register:40f0:8", ["const:8d01e0:8", "const:4:8"]]
- 008d01e0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00904298 ["INT_ADD", "register:40f0:8", ["const:904298:8", "const:4:8"]]
+ 00904298 ["CALL", null, ["callee:00c57ab0:8"]]
- 008d01e0 bytes a02b0c94
+ 00904298 bytes 064e0d94
- 008d01fc ["INT_ADD", "register:40f0:8", ["const:8d01fc:8", "const:4:8"]]
- 008d01fc ["CALL", null, ["callee:00c57ab0:8"]]
+ 009042b4 ["INT_ADD", "register:40f0:8", ["const:9042b4:8", "const:4:8"]]
+ 009042b4 ["CALL", null, ["callee:00c57ab0:8"]]
- 008d01fc bytes 992b0c94
+ 009042b4 bytes ff4d0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa66cfdfbb451fc6ab673f782e78cb5"></a>

### [`008d0238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0238.md) → [`009042f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/009042f0.md) FUN_009042f0

採用 · 移動量 `+0x340b8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008cfa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cfa1c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008d03bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d03bc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00903ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903ad4.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00904474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904474.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d02c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0238.md#insn-008d02c0) · [`008d0378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0238.md#insn-008d0378) · [`008d0394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0238.md#insn-008d0394)
- 新版 [`00904378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/009042f0.md#insn-00904378) · [`00904430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/009042f0.md#insn-00904430) · [`0090444c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/009042f0.md#insn-0090444c)

~~~diff
- 008d02c0 ["INT_ADD", "register:40f0:8", ["const:8d02c0:8", "const:4:8"]]
- 008d02c0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00904378 ["INT_ADD", "register:40f0:8", ["const:904378:8", "const:4:8"]]
+ 00904378 ["CALL", null, ["callee:00c57a90:8"]]
- 008d02c0 bytes 602b0c94
+ 00904378 bytes c64d0d94
- 008d0378 ["INT_ADD", "register:40f0:8", ["const:8d0378:8", "const:4:8"]]
- 008d0378 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00904430 ["INT_ADD", "register:40f0:8", ["const:904430:8", "const:4:8"]]
+ 00904430 ["CALL", null, ["callee:00c57ab0:8"]]
- 008d0378 bytes 3a2b0c94
+ 00904430 bytes a04d0d94
- 008d0394 ["INT_ADD", "register:40f0:8", ["const:8d0394:8", "const:4:8"]]
- 008d0394 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0090444c ["INT_ADD", "register:40f0:8", ["const:90444c:8", "const:4:8"]]
+ 0090444c ["CALL", null, ["callee:00c57ab0:8"]]
- 008d0394 bytes 332b0c94
+ 0090444c bytes 994d0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b36460f15084a75b13aff3a9be70d3be"></a>

### [`008d5d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d5/008d5d88.md) → [`00909e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00909/00909e44.md) FUN_00909e44

採用 · 移動量 `+0x340bc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`008d0760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0760.md) [`00a11d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a11/00a11d04.md) [`00a154a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a15/00a154a8.md) [`00a1e46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e46c.md) [`00ace5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ace/00ace5d8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`008ec2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ec/008ec2d8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 5件 [`00904818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904818.md) [`00a6fb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md) [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) [`00a7c2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c2fc.md) [`00b2e090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2e/00b2e090.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00920364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00920/00920364.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d5ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d5/008d5d88.md#insn-008d5ddc) · [`008d5dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d5/008d5d88.md#insn-008d5dec) · [`008d5e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d5/008d5d88.md#insn-008d5e1c)
- 新版 [`00909e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00909/00909e44.md#insn-00909e98) · [`00909ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00909/00909e44.md#insn-00909ea8) · [`00909ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00909/00909e44.md#insn-00909ed8)

~~~diff
- 008d5ddc ["INT_ADD", "register:40f0:8", ["const:8d5ddc:8", "const:4:8"]]
- 008d5ddc ["CALL", null, ["callee:0043bae0:8"]]
+ 00909e98 ["INT_ADD", "register:40f0:8", ["const:909e98:8", "const:4:8"]]
+ 00909e98 ["CALL", null, ["callee:0043bae0:8"]]
- 008d5ddc bytes 810ced97
+ 00909e98 bytes 12c7ec97
- 008d5dec ["INT_ADD", "register:40f0:8", ["const:8d5dec:8", "const:4:8"]]
- 008d5dec ["CALL", null, ["callee:0043bae0:8"]]
+ 00909ea8 ["INT_ADD", "register:40f0:8", ["const:909ea8:8", "const:4:8"]]
+ 00909ea8 ["CALL", null, ["callee:0043bae0:8"]]
- 008d5dec bytes 7d0ced97
+ 00909ea8 bytes 0ec7ec97
- 008d5e1c ["INT_ADD", "register:40f0:8", ["const:8d5e1c:8", "const:4:8"]]
- 008d5e1c ["CALL", null, ["callee:00920364:8"]]
+ 00909ed8 ["INT_ADD", "register:40f0:8", ["const:909ed8:8", "const:4:8"]]
+ 00909ed8 ["CALL", null, ["callee:00920364:8"]]
- 008d5e1c bytes 2f590094
+ 00909ed8 bytes 23590094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0ec768d15e27a7b46d5193755bca934"></a>

### [`008ec2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ec/008ec2b4.md) → [`00920340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00920/00920340.md) FUN_00920340

採用 · 移動量 `+0x3408c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008ec0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ec/008ec0b0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0092013c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00920/0092013c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ec2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ec/008ec2b4.md#insn-008ec2c4)
- 新版 [`00920350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00920/00920340.md#insn-00920350)

~~~diff
- 008ec2c4 ["INT_ADD", "register:40f0:8", ["const:8ec2c4:8", "const:4:8"]]
- 008ec2c4 ["CALL", null, ["callee:0092013c:8"]]
+ 00920350 ["INT_ADD", "register:40f0:8", ["const:920350:8", "const:4:8"]]
+ 00920350 ["CALL", null, ["callee:0092013c:8"]]
- 008ec2c4 bytes 7bffff97
+ 00920350 bytes 7bffff97
~~~


<a id="compare-c510e4bd94e60262ab526efe2bda001c"></a>

### [`008f2e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f2/008f2e74.md) → [`00926f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926f00.md) FUN_00926f00

採用 · 移動量 `+0x3408c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008f2c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f2/008f2c38.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00926cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926cc4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008f2e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f2/008f2e74.md#insn-008f2e84)
- 新版 [`00926f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926f00.md#insn-00926f10)

~~~diff
- 008f2e84 ["INT_ADD", "register:40f0:8", ["const:8f2e84:8", "const:4:8"]]
- 008f2e84 ["CALL", null, ["callee:00926cc4:8"]]
+ 00926f10 ["INT_ADD", "register:40f0:8", ["const:926f10:8", "const:4:8"]]
+ 00926f10 ["CALL", null, ["callee:00926cc4:8"]]
- 008f2e84 bytes 6dffff97
+ 00926f10 bytes 6dffff97
~~~


<a id="compare-9d0d8267de52c17e3a746bc21414e796"></a>

### [`008f598c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f5/008f598c.md) → [`00929a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929a18.md) FUN_00929a18

採用 · 移動量 `+0x3408c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 3件 [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md) [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00929a38",
      "incomplete_value": true,
      "site": "00929a40",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008f59bc",
      "incomplete_value": true,
      "site": "008f59c4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008f59b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f5/008f598c.md#insn-008f59b4) · [`008f59c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f5/008f598c.md#insn-008f59c4) · [`008f59a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f5/008f598c.md#insn-008f59a4)
- 新版 [`00929a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929a18.md#insn-00929a40) · [`00929a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929a18.md#insn-00929a50) · [`00929a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929a18.md#insn-00929a30)

~~~diff
- 008f59b4 ["INT_ADD", "register:40f0:8", ["const:8f59b4:8", "const:4:8"]]
- 008f59b4 ["CALL", null, ["callee:00480138:8"]]
+ 00929a40 ["INT_ADD", "register:40f0:8", ["const:929a40:8", "const:4:8"]]
+ 00929a40 ["CALL", null, ["callee:00480138:8"]]
- 008f59b4 bytes 3b9eed97
+ 00929a40 bytes be59ed97
- 008f59c4 ["INT_ADD", "register:40f0:8", ["const:8f59c4:8", "const:4:8"]]
- 008f59c4 ["CALL", null, ["callee:004803b0:8"]]
+ 00929a50 ["INT_ADD", "register:40f0:8", ["const:929a50:8", "const:4:8"]]
+ 00929a50 ["CALL", null, ["callee:004803b0:8"]]
- 008f59c4 bytes d59eed97
+ 00929a50 bytes 585aed97
- 008f59a4 ["INT_ADD", "register:40f0:8", ["const:8f59a4:8", "const:4:8"]]
- 008f59a4 ["CALL", null, ["callee:00480138:8"]]
+ 00929a30 ["INT_ADD", "register:40f0:8", ["const:929a30:8", "const:4:8"]]
+ 00929a30 ["CALL", null, ["callee:00480138:8"]]
- 008f59a4 bytes 3f9eed97
+ 00929a30 bytes c259ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde462690cda0020a4ca45f6d9b7facb"></a>

### [`008fbb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbb48.md) → [`009301f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009301f8.md) FUN_009301f8

採用 · 移動量 `+0x346b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) [`00a3ac60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3ac60.md) [`00a3ae14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3ae14.md) · 呼出先 3件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 3件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) [`00a98b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a98/00a98b54.md) [`00a98d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a98/00a98d08.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008fbb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbb48.md#insn-008fbb74) · [`008fbb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbb48.md#insn-008fbb8c) · [`008fbbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbb48.md#insn-008fbbb0)
- 新版 [`00930224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009301f8.md#insn-00930224) · [`0093023c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009301f8.md#insn-0093023c) · [`00930260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009301f8.md#insn-00930260)

~~~diff
- 008fbb74 ["INT_ADD", "register:40f0:8", ["const:8fbb74:8", "const:4:8"]]
- 008fbb74 ["CALL", null, ["callee:00c538b0:8"]]
+ 00930224 ["INT_ADD", "register:40f0:8", ["const:930224:8", "const:4:8"]]
+ 00930224 ["CALL", null, ["callee:00c538b0:8"]]
- 008fbb74 bytes bb6c0b94
+ 00930224 bytes a38d0c94
- 008fbb8c ["INT_ADD", "register:40f0:8", ["const:8fbb8c:8", "const:4:8"]]
- 008fbb8c ["CALL", null, ["callee:00c538e0:8"]]
+ 0093023c ["INT_ADD", "register:40f0:8", ["const:93023c:8", "const:4:8"]]
+ 0093023c ["CALL", null, ["callee:00c538e0:8"]]
- 008fbb8c bytes c16c0b94
+ 0093023c bytes a98d0c94
- 008fbbb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008fbbb0 ["INT_ADD", "register:40f0:8", ["const:8fbbb0:8", "const:4:8"]]
- 008fbbb0 ["CALLIND", null, ["register:0:8"]]
+ 00930260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00930260 ["INT_ADD", "register:40f0:8", ["const:930260:8", "const:4:8"]]
+ 00930260 ["CALLIND", null, ["register:0:8"]]
- 008fbbb0 bytes 00013fd6
+ 00930260 bytes 00013fd6
~~~


<a id="compare-c41286e33ee8529814cf8ba3bcd1dbfd"></a>

### [`00902dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00902/00902dd0.md) → [`00937804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937804.md) FUN_00937804

採用 · 移動量 `+0x34a34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00902e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00902/00902dd0.md#insn-00902e68) · [`00902ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00902/00902dd0.md#insn-00902ec0)
- 新版 [`0093789c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937804.md#insn-0093789c) · [`009378f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937804.md#insn-009378f4)

~~~diff
- 00902e68 ["INT_ADD", "register:40f0:8", ["const:902e68:8", "const:4:8"]]
- 00902e68 ["CALL", null, ["callee:00c57a90:8"]]
+ 0093789c ["INT_ADD", "register:40f0:8", ["const:93789c:8", "const:4:8"]]
+ 0093789c ["CALL", null, ["callee:00c57a90:8"]]
- 00902e68 bytes 76600b94
+ 0093789c bytes 7d800c94
- 00902ec0 ["INT_ADD", "register:40f0:8", ["const:902ec0:8", "const:4:8"]]
- 00902ec0 ["CALL", null, ["callee:0043bb64:8"]]
+ 009378f4 ["INT_ADD", "register:40f0:8", ["const:9378f4:8", "const:4:8"]]
+ 009378f4 ["CALL", null, ["callee:0043bb64:8"]]
- 00902ec0 bytes 6958ec97
+ 009378f4 bytes 9c10ec97
~~~


<a id="compare-a14ff5b18cc9e5f01b4b4a93cd99cf24"></a>

### [`009055a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/009055a4.md) → [`00939fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00939/00939fdc.md) FUN_00939fdc

採用 · 移動量 `+0x34a38` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009055c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/009055a4.md#insn-009055c0)
- 新版 [`00939ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00939/00939fdc.md#insn-00939ff8)

~~~diff
- 009055c0 ["INT_ADD", "register:40f0:8", ["const:9055c0:8", "const:4:8"]]
- 009055c0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00939ff8 ["INT_ADD", "register:40f0:8", ["const:939ff8:8", "const:4:8"]]
+ 00939ff8 ["CALL", null, ["callee:00c57ab0:8"]]
- 009055c0 bytes a8560b94
+ 00939ff8 bytes ae760c94
~~~


<a id="compare-6584fa88e2f0cf4cdaf09f177f5a7c90"></a>

### [`009055e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/009055e8.md) → [`0093a020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093a/0093a020.md) FUN_0093a020

採用 · 移動量 `+0x34a38` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 2件 [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00905604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/009055e8.md#insn-00905604) · [`0090561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/009055e8.md#insn-0090561c)
- 新版 [`0093a03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093a/0093a020.md#insn-0093a03c) · [`0093a054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093a/0093a020.md#insn-0093a054)

~~~diff
- 00905604 ["INT_ADD", "register:40f0:8", ["const:905604:8", "const:4:8"]]
- 00905604 ["CALL", null, ["callee:005c3e3c:8"]]
+ 0093a03c ["INT_ADD", "register:40f0:8", ["const:93a03c:8", "const:4:8"]]
+ 0093a03c ["CALL", null, ["callee:005c3e3c:8"]]
- 00905604 bytes 8268f297
+ 0093a03c bytes 8027f297
- 0090561c ["INT_ADD", "register:40f0:8", ["const:90561c:8", "const:4:8"]]
- 0090561c ["CALL", null, ["callee:00676a20:8"]]
+ 0093a054 ["INT_ADD", "register:40f0:8", ["const:93a054:8", "const:4:8"]]
+ 0093a054 ["CALL", null, ["callee:00676a20:8"]]
- 0090561c bytes 492cf597
+ 0093a054 bytes 73f2f497
~~~


<a id="compare-2f74347d4aed82f9830c47a4b6bb0ba6"></a>

### [`00905c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/00905c04.md) → [`0093a63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093a/0093a63c.md) FUN_0093a63c

採用 · 移動量 `+0x34a38` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00905c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/00905c04.md#insn-00905c9c) · [`00905cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/00905c04.md#insn-00905cdc)
- 新版 [`0093a6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093a/0093a63c.md#insn-0093a6d4) · [`0093a714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093a/0093a63c.md#insn-0093a714)

~~~diff
- 00905c9c ["INT_ADD", "register:40f0:8", ["const:905c9c:8", "const:4:8"]]
- 00905c9c ["CALL", null, ["callee:00c57a90:8"]]
+ 0093a6d4 ["INT_ADD", "register:40f0:8", ["const:93a6d4:8", "const:4:8"]]
+ 0093a6d4 ["CALL", null, ["callee:00c57a90:8"]]
- 00905c9c bytes e9540b94
+ 0093a6d4 bytes ef740c94
- 00905cdc ["INT_ADD", "register:40f0:8", ["const:905cdc:8", "const:4:8"]]
- 00905cdc ["CALL", null, ["callee:0043bb64:8"]]
+ 0093a714 ["INT_ADD", "register:40f0:8", ["const:93a714:8", "const:4:8"]]
+ 0093a714 ["CALL", null, ["callee:0043bb64:8"]]
- 00905cdc bytes e24cec97
+ 0093a714 bytes 1405ec97
~~~


<a id="compare-84bdd8a3e0532f3ad6ddf7286854535c"></a>

### [`00906ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906ad0.md) → [`0093b508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b508.md) FUN_0093b508

採用 · 移動量 `+0x34a38` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00906b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906ad0.md#insn-00906b38) · [`00906b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906ad0.md#insn-00906b70)
- 新版 [`0093b570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b508.md#insn-0093b570) · [`0093b5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b508.md#insn-0093b5a8)

~~~diff
- 00906b38 ["INT_ADD", "register:40f0:8", ["const:906b38:8", "const:4:8"]]
- 00906b38 ["CALL", null, ["callee:00c57a90:8"]]
+ 0093b570 ["INT_ADD", "register:40f0:8", ["const:93b570:8", "const:4:8"]]
+ 0093b570 ["CALL", null, ["callee:00c57a90:8"]]
- 00906b38 bytes 42510b94
+ 0093b570 bytes 48710c94
- 00906b70 ["INT_ADD", "register:40f0:8", ["const:906b70:8", "const:4:8"]]
- 00906b70 ["CALL", null, ["callee:0043bb64:8"]]
+ 0093b5a8 ["INT_ADD", "register:40f0:8", ["const:93b5a8:8", "const:4:8"]]
+ 0093b5a8 ["CALL", null, ["callee:0043bb64:8"]]
- 00906b70 bytes 3d49ec97
+ 0093b5a8 bytes 6f01ec97
~~~


<a id="compare-94cf64b4193686657b07f30624b309cb"></a>

### [`00909fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00909/00909fd4.md) → [`0093ed98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md) FUN_0093ed98

採用 · 移動量 `+0x34dc4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090a04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00909/00909fd4.md#insn-0090a04c) · [`0090a05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00909/00909fd4.md#insn-0090a05c) · [`0090a070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00909/00909fd4.md#insn-0090a070)
- 新版 [`0093ee10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md#insn-0093ee10) · [`0093ee20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md#insn-0093ee20) · [`0093ee34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ed98.md#insn-0093ee34)

~~~diff
- 0090a04c ["INT_ADD", "register:40f0:8", ["const:90a04c:8", "const:4:8"]]
- 0090a04c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0093ee10 ["INT_ADD", "register:40f0:8", ["const:93ee10:8", "const:4:8"]]
+ 0093ee10 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090a04c bytes 05440b94
+ 0093ee10 bytes 28630c94
- 0090a05c ["INT_ADD", "register:40f0:8", ["const:90a05c:8", "const:4:8"]]
- 0090a05c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0093ee20 ["INT_ADD", "register:40f0:8", ["const:93ee20:8", "const:4:8"]]
+ 0093ee20 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090a05c bytes 01440b94
+ 0093ee20 bytes 24630c94
- 0090a070 ["INT_ADD", "register:40f0:8", ["const:90a070:8", "const:4:8"]]
- 0090a070 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0093ee34 ["INT_ADD", "register:40f0:8", ["const:93ee34:8", "const:4:8"]]
+ 0093ee34 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090a070 bytes fc430b94
+ 0093ee34 bytes 1f630c94
~~~


<a id="compare-582faccbeb4b6171ab7b02bc8f3306a8"></a>

### [`0090a0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a0a8.md) → [`0093ee80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ee80.md) FUN_0093ee80

採用 · 移動量 `+0x34dd8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090a0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a0a8.md#insn-0090a0f0)
- 新版 [`0093eec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093ee80.md#insn-0093eec8)

~~~diff
- 0090a0f0 ["INT_ADD", "register:40f0:8", ["const:90a0f0:8", "const:4:8"]]
- 0090a0f0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0093eec8 ["INT_ADD", "register:40f0:8", ["const:93eec8:8", "const:4:8"]]
+ 0093eec8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090a0f0 bytes dc430b94
+ 0093eec8 bytes fa620c94
~~~


<a id="compare-8248f9f4b257a42ab9eaebd5065a4e93"></a>

### [`0090a130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a130.md) → [`0093f03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md) FUN_0093f03c

採用 · 移動量 `+0x34f0c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009044e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00904/009044e0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0090a308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a308.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00938f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0093f214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f214.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090a1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a130.md#insn-0090a1d0) · [`0090a2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a130.md#insn-0090a2b4) · [`0090a2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a130.md#insn-0090a2c4)
- 新版 [`0093f0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md#insn-0093f0dc) · [`0093f1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md#insn-0093f1c0) · [`0093f1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md#insn-0093f1d0)

~~~diff
- 0090a1d0 ["INT_ADD", "register:40f0:8", ["const:90a1d0:8", "const:4:8"]]
- 0090a1d0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0093f0dc ["INT_ADD", "register:40f0:8", ["const:93f0dc:8", "const:4:8"]]
+ 0093f0dc ["CALL", null, ["callee:00c57a90:8"]]
- 0090a1d0 bytes 9c430b94
+ 0093f0dc bytes 6d620c94
- 0090a2b4 ["INT_ADD", "register:40f0:8", ["const:90a2b4:8", "const:4:8"]]
- 0090a2b4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0093f1c0 ["INT_ADD", "register:40f0:8", ["const:93f1c0:8", "const:4:8"]]
+ 0093f1c0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090a2b4 bytes 6b430b94
+ 0093f1c0 bytes 3c620c94
- 0090a2c4 ["INT_ADD", "register:40f0:8", ["const:90a2c4:8", "const:4:8"]]
- 0090a2c4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0093f1d0 ["INT_ADD", "register:40f0:8", ["const:93f1d0:8", "const:4:8"]]
+ 0093f1d0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090a2c4 bytes 67430b94
+ 0093f1d0 bytes 38620c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89c697ae34a09dfca66d868ed2b87305"></a>

### [`0090f630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f630.md) → [`0094453c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md) FUN_0094453c

採用 · 移動量 `+0x34f0c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090f69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f630.md#insn-0090f69c) · [`0090f6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f630.md#insn-0090f6ac) · [`0090f6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f630.md#insn-0090f6bc)
- 新版 [`009445a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md#insn-009445a8) · [`009445b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md#insn-009445b8) · [`009445c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/0094453c.md#insn-009445c8)

~~~diff
- 0090f69c ["INT_ADD", "register:40f0:8", ["const:90f69c:8", "const:4:8"]]
- 0090f69c ["CALL", null, ["callee:00c57ab0:8"]]
+ 009445a8 ["INT_ADD", "register:40f0:8", ["const:9445a8:8", "const:4:8"]]
+ 009445a8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090f69c bytes 712e0b94
+ 009445a8 bytes 424d0c94
- 0090f6ac ["INT_ADD", "register:40f0:8", ["const:90f6ac:8", "const:4:8"]]
- 0090f6ac ["CALL", null, ["callee:00c57ab0:8"]]
+ 009445b8 ["INT_ADD", "register:40f0:8", ["const:9445b8:8", "const:4:8"]]
+ 009445b8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090f6ac bytes 6d2e0b94
+ 009445b8 bytes 3e4d0c94
- 0090f6bc ["INT_ADD", "register:40f0:8", ["const:90f6bc:8", "const:4:8"]]
- 0090f6bc ["CALL", null, ["callee:00c57ab0:8"]]
+ 009445c8 ["INT_ADD", "register:40f0:8", ["const:9445c8:8", "const:4:8"]]
+ 009445c8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0090f6bc bytes 692e0b94
+ 009445c8 bytes 3a4d0c94
~~~


<a id="compare-e6392658af005105dfcfbaa3cfeab333"></a>

### [`0094c7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094c/0094c7b8.md) → [`00982264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982264.md) FUN_00982264

採用 · 移動量 `+0x35aac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0094c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094c/0094c7b8.md#insn-0094c7f0)
- 新版 [`0098229c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982264.md#insn-0098229c)

~~~diff
- 0094c7f0 ["INT_ADD", "register:40f0:8", ["const:94c7f0:8", "const:4:8"]]
- 0094c7f0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0098229c ["INT_ADD", "register:40f0:8", ["const:98229c:8", "const:4:8"]]
+ 0098229c ["CALL", null, ["callee:00c57ab0:8"]]
- 0094c7f0 bytes 1c3a0a94
+ 0098229c bytes 05560b94
~~~


<a id="compare-96f72f331a4b73224826d9ff862e8627"></a>

### [`0094cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094c/0094cba0.md) → [`0098264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098264c.md) FUN_0098264c

採用 · 移動量 `+0x35aac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`008384a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008384a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0094cbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094c/0094cba0.md#insn-0094cbb8)
- 新版 [`00982664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098264c.md#insn-00982664)

~~~diff
- 0094cbb8 ["INT_ADD", "register:40f0:8", ["const:94cbb8:8", "const:4:8"]]
- 0094cbb8 ["CALL", null, ["callee:0086a420:8"]]
+ 00982664 ["INT_ADD", "register:40f0:8", ["const:982664:8", "const:4:8"]]
+ 00982664 ["CALL", null, ["callee:0086a420:8"]]
- 0094cbb8 bytes 3caefb97
+ 00982664 bytes 6f9ffb97
~~~


<a id="compare-54d93e5c68f414886a5d8974d55a3d75"></a>

### [`00956ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00956/00956ce8.md) → [`0098c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c7b8.md) FUN_0098c7b8

採用 · 移動量 `+0x35ad0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 1件 [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md)
- 新版 呼出元 2件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 1件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00956d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00956/00956ce8.md#insn-00956d0c)
- 新版 [`0098c7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c7b8.md#insn-0098c7dc)

~~~diff
- 00956d0c ["INT_ADD", "register:40f0:8", ["const:956d0c:8", "const:4:8"]]
- 00956d0c ["CALL", null, ["callee:00676a20:8"]]
+ 0098c7dc ["INT_ADD", "register:40f0:8", ["const:98c7dc:8", "const:4:8"]]
+ 0098c7dc ["CALL", null, ["callee:00676a20:8"]]
- 00956d0c bytes 8de6f397
+ 0098c7dc bytes 91a8f397
~~~


<a id="compare-7992a752fbc2a63c1e2769ec67054300"></a>

### [`009711ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/009711ac.md) → [`009a6c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6c90.md) FUN_009a6c90

採用 · 移動量 `+0x35ae4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009711c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/009711ac.md#insn-009711c8) · [`009711e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/009711ac.md#insn-009711e8)
- 新版 [`009a6cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6c90.md#insn-009a6cac) · [`009a6ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6c90.md#insn-009a6ccc)

~~~diff
- 009711c8 ["INT_ADD", "register:40f0:8", ["const:9711c8:8", "const:4:8"]]
- 009711c8 ["CALL", null, ["callee:00c538e0:8"]]
+ 009a6cac ["INT_ADD", "register:40f0:8", ["const:9a6cac:8", "const:4:8"]]
+ 009a6cac ["CALL", null, ["callee:00c538e0:8"]]
- 009711c8 bytes 32970994
+ 009a6cac bytes 0db30a94
- 009711e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009711e8 ["INT_ADD", "register:40f0:8", ["const:9711e8:8", "const:4:8"]]
- 009711e8 ["CALLIND", null, ["register:0:8"]]
+ 009a6ccc ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a6ccc ["INT_ADD", "register:40f0:8", ["const:9a6ccc:8", "const:4:8"]]
+ 009a6ccc ["CALLIND", null, ["register:0:8"]]
- 009711e8 bytes 00013fd6
+ 009a6ccc bytes 00013fd6
~~~


<a id="compare-e42dfe49efddcdbd1d829e750c13fb1a"></a>

### [`00976da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976da4.md) → [`009ac888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac888.md) FUN_009ac888

採用 · 移動量 `+0x35ae4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979d0c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`009af7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af7ec.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00976dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976da4.md#insn-00976dc0) · [`00976de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976da4.md#insn-00976de0)
- 新版 [`009ac8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac888.md#insn-009ac8a4) · [`009ac8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac888.md#insn-009ac8c4)

~~~diff
- 00976dc0 ["INT_ADD", "register:40f0:8", ["const:976dc0:8", "const:4:8"]]
- 00976dc0 ["CALL", null, ["callee:00c538e0:8"]]
+ 009ac8a4 ["INT_ADD", "register:40f0:8", ["const:9ac8a4:8", "const:4:8"]]
+ 009ac8a4 ["CALL", null, ["callee:00c538e0:8"]]
- 00976dc0 bytes 34800994
+ 009ac8a4 bytes 0f9c0a94
- 00976de0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00976de0 ["INT_ADD", "register:40f0:8", ["const:976de0:8", "const:4:8"]]
- 00976de0 ["CALLIND", null, ["register:0:8"]]
+ 009ac8c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ac8c4 ["INT_ADD", "register:40f0:8", ["const:9ac8c4:8", "const:4:8"]]
+ 009ac8c4 ["CALLIND", null, ["register:0:8"]]
- 00976de0 bytes 00013fd6
+ 009ac8c4 bytes 00013fd6
~~~


<a id="compare-06c01562e7b3f4f8ee731c79405bf9fa"></a>

### [`0097727c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/0097727c.md) → [`009acd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009acd5c.md) FUN_009acd5c

採用 · 移動量 `+0x35ae0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009772b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/0097727c.md#insn-009772b4) · [`009772c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/0097727c.md#insn-009772c8) · [`009772d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/0097727c.md#insn-009772d0)
- 新版 [`009acd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009acd5c.md#insn-009acd94) · [`009acda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009acd5c.md#insn-009acda8) · [`009acdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009acd5c.md#insn-009acdb0)

~~~diff
- 009772b4 ["INT_ADD", "register:40f0:8", ["const:9772b4:8", "const:4:8"]]
- 009772b4 ["CALL", null, ["callee:00c538e0:8"]]
+ 009acd94 ["INT_ADD", "register:40f0:8", ["const:9acd94:8", "const:4:8"]]
+ 009acd94 ["CALL", null, ["callee:00c538e0:8"]]
- 009772b4 bytes f77e0994
+ 009acd94 bytes d39a0a94
- 009772c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009772c8 ["INT_ADD", "register:40f0:8", ["const:9772c8:8", "const:4:8"]]
- 009772c8 ["CALLIND", null, ["register:0:8"]]
+ 009acda8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009acda8 ["INT_ADD", "register:40f0:8", ["const:9acda8:8", "const:4:8"]]
+ 009acda8 ["CALLIND", null, ["register:0:8"]]
- 009772c8 bytes 00013fd6
+ 009acda8 bytes 00013fd6
- 009772d0 ["INT_ADD", "register:40f0:8", ["const:9772d0:8", "const:4:8"]]
- 009772d0 ["CALL", null, ["callee:00c57a80:8"]]
+ 009acdb0 ["INT_ADD", "register:40f0:8", ["const:9acdb0:8", "const:4:8"]]
+ 009acdb0 ["CALL", null, ["callee:00c57a80:8"]]
- 009772d0 bytes 588f0994
+ 009acdb0 bytes 34ab0a94
~~~


<a id="compare-4a1e3f95d6b9d5b07bb850b3beb27c5e"></a>

### [`00978140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978140.md) → [`009adc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adc20.md) FUN_009adc20

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005edb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ed/005edb40.md) · 呼出先 6件 [`00980018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md) [`00980058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980058.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · 呼出先 6件 [`009b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5af8.md) [`009b5b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b38.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00978190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978140.md#insn-00978190) · [`00978198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978140.md#insn-00978198) · [`009781ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978140.md#insn-009781ac)
- 新版 [`009adc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adc20.md#insn-009adc70) · [`009adc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adc20.md#insn-009adc78) · [`009adc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adc20.md#insn-009adc8c)

~~~diff
- 00978190 ["INT_ADD", "register:40f0:8", ["const:978190:8", "const:4:8"]]
- 00978190 ["CALL", null, ["callee:00c538b0:8"]]
+ 009adc70 ["INT_ADD", "register:40f0:8", ["const:9adc70:8", "const:4:8"]]
+ 009adc70 ["CALL", null, ["callee:00c538b0:8"]]
- 00978190 bytes 347b0994
+ 009adc70 bytes 10970a94
- 00978198 ["INT_ADD", "register:40f0:8", ["const:978198:8", "const:4:8"]]
- 00978198 ["CALL", null, ["callee:009b5af8:8"]]
+ 009adc78 ["INT_ADD", "register:40f0:8", ["const:9adc78:8", "const:4:8"]]
+ 009adc78 ["CALL", null, ["callee:009b5af8:8"]]
- 00978198 bytes a01f0094
+ 009adc78 bytes a01f0094
- 009781ac ["INT_ADD", "register:40f0:8", ["const:9781ac:8", "const:4:8"]]
- 009781ac ["CALL", null, ["callee:00c538e0:8"]]
+ 009adc8c ["INT_ADD", "register:40f0:8", ["const:9adc8c:8", "const:4:8"]]
+ 009adc8c ["CALL", null, ["callee:00c538e0:8"]]
- 009781ac bytes 397b0994
+ 009adc8c bytes 15970a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb7ebd15c965ae95fa792632fbc1d3f"></a>

### [`0097cfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cfcc.md) → [`009b2aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2aac.md) FUN_009b2aac

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979d0c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009af7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af7ec.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0097d00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cfcc.md#insn-0097d00c) · [`0097d038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cfcc.md#insn-0097d038)
- 新版 [`009b2aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2aac.md#insn-009b2aec) · [`009b2b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2aac.md#insn-009b2b18)

~~~diff
- 0097d00c ["COPY", "register:0:8", ["register:4040:8"]]
- 0097d00c ["INT_ADD", "register:40f0:8", ["const:97d00c:8", "const:4:8"]]
- 0097d00c ["CALLIND", null, ["register:0:8"]]
+ 009b2aec ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b2aec ["INT_ADD", "register:40f0:8", ["const:9b2aec:8", "const:4:8"]]
+ 009b2aec ["CALLIND", null, ["register:0:8"]]
- 0097d00c bytes 00013fd6
+ 009b2aec bytes 00013fd6
- 0097d038 ["COPY", "register:0:8", ["register:4040:8"]]
- 0097d038 ["INT_ADD", "register:40f0:8", ["const:97d038:8", "const:4:8"]]
- 0097d038 ["CALLIND", null, ["register:0:8"]]
+ 009b2b18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b2b18 ["INT_ADD", "register:40f0:8", ["const:9b2b18:8", "const:4:8"]]
+ 009b2b18 ["CALLIND", null, ["register:0:8"]]
- 0097d038 bytes 00013fd6
+ 009b2b18 bytes 00013fd6
~~~


<a id="compare-31c9cc0d24f75c9a3f206fd8b67bc8c1"></a>

### [`0098132c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098132c.md) → [`009b6e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e0c.md) FUN_009b6e0c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0097f1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f1b0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009b4c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00981368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098132c.md#insn-00981368)
- 新版 [`009b6e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e0c.md#insn-009b6e48)

~~~diff
- 00981368 ["COPY", "register:0:8", ["register:4040:8"]]
- 00981368 ["INT_ADD", "register:40f0:8", ["const:981368:8", "const:4:8"]]
- 00981368 ["CALLIND", null, ["register:0:8"]]
+ 009b6e48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b6e48 ["INT_ADD", "register:40f0:8", ["const:9b6e48:8", "const:4:8"]]
+ 009b6e48 ["CALLIND", null, ["register:0:8"]]
- 00981368 bytes 00013fd6
+ 009b6e48 bytes 00013fd6
~~~


<a id="compare-194bb3193f19ca33db8688e4bb74e230"></a>

### [`009827c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009827c4.md) → [`009b82a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82a4.md) FUN_009b82a4

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009827e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009827c4.md#insn-009827e0)
- 新版 [`009b82c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82a4.md#insn-009b82c0)

~~~diff
- 009827e0 ["INT_ADD", "register:40f0:8", ["const:9827e0:8", "const:4:8"]]
- 009827e0 ["CALL", null, ["callee:00459d34:8"]]
+ 009b82c0 ["INT_ADD", "register:40f0:8", ["const:9b82c0:8", "const:4:8"]]
+ 009b82c0 ["CALL", null, ["callee:00459d34:8"]]
- 009827e0 bytes afd1ea97
+ 009b82c0 bytes 9d86ea97
~~~


<a id="compare-32a22f49208e136ff7186de92eeab361"></a>

### [`00982bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982bf0.md) → [`009b86d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md) FUN_009b86d0

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00816954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816954.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 3件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084874c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084874c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00982c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982bf0.md#insn-00982c14) · [`00982c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982bf0.md#insn-00982c28) · [`00982c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982bf0.md#insn-00982c48)
- 新版 [`009b86f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md#insn-009b86f4) · [`009b8708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md#insn-009b8708) · [`009b8728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md#insn-009b8728)

~~~diff
- 00982c14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00982c14 ["INT_ADD", "register:40f0:8", ["const:982c14:8", "const:4:8"]]
- 00982c14 ["CALLIND", null, ["register:0:8"]]
+ 009b86f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b86f4 ["INT_ADD", "register:40f0:8", ["const:9b86f4:8", "const:4:8"]]
+ 009b86f4 ["CALLIND", null, ["register:0:8"]]
- 00982c14 bytes 00013fd6
+ 009b86f4 bytes 00013fd6
- 00982c28 ["INT_ADD", "register:40f0:8", ["const:982c28:8", "const:4:8"]]
- 00982c28 ["CALL", null, ["callee:00c538e0:8"]]
+ 009b8708 ["INT_ADD", "register:40f0:8", ["const:9b8708:8", "const:4:8"]]
+ 009b8708 ["CALL", null, ["callee:00c538e0:8"]]
- 00982c28 bytes 9a500994
+ 009b8708 bytes 766c0a94
- 00982c48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00982c48 ["INT_ADD", "register:40f0:8", ["const:982c48:8", "const:4:8"]]
- 00982c48 ["CALLIND", null, ["register:0:8"]]
+ 009b8728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b8728 ["INT_ADD", "register:40f0:8", ["const:9b8728:8", "const:4:8"]]
+ 009b8728 ["CALLIND", null, ["register:0:8"]]
- 00982c48 bytes 00013fd6
+ 009b8728 bytes 00013fd6
~~~


<a id="compare-b4163ba3af31fcf75c3353775194a397"></a>

### [`00983810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983810.md) → [`009b92f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md) FUN_009b92f0

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00984700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984700.md) · 呼出先 4件 [`00901264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901264.md) [`00977d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977d04.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`009ba1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba1e0.md) · 呼出先 4件 [`00935c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935c98.md) [`009ad7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad7e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00983840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983810.md#insn-00983840) · [`00983898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983810.md#insn-00983898) · [`009838a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983810.md#insn-009838a8)
- 新版 [`009b9320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md#insn-009b9320) · [`009b9378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md#insn-009b9378) · [`009b9388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md#insn-009b9388)

~~~diff
- 00983840 ["INT_ADD", "register:40f0:8", ["const:983840:8", "const:4:8"]]
- 00983840 ["CALL", null, ["callee:009ad7e4:8"]]
+ 009b9320 ["INT_ADD", "register:40f0:8", ["const:9b9320:8", "const:4:8"]]
+ 009b9320 ["CALL", null, ["callee:009ad7e4:8"]]
- 00983840 bytes 31d1ff97
+ 009b9320 bytes 31d1ff97
- 00983898 ["INT_ADD", "register:40f0:8", ["const:983898:8", "const:4:8"]]
- 00983898 ["CALL", null, ["callee:00935c98:8"]]
+ 009b9378 ["INT_ADD", "register:40f0:8", ["const:9b9378:8", "const:4:8"]]
+ 009b9378 ["CALL", null, ["callee:00935c98:8"]]
- 00983898 bytes 73f6fd97
+ 009b9378 bytes 48f2fd97
- 009838a8 ["INT_ADD", "register:40f0:8", ["const:9838a8:8", "const:4:8"]]
- 009838a8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 009b9388 ["INT_ADD", "register:40f0:8", ["const:9b9388:8", "const:4:8"]]
+ 009b9388 ["CALL", null, ["callee:00c57ab0:8"]]
- 009838a8 bytes ee5d0994
+ 009b9388 bytes ca790a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54a83a1747007e351f5791c8758bfb51"></a>

### [`00983a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983a68.md) → [`009b9548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9548.md) FUN_009b9548

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 2件 [`00977eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977eec.md) [`00a6dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md)
- 新版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`009ad9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9cc.md) [`00acbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00983a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983a68.md#insn-00983a8c) · [`00983aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983a68.md#insn-00983aa0)
- 新版 [`009b956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9548.md#insn-009b956c) · [`009b9580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9548.md#insn-009b9580)

~~~diff
- 00983a8c ["INT_ADD", "register:40f0:8", ["const:983a8c:8", "const:4:8"]]
- 00983a8c ["CALL", null, ["callee:009ad9cc:8"]]
+ 009b956c ["INT_ADD", "register:40f0:8", ["const:9b956c:8", "const:4:8"]]
+ 009b956c ["CALL", null, ["callee:009ad9cc:8"]]
- 00983a8c bytes 18d1ff97
+ 009b956c bytes 18d1ff97
- 00983aa0 ["INT_ADD", "register:40f0:8", ["const:983aa0:8", "const:4:8"]]
- 00983aa0 ["CALL", null, ["callee:00acbd30:8"]]
+ 009b9580 ["INT_ADD", "register:40f0:8", ["const:9b9580:8", "const:4:8"]]
+ 009b9580 ["CALL", null, ["callee:00acbd30:8"]]
- 00983aa0 bytes bfa80394
+ 009b9580 bytes ec490494
~~~


<a id="compare-ed80f3efff2160002ad889aa3d7e190c"></a>

### [`009843c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/009843c0.md) → [`009b9ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9ea0.md) FUN_009b9ea0

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`00977eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977eec.md)
- 新版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`009ad9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009843d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/009843c0.md#insn-009843d4)
- 新版 [`009b9eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9ea0.md#insn-009b9eb4)

~~~diff
- 009843d4 ["INT_ADD", "register:40f0:8", ["const:9843d4:8", "const:4:8"]]
- 009843d4 ["CALL", null, ["callee:009ad9cc:8"]]
+ 009b9eb4 ["INT_ADD", "register:40f0:8", ["const:9b9eb4:8", "const:4:8"]]
+ 009b9eb4 ["CALL", null, ["callee:009ad9cc:8"]]
- 009843d4 bytes c6ceff97
+ 009b9eb4 bytes c6ceff97
~~~


<a id="compare-50e288bea7886c1a2074cae77149c96c"></a>

### [`0098b354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b354.md) → [`009c0e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0e48.md) FUN_009c0e48

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00837810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869788.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0098b378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b354.md#insn-0098b378)
- 新版 [`009c0e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0e48.md#insn-009c0e6c)

~~~diff
- 0098b378 ["INT_ADD", "register:40f0:8", ["const:98b378:8", "const:4:8"]]
- 0098b378 ["CALL", null, ["callee:00869788:8"]]
+ 009c0e6c ["INT_ADD", "register:40f0:8", ["const:9c0e6c:8", "const:4:8"]]
+ 009c0e6c ["CALL", null, ["callee:00869788:8"]]
- 0098b378 bytes 26b1fa97
+ 009c0e6c bytes 47a2fa97
~~~


<a id="compare-5ac8d44ff0852ab3a5905a8c873e88e2"></a>

### [`0098ca8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098ca8c.md) → [`009c2580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c2/009c2580.md) FUN_009c2580

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0098c998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098c998.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009c248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c2/009c248c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0098ca9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098ca8c.md#insn-0098ca9c)
- 新版 [`009c2590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c2/009c2580.md#insn-009c2590)

~~~diff
- 0098ca9c ["INT_ADD", "register:40f0:8", ["const:98ca9c:8", "const:4:8"]]
- 0098ca9c ["CALL", null, ["callee:009c248c:8"]]
+ 009c2590 ["INT_ADD", "register:40f0:8", ["const:9c2590:8", "const:4:8"]]
+ 009c2590 ["CALL", null, ["callee:009c248c:8"]]
- 0098ca9c bytes bfffff97
+ 009c2590 bytes bfffff97
~~~


<a id="compare-af55cc15d777ea80f448dcd2551924d8"></a>

### [`00992e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00992/00992e4c.md) → [`009c8940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md) FUN_009c8940

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0098dd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098d/0098dd80.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009c3874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c3874.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00992efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00992/00992e4c.md#insn-00992efc) · [`00992f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00992/00992e4c.md#insn-00992f0c) · [`00992f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00992/00992e4c.md#insn-00992f14)
- 新版 [`009c89f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md#insn-009c89f0) · [`009c8a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md#insn-009c8a00) · [`009c8a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c8940.md#insn-009c8a08)

~~~diff
- 00992efc ["INT_ADD", "register:40f0:8", ["const:992efc:8", "const:4:8"]]
- 00992efc ["CALL", null, ["callee:004945d0:8"]]
+ 009c89f0 ["INT_ADD", "register:40f0:8", ["const:9c89f0:8", "const:4:8"]]
+ 009c89f0 ["CALL", null, ["callee:004945d0:8"]]
- 00992efc bytes 0f7aeb97
+ 009c89f0 bytes f82eeb97
- 00992f0c ["INT_ADD", "register:40f0:8", ["const:992f0c:8", "const:4:8"]]
- 00992f0c ["CALL", null, ["callee:00c57ab0:8"]]
+ 009c8a00 ["INT_ADD", "register:40f0:8", ["const:9c8a00:8", "const:4:8"]]
+ 009c8a00 ["CALL", null, ["callee:00c57ab0:8"]]
- 00992f0c bytes 55200994
+ 009c8a00 bytes 2c3c0a94
- 00992f14 ["INT_ADD", "register:40f0:8", ["const:992f14:8", "const:4:8"]]
- 00992f14 ["CALL", null, ["callee:00c57ab0:8"]]
+ 009c8a08 ["INT_ADD", "register:40f0:8", ["const:9c8a08:8", "const:4:8"]]
+ 009c8a08 ["CALL", null, ["callee:00c57ab0:8"]]
- 00992f14 bytes 53200994
+ 009c8a08 bytes 2a3c0a94
~~~


<a id="compare-657d11fd1d64a4a04bf5bc4eb0204c68"></a>

### [`009a1b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1b84.md) → [`009d7890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md) FUN_009d7890

採用 · 移動量 `+0x35d0c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0099fe4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099f/0099fe4c.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`009a71f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a71f4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`009dcf54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcf54.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a1c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1b84.md#insn-009a1c4c) · [`009a1c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1b84.md#insn-009a1c98) · [`009a1cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1b84.md#insn-009a1cac)
- 新版 [`009d7958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md#insn-009d7958) · [`009d79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md#insn-009d79a4) · [`009d79b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md#insn-009d79b8)

~~~diff
- 009a1c4c ["INT_ADD", "register:40f0:8", ["const:9a1c4c:8", "const:4:8"]]
- 009a1c4c ["CALL", null, ["callee:00c57a90:8"]]
+ 009d7958 ["INT_ADD", "register:40f0:8", ["const:9d7958:8", "const:4:8"]]
+ 009d7958 ["CALL", null, ["callee:00c57a90:8"]]
- 009a1c4c bytes fde40894
+ 009d7958 bytes 4e000a94
- 009a1c98 ["INT_ADD", "register:40f0:8", ["const:9a1c98:8", "const:4:8"]]
- 009a1c98 ["CALL", null, ["callee:00c57c00:8"]]
+ 009d79a4 ["INT_ADD", "register:40f0:8", ["const:9d79a4:8", "const:4:8"]]
+ 009d79a4 ["CALL", null, ["callee:00c57c00:8"]]
- 009a1c98 bytes 46e50894
+ 009d79a4 bytes 97000a94
- 009a1cac ["INT_ADD", "register:40f0:8", ["const:9a1cac:8", "const:4:8"]]
- 009a1cac ["CALL", null, ["callee:00c57ab0:8"]]
+ 009d79b8 ["INT_ADD", "register:40f0:8", ["const:9d79b8:8", "const:4:8"]]
+ 009d79b8 ["CALL", null, ["callee:00c57ab0:8"]]
- 009a1cac bytes ede40894
+ 009d79b8 bytes 3e000a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9037450a24bedaeb2c2f4ba4ea5984f"></a>

### [`009a60b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a60b4.md) → [`009dbe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbe14.md) FUN_009dbe14

採用 · 移動量 `+0x35d60` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 2件 [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a6104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a60b4.md#insn-009a6104)
- 新版 [`009dbe64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbe14.md#insn-009dbe64)

~~~diff
- 009a6104 ["INT_ADD", "register:40f0:8", ["const:9a6104:8", "const:4:8"]]
- 009a6104 ["CALL", null, ["callee:00470074:8"]]
+ 009dbe64 ["INT_ADD", "register:40f0:8", ["const:9dbe64:8", "const:4:8"]]
+ 009dbe64 ["CALL", null, ["callee:00470074:8"]]
- 009a6104 bytes 369cea97
+ 009dbe64 bytes 8450ea97
~~~


<a id="compare-ed3ec5b05e9f279865cd8f8d58021df1"></a>

### [`009a8908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8908.md) → [`009de668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md) FUN_009de668

採用 · 移動量 `+0x35d60` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d0/009d0f70.md) · 呼出先 2件 [`0045d300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d300.md) [`0045d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md)
- 新版 呼出元 1件 [`00a2de6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2d/00a2de6c.md) · 呼出先 2件 [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a8920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8908.md#insn-009a8920) · [`009a892c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8908.md#insn-009a892c) · [`009a8938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8908.md#insn-009a8938)
- 新版 [`009de680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md#insn-009de680) · [`009de68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md#insn-009de68c) · [`009de698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de668.md#insn-009de698)

~~~diff
- 009a8920 ["INT_ADD", "register:40f0:8", ["const:9a8920:8", "const:4:8"]]
- 009a8920 ["CALL", null, ["callee:00480198:8"]]
+ 009de680 ["INT_ADD", "register:40f0:8", ["const:9de680:8", "const:4:8"]]
+ 009de680 ["CALL", null, ["callee:00480198:8"]]
- 009a8920 bytes 78d2ea97
+ 009de680 bytes c686ea97
- 009a892c ["INT_ADD", "register:40f0:8", ["const:9a892c:8", "const:4:8"]]
- 009a892c ["CALL", null, ["callee:00480198:8"]]
+ 009de68c ["INT_ADD", "register:40f0:8", ["const:9de68c:8", "const:4:8"]]
+ 009de68c ["CALL", null, ["callee:00480198:8"]]
- 009a892c bytes 75d2ea97
+ 009de68c bytes c386ea97
- 009a8938 ["INT_ADD", "register:40f0:8", ["const:9a8938:8", "const:4:8"]]
- 009a8938 ["CALL", null, ["callee:004802b8:8"]]
+ 009de698 ["INT_ADD", "register:40f0:8", ["const:9de698:8", "const:4:8"]]
+ 009de698 ["CALL", null, ["callee:004802b8:8"]]
- 009a8938 bytes bad2ea97
+ 009de698 bytes 0887ea97
~~~


<a id="compare-18dd26c50425fdb9e97506de26cf99f5"></a>

### [`009a8950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8950.md) → [`009de6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de6b0.md) FUN_009de6b0

採用 · 移動量 `+0x35d60` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d1474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d1/009d1474.md) · 呼出先 2件 [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md) [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md)
- 新版 呼出元 1件 [`00a2e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e370.md) · 呼出先 2件 [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a8970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8950.md#insn-009a8970) · [`009a897c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8950.md#insn-009a897c)
- 新版 [`009de6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de6b0.md#insn-009de6d0) · [`009de6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de6b0.md#insn-009de6dc)

~~~diff
- 009a8970 ["INT_ADD", "register:40f0:8", ["const:9a8970:8", "const:4:8"]]
- 009a8970 ["CALL", null, ["callee:00480ba8:8"]]
+ 009de6d0 ["INT_ADD", "register:40f0:8", ["const:9de6d0:8", "const:4:8"]]
+ 009de6d0 ["CALL", null, ["callee:00480ba8:8"]]
- 009a8970 bytes e8d4ea97
+ 009de6d0 bytes 3689ea97
- 009a897c ["INT_ADD", "register:40f0:8", ["const:9a897c:8", "const:4:8"]]
- 009a897c ["CALL", null, ["callee:00480ba8:8"]]
+ 009de6dc ["INT_ADD", "register:40f0:8", ["const:9de6dc:8", "const:4:8"]]
+ 009de6dc ["CALL", null, ["callee:00480ba8:8"]]
- 009a897c bytes e5d4ea97
+ 009de6dc bytes 3389ea97
~~~


<a id="compare-c629cc7f7c5a1218ca022ed0a14a44d7"></a>

### [`009d4e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d4/009d4e60.md) → [`00a31d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31d5c.md) FUN_00a31d5c

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`009d4bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d4/009d4bbc.md)
- 新版 呼出元 3件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`00a31ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ab8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d4e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d4/009d4e60.md#insn-009d4e70)
- 新版 [`00a31d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31d5c.md#insn-00a31d6c)

~~~diff
- 009d4e70 ["INT_ADD", "register:40f0:8", ["const:9d4e70:8", "const:4:8"]]
- 009d4e70 ["CALL", null, ["callee:00a31ab8:8"]]
+ 00a31d6c ["INT_ADD", "register:40f0:8", ["const:a31d6c:8", "const:4:8"]]
+ 00a31d6c ["CALL", null, ["callee:00a31ab8:8"]]
- 009d4e70 bytes 53ffff97
+ 00a31d6c bytes 53ffff97
~~~


<a id="compare-94fcc0a0882bbe3352a204b0046ee7ae"></a>

### [`009d4ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d4/009d4ea4.md) → [`00a31da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31da0.md) FUN_00a31da0

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d4eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d4/009d4ea4.md#insn-009d4eb8)
- 新版 [`00a31db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31da0.md#insn-00a31db4)

~~~diff
- 009d4eb8 ["INT_ADD", "register:40f0:8", ["const:9d4eb8:8", "const:4:8"]]
- 009d4eb8 ["CALL", null, ["callee:004802b8:8"]]
+ 00a31db4 ["INT_ADD", "register:40f0:8", ["const:a31db4:8", "const:4:8"]]
+ 00a31db4 ["CALL", null, ["callee:004802b8:8"]]
- 009d4eb8 bytes 5a21ea97
+ 00a31db4 bytes 4139e997
~~~


<a id="compare-40f900c38eb739976cdfcd850ba966c3"></a>

### [`009d5270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5270.md) → [`00a3216c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a3216c.md) FUN_00a3216c

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 1件 [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d528c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5270.md#insn-009d528c)
- 新版 [`00a32188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a3216c.md#insn-00a32188)

~~~diff
- 009d528c ["INT_ADD", "register:40f0:8", ["const:9d528c:8", "const:4:8"]]
- 009d528c ["CALL", null, ["callee:005c3e3c:8"]]
+ 00a32188 ["INT_ADD", "register:40f0:8", ["const:a32188:8", "const:4:8"]]
+ 00a32188 ["CALL", null, ["callee:005c3e3c:8"]]
- 009d528c bytes 6029ef97
+ 00a32188 bytes 2d47ee97
~~~


<a id="compare-95b0cc31d3542c2acc842572e2997285"></a>

### [`009d5384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5384.md) → [`00a32280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32280.md) FUN_00a32280

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) · 呼出先 2件 [`006ef68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006ef68c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 2件 [`007196f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5384.md#insn-009d53dc) · [`009d5408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5384.md#insn-009d5408)
- 新版 [`00a322d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32280.md#insn-00a322d8) · [`00a32304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32280.md#insn-00a32304)

~~~diff
- 009d53dc ["INT_ADD", "register:40f0:8", ["const:9d53dc:8", "const:4:8"]]
- 009d53dc ["CALL", null, ["callee:007196f8:8"]]
+ 00a322d8 ["INT_ADD", "register:40f0:8", ["const:a322d8:8", "const:4:8"]]
+ 00a322d8 ["CALL", null, ["callee:007196f8:8"]]
- 009d53dc bytes ac68f497
+ 00a322d8 bytes 089df397
- 009d5408 ["INT_ADD", "register:40f0:8", ["const:9d5408:8", "const:4:8"]]
- 009d5408 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00a32304 ["INT_ADD", "register:40f0:8", ["const:a32304:8", "const:4:8"]]
+ 00a32304 ["CALL", null, ["callee:00c57ae0:8"]]
- 009d5408 bytes 22170894
+ 00a32304 bytes f7950894
~~~


<a id="compare-a88c08ba1ccbc35ce58b9bdaeaea9399"></a>

### [`009d6538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6538.md) → [`00a33434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md) FUN_00a33434

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 9件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md) [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md) [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 9件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009d6578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6538.md#insn-009d6578) · [`009d6584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6538.md#insn-009d6584) · [`009d6590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6538.md#insn-009d6590)
- 新版 [`00a33474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md#insn-00a33474) · [`00a33480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md#insn-00a33480) · [`00a3348c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md#insn-00a3348c)

~~~diff
- 009d6578 ["INT_ADD", "register:40f0:8", ["const:9d6578:8", "const:4:8"]]
- 009d6578 ["CALL", null, ["callee:00480ba8:8"]]
+ 00a33474 ["INT_ADD", "register:40f0:8", ["const:a33474:8", "const:4:8"]]
+ 00a33474 ["CALL", null, ["callee:00480ba8:8"]]
- 009d6578 bytes e61dea97
+ 00a33474 bytes cd35e997
- 009d6584 ["INT_ADD", "register:40f0:8", ["const:9d6584:8", "const:4:8"]]
- 009d6584 ["CALL", null, ["callee:00481058:8"]]
+ 00a33480 ["INT_ADD", "register:40f0:8", ["const:a33480:8", "const:4:8"]]
+ 00a33480 ["CALL", null, ["callee:00481058:8"]]
- 009d6584 bytes 0f1fea97
+ 00a33480 bytes f636e997
- 009d6590 ["INT_ADD", "register:40f0:8", ["const:9d6590:8", "const:4:8"]]
- 009d6590 ["CALL", null, ["callee:00480d08:8"]]
+ 00a3348c ["INT_ADD", "register:40f0:8", ["const:a3348c:8", "const:4:8"]]
+ 00a3348c ["CALL", null, ["callee:00480d08:8"]]
- 009d6590 bytes 381eea97
+ 00a3348c bytes 1f36e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-892cbd69f8ba083d0e865df057eeab24"></a>

### [`009dad10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009dad10.md) → [`00a37c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37c0c.md) FUN_00a37c0c

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0060b7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b7bc.md) [`007317b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007317b0.md) · 呼出先 4件 [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`009daa54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009daa54.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) · 呼出先 4件 [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) [`00a37950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37950.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009dad10.md#insn-009dad34) · [`009dad5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009dad10.md#insn-009dad5c) · [`009dad6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009dad10.md#insn-009dad6c)
- 新版 [`00a37c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37c0c.md#insn-00a37c30) · [`00a37c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37c0c.md#insn-00a37c58) · [`00a37c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37c0c.md#insn-00a37c68)

~~~diff
- 009dad34 ["INT_ADD", "register:40f0:8", ["const:9dad34:8", "const:4:8"]]
- 009dad34 ["CALL", null, ["callee:00a37950:8"]]
+ 00a37c30 ["INT_ADD", "register:40f0:8", ["const:a37c30:8", "const:4:8"]]
+ 00a37c30 ["CALL", null, ["callee:00a37950:8"]]
- 009dad34 bytes 48ffff97
+ 00a37c30 bytes 48ffff97
- 009dad5c ["INT_ADD", "register:40f0:8", ["const:9dad5c:8", "const:4:8"]]
- 009dad5c ["CALL", null, ["callee:005626b4:8"]]
+ 00a37c58 ["INT_ADD", "register:40f0:8", ["const:a37c58:8", "const:4:8"]]
+ 00a37c58 ["CALL", null, ["callee:005626b4:8"]]
- 009dad5c bytes b092ed97
+ 00a37c58 bytes 97aaec97
- 009dad6c ["INT_ADD", "register:40f0:8", ["const:9dad6c:8", "const:4:8"]]
- 009dad6c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a37c68 ["INT_ADD", "register:40f0:8", ["const:a37c68:8", "const:4:8"]]
+ 00a37c68 ["CALL", null, ["callee:00c57ab0:8"]]
- 009dad6c bytes bd000894
+ 00a37c68 bytes 927f0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d50261b95b2ace32b6d0b6c4d8226730"></a>

### [`009daf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009daf04.md) → [`00a37e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e00.md) FUN_00a37e00

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008371d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008371d0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009daf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009daf04.md#insn-009daf3c)
- 新版 [`00a37e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e00.md#insn-00a37e38)

~~~diff
- 009daf3c ["INT_ADD", "register:40f0:8", ["const:9daf3c:8", "const:4:8"]]
- 009daf3c ["CALL", null, ["callee:00869148:8"]]
+ 00a37e38 ["INT_ADD", "register:40f0:8", ["const:a37e38:8", "const:4:8"]]
+ 00a37e38 ["CALL", null, ["callee:00869148:8"]]
- 009daf3c bytes a570f997
+ 00a37e38 bytes c4c4f897
~~~


<a id="compare-760331fc8416498199831156ac42cc87"></a>

### [`009daf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009daf70.md) → [`00a37e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e6c.md) FUN_00a37e6c

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00837270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837270.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008691e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009daf70.md#insn-009dafa4)
- 新版 [`00a37ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e6c.md#insn-00a37ea0)

~~~diff
- 009dafa4 ["INT_ADD", "register:40f0:8", ["const:9dafa4:8", "const:4:8"]]
- 009dafa4 ["CALL", null, ["callee:008691e8:8"]]
+ 00a37ea0 ["INT_ADD", "register:40f0:8", ["const:a37ea0:8", "const:4:8"]]
+ 00a37ea0 ["CALL", null, ["callee:008691e8:8"]]
- 009dafa4 bytes b370f997
+ 00a37ea0 bytes d2c4f897
~~~


<a id="compare-f448e3b9c30bfe7b1092bb109dd9005b"></a>

### [`009dafd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009dafd8.md) → [`00a37ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37ed4.md) FUN_00a37ed4

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00837354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837354.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008692cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008692cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009daff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009dafd8.md#insn-009daff0)
- 新版 [`00a37eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37ed4.md#insn-00a37eec)

~~~diff
- 009daff0 ["INT_ADD", "register:40f0:8", ["const:9daff0:8", "const:4:8"]]
- 009daff0 ["CALL", null, ["callee:008692cc:8"]]
+ 00a37eec ["INT_ADD", "register:40f0:8", ["const:a37eec:8", "const:4:8"]]
+ 00a37eec ["CALL", null, ["callee:008692cc:8"]]
- 009daff0 bytes d970f997
+ 00a37eec bytes f8c4f897
~~~


<a id="compare-e5517d4bf396ba919cf9f3c17a76e9bd"></a>

### [`009dc55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc55c.md) → [`00a39458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39458.md) FUN_00a39458

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dc58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc55c.md#insn-009dc58c) · [`009dc598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc55c.md#insn-009dc598) · [`009dc5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc55c.md#insn-009dc5a4)
- 新版 [`00a39488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39458.md#insn-00a39488) · [`00a39494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39458.md#insn-00a39494) · [`00a394a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39458.md#insn-00a394a0)

~~~diff
- 009dc58c ["INT_ADD", "register:40f0:8", ["const:9dc58c:8", "const:4:8"]]
- 009dc58c ["CALL", null, ["callee:0046d450:8"]]
+ 00a39488 ["INT_ADD", "register:40f0:8", ["const:a39488:8", "const:4:8"]]
+ 00a39488 ["CALL", null, ["callee:0046d450:8"]]
- 009dc58c bytes 0bb8e997
+ 00a39488 bytes f2cfe897
- 009dc598 ["INT_ADD", "register:40f0:8", ["const:9dc598:8", "const:4:8"]]
- 009dc598 ["CALL", null, ["callee:0046d450:8"]]
+ 00a39494 ["INT_ADD", "register:40f0:8", ["const:a39494:8", "const:4:8"]]
+ 00a39494 ["CALL", null, ["callee:0046d450:8"]]
- 009dc598 bytes 08b8e997
+ 00a39494 bytes efcfe897
- 009dc5a4 ["INT_ADD", "register:40f0:8", ["const:9dc5a4:8", "const:4:8"]]
- 009dc5a4 ["CALL", null, ["callee:0046d450:8"]]
+ 00a394a0 ["INT_ADD", "register:40f0:8", ["const:a394a0:8", "const:4:8"]]
+ 00a394a0 ["CALL", null, ["callee:0046d450:8"]]
- 009dc5a4 bytes 05b8e997
+ 00a394a0 bytes eccfe897
~~~


<a id="compare-82e76fb79e9d27d5f4f9fb11142b0284"></a>

### [`009dd314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd314.md) → [`00a3a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3a/00a3a210.md) FUN_00a3a210

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008371d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008371d0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009dd33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd314.md#insn-009dd33c)
- 新版 [`00a3a238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3a/00a3a210.md#insn-00a3a238)

~~~diff
- 009dd33c ["INT_ADD", "register:40f0:8", ["const:9dd33c:8", "const:4:8"]]
- 009dd33c ["CALL", null, ["callee:00869148:8"]]
+ 00a3a238 ["INT_ADD", "register:40f0:8", ["const:a3a238:8", "const:4:8"]]
+ 00a3a238 ["CALL", null, ["callee:00869148:8"]]
- 009dd33c bytes a567f997
+ 00a3a238 bytes c4bbf897
~~~


<a id="compare-bcefe9a8e1cb46e2b6a1b5be419b9349"></a>

### [`009e1e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1e84.md) → [`00a3ed80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ed80.md) FUN_00a3ed80

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e1e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1e84.md#insn-009e1e9c)
- 新版 [`00a3ed98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ed80.md#insn-00a3ed98)

~~~diff
- 009e1e9c ["INT_ADD", "register:40f0:8", ["const:9e1e9c:8", "const:4:8"]]
- 009e1e9c ["CALL", null, ["callee:005c175c:8"]]
+ 00a3ed98 ["INT_ADD", "register:40f0:8", ["const:a3ed98:8", "const:4:8"]]
+ 00a3ed98 ["CALL", null, ["callee:005c175c:8"]]
- 009e1e9c bytes a4ecee97
+ 00a3ed98 bytes 710aee97
~~~


<a id="compare-9b9dfeebf58bf6d48587a061a81c146a"></a>

### [`009e1eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1eb4.md) → [`00a3edb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3edb0.md) FUN_00a3edb0

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e18dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e18dc.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00a3e7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e7d8.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1eb4.md#insn-009e1ecc) · [`009e1ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1eb4.md#insn-009e1ed8)
- 新版 [`00a3edc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3edb0.md#insn-00a3edc8) · [`00a3edd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3edb0.md#insn-00a3edd4)

~~~diff
- 009e1ecc ["INT_ADD", "register:40f0:8", ["const:9e1ecc:8", "const:4:8"]]
- 009e1ecc ["CALL", null, ["callee:005c175c:8"]]
+ 00a3edc8 ["INT_ADD", "register:40f0:8", ["const:a3edc8:8", "const:4:8"]]
+ 00a3edc8 ["CALL", null, ["callee:005c175c:8"]]
- 009e1ecc bytes 98ecee97
+ 00a3edc8 bytes 650aee97
- 009e1ed8 ["INT_ADD", "register:40f0:8", ["const:9e1ed8:8", "const:4:8"]]
- 009e1ed8 ["CALL", null, ["callee:005c175c:8"]]
+ 00a3edd4 ["INT_ADD", "register:40f0:8", ["const:a3edd4:8", "const:4:8"]]
+ 00a3edd4 ["CALL", null, ["callee:005c175c:8"]]
- 009e1ed8 bytes 95ecee97
+ 00a3edd4 bytes 620aee97
~~~


<a id="compare-86af0ef9a9cd3a1445635f3788538786"></a>

### [`009e3b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3b98.md) → [`00a40a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40a94.md) FUN_00a40a94

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009e3aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3aa0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a4099c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a4099c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e3ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3b98.md#insn-009e3ba8)
- 新版 [`00a40aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40a94.md#insn-00a40aa4)

~~~diff
- 009e3ba8 ["INT_ADD", "register:40f0:8", ["const:9e3ba8:8", "const:4:8"]]
- 009e3ba8 ["CALL", null, ["callee:00a4099c:8"]]
+ 00a40aa4 ["INT_ADD", "register:40f0:8", ["const:a40aa4:8", "const:4:8"]]
+ 00a40aa4 ["CALL", null, ["callee:00a4099c:8"]]
- 009e3ba8 bytes beffff97
+ 00a40aa4 bytes beffff97
~~~


<a id="compare-5985e02644fc6e7e4d42c9a7ccb993f9"></a>

### [`009e4290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4290.md) → [`00a4118c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a4118c.md) FUN_00a4118c

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009e44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e44b8.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a413b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a413b4.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e42ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4290.md#insn-009e42ec) · [`009e42fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4290.md#insn-009e42fc) · [`009e4318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4290.md#insn-009e4318)
- 新版 [`00a411e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a4118c.md#insn-00a411e8) · [`00a411f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a4118c.md#insn-00a411f8) · [`00a41214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a4118c.md#insn-00a41214)

~~~diff
- 009e42ec ["INT_ADD", "register:40f0:8", ["const:9e42ec:8", "const:4:8"]]
- 009e42ec ["CALL", null, ["callee:00487a24:8"]]
+ 00a411e8 ["INT_ADD", "register:40f0:8", ["const:a411e8:8", "const:4:8"]]
+ 00a411e8 ["CALL", null, ["callee:00487a24:8"]]
- 009e42ec bytes 2802ea97
+ 00a411e8 bytes 0f1ae997
- 009e42fc ["INT_ADD", "register:40f0:8", ["const:9e42fc:8", "const:4:8"]]
- 009e42fc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a411f8 ["INT_ADD", "register:40f0:8", ["const:a411f8:8", "const:4:8"]]
+ 00a411f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 009e42fc bytes 59db0794
+ 00a411f8 bytes 2e5a0894
- 009e4318 ["INT_ADD", "register:40f0:8", ["const:9e4318:8", "const:4:8"]]
- 009e4318 ["CALL", null, ["callee:004878fc:8"]]
+ 00a41214 ["INT_ADD", "register:40f0:8", ["const:a41214:8", "const:4:8"]]
+ 00a41214 ["CALL", null, ["callee:004878fc:8"]]
- 009e4318 bytes d301ea97
+ 00a41214 bytes ba19e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a1bb31af224f3c7d1c84a3542f352b"></a>

### [`009e4e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e58.md) → [`00a41d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41d54.md) FUN_00a41d54

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f9e4.md) [`0088faec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088faec.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 2件 [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) [`008c2e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2e68.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e4ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e58.md#insn-009e4ec0)
- 新版 [`00a41dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41d54.md#insn-00a41dbc)

~~~diff
- 009e4ec0 ["INT_ADD", "register:40f0:8", ["const:9e4ec0:8", "const:4:8"]]
- 009e4ec0 ["CALL", null, ["callee:00c58050:8"]]
+ 00a41dbc ["INT_ADD", "register:40f0:8", ["const:a41dbc:8", "const:4:8"]]
+ 00a41dbc ["CALL", null, ["callee:00c58050:8"]]
- 009e4ec0 bytes d0d90794
+ 00a41dbc bytes a5580894
~~~


<a id="compare-7e24123a988d8a0c0ca0488760837f20"></a>

### [`009e9508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9508.md) → [`00a46404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46404.md) FUN_00a46404

採用 · 移動量 `+0x5cefc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) [`007999cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/007999cc.md) [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 2件 [`009e955c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e955c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`007caa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md) [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 2件 [`00a46458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46458.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e952c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9508.md#insn-009e952c) · [`009e9558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9508.md#insn-009e9558)
- 新版 [`00a46428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46404.md#insn-00a46428) · [`00a46454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46404.md#insn-00a46454)

~~~diff
- 009e952c ["INT_ADD", "register:40f0:8", ["const:9e952c:8", "const:4:8"]]
- 009e952c ["CALL", null, ["callee:00a46458:8"]]
+ 00a46428 ["INT_ADD", "register:40f0:8", ["const:a46428:8", "const:4:8"]]
+ 00a46428 ["CALL", null, ["callee:00a46458:8"]]
- 009e952c bytes 0c000094
+ 00a46428 bytes 0c000094
- 009e9558 ["INT_ADD", "register:40f0:8", ["const:9e9558:8", "const:4:8"]]
- 009e9558 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00a46454 ["INT_ADD", "register:40f0:8", ["const:a46454:8", "const:4:8"]]
+ 00a46454 ["CALL", null, ["callee:00c57ae0:8"]]
- 009e9558 bytes cec60794
+ 00a46454 bytes a3450894
~~~


<a id="compare-90871e4394588192aeb916d6a921afcb"></a>

### [`009e9690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md) → [`00a4658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md) FUN_00a4658c

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 58件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e144c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`009ea9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9a8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 62件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00a478a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478a4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e9718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md#insn-009e9718) · [`009e9754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md#insn-009e9754) · [`009e9768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md#insn-009e9768)
- 新版 [`00a46614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md#insn-00a46614) · [`00a46650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md#insn-00a46650) · [`00a46664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md#insn-00a46664)

~~~diff
- 009e9718 ["INT_ADD", "register:40f0:8", ["const:9e9718:8", "const:4:8"]]
- 009e9718 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a46614 ["INT_ADD", "register:40f0:8", ["const:a46614:8", "const:4:8"]]
+ 00a46614 ["CALL", null, ["callee:00c57a90:8"]]
- 009e9718 bytes 4ac60794
+ 00a46614 bytes 1f450894
- 009e9754 ["INT_ADD", "register:40f0:8", ["const:9e9754:8", "const:4:8"]]
- 009e9754 ["CALL", null, ["callee:00c57c00:8"]]
+ 00a46650 ["INT_ADD", "register:40f0:8", ["const:a46650:8", "const:4:8"]]
+ 00a46650 ["CALL", null, ["callee:00c57c00:8"]]
- 009e9754 bytes 97c60794
+ 00a46650 bytes 6c450894
- 009e9768 ["INT_ADD", "register:40f0:8", ["const:9e9768:8", "const:4:8"]]
- 009e9768 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a46664 ["INT_ADD", "register:40f0:8", ["const:a46664:8", "const:4:8"]]
+ 00a46664 ["CALL", null, ["callee:00c57ab0:8"]]
- 009e9768 bytes 3ec60794
+ 00a46664 bytes 13450894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a616322c32279790a6296696e92b494"></a>

### [`009e9808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9808.md) → [`00a46704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46704.md) FUN_00a46704

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 71件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e144c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) · 呼出先 9件 [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00467080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467080.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c70.md) [`009e9930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md)
- 新版 呼出元 75件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 9件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00489f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f18.md) [`0048ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab00.md) [`0048ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab08.md) [`00a4682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e9834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9808.md#insn-009e9834) · [`009e984c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9808.md#insn-009e984c) · [`009e9864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9808.md#insn-009e9864)
- 新版 [`00a46730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46704.md#insn-00a46730) · [`00a46748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46704.md#insn-00a46748) · [`00a46760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46704.md#insn-00a46760)

~~~diff
- 009e9834 ["INT_ADD", "register:40f0:8", ["const:9e9834:8", "const:4:8"]]
- 009e9834 ["CALL", null, ["callee:00a4682c:8"]]
+ 00a46730 ["INT_ADD", "register:40f0:8", ["const:a46730:8", "const:4:8"]]
+ 00a46730 ["CALL", null, ["callee:00a4682c:8"]]
- 009e9834 bytes 3f000094
+ 00a46730 bytes 3f000094
- 009e984c ["INT_ADD", "register:40f0:8", ["const:9e984c:8", "const:4:8"]]
- 009e984c ["CALL", null, ["callee:00c538b0:8"]]
+ 00a46748 ["INT_ADD", "register:40f0:8", ["const:a46748:8", "const:4:8"]]
+ 00a46748 ["CALL", null, ["callee:00c538b0:8"]]
- 009e984c bytes 85b50794
+ 00a46748 bytes 5a340894
- 009e9864 ["INT_ADD", "register:40f0:8", ["const:9e9864:8", "const:4:8"]]
- 009e9864 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a46760 ["INT_ADD", "register:40f0:8", ["const:a46760:8", "const:4:8"]]
+ 00a46760 ["CALL", null, ["callee:00c538e0:8"]]
- 009e9864 bytes 8bb50794
+ 00a46760 bytes 60340894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7feec28d5b0152a99556e84cda7afcce"></a>

### [`009e9a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9a54.md) → [`00a46950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46950.md) FUN_00a46950

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0075c6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c6cc.md) [`00797bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00797/00797bfc.md) [`00a2fd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2f/00a2fd5c.md) [`00a33db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33db0.md) [`00a3479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a3479c.md) · 呼出先 3件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 5件 [`00786b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md) [`007c8cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c8/007c8cb0.md) [`00a8dbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8d/00a8dbc0.md) [`00a91c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a91/00a91c18.md) [`00a92604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a92/00a92604.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e9a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9a54.md#insn-009e9a78) · [`009e9a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9a54.md#insn-009e9a90) · [`009e9aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9a54.md#insn-009e9aa4)
- 新版 [`00a46974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46950.md#insn-00a46974) · [`00a4698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46950.md#insn-00a4698c) · [`00a469a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46950.md#insn-00a469a0)

~~~diff
- 009e9a78 ["INT_ADD", "register:40f0:8", ["const:9e9a78:8", "const:4:8"]]
- 009e9a78 ["CALL", null, ["callee:00c538b0:8"]]
+ 00a46974 ["INT_ADD", "register:40f0:8", ["const:a46974:8", "const:4:8"]]
+ 00a46974 ["CALL", null, ["callee:00c538b0:8"]]
- 009e9a78 bytes fab40794
+ 00a46974 bytes cf330894
- 009e9a90 ["INT_ADD", "register:40f0:8", ["const:9e9a90:8", "const:4:8"]]
- 009e9a90 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a4698c ["INT_ADD", "register:40f0:8", ["const:a4698c:8", "const:4:8"]]
+ 00a4698c ["CALL", null, ["callee:00c538e0:8"]]
- 009e9a90 bytes 00b50794
+ 00a4698c bytes d5330894
- 009e9aa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009e9aa4 ["INT_ADD", "register:40f0:8", ["const:9e9aa4:8", "const:4:8"]]
- 009e9aa4 ["CALLIND", null, ["register:0:8"]]
+ 00a469a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a469a0 ["INT_ADD", "register:40f0:8", ["const:a469a0:8", "const:4:8"]]
+ 00a469a0 ["CALLIND", null, ["register:0:8"]]
- 009e9aa4 bytes 00013fd6
+ 00a469a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f3cb148c273b4f94eb3905d3a53c62b"></a>

### [`009e9ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md) → [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md) FUN_00a469c0

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 57件 [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) [`005a3eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3eb8.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005b74d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b74d0.md) [`005f8b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b54.md) · 呼出先 4件 [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00467080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467080.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c70.md)
- 新版 呼出元 59件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005dc1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc1a0.md) [`0061e558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e558.md) · 呼出先 4件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00489f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f18.md) [`0048ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab00.md) [`0048ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e9ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md#insn-009e9ae4) · [`009e9af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md#insn-009e9af8) · [`009e9b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md#insn-009e9b10)
- 新版 [`00a469e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md#insn-00a469e0) · [`00a469f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md#insn-00a469f4) · [`00a46a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md#insn-00a46a0c)

~~~diff
- 009e9ae4 ["INT_ADD", "register:40f0:8", ["const:9e9ae4:8", "const:4:8"]]
- 009e9ae4 ["CALL", null, ["callee:00489f18:8"]]
+ 00a469e0 ["INT_ADD", "register:40f0:8", ["const:a469e0:8", "const:4:8"]]
+ 00a469e0 ["CALL", null, ["callee:00489f18:8"]]
- 009e9ae4 bytes 67f5e997
+ 00a469e0 bytes 4e0de997
- 009e9af8 ["INT_ADD", "register:40f0:8", ["const:9e9af8:8", "const:4:8"]]
- 009e9af8 ["CALL", null, ["callee:00489f0c:8"]]
+ 00a469f4 ["INT_ADD", "register:40f0:8", ["const:a469f4:8", "const:4:8"]]
+ 00a469f4 ["CALL", null, ["callee:00489f0c:8"]]
- 009e9af8 bytes 5ff5e997
+ 00a469f4 bytes 460de997
- 009e9b10 ["INT_ADD", "register:40f0:8", ["const:9e9b10:8", "const:4:8"]]
- 009e9b10 ["CALL", null, ["callee:0048ab00:8"]]
+ 00a46a0c ["INT_ADD", "register:40f0:8", ["const:a46a0c:8", "const:4:8"]]
+ 00a46a0c ["CALL", null, ["callee:0048ab00:8"]]
- 009e9b10 bytes 56f8e997
+ 00a46a0c bytes 3d10e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d74f1b56115ec9e0009dbd1dd45e700d"></a>

### [`009e9bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9bd4.md) → [`00a46ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ad0.md) FUN_00a46ad0

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`007999cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/007999cc.md) [`007be3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007be3c8.md) · 呼出先 9件 [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00467080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467080.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c70.md) [`009e9930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md)
- 新版 呼出元 3件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`007caa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md) [`007f0534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0534.md) · 呼出先 9件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00489f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f18.md) [`0048ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab00.md) [`0048ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab08.md) [`00a4682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e9c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9bd4.md#insn-009e9c00) · [`009e9c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9bd4.md#insn-009e9c18) · [`009e9c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9bd4.md#insn-009e9c30)
- 新版 [`00a46afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ad0.md#insn-00a46afc) · [`00a46b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ad0.md#insn-00a46b14) · [`00a46b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ad0.md#insn-00a46b2c)

~~~diff
- 009e9c00 ["INT_ADD", "register:40f0:8", ["const:9e9c00:8", "const:4:8"]]
- 009e9c00 ["CALL", null, ["callee:00a4682c:8"]]
+ 00a46afc ["INT_ADD", "register:40f0:8", ["const:a46afc:8", "const:4:8"]]
+ 00a46afc ["CALL", null, ["callee:00a4682c:8"]]
- 009e9c00 bytes 4cffff97
+ 00a46afc bytes 4cffff97
- 009e9c18 ["INT_ADD", "register:40f0:8", ["const:9e9c18:8", "const:4:8"]]
- 009e9c18 ["CALL", null, ["callee:00c538b0:8"]]
+ 00a46b14 ["INT_ADD", "register:40f0:8", ["const:a46b14:8", "const:4:8"]]
+ 00a46b14 ["CALL", null, ["callee:00c538b0:8"]]
- 009e9c18 bytes 92b40794
+ 00a46b14 bytes 67330894
- 009e9c30 ["INT_ADD", "register:40f0:8", ["const:9e9c30:8", "const:4:8"]]
- 009e9c30 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a46b2c ["INT_ADD", "register:40f0:8", ["const:a46b2c:8", "const:4:8"]]
+ 00a46b2c ["CALL", null, ["callee:00c538e0:8"]]
- 009e9c30 bytes 98b40794
+ 00a46b2c bytes 6d330894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de52f3939f9e4a12ab99a3e19ba229e3"></a>

### [`009e9cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9cf4.md) → [`00a46bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46bf0.md) FUN_00a46bf0

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088a82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088a/0088a82c.md) · 呼出先 5件 [`009e9930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md) [`009e9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008bdabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bd/008bdabc.md) · 呼出先 5件 [`00a4682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md) [`00a46a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e9d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9cf4.md#insn-009e9d34) · [`009e9d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9cf4.md#insn-009e9d4c) · [`009e9d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9cf4.md#insn-009e9d64)
- 新版 [`00a46c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46bf0.md#insn-00a46c30) · [`00a46c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46bf0.md#insn-00a46c48) · [`00a46c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46bf0.md#insn-00a46c60)

~~~diff
- 009e9d34 ["INT_ADD", "register:40f0:8", ["const:9e9d34:8", "const:4:8"]]
- 009e9d34 ["CALL", null, ["callee:00a4682c:8"]]
+ 00a46c30 ["INT_ADD", "register:40f0:8", ["const:a46c30:8", "const:4:8"]]
+ 00a46c30 ["CALL", null, ["callee:00a4682c:8"]]
- 009e9d34 bytes fffeff97
+ 00a46c30 bytes fffeff97
- 009e9d4c ["INT_ADD", "register:40f0:8", ["const:9e9d4c:8", "const:4:8"]]
- 009e9d4c ["CALL", null, ["callee:00c538b0:8"]]
+ 00a46c48 ["INT_ADD", "register:40f0:8", ["const:a46c48:8", "const:4:8"]]
+ 00a46c48 ["CALL", null, ["callee:00c538b0:8"]]
- 009e9d4c bytes 45b40794
+ 00a46c48 bytes 1a330894
- 009e9d64 ["INT_ADD", "register:40f0:8", ["const:9e9d64:8", "const:4:8"]]
- 009e9d64 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a46c60 ["INT_ADD", "register:40f0:8", ["const:a46c60:8", "const:4:8"]]
+ 00a46c60 ["CALL", null, ["callee:00c538e0:8"]]
- 009e9d64 bytes 4bb40794
+ 00a46c60 bytes 20330894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86a73d7124e2d63f7dd9bb07e5fd8e24"></a>

### [`009ea300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea300.md) → [`00a471fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a471fc.md) FUN_00a471fc

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00447b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447b24.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ea324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea300.md#insn-009ea324) · [`009ea328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea300.md#insn-009ea328) · [`009ea35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea300.md#insn-009ea35c)
- 新版 [`00a47220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a471fc.md#insn-00a47220) · [`00a47224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a471fc.md#insn-00a47224) · [`00a47258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a471fc.md#insn-00a47258)

~~~diff
- 009ea324 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ea324 ["INT_ADD", "register:40f0:8", ["const:9ea324:8", "const:4:8"]]
- 009ea324 ["CALLIND", null, ["register:0:8"]]
+ 00a47220 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a47220 ["INT_ADD", "register:40f0:8", ["const:a47220:8", "const:4:8"]]
+ 00a47220 ["CALLIND", null, ["register:0:8"]]
- 009ea324 bytes 00013fd6
+ 00a47220 bytes 00013fd6
- 009ea328 ["INT_ADD", "register:40f0:8", ["const:9ea328:8", "const:4:8"]]
- 009ea328 ["CALL", null, ["callee:00467820:8"]]
+ 00a47224 ["INT_ADD", "register:40f0:8", ["const:a47224:8", "const:4:8"]]
+ 00a47224 ["CALL", null, ["callee:00467820:8"]]
- 009ea328 bytes 9869e997
+ 00a47224 bytes 7f81e897
- 009ea35c ["INT_ADD", "register:40f0:8", ["const:9ea35c:8", "const:4:8"]]
- 009ea35c ["CALL", null, ["callee:00467aec:8"]]
+ 00a47258 ["INT_ADD", "register:40f0:8", ["const:a47258:8", "const:4:8"]]
+ 00a47258 ["CALL", null, ["callee:00467aec:8"]]
- 009ea35c bytes 3e6ae997
+ 00a47258 bytes 2582e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06726e45cabc5be4d2e2a131c0cd6ea4"></a>

### [`009ea458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea458.md) → [`00a47354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47354.md) FUN_00a47354

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 21件 [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e144c.md) [`00633eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/00633eb0.md) [`00635b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00635/00635b20.md) · 呼出先 5件 [`009e955c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e955c.md) [`009e9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 25件 [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md) [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md) [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md) · 呼出先 5件 [`00a46458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46458.md) [`00a46a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ea49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea458.md#insn-009ea49c) · [`009ea4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea458.md#insn-009ea4b4) · [`009ea4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea458.md#insn-009ea4cc)
- 新版 [`00a47398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47354.md#insn-00a47398) · [`00a473b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47354.md#insn-00a473b0) · [`00a473c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47354.md#insn-00a473c8)

~~~diff
- 009ea49c ["INT_ADD", "register:40f0:8", ["const:9ea49c:8", "const:4:8"]]
- 009ea49c ["CALL", null, ["callee:00a46458:8"]]
+ 00a47398 ["INT_ADD", "register:40f0:8", ["const:a47398:8", "const:4:8"]]
+ 00a47398 ["CALL", null, ["callee:00a46458:8"]]
- 009ea49c bytes 30fcff97
+ 00a47398 bytes 30fcff97
- 009ea4b4 ["INT_ADD", "register:40f0:8", ["const:9ea4b4:8", "const:4:8"]]
- 009ea4b4 ["CALL", null, ["callee:00c538b0:8"]]
+ 00a473b0 ["INT_ADD", "register:40f0:8", ["const:a473b0:8", "const:4:8"]]
+ 00a473b0 ["CALL", null, ["callee:00c538b0:8"]]
- 009ea4b4 bytes 6bb20794
+ 00a473b0 bytes 40310894
- 009ea4cc ["INT_ADD", "register:40f0:8", ["const:9ea4cc:8", "const:4:8"]]
- 009ea4cc ["CALL", null, ["callee:00c538e0:8"]]
+ 00a473c8 ["INT_ADD", "register:40f0:8", ["const:a473c8:8", "const:4:8"]]
+ 00a473c8 ["CALL", null, ["callee:00c538e0:8"]]
- 009ea4cc bytes 71b20794
+ 00a473c8 bytes 46310894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6fa5d82c5dea114eb0e77e1f67dd379"></a>

### [`00a00e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00e18.md) → [`00a5e400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e400.md) FUN_00a5e400

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) · 呼出先 1件 [`0065bee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bee8.md)
- 新版 呼出元 1件 [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) · 呼出先 1件 [`006821d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a00e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00e18.md#insn-00a00e30) · [`00a00e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00e18.md#insn-00a00e3c) · [`00a00e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00e18.md#insn-00a00e48)
- 新版 [`00a5e418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e400.md#insn-00a5e418) · [`00a5e424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e400.md#insn-00a5e424) · [`00a5e430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e400.md#insn-00a5e430)

~~~diff
- 00a00e30 ["INT_ADD", "register:40f0:8", ["const:a00e30:8", "const:4:8"]]
- 00a00e30 ["CALL", null, ["callee:006821d8:8"]]
+ 00a5e418 ["INT_ADD", "register:40f0:8", ["const:a5e418:8", "const:4:8"]]
+ 00a5e418 ["CALL", null, ["callee:006821d8:8"]]
- 00a00e30 bytes 2e6cf197
+ 00a5e418 bytes 708ff097
- 00a00e3c ["INT_ADD", "register:40f0:8", ["const:a00e3c:8", "const:4:8"]]
- 00a00e3c ["CALL", null, ["callee:006821d8:8"]]
+ 00a5e424 ["INT_ADD", "register:40f0:8", ["const:a5e424:8", "const:4:8"]]
+ 00a5e424 ["CALL", null, ["callee:006821d8:8"]]
- 00a00e3c bytes 2b6cf197
+ 00a5e424 bytes 6d8ff097
- 00a00e48 ["INT_ADD", "register:40f0:8", ["const:a00e48:8", "const:4:8"]]
- 00a00e48 ["CALL", null, ["callee:006821d8:8"]]
+ 00a5e430 ["INT_ADD", "register:40f0:8", ["const:a5e430:8", "const:4:8"]]
+ 00a5e430 ["CALL", null, ["callee:006821d8:8"]]
- 00a00e48 bytes 286cf197
+ 00a5e430 bytes 6a8ff097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dfa34fc8bf18b9533ca4925b37e88c2"></a>

### [`00a00f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00f2c.md) → [`00a5e514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e514.md) FUN_00a5e514

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) · 呼出先 1件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md)
- 新版 呼出元 1件 [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) · 呼出先 1件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a00f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00f2c.md#insn-00a00f40) · [`00a00f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00f2c.md#insn-00a00f48) · [`00a00f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00f2c.md#insn-00a00f50)
- 新版 [`00a5e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e514.md#insn-00a5e528) · [`00a5e530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e514.md#insn-00a5e530) · [`00a5e538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e514.md#insn-00a5e538)

~~~diff
- 00a00f40 ["INT_ADD", "register:40f0:8", ["const:a00f40:8", "const:4:8"]]
- 00a00f40 ["CALL", null, ["callee:0046ef9c:8"]]
+ 00a5e528 ["INT_ADD", "register:40f0:8", ["const:a5e528:8", "const:4:8"]]
+ 00a5e528 ["CALL", null, ["callee:0046ef9c:8"]]
- 00a00f40 bytes 712ce997
+ 00a5e528 bytes 9d42e897
- 00a00f48 ["INT_ADD", "register:40f0:8", ["const:a00f48:8", "const:4:8"]]
- 00a00f48 ["CALL", null, ["callee:0046ef9c:8"]]
+ 00a5e530 ["INT_ADD", "register:40f0:8", ["const:a5e530:8", "const:4:8"]]
+ 00a5e530 ["CALL", null, ["callee:0046ef9c:8"]]
- 00a00f48 bytes 6f2ce997
+ 00a5e530 bytes 9b42e897
- 00a00f50 ["INT_ADD", "register:40f0:8", ["const:a00f50:8", "const:4:8"]]
- 00a00f50 ["CALL", null, ["callee:0046ef9c:8"]]
+ 00a5e538 ["INT_ADD", "register:40f0:8", ["const:a5e538:8", "const:4:8"]]
+ 00a5e538 ["CALL", null, ["callee:0046ef9c:8"]]
- 00a00f50 bytes 6d2ce997
+ 00a5e538 bytes 9942e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eae3f00479983c47a25ec1fe598444e6"></a>

### [`00a00fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00fec.md) → [`00a5e5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e5d4.md) FUN_00a5e5d4

採用 · 移動量 `+0x5d5e8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a01000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00fec.md#insn-00a01000) · [`00a01008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00fec.md#insn-00a01008)
- 新版 [`00a5e5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e5d4.md#insn-00a5e5e8) · [`00a5e5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e5d4.md#insn-00a5e5f0)

~~~diff
- 00a01000 ["INT_ADD", "register:40f0:8", ["const:a01000:8", "const:4:8"]]
- 00a01000 ["CALL", null, ["callee:0046e864:8"]]
+ 00a5e5e8 ["INT_ADD", "register:40f0:8", ["const:a5e5e8:8", "const:4:8"]]
+ 00a5e5e8 ["CALL", null, ["callee:0046e864:8"]]
- 00a01000 bytes 732ae997
+ 00a5e5e8 bytes 9f40e897
- 00a01008 ["INT_ADD", "register:40f0:8", ["const:a01008:8", "const:4:8"]]
- 00a01008 ["CALL", null, ["callee:0046e864:8"]]
+ 00a5e5f0 ["INT_ADD", "register:40f0:8", ["const:a5e5f0:8", "const:4:8"]]
+ 00a5e5f0 ["CALL", null, ["callee:0046e864:8"]]
- 00a01008 bytes 712ae997
+ 00a5e5f0 bytes 9d40e897
~~~


<a id="compare-be5d6eb8413f6b84050e2db641aceed1"></a>

### [`00a0101c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0101c.md) → [`00a5e604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e604.md) FUN_00a5e604

採用 · 移動量 `+0x5d5e8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a01030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0101c.md#insn-00a01030) · [`00a01038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0101c.md#insn-00a01038) · [`00a01040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0101c.md#insn-00a01040)
- 新版 [`00a5e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e604.md#insn-00a5e618) · [`00a5e620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e604.md#insn-00a5e620) · [`00a5e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e604.md#insn-00a5e628)

~~~diff
- 00a01030 ["INT_ADD", "register:40f0:8", ["const:a01030:8", "const:4:8"]]
- 00a01030 ["CALL", null, ["callee:0046e864:8"]]
+ 00a5e618 ["INT_ADD", "register:40f0:8", ["const:a5e618:8", "const:4:8"]]
+ 00a5e618 ["CALL", null, ["callee:0046e864:8"]]
- 00a01030 bytes 672ae997
+ 00a5e618 bytes 9340e897
- 00a01038 ["INT_ADD", "register:40f0:8", ["const:a01038:8", "const:4:8"]]
- 00a01038 ["CALL", null, ["callee:0046e864:8"]]
+ 00a5e620 ["INT_ADD", "register:40f0:8", ["const:a5e620:8", "const:4:8"]]
+ 00a5e620 ["CALL", null, ["callee:0046e864:8"]]
- 00a01038 bytes 652ae997
+ 00a5e620 bytes 9140e897
- 00a01040 ["INT_ADD", "register:40f0:8", ["const:a01040:8", "const:4:8"]]
- 00a01040 ["CALL", null, ["callee:0046e864:8"]]
+ 00a5e628 ["INT_ADD", "register:40f0:8", ["const:a5e628:8", "const:4:8"]]
+ 00a5e628 ["CALL", null, ["callee:0046e864:8"]]
- 00a01040 bytes 632ae997
+ 00a5e628 bytes 8f40e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32c16f4126d22454fd1b63017987e212"></a>

### [`00a0105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0105c.md) → [`00a5e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e644.md) FUN_00a5e644

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a01094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0105c.md#insn-00a01094) · [`00a010a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0105c.md#insn-00a010a8) · [`00a010b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a0105c.md#insn-00a010b0)
- 新版 [`00a5e67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e644.md#insn-00a5e67c) · [`00a5e690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e644.md#insn-00a5e690) · [`00a5e698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e644.md#insn-00a5e698)

~~~diff
- 00a01094 ["INT_ADD", "register:40f0:8", ["const:a01094:8", "const:4:8"]]
- 00a01094 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a5e67c ["INT_ADD", "register:40f0:8", ["const:a5e67c:8", "const:4:8"]]
+ 00a5e67c ["CALL", null, ["callee:00c538e0:8"]]
- 00a01094 bytes 7f570794
+ 00a5e67c bytes 99d40794
- 00a010a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a010a8 ["INT_ADD", "register:40f0:8", ["const:a010a8:8", "const:4:8"]]
- 00a010a8 ["CALLIND", null, ["register:0:8"]]
+ 00a5e690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a5e690 ["INT_ADD", "register:40f0:8", ["const:a5e690:8", "const:4:8"]]
+ 00a5e690 ["CALLIND", null, ["register:0:8"]]
- 00a010a8 bytes 00013fd6
+ 00a5e690 bytes 00013fd6
- 00a010b0 ["INT_ADD", "register:40f0:8", ["const:a010b0:8", "const:4:8"]]
- 00a010b0 ["CALL", null, ["callee:00c57a80:8"]]
+ 00a5e698 ["INT_ADD", "register:40f0:8", ["const:a5e698:8", "const:4:8"]]
+ 00a5e698 ["CALL", null, ["callee:00c57a80:8"]]
- 00a010b0 bytes e0670794
+ 00a5e698 bytes fae40794
~~~


<a id="compare-0f2fc015ea75b05275b9602833bd57bb"></a>

### [`00a028b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a028b8.md) → [`00a5fea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5fea0.md) FUN_00a5fea0

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a028d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a028b8.md#insn-00a028d4)
- 新版 [`00a5febc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5fea0.md#insn-00a5febc)

~~~diff
- 00a028d4 ["INT_ADD", "register:40f0:8", ["const:a028d4:8", "const:4:8"]]
- 00a028d4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a5febc ["INT_ADD", "register:40f0:8", ["const:a5febc:8", "const:4:8"]]
+ 00a5febc ["CALL", null, ["callee:00c57ab0:8"]]
- 00a028d4 bytes e3610794
+ 00a5febc bytes fdde0794
~~~


<a id="compare-fcd2cee9be301c1b7d06ec253f88376d"></a>

### [`00a05234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05234.md) → [`00a62820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62820.md) FUN_00a62820

採用 · 移動量 `+0x5d5ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a05118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05118.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a62704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62704.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a05244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05234.md#insn-00a05244)
- 新版 [`00a62830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62820.md#insn-00a62830)

~~~diff
- 00a05244 ["INT_ADD", "register:40f0:8", ["const:a05244:8", "const:4:8"]]
- 00a05244 ["CALL", null, ["callee:00a62704:8"]]
+ 00a62830 ["INT_ADD", "register:40f0:8", ["const:a62830:8", "const:4:8"]]
+ 00a62830 ["CALL", null, ["callee:00a62704:8"]]
- 00a05244 bytes b5ffff97
+ 00a62830 bytes b5ffff97
~~~


<a id="compare-cb9674b52edaea5c42f23f012c09fce8"></a>

### [`00a09d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09d6c.md) → [`00a67a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67a3c.md) FUN_00a67a3c

採用 · 移動量 `+0x5dcd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a0a4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00a6819c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a6819c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a09d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09d6c.md#insn-00a09d98)
- 新版 [`00a67a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67a3c.md#insn-00a67a68)

~~~diff
- 00a09d98 ["INT_ADD", "register:40f0:8", ["const:a09d98:8", "const:4:8"]]
- 00a09d98 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a67a68 ["INT_ADD", "register:40f0:8", ["const:a67a68:8", "const:4:8"]]
+ 00a67a68 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a09d98 bytes b2440794
+ 00a67a68 bytes 12c00794
~~~


<a id="compare-0f761c225606f925848b9e93f3e3de21"></a>

### [`00a0a14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a14c.md) → [`00a67e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67e1c.md) FUN_00a67e1c

採用 · 移動量 `+0x5dcd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00837180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0a164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a14c.md#insn-00a0a164)
- 新版 [`00a67e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67e1c.md#insn-00a67e34)

~~~diff
- 00a0a164 ["INT_ADD", "register:40f0:8", ["const:a0a164:8", "const:4:8"]]
- 00a0a164 ["CALL", null, ["callee:008690f8:8"]]
+ 00a67e34 ["INT_ADD", "register:40f0:8", ["const:a67e34:8", "const:4:8"]]
+ 00a67e34 ["CALL", null, ["callee:008690f8:8"]]
- 00a0a164 bytes 07b4f897
+ 00a67e34 bytes b104f897
~~~


<a id="compare-d33f3c6805b09fd027944f65c48559e3"></a>

### [`00a0b50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b50c.md) → [`00a69240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69240.md) FUN_00a69240

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d0/009d0f70.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a2de6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2d/00a2de6c.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0b524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b50c.md#insn-00a0b524) · [`00a0b530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b50c.md#insn-00a0b530) · [`00a0b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b50c.md#insn-00a0b53c)
- 新版 [`00a69258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69240.md#insn-00a69258) · [`00a69264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69240.md#insn-00a69264) · [`00a69270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69240.md#insn-00a69270)

~~~diff
- 00a0b524 ["INT_ADD", "register:40f0:8", ["const:a0b524:8", "const:4:8"]]
- 00a0b524 ["CALL", null, ["callee:004803b0:8"]]
+ 00a69258 ["INT_ADD", "register:40f0:8", ["const:a69258:8", "const:4:8"]]
+ 00a69258 ["CALL", null, ["callee:004803b0:8"]]
- 00a0b524 bytes fd47e997
+ 00a69258 bytes 565ce897
- 00a0b530 ["INT_ADD", "register:40f0:8", ["const:a0b530:8", "const:4:8"]]
- 00a0b530 ["CALL", null, ["callee:004803b0:8"]]
+ 00a69264 ["INT_ADD", "register:40f0:8", ["const:a69264:8", "const:4:8"]]
+ 00a69264 ["CALL", null, ["callee:004803b0:8"]]
- 00a0b530 bytes fa47e997
+ 00a69264 bytes 535ce897
- 00a0b53c ["INT_ADD", "register:40f0:8", ["const:a0b53c:8", "const:4:8"]]
- 00a0b53c ["CALL", null, ["callee:004803b0:8"]]
+ 00a69270 ["INT_ADD", "register:40f0:8", ["const:a69270:8", "const:4:8"]]
+ 00a69270 ["CALL", null, ["callee:004803b0:8"]]
- 00a0b53c bytes f747e997
+ 00a69270 bytes 505ce897
~~~


<a id="compare-70887a6413f0e207105f07f7a9d79d95"></a>

### [`00a0be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0be80.md) → [`00a69bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bb4.md) FUN_00a69bb4

採用 · 移動量 `+0x5dd34` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 2件 [`00a0bea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bea4.md) [`00a0c374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c374.md)
- 新版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 2件 [`00a69bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bd8.md) [`00a6a0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0be90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0be80.md#insn-00a0be90)
- 新版 [`00a69bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bb4.md#insn-00a69bc4)

~~~diff
- 00a0be90 ["INT_ADD", "register:40f0:8", ["const:a0be90:8", "const:4:8"]]
- 00a0be90 ["CALL", null, ["callee:00a69bd8:8"]]
+ 00a69bc4 ["INT_ADD", "register:40f0:8", ["const:a69bc4:8", "const:4:8"]]
+ 00a69bc4 ["CALL", null, ["callee:00a69bd8:8"]]
- 00a0be90 bytes 05000094
+ 00a69bc4 bytes 05000094
~~~


<a id="compare-ebacc7caabd073f5a88cab4b103bdf30"></a>

### [`00a0c734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c734.md) → [`00a6a468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a468.md) FUN_00a6a468

採用 · 移動量 `+0x5dd34` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00839918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839918.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086bbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0c754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c734.md#insn-00a0c754)
- 新版 [`00a6a488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a468.md#insn-00a6a488)

~~~diff
- 00a0c754 ["INT_ADD", "register:40f0:8", ["const:a0c754:8", "const:4:8"]]
- 00a0c754 ["CALL", null, ["callee:0086bbb8:8"]]
+ 00a6a488 ["INT_ADD", "register:40f0:8", ["const:a6a488:8", "const:4:8"]]
+ 00a6a488 ["CALL", null, ["callee:0086bbb8:8"]]
- 00a0c754 bytes 71b4f897
+ 00a6a488 bytes cc05f897
~~~


<a id="compare-8c917a938a73e76b3670dd82648cc372"></a>

### [`00a0d958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d958.md) → [`00a6b5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b5c0.md) FUN_00a6b5c0

採用 · 移動量 `+0x5dc68` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 1件 [`0066b478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b478.md)
- 新版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0d980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d958.md#insn-00a0d980)
- 新版 [`00a6b5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b5c0.md#insn-00a6b5e8)

~~~diff
- 00a0d980 ["INT_ADD", "register:40f0:8", ["const:a0d980:8", "const:4:8"]]
- 00a0d980 ["CALL", null, ["callee:006917c0:8"]]
+ 00a6b5e8 ["INT_ADD", "register:40f0:8", ["const:a6b5e8:8", "const:4:8"]]
+ 00a6b5e8 ["CALL", null, ["callee:006917c0:8"]]
- 00a0d980 bytes be76f197
+ 00a6b5e8 bytes 7698f097
~~~


<a id="compare-b4f09a3079406ca83e9d4a9a993d4c7e"></a>

### [`00a116d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a11/00a116d0.md) → [`00a6f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f55c.md) FUN_00a6f55c

採用 · 移動量 `+0x5de8c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a115b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a11/00a115b0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a6f43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f43c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a116e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a11/00a116d0.md#insn-00a116e0)
- 新版 [`00a6f56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6f55c.md#insn-00a6f56c)

~~~diff
- 00a116e0 ["INT_ADD", "register:40f0:8", ["const:a116e0:8", "const:4:8"]]
- 00a116e0 ["CALL", null, ["callee:00a6f43c:8"]]
+ 00a6f56c ["INT_ADD", "register:40f0:8", ["const:a6f56c:8", "const:4:8"]]
+ 00a6f56c ["CALL", null, ["callee:00a6f43c:8"]]
- 00a116e0 bytes b4ffff97
+ 00a6f56c bytes b4ffff97
~~~


