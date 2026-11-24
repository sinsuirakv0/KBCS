# v16.0.0 → v16.0.1 · 要調査の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-ac16a238ea18704e6b5662ba21f062a5"></a>

### [`00545198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md) → [`005451d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005451d8.md) FUN_005451d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004e7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) · 呼出先 2件 [`005454fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`004e7494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md) · 呼出先 2件 [`0054553c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/0054553c.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00545220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md#insn-00545220) · [`00545274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md#insn-00545274) · [`00545310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md#insn-00545310)
- 新版 [`00545260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005451d8.md#insn-00545260) · [`005452b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005451d8.md#insn-005452b4) · [`00545350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005451d8.md#insn-00545350)

~~~diff
- 00545220 ["INT_ADD", "register:40f0:8", ["const:545220:8", "const:4:8"]]
- 00545220 ["CALL", null, ["callee:00c58050:8"]]
+ 00545260 ["INT_ADD", "register:40f0:8", ["const:545260:8", "const:4:8"]]
+ 00545260 ["CALL", null, ["callee:00c58050:8"]]
- 00545220 bytes 8c4a1c94
+ 00545260 bytes 7c4b1c94
- 00545274 ["INT_ADD", "register:40f0:8", ["const:545274:8", "const:4:8"]]
- 00545274 ["CALL", null, ["callee:00c58050:8"]]
+ 005452b4 ["INT_ADD", "register:40f0:8", ["const:5452b4:8", "const:4:8"]]
+ 005452b4 ["CALL", null, ["callee:00c58050:8"]]
- 00545274 bytes 774a1c94
+ 005452b4 bytes 674b1c94
- 00545310 ["INT_ADD", "register:40f0:8", ["const:545310:8", "const:4:8"]]
- 00545310 ["CALL", null, ["callee:00c58050:8"]]
+ 00545350 ["INT_ADD", "register:40f0:8", ["const:545350:8", "const:4:8"]]
+ 00545350 ["CALL", null, ["callee:00c58050:8"]]
- 00545310 bytes 504a1c94
+ 00545350 bytes 404b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b42c6ee6d0e0567b035d3e113e75f5a"></a>

### [`00545434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545434.md) → [`00545474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545474.md) FUN_00545474

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004e7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004e7494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00545454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545434.md#insn-00545454) · [`00545488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545434.md#insn-00545488) · [`005454b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545434.md#insn-005454b0)
- 新版 [`00545494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545474.md#insn-00545494) · [`005454c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545474.md#insn-005454c8) · [`005454f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545474.md#insn-005454f0)

~~~diff
- 00545454 ["INT_ADD", "register:40f0:8", ["const:545454:8", "const:4:8"]]
- 00545454 ["CALL", null, ["callee:00c57e90:8"]]
+ 00545494 ["INT_ADD", "register:40f0:8", ["const:545494:8", "const:4:8"]]
+ 00545494 ["CALL", null, ["callee:00c57e90:8"]]
- 00545454 bytes 8f491c94
+ 00545494 bytes 7f4a1c94
- 00545488 ["INT_ADD", "register:40f0:8", ["const:545488:8", "const:4:8"]]
- 00545488 ["CALL", null, ["callee:0043bb20:8"]]
+ 005454c8 ["INT_ADD", "register:40f0:8", ["const:5454c8:8", "const:4:8"]]
+ 005454c8 ["CALL", null, ["callee:0043bb20:8"]]
- 00545488 bytes 96d9fb97
+ 005454c8 bytes 96d9fb97
- 005454b0 ["INT_ADD", "register:40f0:8", ["const:5454b0:8", "const:4:8"]]
- 005454b0 ["CALL", null, ["callee:0054075c:8"]]
+ 005454f0 ["INT_ADD", "register:40f0:8", ["const:5454f0:8", "const:4:8"]]
+ 005454f0 ["CALL", null, ["callee:0054075c:8"]]
- 005454b0 bytes 9becff97
+ 005454f0 bytes 9becff97
~~~


<a id="compare-448598095966a4f77e7704be78a0cf0b"></a>

### [`005454fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md) → [`0054553c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/0054553c.md) FUN_0054553c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004e7604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md) [`00545198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`004e7644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7644.md) [`005451d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005451d8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00545580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md#insn-00545580) · [`005455ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md#insn-005455ac)
- 新版 [`005455c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/0054553c.md#insn-005455c0) · [`005455ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/0054553c.md#insn-005455ec)

~~~diff
- 00545580 ["INT_ADD", "register:40f0:8", ["const:545580:8", "const:4:8"]]
- 00545580 ["CALL", null, ["callee:00c58050:8"]]
+ 005455c0 ["INT_ADD", "register:40f0:8", ["const:5455c0:8", "const:4:8"]]
+ 005455c0 ["CALL", null, ["callee:00c58050:8"]]
- 00545580 bytes b4491c94
+ 005455c0 bytes a44a1c94
- 005455ac ["INT_ADD", "register:40f0:8", ["const:5455ac:8", "const:4:8"]]
- 005455ac ["CALL", null, ["callee:00c58050:8"]]
+ 005455ec ["INT_ADD", "register:40f0:8", ["const:5455ec:8", "const:4:8"]]
+ 005455ec ["CALL", null, ["callee:00c58050:8"]]
- 005455ac bytes a9491c94
+ 005455ec bytes 994a1c94
~~~


<a id="compare-11b7763fa6925e7c398ef5f0e9c336b4"></a>

### [`00545600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545600.md) → [`00545640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545640.md) FUN_00545640

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545600.md#insn-0054565c) · [`0054567c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545600.md#insn-0054567c) · [`0054568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545600.md#insn-0054568c)
- 新版 [`0054569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545640.md#insn-0054569c) · [`005456bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545640.md#insn-005456bc) · [`005456cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545640.md#insn-005456cc)

~~~diff
- 0054565c ["INT_ADD", "register:40f0:8", ["const:54565c:8", "const:4:8"]]
- 0054565c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054569c ["INT_ADD", "register:40f0:8", ["const:54569c:8", "const:4:8"]]
+ 0054569c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054565c bytes 15491c94
+ 0054569c bytes 054a1c94
- 0054567c ["INT_ADD", "register:40f0:8", ["const:54567c:8", "const:4:8"]]
- 0054567c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005456bc ["INT_ADD", "register:40f0:8", ["const:5456bc:8", "const:4:8"]]
+ 005456bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0054567c bytes 0d491c94
+ 005456bc bytes fd491c94
- 0054568c ["INT_ADD", "register:40f0:8", ["const:54568c:8", "const:4:8"]]
- 0054568c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005456cc ["INT_ADD", "register:40f0:8", ["const:5456cc:8", "const:4:8"]]
+ 005456cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0054568c bytes 09491c94
+ 005456cc bytes f9491c94
~~~


<a id="compare-e57bfcfc49c1ee2744dbc3b73450a4f4"></a>

### [`005456a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005456a4.md) → [`005456e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005456e4.md) FUN_005456e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004e75fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e75fc.md) [`005456a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005456a4.md) · 呼出先 2件 [`005456a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005456a4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`004e763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e763c.md) [`005456e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005456e4.md) · 呼出先 2件 [`005456e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005456e4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005456c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005456a4.md#insn-005456c4) · [`005456d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005456a4.md#insn-005456d0) · [`0054570c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005456a4.md#insn-0054570c)
- 新版 [`00545704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005456e4.md#insn-00545704) · [`00545710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005456e4.md#insn-00545710) · [`0054574c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005456e4.md#insn-0054574c)

~~~diff
- 005456c4 ["INT_ADD", "register:40f0:8", ["const:5456c4:8", "const:4:8"]]
- 005456c4 ["CALL", null, ["local:b0:8"]]
+ 00545704 ["INT_ADD", "register:40f0:8", ["const:545704:8", "const:4:8"]]
+ 00545704 ["CALL", null, ["local:b0:8"]]
- 005456c4 bytes f8ffff97
+ 00545704 bytes f8ffff97
- 005456d0 ["INT_ADD", "register:40f0:8", ["const:5456d0:8", "const:4:8"]]
- 005456d0 ["CALL", null, ["local:b0:8"]]
+ 00545710 ["INT_ADD", "register:40f0:8", ["const:545710:8", "const:4:8"]]
+ 00545710 ["CALL", null, ["local:b0:8"]]
- 005456d0 bytes f5ffff97
+ 00545710 bytes f5ffff97
- 0054570c ["INT_ADD", "register:40f0:8", ["const:54570c:8", "const:4:8"]]
- 0054570c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054574c ["INT_ADD", "register:40f0:8", ["const:54574c:8", "const:4:8"]]
+ 0054574c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054570c bytes e9481c94
+ 0054574c bytes d9491c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96a8bee090d67571e364a148c86fc2f9"></a>

### [`0054586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/0054586c.md) → [`005458ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005458ac.md) FUN_005458ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004edc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004edc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edc94.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054588c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/0054586c.md#insn-0054588c)
- 新版 [`005458cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005458ac.md#insn-005458cc)

~~~diff
- 0054588c ["INT_ADD", "register:40f0:8", ["const:54588c:8", "const:4:8"]]
- 0054588c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005458cc ["INT_ADD", "register:40f0:8", ["const:5458cc:8", "const:4:8"]]
+ 005458cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0054588c bytes 89481c94
+ 005458cc bytes 79491c94
~~~


<a id="compare-b4d12f72dc758e391bb37f0a3e1ac6ae"></a>

### [`00545b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b74.md) → [`00545bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545bb4.md) FUN_00545bb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ee4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004ee534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee534.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00545b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b74.md#insn-00545b94)
- 新版 [`00545bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545bb4.md#insn-00545bd4)

~~~diff
- 00545b94 ["INT_ADD", "register:40f0:8", ["const:545b94:8", "const:4:8"]]
- 00545b94 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00545bd4 ["INT_ADD", "register:40f0:8", ["const:545bd4:8", "const:4:8"]]
+ 00545bd4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00545b94 bytes c7471c94
+ 00545bd4 bytes b7481c94
~~~


<a id="compare-93fb9e6a30915c20cef1552c59ccab07"></a>

### [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) → [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) FUN_00545c3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 13件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) [`00546108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546108.md) [`005462c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005462c4.md) [`00546454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md) [`005466d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005466d4.md)
- 新版 呼出元 2件 [`004fbefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md) [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 13件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) [`00546148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546148.md) [`00546304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546304.md) [`00546494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546494.md) [`00546714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546714.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00545cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md#insn-00545cd8) · [`00545d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md#insn-00545d00) · [`00545d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md#insn-00545d14)
- 新版 [`00545d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md#insn-00545d18) · [`00545d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md#insn-00545d40) · [`00545d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md#insn-00545d54)

~~~diff
- 00545cd8 ["INT_ADD", "register:40f0:8", ["const:545cd8:8", "const:4:8"]]
- 00545cd8 ["CALL", null, ["callee:00546494:8"]]
+ 00545d18 ["INT_ADD", "register:40f0:8", ["const:545d18:8", "const:4:8"]]
+ 00545d18 ["CALL", null, ["callee:00546494:8"]]
- 00545cd8 bytes df010094
+ 00545d18 bytes df010094
- 00545d00 ["INT_ADD", "register:40f0:8", ["const:545d00:8", "const:4:8"]]
- 00545d00 ["CALL", null, ["callee:00546494:8"]]
+ 00545d40 ["INT_ADD", "register:40f0:8", ["const:545d40:8", "const:4:8"]]
+ 00545d40 ["CALL", null, ["callee:00546494:8"]]
- 00545d00 bytes d5010094
+ 00545d40 bytes d5010094
- 00545d14 ["INT_ADD", "register:40f0:8", ["const:545d14:8", "const:4:8"]]
- 00545d14 ["CALL", null, ["callee:00546494:8"]]
+ 00545d54 ["INT_ADD", "register:40f0:8", ["const:545d54:8", "const:4:8"]]
+ 00545d54 ["CALL", null, ["callee:00546494:8"]]
- 00545d14 bytes d0010094
+ 00545d54 bytes d0010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1659b9de07d14c926db7f2d1ba14b095"></a>

### [`00546108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546108.md) → [`00546148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546148.md) FUN_00546148

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005461cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546108.md#insn-005461cc) · [`00546264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546108.md#insn-00546264) · [`005462c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546108.md#insn-005462c0)
- 新版 [`0054620c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546148.md#insn-0054620c) · [`005462a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546148.md#insn-005462a4) · [`00546300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546148.md#insn-00546300)

~~~diff
- 005461cc ["INT_ADD", "register:40f0:8", ["const:5461cc:8", "const:4:8"]]
- 005461cc ["CALL", null, ["callee:00c58050:8"]]
+ 0054620c ["INT_ADD", "register:40f0:8", ["const:54620c:8", "const:4:8"]]
+ 0054620c ["CALL", null, ["callee:00c58050:8"]]
- 005461cc bytes a1461c94
+ 0054620c bytes 91471c94
- 00546264 ["INT_ADD", "register:40f0:8", ["const:546264:8", "const:4:8"]]
- 00546264 ["CALL", null, ["callee:00c58050:8"]]
+ 005462a4 ["INT_ADD", "register:40f0:8", ["const:5462a4:8", "const:4:8"]]
+ 005462a4 ["CALL", null, ["callee:00c58050:8"]]
- 00546264 bytes 7b461c94
+ 005462a4 bytes 6b471c94
- 005462c0 ["INT_ADD", "register:40f0:8", ["const:5462c0:8", "const:4:8"]]
- 005462c0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00546300 ["INT_ADD", "register:40f0:8", ["const:546300:8", "const:4:8"]]
+ 00546300 ["CALL", null, ["callee:00c57ee0:8"]]
- 005462c0 bytes 08461c94
+ 00546300 bytes f8461c94
~~~


<a id="compare-dac71e60362943ff6bd93c49de5591c7"></a>

### [`005462c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005462c4.md) → [`00546304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546304.md) FUN_00546304

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005462c4.md#insn-00546364) · [`005463f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005462c4.md#insn-005463f4) · [`00546450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005462c4.md#insn-00546450)
- 新版 [`005463a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546304.md#insn-005463a4) · [`00546434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546304.md#insn-00546434) · [`00546490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546304.md#insn-00546490)

~~~diff
- 00546364 ["INT_ADD", "register:40f0:8", ["const:546364:8", "const:4:8"]]
- 00546364 ["CALL", null, ["callee:00c58050:8"]]
+ 005463a4 ["INT_ADD", "register:40f0:8", ["const:5463a4:8", "const:4:8"]]
+ 005463a4 ["CALL", null, ["callee:00c58050:8"]]
- 00546364 bytes 3b461c94
+ 005463a4 bytes 2b471c94
- 005463f4 ["INT_ADD", "register:40f0:8", ["const:5463f4:8", "const:4:8"]]
- 005463f4 ["CALL", null, ["callee:00c58050:8"]]
+ 00546434 ["INT_ADD", "register:40f0:8", ["const:546434:8", "const:4:8"]]
+ 00546434 ["CALL", null, ["callee:00c58050:8"]]
- 005463f4 bytes 17461c94
+ 00546434 bytes 07471c94
- 00546450 ["INT_ADD", "register:40f0:8", ["const:546450:8", "const:4:8"]]
- 00546450 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00546490 ["INT_ADD", "register:40f0:8", ["const:546490:8", "const:4:8"]]
+ 00546490 ["CALL", null, ["callee:00c57ee0:8"]]
- 00546450 bytes a4451c94
+ 00546490 bytes 94461c94
~~~


<a id="compare-e2b1e6fb04514b27800e7fef46e1ff76"></a>

### [`00546454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md) → [`00546494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546494.md) FUN_00546494

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) [`00546c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md) [`00546f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) [`00546ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546ccc.md) [`00546fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546fc4.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005464cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md#insn-005464cc) · [`00546508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md#insn-00546508) · [`005465a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md#insn-005465a8)
- 新版 [`0054650c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546494.md#insn-0054650c) · [`00546548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546494.md#insn-00546548) · [`005465e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546494.md#insn-005465e8)

~~~diff
- 005464cc ["INT_ADD", "register:40f0:8", ["const:5464cc:8", "const:4:8"]]
- 005464cc ["CALL", null, ["callee:00c58050:8"]]
+ 0054650c ["INT_ADD", "register:40f0:8", ["const:54650c:8", "const:4:8"]]
+ 0054650c ["CALL", null, ["callee:00c58050:8"]]
- 005464cc bytes e1451c94
+ 0054650c bytes d1461c94
- 00546508 ["INT_ADD", "register:40f0:8", ["const:546508:8", "const:4:8"]]
- 00546508 ["CALL", null, ["callee:00c58050:8"]]
+ 00546548 ["INT_ADD", "register:40f0:8", ["const:546548:8", "const:4:8"]]
+ 00546548 ["CALL", null, ["callee:00c58050:8"]]
- 00546508 bytes d2451c94
+ 00546548 bytes c2461c94
- 005465a8 ["INT_ADD", "register:40f0:8", ["const:5465a8:8", "const:4:8"]]
- 005465a8 ["CALL", null, ["callee:00c58050:8"]]
+ 005465e8 ["INT_ADD", "register:40f0:8", ["const:5465e8:8", "const:4:8"]]
+ 005465e8 ["CALL", null, ["callee:00c58050:8"]]
- 005465a8 bytes aa451c94
+ 005465e8 bytes 9a461c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d39f5ebfb67e5c071076dc158bc2b1a3"></a>

### [`005466d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005466d4.md) → [`00546714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546714.md) FUN_00546714

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005466d4.md#insn-00546760) · [`005467a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005466d4.md#insn-005467a4) · [`005467f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005466d4.md#insn-005467f8)
- 新版 [`005467a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546714.md#insn-005467a0) · [`005467e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546714.md#insn-005467e4) · [`00546838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546714.md#insn-00546838)

~~~diff
- 00546760 ["INT_ADD", "register:40f0:8", ["const:546760:8", "const:4:8"]]
- 00546760 ["CALL", null, ["callee:00c58050:8"]]
+ 005467a0 ["INT_ADD", "register:40f0:8", ["const:5467a0:8", "const:4:8"]]
+ 005467a0 ["CALL", null, ["callee:00c58050:8"]]
- 00546760 bytes 3c451c94
+ 005467a0 bytes 2c461c94
- 005467a4 ["INT_ADD", "register:40f0:8", ["const:5467a4:8", "const:4:8"]]
- 005467a4 ["CALL", null, ["callee:00c58050:8"]]
+ 005467e4 ["INT_ADD", "register:40f0:8", ["const:5467e4:8", "const:4:8"]]
+ 005467e4 ["CALL", null, ["callee:00c58050:8"]]
- 005467a4 bytes 2b451c94
+ 005467e4 bytes 1b461c94
- 005467f8 ["INT_ADD", "register:40f0:8", ["const:5467f8:8", "const:4:8"]]
- 005467f8 ["CALL", null, ["callee:00c58050:8"]]
+ 00546838 ["INT_ADD", "register:40f0:8", ["const:546838:8", "const:4:8"]]
+ 00546838 ["CALL", null, ["callee:00c58050:8"]]
- 005467f8 bytes 16451c94
+ 00546838 bytes 06461c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-561a714a5b3d57cbf19a1fb087770684"></a>

### [`005469c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005469c8.md) → [`00546a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546a08.md) FUN_00546a08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005469c8.md#insn-00546a64) · [`00546ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005469c8.md#insn-00546ab4) · [`00546afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005469c8.md#insn-00546afc)
- 新版 [`00546aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546a08.md#insn-00546aa4) · [`00546af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546a08.md#insn-00546af4) · [`00546b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546a08.md#insn-00546b3c)

~~~diff
- 00546a64 ["INT_ADD", "register:40f0:8", ["const:546a64:8", "const:4:8"]]
- 00546a64 ["CALL", null, ["callee:00c58050:8"]]
+ 00546aa4 ["INT_ADD", "register:40f0:8", ["const:546aa4:8", "const:4:8"]]
+ 00546aa4 ["CALL", null, ["callee:00c58050:8"]]
- 00546a64 bytes 7b441c94
+ 00546aa4 bytes 6b451c94
- 00546ab4 ["INT_ADD", "register:40f0:8", ["const:546ab4:8", "const:4:8"]]
- 00546ab4 ["CALL", null, ["callee:00c58050:8"]]
+ 00546af4 ["INT_ADD", "register:40f0:8", ["const:546af4:8", "const:4:8"]]
+ 00546af4 ["CALL", null, ["callee:00c58050:8"]]
- 00546ab4 bytes 67441c94
+ 00546af4 bytes 57451c94
- 00546afc ["INT_ADD", "register:40f0:8", ["const:546afc:8", "const:4:8"]]
- 00546afc ["CALL", null, ["callee:00c58050:8"]]
+ 00546b3c ["INT_ADD", "register:40f0:8", ["const:546b3c:8", "const:4:8"]]
+ 00546b3c ["CALL", null, ["callee:00c58050:8"]]
- 00546afc bytes 55441c94
+ 00546b3c bytes 45451c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5251dae9f6d9b1acc8caf099c13ddbc3"></a>

### [`00546c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md) → [`00546ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546ccc.md) FUN_00546ccc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 5件 [`00546454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md) [`00546f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md) [`00547164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 5件 [`00546494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546494.md) [`00546fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546fc4.md) [`005471a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005471a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md#insn-00546d24) · [`00546d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md#insn-00546d98) · [`00546db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md#insn-00546db0)
- 新版 [`00546d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546ccc.md#insn-00546d64) · [`00546dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546ccc.md#insn-00546dd8) · [`00546df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546ccc.md#insn-00546df0)

~~~diff
- 00546d24 ["INT_ADD", "register:40f0:8", ["const:546d24:8", "const:4:8"]]
- 00546d24 ["CALL", null, ["callee:00c58050:8"]]
+ 00546d64 ["INT_ADD", "register:40f0:8", ["const:546d64:8", "const:4:8"]]
+ 00546d64 ["CALL", null, ["callee:00c58050:8"]]
- 00546d24 bytes cb431c94
+ 00546d64 bytes bb441c94
- 00546d98 ["INT_ADD", "register:40f0:8", ["const:546d98:8", "const:4:8"]]
- 00546d98 ["CALL", null, ["callee:005471a4:8"]]
+ 00546dd8 ["INT_ADD", "register:40f0:8", ["const:546dd8:8", "const:4:8"]]
+ 00546dd8 ["CALL", null, ["callee:005471a4:8"]]
- 00546d98 bytes f3000094
+ 00546dd8 bytes f3000094
- 00546db0 ["INT_ADD", "register:40f0:8", ["const:546db0:8", "const:4:8"]]
- 00546db0 ["CALL", null, ["callee:00546494:8"]]
+ 00546df0 ["INT_ADD", "register:40f0:8", ["const:546df0:8", "const:4:8"]]
+ 00546df0 ["CALL", null, ["callee:00546494:8"]]
- 00546db0 bytes a9fdff97
+ 00546df0 bytes a9fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0db9a4ad63bb53ffb8b5b93cdfacf2ac"></a>

### [`00546f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md) → [`00546fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546fc4.md) FUN_00546fc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) [`00546c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md) [`00547164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md) · 呼出先 3件 [`00546454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) [`00546ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546ccc.md) [`005471a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005471a4.md) · 呼出先 3件 [`00546494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546494.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00546fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md#insn-00546fc0) · [`00546ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md#insn-00546ffc) · [`00547078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md#insn-00547078)
- 新版 [`00547000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546fc4.md#insn-00547000) · [`0054703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546fc4.md#insn-0054703c) · [`005470b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546fc4.md#insn-005470b8)

~~~diff
- 00546fc0 ["INT_ADD", "register:40f0:8", ["const:546fc0:8", "const:4:8"]]
- 00546fc0 ["CALL", null, ["callee:00546494:8"]]
+ 00547000 ["INT_ADD", "register:40f0:8", ["const:547000:8", "const:4:8"]]
+ 00547000 ["CALL", null, ["callee:00546494:8"]]
- 00546fc0 bytes 25fdff97
+ 00547000 bytes 25fdff97
- 00546ffc ["INT_ADD", "register:40f0:8", ["const:546ffc:8", "const:4:8"]]
- 00546ffc ["CALL", null, ["callee:00c58050:8"]]
+ 0054703c ["INT_ADD", "register:40f0:8", ["const:54703c:8", "const:4:8"]]
+ 0054703c ["CALL", null, ["callee:00c58050:8"]]
- 00546ffc bytes 15431c94
+ 0054703c bytes 05441c94
- 00547078 ["INT_ADD", "register:40f0:8", ["const:547078:8", "const:4:8"]]
- 00547078 ["CALL", null, ["callee:00c58050:8"]]
+ 005470b8 ["INT_ADD", "register:40f0:8", ["const:5470b8:8", "const:4:8"]]
+ 005470b8 ["CALL", null, ["callee:00c58050:8"]]
- 00547078 bytes f6421c94
+ 005470b8 bytes e6431c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1278227e665301686609e077f14c213a"></a>

### [`00547164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md) → [`005471a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005471a4.md) FUN_005471a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) [`00546c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md) · 呼出先 3件 [`00546f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) [`00546ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546ccc.md) · 呼出先 3件 [`00546fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00546/00546fc4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005471a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md#insn-005471a4) · [`005471e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md#insn-005471e0) · [`0054725c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md#insn-0054725c)
- 新版 [`005471e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005471a4.md#insn-005471e4) · [`00547220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005471a4.md#insn-00547220) · [`0054729c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005471a4.md#insn-0054729c)

~~~diff
- 005471a4 ["INT_ADD", "register:40f0:8", ["const:5471a4:8", "const:4:8"]]
- 005471a4 ["CALL", null, ["callee:00546fc4:8"]]
+ 005471e4 ["INT_ADD", "register:40f0:8", ["const:5471e4:8", "const:4:8"]]
+ 005471e4 ["CALL", null, ["callee:00546fc4:8"]]
- 005471a4 bytes 78ffff97
+ 005471e4 bytes 78ffff97
- 005471e0 ["INT_ADD", "register:40f0:8", ["const:5471e0:8", "const:4:8"]]
- 005471e0 ["CALL", null, ["callee:00c58050:8"]]
+ 00547220 ["INT_ADD", "register:40f0:8", ["const:547220:8", "const:4:8"]]
+ 00547220 ["CALL", null, ["callee:00c58050:8"]]
- 005471e0 bytes 9c421c94
+ 00547220 bytes 8c431c94
- 0054725c ["INT_ADD", "register:40f0:8", ["const:54725c:8", "const:4:8"]]
- 0054725c ["CALL", null, ["callee:00c58050:8"]]
+ 0054729c ["INT_ADD", "register:40f0:8", ["const:54729c:8", "const:4:8"]]
+ 0054729c ["CALL", null, ["callee:00c58050:8"]]
- 0054725c bytes 7d421c94
+ 0054729c bytes 6d431c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1724460be869abb43d5786a830067aac"></a>

### [`005473c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005473c4.md) → [`00547404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547404.md) FUN_00547404

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054748c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005473c4.md#insn-0054748c) · [`005474f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005473c4.md#insn-005474f8) · [`00547588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005473c4.md#insn-00547588)
- 新版 [`005474cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547404.md#insn-005474cc) · [`00547538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547404.md#insn-00547538) · [`005475c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547404.md#insn-005475c8)

~~~diff
- 0054748c ["INT_ADD", "register:40f0:8", ["const:54748c:8", "const:4:8"]]
- 0054748c ["CALL", null, ["callee:00c58050:8"]]
+ 005474cc ["INT_ADD", "register:40f0:8", ["const:5474cc:8", "const:4:8"]]
+ 005474cc ["CALL", null, ["callee:00c58050:8"]]
- 0054748c bytes f1411c94
+ 005474cc bytes e1421c94
- 005474f8 ["INT_ADD", "register:40f0:8", ["const:5474f8:8", "const:4:8"]]
- 005474f8 ["CALL", null, ["callee:00c58050:8"]]
+ 00547538 ["INT_ADD", "register:40f0:8", ["const:547538:8", "const:4:8"]]
+ 00547538 ["CALL", null, ["callee:00c58050:8"]]
- 005474f8 bytes d6411c94
+ 00547538 bytes c6421c94
- 00547588 ["INT_ADD", "register:40f0:8", ["const:547588:8", "const:4:8"]]
- 00547588 ["CALL", null, ["callee:00c58050:8"]]
+ 005475c8 ["INT_ADD", "register:40f0:8", ["const:5475c8:8", "const:4:8"]]
+ 005475c8 ["CALL", null, ["callee:00c58050:8"]]
- 00547588 bytes b2411c94
+ 005475c8 bytes a2421c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15f65f01f94253ef993a19b691f47287"></a>

### [`005476a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md) → [`005476e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005476e8.md) FUN_005476e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 4件 [`00547828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547828.md) [`0054794c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00545c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545c3c.md) · 呼出先 4件 [`00547868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547868.md) [`0054798c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/0054798c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00547740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md#insn-00547740) · [`00547780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md#insn-00547780) · [`0054779c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md#insn-0054779c)
- 新版 [`00547780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005476e8.md#insn-00547780) · [`005477c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005476e8.md#insn-005477c0) · [`005477dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005476e8.md#insn-005477dc)

~~~diff
- 00547740 ["INT_ADD", "register:40f0:8", ["const:547740:8", "const:4:8"]]
- 00547740 ["CALL", null, ["callee:0054798c:8"]]
+ 00547780 ["INT_ADD", "register:40f0:8", ["const:547780:8", "const:4:8"]]
+ 00547780 ["CALL", null, ["callee:0054798c:8"]]
- 00547740 bytes 83000094
+ 00547780 bytes 83000094
- 00547780 ["INT_ADD", "register:40f0:8", ["const:547780:8", "const:4:8"]]
- 00547780 ["CALL", null, ["callee:00547868:8"]]
+ 005477c0 ["INT_ADD", "register:40f0:8", ["const:5477c0:8", "const:4:8"]]
+ 005477c0 ["CALL", null, ["callee:00547868:8"]]
- 00547780 bytes 2a000094
+ 005477c0 bytes 2a000094
- 0054779c ["INT_ADD", "register:40f0:8", ["const:54779c:8", "const:4:8"]]
- 0054779c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005477dc ["INT_ADD", "register:40f0:8", ["const:5477dc:8", "const:4:8"]]
+ 005477dc ["CALL", null, ["callee:00c57eb0:8"]]
- 0054779c bytes c5401c94
+ 005477dc bytes b5411c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb20a14bac0abd5abdddd6838096857"></a>

### [`00547828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547828.md) → [`00547868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547868.md) FUN_00547868

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005476a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`005476e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005476e8.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005478e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547828.md#insn-005478e4) · [`00547924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547828.md#insn-00547924)
- 新版 [`00547924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547868.md#insn-00547924) · [`00547964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547868.md#insn-00547964)

~~~diff
- 005478e4 ["INT_ADD", "register:40f0:8", ["const:5478e4:8", "const:4:8"]]
- 005478e4 ["CALL", null, ["callee:00c58050:8"]]
+ 00547924 ["INT_ADD", "register:40f0:8", ["const:547924:8", "const:4:8"]]
+ 00547924 ["CALL", null, ["callee:00c58050:8"]]
- 005478e4 bytes db401c94
+ 00547924 bytes cb411c94
- 00547924 ["INT_ADD", "register:40f0:8", ["const:547924:8", "const:4:8"]]
- 00547924 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00547964 ["INT_ADD", "register:40f0:8", ["const:547964:8", "const:4:8"]]
+ 00547964 ["CALL", null, ["callee:00c57eb0:8"]]
- 00547924 bytes 63401c94
+ 00547964 bytes 53411c94
~~~


<a id="compare-c7e186f42a78e0d4daeef4539d481a47"></a>

### [`0054794c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md) → [`0054798c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/0054798c.md) FUN_0054798c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005476a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`005476e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/005476e8.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005479cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md#insn-005479cc) · [`00547a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md#insn-00547a70) · [`00547ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md#insn-00547ad0)
- 新版 [`00547a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/0054798c.md#insn-00547a0c) · [`00547ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/0054798c.md#insn-00547ab0) · [`00547b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/0054798c.md#insn-00547b10)

~~~diff
- 005479cc ["INT_ADD", "register:40f0:8", ["const:5479cc:8", "const:4:8"]]
- 005479cc ["CALL", null, ["callee:00c58050:8"]]
+ 00547a0c ["INT_ADD", "register:40f0:8", ["const:547a0c:8", "const:4:8"]]
+ 00547a0c ["CALL", null, ["callee:00c58050:8"]]
- 005479cc bytes a1401c94
+ 00547a0c bytes 91411c94
- 00547a70 ["INT_ADD", "register:40f0:8", ["const:547a70:8", "const:4:8"]]
- 00547a70 ["CALL", null, ["callee:00c58050:8"]]
+ 00547ab0 ["INT_ADD", "register:40f0:8", ["const:547ab0:8", "const:4:8"]]
+ 00547ab0 ["CALL", null, ["callee:00c58050:8"]]
- 00547a70 bytes 78401c94
+ 00547ab0 bytes 68411c94
- 00547ad0 ["INT_ADD", "register:40f0:8", ["const:547ad0:8", "const:4:8"]]
- 00547ad0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00547b10 ["INT_ADD", "register:40f0:8", ["const:547b10:8", "const:4:8"]]
+ 00547b10 ["CALL", null, ["callee:00c57ee0:8"]]
- 00547ad0 bytes 04401c94
+ 00547b10 bytes f4401c94
~~~


<a id="compare-4f874bbd455f152aa4f0a587ad938100"></a>

### [`00547b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) → [`00547bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md) FUN_00547bb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`004ff000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md) [`00563bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md) [`00584ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`004ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff040.md) [`00563c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c14.md) [`00584f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00547bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md#insn-00547bec) · [`00547c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md#insn-00547c14) · [`00547ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md#insn-00547ca0)
- 新版 [`00547c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md#insn-00547c2c) · [`00547c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md#insn-00547c54) · [`00547ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md#insn-00547ce0)

~~~diff
- 00547bec ["INT_ADD", "register:40f0:8", ["const:547bec:8", "const:4:8"]]
- 00547bec ["CALL", null, ["callee:00c58050:8"]]
+ 00547c2c ["INT_ADD", "register:40f0:8", ["const:547c2c:8", "const:4:8"]]
+ 00547c2c ["CALL", null, ["callee:00c58050:8"]]
- 00547bec bytes 19401c94
+ 00547c2c bytes 09411c94
- 00547c14 ["INT_ADD", "register:40f0:8", ["const:547c14:8", "const:4:8"]]
- 00547c14 ["CALL", null, ["callee:00c58050:8"]]
+ 00547c54 ["INT_ADD", "register:40f0:8", ["const:547c54:8", "const:4:8"]]
+ 00547c54 ["CALL", null, ["callee:00c58050:8"]]
- 00547c14 bytes 0f401c94
+ 00547c54 bytes ff401c94
- 00547ca0 ["INT_ADD", "register:40f0:8", ["const:547ca0:8", "const:4:8"]]
- 00547ca0 ["CALL", null, ["callee:00c58050:8"]]
+ 00547ce0 ["INT_ADD", "register:40f0:8", ["const:547ce0:8", "const:4:8"]]
+ 00547ce0 ["CALL", null, ["callee:00c58050:8"]]
- 00547ca0 bytes ec3f1c94
+ 00547ce0 bytes dc401c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6b01b910ca60d314d86179dae466b4"></a>

### [`00547d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d30.md) → [`00547d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547d70.md) FUN_00547d70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00547d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d30.md#insn-00547d4c) · [`00547d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d30.md#insn-00547d5c)
- 新版 [`00547d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547d70.md#insn-00547d8c) · [`00547d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547d70.md#insn-00547d9c)

~~~diff
- 00547d4c ["INT_ADD", "register:40f0:8", ["const:547d4c:8", "const:4:8"]]
- 00547d4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00547d8c ["INT_ADD", "register:40f0:8", ["const:547d8c:8", "const:4:8"]]
+ 00547d8c ["CALL", null, ["callee:00c57eb0:8"]]
- 00547d4c bytes 593f1c94
+ 00547d8c bytes 49401c94
- 00547d5c ["INT_ADD", "register:40f0:8", ["const:547d5c:8", "const:4:8"]]
- 00547d5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00547d9c ["INT_ADD", "register:40f0:8", ["const:547d9c:8", "const:4:8"]]
+ 00547d9c ["CALL", null, ["callee:00c57eb0:8"]]
- 00547d5c bytes 553f1c94
+ 00547d9c bytes 45401c94
~~~


<a id="compare-e2a908b1aa45a10cbdac125fba6349f0"></a>

### [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md) → [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md) FUN_00548098

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`004ff568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff568.md) [`004ff6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff6e4.md) [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`00504180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504180.md) [`0052308c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/0052308c.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 7件 [`004ff5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff5a8.md) [`004ff724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff724.md) [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) [`005041c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005041c0.md) [`005230cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230cc.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005480d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md#insn-005480d4) · [`005480fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md#insn-005480fc) · [`00548188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md#insn-00548188)
- 新版 [`00548114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md#insn-00548114) · [`0054813c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md#insn-0054813c) · [`005481c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md#insn-005481c8)

~~~diff
- 005480d4 ["INT_ADD", "register:40f0:8", ["const:5480d4:8", "const:4:8"]]
- 005480d4 ["CALL", null, ["callee:00c58050:8"]]
+ 00548114 ["INT_ADD", "register:40f0:8", ["const:548114:8", "const:4:8"]]
+ 00548114 ["CALL", null, ["callee:00c58050:8"]]
- 005480d4 bytes df3e1c94
+ 00548114 bytes cf3f1c94
- 005480fc ["INT_ADD", "register:40f0:8", ["const:5480fc:8", "const:4:8"]]
- 005480fc ["CALL", null, ["callee:00c58050:8"]]
+ 0054813c ["INT_ADD", "register:40f0:8", ["const:54813c:8", "const:4:8"]]
+ 0054813c ["CALL", null, ["callee:00c58050:8"]]
- 005480fc bytes d53e1c94
+ 0054813c bytes c53f1c94
- 00548188 ["INT_ADD", "register:40f0:8", ["const:548188:8", "const:4:8"]]
- 00548188 ["CALL", null, ["callee:00c58050:8"]]
+ 005481c8 ["INT_ADD", "register:40f0:8", ["const:5481c8:8", "const:4:8"]]
+ 005481c8 ["CALL", null, ["callee:00c58050:8"]]
- 00548188 bytes b23e1c94
+ 005481c8 bytes a23f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f67b3eb84e3e3f075a16fcd8358258f0"></a>

### [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) → [`00548258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md) FUN_00548258

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) [`0051adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md) [`00560000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md) [`00c04d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md) · 呼出先 1件 [`00c59bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59bc0.md)
- 新版 呼出元 4件 [`005085bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md) [`0051ae2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md) [`00560040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560040.md) [`00c05180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md) · 呼出先 1件 [`00c59fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59fc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md#insn-00548288)
- 新版 [`005482c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md#insn-005482c8)

~~~diff
- 00548288 ["INT_ADD", "register:40f0:8", ["const:548288:8", "const:4:8"]]
- 00548288 ["CALL", null, ["callee:00c59fc0:8"]]
+ 005482c8 ["INT_ADD", "register:40f0:8", ["const:5482c8:8", "const:4:8"]]
+ 005482c8 ["CALL", null, ["callee:00c59fc0:8"]]
- 00548288 bytes 4e461c94
+ 005482c8 bytes 3e471c94
~~~


<a id="compare-6ff2a9f1a4f082d7a2832ab87830633e"></a>

### [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) → [`005483b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md) FUN_005483b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00501348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md) [`00502bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md) [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00501388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501388.md) [`00502c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502c3c.md) [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00548584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005483e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md#insn-005483e4) · [`00548454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md#insn-00548454) · [`00548468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md#insn-00548468)
- 新版 [`00548424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md#insn-00548424) · [`00548494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md#insn-00548494) · [`005484a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md#insn-005484a8)

~~~diff
- 005483e4 ["INT_ADD", "register:40f0:8", ["const:5483e4:8", "const:4:8"]]
- 005483e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00548424 ["INT_ADD", "register:40f0:8", ["const:548424:8", "const:4:8"]]
+ 00548424 ["CALL", null, ["callee:00c57e90:8"]]
- 005483e4 bytes ab3d1c94
+ 00548424 bytes 9b3e1c94
- 00548454 ["INT_ADD", "register:40f0:8", ["const:548454:8", "const:4:8"]]
- 00548454 ["CALL", null, ["callee:00c53d00:8"]]
+ 00548494 ["INT_ADD", "register:40f0:8", ["const:548494:8", "const:4:8"]]
+ 00548494 ["CALL", null, ["callee:00c53d00:8"]]
- 00548454 bytes 232d1c94
+ 00548494 bytes 1b2e1c94
- 00548468 ["COPY", "register:0:8", ["register:4040:8"]]
- 00548468 ["INT_ADD", "register:40f0:8", ["const:548468:8", "const:4:8"]]
- 00548468 ["CALLIND", null, ["register:0:8"]]
+ 005484a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005484a8 ["INT_ADD", "register:40f0:8", ["const:5484a8:8", "const:4:8"]]
+ 005484a8 ["CALLIND", null, ["register:0:8"]]
- 00548468 bytes 00013fd6
+ 005484a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a82c5b44dc06c9243961ba799ea2319"></a>

### [`005484b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005484b8.md) → [`005484f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005484f8.md) FUN_005484f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005484f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005484b8.md#insn-005484f8) · [`0054850c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005484b8.md#insn-0054850c) · [`00548514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005484b8.md#insn-00548514)
- 新版 [`00548538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005484f8.md#insn-00548538) · [`0054854c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005484f8.md#insn-0054854c) · [`00548554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005484f8.md#insn-00548554)

~~~diff
- 005484f8 ["INT_ADD", "register:40f0:8", ["const:5484f8:8", "const:4:8"]]
- 005484f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00548538 ["INT_ADD", "register:40f0:8", ["const:548538:8", "const:4:8"]]
+ 00548538 ["CALL", null, ["callee:00c53d00:8"]]
- 005484f8 bytes fa2c1c94
+ 00548538 bytes f22d1c94
- 0054850c ["COPY", "register:0:8", ["register:4040:8"]]
- 0054850c ["INT_ADD", "register:40f0:8", ["const:54850c:8", "const:4:8"]]
- 0054850c ["CALLIND", null, ["register:0:8"]]
+ 0054854c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054854c ["INT_ADD", "register:40f0:8", ["const:54854c:8", "const:4:8"]]
+ 0054854c ["CALLIND", null, ["register:0:8"]]
- 0054850c bytes 00013fd6
+ 0054854c bytes 00013fd6
- 00548514 ["INT_ADD", "register:40f0:8", ["const:548514:8", "const:4:8"]]
- 00548514 ["CALL", null, ["callee:00c57e80:8"]]
+ 00548554 ["INT_ADD", "register:40f0:8", ["const:548554:8", "const:4:8"]]
+ 00548554 ["CALL", null, ["callee:00c57e80:8"]]
- 00548514 bytes 5b3d1c94
+ 00548554 bytes 4b3e1c94
~~~


<a id="compare-6eb13e0e637da5fd225cf20a218ac066"></a>

### [`00548558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md) → [`00548598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md) FUN_00548598

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00501600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501600.md) [`00501bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501bac.md) [`005292f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 4件 [`00501640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501640.md) [`00501bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501bec.md) [`00529334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md) [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00548584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005485c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md#insn-005485c4) · [`005485f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md#insn-005485f0) · [`00548650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md#insn-00548650)
- 新版 [`00548604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md#insn-00548604) · [`00548630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md#insn-00548630) · [`00548690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md#insn-00548690)

~~~diff
- 005485c4 ["INT_ADD", "register:40f0:8", ["const:5485c4:8", "const:4:8"]]
- 005485c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00548604 ["INT_ADD", "register:40f0:8", ["const:548604:8", "const:4:8"]]
+ 00548604 ["CALL", null, ["callee:00c57e90:8"]]
- 005485c4 bytes 333d1c94
+ 00548604 bytes 233e1c94
- 005485f0 ["INT_ADD", "register:40f0:8", ["const:5485f0:8", "const:4:8"]]
- 005485f0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00548630 ["INT_ADD", "register:40f0:8", ["const:548630:8", "const:4:8"]]
+ 00548630 ["CALL", null, ["callee:00c53cd0:8"]]
- 005485f0 bytes b02c1c94
+ 00548630 bytes a82d1c94
- 00548650 ["INT_ADD", "register:40f0:8", ["const:548650:8", "const:4:8"]]
- 00548650 ["CALL", null, ["callee:00c53d00:8"]]
+ 00548690 ["INT_ADD", "register:40f0:8", ["const:548690:8", "const:4:8"]]
+ 00548690 ["CALL", null, ["callee:00c53d00:8"]]
- 00548650 bytes a42c1c94
+ 00548690 bytes 9c2d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d6c22143d935edce94ae657a28da59"></a>

### [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) → [`005486f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md) FUN_005486f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00501700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0054887c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/0054887c.md) [`00548a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md)
- 新版 呼出元 1件 [`00501740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`005488bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005488bc.md) [`00548a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md#insn-0054876c) · [`00548794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md#insn-00548794) · [`005487ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md#insn-005487ac)
- 新版 [`005487ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md#insn-005487ac) · [`005487d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md#insn-005487d4) · [`005487ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md#insn-005487ec)

~~~diff
- 0054876c ["INT_ADD", "register:40f0:8", ["const:54876c:8", "const:4:8"]]
- 0054876c ["CALL", null, ["callee:00c57e90:8"]]
+ 005487ac ["INT_ADD", "register:40f0:8", ["const:5487ac:8", "const:4:8"]]
+ 005487ac ["CALL", null, ["callee:00c57e90:8"]]
- 0054876c bytes c93c1c94
+ 005487ac bytes b93d1c94
- 00548794 ["INT_ADD", "register:40f0:8", ["const:548794:8", "const:4:8"]]
- 00548794 ["CALL", null, ["callee:005027f8:8"]]
+ 005487d4 ["INT_ADD", "register:40f0:8", ["const:5487d4:8", "const:4:8"]]
+ 005487d4 ["CALL", null, ["callee:005027f8:8"]]
- 00548794 bytes 09e8fe97
+ 005487d4 bytes 09e8fe97
- 005487ac ["INT_ADD", "register:40f0:8", ["const:5487ac:8", "const:4:8"]]
- 005487ac ["CALL", null, ["callee:005488bc:8"]]
+ 005487ec ["INT_ADD", "register:40f0:8", ["const:5487ec:8", "const:4:8"]]
+ 005487ec ["CALL", null, ["callee:005488bc:8"]]
- 005487ac bytes 34000094
+ 005487ec bytes 34000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd6d037e98450d39669bd0694debdd6"></a>

### [`005489b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005489b4.md) → [`005489f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005489f4.md) FUN_005489f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005489d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005489b4.md#insn-005489d8) · [`005489fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005489b4.md#insn-005489fc)
- 新版 [`00548a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005489f4.md#insn-00548a18) · [`00548a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005489f4.md#insn-00548a3c)

~~~diff
- 005489d8 ["INT_ADD", "register:40f0:8", ["const:5489d8:8", "const:4:8"]]
- 005489d8 ["CALL", null, ["callee:0053af90:8"]]
+ 00548a18 ["INT_ADD", "register:40f0:8", ["const:548a18:8", "const:4:8"]]
+ 00548a18 ["CALL", null, ["callee:0053af90:8"]]
- 005489d8 bytes 5ec9ff97
+ 00548a18 bytes 5ec9ff97
- 005489fc ["INT_ADD", "register:40f0:8", ["const:5489fc:8", "const:4:8"]]
- 005489fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00548a3c ["INT_ADD", "register:40f0:8", ["const:548a3c:8", "const:4:8"]]
+ 00548a3c ["CALL", null, ["callee:00c57eb0:8"]]
- 005489fc bytes 2d3c1c94
+ 00548a3c bytes 1d3d1c94
~~~


<a id="compare-2cbe129bfb3bb7fca7371b6367370d02"></a>

### [`00548a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a88.md) → [`00548ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548ac8.md) FUN_00548ac8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00502448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md) · 呼出先 2件 [`00548adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548adc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00502488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502488.md) · 呼出先 2件 [`00548b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548b1c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a88.md#insn-00548ab0) · [`00548ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a88.md#insn-00548ad4)
- 新版 [`00548af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548ac8.md#insn-00548af0) · [`00548b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548ac8.md#insn-00548b14)

~~~diff
- 00548ab0 ["INT_ADD", "register:40f0:8", ["const:548ab0:8", "const:4:8"]]
- 00548ab0 ["CALL", null, ["callee:00548b1c:8"]]
+ 00548af0 ["INT_ADD", "register:40f0:8", ["const:548af0:8", "const:4:8"]]
+ 00548af0 ["CALL", null, ["callee:00548b1c:8"]]
- 00548ab0 bytes 0b000094
+ 00548af0 bytes 0b000094
- 00548ad4 ["INT_ADD", "register:40f0:8", ["const:548ad4:8", "const:4:8"]]
- 00548ad4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00548b14 ["INT_ADD", "register:40f0:8", ["const:548b14:8", "const:4:8"]]
+ 00548b14 ["CALL", null, ["callee:00c57ee0:8"]]
- 00548ad4 bytes 033c1c94
+ 00548b14 bytes f33c1c94
~~~


<a id="compare-81f051e3359965b5204b842d586cc1cd"></a>

### [`00548b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md) → [`00548bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548bc0.md) FUN_00548bc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005025bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548cdc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`005025fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00548d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d1c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md#insn-00548bec) · [`00548c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md#insn-00548c18) · [`00548c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md#insn-00548c78)
- 新版 [`00548c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548bc0.md#insn-00548c2c) · [`00548c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548bc0.md#insn-00548c58) · [`00548cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548bc0.md#insn-00548cb8)

~~~diff
- 00548bec ["INT_ADD", "register:40f0:8", ["const:548bec:8", "const:4:8"]]
- 00548bec ["CALL", null, ["callee:00c57e90:8"]]
+ 00548c2c ["INT_ADD", "register:40f0:8", ["const:548c2c:8", "const:4:8"]]
+ 00548c2c ["CALL", null, ["callee:00c57e90:8"]]
- 00548bec bytes a93b1c94
+ 00548c2c bytes 993c1c94
- 00548c18 ["INT_ADD", "register:40f0:8", ["const:548c18:8", "const:4:8"]]
- 00548c18 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00548c58 ["INT_ADD", "register:40f0:8", ["const:548c58:8", "const:4:8"]]
+ 00548c58 ["CALL", null, ["callee:00c53cd0:8"]]
- 00548c18 bytes 262b1c94
+ 00548c58 bytes 1e2c1c94
- 00548c78 ["INT_ADD", "register:40f0:8", ["const:548c78:8", "const:4:8"]]
- 00548c78 ["CALL", null, ["callee:00c53d00:8"]]
+ 00548cb8 ["INT_ADD", "register:40f0:8", ["const:548cb8:8", "const:4:8"]]
+ 00548cb8 ["CALL", null, ["callee:00c53d00:8"]]
- 00548c78 bytes 1a2b1c94
+ 00548cb8 bytes 122c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f51cb64100913bfb8b9691fac3bbd51"></a>

### [`00548d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d48.md) → [`00548d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d88.md) FUN_00548d88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d48.md#insn-00548d58)
- 新版 [`00548d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d88.md#insn-00548d98)

~~~diff
- 00548d58 ["INT_ADD", "register:40f0:8", ["const:548d58:8", "const:4:8"]]
- 00548d58 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00548d98 ["INT_ADD", "register:40f0:8", ["const:548d98:8", "const:4:8"]]
+ 00548d98 ["CALL", null, ["callee:00c57ea0:8"]]
- 00548d58 bytes 523b1c94
+ 00548d98 bytes 423c1c94
~~~


<a id="compare-7641b051ea3132a1a47d7367692dbc36"></a>

### [`00548d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md) → [`00548dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548dd4.md) FUN_00548dd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) [`00548d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d6c.md) · 呼出先 2件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0050376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md) [`00548dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548dac.md) · 呼出先 2件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md#insn-00548db4) · [`00548dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md#insn-00548dec) · [`00548e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md#insn-00548e00)
- 新版 [`00548df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548dd4.md#insn-00548df4) · [`00548e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548dd4.md#insn-00548e2c) · [`00548e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548dd4.md#insn-00548e40)

~~~diff
- 00548db4 ["INT_ADD", "register:40f0:8", ["const:548db4:8", "const:4:8"]]
- 00548db4 ["CALL", null, ["callee:0053b424:8"]]
+ 00548df4 ["INT_ADD", "register:40f0:8", ["const:548df4:8", "const:4:8"]]
+ 00548df4 ["CALL", null, ["callee:0053b424:8"]]
- 00548db4 bytes 8cc9ff97
+ 00548df4 bytes 8cc9ff97
- 00548dec ["INT_ADD", "register:40f0:8", ["const:548dec:8", "const:4:8"]]
- 00548dec ["CALL", null, ["callee:00c57eb0:8"]]
+ 00548e2c ["INT_ADD", "register:40f0:8", ["const:548e2c:8", "const:4:8"]]
+ 00548e2c ["CALL", null, ["callee:00c57eb0:8"]]
- 00548dec bytes 313b1c94
+ 00548e2c bytes 213c1c94
- 00548e00 ["INT_ADD", "register:40f0:8", ["const:548e00:8", "const:4:8"]]
- 00548e00 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00548e40 ["INT_ADD", "register:40f0:8", ["const:548e40:8", "const:4:8"]]
+ 00548e40 ["CALL", null, ["callee:00c57eb0:8"]]
- 00548e00 bytes 2c3b1c94
+ 00548e40 bytes 1c3c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbc7cae7f523098f4b791f34b4bca8b3"></a>

### [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) → [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) FUN_00548e68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`004e443c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md) [`00502ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md) [`00506f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md) [`0050aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md) [`00512cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 10件 [`004e447c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e447c.md) [`00502f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502f10.md) [`00506f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md) [`0050aae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050aae4.md) [`00512d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512d08.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md#insn-00548e6c) · [`00548ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md#insn-00548ea4) · [`00548ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md#insn-00548ecc)
- 新版 [`00548eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md#insn-00548eac) · [`00548ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md#insn-00548ee4) · [`00548f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md#insn-00548f0c)

~~~diff
- 00548e6c ["INT_ADD", "register:40f0:8", ["const:548e6c:8", "const:4:8"]]
- 00548e6c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00548eac ["INT_ADD", "register:40f0:8", ["const:548eac:8", "const:4:8"]]
+ 00548eac ["CALL", null, ["callee:00c57eb0:8"]]
- 00548e6c bytes 113b1c94
+ 00548eac bytes 013c1c94
- 00548ea4 ["INT_ADD", "register:40f0:8", ["const:548ea4:8", "const:4:8"]]
- 00548ea4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00548ee4 ["INT_ADD", "register:40f0:8", ["const:548ee4:8", "const:4:8"]]
+ 00548ee4 ["CALL", null, ["callee:00c57e90:8"]]
- 00548ea4 bytes fb3a1c94
+ 00548ee4 bytes eb3b1c94
- 00548ecc ["INT_ADD", "register:40f0:8", ["const:548ecc:8", "const:4:8"]]
- 00548ecc ["CALL", null, ["callee:00c58000:8"]]
+ 00548f0c ["INT_ADD", "register:40f0:8", ["const:548f0c:8", "const:4:8"]]
+ 00548f0c ["CALL", null, ["callee:00c58000:8"]]
- 00548ecc bytes 4d3b1c94
+ 00548f0c bytes 3d3c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98ecfd214e1735f3dd97a535f178ceba"></a>

### [`00548f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548f48.md) → [`00548f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548f88.md) FUN_00548f88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00503d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503d58.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00503d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503d98.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00548fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548f48.md#insn-00548fdc) · [`00549058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548f48.md#insn-00549058)
- 新版 [`0054901c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548f88.md#insn-0054901c) · [`00549098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548f88.md#insn-00549098)

~~~diff
- 00548fdc ["INT_ADD", "register:40f0:8", ["const:548fdc:8", "const:4:8"]]
- 00548fdc ["CALL", null, ["callee:00c58050:8"]]
+ 0054901c ["INT_ADD", "register:40f0:8", ["const:54901c:8", "const:4:8"]]
+ 0054901c ["CALL", null, ["callee:00c58050:8"]]
- 00548fdc bytes 1d3b1c94
+ 0054901c bytes 0d3c1c94
- 00549058 ["INT_ADD", "register:40f0:8", ["const:549058:8", "const:4:8"]]
- 00549058 ["CALL", null, ["callee:00c58050:8"]]
+ 00549098 ["INT_ADD", "register:40f0:8", ["const:549098:8", "const:4:8"]]
+ 00549098 ["CALL", null, ["callee:00c58050:8"]]
- 00549058 bytes fe3a1c94
+ 00549098 bytes ee3b1c94
~~~


<a id="compare-ded93d8bf91fac45f15e3126bf2a1b6f"></a>

### [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) → [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) FUN_005490d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00503ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503ef4.md) [`00563ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md) [`005836cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005836cc.md) [`00584ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00503f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503f34.md) [`00563b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md) [`0058370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md) [`00584f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005490b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md#insn-005490b4) · [`00549148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md#insn-00549148) · [`005491ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md#insn-005491ac)
- 新版 [`005490f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md#insn-005490f4) · [`00549188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md#insn-00549188) · [`005491ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md#insn-005491ec)

~~~diff
- 005490b4 ["INT_ADD", "register:40f0:8", ["const:5490b4:8", "const:4:8"]]
- 005490b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005490f4 ["INT_ADD", "register:40f0:8", ["const:5490f4:8", "const:4:8"]]
+ 005490f4 ["CALL", null, ["callee:00c57e90:8"]]
- 005490b4 bytes 773a1c94
+ 005490f4 bytes 673b1c94
- 00549148 ["INT_ADD", "register:40f0:8", ["const:549148:8", "const:4:8"]]
- 00549148 ["CALL", null, ["callee:00c58050:8"]]
+ 00549188 ["INT_ADD", "register:40f0:8", ["const:549188:8", "const:4:8"]]
+ 00549188 ["CALL", null, ["callee:00c58050:8"]]
- 00549148 bytes c23a1c94
+ 00549188 bytes b23b1c94
- 005491ac ["INT_ADD", "register:40f0:8", ["const:5491ac:8", "const:4:8"]]
- 005491ac ["CALL", null, ["callee:0043bba4:8"]]
+ 005491ec ["INT_ADD", "register:40f0:8", ["const:5491ec:8", "const:4:8"]]
+ 005491ec ["CALL", null, ["callee:0043bba4:8"]]
- 005491ac bytes 6ecafb97
+ 005491ec bytes 6ecafb97
~~~


<a id="compare-6e18e68468bf13b7e7926dac0a874871"></a>

### [`00549214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549214.md) → [`00549254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549254.md) FUN_00549254

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549214.md#insn-00549260)
- 新版 [`005492a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549254.md#insn-005492a0)

~~~diff
- 00549260 ["INT_ADD", "register:40f0:8", ["const:549260:8", "const:4:8"]]
- 00549260 ["CALL", null, ["callee:00c57fd0:8"]]
+ 005492a0 ["INT_ADD", "register:40f0:8", ["const:5492a0:8", "const:4:8"]]
+ 005492a0 ["CALL", null, ["callee:00c57fd0:8"]]
- 00549260 bytes 5c3a1c94
+ 005492a0 bytes 4c3b1c94
~~~


<a id="compare-e53e6f7a46f855d41849f9f23a1bab45"></a>

### [`005494c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005494c0.md) → [`00549500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549500.md) FUN_00549500

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005494c0.md#insn-0054952c) · [`0054953c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005494c0.md#insn-0054953c) · [`0054955c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005494c0.md#insn-0054955c)
- 新版 [`0054956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549500.md#insn-0054956c) · [`0054957c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549500.md#insn-0054957c) · [`0054959c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549500.md#insn-0054959c)

~~~diff
- 0054952c ["COPY", "register:0:8", ["register:4040:8"]]
- 0054952c ["INT_ADD", "register:40f0:8", ["const:54952c:8", "const:4:8"]]
- 0054952c ["CALLIND", null, ["register:0:8"]]
+ 0054956c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054956c ["INT_ADD", "register:40f0:8", ["const:54956c:8", "const:4:8"]]
+ 0054956c ["CALLIND", null, ["register:0:8"]]
- 0054952c bytes 00013fd6
+ 0054956c bytes 00013fd6
- 0054953c ["COPY", "register:0:8", ["register:4040:8"]]
- 0054953c ["INT_ADD", "register:40f0:8", ["const:54953c:8", "const:4:8"]]
- 0054953c ["CALLIND", null, ["register:0:8"]]
+ 0054957c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054957c ["INT_ADD", "register:40f0:8", ["const:54957c:8", "const:4:8"]]
+ 0054957c ["CALLIND", null, ["register:0:8"]]
- 0054953c bytes 00013fd6
+ 0054957c bytes 00013fd6
- 0054955c ["COPY", "register:0:8", ["register:4040:8"]]
- 0054955c ["INT_ADD", "register:40f0:8", ["const:54955c:8", "const:4:8"]]
- 0054955c ["CALLIND", null, ["register:0:8"]]
+ 0054959c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054959c ["INT_ADD", "register:40f0:8", ["const:54959c:8", "const:4:8"]]
+ 0054959c ["CALLIND", null, ["register:0:8"]]
- 0054955c bytes 00013fd6
+ 0054959c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-801b51e4e53441ff3cf38e58ff7870c7"></a>

### [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) → [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) FUN_00549668

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`005019f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019f4.md) [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) [`00514ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514ac8.md) [`00514d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) · 呼出先 2件 [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`00501a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a34.md) [`00507fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md) [`00514b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514b08.md) [`00514da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md) [`005269d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md) · 呼出先 2件 [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md#insn-00549644) · [`00549650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md#insn-00549650) · [`00549660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md#insn-00549660)
- 新版 [`00549684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md#insn-00549684) · [`00549690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md#insn-00549690) · [`005496a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md#insn-005496a0)

~~~diff
- 00549644 ["INT_ADD", "register:40f0:8", ["const:549644:8", "const:4:8"]]
- 00549644 ["CALL", null, ["local:b0:8"]]
+ 00549684 ["INT_ADD", "register:40f0:8", ["const:549684:8", "const:4:8"]]
+ 00549684 ["CALL", null, ["local:b0:8"]]
- 00549644 bytes f9ffff97
+ 00549684 bytes f9ffff97
- 00549650 ["INT_ADD", "register:40f0:8", ["const:549650:8", "const:4:8"]]
- 00549650 ["CALL", null, ["local:b0:8"]]
+ 00549690 ["INT_ADD", "register:40f0:8", ["const:549690:8", "const:4:8"]]
+ 00549690 ["CALL", null, ["local:b0:8"]]
- 00549650 bytes f6ffff97
+ 00549690 bytes f6ffff97
- 00549660 ["INT_ADD", "register:40f0:8", ["const:549660:8", "const:4:8"]]
- 00549660 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005496a0 ["INT_ADD", "register:40f0:8", ["const:5496a0:8", "const:4:8"]]
+ 005496a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00549660 bytes 14391c94
+ 005496a0 bytes 043a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb09d91f19ce1eacd9067513e432a49"></a>

### [`00549d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d24.md) → [`00549d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549d64.md) FUN_00549d64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005405fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054063c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d24.md#insn-00549d4c)
- 新版 [`00549d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549d64.md#insn-00549d8c)

~~~diff
- 00549d4c ["INT_ADD", "register:40f0:8", ["const:549d4c:8", "const:4:8"]]
- 00549d4c ["CALL", null, ["callee:0054063c:8"]]
+ 00549d8c ["INT_ADD", "register:40f0:8", ["const:549d8c:8", "const:4:8"]]
+ 00549d8c ["CALL", null, ["callee:0054063c:8"]]
- 00549d4c bytes 2cdaff97
+ 00549d8c bytes 2cdaff97
~~~


<a id="compare-373694c98211439d9cc46112c1e96255"></a>

### [`00549d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d90.md) → [`00549dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549dd0.md) FUN_00549dd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005405fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0054063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054063c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d90.md#insn-00549dd0)
- 新版 [`00549e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549dd0.md#insn-00549e10)

~~~diff
- 00549dd0 ["INT_ADD", "register:40f0:8", ["const:549dd0:8", "const:4:8"]]
- 00549dd0 ["CALL", null, ["callee:0054063c:8"]]
+ 00549e10 ["INT_ADD", "register:40f0:8", ["const:549e10:8", "const:4:8"]]
+ 00549e10 ["CALL", null, ["callee:0054063c:8"]]
- 00549dd0 bytes 0bdaff97
+ 00549e10 bytes 0bdaff97
~~~


<a id="compare-03a35f065be2a9c7944337014b4fd38b"></a>

### [`00549dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) → [`00549e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549e2c.md) FUN_00549e2c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050b144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md) · 呼出先 5件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`0054a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a074.md) [`0054a1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md) [`0054a284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0050b184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b184.md) · 呼出先 5件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`0054a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a0b4.md) [`0054a1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1f8.md) [`0054a2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a2c4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00549ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md#insn-00549ed8) · [`00549ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md#insn-00549ee4) · [`00549fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md#insn-00549fa8)
- 新版 [`00549f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549e2c.md#insn-00549f18) · [`00549f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549e2c.md#insn-00549f24) · [`00549fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549e2c.md#insn-00549fe8)

~~~diff
- 00549ed8 ["INT_ADD", "register:40f0:8", ["const:549ed8:8", "const:4:8"]]
- 00549ed8 ["CALL", null, ["callee:0054a1f8:8"]]
+ 00549f18 ["INT_ADD", "register:40f0:8", ["const:549f18:8", "const:4:8"]]
+ 00549f18 ["CALL", null, ["callee:0054a1f8:8"]]
- 00549ed8 bytes b8000094
+ 00549f18 bytes b8000094
- 00549ee4 ["INT_ADD", "register:40f0:8", ["const:549ee4:8", "const:4:8"]]
- 00549ee4 ["CALL", null, ["callee:0054a0b4:8"]]
+ 00549f24 ["INT_ADD", "register:40f0:8", ["const:549f24:8", "const:4:8"]]
+ 00549f24 ["CALL", null, ["callee:0054a0b4:8"]]
- 00549ee4 bytes 64000094
+ 00549f24 bytes 64000094
- 00549fa8 ["INT_ADD", "register:40f0:8", ["const:549fa8:8", "const:4:8"]]
- 00549fa8 ["CALL", null, ["callee:0053b424:8"]]
+ 00549fe8 ["INT_ADD", "register:40f0:8", ["const:549fe8:8", "const:4:8"]]
+ 00549fe8 ["CALL", null, ["callee:0053b424:8"]]
- 00549fa8 bytes 0fc5ff97
+ 00549fe8 bytes 0fc5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00e35d7db88a426567c56d68053e99b7"></a>

### [`0054a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a074.md) → [`0054a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a0b4.md) FUN_0054a0b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00549dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) · 呼出先 1件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md)
- 新版 呼出元 1件 [`00549e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549e2c.md) · 呼出先 1件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a074.md#insn-0054a140)
- 新版 [`0054a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a0b4.md#insn-0054a180)

~~~diff
- 0054a140 ["INT_ADD", "register:40f0:8", ["const:54a140:8", "const:4:8"]]
- 0054a140 ["CALL", null, ["callee:0043bba4:8"]]
+ 0054a180 ["INT_ADD", "register:40f0:8", ["const:54a180:8", "const:4:8"]]
+ 0054a180 ["CALL", null, ["callee:0043bba4:8"]]
- 0054a140 bytes 89c6fb97
+ 0054a180 bytes 89c6fb97
~~~


<a id="compare-1a7c8b2339560247a59dd06808553e9e"></a>

### [`0054a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a160.md) → [`0054a1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1a0.md) FUN_0054a1a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a160.md#insn-0054a178)
- 新版 [`0054a1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1a0.md#insn-0054a1b8)

~~~diff
- 0054a178 ["INT_ADD", "register:40f0:8", ["const:54a178:8", "const:4:8"]]
- 0054a178 ["CALL", null, ["callee:0053b424:8"]]
+ 0054a1b8 ["INT_ADD", "register:40f0:8", ["const:54a1b8:8", "const:4:8"]]
+ 0054a1b8 ["CALL", null, ["callee:0053b424:8"]]
- 0054a178 bytes 9bc4ff97
+ 0054a1b8 bytes 9bc4ff97
~~~


<a id="compare-5c570449bab65156cfb6153860ef1eec"></a>

### [`0054a1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md) → [`0054a1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1f8.md) FUN_0054a1f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00549dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) · 呼出先 5件 [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00549e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549e2c.md) · 呼出先 5件 [`0053c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c178.md) [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md#insn-0054a1f4) · [`0054a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md#insn-0054a210) · [`0054a228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md#insn-0054a228)
- 新版 [`0054a234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1f8.md#insn-0054a234) · [`0054a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1f8.md#insn-0054a250) · [`0054a268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1f8.md#insn-0054a268)

~~~diff
- 0054a1f4 ["INT_ADD", "register:40f0:8", ["const:54a1f4:8", "const:4:8"]]
- 0054a1f4 ["CALL", null, ["callee:0053c178:8"]]
+ 0054a234 ["INT_ADD", "register:40f0:8", ["const:54a234:8", "const:4:8"]]
+ 0054a234 ["CALL", null, ["callee:0053c178:8"]]
- 0054a1f4 bytes d1c7ff97
+ 0054a234 bytes d1c7ff97
- 0054a210 ["INT_ADD", "register:40f0:8", ["const:54a210:8", "const:4:8"]]
- 0054a210 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0054a250 ["INT_ADD", "register:40f0:8", ["const:54a250:8", "const:4:8"]]
+ 0054a250 ["CALL", null, ["callee:00c53cd0:8"]]
- 0054a210 bytes a8251c94
+ 0054a250 bytes a0261c94
- 0054a228 ["INT_ADD", "register:40f0:8", ["const:54a228:8", "const:4:8"]]
- 0054a228 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054a268 ["INT_ADD", "register:40f0:8", ["const:54a268:8", "const:4:8"]]
+ 0054a268 ["CALL", null, ["callee:00c53d00:8"]]
- 0054a228 bytes ae251c94
+ 0054a268 bytes a6261c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f7b40c32e3d3a49335b12cfae3031e3"></a>

### [`0054a284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md) → [`0054a2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a2c4.md) FUN_0054a2c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00549dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00517448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00549e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549e2c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00517488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md#insn-0054a2b8) · [`0054a2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md#insn-0054a2d0) · [`0054a384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md#insn-0054a384)
- 新版 [`0054a2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a2c4.md#insn-0054a2f8) · [`0054a310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a2c4.md#insn-0054a310) · [`0054a3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a2c4.md#insn-0054a3c4)

~~~diff
- 0054a2b8 ["INT_ADD", "register:40f0:8", ["const:54a2b8:8", "const:4:8"]]
- 0054a2b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054a2f8 ["INT_ADD", "register:40f0:8", ["const:54a2f8:8", "const:4:8"]]
+ 0054a2f8 ["CALL", null, ["callee:00c57e90:8"]]
- 0054a2b8 bytes f6351c94
+ 0054a2f8 bytes e6361c94
- 0054a2d0 ["INT_ADD", "register:40f0:8", ["const:54a2d0:8", "const:4:8"]]
- 0054a2d0 ["CALL", null, ["callee:00517488:8"]]
+ 0054a310 ["INT_ADD", "register:40f0:8", ["const:54a310:8", "const:4:8"]]
+ 0054a310 ["CALL", null, ["callee:00517488:8"]]
- 0054a2d0 bytes 5e34ff97
+ 0054a310 bytes 5e34ff97
- 0054a384 ["INT_ADD", "register:40f0:8", ["const:54a384:8", "const:4:8"]]
- 0054a384 ["CALL", null, ["callee:0043bba4:8"]]
+ 0054a3c4 ["INT_ADD", "register:40f0:8", ["const:54a3c4:8", "const:4:8"]]
+ 0054a3c4 ["CALL", null, ["callee:0043bba4:8"]]
- 0054a384 bytes f8c5fb97
+ 0054a3c4 bytes f8c5fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a8f49b7b3cd900283842614e69f6718"></a>

### [`0054a3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md) → [`0054a42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a42c.md) FUN_0054a42c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`0050f02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f02c.md) [`0054a74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a74c.md) · 呼出先 4件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) [`0050f06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f06c.md) [`0054a78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a78c.md) · 呼出先 4件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md#insn-0054a408) · [`0054a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md#insn-0054a440) · [`0054a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md#insn-0054a450)
- 新版 [`0054a448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a42c.md#insn-0054a448) · [`0054a480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a42c.md#insn-0054a480) · [`0054a490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a42c.md#insn-0054a490)

~~~diff
- 0054a408 ["INT_ADD", "register:40f0:8", ["const:54a408:8", "const:4:8"]]
- 0054a408 ["CALL", null, ["callee:0053b424:8"]]
+ 0054a448 ["INT_ADD", "register:40f0:8", ["const:54a448:8", "const:4:8"]]
+ 0054a448 ["CALL", null, ["callee:0053b424:8"]]
- 0054a408 bytes f7c3ff97
+ 0054a448 bytes f7c3ff97
- 0054a440 ["INT_ADD", "register:40f0:8", ["const:54a440:8", "const:4:8"]]
- 0054a440 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054a480 ["INT_ADD", "register:40f0:8", ["const:54a480:8", "const:4:8"]]
+ 0054a480 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054a440 bytes 9c351c94
+ 0054a480 bytes 8c361c94
- 0054a450 ["INT_ADD", "register:40f0:8", ["const:54a450:8", "const:4:8"]]
- 0054a450 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054a490 ["INT_ADD", "register:40f0:8", ["const:54a490:8", "const:4:8"]]
+ 0054a490 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054a450 bytes 98351c94
+ 0054a490 bytes 88361c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eaeb08d89eaa49fff4da31fc953c3aa"></a>

### [`0054a4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md) → [`0054a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a4f4.md) FUN_0054a4f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`005292f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`00bc82c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) [`00529334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md) [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) [`00bc86ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc86ec.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md#insn-0054a4e8) · [`0054a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md#insn-0054a508) · [`0054a53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md#insn-0054a53c)
- 新版 [`0054a528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a4f4.md#insn-0054a528) · [`0054a548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a4f4.md#insn-0054a548) · [`0054a57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a4f4.md#insn-0054a57c)

~~~diff
- 0054a4e8 ["INT_ADD", "register:40f0:8", ["const:54a4e8:8", "const:4:8"]]
- 0054a4e8 ["CALL", null, ["callee:0054a614:8"]]
+ 0054a528 ["INT_ADD", "register:40f0:8", ["const:54a528:8", "const:4:8"]]
+ 0054a528 ["CALL", null, ["callee:0054a614:8"]]
- 0054a4e8 bytes 3b000094
+ 0054a528 bytes 3b000094
- 0054a508 ["INT_ADD", "register:40f0:8", ["const:54a508:8", "const:4:8"]]
- 0054a508 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054a548 ["INT_ADD", "register:40f0:8", ["const:54a548:8", "const:4:8"]]
+ 0054a548 ["CALL", null, ["callee:00c57e90:8"]]
- 0054a508 bytes 62351c94
+ 0054a548 bytes 52361c94
- 0054a53c ["INT_ADD", "register:40f0:8", ["const:54a53c:8", "const:4:8"]]
- 0054a53c ["CALL", null, ["callee:0043bb20:8"]]
+ 0054a57c ["INT_ADD", "register:40f0:8", ["const:54a57c:8", "const:4:8"]]
+ 0054a57c ["CALL", null, ["callee:0043bb20:8"]]
- 0054a53c bytes 69c5fb97
+ 0054a57c bytes 69c5fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfc0a3020606ac91a420688dc7830d77"></a>

### [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) → [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) FUN_0054a614

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`0052c958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md) [`0052d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md) [`0054a4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md) [`00b6eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eebc.md) [`00b82890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82890.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 9件 [`0052c998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md) [`0052d284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md) [`0054a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a4f4.md) [`00b6f2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f2e4.md) [`00b82cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b82cb8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md#insn-0054a658) · [`0054a684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md#insn-0054a684)
- 新版 [`0054a698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md#insn-0054a698) · [`0054a6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md#insn-0054a6c4)

~~~diff
- 0054a658 ["INT_ADD", "register:40f0:8", ["const:54a658:8", "const:4:8"]]
- 0054a658 ["CALL", null, ["callee:00c58050:8"]]
+ 0054a698 ["INT_ADD", "register:40f0:8", ["const:54a698:8", "const:4:8"]]
+ 0054a698 ["CALL", null, ["callee:00c58050:8"]]
- 0054a658 bytes 7e351c94
+ 0054a698 bytes 6e361c94
- 0054a684 ["INT_ADD", "register:40f0:8", ["const:54a684:8", "const:4:8"]]
- 0054a684 ["CALL", null, ["callee:00c58050:8"]]
+ 0054a6c4 ["INT_ADD", "register:40f0:8", ["const:54a6c4:8", "const:4:8"]]
+ 0054a6c4 ["CALL", null, ["callee:00c58050:8"]]
- 0054a684 bytes 73351c94
+ 0054a6c4 bytes 63361c94
~~~


<a id="compare-429103b9f73f9cf778723fc5b2b8aba1"></a>

### [`0054a6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a6d8.md) → [`0054a718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a718.md) FUN_0054a718

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a6d8.md#insn-0054a710)
- 新版 [`0054a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a718.md#insn-0054a750)

~~~diff
- 0054a710 ["INT_ADD", "register:40f0:8", ["const:54a710:8", "const:4:8"]]
- 0054a710 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054a750 ["INT_ADD", "register:40f0:8", ["const:54a750:8", "const:4:8"]]
+ 0054a750 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054a710 bytes e8341c94
+ 0054a750 bytes d8351c94
~~~


<a id="compare-b2d439153a8f871db6b5dcf8a349dce9"></a>

### [`0054a728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a728.md) → [`0054a768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a768.md) FUN_0054a768

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a728.md#insn-0054a738)
- 新版 [`0054a778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a768.md#insn-0054a778)

~~~diff
- 0054a738 ["INT_ADD", "register:40f0:8", ["const:54a738:8", "const:4:8"]]
- 0054a738 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0054a778 ["INT_ADD", "register:40f0:8", ["const:54a778:8", "const:4:8"]]
+ 0054a778 ["CALL", null, ["callee:00c57ea0:8"]]
- 0054a738 bytes da341c94
+ 0054a778 bytes ca351c94
~~~


<a id="compare-cc2f7676ae348d78dff528923c1f18bc"></a>

### [`0054a74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a74c.md) → [`0054a78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a78c.md) FUN_0054a78c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054a3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054a42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a42c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a74c.md#insn-0054a764)
- 新版 [`0054a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a78c.md#insn-0054a7a4)

~~~diff
- 0054a764 ["INT_ADD", "register:40f0:8", ["const:54a764:8", "const:4:8"]]
- 0054a764 ["CALL", null, ["callee:0054a42c:8"]]
+ 0054a7a4 ["INT_ADD", "register:40f0:8", ["const:54a7a4:8", "const:4:8"]]
+ 0054a7a4 ["CALL", null, ["callee:0054a42c:8"]]
- 0054a764 bytes 22ffff97
+ 0054a7a4 bytes 22ffff97
~~~


<a id="compare-775864502e639046ad9f335c8f856976"></a>

### [`0054a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a7a4.md) → [`0054a7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a7e4.md) FUN_0054a7e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0050fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a7a4.md#insn-0054a7d8) · [`0054a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a7a4.md#insn-0054a7f8) · [`0054a82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a7a4.md#insn-0054a82c)
- 新版 [`0054a818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a7e4.md#insn-0054a818) · [`0054a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a7e4.md#insn-0054a838) · [`0054a86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a7e4.md#insn-0054a86c)

~~~diff
- 0054a7d8 ["INT_ADD", "register:40f0:8", ["const:54a7d8:8", "const:4:8"]]
- 0054a7d8 ["CALL", null, ["callee:0046d5a8:8"]]
+ 0054a818 ["INT_ADD", "register:40f0:8", ["const:54a818:8", "const:4:8"]]
+ 0054a818 ["CALL", null, ["callee:0046d5a8:8"]]
- 0054a7d8 bytes 648bfc97
+ 0054a818 bytes 648bfc97
- 0054a7f8 ["INT_ADD", "register:40f0:8", ["const:54a7f8:8", "const:4:8"]]
- 0054a7f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054a838 ["INT_ADD", "register:40f0:8", ["const:54a838:8", "const:4:8"]]
+ 0054a838 ["CALL", null, ["callee:00c57e90:8"]]
- 0054a7f8 bytes a6341c94
+ 0054a838 bytes 96351c94
- 0054a82c ["INT_ADD", "register:40f0:8", ["const:54a82c:8", "const:4:8"]]
- 0054a82c ["CALL", null, ["callee:0043bb20:8"]]
+ 0054a86c ["INT_ADD", "register:40f0:8", ["const:54a86c:8", "const:4:8"]]
+ 0054a86c ["CALL", null, ["callee:0043bb20:8"]]
- 0054a82c bytes adc4fb97
+ 0054a86c bytes adc4fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f186576440359e9e202a667238f7f6"></a>

### [`0054a8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a8dc.md) → [`0054a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a91c.md) FUN_0054a91c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00511e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511e1c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00511e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511e5c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a8dc.md#insn-0054a94c) · [`0054a960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a8dc.md#insn-0054a960) · [`0054a968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a8dc.md#insn-0054a968)
- 新版 [`0054a98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a91c.md#insn-0054a98c) · [`0054a9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a91c.md#insn-0054a9a0) · [`0054a9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a91c.md#insn-0054a9a8)

~~~diff
- 0054a94c ["INT_ADD", "register:40f0:8", ["const:54a94c:8", "const:4:8"]]
- 0054a94c ["CALL", null, ["callee:00c53d00:8"]]
+ 0054a98c ["INT_ADD", "register:40f0:8", ["const:54a98c:8", "const:4:8"]]
+ 0054a98c ["CALL", null, ["callee:00c53d00:8"]]
- 0054a94c bytes e5231c94
+ 0054a98c bytes dd241c94
- 0054a960 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054a960 ["INT_ADD", "register:40f0:8", ["const:54a960:8", "const:4:8"]]
- 0054a960 ["CALLIND", null, ["register:0:8"]]
+ 0054a9a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054a9a0 ["INT_ADD", "register:40f0:8", ["const:54a9a0:8", "const:4:8"]]
+ 0054a9a0 ["CALLIND", null, ["register:0:8"]]
- 0054a960 bytes 00013fd6
+ 0054a9a0 bytes 00013fd6
- 0054a968 ["INT_ADD", "register:40f0:8", ["const:54a968:8", "const:4:8"]]
- 0054a968 ["CALL", null, ["callee:00c57e80:8"]]
+ 0054a9a8 ["INT_ADD", "register:40f0:8", ["const:54a9a8:8", "const:4:8"]]
+ 0054a9a8 ["CALL", null, ["callee:00c57e80:8"]]
- 0054a968 bytes 46341c94
+ 0054a9a8 bytes 36351c94
~~~


<a id="compare-f3dd6adfa5f1355a20e0247bcbaedbfb"></a>

### [`0054a990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a990.md) → [`0054a9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a9d0.md) FUN_0054a9d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a990.md#insn-0054a9a0)
- 新版 [`0054a9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a9d0.md#insn-0054a9e0)

~~~diff
- 0054a9a0 ["INT_ADD", "register:40f0:8", ["const:54a9a0:8", "const:4:8"]]
- 0054a9a0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0054a9e0 ["INT_ADD", "register:40f0:8", ["const:54a9e0:8", "const:4:8"]]
+ 0054a9e0 ["CALL", null, ["callee:00c57ea0:8"]]
- 0054a9a0 bytes 40341c94
+ 0054a9e0 bytes 30351c94
~~~


<a id="compare-0cb60c5ecefbff8d7fb42b2e73c2b30f"></a>

### [`0054a9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a9b4.md) → [`0054a9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a9f4.md) FUN_0054a9f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054aa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054aa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aa4c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054a9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a9b4.md#insn-0054a9cc)
- 新版 [`0054aa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a9f4.md#insn-0054aa0c)

~~~diff
- 0054a9cc ["INT_ADD", "register:40f0:8", ["const:54a9cc:8", "const:4:8"]]
- 0054a9cc ["CALL", null, ["callee:0054aa4c:8"]]
+ 0054aa0c ["INT_ADD", "register:40f0:8", ["const:54aa0c:8", "const:4:8"]]
+ 0054aa0c ["CALL", null, ["callee:0054aa4c:8"]]
- 0054a9cc bytes 10000094
+ 0054aa0c bytes 10000094
~~~


<a id="compare-c65115c2f2500dbe642f5656e8c4af39"></a>

### [`0054aa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md) → [`0054aa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aa4c.md) FUN_0054aa4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) [`00513dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513dd4.md) [`0054a9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a9b4.md) · 呼出先 5件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005132b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md) [`00513e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e14.md) [`0054a9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a9f4.md) · 呼出先 5件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054aa2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md#insn-0054aa2c) · [`0054aa3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md#insn-0054aa3c) · [`0054aa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md#insn-0054aa48)
- 新版 [`0054aa6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aa4c.md#insn-0054aa6c) · [`0054aa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aa4c.md#insn-0054aa7c) · [`0054aa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aa4c.md#insn-0054aa88)

~~~diff
- 0054aa2c ["INT_ADD", "register:40f0:8", ["const:54aa2c:8", "const:4:8"]]
- 0054aa2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054aa6c ["INT_ADD", "register:40f0:8", ["const:54aa6c:8", "const:4:8"]]
+ 0054aa6c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054aa2c bytes 21341c94
+ 0054aa6c bytes 11351c94
- 0054aa3c ["INT_ADD", "register:40f0:8", ["const:54aa3c:8", "const:4:8"]]
- 0054aa3c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054aa7c ["INT_ADD", "register:40f0:8", ["const:54aa7c:8", "const:4:8"]]
+ 0054aa7c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054aa3c bytes 1d341c94
+ 0054aa7c bytes 0d351c94
- 0054aa48 ["INT_ADD", "register:40f0:8", ["const:54aa48:8", "const:4:8"]]
- 0054aa48 ["CALL", null, ["callee:0053b424:8"]]
+ 0054aa88 ["INT_ADD", "register:40f0:8", ["const:54aa88:8", "const:4:8"]]
+ 0054aa88 ["CALL", null, ["callee:0053b424:8"]]
- 0054aa48 bytes 67c2ff97
+ 0054aa88 bytes 67c2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b9f06a4ecf14888936c5ee465a58cb"></a>

### [`0054b868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b868.md) → [`0054b8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8a8.md) FUN_0054b8a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054b790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054b7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b7d0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b868.md#insn-0054b894)
- 新版 [`0054b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8a8.md#insn-0054b8d4)

~~~diff
- 0054b894 ["INT_ADD", "register:40f0:8", ["const:54b894:8", "const:4:8"]]
- 0054b894 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054b8d4 ["INT_ADD", "register:40f0:8", ["const:54b8d4:8", "const:4:8"]]
+ 0054b8d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054b894 bytes 87301c94
+ 0054b8d4 bytes 77311c94
~~~


<a id="compare-ed8214e699a1678bc7ddc92ae6880ad8"></a>

### [`0054b8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md) → [`0054b8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8f4.md) FUN_0054b8f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00515590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515590.md) [`0054b8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md) · 呼出先 2件 [`0054b8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005155d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005155d0.md) [`0054b8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8f4.md) · 呼出先 2件 [`0054b8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054b8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md#insn-0054b8d0) · [`0054b8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md#insn-0054b8dc) · [`0054b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md#insn-0054b8ec)
- 新版 [`0054b910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8f4.md#insn-0054b910) · [`0054b91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8f4.md#insn-0054b91c) · [`0054b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8f4.md#insn-0054b92c)

~~~diff
- 0054b8d0 ["INT_ADD", "register:40f0:8", ["const:54b8d0:8", "const:4:8"]]
- 0054b8d0 ["CALL", null, ["local:b0:8"]]
+ 0054b910 ["INT_ADD", "register:40f0:8", ["const:54b910:8", "const:4:8"]]
+ 0054b910 ["CALL", null, ["local:b0:8"]]
- 0054b8d0 bytes f9ffff97
+ 0054b910 bytes f9ffff97
- 0054b8dc ["INT_ADD", "register:40f0:8", ["const:54b8dc:8", "const:4:8"]]
- 0054b8dc ["CALL", null, ["local:b0:8"]]
+ 0054b91c ["INT_ADD", "register:40f0:8", ["const:54b91c:8", "const:4:8"]]
+ 0054b91c ["CALL", null, ["local:b0:8"]]
- 0054b8dc bytes f6ffff97
+ 0054b91c bytes f6ffff97
- 0054b8ec ["INT_ADD", "register:40f0:8", ["const:54b8ec:8", "const:4:8"]]
- 0054b8ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054b92c ["INT_ADD", "register:40f0:8", ["const:54b92c:8", "const:4:8"]]
+ 0054b92c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054b8ec bytes 71301c94
+ 0054b92c bytes 61311c94
~~~


<a id="compare-87e33a35c3adfdeebc148a7c2e9bdc0f"></a>

### [`0054bb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md) → [`0054bb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bb8c.md) FUN_0054bb8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054bb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md#insn-0054bb70)
- 新版 [`0054bbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bb8c.md#insn-0054bbb0)

~~~diff
- 0054bb70 ["INT_ADD", "register:40f0:8", ["const:54bb70:8", "const:4:8"]]
- 0054bb70 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054bbb0 ["INT_ADD", "register:40f0:8", ["const:54bbb0:8", "const:4:8"]]
+ 0054bbb0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054bb70 bytes d02f1c94
+ 0054bbb0 bytes c0301c94
~~~


<a id="compare-28ef8323f08f21f3f61a1cd817bce9ba"></a>

### [`0054bbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md) → [`0054bbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bbfc.md) FUN_0054bbfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00503084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054bd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bd88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`005030c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md) [`005113cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054bdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bdc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054bccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md#insn-0054bccc) · [`0054bce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md#insn-0054bce8) · [`0054bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md#insn-0054bd14)
- 新版 [`0054bd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bbfc.md#insn-0054bd0c) · [`0054bd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bbfc.md#insn-0054bd28) · [`0054bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bbfc.md#insn-0054bd54)

~~~diff
- 0054bccc ["INT_ADD", "register:40f0:8", ["const:54bccc:8", "const:4:8"]]
- 0054bccc ["CALL", null, ["callee:00c57e90:8"]]
+ 0054bd0c ["INT_ADD", "register:40f0:8", ["const:54bd0c:8", "const:4:8"]]
+ 0054bd0c ["CALL", null, ["callee:00c57e90:8"]]
- 0054bccc bytes 712f1c94
+ 0054bd0c bytes 61301c94
- 0054bce8 ["INT_ADD", "register:40f0:8", ["const:54bce8:8", "const:4:8"]]
- 0054bce8 ["CALL", null, ["callee:0054bdc8:8"]]
+ 0054bd28 ["INT_ADD", "register:40f0:8", ["const:54bd28:8", "const:4:8"]]
+ 0054bd28 ["CALL", null, ["callee:0054bdc8:8"]]
- 0054bce8 bytes 28000094
+ 0054bd28 bytes 28000094
- 0054bd14 ["INT_ADD", "register:40f0:8", ["const:54bd14:8", "const:4:8"]]
- 0054bd14 ["CALL", null, ["callee:0043bba4:8"]]
+ 0054bd54 ["INT_ADD", "register:40f0:8", ["const:54bd54:8", "const:4:8"]]
+ 0054bd54 ["CALL", null, ["callee:0043bba4:8"]]
- 0054bd14 bytes 94bffb97
+ 0054bd54 bytes 94bffb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d077f88657e0d7ae7b6516264d1b37"></a>

### [`0054bed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bed4.md) → [`0054bf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bf14.md) FUN_0054bf14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) · 呼出先 1件 [`0054bfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bfd4.md)
- 新版 呼出元 1件 [`005113cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md) · 呼出先 1件 [`0054c014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c014.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054bfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bed4.md#insn-0054bfc4)
- 新版 [`0054c004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bf14.md#insn-0054c004)

~~~diff
- 0054bfc4 ["INT_ADD", "register:40f0:8", ["const:54bfc4:8", "const:4:8"]]
- 0054bfc4 ["CALL", null, ["callee:0054c014:8"]]
+ 0054c004 ["INT_ADD", "register:40f0:8", ["const:54c004:8", "const:4:8"]]
+ 0054c004 ["CALL", null, ["callee:0054c014:8"]]
- 0054bfc4 bytes 04000094
+ 0054c004 bytes 04000094
~~~


<a id="compare-051ad9ca7a8a2ac774203ac17c2511ae"></a>

### [`0054bfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bfd4.md) → [`0054c014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c014.md) FUN_0054c014

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054bed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bed4.md) · 呼出先 4件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054bf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bf14.md) · 呼出先 4件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bfd4.md#insn-0054c03c) · [`0054c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bfd4.md#insn-0054c04c) · [`0054c060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bfd4.md#insn-0054c060)
- 新版 [`0054c07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c014.md#insn-0054c07c) · [`0054c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c014.md#insn-0054c08c) · [`0054c0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c014.md#insn-0054c0a0)

~~~diff
- 0054c03c ["INT_ADD", "register:40f0:8", ["const:54c03c:8", "const:4:8"]]
- 0054c03c ["CALL", null, ["callee:00494610:8"]]
+ 0054c07c ["INT_ADD", "register:40f0:8", ["const:54c07c:8", "const:4:8"]]
+ 0054c07c ["CALL", null, ["callee:00494610:8"]]
- 0054c03c bytes 6521fd97
+ 0054c07c bytes 6521fd97
- 0054c04c ["INT_ADD", "register:40f0:8", ["const:54c04c:8", "const:4:8"]]
- 0054c04c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054c08c ["INT_ADD", "register:40f0:8", ["const:54c08c:8", "const:4:8"]]
+ 0054c08c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054c04c bytes 992e1c94
+ 0054c08c bytes 892f1c94
- 0054c060 ["INT_ADD", "register:40f0:8", ["const:54c060:8", "const:4:8"]]
- 0054c060 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054c0a0 ["INT_ADD", "register:40f0:8", ["const:54c0a0:8", "const:4:8"]]
+ 0054c0a0 ["CALL", null, ["callee:00c53d00:8"]]
- 0054c060 bytes 201e1c94
+ 0054c0a0 bytes 181f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca14b2b796282812d80340e0d5accda6"></a>

### [`0054c0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md) → [`0054c0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c0ec.md) FUN_0054c0ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00516ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ec8.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054c1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1e4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00516f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516f08.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0054c224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c224.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md#insn-0054c114) · [`0054c1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md#insn-0054c1a0) · [`0054c1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md#insn-0054c1bc)
- 新版 [`0054c154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c0ec.md#insn-0054c154) · [`0054c1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c0ec.md#insn-0054c1e0) · [`0054c1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c0ec.md#insn-0054c1fc)

~~~diff
- 0054c114 ["INT_ADD", "register:40f0:8", ["const:54c114:8", "const:4:8"]]
- 0054c114 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054c154 ["INT_ADD", "register:40f0:8", ["const:54c154:8", "const:4:8"]]
+ 0054c154 ["CALL", null, ["callee:00c57e90:8"]]
- 0054c114 bytes 5f2e1c94
+ 0054c154 bytes 4f2f1c94
- 0054c1a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054c1a0 ["INT_ADD", "register:40f0:8", ["const:54c1a0:8", "const:4:8"]]
- 0054c1a0 ["CALLIND", null, ["register:0:8"]]
+ 0054c1e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054c1e0 ["INT_ADD", "register:40f0:8", ["const:54c1e0:8", "const:4:8"]]
+ 0054c1e0 ["CALLIND", null, ["register:0:8"]]
- 0054c1a0 bytes 00013fd6
+ 0054c1e0 bytes 00013fd6
- 0054c1bc ["INT_ADD", "register:40f0:8", ["const:54c1bc:8", "const:4:8"]]
- 0054c1bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054c1fc ["INT_ADD", "register:40f0:8", ["const:54c1fc:8", "const:4:8"]]
+ 0054c1fc ["CALL", null, ["callee:00c57eb0:8"]]
- 0054c1bc bytes 3d2e1c94
+ 0054c1fc bytes 2d2f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f66c8a53e21fb4ef389ac5e3c9c0a2"></a>

### [`0054c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md) → [`0054c238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c238.md) FUN_0054c238

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md) · 呼出先 2件 [`0054c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054c238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c238.md) · 呼出先 2件 [`0054c238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c238.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md#insn-0054c214) · [`0054c220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md#insn-0054c220) · [`0054c230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md#insn-0054c230)
- 新版 [`0054c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c238.md#insn-0054c254) · [`0054c260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c238.md#insn-0054c260) · [`0054c270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c238.md#insn-0054c270)

~~~diff
- 0054c214 ["INT_ADD", "register:40f0:8", ["const:54c214:8", "const:4:8"]]
- 0054c214 ["CALL", null, ["local:b0:8"]]
+ 0054c254 ["INT_ADD", "register:40f0:8", ["const:54c254:8", "const:4:8"]]
+ 0054c254 ["CALL", null, ["local:b0:8"]]
- 0054c214 bytes f9ffff97
+ 0054c254 bytes f9ffff97
- 0054c220 ["INT_ADD", "register:40f0:8", ["const:54c220:8", "const:4:8"]]
- 0054c220 ["CALL", null, ["local:b0:8"]]
+ 0054c260 ["INT_ADD", "register:40f0:8", ["const:54c260:8", "const:4:8"]]
+ 0054c260 ["CALL", null, ["local:b0:8"]]
- 0054c220 bytes f6ffff97
+ 0054c260 bytes f6ffff97
- 0054c230 ["INT_ADD", "register:40f0:8", ["const:54c230:8", "const:4:8"]]
- 0054c230 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054c270 ["INT_ADD", "register:40f0:8", ["const:54c270:8", "const:4:8"]]
+ 0054c270 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054c230 bytes 202e1c94
+ 0054c270 bytes 102f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-876a9e16cd23ec51293efc45472f5dbb"></a>

### [`0054c258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c258.md) → [`0054c298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c298.md) FUN_0054c298

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005170d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054c3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c3d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00517110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517110.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054c414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c414.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c258.md#insn-0054c35c) · [`0054c388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c258.md#insn-0054c388) · [`0054c3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c258.md#insn-0054c3d0)
- 新版 [`0054c39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c298.md#insn-0054c39c) · [`0054c3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c298.md#insn-0054c3c8) · [`0054c410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c298.md#insn-0054c410)

~~~diff
- 0054c35c ["INT_ADD", "register:40f0:8", ["const:54c35c:8", "const:4:8"]]
- 0054c35c ["CALL", null, ["callee:0054c414:8"]]
+ 0054c39c ["INT_ADD", "register:40f0:8", ["const:54c39c:8", "const:4:8"]]
+ 0054c39c ["CALL", null, ["callee:0054c414:8"]]
- 0054c35c bytes 1e000094
+ 0054c39c bytes 1e000094
- 0054c388 ["INT_ADD", "register:40f0:8", ["const:54c388:8", "const:4:8"]]
- 0054c388 ["CALL", null, ["callee:0043bba4:8"]]
+ 0054c3c8 ["INT_ADD", "register:40f0:8", ["const:54c3c8:8", "const:4:8"]]
+ 0054c3c8 ["CALL", null, ["callee:0043bba4:8"]]
- 0054c388 bytes f7bdfb97
+ 0054c3c8 bytes f7bdfb97
- 0054c3d0 ["INT_ADD", "register:40f0:8", ["const:54c3d0:8", "const:4:8"]]
- 0054c3d0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0054c410 ["INT_ADD", "register:40f0:8", ["const:54c410:8", "const:4:8"]]
+ 0054c410 ["CALL", null, ["callee:00c57ee0:8"]]
- 0054c3d0 bytes c42d1c94
+ 0054c410 bytes b42e1c94
~~~


<a id="compare-e3bc91f2c62518d22f97eabc03951612"></a>

### [`0054c4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c4c8.md) → [`0054c508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c508.md) FUN_0054c508

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054c3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c3d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054c414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c414.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c4c8.md#insn-0054c4f4) · [`0054c504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c4c8.md#insn-0054c504)
- 新版 [`0054c534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c508.md#insn-0054c534) · [`0054c544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c508.md#insn-0054c544)

~~~diff
- 0054c4f4 ["INT_ADD", "register:40f0:8", ["const:54c4f4:8", "const:4:8"]]
- 0054c4f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054c534 ["INT_ADD", "register:40f0:8", ["const:54c534:8", "const:4:8"]]
+ 0054c534 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054c4f4 bytes 6f2d1c94
+ 0054c534 bytes 5f2e1c94
- 0054c504 ["INT_ADD", "register:40f0:8", ["const:54c504:8", "const:4:8"]]
- 0054c504 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054c544 ["INT_ADD", "register:40f0:8", ["const:54c544:8", "const:4:8"]]
+ 0054c544 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054c504 bytes 6b2d1c94
+ 0054c544 bytes 5b2e1c94
~~~


<a id="compare-0092ea320d455b0a0f02b12ffe348435"></a>

### [`0054c524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md) → [`0054c564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c564.md) FUN_0054c564

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00517610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054c6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c6f0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054c730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c730.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054c634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md#insn-0054c634) · [`0054c650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md#insn-0054c650) · [`0054c67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md#insn-0054c67c)
- 新版 [`0054c674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c564.md#insn-0054c674) · [`0054c690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c564.md#insn-0054c690) · [`0054c6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c564.md#insn-0054c6bc)

~~~diff
- 0054c634 ["INT_ADD", "register:40f0:8", ["const:54c634:8", "const:4:8"]]
- 0054c634 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054c674 ["INT_ADD", "register:40f0:8", ["const:54c674:8", "const:4:8"]]
+ 0054c674 ["CALL", null, ["callee:00c57e90:8"]]
- 0054c634 bytes 172d1c94
+ 0054c674 bytes 072e1c94
- 0054c650 ["INT_ADD", "register:40f0:8", ["const:54c650:8", "const:4:8"]]
- 0054c650 ["CALL", null, ["callee:0054c730:8"]]
+ 0054c690 ["INT_ADD", "register:40f0:8", ["const:54c690:8", "const:4:8"]]
+ 0054c690 ["CALL", null, ["callee:0054c730:8"]]
- 0054c650 bytes 28000094
+ 0054c690 bytes 28000094
- 0054c67c ["INT_ADD", "register:40f0:8", ["const:54c67c:8", "const:4:8"]]
- 0054c67c ["CALL", null, ["callee:0043bba4:8"]]
+ 0054c6bc ["INT_ADD", "register:40f0:8", ["const:54c6bc:8", "const:4:8"]]
+ 0054c6bc ["CALL", null, ["callee:0043bba4:8"]]
- 0054c67c bytes 3abdfb97
+ 0054c6bc bytes 3abdfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6619403c2d8f37a88a6459a64dbba0a3"></a>

### [`0054cae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cae0.md) → [`0054cb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb20.md) FUN_0054cb20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cae0.md#insn-0054cb1c) · [`0054cb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cae0.md#insn-0054cb2c)
- 新版 [`0054cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb20.md#insn-0054cb5c) · [`0054cb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb20.md#insn-0054cb6c)

~~~diff
- 0054cb1c ["INT_ADD", "register:40f0:8", ["const:54cb1c:8", "const:4:8"]]
- 0054cb1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054cb5c ["INT_ADD", "register:40f0:8", ["const:54cb5c:8", "const:4:8"]]
+ 0054cb5c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054cb1c bytes e52b1c94
+ 0054cb5c bytes d52c1c94
- 0054cb2c ["INT_ADD", "register:40f0:8", ["const:54cb2c:8", "const:4:8"]]
- 0054cb2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054cb6c ["INT_ADD", "register:40f0:8", ["const:54cb6c:8", "const:4:8"]]
+ 0054cb6c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054cb2c bytes e12b1c94
+ 0054cb6c bytes d12c1c94
~~~


<a id="compare-4f11df251de58eb447cba9c6bece0a41"></a>

### [`0054cb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb70.md) → [`0054cbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cbb0.md) FUN_0054cbb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054cb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb70.md#insn-0054cb94)
- 新版 [`0054cbd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cbb0.md#insn-0054cbd4)

~~~diff
- 0054cb94 ["INT_ADD", "register:40f0:8", ["const:54cb94:8", "const:4:8"]]
- 0054cb94 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054cbd4 ["INT_ADD", "register:40f0:8", ["const:54cbd4:8", "const:4:8"]]
+ 0054cbd4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054cb94 bytes c72b1c94
+ 0054cbd4 bytes b72c1c94
~~~


<a id="compare-6f85a51d3b93c491586637434dfcd10c"></a>

### [`0054d060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d060.md) → [`0054d0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0a0.md) FUN_0054d0a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054cf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cf90.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cfd0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054d08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d060.md#insn-0054d08c)
- 新版 [`0054d0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0a0.md#insn-0054d0cc)

~~~diff
- 0054d08c ["INT_ADD", "register:40f0:8", ["const:54d08c:8", "const:4:8"]]
- 0054d08c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054d0cc ["INT_ADD", "register:40f0:8", ["const:54d0cc:8", "const:4:8"]]
+ 0054d0cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0054d08c bytes 892a1c94
+ 0054d0cc bytes 792b1c94
~~~


<a id="compare-0881f6d68f8d3614aa6e3a9bf78f0636"></a>

### [`0054d0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md) → [`0054d0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md) FUN_0054d0ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) [`0054d0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md) · 呼出先 2件 [`0054d0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0051c80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md) [`0054d0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md) · 呼出先 2件 [`0054d0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054d0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md#insn-0054d0c8) · [`0054d0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md#insn-0054d0d4) · [`0054d0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md#insn-0054d0e4)
- 新版 [`0054d108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md#insn-0054d108) · [`0054d114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md#insn-0054d114) · [`0054d124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md#insn-0054d124)

~~~diff
- 0054d0c8 ["INT_ADD", "register:40f0:8", ["const:54d0c8:8", "const:4:8"]]
- 0054d0c8 ["CALL", null, ["local:b0:8"]]
+ 0054d108 ["INT_ADD", "register:40f0:8", ["const:54d108:8", "const:4:8"]]
+ 0054d108 ["CALL", null, ["local:b0:8"]]
- 0054d0c8 bytes f9ffff97
+ 0054d108 bytes f9ffff97
- 0054d0d4 ["INT_ADD", "register:40f0:8", ["const:54d0d4:8", "const:4:8"]]
- 0054d0d4 ["CALL", null, ["local:b0:8"]]
+ 0054d114 ["INT_ADD", "register:40f0:8", ["const:54d114:8", "const:4:8"]]
+ 0054d114 ["CALL", null, ["local:b0:8"]]
- 0054d0d4 bytes f6ffff97
+ 0054d114 bytes f6ffff97
- 0054d0e4 ["INT_ADD", "register:40f0:8", ["const:54d0e4:8", "const:4:8"]]
- 0054d0e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054d124 ["INT_ADD", "register:40f0:8", ["const:54d124:8", "const:4:8"]]
+ 0054d124 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054d0e4 bytes 732a1c94
+ 0054d124 bytes 632b1c94
~~~


<a id="compare-cf12cecc452238250922db66f82ffc69"></a>

### [`0054d3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d3f0.md) → [`0054d430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d430.md) FUN_0054d430

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054d420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d3f0.md#insn-0054d420) · [`0054d42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d3f0.md#insn-0054d42c)
- 新版 [`0054d460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d430.md#insn-0054d460) · [`0054d46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d430.md#insn-0054d46c)

~~~diff
- 0054d420 ["INT_ADD", "register:40f0:8", ["const:54d420:8", "const:4:8"]]
- 0054d420 ["CALL", null, ["callee:0053af90:8"]]
+ 0054d460 ["INT_ADD", "register:40f0:8", ["const:54d460:8", "const:4:8"]]
+ 0054d460 ["CALL", null, ["callee:0053af90:8"]]
- 0054d420 bytes ccb6ff97
+ 0054d460 bytes ccb6ff97
- 0054d42c ["INT_ADD", "register:40f0:8", ["const:54d42c:8", "const:4:8"]]
- 0054d42c ["CALL", null, ["callee:0046d490:8"]]
+ 0054d46c ["INT_ADD", "register:40f0:8", ["const:54d46c:8", "const:4:8"]]
+ 0054d46c ["CALL", null, ["callee:0046d490:8"]]
- 0054d42c bytes 0980fc97
+ 0054d46c bytes 0980fc97
~~~


<a id="compare-f9a78aa1ca0721875c04797e99c1411e"></a>

### [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) → [`0054d4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md) FUN_0054d4a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`005227e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005227e8.md) [`0054d7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d7ac.md) · 呼出先 5件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) [`00522828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522828.md) [`0054d7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d7ec.md) · 呼出先 5件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0051acc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md#insn-0054d480) · [`0054d48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md#insn-0054d48c) · [`0054d494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md#insn-0054d494)
- 新版 [`0054d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md#insn-0054d4c0) · [`0054d4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md#insn-0054d4cc) · [`0054d4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md#insn-0054d4d4)

~~~diff
- 0054d480 ["INT_ADD", "register:40f0:8", ["const:54d480:8", "const:4:8"]]
- 0054d480 ["CALL", null, ["callee:0046d490:8"]]
+ 0054d4c0 ["INT_ADD", "register:40f0:8", ["const:54d4c0:8", "const:4:8"]]
+ 0054d4c0 ["CALL", null, ["callee:0046d490:8"]]
- 0054d480 bytes f47ffc97
+ 0054d4c0 bytes f47ffc97
- 0054d48c ["INT_ADD", "register:40f0:8", ["const:54d48c:8", "const:4:8"]]
- 0054d48c ["CALL", null, ["callee:0046d490:8"]]
+ 0054d4cc ["INT_ADD", "register:40f0:8", ["const:54d4cc:8", "const:4:8"]]
+ 0054d4cc ["CALL", null, ["callee:0046d490:8"]]
- 0054d48c bytes f17ffc97
+ 0054d4cc bytes f17ffc97
- 0054d494 ["INT_ADD", "register:40f0:8", ["const:54d494:8", "const:4:8"]]
- 0054d494 ["CALL", null, ["callee:0051acc4:8"]]
+ 0054d4d4 ["INT_ADD", "register:40f0:8", ["const:54d4d4:8", "const:4:8"]]
+ 0054d4d4 ["CALL", null, ["callee:0051acc4:8"]]
- 0054d494 bytes fc35ff97
+ 0054d4d4 bytes fc35ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8802e7692371c6feb73b7ecfb01d2a67"></a>

### [`0054d788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d788.md) → [`0054d7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d7c8.md) FUN_0054d7c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054d798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d788.md#insn-0054d798)
- 新版 [`0054d7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d7c8.md#insn-0054d7d8)

~~~diff
- 0054d798 ["INT_ADD", "register:40f0:8", ["const:54d798:8", "const:4:8"]]
- 0054d798 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0054d7d8 ["INT_ADD", "register:40f0:8", ["const:54d7d8:8", "const:4:8"]]
+ 0054d7d8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0054d798 bytes c2281c94
+ 0054d7d8 bytes b2291c94
~~~


<a id="compare-abde09e9374c09c0d831286fed3c2a98"></a>

### [`0054d7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d7ac.md) → [`0054d7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d7ec.md) FUN_0054d7ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054d4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054d7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d7ac.md#insn-0054d7c4)
- 新版 [`0054d804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d7ec.md#insn-0054d804)

~~~diff
- 0054d7c4 ["INT_ADD", "register:40f0:8", ["const:54d7c4:8", "const:4:8"]]
- 0054d7c4 ["CALL", null, ["callee:0054d4a4:8"]]
+ 0054d804 ["INT_ADD", "register:40f0:8", ["const:54d804:8", "const:4:8"]]
+ 0054d804 ["CALL", null, ["callee:0054d4a4:8"]]
- 0054d7c4 bytes 28ffff97
+ 0054d804 bytes 28ffff97
~~~


<a id="compare-711b4bba859ccf961b98cadb7e5f2de2"></a>

### [`0054d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d958.md) → [`0054d998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d998.md) FUN_0054d998

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md) · 呼出先 2件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md) · 呼出先 2件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d958.md#insn-0054d9ac)
- 新版 [`0054d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d998.md#insn-0054d9ec)

~~~diff
- 0054d9ac ["INT_ADD", "register:40f0:8", ["const:54d9ac:8", "const:4:8"]]
- 0054d9ac ["CALL", null, ["callee:0053f810:8"]]
+ 0054d9ec ["INT_ADD", "register:40f0:8", ["const:54d9ec:8", "const:4:8"]]
+ 0054d9ec ["CALL", null, ["callee:0053f810:8"]]
- 0054d9ac bytes 89c7ff97
+ 0054d9ec bytes 89c7ff97
~~~


<a id="compare-7156e42fba4e24cbeb49e996c331e25b"></a>

### [`0054d9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md) → [`0054da2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054da2c.md) FUN_0054da2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054da5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md#insn-0054da5c) · [`0054da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md#insn-0054da70) · [`0054da78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9ec.md#insn-0054da78)
- 新版 [`0054da9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054da2c.md#insn-0054da9c) · [`0054dab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054da2c.md#insn-0054dab0) · [`0054dab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054da2c.md#insn-0054dab8)

~~~diff
- 0054da5c ["INT_ADD", "register:40f0:8", ["const:54da5c:8", "const:4:8"]]
- 0054da5c ["CALL", null, ["callee:00c53d00:8"]]
+ 0054da9c ["INT_ADD", "register:40f0:8", ["const:54da9c:8", "const:4:8"]]
+ 0054da9c ["CALL", null, ["callee:00c53d00:8"]]
- 0054da5c bytes a1171c94
+ 0054da9c bytes 99181c94
- 0054da70 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054da70 ["INT_ADD", "register:40f0:8", ["const:54da70:8", "const:4:8"]]
- 0054da70 ["CALLIND", null, ["register:0:8"]]
+ 0054dab0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054dab0 ["INT_ADD", "register:40f0:8", ["const:54dab0:8", "const:4:8"]]
+ 0054dab0 ["CALLIND", null, ["register:0:8"]]
- 0054da70 bytes 00013fd6
+ 0054dab0 bytes 00013fd6
- 0054da78 ["INT_ADD", "register:40f0:8", ["const:54da78:8", "const:4:8"]]
- 0054da78 ["CALL", null, ["callee:00c57e80:8"]]
+ 0054dab8 ["INT_ADD", "register:40f0:8", ["const:54dab8:8", "const:4:8"]]
+ 0054dab8 ["CALL", null, ["callee:00c57e80:8"]]
- 0054da78 bytes 02281c94
+ 0054dab8 bytes f2281c94
~~~


<a id="compare-a3c6fd8353353c40927632195129649c"></a>

### [`0054daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md) → [`0054dae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dae0.md) FUN_0054dae0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md#insn-0054db10) · [`0054db24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md#insn-0054db24) · [`0054db2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054daa0.md#insn-0054db2c)
- 新版 [`0054db50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dae0.md#insn-0054db50) · [`0054db64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dae0.md#insn-0054db64) · [`0054db6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dae0.md#insn-0054db6c)

~~~diff
- 0054db10 ["INT_ADD", "register:40f0:8", ["const:54db10:8", "const:4:8"]]
- 0054db10 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054db50 ["INT_ADD", "register:40f0:8", ["const:54db50:8", "const:4:8"]]
+ 0054db50 ["CALL", null, ["callee:00c53d00:8"]]
- 0054db10 bytes 74171c94
+ 0054db50 bytes 6c181c94
- 0054db24 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054db24 ["INT_ADD", "register:40f0:8", ["const:54db24:8", "const:4:8"]]
- 0054db24 ["CALLIND", null, ["register:0:8"]]
+ 0054db64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054db64 ["INT_ADD", "register:40f0:8", ["const:54db64:8", "const:4:8"]]
+ 0054db64 ["CALLIND", null, ["register:0:8"]]
- 0054db24 bytes 00013fd6
+ 0054db64 bytes 00013fd6
- 0054db2c ["INT_ADD", "register:40f0:8", ["const:54db2c:8", "const:4:8"]]
- 0054db2c ["CALL", null, ["callee:00c57e80:8"]]
+ 0054db6c ["INT_ADD", "register:40f0:8", ["const:54db6c:8", "const:4:8"]]
+ 0054db6c ["CALL", null, ["callee:00c57e80:8"]]
- 0054db2c bytes d5271c94
+ 0054db6c bytes c5281c94
~~~


<a id="compare-27ddd4ff5f555a53a93d9ea231858458"></a>

### [`0054db68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md) → [`0054dba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dba8.md) FUN_0054dba8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0054dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0054dc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dc50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054db78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md#insn-0054db78) · [`0054dbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md#insn-0054dbe4) · [`0054dbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md#insn-0054dbf4)
- 新版 [`0054dbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dba8.md#insn-0054dbb8) · [`0054dc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dba8.md#insn-0054dc24) · [`0054dc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dba8.md#insn-0054dc34)

~~~diff
- 0054db78 ["INT_ADD", "register:40f0:8", ["const:54db78:8", "const:4:8"]]
- 0054db78 ["CALL", null, ["callee:0054dc50:8"]]
+ 0054dbb8 ["INT_ADD", "register:40f0:8", ["const:54dbb8:8", "const:4:8"]]
+ 0054dbb8 ["CALL", null, ["callee:0054dc50:8"]]
- 0054db78 bytes 26000094
+ 0054dbb8 bytes 26000094
- 0054dbe4 ["INT_ADD", "register:40f0:8", ["const:54dbe4:8", "const:4:8"]]
- 0054dbe4 ["CALL", null, ["callee:00494610:8"]]
+ 0054dc24 ["INT_ADD", "register:40f0:8", ["const:54dc24:8", "const:4:8"]]
+ 0054dc24 ["CALL", null, ["callee:00494610:8"]]
- 0054dbe4 bytes 7b1afd97
+ 0054dc24 bytes 7b1afd97
- 0054dbf4 ["INT_ADD", "register:40f0:8", ["const:54dbf4:8", "const:4:8"]]
- 0054dbf4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054dc34 ["INT_ADD", "register:40f0:8", ["const:54dc34:8", "const:4:8"]]
+ 0054dc34 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054dbf4 bytes af271c94
+ 0054dc34 bytes 9f281c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e59343e2a14c1f1c9ce26dc8a092a515"></a>

### [`0054dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md) → [`0054dc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dc50.md) FUN_0054dc50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0054db68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db68.md) [`00b8d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d830.md) [`00bc82c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`0054dba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dba8.md) [`00b8dc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8dc58.md) [`00bc86ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc86ec.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054dc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md#insn-0054dc7c) · [`0054dcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md#insn-0054dcd8)
- 新版 [`0054dcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dc50.md#insn-0054dcbc) · [`0054dd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dc50.md#insn-0054dd18)

~~~diff
- 0054dc7c ["INT_ADD", "register:40f0:8", ["const:54dc7c:8", "const:4:8"]]
- 0054dc7c ["CALL", null, ["callee:00c58050:8"]]
+ 0054dcbc ["INT_ADD", "register:40f0:8", ["const:54dcbc:8", "const:4:8"]]
+ 0054dcbc ["CALL", null, ["callee:00c58050:8"]]
- 0054dc7c bytes f5271c94
+ 0054dcbc bytes e5281c94
- 0054dcd8 ["INT_ADD", "register:40f0:8", ["const:54dcd8:8", "const:4:8"]]
- 0054dcd8 ["CALL", null, ["callee:00c58050:8"]]
+ 0054dd18 ["INT_ADD", "register:40f0:8", ["const:54dd18:8", "const:4:8"]]
+ 0054dd18 ["CALL", null, ["callee:00c58050:8"]]
- 0054dcd8 bytes de271c94
+ 0054dd18 bytes ce281c94
~~~


<a id="compare-711457603aec44dd8d7a7691631819d3"></a>

### [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) → [`0054dd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd68.md) FUN_0054dd68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`0054dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md) [`0054e0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md) [`0054e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md)
- 新版 呼出元 1件 [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00548584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md) [`0054e004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e004.md) [`0054e13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e13c.md) [`0054e220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054ddcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md#insn-0054ddcc) · [`0054de18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md#insn-0054de18) · [`0054de54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md#insn-0054de54)
- 新版 [`0054de0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd68.md#insn-0054de0c) · [`0054de58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd68.md#insn-0054de58) · [`0054de94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd68.md#insn-0054de94)

~~~diff
- 0054ddcc ["INT_ADD", "register:40f0:8", ["const:54ddcc:8", "const:4:8"]]
- 0054ddcc ["CALL", null, ["callee:00c57e90:8"]]
+ 0054de0c ["INT_ADD", "register:40f0:8", ["const:54de0c:8", "const:4:8"]]
+ 0054de0c ["CALL", null, ["callee:00c57e90:8"]]
- 0054ddcc bytes 31271c94
+ 0054de0c bytes 21281c94
- 0054de18 ["INT_ADD", "register:40f0:8", ["const:54de18:8", "const:4:8"]]
- 0054de18 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054de58 ["INT_ADD", "register:40f0:8", ["const:54de58:8", "const:4:8"]]
+ 0054de58 ["CALL", null, ["callee:00c57e90:8"]]
- 0054de18 bytes 1e271c94
+ 0054de58 bytes 0e281c94
- 0054de54 ["INT_ADD", "register:40f0:8", ["const:54de54:8", "const:4:8"]]
- 0054de54 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0054de94 ["INT_ADD", "register:40f0:8", ["const:54de94:8", "const:4:8"]]
+ 0054de94 ["CALL", null, ["callee:00c53cd0:8"]]
- 0054de54 bytes 97161c94
+ 0054de94 bytes 8f171c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8e79286bf7af24b59832a4a18e42429"></a>

### [`0054dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md) → [`0054e004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e004.md) FUN_0054e004

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054dd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd68.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md#insn-0054e040) · [`0054e088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md#insn-0054e088) · [`0054e09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dfc4.md#insn-0054e09c)
- 新版 [`0054e080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e004.md#insn-0054e080) · [`0054e0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e004.md#insn-0054e0c8) · [`0054e0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e004.md#insn-0054e0dc)

~~~diff
- 0054e040 ["INT_ADD", "register:40f0:8", ["const:54e040:8", "const:4:8"]]
- 0054e040 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054e080 ["INT_ADD", "register:40f0:8", ["const:54e080:8", "const:4:8"]]
+ 0054e080 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054e040 bytes 9c261c94
+ 0054e080 bytes 8c271c94
- 0054e088 ["INT_ADD", "register:40f0:8", ["const:54e088:8", "const:4:8"]]
- 0054e088 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054e0c8 ["INT_ADD", "register:40f0:8", ["const:54e0c8:8", "const:4:8"]]
+ 0054e0c8 ["CALL", null, ["callee:00c53d00:8"]]
- 0054e088 bytes 16161c94
+ 0054e0c8 bytes 0e171c94
- 0054e09c ["COPY", "register:0:8", ["register:4040:8"]]
- 0054e09c ["INT_ADD", "register:40f0:8", ["const:54e09c:8", "const:4:8"]]
- 0054e09c ["CALLIND", null, ["register:0:8"]]
+ 0054e0dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e0dc ["INT_ADD", "register:40f0:8", ["const:54e0dc:8", "const:4:8"]]
+ 0054e0dc ["CALLIND", null, ["register:0:8"]]
- 0054e09c bytes 00013fd6
+ 0054e0dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b5931c024320a2bd83b3d30ebcd7e58"></a>

### [`0054e0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md) → [`0054e13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e13c.md) FUN_0054e13c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0054dd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd68.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md#insn-0054e134) · [`0054e184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md#insn-0054e184) · [`0054e198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e0fc.md#insn-0054e198)
- 新版 [`0054e174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e13c.md#insn-0054e174) · [`0054e1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e13c.md#insn-0054e1c4) · [`0054e1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e13c.md#insn-0054e1d8)

~~~diff
- 0054e134 ["INT_ADD", "register:40f0:8", ["const:54e134:8", "const:4:8"]]
- 0054e134 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054e174 ["INT_ADD", "register:40f0:8", ["const:54e174:8", "const:4:8"]]
+ 0054e174 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054e134 bytes 5f261c94
+ 0054e174 bytes 4f271c94
- 0054e184 ["INT_ADD", "register:40f0:8", ["const:54e184:8", "const:4:8"]]
- 0054e184 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054e1c4 ["INT_ADD", "register:40f0:8", ["const:54e1c4:8", "const:4:8"]]
+ 0054e1c4 ["CALL", null, ["callee:00c53d00:8"]]
- 0054e184 bytes d7151c94
+ 0054e1c4 bytes cf161c94
- 0054e198 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054e198 ["INT_ADD", "register:40f0:8", ["const:54e198:8", "const:4:8"]]
- 0054e198 ["CALLIND", null, ["register:0:8"]]
+ 0054e1d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e1d8 ["INT_ADD", "register:40f0:8", ["const:54e1d8:8", "const:4:8"]]
+ 0054e1d8 ["CALLIND", null, ["register:0:8"]]
- 0054e198 bytes 00013fd6
+ 0054e1d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b058dc33778b7a9137331b8a03dc5adf"></a>

### [`0054e1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md) → [`0054e234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e234.md) FUN_0054e234

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`0054e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00548584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md) [`0054e5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e5d0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md#insn-0054e298) · [`0054e304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md#insn-0054e304) · [`0054e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md#insn-0054e360)
- 新版 [`0054e2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e234.md#insn-0054e2d8) · [`0054e344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e234.md#insn-0054e344) · [`0054e3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e234.md#insn-0054e3a0)

~~~diff
- 0054e298 ["INT_ADD", "register:40f0:8", ["const:54e298:8", "const:4:8"]]
- 0054e298 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054e2d8 ["INT_ADD", "register:40f0:8", ["const:54e2d8:8", "const:4:8"]]
+ 0054e2d8 ["CALL", null, ["callee:00c57e90:8"]]
- 0054e298 bytes fe251c94
+ 0054e2d8 bytes ee261c94
- 0054e304 ["INT_ADD", "register:40f0:8", ["const:54e304:8", "const:4:8"]]
- 0054e304 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0054e344 ["INT_ADD", "register:40f0:8", ["const:54e344:8", "const:4:8"]]
+ 0054e344 ["CALL", null, ["callee:00c53cd0:8"]]
- 0054e304 bytes 6b151c94
+ 0054e344 bytes 63161c94
- 0054e360 ["INT_ADD", "register:40f0:8", ["const:54e360:8", "const:4:8"]]
- 0054e360 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0054e3a0 ["INT_ADD", "register:40f0:8", ["const:54e3a0:8", "const:4:8"]]
+ 0054e3a0 ["CALL", null, ["callee:00c53cd0:8"]]
- 0054e360 bytes 54151c94
+ 0054e3a0 bytes 4c161c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ff1109ebee6f9166c7d44c899809fb"></a>

### [`0054e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md) → [`0054e5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e5d0.md) FUN_0054e5d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054e1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1f4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0054e234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e234.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md#insn-0054e604) · [`0054e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md#insn-0054e618) · [`0054e620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e590.md#insn-0054e620)
- 新版 [`0054e644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e5d0.md#insn-0054e644) · [`0054e658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e5d0.md#insn-0054e658) · [`0054e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e5d0.md#insn-0054e660)

~~~diff
- 0054e604 ["INT_ADD", "register:40f0:8", ["const:54e604:8", "const:4:8"]]
- 0054e604 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054e644 ["INT_ADD", "register:40f0:8", ["const:54e644:8", "const:4:8"]]
+ 0054e644 ["CALL", null, ["callee:00c53d00:8"]]
- 0054e604 bytes b7141c94
+ 0054e644 bytes af151c94
- 0054e618 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054e618 ["INT_ADD", "register:40f0:8", ["const:54e618:8", "const:4:8"]]
- 0054e618 ["CALLIND", null, ["register:0:8"]]
+ 0054e658 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e658 ["INT_ADD", "register:40f0:8", ["const:54e658:8", "const:4:8"]]
+ 0054e658 ["CALLIND", null, ["register:0:8"]]
- 0054e618 bytes 00013fd6
+ 0054e658 bytes 00013fd6
- 0054e620 ["INT_ADD", "register:40f0:8", ["const:54e620:8", "const:4:8"]]
- 0054e620 ["CALL", null, ["callee:00c57e80:8"]]
+ 0054e660 ["INT_ADD", "register:40f0:8", ["const:54e660:8", "const:4:8"]]
+ 0054e660 ["CALL", null, ["callee:00c57e80:8"]]
- 0054e620 bytes 18251c94
+ 0054e660 bytes 08261c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85656845da9d8ee996e7a850e4e03baa"></a>

### [`0054e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md) → [`0054e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e740.md) FUN_0054e740

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0054db94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054db94.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md#insn-0054e78c) · [`0054e820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md#insn-0054e820) · [`0054e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md#insn-0054e834)
- 新版 [`0054e7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e740.md#insn-0054e7cc) · [`0054e860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e740.md#insn-0054e860) · [`0054e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e740.md#insn-0054e874)

~~~diff
- 0054e78c ["INT_ADD", "register:40f0:8", ["const:54e78c:8", "const:4:8"]]
- 0054e78c ["CALL", null, ["callee:00c57e90:8"]]
+ 0054e7cc ["INT_ADD", "register:40f0:8", ["const:54e7cc:8", "const:4:8"]]
+ 0054e7cc ["CALL", null, ["callee:00c57e90:8"]]
- 0054e78c bytes c1241c94
+ 0054e7cc bytes b1251c94
- 0054e820 ["INT_ADD", "register:40f0:8", ["const:54e820:8", "const:4:8"]]
- 0054e820 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054e860 ["INT_ADD", "register:40f0:8", ["const:54e860:8", "const:4:8"]]
+ 0054e860 ["CALL", null, ["callee:00c53d00:8"]]
- 0054e820 bytes 30141c94
+ 0054e860 bytes 28151c94
- 0054e834 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054e834 ["INT_ADD", "register:40f0:8", ["const:54e834:8", "const:4:8"]]
- 0054e834 ["CALLIND", null, ["register:0:8"]]
+ 0054e874 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e874 ["INT_ADD", "register:40f0:8", ["const:54e874:8", "const:4:8"]]
+ 0054e874 ["CALLIND", null, ["register:0:8"]]
- 0054e834 bytes 00013fd6
+ 0054e874 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3cb03b8054fde4551ce3a9daa3c4239"></a>

### [`0054e884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md) → [`0054e8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e8c4.md) FUN_0054e8c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md#insn-0054e8f4) · [`0054e908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md#insn-0054e908) · [`0054e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e884.md#insn-0054e910)
- 新版 [`0054e934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e8c4.md#insn-0054e934) · [`0054e948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e8c4.md#insn-0054e948) · [`0054e950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e8c4.md#insn-0054e950)

~~~diff
- 0054e8f4 ["INT_ADD", "register:40f0:8", ["const:54e8f4:8", "const:4:8"]]
- 0054e8f4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0054e934 ["INT_ADD", "register:40f0:8", ["const:54e934:8", "const:4:8"]]
+ 0054e934 ["CALL", null, ["callee:00c53d00:8"]]
- 0054e8f4 bytes fb131c94
+ 0054e934 bytes f3141c94
- 0054e908 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054e908 ["INT_ADD", "register:40f0:8", ["const:54e908:8", "const:4:8"]]
- 0054e908 ["CALLIND", null, ["register:0:8"]]
+ 0054e948 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0054e948 ["INT_ADD", "register:40f0:8", ["const:54e948:8", "const:4:8"]]
+ 0054e948 ["CALLIND", null, ["register:0:8"]]
- 0054e908 bytes 00013fd6
+ 0054e948 bytes 00013fd6
- 0054e910 ["INT_ADD", "register:40f0:8", ["const:54e910:8", "const:4:8"]]
- 0054e910 ["CALL", null, ["callee:00c57e80:8"]]
+ 0054e950 ["INT_ADD", "register:40f0:8", ["const:54e950:8", "const:4:8"]]
+ 0054e950 ["CALL", null, ["callee:00c57e80:8"]]
- 0054e910 bytes 5c241c94
+ 0054e950 bytes 4c251c94
~~~


<a id="compare-8071b231a5f527854e414ec27da311c4"></a>

### [`0054e938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md) → [`0054e978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e978.md) FUN_0054e978

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`0053f86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f86c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`0053f8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f8ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054e9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md#insn-0054e9e0) · [`0054eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md#insn-0054eaec) · [`0054eb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e938.md#insn-0054eb44)
- 新版 [`0054ea20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e978.md#insn-0054ea20) · [`0054eb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e978.md#insn-0054eb2c) · [`0054eb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e978.md#insn-0054eb84)

~~~diff
- 0054e9e0 ["INT_ADD", "register:40f0:8", ["const:54e9e0:8", "const:4:8"]]
- 0054e9e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054ea20 ["INT_ADD", "register:40f0:8", ["const:54ea20:8", "const:4:8"]]
+ 0054ea20 ["CALL", null, ["callee:00c57e90:8"]]
- 0054e9e0 bytes 2c241c94
+ 0054ea20 bytes 1c251c94
- 0054eaec ["INT_ADD", "register:40f0:8", ["const:54eaec:8", "const:4:8"]]
- 0054eaec ["CALL", null, ["callee:0053f810:8"]]
+ 0054eb2c ["INT_ADD", "register:40f0:8", ["const:54eb2c:8", "const:4:8"]]
+ 0054eb2c ["CALL", null, ["callee:0053f810:8"]]
- 0054eaec bytes 39c3ff97
+ 0054eb2c bytes 39c3ff97
- 0054eb44 ["INT_ADD", "register:40f0:8", ["const:54eb44:8", "const:4:8"]]
- 0054eb44 ["CALL", null, ["callee:0053f8ac:8"]]
+ 0054eb84 ["INT_ADD", "register:40f0:8", ["const:54eb84:8", "const:4:8"]]
+ 0054eb84 ["CALL", null, ["callee:0053f8ac:8"]]
- 0054eb44 bytes 4ac3ff97
+ 0054eb84 bytes 4ac3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88da1c24e187a92b5efa897f05e8a67d"></a>

### [`0054eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md) → [`0054eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md) FUN_0054eb8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) [`0052d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d3d0.md) · 呼出先 6件 [`0053f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md) [`0053f86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f86c.md) [`0054d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d958.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md) [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) [`0052d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d410.md) · 呼出先 6件 [`0053f544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f544.md) [`0053f8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f8ac.md) [`0054d998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d998.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054ebac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md#insn-0054ebac) · [`0054ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md#insn-0054ec0c) · [`0054ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md#insn-0054ec78)
- 新版 [`0054ebec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md#insn-0054ebec) · [`0054ec4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md#insn-0054ec4c) · [`0054ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md#insn-0054ecb8)

~~~diff
- 0054ebac ["INT_ADD", "register:40f0:8", ["const:54ebac:8", "const:4:8"]]
- 0054ebac ["CALL", null, ["callee:00c57e90:8"]]
+ 0054ebec ["INT_ADD", "register:40f0:8", ["const:54ebec:8", "const:4:8"]]
+ 0054ebec ["CALL", null, ["callee:00c57e90:8"]]
- 0054ebac bytes b9231c94
+ 0054ebec bytes a9241c94
- 0054ec0c ["INT_ADD", "register:40f0:8", ["const:54ec0c:8", "const:4:8"]]
- 0054ec0c ["CALL", null, ["callee:0053f544:8"]]
+ 0054ec4c ["INT_ADD", "register:40f0:8", ["const:54ec4c:8", "const:4:8"]]
+ 0054ec4c ["CALL", null, ["callee:0053f544:8"]]
- 0054ec0c bytes 3ec2ff97
+ 0054ec4c bytes 3ec2ff97
- 0054ec78 ["INT_ADD", "register:40f0:8", ["const:54ec78:8", "const:4:8"]]
- 0054ec78 ["CALL", null, ["callee:0053f8ac:8"]]
+ 0054ecb8 ["INT_ADD", "register:40f0:8", ["const:54ecb8:8", "const:4:8"]]
+ 0054ecb8 ["CALL", null, ["callee:0053f8ac:8"]]
- 0054ec78 bytes fdc2ff97
+ 0054ecb8 bytes fdc2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044601267cf32effc8dc65ea97020373"></a>

### [`0054ecc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md) → [`0054ed04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ed04.md) FUN_0054ed04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) [`0054eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) [`0054eefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eefc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054ed50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md#insn-0054ed50) · [`0054ee6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md#insn-0054ee6c) · [`0054ee90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md#insn-0054ee90)
- 新版 [`0054ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ed04.md#insn-0054ed90) · [`0054eeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ed04.md#insn-0054eeac) · [`0054eed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ed04.md#insn-0054eed0)

~~~diff
- 0054ed50 ["INT_ADD", "register:40f0:8", ["const:54ed50:8", "const:4:8"]]
- 0054ed50 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054ed90 ["INT_ADD", "register:40f0:8", ["const:54ed90:8", "const:4:8"]]
+ 0054ed90 ["CALL", null, ["callee:00c57e90:8"]]
- 0054ed50 bytes 50231c94
+ 0054ed90 bytes 40241c94
- 0054ee6c ["INT_ADD", "register:40f0:8", ["const:54ee6c:8", "const:4:8"]]
- 0054ee6c ["CALL", null, ["callee:0052c244:8"]]
+ 0054eeac ["INT_ADD", "register:40f0:8", ["const:54eeac:8", "const:4:8"]]
+ 0054eeac ["CALL", null, ["callee:0052c244:8"]]
- 0054ee6c bytes e674ff97
+ 0054eeac bytes e674ff97
- 0054ee90 ["INT_ADD", "register:40f0:8", ["const:54ee90:8", "const:4:8"]]
- 0054ee90 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054eed0 ["INT_ADD", "register:40f0:8", ["const:54eed0:8", "const:4:8"]]
+ 0054eed0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0054ee90 bytes 08231c94
+ 0054eed0 bytes f8231c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4991e2ca9a64660a3055a1a1cdce83b9"></a>

### [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) → [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) FUN_0054f194

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) [`005881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md) [`00726234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md) · 呼出先 2件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`0058820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md) [`00726274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726274.md) · 呼出先 2件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0054f1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md#insn-0054f1dc) · [`0054f230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md#insn-0054f230) · [`0054f2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md#insn-0054f2cc)
- 新版 [`0054f21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md#insn-0054f21c) · [`0054f270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md#insn-0054f270) · [`0054f30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md#insn-0054f30c)

~~~diff
- 0054f1dc ["INT_ADD", "register:40f0:8", ["const:54f1dc:8", "const:4:8"]]
- 0054f1dc ["CALL", null, ["callee:00c58050:8"]]
+ 0054f21c ["INT_ADD", "register:40f0:8", ["const:54f21c:8", "const:4:8"]]
+ 0054f21c ["CALL", null, ["callee:00c58050:8"]]
- 0054f1dc bytes 9d221c94
+ 0054f21c bytes 8d231c94
- 0054f230 ["INT_ADD", "register:40f0:8", ["const:54f230:8", "const:4:8"]]
- 0054f230 ["CALL", null, ["callee:00c58050:8"]]
+ 0054f270 ["INT_ADD", "register:40f0:8", ["const:54f270:8", "const:4:8"]]
+ 0054f270 ["CALL", null, ["callee:00c58050:8"]]
- 0054f230 bytes 88221c94
+ 0054f270 bytes 78231c94
- 0054f2cc ["INT_ADD", "register:40f0:8", ["const:54f2cc:8", "const:4:8"]]
- 0054f2cc ["CALL", null, ["callee:00c58050:8"]]
+ 0054f30c ["INT_ADD", "register:40f0:8", ["const:54f30c:8", "const:4:8"]]
+ 0054f30c ["CALL", null, ["callee:00c58050:8"]]
- 0054f2cc bytes 61221c94
+ 0054f30c bytes 51231c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70038495c412c3c28c8ce89fa8b0807"></a>

### [`00550b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b68.md) → [`00550ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba8.md) FUN_00550ba8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00550b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b68.md#insn-00550b78)
- 新版 [`00550bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba8.md#insn-00550bb8)

~~~diff
- 00550b78 ["INT_ADD", "register:40f0:8", ["const:550b78:8", "const:4:8"]]
- 00550b78 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00550bb8 ["INT_ADD", "register:40f0:8", ["const:550bb8:8", "const:4:8"]]
+ 00550bb8 ["CALL", null, ["callee:00c57ea0:8"]]
- 00550b78 bytes ca1b1c94
+ 00550bb8 bytes ba1c1c94
~~~


<a id="compare-6ce24ba59ae124e28277600cef2b4950"></a>

### [`00550bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md) → [`00550c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c38.md) FUN_00550c38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 4件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 4件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00550c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md#insn-00550c24) · [`00550c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md#insn-00550c3c) · [`00550c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md#insn-00550c4c)
- 新版 [`00550c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c38.md#insn-00550c64) · [`00550c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c38.md#insn-00550c7c) · [`00550c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c38.md#insn-00550c8c)

~~~diff
- 00550c24 ["INT_ADD", "register:40f0:8", ["const:550c24:8", "const:4:8"]]
- 00550c24 ["CALL", null, ["callee:00550ba4:8"]]
+ 00550c64 ["INT_ADD", "register:40f0:8", ["const:550c64:8", "const:4:8"]]
+ 00550c64 ["CALL", null, ["callee:00550ba4:8"]]
- 00550c24 bytes d0ffff97
+ 00550c64 bytes d0ffff97
- 00550c3c ["COPY", "register:0:8", ["register:4048:8"]]
- 00550c3c ["INT_ADD", "register:40f0:8", ["const:550c3c:8", "const:4:8"]]
- 00550c3c ["CALLIND", null, ["register:0:8"]]
+ 00550c7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00550c7c ["INT_ADD", "register:40f0:8", ["const:550c7c:8", "const:4:8"]]
+ 00550c7c ["CALLIND", null, ["register:0:8"]]
- 00550c3c bytes 20013fd6
+ 00550c7c bytes 20013fd6
- 00550c4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00550c4c ["INT_ADD", "register:40f0:8", ["const:550c4c:8", "const:4:8"]]
- 00550c4c ["CALLIND", null, ["register:0:8"]]
+ 00550c8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550c8c ["INT_ADD", "register:40f0:8", ["const:550c8c:8", "const:4:8"]]
+ 00550c8c ["CALLIND", null, ["register:0:8"]]
- 00550c4c bytes 00013fd6
+ 00550c8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3bc03d6f5174272192dc29503c8bf89"></a>

### [`00550cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md) → [`00550d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d38.md) FUN_00550d38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00488684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488684.md) [`00497380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) · 呼出先 4件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`004886c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md) [`004973c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004973c0.md) [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) · 呼出先 4件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00550d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md#insn-00550d24) · [`00550d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md#insn-00550d3c) · [`00550d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md#insn-00550d50)
- 新版 [`00550d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d38.md#insn-00550d64) · [`00550d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d38.md#insn-00550d7c) · [`00550d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d38.md#insn-00550d90)

~~~diff
- 00550d24 ["INT_ADD", "register:40f0:8", ["const:550d24:8", "const:4:8"]]
- 00550d24 ["CALL", null, ["callee:00550ba4:8"]]
+ 00550d64 ["INT_ADD", "register:40f0:8", ["const:550d64:8", "const:4:8"]]
+ 00550d64 ["CALL", null, ["callee:00550ba4:8"]]
- 00550d24 bytes 90ffff97
+ 00550d64 bytes 90ffff97
- 00550d3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00550d3c ["INT_ADD", "register:40f0:8", ["const:550d3c:8", "const:4:8"]]
- 00550d3c ["CALLIND", null, ["register:0:8"]]
+ 00550d7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550d7c ["INT_ADD", "register:40f0:8", ["const:550d7c:8", "const:4:8"]]
+ 00550d7c ["CALLIND", null, ["register:0:8"]]
- 00550d3c bytes 00013fd6
+ 00550d7c bytes 00013fd6
- 00550d50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00550d50 ["INT_ADD", "register:40f0:8", ["const:550d50:8", "const:4:8"]]
- 00550d50 ["CALLIND", null, ["register:0:8"]]
+ 00550d90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550d90 ["INT_ADD", "register:40f0:8", ["const:550d90:8", "const:4:8"]]
+ 00550d90 ["CALLIND", null, ["register:0:8"]]
- 00550d50 bytes 00013fd6
+ 00550d90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ebfa13f9b0f5b0f0da8b2e37f2e75b"></a>

### [`00550df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md) → [`00550e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550e34.md) FUN_00550e34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 4件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md) [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) · 呼出先 4件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00550e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md#insn-00550e20) · [`00550e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md#insn-00550e38) · [`00550e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550df4.md#insn-00550e4c)
- 新版 [`00550e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550e34.md#insn-00550e60) · [`00550e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550e34.md#insn-00550e78) · [`00550e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550e34.md#insn-00550e8c)

~~~diff
- 00550e20 ["INT_ADD", "register:40f0:8", ["const:550e20:8", "const:4:8"]]
- 00550e20 ["CALL", null, ["callee:00550ba4:8"]]
+ 00550e60 ["INT_ADD", "register:40f0:8", ["const:550e60:8", "const:4:8"]]
+ 00550e60 ["CALL", null, ["callee:00550ba4:8"]]
- 00550e20 bytes 51ffff97
+ 00550e60 bytes 51ffff97
- 00550e38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00550e38 ["INT_ADD", "register:40f0:8", ["const:550e38:8", "const:4:8"]]
- 00550e38 ["CALLIND", null, ["register:0:8"]]
+ 00550e78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550e78 ["INT_ADD", "register:40f0:8", ["const:550e78:8", "const:4:8"]]
+ 00550e78 ["CALLIND", null, ["register:0:8"]]
- 00550e38 bytes 00013fd6
+ 00550e78 bytes 00013fd6
- 00550e4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00550e4c ["INT_ADD", "register:40f0:8", ["const:550e4c:8", "const:4:8"]]
- 00550e4c ["CALLIND", null, ["register:0:8"]]
+ 00550e8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00550e8c ["INT_ADD", "register:40f0:8", ["const:550e8c:8", "const:4:8"]]
+ 00550e8c ["CALLIND", null, ["register:0:8"]]
- 00550e4c bytes 00013fd6
+ 00550e8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-469955674daf86615b7c259fb553d06c"></a>

### [`005511e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005511e4.md) → [`00551224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551224.md) FUN_00551224

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00b2b8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005511e4.md#insn-00551200) · [`00551220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005511e4.md#insn-00551220)
- 新版 [`00551240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551224.md#insn-00551240) · [`00551260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551224.md#insn-00551260)

~~~diff
- 00551200 ["INT_ADD", "register:40f0:8", ["const:551200:8", "const:4:8"]]
- 00551200 ["CALL", null, ["callee:00c53d00:8"]]
+ 00551240 ["INT_ADD", "register:40f0:8", ["const:551240:8", "const:4:8"]]
+ 00551240 ["CALL", null, ["callee:00c53d00:8"]]
- 00551200 bytes b8091c94
+ 00551240 bytes b00a1c94
- 00551220 ["COPY", "register:0:8", ["register:4040:8"]]
- 00551220 ["INT_ADD", "register:40f0:8", ["const:551220:8", "const:4:8"]]
- 00551220 ["CALLIND", null, ["register:0:8"]]
+ 00551260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00551260 ["INT_ADD", "register:40f0:8", ["const:551260:8", "const:4:8"]]
+ 00551260 ["CALLIND", null, ["register:0:8"]]
- 00551220 bytes 00013fd6
+ 00551260 bytes 00013fd6
~~~


<a id="compare-28373578bbb4b25a3d9785191645fd6e"></a>

### [`005513d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005513d4.md) → [`00551414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551414.md) FUN_00551414

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005513f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005513d4.md#insn-005513f0) · [`00551410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005513d4.md#insn-00551410)
- 新版 [`00551430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551414.md#insn-00551430) · [`00551450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551414.md#insn-00551450)

~~~diff
- 005513f0 ["INT_ADD", "register:40f0:8", ["const:5513f0:8", "const:4:8"]]
- 005513f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00551430 ["INT_ADD", "register:40f0:8", ["const:551430:8", "const:4:8"]]
+ 00551430 ["CALL", null, ["callee:00c53d00:8"]]
- 005513f0 bytes 3c091c94
+ 00551430 bytes 340a1c94
- 00551410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00551410 ["INT_ADD", "register:40f0:8", ["const:551410:8", "const:4:8"]]
- 00551410 ["CALLIND", null, ["register:0:8"]]
+ 00551450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00551450 ["INT_ADD", "register:40f0:8", ["const:551450:8", "const:4:8"]]
+ 00551450 ["CALLIND", null, ["register:0:8"]]
- 00551410 bytes 00013fd6
+ 00551450 bytes 00013fd6
~~~


<a id="compare-1c75f626b748ed70f6b7fa6a8f7d3641"></a>

### [`00551e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md) → [`00551eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551eac.md) FUN_00551eac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) · 呼出先 2件 [`00555070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) [`008aac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008aa/008aac28.md) [`008abcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008abcf8.md) [`008d8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md) · 呼出先 2件 [`005550b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005550b0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00551ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md#insn-00551ea4) · [`00551ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md#insn-00551ec8)
- 新版 [`00551ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551eac.md#insn-00551ee4) · [`00551f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551eac.md#insn-00551f08)

~~~diff
- 00551ea4 ["INT_ADD", "register:40f0:8", ["const:551ea4:8", "const:4:8"]]
- 00551ea4 ["CALL", null, ["callee:005550b0:8"]]
+ 00551ee4 ["INT_ADD", "register:40f0:8", ["const:551ee4:8", "const:4:8"]]
+ 00551ee4 ["CALL", null, ["callee:005550b0:8"]]
- 00551ea4 bytes 730c0094
+ 00551ee4 bytes 730c0094
- 00551ec8 ["INT_ADD", "register:40f0:8", ["const:551ec8:8", "const:4:8"]]
- 00551ec8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00551f08 ["INT_ADD", "register:40f0:8", ["const:551f08:8", "const:4:8"]]
+ 00551f08 ["CALL", null, ["callee:00c57ee0:8"]]
- 00551ec8 bytes 06171c94
+ 00551f08 bytes f6171c94
~~~


<a id="compare-408328ab71cf6bad716f26de1b2ff5d2"></a>

### [`005551e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551e4.md) → [`00555224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555224.md) FUN_00555224

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00555200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551e4.md#insn-00555200) · [`00555220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551e4.md#insn-00555220)
- 新版 [`00555240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555224.md#insn-00555240) · [`00555260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555224.md#insn-00555260)

~~~diff
- 00555200 ["INT_ADD", "register:40f0:8", ["const:555200:8", "const:4:8"]]
- 00555200 ["CALL", null, ["callee:00c53d00:8"]]
+ 00555240 ["INT_ADD", "register:40f0:8", ["const:555240:8", "const:4:8"]]
+ 00555240 ["CALL", null, ["callee:00c53d00:8"]]
- 00555200 bytes b8f91b94
+ 00555240 bytes b0fa1b94
- 00555220 ["COPY", "register:0:8", ["register:4040:8"]]
- 00555220 ["INT_ADD", "register:40f0:8", ["const:555220:8", "const:4:8"]]
- 00555220 ["CALLIND", null, ["register:0:8"]]
+ 00555260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00555260 ["INT_ADD", "register:40f0:8", ["const:555260:8", "const:4:8"]]
+ 00555260 ["CALLIND", null, ["register:0:8"]]
- 00555220 bytes 00013fd6
+ 00555260 bytes 00013fd6
~~~


