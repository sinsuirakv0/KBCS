# v15.7.3 → v15.7.4 · 要調査の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-a71de58ab917503f620b19e183fa9698"></a>

### [`00a9d164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d164.md) → [`00a9d1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d1a8.md) FUN_00a9d1a8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d164.md#insn-00a9d180)
- 新版 [`00a9d1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d1a8.md#insn-00a9d1c4)

~~~diff
- 00a9d180 ["INT_ADD", "register:40f0:8", ["const:a9d180:8", "const:4:8"]]
- 00a9d180 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d1c4 ["INT_ADD", "register:40f0:8", ["const:a9d1c4:8", "const:4:8"]]
+ 00a9d1c4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d180 bytes 0009f697
+ 00a9d1c4 bytes ef08f697
~~~


<a id="compare-842274cf774257cfd7c06f92f2836855"></a>

### [`00a9d1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d1b0.md) → [`00a9d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d1f4.md) FUN_00a9d1f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d1b0.md#insn-00a9d1cc)
- 新版 [`00a9d210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d1f4.md#insn-00a9d210)

~~~diff
- 00a9d1cc ["INT_ADD", "register:40f0:8", ["const:a9d1cc:8", "const:4:8"]]
- 00a9d1cc ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d210 ["INT_ADD", "register:40f0:8", ["const:a9d210:8", "const:4:8"]]
+ 00a9d210 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d1cc bytes ed08f697
+ 00a9d210 bytes dc08f697
~~~


<a id="compare-d218e32ed0b3d2f8f876e71cbc549a43"></a>

### [`00a9d204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d204.md) → [`00a9d248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d248.md) FUN_00a9d248

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005ce03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ce/005ce03c.md) [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`005ce03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ce03c.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d204.md#insn-00a9d218)
- 新版 [`00a9d25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d248.md#insn-00a9d25c)

~~~diff
- 00a9d218 ["INT_ADD", "register:40f0:8", ["const:a9d218:8", "const:4:8"]]
- 00a9d218 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d25c ["INT_ADD", "register:40f0:8", ["const:a9d25c:8", "const:4:8"]]
+ 00a9d25c ["CALL", null, ["callee:0081f580:8"]]
- 00a9d218 bytes da08f697
+ 00a9d25c bytes c908f697
~~~


<a id="compare-bdba37743cedb18f6716c0f1b87044a3"></a>

### [`00a9d244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d244.md) → [`00a9d288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d288.md) FUN_00a9d288

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d244.md#insn-00a9d260)
- 新版 [`00a9d2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d288.md#insn-00a9d2a4)

~~~diff
- 00a9d260 ["INT_ADD", "register:40f0:8", ["const:a9d260:8", "const:4:8"]]
- 00a9d260 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d2a4 ["INT_ADD", "register:40f0:8", ["const:a9d2a4:8", "const:4:8"]]
+ 00a9d2a4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d260 bytes c808f697
+ 00a9d2a4 bytes b708f697
~~~


<a id="compare-243aad1f7704aa7e0484c1d585e39e3c"></a>

### [`00a9d290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d290.md) → [`00a9d2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d2d4.md) FUN_00a9d2d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005ce03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ce/005ce03c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`005ce03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ce03c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d290.md#insn-00a9d2ac)
- 新版 [`00a9d2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d2d4.md#insn-00a9d2f0)

~~~diff
- 00a9d2ac ["INT_ADD", "register:40f0:8", ["const:a9d2ac:8", "const:4:8"]]
- 00a9d2ac ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d2f0 ["INT_ADD", "register:40f0:8", ["const:a9d2f0:8", "const:4:8"]]
+ 00a9d2f0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d2ac bytes b508f697
+ 00a9d2f0 bytes a408f697
~~~


<a id="compare-bca9dcf86240e2df3afc00849959a98c"></a>

### [`00a9d2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d2e4.md) → [`00a9d328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d328.md) FUN_00a9d328

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d2e4.md#insn-00a9d2f8)
- 新版 [`00a9d33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d328.md#insn-00a9d33c)

~~~diff
- 00a9d2f8 ["INT_ADD", "register:40f0:8", ["const:a9d2f8:8", "const:4:8"]]
- 00a9d2f8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d33c ["INT_ADD", "register:40f0:8", ["const:a9d33c:8", "const:4:8"]]
+ 00a9d33c ["CALL", null, ["callee:0081f580:8"]]
- 00a9d2f8 bytes a208f697
+ 00a9d33c bytes 9108f697
~~~


<a id="compare-91d087a9895624a58f4c8feff1d6fd5d"></a>

### [`00a9d6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d6c0.md) → [`00a9d704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d704.md) FUN_00a9d704

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d6c0.md#insn-00a9d6d4) · [`00a9d6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d6c0.md#insn-00a9d6e8) · [`00a9d6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d6c0.md#insn-00a9d6f4)
- 新版 [`00a9d718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d704.md#insn-00a9d718) · [`00a9d72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d704.md#insn-00a9d72c) · [`00a9d738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d704.md#insn-00a9d738)

~~~diff
- 00a9d6d4 ["INT_ADD", "register:40f0:8", ["const:a9d6d4:8", "const:4:8"]]
- 00a9d6d4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d718 ["INT_ADD", "register:40f0:8", ["const:a9d718:8", "const:4:8"]]
+ 00a9d718 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d6d4 bytes ab07f697
+ 00a9d718 bytes 9a07f697
- 00a9d6e8 ["INT_ADD", "register:40f0:8", ["const:a9d6e8:8", "const:4:8"]]
- 00a9d6e8 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d72c ["INT_ADD", "register:40f0:8", ["const:a9d72c:8", "const:4:8"]]
+ 00a9d72c ["CALL", null, ["callee:005c2710:8"]]
- 00a9d6e8 bytes 0a94ec97
+ 00a9d72c bytes f993ec97
- 00a9d6f4 ["INT_ADD", "register:40f0:8", ["const:a9d6f4:8", "const:4:8"]]
- 00a9d6f4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d738 ["INT_ADD", "register:40f0:8", ["const:a9d738:8", "const:4:8"]]
+ 00a9d738 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d6f4 bytes a307f697
+ 00a9d738 bytes 9207f697
~~~


<a id="compare-3a65eb8e9c97f1f277b6b837e74d3a8a"></a>

### [`00a9d728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d728.md) → [`00a9d76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d76c.md) FUN_00a9d76c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d728.md#insn-00a9d744) · [`00a9d758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d728.md#insn-00a9d758) · [`00a9d764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d728.md#insn-00a9d764)
- 新版 [`00a9d788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d76c.md#insn-00a9d788) · [`00a9d79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d76c.md#insn-00a9d79c) · [`00a9d7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d76c.md#insn-00a9d7a8)

~~~diff
- 00a9d744 ["INT_ADD", "register:40f0:8", ["const:a9d744:8", "const:4:8"]]
- 00a9d744 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d788 ["INT_ADD", "register:40f0:8", ["const:a9d788:8", "const:4:8"]]
+ 00a9d788 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d744 bytes 8f07f697
+ 00a9d788 bytes 7e07f697
- 00a9d758 ["INT_ADD", "register:40f0:8", ["const:a9d758:8", "const:4:8"]]
- 00a9d758 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d79c ["INT_ADD", "register:40f0:8", ["const:a9d79c:8", "const:4:8"]]
+ 00a9d79c ["CALL", null, ["callee:005c2710:8"]]
- 00a9d758 bytes ee93ec97
+ 00a9d79c bytes dd93ec97
- 00a9d764 ["INT_ADD", "register:40f0:8", ["const:a9d764:8", "const:4:8"]]
- 00a9d764 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d7a8 ["INT_ADD", "register:40f0:8", ["const:a9d7a8:8", "const:4:8"]]
+ 00a9d7a8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d764 bytes 8707f697
+ 00a9d7a8 bytes 7607f697
~~~


<a id="compare-4dc4c3bb9824e3d42fd69afa187e8304"></a>

### [`00a9d794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d794.md) → [`00a9d7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d7d8.md) FUN_00a9d7d8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d794.md#insn-00a9d7b0) · [`00a9d7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d794.md#insn-00a9d7c8) · [`00a9d7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d794.md#insn-00a9d7d0)
- 新版 [`00a9d7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d7d8.md#insn-00a9d7f4) · [`00a9d80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d7d8.md#insn-00a9d80c) · [`00a9d814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d7d8.md#insn-00a9d814)

~~~diff
- 00a9d7b0 ["INT_ADD", "register:40f0:8", ["const:a9d7b0:8", "const:4:8"]]
- 00a9d7b0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d7f4 ["INT_ADD", "register:40f0:8", ["const:a9d7f4:8", "const:4:8"]]
+ 00a9d7f4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d7b0 bytes 7407f697
+ 00a9d7f4 bytes 6307f697
- 00a9d7c8 ["INT_ADD", "register:40f0:8", ["const:a9d7c8:8", "const:4:8"]]
- 00a9d7c8 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d80c ["INT_ADD", "register:40f0:8", ["const:a9d80c:8", "const:4:8"]]
+ 00a9d80c ["CALL", null, ["callee:005c2710:8"]]
- 00a9d7c8 bytes d293ec97
+ 00a9d80c bytes c193ec97
- 00a9d7d0 ["INT_ADD", "register:40f0:8", ["const:a9d7d0:8", "const:4:8"]]
- 00a9d7d0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d814 ["INT_ADD", "register:40f0:8", ["const:a9d814:8", "const:4:8"]]
+ 00a9d814 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d7d0 bytes 6c07f697
+ 00a9d814 bytes 5b07f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aefbde12810dbedea519c794f99049e"></a>

### [`00a9d848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d848.md) → [`00a9d88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d88c.md) FUN_00a9d88c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d848.md#insn-00a9d864) · [`00a9d878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d848.md#insn-00a9d878) · [`00a9d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d848.md#insn-00a9d884)
- 新版 [`00a9d8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d88c.md#insn-00a9d8a8) · [`00a9d8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d88c.md#insn-00a9d8bc) · [`00a9d8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d88c.md#insn-00a9d8c8)

~~~diff
- 00a9d864 ["INT_ADD", "register:40f0:8", ["const:a9d864:8", "const:4:8"]]
- 00a9d864 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d8a8 ["INT_ADD", "register:40f0:8", ["const:a9d8a8:8", "const:4:8"]]
+ 00a9d8a8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d864 bytes 4707f697
+ 00a9d8a8 bytes 3607f697
- 00a9d878 ["INT_ADD", "register:40f0:8", ["const:a9d878:8", "const:4:8"]]
- 00a9d878 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d8bc ["INT_ADD", "register:40f0:8", ["const:a9d8bc:8", "const:4:8"]]
+ 00a9d8bc ["CALL", null, ["callee:005c2710:8"]]
- 00a9d878 bytes a693ec97
+ 00a9d8bc bytes 9593ec97
- 00a9d884 ["INT_ADD", "register:40f0:8", ["const:a9d884:8", "const:4:8"]]
- 00a9d884 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d8c8 ["INT_ADD", "register:40f0:8", ["const:a9d8c8:8", "const:4:8"]]
+ 00a9d8c8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d884 bytes 3f07f697
+ 00a9d8c8 bytes 2e07f697
~~~


<a id="compare-f25d4bdcb991f7251be386c48782fc7e"></a>

### [`00a9d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d8b4.md) → [`00a9d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d8f8.md) FUN_00a9d8f8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d8b4.md#insn-00a9d8d0) · [`00a9d8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d8b4.md#insn-00a9d8e4) · [`00a9d8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d8b4.md#insn-00a9d8f0)
- 新版 [`00a9d914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d8f8.md#insn-00a9d914) · [`00a9d928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d8f8.md#insn-00a9d928) · [`00a9d934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d8f8.md#insn-00a9d934)

~~~diff
- 00a9d8d0 ["INT_ADD", "register:40f0:8", ["const:a9d8d0:8", "const:4:8"]]
- 00a9d8d0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d914 ["INT_ADD", "register:40f0:8", ["const:a9d914:8", "const:4:8"]]
+ 00a9d914 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d8d0 bytes 2c07f697
+ 00a9d914 bytes 1b07f697
- 00a9d8e4 ["INT_ADD", "register:40f0:8", ["const:a9d8e4:8", "const:4:8"]]
- 00a9d8e4 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d928 ["INT_ADD", "register:40f0:8", ["const:a9d928:8", "const:4:8"]]
+ 00a9d928 ["CALL", null, ["callee:005c2710:8"]]
- 00a9d8e4 bytes 8b93ec97
+ 00a9d928 bytes 7a93ec97
- 00a9d8f0 ["INT_ADD", "register:40f0:8", ["const:a9d8f0:8", "const:4:8"]]
- 00a9d8f0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d934 ["INT_ADD", "register:40f0:8", ["const:a9d934:8", "const:4:8"]]
+ 00a9d934 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d8f0 bytes 2407f697
+ 00a9d934 bytes 1307f697
~~~


<a id="compare-cfb7321be48f8e16d616818e7ceb7b94"></a>

### [`00a9d928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d928.md) → [`00a9d96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d96c.md) FUN_00a9d96c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d928.md#insn-00a9d93c) · [`00a9d950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d928.md#insn-00a9d950) · [`00a9d95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d928.md#insn-00a9d95c)
- 新版 [`00a9d980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d96c.md#insn-00a9d980) · [`00a9d994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d96c.md#insn-00a9d994) · [`00a9d9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d96c.md#insn-00a9d9a0)

~~~diff
- 00a9d93c ["INT_ADD", "register:40f0:8", ["const:a9d93c:8", "const:4:8"]]
- 00a9d93c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d980 ["INT_ADD", "register:40f0:8", ["const:a9d980:8", "const:4:8"]]
+ 00a9d980 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d93c bytes 1107f697
+ 00a9d980 bytes 0007f697
- 00a9d950 ["INT_ADD", "register:40f0:8", ["const:a9d950:8", "const:4:8"]]
- 00a9d950 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d994 ["INT_ADD", "register:40f0:8", ["const:a9d994:8", "const:4:8"]]
+ 00a9d994 ["CALL", null, ["callee:005c2710:8"]]
- 00a9d950 bytes 7093ec97
+ 00a9d994 bytes 5f93ec97
- 00a9d95c ["INT_ADD", "register:40f0:8", ["const:a9d95c:8", "const:4:8"]]
- 00a9d95c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d9a0 ["INT_ADD", "register:40f0:8", ["const:a9d9a0:8", "const:4:8"]]
+ 00a9d9a0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d95c bytes 0907f697
+ 00a9d9a0 bytes f806f697
~~~


<a id="compare-1ea8a952dbb9c1db7c5bbef08abed917"></a>

### [`00a9d990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d990.md) → [`00a9d9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d9d4.md) FUN_00a9d9d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d990.md#insn-00a9d9ac) · [`00a9d9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d990.md#insn-00a9d9c0) · [`00a9d9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d990.md#insn-00a9d9cc)
- 新版 [`00a9d9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d9d4.md#insn-00a9d9f0) · [`00a9da04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d9d4.md#insn-00a9da04) · [`00a9da10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d9d4.md#insn-00a9da10)

~~~diff
- 00a9d9ac ["INT_ADD", "register:40f0:8", ["const:a9d9ac:8", "const:4:8"]]
- 00a9d9ac ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d9f0 ["INT_ADD", "register:40f0:8", ["const:a9d9f0:8", "const:4:8"]]
+ 00a9d9f0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d9ac bytes f506f697
+ 00a9d9f0 bytes e406f697
- 00a9d9c0 ["INT_ADD", "register:40f0:8", ["const:a9d9c0:8", "const:4:8"]]
- 00a9d9c0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9da04 ["INT_ADD", "register:40f0:8", ["const:a9da04:8", "const:4:8"]]
+ 00a9da04 ["CALL", null, ["callee:005c2710:8"]]
- 00a9d9c0 bytes 5493ec97
+ 00a9da04 bytes 4393ec97
- 00a9d9cc ["INT_ADD", "register:40f0:8", ["const:a9d9cc:8", "const:4:8"]]
- 00a9d9cc ["CALL", null, ["callee:0081f580:8"]]
+ 00a9da10 ["INT_ADD", "register:40f0:8", ["const:a9da10:8", "const:4:8"]]
+ 00a9da10 ["CALL", null, ["callee:0081f580:8"]]
- 00a9d9cc bytes ed06f697
+ 00a9da10 bytes dc06f697
~~~


<a id="compare-e32b76e3e3e333f5ab57a6e66a5aa595"></a>

### [`00a9d9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d9fc.md) → [`00a9da40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9da40.md) FUN_00a9da40

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9da10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d9fc.md#insn-00a9da10) · [`00a9da24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d9fc.md#insn-00a9da24) · [`00a9da30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d9fc.md#insn-00a9da30)
- 新版 [`00a9da54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9da40.md#insn-00a9da54) · [`00a9da68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9da40.md#insn-00a9da68) · [`00a9da74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9da40.md#insn-00a9da74)

~~~diff
- 00a9da10 ["INT_ADD", "register:40f0:8", ["const:a9da10:8", "const:4:8"]]
- 00a9da10 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9da54 ["INT_ADD", "register:40f0:8", ["const:a9da54:8", "const:4:8"]]
+ 00a9da54 ["CALL", null, ["callee:0081f580:8"]]
- 00a9da10 bytes dc06f697
+ 00a9da54 bytes cb06f697
- 00a9da24 ["INT_ADD", "register:40f0:8", ["const:a9da24:8", "const:4:8"]]
- 00a9da24 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9da68 ["INT_ADD", "register:40f0:8", ["const:a9da68:8", "const:4:8"]]
+ 00a9da68 ["CALL", null, ["callee:005c2710:8"]]
- 00a9da24 bytes 3b93ec97
+ 00a9da68 bytes 2a93ec97
- 00a9da30 ["INT_ADD", "register:40f0:8", ["const:a9da30:8", "const:4:8"]]
- 00a9da30 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9da74 ["INT_ADD", "register:40f0:8", ["const:a9da74:8", "const:4:8"]]
+ 00a9da74 ["CALL", null, ["callee:0081f580:8"]]
- 00a9da30 bytes d406f697
+ 00a9da74 bytes c306f697
~~~


<a id="compare-07f15fffa49dea7917f36cb68ee1dc25"></a>

### [`00a9da64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9da64.md) → [`00a9daa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9daa8.md) FUN_00a9daa8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9da80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9da64.md#insn-00a9da80) · [`00a9da94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9da64.md#insn-00a9da94) · [`00a9daa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9da64.md#insn-00a9daa0)
- 新版 [`00a9dac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9daa8.md#insn-00a9dac4) · [`00a9dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9daa8.md#insn-00a9dad8) · [`00a9dae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9daa8.md#insn-00a9dae4)

~~~diff
- 00a9da80 ["INT_ADD", "register:40f0:8", ["const:a9da80:8", "const:4:8"]]
- 00a9da80 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dac4 ["INT_ADD", "register:40f0:8", ["const:a9dac4:8", "const:4:8"]]
+ 00a9dac4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9da80 bytes c006f697
+ 00a9dac4 bytes af06f697
- 00a9da94 ["INT_ADD", "register:40f0:8", ["const:a9da94:8", "const:4:8"]]
- 00a9da94 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9dad8 ["INT_ADD", "register:40f0:8", ["const:a9dad8:8", "const:4:8"]]
+ 00a9dad8 ["CALL", null, ["callee:005c2710:8"]]
- 00a9da94 bytes 1f93ec97
+ 00a9dad8 bytes 0e93ec97
- 00a9daa0 ["INT_ADD", "register:40f0:8", ["const:a9daa0:8", "const:4:8"]]
- 00a9daa0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dae4 ["INT_ADD", "register:40f0:8", ["const:a9dae4:8", "const:4:8"]]
+ 00a9dae4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9daa0 bytes b806f697
+ 00a9dae4 bytes a706f697
~~~


<a id="compare-bd0e27c765ab5c5b3bde9443d27e6b89"></a>

### [`00a9dad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dad0.md) → [`00a9db14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db14.md) FUN_00a9db14

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dad0.md#insn-00a9dae4) · [`00a9daf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dad0.md#insn-00a9daf8) · [`00a9db04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dad0.md#insn-00a9db04)
- 新版 [`00a9db28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db14.md#insn-00a9db28) · [`00a9db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db14.md#insn-00a9db3c) · [`00a9db48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db14.md#insn-00a9db48)

~~~diff
- 00a9dae4 ["INT_ADD", "register:40f0:8", ["const:a9dae4:8", "const:4:8"]]
- 00a9dae4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9db28 ["INT_ADD", "register:40f0:8", ["const:a9db28:8", "const:4:8"]]
+ 00a9db28 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dae4 bytes a706f697
+ 00a9db28 bytes 9606f697
- 00a9daf8 ["INT_ADD", "register:40f0:8", ["const:a9daf8:8", "const:4:8"]]
- 00a9daf8 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9db3c ["INT_ADD", "register:40f0:8", ["const:a9db3c:8", "const:4:8"]]
+ 00a9db3c ["CALL", null, ["callee:005c2710:8"]]
- 00a9daf8 bytes 0693ec97
+ 00a9db3c bytes f592ec97
- 00a9db04 ["INT_ADD", "register:40f0:8", ["const:a9db04:8", "const:4:8"]]
- 00a9db04 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9db48 ["INT_ADD", "register:40f0:8", ["const:a9db48:8", "const:4:8"]]
+ 00a9db48 ["CALL", null, ["callee:0081f580:8"]]
- 00a9db04 bytes 9f06f697
+ 00a9db48 bytes 8e06f697
~~~


<a id="compare-cf1b659de7d84ad5d5285800f767895a"></a>

### [`00a9db38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9db38.md) → [`00a9db7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db7c.md) FUN_00a9db7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9db54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9db38.md#insn-00a9db54) · [`00a9db68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9db38.md#insn-00a9db68) · [`00a9db74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9db38.md#insn-00a9db74)
- 新版 [`00a9db98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db7c.md#insn-00a9db98) · [`00a9dbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db7c.md#insn-00a9dbac) · [`00a9dbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9db7c.md#insn-00a9dbb8)

~~~diff
- 00a9db54 ["INT_ADD", "register:40f0:8", ["const:a9db54:8", "const:4:8"]]
- 00a9db54 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9db98 ["INT_ADD", "register:40f0:8", ["const:a9db98:8", "const:4:8"]]
+ 00a9db98 ["CALL", null, ["callee:0081f580:8"]]
- 00a9db54 bytes 8b06f697
+ 00a9db98 bytes 7a06f697
- 00a9db68 ["INT_ADD", "register:40f0:8", ["const:a9db68:8", "const:4:8"]]
- 00a9db68 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9dbac ["INT_ADD", "register:40f0:8", ["const:a9dbac:8", "const:4:8"]]
+ 00a9dbac ["CALL", null, ["callee:005c2710:8"]]
- 00a9db68 bytes ea92ec97
+ 00a9dbac bytes d992ec97
- 00a9db74 ["INT_ADD", "register:40f0:8", ["const:a9db74:8", "const:4:8"]]
- 00a9db74 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dbb8 ["INT_ADD", "register:40f0:8", ["const:a9dbb8:8", "const:4:8"]]
+ 00a9dbb8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9db74 bytes 8306f697
+ 00a9dbb8 bytes 7206f697
~~~


<a id="compare-ebae357a7735b443db3a82a4415bf6c4"></a>

### [`00a9dba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dba4.md) → [`00a9dbe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dbe8.md) FUN_00a9dbe8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dba4.md#insn-00a9dbb8) · [`00a9dbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dba4.md#insn-00a9dbcc) · [`00a9dbd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dba4.md#insn-00a9dbd8)
- 新版 [`00a9dbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dbe8.md#insn-00a9dbfc) · [`00a9dc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dbe8.md#insn-00a9dc10) · [`00a9dc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dbe8.md#insn-00a9dc1c)

~~~diff
- 00a9dbb8 ["INT_ADD", "register:40f0:8", ["const:a9dbb8:8", "const:4:8"]]
- 00a9dbb8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dbfc ["INT_ADD", "register:40f0:8", ["const:a9dbfc:8", "const:4:8"]]
+ 00a9dbfc ["CALL", null, ["callee:0081f580:8"]]
- 00a9dbb8 bytes 7206f697
+ 00a9dbfc bytes 6106f697
- 00a9dbcc ["INT_ADD", "register:40f0:8", ["const:a9dbcc:8", "const:4:8"]]
- 00a9dbcc ["CALL", null, ["callee:005c2710:8"]]
+ 00a9dc10 ["INT_ADD", "register:40f0:8", ["const:a9dc10:8", "const:4:8"]]
+ 00a9dc10 ["CALL", null, ["callee:005c2710:8"]]
- 00a9dbcc bytes d192ec97
+ 00a9dc10 bytes c092ec97
- 00a9dbd8 ["INT_ADD", "register:40f0:8", ["const:a9dbd8:8", "const:4:8"]]
- 00a9dbd8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dc1c ["INT_ADD", "register:40f0:8", ["const:a9dc1c:8", "const:4:8"]]
+ 00a9dc1c ["CALL", null, ["callee:0081f580:8"]]
- 00a9dbd8 bytes 6a06f697
+ 00a9dc1c bytes 5906f697
~~~


<a id="compare-b3741f7379d4c57adf3968cf468b1ac8"></a>

### [`00a9dc78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dc78.md) → [`00a9dcbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dcbc.md) FUN_00a9dcbc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dc78.md#insn-00a9dc8c) · [`00a9dca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dc78.md#insn-00a9dca0) · [`00a9dcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dc78.md#insn-00a9dcac)
- 新版 [`00a9dcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dcbc.md#insn-00a9dcd0) · [`00a9dce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dcbc.md#insn-00a9dce4) · [`00a9dcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dcbc.md#insn-00a9dcf0)

~~~diff
- 00a9dc8c ["INT_ADD", "register:40f0:8", ["const:a9dc8c:8", "const:4:8"]]
- 00a9dc8c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dcd0 ["INT_ADD", "register:40f0:8", ["const:a9dcd0:8", "const:4:8"]]
+ 00a9dcd0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dc8c bytes 3d06f697
+ 00a9dcd0 bytes 2c06f697
- 00a9dca0 ["INT_ADD", "register:40f0:8", ["const:a9dca0:8", "const:4:8"]]
- 00a9dca0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9dce4 ["INT_ADD", "register:40f0:8", ["const:a9dce4:8", "const:4:8"]]
+ 00a9dce4 ["CALL", null, ["callee:005c2710:8"]]
- 00a9dca0 bytes 9c92ec97
+ 00a9dce4 bytes 8b92ec97
- 00a9dcac ["INT_ADD", "register:40f0:8", ["const:a9dcac:8", "const:4:8"]]
- 00a9dcac ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dcf0 ["INT_ADD", "register:40f0:8", ["const:a9dcf0:8", "const:4:8"]]
+ 00a9dcf0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dcac bytes 3506f697
+ 00a9dcf0 bytes 2406f697
~~~


<a id="compare-00a6a531488d34d578f06a3aafbca321"></a>

### [`00a9dce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dce8.md) → [`00a9dd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd2c.md) FUN_00a9dd2c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dce8.md#insn-00a9dd04) · [`00a9dd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dce8.md#insn-00a9dd18) · [`00a9dd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dce8.md#insn-00a9dd28)
- 新版 [`00a9dd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd2c.md#insn-00a9dd48) · [`00a9dd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd2c.md#insn-00a9dd5c) · [`00a9dd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd2c.md#insn-00a9dd6c)

~~~diff
- 00a9dd04 ["INT_ADD", "register:40f0:8", ["const:a9dd04:8", "const:4:8"]]
- 00a9dd04 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dd48 ["INT_ADD", "register:40f0:8", ["const:a9dd48:8", "const:4:8"]]
+ 00a9dd48 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dd04 bytes 1f06f697
+ 00a9dd48 bytes 0e06f697
- 00a9dd18 ["INT_ADD", "register:40f0:8", ["const:a9dd18:8", "const:4:8"]]
- 00a9dd18 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9dd5c ["INT_ADD", "register:40f0:8", ["const:a9dd5c:8", "const:4:8"]]
+ 00a9dd5c ["CALL", null, ["callee:005c2710:8"]]
- 00a9dd18 bytes 7e92ec97
+ 00a9dd5c bytes 6d92ec97
- 00a9dd28 ["INT_ADD", "register:40f0:8", ["const:a9dd28:8", "const:4:8"]]
- 00a9dd28 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dd6c ["INT_ADD", "register:40f0:8", ["const:a9dd6c:8", "const:4:8"]]
+ 00a9dd6c ["CALL", null, ["callee:0081f580:8"]]
- 00a9dd28 bytes 1606f697
+ 00a9dd6c bytes 0506f697
~~~


<a id="compare-00e952c8cdd05611574fad1883995b8d"></a>

### [`00a9dd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dd58.md) → [`00a9dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd9c.md) FUN_00a9dd9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dd58.md#insn-00a9dd6c) · [`00a9dd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dd58.md#insn-00a9dd80) · [`00a9dd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dd58.md#insn-00a9dd8c)
- 新版 [`00a9ddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd9c.md#insn-00a9ddb0) · [`00a9ddc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd9c.md#insn-00a9ddc4) · [`00a9ddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dd9c.md#insn-00a9ddd0)

~~~diff
- 00a9dd6c ["INT_ADD", "register:40f0:8", ["const:a9dd6c:8", "const:4:8"]]
- 00a9dd6c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9ddb0 ["INT_ADD", "register:40f0:8", ["const:a9ddb0:8", "const:4:8"]]
+ 00a9ddb0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dd6c bytes 0506f697
+ 00a9ddb0 bytes f405f697
- 00a9dd80 ["INT_ADD", "register:40f0:8", ["const:a9dd80:8", "const:4:8"]]
- 00a9dd80 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9ddc4 ["INT_ADD", "register:40f0:8", ["const:a9ddc4:8", "const:4:8"]]
+ 00a9ddc4 ["CALL", null, ["callee:005c2710:8"]]
- 00a9dd80 bytes 6492ec97
+ 00a9ddc4 bytes 5392ec97
- 00a9dd8c ["INT_ADD", "register:40f0:8", ["const:a9dd8c:8", "const:4:8"]]
- 00a9dd8c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9ddd0 ["INT_ADD", "register:40f0:8", ["const:a9ddd0:8", "const:4:8"]]
+ 00a9ddd0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dd8c bytes fd05f697
+ 00a9ddd0 bytes ec05f697
~~~


<a id="compare-cb36c1f95679d03f9dd152b3a90d3274"></a>

### [`00a9ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9ddc8.md) → [`00a9de0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9de0c.md) FUN_00a9de0c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9ddc8.md#insn-00a9dde4) · [`00a9ddf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9ddc8.md#insn-00a9ddf8) · [`00a9de08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9ddc8.md#insn-00a9de08)
- 新版 [`00a9de28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9de0c.md#insn-00a9de28) · [`00a9de3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9de0c.md#insn-00a9de3c) · [`00a9de4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9de0c.md#insn-00a9de4c)

~~~diff
- 00a9dde4 ["INT_ADD", "register:40f0:8", ["const:a9dde4:8", "const:4:8"]]
- 00a9dde4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9de28 ["INT_ADD", "register:40f0:8", ["const:a9de28:8", "const:4:8"]]
+ 00a9de28 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dde4 bytes e705f697
+ 00a9de28 bytes d605f697
- 00a9ddf8 ["INT_ADD", "register:40f0:8", ["const:a9ddf8:8", "const:4:8"]]
- 00a9ddf8 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9de3c ["INT_ADD", "register:40f0:8", ["const:a9de3c:8", "const:4:8"]]
+ 00a9de3c ["CALL", null, ["callee:005c2710:8"]]
- 00a9ddf8 bytes 4692ec97
+ 00a9de3c bytes 3592ec97
- 00a9de08 ["INT_ADD", "register:40f0:8", ["const:a9de08:8", "const:4:8"]]
- 00a9de08 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9de4c ["INT_ADD", "register:40f0:8", ["const:a9de4c:8", "const:4:8"]]
+ 00a9de4c ["CALL", null, ["callee:0081f580:8"]]
- 00a9de08 bytes de05f697
+ 00a9de4c bytes cd05f697
~~~


<a id="compare-9db1045bce2c644ad1ffeb343895ca17"></a>

### [`00a9de38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9de38.md) → [`00a9de7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9de7c.md) FUN_00a9de7c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9de4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9de38.md#insn-00a9de4c)
- 新版 [`00a9de90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9de7c.md#insn-00a9de90)

~~~diff
- 00a9de4c ["INT_ADD", "register:40f0:8", ["const:a9de4c:8", "const:4:8"]]
- 00a9de4c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9de90 ["INT_ADD", "register:40f0:8", ["const:a9de90:8", "const:4:8"]]
+ 00a9de90 ["CALL", null, ["callee:0081f580:8"]]
- 00a9de4c bytes cd05f697
+ 00a9de90 bytes bc05f697
~~~


<a id="compare-ca932752b15352d459ec8528812043fe"></a>

### [`00a9de78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9de78.md) → [`00a9debc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9debc.md) FUN_00a9debc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9de94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9de78.md#insn-00a9de94)
- 新版 [`00a9ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9debc.md#insn-00a9ded8)

~~~diff
- 00a9de94 ["INT_ADD", "register:40f0:8", ["const:a9de94:8", "const:4:8"]]
- 00a9de94 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9ded8 ["INT_ADD", "register:40f0:8", ["const:a9ded8:8", "const:4:8"]]
+ 00a9ded8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9de94 bytes bb05f697
+ 00a9ded8 bytes aa05f697
~~~


<a id="compare-759e8bc4077db5ccfb817a483361a88e"></a>

### [`00a9dec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dec4.md) → [`00a9df08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9df08.md) FUN_00a9df08

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9ded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dec4.md#insn-00a9ded8)
- 新版 [`00a9df1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9df08.md#insn-00a9df1c)

~~~diff
- 00a9ded8 ["INT_ADD", "register:40f0:8", ["const:a9ded8:8", "const:4:8"]]
- 00a9ded8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9df1c ["INT_ADD", "register:40f0:8", ["const:a9df1c:8", "const:4:8"]]
+ 00a9df1c ["CALL", null, ["callee:0081f580:8"]]
- 00a9ded8 bytes aa05f697
+ 00a9df1c bytes 9905f697
~~~


<a id="compare-aec4b2c9e77e928027256a77c4ef2fee"></a>

### [`00a9df04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9df04.md) → [`00a9df48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9df48.md) FUN_00a9df48

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9df20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9df04.md#insn-00a9df20)
- 新版 [`00a9df64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9df48.md#insn-00a9df64)

~~~diff
- 00a9df20 ["INT_ADD", "register:40f0:8", ["const:a9df20:8", "const:4:8"]]
- 00a9df20 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9df64 ["INT_ADD", "register:40f0:8", ["const:a9df64:8", "const:4:8"]]
+ 00a9df64 ["CALL", null, ["callee:0081f580:8"]]
- 00a9df20 bytes 9805f697
+ 00a9df64 bytes 8705f697
~~~


<a id="compare-c8be3235bff41ca4bc31457f1bf0184b"></a>

### [`00a9df50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9df50.md) → [`00a9df94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9df94.md) FUN_00a9df94

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9df64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9df50.md#insn-00a9df64)
- 新版 [`00a9dfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9df94.md#insn-00a9dfa8)

~~~diff
- 00a9df64 ["INT_ADD", "register:40f0:8", ["const:a9df64:8", "const:4:8"]]
- 00a9df64 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dfa8 ["INT_ADD", "register:40f0:8", ["const:a9dfa8:8", "const:4:8"]]
+ 00a9dfa8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9df64 bytes 8705f697
+ 00a9dfa8 bytes 7605f697
~~~


<a id="compare-5f5c5491b342efa3e5eb44f6e362305a"></a>

### [`00a9df90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9df90.md) → [`00a9dfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dfd4.md) FUN_00a9dfd4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dfac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9df90.md#insn-00a9dfac)
- 新版 [`00a9dff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9dfd4.md#insn-00a9dff0)

~~~diff
- 00a9dfac ["INT_ADD", "register:40f0:8", ["const:a9dfac:8", "const:4:8"]]
- 00a9dfac ["CALL", null, ["callee:0081f580:8"]]
+ 00a9dff0 ["INT_ADD", "register:40f0:8", ["const:a9dff0:8", "const:4:8"]]
+ 00a9dff0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dfac bytes 7505f697
+ 00a9dff0 bytes 6405f697
~~~


<a id="compare-d0d7fa29de4df74503b7e7165e4e7f33"></a>

### [`00a9dfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dfdc.md) → [`00a9e020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e020.md) FUN_00a9e020

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dfdc.md#insn-00a9dff0)
- 新版 [`00a9e034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e020.md#insn-00a9e034)

~~~diff
- 00a9dff0 ["INT_ADD", "register:40f0:8", ["const:a9dff0:8", "const:4:8"]]
- 00a9dff0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e034 ["INT_ADD", "register:40f0:8", ["const:a9e034:8", "const:4:8"]]
+ 00a9e034 ["CALL", null, ["callee:0081f580:8"]]
- 00a9dff0 bytes 6405f697
+ 00a9e034 bytes 5305f697
~~~


<a id="compare-8bb0ccad7ac74af444a07c57acd240e2"></a>

### [`00a9e01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e01c.md) → [`00a9e060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e060.md) FUN_00a9e060

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e01c.md#insn-00a9e038)
- 新版 [`00a9e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e060.md#insn-00a9e07c)

~~~diff
- 00a9e038 ["INT_ADD", "register:40f0:8", ["const:a9e038:8", "const:4:8"]]
- 00a9e038 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e07c ["INT_ADD", "register:40f0:8", ["const:a9e07c:8", "const:4:8"]]
+ 00a9e07c ["CALL", null, ["callee:0081f580:8"]]
- 00a9e038 bytes 5205f697
+ 00a9e07c bytes 4105f697
~~~


<a id="compare-d94c535ffabbead9fad48cd50f9600ec"></a>

### [`00a9e068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e068.md) → [`00a9e0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e0ac.md) FUN_00a9e0ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e068.md#insn-00a9e07c)
- 新版 [`00a9e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e0ac.md#insn-00a9e0c0)

~~~diff
- 00a9e07c ["INT_ADD", "register:40f0:8", ["const:a9e07c:8", "const:4:8"]]
- 00a9e07c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e0c0 ["INT_ADD", "register:40f0:8", ["const:a9e0c0:8", "const:4:8"]]
+ 00a9e0c0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e07c bytes 4105f697
+ 00a9e0c0 bytes 3005f697
~~~


<a id="compare-f07be69b714fbe4e9d668a4fb58c6fe9"></a>

### [`00a9e0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e0a8.md) → [`00a9e0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e0ec.md) FUN_00a9e0ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e0a8.md#insn-00a9e0c4)
- 新版 [`00a9e108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e0ec.md#insn-00a9e108)

~~~diff
- 00a9e0c4 ["INT_ADD", "register:40f0:8", ["const:a9e0c4:8", "const:4:8"]]
- 00a9e0c4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e108 ["INT_ADD", "register:40f0:8", ["const:a9e108:8", "const:4:8"]]
+ 00a9e108 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e0c4 bytes 2f05f697
+ 00a9e108 bytes 1e05f697
~~~


<a id="compare-d7298f5dff0709fcda01a61af826e297"></a>

### [`00a9e0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e0f4.md) → [`00a9e138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e138.md) FUN_00a9e138

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e0f4.md#insn-00a9e108)
- 新版 [`00a9e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e138.md#insn-00a9e14c)

~~~diff
- 00a9e108 ["INT_ADD", "register:40f0:8", ["const:a9e108:8", "const:4:8"]]
- 00a9e108 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e14c ["INT_ADD", "register:40f0:8", ["const:a9e14c:8", "const:4:8"]]
+ 00a9e14c ["CALL", null, ["callee:0081f580:8"]]
- 00a9e108 bytes 1e05f697
+ 00a9e14c bytes 0d05f697
~~~


<a id="compare-62d589f2a56a145795954b101cd35c40"></a>

### [`00a9e134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e134.md) → [`00a9e178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e178.md) FUN_00a9e178

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e134.md#insn-00a9e150)
- 新版 [`00a9e194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e178.md#insn-00a9e194)

~~~diff
- 00a9e150 ["INT_ADD", "register:40f0:8", ["const:a9e150:8", "const:4:8"]]
- 00a9e150 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e194 ["INT_ADD", "register:40f0:8", ["const:a9e194:8", "const:4:8"]]
+ 00a9e194 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e150 bytes 0c05f697
+ 00a9e194 bytes fb04f697
~~~


<a id="compare-ee96208421ee5beff566cf829e29f6d8"></a>

### [`00a9e180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e180.md) → [`00a9e1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e1c4.md) FUN_00a9e1c4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e180.md#insn-00a9e194)
- 新版 [`00a9e1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e1c4.md#insn-00a9e1d8)

~~~diff
- 00a9e194 ["INT_ADD", "register:40f0:8", ["const:a9e194:8", "const:4:8"]]
- 00a9e194 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e1d8 ["INT_ADD", "register:40f0:8", ["const:a9e1d8:8", "const:4:8"]]
+ 00a9e1d8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e194 bytes fb04f697
+ 00a9e1d8 bytes ea04f697
~~~


<a id="compare-2ad0c80dc4f4d0bbabfa8c41556cfff5"></a>

### [`00a9e1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e1c0.md) → [`00a9e204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e204.md) FUN_00a9e204

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e1c0.md#insn-00a9e1dc)
- 新版 [`00a9e220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e204.md#insn-00a9e220)

~~~diff
- 00a9e1dc ["INT_ADD", "register:40f0:8", ["const:a9e1dc:8", "const:4:8"]]
- 00a9e1dc ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e220 ["INT_ADD", "register:40f0:8", ["const:a9e220:8", "const:4:8"]]
+ 00a9e220 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e1dc bytes e904f697
+ 00a9e220 bytes d804f697
~~~


<a id="compare-f54a42fb6d4b18dee143788729a70a63"></a>

### [`00a9e20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e20c.md) → [`00a9e250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e250.md) FUN_00a9e250

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e20c.md#insn-00a9e220)
- 新版 [`00a9e264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e250.md#insn-00a9e264)

~~~diff
- 00a9e220 ["INT_ADD", "register:40f0:8", ["const:a9e220:8", "const:4:8"]]
- 00a9e220 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e264 ["INT_ADD", "register:40f0:8", ["const:a9e264:8", "const:4:8"]]
+ 00a9e264 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e220 bytes d804f697
+ 00a9e264 bytes c704f697
~~~


<a id="compare-2057a2ea9a08562997a84e4f86f3c2d0"></a>

### [`00a9e24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e24c.md) → [`00a9e290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e290.md) FUN_00a9e290

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e24c.md#insn-00a9e268)
- 新版 [`00a9e2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e290.md#insn-00a9e2ac)

~~~diff
- 00a9e268 ["INT_ADD", "register:40f0:8", ["const:a9e268:8", "const:4:8"]]
- 00a9e268 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e2ac ["INT_ADD", "register:40f0:8", ["const:a9e2ac:8", "const:4:8"]]
+ 00a9e2ac ["CALL", null, ["callee:0081f580:8"]]
- 00a9e268 bytes c604f697
+ 00a9e2ac bytes b504f697
~~~


<a id="compare-600dd377d1a36fc1d8cbeb8cbac6034f"></a>

### [`00a9e298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e298.md) → [`00a9e2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e2dc.md) FUN_00a9e2dc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e298.md#insn-00a9e2ac)
- 新版 [`00a9e2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e2dc.md#insn-00a9e2f0)

~~~diff
- 00a9e2ac ["INT_ADD", "register:40f0:8", ["const:a9e2ac:8", "const:4:8"]]
- 00a9e2ac ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e2f0 ["INT_ADD", "register:40f0:8", ["const:a9e2f0:8", "const:4:8"]]
+ 00a9e2f0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e2ac bytes b504f697
+ 00a9e2f0 bytes a404f697
~~~


<a id="compare-3081a16fe4d735d32eb1c9ab8c1f9184"></a>

### [`00a9e2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e2d8.md) → [`00a9e31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e31c.md) FUN_00a9e31c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e2d8.md#insn-00a9e2f4)
- 新版 [`00a9e338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e31c.md#insn-00a9e338)

~~~diff
- 00a9e2f4 ["INT_ADD", "register:40f0:8", ["const:a9e2f4:8", "const:4:8"]]
- 00a9e2f4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e338 ["INT_ADD", "register:40f0:8", ["const:a9e338:8", "const:4:8"]]
+ 00a9e338 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e2f4 bytes a304f697
+ 00a9e338 bytes 9204f697
~~~


<a id="compare-7dc33471847df152284824e3dde73144"></a>

### [`00a9e324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e324.md) → [`00a9e368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e368.md) FUN_00a9e368

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e324.md#insn-00a9e338)
- 新版 [`00a9e37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e368.md#insn-00a9e37c)

~~~diff
- 00a9e338 ["INT_ADD", "register:40f0:8", ["const:a9e338:8", "const:4:8"]]
- 00a9e338 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e37c ["INT_ADD", "register:40f0:8", ["const:a9e37c:8", "const:4:8"]]
+ 00a9e37c ["CALL", null, ["callee:0081f580:8"]]
- 00a9e338 bytes 9204f697
+ 00a9e37c bytes 8104f697
~~~


<a id="compare-95a07158aa8f8b9f31049dc041b399b4"></a>

### [`00a9e364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e364.md) → [`00a9e3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e3a8.md) FUN_00a9e3a8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e364.md#insn-00a9e380)
- 新版 [`00a9e3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e3a8.md#insn-00a9e3c4)

~~~diff
- 00a9e380 ["INT_ADD", "register:40f0:8", ["const:a9e380:8", "const:4:8"]]
- 00a9e380 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e3c4 ["INT_ADD", "register:40f0:8", ["const:a9e3c4:8", "const:4:8"]]
+ 00a9e3c4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e380 bytes 8004f697
+ 00a9e3c4 bytes 6f04f697
~~~


<a id="compare-085de82612a00c4ccab474f2afddf0e9"></a>

### [`00a9e3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e3b0.md) → [`00a9e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e3f4.md) FUN_00a9e3f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e3b0.md#insn-00a9e3c4)
- 新版 [`00a9e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e3f4.md#insn-00a9e408)

~~~diff
- 00a9e3c4 ["INT_ADD", "register:40f0:8", ["const:a9e3c4:8", "const:4:8"]]
- 00a9e3c4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e408 ["INT_ADD", "register:40f0:8", ["const:a9e408:8", "const:4:8"]]
+ 00a9e408 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e3c4 bytes 6f04f697
+ 00a9e408 bytes 5e04f697
~~~


<a id="compare-3c5d926aa76b30f9615639dc5487101b"></a>

### [`00a9e3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e3f0.md) → [`00a9e434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e434.md) FUN_00a9e434

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e3f0.md#insn-00a9e40c)
- 新版 [`00a9e450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e434.md#insn-00a9e450)

~~~diff
- 00a9e40c ["INT_ADD", "register:40f0:8", ["const:a9e40c:8", "const:4:8"]]
- 00a9e40c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e450 ["INT_ADD", "register:40f0:8", ["const:a9e450:8", "const:4:8"]]
+ 00a9e450 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e40c bytes 5d04f697
+ 00a9e450 bytes 4c04f697
~~~


<a id="compare-fdff8f67fdc2d2c845b05647fbd9e232"></a>

### [`00a9e43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e43c.md) → [`00a9e480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e480.md) FUN_00a9e480

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e43c.md#insn-00a9e450)
- 新版 [`00a9e494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e480.md#insn-00a9e494)

~~~diff
- 00a9e450 ["INT_ADD", "register:40f0:8", ["const:a9e450:8", "const:4:8"]]
- 00a9e450 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e494 ["INT_ADD", "register:40f0:8", ["const:a9e494:8", "const:4:8"]]
+ 00a9e494 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e450 bytes 4c04f697
+ 00a9e494 bytes 3b04f697
~~~


<a id="compare-2d23715f1550aaf6c33c2c9468592814"></a>

### [`00a9e47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e47c.md) → [`00a9e4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e4c0.md) FUN_00a9e4c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e47c.md#insn-00a9e498)
- 新版 [`00a9e4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e4c0.md#insn-00a9e4dc)

~~~diff
- 00a9e498 ["INT_ADD", "register:40f0:8", ["const:a9e498:8", "const:4:8"]]
- 00a9e498 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e4dc ["INT_ADD", "register:40f0:8", ["const:a9e4dc:8", "const:4:8"]]
+ 00a9e4dc ["CALL", null, ["callee:0081f580:8"]]
- 00a9e498 bytes 3a04f697
+ 00a9e4dc bytes 2904f697
~~~


<a id="compare-6950bee7609d385a295540114707ea20"></a>

### [`00a9e4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e4c8.md) → [`00a9e50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e50c.md) FUN_00a9e50c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e4dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e4c8.md#insn-00a9e4dc)
- 新版 [`00a9e520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e50c.md#insn-00a9e520)

~~~diff
- 00a9e4dc ["INT_ADD", "register:40f0:8", ["const:a9e4dc:8", "const:4:8"]]
- 00a9e4dc ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e520 ["INT_ADD", "register:40f0:8", ["const:a9e520:8", "const:4:8"]]
+ 00a9e520 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e4dc bytes 2904f697
+ 00a9e520 bytes 1804f697
~~~


<a id="compare-66de2aede4fb0a151f2dd5544588aead"></a>

### [`00a9e508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e508.md) → [`00a9e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e54c.md) FUN_00a9e54c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e508.md#insn-00a9e524)
- 新版 [`00a9e568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e54c.md#insn-00a9e568)

~~~diff
- 00a9e524 ["INT_ADD", "register:40f0:8", ["const:a9e524:8", "const:4:8"]]
- 00a9e524 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e568 ["INT_ADD", "register:40f0:8", ["const:a9e568:8", "const:4:8"]]
+ 00a9e568 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e524 bytes 1704f697
+ 00a9e568 bytes 0604f697
~~~


<a id="compare-605ea8362fac13937a6e48d8388c9b42"></a>

### [`00a9e554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e554.md) → [`00a9e598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e598.md) FUN_00a9e598

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e554.md#insn-00a9e568)
- 新版 [`00a9e5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e598.md#insn-00a9e5ac)

~~~diff
- 00a9e568 ["INT_ADD", "register:40f0:8", ["const:a9e568:8", "const:4:8"]]
- 00a9e568 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e5ac ["INT_ADD", "register:40f0:8", ["const:a9e5ac:8", "const:4:8"]]
+ 00a9e5ac ["CALL", null, ["callee:0081f580:8"]]
- 00a9e568 bytes 0604f697
+ 00a9e5ac bytes f503f697
~~~


<a id="compare-1435a92acf3916be3b95033feab48121"></a>

### [`00a9e594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e594.md) → [`00a9e5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e5d8.md) FUN_00a9e5d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e594.md#insn-00a9e5b0)
- 新版 [`00a9e5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e5d8.md#insn-00a9e5f4)

~~~diff
- 00a9e5b0 ["INT_ADD", "register:40f0:8", ["const:a9e5b0:8", "const:4:8"]]
- 00a9e5b0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e5f4 ["INT_ADD", "register:40f0:8", ["const:a9e5f4:8", "const:4:8"]]
+ 00a9e5f4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e5b0 bytes f403f697
+ 00a9e5f4 bytes e303f697
~~~


<a id="compare-74214b1e0fbbc7d131118cc8cb4baad4"></a>

### [`00a9e5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e5e0.md) → [`00a9e624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e624.md) FUN_00a9e624

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e5e0.md#insn-00a9e5f4)
- 新版 [`00a9e638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e624.md#insn-00a9e638)

~~~diff
- 00a9e5f4 ["INT_ADD", "register:40f0:8", ["const:a9e5f4:8", "const:4:8"]]
- 00a9e5f4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e638 ["INT_ADD", "register:40f0:8", ["const:a9e638:8", "const:4:8"]]
+ 00a9e638 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e5f4 bytes e303f697
+ 00a9e638 bytes d203f697
~~~


<a id="compare-3ea7a0d5969149b76a2cff904a9d00eb"></a>

### [`00a9e620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e620.md) → [`00a9e664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e664.md) FUN_00a9e664

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9e63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e620.md#insn-00a9e63c)
- 新版 [`00a9e680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e664.md#insn-00a9e680)

~~~diff
- 00a9e63c ["INT_ADD", "register:40f0:8", ["const:a9e63c:8", "const:4:8"]]
- 00a9e63c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9e680 ["INT_ADD", "register:40f0:8", ["const:a9e680:8", "const:4:8"]]
+ 00a9e680 ["CALL", null, ["callee:0081f580:8"]]
- 00a9e63c bytes d103f697
+ 00a9e680 bytes c003f697
~~~


<a id="compare-04602289c25c1f819fbab330eb8686a7"></a>

### [`00a9f8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f8f8.md) → [`00a9f93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f93c.md) FUN_00a9f93c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9f90c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f8f8.md#insn-00a9f90c) · [`00a9f920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f8f8.md#insn-00a9f920) · [`00a9f928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f8f8.md#insn-00a9f928)
- 新版 [`00a9f950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f93c.md#insn-00a9f950) · [`00a9f964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f93c.md#insn-00a9f964) · [`00a9f96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f93c.md#insn-00a9f96c)

~~~diff
- 00a9f90c ["INT_ADD", "register:40f0:8", ["const:a9f90c:8", "const:4:8"]]
- 00a9f90c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9f950 ["INT_ADD", "register:40f0:8", ["const:a9f950:8", "const:4:8"]]
+ 00a9f950 ["CALL", null, ["callee:0081f580:8"]]
- 00a9f90c bytes 1dfff597
+ 00a9f950 bytes 0cfff597
- 00a9f920 ["INT_ADD", "register:40f0:8", ["const:a9f920:8", "const:4:8"]]
- 00a9f920 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9f964 ["INT_ADD", "register:40f0:8", ["const:a9f964:8", "const:4:8"]]
+ 00a9f964 ["CALL", null, ["callee:005c2710:8"]]
- 00a9f920 bytes 7c8bec97
+ 00a9f964 bytes 6b8bec97
- 00a9f928 ["INT_ADD", "register:40f0:8", ["const:a9f928:8", "const:4:8"]]
- 00a9f928 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9f96c ["INT_ADD", "register:40f0:8", ["const:a9f96c:8", "const:4:8"]]
+ 00a9f96c ["CALL", null, ["callee:0081f580:8"]]
- 00a9f928 bytes 16fff597
+ 00a9f96c bytes 05fff597
~~~


<a id="compare-7d467416536bbff5d88c603361f32486"></a>

### [`00aa19d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa19d4.md) → [`00aa1a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1a18.md) FUN_00aa1a18

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa19f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa19d4.md#insn-00aa19f0) · [`00aa1a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa19d4.md#insn-00aa1a04) · [`00aa1a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa19d4.md#insn-00aa1a14)
- 新版 [`00aa1a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1a18.md#insn-00aa1a34) · [`00aa1a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1a18.md#insn-00aa1a48) · [`00aa1a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1a18.md#insn-00aa1a58)

~~~diff
- 00aa19f0 ["INT_ADD", "register:40f0:8", ["const:aa19f0:8", "const:4:8"]]
- 00aa19f0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1a34 ["INT_ADD", "register:40f0:8", ["const:aa1a34:8", "const:4:8"]]
+ 00aa1a34 ["CALL", null, ["callee:0081f580:8"]]
- 00aa19f0 bytes e4f6f597
+ 00aa1a34 bytes d3f6f597
- 00aa1a04 ["INT_ADD", "register:40f0:8", ["const:aa1a04:8", "const:4:8"]]
- 00aa1a04 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1a48 ["INT_ADD", "register:40f0:8", ["const:aa1a48:8", "const:4:8"]]
+ 00aa1a48 ["CALL", null, ["callee:005c2710:8"]]
- 00aa1a04 bytes 4383ec97
+ 00aa1a48 bytes 3283ec97
- 00aa1a14 ["INT_ADD", "register:40f0:8", ["const:aa1a14:8", "const:4:8"]]
- 00aa1a14 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1a58 ["INT_ADD", "register:40f0:8", ["const:aa1a58:8", "const:4:8"]]
+ 00aa1a58 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1a14 bytes dbf6f597
+ 00aa1a58 bytes caf6f597
~~~


<a id="compare-3c6d4106c22be3d6d0f67beafa0d18e2"></a>

### [`00aa1b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1b90.md) → [`00aa1bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1bd4.md) FUN_00aa1bd4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa1bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1b90.md#insn-00aa1bac) · [`00aa1bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1b90.md#insn-00aa1bc0) · [`00aa1bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1b90.md#insn-00aa1bd0)
- 新版 [`00aa1bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1bd4.md#insn-00aa1bf0) · [`00aa1c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1bd4.md#insn-00aa1c04) · [`00aa1c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1bd4.md#insn-00aa1c14)

~~~diff
- 00aa1bac ["INT_ADD", "register:40f0:8", ["const:aa1bac:8", "const:4:8"]]
- 00aa1bac ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1bf0 ["INT_ADD", "register:40f0:8", ["const:aa1bf0:8", "const:4:8"]]
+ 00aa1bf0 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1bac bytes 75f6f597
+ 00aa1bf0 bytes 64f6f597
- 00aa1bc0 ["INT_ADD", "register:40f0:8", ["const:aa1bc0:8", "const:4:8"]]
- 00aa1bc0 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1c04 ["INT_ADD", "register:40f0:8", ["const:aa1c04:8", "const:4:8"]]
+ 00aa1c04 ["CALL", null, ["callee:005c2710:8"]]
- 00aa1bc0 bytes d482ec97
+ 00aa1c04 bytes c382ec97
- 00aa1bd0 ["INT_ADD", "register:40f0:8", ["const:aa1bd0:8", "const:4:8"]]
- 00aa1bd0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1c14 ["INT_ADD", "register:40f0:8", ["const:aa1c14:8", "const:4:8"]]
+ 00aa1c14 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1bd0 bytes 6cf6f597
+ 00aa1c14 bytes 5bf6f597
~~~


<a id="compare-06a90ea3339392e518292991ac83bb77"></a>

### [`00aa1ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1ed8.md) → [`00aa1f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1f1c.md) FUN_00aa1f1c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa1ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1ed8.md#insn-00aa1ef4) · [`00aa1f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1ed8.md#insn-00aa1f08) · [`00aa1f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1ed8.md#insn-00aa1f10)
- 新版 [`00aa1f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1f1c.md#insn-00aa1f38) · [`00aa1f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1f1c.md#insn-00aa1f4c) · [`00aa1f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1f1c.md#insn-00aa1f54)

~~~diff
- 00aa1ef4 ["INT_ADD", "register:40f0:8", ["const:aa1ef4:8", "const:4:8"]]
- 00aa1ef4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1f38 ["INT_ADD", "register:40f0:8", ["const:aa1f38:8", "const:4:8"]]
+ 00aa1f38 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1ef4 bytes a3f5f597
+ 00aa1f38 bytes 92f5f597
- 00aa1f08 ["INT_ADD", "register:40f0:8", ["const:aa1f08:8", "const:4:8"]]
- 00aa1f08 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1f4c ["INT_ADD", "register:40f0:8", ["const:aa1f4c:8", "const:4:8"]]
+ 00aa1f4c ["CALL", null, ["callee:005c2710:8"]]
- 00aa1f08 bytes 0282ec97
+ 00aa1f4c bytes f181ec97
- 00aa1f10 ["INT_ADD", "register:40f0:8", ["const:aa1f10:8", "const:4:8"]]
- 00aa1f10 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1f54 ["INT_ADD", "register:40f0:8", ["const:aa1f54:8", "const:4:8"]]
+ 00aa1f54 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1f10 bytes 9cf5f597
+ 00aa1f54 bytes 8bf5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbba4b936dbc29b008dc5fb5d6363c08"></a>

### [`00aa2a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2a54.md) → [`00aa2a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2a98.md) FUN_00aa2a98

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa2a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2a54.md#insn-00aa2a70) · [`00aa2a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2a54.md#insn-00aa2a84) · [`00aa2a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2a54.md#insn-00aa2a94)
- 新版 [`00aa2ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2a98.md#insn-00aa2ab4) · [`00aa2ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2a98.md#insn-00aa2ac8) · [`00aa2ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2a98.md#insn-00aa2ad8)

~~~diff
- 00aa2a70 ["INT_ADD", "register:40f0:8", ["const:aa2a70:8", "const:4:8"]]
- 00aa2a70 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa2ab4 ["INT_ADD", "register:40f0:8", ["const:aa2ab4:8", "const:4:8"]]
+ 00aa2ab4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2a70 bytes c4f2f597
+ 00aa2ab4 bytes b3f2f597
- 00aa2a84 ["INT_ADD", "register:40f0:8", ["const:aa2a84:8", "const:4:8"]]
- 00aa2a84 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa2ac8 ["INT_ADD", "register:40f0:8", ["const:aa2ac8:8", "const:4:8"]]
+ 00aa2ac8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa2a84 bytes 237fec97
+ 00aa2ac8 bytes 127fec97
- 00aa2a94 ["INT_ADD", "register:40f0:8", ["const:aa2a94:8", "const:4:8"]]
- 00aa2a94 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa2ad8 ["INT_ADD", "register:40f0:8", ["const:aa2ad8:8", "const:4:8"]]
+ 00aa2ad8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2a94 bytes bbf2f597
+ 00aa2ad8 bytes aaf2f597
~~~


<a id="compare-005a4ca91aa2ba92b3e8be070fe44a19"></a>

### [`00aa2fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2fb8.md) → [`00aa2ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2ffc.md) FUN_00aa2ffc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa2fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2fb8.md#insn-00aa2fd4) · [`00aa2fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2fb8.md#insn-00aa2fe8) · [`00aa2ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2fb8.md#insn-00aa2ff8)
- 新版 [`00aa3018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2ffc.md#insn-00aa3018) · [`00aa302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2ffc.md#insn-00aa302c) · [`00aa303c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2ffc.md#insn-00aa303c)

~~~diff
- 00aa2fd4 ["INT_ADD", "register:40f0:8", ["const:aa2fd4:8", "const:4:8"]]
- 00aa2fd4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa3018 ["INT_ADD", "register:40f0:8", ["const:aa3018:8", "const:4:8"]]
+ 00aa3018 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2fd4 bytes 6bf1f597
+ 00aa3018 bytes 5af1f597
- 00aa2fe8 ["INT_ADD", "register:40f0:8", ["const:aa2fe8:8", "const:4:8"]]
- 00aa2fe8 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa302c ["INT_ADD", "register:40f0:8", ["const:aa302c:8", "const:4:8"]]
+ 00aa302c ["CALL", null, ["callee:005c2710:8"]]
- 00aa2fe8 bytes ca7dec97
+ 00aa302c bytes b97dec97
- 00aa2ff8 ["INT_ADD", "register:40f0:8", ["const:aa2ff8:8", "const:4:8"]]
- 00aa2ff8 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa303c ["INT_ADD", "register:40f0:8", ["const:aa303c:8", "const:4:8"]]
+ 00aa303c ["CALL", null, ["callee:0081f580:8"]]
- 00aa2ff8 bytes 62f1f597
+ 00aa303c bytes 51f1f597
~~~


<a id="compare-b1631e9e1b8b38bb7191ea00cde7861e"></a>

### [`00aa3030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3030.md) → [`00aa3074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3074.md) FUN_00aa3074

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa304c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3030.md#insn-00aa304c) · [`00aa3060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3030.md#insn-00aa3060) · [`00aa3070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3030.md#insn-00aa3070)
- 新版 [`00aa3090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3074.md#insn-00aa3090) · [`00aa30a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3074.md#insn-00aa30a4) · [`00aa30b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3074.md#insn-00aa30b4)

~~~diff
- 00aa304c ["INT_ADD", "register:40f0:8", ["const:aa304c:8", "const:4:8"]]
- 00aa304c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa3090 ["INT_ADD", "register:40f0:8", ["const:aa3090:8", "const:4:8"]]
+ 00aa3090 ["CALL", null, ["callee:0081f580:8"]]
- 00aa304c bytes 4df1f597
+ 00aa3090 bytes 3cf1f597
- 00aa3060 ["INT_ADD", "register:40f0:8", ["const:aa3060:8", "const:4:8"]]
- 00aa3060 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa30a4 ["INT_ADD", "register:40f0:8", ["const:aa30a4:8", "const:4:8"]]
+ 00aa30a4 ["CALL", null, ["callee:005c2710:8"]]
- 00aa3060 bytes ac7dec97
+ 00aa30a4 bytes 9b7dec97
- 00aa3070 ["INT_ADD", "register:40f0:8", ["const:aa3070:8", "const:4:8"]]
- 00aa3070 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa30b4 ["INT_ADD", "register:40f0:8", ["const:aa30b4:8", "const:4:8"]]
+ 00aa30b4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa3070 bytes 44f1f597
+ 00aa30b4 bytes 33f1f597
~~~


<a id="compare-5eeeedb09b1b04acf85a992c31ba863b"></a>

### [`00aa410c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa410c.md) → [`00aa4150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4150.md) FUN_00aa4150

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa410c.md#insn-00aa4120) · [`00aa4134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa410c.md#insn-00aa4134) · [`00aa413c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa410c.md#insn-00aa413c)
- 新版 [`00aa4164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4150.md#insn-00aa4164) · [`00aa4178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4150.md#insn-00aa4178) · [`00aa4180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4150.md#insn-00aa4180)

~~~diff
- 00aa4120 ["INT_ADD", "register:40f0:8", ["const:aa4120:8", "const:4:8"]]
- 00aa4120 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4164 ["INT_ADD", "register:40f0:8", ["const:aa4164:8", "const:4:8"]]
+ 00aa4164 ["CALL", null, ["callee:0081f580:8"]]
- 00aa4120 bytes 18edf597
+ 00aa4164 bytes 07edf597
- 00aa4134 ["INT_ADD", "register:40f0:8", ["const:aa4134:8", "const:4:8"]]
- 00aa4134 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa4178 ["INT_ADD", "register:40f0:8", ["const:aa4178:8", "const:4:8"]]
+ 00aa4178 ["CALL", null, ["callee:005c2710:8"]]
- 00aa4134 bytes 7779ec97
+ 00aa4178 bytes 6679ec97
- 00aa413c ["INT_ADD", "register:40f0:8", ["const:aa413c:8", "const:4:8"]]
- 00aa413c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4180 ["INT_ADD", "register:40f0:8", ["const:aa4180:8", "const:4:8"]]
+ 00aa4180 ["CALL", null, ["callee:0081f580:8"]]
- 00aa413c bytes 11edf597
+ 00aa4180 bytes 00edf597
~~~


<a id="compare-337237d409ad3ee751ead5fe2b5d768b"></a>

### [`00aa5d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d20.md) → [`00aa5d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5d64.md) FUN_00aa5d64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa5d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d20.md#insn-00aa5d34) · [`00aa5d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d20.md#insn-00aa5d48) · [`00aa5d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d20.md#insn-00aa5d50)
- 新版 [`00aa5d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5d64.md#insn-00aa5d78) · [`00aa5d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5d64.md#insn-00aa5d8c) · [`00aa5d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5d64.md#insn-00aa5d94)

~~~diff
- 00aa5d34 ["INT_ADD", "register:40f0:8", ["const:aa5d34:8", "const:4:8"]]
- 00aa5d34 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa5d78 ["INT_ADD", "register:40f0:8", ["const:aa5d78:8", "const:4:8"]]
+ 00aa5d78 ["CALL", null, ["callee:0081f580:8"]]
- 00aa5d34 bytes 13e6f597
+ 00aa5d78 bytes 02e6f597
- 00aa5d48 ["INT_ADD", "register:40f0:8", ["const:aa5d48:8", "const:4:8"]]
- 00aa5d48 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa5d8c ["INT_ADD", "register:40f0:8", ["const:aa5d8c:8", "const:4:8"]]
+ 00aa5d8c ["CALL", null, ["callee:005c2710:8"]]
- 00aa5d48 bytes 7272ec97
+ 00aa5d8c bytes 6172ec97
- 00aa5d50 ["INT_ADD", "register:40f0:8", ["const:aa5d50:8", "const:4:8"]]
- 00aa5d50 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa5d94 ["INT_ADD", "register:40f0:8", ["const:aa5d94:8", "const:4:8"]]
+ 00aa5d94 ["CALL", null, ["callee:0081f580:8"]]
- 00aa5d50 bytes 0ce6f597
+ 00aa5d94 bytes fbe5f597
~~~


<a id="compare-4a17b67cfccde81c30e92e0182212b3f"></a>

### [`00aa5f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5f84.md) → [`00aa5fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5fc8.md) FUN_00aa5fc8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005d0a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d0/005d0a68.md) [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 4件 [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa5fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5f84.md#insn-00aa5fa0) · [`00aa5fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5f84.md#insn-00aa5fb4) · [`00aa5fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5f84.md#insn-00aa5fc4)
- 新版 [`00aa5fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5fc8.md#insn-00aa5fe4) · [`00aa5ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5fc8.md#insn-00aa5ff8) · [`00aa6008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5fc8.md#insn-00aa6008)

~~~diff
- 00aa5fa0 ["INT_ADD", "register:40f0:8", ["const:aa5fa0:8", "const:4:8"]]
- 00aa5fa0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa5fe4 ["INT_ADD", "register:40f0:8", ["const:aa5fe4:8", "const:4:8"]]
+ 00aa5fe4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa5fa0 bytes 78e5f597
+ 00aa5fe4 bytes 67e5f597
- 00aa5fb4 ["INT_ADD", "register:40f0:8", ["const:aa5fb4:8", "const:4:8"]]
- 00aa5fb4 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa5ff8 ["INT_ADD", "register:40f0:8", ["const:aa5ff8:8", "const:4:8"]]
+ 00aa5ff8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa5fb4 bytes d771ec97
+ 00aa5ff8 bytes c671ec97
- 00aa5fc4 ["INT_ADD", "register:40f0:8", ["const:aa5fc4:8", "const:4:8"]]
- 00aa5fc4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6008 ["INT_ADD", "register:40f0:8", ["const:aa6008:8", "const:4:8"]]
+ 00aa6008 ["CALL", null, ["callee:0081f580:8"]]
- 00aa5fc4 bytes 6fe5f597
+ 00aa6008 bytes 5ee5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-826ae9d909edf7b0d9f57e30ebcce035"></a>

### [`00aa6010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6010.md) → [`00aa6054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6054.md) FUN_00aa6054

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 5件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`006440f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00644/006440f0.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 5件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`006440f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/006440f0.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa602c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6010.md#insn-00aa602c) · [`00aa6040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6010.md#insn-00aa6040) · [`00aa6048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6010.md#insn-00aa6048)
- 新版 [`00aa6070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6054.md#insn-00aa6070) · [`00aa6084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6054.md#insn-00aa6084) · [`00aa608c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6054.md#insn-00aa608c)

~~~diff
- 00aa602c ["INT_ADD", "register:40f0:8", ["const:aa602c:8", "const:4:8"]]
- 00aa602c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6070 ["INT_ADD", "register:40f0:8", ["const:aa6070:8", "const:4:8"]]
+ 00aa6070 ["CALL", null, ["callee:0081f580:8"]]
- 00aa602c bytes 55e5f597
+ 00aa6070 bytes 44e5f597
- 00aa6040 ["INT_ADD", "register:40f0:8", ["const:aa6040:8", "const:4:8"]]
- 00aa6040 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa6084 ["INT_ADD", "register:40f0:8", ["const:aa6084:8", "const:4:8"]]
+ 00aa6084 ["CALL", null, ["callee:005c2710:8"]]
- 00aa6040 bytes b471ec97
+ 00aa6084 bytes a371ec97
- 00aa6048 ["INT_ADD", "register:40f0:8", ["const:aa6048:8", "const:4:8"]]
- 00aa6048 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa608c ["INT_ADD", "register:40f0:8", ["const:aa608c:8", "const:4:8"]]
+ 00aa608c ["CALL", null, ["callee:0081f580:8"]]
- 00aa6048 bytes 4ee5f597
+ 00aa608c bytes 3de5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bc42b5bfa04ff6ca73feb7cba05f9b2"></a>

### [`00aa65c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa65c8.md) → [`00aa660c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa660c.md) FUN_00aa660c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa65e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa65c8.md#insn-00aa65e4) · [`00aa65f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa65c8.md#insn-00aa65f8) · [`00aa6608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa65c8.md#insn-00aa6608)
- 新版 [`00aa6628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa660c.md#insn-00aa6628) · [`00aa663c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa660c.md#insn-00aa663c) · [`00aa664c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa660c.md#insn-00aa664c)

~~~diff
- 00aa65e4 ["INT_ADD", "register:40f0:8", ["const:aa65e4:8", "const:4:8"]]
- 00aa65e4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6628 ["INT_ADD", "register:40f0:8", ["const:aa6628:8", "const:4:8"]]
+ 00aa6628 ["CALL", null, ["callee:0081f580:8"]]
- 00aa65e4 bytes e7e3f597
+ 00aa6628 bytes d6e3f597
- 00aa65f8 ["INT_ADD", "register:40f0:8", ["const:aa65f8:8", "const:4:8"]]
- 00aa65f8 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa663c ["INT_ADD", "register:40f0:8", ["const:aa663c:8", "const:4:8"]]
+ 00aa663c ["CALL", null, ["callee:005c2710:8"]]
- 00aa65f8 bytes 4670ec97
+ 00aa663c bytes 3570ec97
- 00aa6608 ["INT_ADD", "register:40f0:8", ["const:aa6608:8", "const:4:8"]]
- 00aa6608 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa664c ["INT_ADD", "register:40f0:8", ["const:aa664c:8", "const:4:8"]]
+ 00aa664c ["CALL", null, ["callee:0081f580:8"]]
- 00aa6608 bytes dee3f597
+ 00aa664c bytes cde3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2de85c29e51d3fad9b5ed03b5593d9d9"></a>

### [`00aa66e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa66e0.md) → [`00aa6724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6724.md) FUN_00aa6724

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa66f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa66e0.md#insn-00aa66f4) · [`00aa6708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa66e0.md#insn-00aa6708) · [`00aa6710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa66e0.md#insn-00aa6710)
- 新版 [`00aa6738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6724.md#insn-00aa6738) · [`00aa674c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6724.md#insn-00aa674c) · [`00aa6754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6724.md#insn-00aa6754)

~~~diff
- 00aa66f4 ["INT_ADD", "register:40f0:8", ["const:aa66f4:8", "const:4:8"]]
- 00aa66f4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6738 ["INT_ADD", "register:40f0:8", ["const:aa6738:8", "const:4:8"]]
+ 00aa6738 ["CALL", null, ["callee:0081f580:8"]]
- 00aa66f4 bytes a3e3f597
+ 00aa6738 bytes 92e3f597
- 00aa6708 ["INT_ADD", "register:40f0:8", ["const:aa6708:8", "const:4:8"]]
- 00aa6708 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa674c ["INT_ADD", "register:40f0:8", ["const:aa674c:8", "const:4:8"]]
+ 00aa674c ["CALL", null, ["callee:005c2710:8"]]
- 00aa6708 bytes 0270ec97
+ 00aa674c bytes f16fec97
- 00aa6710 ["INT_ADD", "register:40f0:8", ["const:aa6710:8", "const:4:8"]]
- 00aa6710 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6754 ["INT_ADD", "register:40f0:8", ["const:aa6754:8", "const:4:8"]]
+ 00aa6754 ["CALL", null, ["callee:0081f580:8"]]
- 00aa6710 bytes 9ce3f597
+ 00aa6754 bytes 8be3f597
~~~


<a id="compare-41a57b69d55669642d18f211fcf09dda"></a>

### [`00aa6888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6888.md) → [`00aa68cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa68cc.md) FUN_00aa68cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa689c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6888.md#insn-00aa689c) · [`00aa68b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6888.md#insn-00aa68b0) · [`00aa68b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6888.md#insn-00aa68b8)
- 新版 [`00aa68e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa68cc.md#insn-00aa68e0) · [`00aa68f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa68cc.md#insn-00aa68f4) · [`00aa68fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa68cc.md#insn-00aa68fc)

~~~diff
- 00aa689c ["INT_ADD", "register:40f0:8", ["const:aa689c:8", "const:4:8"]]
- 00aa689c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa68e0 ["INT_ADD", "register:40f0:8", ["const:aa68e0:8", "const:4:8"]]
+ 00aa68e0 ["CALL", null, ["callee:0081f580:8"]]
- 00aa689c bytes 39e3f597
+ 00aa68e0 bytes 28e3f597
- 00aa68b0 ["INT_ADD", "register:40f0:8", ["const:aa68b0:8", "const:4:8"]]
- 00aa68b0 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa68f4 ["INT_ADD", "register:40f0:8", ["const:aa68f4:8", "const:4:8"]]
+ 00aa68f4 ["CALL", null, ["callee:005c2710:8"]]
- 00aa68b0 bytes 986fec97
+ 00aa68f4 bytes 876fec97
- 00aa68b8 ["INT_ADD", "register:40f0:8", ["const:aa68b8:8", "const:4:8"]]
- 00aa68b8 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa68fc ["INT_ADD", "register:40f0:8", ["const:aa68fc:8", "const:4:8"]]
+ 00aa68fc ["CALL", null, ["callee:0081f580:8"]]
- 00aa68b8 bytes 32e3f597
+ 00aa68fc bytes 21e3f597
~~~


<a id="compare-35efba7c89aea9a11056ffc0268b16dc"></a>

### [`00aa76b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76b0.md) → [`00aa76f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa76f4.md) FUN_00aa76f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md) [`00aa76b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76b0.md) · 呼出先 2件 [`00aa76b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76b0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md) [`00aa76f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa76f4.md) · 呼出先 2件 [`00aa76f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa76f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa76d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76b0.md#insn-00aa76d0) · [`00aa76dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76b0.md#insn-00aa76dc)
- 新版 [`00aa7714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa76f4.md#insn-00aa7714) · [`00aa7720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa76f4.md#insn-00aa7720)

~~~diff
- 00aa76d0 ["INT_ADD", "register:40f0:8", ["const:aa76d0:8", "const:4:8"]]
- 00aa76d0 ["CALL", null, ["local:b0:8"]]
+ 00aa7714 ["INT_ADD", "register:40f0:8", ["const:aa7714:8", "const:4:8"]]
+ 00aa7714 ["CALL", null, ["local:b0:8"]]
- 00aa76d0 bytes f8ffff97
+ 00aa7714 bytes f8ffff97
- 00aa76dc ["INT_ADD", "register:40f0:8", ["const:aa76dc:8", "const:4:8"]]
- 00aa76dc ["CALL", null, ["local:b0:8"]]
+ 00aa7720 ["INT_ADD", "register:40f0:8", ["const:aa7720:8", "const:4:8"]]
+ 00aa7720 ["CALL", null, ["local:b0:8"]]
- 00aa76dc bytes f5ffff97
+ 00aa7720 bytes f5ffff97
~~~


<a id="compare-ca1c6d7f564a2d06514ef5ad91f8651c"></a>

### [`00aa7a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7a84.md) → [`00aa7ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7ac8.md) FUN_00aa7ac8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa7a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7a84.md#insn-00aa7a9c) · [`00aa7aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7a84.md#insn-00aa7aa8) · [`00aa7ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7a84.md#insn-00aa7ab4)
- 新版 [`00aa7ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7ac8.md#insn-00aa7ae0) · [`00aa7aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7ac8.md#insn-00aa7aec) · [`00aa7af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7ac8.md#insn-00aa7af8)

~~~diff
- 00aa7a9c ["INT_ADD", "register:40f0:8", ["const:aa7a9c:8", "const:4:8"]]
- 00aa7a9c ["CALL", null, ["callee:0059d12c:8"]]
+ 00aa7ae0 ["INT_ADD", "register:40f0:8", ["const:aa7ae0:8", "const:4:8"]]
+ 00aa7ae0 ["CALL", null, ["callee:0059d12c:8"]]
- 00aa7a9c bytes a4d5eb97
+ 00aa7ae0 bytes 93d5eb97
- 00aa7aa8 ["INT_ADD", "register:40f0:8", ["const:aa7aa8:8", "const:4:8"]]
- 00aa7aa8 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa7aec ["INT_ADD", "register:40f0:8", ["const:aa7aec:8", "const:4:8"]]
+ 00aa7aec ["CALL", null, ["callee:0081f580:8"]]
- 00aa7aa8 bytes b6def597
+ 00aa7aec bytes a5def597
- 00aa7ab4 ["INT_ADD", "register:40f0:8", ["const:aa7ab4:8", "const:4:8"]]
- 00aa7ab4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa7af8 ["INT_ADD", "register:40f0:8", ["const:aa7af8:8", "const:4:8"]]
+ 00aa7af8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa7ab4 bytes b3def597
+ 00aa7af8 bytes a2def597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f0bfc7f7c8f5b7f71b5279b01da81a3"></a>

### [`00aa9238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9238.md) → [`00aa927c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa927c.md) FUN_00aa927c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aa8e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e8c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00aa8ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa8/00aa8ed0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9238.md#insn-00aa9260) · [`00aa9278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9238.md#insn-00aa9278) · [`00aa9290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9238.md#insn-00aa9290)
- 新版 [`00aa92a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa927c.md#insn-00aa92a4) · [`00aa92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa927c.md#insn-00aa92bc) · [`00aa92d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa927c.md#insn-00aa92d4)

~~~diff
- 00aa9260 ["INT_ADD", "register:40f0:8", ["const:aa9260:8", "const:4:8"]]
- 00aa9260 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa92a4 ["INT_ADD", "register:40f0:8", ["const:aa92a4:8", "const:4:8"]]
+ 00aa92a4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa9260 bytes c8d8f597
+ 00aa92a4 bytes b7d8f597
- 00aa9278 ["INT_ADD", "register:40f0:8", ["const:aa9278:8", "const:4:8"]]
- 00aa9278 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa92bc ["INT_ADD", "register:40f0:8", ["const:aa92bc:8", "const:4:8"]]
+ 00aa92bc ["CALL", null, ["callee:0081f580:8"]]
- 00aa9278 bytes c2d8f597
+ 00aa92bc bytes b1d8f597
- 00aa9290 ["INT_ADD", "register:40f0:8", ["const:aa9290:8", "const:4:8"]]
- 00aa9290 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa92d4 ["INT_ADD", "register:40f0:8", ["const:aa92d4:8", "const:4:8"]]
+ 00aa92d4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa9290 bytes bcd8f597
+ 00aa92d4 bytes abd8f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-429202892f8f10f95efffab038129b0f"></a>

### [`00aa92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa92bc.md) → [`00aa9300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9300.md) FUN_00aa9300

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa9324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa92bc.md#insn-00aa9324) · [`00aa9328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa92bc.md#insn-00aa9328)
- 新版 [`00aa9368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9300.md#insn-00aa9368) · [`00aa936c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9300.md#insn-00aa936c)

~~~diff
- 00aa9324 ["INT_ADD", "register:40f0:8", ["const:aa9324:8", "const:4:8"]]
- 00aa9324 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00aa9368 ["INT_ADD", "register:40f0:8", ["const:aa9368:8", "const:4:8"]]
+ 00aa9368 ["CALL", null, ["callee:0041fdf0:8"]]
- 00aa9324 bytes b3dae597
+ 00aa9368 bytes a2dae597
- 00aa9328 ["INT_ADD", "register:40f0:8", ["const:aa9328:8", "const:4:8"]]
- 00aa9328 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa936c ["INT_ADD", "register:40f0:8", ["const:aa936c:8", "const:4:8"]]
+ 00aa936c ["CALL", null, ["callee:0081f580:8"]]
- 00aa9328 bytes 96d8f597
+ 00aa936c bytes 85d8f597
~~~


<a id="compare-d661f8641862cdc991721b87e8ea3add"></a>

### [`00aa9720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9720.md) → [`00aa9764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9764.md) FUN_00aa9764

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md) · 呼出先 2件 [`008387ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/008387ec.md) [`00838880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838880.md)
- 新版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 2件 [`008387ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008387ec.md) [`00838880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9720.md#insn-00aa973c) · [`00aa9758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9720.md#insn-00aa9758)
- 新版 [`00aa9780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9764.md#insn-00aa9780) · [`00aa979c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9764.md#insn-00aa979c)

~~~diff
- 00aa973c ["INT_ADD", "register:40f0:8", ["const:aa973c:8", "const:4:8"]]
- 00aa973c ["CALL", null, ["callee:00838880:8"]]
+ 00aa9780 ["INT_ADD", "register:40f0:8", ["const:aa9780:8", "const:4:8"]]
+ 00aa9780 ["CALL", null, ["callee:00838880:8"]]
- 00aa973c bytes 513cf697
+ 00aa9780 bytes 403cf697
- 00aa9758 ["INT_ADD", "register:40f0:8", ["const:aa9758:8", "const:4:8"]]
- 00aa9758 ["CALL", null, ["callee:008387ec:8"]]
+ 00aa979c ["INT_ADD", "register:40f0:8", ["const:aa979c:8", "const:4:8"]]
+ 00aa979c ["CALL", null, ["callee:008387ec:8"]]
- 00aa9758 bytes 253cf697
+ 00aa979c bytes 143cf697
~~~


<a id="compare-cd827117333b0d37d2aa6e9c13f9f242"></a>

### [`00aa9778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9778.md) → [`00aa97bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa97bc.md) FUN_00aa97bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 16件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`0071a134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a134.md) [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 3件 [`007d0b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d0/007d0b74.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md)
- 新版 呼出元 16件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0071a134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a134.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 3件 [`007d0b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0b74.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa9780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9778.md#insn-00aa9780) · [`00aa9784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9778.md#insn-00aa9784) · [`00aa9790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9778.md#insn-00aa9790)
- 新版 [`00aa97c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa97bc.md#insn-00aa97c4) · [`00aa97c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa97bc.md#insn-00aa97c8) · [`00aa97d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa97bc.md#insn-00aa97d4)

~~~diff
- 00aa9780 ["INT_ADD", "register:40f0:8", ["const:aa9780:8", "const:4:8"]]
- 00aa9780 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa97c4 ["INT_ADD", "register:40f0:8", ["const:aa97c4:8", "const:4:8"]]
+ 00aa97c4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa9780 bytes 80d7f597
+ 00aa97c4 bytes 6fd7f597
- 00aa9784 ["INT_ADD", "register:40f0:8", ["const:aa9784:8", "const:4:8"]]
- 00aa9784 ["CALL", null, ["callee:00821cb4:8"]]
+ 00aa97c8 ["INT_ADD", "register:40f0:8", ["const:aa97c8:8", "const:4:8"]]
+ 00aa97c8 ["CALL", null, ["callee:00821cb4:8"]]
- 00aa9784 bytes 4ce1f597
+ 00aa97c8 bytes 3be1f597
- 00aa9790 ["INT_ADD", "register:40f0:8", ["const:aa9790:8", "const:4:8"]]
- 00aa9790 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa97d4 ["INT_ADD", "register:40f0:8", ["const:aa97d4:8", "const:4:8"]]
+ 00aa97d4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa9790 bytes 7cd7f597
+ 00aa97d4 bytes 6bd7f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49027b1003f5ce591643d2a5eecb99bf"></a>

### [`00aa9fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md) → [`00aa9ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md) FUN_00aa9ff4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ce/009ce1d0.md) · 呼出先 3件 [`0045dc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dd10.md)
- 新版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 3件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md#insn-00aa9fdc) · [`00aa9ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md#insn-00aa9ff8) · [`00aaa02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md#insn-00aaa02c)
- 新版 [`00aaa020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md#insn-00aaa020) · [`00aaa03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md#insn-00aaa03c) · [`00aaa070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9ff4.md#insn-00aaa070)

~~~diff
- 00aa9fdc ["INT_ADD", "register:40f0:8", ["const:aa9fdc:8", "const:4:8"]]
- 00aa9fdc ["CALL", null, ["callee:0045dcb8:8"]]
+ 00aaa020 ["INT_ADD", "register:40f0:8", ["const:aaa020:8", "const:4:8"]]
+ 00aaa020 ["CALL", null, ["callee:0045dcb8:8"]]
- 00aa9fdc bytes 37cfe697
+ 00aaa020 bytes 26cfe697
- 00aa9ff8 ["INT_ADD", "register:40f0:8", ["const:aa9ff8:8", "const:4:8"]]
- 00aa9ff8 ["CALL", null, ["callee:0045dcb8:8"]]
+ 00aaa03c ["INT_ADD", "register:40f0:8", ["const:aaa03c:8", "const:4:8"]]
+ 00aaa03c ["CALL", null, ["callee:0045dcb8:8"]]
- 00aa9ff8 bytes 30cfe697
+ 00aaa03c bytes 1fcfe697
- 00aaa02c ["INT_ADD", "register:40f0:8", ["const:aaa02c:8", "const:4:8"]]
- 00aaa02c ["CALL", null, ["callee:0045dd10:8"]]
+ 00aaa070 ["INT_ADD", "register:40f0:8", ["const:aaa070:8", "const:4:8"]]
+ 00aaa070 ["CALL", null, ["callee:0045dd10:8"]]
- 00aaa02c bytes 39cfe697
+ 00aaa070 bytes 28cfe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62dd485e681295b4f6cb5c49966ef445"></a>

### [`00aaa18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md) → [`00aaa1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa1d0.md) FUN_00aaa1d0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071a134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a134.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0071a134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a134.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaa1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md#insn-00aaa1c8) · [`00aaa1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md#insn-00aaa1d0) · [`00aaa1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md#insn-00aaa1d8)
- 新版 [`00aaa20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa1d0.md#insn-00aaa20c) · [`00aaa214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa1d0.md#insn-00aaa214) · [`00aaa21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa1d0.md#insn-00aaa21c)

~~~diff
- 00aaa1c8 ["INT_ADD", "register:40f0:8", ["const:aaa1c8:8", "const:4:8"]]
- 00aaa1c8 ["CALL", null, ["callee:007cf950:8"]]
+ 00aaa20c ["INT_ADD", "register:40f0:8", ["const:aaa20c:8", "const:4:8"]]
+ 00aaa20c ["CALL", null, ["callee:007cf950:8"]]
- 00aaa1c8 bytes e295f497
+ 00aaa20c bytes d195f497
- 00aaa1d0 ["INT_ADD", "register:40f0:8", ["const:aaa1d0:8", "const:4:8"]]
- 00aaa1d0 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaa214 ["INT_ADD", "register:40f0:8", ["const:aaa214:8", "const:4:8"]]
+ 00aaa214 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaa1d0 bytes 3496f497
+ 00aaa214 bytes 2396f497
- 00aaa1d8 ["INT_ADD", "register:40f0:8", ["const:aaa1d8:8", "const:4:8"]]
- 00aaa1d8 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaa21c ["INT_ADD", "register:40f0:8", ["const:aaa21c:8", "const:4:8"]]
+ 00aaa21c ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaa1d8 bytes c096f497
+ 00aaa21c bytes af96f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e863e77bdbc246c5443174918a823420"></a>

### [`00aaa6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md) → [`00aaa700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa700.md) FUN_00aaa700

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00aaa18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md) [`00aaae5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md) [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md)
- 新版 呼出元 3件 [`00aaa1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa1d0.md) [`00aaaea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaaea0.md) [`00aac39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaa6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md#insn-00aaa6ec) · [`00aaa6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md#insn-00aaa6f4) · [`00aaa6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md#insn-00aaa6fc)
- 新版 [`00aaa730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa700.md#insn-00aaa730) · [`00aaa738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa700.md#insn-00aaa738) · [`00aaa740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa700.md#insn-00aaa740)

~~~diff
- 00aaa6ec ["INT_ADD", "register:40f0:8", ["const:aaa6ec:8", "const:4:8"]]
- 00aaa6ec ["CALL", null, ["callee:007cf950:8"]]
+ 00aaa730 ["INT_ADD", "register:40f0:8", ["const:aaa730:8", "const:4:8"]]
+ 00aaa730 ["CALL", null, ["callee:007cf950:8"]]
- 00aaa6ec bytes 9994f497
+ 00aaa730 bytes 8894f497
- 00aaa6f4 ["INT_ADD", "register:40f0:8", ["const:aaa6f4:8", "const:4:8"]]
- 00aaa6f4 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaa738 ["INT_ADD", "register:40f0:8", ["const:aaa738:8", "const:4:8"]]
+ 00aaa738 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaa6f4 bytes eb94f497
+ 00aaa738 bytes da94f497
- 00aaa6fc ["INT_ADD", "register:40f0:8", ["const:aaa6fc:8", "const:4:8"]]
- 00aaa6fc ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaa740 ["INT_ADD", "register:40f0:8", ["const:aaa740:8", "const:4:8"]]
+ 00aaa740 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaa6fc bytes 7795f497
+ 00aaa740 bytes 6695f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-163fc25f2fbbd166659719292a27564c"></a>

### [`00aaa8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md) → [`00aaa93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa93c.md) FUN_00aaa93c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00895118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/00895118.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) [`00a8df08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8df08.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0063c0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c178.md) [`0063c21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c21c.md)
- 新版 呼出元 3件 [`00895118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895118.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a8df4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8df4c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0063c0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c178.md) [`0063c21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c21c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaa928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md#insn-00aaa928) · [`00aaa930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md#insn-00aaa930) · [`00aaa934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md#insn-00aaa934)
- 新版 [`00aaa96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa93c.md#insn-00aaa96c) · [`00aaa974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa93c.md#insn-00aaa974) · [`00aaa978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa93c.md#insn-00aaa978)

~~~diff
- 00aaa928 ["INT_ADD", "register:40f0:8", ["const:aaa928:8", "const:4:8"]]
- 00aaa928 ["CALL", null, ["callee:007cf950:8"]]
+ 00aaa96c ["INT_ADD", "register:40f0:8", ["const:aaa96c:8", "const:4:8"]]
+ 00aaa96c ["CALL", null, ["callee:007cf950:8"]]
- 00aaa928 bytes 0a94f497
+ 00aaa96c bytes f993f497
- 00aaa930 ["INT_ADD", "register:40f0:8", ["const:aaa930:8", "const:4:8"]]
- 00aaa930 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaa974 ["INT_ADD", "register:40f0:8", ["const:aaa974:8", "const:4:8"]]
+ 00aaa974 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaa930 bytes 5c94f497
+ 00aaa974 bytes 4b94f497
- 00aaa934 ["INT_ADD", "register:40f0:8", ["const:aaa934:8", "const:4:8"]]
- 00aaa934 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaa978 ["INT_ADD", "register:40f0:8", ["const:aaa978:8", "const:4:8"]]
+ 00aaa978 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaa934 bytes e994f497
+ 00aaa978 bytes d894f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcca9f70da6cae583c2be0c1352e0c55"></a>

### [`00aaae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae18.md) → [`00aaae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaae5c.md) FUN_00aaae5c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) [`00a783c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a783c8.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) [`00a8052c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a80/00a8052c.md) · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 8件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) [`00a7840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a7840c.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a80570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a80/00a80570.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaae38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae18.md#insn-00aaae38)
- 新版 [`00aaae7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaae5c.md#insn-00aaae7c)

~~~diff
- 00aaae38 ["INT_ADD", "register:40f0:8", ["const:aaae38:8", "const:4:8"]]
- 00aaae38 ["CALL", null, ["callee:00bdb600:8"]]
+ 00aaae7c ["INT_ADD", "register:40f0:8", ["const:aaae7c:8", "const:4:8"]]
+ 00aaae7c ["CALL", null, ["callee:00bdb600:8"]]
- 00aaae38 bytes dec10494
+ 00aaae7c bytes e1c10494
~~~


<a id="compare-a354d393ebf3248c4b02fbe9c3566575"></a>

### [`00aaae5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md) → [`00aaaea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaaea0.md) FUN_00aaaea0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) · 呼出先 6件 [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aaa6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md)
- 新版 呼出元 2件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 6件 [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aaa700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaae7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md#insn-00aaae7c) · [`00aaae84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md#insn-00aaae84) · [`00aaae8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md#insn-00aaae8c)
- 新版 [`00aaaec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaaea0.md#insn-00aaaec0) · [`00aaaec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaaea0.md#insn-00aaaec8) · [`00aaaed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaaea0.md#insn-00aaaed0)

~~~diff
- 00aaae7c ["INT_ADD", "register:40f0:8", ["const:aaae7c:8", "const:4:8"]]
- 00aaae7c ["CALL", null, ["callee:007cf950:8"]]
+ 00aaaec0 ["INT_ADD", "register:40f0:8", ["const:aaaec0:8", "const:4:8"]]
+ 00aaaec0 ["CALL", null, ["callee:007cf950:8"]]
- 00aaae7c bytes b592f497
+ 00aaaec0 bytes a492f497
- 00aaae84 ["INT_ADD", "register:40f0:8", ["const:aaae84:8", "const:4:8"]]
- 00aaae84 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaaec8 ["INT_ADD", "register:40f0:8", ["const:aaaec8:8", "const:4:8"]]
+ 00aaaec8 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaae84 bytes 0793f497
+ 00aaaec8 bytes f692f497
- 00aaae8c ["INT_ADD", "register:40f0:8", ["const:aaae8c:8", "const:4:8"]]
- 00aaae8c ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaaed0 ["INT_ADD", "register:40f0:8", ["const:aaaed0:8", "const:4:8"]]
+ 00aaaed0 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaae8c bytes 9393f497
+ 00aaaed0 bytes 8293f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb9a421efdf5205024bc3fd4c377f8a7"></a>

### [`00aaafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) → [`00aaafe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md) FUN_00aaafe8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md)
- 新版 呼出元 1件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaafec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md#insn-00aaafec) · [`00aaaff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md#insn-00aaaff4) · [`00aaaffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md#insn-00aaaffc)
- 新版 [`00aab030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md#insn-00aab030) · [`00aab038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md#insn-00aab038) · [`00aab040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md#insn-00aab040)

~~~diff
- 00aaafec ["INT_ADD", "register:40f0:8", ["const:aaafec:8", "const:4:8"]]
- 00aaafec ["CALL", null, ["callee:007cf950:8"]]
+ 00aab030 ["INT_ADD", "register:40f0:8", ["const:aab030:8", "const:4:8"]]
+ 00aab030 ["CALL", null, ["callee:007cf950:8"]]
- 00aaafec bytes 5992f497
+ 00aab030 bytes 4892f497
- 00aaaff4 ["INT_ADD", "register:40f0:8", ["const:aaaff4:8", "const:4:8"]]
- 00aaaff4 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aab038 ["INT_ADD", "register:40f0:8", ["const:aab038:8", "const:4:8"]]
+ 00aab038 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaaff4 bytes ab92f497
+ 00aab038 bytes 9a92f497
- 00aaaffc ["INT_ADD", "register:40f0:8", ["const:aaaffc:8", "const:4:8"]]
- 00aaaffc ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aab040 ["INT_ADD", "register:40f0:8", ["const:aab040:8", "const:4:8"]]
+ 00aab040 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaaffc bytes 3793f497
+ 00aab040 bytes 2693f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7329e55917a32c89bfd31438f50c6db7"></a>

### [`00aab488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md) → [`00aab4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab4cc.md) FUN_00aab4cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 8件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aab4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md#insn-00aab4c0) · [`00aab4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md#insn-00aab4c8) · [`00aab4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md#insn-00aab4d0)
- 新版 [`00aab504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab4cc.md#insn-00aab504) · [`00aab50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab4cc.md#insn-00aab50c) · [`00aab514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab4cc.md#insn-00aab514)

~~~diff
- 00aab4c0 ["INT_ADD", "register:40f0:8", ["const:aab4c0:8", "const:4:8"]]
- 00aab4c0 ["CALL", null, ["callee:007cf950:8"]]
+ 00aab504 ["INT_ADD", "register:40f0:8", ["const:aab504:8", "const:4:8"]]
+ 00aab504 ["CALL", null, ["callee:007cf950:8"]]
- 00aab4c0 bytes 2491f497
+ 00aab504 bytes 1391f497
- 00aab4c8 ["INT_ADD", "register:40f0:8", ["const:aab4c8:8", "const:4:8"]]
- 00aab4c8 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aab50c ["INT_ADD", "register:40f0:8", ["const:aab50c:8", "const:4:8"]]
+ 00aab50c ["CALL", null, ["callee:007cfaa0:8"]]
- 00aab4c8 bytes 7691f497
+ 00aab50c bytes 6591f497
- 00aab4d0 ["INT_ADD", "register:40f0:8", ["const:aab4d0:8", "const:4:8"]]
- 00aab4d0 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aab514 ["INT_ADD", "register:40f0:8", ["const:aab514:8", "const:4:8"]]
+ 00aab514 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aab4d0 bytes 0292f497
+ 00aab514 bytes f191f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60be2b7e80bd9b4fd0345b12f9ebd6ba"></a>

### [`00aab5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md) → [`00aab624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab624.md) FUN_00aab624

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`00aab788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab788.md) [`00aabe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aabe48.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aab61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md#insn-00aab61c) · [`00aab624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md#insn-00aab624) · [`00aab62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md#insn-00aab62c)
- 新版 [`00aab660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab624.md#insn-00aab660) · [`00aab668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab624.md#insn-00aab668) · [`00aab670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab624.md#insn-00aab670)

~~~diff
- 00aab61c ["INT_ADD", "register:40f0:8", ["const:aab61c:8", "const:4:8"]]
- 00aab61c ["CALL", null, ["callee:007cf950:8"]]
+ 00aab660 ["INT_ADD", "register:40f0:8", ["const:aab660:8", "const:4:8"]]
+ 00aab660 ["CALL", null, ["callee:007cf950:8"]]
- 00aab61c bytes cd90f497
+ 00aab660 bytes bc90f497
- 00aab624 ["INT_ADD", "register:40f0:8", ["const:aab624:8", "const:4:8"]]
- 00aab624 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aab668 ["INT_ADD", "register:40f0:8", ["const:aab668:8", "const:4:8"]]
+ 00aab668 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aab624 bytes 1f91f497
+ 00aab668 bytes 0e91f497
- 00aab62c ["INT_ADD", "register:40f0:8", ["const:aab62c:8", "const:4:8"]]
- 00aab62c ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aab670 ["INT_ADD", "register:40f0:8", ["const:aab670:8", "const:4:8"]]
+ 00aab670 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aab62c bytes ab91f497
+ 00aab670 bytes 9a91f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65f30d5c38375fa30914e515bd8aba8b"></a>

### [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md) → [`00aac39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md) FUN_00aac39c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00aad1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md) [`00aad2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`00aad21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad21c.md) [`00aad338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad338.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aac398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md#insn-00aac398) · [`00aac3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md#insn-00aac3a0) · [`00aac3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md#insn-00aac3a8)
- 新版 [`00aac3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md#insn-00aac3dc) · [`00aac3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md#insn-00aac3e4) · [`00aac3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md#insn-00aac3ec)

~~~diff
- 00aac398 ["INT_ADD", "register:40f0:8", ["const:aac398:8", "const:4:8"]]
- 00aac398 ["CALL", null, ["callee:007cf950:8"]]
+ 00aac3dc ["INT_ADD", "register:40f0:8", ["const:aac3dc:8", "const:4:8"]]
+ 00aac3dc ["CALL", null, ["callee:007cf950:8"]]
- 00aac398 bytes 6e8df497
+ 00aac3dc bytes 5d8df497
- 00aac3a0 ["INT_ADD", "register:40f0:8", ["const:aac3a0:8", "const:4:8"]]
- 00aac3a0 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aac3e4 ["INT_ADD", "register:40f0:8", ["const:aac3e4:8", "const:4:8"]]
+ 00aac3e4 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aac3a0 bytes c08df497
+ 00aac3e4 bytes af8df497
- 00aac3a8 ["INT_ADD", "register:40f0:8", ["const:aac3a8:8", "const:4:8"]]
- 00aac3a8 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aac3ec ["INT_ADD", "register:40f0:8", ["const:aac3ec:8", "const:4:8"]]
+ 00aac3ec ["CALL", null, ["callee:007cfcd8:8"]]
- 00aac3a8 bytes 4c8ef497
+ 00aac3ec bytes 3b8ef497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b772518f254fd5b68b1416507d431c"></a>

### [`00aac920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md) → [`00aac964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md) FUN_00aac964

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aa980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aacb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00aa9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9850.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aacb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aac9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md#insn-00aac9cc) · [`00aaca10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md#insn-00aaca10) · [`00aaca54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md#insn-00aaca54)
- 新版 [`00aaca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md#insn-00aaca10) · [`00aaca54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md#insn-00aaca54) · [`00aaca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md#insn-00aaca98)

~~~diff
- 00aac9cc ["INT_ADD", "register:40f0:8", ["const:aac9cc:8", "const:4:8"]]
- 00aac9cc ["CALL", null, ["callee:00bdb040:8"]]
+ 00aaca10 ["INT_ADD", "register:40f0:8", ["const:aaca10:8", "const:4:8"]]
+ 00aaca10 ["CALL", null, ["callee:00bdb040:8"]]
- 00aac9cc bytes 89b90494
+ 00aaca10 bytes 8cb90494
- 00aaca10 ["INT_ADD", "register:40f0:8", ["const:aaca10:8", "const:4:8"]]
- 00aaca10 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aaca54 ["INT_ADD", "register:40f0:8", ["const:aaca54:8", "const:4:8"]]
+ 00aaca54 ["CALL", null, ["callee:00bdb240:8"]]
- 00aaca10 bytes f8b90494
+ 00aaca54 bytes fbb90494
- 00aaca54 ["INT_ADD", "register:40f0:8", ["const:aaca54:8", "const:4:8"]]
- 00aaca54 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aaca98 ["INT_ADD", "register:40f0:8", ["const:aaca98:8", "const:4:8"]]
+ 00aaca98 ["CALL", null, ["callee:00bdb240:8"]]
- 00aaca54 bytes e7b90494
+ 00aaca98 bytes eab90494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-414363ff18680c79a9ac99bafc1ec1c0"></a>

### [`00aacb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md) → [`00aacb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md) FUN_00aacb98

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aaafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aacb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00aaafe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aacb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aacbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md#insn-00aacbe0) · [`00aacc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md#insn-00aacc98) · [`00aaccb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md#insn-00aaccb4)
- 新版 [`00aacc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md#insn-00aacc24) · [`00aaccdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md#insn-00aaccdc) · [`00aaccf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md#insn-00aaccf8)

~~~diff
- 00aacbe0 ["INT_ADD", "register:40f0:8", ["const:aacbe0:8", "const:4:8"]]
- 00aacbe0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aacc24 ["INT_ADD", "register:40f0:8", ["const:aacc24:8", "const:4:8"]]
+ 00aacc24 ["CALL", null, ["callee:00bdb040:8"]]
- 00aacbe0 bytes 04b90494
+ 00aacc24 bytes 07b90494
- 00aacc98 ["INT_ADD", "register:40f0:8", ["const:aacc98:8", "const:4:8"]]
- 00aacc98 ["CALL", null, ["callee:00bdb060:8"]]
+ 00aaccdc ["INT_ADD", "register:40f0:8", ["const:aaccdc:8", "const:4:8"]]
+ 00aaccdc ["CALL", null, ["callee:00bdb060:8"]]
- 00aacc98 bytes deb80494
+ 00aaccdc bytes e1b80494
- 00aaccb4 ["INT_ADD", "register:40f0:8", ["const:aaccb4:8", "const:4:8"]]
- 00aaccb4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00aaccf8 ["INT_ADD", "register:40f0:8", ["const:aaccf8:8", "const:4:8"]]
+ 00aaccf8 ["CALL", null, ["callee:00bdb060:8"]]
- 00aaccb4 bytes d7b80494
+ 00aaccf8 bytes dab80494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7ee2c5e3cf39a832f5a72595356ee6f"></a>

### [`00aad1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md) → [`00aad21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad21c.md) FUN_00aad21c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`00aab788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab788.md) [`00aac39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md#insn-00aad208) · [`00aad214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md#insn-00aad214)
- 新版 [`00aad24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad21c.md#insn-00aad24c) · [`00aad258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad21c.md#insn-00aad258)

~~~diff
- 00aad208 ["INT_ADD", "register:40f0:8", ["const:aad208:8", "const:4:8"]]
- 00aad208 ["CALL", null, ["ram:457e1c:8"]]
+ 00aad24c ["INT_ADD", "register:40f0:8", ["const:aad24c:8", "const:4:8"]]
+ 00aad24c ["CALL", null, ["ram:457e1c:8"]]
- 00aad208 bytes 05abe697
+ 00aad24c bytes f4aae697
- 00aad214 ["INT_ADD", "register:40f0:8", ["const:aad214:8", "const:4:8"]]
- 00aad214 ["CALL", null, ["callee:00459efc:8"]]
+ 00aad258 ["INT_ADD", "register:40f0:8", ["const:aad258:8", "const:4:8"]]
+ 00aad258 ["CALL", null, ["callee:00459efc:8"]]
- 00aad214 bytes 3ab3e697
+ 00aad258 bytes 29b3e697
~~~


<a id="compare-7bd7b1183ac0507f2e5190feb63168b7"></a>

### [`00aad2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md) → [`00aad338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad338.md) FUN_00aad338

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`00aab788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab788.md) [`00aac39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md#insn-00aad324) · [`00aad330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md#insn-00aad330)
- 新版 [`00aad368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad338.md#insn-00aad368) · [`00aad374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad338.md#insn-00aad374)

~~~diff
- 00aad324 ["INT_ADD", "register:40f0:8", ["const:aad324:8", "const:4:8"]]
- 00aad324 ["CALL", null, ["ram:457e1c:8"]]
+ 00aad368 ["INT_ADD", "register:40f0:8", ["const:aad368:8", "const:4:8"]]
+ 00aad368 ["CALL", null, ["ram:457e1c:8"]]
- 00aad324 bytes beaae697
+ 00aad368 bytes adaae697
- 00aad330 ["INT_ADD", "register:40f0:8", ["const:aad330:8", "const:4:8"]]
- 00aad330 ["CALL", null, ["callee:00459efc:8"]]
+ 00aad374 ["INT_ADD", "register:40f0:8", ["const:aad374:8", "const:4:8"]]
+ 00aad374 ["CALL", null, ["callee:00459efc:8"]]
- 00aad330 bytes f3b2e697
+ 00aad374 bytes e2b2e697
~~~


<a id="compare-78b6d1f14061e9417160121ce0ee4e06"></a>

### [`00aad3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md) → [`00aad43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad43c.md) FUN_00aad43c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883878.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883878.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md#insn-00aad404) · [`00aad414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md#insn-00aad414) · [`00aad41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md#insn-00aad41c)
- 新版 [`00aad448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad43c.md#insn-00aad448) · [`00aad458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad43c.md#insn-00aad458) · [`00aad460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad43c.md#insn-00aad460)

~~~diff
- 00aad404 ["INT_ADD", "register:40f0:8", ["const:aad404:8", "const:4:8"]]
- 00aad404 ["CALL", null, ["callee:0081f580:8"]]
+ 00aad448 ["INT_ADD", "register:40f0:8", ["const:aad448:8", "const:4:8"]]
+ 00aad448 ["CALL", null, ["callee:0081f580:8"]]
- 00aad404 bytes 5fc8f597
+ 00aad448 bytes 4ec8f597
- 00aad414 ["INT_ADD", "register:40f0:8", ["const:aad414:8", "const:4:8"]]
- 00aad414 ["CALL", null, ["callee:008847e4:8"]]
+ 00aad458 ["INT_ADD", "register:40f0:8", ["const:aad458:8", "const:4:8"]]
+ 00aad458 ["CALL", null, ["callee:008847e4:8"]]
- 00aad414 bytes f45cf797
+ 00aad458 bytes e35cf797
- 00aad41c ["INT_ADD", "register:40f0:8", ["const:aad41c:8", "const:4:8"]]
- 00aad41c ["CALL", null, ["callee:00883878:8"]]
+ 00aad460 ["INT_ADD", "register:40f0:8", ["const:aad460:8", "const:4:8"]]
+ 00aad460 ["CALL", null, ["callee:00883878:8"]]
- 00aad41c bytes 1759f797
+ 00aad460 bytes 0659f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f00b91d8dcc5653ef1598decbf304535"></a>

### [`00aad4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md) → [`00aad518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad518.md) FUN_00aad518

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 13件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md#insn-00aad500) · [`00aad520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md#insn-00aad520) · [`00aad52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md#insn-00aad52c)
- 新版 [`00aad544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad518.md#insn-00aad544) · [`00aad564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad518.md#insn-00aad564) · [`00aad570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad518.md#insn-00aad570)

~~~diff
- 00aad500 ["INT_ADD", "register:40f0:8", ["const:aad500:8", "const:4:8"]]
- 00aad500 ["CALL", null, ["callee:0088600c:8"]]
+ 00aad544 ["INT_ADD", "register:40f0:8", ["const:aad544:8", "const:4:8"]]
+ 00aad544 ["CALL", null, ["callee:0088600c:8"]]
- 00aad500 bytes c362f797
+ 00aad544 bytes b262f797
- 00aad520 ["INT_ADD", "register:40f0:8", ["const:aad520:8", "const:4:8"]]
- 00aad520 ["CALL", null, ["callee:00886014:8"]]
+ 00aad564 ["INT_ADD", "register:40f0:8", ["const:aad564:8", "const:4:8"]]
+ 00aad564 ["CALL", null, ["callee:00886014:8"]]
- 00aad520 bytes bd62f797
+ 00aad564 bytes ac62f797
- 00aad52c ["INT_ADD", "register:40f0:8", ["const:aad52c:8", "const:4:8"]]
- 00aad52c ["CALL", null, ["callee:00886014:8"]]
+ 00aad570 ["INT_ADD", "register:40f0:8", ["const:aad570:8", "const:4:8"]]
+ 00aad570 ["CALL", null, ["callee:00886014:8"]]
- 00aad52c bytes ba62f797
+ 00aad570 bytes a962f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c666f8c38301b57367960b12abaa90c"></a>

### [`00aad9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md) → [`00aad9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad9e4.md) FUN_00aad9e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00aab488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md) [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00aab4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab4cc.md) [`00aabe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aabe48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad9c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md#insn-00aad9c8) · [`00aad9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md#insn-00aad9d4) · [`00aada08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md#insn-00aada08)
- 新版 [`00aada0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad9e4.md#insn-00aada0c) · [`00aada18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad9e4.md#insn-00aada18) · [`00aada4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad9e4.md#insn-00aada4c)

~~~diff
- 00aad9c8 ["INT_ADD", "register:40f0:8", ["const:aad9c8:8", "const:4:8"]]
- 00aad9c8 ["CALL", null, ["ram:457e1c:8"]]
+ 00aada0c ["INT_ADD", "register:40f0:8", ["const:aada0c:8", "const:4:8"]]
+ 00aada0c ["CALL", null, ["ram:457e1c:8"]]
- 00aad9c8 bytes 15a9e697
+ 00aada0c bytes 04a9e697
- 00aad9d4 ["INT_ADD", "register:40f0:8", ["const:aad9d4:8", "const:4:8"]]
- 00aad9d4 ["CALL", null, ["ram:457e1c:8"]]
+ 00aada18 ["INT_ADD", "register:40f0:8", ["const:aada18:8", "const:4:8"]]
+ 00aada18 ["CALL", null, ["ram:457e1c:8"]]
- 00aad9d4 bytes 12a9e697
+ 00aada18 bytes 01a9e697
- 00aada08 ["INT_ADD", "register:40f0:8", ["const:aada08:8", "const:4:8"]]
- 00aada08 ["CALL", null, ["callee:00aab4cc:8"]]
+ 00aada4c ["INT_ADD", "register:40f0:8", ["const:aada4c:8", "const:4:8"]]
+ 00aada4c ["CALL", null, ["callee:00aab4cc:8"]]
- 00aada08 bytes a0f6ff97
+ 00aada4c bytes a0f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfe42f6115c6427a2b6d8ea42d159e30"></a>

### [`00aadadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md) → [`00aadb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb20.md) FUN_00aadb20

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00aab488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md) [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00aab4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab4cc.md) [`00aabe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aabe48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aadb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md#insn-00aadb04) · [`00aadb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md#insn-00aadb10) · [`00aadb48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md#insn-00aadb48)
- 新版 [`00aadb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb20.md#insn-00aadb48) · [`00aadb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb20.md#insn-00aadb54) · [`00aadb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb20.md#insn-00aadb8c)

~~~diff
- 00aadb04 ["INT_ADD", "register:40f0:8", ["const:aadb04:8", "const:4:8"]]
- 00aadb04 ["CALL", null, ["ram:457e1c:8"]]
+ 00aadb48 ["INT_ADD", "register:40f0:8", ["const:aadb48:8", "const:4:8"]]
+ 00aadb48 ["CALL", null, ["ram:457e1c:8"]]
- 00aadb04 bytes c6a8e697
+ 00aadb48 bytes b5a8e697
- 00aadb10 ["INT_ADD", "register:40f0:8", ["const:aadb10:8", "const:4:8"]]
- 00aadb10 ["CALL", null, ["ram:457e1c:8"]]
+ 00aadb54 ["INT_ADD", "register:40f0:8", ["const:aadb54:8", "const:4:8"]]
+ 00aadb54 ["CALL", null, ["ram:457e1c:8"]]
- 00aadb10 bytes c3a8e697
+ 00aadb54 bytes b2a8e697
- 00aadb48 ["INT_ADD", "register:40f0:8", ["const:aadb48:8", "const:4:8"]]
- 00aadb48 ["CALL", null, ["callee:00aab4cc:8"]]
+ 00aadb8c ["INT_ADD", "register:40f0:8", ["const:aadb8c:8", "const:4:8"]]
+ 00aadb8c ["CALL", null, ["callee:00aab4cc:8"]]
- 00aadb48 bytes 50f6ff97
+ 00aadb8c bytes 50f6ff97
~~~


<a id="compare-7d6ed14220a2a849a00331b42dd36d70"></a>

### [`00aadba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md) → [`00aadbe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md) FUN_00aadbe8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00aac39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac39c.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aadc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md#insn-00aadc0c) · [`00aadc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md#insn-00aadc48) · [`00aadc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md#insn-00aadc58)
- 新版 [`00aadc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md#insn-00aadc50) · [`00aadc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md#insn-00aadc8c) · [`00aadc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md#insn-00aadc9c)

~~~diff
- 00aadc0c ["INT_ADD", "register:40f0:8", ["const:aadc0c:8", "const:4:8"]]
- 00aadc0c ["CALL", null, ["callee:00471738:8"]]
+ 00aadc50 ["INT_ADD", "register:40f0:8", ["const:aadc50:8", "const:4:8"]]
+ 00aadc50 ["CALL", null, ["callee:00471738:8"]]
- 00aadc0c bytes cb0ee797
+ 00aadc50 bytes ba0ee797
- 00aadc48 ["INT_ADD", "register:40f0:8", ["const:aadc48:8", "const:4:8"]]
- 00aadc48 ["CALL", null, ["callee:00bdb060:8"]]
+ 00aadc8c ["INT_ADD", "register:40f0:8", ["const:aadc8c:8", "const:4:8"]]
+ 00aadc8c ["CALL", null, ["callee:00bdb060:8"]]
- 00aadc48 bytes f2b40494
+ 00aadc8c bytes f5b40494
- 00aadc58 ["INT_ADD", "register:40f0:8", ["const:aadc58:8", "const:4:8"]]
- 00aadc58 ["CALL", null, ["callee:00bdb060:8"]]
+ 00aadc9c ["INT_ADD", "register:40f0:8", ["const:aadc9c:8", "const:4:8"]]
+ 00aadc9c ["CALL", null, ["callee:00bdb060:8"]]
- 00aadc58 bytes eeb40494
+ 00aadc9c bytes f1b40494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b56ddf43ab600f7399bac67172abbc41"></a>

### [`00aaeec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md) → [`00aaef04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md) FUN_00aaef04

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bd6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd6b8.md) · 呼出先 2件 [`0045d420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d420.md) [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 2件 [`0045d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d420.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaeee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md#insn-00aaeee0) · [`00aaeeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md#insn-00aaeeec) · [`00aaeef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md#insn-00aaeef8)
- 新版 [`00aaef24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md#insn-00aaef24) · [`00aaef30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md#insn-00aaef30) · [`00aaef3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md#insn-00aaef3c)

~~~diff
- 00aaeee0 ["INT_ADD", "register:40f0:8", ["const:aaeee0:8", "const:4:8"]]
- 00aaeee0 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaef24 ["INT_ADD", "register:40f0:8", ["const:aaef24:8", "const:4:8"]]
+ 00aaef24 ["CALL", null, ["callee:0045d518:8"]]
- 00aaeee0 bytes 8eb9e697
+ 00aaef24 bytes 7db9e697
- 00aaeeec ["INT_ADD", "register:40f0:8", ["const:aaeeec:8", "const:4:8"]]
- 00aaeeec ["CALL", null, ["callee:0045d518:8"]]
+ 00aaef30 ["INT_ADD", "register:40f0:8", ["const:aaef30:8", "const:4:8"]]
+ 00aaef30 ["CALL", null, ["callee:0045d518:8"]]
- 00aaeeec bytes 8bb9e697
+ 00aaef30 bytes 7ab9e697
- 00aaeef8 ["INT_ADD", "register:40f0:8", ["const:aaeef8:8", "const:4:8"]]
- 00aaeef8 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaef3c ["INT_ADD", "register:40f0:8", ["const:aaef3c:8", "const:4:8"]]
+ 00aaef3c ["CALL", null, ["callee:0045d518:8"]]
- 00aaeef8 bytes 88b9e697
+ 00aaef3c bytes 77b9e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf7a85bc469f5a990ae61aff9796b67c"></a>

### [`00aaefe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md) → [`00aaf024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md) FUN_00aaf024

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c5338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c5/009c5338.md) · 呼出先 2件 [`0045de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045de70.md) [`0045df50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 2件 [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md) [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md#insn-00aaf000) · [`00aaf00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md#insn-00aaf00c) · [`00aaf018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md#insn-00aaf018)
- 新版 [`00aaf044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md#insn-00aaf044) · [`00aaf050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md#insn-00aaf050) · [`00aaf05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md#insn-00aaf05c)

~~~diff
- 00aaf000 ["INT_ADD", "register:40f0:8", ["const:aaf000:8", "const:4:8"]]
- 00aaf000 ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf044 ["INT_ADD", "register:40f0:8", ["const:aaf044:8", "const:4:8"]]
+ 00aaf044 ["CALL", null, ["callee:0045df50:8"]]
- 00aaf000 bytes d4bbe697
+ 00aaf044 bytes c3bbe697
- 00aaf00c ["INT_ADD", "register:40f0:8", ["const:aaf00c:8", "const:4:8"]]
- 00aaf00c ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf050 ["INT_ADD", "register:40f0:8", ["const:aaf050:8", "const:4:8"]]
+ 00aaf050 ["CALL", null, ["callee:0045df50:8"]]
- 00aaf00c bytes d1bbe697
+ 00aaf050 bytes c0bbe697
- 00aaf018 ["INT_ADD", "register:40f0:8", ["const:aaf018:8", "const:4:8"]]
- 00aaf018 ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf05c ["INT_ADD", "register:40f0:8", ["const:aaf05c:8", "const:4:8"]]
+ 00aaf05c ["CALL", null, ["callee:0045df50:8"]]
- 00aaf018 bytes cebbe697
+ 00aaf05c bytes bdbbe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e1355d23cf4983003df90418d91a2a6"></a>

### [`00aaf0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0a4.md) → [`00aaf0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf0e8.md) FUN_00aaf0e8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bd6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd6b8.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0a4.md#insn-00aaf0bc) · [`00aaf0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0a4.md#insn-00aaf0c8)
- 新版 [`00aaf100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf0e8.md#insn-00aaf100) · [`00aaf10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf0e8.md#insn-00aaf10c)

~~~diff
- 00aaf0bc ["INT_ADD", "register:40f0:8", ["const:aaf0bc:8", "const:4:8"]]
- 00aaf0bc ["CALL", null, ["callee:0045d518:8"]]
+ 00aaf100 ["INT_ADD", "register:40f0:8", ["const:aaf100:8", "const:4:8"]]
+ 00aaf100 ["CALL", null, ["callee:0045d518:8"]]
- 00aaf0bc bytes 17b9e697
+ 00aaf100 bytes 06b9e697
- 00aaf0c8 ["INT_ADD", "register:40f0:8", ["const:aaf0c8:8", "const:4:8"]]
- 00aaf0c8 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaf10c ["INT_ADD", "register:40f0:8", ["const:aaf10c:8", "const:4:8"]]
+ 00aaf10c ["CALL", null, ["callee:0045d518:8"]]
- 00aaf0c8 bytes 14b9e697
+ 00aaf10c bytes 03b9e697
~~~


<a id="compare-135839fbf2f454997fb464e2d1144e00"></a>

### [`00aaf0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0dc.md) → [`00aaf120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf120.md) FUN_00aaf120

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c5338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c5/009c5338.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0dc.md#insn-00aaf0fc)
- 新版 [`00aaf140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf120.md#insn-00aaf140)

~~~diff
- 00aaf0fc ["INT_ADD", "register:40f0:8", ["const:aaf0fc:8", "const:4:8"]]
- 00aaf0fc ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf140 ["INT_ADD", "register:40f0:8", ["const:aaf140:8", "const:4:8"]]
+ 00aaf140 ["CALL", null, ["callee:0045df50:8"]]
- 00aaf0fc bytes 95bbe697
+ 00aaf140 bytes 84bbe697
~~~


<a id="compare-a06fee1eb420b6affeb0257fcb186fee"></a>

### [`00aaf114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf114.md) → [`00aaf158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf158.md) FUN_00aaf158

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d2c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2c18.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`005d2c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d2/005d2c18.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf114.md#insn-00aaf124) · [`00aaf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf114.md#insn-00aaf150)
- 新版 [`00aaf168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf158.md#insn-00aaf168) · [`00aaf194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf158.md#insn-00aaf194)

~~~diff
- 00aaf124 ["INT_ADD", "register:40f0:8", ["const:aaf124:8", "const:4:8"]]
- 00aaf124 ["CALL", null, ["callee:0081f580:8"]]
+ 00aaf168 ["INT_ADD", "register:40f0:8", ["const:aaf168:8", "const:4:8"]]
+ 00aaf168 ["CALL", null, ["callee:0081f580:8"]]
- 00aaf124 bytes 17c1f597
+ 00aaf168 bytes 06c1f597
- 00aaf150 ["INT_ADD", "register:40f0:8", ["const:aaf150:8", "const:4:8"]]
- 00aaf150 ["CALL", null, ["callee:0081f580:8"]]
+ 00aaf194 ["INT_ADD", "register:40f0:8", ["const:aaf194:8", "const:4:8"]]
+ 00aaf194 ["CALL", null, ["callee:0081f580:8"]]
- 00aaf150 bytes 0cc1f597
+ 00aaf194 bytes fbc0f597
~~~


<a id="compare-f8f840dda82b14479223d3589474dc49"></a>

### [`00aaf510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md) → [`00aaf554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md) FUN_00aaf554

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00aaf6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf6f8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00ab0e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e38.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00aaf73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf73c.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00ab0e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab0/00ab0e7c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md#insn-00aaf550) · [`00aaf560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md#insn-00aaf560) · [`00aaf588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md#insn-00aaf588)
- 新版 [`00aaf594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md#insn-00aaf594) · [`00aaf5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md#insn-00aaf5a4) · [`00aaf5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md#insn-00aaf5cc)

~~~diff
- 00aaf550 ["INT_ADD", "register:40f0:8", ["const:aaf550:8", "const:4:8"]]
- 00aaf550 ["CALL", null, ["callee:00464a64:8"]]
+ 00aaf594 ["INT_ADD", "register:40f0:8", ["const:aaf594:8", "const:4:8"]]
+ 00aaf594 ["CALL", null, ["callee:00464a64:8"]]
- 00aaf550 bytes 45d5e697
+ 00aaf594 bytes 34d5e697
- 00aaf560 ["INT_ADD", "register:40f0:8", ["const:aaf560:8", "const:4:8"]]
- 00aaf560 ["CALL", null, ["callee:00464a64:8"]]
+ 00aaf5a4 ["INT_ADD", "register:40f0:8", ["const:aaf5a4:8", "const:4:8"]]
+ 00aaf5a4 ["CALL", null, ["callee:00464a64:8"]]
- 00aaf560 bytes 41d5e697
+ 00aaf5a4 bytes 30d5e697
- 00aaf588 ["INT_ADD", "register:40f0:8", ["const:aaf588:8", "const:4:8"]]
- 00aaf588 ["CALL", null, ["callee:00464a44:8"]]
+ 00aaf5cc ["INT_ADD", "register:40f0:8", ["const:aaf5cc:8", "const:4:8"]]
+ 00aaf5cc ["CALL", null, ["callee:00464a44:8"]]
- 00aaf588 bytes 2fd5e697
+ 00aaf5cc bytes 1ed5e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b9194fff41c412987f17f83c1433d34"></a>

### [`00aaf9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md) → [`00aaf9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf9fc.md) FUN_00aaf9fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a271c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md) [`00aafb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00ab0e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e38.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00a2720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a27/00a2720c.md) [`00aafb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aafb60.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00ab0e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab0/00ab0e7c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aafa5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md#insn-00aafa5c) · [`00aafa88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md#insn-00aafa88) · [`00aafab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md#insn-00aafab8)
- 新版 [`00aafaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf9fc.md#insn-00aafaa0) · [`00aafacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf9fc.md#insn-00aafacc) · [`00aafafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf9fc.md#insn-00aafafc)

~~~diff
- 00aafa5c ["INT_ADD", "register:40f0:8", ["const:aafa5c:8", "const:4:8"]]
- 00aafa5c ["CALL", null, ["callee:0041fdf0:8"]]
+ 00aafaa0 ["INT_ADD", "register:40f0:8", ["const:aafaa0:8", "const:4:8"]]
+ 00aafaa0 ["CALL", null, ["callee:0041fdf0:8"]]
- 00aafa5c bytes e5c0e597
+ 00aafaa0 bytes d4c0e597
- 00aafa88 ["INT_ADD", "register:40f0:8", ["const:aafa88:8", "const:4:8"]]
- 00aafa88 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aafacc ["INT_ADD", "register:40f0:8", ["const:aafacc:8", "const:4:8"]]
+ 00aafacc ["CALL", null, ["callee:00bdb040:8"]]
- 00aafa88 bytes 5aad0494
+ 00aafacc bytes 5dad0494
- 00aafab8 ["INT_ADD", "register:40f0:8", ["const:aafab8:8", "const:4:8"]]
- 00aafab8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aafafc ["INT_ADD", "register:40f0:8", ["const:aafafc:8", "const:4:8"]]
+ 00aafafc ["CALL", null, ["callee:00bdb040:8"]]
- 00aafab8 bytes 4ead0494
+ 00aafafc bytes 51ad0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a34a1694c2bf3dab8bc31b7ea43e0fd5"></a>

### [`00aafb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md) → [`00aafb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aafb60.md) FUN_00aafb60

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0082ea34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082e/0082ea34.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`007ac4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac4fc.md)
- 新版 呼出元 1件 [`0082ea34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082e/0082ea34.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`007ac4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007ac4fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aafb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md#insn-00aafb50) · [`00aafb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md#insn-00aafb74) · [`00aafbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md#insn-00aafbd0)
- 新版 [`00aafb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aafb60.md#insn-00aafb94) · [`00aafbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aafb60.md#insn-00aafbb8) · [`00aafc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aafb60.md#insn-00aafc14)

~~~diff
- 00aafb50 ["INT_ADD", "register:40f0:8", ["const:aafb50:8", "const:4:8"]]
- 00aafb50 ["CALL", null, ["callee:00aaf9fc:8"]]
+ 00aafb94 ["INT_ADD", "register:40f0:8", ["const:aafb94:8", "const:4:8"]]
+ 00aafb94 ["CALL", null, ["callee:00aaf9fc:8"]]
- 00aafb50 bytes 9affff97
+ 00aafb94 bytes 9affff97
- 00aafb74 ["INT_ADD", "register:40f0:8", ["const:aafb74:8", "const:4:8"]]
- 00aafb74 ["CALL", null, ["callee:0081f580:8"]]
+ 00aafbb8 ["INT_ADD", "register:40f0:8", ["const:aafbb8:8", "const:4:8"]]
+ 00aafbb8 ["CALL", null, ["callee:0081f580:8"]]
- 00aafb74 bytes 83bef597
+ 00aafbb8 bytes 72bef597
- 00aafbd0 ["INT_ADD", "register:40f0:8", ["const:aafbd0:8", "const:4:8"]]
- 00aafbd0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aafc14 ["INT_ADD", "register:40f0:8", ["const:aafc14:8", "const:4:8"]]
+ 00aafc14 ["CALL", null, ["callee:0081f580:8"]]
- 00aafbd0 bytes 6cbef597
+ 00aafc14 bytes 5bbef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55ef79bfff24f9f376d4c9a6279497bf"></a>

### [`00ab1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1d20.md) → [`00ab1d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1d64.md) FUN_00ab1d64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00596128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md) · 呼出先 2件 [`00449ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449ae0.md) [`00449bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bdc.md)
- 新版 呼出元 1件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) · 呼出先 2件 [`00449ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449ae0.md) [`00449bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bdc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ab1d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1d20.md#insn-00ab1d54)
- 新版 [`00ab1d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1d64.md#insn-00ab1d98)

~~~diff
- 00ab1d54 ["INT_ADD", "register:40f0:8", ["const:ab1d54:8", "const:4:8"]]
- 00ab1d54 ["CALL", null, ["callee:00449bdc:8"]]
+ 00ab1d98 ["INT_ADD", "register:40f0:8", ["const:ab1d98:8", "const:4:8"]]
+ 00ab1d98 ["CALL", null, ["callee:00449bdc:8"]]
- 00ab1d54 bytes a25fe697
+ 00ab1d98 bytes 915fe697
~~~


