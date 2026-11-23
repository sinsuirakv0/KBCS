# v15.7.4 → v16.0.0 · 要調査の変更候補 (10)

[一覧の目次](README.md)

<a id="compare-6337f9ca8b101cc5c0c8a207a846ce50"></a>

### [`0052968c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052968c.md) → [`0054c524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md) FUN_0054c524

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004f4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4778.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00529858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529858.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00517610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054c6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c6f0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052979c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052968c.md#insn-0052979c) · [`005297b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052968c.md#insn-005297b8) · [`005297e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052968c.md#insn-005297e4)
- 新版 [`0054c634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md#insn-0054c634) · [`0054c650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md#insn-0054c650) · [`0054c67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md#insn-0054c67c)

~~~diff
- 0052979c ["INT_ADD", "register:40f0:8", ["const:52979c:8", "const:4:8"]]
- 0052979c ["CALL", null, ["callee:00c57a90:8"]]
+ 0054c634 ["INT_ADD", "register:40f0:8", ["const:54c634:8", "const:4:8"]]
+ 0054c634 ["CALL", null, ["callee:00c57a90:8"]]
- 0052979c bytes 29c61a94
+ 0054c634 bytes 172d1c94
- 005297b8 ["INT_ADD", "register:40f0:8", ["const:5297b8:8", "const:4:8"]]
- 005297b8 ["CALL", null, ["callee:0054c6f0:8"]]
+ 0054c650 ["INT_ADD", "register:40f0:8", ["const:54c650:8", "const:4:8"]]
+ 0054c650 ["CALL", null, ["callee:0054c6f0:8"]]
- 005297b8 bytes 28000094
+ 0054c650 bytes 28000094
- 005297e4 ["INT_ADD", "register:40f0:8", ["const:5297e4:8", "const:4:8"]]
- 005297e4 ["CALL", null, ["callee:0043bb64:8"]]
+ 0054c67c ["INT_ADD", "register:40f0:8", ["const:54c67c:8", "const:4:8"]]
+ 0054c67c ["CALL", null, ["callee:0043bb64:8"]]
- 005297e4 bytes 20befb97
+ 0054c67c bytes 3abdfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea84081b3a421d0024598fa9c1c812f"></a>

### [`00529cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cd8.md) → [`0054cb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb70.md) FUN_0054cb70

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00529cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cd8.md#insn-00529cfc)
- 新版 [`0054cb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb70.md#insn-0054cb94)

~~~diff
- 00529cfc ["INT_ADD", "register:40f0:8", ["const:529cfc:8", "const:4:8"]]
- 00529cfc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054cb94 ["INT_ADD", "register:40f0:8", ["const:54cb94:8", "const:4:8"]]
+ 0054cb94 ["CALL", null, ["callee:00c57ab0:8"]]
- 00529cfc bytes d9c41a94
+ 0054cb94 bytes c72b1c94
~~~


<a id="compare-d817b3dcf9f8247a8ba42e696eb1c3aa"></a>

### [`0052a914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a914.md) → [`0054d7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d7ac.md) FUN_0054d7ac

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052a5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052a92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a914.md#insn-0052a92c)
- 新版 [`0054d7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d7ac.md#insn-0054d7c4)

~~~diff
- 0052a92c ["INT_ADD", "register:40f0:8", ["const:52a92c:8", "const:4:8"]]
- 0052a92c ["CALL", null, ["callee:0054d464:8"]]
+ 0054d7c4 ["INT_ADD", "register:40f0:8", ["const:54d7c4:8", "const:4:8"]]
+ 0054d7c4 ["CALL", null, ["callee:0054d464:8"]]
- 0052a92c bytes 28ffff97
+ 0054d7c4 bytes 28ffff97
~~~


<a id="compare-9a2d970e7849560da415a62ffc6c2982"></a>

### [`0052aac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052aac0.md) → [`0054d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d958.md) FUN_0054d958

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052bcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052bcb4.md) · 呼出先 2件 [`0051c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c938.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md) · 呼出先 2件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ab14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052aac0.md#insn-0052ab14)
- 新版 [`0054d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d958.md#insn-0054d9ac)

~~~diff
- 0052ab14 ["INT_ADD", "register:40f0:8", ["const:52ab14:8", "const:4:8"]]
- 0052ab14 ["CALL", null, ["callee:0053f7d0:8"]]
+ 0054d9ac ["INT_ADD", "register:40f0:8", ["const:54d9ac:8", "const:4:8"]]
+ 0054d9ac ["CALL", null, ["callee:0053f7d0:8"]]
- 0052ab14 bytes 89c7ff97
+ 0054d9ac bytes 89c7ff97
~~~


<a id="compare-fb23ab1550a75fe9dad2ff4628bb93c6"></a>

### [`0052ab54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab54.md) → [`0054d9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md) FUN_0054d9ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052abc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab54.md#insn-0052abc4) · [`0052abd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab54.md#insn-0052abd8) · [`0052abe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab54.md#insn-0052abe0)
- 新版 [`0054da5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md#insn-0054da5c) · [`0054da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md#insn-0054da70) · [`0054da78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md#insn-0054da78)

~~~diff
- 0052abc4 ["INT_ADD", "register:40f0:8", ["const:52abc4:8", "const:4:8"]]
- 0052abc4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0054da5c ["INT_ADD", "register:40f0:8", ["const:54da5c:8", "const:4:8"]]
+ 0054da5c ["CALL", null, ["callee:00c538e0:8"]]
- 0052abc4 bytes b3b01a94
+ 0054da5c bytes a1171c94
- 0052abd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052abd8 ["INT_ADD", "register:40f0:8", ["const:52abd8:8", "const:4:8"]]
- 0052abd8 ["CALLIND", null, ["register:0:8"]]
+ 0054da70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054da70 ["INT_ADD", "register:40f0:8", ["const:54da70:8", "const:4:8"]]
+ 0054da70 ["CALLIND", null, ["register:0:8"]]
- 0052abd8 bytes 00013fd6
+ 0054da70 bytes 00013fd6
- 0052abe0 ["INT_ADD", "register:40f0:8", ["const:52abe0:8", "const:4:8"]]
- 0052abe0 ["CALL", null, ["callee:00c57a80:8"]]
+ 0054da78 ["INT_ADD", "register:40f0:8", ["const:54da78:8", "const:4:8"]]
+ 0054da78 ["CALL", null, ["callee:00c57a80:8"]]
- 0052abe0 bytes 14c11a94
+ 0054da78 bytes 02281c94
~~~


<a id="compare-8dec75ee489f73bd747b9903d89d883d"></a>

### [`0052ac08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ac08.md) → [`0054daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md) FUN_0054daa0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ac78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ac08.md#insn-0052ac78) · [`0052ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ac08.md#insn-0052ac8c) · [`0052ac94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ac08.md#insn-0052ac94)
- 新版 [`0054db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md#insn-0054db10) · [`0054db24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md#insn-0054db24) · [`0054db2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md#insn-0054db2c)

~~~diff
- 0052ac78 ["INT_ADD", "register:40f0:8", ["const:52ac78:8", "const:4:8"]]
- 0052ac78 ["CALL", null, ["callee:00c538e0:8"]]
+ 0054db10 ["INT_ADD", "register:40f0:8", ["const:54db10:8", "const:4:8"]]
+ 0054db10 ["CALL", null, ["callee:00c538e0:8"]]
- 0052ac78 bytes 86b01a94
+ 0054db10 bytes 74171c94
- 0052ac8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ac8c ["INT_ADD", "register:40f0:8", ["const:52ac8c:8", "const:4:8"]]
- 0052ac8c ["CALLIND", null, ["register:0:8"]]
+ 0054db24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054db24 ["INT_ADD", "register:40f0:8", ["const:54db24:8", "const:4:8"]]
+ 0054db24 ["CALLIND", null, ["register:0:8"]]
- 0052ac8c bytes 00013fd6
+ 0054db24 bytes 00013fd6
- 0052ac94 ["INT_ADD", "register:40f0:8", ["const:52ac94:8", "const:4:8"]]
- 0052ac94 ["CALL", null, ["callee:00c57a80:8"]]
+ 0054db2c ["INT_ADD", "register:40f0:8", ["const:54db2c:8", "const:4:8"]]
+ 0054db2c ["CALL", null, ["callee:00c57a80:8"]]
- 0052ac94 bytes e7c01a94
+ 0054db2c bytes d5271c94
~~~


<a id="compare-340751d585478cd93ebb8ab8036f7dec"></a>

### [`0052acd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acd0.md) → [`0054db68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md) FUN_0054db68

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 3件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`0052ad78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ad78.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0054dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ace0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acd0.md#insn-0052ace0) · [`0052ad4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acd0.md#insn-0052ad4c) · [`0052ad5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acd0.md#insn-0052ad5c)
- 新版 [`0054db78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md#insn-0054db78) · [`0054dbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md#insn-0054dbe4) · [`0054dbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md#insn-0054dbf4)

~~~diff
- 0052ace0 ["INT_ADD", "register:40f0:8", ["const:52ace0:8", "const:4:8"]]
- 0052ace0 ["CALL", null, ["callee:0054dc10:8"]]
+ 0054db78 ["INT_ADD", "register:40f0:8", ["const:54db78:8", "const:4:8"]]
+ 0054db78 ["CALL", null, ["callee:0054dc10:8"]]
- 0052ace0 bytes 26000094
+ 0054db78 bytes 26000094
- 0052ad4c ["INT_ADD", "register:40f0:8", ["const:52ad4c:8", "const:4:8"]]
- 0052ad4c ["CALL", null, ["callee:004945d0:8"]]
+ 0054dbe4 ["INT_ADD", "register:40f0:8", ["const:54dbe4:8", "const:4:8"]]
+ 0054dbe4 ["CALL", null, ["callee:004945d0:8"]]
- 0052ad4c bytes 7b1afd97
+ 0054dbe4 bytes 7b1afd97
- 0052ad5c ["INT_ADD", "register:40f0:8", ["const:52ad5c:8", "const:4:8"]]
- 0052ad5c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054dbf4 ["INT_ADD", "register:40f0:8", ["const:54dbf4:8", "const:4:8"]]
+ 0054dbf4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0052ad5c bytes c1c01a94
+ 0054dbf4 bytes af271c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1328bb1a5baac4f77f16bb450a2de511"></a>

### [`0052ad78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ad78.md) → [`0054dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md) FUN_0054dc10

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0052acd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acd0.md) [`00b284c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b284c4.md) [`00b58dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58dc4.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 3件 [`0054db68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md) [`00b8d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d830.md) [`00bc82c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ade4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ad78.md#insn-0052ade4) · [`0052ae40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ad78.md#insn-0052ae40)
- 新版 [`0054dc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md#insn-0054dc7c) · [`0054dcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md#insn-0054dcd8)

~~~diff
- 0052ade4 ["INT_ADD", "register:40f0:8", ["const:52ade4:8", "const:4:8"]]
- 0052ade4 ["CALL", null, ["callee:00c57c50:8"]]
+ 0054dc7c ["INT_ADD", "register:40f0:8", ["const:54dc7c:8", "const:4:8"]]
+ 0054dc7c ["CALL", null, ["callee:00c57c50:8"]]
- 0052ade4 bytes 07c11a94
+ 0054dc7c bytes f5271c94
- 0052ae40 ["INT_ADD", "register:40f0:8", ["const:52ae40:8", "const:4:8"]]
- 0052ae40 ["CALL", null, ["callee:00c57c50:8"]]
+ 0054dcd8 ["INT_ADD", "register:40f0:8", ["const:54dcd8:8", "const:4:8"]]
+ 0054dcd8 ["CALL", null, ["callee:00c57c50:8"]]
- 0052ae40 bytes f0c01a94
+ 0054dcd8 bytes de271c94
~~~


<a id="compare-c4c33dd47a88316904ba89715e1aed8e"></a>

### [`0052ae90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md) → [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) FUN_0054dd28

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005256ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) [`0052b12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b12c.md) [`0052b264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b264.md) [`0052b348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b348.md)
- 新版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`0054dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md) [`0054e0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md) [`0054e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052af34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md#insn-0052af34) · [`0052af80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md#insn-0052af80) · [`0052afbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md#insn-0052afbc)
- 新版 [`0054ddcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md#insn-0054ddcc) · [`0054de18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md#insn-0054de18) · [`0054de54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md#insn-0054de54)

~~~diff
- 0052af34 ["INT_ADD", "register:40f0:8", ["const:52af34:8", "const:4:8"]]
- 0052af34 ["CALL", null, ["callee:00c57a90:8"]]
+ 0054ddcc ["INT_ADD", "register:40f0:8", ["const:54ddcc:8", "const:4:8"]]
+ 0054ddcc ["CALL", null, ["callee:00c57a90:8"]]
- 0052af34 bytes 43c01a94
+ 0054ddcc bytes 31271c94
- 0052af80 ["INT_ADD", "register:40f0:8", ["const:52af80:8", "const:4:8"]]
- 0052af80 ["CALL", null, ["callee:00c57a90:8"]]
+ 0054de18 ["INT_ADD", "register:40f0:8", ["const:54de18:8", "const:4:8"]]
+ 0054de18 ["CALL", null, ["callee:00c57a90:8"]]
- 0052af80 bytes 30c01a94
+ 0054de18 bytes 1e271c94
- 0052afbc ["INT_ADD", "register:40f0:8", ["const:52afbc:8", "const:4:8"]]
- 0052afbc ["CALL", null, ["callee:00c538b0:8"]]
+ 0054de54 ["INT_ADD", "register:40f0:8", ["const:54de54:8", "const:4:8"]]
+ 0054de54 ["CALL", null, ["callee:00c538b0:8"]]
- 0052afbc bytes a9af1a94
+ 0054de54 bytes 97161c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e190a9475f4ebe261ef6f4aac10b6614"></a>

### [`0052b12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b12c.md) → [`0054dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md) FUN_0054dfc4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052ae90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b12c.md#insn-0052b1a8) · [`0052b1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b12c.md#insn-0052b1f0) · [`0052b204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b12c.md#insn-0052b204)
- 新版 [`0054e040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md#insn-0054e040) · [`0054e088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md#insn-0054e088) · [`0054e09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md#insn-0054e09c)

~~~diff
- 0052b1a8 ["INT_ADD", "register:40f0:8", ["const:52b1a8:8", "const:4:8"]]
- 0052b1a8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054e040 ["INT_ADD", "register:40f0:8", ["const:54e040:8", "const:4:8"]]
+ 0054e040 ["CALL", null, ["callee:00c57ab0:8"]]
- 0052b1a8 bytes aebf1a94
+ 0054e040 bytes 9c261c94
- 0052b1f0 ["INT_ADD", "register:40f0:8", ["const:52b1f0:8", "const:4:8"]]
- 0052b1f0 ["CALL", null, ["callee:00c538e0:8"]]
+ 0054e088 ["INT_ADD", "register:40f0:8", ["const:54e088:8", "const:4:8"]]
+ 0054e088 ["CALL", null, ["callee:00c538e0:8"]]
- 0052b1f0 bytes 28af1a94
+ 0054e088 bytes 16161c94
- 0052b204 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b204 ["INT_ADD", "register:40f0:8", ["const:52b204:8", "const:4:8"]]
- 0052b204 ["CALLIND", null, ["register:0:8"]]
+ 0054e09c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e09c ["INT_ADD", "register:40f0:8", ["const:54e09c:8", "const:4:8"]]
+ 0054e09c ["CALLIND", null, ["register:0:8"]]
- 0052b204 bytes 00013fd6
+ 0054e09c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a01c534f671354ea66bcfbfa0a0c810e"></a>

### [`0052b264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b264.md) → [`0054e0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md) FUN_0054e0fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052ae90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b264.md#insn-0052b29c) · [`0052b2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b264.md#insn-0052b2ec) · [`0052b300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b264.md#insn-0052b300)
- 新版 [`0054e134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md#insn-0054e134) · [`0054e184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md#insn-0054e184) · [`0054e198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md#insn-0054e198)

~~~diff
- 0052b29c ["INT_ADD", "register:40f0:8", ["const:52b29c:8", "const:4:8"]]
- 0052b29c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054e134 ["INT_ADD", "register:40f0:8", ["const:54e134:8", "const:4:8"]]
+ 0054e134 ["CALL", null, ["callee:00c57ab0:8"]]
- 0052b29c bytes 71bf1a94
+ 0054e134 bytes 5f261c94
- 0052b2ec ["INT_ADD", "register:40f0:8", ["const:52b2ec:8", "const:4:8"]]
- 0052b2ec ["CALL", null, ["callee:00c538e0:8"]]
+ 0054e184 ["INT_ADD", "register:40f0:8", ["const:54e184:8", "const:4:8"]]
+ 0054e184 ["CALL", null, ["callee:00c538e0:8"]]
- 0052b2ec bytes e9ae1a94
+ 0054e184 bytes d7151c94
- 0052b300 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b300 ["INT_ADD", "register:40f0:8", ["const:52b300:8", "const:4:8"]]
- 0052b300 ["CALLIND", null, ["register:0:8"]]
+ 0054e198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e198 ["INT_ADD", "register:40f0:8", ["const:54e198:8", "const:4:8"]]
+ 0054e198 ["CALLIND", null, ["register:0:8"]]
- 0052b300 bytes 00013fd6
+ 0054e198 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c5620b9e05291451fa1fb60c94f2a5"></a>

### [`0052b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b35c.md) → [`0054e1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md) FUN_0054e1f4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 9件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005256ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) [`0052b6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b6f8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`0054e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b35c.md#insn-0052b400) · [`0052b46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b35c.md#insn-0052b46c) · [`0052b4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b35c.md#insn-0052b4c8)
- 新版 [`0054e298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md#insn-0054e298) · [`0054e304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md#insn-0054e304) · [`0054e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md#insn-0054e360)

~~~diff
- 0052b400 ["INT_ADD", "register:40f0:8", ["const:52b400:8", "const:4:8"]]
- 0052b400 ["CALL", null, ["callee:00c57a90:8"]]
+ 0054e298 ["INT_ADD", "register:40f0:8", ["const:54e298:8", "const:4:8"]]
+ 0054e298 ["CALL", null, ["callee:00c57a90:8"]]
- 0052b400 bytes 10bf1a94
+ 0054e298 bytes fe251c94
- 0052b46c ["INT_ADD", "register:40f0:8", ["const:52b46c:8", "const:4:8"]]
- 0052b46c ["CALL", null, ["callee:00c538b0:8"]]
+ 0054e304 ["INT_ADD", "register:40f0:8", ["const:54e304:8", "const:4:8"]]
+ 0054e304 ["CALL", null, ["callee:00c538b0:8"]]
- 0052b46c bytes 7dae1a94
+ 0054e304 bytes 6b151c94
- 0052b4c8 ["INT_ADD", "register:40f0:8", ["const:52b4c8:8", "const:4:8"]]
- 0052b4c8 ["CALL", null, ["callee:00c538b0:8"]]
+ 0054e360 ["INT_ADD", "register:40f0:8", ["const:54e360:8", "const:4:8"]]
+ 0054e360 ["CALL", null, ["callee:00c538b0:8"]]
- 0052b4c8 bytes 66ae1a94
+ 0054e360 bytes 54151c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b007539b722d54cdb477bbda8f918ac0"></a>

### [`0052b6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b6f8.md) → [`0054e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md) FUN_0054e590

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b35c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0054e1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b6f8.md#insn-0052b76c) · [`0052b780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b6f8.md#insn-0052b780) · [`0052b788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b6f8.md#insn-0052b788)
- 新版 [`0054e604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md#insn-0054e604) · [`0054e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md#insn-0054e618) · [`0054e620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md#insn-0054e620)

~~~diff
- 0052b76c ["INT_ADD", "register:40f0:8", ["const:52b76c:8", "const:4:8"]]
- 0052b76c ["CALL", null, ["callee:00c538e0:8"]]
+ 0054e604 ["INT_ADD", "register:40f0:8", ["const:54e604:8", "const:4:8"]]
+ 0054e604 ["CALL", null, ["callee:00c538e0:8"]]
- 0052b76c bytes c9ad1a94
+ 0054e604 bytes b7141c94
- 0052b780 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b780 ["INT_ADD", "register:40f0:8", ["const:52b780:8", "const:4:8"]]
- 0052b780 ["CALLIND", null, ["register:0:8"]]
+ 0054e618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e618 ["INT_ADD", "register:40f0:8", ["const:54e618:8", "const:4:8"]]
+ 0054e618 ["CALLIND", null, ["register:0:8"]]
- 0052b780 bytes 00013fd6
+ 0054e618 bytes 00013fd6
- 0052b788 ["INT_ADD", "register:40f0:8", ["const:52b788:8", "const:4:8"]]
- 0052b788 ["CALL", null, ["callee:00c57a80:8"]]
+ 0054e620 ["INT_ADD", "register:40f0:8", ["const:54e620:8", "const:4:8"]]
+ 0054e620 ["CALL", null, ["callee:00c57a80:8"]]
- 0052b788 bytes 2abe1a94
+ 0054e620 bytes 18251c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c1dfa0ba119a037c3645735d79c6b8"></a>

### [`0052b868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b868.md) → [`0054e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md) FUN_0054e700

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0052acbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acbc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b868.md#insn-0052b8f4) · [`0052b988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b868.md#insn-0052b988) · [`0052b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b868.md#insn-0052b99c)
- 新版 [`0054e78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md#insn-0054e78c) · [`0054e820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md#insn-0054e820) · [`0054e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md#insn-0054e834)

~~~diff
- 0052b8f4 ["INT_ADD", "register:40f0:8", ["const:52b8f4:8", "const:4:8"]]
- 0052b8f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0054e78c ["INT_ADD", "register:40f0:8", ["const:54e78c:8", "const:4:8"]]
+ 0054e78c ["CALL", null, ["callee:00c57a90:8"]]
- 0052b8f4 bytes d3bd1a94
+ 0054e78c bytes c1241c94
- 0052b988 ["INT_ADD", "register:40f0:8", ["const:52b988:8", "const:4:8"]]
- 0052b988 ["CALL", null, ["callee:00c538e0:8"]]
+ 0054e820 ["INT_ADD", "register:40f0:8", ["const:54e820:8", "const:4:8"]]
+ 0054e820 ["CALL", null, ["callee:00c538e0:8"]]
- 0052b988 bytes 42ad1a94
+ 0054e820 bytes 30141c94
- 0052b99c ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b99c ["INT_ADD", "register:40f0:8", ["const:52b99c:8", "const:4:8"]]
- 0052b99c ["CALLIND", null, ["register:0:8"]]
+ 0054e834 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e834 ["INT_ADD", "register:40f0:8", ["const:54e834:8", "const:4:8"]]
+ 0054e834 ["CALLIND", null, ["register:0:8"]]
- 0052b99c bytes 00013fd6
+ 0054e834 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7703727cd89c8dd79ce9d5370a1df64a"></a>

### [`0052b9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b9ec.md) → [`0054e884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md) FUN_0054e884

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ba5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b9ec.md#insn-0052ba5c) · [`0052ba70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b9ec.md#insn-0052ba70) · [`0052ba78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b9ec.md#insn-0052ba78)
- 新版 [`0054e8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md#insn-0054e8f4) · [`0054e908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md#insn-0054e908) · [`0054e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md#insn-0054e910)

~~~diff
- 0052ba5c ["INT_ADD", "register:40f0:8", ["const:52ba5c:8", "const:4:8"]]
- 0052ba5c ["CALL", null, ["callee:00c538e0:8"]]
+ 0054e8f4 ["INT_ADD", "register:40f0:8", ["const:54e8f4:8", "const:4:8"]]
+ 0054e8f4 ["CALL", null, ["callee:00c538e0:8"]]
- 0052ba5c bytes 0dad1a94
+ 0054e8f4 bytes fb131c94
- 0052ba70 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ba70 ["INT_ADD", "register:40f0:8", ["const:52ba70:8", "const:4:8"]]
- 0052ba70 ["CALLIND", null, ["register:0:8"]]
+ 0054e908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e908 ["INT_ADD", "register:40f0:8", ["const:54e908:8", "const:4:8"]]
+ 0054e908 ["CALLIND", null, ["register:0:8"]]
- 0052ba70 bytes 00013fd6
+ 0054e908 bytes 00013fd6
- 0052ba78 ["INT_ADD", "register:40f0:8", ["const:52ba78:8", "const:4:8"]]
- 0052ba78 ["CALL", null, ["callee:00c57a80:8"]]
+ 0054e910 ["INT_ADD", "register:40f0:8", ["const:54e910:8", "const:4:8"]]
+ 0054e910 ["CALL", null, ["callee:00c57a80:8"]]
- 0052ba78 bytes 6ebd1a94
+ 0054e910 bytes 5c241c94
~~~


<a id="compare-2136168e3a7755c4cfc930ecd4d6d3c8"></a>

### [`0052baa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052baa0.md) → [`0054e938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md) FUN_0054e938

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0051c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c938.md) [`0051c9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c9d4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`0053f86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f86c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052bb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052baa0.md#insn-0052bb48) · [`0052bc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052baa0.md#insn-0052bc54) · [`0052bcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052baa0.md#insn-0052bcac)
- 新版 [`0054e9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md#insn-0054e9e0) · [`0054eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md#insn-0054eaec) · [`0054eb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md#insn-0054eb44)

~~~diff
- 0052bb48 ["INT_ADD", "register:40f0:8", ["const:52bb48:8", "const:4:8"]]
- 0052bb48 ["CALL", null, ["callee:00c57a90:8"]]
+ 0054e9e0 ["INT_ADD", "register:40f0:8", ["const:54e9e0:8", "const:4:8"]]
+ 0054e9e0 ["CALL", null, ["callee:00c57a90:8"]]
- 0052bb48 bytes 3ebd1a94
+ 0054e9e0 bytes 2c241c94
- 0052bc54 ["INT_ADD", "register:40f0:8", ["const:52bc54:8", "const:4:8"]]
- 0052bc54 ["CALL", null, ["callee:0053f7d0:8"]]
+ 0054eaec ["INT_ADD", "register:40f0:8", ["const:54eaec:8", "const:4:8"]]
+ 0054eaec ["CALL", null, ["callee:0053f7d0:8"]]
- 0052bc54 bytes 39c3ff97
+ 0054eaec bytes 39c3ff97
- 0052bcac ["INT_ADD", "register:40f0:8", ["const:52bcac:8", "const:4:8"]]
- 0052bcac ["CALL", null, ["callee:0053f86c:8"]]
+ 0054eb44 ["INT_ADD", "register:40f0:8", ["const:54eb44:8", "const:4:8"]]
+ 0054eb44 ["CALL", null, ["callee:0053f86c:8"]]
- 0052bcac bytes 4ac3ff97
+ 0054eb44 bytes 4ac3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ec4fd0e7c606a6fc679099d3aa27719"></a>

### [`0052bcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052bcb4.md) → [`0054eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md) FUN_0054eb4c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) [`0050947c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md) [`00509f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) [`0050a538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a538.md) · 呼出先 6件 [`0051c66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c66c.md) [`0051c9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c9d4.md) [`0052aac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052aac0.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 4件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) [`0052d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d3d0.md) · 呼出先 6件 [`0053f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md) [`0053f86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f86c.md) [`0054d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d958.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052bd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052bcb4.md#insn-0052bd14) · [`0052bd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052bcb4.md#insn-0052bd74) · [`0052bde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052bcb4.md#insn-0052bde0)
- 新版 [`0054ebac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md#insn-0054ebac) · [`0054ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md#insn-0054ec0c) · [`0054ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md#insn-0054ec78)

~~~diff
- 0052bd14 ["INT_ADD", "register:40f0:8", ["const:52bd14:8", "const:4:8"]]
- 0052bd14 ["CALL", null, ["callee:00c57a90:8"]]
+ 0054ebac ["INT_ADD", "register:40f0:8", ["const:54ebac:8", "const:4:8"]]
+ 0054ebac ["CALL", null, ["callee:00c57a90:8"]]
- 0052bd14 bytes cbbc1a94
+ 0054ebac bytes b9231c94
- 0052bd74 ["INT_ADD", "register:40f0:8", ["const:52bd74:8", "const:4:8"]]
- 0052bd74 ["CALL", null, ["callee:0053f504:8"]]
+ 0054ec0c ["INT_ADD", "register:40f0:8", ["const:54ec0c:8", "const:4:8"]]
+ 0054ec0c ["CALL", null, ["callee:0053f504:8"]]
- 0052bd74 bytes 3ec2ff97
+ 0054ec0c bytes 3ec2ff97
- 0052bde0 ["INT_ADD", "register:40f0:8", ["const:52bde0:8", "const:4:8"]]
- 0052bde0 ["CALL", null, ["callee:0053f86c:8"]]
+ 0054ec78 ["INT_ADD", "register:40f0:8", ["const:54ec78:8", "const:4:8"]]
+ 0054ec78 ["CALL", null, ["callee:0053f86c:8"]]
- 0052bde0 bytes fdc2ff97
+ 0054ec78 bytes fdc2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d1dc3437a150ed8d97650d36a3e3f55"></a>

### [`0052be2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052be2c.md) → [`0054ecc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md) FUN_0054ecc4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0050936c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050936c.md) [`0052c024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c024.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) [`0054eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052beb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052be2c.md#insn-0052beb8) · [`0052bfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052be2c.md#insn-0052bfd4) · [`0052bff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052be2c.md#insn-0052bff8)
- 新版 [`0054ed50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md#insn-0054ed50) · [`0054ee6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md#insn-0054ee6c) · [`0054ee90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md#insn-0054ee90)

~~~diff
- 0052beb8 ["INT_ADD", "register:40f0:8", ["const:52beb8:8", "const:4:8"]]
- 0052beb8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0054ed50 ["INT_ADD", "register:40f0:8", ["const:54ed50:8", "const:4:8"]]
+ 0054ed50 ["CALL", null, ["callee:00c57a90:8"]]
- 0052beb8 bytes 62bc1a94
+ 0054ed50 bytes 50231c94
- 0052bfd4 ["INT_ADD", "register:40f0:8", ["const:52bfd4:8", "const:4:8"]]
- 0052bfd4 ["CALL", null, ["callee:0052c204:8"]]
+ 0054ee6c ["INT_ADD", "register:40f0:8", ["const:54ee6c:8", "const:4:8"]]
+ 0054ee6c ["CALL", null, ["callee:0052c204:8"]]
- 0052bfd4 bytes e674ff97
+ 0054ee6c bytes e674ff97
- 0052bff8 ["INT_ADD", "register:40f0:8", ["const:52bff8:8", "const:4:8"]]
- 0052bff8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054ee90 ["INT_ADD", "register:40f0:8", ["const:54ee90:8", "const:4:8"]]
+ 0054ee90 ["CALL", null, ["callee:00c57ab0:8"]]
- 0052bff8 bytes 1abc1a94
+ 0054ee90 bytes 08231c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99e3123cb41db3d034ae81011b6851b1"></a>

### [`0052c2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c2bc.md) → [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) FUN_0054f154

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) [`00565334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565334.md) [`006fc134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc134.md) · 呼出先 2件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 3件 [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) [`005881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md) [`00726234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md) · 呼出先 2件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c2bc.md#insn-0052c344) · [`0052c398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c2bc.md#insn-0052c398) · [`0052c434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c2bc.md#insn-0052c434)
- 新版 [`0054f1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md#insn-0054f1dc) · [`0054f230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md#insn-0054f230) · [`0054f2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md#insn-0054f2cc)

~~~diff
- 0052c344 ["INT_ADD", "register:40f0:8", ["const:52c344:8", "const:4:8"]]
- 0052c344 ["CALL", null, ["callee:00c57c50:8"]]
+ 0054f1dc ["INT_ADD", "register:40f0:8", ["const:54f1dc:8", "const:4:8"]]
+ 0054f1dc ["CALL", null, ["callee:00c57c50:8"]]
- 0052c344 bytes afbb1a94
+ 0054f1dc bytes 9d221c94
- 0052c398 ["INT_ADD", "register:40f0:8", ["const:52c398:8", "const:4:8"]]
- 0052c398 ["CALL", null, ["callee:00c57c50:8"]]
+ 0054f230 ["INT_ADD", "register:40f0:8", ["const:54f230:8", "const:4:8"]]
+ 0054f230 ["CALL", null, ["callee:00c57c50:8"]]
- 0052c398 bytes 9abb1a94
+ 0054f230 bytes 88221c94
- 0052c434 ["INT_ADD", "register:40f0:8", ["const:52c434:8", "const:4:8"]]
- 0052c434 ["CALL", null, ["callee:00c57c50:8"]]
+ 0054f2cc ["INT_ADD", "register:40f0:8", ["const:54f2cc:8", "const:4:8"]]
+ 0054f2cc ["CALL", null, ["callee:00c57c50:8"]]
- 0052c434 bytes 73bb1a94
+ 0054f2cc bytes 61221c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da108ba69d38f820d3db6e0ce86a10d1"></a>

### [`0052dd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd60.md) → [`00550bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md) FUN_00550bf8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0042d2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md) [`004618e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md) [`004658b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004658b8.md) [`004667c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004667c4.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md) · 呼出先 4件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 5件 [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 4件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052dd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd60.md#insn-0052dd8c) · [`0052dda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd60.md#insn-0052dda4) · [`0052ddb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd60.md#insn-0052ddb4)
- 新版 [`00550c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md#insn-00550c24) · [`00550c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md#insn-00550c3c) · [`00550c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md#insn-00550c4c)

~~~diff
- 0052dd8c ["INT_ADD", "register:40f0:8", ["const:52dd8c:8", "const:4:8"]]
- 0052dd8c ["CALL", null, ["callee:00550b64:8"]]
+ 00550c24 ["INT_ADD", "register:40f0:8", ["const:550c24:8", "const:4:8"]]
+ 00550c24 ["CALL", null, ["callee:00550b64:8"]]
- 0052dd8c bytes d0ffff97
+ 00550c24 bytes d0ffff97
- 0052dda4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052dda4 ["INT_ADD", "register:40f0:8", ["const:52dda4:8", "const:4:8"]]
- 0052dda4 ["CALLIND", null, ["register:0:8"]]
+ 00550c3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00550c3c ["INT_ADD", "register:40f0:8", ["const:550c3c:8", "const:4:8"]]
+ 00550c3c ["CALLIND", null, ["register:0:8"]]
- 0052dda4 bytes 20013fd6
+ 00550c3c bytes 20013fd6
- 0052ddb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ddb4 ["INT_ADD", "register:40f0:8", ["const:52ddb4:8", "const:4:8"]]
- 0052ddb4 ["CALLIND", null, ["register:0:8"]]
+ 00550c4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550c4c ["INT_ADD", "register:40f0:8", ["const:550c4c:8", "const:4:8"]]
+ 00550c4c ["CALLIND", null, ["register:0:8"]]
- 0052ddb4 bytes 00013fd6
+ 00550c4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d58da8dae3a5c4ad4ec01392f29ad12"></a>

### [`0052de60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de60.md) → [`00550cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md) FUN_00550cf8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004657ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004657ec.md) [`004744e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004744e8.md) [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) · 呼出先 4件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`00488684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488684.md) [`00497380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) · 呼出先 4件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052de8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de60.md#insn-0052de8c) · [`0052dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de60.md#insn-0052dea4) · [`0052deb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de60.md#insn-0052deb8)
- 新版 [`00550d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md#insn-00550d24) · [`00550d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md#insn-00550d3c) · [`00550d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md#insn-00550d50)

~~~diff
- 0052de8c ["INT_ADD", "register:40f0:8", ["const:52de8c:8", "const:4:8"]]
- 0052de8c ["CALL", null, ["callee:00550b64:8"]]
+ 00550d24 ["INT_ADD", "register:40f0:8", ["const:550d24:8", "const:4:8"]]
+ 00550d24 ["CALL", null, ["callee:00550b64:8"]]
- 0052de8c bytes 90ffff97
+ 00550d24 bytes 90ffff97
- 0052dea4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052dea4 ["INT_ADD", "register:40f0:8", ["const:52dea4:8", "const:4:8"]]
- 0052dea4 ["CALLIND", null, ["register:0:8"]]
+ 00550d3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550d3c ["INT_ADD", "register:40f0:8", ["const:550d3c:8", "const:4:8"]]
+ 00550d3c ["CALLIND", null, ["register:0:8"]]
- 0052dea4 bytes 00013fd6
+ 00550d3c bytes 00013fd6
- 0052deb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052deb8 ["INT_ADD", "register:40f0:8", ["const:52deb8:8", "const:4:8"]]
- 0052deb8 ["CALLIND", null, ["register:0:8"]]
+ 00550d50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550d50 ["INT_ADD", "register:40f0:8", ["const:550d50:8", "const:4:8"]]
+ 00550d50 ["CALLIND", null, ["register:0:8"]]
- 0052deb8 bytes 00013fd6
+ 00550d50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed461cb1e4494089d646e0199855944a"></a>

### [`0052df5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052df5c.md) → [`00550df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md) FUN_00550df4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0045e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e588.md) [`0045fc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) [`004609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md) · 呼出先 4件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 4件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052df88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052df5c.md#insn-0052df88) · [`0052dfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052df5c.md#insn-0052dfa0) · [`0052dfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052df5c.md#insn-0052dfb4)
- 新版 [`00550e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md#insn-00550e20) · [`00550e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md#insn-00550e38) · [`00550e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md#insn-00550e4c)

~~~diff
- 0052df88 ["INT_ADD", "register:40f0:8", ["const:52df88:8", "const:4:8"]]
- 0052df88 ["CALL", null, ["callee:00550b64:8"]]
+ 00550e20 ["INT_ADD", "register:40f0:8", ["const:550e20:8", "const:4:8"]]
+ 00550e20 ["CALL", null, ["callee:00550b64:8"]]
- 0052df88 bytes 51ffff97
+ 00550e20 bytes 51ffff97
- 0052dfa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052dfa0 ["INT_ADD", "register:40f0:8", ["const:52dfa0:8", "const:4:8"]]
- 0052dfa0 ["CALLIND", null, ["register:0:8"]]
+ 00550e38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550e38 ["INT_ADD", "register:40f0:8", ["const:550e38:8", "const:4:8"]]
+ 00550e38 ["CALLIND", null, ["register:0:8"]]
- 0052dfa0 bytes 00013fd6
+ 00550e38 bytes 00013fd6
- 0052dfb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052dfb4 ["INT_ADD", "register:40f0:8", ["const:52dfb4:8", "const:4:8"]]
- 0052dfb4 ["CALLIND", null, ["register:0:8"]]
+ 00550e4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550e4c ["INT_ADD", "register:40f0:8", ["const:550e4c:8", "const:4:8"]]
+ 00550e4c ["CALLIND", null, ["register:0:8"]]
- 0052dfb4 bytes 00013fd6
+ 00550e4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f46e6986184ddb14d01a6a13b7407cb"></a>

### [`0052e34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e34c.md) → [`005511e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005511e4.md) FUN_005511e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00acba3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052e368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e34c.md#insn-0052e368) · [`0052e388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e34c.md#insn-0052e388)
- 新版 [`00551200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005511e4.md#insn-00551200) · [`00551220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005511e4.md#insn-00551220)

~~~diff
- 0052e368 ["INT_ADD", "register:40f0:8", ["const:52e368:8", "const:4:8"]]
- 0052e368 ["CALL", null, ["callee:00c538e0:8"]]
+ 00551200 ["INT_ADD", "register:40f0:8", ["const:551200:8", "const:4:8"]]
+ 00551200 ["CALL", null, ["callee:00c538e0:8"]]
- 0052e368 bytes caa21a94
+ 00551200 bytes b8091c94
- 0052e388 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052e388 ["INT_ADD", "register:40f0:8", ["const:52e388:8", "const:4:8"]]
- 0052e388 ["CALLIND", null, ["register:0:8"]]
+ 00551220 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00551220 ["INT_ADD", "register:40f0:8", ["const:551220:8", "const:4:8"]]
+ 00551220 ["CALLIND", null, ["register:0:8"]]
- 0052e388 bytes 00013fd6
+ 00551220 bytes 00013fd6
~~~


<a id="compare-f42bc896a3209817c5d79a6e31f89c36"></a>

### [`0052e53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e53c.md) → [`005513d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005513d4.md) FUN_005513d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e53c.md#insn-0052e558) · [`0052e578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e53c.md#insn-0052e578)
- 新版 [`005513f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005513d4.md#insn-005513f0) · [`00551410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005513d4.md#insn-00551410)

~~~diff
- 0052e558 ["INT_ADD", "register:40f0:8", ["const:52e558:8", "const:4:8"]]
- 0052e558 ["CALL", null, ["callee:00c538e0:8"]]
+ 005513f0 ["INT_ADD", "register:40f0:8", ["const:5513f0:8", "const:4:8"]]
+ 005513f0 ["CALL", null, ["callee:00c538e0:8"]]
- 0052e558 bytes 4ea21a94
+ 005513f0 bytes 3c091c94
- 0052e578 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052e578 ["INT_ADD", "register:40f0:8", ["const:52e578:8", "const:4:8"]]
- 0052e578 ["CALLIND", null, ["register:0:8"]]
+ 00551410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00551410 ["INT_ADD", "register:40f0:8", ["const:551410:8", "const:4:8"]]
+ 00551410 ["CALLIND", null, ["register:0:8"]]
- 0052e578 bytes 00013fd6
+ 00551410 bytes 00013fd6
~~~


<a id="compare-37def81ad4ac65bc80184193f0e438c5"></a>

### [`0052efd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052efd4.md) → [`00551e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md) FUN_00551e6c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) · 呼出先 2件 [`005321d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) · 呼出先 2件 [`00555070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052efd4.md#insn-0052f00c) · [`0052f030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052efd4.md#insn-0052f030)
- 新版 [`00551ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md#insn-00551ea4) · [`00551ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md#insn-00551ec8)

~~~diff
- 0052f00c ["INT_ADD", "register:40f0:8", ["const:52f00c:8", "const:4:8"]]
- 0052f00c ["CALL", null, ["callee:00555070:8"]]
+ 00551ea4 ["INT_ADD", "register:40f0:8", ["const:551ea4:8", "const:4:8"]]
+ 00551ea4 ["CALL", null, ["callee:00555070:8"]]
- 0052f00c bytes 730c0094
+ 00551ea4 bytes 730c0094
- 0052f030 ["INT_ADD", "register:40f0:8", ["const:52f030:8", "const:4:8"]]
- 0052f030 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00551ec8 ["INT_ADD", "register:40f0:8", ["const:551ec8:8", "const:4:8"]]
+ 00551ec8 ["CALL", null, ["callee:00c57ae0:8"]]
- 0052f030 bytes 18b01a94
+ 00551ec8 bytes 06171c94
~~~


<a id="compare-0d4ec7d7919cd81195b3905f4f9353fa"></a>

### [`0053234c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053234c.md) → [`005551e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551e4.md) FUN_005551e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053234c.md#insn-00532368) · [`00532388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053234c.md#insn-00532388)
- 新版 [`00555200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551e4.md#insn-00555200) · [`00555220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551e4.md#insn-00555220)

~~~diff
- 00532368 ["INT_ADD", "register:40f0:8", ["const:532368:8", "const:4:8"]]
- 00532368 ["CALL", null, ["callee:00c538e0:8"]]
+ 00555200 ["INT_ADD", "register:40f0:8", ["const:555200:8", "const:4:8"]]
+ 00555200 ["CALL", null, ["callee:00c538e0:8"]]
- 00532368 bytes ca921a94
+ 00555200 bytes b8f91b94
- 00532388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00532388 ["INT_ADD", "register:40f0:8", ["const:532388:8", "const:4:8"]]
- 00532388 ["CALLIND", null, ["register:0:8"]]
+ 00555220 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00555220 ["INT_ADD", "register:40f0:8", ["const:555220:8", "const:4:8"]]
+ 00555220 ["CALLIND", null, ["register:0:8"]]
- 00532388 bytes 00013fd6
+ 00555220 bytes 00013fd6
~~~


<a id="compare-40d623ff7ab83ad53e618b979d466c36"></a>

### [`0053699c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/0053699c.md) → [`00559834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md) FUN_00559834

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00538370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00536a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/0053699c.md#insn-00536a1c) · [`00536a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/0053699c.md#insn-00536a4c) · [`00536a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/0053699c.md#insn-00536a60)
- 新版 [`005598b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md#insn-005598b4) · [`005598e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md#insn-005598e4) · [`005598f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md#insn-005598f8)

~~~diff
- 00536a1c ["INT_ADD", "register:40f0:8", ["const:536a1c:8", "const:4:8"]]
- 00536a1c ["CALL", null, ["callee:00c57a90:8"]]
+ 005598b4 ["INT_ADD", "register:40f0:8", ["const:5598b4:8", "const:4:8"]]
+ 005598b4 ["CALL", null, ["callee:00c57a90:8"]]
- 00536a1c bytes 89911a94
+ 005598b4 bytes 77f81b94
- 00536a4c ["INT_ADD", "register:40f0:8", ["const:536a4c:8", "const:4:8"]]
- 00536a4c ["CALL", null, ["callee:00c57c00:8"]]
+ 005598e4 ["INT_ADD", "register:40f0:8", ["const:5598e4:8", "const:4:8"]]
+ 005598e4 ["CALL", null, ["callee:00c57c00:8"]]
- 00536a4c bytes d9911a94
+ 005598e4 bytes c7f81b94
- 00536a60 ["INT_ADD", "register:40f0:8", ["const:536a60:8", "const:4:8"]]
- 00536a60 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005598f8 ["INT_ADD", "register:40f0:8", ["const:5598f8:8", "const:4:8"]]
+ 005598f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00536a60 bytes 80911a94
+ 005598f8 bytes 6ef81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55af3fac1df7c259897dd5c3fe544cda"></a>

### [`00537664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537664.md) → [`0055a4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md) FUN_0055a4fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`004450d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004450d4.md) · 呼出先 2件 [`00536a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00467f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f6c.md) · 呼出先 2件 [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005376a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537664.md#insn-005376a8) · [`005376cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537664.md#insn-005376cc)
- 新版 [`0055a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md#insn-0055a540) · [`0055a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md#insn-0055a564)

~~~diff
- 005376a8 ["INT_ADD", "register:40f0:8", ["const:5376a8:8", "const:4:8"]]
- 005376a8 ["CALL", null, ["callee:00559924:8"]]
+ 0055a540 ["INT_ADD", "register:40f0:8", ["const:55a540:8", "const:4:8"]]
+ 0055a540 ["CALL", null, ["callee:00559924:8"]]
- 005376a8 bytes f9fcff97
+ 0055a540 bytes f9fcff97
- 005376cc ["INT_ADD", "register:40f0:8", ["const:5376cc:8", "const:4:8"]]
- 005376cc ["CALL", null, ["callee:00c57ae0:8"]]
+ 0055a564 ["INT_ADD", "register:40f0:8", ["const:55a564:8", "const:4:8"]]
+ 0055a564 ["CALL", null, ["callee:00c57ae0:8"]]
- 005376cc bytes 718e1a94
+ 0055a564 bytes 5ff51b94
~~~


<a id="compare-e7ed402442059db3da1501355509774d"></a>

### [`0053777c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053777c.md) → [`0055a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a614.md) FUN_0055a614

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056de40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056de40.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00590cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590cd8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00537798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053777c.md#insn-00537798) · [`005377b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053777c.md#insn-005377b8)
- 新版 [`0055a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a614.md#insn-0055a630) · [`0055a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a614.md#insn-0055a650)

~~~diff
- 00537798 ["INT_ADD", "register:40f0:8", ["const:537798:8", "const:4:8"]]
- 00537798 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055a630 ["INT_ADD", "register:40f0:8", ["const:55a630:8", "const:4:8"]]
+ 0055a630 ["CALL", null, ["callee:00c538e0:8"]]
- 00537798 bytes be7d1a94
+ 0055a630 bytes ace41b94
- 005377b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005377b8 ["INT_ADD", "register:40f0:8", ["const:5377b8:8", "const:4:8"]]
- 005377b8 ["CALLIND", null, ["register:0:8"]]
+ 0055a650 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055a650 ["INT_ADD", "register:40f0:8", ["const:55a650:8", "const:4:8"]]
+ 0055a650 ["CALLIND", null, ["register:0:8"]]
- 005377b8 bytes 00013fd6
+ 0055a650 bytes 00013fd6
~~~


<a id="compare-0d5dfaf9fa7cc798c2601555689e3259"></a>

### [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md) → [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) FUN_0055a6b4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005325a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md) [`00537068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537068.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005380a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005380a0.md) [`00538260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538260.md) [`00538274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538274.md) [`00538288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538288.md)
- 新版 呼出元 2件 [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0055af38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md) [`0055b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md) [`0055b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md) [`0055b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005378d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md#insn-005378d4) · [`005378f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md#insn-005378f0) · [`00537900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md#insn-00537900)
- 新版 [`0055a76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md#insn-0055a76c) · [`0055a788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md#insn-0055a788) · [`0055a798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md#insn-0055a798)

~~~diff
- 005378d4 ["INT_ADD", "register:40f0:8", ["const:5378d4:8", "const:4:8"]]
- 005378d4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055a76c ["INT_ADD", "register:40f0:8", ["const:55a76c:8", "const:4:8"]]
+ 0055a76c ["CALL", null, ["callee:00c57a90:8"]]
- 005378d4 bytes db8d1a94
+ 0055a76c bytes c9f41b94
- 005378f0 ["INT_ADD", "register:40f0:8", ["const:5378f0:8", "const:4:8"]]
- 005378f0 ["CALL", null, ["callee:00c57c90:8"]]
+ 0055a788 ["INT_ADD", "register:40f0:8", ["const:55a788:8", "const:4:8"]]
+ 0055a788 ["CALL", null, ["callee:00c57c90:8"]]
- 005378f0 bytes 548e1a94
+ 0055a788 bytes 42f51b94
- 00537900 ["INT_ADD", "register:40f0:8", ["const:537900:8", "const:4:8"]]
- 00537900 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055a798 ["INT_ADD", "register:40f0:8", ["const:55a798:8", "const:4:8"]]
+ 0055a798 ["CALL", null, ["callee:00c57a90:8"]]
- 00537900 bytes d08d1a94
+ 0055a798 bytes bef41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-880e9bf47be5d88004cbafd096b09fec"></a>

### [`005380a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005380a0.md) → [`0055af38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md) FUN_0055af38

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005381cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005380a0.md#insn-005381cc) · [`00538200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005380a0.md#insn-00538200)
- 新版 [`0055b064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md#insn-0055b064) · [`0055b098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055af38.md#insn-0055b098)

~~~diff
- 005381cc ["INT_ADD", "register:40f0:8", ["const:5381cc:8", "const:4:8"]]
- 005381cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0055b064 ["INT_ADD", "register:40f0:8", ["const:55b064:8", "const:4:8"]]
+ 0055b064 ["CALL", null, ["callee:00c57ab0:8"]]
- 005381cc bytes a58b1a94
+ 0055b064 bytes 93f21b94
- 00538200 ["INT_ADD", "register:40f0:8", ["const:538200:8", "const:4:8"]]
- 00538200 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0055b098 ["INT_ADD", "register:40f0:8", ["const:55b098:8", "const:4:8"]]
+ 0055b098 ["CALL", null, ["callee:00c57ae0:8"]]
- 00538200 bytes a48b1a94
+ 0055b098 bytes 92f21b94
~~~


<a id="compare-ee7261210460af24de57bae2891221ce"></a>

### [`00538204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538204.md) → [`0055b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b09c.md) FUN_0055b09c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00538244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538204.md#insn-00538244)
- 新版 [`0055b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b09c.md#insn-0055b0dc)

~~~diff
- 00538244 ["INT_ADD", "register:40f0:8", ["const:538244:8", "const:4:8"]]
- 00538244 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0055b0dc ["INT_ADD", "register:40f0:8", ["const:55b0dc:8", "const:4:8"]]
+ 0055b0dc ["CALL", null, ["callee:00c57ab0:8"]]
- 00538244 bytes 878b1a94
+ 0055b0dc bytes 75f21b94
~~~


<a id="compare-ac74695ad5350849656442cf1a1cdbfc"></a>

### [`005384a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md) → [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) FUN_0055b340

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00538384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538384.md) [`0053940c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053940c.md) [`0053944c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053944c.md) · 呼出先 5件 [`005385e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005385e0.md) [`0056d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d080.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0055b21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md) [`0055c2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md) [`0055c2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md) · 呼出先 5件 [`0055b478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md) [`0058ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff18.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005384dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md#insn-005384dc) · [`005384fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md#insn-005384fc) · [`00538510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md#insn-00538510)
- 新版 [`0055b374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md#insn-0055b374) · [`0055b394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md#insn-0055b394) · [`0055b3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md#insn-0055b3a8)

~~~diff
- 005384dc ["INT_ADD", "register:40f0:8", ["const:5384dc:8", "const:4:8"]]
- 005384dc ["CALL", null, ["callee:0058ff18:8"]]
+ 0055b374 ["INT_ADD", "register:40f0:8", ["const:55b374:8", "const:4:8"]]
+ 0055b374 ["CALL", null, ["callee:0058ff18:8"]]
- 005384dc bytes e9d20094
+ 0055b374 bytes e9d20094
- 005384fc ["INT_ADD", "register:40f0:8", ["const:5384fc:8", "const:4:8"]]
- 005384fc ["CALL", null, ["callee:00c538e0:8"]]
+ 0055b394 ["INT_ADD", "register:40f0:8", ["const:55b394:8", "const:4:8"]]
+ 0055b394 ["CALL", null, ["callee:00c538e0:8"]]
- 005384fc bytes 657a1a94
+ 0055b394 bytes 53e11b94
- 00538510 ["COPY", "register:0:8", ["register:4040:8"]]
- 00538510 ["INT_ADD", "register:40f0:8", ["const:538510:8", "const:4:8"]]
- 00538510 ["CALLIND", null, ["register:0:8"]]
+ 0055b3a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055b3a8 ["INT_ADD", "register:40f0:8", ["const:55b3a8:8", "const:4:8"]]
+ 0055b3a8 ["CALLIND", null, ["register:0:8"]]
- 00538510 bytes 00013fd6
+ 0055b3a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58dfd8d729c9a5009bb374f9eb0d1b0e"></a>

### [`005385e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005385e0.md) → [`0055b478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md) FUN_0055b478

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005384a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md) · 呼出先 6件 [`00539804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539804.md) [`0053980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) · 呼出先 6件 [`0055c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c69c.md) [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053862c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005385e0.md#insn-0053862c) · [`0053864c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005385e0.md#insn-0053864c) · [`00538668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005385e0.md#insn-00538668)
- 新版 [`0055b4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md#insn-0055b4c4) · [`0055b4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md#insn-0055b4e4) · [`0055b500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md#insn-0055b500)

~~~diff
- 0053862c ["INT_ADD", "register:40f0:8", ["const:53862c:8", "const:4:8"]]
- 0053862c ["CALL", null, ["callee:00c538b0:8"]]
+ 0055b4c4 ["INT_ADD", "register:40f0:8", ["const:55b4c4:8", "const:4:8"]]
+ 0055b4c4 ["CALL", null, ["callee:00c538b0:8"]]
- 0053862c bytes 0d7a1a94
+ 0055b4c4 bytes fbe01b94
- 0053864c ["INT_ADD", "register:40f0:8", ["const:53864c:8", "const:4:8"]]
- 0053864c ["CALL", null, ["callee:0055c69c:8"]]
+ 0055b4e4 ["INT_ADD", "register:40f0:8", ["const:55b4e4:8", "const:4:8"]]
+ 0055b4e4 ["CALL", null, ["callee:0055c69c:8"]]
- 0053864c bytes 6e040094
+ 0055b4e4 bytes 6e040094
- 00538668 ["INT_ADD", "register:40f0:8", ["const:538668:8", "const:4:8"]]
- 00538668 ["CALL", null, ["callee:0055c6a4:8"]]
+ 0055b500 ["INT_ADD", "register:40f0:8", ["const:55b500:8", "const:4:8"]]
+ 0055b500 ["CALL", null, ["callee:0055c6a4:8"]]
- 00538668 bytes 69040094
+ 0055b500 bytes 69040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc123328ea56535ce54c0a5105dbdaac"></a>

### [`00538938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538938.md) → [`0055b7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b7d0.md) FUN_0055b7d0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053b7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b7e8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0055e680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00538958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538938.md#insn-00538958)
- 新版 [`0055b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b7d0.md#insn-0055b7f0)

~~~diff
- 00538958 ["INT_ADD", "register:40f0:8", ["const:538958:8", "const:4:8"]]
- 00538958 ["CALL", null, ["callee:0055e680:8"]]
+ 0055b7f0 ["INT_ADD", "register:40f0:8", ["const:55b7f0:8", "const:4:8"]]
+ 0055b7f0 ["CALL", null, ["callee:0055e680:8"]]
- 00538958 bytes a40b0094
+ 0055b7f0 bytes a40b0094
~~~


<a id="compare-944d1d0475ee4fdd9aeec751765ad750"></a>

### [`0053899c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/0053899c.md) → [`0055b834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b834.md) FUN_0055b834

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053b7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b7e8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0055e680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005389b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/0053899c.md#insn-005389b8)
- 新版 [`0055b850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b834.md#insn-0055b850)

~~~diff
- 005389b8 ["INT_ADD", "register:40f0:8", ["const:5389b8:8", "const:4:8"]]
- 005389b8 ["CALL", null, ["callee:0055e680:8"]]
+ 0055b850 ["INT_ADD", "register:40f0:8", ["const:55b850:8", "const:4:8"]]
+ 0055b850 ["CALL", null, ["callee:0055e680:8"]]
- 005389b8 bytes 8c0b0094
+ 0055b850 bytes 8c0b0094
~~~


<a id="compare-394ad23103277a37d12c3017812b1a47"></a>

### [`0053940c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053940c.md) → [`0055c2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md) FUN_0055c2a4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005384a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md) [`0053b74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b74c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) [`0055e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053940c.md#insn-00539428) · [`00539434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053940c.md#insn-00539434)
- 新版 [`0055c2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md#insn-0055c2c0) · [`0055c2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2a4.md#insn-0055c2cc)

~~~diff
- 00539428 ["INT_ADD", "register:40f0:8", ["const:539428:8", "const:4:8"]]
- 00539428 ["CALL", null, ["callee:0055e5e4:8"]]
+ 0055c2c0 ["INT_ADD", "register:40f0:8", ["const:55c2c0:8", "const:4:8"]]
+ 0055c2c0 ["CALL", null, ["callee:0055e5e4:8"]]
- 00539428 bytes c9080094
+ 0055c2c0 bytes c9080094
- 00539434 ["INT_ADD", "register:40f0:8", ["const:539434:8", "const:4:8"]]
- 00539434 ["CALL", null, ["callee:0055b340:8"]]
+ 0055c2cc ["INT_ADD", "register:40f0:8", ["const:55c2cc:8", "const:4:8"]]
+ 0055c2cc ["CALL", null, ["callee:0055b340:8"]]
- 00539434 bytes 1dfcff97
+ 0055c2cc bytes 1dfcff97
~~~


<a id="compare-34fcaf916eefc43687a44eb046465529"></a>

### [`0053944c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053944c.md) → [`0055c2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md) FUN_0055c2e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005384a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md) [`0053b74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b74c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) [`0055e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053944c.md#insn-00539464) · [`00539470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053944c.md#insn-00539470)
- 新版 [`0055c2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md#insn-0055c2fc) · [`0055c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c2e4.md#insn-0055c308)

~~~diff
- 00539464 ["INT_ADD", "register:40f0:8", ["const:539464:8", "const:4:8"]]
- 00539464 ["CALL", null, ["callee:0055e5e4:8"]]
+ 0055c2fc ["INT_ADD", "register:40f0:8", ["const:55c2fc:8", "const:4:8"]]
+ 0055c2fc ["CALL", null, ["callee:0055e5e4:8"]]
- 00539464 bytes ba080094
+ 0055c2fc bytes ba080094
- 00539470 ["INT_ADD", "register:40f0:8", ["const:539470:8", "const:4:8"]]
- 00539470 ["CALL", null, ["callee:0055b340:8"]]
+ 0055c308 ["INT_ADD", "register:40f0:8", ["const:55c308:8", "const:4:8"]]
+ 0055c308 ["CALL", null, ["callee:0055b340:8"]]
- 00539470 bytes 0efcff97
+ 0055c308 bytes 0efcff97
~~~


<a id="compare-eea1c6f33705ebbffb143e96c94b2bff"></a>

### [`005398ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md) → [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) FUN_0055c784

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0055c994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) · 呼出先 2件 [`00539b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b2c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`0057f82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md) [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) · 呼出先 2件 [`0055c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md#insn-00539920) · [`00539944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md#insn-00539944)
- 新版 [`0055c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md#insn-0055c7b8) · [`0055c7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md#insn-0055c7dc)

~~~diff
- 00539920 ["INT_ADD", "register:40f0:8", ["const:539920:8", "const:4:8"]]
- 00539920 ["CALL", null, ["callee:0055c9c4:8"]]
+ 0055c7b8 ["INT_ADD", "register:40f0:8", ["const:55c7b8:8", "const:4:8"]]
+ 0055c7b8 ["CALL", null, ["callee:0055c9c4:8"]]
- 00539920 bytes 83000094
+ 0055c7b8 bytes 83000094
- 00539944 ["INT_ADD", "register:40f0:8", ["const:539944:8", "const:4:8"]]
- 00539944 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0055c7dc ["INT_ADD", "register:40f0:8", ["const:55c7dc:8", "const:4:8"]]
+ 0055c7dc ["CALL", null, ["callee:00c57ae0:8"]]
- 00539944 bytes d3851a94
+ 0055c7dc bytes c1ec1b94
~~~


<a id="compare-a3957ce52b70280470700b577c2ca766"></a>

### [`005399b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md) → [`0055c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md) FUN_0055c848

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0053980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md) [`00539b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b2c.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) [`0055c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md#insn-00539a28) · [`00539a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md#insn-00539a4c) · [`00539a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md#insn-00539a78)
- 新版 [`0055c8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md#insn-0055c8c0) · [`0055c8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md#insn-0055c8e4) · [`0055c910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md#insn-0055c910)

~~~diff
- 00539a28 ["INT_ADD", "register:40f0:8", ["const:539a28:8", "const:4:8"]]
- 00539a28 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055c8c0 ["INT_ADD", "register:40f0:8", ["const:55c8c0:8", "const:4:8"]]
+ 0055c8c0 ["CALL", null, ["callee:00c57a90:8"]]
- 00539a28 bytes 86851a94
+ 0055c8c0 bytes 74ec1b94
- 00539a4c ["INT_ADD", "register:40f0:8", ["const:539a4c:8", "const:4:8"]]
- 00539a4c ["CALL", null, ["callee:00c57c90:8"]]
+ 0055c8e4 ["INT_ADD", "register:40f0:8", ["const:55c8e4:8", "const:4:8"]]
+ 0055c8e4 ["CALL", null, ["callee:00c57c90:8"]]
- 00539a4c bytes fd851a94
+ 0055c8e4 bytes ebec1b94
- 00539a78 ["INT_ADD", "register:40f0:8", ["const:539a78:8", "const:4:8"]]
- 00539a78 ["CALL", null, ["callee:00c57c90:8"]]
+ 0055c910 ["INT_ADD", "register:40f0:8", ["const:55c910:8", "const:4:8"]]
+ 0055c910 ["CALL", null, ["callee:00c57c90:8"]]
- 00539a78 bytes f2851a94
+ 0055c910 bytes e0ec1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1487498ae16fb3fd0aead4598b76bc41"></a>

### [`00539e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539e58.md) → [`0055ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ccf0.md) FUN_0055ccf0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539e58.md#insn-00539e74) · [`00539e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539e58.md#insn-00539e94)
- 新版 [`0055cd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ccf0.md#insn-0055cd0c) · [`0055cd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ccf0.md#insn-0055cd2c)

~~~diff
- 00539e74 ["INT_ADD", "register:40f0:8", ["const:539e74:8", "const:4:8"]]
- 00539e74 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055cd0c ["INT_ADD", "register:40f0:8", ["const:55cd0c:8", "const:4:8"]]
+ 0055cd0c ["CALL", null, ["callee:00c538e0:8"]]
- 00539e74 bytes 07741a94
+ 0055cd0c bytes f5da1b94
- 00539e94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00539e94 ["INT_ADD", "register:40f0:8", ["const:539e94:8", "const:4:8"]]
- 00539e94 ["CALLIND", null, ["register:0:8"]]
+ 0055cd2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055cd2c ["INT_ADD", "register:40f0:8", ["const:55cd2c:8", "const:4:8"]]
+ 0055cd2c ["CALLIND", null, ["register:0:8"]]
- 00539e94 bytes 00013fd6
+ 0055cd2c bytes 00013fd6
~~~


<a id="compare-2ed2ae1589879921522b70888b713fe5"></a>

### [`00539f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539f90.md) → [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) FUN_0055ce28

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0053a158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a158.md) [`0053a2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a2b8.md) [`0053a418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a418.md) · 呼出先 2件 [`005192a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005192a0.md) [`0053aef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aef8.md)
- 新版 呼出元 3件 [`0055cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md) [`0055d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md) [`0055d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md) · 呼出先 2件 [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`0055dd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539f90.md#insn-00539fc8) · [`0053a01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539f90.md#insn-0053a01c)
- 新版 [`0055ce60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md#insn-0055ce60) · [`0055ceb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md#insn-0055ceb4)

~~~diff
- 00539fc8 ["INT_ADD", "register:40f0:8", ["const:539fc8:8", "const:4:8"]]
- 00539fc8 ["CALL", null, ["callee:0055dd90:8"]]
+ 0055ce60 ["INT_ADD", "register:40f0:8", ["const:55ce60:8", "const:4:8"]]
+ 0055ce60 ["CALL", null, ["callee:0055dd90:8"]]
- 00539fc8 bytes cc030094
+ 0055ce60 bytes cc030094
- 0053a01c ["INT_ADD", "register:40f0:8", ["const:53a01c:8", "const:4:8"]]
- 0053a01c ["CALL", null, ["callee:0053c138:8"]]
+ 0055ceb4 ["INT_ADD", "register:40f0:8", ["const:55ceb4:8", "const:4:8"]]
+ 0055ceb4 ["CALL", null, ["callee:0053c138:8"]]
- 0053a01c bytes a17cff97
+ 0055ceb4 bytes a17cff97
~~~


<a id="compare-7ad337e3b64cc6f0bc6d2cae0a14f91e"></a>

### [`0053a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a0e0.md) → [`0055cf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md) FUN_0055cf78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00444ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444ee4.md) · 呼出先 3件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a0e0.md#insn-0053a104) · [`0053a11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a0e0.md#insn-0053a11c) · [`0053a140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a0e0.md#insn-0053a140)
- 新版 [`0055cf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md#insn-0055cf9c) · [`0055cfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md#insn-0055cfb4) · [`0055cfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md#insn-0055cfd8)

~~~diff
- 0053a104 ["INT_ADD", "register:40f0:8", ["const:53a104:8", "const:4:8"]]
- 0053a104 ["CALL", null, ["callee:00c538b0:8"]]
+ 0055cf9c ["INT_ADD", "register:40f0:8", ["const:55cf9c:8", "const:4:8"]]
+ 0055cf9c ["CALL", null, ["callee:00c538b0:8"]]
- 0053a104 bytes 57731a94
+ 0055cf9c bytes 45da1b94
- 0053a11c ["INT_ADD", "register:40f0:8", ["const:53a11c:8", "const:4:8"]]
- 0053a11c ["CALL", null, ["callee:00c538e0:8"]]
+ 0055cfb4 ["INT_ADD", "register:40f0:8", ["const:55cfb4:8", "const:4:8"]]
+ 0055cfb4 ["CALL", null, ["callee:00c538e0:8"]]
- 0053a11c bytes 5d731a94
+ 0055cfb4 bytes 4bda1b94
- 0053a140 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053a140 ["INT_ADD", "register:40f0:8", ["const:53a140:8", "const:4:8"]]
- 0053a140 ["CALLIND", null, ["register:0:8"]]
+ 0055cfd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055cfd8 ["INT_ADD", "register:40f0:8", ["const:55cfd8:8", "const:4:8"]]
+ 0055cfd8 ["CALLIND", null, ["register:0:8"]]
- 0053a140 bytes 00013fd6
+ 0055cfd8 bytes 00013fd6
~~~


<a id="compare-692d02913f3062f8d79e9b13d12b3963"></a>

### [`0053a158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a158.md) → [`0055cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md) FUN_0055cff0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00539f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539f90.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a158.md#insn-0053a1a0) · [`0053a1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a158.md#insn-0053a1c4) · [`0053a1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a158.md#insn-0053a1e8)
- 新版 [`0055d038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md#insn-0055d038) · [`0055d05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md#insn-0055d05c) · [`0055d080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cff0.md#insn-0055d080)

~~~diff
- 0053a1a0 ["INT_ADD", "register:40f0:8", ["const:53a1a0:8", "const:4:8"]]
- 0053a1a0 ["CALL", null, ["callee:0055ce28:8"]]
+ 0055d038 ["INT_ADD", "register:40f0:8", ["const:55d038:8", "const:4:8"]]
+ 0055d038 ["CALL", null, ["callee:0055ce28:8"]]
- 0053a1a0 bytes 7cffff97
+ 0055d038 bytes 7cffff97
- 0053a1c4 ["INT_ADD", "register:40f0:8", ["const:53a1c4:8", "const:4:8"]]
- 0053a1c4 ["CALL", null, ["callee:00c538b0:8"]]
+ 0055d05c ["INT_ADD", "register:40f0:8", ["const:55d05c:8", "const:4:8"]]
+ 0055d05c ["CALL", null, ["callee:00c538b0:8"]]
- 0053a1c4 bytes 27731a94
+ 0055d05c bytes 15da1b94
- 0053a1e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053a1e8 ["INT_ADD", "register:40f0:8", ["const:53a1e8:8", "const:4:8"]]
- 0053a1e8 ["CALLIND", null, ["register:0:8"]]
+ 0055d080 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d080 ["INT_ADD", "register:40f0:8", ["const:55d080:8", "const:4:8"]]
+ 0055d080 ["CALLIND", null, ["register:0:8"]]
- 0053a1e8 bytes 00013fd6
+ 0055d080 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a273a85d1a9cf6ed2bf17f802459d1c"></a>

### [`0053a268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a268.md) → [`0055d100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d100.md) FUN_0055d100

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a268.md#insn-0053a284) · [`0053a2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a268.md#insn-0053a2a4)
- 新版 [`0055d11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d100.md#insn-0055d11c) · [`0055d13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d100.md#insn-0055d13c)

~~~diff
- 0053a284 ["INT_ADD", "register:40f0:8", ["const:53a284:8", "const:4:8"]]
- 0053a284 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055d11c ["INT_ADD", "register:40f0:8", ["const:55d11c:8", "const:4:8"]]
+ 0055d11c ["CALL", null, ["callee:00c538e0:8"]]
- 0053a284 bytes 03731a94
+ 0055d11c bytes f1d91b94
- 0053a2a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053a2a4 ["INT_ADD", "register:40f0:8", ["const:53a2a4:8", "const:4:8"]]
- 0053a2a4 ["CALLIND", null, ["register:0:8"]]
+ 0055d13c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d13c ["INT_ADD", "register:40f0:8", ["const:55d13c:8", "const:4:8"]]
+ 0055d13c ["CALLIND", null, ["register:0:8"]]
- 0053a2a4 bytes 00013fd6
+ 0055d13c bytes 00013fd6
~~~


<a id="compare-d8d50c80975e1fa2510308666dbbcde8"></a>

### [`0053a2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a2b8.md) → [`0055d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md) FUN_0055d150

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00539f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539f90.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a2b8.md#insn-0053a324) · [`0053a34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a2b8.md#insn-0053a34c) · [`0053a38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a2b8.md#insn-0053a38c)
- 新版 [`0055d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md#insn-0055d1bc) · [`0055d1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md#insn-0055d1e4) · [`0055d224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d150.md#insn-0055d224)

~~~diff
- 0053a324 ["INT_ADD", "register:40f0:8", ["const:53a324:8", "const:4:8"]]
- 0053a324 ["CALL", null, ["callee:0055ce28:8"]]
+ 0055d1bc ["INT_ADD", "register:40f0:8", ["const:55d1bc:8", "const:4:8"]]
+ 0055d1bc ["CALL", null, ["callee:0055ce28:8"]]
- 0053a324 bytes 1bffff97
+ 0055d1bc bytes 1bffff97
- 0053a34c ["INT_ADD", "register:40f0:8", ["const:53a34c:8", "const:4:8"]]
- 0053a34c ["CALL", null, ["callee:00c538b0:8"]]
+ 0055d1e4 ["INT_ADD", "register:40f0:8", ["const:55d1e4:8", "const:4:8"]]
+ 0055d1e4 ["CALL", null, ["callee:00c538b0:8"]]
- 0053a34c bytes c5721a94
+ 0055d1e4 bytes b3d91b94
- 0053a38c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053a38c ["INT_ADD", "register:40f0:8", ["const:53a38c:8", "const:4:8"]]
- 0053a38c ["CALLIND", null, ["register:0:8"]]
+ 0055d224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d224 ["INT_ADD", "register:40f0:8", ["const:55d224:8", "const:4:8"]]
+ 0055d224 ["CALLIND", null, ["register:0:8"]]
- 0053a38c bytes 00013fd6
+ 0055d224 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e5e0a981d9b2a14cc1aeda878a6ce19"></a>

### [`0053a418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a418.md) → [`0055d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md) FUN_0055d2b0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00539f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539f90.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a418.md#insn-0053a458) · [`0053a47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a418.md#insn-0053a47c) · [`0053a49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a418.md#insn-0053a49c)
- 新版 [`0055d2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md#insn-0055d2f0) · [`0055d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md#insn-0055d314) · [`0055d334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d2b0.md#insn-0055d334)

~~~diff
- 0053a458 ["INT_ADD", "register:40f0:8", ["const:53a458:8", "const:4:8"]]
- 0053a458 ["CALL", null, ["callee:0055ce28:8"]]
+ 0055d2f0 ["INT_ADD", "register:40f0:8", ["const:55d2f0:8", "const:4:8"]]
+ 0055d2f0 ["CALL", null, ["callee:0055ce28:8"]]
- 0053a458 bytes cefeff97
+ 0055d2f0 bytes cefeff97
- 0053a47c ["INT_ADD", "register:40f0:8", ["const:53a47c:8", "const:4:8"]]
- 0053a47c ["CALL", null, ["callee:00c538b0:8"]]
+ 0055d314 ["INT_ADD", "register:40f0:8", ["const:55d314:8", "const:4:8"]]
+ 0055d314 ["CALL", null, ["callee:00c538b0:8"]]
- 0053a47c bytes 79721a94
+ 0055d314 bytes 67d91b94
- 0053a49c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053a49c ["INT_ADD", "register:40f0:8", ["const:53a49c:8", "const:4:8"]]
- 0053a49c ["CALLIND", null, ["register:0:8"]]
+ 0055d334 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d334 ["INT_ADD", "register:40f0:8", ["const:55d334:8", "const:4:8"]]
+ 0055d334 ["CALLIND", null, ["register:0:8"]]
- 0053a49c bytes 00013fd6
+ 0055d334 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d340e7590700cc07af396c418c1c7032"></a>

### [`0053a6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a6c0.md) → [`0055d558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d558.md) FUN_0055d558

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a6c0.md#insn-0053a6dc) · [`0053a6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a6c0.md#insn-0053a6fc)
- 新版 [`0055d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d558.md#insn-0055d574) · [`0055d594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d558.md#insn-0055d594)

~~~diff
- 0053a6dc ["INT_ADD", "register:40f0:8", ["const:53a6dc:8", "const:4:8"]]
- 0053a6dc ["CALL", null, ["callee:00c538e0:8"]]
+ 0055d574 ["INT_ADD", "register:40f0:8", ["const:55d574:8", "const:4:8"]]
+ 0055d574 ["CALL", null, ["callee:00c538e0:8"]]
- 0053a6dc bytes ed711a94
+ 0055d574 bytes dbd81b94
- 0053a6fc ["COPY", "register:0:8", ["register:4040:8"]]
- 0053a6fc ["INT_ADD", "register:40f0:8", ["const:53a6fc:8", "const:4:8"]]
- 0053a6fc ["CALLIND", null, ["register:0:8"]]
+ 0055d594 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055d594 ["INT_ADD", "register:40f0:8", ["const:55d594:8", "const:4:8"]]
+ 0055d594 ["CALLIND", null, ["register:0:8"]]
- 0053a6fc bytes 00013fd6
+ 0055d594 bytes 00013fd6
~~~


<a id="compare-8181dda8238b1b92c83b3c85d27e6afe"></a>

### [`0053ac34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac34.md) → [`0055dacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dacc.md) FUN_0055dacc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053ac50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac34.md#insn-0053ac50) · [`0053ac70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac34.md#insn-0053ac70)
- 新版 [`0055dae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dacc.md#insn-0055dae8) · [`0055db08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dacc.md#insn-0055db08)

~~~diff
- 0053ac50 ["INT_ADD", "register:40f0:8", ["const:53ac50:8", "const:4:8"]]
- 0053ac50 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055dae8 ["INT_ADD", "register:40f0:8", ["const:55dae8:8", "const:4:8"]]
+ 0055dae8 ["CALL", null, ["callee:00c538e0:8"]]
- 0053ac50 bytes 90701a94
+ 0055dae8 bytes 7ed71b94
- 0053ac70 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053ac70 ["INT_ADD", "register:40f0:8", ["const:53ac70:8", "const:4:8"]]
- 0053ac70 ["CALLIND", null, ["register:0:8"]]
+ 0055db08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055db08 ["INT_ADD", "register:40f0:8", ["const:55db08:8", "const:4:8"]]
+ 0055db08 ["CALLIND", null, ["register:0:8"]]
- 0053ac70 bytes 00013fd6
+ 0055db08 bytes 00013fd6
~~~


<a id="compare-3d2d0b6dca200bda8140d33c9fa24c45"></a>

### [`0053ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac84.md) → [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) FUN_0055db1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0053a710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a710.md) [`0053a8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a8e8.md) [`0053aac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md) · 呼出先 4件 [`0056d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d0b4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 4件 [`0058ff4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff4c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053acbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac84.md#insn-0053acbc) · [`0053acdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac84.md#insn-0053acdc) · [`0053acf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac84.md#insn-0053acf0)
- 新版 [`0055db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md#insn-0055db54) · [`0055db74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md#insn-0055db74) · [`0055db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md#insn-0055db88)

~~~diff
- 0053acbc ["INT_ADD", "register:40f0:8", ["const:53acbc:8", "const:4:8"]]
- 0053acbc ["CALL", null, ["callee:0058ff4c:8"]]
+ 0055db54 ["INT_ADD", "register:40f0:8", ["const:55db54:8", "const:4:8"]]
+ 0055db54 ["CALL", null, ["callee:0058ff4c:8"]]
- 0053acbc bytes fec80094
+ 0055db54 bytes fec80094
- 0053acdc ["INT_ADD", "register:40f0:8", ["const:53acdc:8", "const:4:8"]]
- 0053acdc ["CALL", null, ["callee:00c538e0:8"]]
+ 0055db74 ["INT_ADD", "register:40f0:8", ["const:55db74:8", "const:4:8"]]
+ 0055db74 ["CALL", null, ["callee:00c538e0:8"]]
- 0053acdc bytes 6d701a94
+ 0055db74 bytes 5bd71b94
- 0053acf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053acf0 ["INT_ADD", "register:40f0:8", ["const:53acf0:8", "const:4:8"]]
- 0053acf0 ["CALLIND", null, ["register:0:8"]]
+ 0055db88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055db88 ["INT_ADD", "register:40f0:8", ["const:55db88:8", "const:4:8"]]
+ 0055db88 ["CALLIND", null, ["register:0:8"]]
- 0053acf0 bytes 00013fd6
+ 0055db88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce427e1d77dfd2675f0a5dd6b2db9e66"></a>

### [`0053aef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aef8.md) → [`0055dd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md) FUN_0055dd90

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00539f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539f90.md) · 呼出先 5件 [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) · 呼出先 5件 [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053af3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aef8.md#insn-0053af3c) · [`0053af84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aef8.md#insn-0053af84) · [`0053afac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aef8.md#insn-0053afac)
- 新版 [`0055ddd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md#insn-0055ddd4) · [`0055de1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md#insn-0055de1c) · [`0055de44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dd90.md#insn-0055de44)

~~~diff
- 0053af3c ["INT_ADD", "register:40f0:8", ["const:53af3c:8", "const:4:8"]]
- 0053af3c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0055ddd4 ["INT_ADD", "register:40f0:8", ["const:55ddd4:8", "const:4:8"]]
+ 0055ddd4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053af3c bytes 49801a94
+ 0055ddd4 bytes 37e71b94
- 0053af84 ["INT_ADD", "register:40f0:8", ["const:53af84:8", "const:4:8"]]
- 0053af84 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055de1c ["INT_ADD", "register:40f0:8", ["const:55de1c:8", "const:4:8"]]
+ 0055de1c ["CALL", null, ["callee:00c57a90:8"]]
- 0053af84 bytes 2f801a94
+ 0055de1c bytes 1de71b94
- 0053afac ["INT_ADD", "register:40f0:8", ["const:53afac:8", "const:4:8"]]
- 0053afac ["CALL", null, ["callee:00c57c00:8"]]
+ 0055de44 ["INT_ADD", "register:40f0:8", ["const:55de44:8", "const:4:8"]]
+ 0055de44 ["CALL", null, ["callee:00c57c00:8"]]
- 0053afac bytes 81801a94
+ 0055de44 bytes 6fe71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0ee6e610e4fcf14f491c3667c11fd9"></a>

### [`0053b028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b028.md) → [`0055dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md) FUN_0055dec0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053a5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0055d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b028.md#insn-0053b09c) · [`0053b114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b028.md#insn-0053b114) · [`0053b154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b028.md#insn-0053b154)
- 新版 [`0055df34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md#insn-0055df34) · [`0055dfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md#insn-0055dfac) · [`0055dfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md#insn-0055dfec)

~~~diff
- 0053b09c ["INT_ADD", "register:40f0:8", ["const:53b09c:8", "const:4:8"]]
- 0053b09c ["CALL", null, ["callee:00c57a90:8"]]
+ 0055df34 ["INT_ADD", "register:40f0:8", ["const:55df34:8", "const:4:8"]]
+ 0055df34 ["CALL", null, ["callee:00c57a90:8"]]
- 0053b09c bytes e97f1a94
+ 0055df34 bytes d7e61b94
- 0053b114 ["INT_ADD", "register:40f0:8", ["const:53b114:8", "const:4:8"]]
- 0053b114 ["CALL", null, ["callee:00c57c00:8"]]
+ 0055dfac ["INT_ADD", "register:40f0:8", ["const:55dfac:8", "const:4:8"]]
+ 0055dfac ["CALL", null, ["callee:00c57c00:8"]]
- 0053b114 bytes 27801a94
+ 0055dfac bytes 15e71b94
- 0053b154 ["INT_ADD", "register:40f0:8", ["const:53b154:8", "const:4:8"]]
- 0053b154 ["CALL", null, ["callee:0046c40c:8"]]
+ 0055dfec ["INT_ADD", "register:40f0:8", ["const:55dfec:8", "const:4:8"]]
+ 0055dfec ["CALL", null, ["callee:0046c40c:8"]]
- 0053b154 bytes 0839fc97
+ 0055dfec bytes 0839fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe99c5f0611bf84b70779c14cd1ab89b"></a>

### [`0053b15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b15c.md) → [`0055dff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md) FUN_0055dff4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00539ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539ea8.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0055cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cd40.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b15c.md#insn-0053b1e0) · [`0053b218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b15c.md#insn-0053b218) · [`0053b280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b15c.md#insn-0053b280)
- 新版 [`0055e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md#insn-0055e078) · [`0055e0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md#insn-0055e0b0) · [`0055e118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dff4.md#insn-0055e118)

~~~diff
- 0053b1e0 ["INT_ADD", "register:40f0:8", ["const:53b1e0:8", "const:4:8"]]
- 0053b1e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055e078 ["INT_ADD", "register:40f0:8", ["const:55e078:8", "const:4:8"]]
+ 0055e078 ["CALL", null, ["callee:00c57a90:8"]]
- 0053b1e0 bytes 987f1a94
+ 0055e078 bytes 86e61b94
- 0053b218 ["INT_ADD", "register:40f0:8", ["const:53b218:8", "const:4:8"]]
- 0053b218 ["CALL", null, ["callee:00c57b40:8"]]
+ 0055e0b0 ["INT_ADD", "register:40f0:8", ["const:55e0b0:8", "const:4:8"]]
+ 0055e0b0 ["CALL", null, ["callee:00c57b40:8"]]
- 0053b218 bytes b67f1a94
+ 0055e0b0 bytes a4e61b94
- 0053b280 ["INT_ADD", "register:40f0:8", ["const:53b280:8", "const:4:8"]]
- 0053b280 ["CALL", null, ["callee:00c57b40:8"]]
+ 0055e118 ["INT_ADD", "register:40f0:8", ["const:55e118:8", "const:4:8"]]
+ 0055e118 ["CALL", null, ["callee:00c57b40:8"]]
- 0053b280 bytes 9c7f1a94
+ 0055e118 bytes 8ae61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f22047ea1960ea2e69cf3651bf222f2"></a>

### [`0053b340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b340.md) → [`0055e1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md) FUN_0055e1d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00539ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539ea8.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0055cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cd40.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b340.md#insn-0053b3c8) · [`0053b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b340.md#insn-0053b404) · [`0053b48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b340.md#insn-0053b48c)
- 新版 [`0055e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md#insn-0055e260) · [`0055e29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md#insn-0055e29c) · [`0055e324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e1d8.md#insn-0055e324)

~~~diff
- 0053b3c8 ["INT_ADD", "register:40f0:8", ["const:53b3c8:8", "const:4:8"]]
- 0053b3c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055e260 ["INT_ADD", "register:40f0:8", ["const:55e260:8", "const:4:8"]]
+ 0055e260 ["CALL", null, ["callee:00c57a90:8"]]
- 0053b3c8 bytes 1e7f1a94
+ 0055e260 bytes 0ce61b94
- 0053b404 ["INT_ADD", "register:40f0:8", ["const:53b404:8", "const:4:8"]]
- 0053b404 ["CALL", null, ["callee:00c57b40:8"]]
+ 0055e29c ["INT_ADD", "register:40f0:8", ["const:55e29c:8", "const:4:8"]]
+ 0055e29c ["CALL", null, ["callee:00c57b40:8"]]
- 0053b404 bytes 3b7f1a94
+ 0055e29c bytes 29e61b94
- 0053b48c ["INT_ADD", "register:40f0:8", ["const:53b48c:8", "const:4:8"]]
- 0053b48c ["CALL", null, ["callee:00c57c00:8"]]
+ 0055e324 ["INT_ADD", "register:40f0:8", ["const:55e324:8", "const:4:8"]]
+ 0055e324 ["CALL", null, ["callee:00c57c00:8"]]
- 0053b48c bytes 497f1a94
+ 0055e324 bytes 37e61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a05024dae553ea47a434f8b81091ca83"></a>

### [`0053b81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b81c.md) → [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) FUN_0055e6b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0053a710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a710.md) [`0053a8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a8e8.md) [`0053aac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md) · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b81c.md#insn-0053b840) · [`0053b860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b81c.md#insn-0053b860)
- 新版 [`0055e6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md#insn-0055e6d8) · [`0055e6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md#insn-0055e6f8)

~~~diff
- 0053b840 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053b840 ["INT_ADD", "register:40f0:8", ["const:53b840:8", "const:4:8"]]
- 0053b840 ["CALLIND", null, ["register:0:8"]]
+ 0055e6d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055e6d8 ["INT_ADD", "register:40f0:8", ["const:55e6d8:8", "const:4:8"]]
+ 0055e6d8 ["CALLIND", null, ["register:0:8"]]
- 0053b840 bytes 00013fd6
+ 0055e6d8 bytes 00013fd6
- 0053b860 ["INT_ADD", "register:40f0:8", ["const:53b860:8", "const:4:8"]]
- 0053b860 ["CALL", null, ["callee:00c538b0:8"]]
+ 0055e6f8 ["INT_ADD", "register:40f0:8", ["const:55e6f8:8", "const:4:8"]]
+ 0055e6f8 ["CALL", null, ["callee:00c538b0:8"]]
- 0053b860 bytes 806d1a94
+ 0055e6f8 bytes 6ed41b94
~~~


<a id="compare-58a37b5f7a733c26ecc83681f95dd824"></a>

### [`0053b878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b878.md) → [`0055e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md) FUN_0055e710

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046a498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a498.md) · 呼出先 4件 [`0055eb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0048d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d330.md) · 呼出先 4件 [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b878.md#insn-0053b8a8) · [`0053b8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b878.md#insn-0053b8c4) · [`0053b8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b878.md#insn-0053b8d8)
- 新版 [`0055e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md#insn-0055e740) · [`0055e75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md#insn-0055e75c) · [`0055e770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md#insn-0055e770)

~~~diff
- 0053b8a8 ["INT_ADD", "register:40f0:8", ["const:53b8a8:8", "const:4:8"]]
- 0053b8a8 ["CALL", null, ["callee:005819f4:8"]]
+ 0055e740 ["INT_ADD", "register:40f0:8", ["const:55e740:8", "const:4:8"]]
+ 0055e740 ["CALL", null, ["callee:005819f4:8"]]
- 0053b8a8 bytes ad8c0094
+ 0055e740 bytes ad8c0094
- 0053b8c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0053b8c4 ["INT_ADD", "register:40f0:8", ["const:53b8c4:8", "const:4:8"]]
- 0053b8c4 ["CALLIND", null, ["register:0:8"]]
+ 0055e75c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055e75c ["INT_ADD", "register:40f0:8", ["const:55e75c:8", "const:4:8"]]
+ 0055e75c ["CALLIND", null, ["register:0:8"]]
- 0053b8c4 bytes 20013fd6
+ 0055e75c bytes 20013fd6
- 0053b8d8 ["INT_ADD", "register:40f0:8", ["const:53b8d8:8", "const:4:8"]]
- 0053b8d8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055e770 ["INT_ADD", "register:40f0:8", ["const:55e770:8", "const:4:8"]]
+ 0055e770 ["CALL", null, ["callee:00c538e0:8"]]
- 0053b8d8 bytes 6e6d1a94
+ 0055e770 bytes 5cd41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-563425b81ee8e1349a98828ae243a923"></a>

### [`0053b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b99c.md) → [`0055e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md) FUN_0055e834

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00442a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md) [`0046a3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3e4.md) [`005891dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a2e0.md) · 呼出先 4件 [`0055eb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) [`0048d27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d27c.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 4件 [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b99c.md#insn-0053b9d8) · [`0053b9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b99c.md#insn-0053b9e8) · [`0053ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b99c.md#insn-0053ba04)
- 新版 [`0055e870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md#insn-0055e870) · [`0055e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md#insn-0055e880) · [`0055e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md#insn-0055e89c)

~~~diff
- 0053b9d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053b9d8 ["INT_ADD", "register:40f0:8", ["const:53b9d8:8", "const:4:8"]]
- 0053b9d8 ["CALLIND", null, ["register:0:8"]]
+ 0055e870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055e870 ["INT_ADD", "register:40f0:8", ["const:55e870:8", "const:4:8"]]
+ 0055e870 ["CALLIND", null, ["register:0:8"]]
- 0053b9d8 bytes 00013fd6
+ 0055e870 bytes 00013fd6
- 0053b9e8 ["INT_ADD", "register:40f0:8", ["const:53b9e8:8", "const:4:8"]]
- 0053b9e8 ["CALL", null, ["callee:005819f4:8"]]
+ 0055e880 ["INT_ADD", "register:40f0:8", ["const:55e880:8", "const:4:8"]]
+ 0055e880 ["CALL", null, ["callee:005819f4:8"]]
- 0053b9e8 bytes 5d8c0094
+ 0055e880 bytes 5d8c0094
- 0053ba04 ["COPY", "register:0:8", ["register:4048:8"]]
- 0053ba04 ["INT_ADD", "register:40f0:8", ["const:53ba04:8", "const:4:8"]]
- 0053ba04 ["CALLIND", null, ["register:0:8"]]
+ 0055e89c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055e89c ["INT_ADD", "register:40f0:8", ["const:55e89c:8", "const:4:8"]]
+ 0055e89c ["CALLIND", null, ["register:0:8"]]
- 0053ba04 bytes 20013fd6
+ 0055e89c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8613ca5d47339610e0d04581af2668be"></a>

### [`0053baf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md) → [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md) FUN_0055e988

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0073addc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073addc.md) [`0073b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 4件 [`0055ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`007650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007650e8.md) [`007656e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053bb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md#insn-0053bb3c) · [`0053bb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md#insn-0053bb58) · [`0053bb6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md#insn-0053bb6c)
- 新版 [`0055e9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md#insn-0055e9d4) · [`0055e9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md#insn-0055e9f0) · [`0055ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md#insn-0055ea04)

~~~diff
- 0053bb3c ["INT_ADD", "register:40f0:8", ["const:53bb3c:8", "const:4:8"]]
- 0053bb3c ["CALL", null, ["callee:00581a68:8"]]
+ 0055e9d4 ["INT_ADD", "register:40f0:8", ["const:55e9d4:8", "const:4:8"]]
+ 0055e9d4 ["CALL", null, ["callee:00581a68:8"]]
- 0053bb3c bytes 258c0094
+ 0055e9d4 bytes 258c0094
- 0053bb58 ["COPY", "register:0:8", ["register:4048:8"]]
- 0053bb58 ["INT_ADD", "register:40f0:8", ["const:53bb58:8", "const:4:8"]]
- 0053bb58 ["CALLIND", null, ["register:0:8"]]
+ 0055e9f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055e9f0 ["INT_ADD", "register:40f0:8", ["const:55e9f0:8", "const:4:8"]]
+ 0055e9f0 ["CALLIND", null, ["register:0:8"]]
- 0053bb58 bytes 20013fd6
+ 0055e9f0 bytes 20013fd6
- 0053bb6c ["INT_ADD", "register:40f0:8", ["const:53bb6c:8", "const:4:8"]]
- 0053bb6c ["CALL", null, ["callee:00c538e0:8"]]
+ 0055ea04 ["INT_ADD", "register:40f0:8", ["const:55ea04:8", "const:4:8"]]
+ 0055ea04 ["CALL", null, ["callee:00c538e0:8"]]
- 0053bb6c bytes c96c1a94
+ 0055ea04 bytes b7d31b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bfdbd4eba1a8572b28c8f235963728d"></a>

### [`0053bc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bc44.md) → [`0055eadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md) FUN_0055eadc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0042d084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d084.md) · 呼出先 4件 [`0055ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0044ff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044ff1c.md) · 呼出先 4件 [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053bc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bc44.md#insn-0053bc88) · [`0053bc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bc44.md#insn-0053bc9c) · [`0053bcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bc44.md#insn-0053bcb8)
- 新版 [`0055eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md#insn-0055eb20) · [`0055eb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md#insn-0055eb34) · [`0055eb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md#insn-0055eb50)

~~~diff
- 0053bc88 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053bc88 ["INT_ADD", "register:40f0:8", ["const:53bc88:8", "const:4:8"]]
- 0053bc88 ["CALLIND", null, ["register:0:8"]]
+ 0055eb20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055eb20 ["INT_ADD", "register:40f0:8", ["const:55eb20:8", "const:4:8"]]
+ 0055eb20 ["CALLIND", null, ["register:0:8"]]
- 0053bc88 bytes 00013fd6
+ 0055eb20 bytes 00013fd6
- 0053bc9c ["INT_ADD", "register:40f0:8", ["const:53bc9c:8", "const:4:8"]]
- 0053bc9c ["CALL", null, ["callee:00581a68:8"]]
+ 0055eb34 ["INT_ADD", "register:40f0:8", ["const:55eb34:8", "const:4:8"]]
+ 0055eb34 ["CALL", null, ["callee:00581a68:8"]]
- 0053bc9c bytes cd8b0094
+ 0055eb34 bytes cd8b0094
- 0053bcb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0053bcb8 ["INT_ADD", "register:40f0:8", ["const:53bcb8:8", "const:4:8"]]
- 0053bcb8 ["CALLIND", null, ["register:0:8"]]
+ 0055eb50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055eb50 ["INT_ADD", "register:40f0:8", ["const:55eb50:8", "const:4:8"]]
+ 0055eb50 ["CALLIND", null, ["register:0:8"]]
- 0053bcb8 bytes 20013fd6
+ 0055eb50 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dfa7668a6df5504f247c7e5ee8f22cb"></a>

### [`0053be08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be08.md) → [`0055eca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eca0.md) FUN_0055eca0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053be24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be08.md#insn-0053be24)
- 新版 [`0055ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eca0.md#insn-0055ecbc)

~~~diff
- 0053be24 ["INT_ADD", "register:40f0:8", ["const:53be24:8", "const:4:8"]]
- 0053be24 ["CALL", null, ["callee:00c538b0:8"]]
+ 0055ecbc ["INT_ADD", "register:40f0:8", ["const:55ecbc:8", "const:4:8"]]
+ 0055ecbc ["CALL", null, ["callee:00c538b0:8"]]
- 0053be24 bytes 0f6c1a94
+ 0055ecbc bytes fdd21b94
~~~


<a id="compare-003c0d50ad1d5bb47a6494b1339a62a1"></a>

### [`0053c1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1c0.md) → [`0055f058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md) FUN_0055f058

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0046a944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a944.md) [`0046aa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046aa44.md) · 呼出先 5件 [`0055e88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md) [`00574740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574740.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`0048d7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d7dc.md) [`0048d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d8dc.md) · 呼出先 5件 [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053c208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1c0.md#insn-0053c208) · [`0053c220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1c0.md#insn-0053c220) · [`0053c23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1c0.md#insn-0053c23c)
- 新版 [`0055f0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md#insn-0055f0a0) · [`0055f0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md#insn-0055f0b8) · [`0055f0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md#insn-0055f0d4)

~~~diff
- 0053c208 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053c208 ["INT_ADD", "register:40f0:8", ["const:53c208:8", "const:4:8"]]
- 0053c208 ["CALLIND", null, ["register:0:8"]]
+ 0055f0a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055f0a0 ["INT_ADD", "register:40f0:8", ["const:55f0a0:8", "const:4:8"]]
+ 0055f0a0 ["CALLIND", null, ["register:0:8"]]
- 0053c208 bytes 00013fd6
+ 0055f0a0 bytes 00013fd6
- 0053c220 ["INT_ADD", "register:40f0:8", ["const:53c220:8", "const:4:8"]]
- 0053c220 ["CALL", null, ["callee:00581724:8"]]
+ 0055f0b8 ["INT_ADD", "register:40f0:8", ["const:55f0b8:8", "const:4:8"]]
+ 0055f0b8 ["CALL", null, ["callee:00581724:8"]]
- 0053c220 bytes 9b890094
+ 0055f0b8 bytes 9b890094
- 0053c23c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053c23c ["INT_ADD", "register:40f0:8", ["const:53c23c:8", "const:4:8"]]
- 0053c23c ["CALLIND", null, ["register:0:8"]]
+ 0055f0d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055f0d4 ["INT_ADD", "register:40f0:8", ["const:55f0d4:8", "const:4:8"]]
+ 0055f0d4 ["CALLIND", null, ["register:0:8"]]
- 0053c23c bytes 20013fd6
+ 0055f0d4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d5fb7a1428a0021535e27a259ff319"></a>

### [`0053cfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cfe4.md) → [`0055fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md) FUN_0055fe7c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053d694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d694.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056052c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cfe4.md#insn-0053d018) · [`0053d03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cfe4.md#insn-0053d03c)
- 新版 [`0055feb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md#insn-0055feb0) · [`0055fed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md#insn-0055fed4)

~~~diff
- 0053d018 ["INT_ADD", "register:40f0:8", ["const:53d018:8", "const:4:8"]]
- 0053d018 ["CALL", null, ["callee:0056052c:8"]]
+ 0055feb0 ["INT_ADD", "register:40f0:8", ["const:55feb0:8", "const:4:8"]]
+ 0055feb0 ["CALL", null, ["callee:0056052c:8"]]
- 0053d018 bytes 9f010094
+ 0055feb0 bytes 9f010094
- 0053d03c ["INT_ADD", "register:40f0:8", ["const:53d03c:8", "const:4:8"]]
- 0053d03c ["CALL", null, ["callee:00c57ae0:8"]]
+ 0055fed4 ["INT_ADD", "register:40f0:8", ["const:55fed4:8", "const:4:8"]]
+ 0055fed4 ["CALL", null, ["callee:00c57ae0:8"]]
- 0053d03c bytes 15781a94
+ 0055fed4 bytes 03df1b94
~~~


<a id="compare-6117c239da71949caa08ba81b286746b"></a>

### [`0053d590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d590.md) → [`00560428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md) FUN_00560428

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0053c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md) [`0053c740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) [`0055f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d590.md#insn-0053d5ac) · [`0053d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d590.md#insn-0053d5cc)
- 新版 [`00560444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md#insn-00560444) · [`00560464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md#insn-00560464)

~~~diff
- 0053d5ac ["INT_ADD", "register:40f0:8", ["const:53d5ac:8", "const:4:8"]]
- 0053d5ac ["CALL", null, ["callee:00c538e0:8"]]
+ 00560444 ["INT_ADD", "register:40f0:8", ["const:560444:8", "const:4:8"]]
+ 00560444 ["CALL", null, ["callee:00c538e0:8"]]
- 0053d5ac bytes 39661a94
+ 00560444 bytes 27cd1b94
- 0053d5cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0053d5cc ["INT_ADD", "register:40f0:8", ["const:53d5cc:8", "const:4:8"]]
- 0053d5cc ["CALLIND", null, ["register:0:8"]]
+ 00560464 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560464 ["INT_ADD", "register:40f0:8", ["const:560464:8", "const:4:8"]]
+ 00560464 ["CALLIND", null, ["register:0:8"]]
- 0053d5cc bytes 00013fd6
+ 00560464 bytes 00013fd6
~~~


<a id="compare-ba11d484ba374b9785d33e2f328bafc0"></a>

### [`0053d694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d694.md) → [`0056052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056052c.md) FUN_0056052c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053cfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cfe4.md) · 呼出先 1件 [`00bdd190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd190.md)
- 新版 呼出元 1件 [`0055fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fe7c.md) · 呼出先 1件 [`00c59be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d694.md#insn-0053d828)
- 新版 [`005606c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056052c.md#insn-005606c0)

~~~diff
- 0053d828 ["INT_ADD", "register:40f0:8", ["const:53d828:8", "const:4:8"]]
- 0053d828 ["CALL", null, ["callee:00c59be0:8"]]
+ 005606c0 ["INT_ADD", "register:40f0:8", ["const:5606c0:8", "const:4:8"]]
+ 005606c0 ["CALL", null, ["callee:00c59be0:8"]]
- 0053d828 bytes 5a7e1a94
+ 005606c0 bytes 48e51b94
~~~


<a id="compare-f8f6c6537e4015d6bf5c0be6a9f74add"></a>

### [`0053dc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc30.md) → [`00560ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md) FUN_00560ac8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) · 呼出先 2件 [`0053e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e008.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) · 呼出先 2件 [`00560ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053dc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc30.md#insn-0053dc50) · [`0053dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc30.md#insn-0053dc60)
- 新版 [`00560ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md#insn-00560ae8) · [`00560af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md#insn-00560af8)

~~~diff
- 0053dc50 ["INT_ADD", "register:40f0:8", ["const:53dc50:8", "const:4:8"]]
- 0053dc50 ["CALL", null, ["callee:00c57a90:8"]]
+ 00560ae8 ["INT_ADD", "register:40f0:8", ["const:560ae8:8", "const:4:8"]]
+ 00560ae8 ["CALL", null, ["callee:00c57a90:8"]]
- 0053dc50 bytes fc741a94
+ 00560ae8 bytes eadb1b94
- 0053dc60 ["INT_ADD", "register:40f0:8", ["const:53dc60:8", "const:4:8"]]
- 0053dc60 ["CALL", null, ["callee:00560ea0:8"]]
+ 00560af8 ["INT_ADD", "register:40f0:8", ["const:560af8:8", "const:4:8"]]
+ 00560af8 ["CALL", null, ["callee:00560ea0:8"]]
- 0053dc60 bytes ea000094
+ 00560af8 bytes ea000094
~~~


<a id="compare-a3ff5885137ed292a7bcf5dfa41b86d2"></a>

### [`0053df70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053df70.md) → [`00560e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e08.md) FUN_00560e08

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053d9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d9cc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00560864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053dfac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053df70.md#insn-0053dfac)
- 新版 [`00560e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e08.md#insn-00560e44)

~~~diff
- 0053dfac ["COPY", "register:0:8", ["register:4040:8"]]
- 0053dfac ["INT_ADD", "register:40f0:8", ["const:53dfac:8", "const:4:8"]]
- 0053dfac ["CALLIND", null, ["register:0:8"]]
+ 00560e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560e44 ["INT_ADD", "register:40f0:8", ["const:560e44:8", "const:4:8"]]
+ 00560e44 ["CALLIND", null, ["register:0:8"]]
- 0053dfac bytes 00013fd6
+ 00560e44 bytes 00013fd6
~~~


<a id="compare-101b3853db9e8f256a6715d077cf7984"></a>

### [`0053dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dfc0.md) → [`00560e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e58.md) FUN_00560e58

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053dfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dfc0.md#insn-0053dfdc)
- 新版 [`00560e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e58.md#insn-00560e74)

~~~diff
- 0053dfdc ["INT_ADD", "register:40f0:8", ["const:53dfdc:8", "const:4:8"]]
- 0053dfdc ["CALL", null, ["callee:00459d34:8"]]
+ 00560e74 ["INT_ADD", "register:40f0:8", ["const:560e74:8", "const:4:8"]]
+ 00560e74 ["CALL", null, ["callee:00459d34:8"]]
- 0053dfdc bytes b0e3fb97
+ 00560e74 bytes b0e3fb97
~~~


<a id="compare-b107d657fac1e4d5ed44db8b7c456a5b"></a>

### [`0053e13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e13c.md) → [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) FUN_00560fd4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) · 呼出先 2件 [`0053feb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md) [`005400f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005400f0.md)
- 新版 呼出元 1件 [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 2件 [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) [`00562f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053e15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e13c.md#insn-0053e15c) · [`0053e170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e13c.md#insn-0053e170)
- 新版 [`00560ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md#insn-00560ff4) · [`00561008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md#insn-00561008)

~~~diff
- 0053e15c ["INT_ADD", "register:40f0:8", ["const:53e15c:8", "const:4:8"]]
- 0053e15c ["CALL", null, ["callee:00562f88:8"]]
+ 00560ff4 ["INT_ADD", "register:40f0:8", ["const:560ff4:8", "const:4:8"]]
+ 00560ff4 ["CALL", null, ["callee:00562f88:8"]]
- 0053e15c bytes e5070094
+ 00560ff4 bytes e5070094
- 0053e170 ["INT_ADD", "register:40f0:8", ["const:53e170:8", "const:4:8"]]
- 0053e170 ["CALL", null, ["callee:00562d50:8"]]
+ 00561008 ["INT_ADD", "register:40f0:8", ["const:561008:8", "const:4:8"]]
+ 00561008 ["CALL", null, ["callee:00562d50:8"]]
- 0053e170 bytes 52070094
+ 00561008 bytes 52070094
~~~


<a id="compare-a56127436f49f15e0b4c6970b5aeb4fb"></a>

### [`0053e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e18c.md) → [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) FUN_00561024

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) · 呼出先 2件 [`005401c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md) [`00540408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540408.md)
- 新版 呼出元 2件 [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 2件 [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) [`005632a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053e1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e18c.md#insn-0053e1ac) · [`0053e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e18c.md#insn-0053e1c0)
- 新版 [`00561044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md#insn-00561044) · [`00561058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md#insn-00561058)

~~~diff
- 0053e1ac ["INT_ADD", "register:40f0:8", ["const:53e1ac:8", "const:4:8"]]
- 0053e1ac ["CALL", null, ["callee:005632a0:8"]]
+ 00561044 ["INT_ADD", "register:40f0:8", ["const:561044:8", "const:4:8"]]
+ 00561044 ["CALL", null, ["callee:005632a0:8"]]
- 0053e1ac bytes 97080094
+ 00561044 bytes 97080094
- 0053e1c0 ["INT_ADD", "register:40f0:8", ["const:53e1c0:8", "const:4:8"]]
- 0053e1c0 ["CALL", null, ["callee:00563058:8"]]
+ 00561058 ["INT_ADD", "register:40f0:8", ["const:561058:8", "const:4:8"]]
+ 00561058 ["CALL", null, ["callee:00563058:8"]]
- 0053e1c0 bytes 00080094
+ 00561058 bytes 00080094
~~~


<a id="compare-65c44dc17ff484d462903941d7fddc83"></a>

### [`0053f0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0b4.md) → [`00561f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f4c.md) FUN_00561f4c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0b4.md#insn-0053f0d0)
- 新版 [`00561f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f4c.md#insn-00561f68)

~~~diff
- 0053f0d0 ["INT_ADD", "register:40f0:8", ["const:53f0d0:8", "const:4:8"]]
- 0053f0d0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00561f68 ["INT_ADD", "register:40f0:8", ["const:561f68:8", "const:4:8"]]
+ 00561f68 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053f0d0 bytes e46f1a94
+ 00561f68 bytes d2d61b94
~~~


<a id="compare-1fe72f17acd95ce41430a1860c11846a"></a>

### [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) → [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) FUN_005626b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`0053f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md) [`005409c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409c4.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`00625684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00625/00625684.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 20件 [`00561f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md) [`0056385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md) [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006d0264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0264.md) · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md#insn-0053f8fc) · [`0053f910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md#insn-0053f910) · [`0053f9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md#insn-0053f9ac)
- 新版 [`00562794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md#insn-00562794) · [`005627a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md#insn-005627a8) · [`00562844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md#insn-00562844)

~~~diff
- 0053f8fc ["INT_ADD", "register:40f0:8", ["const:53f8fc:8", "const:4:8"]]
- 0053f8fc ["CALL", null, ["callee:00c57bd0:8"]]
+ 00562794 ["INT_ADD", "register:40f0:8", ["const:562794:8", "const:4:8"]]
+ 00562794 ["CALL", null, ["callee:00c57bd0:8"]]
- 0053f8fc bytes 216e1a94
+ 00562794 bytes 0fd51b94
- 0053f910 ["INT_ADD", "register:40f0:8", ["const:53f910:8", "const:4:8"]]
- 0053f910 ["CALL", null, ["callee:00c57c50:8"]]
+ 005627a8 ["INT_ADD", "register:40f0:8", ["const:5627a8:8", "const:4:8"]]
+ 005627a8 ["CALL", null, ["callee:00c57c50:8"]]
- 0053f910 bytes 3c6e1a94
+ 005627a8 bytes 2ad51b94
- 0053f9ac ["INT_ADD", "register:40f0:8", ["const:53f9ac:8", "const:4:8"]]
- 0053f9ac ["CALL", null, ["callee:00c57a90:8"]]
+ 00562844 ["INT_ADD", "register:40f0:8", ["const:562844:8", "const:4:8"]]
+ 00562844 ["CALL", null, ["callee:00c57a90:8"]]
- 0053f9ac bytes a56d1a94
+ 00562844 bytes 93d41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-022e188e45505f3f2bc85f3c31e5229b"></a>

### [`0053fdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fdac.md) → [`00562c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c44.md) FUN_00562c44

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053fdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fdac.md#insn-0053fdd4)
- 新版 [`00562c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c44.md#insn-00562c6c)

~~~diff
- 0053fdd4 ["INT_ADD", "register:40f0:8", ["const:53fdd4:8", "const:4:8"]]
- 0053fdd4 ["CALL", null, ["callee:00562cb0:8"]]
+ 00562c6c ["INT_ADD", "register:40f0:8", ["const:562c6c:8", "const:4:8"]]
+ 00562c6c ["CALL", null, ["callee:00562cb0:8"]]
- 0053fdd4 bytes 11000094
+ 00562c6c bytes 11000094
~~~


<a id="compare-5498768c8b713aed60e6437ee09472ea"></a>

### [`0053fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md) → [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) FUN_00562cb0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0053fdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fdac.md) [`0053feb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md) [`005401c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md) [`0054054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/0054054c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00562c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c44.md) [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) [`005633e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633e4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053fe50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md#insn-0053fe50) · [`0053fe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md#insn-0053fe60) · [`0053fe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md#insn-0053fe70)
- 新版 [`00562ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md#insn-00562ce8) · [`00562cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md#insn-00562cf8) · [`00562d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md#insn-00562d08)

~~~diff
- 0053fe50 ["INT_ADD", "register:40f0:8", ["const:53fe50:8", "const:4:8"]]
- 0053fe50 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00562ce8 ["INT_ADD", "register:40f0:8", ["const:562ce8:8", "const:4:8"]]
+ 00562ce8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053fe50 bytes 846c1a94
+ 00562ce8 bytes 72d31b94
- 0053fe60 ["INT_ADD", "register:40f0:8", ["const:53fe60:8", "const:4:8"]]
- 0053fe60 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00562cf8 ["INT_ADD", "register:40f0:8", ["const:562cf8:8", "const:4:8"]]
+ 00562cf8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053fe60 bytes 806c1a94
+ 00562cf8 bytes 6ed31b94
- 0053fe70 ["INT_ADD", "register:40f0:8", ["const:53fe70:8", "const:4:8"]]
- 0053fe70 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00562d08 ["INT_ADD", "register:40f0:8", ["const:562d08:8", "const:4:8"]]
+ 00562d08 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053fe70 bytes 7c6c1a94
+ 00562d08 bytes 6ad31b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ee076b353c9ff85aa901eb393bb82c5"></a>

### [`0053feb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md) → [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) FUN_00562d50

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053e13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e13c.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0053fe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe04.md) [`0053fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md) [`005400f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005400f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00562c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md) [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`00562f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053ff7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md#insn-0053ff7c) · [`0053ffac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md#insn-0053ffac) · [`00540040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md#insn-00540040)
- 新版 [`00562e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md#insn-00562e14) · [`00562e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md#insn-00562e44) · [`00562ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md#insn-00562ed8)

~~~diff
- 0053ff7c ["INT_ADD", "register:40f0:8", ["const:53ff7c:8", "const:4:8"]]
- 0053ff7c ["CALL", null, ["callee:00c57a90:8"]]
+ 00562e14 ["INT_ADD", "register:40f0:8", ["const:562e14:8", "const:4:8"]]
+ 00562e14 ["CALL", null, ["callee:00c57a90:8"]]
- 0053ff7c bytes 316c1a94
+ 00562e14 bytes 1fd31b94
- 0053ffac ["INT_ADD", "register:40f0:8", ["const:53ffac:8", "const:4:8"]]
- 0053ffac ["CALL", null, ["callee:00562f88:8"]]
+ 00562e44 ["INT_ADD", "register:40f0:8", ["const:562e44:8", "const:4:8"]]
+ 00562e44 ["CALL", null, ["callee:00562f88:8"]]
- 0053ffac bytes 51000094
+ 00562e44 bytes 51000094
- 00540040 ["INT_ADD", "register:40f0:8", ["const:540040:8", "const:4:8"]]
- 00540040 ["CALL", null, ["callee:00562cb0:8"]]
+ 00562ed8 ["INT_ADD", "register:40f0:8", ["const:562ed8:8", "const:4:8"]]
+ 00562ed8 ["CALL", null, ["callee:00562cb0:8"]]
- 00540040 bytes 76ffff97
+ 00562ed8 bytes 76ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f574c457528b6610c21f1dcb36bae288"></a>

### [`005400f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005400f0.md) → [`00562f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md) FUN_00562f88

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0053e13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e13c.md) [`0053feb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00574730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574730.md)
- 新版 呼出元 2件 [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005400f0.md#insn-00540114) · [`0054013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005400f0.md#insn-0054013c) · [`00540170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005400f0.md#insn-00540170)
- 新版 [`00562fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md#insn-00562fac) · [`00562fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md#insn-00562fd4) · [`00563008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562f88.md#insn-00563008)

~~~diff
- 00540114 ["INT_ADD", "register:40f0:8", ["const:540114:8", "const:4:8"]]
- 00540114 ["CALL", null, ["callee:005975c8:8"]]
+ 00562fac ["INT_ADD", "register:40f0:8", ["const:562fac:8", "const:4:8"]]
+ 00562fac ["CALL", null, ["callee:005975c8:8"]]
- 00540114 bytes 87d10094
+ 00562fac bytes 87d10094
- 0054013c ["INT_ADD", "register:40f0:8", ["const:54013c:8", "const:4:8"]]
- 0054013c ["CALL", null, ["callee:0043bae0:8"]]
+ 00562fd4 ["INT_ADD", "register:40f0:8", ["const:562fd4:8", "const:4:8"]]
+ 00562fd4 ["CALL", null, ["callee:0043bae0:8"]]
- 0054013c bytes a963fb97
+ 00562fd4 bytes c362fb97
- 00540170 ["INT_ADD", "register:40f0:8", ["const:540170:8", "const:4:8"]]
- 00540170 ["CALL", null, ["callee:0043bae0:8"]]
+ 00563008 ["INT_ADD", "register:40f0:8", ["const:563008:8", "const:4:8"]]
+ 00563008 ["CALL", null, ["callee:0043bae0:8"]]
- 00540170 bytes 9c63fb97
+ 00563008 bytes b662fb97
~~~


<a id="compare-70123579745043e4ce80611f8525fa6b"></a>

### [`005401c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md) → [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) FUN_00563058

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e18c.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0053fe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe04.md) [`0053fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md) [`00540408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540408.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00562c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md) [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`005632a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054028c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md#insn-0054028c) · [`005402c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md#insn-005402c0) · [`00540354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md#insn-00540354)
- 新版 [`00563124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md#insn-00563124) · [`00563158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md#insn-00563158) · [`005631ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md#insn-005631ec)

~~~diff
- 0054028c ["INT_ADD", "register:40f0:8", ["const:54028c:8", "const:4:8"]]
- 0054028c ["CALL", null, ["callee:00c57a90:8"]]
+ 00563124 ["INT_ADD", "register:40f0:8", ["const:563124:8", "const:4:8"]]
+ 00563124 ["CALL", null, ["callee:00c57a90:8"]]
- 0054028c bytes 6d6b1a94
+ 00563124 bytes 5bd21b94
- 005402c0 ["INT_ADD", "register:40f0:8", ["const:5402c0:8", "const:4:8"]]
- 005402c0 ["CALL", null, ["callee:005632a0:8"]]
+ 00563158 ["INT_ADD", "register:40f0:8", ["const:563158:8", "const:4:8"]]
+ 00563158 ["CALL", null, ["callee:005632a0:8"]]
- 005402c0 bytes 52000094
+ 00563158 bytes 52000094
- 00540354 ["INT_ADD", "register:40f0:8", ["const:540354:8", "const:4:8"]]
- 00540354 ["CALL", null, ["callee:00562cb0:8"]]
+ 005631ec ["INT_ADD", "register:40f0:8", ["const:5631ec:8", "const:4:8"]]
+ 005631ec ["CALL", null, ["callee:00562cb0:8"]]
- 00540354 bytes b1feff97
+ 005631ec bytes b1feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d10881c9e0b0779fd90f39bbd9bc518"></a>

### [`00540408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540408.md) → [`005632a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md) FUN_005632a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0053e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e18c.md) [`005401c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 2件 [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054043c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540408.md#insn-0054043c) · [`00540464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540408.md#insn-00540464) · [`0054048c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540408.md#insn-0054048c)
- 新版 [`005632d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md#insn-005632d4) · [`005632fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md#insn-005632fc) · [`00563324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005632a0.md#insn-00563324)

~~~diff
- 0054043c ["INT_ADD", "register:40f0:8", ["const:54043c:8", "const:4:8"]]
- 0054043c ["CALL", null, ["callee:00c538b0:8"]]
+ 005632d4 ["INT_ADD", "register:40f0:8", ["const:5632d4:8", "const:4:8"]]
+ 005632d4 ["CALL", null, ["callee:00c538b0:8"]]
- 0054043c bytes 895a1a94
+ 005632d4 bytes 77c11b94
- 00540464 ["INT_ADD", "register:40f0:8", ["const:540464:8", "const:4:8"]]
- 00540464 ["CALL", null, ["callee:0043bae0:8"]]
+ 005632fc ["INT_ADD", "register:40f0:8", ["const:5632fc:8", "const:4:8"]]
+ 005632fc ["CALL", null, ["callee:0043bae0:8"]]
- 00540464 bytes df62fb97
+ 005632fc bytes f961fb97
- 0054048c ["INT_ADD", "register:40f0:8", ["const:54048c:8", "const:4:8"]]
- 0054048c ["CALL", null, ["callee:0043bae0:8"]]
+ 00563324 ["INT_ADD", "register:40f0:8", ["const:563324:8", "const:4:8"]]
+ 00563324 ["CALL", null, ["callee:0043bae0:8"]]
- 0054048c bytes d562fb97
+ 00563324 bytes ef61fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2921557b4c02af9e4e9ed27eea3505a4"></a>

### [`0054054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/0054054c.md) → [`005633e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633e4.md) FUN_005633e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe18.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00562cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562cb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/0054054c.md#insn-00540584)
- 新版 [`0056341c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633e4.md#insn-0056341c)

~~~diff
- 00540584 ["INT_ADD", "register:40f0:8", ["const:540584:8", "const:4:8"]]
- 00540584 ["CALL", null, ["callee:00562cb0:8"]]
+ 0056341c ["INT_ADD", "register:40f0:8", ["const:56341c:8", "const:4:8"]]
+ 0056341c ["CALL", null, ["callee:00562cb0:8"]]
- 00540584 bytes 25feff97
+ 0056341c bytes 25feff97
~~~


<a id="compare-8dcfdc5984c2df5c354a58dc881fe864"></a>

### [`00540834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540834.md) → [`005636cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005636cc.md) FUN_005636cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540834.md#insn-00540850)
- 新版 [`005636e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005636cc.md#insn-005636e8)

~~~diff
- 00540850 ["INT_ADD", "register:40f0:8", ["const:540850:8", "const:4:8"]]
- 00540850 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005636e8 ["INT_ADD", "register:40f0:8", ["const:5636e8:8", "const:4:8"]]
+ 005636e8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00540850 bytes 046a1a94
+ 005636e8 bytes f2d01b94
~~~


<a id="compare-ff2650c87e8c2e407ffdca518d9eeccc"></a>

### [`00540878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540878.md) → [`00563710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md) FUN_00563710

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540878.md#insn-00540894) · [`005408a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540878.md#insn-005408a4)
- 新版 [`0056372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md#insn-0056372c) · [`0056373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md#insn-0056373c)

~~~diff
- 00540894 ["INT_ADD", "register:40f0:8", ["const:540894:8", "const:4:8"]]
- 00540894 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0056372c ["INT_ADD", "register:40f0:8", ["const:56372c:8", "const:4:8"]]
+ 0056372c ["CALL", null, ["callee:00c57ab0:8"]]
- 00540894 bytes f3691a94
+ 0056372c bytes e1d01b94
- 005408a4 ["INT_ADD", "register:40f0:8", ["const:5408a4:8", "const:4:8"]]
- 005408a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0056373c ["INT_ADD", "register:40f0:8", ["const:56373c:8", "const:4:8"]]
+ 0056373c ["CALL", null, ["callee:00c57ab0:8"]]
- 005408a4 bytes ef691a94
+ 0056373c bytes ddd01b94
~~~


<a id="compare-600ef8dfeb4680f76ac4064ab41e9c66"></a>

### [`00540c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540c2c.md) → [`00563ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md) FUN_00563ac4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005409c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409c4.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005261fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005261fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0056385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540c2c.md#insn-00540c7c) · [`00540ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540c2c.md#insn-00540ca8) · [`00540cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540c2c.md#insn-00540cb4)
- 新版 [`00563b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md#insn-00563b14) · [`00563b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md#insn-00563b40) · [`00563b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md#insn-00563b4c)

~~~diff
- 00540c7c ["INT_ADD", "register:40f0:8", ["const:540c7c:8", "const:4:8"]]
- 00540c7c ["CALL", null, ["callee:0043bae0:8"]]
+ 00563b14 ["INT_ADD", "register:40f0:8", ["const:563b14:8", "const:4:8"]]
+ 00563b14 ["CALL", null, ["callee:0043bae0:8"]]
- 00540c7c bytes d960fb97
+ 00563b14 bytes f35ffb97
- 00540ca8 ["INT_ADD", "register:40f0:8", ["const:540ca8:8", "const:4:8"]]
- 00540ca8 ["CALL", null, ["callee:0043bae0:8"]]
+ 00563b40 ["INT_ADD", "register:40f0:8", ["const:563b40:8", "const:4:8"]]
+ 00563b40 ["CALL", null, ["callee:0043bae0:8"]]
- 00540ca8 bytes ce60fb97
+ 00563b40 bytes e85ffb97
- 00540cb4 ["INT_ADD", "register:40f0:8", ["const:540cb4:8", "const:4:8"]]
- 00540cb4 ["CALL", null, ["callee:00549094:8"]]
+ 00563b4c ["INT_ADD", "register:40f0:8", ["const:563b4c:8", "const:4:8"]]
+ 00563b4c ["CALL", null, ["callee:00549094:8"]]
- 00540cb4 bytes 5295ff97
+ 00563b4c bytes 5295ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66b6df343b4914cef3440102c9eb0256"></a>

### [`00540d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d3c.md) → [`00563bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md) FUN_00563bd4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00524cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524cd8.md) [`00541408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00547b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) [`005642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d3c.md#insn-00540d50) · [`00540d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d3c.md#insn-00540d6c)
- 新版 [`00563be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md#insn-00563be8) · [`00563c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md#insn-00563c04)

~~~diff
- 00540d50 ["INT_ADD", "register:40f0:8", ["const:540d50:8", "const:4:8"]]
- 00540d50 ["CALL", null, ["callee:00547b70:8"]]
+ 00563be8 ["INT_ADD", "register:40f0:8", ["const:563be8:8", "const:4:8"]]
+ 00563be8 ["CALL", null, ["callee:00547b70:8"]]
- 00540d50 bytes e28fff97
+ 00563be8 bytes e28fff97
- 00540d6c ["INT_ADD", "register:40f0:8", ["const:540d6c:8", "const:4:8"]]
- 00540d6c ["CALL", null, ["callee:005642a0:8"]]
+ 00563c04 ["INT_ADD", "register:40f0:8", ["const:563c04:8", "const:4:8"]]
+ 00563c04 ["CALL", null, ["callee:005642a0:8"]]
- 00540d6c bytes a7010094
+ 00563c04 bytes a7010094
~~~


<a id="compare-3d45c90dca4561f9577cfa613700e03a"></a>

### [`00540d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d88.md) → [`00563c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c20.md) FUN_00563c20

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00470ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ef0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d88.md#insn-00540da0)
- 新版 [`00563c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c20.md#insn-00563c38)

~~~diff
- 00540da0 ["INT_ADD", "register:40f0:8", ["const:540da0:8", "const:4:8"]]
- 00540da0 ["CALL", null, ["callee:00493d88:8"]]
+ 00563c38 ["INT_ADD", "register:40f0:8", ["const:563c38:8", "const:4:8"]]
+ 00563c38 ["CALL", null, ["callee:00493d88:8"]]
- 00540da0 bytes 54c0fc97
+ 00563c38 bytes 54c0fc97
~~~


<a id="compare-46c9d46ad96decf8e1ed028b0e48b8dc"></a>

### [`00540df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540df4.md) → [`00563c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md) FUN_00563c8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`005251c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005251c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540df4.md#insn-00540e0c) · [`00540e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540df4.md#insn-00540e6c) · [`00540e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540df4.md#insn-00540e80)
- 新版 [`00563ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md#insn-00563ca4) · [`00563d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md#insn-00563d04) · [`00563d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c8c.md#insn-00563d18)

~~~diff
- 00540e0c ["INT_ADD", "register:40f0:8", ["const:540e0c:8", "const:4:8"]]
- 00540e0c ["CALL", null, ["callee:00548058:8"]]
+ 00563ca4 ["INT_ADD", "register:40f0:8", ["const:563ca4:8", "const:4:8"]]
+ 00563ca4 ["CALL", null, ["callee:00548058:8"]]
- 00540e0c bytes ed90ff97
+ 00563ca4 bytes ed90ff97
- 00540e6c ["INT_ADD", "register:40f0:8", ["const:540e6c:8", "const:4:8"]]
- 00540e6c ["CALL", null, ["callee:00540d3c:8"]]
+ 00563d04 ["INT_ADD", "register:40f0:8", ["const:563d04:8", "const:4:8"]]
+ 00563d04 ["CALL", null, ["callee:00540d3c:8"]]
- 00540e6c bytes 0e74ff97
+ 00563d04 bytes 0e74ff97
- 00540e80 ["INT_ADD", "register:40f0:8", ["const:540e80:8", "const:4:8"]]
- 00540e80 ["CALL", null, ["callee:0043bae0:8"]]
+ 00563d18 ["INT_ADD", "register:40f0:8", ["const:563d18:8", "const:4:8"]]
+ 00563d18 ["CALL", null, ["callee:0043bae0:8"]]
- 00540e80 bytes 5860fb97
+ 00563d18 bytes 725ffb97
~~~


<a id="compare-1874d13c14b35ee0b9559b32017fd435"></a>

### [`00540eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540eec.md) → [`00563d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563d84.md) FUN_00563d84

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005414a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005414a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00564340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540eec.md#insn-00540ef8)
- 新版 [`00563d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563d84.md#insn-00563d90)

~~~diff
- 00540ef8 ["INT_ADD", "register:40f0:8", ["const:540ef8:8", "const:4:8"]]
- 00540ef8 ["CALL", null, ["callee:00564340:8"]]
+ 00563d90 ["INT_ADD", "register:40f0:8", ["const:563d90:8", "const:4:8"]]
+ 00563d90 ["CALL", null, ["callee:00564340:8"]]
- 00540ef8 bytes 6c010094
+ 00563d90 bytes 6c010094
~~~


<a id="compare-f714885d8294b47eff1ae07f940e9c34"></a>

### [`00540f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540f58.md) → [`00563df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md) FUN_00563df0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`005416b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005416b0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00564548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00541000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540f58.md#insn-00541000) · [`00541034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540f58.md#insn-00541034) · [`00541098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540f58.md#insn-00541098)
- 新版 [`00563e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md#insn-00563e98) · [`00563ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md#insn-00563ecc) · [`00563f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md#insn-00563f30)

~~~diff
- 00541000 ["INT_ADD", "register:40f0:8", ["const:541000:8", "const:4:8"]]
- 00541000 ["CALL", null, ["callee:0043bae0:8"]]
+ 00563e98 ["INT_ADD", "register:40f0:8", ["const:563e98:8", "const:4:8"]]
+ 00563e98 ["CALL", null, ["callee:0043bae0:8"]]
- 00541000 bytes f85ffb97
+ 00563e98 bytes 125ffb97
- 00541034 ["INT_ADD", "register:40f0:8", ["const:541034:8", "const:4:8"]]
- 00541034 ["CALL", null, ["callee:0043bae0:8"]]
+ 00563ecc ["INT_ADD", "register:40f0:8", ["const:563ecc:8", "const:4:8"]]
+ 00563ecc ["CALL", null, ["callee:0043bae0:8"]]
- 00541034 bytes eb5ffb97
+ 00563ecc bytes 055ffb97
- 00541098 ["INT_ADD", "register:40f0:8", ["const:541098:8", "const:4:8"]]
- 00541098 ["CALL", null, ["callee:00c57a90:8"]]
+ 00563f30 ["INT_ADD", "register:40f0:8", ["const:563f30:8", "const:4:8"]]
+ 00563f30 ["CALL", null, ["callee:00c57a90:8"]]
- 00541098 bytes ea671a94
+ 00563f30 bytes d8ce1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82d186f79ae2f048263f55a4a1007b12"></a>

### [`00541408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md) → [`005642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md) FUN_005642a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00540d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d3c.md) [`00562028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562028.md) [`00832958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832958.md) [`0085c31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c31c.md) [`00b26b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00563bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md) [`00584ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) [`0088f2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2b4.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054146c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md#insn-0054146c) · [`0054147c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md#insn-0054147c) · [`0054148c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md#insn-0054148c)
- 新版 [`00564304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md#insn-00564304) · [`00564314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md#insn-00564314) · [`00564324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md#insn-00564324)

~~~diff
- 0054146c ["INT_ADD", "register:40f0:8", ["const:54146c:8", "const:4:8"]]
- 0054146c ["CALL", null, ["callee:004945d0:8"]]
+ 00564304 ["INT_ADD", "register:40f0:8", ["const:564304:8", "const:4:8"]]
+ 00564304 ["CALL", null, ["callee:004945d0:8"]]
- 0054146c bytes b3c0fc97
+ 00564304 bytes b3c0fc97
- 0054147c ["INT_ADD", "register:40f0:8", ["const:54147c:8", "const:4:8"]]
- 0054147c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00564314 ["INT_ADD", "register:40f0:8", ["const:564314:8", "const:4:8"]]
+ 00564314 ["CALL", null, ["callee:00c57ab0:8"]]
- 0054147c bytes f9661a94
+ 00564314 bytes e7cd1b94
- 0054148c ["INT_ADD", "register:40f0:8", ["const:54148c:8", "const:4:8"]]
- 0054148c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00564324 ["INT_ADD", "register:40f0:8", ["const:564324:8", "const:4:8"]]
+ 00564324 ["CALL", null, ["callee:00c57ab0:8"]]
- 0054148c bytes f5661a94
+ 00564324 bytes e3cd1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-798c6e5f6cec3b8c56ea95ae68b08dca"></a>

### [`005414a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005414a8.md) → [`00564340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md) FUN_00564340

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00540eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540eec.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00563d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563d84.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00541524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005414a8.md#insn-00541524) · [`0054154c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005414a8.md#insn-0054154c) · [`005415b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005414a8.md#insn-005415b8)
- 新版 [`005643bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md#insn-005643bc) · [`005643e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md#insn-005643e4) · [`00564450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564340.md#insn-00564450)

~~~diff
- 00541524 ["INT_ADD", "register:40f0:8", ["const:541524:8", "const:4:8"]]
- 00541524 ["CALL", null, ["callee:00c57c50:8"]]
+ 005643bc ["INT_ADD", "register:40f0:8", ["const:5643bc:8", "const:4:8"]]
+ 005643bc ["CALL", null, ["callee:00c57c50:8"]]
- 00541524 bytes 37671a94
+ 005643bc bytes 25ce1b94
- 0054154c ["INT_ADD", "register:40f0:8", ["const:54154c:8", "const:4:8"]]
- 0054154c ["CALL", null, ["callee:00c57c50:8"]]
+ 005643e4 ["INT_ADD", "register:40f0:8", ["const:5643e4:8", "const:4:8"]]
+ 005643e4 ["CALL", null, ["callee:00c57c50:8"]]
- 0054154c bytes 2d671a94
+ 005643e4 bytes 1bce1b94
- 005415b8 ["INT_ADD", "register:40f0:8", ["const:5415b8:8", "const:4:8"]]
- 005415b8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00564450 ["INT_ADD", "register:40f0:8", ["const:564450:8", "const:4:8"]]
+ 00564450 ["CALL", null, ["callee:00c57c50:8"]]
- 005415b8 bytes 12671a94
+ 00564450 bytes 00ce1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-569baf968864607f22e7292c70d4a7e6"></a>

### [`00541afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541afc.md) → [`00564994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md) FUN_00564994

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00541b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541afc.md#insn-00541b38) · [`00541b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541afc.md#insn-00541b5c) · [`00541ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541afc.md#insn-00541ba8)
- 新版 [`005649d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md#insn-005649d0) · [`005649f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md#insn-005649f4) · [`00564a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564994.md#insn-00564a40)

~~~diff
- 00541b38 ["COPY", "register:0:8", ["register:4048:8"]]
- 00541b38 ["INT_ADD", "register:40f0:8", ["const:541b38:8", "const:4:8"]]
- 00541b38 ["CALLIND", null, ["register:0:8"]]
+ 005649d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005649d0 ["INT_ADD", "register:40f0:8", ["const:5649d0:8", "const:4:8"]]
+ 005649d0 ["CALLIND", null, ["register:0:8"]]
- 00541b38 bytes 20013fd6
+ 005649d0 bytes 20013fd6
- 00541b5c ["COPY", "register:0:8", ["register:4048:8"]]
- 00541b5c ["INT_ADD", "register:40f0:8", ["const:541b5c:8", "const:4:8"]]
- 00541b5c ["CALLIND", null, ["register:0:8"]]
+ 005649f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005649f4 ["INT_ADD", "register:40f0:8", ["const:5649f4:8", "const:4:8"]]
+ 005649f4 ["CALLIND", null, ["register:0:8"]]
- 00541b5c bytes 20013fd6
+ 005649f4 bytes 20013fd6
- 00541ba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00541ba8 ["INT_ADD", "register:40f0:8", ["const:541ba8:8", "const:4:8"]]
- 00541ba8 ["CALLIND", null, ["register:0:8"]]
+ 00564a40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00564a40 ["INT_ADD", "register:40f0:8", ["const:564a40:8", "const:4:8"]]
+ 00564a40 ["CALLIND", null, ["register:0:8"]]
- 00541ba8 bytes 00013fd6
+ 00564a40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdfc1eeedd9c86dd48896bbade9f36c1"></a>

### [`0054226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054226c.md) → [`00565104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md) FUN_00565104

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005422a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054226c.md#insn-005422a8) · [`005422f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054226c.md#insn-005422f8) · [`00542368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054226c.md#insn-00542368)
- 新版 [`00565140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md#insn-00565140) · [`00565190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md#insn-00565190) · [`00565200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565104.md#insn-00565200)

~~~diff
- 005422a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005422a8 ["INT_ADD", "register:40f0:8", ["const:5422a8:8", "const:4:8"]]
- 005422a8 ["CALLIND", null, ["register:0:8"]]
+ 00565140 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00565140 ["INT_ADD", "register:40f0:8", ["const:565140:8", "const:4:8"]]
+ 00565140 ["CALLIND", null, ["register:0:8"]]
- 005422a8 bytes 20013fd6
+ 00565140 bytes 20013fd6
- 005422f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005422f8 ["INT_ADD", "register:40f0:8", ["const:5422f8:8", "const:4:8"]]
- 005422f8 ["CALLIND", null, ["register:0:8"]]
+ 00565190 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00565190 ["INT_ADD", "register:40f0:8", ["const:565190:8", "const:4:8"]]
+ 00565190 ["CALLIND", null, ["register:0:8"]]
- 005422f8 bytes 20013fd6
+ 00565190 bytes 20013fd6
- 00542368 ["INT_ADD", "register:40f0:8", ["const:542368:8", "const:4:8"]]
- 00542368 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00565200 ["INT_ADD", "register:40f0:8", ["const:565200:8", "const:4:8"]]
+ 00565200 ["CALL", null, ["callee:00c57ab0:8"]]
- 00542368 bytes 3e631a94
+ 00565200 bytes 2cca1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a2863002137f9677c1a5f736aff1c4f"></a>

### [`005426ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md) → [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) FUN_00565544

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0054729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md) [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) [`005488c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md) [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md)
- 新版 呼出元 4件 [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`0056b75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005426d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md#insn-005426d0) · [`00542704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md#insn-00542704) · [`0054271c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md#insn-0054271c)
- 新版 [`00565568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md#insn-00565568) · [`0056559c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md#insn-0056559c) · [`005655b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md#insn-005655b4)

~~~diff
- 005426d0 ["INT_ADD", "register:40f0:8", ["const:5426d0:8", "const:4:8"]]
- 005426d0 ["CALL", null, ["callee:00c58260:8"]]
+ 00565568 ["INT_ADD", "register:40f0:8", ["const:565568:8", "const:4:8"]]
+ 00565568 ["CALL", null, ["callee:00c58260:8"]]
- 005426d0 bytes 50641a94
+ 00565568 bytes 3ecb1b94
- 00542704 ["INT_ADD", "register:40f0:8", ["const:542704:8", "const:4:8"]]
- 00542704 ["CALL", null, ["callee:00c58260:8"]]
+ 0056559c ["INT_ADD", "register:40f0:8", ["const:56559c:8", "const:4:8"]]
+ 0056559c ["CALL", null, ["callee:00c58260:8"]]
- 00542704 bytes 43641a94
+ 0056559c bytes 31cb1b94
- 0054271c ["INT_ADD", "register:40f0:8", ["const:54271c:8", "const:4:8"]]
- 0054271c ["CALL", null, ["callee:00c58260:8"]]
+ 005655b4 ["INT_ADD", "register:40f0:8", ["const:5655b4:8", "const:4:8"]]
+ 005655b4 ["CALL", null, ["callee:00c58260:8"]]
- 0054271c bytes 3d641a94
+ 005655b4 bytes 2bcb1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cf6d47f3dcfe882496e170bdb51c218"></a>

### [`00545a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545a50.md) → [`005688e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/005688e8.md) FUN_005688e8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) [`00546c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546c14.md) · 呼出先 1件 [`00bdd200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd200.md)
- 新版 呼出元 2件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`00569aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569aac.md) · 呼出先 1件 [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00545a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545a50.md#insn-00545a8c)
- 新版 [`00568924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/005688e8.md#insn-00568924)

~~~diff
- 00545a8c ["INT_ADD", "register:40f0:8", ["const:545a8c:8", "const:4:8"]]
- 00545a8c ["CALL", null, ["callee:00c59c50:8"]]
+ 00568924 ["INT_ADD", "register:40f0:8", ["const:568924:8", "const:4:8"]]
+ 00568924 ["CALL", null, ["callee:00c59c50:8"]]
- 00545a8c bytes dd5d1a94
+ 00568924 bytes cbc41b94
~~~


<a id="compare-5ba8ba8cc00ce7b4eea55b0a4698295f"></a>

### [`005463e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005463e4.md) → [`0056927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md) FUN_0056927c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) · 呼出先 3件 [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) [`00543a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543a40.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) · 呼出先 3件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005463e4.md#insn-00546414) · [`0054642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005463e4.md#insn-0054642c) · [`00546458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005463e4.md#insn-00546458)
- 新版 [`005692ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md#insn-005692ac) · [`005692c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md#insn-005692c4) · [`005692f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md#insn-005692f0)

~~~diff
- 00546414 ["INT_ADD", "register:40f0:8", ["const:546414:8", "const:4:8"]]
- 00546414 ["CALL", null, ["callee:00565a18:8"]]
+ 005692ac ["INT_ADD", "register:40f0:8", ["const:5692ac:8", "const:4:8"]]
+ 005692ac ["CALL", null, ["callee:00565a18:8"]]
- 00546414 bytes dbf1ff97
+ 005692ac bytes dbf1ff97
- 0054642c ["INT_ADD", "register:40f0:8", ["const:54642c:8", "const:4:8"]]
- 0054642c ["CALL", null, ["callee:005668d8:8"]]
+ 005692c4 ["INT_ADD", "register:40f0:8", ["const:5692c4:8", "const:4:8"]]
+ 005692c4 ["CALL", null, ["callee:005668d8:8"]]
- 0054642c bytes 85f5ff97
+ 005692c4 bytes 85f5ff97
- 00546458 ["INT_ADD", "register:40f0:8", ["const:546458:8", "const:4:8"]]
- 00546458 ["CALL", null, ["callee:00c57ae0:8"]]
+ 005692f0 ["INT_ADD", "register:40f0:8", ["const:5692f0:8", "const:4:8"]]
+ 005692f0 ["CALL", null, ["callee:00c57ae0:8"]]
- 00546458 bytes 0e531a94
+ 005692f0 bytes fcb91b94
~~~


<a id="compare-8db6a06b8ad1a143aa62393db446dbaf"></a>

### [`0054645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/0054645c.md) → [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) FUN_005692f4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`00549b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549b88.md) · 呼出先 4件 [`0054a398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a398.md) [`0054a408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md) [`0054a560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a560.md) [`00bdd220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd220.md)
- 新版 呼出元 2件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) · 呼出先 4件 [`0056d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d230.md) [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/0054645c.md#insn-00546488) · [`0054651c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/0054645c.md#insn-0054651c) · [`00546558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/0054645c.md#insn-00546558)
- 新版 [`00569320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md#insn-00569320) · [`005693b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md#insn-005693b4) · [`005693f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md#insn-005693f0)

~~~diff
- 00546488 ["INT_ADD", "register:40f0:8", ["const:546488:8", "const:4:8"]]
- 00546488 ["CALL", null, ["callee:0056d2a0:8"]]
+ 00569320 ["INT_ADD", "register:40f0:8", ["const:569320:8", "const:4:8"]]
+ 00569320 ["CALL", null, ["callee:0056d2a0:8"]]
- 00546488 bytes e00f0094
+ 00569320 bytes e00f0094
- 0054651c ["INT_ADD", "register:40f0:8", ["const:54651c:8", "const:4:8"]]
- 0054651c ["CALL", null, ["callee:00c59c70:8"]]
+ 005693b4 ["INT_ADD", "register:40f0:8", ["const:5693b4:8", "const:4:8"]]
+ 005693b4 ["CALL", null, ["callee:00c59c70:8"]]
- 0054651c bytes 415b1a94
+ 005693b4 bytes 2fc21b94
- 00546558 ["INT_ADD", "register:40f0:8", ["const:546558:8", "const:4:8"]]
- 00546558 ["CALL", null, ["callee:00c59c70:8"]]
+ 005693f0 ["INT_ADD", "register:40f0:8", ["const:5693f0:8", "const:4:8"]]
+ 005693f0 ["CALL", null, ["callee:00c59c70:8"]]
- 00546558 bytes 325b1a94
+ 005693f0 bytes 20c21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86170ae355213d725051aeb0839802b"></a>

### [`00546608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546608.md) → [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) FUN_005694a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) [`00549364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md) · 呼出先 4件 [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) [`00543a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543a40.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md)
- 新版 呼出元 3件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) · 呼出先 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546608.md#insn-00546694) · [`005466b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546608.md#insn-005466b0) · [`005466e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546608.md#insn-005466e8)
- 新版 [`0056952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md#insn-0056952c) · [`00569548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md#insn-00569548) · [`00569580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md#insn-00569580)

~~~diff
- 00546694 ["INT_ADD", "register:40f0:8", ["const:546694:8", "const:4:8"]]
- 00546694 ["CALL", null, ["callee:00c59c60:8"]]
+ 0056952c ["INT_ADD", "register:40f0:8", ["const:56952c:8", "const:4:8"]]
+ 0056952c ["CALL", null, ["callee:00c59c60:8"]]
- 00546694 bytes df5a1a94
+ 0056952c bytes cdc11b94
- 005466b0 ["INT_ADD", "register:40f0:8", ["const:5466b0:8", "const:4:8"]]
- 005466b0 ["CALL", null, ["callee:00c59c60:8"]]
+ 00569548 ["INT_ADD", "register:40f0:8", ["const:569548:8", "const:4:8"]]
+ 00569548 ["CALL", null, ["callee:00c59c60:8"]]
- 005466b0 bytes d85a1a94
+ 00569548 bytes c6c11b94
- 005466e8 ["INT_ADD", "register:40f0:8", ["const:5466e8:8", "const:4:8"]]
- 005466e8 ["CALL", null, ["callee:00565a18:8"]]
+ 00569580 ["INT_ADD", "register:40f0:8", ["const:569580:8", "const:4:8"]]
+ 00569580 ["CALL", null, ["callee:00565a18:8"]]
- 005466e8 bytes 26f1ff97
+ 00569580 bytes 26f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cc171c22526c33967d98ecc7031c220"></a>

### [`00546730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546730.md) → [`005695c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005695c8.md) FUN_005695c8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`00546c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546c14.md) · 呼出先 1件 [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md)
- 新版 呼出元 2件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`00569aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569aac.md) · 呼出先 1件 [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005467a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546730.md#insn-005467a8)
- 新版 [`00569640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005695c8.md#insn-00569640)

~~~diff
- 005467a8 ["INT_ADD", "register:40f0:8", ["const:5467a8:8", "const:4:8"]]
- 005467a8 ["CALL", null, ["callee:00c59c60:8"]]
+ 00569640 ["INT_ADD", "register:40f0:8", ["const:569640:8", "const:4:8"]]
+ 00569640 ["CALL", null, ["callee:00c59c60:8"]]
- 005467a8 bytes 9a5a1a94
+ 00569640 bytes 88c11b94
~~~


<a id="compare-0b5ff9f534b768b8752919e1f2475c40"></a>

### [`005467e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005467e0.md) → [`00569678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md) FUN_00569678

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) · 呼出先 6件 [`00546c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546c14.md) [`00547138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547138.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd200.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md)
- 新版 呼出元 2件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) · 呼出先 6件 [`00569aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569aac.md) [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005467e0.md#insn-00546840) · [`005468cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005467e0.md#insn-005468cc) · [`005468e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005467e0.md#insn-005468e8)
- 新版 [`005696d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md#insn-005696d8) · [`00569764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md#insn-00569764) · [`00569780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md#insn-00569780)

~~~diff
- 00546840 ["INT_ADD", "register:40f0:8", ["const:546840:8", "const:4:8"]]
- 00546840 ["CALL", null, ["callee:00c59c50:8"]]
+ 005696d8 ["INT_ADD", "register:40f0:8", ["const:5696d8:8", "const:4:8"]]
+ 005696d8 ["CALL", null, ["callee:00c59c50:8"]]
- 00546840 bytes 705a1a94
+ 005696d8 bytes 5ec11b94
- 005468cc ["INT_ADD", "register:40f0:8", ["const:5468cc:8", "const:4:8"]]
- 005468cc ["CALL", null, ["callee:00c59c60:8"]]
+ 00569764 ["INT_ADD", "register:40f0:8", ["const:569764:8", "const:4:8"]]
+ 00569764 ["CALL", null, ["callee:00c59c60:8"]]
- 005468cc bytes 515a1a94
+ 00569764 bytes 3fc11b94
- 005468e8 ["INT_ADD", "register:40f0:8", ["const:5468e8:8", "const:4:8"]]
- 005468e8 ["CALL", null, ["callee:00c59c60:8"]]
+ 00569780 ["INT_ADD", "register:40f0:8", ["const:569780:8", "const:4:8"]]
+ 00569780 ["CALL", null, ["callee:00c59c60:8"]]
- 005468e8 bytes 4a5a1a94
+ 00569780 bytes 38c11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c5d0014b3ed71ac7f476b7c34215561"></a>

### [`0054709c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054709c.md) → [`00569f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md) FUN_00569f34

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd230.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 2件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005470f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054709c.md#insn-005470f0) · [`00547114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054709c.md#insn-00547114)
- 新版 [`00569f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md#insn-00569f88) · [`00569fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md#insn-00569fac)

~~~diff
- 005470f0 ["INT_ADD", "register:40f0:8", ["const:5470f0:8", "const:4:8"]]
- 005470f0 ["CALL", null, ["callee:00c59c80:8"]]
+ 00569f88 ["INT_ADD", "register:40f0:8", ["const:569f88:8", "const:4:8"]]
+ 00569f88 ["CALL", null, ["callee:00c59c80:8"]]
- 005470f0 bytes 50581a94
+ 00569f88 bytes 3ebf1b94
- 00547114 ["INT_ADD", "register:40f0:8", ["const:547114:8", "const:4:8"]]
- 00547114 ["CALL", null, ["callee:00c57c00:8"]]
+ 00569fac ["INT_ADD", "register:40f0:8", ["const:569fac:8", "const:4:8"]]
+ 00569fac ["CALL", null, ["callee:00c57c00:8"]]
- 00547114 bytes 27501a94
+ 00569fac bytes 15b71b94
~~~


<a id="compare-0f30bab294684d21a5d8326f0959bea3"></a>

### [`00547138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547138.md) → [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) FUN_00569fd0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) [`005467e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005467e0.md) [`0054a560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a560.md) · 呼出先 1件 [`00bdd220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd220.md)
- 新版 呼出元 3件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`00569678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md) [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) · 呼出先 1件 [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00547178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547138.md#insn-00547178) · [`00547194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547138.md#insn-00547194) · [`00547228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547138.md#insn-00547228)
- 新版 [`0056a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md#insn-0056a010) · [`0056a02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md#insn-0056a02c) · [`0056a0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md#insn-0056a0c0)

~~~diff
- 00547178 ["INT_ADD", "register:40f0:8", ["const:547178:8", "const:4:8"]]
- 00547178 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056a010 ["INT_ADD", "register:40f0:8", ["const:56a010:8", "const:4:8"]]
+ 0056a010 ["CALL", null, ["callee:00c59c70:8"]]
- 00547178 bytes 2a581a94
+ 0056a010 bytes 18bf1b94
- 00547194 ["INT_ADD", "register:40f0:8", ["const:547194:8", "const:4:8"]]
- 00547194 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056a02c ["INT_ADD", "register:40f0:8", ["const:56a02c:8", "const:4:8"]]
+ 0056a02c ["CALL", null, ["callee:00c59c70:8"]]
- 00547194 bytes 23581a94
+ 0056a02c bytes 11bf1b94
- 00547228 ["INT_ADD", "register:40f0:8", ["const:547228:8", "const:4:8"]]
- 00547228 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056a0c0 ["INT_ADD", "register:40f0:8", ["const:56a0c0:8", "const:4:8"]]
+ 0056a0c0 ["CALL", null, ["callee:00c59c70:8"]]
- 00547228 bytes fe571a94
+ 0056a0c0 bytes ecbe1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd1cf58f8ab89f1f53ee15cf6ac7609e"></a>

### [`0054729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md) → [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) FUN_0056a134

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) · 呼出先 8件 [`005426ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md) [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) [`00543a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543a40.md) [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) · 呼出先 8件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005472e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md#insn-005472e8) · [`00547338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md#insn-00547338) · [`00547384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md#insn-00547384)
- 新版 [`0056a180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md#insn-0056a180) · [`0056a1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md#insn-0056a1d0) · [`0056a21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md#insn-0056a21c)

~~~diff
- 005472e8 ["INT_ADD", "register:40f0:8", ["const:5472e8:8", "const:4:8"]]
- 005472e8 ["CALL", null, ["callee:00c57c90:8"]]
+ 0056a180 ["INT_ADD", "register:40f0:8", ["const:56a180:8", "const:4:8"]]
+ 0056a180 ["CALL", null, ["callee:00c57c90:8"]]
- 005472e8 bytes d64f1a94
+ 0056a180 bytes c4b61b94
- 00547338 ["INT_ADD", "register:40f0:8", ["const:547338:8", "const:4:8"]]
- 00547338 ["CALL", null, ["callee:00566bc0:8"]]
+ 0056a1d0 ["INT_ADD", "register:40f0:8", ["const:56a1d0:8", "const:4:8"]]
+ 0056a1d0 ["CALL", null, ["callee:00566bc0:8"]]
- 00547338 bytes 7cf2ff97
+ 0056a1d0 bytes 7cf2ff97
- 00547384 ["INT_ADD", "register:40f0:8", ["const:547384:8", "const:4:8"]]
- 00547384 ["CALL", null, ["callee:00565544:8"]]
+ 0056a21c ["INT_ADD", "register:40f0:8", ["const:56a21c:8", "const:4:8"]]
+ 0056a21c ["CALL", null, ["callee:00565544:8"]]
- 00547384 bytes caecff97
+ 0056a21c bytes caecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

