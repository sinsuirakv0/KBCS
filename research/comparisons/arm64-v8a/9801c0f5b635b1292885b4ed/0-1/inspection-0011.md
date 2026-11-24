# v15.7.4 → v16.0.0 · 要調査の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-1c972c7c58d6ba90ee35e7c05ad0f198"></a>

### [`00547a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547a3c.md) → [`0056a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md) FUN_0056a8d4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) · 呼出先 4件 [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) [`00543a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543a40.md) [`00547430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547430.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) · 呼出先 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`005668d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/005668d8.md) [`0056a2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a2c8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00547ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547a3c.md#insn-00547ae0) · [`00547b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547a3c.md#insn-00547b14) · [`00547b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547a3c.md#insn-00547b2c)
- 新版 [`0056a978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md#insn-0056a978) · [`0056a9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md#insn-0056a9ac) · [`0056a9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md#insn-0056a9c4)

~~~diff
- 00547ae0 ["INT_ADD", "register:40f0:8", ["const:547ae0:8", "const:4:8"]]
- 00547ae0 ["CALL", null, ["callee:0056a2c8:8"]]
+ 0056a978 ["INT_ADD", "register:40f0:8", ["const:56a978:8", "const:4:8"]]
+ 0056a978 ["CALL", null, ["callee:0056a2c8:8"]]
- 00547ae0 bytes 54feff97
+ 0056a978 bytes 54feff97
- 00547b14 ["INT_ADD", "register:40f0:8", ["const:547b14:8", "const:4:8"]]
- 00547b14 ["CALL", null, ["callee:00565a18:8"]]
+ 0056a9ac ["INT_ADD", "register:40f0:8", ["const:56a9ac:8", "const:4:8"]]
+ 0056a9ac ["CALL", null, ["callee:00565a18:8"]]
- 00547b14 bytes 1becff97
+ 0056a9ac bytes 1becff97
- 00547b2c ["INT_ADD", "register:40f0:8", ["const:547b2c:8", "const:4:8"]]
- 00547b2c ["CALL", null, ["callee:005668d8:8"]]
+ 0056a9c4 ["INT_ADD", "register:40f0:8", ["const:56a9c4:8", "const:4:8"]]
+ 0056a9c4 ["CALL", null, ["callee:005668d8:8"]]
- 00547b2c bytes c5efff97
+ 0056a9c4 bytes c5efff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d9eec9ad7eda1740eea222190ab744e"></a>

### [`00547bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547bf8.md) → [`0056aa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md) FUN_0056aa90

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054e3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e3ac.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00571244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571244.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00547c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547bf8.md#insn-00547c44) · [`00547c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547bf8.md#insn-00547c58) · [`00547c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547bf8.md#insn-00547c60)
- 新版 [`0056aadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md#insn-0056aadc) · [`0056aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md#insn-0056aaf0) · [`0056aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md#insn-0056aaf8)

~~~diff
- 00547c44 ["INT_ADD", "register:40f0:8", ["const:547c44:8", "const:4:8"]]
- 00547c44 ["CALL", null, ["callee:00c538e0:8"]]
+ 0056aadc ["INT_ADD", "register:40f0:8", ["const:56aadc:8", "const:4:8"]]
+ 0056aadc ["CALL", null, ["callee:00c538e0:8"]]
- 00547c44 bytes 933c1a94
+ 0056aadc bytes 81a31b94
- 00547c58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00547c58 ["INT_ADD", "register:40f0:8", ["const:547c58:8", "const:4:8"]]
- 00547c58 ["CALLIND", null, ["register:0:8"]]
+ 0056aaf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056aaf0 ["INT_ADD", "register:40f0:8", ["const:56aaf0:8", "const:4:8"]]
+ 0056aaf0 ["CALLIND", null, ["register:0:8"]]
- 00547c58 bytes 00013fd6
+ 0056aaf0 bytes 00013fd6
- 00547c60 ["INT_ADD", "register:40f0:8", ["const:547c60:8", "const:4:8"]]
- 00547c60 ["CALL", null, ["callee:00c57a80:8"]]
+ 0056aaf8 ["INT_ADD", "register:40f0:8", ["const:56aaf8:8", "const:4:8"]]
+ 0056aaf8 ["CALL", null, ["callee:00c57a80:8"]]
- 00547c60 bytes f44c1a94
+ 0056aaf8 bytes e2b31b94
~~~


<a id="compare-4523f24ab0fa726a0781a2986c8a0ef9"></a>

### [`00548094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548094.md) → [`0056af2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md) FUN_0056af2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00547c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005480cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548094.md#insn-005480cc) · [`005480e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548094.md#insn-005480e0) · [`005480e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548094.md#insn-005480e8)
- 新版 [`0056af64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md#insn-0056af64) · [`0056af78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md#insn-0056af78) · [`0056af80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md#insn-0056af80)

~~~diff
- 005480cc ["INT_ADD", "register:40f0:8", ["const:5480cc:8", "const:4:8"]]
- 005480cc ["CALL", null, ["callee:00c538e0:8"]]
+ 0056af64 ["INT_ADD", "register:40f0:8", ["const:56af64:8", "const:4:8"]]
+ 0056af64 ["CALL", null, ["callee:00c538e0:8"]]
- 005480cc bytes 713b1a94
+ 0056af64 bytes 5fa21b94
- 005480e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005480e0 ["INT_ADD", "register:40f0:8", ["const:5480e0:8", "const:4:8"]]
- 005480e0 ["CALLIND", null, ["register:0:8"]]
+ 0056af78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056af78 ["INT_ADD", "register:40f0:8", ["const:56af78:8", "const:4:8"]]
+ 0056af78 ["CALLIND", null, ["register:0:8"]]
- 005480e0 bytes 00013fd6
+ 0056af78 bytes 00013fd6
- 005480e8 ["INT_ADD", "register:40f0:8", ["const:5480e8:8", "const:4:8"]]
- 005480e8 ["CALL", null, ["callee:00c57a80:8"]]
+ 0056af80 ["INT_ADD", "register:40f0:8", ["const:56af80:8", "const:4:8"]]
+ 0056af80 ["CALL", null, ["callee:00c57a80:8"]]
- 005480e8 bytes d24b1a94
+ 0056af80 bytes c0b21b94
~~~


<a id="compare-5dc8da080e4194e198cb079c79c913ed"></a>

### [`00548104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548104.md) → [`0056af9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md) FUN_0056af9c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00547c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548104.md#insn-00548120) · [`00548140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548104.md#insn-00548140)
- 新版 [`0056afb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md#insn-0056afb8) · [`0056afd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md#insn-0056afd8)

~~~diff
- 00548120 ["INT_ADD", "register:40f0:8", ["const:548120:8", "const:4:8"]]
- 00548120 ["CALL", null, ["callee:00c538e0:8"]]
+ 0056afb8 ["INT_ADD", "register:40f0:8", ["const:56afb8:8", "const:4:8"]]
+ 0056afb8 ["CALL", null, ["callee:00c538e0:8"]]
- 00548120 bytes 5c3b1a94
+ 0056afb8 bytes 4aa21b94
- 00548140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00548140 ["INT_ADD", "register:40f0:8", ["const:548140:8", "const:4:8"]]
- 00548140 ["CALLIND", null, ["register:0:8"]]
+ 0056afd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056afd8 ["INT_ADD", "register:40f0:8", ["const:56afd8:8", "const:4:8"]]
+ 0056afd8 ["CALLIND", null, ["register:0:8"]]
- 00548140 bytes 00013fd6
+ 0056afd8 bytes 00013fd6
~~~


<a id="compare-de8b79cb3675a4712a5863fb79de018e"></a>

### [`005487a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487a8.md) → [`0056b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b640.md) FUN_0056b640

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005487c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487a8.md#insn-005487c4) · [`005487e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487a8.md#insn-005487e4)
- 新版 [`0056b65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b640.md#insn-0056b65c) · [`0056b67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b640.md#insn-0056b67c)

~~~diff
- 005487c4 ["INT_ADD", "register:40f0:8", ["const:5487c4:8", "const:4:8"]]
- 005487c4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0056b65c ["INT_ADD", "register:40f0:8", ["const:56b65c:8", "const:4:8"]]
+ 0056b65c ["CALL", null, ["callee:00c538e0:8"]]
- 005487c4 bytes b3391a94
+ 0056b65c bytes a1a01b94
- 005487e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005487e4 ["INT_ADD", "register:40f0:8", ["const:5487e4:8", "const:4:8"]]
- 005487e4 ["CALLIND", null, ["register:0:8"]]
+ 0056b67c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b67c ["INT_ADD", "register:40f0:8", ["const:56b67c:8", "const:4:8"]]
+ 0056b67c ["CALLIND", null, ["register:0:8"]]
- 005487e4 bytes 00013fd6
+ 0056b67c bytes 00013fd6
~~~


<a id="compare-d23fbc9d8598fb652ae510780a9e1841"></a>

### [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) → [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) FUN_0056b690

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0054e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e19c.md) [`0054e2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e2dc.md) · 呼出先 4件 [`005426ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md)
- 新版 呼出元 2件 [`00571034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md) [`00571174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md) · 呼出先 4件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md#insn-00548824) · [`00548838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md#insn-00548838) · [`00548848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md#insn-00548848)
- 新版 [`0056b6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md#insn-0056b6bc) · [`0056b6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md#insn-0056b6d0) · [`0056b6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md#insn-0056b6e0)

~~~diff
- 00548824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00548824 ["INT_ADD", "register:40f0:8", ["const:548824:8", "const:4:8"]]
- 00548824 ["CALLIND", null, ["register:0:8"]]
+ 0056b6bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b6bc ["INT_ADD", "register:40f0:8", ["const:56b6bc:8", "const:4:8"]]
+ 0056b6bc ["CALLIND", null, ["register:0:8"]]
- 00548824 bytes 00013fd6
+ 0056b6bc bytes 00013fd6
- 00548838 ["COPY", "register:0:8", ["register:4040:8"]]
- 00548838 ["INT_ADD", "register:40f0:8", ["const:548838:8", "const:4:8"]]
- 00548838 ["CALLIND", null, ["register:0:8"]]
+ 0056b6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b6d0 ["INT_ADD", "register:40f0:8", ["const:56b6d0:8", "const:4:8"]]
+ 0056b6d0 ["CALLIND", null, ["register:0:8"]]
- 00548838 bytes 00013fd6
+ 0056b6d0 bytes 00013fd6
- 00548848 ["INT_ADD", "register:40f0:8", ["const:548848:8", "const:4:8"]]
- 00548848 ["CALL", null, ["callee:00c59ce0:8"]]
+ 0056b6e0 ["INT_ADD", "register:40f0:8", ["const:56b6e0:8", "const:4:8"]]
+ 0056b6e0 ["CALL", null, ["callee:00c59ce0:8"]]
- 00548848 bytes 92521a94
+ 0056b6e0 bytes 80b91b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3116f24eea2d7598725f809801a20b9"></a>

### [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) → [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) FUN_0056b8cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0054873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054873c.md) [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) [`00549364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md) · 呼出先 5件 [`00546608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546608.md) [`00547a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547a3c.md) [`00bd6e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e00.md) [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md)
- 新版 呼出元 3件 [`0056b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b5d4.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) · 呼出先 5件 [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) [`0056a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md) [`00c53850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53850.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md#insn-00548a4c) · [`00548a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md#insn-00548a80) · [`00548a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md#insn-00548a94)
- 新版 [`0056b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md#insn-0056b8e4) · [`0056b918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md#insn-0056b918) · [`0056b92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md#insn-0056b92c)

~~~diff
- 00548a4c ["INT_ADD", "register:40f0:8", ["const:548a4c:8", "const:4:8"]]
- 00548a4c ["CALL", null, ["callee:00c59ce0:8"]]
+ 0056b8e4 ["INT_ADD", "register:40f0:8", ["const:56b8e4:8", "const:4:8"]]
+ 0056b8e4 ["CALL", null, ["callee:00c59ce0:8"]]
- 00548a4c bytes 11521a94
+ 0056b8e4 bytes ffb81b94
- 00548a80 ["INT_ADD", "register:40f0:8", ["const:548a80:8", "const:4:8"]]
- 00548a80 ["CALL", null, ["callee:0056a8d4:8"]]
+ 0056b918 ["INT_ADD", "register:40f0:8", ["const:56b918:8", "const:4:8"]]
+ 0056b918 ["CALL", null, ["callee:0056a8d4:8"]]
- 00548a80 bytes effbff97
+ 0056b918 bytes effbff97
- 00548a94 ["INT_ADD", "register:40f0:8", ["const:548a94:8", "const:4:8"]]
- 00548a94 ["CALL", null, ["callee:00c53850:8"]]
+ 0056b92c ["INT_ADD", "register:40f0:8", ["const:56b92c:8", "const:4:8"]]
+ 0056b92c ["CALL", null, ["callee:00c53850:8"]]
- 00548a94 bytes db381a94
+ 0056b92c bytes c99f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac79ae4c5a9921cd7326c66e8a32f5c5"></a>

### [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) → [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) FUN_0056b9e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00549868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549868.md) · 呼出先 12件 [`005426ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md) [`005467e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005467e0.md) [`0054729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md) [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 1件 [`0056c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c700.md) · 呼出先 12件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00569678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569678.md) [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md#insn-00548b7c) · [`00548b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md#insn-00548b94) · [`00548ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md#insn-00548ba4)
- 新版 [`0056ba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md#insn-0056ba14) · [`0056ba2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md#insn-0056ba2c) · [`0056ba3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md#insn-0056ba3c)

~~~diff
- 00548b7c ["INT_ADD", "register:40f0:8", ["const:548b7c:8", "const:4:8"]]
- 00548b7c ["CALL", null, ["callee:00c59ce0:8"]]
+ 0056ba14 ["INT_ADD", "register:40f0:8", ["const:56ba14:8", "const:4:8"]]
+ 0056ba14 ["CALL", null, ["callee:00c59ce0:8"]]
- 00548b7c bytes c5511a94
+ 0056ba14 bytes b3b81b94
- 00548b94 ["INT_ADD", "register:40f0:8", ["const:548b94:8", "const:4:8"]]
- 00548b94 ["CALL", null, ["callee:00565544:8"]]
+ 0056ba2c ["INT_ADD", "register:40f0:8", ["const:56ba2c:8", "const:4:8"]]
+ 0056ba2c ["CALL", null, ["callee:00565544:8"]]
- 00548b94 bytes c6e6ff97
+ 0056ba2c bytes c6e6ff97
- 00548ba4 ["INT_ADD", "register:40f0:8", ["const:548ba4:8", "const:4:8"]]
- 00548ba4 ["CALL", null, ["callee:00c58260:8"]]
+ 0056ba3c ["INT_ADD", "register:40f0:8", ["const:56ba3c:8", "const:4:8"]]
+ 0056ba3c ["CALL", null, ["callee:00c58260:8"]]
- 00548ba4 bytes 1b4b1a94
+ 0056ba3c bytes 09b21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-840244841e135852d060021f54b3b373"></a>

### [`00548e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548e1c.md) → [`0056bcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md) FUN_0056bcb4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00549624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549624.md) · 呼出先 5件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`0056c4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c4bc.md) · 呼出先 5件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548e1c.md#insn-00548e54) · [`00548e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548e1c.md#insn-00548e6c) · [`00548e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548e1c.md#insn-00548e80)
- 新版 [`0056bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md#insn-0056bcec) · [`0056bd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md#insn-0056bd04) · [`0056bd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md#insn-0056bd18)

~~~diff
- 00548e54 ["INT_ADD", "register:40f0:8", ["const:548e54:8", "const:4:8"]]
- 00548e54 ["CALL", null, ["callee:00c538b0:8"]]
+ 0056bcec ["INT_ADD", "register:40f0:8", ["const:56bcec:8", "const:4:8"]]
+ 0056bcec ["CALL", null, ["callee:00c538b0:8"]]
- 00548e54 bytes 03381a94
+ 0056bcec bytes f19e1b94
- 00548e6c ["INT_ADD", "register:40f0:8", ["const:548e6c:8", "const:4:8"]]
- 00548e6c ["CALL", null, ["callee:00c538e0:8"]]
+ 0056bd04 ["INT_ADD", "register:40f0:8", ["const:56bd04:8", "const:4:8"]]
+ 0056bd04 ["CALL", null, ["callee:00c538e0:8"]]
- 00548e6c bytes 09381a94
+ 0056bd04 bytes f79e1b94
- 00548e80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00548e80 ["INT_ADD", "register:40f0:8", ["const:548e80:8", "const:4:8"]]
- 00548e80 ["CALLIND", null, ["register:0:8"]]
+ 0056bd18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056bd18 ["INT_ADD", "register:40f0:8", ["const:56bd18:8", "const:4:8"]]
+ 0056bd18 ["CALLIND", null, ["register:0:8"]]
- 00548e80 bytes 00013fd6
+ 0056bd18 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c76dcd59b9eff341f50fe07fbf68d52"></a>

### [`00549128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549128.md) → [`0056bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md) FUN_0056bfc0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054915c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549128.md#insn-0054915c) · [`00549180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549128.md#insn-00549180) · [`005491a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549128.md#insn-005491a4)
- 新版 [`0056bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md#insn-0056bff4) · [`0056c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md#insn-0056c018) · [`0056c03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bfc0.md#insn-0056c03c)

~~~diff
- 0054915c ["COPY", "register:0:8", ["register:4040:8"]]
- 0054915c ["INT_ADD", "register:40f0:8", ["const:54915c:8", "const:4:8"]]
- 0054915c ["CALLIND", null, ["register:0:8"]]
+ 0056bff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056bff4 ["INT_ADD", "register:40f0:8", ["const:56bff4:8", "const:4:8"]]
+ 0056bff4 ["CALLIND", null, ["register:0:8"]]
- 0054915c bytes 00013fd6
+ 0056bff4 bytes 00013fd6
- 00549180 ["INT_ADD", "register:40f0:8", ["const:549180:8", "const:4:8"]]
- 00549180 ["CALL", null, ["callee:00c58020:8"]]
+ 0056c018 ["INT_ADD", "register:40f0:8", ["const:56c018:8", "const:4:8"]]
+ 0056c018 ["CALL", null, ["callee:00c58020:8"]]
- 00549180 bytes 14491a94
+ 0056c018 bytes 02b01b94
- 005491a4 ["INT_ADD", "register:40f0:8", ["const:5491a4:8", "const:4:8"]]
- 005491a4 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0056c03c ["INT_ADD", "register:40f0:8", ["const:56c03c:8", "const:4:8"]]
+ 0056c03c ["CALL", null, ["callee:00c57ae0:8"]]
- 005491a4 bytes bb471a94
+ 0056c03c bytes a9ae1b94
~~~


<a id="compare-e1d4e5bc002de9bd418672bf2f87f1f8"></a>

### [`005491c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005491c4.md) → [`0056c05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c05c.md) FUN_0056c05c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005491c4.md#insn-00549208) · [`00549238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005491c4.md#insn-00549238)
- 新版 [`0056c0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c05c.md#insn-0056c0a0) · [`0056c0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c05c.md#insn-0056c0d0)

~~~diff
- 00549208 ["COPY", "register:0:8", ["register:4048:8"]]
- 00549208 ["INT_ADD", "register:40f0:8", ["const:549208:8", "const:4:8"]]
- 00549208 ["CALLIND", null, ["register:0:8"]]
+ 0056c0a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0056c0a0 ["INT_ADD", "register:40f0:8", ["const:56c0a0:8", "const:4:8"]]
+ 0056c0a0 ["CALLIND", null, ["register:0:8"]]
- 00549208 bytes 20013fd6
+ 0056c0a0 bytes 20013fd6
- 00549238 ["INT_ADD", "register:40f0:8", ["const:549238:8", "const:4:8"]]
- 00549238 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0056c0d0 ["INT_ADD", "register:40f0:8", ["const:56c0d0:8", "const:4:8"]]
+ 0056c0d0 ["CALL", null, ["callee:00c57ae0:8"]]
- 00549238 bytes 96471a94
+ 0056c0d0 bytes 84ae1b94
~~~


<a id="compare-4df28f72bc16f8a4333cfb150f538190"></a>

### [`00549364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md) → [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) FUN_0056c1fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00549584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549584.md) · 呼出先 4件 [`00546608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546608.md) [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md)
- 新版 呼出元 1件 [`0056c41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c41c.md) · 呼出先 4件 [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md#insn-00549390) · [`005493a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md#insn-005493a4) · [`005493b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md#insn-005493b4)
- 新版 [`0056c228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md#insn-0056c228) · [`0056c23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md#insn-0056c23c) · [`0056c24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md#insn-0056c24c)

~~~diff
- 00549390 ["COPY", "register:0:8", ["register:4040:8"]]
- 00549390 ["INT_ADD", "register:40f0:8", ["const:549390:8", "const:4:8"]]
- 00549390 ["CALLIND", null, ["register:0:8"]]
+ 0056c228 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c228 ["INT_ADD", "register:40f0:8", ["const:56c228:8", "const:4:8"]]
+ 0056c228 ["CALLIND", null, ["register:0:8"]]
- 00549390 bytes 00013fd6
+ 0056c228 bytes 00013fd6
- 005493a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005493a4 ["INT_ADD", "register:40f0:8", ["const:5493a4:8", "const:4:8"]]
- 005493a4 ["CALLIND", null, ["register:0:8"]]
+ 0056c23c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c23c ["INT_ADD", "register:40f0:8", ["const:56c23c:8", "const:4:8"]]
+ 0056c23c ["CALLIND", null, ["register:0:8"]]
- 005493a4 bytes 00013fd6
+ 0056c23c bytes 00013fd6
- 005493b4 ["INT_ADD", "register:40f0:8", ["const:5493b4:8", "const:4:8"]]
- 005493b4 ["CALL", null, ["callee:00c59ce0:8"]]
+ 0056c24c ["INT_ADD", "register:40f0:8", ["const:56c24c:8", "const:4:8"]]
+ 0056c24c ["CALL", null, ["callee:00c59ce0:8"]]
- 005493b4 bytes b74f1a94
+ 0056c24c bytes a5b61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab5f97402854fb6e02ac2f78fd935a6a"></a>

### [`00549424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549424.md) → [`0056c2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c2bc.md) FUN_0056c2bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549424.md#insn-00549448) · [`00549464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549424.md#insn-00549464)
- 新版 [`0056c2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c2bc.md#insn-0056c2e0) · [`0056c2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c2bc.md#insn-0056c2fc)

~~~diff
- 00549448 ["INT_ADD", "register:40f0:8", ["const:549448:8", "const:4:8"]]
- 00549448 ["CALL", null, ["callee:00c59ce0:8"]]
+ 0056c2e0 ["INT_ADD", "register:40f0:8", ["const:56c2e0:8", "const:4:8"]]
+ 0056c2e0 ["CALL", null, ["callee:00c59ce0:8"]]
- 00549448 bytes 924f1a94
+ 0056c2e0 bytes 80b61b94
- 00549464 ["INT_ADD", "register:40f0:8", ["const:549464:8", "const:4:8"]]
- 00549464 ["CALL", null, ["callee:0056893c:8"]]
+ 0056c2fc ["INT_ADD", "register:40f0:8", ["const:56c2fc:8", "const:4:8"]]
+ 0056c2fc ["CALL", null, ["callee:0056893c:8"]]
- 00549464 bytes 90f1ff97
+ 0056c2fc bytes 90f1ff97
~~~


<a id="compare-c3b080cfef6f4a7270c5f4ff92ae50ca"></a>

### [`00549504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549504.md) → [`0056c39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c39c.md) FUN_0056c39c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549504.md#insn-00549538)
- 新版 [`0056c3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c39c.md#insn-0056c3d0)

~~~diff
- 00549538 ["INT_ADD", "register:40f0:8", ["const:549538:8", "const:4:8"]]
- 00549538 ["CALL", null, ["callee:00c59d00:8"]]
+ 0056c3d0 ["INT_ADD", "register:40f0:8", ["const:56c3d0:8", "const:4:8"]]
+ 0056c3d0 ["CALL", null, ["callee:00c59d00:8"]]
- 00549538 bytes 5e4f1a94
+ 0056c3d0 bytes 4cb61b94
~~~


<a id="compare-7ddb4df57d1aa346b270e4d59e7e6786"></a>

### [`00549590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549590.md) → [`0056c428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c428.md) FUN_0056c428

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005495e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549590.md#insn-005495e0) · [`00549620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549590.md#insn-00549620)
- 新版 [`0056c478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c428.md#insn-0056c478) · [`0056c4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c428.md#insn-0056c4b8)

~~~diff
- 005495e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005495e0 ["INT_ADD", "register:40f0:8", ["const:5495e0:8", "const:4:8"]]
- 005495e0 ["CALLIND", null, ["register:0:8"]]
+ 0056c478 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c478 ["INT_ADD", "register:40f0:8", ["const:56c478:8", "const:4:8"]]
+ 0056c478 ["CALLIND", null, ["register:0:8"]]
- 005495e0 bytes 00013fd6
+ 0056c478 bytes 00013fd6
- 00549620 ["INT_ADD", "register:40f0:8", ["const:549620:8", "const:4:8"]]
- 00549620 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0056c4b8 ["INT_ADD", "register:40f0:8", ["const:56c4b8:8", "const:4:8"]]
+ 0056c4b8 ["CALL", null, ["callee:00c57ae0:8"]]
- 00549620 bytes 9c461a94
+ 0056c4b8 bytes 8aad1b94
~~~


<a id="compare-d26b2a0c518e0144dd3c4e412aa00334"></a>

### [`00549814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549814.md) → [`0056c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6ac.md) FUN_0056c6ac

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549814.md#insn-00549830) · [`00549850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549814.md#insn-00549850)
- 新版 [`0056c6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6ac.md#insn-0056c6c8) · [`0056c6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6ac.md#insn-0056c6e8)

~~~diff
- 00549830 ["INT_ADD", "register:40f0:8", ["const:549830:8", "const:4:8"]]
- 00549830 ["CALL", null, ["callee:00c538e0:8"]]
+ 0056c6c8 ["INT_ADD", "register:40f0:8", ["const:56c6c8:8", "const:4:8"]]
+ 0056c6c8 ["CALL", null, ["callee:00c538e0:8"]]
- 00549830 bytes 98351a94
+ 0056c6c8 bytes 869c1b94
- 00549850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00549850 ["INT_ADD", "register:40f0:8", ["const:549850:8", "const:4:8"]]
- 00549850 ["CALLIND", null, ["register:0:8"]]
+ 0056c6e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c6e8 ["INT_ADD", "register:40f0:8", ["const:56c6e8:8", "const:4:8"]]
+ 0056c6e8 ["CALLIND", null, ["register:0:8"]]
- 00549850 bytes 00013fd6
+ 0056c6e8 bytes 00013fd6
~~~


<a id="compare-4cb27703efcd2ba6f5a5fbb84be8761f"></a>

### [`00549a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549a28.md) → [`0056c8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c8c0.md) FUN_0056c8c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549a28.md#insn-00549a44) · [`00549a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549a28.md#insn-00549a64)
- 新版 [`0056c8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c8c0.md#insn-0056c8dc) · [`0056c8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c8c0.md#insn-0056c8fc)

~~~diff
- 00549a44 ["INT_ADD", "register:40f0:8", ["const:549a44:8", "const:4:8"]]
- 00549a44 ["CALL", null, ["callee:00c538e0:8"]]
+ 0056c8dc ["INT_ADD", "register:40f0:8", ["const:56c8dc:8", "const:4:8"]]
+ 0056c8dc ["CALL", null, ["callee:00c538e0:8"]]
- 00549a44 bytes 13351a94
+ 0056c8dc bytes 019c1b94
- 00549a64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00549a64 ["INT_ADD", "register:40f0:8", ["const:549a64:8", "const:4:8"]]
- 00549a64 ["CALLIND", null, ["register:0:8"]]
+ 0056c8fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c8fc ["INT_ADD", "register:40f0:8", ["const:56c8fc:8", "const:4:8"]]
+ 0056c8fc ["CALLIND", null, ["register:0:8"]]
- 00549a64 bytes 00013fd6
+ 0056c8fc bytes 00013fd6
~~~


<a id="compare-5244237ac035bd8c867d12f0ed385cb1"></a>

### [`00549a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549a78.md) → [`0056c910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c910.md) FUN_0056c910

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549a78.md#insn-00549a94) · [`00549ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549a78.md#insn-00549ab4)
- 新版 [`0056c92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c910.md#insn-0056c92c) · [`0056c94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c910.md#insn-0056c94c)

~~~diff
- 00549a94 ["INT_ADD", "register:40f0:8", ["const:549a94:8", "const:4:8"]]
- 00549a94 ["CALL", null, ["callee:00c538e0:8"]]
+ 0056c92c ["INT_ADD", "register:40f0:8", ["const:56c92c:8", "const:4:8"]]
+ 0056c92c ["CALL", null, ["callee:00c538e0:8"]]
- 00549a94 bytes ff341a94
+ 0056c92c bytes ed9b1b94
- 00549ab4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00549ab4 ["INT_ADD", "register:40f0:8", ["const:549ab4:8", "const:4:8"]]
- 00549ab4 ["CALLIND", null, ["register:0:8"]]
+ 0056c94c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056c94c ["INT_ADD", "register:40f0:8", ["const:56c94c:8", "const:4:8"]]
+ 0056c94c ["CALLIND", null, ["register:0:8"]]
- 00549ab4 bytes 00013fd6
+ 0056c94c bytes 00013fd6
~~~


<a id="compare-f291c22bb5cdf533aeaa308f26773ea9"></a>

### [`00549ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549ac8.md) → [`0056c960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md) FUN_0056c960

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052daac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daac.md) · 呼出先 5件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00549868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549868.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00550944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550944.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`0056c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c700.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549ac8.md#insn-00549af8) · [`00549b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549ac8.md#insn-00549b08) · [`00549b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549ac8.md#insn-00549b1c)
- 新版 [`0056c990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md#insn-0056c990) · [`0056c9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md#insn-0056c9a0) · [`0056c9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c960.md#insn-0056c9b4)

~~~diff
- 00549af8 ["INT_ADD", "register:40f0:8", ["const:549af8:8", "const:4:8"]]
- 00549af8 ["CALL", null, ["callee:00550b64:8"]]
+ 0056c990 ["INT_ADD", "register:40f0:8", ["const:56c990:8", "const:4:8"]]
+ 0056c990 ["CALL", null, ["callee:00550b64:8"]]
- 00549af8 bytes 7590ff97
+ 0056c990 bytes 7590ff97
- 00549b08 ["INT_ADD", "register:40f0:8", ["const:549b08:8", "const:4:8"]]
- 00549b08 ["CALL", null, ["callee:0056c700:8"]]
+ 0056c9a0 ["INT_ADD", "register:40f0:8", ["const:56c9a0:8", "const:4:8"]]
+ 0056c9a0 ["CALL", null, ["callee:0056c700:8"]]
- 00549b08 bytes 58ffff97
+ 0056c9a0 bytes 58ffff97
- 00549b1c ["INT_ADD", "register:40f0:8", ["const:549b1c:8", "const:4:8"]]
- 00549b1c ["CALL", null, ["callee:00c538e0:8"]]
+ 0056c9b4 ["INT_ADD", "register:40f0:8", ["const:56c9b4:8", "const:4:8"]]
+ 0056c9b4 ["CALL", null, ["callee:00c538e0:8"]]
- 00549b1c bytes dd341a94
+ 0056c9b4 bytes cb9b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d736c82ce381fb2aa8c1a9427528fd4"></a>

### [`00549f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md) → [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) FUN_0056ce0c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) [`00549b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549b88.md) [`00549f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md) · 呼出先 2件 [`00549f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md) [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md)
- 新版 呼出元 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) · 呼出先 2件 [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md#insn-00549fb8) · [`0054a014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md#insn-0054a014) · [`0054a088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md#insn-0054a088)
- 新版 [`0056ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md#insn-0056ce50) · [`0056ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md#insn-0056ceac) · [`0056cf20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md#insn-0056cf20)

~~~diff
- 00549fb8 ["INT_ADD", "register:40f0:8", ["const:549fb8:8", "const:4:8"]]
- 00549fb8 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056ce50 ["INT_ADD", "register:40f0:8", ["const:56ce50:8", "const:4:8"]]
+ 0056ce50 ["CALL", null, ["callee:0056d02c:8"]]
- 00549fb8 bytes 77000094
+ 0056ce50 bytes 77000094
- 0054a014 ["INT_ADD", "register:40f0:8", ["const:54a014:8", "const:4:8"]]
- 0054a014 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056ceac ["INT_ADD", "register:40f0:8", ["const:56ceac:8", "const:4:8"]]
+ 0056ceac ["CALL", null, ["callee:0056d02c:8"]]
- 0054a014 bytes 60000094
+ 0056ceac bytes 60000094
- 0054a088 ["INT_ADD", "register:40f0:8", ["const:54a088:8", "const:4:8"]]
- 0054a088 ["CALL", null, ["local:b0:8"]]
+ 0056cf20 ["INT_ADD", "register:40f0:8", ["const:56cf20:8", "const:4:8"]]
+ 0056cf20 ["CALL", null, ["local:b0:8"]]
- 0054a088 bytes bbffff97
+ 0056cf20 bytes bbffff97
~~~


<a id="compare-1fa1c83a79bc9723c88810df8b46c953"></a>

### [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md) → [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) FUN_0056d02c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`00549b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549b88.md) [`00549f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md) · 呼出先 2件 [`0054a408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md) [`00bdd220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd220.md)
- 新版 呼出元 10件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) · 呼出先 2件 [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md#insn-0054a1f8) · [`0054a298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md#insn-0054a298)
- 新版 [`0056d090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md#insn-0056d090) · [`0056d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md#insn-0056d130)

~~~diff
- 0054a1f8 ["INT_ADD", "register:40f0:8", ["const:54a1f8:8", "const:4:8"]]
- 0054a1f8 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056d090 ["INT_ADD", "register:40f0:8", ["const:56d090:8", "const:4:8"]]
+ 0056d090 ["CALL", null, ["callee:00c59c70:8"]]
- 0054a1f8 bytes 0a4c1a94
+ 0056d090 bytes f8b21b94
- 0054a298 ["INT_ADD", "register:40f0:8", ["const:54a298:8", "const:4:8"]]
- 0054a298 ["CALL", null, ["callee:0056d2a0:8"]]
+ 0056d130 ["INT_ADD", "register:40f0:8", ["const:56d130:8", "const:4:8"]]
+ 0056d130 ["CALL", null, ["callee:0056d2a0:8"]]
- 0054a298 bytes 5c000094
+ 0056d130 bytes 5c000094
~~~


<a id="compare-c5c1ba62ea553233f74d3069aa6a796e"></a>

### [`0054a2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a2d4.md) → [`0056d16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d16c.md) FUN_0056d16c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 1件 [`0054a408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a2d4.md#insn-0054a35c)
- 新版 [`0056d1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d16c.md#insn-0056d1f4)

~~~diff
- 0054a35c ["INT_ADD", "register:40f0:8", ["const:54a35c:8", "const:4:8"]]
- 0054a35c ["CALL", null, ["callee:0056d2a0:8"]]
+ 0056d1f4 ["INT_ADD", "register:40f0:8", ["const:56d1f4:8", "const:4:8"]]
+ 0056d1f4 ["CALL", null, ["callee:0056d2a0:8"]]
- 0054a35c bytes 2b000094
+ 0056d1f4 bytes 2b000094
~~~


<a id="compare-872534a844d84aff4986a1d9ab43daa0"></a>

### [`0054a398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a398.md) → [`0056d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d230.md) FUN_0056d230

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) [`0054645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/0054645c.md) · 呼出先 1件 [`00bdd220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd220.md)
- 新版 呼出元 2件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) · 呼出先 1件 [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a398.md#insn-0054a3d0)
- 新版 [`0056d268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d230.md#insn-0056d268)

~~~diff
- 0054a3d0 ["INT_ADD", "register:40f0:8", ["const:54a3d0:8", "const:4:8"]]
- 0054a3d0 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056d268 ["INT_ADD", "register:40f0:8", ["const:56d268:8", "const:4:8"]]
+ 0056d268 ["CALL", null, ["callee:00c59c70:8"]]
- 0054a3d0 bytes 944b1a94
+ 0056d268 bytes 82b21b94
~~~


<a id="compare-7b0f9dabd3069876e6760d8823d1de44"></a>

### [`0054a408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md) → [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) FUN_0056d2a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`0054645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/0054645c.md) [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md) [`0054a2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a2d4.md) · 呼出先 2件 [`0054a560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a560.md) [`00bdd220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd220.md)
- 新版 呼出元 6件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d16c.md) · 呼出先 2件 [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md#insn-0054a448) · [`0054a490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md#insn-0054a490) · [`0054a4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md#insn-0054a4d8)
- 新版 [`0056d2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md#insn-0056d2e0) · [`0056d328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md#insn-0056d328) · [`0056d370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md#insn-0056d370)

~~~diff
- 0054a448 ["INT_ADD", "register:40f0:8", ["const:54a448:8", "const:4:8"]]
- 0054a448 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056d2e0 ["INT_ADD", "register:40f0:8", ["const:56d2e0:8", "const:4:8"]]
+ 0056d2e0 ["CALL", null, ["callee:00c59c70:8"]]
- 0054a448 bytes 764b1a94
+ 0056d2e0 bytes 64b21b94
- 0054a490 ["INT_ADD", "register:40f0:8", ["const:54a490:8", "const:4:8"]]
- 0054a490 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056d328 ["INT_ADD", "register:40f0:8", ["const:56d328:8", "const:4:8"]]
+ 0056d328 ["CALL", null, ["callee:00c59c70:8"]]
- 0054a490 bytes 644b1a94
+ 0056d328 bytes 52b21b94
- 0054a4d8 ["INT_ADD", "register:40f0:8", ["const:54a4d8:8", "const:4:8"]]
- 0054a4d8 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056d370 ["INT_ADD", "register:40f0:8", ["const:56d370:8", "const:4:8"]]
+ 0056d370 ["CALL", null, ["callee:00c59c70:8"]]
- 0054a4d8 bytes 524b1a94
+ 0056d370 bytes 40b21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6834bccc42855fc43c113bf2f5a3ddb"></a>

### [`0054a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a8fc.md) → [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md) FUN_0056d794

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) [`0054aaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md) [`0054c078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c078.md) [`0054c2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c2cc.md) · 呼出先 1件 [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md)
- 新版 呼出元 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) [`0056ef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md) [`0056f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md) · 呼出先 1件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a8fc.md#insn-0054a938)
- 新版 [`0056d7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md#insn-0056d7d0)

~~~diff
- 0054a938 ["INT_ADD", "register:40f0:8", ["const:54a938:8", "const:4:8"]]
- 0054a938 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056d7d0 ["INT_ADD", "register:40f0:8", ["const:56d7d0:8", "const:4:8"]]
+ 0056d7d0 ["CALL", null, ["callee:0056d02c:8"]]
- 0054a938 bytes 17feff97
+ 0056d7d0 bytes 17feff97
~~~


<a id="compare-f234f61e72b767b4d524e4f64994d35e"></a>

### [`0054aaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md) → [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) FUN_0056d93c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) · 呼出先 6件 [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md) [`0054a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a8fc.md) [`0054c078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c078.md) [`0054c2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) · 呼出先 6件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md) [`0056ef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md) [`0056f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md#insn-0054ac28) · [`0054ada4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md#insn-0054ada4) · [`0054af18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md#insn-0054af18)
- 新版 [`0056dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md#insn-0056dac0) · [`0056dc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md#insn-0056dc3c) · [`0056ddb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md#insn-0056ddb0)

~~~diff
- 0054ac28 ["INT_ADD", "register:40f0:8", ["const:54ac28:8", "const:4:8"]]
- 0054ac28 ["CALL", null, ["callee:00c57c90:8"]]
+ 0056dac0 ["INT_ADD", "register:40f0:8", ["const:56dac0:8", "const:4:8"]]
+ 0056dac0 ["CALL", null, ["callee:00c57c90:8"]]
- 0054ac28 bytes 86411a94
+ 0056dac0 bytes 74a81b94
- 0054ada4 ["INT_ADD", "register:40f0:8", ["const:54ada4:8", "const:4:8"]]
- 0054ada4 ["CALL", null, ["callee:0056f164:8"]]
+ 0056dc3c ["INT_ADD", "register:40f0:8", ["const:56dc3c:8", "const:4:8"]]
+ 0056dc3c ["CALL", null, ["callee:0056f164:8"]]
- 0054ada4 bytes 4a050094
+ 0056dc3c bytes 4a050094
- 0054af18 ["INT_ADD", "register:40f0:8", ["const:54af18:8", "const:4:8"]]
- 0054af18 ["CALL", null, ["callee:0056f164:8"]]
+ 0056ddb0 ["INT_ADD", "register:40f0:8", ["const:56ddb0:8", "const:4:8"]]
+ 0056ddb0 ["CALL", null, ["callee:0056f164:8"]]
- 0054af18 bytes ed040094
+ 0056ddb0 bytes ed040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e317411df8cdbc1cf4104634d783f1"></a>

### [`0054c078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c078.md) → [`0056ef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md) FUN_0056ef10

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054aaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md) · 呼出先 2件 [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md) [`0054a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a8fc.md)
- 新版 呼出元 1件 [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) · 呼出先 2件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c078.md#insn-0054c114) · [`0054c184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c078.md#insn-0054c184)
- 新版 [`0056efac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md#insn-0056efac) · [`0056f01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md#insn-0056f01c)

~~~diff
- 0054c114 ["INT_ADD", "register:40f0:8", ["const:54c114:8", "const:4:8"]]
- 0054c114 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056efac ["INT_ADD", "register:40f0:8", ["const:56efac:8", "const:4:8"]]
+ 0056efac ["CALL", null, ["callee:0056d02c:8"]]
- 0054c114 bytes 20f8ff97
+ 0056efac bytes 20f8ff97
- 0054c184 ["INT_ADD", "register:40f0:8", ["const:54c184:8", "const:4:8"]]
- 0054c184 ["CALL", null, ["callee:0056d794:8"]]
+ 0056f01c ["INT_ADD", "register:40f0:8", ["const:56f01c:8", "const:4:8"]]
+ 0056f01c ["CALL", null, ["callee:0056d794:8"]]
- 0054c184 bytes def9ff97
+ 0056f01c bytes def9ff97
~~~


<a id="compare-75caec1c86ebb48e6c23c2c0e36579b0"></a>

### [`0054c2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c2cc.md) → [`0056f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md) FUN_0056f164

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054aaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md) · 呼出先 2件 [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md) [`0054a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a8fc.md)
- 新版 呼出元 1件 [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) · 呼出先 2件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c2cc.md#insn-0054c310) · [`0054c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c2cc.md#insn-0054c390)
- 新版 [`0056f1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md#insn-0056f1a8) · [`0056f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md#insn-0056f228)

~~~diff
- 0054c310 ["INT_ADD", "register:40f0:8", ["const:54c310:8", "const:4:8"]]
- 0054c310 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056f1a8 ["INT_ADD", "register:40f0:8", ["const:56f1a8:8", "const:4:8"]]
+ 0056f1a8 ["CALL", null, ["callee:0056d02c:8"]]
- 0054c310 bytes a1f7ff97
+ 0056f1a8 bytes a1f7ff97
- 0054c390 ["INT_ADD", "register:40f0:8", ["const:54c390:8", "const:4:8"]]
- 0054c390 ["CALL", null, ["callee:0056d794:8"]]
+ 0056f228 ["INT_ADD", "register:40f0:8", ["const:56f228:8", "const:4:8"]]
+ 0056f228 ["CALL", null, ["callee:0056d794:8"]]
- 0054c390 bytes 5bf9ff97
+ 0056f228 bytes 5bf9ff97
~~~


<a id="compare-6e8a9cbaea9a88ae0d52bb1f971b2f3a"></a>

### [`0054c660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c660.md) → [`0056f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f4f8.md) FUN_0056f4f8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 1件 [`0054a408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c660.md#insn-0054c680)
- 新版 [`0056f518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f4f8.md#insn-0056f518)

~~~diff
- 0054c680 ["INT_ADD", "register:40f0:8", ["const:54c680:8", "const:4:8"]]
- 0054c680 ["CALL", null, ["callee:0056d2a0:8"]]
+ 0056f518 ["INT_ADD", "register:40f0:8", ["const:56f518:8", "const:4:8"]]
+ 0056f518 ["CALL", null, ["callee:0056d2a0:8"]]
- 0054c680 bytes 62f7ff97
+ 0056f518 bytes 62f7ff97
~~~


<a id="compare-740b82e079c5e9eadfaed0c111113570"></a>

### [`0054c6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c6c0.md) → [`0056f558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md) FUN_0056f558

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 1件 [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c6c0.md#insn-0054c6d0) · [`0054c6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c6c0.md#insn-0054c6e0) · [`0054c6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c6c0.md#insn-0054c6f0)
- 新版 [`0056f568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md#insn-0056f568) · [`0056f578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md#insn-0056f578) · [`0056f588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md#insn-0056f588)

~~~diff
- 0054c6d0 ["INT_ADD", "register:40f0:8", ["const:54c6d0:8", "const:4:8"]]
- 0054c6d0 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056f568 ["INT_ADD", "register:40f0:8", ["const:56f568:8", "const:4:8"]]
+ 0056f568 ["CALL", null, ["callee:0056d02c:8"]]
- 0054c6d0 bytes b1f6ff97
+ 0056f568 bytes b1f6ff97
- 0054c6e0 ["INT_ADD", "register:40f0:8", ["const:54c6e0:8", "const:4:8"]]
- 0054c6e0 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056f578 ["INT_ADD", "register:40f0:8", ["const:56f578:8", "const:4:8"]]
+ 0056f578 ["CALL", null, ["callee:0056d02c:8"]]
- 0054c6e0 bytes adf6ff97
+ 0056f578 bytes adf6ff97
- 0054c6f0 ["INT_ADD", "register:40f0:8", ["const:54c6f0:8", "const:4:8"]]
- 0054c6f0 ["CALL", null, ["callee:0056d02c:8"]]
+ 0056f588 ["INT_ADD", "register:40f0:8", ["const:56f588:8", "const:4:8"]]
+ 0056f588 ["CALL", null, ["callee:0056d02c:8"]]
- 0054c6f0 bytes a9f6ff97
+ 0056f588 bytes a9f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6973d681db4ff0ccf42550cbf79fe93f"></a>

### [`0054c76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c76c.md) → [`0056f604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f604.md) FUN_0056f604

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd200.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 2件 [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c76c.md#insn-0054c7b8)
- 新版 [`0056f650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f604.md#insn-0056f650)

~~~diff
- 0054c7b8 ["INT_ADD", "register:40f0:8", ["const:54c7b8:8", "const:4:8"]]
- 0054c7b8 ["CALL", null, ["callee:00c59c50:8"]]
+ 0056f650 ["INT_ADD", "register:40f0:8", ["const:56f650:8", "const:4:8"]]
+ 0056f650 ["CALL", null, ["callee:00c59c50:8"]]
- 0054c7b8 bytes 92421a94
+ 0056f650 bytes 80a91b94
~~~


<a id="compare-467f2e321149d50271d90cd1e499b29a"></a>

### [`0054cd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cd24.md) → [`0056fbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fbbc.md) FUN_0056fbbc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054cd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cd24.md#insn-0054cd44)
- 新版 [`0056fbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fbbc.md#insn-0056fbdc)

~~~diff
- 0054cd44 ["INT_ADD", "register:40f0:8", ["const:54cd44:8", "const:4:8"]]
- 0054cd44 ["CALL", null, ["callee:00c57c90:8"]]
+ 0056fbdc ["INT_ADD", "register:40f0:8", ["const:56fbdc:8", "const:4:8"]]
+ 0056fbdc ["CALL", null, ["callee:00c57c90:8"]]
- 0054cd44 bytes 3f391a94
+ 0056fbdc bytes 2da01b94
~~~


<a id="compare-7e06b601a00bc95ca78fd3cd8d703ab9"></a>

### [`0054cdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cdf0.md) → [`0056fc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md) FUN_0056fc88

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 3件 [`00bdb5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdd190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd190.md) [`00bdd2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2c0.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 3件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c59be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59be0.md) [`00c59d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054ce14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cdf0.md#insn-0054ce14) · [`0054ce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cdf0.md#insn-0054ce20) · [`0054ce48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cdf0.md#insn-0054ce48)
- 新版 [`0056fcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md#insn-0056fcac) · [`0056fcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md#insn-0056fcb8) · [`0056fce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md#insn-0056fce0)

~~~diff
- 0054ce14 ["INT_ADD", "register:40f0:8", ["const:54ce14:8", "const:4:8"]]
- 0054ce14 ["CALL", null, ["callee:00c59be0:8"]]
+ 0056fcac ["INT_ADD", "register:40f0:8", ["const:56fcac:8", "const:4:8"]]
+ 0056fcac ["CALL", null, ["callee:00c59be0:8"]]
- 0054ce14 bytes df401a94
+ 0056fcac bytes cda71b94
- 0054ce20 ["INT_ADD", "register:40f0:8", ["const:54ce20:8", "const:4:8"]]
- 0054ce20 ["CALL", null, ["callee:00c59d10:8"]]
+ 0056fcb8 ["INT_ADD", "register:40f0:8", ["const:56fcb8:8", "const:4:8"]]
+ 0056fcb8 ["CALL", null, ["callee:00c59d10:8"]]
- 0054ce20 bytes 28411a94
+ 0056fcb8 bytes 16a81b94
- 0054ce48 ["INT_ADD", "register:40f0:8", ["const:54ce48:8", "const:4:8"]]
- 0054ce48 ["CALL", null, ["callee:00c58040:8"]]
+ 0056fce0 ["INT_ADD", "register:40f0:8", ["const:56fce0:8", "const:4:8"]]
+ 0056fce0 ["CALL", null, ["callee:00c58040:8"]]
- 0054ce48 bytes ea391a94
+ 0056fce0 bytes d8a01b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f591a95db1460513fffd03afdfea41d9"></a>

### [`0054da70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054da70.md) → [`00570908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md) FUN_00570908

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1c0.md) [`00bdd200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd200.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd230.md)
- 新版 呼出元 1件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c10.md) [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md) [`00c59c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054dac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054da70.md#insn-0054dac8) · [`0054db18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054da70.md#insn-0054db18) · [`0054dbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054da70.md#insn-0054dbac)
- 新版 [`00570960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md#insn-00570960) · [`005709b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md#insn-005709b0) · [`00570a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md#insn-00570a44)

~~~diff
- 0054dac8 ["INT_ADD", "register:40f0:8", ["const:54dac8:8", "const:4:8"]]
- 0054dac8 ["CALL", null, ["callee:00c59c50:8"]]
+ 00570960 ["INT_ADD", "register:40f0:8", ["const:570960:8", "const:4:8"]]
+ 00570960 ["CALL", null, ["callee:00c59c50:8"]]
- 0054dac8 bytes ce3d1a94
+ 00570960 bytes bca41b94
- 0054db18 ["INT_ADD", "register:40f0:8", ["const:54db18:8", "const:4:8"]]
- 0054db18 ["CALL", null, ["callee:00c59c80:8"]]
+ 005709b0 ["INT_ADD", "register:40f0:8", ["const:5709b0:8", "const:4:8"]]
+ 005709b0 ["CALL", null, ["callee:00c59c80:8"]]
- 0054db18 bytes c63d1a94
+ 005709b0 bytes b4a41b94
- 0054dbac ["INT_ADD", "register:40f0:8", ["const:54dbac:8", "const:4:8"]]
- 0054dbac ["CALL", null, ["callee:00c59d30:8"]]
+ 00570a44 ["INT_ADD", "register:40f0:8", ["const:570a44:8", "const:4:8"]]
+ 00570a44 ["CALL", null, ["callee:00c59d30:8"]]
- 0054dbac bytes cd3d1a94
+ 00570a44 bytes bba41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f85ca4eb91cb37d487c0c9c17fd7932c"></a>

### [`0054df6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df6c.md) → [`00570e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md) FUN_00570e04

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00547c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0054e0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e0c8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00570f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f60.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054dfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df6c.md#insn-0054dfd8) · [`0054e004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df6c.md#insn-0054e004) · [`0054e064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df6c.md#insn-0054e064)
- 新版 [`00570e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md#insn-00570e70) · [`00570e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md#insn-00570e9c) · [`00570efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md#insn-00570efc)

~~~diff
- 0054dfd8 ["INT_ADD", "register:40f0:8", ["const:54dfd8:8", "const:4:8"]]
- 0054dfd8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00570e70 ["INT_ADD", "register:40f0:8", ["const:570e70:8", "const:4:8"]]
+ 00570e70 ["CALL", null, ["callee:00c57a90:8"]]
- 0054dfd8 bytes 1a341a94
+ 00570e70 bytes 089b1b94
- 0054e004 ["INT_ADD", "register:40f0:8", ["const:54e004:8", "const:4:8"]]
- 0054e004 ["CALL", null, ["callee:00c538b0:8"]]
+ 00570e9c ["INT_ADD", "register:40f0:8", ["const:570e9c:8", "const:4:8"]]
+ 00570e9c ["CALL", null, ["callee:00c538b0:8"]]
- 0054e004 bytes 97231a94
+ 00570e9c bytes 858a1b94
- 0054e064 ["INT_ADD", "register:40f0:8", ["const:54e064:8", "const:4:8"]]
- 0054e064 ["CALL", null, ["callee:00c538e0:8"]]
+ 00570efc ["INT_ADD", "register:40f0:8", ["const:570efc:8", "const:4:8"]]
+ 00570efc ["CALL", null, ["callee:00c538e0:8"]]
- 0054e064 bytes 8b231a94
+ 00570efc bytes 798a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4202fa02dfe32c1736476c00dd5714a"></a>

### [`0054e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e19c.md) → [`00571034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md) FUN_00571034

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e19c.md#insn-0054e1b0) · [`0054e1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e19c.md#insn-0054e1c4) · [`0054e1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e19c.md#insn-0054e1e4)
- 新版 [`00571048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md#insn-00571048) · [`0057105c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md#insn-0057105c) · [`0057107c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md#insn-0057107c)

~~~diff
- 0054e1b0 ["INT_ADD", "register:40f0:8", ["const:54e1b0:8", "const:4:8"]]
- 0054e1b0 ["CALL", null, ["callee:0056b690:8"]]
+ 00571048 ["INT_ADD", "register:40f0:8", ["const:571048:8", "const:4:8"]]
+ 00571048 ["CALL", null, ["callee:0056b690:8"]]
- 0054e1b0 bytes 92e9ff97
+ 00571048 bytes 92e9ff97
- 0054e1c4 ["INT_ADD", "register:40f0:8", ["const:54e1c4:8", "const:4:8"]]
- 0054e1c4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057105c ["INT_ADD", "register:40f0:8", ["const:57105c:8", "const:4:8"]]
+ 0057105c ["CALL", null, ["callee:00c538e0:8"]]
- 0054e1c4 bytes 33231a94
+ 0057105c bytes 218a1b94
- 0054e1e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054e1e4 ["INT_ADD", "register:40f0:8", ["const:54e1e4:8", "const:4:8"]]
- 0054e1e4 ["CALLIND", null, ["register:0:8"]]
+ 0057107c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057107c ["INT_ADD", "register:40f0:8", ["const:57107c:8", "const:4:8"]]
+ 0057107c ["CALLIND", null, ["register:0:8"]]
- 0054e1e4 bytes 00013fd6
+ 0057107c bytes 00013fd6
~~~


<a id="compare-93596e16f589d752e0e17df556429918"></a>

### [`0054e2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e2dc.md) → [`00571174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md) FUN_00571174

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e2dc.md#insn-0054e2f0) · [`0054e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e2dc.md#insn-0054e304) · [`0054e324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e2dc.md#insn-0054e324)
- 新版 [`00571188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md#insn-00571188) · [`0057119c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md#insn-0057119c) · [`005711bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md#insn-005711bc)

~~~diff
- 0054e2f0 ["INT_ADD", "register:40f0:8", ["const:54e2f0:8", "const:4:8"]]
- 0054e2f0 ["CALL", null, ["callee:0056b690:8"]]
+ 00571188 ["INT_ADD", "register:40f0:8", ["const:571188:8", "const:4:8"]]
+ 00571188 ["CALL", null, ["callee:0056b690:8"]]
- 0054e2f0 bytes 42e9ff97
+ 00571188 bytes 42e9ff97
- 0054e304 ["INT_ADD", "register:40f0:8", ["const:54e304:8", "const:4:8"]]
- 0054e304 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057119c ["INT_ADD", "register:40f0:8", ["const:57119c:8", "const:4:8"]]
+ 0057119c ["CALL", null, ["callee:00c538e0:8"]]
- 0054e304 bytes e3221a94
+ 0057119c bytes d1891b94
- 0054e324 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054e324 ["INT_ADD", "register:40f0:8", ["const:54e324:8", "const:4:8"]]
- 0054e324 ["CALLIND", null, ["register:0:8"]]
+ 005711bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005711bc ["INT_ADD", "register:40f0:8", ["const:5711bc:8", "const:4:8"]]
+ 005711bc ["CALLIND", null, ["register:0:8"]]
- 0054e324 bytes 00013fd6
+ 005711bc bytes 00013fd6
~~~


<a id="compare-db490148c30e2c4285036f3cd79f461d"></a>

### [`0054e928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md) → [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) FUN_005717c0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dab4.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0055094c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055094c.md) · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md#insn-0054e948) · [`0054e950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md#insn-0054e950) · [`0054e994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md#insn-0054e994)
- 新版 [`005717e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md#insn-005717e0) · [`005717e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md#insn-005717e8) · [`0057182c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md#insn-0057182c)

~~~diff
- 0054e948 ["INT_ADD", "register:40f0:8", ["const:54e948:8", "const:4:8"]]
- 0054e948 ["CALL", null, ["callee:00588e2c:8"]]
+ 005717e0 ["INT_ADD", "register:40f0:8", ["const:5717e0:8", "const:4:8"]]
+ 005717e0 ["CALL", null, ["callee:00588e2c:8"]]
- 0054e948 bytes 935d0094
+ 005717e0 bytes 935d0094
- 0054e950 ["INT_ADD", "register:40f0:8", ["const:54e950:8", "const:4:8"]]
- 0054e950 ["CALL", null, ["callee:0058911c:8"]]
+ 005717e8 ["INT_ADD", "register:40f0:8", ["const:5717e8:8", "const:4:8"]]
+ 005717e8 ["CALL", null, ["callee:0058911c:8"]]
- 0054e950 bytes 4d5e0094
+ 005717e8 bytes 4d5e0094
- 0054e994 ["INT_ADD", "register:40f0:8", ["const:54e994:8", "const:4:8"]]
- 0054e994 ["CALL", null, ["callee:005892e0:8"]]
+ 0057182c ["INT_ADD", "register:40f0:8", ["const:57182c:8", "const:4:8"]]
+ 0057182c ["CALL", null, ["callee:005892e0:8"]]
- 0054e994 bytes ad5e0094
+ 0057182c bytes ad5e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b02c7894d751e0613b1b419f1a131b9"></a>

### [`0054f98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f98c.md) → [`00572824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572824.md) FUN_00572824

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054f9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f98c.md#insn-0054f9a8) · [`0054f9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f98c.md#insn-0054f9c8)
- 新版 [`00572840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572824.md#insn-00572840) · [`00572860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572824.md#insn-00572860)

~~~diff
- 0054f9a8 ["INT_ADD", "register:40f0:8", ["const:54f9a8:8", "const:4:8"]]
- 0054f9a8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00572840 ["INT_ADD", "register:40f0:8", ["const:572840:8", "const:4:8"]]
+ 00572840 ["CALL", null, ["callee:00c538e0:8"]]
- 0054f9a8 bytes 3a1d1a94
+ 00572840 bytes 28841b94
- 0054f9c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054f9c8 ["INT_ADD", "register:40f0:8", ["const:54f9c8:8", "const:4:8"]]
- 0054f9c8 ["CALLIND", null, ["register:0:8"]]
+ 00572860 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00572860 ["INT_ADD", "register:40f0:8", ["const:572860:8", "const:4:8"]]
+ 00572860 ["CALLIND", null, ["register:0:8"]]
- 0054f9c8 bytes 00013fd6
+ 00572860 bytes 00013fd6
~~~


<a id="compare-c154a21697b8b3a11388c5e9d4c96c87"></a>

### [`0055154c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/0055154c.md) → [`005743e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md) FUN_005743e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551850.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005746e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005746e8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/0055154c.md#insn-00551574) · [`00551598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/0055154c.md#insn-00551598)
- 新版 [`0057440c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md#insn-0057440c) · [`00574430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md#insn-00574430)

~~~diff
- 00551574 ["INT_ADD", "register:40f0:8", ["const:551574:8", "const:4:8"]]
- 00551574 ["CALL", null, ["callee:005746e8:8"]]
+ 0057440c ["INT_ADD", "register:40f0:8", ["const:57440c:8", "const:4:8"]]
+ 0057440c ["CALL", null, ["callee:005746e8:8"]]
- 00551574 bytes b7000094
+ 0057440c bytes b7000094
- 00551598 ["INT_ADD", "register:40f0:8", ["const:551598:8", "const:4:8"]]
- 00551598 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00574430 ["INT_ADD", "register:40f0:8", ["const:574430:8", "const:4:8"]]
+ 00574430 ["CALL", null, ["callee:00c57ae0:8"]]
- 00551598 bytes be261a94
+ 00574430 bytes ac8d1b94
~~~


<a id="compare-07b6470860a07bc68ad63b5095b852fc"></a>

### [`00551930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551930.md) → [`005747c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md) FUN_005747c8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bf4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a8c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551930.md#insn-00551958) · [`0055197c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551930.md#insn-0055197c)
- 新版 [`005747f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md#insn-005747f0) · [`00574814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md#insn-00574814)

~~~diff
- 00551958 ["INT_ADD", "register:40f0:8", ["const:551958:8", "const:4:8"]]
- 00551958 ["CALL", null, ["callee:00574a8c:8"]]
+ 005747f0 ["INT_ADD", "register:40f0:8", ["const:5747f0:8", "const:4:8"]]
+ 005747f0 ["CALL", null, ["callee:00574a8c:8"]]
- 00551958 bytes a7000094
+ 005747f0 bytes a7000094
- 0055197c ["INT_ADD", "register:40f0:8", ["const:55197c:8", "const:4:8"]]
- 0055197c ["CALL", null, ["callee:00c57ae0:8"]]
+ 00574814 ["INT_ADD", "register:40f0:8", ["const:574814:8", "const:4:8"]]
+ 00574814 ["CALL", null, ["callee:00c57ae0:8"]]
- 0055197c bytes c5251a94
+ 00574814 bytes b38c1b94
~~~


<a id="compare-0bac0e54fbc4fcda9be96f848d89a6fe"></a>

### [`00551b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551b94.md) → [`00574a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a2c.md) FUN_00574a2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551b94.md#insn-00551bb0)
- 新版 [`00574a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a2c.md#insn-00574a48)

~~~diff
- 00551bb0 ["INT_ADD", "register:40f0:8", ["const:551bb0:8", "const:4:8"]]
- 00551bb0 ["CALL", null, ["callee:00c538b0:8"]]
+ 00574a48 ["INT_ADD", "register:40f0:8", ["const:574a48:8", "const:4:8"]]
+ 00574a48 ["CALL", null, ["callee:00c538b0:8"]]
- 00551bb0 bytes ac141a94
+ 00574a48 bytes 9a7b1b94
~~~


<a id="compare-d197b26730c0825e627dee94e0349e03"></a>

### [`00551bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bbc.md) → [`00574a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a54.md) FUN_00574a54

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bbc.md#insn-00551bd8)
- 新版 [`00574a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a54.md#insn-00574a70)

~~~diff
- 00551bd8 ["INT_ADD", "register:40f0:8", ["const:551bd8:8", "const:4:8"]]
- 00551bd8 ["CALL", null, ["callee:00c538b0:8"]]
+ 00574a70 ["INT_ADD", "register:40f0:8", ["const:574a70:8", "const:4:8"]]
+ 00574a70 ["CALL", null, ["callee:00c538b0:8"]]
- 00551bd8 bytes a2141a94
+ 00574a70 bytes 907b1b94
~~~


<a id="compare-f142edfd83439c95ccc7b38241a070ec"></a>

### [`00551da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551da4.md) → [`00574c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md) FUN_00574c3c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0054e920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e920.md) [`00551da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551da4.md) · 呼出先 2件 [`00551da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551da4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005717b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717b8.md) [`00574c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md) · 呼出先 2件 [`00574c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551da4.md#insn-00551dc0) · [`00551dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551da4.md#insn-00551dcc) · [`00551e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551da4.md#insn-00551e00)
- 新版 [`00574c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md#insn-00574c58) · [`00574c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md#insn-00574c64) · [`00574c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md#insn-00574c98)

~~~diff
- 00551dc0 ["INT_ADD", "register:40f0:8", ["const:551dc0:8", "const:4:8"]]
- 00551dc0 ["CALL", null, ["local:b0:8"]]
+ 00574c58 ["INT_ADD", "register:40f0:8", ["const:574c58:8", "const:4:8"]]
+ 00574c58 ["CALL", null, ["local:b0:8"]]
- 00551dc0 bytes f9ffff97
+ 00574c58 bytes f9ffff97
- 00551dcc ["INT_ADD", "register:40f0:8", ["const:551dcc:8", "const:4:8"]]
- 00551dcc ["CALL", null, ["local:b0:8"]]
+ 00574c64 ["INT_ADD", "register:40f0:8", ["const:574c64:8", "const:4:8"]]
+ 00574c64 ["CALL", null, ["local:b0:8"]]
- 00551dcc bytes f6ffff97
+ 00574c64 bytes f6ffff97
- 00551e00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00551e00 ["INT_ADD", "register:40f0:8", ["const:551e00:8", "const:4:8"]]
- 00551e00 ["CALLIND", null, ["register:0:8"]]
+ 00574c98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574c98 ["INT_ADD", "register:40f0:8", ["const:574c98:8", "const:4:8"]]
+ 00574c98 ["CALLIND", null, ["register:0:8"]]
- 00551e00 bytes 00013fd6
+ 00574c98 bytes 00013fd6
~~~


<a id="compare-64df240d6821dcb56db619f8bd3f3ed4"></a>

### [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) → [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) FUN_00574cac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 96件 [`0054ec1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ec1c.md) [`0054ef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ef40.md) [`0054f220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f220.md) [`0054f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f3d4.md) [`0054f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 96件 [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md#insn-00551e88) · [`00551eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md#insn-00551eac)
- 新版 [`00574d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md#insn-00574d20) · [`00574d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md#insn-00574d44)

~~~diff
- 00551e88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00551e88 ["INT_ADD", "register:40f0:8", ["const:551e88:8", "const:4:8"]]
- 00551e88 ["CALLIND", null, ["register:0:8"]]
+ 00574d20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574d20 ["INT_ADD", "register:40f0:8", ["const:574d20:8", "const:4:8"]]
+ 00574d20 ["CALLIND", null, ["register:0:8"]]
- 00551e88 bytes 00013fd6
+ 00574d20 bytes 00013fd6
- 00551eac ["INT_ADD", "register:40f0:8", ["const:551eac:8", "const:4:8"]]
- 00551eac ["CALL", null, ["callee:00c57ae0:8"]]
+ 00574d44 ["INT_ADD", "register:40f0:8", ["const:574d44:8", "const:4:8"]]
+ 00574d44 ["CALL", null, ["callee:00c57ae0:8"]]
- 00551eac bytes 79241a94
+ 00574d44 bytes 678b1b94
~~~


<a id="compare-6d9f687923097899ca1272272ec154d8"></a>

### [`00551eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551eb0.md) → [`00574d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md) FUN_00574d48

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551eb0.md#insn-00551f1c) · [`00551f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551eb0.md#insn-00551f2c) · [`00551f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551eb0.md#insn-00551f4c)
- 新版 [`00574db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md#insn-00574db4) · [`00574dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md#insn-00574dc4) · [`00574de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md#insn-00574de4)

~~~diff
- 00551f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00551f1c ["INT_ADD", "register:40f0:8", ["const:551f1c:8", "const:4:8"]]
- 00551f1c ["CALLIND", null, ["register:0:8"]]
+ 00574db4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574db4 ["INT_ADD", "register:40f0:8", ["const:574db4:8", "const:4:8"]]
+ 00574db4 ["CALLIND", null, ["register:0:8"]]
- 00551f1c bytes 00013fd6
+ 00574db4 bytes 00013fd6
- 00551f2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00551f2c ["INT_ADD", "register:40f0:8", ["const:551f2c:8", "const:4:8"]]
- 00551f2c ["CALLIND", null, ["register:0:8"]]
+ 00574dc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574dc4 ["INT_ADD", "register:40f0:8", ["const:574dc4:8", "const:4:8"]]
+ 00574dc4 ["CALLIND", null, ["register:0:8"]]
- 00551f2c bytes 00013fd6
+ 00574dc4 bytes 00013fd6
- 00551f4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00551f4c ["INT_ADD", "register:40f0:8", ["const:551f4c:8", "const:4:8"]]
- 00551f4c ["CALLIND", null, ["register:0:8"]]
+ 00574de4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574de4 ["INT_ADD", "register:40f0:8", ["const:574de4:8", "const:4:8"]]
+ 00574de4 ["CALLIND", null, ["register:0:8"]]
- 00551f4c bytes 00013fd6
+ 00574de4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82db97e7d1de8a51f3f6a5d59c13dd80"></a>

### [`00552018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552018.md) → [`00574eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md) FUN_00574eb0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054fcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fcc8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00572b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572b60.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00552084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552018.md#insn-00552084) · [`00552094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552018.md#insn-00552094) · [`005520b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552018.md#insn-005520b4)
- 新版 [`00574f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md#insn-00574f1c) · [`00574f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md#insn-00574f2c) · [`00574f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md#insn-00574f4c)

~~~diff
- 00552084 ["COPY", "register:0:8", ["register:4040:8"]]
- 00552084 ["INT_ADD", "register:40f0:8", ["const:552084:8", "const:4:8"]]
- 00552084 ["CALLIND", null, ["register:0:8"]]
+ 00574f1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574f1c ["INT_ADD", "register:40f0:8", ["const:574f1c:8", "const:4:8"]]
+ 00574f1c ["CALLIND", null, ["register:0:8"]]
- 00552084 bytes 00013fd6
+ 00574f1c bytes 00013fd6
- 00552094 ["COPY", "register:0:8", ["register:4040:8"]]
- 00552094 ["INT_ADD", "register:40f0:8", ["const:552094:8", "const:4:8"]]
- 00552094 ["CALLIND", null, ["register:0:8"]]
+ 00574f2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574f2c ["INT_ADD", "register:40f0:8", ["const:574f2c:8", "const:4:8"]]
+ 00574f2c ["CALLIND", null, ["register:0:8"]]
- 00552094 bytes 00013fd6
+ 00574f2c bytes 00013fd6
- 005520b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005520b4 ["INT_ADD", "register:40f0:8", ["const:5520b4:8", "const:4:8"]]
- 005520b4 ["CALLIND", null, ["register:0:8"]]
+ 00574f4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574f4c ["INT_ADD", "register:40f0:8", ["const:574f4c:8", "const:4:8"]]
+ 00574f4c ["CALLIND", null, ["register:0:8"]]
- 005520b4 bytes 00013fd6
+ 00574f4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f342fa3aa8aaa725ef8511e3373d5208"></a>

### [`00552180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552180.md) → [`00575018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md) FUN_00575018

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005521d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552180.md#insn-005521d4) · [`005521e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552180.md#insn-005521e8) · [`005521f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552180.md#insn-005521f0)
- 新版 [`0057506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md#insn-0057506c) · [`00575080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md#insn-00575080) · [`00575088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md#insn-00575088)

~~~diff
- 005521d4 ["INT_ADD", "register:40f0:8", ["const:5521d4:8", "const:4:8"]]
- 005521d4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057506c ["INT_ADD", "register:40f0:8", ["const:57506c:8", "const:4:8"]]
+ 0057506c ["CALL", null, ["callee:00c538e0:8"]]
- 005521d4 bytes 2f131a94
+ 0057506c bytes 1d7a1b94
- 005521e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005521e8 ["INT_ADD", "register:40f0:8", ["const:5521e8:8", "const:4:8"]]
- 005521e8 ["CALLIND", null, ["register:0:8"]]
+ 00575080 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575080 ["INT_ADD", "register:40f0:8", ["const:575080:8", "const:4:8"]]
+ 00575080 ["CALLIND", null, ["register:0:8"]]
- 005521e8 bytes 00013fd6
+ 00575080 bytes 00013fd6
- 005521f0 ["INT_ADD", "register:40f0:8", ["const:5521f0:8", "const:4:8"]]
- 005521f0 ["CALL", null, ["callee:00c57a80:8"]]
+ 00575088 ["INT_ADD", "register:40f0:8", ["const:575088:8", "const:4:8"]]
+ 00575088 ["CALL", null, ["callee:00c57a80:8"]]
- 005521f0 bytes 90231a94
+ 00575088 bytes 7e8a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcb357e52438b89a1fd9c2d0df900c6b"></a>

### [`0055224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055224c.md) → [`005750e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md) FUN_005750e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055229c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055224c.md#insn-0055229c) · [`005522b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055224c.md#insn-005522b0) · [`005522b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055224c.md#insn-005522b8)
- 新版 [`00575134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md#insn-00575134) · [`00575148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md#insn-00575148) · [`00575150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md#insn-00575150)

~~~diff
- 0055229c ["INT_ADD", "register:40f0:8", ["const:55229c:8", "const:4:8"]]
- 0055229c ["CALL", null, ["callee:00c538e0:8"]]
+ 00575134 ["INT_ADD", "register:40f0:8", ["const:575134:8", "const:4:8"]]
+ 00575134 ["CALL", null, ["callee:00c538e0:8"]]
- 0055229c bytes fd121a94
+ 00575134 bytes eb791b94
- 005522b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005522b0 ["INT_ADD", "register:40f0:8", ["const:5522b0:8", "const:4:8"]]
- 005522b0 ["CALLIND", null, ["register:0:8"]]
+ 00575148 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575148 ["INT_ADD", "register:40f0:8", ["const:575148:8", "const:4:8"]]
+ 00575148 ["CALLIND", null, ["register:0:8"]]
- 005522b0 bytes 00013fd6
+ 00575148 bytes 00013fd6
- 005522b8 ["INT_ADD", "register:40f0:8", ["const:5522b8:8", "const:4:8"]]
- 005522b8 ["CALL", null, ["callee:00c57a80:8"]]
+ 00575150 ["INT_ADD", "register:40f0:8", ["const:575150:8", "const:4:8"]]
+ 00575150 ["CALL", null, ["callee:00c57a80:8"]]
- 005522b8 bytes 5e231a94
+ 00575150 bytes 4c8a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c75854e655f1fcf1d3c6b249a60029f9"></a>

### [`00552310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552310.md) → [`005751a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md) FUN_005751a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0055246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055246c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00575304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575304.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055237c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552310.md#insn-0055237c) · [`005523a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552310.md#insn-005523a8) · [`00552408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552310.md#insn-00552408)
- 新版 [`00575214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md#insn-00575214) · [`00575240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md#insn-00575240) · [`005752a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md#insn-005752a0)

~~~diff
- 0055237c ["INT_ADD", "register:40f0:8", ["const:55237c:8", "const:4:8"]]
- 0055237c ["CALL", null, ["callee:00c57a90:8"]]
+ 00575214 ["INT_ADD", "register:40f0:8", ["const:575214:8", "const:4:8"]]
+ 00575214 ["CALL", null, ["callee:00c57a90:8"]]
- 0055237c bytes 31231a94
+ 00575214 bytes 1f8a1b94
- 005523a8 ["INT_ADD", "register:40f0:8", ["const:5523a8:8", "const:4:8"]]
- 005523a8 ["CALL", null, ["callee:00c538b0:8"]]
+ 00575240 ["INT_ADD", "register:40f0:8", ["const:575240:8", "const:4:8"]]
+ 00575240 ["CALL", null, ["callee:00c538b0:8"]]
- 005523a8 bytes ae121a94
+ 00575240 bytes 9c791b94
- 00552408 ["INT_ADD", "register:40f0:8", ["const:552408:8", "const:4:8"]]
- 00552408 ["CALL", null, ["callee:00c538e0:8"]]
+ 005752a0 ["INT_ADD", "register:40f0:8", ["const:5752a0:8", "const:4:8"]]
+ 005752a0 ["CALL", null, ["callee:00c538e0:8"]]
- 00552408 bytes a2121a94
+ 005752a0 bytes 90791b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bcfe6d65cfd966af93b176f3e9744c4"></a>

### [`00552eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552eb4.md) → [`00575d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md) FUN_00575d4c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005526b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005526b0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00575548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00552ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552eb4.md#insn-00552ee8) · [`00552f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552eb4.md#insn-00552f30) · [`00552f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552eb4.md#insn-00552f50)
- 新版 [`00575d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md#insn-00575d80) · [`00575dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md#insn-00575dc8) · [`00575de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md#insn-00575de8)

~~~diff
- 00552ee8 ["INT_ADD", "register:40f0:8", ["const:552ee8:8", "const:4:8"]]
- 00552ee8 ["CALL", null, ["callee:00c57be0:8"]]
+ 00575d80 ["INT_ADD", "register:40f0:8", ["const:575d80:8", "const:4:8"]]
+ 00575d80 ["CALL", null, ["callee:00c57be0:8"]]
- 00552ee8 bytes aa201a94
+ 00575d80 bytes 98871b94
- 00552f30 ["INT_ADD", "register:40f0:8", ["const:552f30:8", "const:4:8"]]
- 00552f30 ["CALL", null, ["callee:00c57a90:8"]]
+ 00575dc8 ["INT_ADD", "register:40f0:8", ["const:575dc8:8", "const:4:8"]]
+ 00575dc8 ["CALL", null, ["callee:00c57a90:8"]]
- 00552f30 bytes 44201a94
+ 00575dc8 bytes 32871b94
- 00552f50 ["INT_ADD", "register:40f0:8", ["const:552f50:8", "const:4:8"]]
- 00552f50 ["CALL", null, ["callee:00c57b40:8"]]
+ 00575de8 ["INT_ADD", "register:40f0:8", ["const:575de8:8", "const:4:8"]]
+ 00575de8 ["CALL", null, ["callee:00c57b40:8"]]
- 00552f50 bytes 68201a94
+ 00575de8 bytes 56871b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-560f1611e04fb4623f170f58ff51a250"></a>

### [`005530c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005530c0.md) → [`00575f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md) FUN_00575f58

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005526b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005526b0.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00575548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005530f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005530c0.md#insn-005530f4) · [`0055313c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005530c0.md#insn-0055313c) · [`0055315c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005530c0.md#insn-0055315c)
- 新版 [`00575f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md#insn-00575f8c) · [`00575fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md#insn-00575fd4) · [`00575ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md#insn-00575ff4)

~~~diff
- 005530f4 ["INT_ADD", "register:40f0:8", ["const:5530f4:8", "const:4:8"]]
- 005530f4 ["CALL", null, ["callee:00c57be0:8"]]
+ 00575f8c ["INT_ADD", "register:40f0:8", ["const:575f8c:8", "const:4:8"]]
+ 00575f8c ["CALL", null, ["callee:00c57be0:8"]]
- 005530f4 bytes 27201a94
+ 00575f8c bytes 15871b94
- 0055313c ["INT_ADD", "register:40f0:8", ["const:55313c:8", "const:4:8"]]
- 0055313c ["CALL", null, ["callee:00c57a90:8"]]
+ 00575fd4 ["INT_ADD", "register:40f0:8", ["const:575fd4:8", "const:4:8"]]
+ 00575fd4 ["CALL", null, ["callee:00c57a90:8"]]
- 0055313c bytes c11f1a94
+ 00575fd4 bytes af861b94
- 0055315c ["INT_ADD", "register:40f0:8", ["const:55315c:8", "const:4:8"]]
- 0055315c ["CALL", null, ["callee:00c57b40:8"]]
+ 00575ff4 ["INT_ADD", "register:40f0:8", ["const:575ff4:8", "const:4:8"]]
+ 00575ff4 ["CALL", null, ["callee:00c57b40:8"]]
- 0055315c bytes e51f1a94
+ 00575ff4 bytes d3861b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d79cb36ef6d6f1e2e858a7e9ec6b07bb"></a>

### [`00553278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553278.md) → [`00576110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md) FUN_00576110

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005528f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005528f8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00575790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575790.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005532e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553278.md#insn-005532e4) · [`005532f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553278.md#insn-005532f4) · [`00553314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553278.md#insn-00553314)
- 新版 [`0057617c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md#insn-0057617c) · [`0057618c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md#insn-0057618c) · [`005761ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md#insn-005761ac)

~~~diff
- 005532e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005532e4 ["INT_ADD", "register:40f0:8", ["const:5532e4:8", "const:4:8"]]
- 005532e4 ["CALLIND", null, ["register:0:8"]]
+ 0057617c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057617c ["INT_ADD", "register:40f0:8", ["const:57617c:8", "const:4:8"]]
+ 0057617c ["CALLIND", null, ["register:0:8"]]
- 005532e4 bytes 00013fd6
+ 0057617c bytes 00013fd6
- 005532f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005532f4 ["INT_ADD", "register:40f0:8", ["const:5532f4:8", "const:4:8"]]
- 005532f4 ["CALLIND", null, ["register:0:8"]]
+ 0057618c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057618c ["INT_ADD", "register:40f0:8", ["const:57618c:8", "const:4:8"]]
+ 0057618c ["CALLIND", null, ["register:0:8"]]
- 005532f4 bytes 00013fd6
+ 0057618c bytes 00013fd6
- 00553314 ["COPY", "register:0:8", ["register:4040:8"]]
- 00553314 ["INT_ADD", "register:40f0:8", ["const:553314:8", "const:4:8"]]
- 00553314 ["CALLIND", null, ["register:0:8"]]
+ 005761ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005761ac ["INT_ADD", "register:40f0:8", ["const:5761ac:8", "const:4:8"]]
+ 005761ac ["CALLIND", null, ["register:0:8"]]
- 00553314 bytes 00013fd6
+ 005761ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20949e981151a379e6bd9183ab0bc387"></a>

### [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) → [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) FUN_00576278

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`00553ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md) [`00554440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md) [`00554a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md) [`00554da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md) [`00557864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557864.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 26件 [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) [`0057a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a6fc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00553454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md#insn-00553454) · [`00553478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md#insn-00553478)
- 新版 [`005762ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md#insn-005762ec) · [`00576310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md#insn-00576310)

~~~diff
- 00553454 ["COPY", "register:0:8", ["register:4040:8"]]
- 00553454 ["INT_ADD", "register:40f0:8", ["const:553454:8", "const:4:8"]]
- 00553454 ["CALLIND", null, ["register:0:8"]]
+ 005762ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005762ec ["INT_ADD", "register:40f0:8", ["const:5762ec:8", "const:4:8"]]
+ 005762ec ["CALLIND", null, ["register:0:8"]]
- 00553454 bytes 00013fd6
+ 005762ec bytes 00013fd6
- 00553478 ["INT_ADD", "register:40f0:8", ["const:553478:8", "const:4:8"]]
- 00553478 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00576310 ["INT_ADD", "register:40f0:8", ["const:576310:8", "const:4:8"]]
+ 00576310 ["CALL", null, ["callee:00c57ae0:8"]]
- 00553478 bytes 061f1a94
+ 00576310 bytes f4851b94
~~~


<a id="compare-9a9772ded4ff877201b69523d03c1f68"></a>

### [`00553950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553950.md) → [`005767e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005767e8.md) FUN_005767e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00553828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553828.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005766c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766c0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00553960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553950.md#insn-00553960)
- 新版 [`005767f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005767e8.md#insn-005767f8)

~~~diff
- 00553960 ["INT_ADD", "register:40f0:8", ["const:553960:8", "const:4:8"]]
- 00553960 ["CALL", null, ["callee:005766c0:8"]]
+ 005767f8 ["INT_ADD", "register:40f0:8", ["const:5767f8:8", "const:4:8"]]
+ 005767f8 ["CALL", null, ["callee:005766c0:8"]]
- 00553960 bytes b2ffff97
+ 005767f8 bytes b2ffff97
~~~


<a id="compare-71cba4182002ace12dcce150672ec880"></a>

### [`005541a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md) → [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md) FUN_00577040

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00554440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md) [`00554a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md) [`00554da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md) · 呼出先 2件 [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 2件 [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005541e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md#insn-005541e4) · [`00554210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md#insn-00554210) · [`00554220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md#insn-00554220)
- 新版 [`0057707c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md#insn-0057707c) · [`005770a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md#insn-005770a8) · [`005770b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md#insn-005770b8)

~~~diff
- 005541e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005541e4 ["INT_ADD", "register:40f0:8", ["const:5541e4:8", "const:4:8"]]
- 005541e4 ["CALLIND", null, ["register:0:8"]]
+ 0057707c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057707c ["INT_ADD", "register:40f0:8", ["const:57707c:8", "const:4:8"]]
+ 0057707c ["CALLIND", null, ["register:0:8"]]
- 005541e4 bytes 20013fd6
+ 0057707c bytes 20013fd6
- 00554210 ["COPY", "register:0:8", ["register:4040:8"]]
- 00554210 ["INT_ADD", "register:40f0:8", ["const:554210:8", "const:4:8"]]
- 00554210 ["CALLIND", null, ["register:0:8"]]
+ 005770a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005770a8 ["INT_ADD", "register:40f0:8", ["const:5770a8:8", "const:4:8"]]
+ 005770a8 ["CALLIND", null, ["register:0:8"]]
- 00554210 bytes 00013fd6
+ 005770a8 bytes 00013fd6
- 00554220 ["INT_ADD", "register:40f0:8", ["const:554220:8", "const:4:8"]]
- 00554220 ["CALL", null, ["callee:0057be68:8"]]
+ 005770b8 ["INT_ADD", "register:40f0:8", ["const:5770b8:8", "const:4:8"]]
+ 005770b8 ["CALL", null, ["callee:0057be68:8"]]
- 00554220 bytes 6c130094
+ 005770b8 bytes 6c130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9baf3baab6a752b04d4d7cf53a1f20f5"></a>

### [`005543f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005543f0.md) → [`00577288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577288.md) FUN_00577288

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055440c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005543f0.md#insn-0055440c) · [`0055442c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005543f0.md#insn-0055442c)
- 新版 [`005772a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577288.md#insn-005772a4) · [`005772c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577288.md#insn-005772c4)

~~~diff
- 0055440c ["INT_ADD", "register:40f0:8", ["const:55440c:8", "const:4:8"]]
- 0055440c ["CALL", null, ["callee:00c538e0:8"]]
+ 005772a4 ["INT_ADD", "register:40f0:8", ["const:5772a4:8", "const:4:8"]]
+ 005772a4 ["CALL", null, ["callee:00c538e0:8"]]
- 0055440c bytes a10a1a94
+ 005772a4 bytes 8f711b94
- 0055442c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055442c ["INT_ADD", "register:40f0:8", ["const:55442c:8", "const:4:8"]]
- 0055442c ["CALLIND", null, ["register:0:8"]]
+ 005772c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005772c4 ["INT_ADD", "register:40f0:8", ["const:5772c4:8", "const:4:8"]]
+ 005772c4 ["CALLIND", null, ["register:0:8"]]
- 0055442c bytes 00013fd6
+ 005772c4 bytes 00013fd6
~~~


<a id="compare-596dcff39750725395c3398fb7af45e1"></a>

### [`005549b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005549b8.md) → [`00577850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577850.md) FUN_00577850

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005549d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005549b8.md#insn-005549d4) · [`005549f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005549b8.md#insn-005549f4)
- 新版 [`0057786c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577850.md#insn-0057786c) · [`0057788c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577850.md#insn-0057788c)

~~~diff
- 005549d4 ["INT_ADD", "register:40f0:8", ["const:5549d4:8", "const:4:8"]]
- 005549d4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057786c ["INT_ADD", "register:40f0:8", ["const:57786c:8", "const:4:8"]]
+ 0057786c ["CALL", null, ["callee:00c538e0:8"]]
- 005549d4 bytes 2f091a94
+ 0057786c bytes 1d701b94
- 005549f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005549f4 ["INT_ADD", "register:40f0:8", ["const:5549f4:8", "const:4:8"]]
- 005549f4 ["CALLIND", null, ["register:0:8"]]
+ 0057788c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057788c ["INT_ADD", "register:40f0:8", ["const:57788c:8", "const:4:8"]]
+ 0057788c ["CALLIND", null, ["register:0:8"]]
- 005549f4 bytes 00013fd6
+ 0057788c bytes 00013fd6
~~~


<a id="compare-a0891af9d862916a7288e5960ca3ab70"></a>

### [`005552ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/005552ec.md) → [`00578184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578184.md) FUN_00578184

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00577fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005552fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/005552ec.md#insn-005552fc)
- 新版 [`00578194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578184.md#insn-00578194)

~~~diff
- 005552fc ["INT_ADD", "register:40f0:8", ["const:5552fc:8", "const:4:8"]]
- 005552fc ["CALL", null, ["callee:00577fe0:8"]]
+ 00578194 ["INT_ADD", "register:40f0:8", ["const:578194:8", "const:4:8"]]
+ 00578194 ["CALL", null, ["callee:00577fe0:8"]]
- 005552fc bytes 93ffff97
+ 00578194 bytes 93ffff97
~~~


<a id="compare-bb8a704118001adf67935e0e9e4c1a8d"></a>

### [`005573cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005573cc.md) → [`0057a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a264.md) FUN_0057a264

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00559444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559444.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00557420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005573cc.md#insn-00557420)
- 新版 [`0057a2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a264.md#insn-0057a2b8)

~~~diff
- 00557420 ["INT_ADD", "register:40f0:8", ["const:557420:8", "const:4:8"]]
- 00557420 ["CALL", null, ["callee:0057c2dc:8"]]
+ 0057a2b8 ["INT_ADD", "register:40f0:8", ["const:57a2b8:8", "const:4:8"]]
+ 0057a2b8 ["CALL", null, ["callee:0057c2dc:8"]]
- 00557420 bytes 09080094
+ 0057a2b8 bytes 09080094
~~~


<a id="compare-3891a518eaf67d067cceaf374bffd53d"></a>

### [`00557424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557424.md) → [`0057a2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a2bc.md) FUN_0057a2bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00559444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559444.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00557468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557424.md#insn-00557468)
- 新版 [`0057a300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a2bc.md#insn-0057a300)

~~~diff
- 00557468 ["INT_ADD", "register:40f0:8", ["const:557468:8", "const:4:8"]]
- 00557468 ["CALL", null, ["callee:0057c2dc:8"]]
+ 0057a300 ["INT_ADD", "register:40f0:8", ["const:57a300:8", "const:4:8"]]
+ 0057a300 ["CALL", null, ["callee:0057c2dc:8"]]
- 00557468 bytes f7070094
+ 0057a300 bytes f7070094
~~~


<a id="compare-9fec4f38c750768356321c460e6c7ef3"></a>

### [`0055746c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/0055746c.md) → [`0057a304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a304.md) FUN_0057a304

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00559444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559444.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005574b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/0055746c.md#insn-005574b0)
- 新版 [`0057a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a304.md#insn-0057a348)

~~~diff
- 005574b0 ["INT_ADD", "register:40f0:8", ["const:5574b0:8", "const:4:8"]]
- 005574b0 ["CALL", null, ["callee:0057c2dc:8"]]
+ 0057a348 ["INT_ADD", "register:40f0:8", ["const:57a348:8", "const:4:8"]]
+ 0057a348 ["CALL", null, ["callee:0057c2dc:8"]]
- 005574b0 bytes e5070094
+ 0057a348 bytes e5070094
~~~


<a id="compare-5f9349e579ac719aa9409619c8eff73e"></a>

### [`00558db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558db4.md) → [`0057bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md) FUN_0057bc4c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005536d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536d4.md) [`00558db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558db4.md) · 呼出先 2件 [`00558db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558db4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0057656c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057656c.md) [`0057bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md) · 呼出先 2件 [`0057bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00558dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558db4.md#insn-00558dd0) · [`00558ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558db4.md#insn-00558ddc) · [`00558e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558db4.md#insn-00558e14)
- 新版 [`0057bc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md#insn-0057bc68) · [`0057bc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md#insn-0057bc74) · [`0057bcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md#insn-0057bcac)

~~~diff
- 00558dd0 ["INT_ADD", "register:40f0:8", ["const:558dd0:8", "const:4:8"]]
- 00558dd0 ["CALL", null, ["local:b0:8"]]
+ 0057bc68 ["INT_ADD", "register:40f0:8", ["const:57bc68:8", "const:4:8"]]
+ 0057bc68 ["CALL", null, ["local:b0:8"]]
- 00558dd0 bytes f9ffff97
+ 0057bc68 bytes f9ffff97
- 00558ddc ["INT_ADD", "register:40f0:8", ["const:558ddc:8", "const:4:8"]]
- 00558ddc ["CALL", null, ["local:b0:8"]]
+ 0057bc74 ["INT_ADD", "register:40f0:8", ["const:57bc74:8", "const:4:8"]]
+ 0057bc74 ["CALL", null, ["local:b0:8"]]
- 00558ddc bytes f6ffff97
+ 0057bc74 bytes f6ffff97
- 00558e14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00558e14 ["INT_ADD", "register:40f0:8", ["const:558e14:8", "const:4:8"]]
- 00558e14 ["CALLIND", null, ["register:0:8"]]
+ 0057bcac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bcac ["INT_ADD", "register:40f0:8", ["const:57bcac:8", "const:4:8"]]
+ 0057bcac ["CALLIND", null, ["register:0:8"]]
- 00558e14 bytes 00013fd6
+ 0057bcac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10001d8f148822fc4bd337861b49be1e"></a>

### [`00558e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558e54.md) → [`0057bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md) FUN_0057bcec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005536dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536dc.md) [`00558e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558e54.md) · 呼出先 2件 [`00558e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558e54.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00576574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576574.md) [`0057bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md) · 呼出先 2件 [`0057bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00558e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558e54.md#insn-00558e70) · [`00558e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558e54.md#insn-00558e7c) · [`00558eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558e54.md#insn-00558eb0)
- 新版 [`0057bd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md#insn-0057bd08) · [`0057bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md#insn-0057bd14) · [`0057bd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md#insn-0057bd48)

~~~diff
- 00558e70 ["INT_ADD", "register:40f0:8", ["const:558e70:8", "const:4:8"]]
- 00558e70 ["CALL", null, ["local:b0:8"]]
+ 0057bd08 ["INT_ADD", "register:40f0:8", ["const:57bd08:8", "const:4:8"]]
+ 0057bd08 ["CALL", null, ["local:b0:8"]]
- 00558e70 bytes f9ffff97
+ 0057bd08 bytes f9ffff97
- 00558e7c ["INT_ADD", "register:40f0:8", ["const:558e7c:8", "const:4:8"]]
- 00558e7c ["CALL", null, ["local:b0:8"]]
+ 0057bd14 ["INT_ADD", "register:40f0:8", ["const:57bd14:8", "const:4:8"]]
+ 0057bd14 ["CALL", null, ["local:b0:8"]]
- 00558e7c bytes f6ffff97
+ 0057bd14 bytes f6ffff97
- 00558eb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00558eb0 ["INT_ADD", "register:40f0:8", ["const:558eb0:8", "const:4:8"]]
- 00558eb0 ["CALLIND", null, ["register:0:8"]]
+ 0057bd48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bd48 ["INT_ADD", "register:40f0:8", ["const:57bd48:8", "const:4:8"]]
+ 0057bd48 ["CALLIND", null, ["register:0:8"]]
- 00558eb0 bytes 00013fd6
+ 0057bd48 bytes 00013fd6
~~~


<a id="compare-2a213992bfb69bece7256b6020f7b73d"></a>

### [`00558ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ec4.md) → [`0057bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md) FUN_0057bd5c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00553820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553820.md) [`00558ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ec4.md) · 呼出先 4件 [`00558ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ec4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005766b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766b8.md) [`0057bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md) · 呼出先 4件 [`0057bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00558ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ec4.md#insn-00558ee0) · [`00558eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ec4.md#insn-00558eec) · [`00558f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ec4.md#insn-00558f00)
- 新版 [`0057bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md#insn-0057bd78) · [`0057bd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md#insn-0057bd84) · [`0057bd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md#insn-0057bd98)

~~~diff
- 00558ee0 ["INT_ADD", "register:40f0:8", ["const:558ee0:8", "const:4:8"]]
- 00558ee0 ["CALL", null, ["local:b0:8"]]
+ 0057bd78 ["INT_ADD", "register:40f0:8", ["const:57bd78:8", "const:4:8"]]
+ 0057bd78 ["CALL", null, ["local:b0:8"]]
- 00558ee0 bytes f9ffff97
+ 0057bd78 bytes f9ffff97
- 00558eec ["INT_ADD", "register:40f0:8", ["const:558eec:8", "const:4:8"]]
- 00558eec ["CALL", null, ["local:b0:8"]]
+ 0057bd84 ["INT_ADD", "register:40f0:8", ["const:57bd84:8", "const:4:8"]]
+ 0057bd84 ["CALL", null, ["local:b0:8"]]
- 00558eec bytes f6ffff97
+ 0057bd84 bytes f6ffff97
- 00558f00 ["INT_ADD", "register:40f0:8", ["const:558f00:8", "const:4:8"]]
- 00558f00 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057bd98 ["INT_ADD", "register:40f0:8", ["const:57bd98:8", "const:4:8"]]
+ 0057bd98 ["CALL", null, ["callee:00c538e0:8"]]
- 00558f00 bytes e4f71994
+ 0057bd98 bytes d25e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e499006e323e7247134f01b7c369ed53"></a>

### [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) → [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) FUN_0057bdcc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`00553ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md) [`0055be18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055be18.md) [`0055bf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bf90.md) [`0055c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c104.md) [`0055c284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c284.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 11件 [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`0057ecb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ecb0.md) [`0057ee28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ee28.md) [`0057ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ef9c.md) [`0057f11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f11c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00558fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md#insn-00558fa8) · [`00558fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md#insn-00558fcc)
- 新版 [`0057be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md#insn-0057be40) · [`0057be64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md#insn-0057be64)

~~~diff
- 00558fa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00558fa8 ["INT_ADD", "register:40f0:8", ["const:558fa8:8", "const:4:8"]]
- 00558fa8 ["CALLIND", null, ["register:0:8"]]
+ 0057be40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057be40 ["INT_ADD", "register:40f0:8", ["const:57be40:8", "const:4:8"]]
+ 0057be40 ["CALLIND", null, ["register:0:8"]]
- 00558fa8 bytes 00013fd6
+ 0057be40 bytes 00013fd6
- 00558fcc ["INT_ADD", "register:40f0:8", ["const:558fcc:8", "const:4:8"]]
- 00558fcc ["CALL", null, ["callee:00c57ae0:8"]]
+ 0057be64 ["INT_ADD", "register:40f0:8", ["const:57be64:8", "const:4:8"]]
+ 0057be64 ["CALL", null, ["callee:00c57ae0:8"]]
- 00558fcc bytes 31081a94
+ 0057be64 bytes 1f6f1b94
~~~


<a id="compare-96d260a918bba187af40c05234bc1670"></a>

### [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) → [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) FUN_0057be68

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`005541a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md) [`00557adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557adc.md) [`005698ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005698ec.md) [`0069d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069d8e0.md) [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 16件 [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md) [`0057a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a974.md) [`0058c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c784.md) [`006c3c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3c44.md) [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055903c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md#insn-0055903c) · [`0055904c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md#insn-0055904c) · [`0055906c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md#insn-0055906c)
- 新版 [`0057bed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md#insn-0057bed4) · [`0057bee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md#insn-0057bee4) · [`0057bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md#insn-0057bf04)

~~~diff
- 0055903c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055903c ["INT_ADD", "register:40f0:8", ["const:55903c:8", "const:4:8"]]
- 0055903c ["CALLIND", null, ["register:0:8"]]
+ 0057bed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bed4 ["INT_ADD", "register:40f0:8", ["const:57bed4:8", "const:4:8"]]
+ 0057bed4 ["CALLIND", null, ["register:0:8"]]
- 0055903c bytes 00013fd6
+ 0057bed4 bytes 00013fd6
- 0055904c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055904c ["INT_ADD", "register:40f0:8", ["const:55904c:8", "const:4:8"]]
- 0055904c ["CALLIND", null, ["register:0:8"]]
+ 0057bee4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bee4 ["INT_ADD", "register:40f0:8", ["const:57bee4:8", "const:4:8"]]
+ 0057bee4 ["CALLIND", null, ["register:0:8"]]
- 0055904c bytes 00013fd6
+ 0057bee4 bytes 00013fd6
- 0055906c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055906c ["INT_ADD", "register:40f0:8", ["const:55906c:8", "const:4:8"]]
- 0055906c ["CALLIND", null, ["register:0:8"]]
+ 0057bf04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bf04 ["INT_ADD", "register:40f0:8", ["const:57bf04:8", "const:4:8"]]
+ 0057bf04 ["CALLIND", null, ["register:0:8"]]
- 0055906c bytes 00013fd6
+ 0057bf04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1452b6851783182b95241405c260f80a"></a>

### [`005591d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005591d8.md) → [`0057c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md) FUN_0057c070

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00554a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md) [`00554da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00559334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559334.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0057c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00559244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005591d8.md#insn-00559244) · [`00559270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005591d8.md#insn-00559270) · [`005592d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005591d8.md#insn-005592d0)
- 新版 [`0057c0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md#insn-0057c0dc) · [`0057c108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md#insn-0057c108) · [`0057c168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md#insn-0057c168)

~~~diff
- 00559244 ["INT_ADD", "register:40f0:8", ["const:559244:8", "const:4:8"]]
- 00559244 ["CALL", null, ["callee:00c57a90:8"]]
+ 0057c0dc ["INT_ADD", "register:40f0:8", ["const:57c0dc:8", "const:4:8"]]
+ 0057c0dc ["CALL", null, ["callee:00c57a90:8"]]
- 00559244 bytes 7f071a94
+ 0057c0dc bytes 6d6e1b94
- 00559270 ["INT_ADD", "register:40f0:8", ["const:559270:8", "const:4:8"]]
- 00559270 ["CALL", null, ["callee:00c538b0:8"]]
+ 0057c108 ["INT_ADD", "register:40f0:8", ["const:57c108:8", "const:4:8"]]
+ 0057c108 ["CALL", null, ["callee:00c538b0:8"]]
- 00559270 bytes fcf61994
+ 0057c108 bytes ea5d1b94
- 005592d0 ["INT_ADD", "register:40f0:8", ["const:5592d0:8", "const:4:8"]]
- 005592d0 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057c168 ["INT_ADD", "register:40f0:8", ["const:57c168:8", "const:4:8"]]
+ 0057c168 ["CALL", null, ["callee:00c538e0:8"]]
- 005592d0 bytes f0f61994
+ 0057c168 bytes de5d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41203f7fd6565eeceb23fbe8affb626f"></a>

### [`00559348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559348.md) → [`0057c1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md) FUN_0057c1e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00555148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555148.md) · 呼出先 4件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00577fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md) · 呼出先 4件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005593f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559348.md#insn-005593f8) · [`0055940c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559348.md#insn-0055940c) · [`00559420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559348.md#insn-00559420)
- 新版 [`0057c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md#insn-0057c290) · [`0057c2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md#insn-0057c2a4) · [`0057c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md#insn-0057c2b8)

~~~diff
- 005593f8 ["INT_ADD", "register:40f0:8", ["const:5593f8:8", "const:4:8"]]
- 005593f8 ["CALL", null, ["callee:004945d0:8"]]
+ 0057c290 ["INT_ADD", "register:40f0:8", ["const:57c290:8", "const:4:8"]]
+ 0057c290 ["CALL", null, ["callee:004945d0:8"]]
- 005593f8 bytes d060fc97
+ 0057c290 bytes d060fc97
- 0055940c ["INT_ADD", "register:40f0:8", ["const:55940c:8", "const:4:8"]]
- 0055940c ["CALL", null, ["callee:00c538e0:8"]]
+ 0057c2a4 ["INT_ADD", "register:40f0:8", ["const:57c2a4:8", "const:4:8"]]
+ 0057c2a4 ["CALL", null, ["callee:00c538e0:8"]]
- 0055940c bytes a1f61994
+ 0057c2a4 bytes 8f5d1b94
- 00559420 ["COPY", "register:0:8", ["register:4040:8"]]
- 00559420 ["INT_ADD", "register:40f0:8", ["const:559420:8", "const:4:8"]]
- 00559420 ["CALLIND", null, ["register:0:8"]]
+ 0057c2b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c2b8 ["INT_ADD", "register:40f0:8", ["const:57c2b8:8", "const:4:8"]]
+ 0057c2b8 ["CALLIND", null, ["register:0:8"]]
- 00559420 bytes 00013fd6
+ 0057c2b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13ce5f26f266cc9d965e4cf2c26c35b1"></a>

### [`00559458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559458.md) → [`0057c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md) FUN_0057c2f0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00557724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557724.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00559334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559334.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0057a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a5bc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0057c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005594c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559458.md#insn-005594c4) · [`005594f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559458.md#insn-005594f0) · [`00559550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559458.md#insn-00559550)
- 新版 [`0057c35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md#insn-0057c35c) · [`0057c388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md#insn-0057c388) · [`0057c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md#insn-0057c3e8)

~~~diff
- 005594c4 ["INT_ADD", "register:40f0:8", ["const:5594c4:8", "const:4:8"]]
- 005594c4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0057c35c ["INT_ADD", "register:40f0:8", ["const:57c35c:8", "const:4:8"]]
+ 0057c35c ["CALL", null, ["callee:00c57a90:8"]]
- 005594c4 bytes df061a94
+ 0057c35c bytes cd6d1b94
- 005594f0 ["INT_ADD", "register:40f0:8", ["const:5594f0:8", "const:4:8"]]
- 005594f0 ["CALL", null, ["callee:00c538b0:8"]]
+ 0057c388 ["INT_ADD", "register:40f0:8", ["const:57c388:8", "const:4:8"]]
+ 0057c388 ["CALL", null, ["callee:00c538b0:8"]]
- 005594f0 bytes 5cf61994
+ 0057c388 bytes 4a5d1b94
- 00559550 ["INT_ADD", "register:40f0:8", ["const:559550:8", "const:4:8"]]
- 00559550 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057c3e8 ["INT_ADD", "register:40f0:8", ["const:57c3e8:8", "const:4:8"]]
+ 0057c3e8 ["CALL", null, ["callee:00c538e0:8"]]
- 00559550 bytes 50f61994
+ 0057c3e8 bytes 3e5d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12d19165f56e9b6be5e914eeb31162a6"></a>

### [`00559654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559654.md) → [`0057c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md) FUN_0057c4ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00557a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a78.md) [`00559654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559654.md) · 呼出先 2件 [`00559654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559654.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0057a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a910.md) [`0057c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md) · 呼出先 2件 [`0057c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00559670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559654.md#insn-00559670) · [`0055967c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559654.md#insn-0055967c) · [`005596b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559654.md#insn-005596b0)
- 新版 [`0057c508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md#insn-0057c508) · [`0057c514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md#insn-0057c514) · [`0057c548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md#insn-0057c548)

~~~diff
- 00559670 ["INT_ADD", "register:40f0:8", ["const:559670:8", "const:4:8"]]
- 00559670 ["CALL", null, ["local:b0:8"]]
+ 0057c508 ["INT_ADD", "register:40f0:8", ["const:57c508:8", "const:4:8"]]
+ 0057c508 ["CALL", null, ["local:b0:8"]]
- 00559670 bytes f9ffff97
+ 0057c508 bytes f9ffff97
- 0055967c ["INT_ADD", "register:40f0:8", ["const:55967c:8", "const:4:8"]]
- 0055967c ["CALL", null, ["local:b0:8"]]
+ 0057c514 ["INT_ADD", "register:40f0:8", ["const:57c514:8", "const:4:8"]]
+ 0057c514 ["CALL", null, ["local:b0:8"]]
- 0055967c bytes f6ffff97
+ 0057c514 bytes f6ffff97
- 005596b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005596b0 ["INT_ADD", "register:40f0:8", ["const:5596b0:8", "const:4:8"]]
- 005596b0 ["CALLIND", null, ["register:0:8"]]
+ 0057c548 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c548 ["INT_ADD", "register:40f0:8", ["const:57c548:8", "const:4:8"]]
+ 0057c548 ["CALLIND", null, ["register:0:8"]]
- 005596b0 bytes 00013fd6
+ 0057c548 bytes 00013fd6
~~~


<a id="compare-49c7f9950ec02c31f020141814d8c229"></a>

### [`005596c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005596c4.md) → [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) FUN_0057c55c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00557a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a80.md) [`005596c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005596c4.md) [`00569550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569550.md) · 呼出先 2件 [`005596c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005596c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0057a918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a918.md) [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) [`0058c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c3e8.md) · 呼出先 2件 [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005596e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005596c4.md#insn-005596e0) · [`005596ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005596c4.md#insn-005596ec) · [`00559720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005596c4.md#insn-00559720)
- 新版 [`0057c578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md#insn-0057c578) · [`0057c584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md#insn-0057c584) · [`0057c5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md#insn-0057c5b8)

~~~diff
- 005596e0 ["INT_ADD", "register:40f0:8", ["const:5596e0:8", "const:4:8"]]
- 005596e0 ["CALL", null, ["local:b0:8"]]
+ 0057c578 ["INT_ADD", "register:40f0:8", ["const:57c578:8", "const:4:8"]]
+ 0057c578 ["CALL", null, ["local:b0:8"]]
- 005596e0 bytes f9ffff97
+ 0057c578 bytes f9ffff97
- 005596ec ["INT_ADD", "register:40f0:8", ["const:5596ec:8", "const:4:8"]]
- 005596ec ["CALL", null, ["local:b0:8"]]
+ 0057c584 ["INT_ADD", "register:40f0:8", ["const:57c584:8", "const:4:8"]]
+ 0057c584 ["CALL", null, ["local:b0:8"]]
- 005596ec bytes f6ffff97
+ 0057c584 bytes f6ffff97
- 00559720 ["COPY", "register:0:8", ["register:4040:8"]]
- 00559720 ["INT_ADD", "register:40f0:8", ["const:559720:8", "const:4:8"]]
- 00559720 ["CALLIND", null, ["register:0:8"]]
+ 0057c5b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c5b8 ["INT_ADD", "register:40f0:8", ["const:57c5b8:8", "const:4:8"]]
+ 0057c5b8 ["CALLIND", null, ["register:0:8"]]
- 00559720 bytes 00013fd6
+ 0057c5b8 bytes 00013fd6
~~~


<a id="compare-43791dc274262a35f8f40a747ca70622"></a>

### [`0055977c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/0055977c.md) → [`0057c614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md) FUN_0057c614

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0055828c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/0055828c.md) [`0090126c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/0090126c.md) [`00a6a9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a9b8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) [`00935ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935ca0.md) [`00ac894c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac894c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005597e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/0055977c.md#insn-005597e8) · [`005597f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/0055977c.md#insn-005597f8) · [`00559818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/0055977c.md#insn-00559818)
- 新版 [`0057c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md#insn-0057c680) · [`0057c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md#insn-0057c690) · [`0057c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md#insn-0057c6b0)

~~~diff
- 005597e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005597e8 ["INT_ADD", "register:40f0:8", ["const:5597e8:8", "const:4:8"]]
- 005597e8 ["CALLIND", null, ["register:0:8"]]
+ 0057c680 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c680 ["INT_ADD", "register:40f0:8", ["const:57c680:8", "const:4:8"]]
+ 0057c680 ["CALLIND", null, ["register:0:8"]]
- 005597e8 bytes 00013fd6
+ 0057c680 bytes 00013fd6
- 005597f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005597f8 ["INT_ADD", "register:40f0:8", ["const:5597f8:8", "const:4:8"]]
- 005597f8 ["CALLIND", null, ["register:0:8"]]
+ 0057c690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c690 ["INT_ADD", "register:40f0:8", ["const:57c690:8", "const:4:8"]]
+ 0057c690 ["CALLIND", null, ["register:0:8"]]
- 005597f8 bytes 00013fd6
+ 0057c690 bytes 00013fd6
- 00559818 ["COPY", "register:0:8", ["register:4040:8"]]
- 00559818 ["INT_ADD", "register:40f0:8", ["const:559818:8", "const:4:8"]]
- 00559818 ["CALLIND", null, ["register:0:8"]]
+ 0057c6b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c6b0 ["INT_ADD", "register:40f0:8", ["const:57c6b0:8", "const:4:8"]]
+ 0057c6b0 ["CALLIND", null, ["register:0:8"]]
- 00559818 bytes 00013fd6
+ 0057c6b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c086926ac11252f667cae3386a21dbe2"></a>

### [`00559dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559dfc.md) → [`0057cc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc94.md) FUN_0057cc94

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00559e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559dfc.md#insn-00559e14)
- 新版 [`0057ccac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc94.md#insn-0057ccac)

~~~diff
- 00559e14 ["INT_ADD", "register:40f0:8", ["const:559e14:8", "const:4:8"]]
- 00559e14 ["CALL", null, ["callee:00c59d40:8"]]
+ 0057ccac ["INT_ADD", "register:40f0:8", ["const:57ccac:8", "const:4:8"]]
+ 0057ccac ["CALL", null, ["callee:00c59d40:8"]]
- 00559e14 bytes 370d1a94
+ 0057ccac bytes 25741b94
~~~


<a id="compare-ad28e36ad34aa26d24db9ab6757977eb"></a>

### [`00559e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559e88.md) → [`0057cd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cd20.md) FUN_0057cd20

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00559ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559e88.md#insn-00559ea8) · [`00559ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559e88.md#insn-00559ebc)
- 新版 [`0057cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cd20.md#insn-0057cd40) · [`0057cd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cd20.md#insn-0057cd54)

~~~diff
- 00559ea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00559ea8 ["INT_ADD", "register:40f0:8", ["const:559ea8:8", "const:4:8"]]
- 00559ea8 ["CALLIND", null, ["register:0:8"]]
+ 0057cd40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057cd40 ["INT_ADD", "register:40f0:8", ["const:57cd40:8", "const:4:8"]]
+ 0057cd40 ["CALLIND", null, ["register:0:8"]]
- 00559ea8 bytes 00013fd6
+ 0057cd40 bytes 00013fd6
- 00559ebc ["COPY", "register:0:8", ["register:4040:8"]]
- 00559ebc ["INT_ADD", "register:40f0:8", ["const:559ebc:8", "const:4:8"]]
- 00559ebc ["CALLIND", null, ["register:0:8"]]
+ 0057cd54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057cd54 ["INT_ADD", "register:40f0:8", ["const:57cd54:8", "const:4:8"]]
+ 0057cd54 ["CALLIND", null, ["register:0:8"]]
- 00559ebc bytes 00013fd6
+ 0057cd54 bytes 00013fd6
~~~


<a id="compare-1afd1ab50a4482f2f463f0e7f24b8386"></a>

### [`00559f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559f90.md) → [`0057ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce28.md) FUN_0057ce28

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00559fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559f90.md#insn-00559fac)
- 新版 [`0057ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce28.md#insn-0057ce44)

~~~diff
- 00559fac ["INT_ADD", "register:40f0:8", ["const:559fac:8", "const:4:8"]]
- 00559fac ["CALL", null, ["callee:00c59d70:8"]]
+ 0057ce44 ["INT_ADD", "register:40f0:8", ["const:57ce44:8", "const:4:8"]]
+ 0057ce44 ["CALL", null, ["callee:00c59d70:8"]]
- 00559fac bytes dd0c1a94
+ 0057ce44 bytes cb731b94
~~~


<a id="compare-70171358377d1888aa69e1f2a1c194ba"></a>

### [`0055a254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a254.md) → [`0057d0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d0ec.md) FUN_0057d0ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd300.md) [`00bdd320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d50.md) [`00c59d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a254.md#insn-0055a26c) · [`0055a27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a254.md#insn-0055a27c)
- 新版 [`0057d104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d0ec.md#insn-0057d104) · [`0057d114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d0ec.md#insn-0057d114)

~~~diff
- 0055a26c ["INT_ADD", "register:40f0:8", ["const:55a26c:8", "const:4:8"]]
- 0055a26c ["CALL", null, ["callee:00c59d50:8"]]
+ 0057d104 ["INT_ADD", "register:40f0:8", ["const:57d104:8", "const:4:8"]]
+ 0057d104 ["CALL", null, ["callee:00c59d50:8"]]
- 0055a26c bytes 250c1a94
+ 0057d104 bytes 13731b94
- 0055a27c ["INT_ADD", "register:40f0:8", ["const:55a27c:8", "const:4:8"]]
- 0055a27c ["CALL", null, ["callee:00c59d70:8"]]
+ 0057d114 ["INT_ADD", "register:40f0:8", ["const:57d114:8", "const:4:8"]]
+ 0057d114 ["CALL", null, ["callee:00c59d70:8"]]
- 0055a27c bytes 290c1a94
+ 0057d114 bytes 17731b94
~~~


<a id="compare-7c0a1b724fe9236820225b99bdec783a"></a>

### [`0055a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a2e0.md) → [`0057d178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d178.md) FUN_0057d178

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a2e0.md#insn-0055a2f8)
- 新版 [`0057d190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d178.md#insn-0057d190)

~~~diff
- 0055a2f8 ["INT_ADD", "register:40f0:8", ["const:55a2f8:8", "const:4:8"]]
- 0055a2f8 ["CALL", null, ["callee:00c59c00:8"]]
+ 0057d190 ["INT_ADD", "register:40f0:8", ["const:57d190:8", "const:4:8"]]
+ 0057d190 ["CALL", null, ["callee:00c59c00:8"]]
- 0055a2f8 bytes ae0b1a94
+ 0057d190 bytes 9c721b94
~~~


<a id="compare-b06a10d32b2821df174bce2bec02c95e"></a>

### [`0055a314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a314.md) → [`0057d1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md) FUN_0057d1ac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd370.md) [`00bdd380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd380.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md) [`00c59dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a314.md#insn-0055a32c) · [`0055a340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a314.md#insn-0055a340) · [`0055a344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a314.md#insn-0055a344)
- 新版 [`0057d1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md#insn-0057d1c4) · [`0057d1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md#insn-0057d1d8) · [`0057d1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md#insn-0057d1dc)

~~~diff
- 0055a32c ["INT_ADD", "register:40f0:8", ["const:55a32c:8", "const:4:8"]]
- 0055a32c ["CALL", null, ["callee:00c59db0:8"]]
+ 0057d1c4 ["INT_ADD", "register:40f0:8", ["const:57d1c4:8", "const:4:8"]]
+ 0057d1c4 ["CALL", null, ["callee:00c59db0:8"]]
- 0055a32c bytes 0d0c1a94
+ 0057d1c4 bytes fb721b94
- 0055a340 ["INT_ADD", "register:40f0:8", ["const:55a340:8", "const:4:8"]]
- 0055a340 ["CALL", null, ["callee:00c59dc0:8"]]
+ 0057d1d8 ["INT_ADD", "register:40f0:8", ["const:57d1d8:8", "const:4:8"]]
+ 0057d1d8 ["CALL", null, ["callee:00c59dc0:8"]]
- 0055a340 bytes 0c0c1a94
+ 0057d1d8 bytes fa721b94
- 0055a344 ["INT_ADD", "register:40f0:8", ["const:55a344:8", "const:4:8"]]
- 0055a344 ["CALL", null, ["callee:00c59dd0:8"]]
+ 0057d1dc ["INT_ADD", "register:40f0:8", ["const:57d1dc:8", "const:4:8"]]
+ 0057d1dc ["CALL", null, ["callee:00c59dd0:8"]]
- 0055a344 bytes 0f0c1a94
+ 0057d1dc bytes fd721b94
~~~


<a id="compare-8c34644f88e18200fa88626b2449d3fe"></a>

### [`0055a35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a35c.md) → [`0057d1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md) FUN_0057d1f4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd370.md) [`00bdd390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd390.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md) [`00c59de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a35c.md#insn-0055a380) · [`0055a388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a35c.md#insn-0055a388) · [`0055a3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a35c.md#insn-0055a3bc)
- 新版 [`0057d218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md#insn-0057d218) · [`0057d220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md#insn-0057d220) · [`0057d254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md#insn-0057d254)

~~~diff
- 0055a380 ["INT_ADD", "register:40f0:8", ["const:55a380:8", "const:4:8"]]
- 0055a380 ["CALL", null, ["callee:00c59dc0:8"]]
+ 0057d218 ["INT_ADD", "register:40f0:8", ["const:57d218:8", "const:4:8"]]
+ 0057d218 ["CALL", null, ["callee:00c59dc0:8"]]
- 0055a380 bytes fc0b1a94
+ 0057d218 bytes ea721b94
- 0055a388 ["INT_ADD", "register:40f0:8", ["const:55a388:8", "const:4:8"]]
- 0055a388 ["CALL", null, ["callee:00c59de0:8"]]
+ 0057d220 ["INT_ADD", "register:40f0:8", ["const:57d220:8", "const:4:8"]]
+ 0057d220 ["CALL", null, ["callee:00c59de0:8"]]
- 0055a388 bytes 020c1a94
+ 0057d220 bytes f0721b94
- 0055a3bc ["INT_ADD", "register:40f0:8", ["const:55a3bc:8", "const:4:8"]]
- 0055a3bc ["CALL", null, ["callee:00c57ae0:8"]]
+ 0057d254 ["INT_ADD", "register:40f0:8", ["const:57d254:8", "const:4:8"]]
+ 0057d254 ["CALL", null, ["callee:00c57ae0:8"]]
- 0055a3bc bytes 35031a94
+ 0057d254 bytes 236a1b94
~~~


<a id="compare-ecb5e171c6b190633e9081c1a72e09ed"></a>

### [`0055a3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a3f4.md) → [`0057d28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md) FUN_0057d28c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd370.md) [`00bdd390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd390.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md) [`00c59de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a3f4.md#insn-0055a418) · [`0055a420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a3f4.md#insn-0055a420) · [`0055a448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a3f4.md#insn-0055a448)
- 新版 [`0057d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md#insn-0057d2b0) · [`0057d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md#insn-0057d2b8) · [`0057d2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md#insn-0057d2e0)

~~~diff
- 0055a418 ["INT_ADD", "register:40f0:8", ["const:55a418:8", "const:4:8"]]
- 0055a418 ["CALL", null, ["callee:00c59dc0:8"]]
+ 0057d2b0 ["INT_ADD", "register:40f0:8", ["const:57d2b0:8", "const:4:8"]]
+ 0057d2b0 ["CALL", null, ["callee:00c59dc0:8"]]
- 0055a418 bytes d60b1a94
+ 0057d2b0 bytes c4721b94
- 0055a420 ["INT_ADD", "register:40f0:8", ["const:55a420:8", "const:4:8"]]
- 0055a420 ["CALL", null, ["callee:00c59de0:8"]]
+ 0057d2b8 ["INT_ADD", "register:40f0:8", ["const:57d2b8:8", "const:4:8"]]
+ 0057d2b8 ["CALL", null, ["callee:00c59de0:8"]]
- 0055a420 bytes dc0b1a94
+ 0057d2b8 bytes ca721b94
- 0055a448 ["INT_ADD", "register:40f0:8", ["const:55a448:8", "const:4:8"]]
- 0055a448 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0057d2e0 ["INT_ADD", "register:40f0:8", ["const:57d2e0:8", "const:4:8"]]
+ 0057d2e0 ["CALL", null, ["callee:00c57ae0:8"]]
- 0055a448 bytes 12031a94
+ 0057d2e0 bytes 006a1b94
~~~


<a id="compare-6ce4ea37da54b29eaa544f6bdd502d0c"></a>

### [`0055a544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a544.md) → [`0057d3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d3dc.md) FUN_0057d3dc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a544.md#insn-0055a56c) · [`0055a580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a544.md#insn-0055a580)
- 新版 [`0057d404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d3dc.md#insn-0057d404) · [`0057d418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d3dc.md#insn-0057d418)

~~~diff
- 0055a56c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055a56c ["INT_ADD", "register:40f0:8", ["const:55a56c:8", "const:4:8"]]
- 0055a56c ["CALLIND", null, ["register:0:8"]]
+ 0057d404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d404 ["INT_ADD", "register:40f0:8", ["const:57d404:8", "const:4:8"]]
+ 0057d404 ["CALLIND", null, ["register:0:8"]]
- 0055a56c bytes 00013fd6
+ 0057d404 bytes 00013fd6
- 0055a580 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055a580 ["INT_ADD", "register:40f0:8", ["const:55a580:8", "const:4:8"]]
- 0055a580 ["CALLIND", null, ["register:0:8"]]
+ 0057d418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d418 ["INT_ADD", "register:40f0:8", ["const:57d418:8", "const:4:8"]]
+ 0057d418 ["CALLIND", null, ["register:0:8"]]
- 0055a580 bytes 00013fd6
+ 0057d418 bytes 00013fd6
~~~


<a id="compare-ca59b19ec86974a812696eab0e160926"></a>

### [`0055a80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a80c.md) → [`0057d6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6a4.md) FUN_0057d6a4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a80c.md#insn-0055a81c)
- 新版 [`0057d6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6a4.md#insn-0057d6b4)

~~~diff
- 0055a81c ["INT_ADD", "register:40f0:8", ["const:55a81c:8", "const:4:8"]]
- 0055a81c ["CALL", null, ["callee:00c59c60:8"]]
+ 0057d6b4 ["INT_ADD", "register:40f0:8", ["const:57d6b4:8", "const:4:8"]]
+ 0057d6b4 ["CALL", null, ["callee:00c59c60:8"]]
- 0055a81c bytes 7d0a1a94
+ 0057d6b4 bytes 6b711b94
~~~


<a id="compare-9ddf2b726112ebcea9f0cf07da3b167f"></a>

### [`0055a830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a830.md) → [`0057d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6c8.md) FUN_0057d6c8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a830.md#insn-0055a84c)
- 新版 [`0057d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6c8.md#insn-0057d6e4)

~~~diff
- 0055a84c ["INT_ADD", "register:40f0:8", ["const:55a84c:8", "const:4:8"]]
- 0055a84c ["CALL", null, ["callee:00c59e00:8"]]
+ 0057d6e4 ["INT_ADD", "register:40f0:8", ["const:57d6e4:8", "const:4:8"]]
+ 0057d6e4 ["CALL", null, ["callee:00c59e00:8"]]
- 0055a84c bytes d90a1a94
+ 0057d6e4 bytes c7711b94
~~~


<a id="compare-b61d91888474e217596e72f761b9ccee"></a>

### [`0055a8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a8ec.md) → [`0057d784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d784.md) FUN_0057d784

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a8ec.md#insn-0055a928)
- 新版 [`0057d7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d784.md#insn-0057d7c0)

~~~diff
- 0055a928 ["INT_ADD", "register:40f0:8", ["const:55a928:8", "const:4:8"]]
- 0055a928 ["CALL", null, ["callee:00c59e20:8"]]
+ 0057d7c0 ["INT_ADD", "register:40f0:8", ["const:57d7c0:8", "const:4:8"]]
+ 0057d7c0 ["CALL", null, ["callee:00c59e20:8"]]
- 0055a928 bytes aa0a1a94
+ 0057d7c0 bytes 98711b94
~~~


<a id="compare-f3f98c0f676fa0a645ed7310853a1aa9"></a>

### [`0055a948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a948.md) → [`0057d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d7e0.md) FUN_0057d7e0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a948.md#insn-0055a970)
- 新版 [`0057d808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d7e0.md#insn-0057d808)

~~~diff
- 0055a970 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055a970 ["INT_ADD", "register:40f0:8", ["const:55a970:8", "const:4:8"]]
- 0055a970 ["CALLIND", null, ["register:0:8"]]
+ 0057d808 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d808 ["INT_ADD", "register:40f0:8", ["const:57d808:8", "const:4:8"]]
+ 0057d808 ["CALLIND", null, ["register:0:8"]]
- 0055a970 bytes 20013fd6
+ 0057d808 bytes 20013fd6
~~~


<a id="compare-e535d34a15f19b1b24a48c3c3be198fe"></a>

### [`0055a99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a99c.md) → [`0057d834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md) FUN_0057d834

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055a9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a99c.md#insn-0055a9cc) · [`0055a9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a99c.md#insn-0055a9f0) · [`0055aa00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a99c.md#insn-0055aa00)
- 新版 [`0057d864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md#insn-0057d864) · [`0057d888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md#insn-0057d888) · [`0057d898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md#insn-0057d898)

~~~diff
- 0055a9cc ["COPY", "register:0:8", ["register:4048:8"]]
- 0055a9cc ["INT_ADD", "register:40f0:8", ["const:55a9cc:8", "const:4:8"]]
- 0055a9cc ["CALLIND", null, ["register:0:8"]]
+ 0057d864 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d864 ["INT_ADD", "register:40f0:8", ["const:57d864:8", "const:4:8"]]
+ 0057d864 ["CALLIND", null, ["register:0:8"]]
- 0055a9cc bytes 20013fd6
+ 0057d864 bytes 20013fd6
- 0055a9f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055a9f0 ["INT_ADD", "register:40f0:8", ["const:55a9f0:8", "const:4:8"]]
- 0055a9f0 ["CALLIND", null, ["register:0:8"]]
+ 0057d888 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d888 ["INT_ADD", "register:40f0:8", ["const:57d888:8", "const:4:8"]]
+ 0057d888 ["CALLIND", null, ["register:0:8"]]
- 0055a9f0 bytes 20013fd6
+ 0057d888 bytes 20013fd6
- 0055aa00 ["INT_ADD", "register:40f0:8", ["const:55aa00:8", "const:4:8"]]
- 0055aa00 ["CALL", null, ["callee:00c59e20:8"]]
+ 0057d898 ["INT_ADD", "register:40f0:8", ["const:57d898:8", "const:4:8"]]
+ 0057d898 ["CALL", null, ["callee:00c59e20:8"]]
- 0055aa00 bytes 740a1a94
+ 0057d898 bytes 62711b94
~~~


<a id="compare-69140e460b6540cbf76de3328f857730"></a>

### [`0055aa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aa2c.md) → [`0057d8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d8c4.md) FUN_0057d8c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd370.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055aa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aa2c.md#insn-0055aa4c)
- 新版 [`0057d8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d8c4.md#insn-0057d8e4)

~~~diff
- 0055aa4c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055aa4c ["INT_ADD", "register:40f0:8", ["const:55aa4c:8", "const:4:8"]]
- 0055aa4c ["CALLIND", null, ["register:0:8"]]
+ 0057d8e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d8e4 ["INT_ADD", "register:40f0:8", ["const:57d8e4:8", "const:4:8"]]
+ 0057d8e4 ["CALLIND", null, ["register:0:8"]]
- 0055aa4c bytes 00013fd6
+ 0057d8e4 bytes 00013fd6
~~~


<a id="compare-1e7c0ee52fd9c03d7f250c392a552502"></a>

### [`0055aa7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aa7c.md) → [`0057d914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d914.md) FUN_0057d914

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd370.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055aaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aa7c.md#insn-0055aaa0)
- 新版 [`0057d938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d914.md#insn-0057d938)

~~~diff
- 0055aaa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055aaa0 ["INT_ADD", "register:40f0:8", ["const:55aaa0:8", "const:4:8"]]
- 0055aaa0 ["CALLIND", null, ["register:0:8"]]
+ 0057d938 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d938 ["INT_ADD", "register:40f0:8", ["const:57d938:8", "const:4:8"]]
+ 0057d938 ["CALLIND", null, ["register:0:8"]]
- 0055aaa0 bytes 00013fd6
+ 0057d938 bytes 00013fd6
~~~


<a id="compare-7311d6c9325150aab554d76f69d6a8bb"></a>

### [`0055adfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055adfc.md) → [`0057dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md) FUN_0057dc94

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdd3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c59e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ae24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055adfc.md#insn-0055ae24) · [`0055ae98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055adfc.md#insn-0055ae98) · [`0055aeb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055adfc.md#insn-0055aeb8)
- 新版 [`0057dcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md#insn-0057dcbc) · [`0057dd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md#insn-0057dd30) · [`0057dd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md#insn-0057dd50)

~~~diff
- 0055ae24 ["INT_ADD", "register:40f0:8", ["const:55ae24:8", "const:4:8"]]
- 0055ae24 ["CALL", null, ["callee:00c59e30:8"]]
+ 0057dcbc ["INT_ADD", "register:40f0:8", ["const:57dcbc:8", "const:4:8"]]
+ 0057dcbc ["CALL", null, ["callee:00c59e30:8"]]
- 0055ae24 bytes 6f091a94
+ 0057dcbc bytes 5d701b94
- 0055ae98 ["INT_ADD", "register:40f0:8", ["const:55ae98:8", "const:4:8"]]
- 0055ae98 ["CALL", null, ["callee:00c57a90:8"]]
+ 0057dd30 ["INT_ADD", "register:40f0:8", ["const:57dd30:8", "const:4:8"]]
+ 0057dd30 ["CALL", null, ["callee:00c57a90:8"]]
- 0055ae98 bytes 6a001a94
+ 0057dd30 bytes 58671b94
- 0055aeb8 ["INT_ADD", "register:40f0:8", ["const:55aeb8:8", "const:4:8"]]
- 0055aeb8 ["CALL", null, ["callee:00c57b40:8"]]
+ 0057dd50 ["INT_ADD", "register:40f0:8", ["const:57dd50:8", "const:4:8"]]
+ 0057dd50 ["CALL", null, ["callee:00c57b40:8"]]
- 0055aeb8 bytes 8e001a94
+ 0057dd50 bytes 7c671b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef3970fef457540ea8afcca58f7a377"></a>

### [`0055af10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af10.md) → [`0057dda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dda8.md) FUN_0057dda8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 1件 [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055af2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af10.md#insn-0055af2c)
- 新版 [`0057ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dda8.md#insn-0057ddc4)

~~~diff
- 0055af2c ["INT_ADD", "register:40f0:8", ["const:55af2c:8", "const:4:8"]]
- 0055af2c ["CALL", null, ["callee:00c538b0:8"]]
+ 0057ddc4 ["INT_ADD", "register:40f0:8", ["const:57ddc4:8", "const:4:8"]]
+ 0057ddc4 ["CALL", null, ["callee:00c538b0:8"]]
- 0055af2c bytes cdef1994
+ 0057ddc4 bytes bb561b94
~~~


<a id="compare-66ddeae3490682949ef3cc8624b1fc7d"></a>

### [`0055b168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b168.md) → [`0057e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e000.md) FUN_0057e000

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b168.md#insn-0055b184) · [`0055b1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b168.md#insn-0055b1a4)
- 新版 [`0057e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e000.md#insn-0057e01c) · [`0057e03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e000.md#insn-0057e03c)

~~~diff
- 0055b184 ["INT_ADD", "register:40f0:8", ["const:55b184:8", "const:4:8"]]
- 0055b184 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057e01c ["INT_ADD", "register:40f0:8", ["const:57e01c:8", "const:4:8"]]
+ 0057e01c ["CALL", null, ["callee:00c538e0:8"]]
- 0055b184 bytes 43ef1994
+ 0057e01c bytes 31561b94
- 0055b1a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055b1a4 ["INT_ADD", "register:40f0:8", ["const:55b1a4:8", "const:4:8"]]
- 0055b1a4 ["CALLIND", null, ["register:0:8"]]
+ 0057e03c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057e03c ["INT_ADD", "register:40f0:8", ["const:57e03c:8", "const:4:8"]]
+ 0057e03c ["CALLIND", null, ["register:0:8"]]
- 0055b1a4 bytes 00013fd6
+ 0057e03c bytes 00013fd6
~~~


<a id="compare-539ec4cb9e77e4d13f9f8e2e233beb8a"></a>

### [`0055b510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b510.md) → [`0057e3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3a8.md) FUN_0057e3a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052dd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md) · 呼出先 1件 [`00bdd400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd400.md)
- 新版 呼出元 1件 [`00550bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bdc.md) · 呼出先 1件 [`00c59e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b510.md#insn-0055b52c)
- 新版 [`0057e3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3a8.md#insn-0057e3c4)

~~~diff
- 0055b52c ["INT_ADD", "register:40f0:8", ["const:55b52c:8", "const:4:8"]]
- 0055b52c ["CALL", null, ["callee:00c59e50:8"]]
+ 0057e3c4 ["INT_ADD", "register:40f0:8", ["const:57e3c4:8", "const:4:8"]]
+ 0057e3c4 ["CALL", null, ["callee:00c59e50:8"]]
- 0055b52c bytes b5071a94
+ 0057e3c4 bytes a36e1b94
~~~


<a id="compare-5a82af96da8ed1626d2f238a4d8b575b"></a>

### [`0055b540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b540.md) → [`0057e3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md) FUN_0057e3d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd48.md) · 呼出先 5件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca10.md)
- 新版 呼出元 1件 [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055b578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b540.md#insn-0055b578) · [`0055b58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b540.md#insn-0055b58c) · [`0055b5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b540.md#insn-0055b5a8)
- 新版 [`0057e410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md#insn-0057e410) · [`0057e424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md#insn-0057e424) · [`0057e440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md#insn-0057e440)

~~~diff
- 0055b578 ["INT_ADD", "register:40f0:8", ["const:55b578:8", "const:4:8"]]
- 0055b578 ["CALL", null, ["callee:00c59460:8"]]
+ 0057e410 ["INT_ADD", "register:40f0:8", ["const:57e410:8", "const:4:8"]]
+ 0057e410 ["CALL", null, ["callee:00c59460:8"]]
- 0055b578 bytes 26051a94
+ 0057e410 bytes 146c1b94
- 0055b58c ["INT_ADD", "register:40f0:8", ["const:55b58c:8", "const:4:8"]]
- 0055b58c ["CALL", null, ["callee:00550b64:8"]]
+ 0057e424 ["INT_ADD", "register:40f0:8", ["const:57e424:8", "const:4:8"]]
+ 0057e424 ["CALL", null, ["callee:00550b64:8"]]
- 0055b58c bytes d049ff97
+ 0057e424 bytes d049ff97
- 0055b5a8 ["INT_ADD", "register:40f0:8", ["const:55b5a8:8", "const:4:8"]]
- 0055b5a8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057e440 ["INT_ADD", "register:40f0:8", ["const:57e440:8", "const:4:8"]]
+ 0057e440 ["CALL", null, ["callee:00c538e0:8"]]
- 0055b5a8 bytes 3aee1994
+ 0057e440 bytes 28551b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2361d6089b8a5e54ba9f56102a418914"></a>

### [`0055bcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bcb4.md) → [`0057eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057eb4c.md) FUN_0057eb4c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052dd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd58.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca10.md)
- 新版 呼出元 1件 [`00550bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055bce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bcb4.md#insn-0055bce4) · [`0055bd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bcb4.md#insn-0055bd14)
- 新版 [`0057eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057eb4c.md#insn-0057eb7c) · [`0057ebac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057eb4c.md#insn-0057ebac)

~~~diff
- 0055bce4 ["INT_ADD", "register:40f0:8", ["const:55bce4:8", "const:4:8"]]
- 0055bce4 ["CALL", null, ["callee:00c59460:8"]]
+ 0057eb7c ["INT_ADD", "register:40f0:8", ["const:57eb7c:8", "const:4:8"]]
+ 0057eb7c ["CALL", null, ["callee:00c59460:8"]]
- 0055bce4 bytes 4b031a94
+ 0057eb7c bytes 396a1b94
- 0055bd14 ["INT_ADD", "register:40f0:8", ["const:55bd14:8", "const:4:8"]]
- 0055bd14 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0057ebac ["INT_ADD", "register:40f0:8", ["const:57ebac:8", "const:4:8"]]
+ 0057ebac ["CALL", null, ["callee:00c57ae0:8"]]
- 0055bd14 bytes dffc1994
+ 0057ebac bytes cd631b94
~~~


<a id="compare-c6734741a570d3a2c4a241d63c5e5ae6"></a>

### [`0055bd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd1c.md) → [`0057ebb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebb4.md) FUN_0057ebb4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052de54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de54.md) · 呼出先 1件 [`00bdd410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd410.md)
- 新版 呼出元 1件 [`00550cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cec.md) · 呼出先 1件 [`00c59e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055bd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd1c.md#insn-0055bd34)
- 新版 [`0057ebcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebb4.md#insn-0057ebcc)

~~~diff
- 0055bd34 ["INT_ADD", "register:40f0:8", ["const:55bd34:8", "const:4:8"]]
- 0055bd34 ["CALL", null, ["callee:00c59e60:8"]]
+ 0057ebcc ["INT_ADD", "register:40f0:8", ["const:57ebcc:8", "const:4:8"]]
+ 0057ebcc ["CALL", null, ["callee:00c59e60:8"]]
- 0055bd34 bytes b7051a94
+ 0057ebcc bytes a56c1b94
~~~


<a id="compare-fa0257f2ed596e63e4c80bb4c8eedb14"></a>

### [`0055bd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd84.md) → [`0057ec1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec1c.md) FUN_0057ec1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052de5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de5c.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd450.md)
- 新版 呼出元 1件 [`00550cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf4.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055bdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd84.md#insn-0055bdb4) · [`0055bdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd84.md#insn-0055bdec)
- 新版 [`0057ec4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec1c.md#insn-0057ec4c) · [`0057ec84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec1c.md#insn-0057ec84)

~~~diff
- 0055bdb4 ["INT_ADD", "register:40f0:8", ["const:55bdb4:8", "const:4:8"]]
- 0055bdb4 ["CALL", null, ["callee:00c59ea0:8"]]
+ 0057ec4c ["INT_ADD", "register:40f0:8", ["const:57ec4c:8", "const:4:8"]]
+ 0057ec4c ["CALL", null, ["callee:00c59ea0:8"]]
- 0055bdb4 bytes a7051a94
+ 0057ec4c bytes 956c1b94
- 0055bdec ["INT_ADD", "register:40f0:8", ["const:55bdec:8", "const:4:8"]]
- 0055bdec ["CALL", null, ["callee:00c57ae0:8"]]
+ 0057ec84 ["INT_ADD", "register:40f0:8", ["const:57ec84:8", "const:4:8"]]
+ 0057ec84 ["CALL", null, ["callee:00c57ae0:8"]]
- 0055bdec bytes a9fc1994
+ 0057ec84 bytes 97631b94
~~~


<a id="compare-939d7ea613f2d43147ec2725dbc89c70"></a>

### [`0055bdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bdf4.md) → [`0057ec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec8c.md) FUN_0057ec8c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005323bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323bc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555254.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055be04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bdf4.md#insn-0055be04)
- 新版 [`0057ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec8c.md#insn-0057ec9c)

~~~diff
- 0055be04 ["INT_ADD", "register:40f0:8", ["const:55be04:8", "const:4:8"]]
- 0055be04 ["CALL", null, ["callee:00555254:8"]]
+ 0057ec9c ["INT_ADD", "register:40f0:8", ["const:57ec9c:8", "const:4:8"]]
+ 0057ec9c ["CALL", null, ["callee:00555254:8"]]
- 0055be04 bytes 6e59ff97
+ 0057ec9c bytes 6e59ff97
~~~


<a id="compare-fbd9401a8bd9af61b3de5663a1f86400"></a>

### [`0055ce48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ce48.md) → [`0057fce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md) FUN_0057fce0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005323c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323c4.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0055525c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/0055525c.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055ce6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ce48.md#insn-0055ce6c) · [`0055ce7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ce48.md#insn-0055ce7c) · [`0055cecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ce48.md#insn-0055cecc)
- 新版 [`0057fd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md#insn-0057fd04) · [`0057fd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md#insn-0057fd14) · [`0057fd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md#insn-0057fd64)

~~~diff
- 0055ce6c ["INT_ADD", "register:40f0:8", ["const:55ce6c:8", "const:4:8"]]
- 0055ce6c ["CALL", null, ["callee:0057facc:8"]]
+ 0057fd04 ["INT_ADD", "register:40f0:8", ["const:57fd04:8", "const:4:8"]]
+ 0057fd04 ["CALL", null, ["callee:0057facc:8"]]
- 0055ce6c bytes 72ffff97
+ 0057fd04 bytes 72ffff97
- 0055ce7c ["INT_ADD", "register:40f0:8", ["const:55ce7c:8", "const:4:8"]]
- 0055ce7c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0057fd14 ["INT_ADD", "register:40f0:8", ["const:57fd14:8", "const:4:8"]]
+ 0057fd14 ["CALL", null, ["callee:00c57ab0:8"]]
- 0055ce7c bytes 79f81994
+ 0057fd14 bytes 675f1b94
- 0055cecc ["INT_ADD", "register:40f0:8", ["const:55cecc:8", "const:4:8"]]
- 0055cecc ["CALL", null, ["callee:00c57ae0:8"]]
+ 0057fd64 ["INT_ADD", "register:40f0:8", ["const:57fd64:8", "const:4:8"]]
+ 0057fd64 ["CALL", null, ["callee:00c57ae0:8"]]
- 0055cecc bytes 71f81994
+ 0057fd64 bytes 5f5f1b94
~~~


<a id="compare-dc3c43fa1ec00f89fd1659942ea74da3"></a>

### [`0055d024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d024.md) → [`0057febc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md) FUN_0057febc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005323d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323d0.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00555268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555268.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0055d064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d024.md#insn-0055d064) · [`0055d074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d024.md#insn-0055d074) · [`0055d0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d024.md#insn-0055d0c4)
- 新版 [`0057fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md#insn-0057fefc) · [`0057ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md#insn-0057ff0c) · [`0057ff5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md#insn-0057ff5c)

~~~diff
- 0055d064 ["INT_ADD", "register:40f0:8", ["const:55d064:8", "const:4:8"]]
- 0055d064 ["CALL", null, ["callee:0057facc:8"]]
+ 0057fefc ["INT_ADD", "register:40f0:8", ["const:57fefc:8", "const:4:8"]]
+ 0057fefc ["CALL", null, ["callee:0057facc:8"]]
- 0055d064 bytes f4feff97
+ 0057fefc bytes f4feff97
- 0055d074 ["INT_ADD", "register:40f0:8", ["const:55d074:8", "const:4:8"]]
- 0055d074 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0057ff0c ["INT_ADD", "register:40f0:8", ["const:57ff0c:8", "const:4:8"]]
+ 0057ff0c ["CALL", null, ["callee:00c57ab0:8"]]
- 0055d074 bytes fbf71994
+ 0057ff0c bytes e95e1b94
- 0055d0c4 ["INT_ADD", "register:40f0:8", ["const:55d0c4:8", "const:4:8"]]
- 0055d0c4 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0057ff5c ["INT_ADD", "register:40f0:8", ["const:57ff5c:8", "const:4:8"]]
+ 0057ff5c ["CALL", null, ["callee:00c57ae0:8"]]
- 0055d0c4 bytes f3f71994
+ 0057ff5c bytes e15e1b94
~~~


