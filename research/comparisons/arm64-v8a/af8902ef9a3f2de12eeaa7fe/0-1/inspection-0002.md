# v15.7.3 → v15.7.4 · 要調査の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-1868e4585e92c9dcb0a34a926093f50d"></a>

### [`00a28a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28a00.md) → [`00a28a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a44.md) FUN_00a28a44

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28a00.md#insn-00a28a14)
- 新版 [`00a28a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a44.md#insn-00a28a58)

~~~diff
- 00a28a14 ["INT_ADD", "register:40f0:8", ["const:a28a14:8", "const:4:8"]]
- 00a28a14 ["CALL", null, ["callee:0045d86c:8"]]
+ 00a28a58 ["INT_ADD", "register:40f0:8", ["const:a28a58:8", "const:4:8"]]
+ 00a28a58 ["CALL", null, ["callee:0045d86c:8"]]
- 00a28a14 bytes 96d3e897
+ 00a28a58 bytes 85d3e897
~~~


<a id="compare-e549e9d636231414d1ecab5053230580"></a>

### [`00a28a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28a3c.md) → [`00a28a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a80.md) FUN_00a28a80

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28a3c.md#insn-00a28a50)
- 新版 [`00a28a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28a80.md#insn-00a28a94)

~~~diff
- 00a28a50 ["INT_ADD", "register:40f0:8", ["const:a28a50:8", "const:4:8"]]
- 00a28a50 ["CALL", null, ["callee:0045d86c:8"]]
+ 00a28a94 ["INT_ADD", "register:40f0:8", ["const:a28a94:8", "const:4:8"]]
+ 00a28a94 ["CALL", null, ["callee:0045d86c:8"]]
- 00a28a50 bytes 87d3e897
+ 00a28a94 bytes 76d3e897
~~~


<a id="compare-e32d4235a9195a26e24e688db0511ecd"></a>

### [`00a28a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28a74.md) → [`00a28ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ab8.md) FUN_00a28ab8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ce/009ce1d0.md) · 呼出先 1件 [`0045e1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 1件 [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28a74.md#insn-00a28a98)
- 新版 [`00a28adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ab8.md#insn-00a28adc)

~~~diff
- 00a28a98 ["INT_ADD", "register:40f0:8", ["const:a28a98:8", "const:4:8"]]
- 00a28a98 ["CALL", null, ["callee:0045e1c0:8"]]
+ 00a28adc ["INT_ADD", "register:40f0:8", ["const:a28adc:8", "const:4:8"]]
+ 00a28adc ["CALL", null, ["callee:0045e1c0:8"]]
- 00a28a98 bytes cad5e897
+ 00a28adc bytes b9d5e897
~~~


<a id="compare-dd9833b1816e89971ce8662a50d8bc79"></a>

### [`00a28ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28ab8.md) → [`00a28afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28afc.md) FUN_00a28afc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28ab8.md#insn-00a28ad0) · [`00a28aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28ab8.md#insn-00a28aec)
- 新版 [`00a28b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28afc.md#insn-00a28b14) · [`00a28b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28afc.md#insn-00a28b30)

~~~diff
- 00a28ad0 ["INT_ADD", "register:40f0:8", ["const:a28ad0:8", "const:4:8"]]
- 00a28ad0 ["CALL", null, ["callee:0045d86c:8"]]
+ 00a28b14 ["INT_ADD", "register:40f0:8", ["const:a28b14:8", "const:4:8"]]
+ 00a28b14 ["CALL", null, ["callee:0045d86c:8"]]
- 00a28ad0 bytes 67d3e897
+ 00a28b14 bytes 56d3e897
- 00a28aec ["INT_ADD", "register:40f0:8", ["const:a28aec:8", "const:4:8"]]
- 00a28aec ["CALL", null, ["callee:0045d86c:8"]]
+ 00a28b30 ["INT_ADD", "register:40f0:8", ["const:a28b30:8", "const:4:8"]]
+ 00a28b30 ["CALL", null, ["callee:0045d86c:8"]]
- 00a28aec bytes 60d3e897
+ 00a28b30 bytes 4fd3e897
~~~


<a id="compare-8c940f55e6241c4af9dcc574d7f26e4f"></a>

### [`00a28b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28b24.md) → [`00a28b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28b68.md) FUN_00a28b68

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28b24.md#insn-00a28b38)
- 新版 [`00a28b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28b68.md#insn-00a28b7c)

~~~diff
- 00a28b38 ["INT_ADD", "register:40f0:8", ["const:a28b38:8", "const:4:8"]]
- 00a28b38 ["CALL", null, ["callee:0045d86c:8"]]
+ 00a28b7c ["INT_ADD", "register:40f0:8", ["const:a28b7c:8", "const:4:8"]]
+ 00a28b7c ["CALL", null, ["callee:0045d86c:8"]]
- 00a28b38 bytes 4dd3e897
+ 00a28b7c bytes 3cd3e897
~~~


<a id="compare-dce35ddd5c03dbab4717f0758d92d562"></a>

### [`00a28b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28b5c.md) → [`00a28ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md) FUN_00a28ba0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ce/009ce1d0.md) · 呼出先 2件 [`0045dcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dcb8.md) [`0045e1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 2件 [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28b5c.md#insn-00a28b84) · [`00a28bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28b5c.md#insn-00a28bc4) · [`00a28bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28b5c.md#insn-00a28bd4)
- 新版 [`00a28bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md#insn-00a28bc8) · [`00a28c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md#insn-00a28c08) · [`00a28c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ba0.md#insn-00a28c18)

~~~diff
- 00a28b84 ["INT_ADD", "register:40f0:8", ["const:a28b84:8", "const:4:8"]]
- 00a28b84 ["CALL", null, ["callee:0045dcb8:8"]]
+ 00a28bc8 ["INT_ADD", "register:40f0:8", ["const:a28bc8:8", "const:4:8"]]
+ 00a28bc8 ["CALL", null, ["callee:0045dcb8:8"]]
- 00a28b84 bytes 4dd4e897
+ 00a28bc8 bytes 3cd4e897
- 00a28bc4 ["INT_ADD", "register:40f0:8", ["const:a28bc4:8", "const:4:8"]]
- 00a28bc4 ["CALL", null, ["callee:0045dcb8:8"]]
+ 00a28c08 ["INT_ADD", "register:40f0:8", ["const:a28c08:8", "const:4:8"]]
+ 00a28c08 ["CALL", null, ["callee:0045dcb8:8"]]
- 00a28bc4 bytes 3dd4e897
+ 00a28c08 bytes 2cd4e897
- 00a28bd4 ["INT_ADD", "register:40f0:8", ["const:a28bd4:8", "const:4:8"]]
- 00a28bd4 ["CALL", null, ["callee:0045e1c0:8"]]
+ 00a28c18 ["INT_ADD", "register:40f0:8", ["const:a28c18:8", "const:4:8"]]
+ 00a28c18 ["CALL", null, ["callee:0045e1c0:8"]]
- 00a28bd4 bytes 7bd5e897
+ 00a28c18 bytes 6ad5e897
~~~


<a id="compare-bdad83f4d914f577ca086b307d323dfa"></a>

### [`00a28c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28c08.md) → [`00a28c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md) FUN_00a28c4c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0045d2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d2a0.md) [`0045d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d86c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md) [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28c08.md#insn-00a28c34) · [`00a28c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28c08.md#insn-00a28c54) · [`00a28c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28c08.md#insn-00a28c7c)
- 新版 [`00a28c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md#insn-00a28c78) · [`00a28c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md#insn-00a28c98) · [`00a28cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28c4c.md#insn-00a28cc0)

~~~diff
- 00a28c34 ["INT_ADD", "register:40f0:8", ["const:a28c34:8", "const:4:8"]]
- 00a28c34 ["CALL", null, ["callee:0045d2a0:8"]]
+ 00a28c78 ["INT_ADD", "register:40f0:8", ["const:a28c78:8", "const:4:8"]]
+ 00a28c78 ["CALL", null, ["callee:0045d2a0:8"]]
- 00a28c34 bytes 9bd1e897
+ 00a28c78 bytes 8ad1e897
- 00a28c54 ["INT_ADD", "register:40f0:8", ["const:a28c54:8", "const:4:8"]]
- 00a28c54 ["CALL", null, ["callee:00419064:8"]]
+ 00a28c98 ["INT_ADD", "register:40f0:8", ["const:a28c98:8", "const:4:8"]]
+ 00a28c98 ["CALL", null, ["callee:00419064:8"]]
- 00a28c54 bytes 04c1e797
+ 00a28c98 bytes f3c0e797
- 00a28c7c ["INT_ADD", "register:40f0:8", ["const:a28c7c:8", "const:4:8"]]
- 00a28c7c ["CALL", null, ["callee:0045d2a0:8"]]
+ 00a28cc0 ["INT_ADD", "register:40f0:8", ["const:a28cc0:8", "const:4:8"]]
+ 00a28cc0 ["CALL", null, ["callee:0045d2a0:8"]]
- 00a28c7c bytes 89d1e897
+ 00a28cc0 bytes 78d1e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fddb345f6407e7b2709d9448076356eb"></a>

### [`00a28d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28d4c.md) → [`00a28d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28d90.md) FUN_00a28d90

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28d4c.md#insn-00a28d60)
- 新版 [`00a28da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28d90.md#insn-00a28da4)

~~~diff
- 00a28d60 ["INT_ADD", "register:40f0:8", ["const:a28d60:8", "const:4:8"]]
- 00a28d60 ["CALL", null, ["callee:0045d86c:8"]]
+ 00a28da4 ["INT_ADD", "register:40f0:8", ["const:a28da4:8", "const:4:8"]]
+ 00a28da4 ["CALL", null, ["callee:0045d86c:8"]]
- 00a28d60 bytes c3d2e897
+ 00a28da4 bytes b2d2e897
~~~


<a id="compare-39f9fc5a138ba39a4bff0e64ef40f31c"></a>

### [`00a28d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28d98.md) → [`00a28ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ddc.md) FUN_00a28ddc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d86c.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d86c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28d98.md#insn-00a28dac)
- 新版 [`00a28df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28ddc.md#insn-00a28df0)

~~~diff
- 00a28dac ["INT_ADD", "register:40f0:8", ["const:a28dac:8", "const:4:8"]]
- 00a28dac ["CALL", null, ["callee:0045d86c:8"]]
+ 00a28df0 ["INT_ADD", "register:40f0:8", ["const:a28df0:8", "const:4:8"]]
+ 00a28df0 ["CALL", null, ["callee:0045d86c:8"]]
- 00a28dac bytes b0d2e897
+ 00a28df0 bytes 9fd2e897
~~~


<a id="compare-f74e59f79eb82738b3f06df1017e2922"></a>

### [`00a28dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28dd0.md) → [`00a28e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28e14.md) FUN_00a28e14

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a29540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29540.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009a9794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9794.md)
- 新版 呼出元 1件 [`00a29584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29584.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009a9794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9794.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a28e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28dd0.md#insn-00a28e04) · [`00a28e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28dd0.md#insn-00a28e48) · [`00a28e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28dd0.md#insn-00a28e64)
- 新版 [`00a28e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28e14.md#insn-00a28e48) · [`00a28e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28e14.md#insn-00a28e8c) · [`00a28ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28e14.md#insn-00a28ea8)

~~~diff
- 00a28e04 ["INT_ADD", "register:40f0:8", ["const:a28e04:8", "const:4:8"]]
- 00a28e04 ["CALL", null, ["callee:00573e38:8"]]
+ 00a28e48 ["INT_ADD", "register:40f0:8", ["const:a28e48:8", "const:4:8"]]
+ 00a28e48 ["CALL", null, ["callee:00573e38:8"]]
- 00a28e04 bytes 0d2ced97
+ 00a28e48 bytes fc2bed97
- 00a28e48 ["INT_ADD", "register:40f0:8", ["const:a28e48:8", "const:4:8"]]
- 00a28e48 ["CALL", null, ["callee:0041e54c:8"]]
+ 00a28e8c ["INT_ADD", "register:40f0:8", ["const:a28e8c:8", "const:4:8"]]
+ 00a28e8c ["CALL", null, ["callee:0041e54c:8"]]
- 00a28e48 bytes c1d5e797
+ 00a28e8c bytes b0d5e797
- 00a28e64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a28e64 ["INT_ADD", "register:40f0:8", ["const:a28e64:8", "const:4:8"]]
- 00a28e64 ["CALLIND", null, ["register:0:8"]]
+ 00a28ea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a28ea8 ["INT_ADD", "register:40f0:8", ["const:a28ea8:8", "const:4:8"]]
+ 00a28ea8 ["CALLIND", null, ["register:0:8"]]
- 00a28e64 bytes 00013fd6
+ 00a28ea8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a05ae442f9982eab7fa7ca0e5aa849bd"></a>

### [`00a290ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ac.md) → [`00a290f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a290f0.md) FUN_00a290f0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 1件 [`00a26ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26ddc.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 1件 [`00a26e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a290c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ac.md#insn-00a290c8)
- 新版 [`00a2910c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a290f0.md#insn-00a2910c)

~~~diff
- 00a290c8 ["INT_ADD", "register:40f0:8", ["const:a290c8:8", "const:4:8"]]
- 00a290c8 ["CALL", null, ["callee:00a26e20:8"]]
+ 00a2910c ["INT_ADD", "register:40f0:8", ["const:a2910c:8", "const:4:8"]]
+ 00a2910c ["CALL", null, ["callee:00a26e20:8"]]
- 00a290c8 bytes 45f7ff97
+ 00a2910c bytes 45f7ff97
~~~


<a id="compare-ffb3ef1c5b6cb8489197ba53289781d1"></a>

### [`00a290ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ec.md) → [`00a29130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md) FUN_00a29130

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a26ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26ddc.md) [`00a271c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00a29208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29208.md) [`00a293b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a293b0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00a26e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26e20.md) [`00a2720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a27/00a2720c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a2924c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a2924c.md) [`00a293f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a29148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ec.md#insn-00a29148) · [`00a29170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ec.md#insn-00a29170) · [`00a2919c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ec.md#insn-00a2919c)
- 新版 [`00a2918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md#insn-00a2918c) · [`00a291b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md#insn-00a291b4) · [`00a291e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md#insn-00a291e0)

~~~diff
- 00a29148 ["INT_ADD", "register:40f0:8", ["const:a29148:8", "const:4:8"]]
- 00a29148 ["CALL", null, ["callee:00a2924c:8"]]
+ 00a2918c ["INT_ADD", "register:40f0:8", ["const:a2918c:8", "const:4:8"]]
+ 00a2918c ["CALL", null, ["callee:00a2924c:8"]]
- 00a29148 bytes 30000094
+ 00a2918c bytes 30000094
- 00a29170 ["INT_ADD", "register:40f0:8", ["const:a29170:8", "const:4:8"]]
- 00a29170 ["CALL", null, ["callee:00a293f4:8"]]
+ 00a291b4 ["INT_ADD", "register:40f0:8", ["const:a291b4:8", "const:4:8"]]
+ 00a291b4 ["CALL", null, ["callee:00a293f4:8"]]
- 00a29170 bytes 90000094
+ 00a291b4 bytes 90000094
- 00a2919c ["INT_ADD", "register:40f0:8", ["const:a2919c:8", "const:4:8"]]
- 00a2919c ["CALL", null, ["callee:00419064:8"]]
+ 00a291e0 ["INT_ADD", "register:40f0:8", ["const:a291e0:8", "const:4:8"]]
+ 00a291e0 ["CALL", null, ["callee:00419064:8"]]
- 00a2919c bytes b2bfe797
+ 00a291e0 bytes a1bfe797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb1f42b405ea21ffd499e176220d0f3"></a>

### [`00a293b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a293b0.md) → [`00a293f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md) FUN_00a293f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a290ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ec.md) · 呼出先 6件 [`00650784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650784.md) [`00a294a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a294a0.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a29130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29130.md) · 呼出先 6件 [`00650784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650784.md) [`00a294e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a294e4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a293d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a293b0.md#insn-00a293d4) · [`00a2942c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a293b0.md#insn-00a2942c) · [`00a29444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a293b0.md#insn-00a29444)
- 新版 [`00a29418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md#insn-00a29418) · [`00a29470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md#insn-00a29470) · [`00a29488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md#insn-00a29488)

~~~diff
- 00a293d4 ["INT_ADD", "register:40f0:8", ["const:a293d4:8", "const:4:8"]]
- 00a293d4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a29418 ["INT_ADD", "register:40f0:8", ["const:a29418:8", "const:4:8"]]
+ 00a29418 ["CALL", null, ["callee:00bdb040:8"]]
- 00a293d4 bytes 07c70694
+ 00a29418 bytes 0ac70694
- 00a2942c ["INT_ADD", "register:40f0:8", ["const:a2942c:8", "const:4:8"]]
- 00a2942c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a29470 ["INT_ADD", "register:40f0:8", ["const:a29470:8", "const:4:8"]]
+ 00a29470 ["CALL", null, ["callee:00bdb040:8"]]
- 00a2942c bytes f1c60694
+ 00a29470 bytes f4c60694
- 00a29444 ["INT_ADD", "register:40f0:8", ["const:a29444:8", "const:4:8"]]
- 00a29444 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00a29488 ["INT_ADD", "register:40f0:8", ["const:a29488:8", "const:4:8"]]
+ 00a29488 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00a29444 bytes 47c70694
+ 00a29488 bytes 4ac70694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc8bb3c4cfb90350af7b6b528b382b9c"></a>

### [`00a303cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a303cc.md) → [`00a30410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30410.md) FUN_00a30410

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 5件 [`00467c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c58.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 5件 [`00467c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c58.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3040c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a303cc.md#insn-00a3040c) · [`00a30428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a303cc.md#insn-00a30428) · [`00a3043c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a303cc.md#insn-00a3043c)
- 新版 [`00a30450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30410.md#insn-00a30450) · [`00a3046c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30410.md#insn-00a3046c) · [`00a30480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30410.md#insn-00a30480)

~~~diff
- 00a3040c ["INT_ADD", "register:40f0:8", ["const:a3040c:8", "const:4:8"]]
- 00a3040c ["CALL", null, ["callee:00bd6e60:8"]]
+ 00a30450 ["INT_ADD", "register:40f0:8", ["const:a30450:8", "const:4:8"]]
+ 00a30450 ["CALL", null, ["callee:00bd6e60:8"]]
- 00a3040c bytes 859a0694
+ 00a30450 bytes 849a0694
- 00a30428 ["INT_ADD", "register:40f0:8", ["const:a30428:8", "const:4:8"]]
- 00a30428 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00a3046c ["INT_ADD", "register:40f0:8", ["const:a3046c:8", "const:4:8"]]
+ 00a3046c ["CALL", null, ["callee:00bd6e60:8"]]
- 00a30428 bytes 7e9a0694
+ 00a3046c bytes 7d9a0694
- 00a3043c ["INT_ADD", "register:40f0:8", ["const:a3043c:8", "const:4:8"]]
- 00a3043c ["CALL", null, ["callee:00467c58:8"]]
+ 00a30480 ["INT_ADD", "register:40f0:8", ["const:a30480:8", "const:4:8"]]
+ 00a30480 ["CALL", null, ["callee:00467c58:8"]]
- 00a3043c bytes 07dee897
+ 00a30480 bytes f6dde897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f6dd3e4664af0210c83f3291dff005"></a>

### [`00a334a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a334a8.md) → [`00a334ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a334ec.md) FUN_00a334ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) · 呼出先 3件 [`0073e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e258.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) · 呼出先 3件 [`0073e258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e258.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a334c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a334a8.md#insn-00a334c8) · [`00a334e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a334a8.md#insn-00a334e0) · [`00a3350c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a334a8.md#insn-00a3350c)
- 新版 [`00a3350c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a334ec.md#insn-00a3350c) · [`00a33524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a334ec.md#insn-00a33524) · [`00a33550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a334ec.md#insn-00a33550)

~~~diff
- 00a334c8 ["INT_ADD", "register:40f0:8", ["const:a334c8:8", "const:4:8"]]
- 00a334c8 ["CALL", null, ["callee:0073e258:8"]]
+ 00a3350c ["INT_ADD", "register:40f0:8", ["const:a3350c:8", "const:4:8"]]
+ 00a3350c ["CALL", null, ["callee:0073e258:8"]]
- 00a334c8 bytes 642bf497
+ 00a3350c bytes 532bf497
- 00a334e0 ["INT_ADD", "register:40f0:8", ["const:a334e0:8", "const:4:8"]]
- 00a334e0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a33524 ["INT_ADD", "register:40f0:8", ["const:a33524:8", "const:4:8"]]
+ 00a33524 ["CALL", null, ["callee:00bdb060:8"]]
- 00a334e0 bytes cc9e0694
+ 00a33524 bytes cf9e0694
- 00a3350c ["INT_ADD", "register:40f0:8", ["const:a3350c:8", "const:4:8"]]
- 00a3350c ["CALL", null, ["callee:00bdb090:8"]]
+ 00a33550 ["INT_ADD", "register:40f0:8", ["const:a33550:8", "const:4:8"]]
+ 00a33550 ["CALL", null, ["callee:00bdb090:8"]]
- 00a3350c bytes cd9e0694
+ 00a33550 bytes d09e0694
~~~


<a id="compare-03b85b11c6e1e25eeafdbdc3ba7ef3fa"></a>

### [`00a34b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34b7c.md) → [`00a34bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34bc0.md) FUN_00a34bc0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 4件 [`00884764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884764.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 2件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 4件 [`00884764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884764.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a34ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34b7c.md#insn-00a34ba4) · [`00a34bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34b7c.md#insn-00a34bbc) · [`00a34bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34b7c.md#insn-00a34bc4)
- 新版 [`00a34be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34bc0.md#insn-00a34be8) · [`00a34c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34bc0.md#insn-00a34c00) · [`00a34c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34bc0.md#insn-00a34c08)

~~~diff
- 00a34ba4 ["INT_ADD", "register:40f0:8", ["const:a34ba4:8", "const:4:8"]]
- 00a34ba4 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00a34be8 ["INT_ADD", "register:40f0:8", ["const:a34be8:8", "const:4:8"]]
+ 00a34be8 ["CALL", null, ["callee:00bd6e90:8"]]
- 00a34ba4 bytes ab880694
+ 00a34be8 bytes aa880694
- 00a34bbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00a34bbc ["INT_ADD", "register:40f0:8", ["const:a34bbc:8", "const:4:8"]]
- 00a34bbc ["CALLIND", null, ["register:0:8"]]
+ 00a34c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a34c00 ["INT_ADD", "register:40f0:8", ["const:a34c00:8", "const:4:8"]]
+ 00a34c00 ["CALLIND", null, ["register:0:8"]]
- 00a34bbc bytes 00013fd6
+ 00a34c00 bytes 00013fd6
- 00a34bc4 ["INT_ADD", "register:40f0:8", ["const:a34bc4:8", "const:4:8"]]
- 00a34bc4 ["CALL", null, ["callee:00bdb030:8"]]
+ 00a34c08 ["INT_ADD", "register:40f0:8", ["const:a34c08:8", "const:4:8"]]
+ 00a34c08 ["CALL", null, ["callee:00bdb030:8"]]
- 00a34bc4 bytes 07990694
+ 00a34c08 bytes 0a990694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bcb94fc9c7d0c543fb7f663fd534459"></a>

### [`00a34c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c34.md) → [`00a34c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34c78.md) FUN_00a34c78

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008f657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f657c.md) · 呼出先 3件 [`00883d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d34.md) [`00883d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d5c.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md)
- 新版 呼出元 1件 [`008f657c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f6/008f657c.md) · 呼出先 3件 [`00883d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d34.md) [`00883d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d5c.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a34c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c34.md#insn-00a34c50) · [`00a34c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c34.md#insn-00a34c60)
- 新版 [`00a34c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34c78.md#insn-00a34c94) · [`00a34ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34c78.md#insn-00a34ca4)

~~~diff
- 00a34c50 ["INT_ADD", "register:40f0:8", ["const:a34c50:8", "const:4:8"]]
- 00a34c50 ["CALL", null, ["callee:008847e4:8"]]
+ 00a34c94 ["INT_ADD", "register:40f0:8", ["const:a34c94:8", "const:4:8"]]
+ 00a34c94 ["CALL", null, ["callee:008847e4:8"]]
- 00a34c50 bytes e53ef997
+ 00a34c94 bytes d43ef997
- 00a34c60 ["INT_ADD", "register:40f0:8", ["const:a34c60:8", "const:4:8"]]
- 00a34c60 ["CALL", null, ["callee:00883d5c:8"]]
+ 00a34ca4 ["INT_ADD", "register:40f0:8", ["const:a34ca4:8", "const:4:8"]]
+ 00a34ca4 ["CALL", null, ["callee:00883d5c:8"]]
- 00a34c60 bytes 3f3cf997
+ 00a34ca4 bytes 2e3cf997
~~~


<a id="compare-7ddfd1ac422fcccbc5566a61eadc6f08"></a>

### [`00a37e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37e2c.md) → [`00a37e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37e70.md) FUN_00a37e70

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a37e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37e2c.md#insn-00a37e4c) · [`00a37e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37e2c.md#insn-00a37e58)
- 新版 [`00a37e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37e70.md#insn-00a37e90) · [`00a37e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37e70.md#insn-00a37e9c)

~~~diff
- 00a37e4c ["INT_ADD", "register:40f0:8", ["const:a37e4c:8", "const:4:8"]]
- 00a37e4c ["CALL", null, ["ram:457e1c:8"]]
+ 00a37e90 ["INT_ADD", "register:40f0:8", ["const:a37e90:8", "const:4:8"]]
+ 00a37e90 ["CALL", null, ["ram:457e1c:8"]]
- 00a37e4c bytes f47fe897
+ 00a37e90 bytes e37fe897
- 00a37e58 ["INT_ADD", "register:40f0:8", ["const:a37e58:8", "const:4:8"]]
- 00a37e58 ["CALL", null, ["ram:457e1c:8"]]
+ 00a37e9c ["INT_ADD", "register:40f0:8", ["const:a37e9c:8", "const:4:8"]]
+ 00a37e9c ["CALL", null, ["ram:457e1c:8"]]
- 00a37e58 bytes f17fe897
+ 00a37e9c bytes e07fe897
~~~


<a id="compare-225ca8a7b44d7c6d84891af731613d80"></a>

### [`00a39ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a39/00a39ff4.md) → [`00a3a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md) FUN_00a3a038

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a37ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ecc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00882a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a37f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37f10.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00882a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/00882a18.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a39/00a39ff4.md#insn-00a3a048) · [`00a3a05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a39/00a39ff4.md#insn-00a3a05c) · [`00a3a08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a39/00a39ff4.md#insn-00a3a08c)
- 新版 [`00a3a08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md#insn-00a3a08c) · [`00a3a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md#insn-00a3a0a0) · [`00a3a0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md#insn-00a3a0d0)

~~~diff
- 00a3a048 ["INT_ADD", "register:40f0:8", ["const:a3a048:8", "const:4:8"]]
- 00a3a048 ["CALL", null, ["callee:00418fe0:8"]]
+ 00a3a08c ["INT_ADD", "register:40f0:8", ["const:a3a08c:8", "const:4:8"]]
+ 00a3a08c ["CALL", null, ["callee:00418fe0:8"]]
- 00a3a048 bytes e67be797
+ 00a3a08c bytes d57be797
- 00a3a05c ["INT_ADD", "register:40f0:8", ["const:a3a05c:8", "const:4:8"]]
- 00a3a05c ["CALL", null, ["callee:00418fe0:8"]]
+ 00a3a0a0 ["INT_ADD", "register:40f0:8", ["const:a3a0a0:8", "const:4:8"]]
+ 00a3a0a0 ["CALL", null, ["callee:00418fe0:8"]]
- 00a3a05c bytes e17be797
+ 00a3a0a0 bytes d07be797
- 00a3a08c ["INT_ADD", "register:40f0:8", ["const:a3a08c:8", "const:4:8"]]
- 00a3a08c ["CALL", null, ["callee:00882a18:8"]]
+ 00a3a0d0 ["INT_ADD", "register:40f0:8", ["const:a3a0d0:8", "const:4:8"]]
+ 00a3a0d0 ["CALL", null, ["callee:00882a18:8"]]
- 00a3a08c bytes 6322f997
+ 00a3a0d0 bytes 5222f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0229ffd0d453e6fc163bd87709b701"></a>

### [`00a3a2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a2e4.md) → [`00a3a328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a328.md) FUN_00a3a328

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a3a11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a11c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a3a160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a160.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a2e4.md#insn-00a3a2f4)
- 新版 [`00a3a338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a328.md#insn-00a3a338)

~~~diff
- 00a3a2f4 ["INT_ADD", "register:40f0:8", ["const:a3a2f4:8", "const:4:8"]]
- 00a3a2f4 ["CALL", null, ["callee:00a3a160:8"]]
+ 00a3a338 ["INT_ADD", "register:40f0:8", ["const:a3a338:8", "const:4:8"]]
+ 00a3a338 ["CALL", null, ["callee:00a3a160:8"]]
- 00a3a2f4 bytes 8affff97
+ 00a3a338 bytes 8affff97
~~~


<a id="compare-732af37ee8b1181e548d64e0e62c6b81"></a>

### [`00a3af88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af88.md) → [`00a3afcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3afcc.md) FUN_00a3afcc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00883cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883cc0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3afa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af88.md#insn-00a3afa8) · [`00a3afb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af88.md#insn-00a3afb0) · [`00a3afe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af88.md#insn-00a3afe8)
- 新版 [`00a3afec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3afcc.md#insn-00a3afec) · [`00a3aff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3afcc.md#insn-00a3aff4) · [`00a3b02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3afcc.md#insn-00a3b02c)

~~~diff
- 00a3afa8 ["INT_ADD", "register:40f0:8", ["const:a3afa8:8", "const:4:8"]]
- 00a3afa8 ["CALL", null, ["callee:00883cc0:8"]]
+ 00a3afec ["INT_ADD", "register:40f0:8", ["const:a3afec:8", "const:4:8"]]
+ 00a3afec ["CALL", null, ["callee:00883cc0:8"]]
- 00a3afa8 bytes 4623f997
+ 00a3afec bytes 3523f997
- 00a3afb0 ["INT_ADD", "register:40f0:8", ["const:a3afb0:8", "const:4:8"]]
- 00a3afb0 ["CALL", null, ["callee:009e97fc:8"]]
+ 00a3aff4 ["INT_ADD", "register:40f0:8", ["const:a3aff4:8", "const:4:8"]]
+ 00a3aff4 ["CALL", null, ["callee:009e97fc:8"]]
- 00a3afb0 bytes 02bafe97
+ 00a3aff4 bytes 02bafe97
- 00a3afe8 ["INT_ADD", "register:40f0:8", ["const:a3afe8:8", "const:4:8"]]
- 00a3afe8 ["CALL", null, ["callee:009ea92c:8"]]
+ 00a3b02c ["INT_ADD", "register:40f0:8", ["const:a3b02c:8", "const:4:8"]]
+ 00a3b02c ["CALL", null, ["callee:009ea92c:8"]]
- 00a3afe8 bytes 40befe97
+ 00a3b02c bytes 40befe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f54af0de72b51e339752eb9dd1d85878"></a>

### [`00a3b108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b108.md) → [`00a3b14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b14c.md) FUN_00a3b14c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md) [`00a2bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2bab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`00a2baf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2baf4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3b12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b108.md#insn-00a3b12c) · [`00a3b13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b108.md#insn-00a3b13c) · [`00a3b140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b108.md#insn-00a3b140)
- 新版 [`00a3b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b14c.md#insn-00a3b170) · [`00a3b180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b14c.md#insn-00a3b180) · [`00a3b184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b14c.md#insn-00a3b184)

~~~diff
- 00a3b12c ["INT_ADD", "register:40f0:8", ["const:a3b12c:8", "const:4:8"]]
- 00a3b12c ["CALL", null, ["callee:0081f580:8"]]
+ 00a3b170 ["INT_ADD", "register:40f0:8", ["const:a3b170:8", "const:4:8"]]
+ 00a3b170 ["CALL", null, ["callee:0081f580:8"]]
- 00a3b12c bytes 1591f797
+ 00a3b170 bytes 0491f797
- 00a3b13c ["INT_ADD", "register:40f0:8", ["const:a3b13c:8", "const:4:8"]]
- 00a3b13c ["CALL", null, ["callee:0081f580:8"]]
+ 00a3b180 ["INT_ADD", "register:40f0:8", ["const:a3b180:8", "const:4:8"]]
+ 00a3b180 ["CALL", null, ["callee:0081f580:8"]]
- 00a3b13c bytes 1191f797
+ 00a3b180 bytes 0091f797
- 00a3b140 ["INT_ADD", "register:40f0:8", ["const:a3b140:8", "const:4:8"]]
- 00a3b140 ["CALL", null, ["callee:00821cb4:8"]]
+ 00a3b184 ["INT_ADD", "register:40f0:8", ["const:a3b184:8", "const:4:8"]]
+ 00a3b184 ["CALL", null, ["callee:00821cb4:8"]]
- 00a3b140 bytes dd9af797
+ 00a3b184 bytes cc9af797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7eefa3f297c9be60250c8b5a456a07"></a>

### [`00a3bddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bddc.md) → [`00a3be20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3be20.md) FUN_00a3be20

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3be1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bddc.md#insn-00a3be1c) · [`00a3be2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bddc.md#insn-00a3be2c) · [`00a3be5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bddc.md#insn-00a3be5c)
- 新版 [`00a3be60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3be20.md#insn-00a3be60) · [`00a3be70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3be20.md#insn-00a3be70) · [`00a3bea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3be20.md#insn-00a3bea0)

~~~diff
- 00a3be1c ["INT_ADD", "register:40f0:8", ["const:a3be1c:8", "const:4:8"]]
- 00a3be1c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a3be60 ["INT_ADD", "register:40f0:8", ["const:a3be60:8", "const:4:8"]]
+ 00a3be60 ["CALL", null, ["callee:00bdb060:8"]]
- 00a3be1c bytes 7d7c0694
+ 00a3be60 bytes 807c0694
- 00a3be2c ["INT_ADD", "register:40f0:8", ["const:a3be2c:8", "const:4:8"]]
- 00a3be2c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a3be70 ["INT_ADD", "register:40f0:8", ["const:a3be70:8", "const:4:8"]]
+ 00a3be70 ["CALL", null, ["callee:00bdb060:8"]]
- 00a3be2c bytes 797c0694
+ 00a3be70 bytes 7c7c0694
- 00a3be5c ["INT_ADD", "register:40f0:8", ["const:a3be5c:8", "const:4:8"]]
- 00a3be5c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a3bea0 ["INT_ADD", "register:40f0:8", ["const:a3bea0:8", "const:4:8"]]
+ 00a3bea0 ["CALL", null, ["callee:00bdb060:8"]]
- 00a3be5c bytes 6d7c0694
+ 00a3bea0 bytes 707c0694
~~~


<a id="compare-34805828be950c3c566d4fae2b1432f1"></a>

### [`00a3becc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3becc.md) → [`00a3bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bf10.md) FUN_00a3bf10

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008f9c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f9c04.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008f9c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f9/008f9c04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3beec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3becc.md#insn-00a3beec) · [`00a3bef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3becc.md#insn-00a3bef8) · [`00a3bf0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3becc.md#insn-00a3bf0c)
- 新版 [`00a3bf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bf10.md#insn-00a3bf30) · [`00a3bf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bf10.md#insn-00a3bf3c) · [`00a3bf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bf10.md#insn-00a3bf50)

~~~diff
- 00a3beec ["INT_ADD", "register:40f0:8", ["const:a3beec:8", "const:4:8"]]
- 00a3beec ["CALL", null, ["ram:457e1c:8"]]
+ 00a3bf30 ["INT_ADD", "register:40f0:8", ["const:a3bf30:8", "const:4:8"]]
+ 00a3bf30 ["CALL", null, ["ram:457e1c:8"]]
- 00a3beec bytes cc6fe897
+ 00a3bf30 bytes bb6fe897
- 00a3bef8 ["INT_ADD", "register:40f0:8", ["const:a3bef8:8", "const:4:8"]]
- 00a3bef8 ["CALL", null, ["ram:457e1c:8"]]
+ 00a3bf3c ["INT_ADD", "register:40f0:8", ["const:a3bf3c:8", "const:4:8"]]
+ 00a3bf3c ["CALL", null, ["ram:457e1c:8"]]
- 00a3bef8 bytes c96fe897
+ 00a3bf3c bytes b86fe897
- 00a3bf0c ["INT_ADD", "register:40f0:8", ["const:a3bf0c:8", "const:4:8"]]
- 00a3bf0c ["CALL", null, ["callee:0081f580:8"]]
+ 00a3bf50 ["INT_ADD", "register:40f0:8", ["const:a3bf50:8", "const:4:8"]]
+ 00a3bf50 ["CALL", null, ["callee:0081f580:8"]]
- 00a3bf0c bytes 9d8df797
+ 00a3bf50 bytes 8c8df797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a4945da014b400a9a505d79236b6a87"></a>

### [`00a3bfa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bfa0.md) → [`00a3bfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bfe4.md) FUN_00a3bfe4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`0073ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009877e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/009877e0.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`0073ef14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ef14.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009877e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009877e0.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3bfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bfa0.md#insn-00a3bfd8) · [`00a3bfe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bfa0.md#insn-00a3bfe8) · [`00a3bfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bfa0.md#insn-00a3bfec)
- 新版 [`00a3c01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bfe4.md#insn-00a3c01c) · [`00a3c02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bfe4.md#insn-00a3c02c) · [`00a3c030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bfe4.md#insn-00a3c030)

~~~diff
- 00a3bfd8 ["INT_ADD", "register:40f0:8", ["const:a3bfd8:8", "const:4:8"]]
- 00a3bfd8 ["CALL", null, ["callee:009877e0:8"]]
+ 00a3c01c ["INT_ADD", "register:40f0:8", ["const:a3c01c:8", "const:4:8"]]
+ 00a3c01c ["CALL", null, ["callee:009877e0:8"]]
- 00a3bfd8 bytes 022efd97
+ 00a3c01c bytes f12dfd97
- 00a3bfe8 ["INT_ADD", "register:40f0:8", ["const:a3bfe8:8", "const:4:8"]]
- 00a3bfe8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a3c02c ["INT_ADD", "register:40f0:8", ["const:a3c02c:8", "const:4:8"]]
+ 00a3c02c ["CALL", null, ["callee:0081f580:8"]]
- 00a3bfe8 bytes 668df797
+ 00a3c02c bytes 558df797
- 00a3bfec ["INT_ADD", "register:40f0:8", ["const:a3bfec:8", "const:4:8"]]
- 00a3bfec ["CALL", null, ["callee:009bd618:8"]]
+ 00a3c030 ["INT_ADD", "register:40f0:8", ["const:a3c030:8", "const:4:8"]]
+ 00a3c030 ["CALL", null, ["callee:009bd618:8"]]
- 00a3bfec bytes 8805fe97
+ 00a3c030 bytes 7a05fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-267181498a45c366d3e92db0d10c2030"></a>

### [`00a3c280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c280.md) → [`00a3c2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c2c4.md) FUN_00a3c2c4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`00a37688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`00a376cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a376cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3c2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c280.md#insn-00a3c2a4) · [`00a3c2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c280.md#insn-00a3c2b0)
- 新版 [`00a3c2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c2c4.md#insn-00a3c2e8) · [`00a3c2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c2c4.md#insn-00a3c2f4)

~~~diff
- 00a3c2a4 ["INT_ADD", "register:40f0:8", ["const:a3c2a4:8", "const:4:8"]]
- 00a3c2a4 ["CALL", null, ["ram:457e1c:8"]]
+ 00a3c2e8 ["INT_ADD", "register:40f0:8", ["const:a3c2e8:8", "const:4:8"]]
+ 00a3c2e8 ["CALL", null, ["ram:457e1c:8"]]
- 00a3c2a4 bytes de6ee897
+ 00a3c2e8 bytes cd6ee897
- 00a3c2b0 ["INT_ADD", "register:40f0:8", ["const:a3c2b0:8", "const:4:8"]]
- 00a3c2b0 ["CALL", null, ["callee:00459efc:8"]]
+ 00a3c2f4 ["INT_ADD", "register:40f0:8", ["const:a3c2f4:8", "const:4:8"]]
+ 00a3c2f4 ["CALL", null, ["callee:00459efc:8"]]
- 00a3c2b0 bytes 1377e897
+ 00a3c2f4 bytes 0277e897
~~~


<a id="compare-9357b1fc26aeda3fb7fb98d4354df004"></a>

### [`00a3c60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c60c.md) → [`00a3c650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c650.md) FUN_00a3c650

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3c630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c60c.md#insn-00a3c630) · [`00a3c63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c60c.md#insn-00a3c63c)
- 新版 [`00a3c674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c650.md#insn-00a3c674) · [`00a3c680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c650.md#insn-00a3c680)

~~~diff
- 00a3c630 ["INT_ADD", "register:40f0:8", ["const:a3c630:8", "const:4:8"]]
- 00a3c630 ["CALL", null, ["ram:457e1c:8"]]
+ 00a3c674 ["INT_ADD", "register:40f0:8", ["const:a3c674:8", "const:4:8"]]
+ 00a3c674 ["CALL", null, ["ram:457e1c:8"]]
- 00a3c630 bytes fb6de897
+ 00a3c674 bytes ea6de897
- 00a3c63c ["INT_ADD", "register:40f0:8", ["const:a3c63c:8", "const:4:8"]]
- 00a3c63c ["CALL", null, ["callee:00459efc:8"]]
+ 00a3c680 ["INT_ADD", "register:40f0:8", ["const:a3c680:8", "const:4:8"]]
+ 00a3c680 ["CALL", null, ["callee:00459efc:8"]]
- 00a3c63c bytes 3076e897
+ 00a3c680 bytes 1f76e897
~~~


<a id="compare-f394975a0e1ae5dc80c0d48609ce2430"></a>

### [`00a3c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c8f8.md) → [`00a3c93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c93c.md) FUN_00a3c93c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md) [`00a2bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2bab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`00a2baf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2baf4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3c91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c8f8.md#insn-00a3c91c) · [`00a3c92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c8f8.md#insn-00a3c92c) · [`00a3c930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c8f8.md#insn-00a3c930)
- 新版 [`00a3c960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c93c.md#insn-00a3c960) · [`00a3c970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c93c.md#insn-00a3c970) · [`00a3c974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c93c.md#insn-00a3c974)

~~~diff
- 00a3c91c ["INT_ADD", "register:40f0:8", ["const:a3c91c:8", "const:4:8"]]
- 00a3c91c ["CALL", null, ["callee:0081f580:8"]]
+ 00a3c960 ["INT_ADD", "register:40f0:8", ["const:a3c960:8", "const:4:8"]]
+ 00a3c960 ["CALL", null, ["callee:0081f580:8"]]
- 00a3c91c bytes 198bf797
+ 00a3c960 bytes 088bf797
- 00a3c92c ["INT_ADD", "register:40f0:8", ["const:a3c92c:8", "const:4:8"]]
- 00a3c92c ["CALL", null, ["callee:0081f580:8"]]
+ 00a3c970 ["INT_ADD", "register:40f0:8", ["const:a3c970:8", "const:4:8"]]
+ 00a3c970 ["CALL", null, ["callee:0081f580:8"]]
- 00a3c92c bytes 158bf797
+ 00a3c970 bytes 048bf797
- 00a3c930 ["INT_ADD", "register:40f0:8", ["const:a3c930:8", "const:4:8"]]
- 00a3c930 ["CALL", null, ["callee:00821cb4:8"]]
+ 00a3c974 ["INT_ADD", "register:40f0:8", ["const:a3c974:8", "const:4:8"]]
+ 00a3c974 ["CALL", null, ["callee:00821cb4:8"]]
- 00a3c930 bytes e194f797
+ 00a3c974 bytes d094f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a751b9445ab119f7f8310f46f448783c"></a>

### [`00a3c9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c9ec.md) → [`00a3ca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3ca30.md) FUN_00a3ca30

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00449bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bf0.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00449bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bf0.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3ca14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c9ec.md#insn-00a3ca14) · [`00a3ca20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c9ec.md#insn-00a3ca20) · [`00a3ca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c9ec.md#insn-00a3ca40)
- 新版 [`00a3ca58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3ca30.md#insn-00a3ca58) · [`00a3ca64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3ca30.md#insn-00a3ca64) · [`00a3ca84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3ca30.md#insn-00a3ca84)

~~~diff
- 00a3ca14 ["INT_ADD", "register:40f0:8", ["const:a3ca14:8", "const:4:8"]]
- 00a3ca14 ["CALL", null, ["ram:457e1c:8"]]
+ 00a3ca58 ["INT_ADD", "register:40f0:8", ["const:a3ca58:8", "const:4:8"]]
+ 00a3ca58 ["CALL", null, ["ram:457e1c:8"]]
- 00a3ca14 bytes 026de897
+ 00a3ca58 bytes f16ce897
- 00a3ca20 ["INT_ADD", "register:40f0:8", ["const:a3ca20:8", "const:4:8"]]
- 00a3ca20 ["CALL", null, ["callee:00459efc:8"]]
+ 00a3ca64 ["INT_ADD", "register:40f0:8", ["const:a3ca64:8", "const:4:8"]]
+ 00a3ca64 ["CALL", null, ["callee:00459efc:8"]]
- 00a3ca20 bytes 3775e897
+ 00a3ca64 bytes 2675e897
- 00a3ca40 ["INT_ADD", "register:40f0:8", ["const:a3ca40:8", "const:4:8"]]
- 00a3ca40 ["CALL", null, ["callee:0081f580:8"]]
+ 00a3ca84 ["INT_ADD", "register:40f0:8", ["const:a3ca84:8", "const:4:8"]]
+ 00a3ca84 ["CALL", null, ["callee:0081f580:8"]]
- 00a3ca40 bytes d08af797
+ 00a3ca84 bytes bf8af797
~~~


<a id="compare-5758d37bf7b7f8252726ea9ec705ad06"></a>

### [`00a3cac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cac8.md) → [`00a3cb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cb0c.md) FUN_00a3cb0c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3cae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cac8.md#insn-00a3cae4) · [`00a3caec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cac8.md#insn-00a3caec) · [`00a3cb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cac8.md#insn-00a3cb04)
- 新版 [`00a3cb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cb0c.md#insn-00a3cb28) · [`00a3cb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cb0c.md#insn-00a3cb30) · [`00a3cb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cb0c.md#insn-00a3cb48)

~~~diff
- 00a3cae4 ["INT_ADD", "register:40f0:8", ["const:a3cae4:8", "const:4:8"]]
- 00a3cae4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a3cb28 ["INT_ADD", "register:40f0:8", ["const:a3cb28:8", "const:4:8"]]
+ 00a3cb28 ["CALL", null, ["callee:0081f580:8"]]
- 00a3cae4 bytes a78af797
+ 00a3cb28 bytes 968af797
- 00a3caec ["INT_ADD", "register:40f0:8", ["const:a3caec:8", "const:4:8"]]
- 00a3caec ["CALL", null, ["callee:0073ab94:8"]]
+ 00a3cb30 ["INT_ADD", "register:40f0:8", ["const:a3cb30:8", "const:4:8"]]
+ 00a3cb30 ["CALL", null, ["callee:0073ab94:8"]]
- 00a3caec bytes 2af8f397
+ 00a3cb30 bytes 19f8f397
- 00a3cb04 ["INT_ADD", "register:40f0:8", ["const:a3cb04:8", "const:4:8"]]
- 00a3cb04 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a3cb48 ["INT_ADD", "register:40f0:8", ["const:a3cb48:8", "const:4:8"]]
+ 00a3cb48 ["CALL", null, ["callee:00bdb060:8"]]
- 00a3cb04 bytes 43790694
+ 00a3cb48 bytes 46790694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57bb910e1f3a83d26230327f729e712c"></a>

### [`00a3cbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cbac.md) → [`00a3cbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cbf0.md) FUN_00a3cbf0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3cbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cbac.md#insn-00a3cbc8) · [`00a3cbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cbac.md#insn-00a3cbd0) · [`00a3cbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cbac.md#insn-00a3cbe8)
- 新版 [`00a3cc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cbf0.md#insn-00a3cc0c) · [`00a3cc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cbf0.md#insn-00a3cc14) · [`00a3cc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cbf0.md#insn-00a3cc2c)

~~~diff
- 00a3cbc8 ["INT_ADD", "register:40f0:8", ["const:a3cbc8:8", "const:4:8"]]
- 00a3cbc8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a3cc0c ["INT_ADD", "register:40f0:8", ["const:a3cc0c:8", "const:4:8"]]
+ 00a3cc0c ["CALL", null, ["callee:0081f580:8"]]
- 00a3cbc8 bytes 6e8af797
+ 00a3cc0c bytes 5d8af797
- 00a3cbd0 ["INT_ADD", "register:40f0:8", ["const:a3cbd0:8", "const:4:8"]]
- 00a3cbd0 ["CALL", null, ["callee:0073ab94:8"]]
+ 00a3cc14 ["INT_ADD", "register:40f0:8", ["const:a3cc14:8", "const:4:8"]]
+ 00a3cc14 ["CALL", null, ["callee:0073ab94:8"]]
- 00a3cbd0 bytes f1f7f397
+ 00a3cc14 bytes e0f7f397
- 00a3cbe8 ["INT_ADD", "register:40f0:8", ["const:a3cbe8:8", "const:4:8"]]
- 00a3cbe8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a3cc2c ["INT_ADD", "register:40f0:8", ["const:a3cc2c:8", "const:4:8"]]
+ 00a3cc2c ["CALL", null, ["callee:00bdb060:8"]]
- 00a3cbe8 bytes 0a790694
+ 00a3cc2c bytes 0d790694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb16e3db8fa6e4bb6b5c1f8daa5bb64f"></a>

### [`00a3ce88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3ce88.md) → [`00a3cecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cecc.md) FUN_00a3cecc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`00a02d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md) [`00a02dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3cee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3ce88.md#insn-00a3cee4) · [`00a3cee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3ce88.md#insn-00a3cee8) · [`00a3cef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3ce88.md#insn-00a3cef0)
- 新版 [`00a3cf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cecc.md#insn-00a3cf28) · [`00a3cf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cecc.md#insn-00a3cf2c) · [`00a3cf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cecc.md#insn-00a3cf34)

~~~diff
- 00a3cee4 ["INT_ADD", "register:40f0:8", ["const:a3cee4:8", "const:4:8"]]
- 00a3cee4 ["CALL", null, ["ram:469e20:8"]]
+ 00a3cf28 ["INT_ADD", "register:40f0:8", ["const:a3cf28:8", "const:4:8"]]
+ 00a3cf28 ["CALL", null, ["ram:469e20:8"]]
- 00a3cee4 bytes cfb3e897
+ 00a3cf28 bytes beb3e897
- 00a3cee8 ["INT_ADD", "register:40f0:8", ["const:a3cee8:8", "const:4:8"]]
- 00a3cee8 ["CALL", null, ["callee:0046b908:8"]]
+ 00a3cf2c ["INT_ADD", "register:40f0:8", ["const:a3cf2c:8", "const:4:8"]]
+ 00a3cf2c ["CALL", null, ["callee:0046b908:8"]]
- 00a3cee8 bytes 88bae897
+ 00a3cf2c bytes 77bae897
- 00a3cef0 ["INT_ADD", "register:40f0:8", ["const:a3cef0:8", "const:4:8"]]
- 00a3cef0 ["CALL", null, ["callee:00646dc4:8"]]
+ 00a3cf34 ["INT_ADD", "register:40f0:8", ["const:a3cf34:8", "const:4:8"]]
+ 00a3cf34 ["CALL", null, ["callee:00646dc4:8"]]
- 00a3cef0 bytes b527f097
+ 00a3cf34 bytes a427f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0e544c26149092be4b6a46870f8511e"></a>

### [`00a3cfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cfc8.md) → [`00a3d00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d00c.md) FUN_00a3d00c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0071a0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0f8.md) [`00a02d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0071a0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0f8.md) [`00a02dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3d010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cfc8.md#insn-00a3d010) · [`00a3d014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cfc8.md#insn-00a3d014) · [`00a3d028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cfc8.md#insn-00a3d028)
- 新版 [`00a3d054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d00c.md#insn-00a3d054) · [`00a3d058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d00c.md#insn-00a3d058) · [`00a3d06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d00c.md#insn-00a3d06c)

~~~diff
- 00a3d010 ["INT_ADD", "register:40f0:8", ["const:a3d010:8", "const:4:8"]]
- 00a3d010 ["CALL", null, ["ram:469e20:8"]]
+ 00a3d054 ["INT_ADD", "register:40f0:8", ["const:a3d054:8", "const:4:8"]]
+ 00a3d054 ["CALL", null, ["ram:469e20:8"]]
- 00a3d010 bytes 84b3e897
+ 00a3d054 bytes 73b3e897
- 00a3d014 ["INT_ADD", "register:40f0:8", ["const:a3d014:8", "const:4:8"]]
- 00a3d014 ["CALL", null, ["callee:0046b908:8"]]
+ 00a3d058 ["INT_ADD", "register:40f0:8", ["const:a3d058:8", "const:4:8"]]
+ 00a3d058 ["CALL", null, ["callee:0046b908:8"]]
- 00a3d014 bytes 3dbae897
+ 00a3d058 bytes 2cbae897
- 00a3d028 ["INT_ADD", "register:40f0:8", ["const:a3d028:8", "const:4:8"]]
- 00a3d028 ["CALL", null, ["callee:0071a0f8:8"]]
+ 00a3d06c ["INT_ADD", "register:40f0:8", ["const:a3d06c:8", "const:4:8"]]
+ 00a3d06c ["CALL", null, ["callee:0071a0f8:8"]]
- 00a3d028 bytes 3474f397
+ 00a3d06c bytes 2374f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc9034bf82a18283d0a95c50d052371"></a>

### [`00a3d0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d0f0.md) → [`00a3d134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d134.md) FUN_00a3d134

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`007f96a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96a4.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md) [`00a34758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34758.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`007f96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f96a4.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`00a3479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a3479c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3d114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d0f0.md#insn-00a3d114) · [`00a3d120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d0f0.md#insn-00a3d120) · [`00a3d140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d0f0.md#insn-00a3d140)
- 新版 [`00a3d158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d134.md#insn-00a3d158) · [`00a3d164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d134.md#insn-00a3d164) · [`00a3d184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d134.md#insn-00a3d184)

~~~diff
- 00a3d114 ["INT_ADD", "register:40f0:8", ["const:a3d114:8", "const:4:8"]]
- 00a3d114 ["CALL", null, ["ram:457e1c:8"]]
+ 00a3d158 ["INT_ADD", "register:40f0:8", ["const:a3d158:8", "const:4:8"]]
+ 00a3d158 ["CALL", null, ["ram:457e1c:8"]]
- 00a3d114 bytes 426be897
+ 00a3d158 bytes 316be897
- 00a3d120 ["INT_ADD", "register:40f0:8", ["const:a3d120:8", "const:4:8"]]
- 00a3d120 ["CALL", null, ["ram:457e1c:8"]]
+ 00a3d164 ["INT_ADD", "register:40f0:8", ["const:a3d164:8", "const:4:8"]]
+ 00a3d164 ["CALL", null, ["ram:457e1c:8"]]
- 00a3d120 bytes 3f6be897
+ 00a3d164 bytes 2e6be897
- 00a3d140 ["INT_ADD", "register:40f0:8", ["const:a3d140:8", "const:4:8"]]
- 00a3d140 ["CALL", null, ["callee:00821cb4:8"]]
+ 00a3d184 ["INT_ADD", "register:40f0:8", ["const:a3d184:8", "const:4:8"]]
+ 00a3d184 ["CALL", null, ["callee:00821cb4:8"]]
- 00a3d140 bytes dd92f797
+ 00a3d184 bytes cc92f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5986fe5d06b0064366b2b8ef7c3c6613"></a>

### [`00a3d1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d1f8.md) → [`00a3d23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d23c.md) FUN_00a3d23c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`007f96a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96a4.md) [`00a34758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34758.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`007f96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f96a4.md) [`00a3479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a3479c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3d21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d1f8.md#insn-00a3d21c) · [`00a3d228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d1f8.md#insn-00a3d228) · [`00a3d254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d1f8.md#insn-00a3d254)
- 新版 [`00a3d260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d23c.md#insn-00a3d260) · [`00a3d26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d23c.md#insn-00a3d26c) · [`00a3d298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d23c.md#insn-00a3d298)

~~~diff
- 00a3d21c ["INT_ADD", "register:40f0:8", ["const:a3d21c:8", "const:4:8"]]
- 00a3d21c ["CALL", null, ["ram:457e1c:8"]]
+ 00a3d260 ["INT_ADD", "register:40f0:8", ["const:a3d260:8", "const:4:8"]]
+ 00a3d260 ["CALL", null, ["ram:457e1c:8"]]
- 00a3d21c bytes 006be897
+ 00a3d260 bytes ef6ae897
- 00a3d228 ["INT_ADD", "register:40f0:8", ["const:a3d228:8", "const:4:8"]]
- 00a3d228 ["CALL", null, ["ram:457e1c:8"]]
+ 00a3d26c ["INT_ADD", "register:40f0:8", ["const:a3d26c:8", "const:4:8"]]
+ 00a3d26c ["CALL", null, ["ram:457e1c:8"]]
- 00a3d228 bytes fd6ae897
+ 00a3d26c bytes ec6ae897
- 00a3d254 ["INT_ADD", "register:40f0:8", ["const:a3d254:8", "const:4:8"]]
- 00a3d254 ["CALL", null, ["callee:007f96a4:8"]]
+ 00a3d298 ["INT_ADD", "register:40f0:8", ["const:a3d298:8", "const:4:8"]]
+ 00a3d298 ["CALL", null, ["callee:007f96a4:8"]]
- 00a3d254 bytes 14f1f697
+ 00a3d298 bytes 03f1f697
~~~


<a id="compare-2d3f7acef8fb808844ef86d738df1094"></a>

### [`00a3d6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d6a8.md) → [`00a3d6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d6ec.md) FUN_00a3d6ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) [`00a34c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c84.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) [`00a34cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34cc8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3d6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d6a8.md#insn-00a3d6b0)
- 新版 [`00a3d6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d6ec.md#insn-00a3d6f4)

~~~diff
- 00a3d6b0 ["INT_ADD", "register:40f0:8", ["const:a3d6b0:8", "const:4:8"]]
- 00a3d6b0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a3d6f4 ["INT_ADD", "register:40f0:8", ["const:a3d6f4:8", "const:4:8"]]
+ 00a3d6f4 ["CALL", null, ["callee:0081f580:8"]]
- 00a3d6b0 bytes b487f797
+ 00a3d6f4 bytes a387f797
~~~


<a id="compare-77bd6f67882db1355745b9cb54821630"></a>

### [`00a3e570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3e/00a3e570.md) → [`00a3e5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3e/00a3e5b4.md) FUN_00a3e5b4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3e58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3e/00a3e570.md#insn-00a3e58c)
- 新版 [`00a3e5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3e/00a3e5b4.md#insn-00a3e5d0)

~~~diff
- 00a3e58c ["INT_ADD", "register:40f0:8", ["const:a3e58c:8", "const:4:8"]]
- 00a3e58c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a3e5d0 ["INT_ADD", "register:40f0:8", ["const:a3e5d0:8", "const:4:8"]]
+ 00a3e5d0 ["CALL", null, ["callee:00bdb060:8"]]
- 00a3e58c bytes a1720694
+ 00a3e5d0 bytes a4720694
~~~


<a id="compare-8a0c23c6d4df6cb2e16b14a1525170d2"></a>

### [`00a41054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41054.md) → [`00a41098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md) FUN_00a41098

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00739a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md) [`00761d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761d08.md) [`00a3d6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d6c8.md) [`00a418e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a418e0.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 4件 [`00739a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00739/00739a10.md) [`00761d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md) [`00a3d70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d70c.md) [`00a41924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41924.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a41148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41054.md#insn-00a41148) · [`00a41170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41054.md#insn-00a41170) · [`00a4117c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41054.md#insn-00a4117c)
- 新版 [`00a4118c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md#insn-00a4118c) · [`00a411b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md#insn-00a411b4) · [`00a411c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a41098.md#insn-00a411c0)

~~~diff
- 00a41148 ["INT_ADD", "register:40f0:8", ["const:a41148:8", "const:4:8"]]
- 00a41148 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a4118c ["INT_ADD", "register:40f0:8", ["const:a4118c:8", "const:4:8"]]
+ 00a4118c ["CALL", null, ["callee:00bdb040:8"]]
- 00a41148 bytes aa670694
+ 00a4118c bytes ad670694
- 00a41170 ["INT_ADD", "register:40f0:8", ["const:a41170:8", "const:4:8"]]
- 00a41170 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00a411b4 ["INT_ADD", "register:40f0:8", ["const:a411b4:8", "const:4:8"]]
+ 00a411b4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00a41170 bytes fc670694
+ 00a411b4 bytes ff670694
- 00a4117c ["INT_ADD", "register:40f0:8", ["const:a4117c:8", "const:4:8"]]
- 00a4117c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a411c0 ["INT_ADD", "register:40f0:8", ["const:a411c0:8", "const:4:8"]]
+ 00a411c0 ["CALL", null, ["callee:00bdb060:8"]]
- 00a4117c bytes a5670694
+ 00a411c0 bytes a8670694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b69fb7bda1eeb9b2068ae7fab0d083d"></a>

### [`00a41518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41518.md) → [`00a4155c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a4155c.md) FUN_00a4155c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a412d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a412d8.md) · 呼出先 8件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005f0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0660.md) [`00a42124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a42/00a42124.md) [`00a42e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a42/00a42e38.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00a4131c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a4131c.md) · 呼出先 8件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`005f0660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0660.md) [`00a42168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a42/00a42168.md) [`00a42e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a42/00a42e7c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a41558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41518.md#insn-00a41558) · [`00a41598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41518.md#insn-00a41598) · [`00a415b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a41518.md#insn-00a415b0)
- 新版 [`00a4159c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a4155c.md#insn-00a4159c) · [`00a415dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a4155c.md#insn-00a415dc) · [`00a415f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a4155c.md#insn-00a415f4)

~~~diff
- 00a41558 ["INT_ADD", "register:40f0:8", ["const:a41558:8", "const:4:8"]]
- 00a41558 ["CALL", null, ["callee:00a42168:8"]]
+ 00a4159c ["INT_ADD", "register:40f0:8", ["const:a4159c:8", "const:4:8"]]
+ 00a4159c ["CALL", null, ["callee:00a42168:8"]]
- 00a41558 bytes f3020094
+ 00a4159c bytes f3020094
- 00a41598 ["INT_ADD", "register:40f0:8", ["const:a41598:8", "const:4:8"]]
- 00a41598 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a415dc ["INT_ADD", "register:40f0:8", ["const:a415dc:8", "const:4:8"]]
+ 00a415dc ["CALL", null, ["callee:00bdb040:8"]]
- 00a41598 bytes 96660694
+ 00a415dc bytes 99660694
- 00a415b0 ["INT_ADD", "register:40f0:8", ["const:a415b0:8", "const:4:8"]]
- 00a415b0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00a415f4 ["INT_ADD", "register:40f0:8", ["const:a415f4:8", "const:4:8"]]
+ 00a415f4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00a415b0 bytes ec660694
+ 00a415f4 bytes ef660694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dae03e89dd9c6de1cc1b72b4cfc9640c"></a>

### [`00a43b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43b04.md) → [`00a43b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43b48.md) FUN_00a43b48

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a432a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a432a8.md) [`00a43c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43c68.md) · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00a432ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a432ec.md) [`00a43cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43cac.md) · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a43b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43b04.md#insn-00a43b28) · [`00a43b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43b04.md#insn-00a43b60) · [`00a43b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43b04.md#insn-00a43b78)
- 新版 [`00a43b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43b48.md#insn-00a43b6c) · [`00a43ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43b48.md#insn-00a43ba4) · [`00a43bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43b48.md#insn-00a43bbc)

~~~diff
- 00a43b28 ["INT_ADD", "register:40f0:8", ["const:a43b28:8", "const:4:8"]]
- 00a43b28 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a43b6c ["INT_ADD", "register:40f0:8", ["const:a43b6c:8", "const:4:8"]]
+ 00a43b6c ["CALL", null, ["callee:00bdb040:8"]]
- 00a43b28 bytes 325d0694
+ 00a43b6c bytes 355d0694
- 00a43b60 ["INT_ADD", "register:40f0:8", ["const:a43b60:8", "const:4:8"]]
- 00a43b60 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a43ba4 ["INT_ADD", "register:40f0:8", ["const:a43ba4:8", "const:4:8"]]
+ 00a43ba4 ["CALL", null, ["callee:00bdb040:8"]]
- 00a43b60 bytes 245d0694
+ 00a43ba4 bytes 275d0694
- 00a43b78 ["INT_ADD", "register:40f0:8", ["const:a43b78:8", "const:4:8"]]
- 00a43b78 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00a43bbc ["INT_ADD", "register:40f0:8", ["const:a43bbc:8", "const:4:8"]]
+ 00a43bbc ["CALL", null, ["callee:00bdb1b0:8"]]
- 00a43b78 bytes 7a5d0694
+ 00a43bbc bytes 7d5d0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5095b3e7a7356d068a4c1f9ee3d0434"></a>

### [`00a43bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43bcc.md) → [`00a43c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c10.md) FUN_00a43c10

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a43bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43bcc.md#insn-00a43bf8)
- 新版 [`00a43c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c10.md#insn-00a43c3c)

~~~diff
- 00a43bf8 ["INT_ADD", "register:40f0:8", ["const:a43bf8:8", "const:4:8"]]
- 00a43bf8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a43c3c ["INT_ADD", "register:40f0:8", ["const:a43c3c:8", "const:4:8"]]
+ 00a43c3c ["CALL", null, ["callee:00bdb060:8"]]
- 00a43bf8 bytes 065d0694
+ 00a43c3c bytes 095d0694
~~~


<a id="compare-7371fd818201271ca0ef93ab74619d5f"></a>

### [`00a43c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43c18.md) → [`00a43c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c5c.md) FUN_00a43c5c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a42124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a42/00a42124.md) [`00a43c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43c18.md) · 呼出先 2件 [`00a43c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43c18.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00a42168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a42/00a42168.md) [`00a43c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c5c.md) · 呼出先 2件 [`00a43c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c5c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a43c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43c18.md#insn-00a43c34) · [`00a43c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43c18.md#insn-00a43c40) · [`00a43c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a43/00a43c18.md#insn-00a43c50)
- 新版 [`00a43c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c5c.md#insn-00a43c78) · [`00a43c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c5c.md#insn-00a43c84) · [`00a43c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43c5c.md#insn-00a43c94)

~~~diff
- 00a43c34 ["INT_ADD", "register:40f0:8", ["const:a43c34:8", "const:4:8"]]
- 00a43c34 ["CALL", null, ["local:b0:8"]]
+ 00a43c78 ["INT_ADD", "register:40f0:8", ["const:a43c78:8", "const:4:8"]]
+ 00a43c78 ["CALL", null, ["local:b0:8"]]
- 00a43c34 bytes f9ffff97
+ 00a43c78 bytes f9ffff97
- 00a43c40 ["INT_ADD", "register:40f0:8", ["const:a43c40:8", "const:4:8"]]
- 00a43c40 ["CALL", null, ["local:b0:8"]]
+ 00a43c84 ["INT_ADD", "register:40f0:8", ["const:a43c84:8", "const:4:8"]]
+ 00a43c84 ["CALL", null, ["local:b0:8"]]
- 00a43c40 bytes f6ffff97
+ 00a43c84 bytes f6ffff97
- 00a43c50 ["INT_ADD", "register:40f0:8", ["const:a43c50:8", "const:4:8"]]
- 00a43c50 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a43c94 ["INT_ADD", "register:40f0:8", ["const:a43c94:8", "const:4:8"]]
+ 00a43c94 ["CALL", null, ["callee:00bdb060:8"]]
- 00a43c50 bytes f05c0694
+ 00a43c94 bytes f35c0694
~~~


<a id="compare-97958bacb2647cce1a3eaf79a8669817"></a>

### [`00a44bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a44/00a44bac.md) → [`00a44bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md) FUN_00a44bf0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 4件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a44c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a44/00a44bac.md#insn-00a44c1c)
- 新版 [`00a44c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md#insn-00a44c60)

~~~diff
- 00a44c1c ["INT_ADD", "register:40f0:8", ["const:a44c1c:8", "const:4:8"]]
- 00a44c1c ["CALL", null, ["callee:0041fdf0:8"]]
+ 00a44c60 ["INT_ADD", "register:40f0:8", ["const:a44c60:8", "const:4:8"]]
+ 00a44c60 ["CALL", null, ["callee:0041fdf0:8"]]
- 00a44c1c bytes 756ce797
+ 00a44c60 bytes 646ce797
~~~


<a id="compare-16941bf3aa757ed1bbd3d2c955559985"></a>

### [`00a4af1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4a/00a4af1c.md) → [`00a4af60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af60.md) FUN_00a4af60

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a45be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a45/00a45be0.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f70.md)
- 新版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4af24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4a/00a4af1c.md#insn-00a4af24)
- 新版 [`00a4af68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af60.md#insn-00a4af68)

~~~diff
- 00a4af24 ["INT_ADD", "register:40f0:8", ["const:a4af24:8", "const:4:8"]]
- 00a4af24 ["CALL", null, ["callee:0081f580:8"]]
+ 00a4af68 ["INT_ADD", "register:40f0:8", ["const:a4af68:8", "const:4:8"]]
+ 00a4af68 ["CALL", null, ["callee:0081f580:8"]]
- 00a4af24 bytes 9751f797
+ 00a4af68 bytes 8651f797
~~~


<a id="compare-d2bf3653acfb7b9d3b13b4f3890a92b3"></a>

### [`00a4fd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fd40.md) → [`00a4fd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fd84.md) FUN_00a4fd84

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4fd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fd40.md#insn-00a4fd8c)
- 新版 [`00a4fdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fd84.md#insn-00a4fdd0)

~~~diff
- 00a4fd8c ["INT_ADD", "register:40f0:8", ["const:a4fd8c:8", "const:4:8"]]
- 00a4fd8c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a4fdd0 ["INT_ADD", "register:40f0:8", ["const:a4fdd0:8", "const:4:8"]]
+ 00a4fdd0 ["CALL", null, ["callee:00bdb060:8"]]
- 00a4fd8c bytes a12c0694
+ 00a4fdd0 bytes a42c0694
~~~


<a id="compare-5c06657516cdd8b0408d14b8812aaa41"></a>

### [`00a4fdbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fdbc.md) → [`00a4fe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md) FUN_00a4fe00

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4b1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4b/00a4b1c8.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a4b20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4b/00a4b20c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fdbc.md#insn-00a4fe2c) · [`00a4fe3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fdbc.md#insn-00a4fe3c) · [`00a4fe4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fdbc.md#insn-00a4fe4c)
- 新版 [`00a4fe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md#insn-00a4fe70) · [`00a4fe80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md#insn-00a4fe80) · [`00a4fe90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md#insn-00a4fe90)

~~~diff
- 00a4fe2c ["INT_ADD", "register:40f0:8", ["const:a4fe2c:8", "const:4:8"]]
- 00a4fe2c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a4fe70 ["INT_ADD", "register:40f0:8", ["const:a4fe70:8", "const:4:8"]]
+ 00a4fe70 ["CALL", null, ["callee:00bdb060:8"]]
- 00a4fe2c bytes 792c0694
+ 00a4fe70 bytes 7c2c0694
- 00a4fe3c ["INT_ADD", "register:40f0:8", ["const:a4fe3c:8", "const:4:8"]]
- 00a4fe3c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a4fe80 ["INT_ADD", "register:40f0:8", ["const:a4fe80:8", "const:4:8"]]
+ 00a4fe80 ["CALL", null, ["callee:00bdb060:8"]]
- 00a4fe3c bytes 752c0694
+ 00a4fe80 bytes 782c0694
- 00a4fe4c ["INT_ADD", "register:40f0:8", ["const:a4fe4c:8", "const:4:8"]]
- 00a4fe4c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a4fe90 ["INT_ADD", "register:40f0:8", ["const:a4fe90:8", "const:4:8"]]
+ 00a4fe90 ["CALL", null, ["callee:00bdb060:8"]]
- 00a4fe4c bytes 712c0694
+ 00a4fe90 bytes 742c0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84fb7b7d47d30a63e29e97032a248f06"></a>

### [`00a50240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50240.md) → [`00a50284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a50284.md) FUN_00a50284

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a50278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50240.md#insn-00a50278)
- 新版 [`00a502bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a50284.md#insn-00a502bc)

~~~diff
- 00a50278 ["INT_ADD", "register:40f0:8", ["const:a50278:8", "const:4:8"]]
- 00a50278 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a502bc ["INT_ADD", "register:40f0:8", ["const:a502bc:8", "const:4:8"]]
+ 00a502bc ["CALL", null, ["callee:00bdb060:8"]]
- 00a50278 bytes 662b0694
+ 00a502bc bytes 692b0694
~~~


<a id="compare-db157c03f105a4c6640007769fddd996"></a>

### [`00a50290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50290.md) → [`00a502d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md) FUN_00a502d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00a4967c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a49/00a4967c.md) [`00a4a240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4a/00a4a240.md) [`00a50290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50290.md) · 呼出先 2件 [`00a50290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50290.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 3件 [`00a496c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a496c0.md) [`00a4a284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a284.md) [`00a502d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md) · 呼出先 2件 [`00a502d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a502ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50290.md#insn-00a502ac) · [`00a502b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50290.md#insn-00a502b8) · [`00a502c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a50/00a50290.md#insn-00a502c8)
- 新版 [`00a502f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md#insn-00a502f0) · [`00a502fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md#insn-00a502fc) · [`00a5030c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md#insn-00a5030c)

~~~diff
- 00a502ac ["INT_ADD", "register:40f0:8", ["const:a502ac:8", "const:4:8"]]
- 00a502ac ["CALL", null, ["local:b0:8"]]
+ 00a502f0 ["INT_ADD", "register:40f0:8", ["const:a502f0:8", "const:4:8"]]
+ 00a502f0 ["CALL", null, ["local:b0:8"]]
- 00a502ac bytes f9ffff97
+ 00a502f0 bytes f9ffff97
- 00a502b8 ["INT_ADD", "register:40f0:8", ["const:a502b8:8", "const:4:8"]]
- 00a502b8 ["CALL", null, ["local:b0:8"]]
+ 00a502fc ["INT_ADD", "register:40f0:8", ["const:a502fc:8", "const:4:8"]]
+ 00a502fc ["CALL", null, ["local:b0:8"]]
- 00a502b8 bytes f6ffff97
+ 00a502fc bytes f6ffff97
- 00a502c8 ["INT_ADD", "register:40f0:8", ["const:a502c8:8", "const:4:8"]]
- 00a502c8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a5030c ["INT_ADD", "register:40f0:8", ["const:a5030c:8", "const:4:8"]]
+ 00a5030c ["CALL", null, ["callee:00bdb060:8"]]
- 00a502c8 bytes 522b0694
+ 00a5030c bytes 552b0694
~~~


<a id="compare-f3ea08491168e0308468687e5133716a"></a>

### [`00a51dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a51dbc.md) → [`00a51e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a51e00.md) FUN_00a51e00

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a52710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52710.md) [`00a52904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52904.md) · 呼出先 11件 [`006fe598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006fe598.md) [`006fe610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006fe610.md) [`007cd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd120.md) [`007cd2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd2ac.md) [`007cea80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007cea80.md)
- 新版 呼出元 2件 [`00a52754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52754.md) [`00a52948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52948.md) · 呼出先 11件 [`006fe598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe598.md) [`006fe610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe610.md) [`007cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd120.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cea80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a51e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a51dbc.md#insn-00a51e28) · [`00a51e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a51dbc.md#insn-00a51e3c) · [`00a51e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a51dbc.md#insn-00a51e44)
- 新版 [`00a51e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a51e00.md#insn-00a51e6c) · [`00a51e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a51e00.md#insn-00a51e80) · [`00a51e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a51e00.md#insn-00a51e88)

~~~diff
- 00a51e28 ["INT_ADD", "register:40f0:8", ["const:a51e28:8", "const:4:8"]]
- 00a51e28 ["CALL", null, ["callee:0081f580:8"]]
+ 00a51e6c ["INT_ADD", "register:40f0:8", ["const:a51e6c:8", "const:4:8"]]
+ 00a51e6c ["CALL", null, ["callee:0081f580:8"]]
- 00a51e28 bytes d635f797
+ 00a51e6c bytes c535f797
- 00a51e3c ["INT_ADD", "register:40f0:8", ["const:a51e3c:8", "const:4:8"]]
- 00a51e3c ["CALL", null, ["callee:006fe598:8"]]
+ 00a51e80 ["INT_ADD", "register:40f0:8", ["const:a51e80:8", "const:4:8"]]
+ 00a51e80 ["CALL", null, ["callee:006fe598:8"]]
- 00a51e3c bytes d7b1f297
+ 00a51e80 bytes c6b1f297
- 00a51e44 ["INT_ADD", "register:40f0:8", ["const:a51e44:8", "const:4:8"]]
- 00a51e44 ["CALL", null, ["callee:0081f580:8"]]
+ 00a51e88 ["INT_ADD", "register:40f0:8", ["const:a51e88:8", "const:4:8"]]
+ 00a51e88 ["CALL", null, ["callee:0081f580:8"]]
- 00a51e44 bytes cf35f797
+ 00a51e88 bytes be35f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bea9076281acdc60a1a6dc7dd6faef6a"></a>

### [`00a52254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52254.md) → [`00a52298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52298.md) FUN_00a52298

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`007f226c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f2/007f226c.md) [`007f24c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f2/007f24c4.md) [`007f534c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f534c.md) [`007fb9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb9f4.md) [`007fca38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fc/007fca38.md) · 呼出先 13件 [`006fd890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd890.md) [`007cd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd120.md) [`007ced74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007ced74.md) [`007cefe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007cefe0.md) [`007cf2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf2e8.md)
- 新版 呼出元 8件 [`007f226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f226c.md) [`007f24c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f24c4.md) [`007f534c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f534c.md) [`007fb9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb9f4.md) [`007fca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fca38.md) · 呼出先 13件 [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`007cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd120.md) [`007ced74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007ced74.md) [`007cefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cefe0.md) [`007cf2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf2e8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a522ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52254.md#insn-00a522ac) · [`00a522c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52254.md#insn-00a522c0) · [`00a52300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52254.md#insn-00a52300)
- 新版 [`00a522f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52298.md#insn-00a522f0) · [`00a52304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52298.md#insn-00a52304) · [`00a52344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52298.md#insn-00a52344)

~~~diff
- 00a522ac ["INT_ADD", "register:40f0:8", ["const:a522ac:8", "const:4:8"]]
- 00a522ac ["CALL", null, ["callee:007d1ffc:8"]]
+ 00a522f0 ["INT_ADD", "register:40f0:8", ["const:a522f0:8", "const:4:8"]]
+ 00a522f0 ["CALL", null, ["callee:007d1ffc:8"]]
- 00a522ac bytes 54fff597
+ 00a522f0 bytes 43fff597
- 00a522c0 ["INT_ADD", "register:40f0:8", ["const:a522c0:8", "const:4:8"]]
- 00a522c0 ["CALL", null, ["callee:007d1ffc:8"]]
+ 00a52304 ["INT_ADD", "register:40f0:8", ["const:a52304:8", "const:4:8"]]
+ 00a52304 ["CALL", null, ["callee:007d1ffc:8"]]
- 00a522c0 bytes 4ffff597
+ 00a52304 bytes 3efff597
- 00a52300 ["INT_ADD", "register:40f0:8", ["const:a52300:8", "const:4:8"]]
- 00a52300 ["CALL", null, ["callee:007d3cf0:8"]]
+ 00a52344 ["INT_ADD", "register:40f0:8", ["const:a52344:8", "const:4:8"]]
+ 00a52344 ["CALL", null, ["callee:007d3cf0:8"]]
- 00a52300 bytes 7c06f697
+ 00a52344 bytes 6b06f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-355f4737c095ec197d85c7d4f31e9b2b"></a>

### [`00a53454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53454.md) → [`00a53498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53498.md) FUN_00a53498

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a53778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53778.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a53480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53454.md#insn-00a53480)
- 新版 [`00a534c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53498.md#insn-00a534c4)

~~~diff
- 00a53480 ["INT_ADD", "register:40f0:8", ["const:a53480:8", "const:4:8"]]
- 00a53480 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a534c4 ["INT_ADD", "register:40f0:8", ["const:a534c4:8", "const:4:8"]]
+ 00a534c4 ["CALL", null, ["callee:00bdb060:8"]]
- 00a53480 bytes e41e0694
+ 00a534c4 bytes e71e0694
~~~


<a id="compare-ef46e086b883153101948f07fc37f4fe"></a>

### [`00a534b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a534b4.md) → [`00a534f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md) FUN_00a534f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a52710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52710.md) [`00a52904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52904.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00a535d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a535d0.md) [`00a53778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53778.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00a52754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52754.md) [`00a52948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52948.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a53614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53614.md) [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a53510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a534b4.md#insn-00a53510) · [`00a53538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a534b4.md#insn-00a53538) · [`00a53564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a534b4.md#insn-00a53564)
- 新版 [`00a53554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md#insn-00a53554) · [`00a5357c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md#insn-00a5357c) · [`00a535a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md#insn-00a535a8)

~~~diff
- 00a53510 ["INT_ADD", "register:40f0:8", ["const:a53510:8", "const:4:8"]]
- 00a53510 ["CALL", null, ["callee:00a53614:8"]]
+ 00a53554 ["INT_ADD", "register:40f0:8", ["const:a53554:8", "const:4:8"]]
+ 00a53554 ["CALL", null, ["callee:00a53614:8"]]
- 00a53510 bytes 30000094
+ 00a53554 bytes 30000094
- 00a53538 ["INT_ADD", "register:40f0:8", ["const:a53538:8", "const:4:8"]]
- 00a53538 ["CALL", null, ["callee:00a537bc:8"]]
+ 00a5357c ["INT_ADD", "register:40f0:8", ["const:a5357c:8", "const:4:8"]]
+ 00a5357c ["CALL", null, ["callee:00a537bc:8"]]
- 00a53538 bytes 90000094
+ 00a5357c bytes 90000094
- 00a53564 ["INT_ADD", "register:40f0:8", ["const:a53564:8", "const:4:8"]]
- 00a53564 ["CALL", null, ["callee:00419064:8"]]
+ 00a535a8 ["INT_ADD", "register:40f0:8", ["const:a535a8:8", "const:4:8"]]
+ 00a535a8 ["CALL", null, ["callee:00419064:8"]]
- 00a53564 bytes c016e797
+ 00a535a8 bytes af16e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb54a54fa8a98d3f81bb87a71dee7a57"></a>

### [`00a54700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a54700.md) → [`00a54744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a54/00a54744.md) FUN_00a54744

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`00647388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md) [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) · 呼出先 1件 [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md)
- 新版 呼出元 18件 [`00647388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md) [`006584d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) · 呼出先 1件 [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a54710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a54700.md#insn-00a54710)
- 新版 [`00a54754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a54/00a54744.md#insn-00a54754)

~~~diff
- 00a54710 ["INT_ADD", "register:40f0:8", ["const:a54710:8", "const:4:8"]]
- 00a54710 ["CALL", null, ["callee:00821cb4:8"]]
+ 00a54754 ["INT_ADD", "register:40f0:8", ["const:a54754:8", "const:4:8"]]
+ 00a54754 ["CALL", null, ["callee:00821cb4:8"]]
- 00a54710 bytes 6935f797
+ 00a54754 bytes 5835f797
~~~


<a id="compare-e1e62525324c2c8f91e8551b1cfe59f5"></a>

### [`00a5b084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b084.md) → [`00a5b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md) FUN_00a5b0c8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`0058b7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058b/0058b7d4.md) [`0058b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058b/0058b8ec.md) [`0058ba50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058b/0058ba50.md) [`0058bad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058b/0058bad0.md) [`0058bef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058b/0058bef8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 17件 [`0058b7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b7d4.md) [`0058b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b8ec.md) [`0058ba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058ba50.md) [`0058bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058bad0.md) [`0058bef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058bef8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5b144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b084.md#insn-00a5b144) · [`00a5b160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b084.md#insn-00a5b160)
- 新版 [`00a5b188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md#insn-00a5b188) · [`00a5b1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md#insn-00a5b1a4)

~~~diff
- 00a5b144 ["INT_ADD", "register:40f0:8", ["const:a5b144:8", "const:4:8"]]
- 00a5b144 ["CALL", null, ["callee:0081f580:8"]]
+ 00a5b188 ["INT_ADD", "register:40f0:8", ["const:a5b188:8", "const:4:8"]]
+ 00a5b188 ["CALL", null, ["callee:0081f580:8"]]
- 00a5b144 bytes 0f11f797
+ 00a5b188 bytes fe10f797
- 00a5b160 ["INT_ADD", "register:40f0:8", ["const:a5b160:8", "const:4:8"]]
- 00a5b160 ["CALL", null, ["callee:0081f580:8"]]
+ 00a5b1a4 ["INT_ADD", "register:40f0:8", ["const:a5b1a4:8", "const:4:8"]]
+ 00a5b1a4 ["CALL", null, ["callee:0081f580:8"]]
- 00a5b160 bytes 0811f797
+ 00a5b1a4 bytes f710f797
~~~


<a id="compare-bc9ef240306c38073c497171f10932c8"></a>

### [`00a5b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b3c0.md) → [`00a5b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b404.md) FUN_00a5b404

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5a6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a6ac.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00a5b550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b550.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a5a6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00a5b594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b594.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5b448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b3c0.md#insn-00a5b448) · [`00a5b50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b3c0.md#insn-00a5b50c) · [`00a5b528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b3c0.md#insn-00a5b528)
- 新版 [`00a5b48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b404.md#insn-00a5b48c) · [`00a5b550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b404.md#insn-00a5b550) · [`00a5b56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b404.md#insn-00a5b56c)

~~~diff
- 00a5b448 ["INT_ADD", "register:40f0:8", ["const:a5b448:8", "const:4:8"]]
- 00a5b448 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a5b48c ["INT_ADD", "register:40f0:8", ["const:a5b48c:8", "const:4:8"]]
+ 00a5b48c ["CALL", null, ["callee:00bdb040:8"]]
- 00a5b448 bytes eafe0594
+ 00a5b48c bytes edfe0594
- 00a5b50c ["INT_ADD", "register:40f0:8", ["const:a5b50c:8", "const:4:8"]]
- 00a5b50c ["CALL", null, ["callee:00bdb060:8"]]
+ 00a5b550 ["INT_ADD", "register:40f0:8", ["const:a5b550:8", "const:4:8"]]
+ 00a5b550 ["CALL", null, ["callee:00bdb060:8"]]
- 00a5b50c bytes c1fe0594
+ 00a5b550 bytes c4fe0594
- 00a5b528 ["INT_ADD", "register:40f0:8", ["const:a5b528:8", "const:4:8"]]
- 00a5b528 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a5b56c ["INT_ADD", "register:40f0:8", ["const:a5b56c:8", "const:4:8"]]
+ 00a5b56c ["CALL", null, ["callee:00bdb060:8"]]
- 00a5b528 bytes bafe0594
+ 00a5b56c bytes bdfe0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5b5159162c00100f769a9385c80d7e5"></a>

### [`00a5b564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b564.md) → [`00a5b5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5a8.md) FUN_00a5b5a8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5b5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b564.md#insn-00a5b5a4)
- 新版 [`00a5b5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5a8.md#insn-00a5b5e8)

~~~diff
- 00a5b5a4 ["INT_ADD", "register:40f0:8", ["const:a5b5a4:8", "const:4:8"]]
- 00a5b5a4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a5b5e8 ["INT_ADD", "register:40f0:8", ["const:a5b5e8:8", "const:4:8"]]
+ 00a5b5e8 ["CALL", null, ["callee:00bdb060:8"]]
- 00a5b5a4 bytes 9bfe0594
+ 00a5b5e8 bytes 9efe0594
~~~


<a id="compare-01da3aa6f3ebeb77f89e592b091d0767"></a>

### [`00a5b5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b5b8.md) → [`00a5b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md) FUN_00a5b5fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5a6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a6ac.md) · 呼出先 6件 [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00a5b550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b550.md) [`00a5b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b838.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00a5a6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md) · 呼出先 6件 [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00a5b594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b594.md) [`00a5b87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b87c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5b638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b5b8.md#insn-00a5b638) · [`00a5b6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b5b8.md#insn-00a5b6bc) · [`00a5b71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b5b8.md#insn-00a5b71c)
- 新版 [`00a5b67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md#insn-00a5b67c) · [`00a5b700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md#insn-00a5b700) · [`00a5b760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md#insn-00a5b760)

~~~diff
- 00a5b638 ["INT_ADD", "register:40f0:8", ["const:a5b638:8", "const:4:8"]]
- 00a5b638 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a5b67c ["INT_ADD", "register:40f0:8", ["const:a5b67c:8", "const:4:8"]]
+ 00a5b67c ["CALL", null, ["callee:00bdb060:8"]]
- 00a5b638 bytes 76fe0594
+ 00a5b67c bytes 79fe0594
- 00a5b6bc ["INT_ADD", "register:40f0:8", ["const:a5b6bc:8", "const:4:8"]]
- 00a5b6bc ["CALL", null, ["callee:0044dabc:8"]]
+ 00a5b700 ["INT_ADD", "register:40f0:8", ["const:a5b700:8", "const:4:8"]]
+ 00a5b700 ["CALL", null, ["callee:0044dabc:8"]]
- 00a5b6bc bytes 00c9e797
+ 00a5b700 bytes efc8e797
- 00a5b71c ["INT_ADD", "register:40f0:8", ["const:a5b71c:8", "const:4:8"]]
- 00a5b71c ["CALL", null, ["callee:0044dabc:8"]]
+ 00a5b760 ["INT_ADD", "register:40f0:8", ["const:a5b760:8", "const:4:8"]]
+ 00a5b760 ["CALL", null, ["callee:0044dabc:8"]]
- 00a5b71c bytes e8c8e797
+ 00a5b760 bytes d7c8e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279b5b49365ca43fd20de42573623b51"></a>

### [`00a5b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b838.md) → [`00a5b87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b87c.md) FUN_00a5b87c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5b5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b5b8.md) · 呼出先 4件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00a5b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md) · 呼出先 4件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5b8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b838.md#insn-00a5b8d8) · [`00a5b8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b838.md#insn-00a5b8f0) · [`00a5b940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b838.md#insn-00a5b940)
- 新版 [`00a5b91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b87c.md#insn-00a5b91c) · [`00a5b934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b87c.md#insn-00a5b934) · [`00a5b984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b87c.md#insn-00a5b984)

~~~diff
- 00a5b8d8 ["INT_ADD", "register:40f0:8", ["const:a5b8d8:8", "const:4:8"]]
- 00a5b8d8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a5b91c ["INT_ADD", "register:40f0:8", ["const:a5b91c:8", "const:4:8"]]
+ 00a5b91c ["CALL", null, ["callee:00bdb040:8"]]
- 00a5b8d8 bytes c6fd0594
+ 00a5b91c bytes c9fd0594
- 00a5b8f0 ["INT_ADD", "register:40f0:8", ["const:a5b8f0:8", "const:4:8"]]
- 00a5b8f0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00a5b934 ["INT_ADD", "register:40f0:8", ["const:a5b934:8", "const:4:8"]]
+ 00a5b934 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00a5b8f0 bytes 1cfe0594
+ 00a5b934 bytes 1ffe0594
- 00a5b940 ["INT_ADD", "register:40f0:8", ["const:a5b940:8", "const:4:8"]]
- 00a5b940 ["CALL", null, ["callee:0044d968:8"]]
+ 00a5b984 ["INT_ADD", "register:40f0:8", ["const:a5b984:8", "const:4:8"]]
+ 00a5b984 ["CALL", null, ["callee:0044d968:8"]]
- 00a5b940 bytes 0ac8e797
+ 00a5b984 bytes f9c7e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d74f3da7ce8ab3bc1e101a994725847b"></a>

### [`00a5c504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c504.md) → [`00a5c548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c548.md) FUN_00a5c548

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007999cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00ade5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md)
- 新版 呼出元 6件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007999cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/007999cc.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c504.md#insn-00a5c50c)
- 新版 [`00a5c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c548.md#insn-00a5c550)

~~~diff
- 00a5c50c ["INT_ADD", "register:40f0:8", ["const:a5c50c:8", "const:4:8"]]
- 00a5c50c ["CALL", null, ["callee:0081f580:8"]]
+ 00a5c550 ["INT_ADD", "register:40f0:8", ["const:a5c550:8", "const:4:8"]]
+ 00a5c550 ["CALL", null, ["callee:0081f580:8"]]
- 00a5c50c bytes 1d0cf797
+ 00a5c550 bytes 0c0cf797
~~~


<a id="compare-fd30db0162704d8ebb9bf101c243d02a"></a>

### [`00a5c524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c524.md) → [`00a5c568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c568.md) FUN_00a5c568

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007999cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md) · 呼出先 1件 [`00a5cf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cf2c.md)
- 新版 呼出元 1件 [`007999cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/007999cc.md) · 呼出先 1件 [`00a5cf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cf70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5c52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c524.md#insn-00a5c52c)
- 新版 [`00a5c570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c568.md#insn-00a5c570)

~~~diff
- 00a5c52c ["INT_ADD", "register:40f0:8", ["const:a5c52c:8", "const:4:8"]]
- 00a5c52c ["CALL", null, ["callee:00a5cf70:8"]]
+ 00a5c570 ["INT_ADD", "register:40f0:8", ["const:a5c570:8", "const:4:8"]]
+ 00a5c570 ["CALL", null, ["callee:00a5cf70:8"]]
- 00a5c52c bytes 80020094
+ 00a5c570 bytes 80020094
~~~


<a id="compare-def5095ee3e3b786ab98393303a8fd46"></a>

### [`00a5c568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c568.md) → [`00a5c5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5ac.md) FUN_00a5c5ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5c580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c568.md#insn-00a5c580) · [`00a5c58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c568.md#insn-00a5c58c)
- 新版 [`00a5c5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5ac.md#insn-00a5c5c4) · [`00a5c5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5ac.md#insn-00a5c5d0)

~~~diff
- 00a5c580 ["INT_ADD", "register:40f0:8", ["const:a5c580:8", "const:4:8"]]
- 00a5c580 ["CALL", null, ["callee:0045d518:8"]]
+ 00a5c5c4 ["INT_ADD", "register:40f0:8", ["const:a5c5c4:8", "const:4:8"]]
+ 00a5c5c4 ["CALL", null, ["callee:0045d518:8"]]
- 00a5c580 bytes e603e897
+ 00a5c5c4 bytes d503e897
- 00a5c58c ["INT_ADD", "register:40f0:8", ["const:a5c58c:8", "const:4:8"]]
- 00a5c58c ["CALL", null, ["callee:0045d518:8"]]
+ 00a5c5d0 ["INT_ADD", "register:40f0:8", ["const:a5c5d0:8", "const:4:8"]]
+ 00a5c5d0 ["CALL", null, ["callee:0045d518:8"]]
- 00a5c58c bytes e303e897
+ 00a5c5d0 bytes d203e897
~~~


<a id="compare-16f87f5397ce83c7a8e8bb0ee41978c6"></a>

### [`00a5c5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c5a0.md) → [`00a5c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5e4.md) FUN_00a5c5e4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ce/009ce1d0.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5c5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c5a0.md#insn-00a5c5c0)
- 新版 [`00a5c604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c5e4.md#insn-00a5c604)

~~~diff
- 00a5c5c0 ["INT_ADD", "register:40f0:8", ["const:a5c5c0:8", "const:4:8"]]
- 00a5c5c0 ["CALL", null, ["callee:0045df50:8"]]
+ 00a5c604 ["INT_ADD", "register:40f0:8", ["const:a5c604:8", "const:4:8"]]
+ 00a5c604 ["CALL", null, ["callee:0045df50:8"]]
- 00a5c5c0 bytes 6406e897
+ 00a5c604 bytes 5306e897
~~~


<a id="compare-8cf247aa7965c85386b7198cdcc4f15f"></a>

### [`00a5cd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cd84.md) → [`00a5cdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cdc8.md) FUN_00a5cdc8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00a26cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26cbc.md) [`00a271c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md) [`00a28640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28640.md) [`00a28744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 4件 [`00a26d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26d00.md) [`00a2720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a27/00a2720c.md) [`00a28684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28684.md) [`00a28788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28788.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5cdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cd84.md#insn-00a5cdb0) · [`00a5cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cd84.md#insn-00a5cde4) · [`00a5ce38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cd84.md#insn-00a5ce38)
- 新版 [`00a5cdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cdc8.md#insn-00a5cdf4) · [`00a5ce28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cdc8.md#insn-00a5ce28) · [`00a5ce7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cdc8.md#insn-00a5ce7c)

~~~diff
- 00a5cdb0 ["INT_ADD", "register:40f0:8", ["const:a5cdb0:8", "const:4:8"]]
- 00a5cdb0 ["CALL", null, ["callee:00419064:8"]]
+ 00a5cdf4 ["INT_ADD", "register:40f0:8", ["const:a5cdf4:8", "const:4:8"]]
+ 00a5cdf4 ["CALL", null, ["callee:00419064:8"]]
- 00a5cdb0 bytes adf0e697
+ 00a5cdf4 bytes 9cf0e697
- 00a5cde4 ["INT_ADD", "register:40f0:8", ["const:a5cde4:8", "const:4:8"]]
- 00a5cde4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a5ce28 ["INT_ADD", "register:40f0:8", ["const:a5ce28:8", "const:4:8"]]
+ 00a5ce28 ["CALL", null, ["callee:0081f580:8"]]
- 00a5cde4 bytes e709f797
+ 00a5ce28 bytes d609f797
- 00a5ce38 ["INT_ADD", "register:40f0:8", ["const:a5ce38:8", "const:4:8"]]
- 00a5ce38 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a5ce7c ["INT_ADD", "register:40f0:8", ["const:a5ce7c:8", "const:4:8"]]
+ 00a5ce7c ["CALL", null, ["callee:00bdb040:8"]]
- 00a5ce38 bytes 6ef80594
+ 00a5ce7c bytes 71f80594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1663f8340de2d31aac64fb42bf56cc4"></a>

### [`00a5cf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cf2c.md) → [`00a5cf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cf70.md) FUN_00a5cf70

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) [`007999cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) [`0099a654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0099a/0099a654.md) [`00a5c524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c524.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 6件 [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`007999cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/007999cc.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) [`00a5c568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c568.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5cf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cf2c.md#insn-00a5cf44) · [`00a5cf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cf2c.md#insn-00a5cf64) · [`00a5cf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cf2c.md#insn-00a5cf90)
- 新版 [`00a5cf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cf70.md#insn-00a5cf88) · [`00a5cfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cf70.md#insn-00a5cfa8) · [`00a5cfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cf70.md#insn-00a5cfd4)

~~~diff
- 00a5cf44 ["INT_ADD", "register:40f0:8", ["const:a5cf44:8", "const:4:8"]]
- 00a5cf44 ["CALL", null, ["callee:0081f580:8"]]
+ 00a5cf88 ["INT_ADD", "register:40f0:8", ["const:a5cf88:8", "const:4:8"]]
+ 00a5cf88 ["CALL", null, ["callee:0081f580:8"]]
- 00a5cf44 bytes 8f09f797
+ 00a5cf88 bytes 7e09f797
- 00a5cf64 ["INT_ADD", "register:40f0:8", ["const:a5cf64:8", "const:4:8"]]
- 00a5cf64 ["CALL", null, ["callee:0081f580:8"]]
+ 00a5cfa8 ["INT_ADD", "register:40f0:8", ["const:a5cfa8:8", "const:4:8"]]
+ 00a5cfa8 ["CALL", null, ["callee:0081f580:8"]]
- 00a5cf64 bytes 8709f797
+ 00a5cfa8 bytes 7609f797
- 00a5cf90 ["INT_ADD", "register:40f0:8", ["const:a5cf90:8", "const:4:8"]]
- 00a5cf90 ["CALL", null, ["callee:0081f580:8"]]
+ 00a5cfd4 ["INT_ADD", "register:40f0:8", ["const:a5cfd4:8", "const:4:8"]]
+ 00a5cfd4 ["CALL", null, ["callee:0081f580:8"]]
- 00a5cf90 bytes 7c09f797
+ 00a5cfd4 bytes 6b09f797
~~~


<a id="compare-bcefe7618b192bf63e7e8e8a7b8231f9"></a>

### [`00a5e61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e61c.md) → [`00a5e660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md) FUN_00a5e660

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md) · 呼出先 4件 [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md) · 呼出先 4件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e61c.md#insn-00a5e648) · [`00a5e65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e61c.md#insn-00a5e65c) · [`00a5e670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e61c.md#insn-00a5e670)
- 新版 [`00a5e68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md#insn-00a5e68c) · [`00a5e6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md#insn-00a5e6a0) · [`00a5e6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md#insn-00a5e6b4)

~~~diff
- 00a5e648 ["INT_ADD", "register:40f0:8", ["const:a5e648:8", "const:4:8"]]
- 00a5e648 ["CALL", null, ["callee:00464a54:8"]]
+ 00a5e68c ["INT_ADD", "register:40f0:8", ["const:a5e68c:8", "const:4:8"]]
+ 00a5e68c ["CALL", null, ["callee:00464a54:8"]]
- 00a5e648 bytes 0319e897
+ 00a5e68c bytes f218e897
- 00a5e65c ["INT_ADD", "register:40f0:8", ["const:a5e65c:8", "const:4:8"]]
- 00a5e65c ["CALL", null, ["callee:00464b8c:8"]]
+ 00a5e6a0 ["INT_ADD", "register:40f0:8", ["const:a5e6a0:8", "const:4:8"]]
+ 00a5e6a0 ["CALL", null, ["callee:00464b8c:8"]]
- 00a5e65c bytes 4c19e897
+ 00a5e6a0 bytes 3b19e897
- 00a5e670 ["INT_ADD", "register:40f0:8", ["const:a5e670:8", "const:4:8"]]
- 00a5e670 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a5e6b4 ["INT_ADD", "register:40f0:8", ["const:a5e6b4:8", "const:4:8"]]
+ 00a5e6b4 ["CALL", null, ["callee:00bdb060:8"]]
- 00a5e670 bytes 68f20594
+ 00a5e6b4 bytes 6bf20594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b902c4b52b1d20fab9ef36b0531dd3f1"></a>

### [`00a5e6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e6e0.md) → [`00a5e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md) FUN_00a5e724

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a601cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a601cc.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044ab70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab70.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`005f0450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0450.md)
- 新版 呼出元 1件 [`00a60210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005f0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e6e0.md#insn-00a5e71c) · [`00a5e764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e6e0.md#insn-00a5e764) · [`00a5e780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e6e0.md#insn-00a5e780)
- 新版 [`00a5e760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md#insn-00a5e760) · [`00a5e7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md#insn-00a5e7a8) · [`00a5e7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md#insn-00a5e7c4)

~~~diff
- 00a5e71c ["INT_ADD", "register:40f0:8", ["const:a5e71c:8", "const:4:8"]]
- 00a5e71c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a5e760 ["INT_ADD", "register:40f0:8", ["const:a5e760:8", "const:4:8"]]
+ 00a5e760 ["CALL", null, ["callee:00bdb040:8"]]
- 00a5e71c bytes 35f20594
+ 00a5e760 bytes 38f20594
- 00a5e764 ["INT_ADD", "register:40f0:8", ["const:a5e764:8", "const:4:8"]]
- 00a5e764 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a5e7a8 ["INT_ADD", "register:40f0:8", ["const:a5e7a8:8", "const:4:8"]]
+ 00a5e7a8 ["CALL", null, ["callee:00bdb040:8"]]
- 00a5e764 bytes 23f20594
+ 00a5e7a8 bytes 26f20594
- 00a5e780 ["INT_ADD", "register:40f0:8", ["const:a5e780:8", "const:4:8"]]
- 00a5e780 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a5e7c4 ["INT_ADD", "register:40f0:8", ["const:a5e7c4:8", "const:4:8"]]
+ 00a5e7c4 ["CALL", null, ["callee:00bdb040:8"]]
- 00a5e780 bytes 1cf20594
+ 00a5e7c4 bytes 1ff20594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b1436a00ff9870a250e6bd8be721dd"></a>

### [`00a5ecbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5ecbc.md) → [`00a5ed00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md) FUN_00a5ed00

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5e6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e6e0.md) · 呼出先 5件 [`007cd2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd2ac.md) [`007cd560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd560.md) [`007d22d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d22d4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a08564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a08/00a08564.md)
- 新版 呼出元 1件 [`00a5e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md) · 呼出先 5件 [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd560.md) [`007d22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d22d4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a085a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a085a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5ece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5ecbc.md#insn-00a5ece0) · [`00a5ecec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5ecbc.md#insn-00a5ecec) · [`00a5ed08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5ecbc.md#insn-00a5ed08)
- 新版 [`00a5ed24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md#insn-00a5ed24) · [`00a5ed30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md#insn-00a5ed30) · [`00a5ed4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md#insn-00a5ed4c)

~~~diff
- 00a5ece0 ["INT_ADD", "register:40f0:8", ["const:a5ece0:8", "const:4:8"]]
- 00a5ece0 ["CALL", null, ["callee:007cd2ac:8"]]
+ 00a5ed24 ["INT_ADD", "register:40f0:8", ["const:a5ed24:8", "const:4:8"]]
+ 00a5ed24 ["CALL", null, ["callee:007cd2ac:8"]]
- 00a5ece0 bytes 73b9f597
+ 00a5ed24 bytes 62b9f597
- 00a5ecec ["INT_ADD", "register:40f0:8", ["const:a5ecec:8", "const:4:8"]]
- 00a5ecec ["CALL", null, ["callee:007cd560:8"]]
+ 00a5ed30 ["INT_ADD", "register:40f0:8", ["const:a5ed30:8", "const:4:8"]]
+ 00a5ed30 ["CALL", null, ["callee:007cd560:8"]]
- 00a5ecec bytes 1dbaf597
+ 00a5ed30 bytes 0cbaf597
- 00a5ed08 ["INT_ADD", "register:40f0:8", ["const:a5ed08:8", "const:4:8"]]
- 00a5ed08 ["CALL", null, ["callee:007d22d4:8"]]
+ 00a5ed4c ["INT_ADD", "register:40f0:8", ["const:a5ed4c:8", "const:4:8"]]
+ 00a5ed4c ["CALL", null, ["callee:007d22d4:8"]]
- 00a5ed08 bytes 73cdf597
+ 00a5ed4c bytes 62cdf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9376af3b3c4db492fa9e58c974ce2ed"></a>

### [`00a5f0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0a0.md) → [`00a5f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f0e4.md) FUN_00a5f0e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00704f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00704/00704f50.md) [`00705000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00705/00705000.md) [`00706234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706234.md) [`007072cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007072cc.md) [`007073e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007073e8.md) · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 5件 [`00704f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704f50.md) [`00705000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00705/00705000.md) [`00706234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706234.md) [`007072cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007072cc.md) [`007073e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007073e8.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5f0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0a0.md#insn-00a5f0c0)
- 新版 [`00a5f104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f0e4.md#insn-00a5f104)

~~~diff
- 00a5f0c0 ["INT_ADD", "register:40f0:8", ["const:a5f0c0:8", "const:4:8"]]
- 00a5f0c0 ["CALL", null, ["callee:00bdb600:8"]]
+ 00a5f104 ["INT_ADD", "register:40f0:8", ["const:a5f104:8", "const:4:8"]]
+ 00a5f104 ["CALL", null, ["callee:00bdb600:8"]]
- 00a5f0c0 bytes 3cf10594
+ 00a5f104 bytes 3ff10594
~~~


<a id="compare-feab8fdc3a36a6425c4ff694fad3d740"></a>

### [`00a5f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0e4.md) → [`00a5f128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md) FUN_00a5f128

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a60600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60600.md) [`00a63b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63b48.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044ab70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab70.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`005f0450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0450.md)
- 新版 呼出元 2件 [`00a60644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md) [`00a63b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b8c.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005f0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5f120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0e4.md#insn-00a5f120) · [`00a5f128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0e4.md#insn-00a5f128) · [`00a5f1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0e4.md#insn-00a5f1c0)
- 新版 [`00a5f164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md#insn-00a5f164) · [`00a5f16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md#insn-00a5f16c) · [`00a5f204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md#insn-00a5f204)

~~~diff
- 00a5f120 ["INT_ADD", "register:40f0:8", ["const:a5f120:8", "const:4:8"]]
- 00a5f120 ["CALL", null, ["callee:0081f580:8"]]
+ 00a5f164 ["INT_ADD", "register:40f0:8", ["const:a5f164:8", "const:4:8"]]
+ 00a5f164 ["CALL", null, ["callee:0081f580:8"]]
- 00a5f120 bytes 1801f797
+ 00a5f164 bytes 0701f797
- 00a5f128 ["INT_ADD", "register:40f0:8", ["const:a5f128:8", "const:4:8"]]
- 00a5f128 ["CALL", null, ["callee:0082e5d0:8"]]
+ 00a5f16c ["INT_ADD", "register:40f0:8", ["const:a5f16c:8", "const:4:8"]]
+ 00a5f16c ["CALL", null, ["callee:0082e5d0:8"]]
- 00a5f128 bytes 2a3df797
+ 00a5f16c bytes 193df797
- 00a5f1c0 ["INT_ADD", "register:40f0:8", ["const:a5f1c0:8", "const:4:8"]]
- 00a5f1c0 ["CALL", null, ["callee:005f0450:8"]]
+ 00a5f204 ["INT_ADD", "register:40f0:8", ["const:a5f204:8", "const:4:8"]]
+ 00a5f204 ["CALL", null, ["callee:005f0450:8"]]
- 00a5f1c0 bytes a444ee97
+ 00a5f204 bytes 9344ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-202363336d8bb92e730412c4dee12d92"></a>

### [`00a5f500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f500.md) → [`00a5f544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md) FUN_00a5f544

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 3件 [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md) [`0044c020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c020.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 3件 [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5f54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f500.md#insn-00a5f54c) · [`00a5f554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f500.md#insn-00a5f554) · [`00a5f570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f500.md#insn-00a5f570)
- 新版 [`00a5f590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md#insn-00a5f590) · [`00a5f598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md#insn-00a5f598) · [`00a5f5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md#insn-00a5f5b4)

~~~diff
- 00a5f54c ["INT_ADD", "register:40f0:8", ["const:a5f54c:8", "const:4:8"]]
- 00a5f54c ["CALL", null, ["callee:0044c020:8"]]
+ 00a5f590 ["INT_ADD", "register:40f0:8", ["const:a5f590:8", "const:4:8"]]
+ 00a5f590 ["CALL", null, ["callee:0044c020:8"]]
- 00a5f54c bytes b5b2e797
+ 00a5f590 bytes a4b2e797
- 00a5f554 ["INT_ADD", "register:40f0:8", ["const:a5f554:8", "const:4:8"]]
- 00a5f554 ["CALL", null, ["callee:0044b8ec:8"]]
+ 00a5f598 ["INT_ADD", "register:40f0:8", ["const:a5f598:8", "const:4:8"]]
+ 00a5f598 ["CALL", null, ["callee:0044b8ec:8"]]
- 00a5f554 bytes e6b0e797
+ 00a5f598 bytes d5b0e797
- 00a5f570 ["INT_ADD", "register:40f0:8", ["const:a5f570:8", "const:4:8"]]
- 00a5f570 ["CALL", null, ["callee:0059d12c:8"]]
+ 00a5f5b4 ["INT_ADD", "register:40f0:8", ["const:a5f5b4:8", "const:4:8"]]
+ 00a5f5b4 ["CALL", null, ["callee:0059d12c:8"]]
- 00a5f570 bytes eff6ec97
+ 00a5f5b4 bytes def6ec97
~~~


<a id="compare-a55a0736f5bf78f670fcb1d7e2da4488"></a>

### [`00a5f618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f618.md) → [`00a5f65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f65c.md) FUN_00a5f65c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md) · 呼出先 1件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md)
- 新版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 1件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5f640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f618.md#insn-00a5f640)
- 新版 [`00a5f684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f65c.md#insn-00a5f684)

~~~diff
- 00a5f640 ["INT_ADD", "register:40f0:8", ["const:a5f640:8", "const:4:8"]]
- 00a5f640 ["CALL", null, ["callee:0059d12c:8"]]
+ 00a5f684 ["INT_ADD", "register:40f0:8", ["const:a5f684:8", "const:4:8"]]
+ 00a5f684 ["CALL", null, ["callee:0059d12c:8"]]
- 00a5f640 bytes bbf6ec97
+ 00a5f684 bytes aaf6ec97
~~~


<a id="compare-174571bb46cd2ae95bae4d5ff1201d1b"></a>

### [`00a5f674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f674.md) → [`00a5f6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f6b8.md) FUN_00a5f6b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00838234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838234.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00838234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838234.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5f6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f674.md#insn-00a5f6c4)
- 新版 [`00a5f708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f6b8.md#insn-00a5f708)

~~~diff
- 00a5f6c4 ["INT_ADD", "register:40f0:8", ["const:a5f6c4:8", "const:4:8"]]
- 00a5f6c4 ["CALL", null, ["callee:00838234:8"]]
+ 00a5f708 ["INT_ADD", "register:40f0:8", ["const:a5f708:8", "const:4:8"]]
+ 00a5f708 ["CALL", null, ["callee:00838234:8"]]
- 00a5f6c4 bytes dc62f797
+ 00a5f708 bytes cb62f797
~~~


<a id="compare-8f65fd9d06a41e0c38052dcdc7f4e642"></a>

### [`00a5fe60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5fe60.md) → [`00a5fea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md) FUN_00a5fea4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0045d240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d240.md) [`0045d2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d2a0.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045d240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md) [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5fe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5fe60.md#insn-00a5fe8c) · [`00a5fe98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5fe60.md#insn-00a5fe98) · [`00a5fea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5fe60.md#insn-00a5fea4)
- 新版 [`00a5fed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md#insn-00a5fed0) · [`00a5fedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md#insn-00a5fedc) · [`00a5fee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md#insn-00a5fee8)

~~~diff
- 00a5fe8c ["INT_ADD", "register:40f0:8", ["const:a5fe8c:8", "const:4:8"]]
- 00a5fe8c ["CALL", null, ["callee:0045d518:8"]]
+ 00a5fed0 ["INT_ADD", "register:40f0:8", ["const:a5fed0:8", "const:4:8"]]
+ 00a5fed0 ["CALL", null, ["callee:0045d518:8"]]
- 00a5fe8c bytes a3f5e797
+ 00a5fed0 bytes 92f5e797
- 00a5fe98 ["INT_ADD", "register:40f0:8", ["const:a5fe98:8", "const:4:8"]]
- 00a5fe98 ["CALL", null, ["callee:0045d518:8"]]
+ 00a5fedc ["INT_ADD", "register:40f0:8", ["const:a5fedc:8", "const:4:8"]]
+ 00a5fedc ["CALL", null, ["callee:0045d518:8"]]
- 00a5fe98 bytes a0f5e797
+ 00a5fedc bytes 8ff5e797
- 00a5fea4 ["INT_ADD", "register:40f0:8", ["const:a5fea4:8", "const:4:8"]]
- 00a5fea4 ["CALL", null, ["callee:0045d518:8"]]
+ 00a5fee8 ["INT_ADD", "register:40f0:8", ["const:a5fee8:8", "const:4:8"]]
+ 00a5fee8 ["CALL", null, ["callee:0045d518:8"]]
- 00a5fea4 bytes 9df5e797
+ 00a5fee8 bytes 8cf5e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-240a2335a38f599c3563289d63be0de8"></a>

### [`00a600b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a600b8.md) → [`00a600fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md) FUN_00a600fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ce/009ce1d0.md) · 呼出先 4件 [`0045dc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dd10.md) [`0045de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045de70.md)
- 新版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 4件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md) [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a600e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a600b8.md#insn-00a600e0) · [`00a600ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a600b8.md#insn-00a600ec) · [`00a600f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a600b8.md#insn-00a600f8)
- 新版 [`00a60124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md#insn-00a60124) · [`00a60130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md#insn-00a60130) · [`00a6013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md#insn-00a6013c)

~~~diff
- 00a600e0 ["INT_ADD", "register:40f0:8", ["const:a600e0:8", "const:4:8"]]
- 00a600e0 ["CALL", null, ["callee:0045dd10:8"]]
+ 00a60124 ["INT_ADD", "register:40f0:8", ["const:a60124:8", "const:4:8"]]
+ 00a60124 ["CALL", null, ["callee:0045dd10:8"]]
- 00a600e0 bytes 0cf7e797
+ 00a60124 bytes fbf6e797
- 00a600ec ["INT_ADD", "register:40f0:8", ["const:a600ec:8", "const:4:8"]]
- 00a600ec ["CALL", null, ["callee:0045dd10:8"]]
+ 00a60130 ["INT_ADD", "register:40f0:8", ["const:a60130:8", "const:4:8"]]
+ 00a60130 ["CALL", null, ["callee:0045dd10:8"]]
- 00a600ec bytes 09f7e797
+ 00a60130 bytes f8f6e797
- 00a600f8 ["INT_ADD", "register:40f0:8", ["const:a600f8:8", "const:4:8"]]
- 00a600f8 ["CALL", null, ["callee:0045dd10:8"]]
+ 00a6013c ["INT_ADD", "register:40f0:8", ["const:a6013c:8", "const:4:8"]]
+ 00a6013c ["CALL", null, ["callee:0045dd10:8"]]
- 00a600f8 bytes 06f7e797
+ 00a6013c bytes f5f6e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b74998048728104eb43e080d458830da"></a>

### [`00a601cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a601cc.md) → [`00a60210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md) FUN_00a60210

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005ef020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005ef020.md) [`00629194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a45be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a45/00a45be0.md)
- 新版 呼出元 8件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005ef020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ef/005ef020.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a601f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a601cc.md#insn-00a601f0) · [`00a60200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a601cc.md#insn-00a60200) · [`00a60264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a601cc.md#insn-00a60264)
- 新版 [`00a60234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md#insn-00a60234) · [`00a60244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md#insn-00a60244) · [`00a602a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md#insn-00a602a8)

~~~diff
- 00a601f0 ["INT_ADD", "register:40f0:8", ["const:a601f0:8", "const:4:8"]]
- 00a601f0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a60234 ["INT_ADD", "register:40f0:8", ["const:a60234:8", "const:4:8"]]
+ 00a60234 ["CALL", null, ["callee:0081f580:8"]]
- 00a601f0 bytes e4fcf697
+ 00a60234 bytes d3fcf697
- 00a60200 ["INT_ADD", "register:40f0:8", ["const:a60200:8", "const:4:8"]]
- 00a60200 ["CALL", null, ["callee:00ade610:8"]]
+ 00a60244 ["INT_ADD", "register:40f0:8", ["const:a60244:8", "const:4:8"]]
+ 00a60244 ["CALL", null, ["callee:00ade610:8"]]
- 00a60200 bytes f3f80194
+ 00a60244 bytes f3f80194
- 00a60264 ["INT_ADD", "register:40f0:8", ["const:a60264:8", "const:4:8"]]
- 00a60264 ["CALL", null, ["callee:00bdb600:8"]]
+ 00a602a8 ["INT_ADD", "register:40f0:8", ["const:a602a8:8", "const:4:8"]]
+ 00a602a8 ["CALL", null, ["callee:00bdb600:8"]]
- 00a60264 bytes d3ec0594
+ 00a602a8 bytes d6ec0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2557210f2fae3f1f952ad0d7fa837174"></a>

### [`00a60434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60434.md) → [`00a60478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md) FUN_00a60478

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a601cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a601cc.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00a60210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6046c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60434.md#insn-00a6046c) · [`00a604b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60434.md#insn-00a604b4) · [`00a604d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60434.md#insn-00a604d8)
- 新版 [`00a604b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md#insn-00a604b0) · [`00a604f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md#insn-00a604f8) · [`00a6051c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md#insn-00a6051c)

~~~diff
- 00a6046c ["INT_ADD", "register:40f0:8", ["const:a6046c:8", "const:4:8"]]
- 00a6046c ["CALL", null, ["callee:00bdb600:8"]]
+ 00a604b0 ["INT_ADD", "register:40f0:8", ["const:a604b0:8", "const:4:8"]]
+ 00a604b0 ["CALL", null, ["callee:00bdb600:8"]]
- 00a6046c bytes 51ec0594
+ 00a604b0 bytes 54ec0594
- 00a604b4 ["INT_ADD", "register:40f0:8", ["const:a604b4:8", "const:4:8"]]
- 00a604b4 ["CALL", null, ["callee:00bdb600:8"]]
+ 00a604f8 ["INT_ADD", "register:40f0:8", ["const:a604f8:8", "const:4:8"]]
+ 00a604f8 ["CALL", null, ["callee:00bdb600:8"]]
- 00a604b4 bytes 3fec0594
+ 00a604f8 bytes 42ec0594
- 00a604d8 ["INT_ADD", "register:40f0:8", ["const:a604d8:8", "const:4:8"]]
- 00a604d8 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00a6051c ["INT_ADD", "register:40f0:8", ["const:a6051c:8", "const:4:8"]]
+ 00a6051c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00a604d8 bytes f2ea0594
+ 00a6051c bytes f5ea0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed43ab769b39d0c2da837eba49fe388"></a>

### [`00a60594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60594.md) → [`00a605d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a605d8.md) FUN_00a605d8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c493c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c493c.md) [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 1件 [`00a5ee18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5ee18.md)
- 新版 呼出元 3件 [`006c493c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c493c.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 1件 [`00a5ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ee5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a605b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60594.md#insn-00a605b0)
- 新版 [`00a605f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a605d8.md#insn-00a605f4)

~~~diff
- 00a605b0 ["INT_ADD", "register:40f0:8", ["const:a605b0:8", "const:4:8"]]
- 00a605b0 ["CALL", null, ["callee:00a5ee5c:8"]]
+ 00a605f4 ["INT_ADD", "register:40f0:8", ["const:a605f4:8", "const:4:8"]]
+ 00a605f4 ["CALL", null, ["callee:00a5ee5c:8"]]
- 00a605b0 bytes 1afaff97
+ 00a605f4 bytes 1afaff97
~~~


<a id="compare-afa950f876427ecc8b21eb3c0211da55"></a>

### [`00a6140c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a6140c.md) → [`00a61450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a61450.md) FUN_00a61450

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0089f868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089f/0089f868.md) [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) [`00a8e548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md) · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 3件 [`0089f868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089f/0089f868.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a8e58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e58c.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a61448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a6140c.md#insn-00a61448)
- 新版 [`00a6148c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a61450.md#insn-00a6148c)

~~~diff
- 00a61448 ["INT_ADD", "register:40f0:8", ["const:a61448:8", "const:4:8"]]
- 00a61448 ["CALL", null, ["callee:00bdb600:8"]]
+ 00a6148c ["INT_ADD", "register:40f0:8", ["const:a6148c:8", "const:4:8"]]
+ 00a6148c ["CALL", null, ["callee:00bdb600:8"]]
- 00a61448 bytes 5ae80594
+ 00a6148c bytes 5de80594
~~~


<a id="compare-d777a3ae4aa0620a1e30416ada4c34b6"></a>

### [`00a61490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a61490.md) → [`00a614d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a614d4.md) FUN_00a614d4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) [`007e0684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0684.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00ade5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md)
- 新版 呼出元 2件 [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`007e0684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e0/007e0684.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a614a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a61490.md#insn-00a614a0) · [`00a614b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a61490.md#insn-00a614b0) · [`00a61554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a61490.md#insn-00a61554)
- 新版 [`00a614e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a614d4.md#insn-00a614e4) · [`00a614f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a614d4.md#insn-00a614f4) · [`00a61598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a614d4.md#insn-00a61598)

~~~diff
- 00a614a0 ["INT_ADD", "register:40f0:8", ["const:a614a0:8", "const:4:8"]]
- 00a614a0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a614e4 ["INT_ADD", "register:40f0:8", ["const:a614e4:8", "const:4:8"]]
+ 00a614e4 ["CALL", null, ["callee:0081f580:8"]]
- 00a614a0 bytes 38f8f697
+ 00a614e4 bytes 27f8f697
- 00a614b0 ["INT_ADD", "register:40f0:8", ["const:a614b0:8", "const:4:8"]]
- 00a614b0 ["CALL", null, ["callee:00ade610:8"]]
+ 00a614f4 ["INT_ADD", "register:40f0:8", ["const:a614f4:8", "const:4:8"]]
+ 00a614f4 ["CALL", null, ["callee:00ade610:8"]]
- 00a614b0 bytes 47f40194
+ 00a614f4 bytes 47f40194
- 00a61554 ["INT_ADD", "register:40f0:8", ["const:a61554:8", "const:4:8"]]
- 00a61554 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00a61598 ["INT_ADD", "register:40f0:8", ["const:a61598:8", "const:4:8"]]
+ 00a61598 ["CALL", null, ["callee:0041fdf0:8"]]
- 00a61554 bytes 27fae697
+ 00a61598 bytes 16fae697
~~~


<a id="compare-92a7095d128d4145ff46a400a4268424"></a>

### [`00a62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md) → [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md) FUN_00a62e58

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00a5f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md) [`00a62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md) [`00a63190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63190.md) · 呼出先 3件 [`00a62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md) [`00a63190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63190.md) [`00a63468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63468.md)
- 新版 呼出元 3件 [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md) [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md) [`00a631d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md) · 呼出先 3件 [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md) [`00a631d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md) [`00a634ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a62eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md#insn-00a62eb8) · [`00a62ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md#insn-00a62ed0) · [`00a62fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md#insn-00a62fa0)
- 新版 [`00a62efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md#insn-00a62efc) · [`00a62f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md#insn-00a62f14) · [`00a62fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md#insn-00a62fe4)

~~~diff
- 00a62eb8 ["INT_ADD", "register:40f0:8", ["const:a62eb8:8", "const:4:8"]]
- 00a62eb8 ["CALL", null, ["local:b0:8"]]
+ 00a62efc ["INT_ADD", "register:40f0:8", ["const:a62efc:8", "const:4:8"]]
+ 00a62efc ["CALL", null, ["local:b0:8"]]
- 00a62eb8 bytes d7ffff97
+ 00a62efc bytes d7ffff97
- 00a62ed0 ["INT_ADD", "register:40f0:8", ["const:a62ed0:8", "const:4:8"]]
- 00a62ed0 ["CALL", null, ["local:b0:8"]]
+ 00a62f14 ["INT_ADD", "register:40f0:8", ["const:a62f14:8", "const:4:8"]]
+ 00a62f14 ["CALL", null, ["local:b0:8"]]
- 00a62ed0 bytes d1ffff97
+ 00a62f14 bytes d1ffff97
- 00a62fa0 ["INT_ADD", "register:40f0:8", ["const:a62fa0:8", "const:4:8"]]
- 00a62fa0 ["CALL", null, ["callee:00a631d4:8"]]
+ 00a62fe4 ["INT_ADD", "register:40f0:8", ["const:a62fe4:8", "const:4:8"]]
+ 00a62fe4 ["CALL", null, ["callee:00a631d4:8"]]
- 00a62fa0 bytes 7c000094
+ 00a62fe4 bytes 7c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be360087e02429d4e3b939357f1209b8"></a>

### [`00a63190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63190.md) → [`00a631d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md) FUN_00a631d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md) · 呼出先 1件 [`00a62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md)
- 新版 呼出元 1件 [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md) · 呼出先 1件 [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a632e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63190.md#insn-00a632e0) · [`00a632f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63190.md#insn-00a632f8)
- 新版 [`00a63324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md#insn-00a63324) · [`00a6333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md#insn-00a6333c)

~~~diff
- 00a632e0 ["INT_ADD", "register:40f0:8", ["const:a632e0:8", "const:4:8"]]
- 00a632e0 ["CALL", null, ["callee:00a62e58:8"]]
+ 00a63324 ["INT_ADD", "register:40f0:8", ["const:a63324:8", "const:4:8"]]
+ 00a63324 ["CALL", null, ["callee:00a62e58:8"]]
- 00a632e0 bytes cdfeff97
+ 00a63324 bytes cdfeff97
- 00a632f8 ["INT_ADD", "register:40f0:8", ["const:a632f8:8", "const:4:8"]]
- 00a632f8 ["CALL", null, ["callee:00a62e58:8"]]
+ 00a6333c ["INT_ADD", "register:40f0:8", ["const:a6333c:8", "const:4:8"]]
+ 00a6333c ["CALL", null, ["callee:00a62e58:8"]]
- 00a632f8 bytes c7feff97
+ 00a6333c bytes c7feff97
~~~


<a id="compare-75fa1f0e3fbe1c7184b154c513c88d2e"></a>

### [`00a63468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63468.md) → [`00a634ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md) FUN_00a634ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e14.md) [`00a63468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63468.md) · 呼出先 1件 [`00a63468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63468.md)
- 新版 呼出元 2件 [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md) [`00a634ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md) · 呼出先 1件 [`00a634ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a63714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63468.md#insn-00a63714) · [`00a63740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63468.md#insn-00a63740)
- 新版 [`00a63758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md#insn-00a63758) · [`00a63784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md#insn-00a63784)

~~~diff
- 00a63714 ["INT_ADD", "register:40f0:8", ["const:a63714:8", "const:4:8"]]
- 00a63714 ["CALL", null, ["local:b0:8"]]
+ 00a63758 ["INT_ADD", "register:40f0:8", ["const:a63758:8", "const:4:8"]]
+ 00a63758 ["CALL", null, ["local:b0:8"]]
- 00a63714 bytes 55ffff97
+ 00a63758 bytes 55ffff97
- 00a63740 ["INT_ADD", "register:40f0:8", ["const:a63740:8", "const:4:8"]]
- 00a63740 ["CALL", null, ["local:b0:8"]]
+ 00a63784 ["INT_ADD", "register:40f0:8", ["const:a63784:8", "const:4:8"]]
+ 00a63784 ["CALL", null, ["local:b0:8"]]
- 00a63740 bytes 4affff97
+ 00a63784 bytes 4affff97
~~~


<a id="compare-c793d4c04ebdd9c13279b617414af144"></a>

### [`00a6407c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a6407c.md) → [`00a640c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640c0.md) FUN_00a640c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a6407c.md#insn-00a64098) · [`00a640a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a6407c.md#insn-00a640a4)
- 新版 [`00a640dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640c0.md#insn-00a640dc) · [`00a640e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640c0.md#insn-00a640e8)

~~~diff
- 00a64098 ["INT_ADD", "register:40f0:8", ["const:a64098:8", "const:4:8"]]
- 00a64098 ["CALL", null, ["ram:457e1c:8"]]
+ 00a640dc ["INT_ADD", "register:40f0:8", ["const:a640dc:8", "const:4:8"]]
+ 00a640dc ["CALL", null, ["ram:457e1c:8"]]
- 00a64098 bytes 61cfe797
+ 00a640dc bytes 50cfe797
- 00a640a4 ["INT_ADD", "register:40f0:8", ["const:a640a4:8", "const:4:8"]]
- 00a640a4 ["CALL", null, ["callee:00459efc:8"]]
+ 00a640e8 ["INT_ADD", "register:40f0:8", ["const:a640e8:8", "const:4:8"]]
+ 00a640e8 ["CALL", null, ["callee:00459efc:8"]]
- 00a640a4 bytes 96d7e797
+ 00a640e8 bytes 85d7e797
~~~


<a id="compare-731d19f2601ae8105336649b39027b61"></a>

### [`00a64da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64da8.md) → [`00a64dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md) FUN_00a64dec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00763798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763798.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00763798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763798.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64da8.md#insn-00a64dbc) · [`00a64dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64da8.md#insn-00a64dc4) · [`00a64dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64da8.md#insn-00a64dcc)
- 新版 [`00a64e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md#insn-00a64e00) · [`00a64e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md#insn-00a64e08) · [`00a64e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md#insn-00a64e10)

~~~diff
- 00a64dbc ["INT_ADD", "register:40f0:8", ["const:a64dbc:8", "const:4:8"]]
- 00a64dbc ["CALL", null, ["callee:00763798:8"]]
+ 00a64e00 ["INT_ADD", "register:40f0:8", ["const:a64e00:8", "const:4:8"]]
+ 00a64e00 ["CALL", null, ["callee:00763798:8"]]
- 00a64dbc bytes 77faf397
+ 00a64e00 bytes 66faf397
- 00a64dc4 ["INT_ADD", "register:40f0:8", ["const:a64dc4:8", "const:4:8"]]
- 00a64dc4 ["CALL", null, ["callee:00763798:8"]]
+ 00a64e08 ["INT_ADD", "register:40f0:8", ["const:a64e08:8", "const:4:8"]]
+ 00a64e08 ["CALL", null, ["callee:00763798:8"]]
- 00a64dc4 bytes 75faf397
+ 00a64e08 bytes 64faf397
- 00a64dcc ["INT_ADD", "register:40f0:8", ["const:a64dcc:8", "const:4:8"]]
- 00a64dcc ["CALL", null, ["callee:00763798:8"]]
+ 00a64e10 ["INT_ADD", "register:40f0:8", ["const:a64e10:8", "const:4:8"]]
+ 00a64e10 ["CALL", null, ["callee:00763798:8"]]
- 00a64dcc bytes 73faf397
+ 00a64e10 bytes 62faf397
~~~


<a id="compare-79111141f5e19b8aa7e003c62d7e7bcc"></a>

### [`00a64f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64f58.md) → [`00a64f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64f9c.md) FUN_00a64f9c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a64de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64de0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a64e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64e24.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64f58.md#insn-00a64f68)
- 新版 [`00a64fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64f9c.md#insn-00a64fac)

~~~diff
- 00a64f68 ["INT_ADD", "register:40f0:8", ["const:a64f68:8", "const:4:8"]]
- 00a64f68 ["CALL", null, ["callee:00a64e24:8"]]
+ 00a64fac ["INT_ADD", "register:40f0:8", ["const:a64fac:8", "const:4:8"]]
+ 00a64fac ["CALL", null, ["callee:00a64e24:8"]]
- 00a64f68 bytes 9effff97
+ 00a64fac bytes 9effff97
~~~


<a id="compare-57c1c653f1e2c3fff9a898831ff9bd12"></a>

### [`00a64fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64fd0.md) → [`00a65014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65014.md) FUN_00a65014

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0088482c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/0088482c.md) [`00a612b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a612b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0088482c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/0088482c.md) [`00a612fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a612fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64fd0.md#insn-00a64ff0)
- 新版 [`00a65034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65014.md#insn-00a65034)

~~~diff
- 00a64ff0 ["INT_ADD", "register:40f0:8", ["const:a64ff0:8", "const:4:8"]]
- 00a64ff0 ["CALL", null, ["callee:00a612fc:8"]]
+ 00a65034 ["INT_ADD", "register:40f0:8", ["const:a65034:8", "const:4:8"]]
+ 00a65034 ["CALL", null, ["callee:00a612fc:8"]]
- 00a64ff0 bytes b2f0ff97
+ 00a65034 bytes b2f0ff97
~~~


<a id="compare-861c9650c4b4ee2c9556cdb12e5852a5"></a>

### [`00a69930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a69930.md) → [`00a69974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69974.md) FUN_00a69974

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`0089dc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089d/0089dc0c.md) · 呼出先 0件 
- 新版 呼出元 11件 [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`0089dc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089dc0c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a69984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a69930.md#insn-00a69984)
- 新版 [`00a699c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69974.md#insn-00a699c8)

~~~diff
- 00a69984 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a69984 ["INT_ADD", "register:40f0:8", ["const:a69984:8", "const:4:8"]]
- 00a69984 ["CALLIND", null, ["register:0:8"]]
+ 00a699c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a699c8 ["INT_ADD", "register:40f0:8", ["const:a699c8:8", "const:4:8"]]
+ 00a699c8 ["CALLIND", null, ["register:0:8"]]
- 00a69984 bytes 00013fd6
+ 00a699c8 bytes 00013fd6
~~~


<a id="compare-bf74195bf0657cdbcf6a750f36495f1c"></a>

### [`00a6a290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a290.md) → [`00a6a2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a2d4.md) FUN_00a6a2d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`007f78c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f78c4.md) [`007f9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md) [`008920f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md) [`00897400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897400.md) [`008c9490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 6件 [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) [`007f9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f9cd4.md) [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) [`008c9490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9490.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6a298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a290.md#insn-00a6a298) · [`00a6a2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a290.md#insn-00a6a2ac) · [`00a6a2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a290.md#insn-00a6a2cc)
- 新版 [`00a6a2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a2d4.md#insn-00a6a2dc) · [`00a6a2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a2d4.md#insn-00a6a2f0) · [`00a6a310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a2d4.md#insn-00a6a310)

~~~diff
- 00a6a298 ["INT_ADD", "register:40f0:8", ["const:a6a298:8", "const:4:8"]]
- 00a6a298 ["CALL", null, ["callee:0081f580:8"]]
+ 00a6a2dc ["INT_ADD", "register:40f0:8", ["const:a6a2dc:8", "const:4:8"]]
+ 00a6a2dc ["CALL", null, ["callee:0081f580:8"]]
- 00a6a298 bytes bad4f697
+ 00a6a2dc bytes a9d4f697
- 00a6a2ac ["INT_ADD", "register:40f0:8", ["const:a6a2ac:8", "const:4:8"]]
- 00a6a2ac ["CALL", null, ["callee:0081f580:8"]]
+ 00a6a2f0 ["INT_ADD", "register:40f0:8", ["const:a6a2f0:8", "const:4:8"]]
+ 00a6a2f0 ["CALL", null, ["callee:0081f580:8"]]
- 00a6a2ac bytes b5d4f697
+ 00a6a2f0 bytes a4d4f697
- 00a6a2cc ["INT_ADD", "register:40f0:8", ["const:a6a2cc:8", "const:4:8"]]
- 00a6a2cc ["CALL", null, ["callee:0081f580:8"]]
+ 00a6a310 ["INT_ADD", "register:40f0:8", ["const:a6a310:8", "const:4:8"]]
+ 00a6a310 ["CALL", null, ["callee:0081f580:8"]]
- 00a6a2cc bytes add4f697
+ 00a6a310 bytes 9cd4f697
~~~


<a id="compare-af09b6192dd20fdbe1cbd899283c3af0"></a>

### [`00a6a974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a974.md) → [`00a6a9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a9b8.md) FUN_00a6a9b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`00a144c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a14/00a144c8.md) [`00a6225c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md) · 呼出先 3件 [`0055977c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/0055977c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 5件 [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`00a1450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a14/00a1450c.md) [`00a622a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md) · 呼出先 3件 [`0055977c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/0055977c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6a9c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a974.md#insn-00a6a9c8) · [`00a6a9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a974.md#insn-00a6a9f4) · [`00a6aa04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a974.md#insn-00a6aa04)
- 新版 [`00a6aa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a9b8.md#insn-00a6aa0c) · [`00a6aa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a9b8.md#insn-00a6aa38) · [`00a6aa48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a9b8.md#insn-00a6aa48)

~~~diff
- 00a6a9c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6a9c8 ["INT_ADD", "register:40f0:8", ["const:a6a9c8:8", "const:4:8"]]
- 00a6a9c8 ["CALLIND", null, ["register:0:8"]]
+ 00a6aa0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6aa0c ["INT_ADD", "register:40f0:8", ["const:a6aa0c:8", "const:4:8"]]
+ 00a6aa0c ["CALLIND", null, ["register:0:8"]]
- 00a6a9c8 bytes 00013fd6
+ 00a6aa0c bytes 00013fd6
- 00a6a9f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6a9f4 ["INT_ADD", "register:40f0:8", ["const:a6a9f4:8", "const:4:8"]]
- 00a6a9f4 ["CALLIND", null, ["register:0:8"]]
+ 00a6aa38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6aa38 ["INT_ADD", "register:40f0:8", ["const:a6aa38:8", "const:4:8"]]
+ 00a6aa38 ["CALLIND", null, ["register:0:8"]]
- 00a6a9f4 bytes 00013fd6
+ 00a6aa38 bytes 00013fd6
- 00a6aa04 ["INT_ADD", "register:40f0:8", ["const:a6aa04:8", "const:4:8"]]
- 00a6aa04 ["CALL", null, ["callee:0055977c:8"]]
+ 00a6aa48 ["INT_ADD", "register:40f0:8", ["const:a6aa48:8", "const:4:8"]]
+ 00a6aa48 ["CALL", null, ["callee:0055977c:8"]]
- 00a6aa04 bytes 5ebbeb97
+ 00a6aa48 bytes 4dbbeb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ee11d5154deb64abde03f304d7a7e0"></a>

### [`00a6ac88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6ac88.md) → [`00a6accc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6accc.md) FUN_00a6accc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00632468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632468.md) [`00664710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/00664710.md) [`006aad48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md) [`006d6364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6364.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 6件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00827b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827b94.md) [`008292ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/008292ec.md) [`008292f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/008292f4.md) [`00829328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829328.md)
- 新版 呼出元 7件 [`00632468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632468.md) [`00664710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664710.md) [`006aad48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006aa/006aad48.md) [`006d6364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6364.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 6件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00827b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827b94.md) [`008292ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292ec.md) [`008292f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292f4.md) [`00829328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829328.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6aca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6ac88.md#insn-00a6aca8) · [`00a6acac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6ac88.md#insn-00a6acac) · [`00a6acb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6ac88.md#insn-00a6acb4)
- 新版 [`00a6acec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6accc.md#insn-00a6acec) · [`00a6acf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6accc.md#insn-00a6acf0) · [`00a6acf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6accc.md#insn-00a6acf8)

~~~diff
- 00a6aca8 ["INT_ADD", "register:40f0:8", ["const:a6aca8:8", "const:4:8"]]
- 00a6aca8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a6acec ["INT_ADD", "register:40f0:8", ["const:a6acec:8", "const:4:8"]]
+ 00a6acec ["CALL", null, ["callee:0081f580:8"]]
- 00a6aca8 bytes 36d2f697
+ 00a6acec bytes 25d2f697
- 00a6acac ["INT_ADD", "register:40f0:8", ["const:a6acac:8", "const:4:8"]]
- 00a6acac ["CALL", null, ["callee:00827b94:8"]]
+ 00a6acf0 ["INT_ADD", "register:40f0:8", ["const:a6acf0:8", "const:4:8"]]
+ 00a6acf0 ["CALL", null, ["callee:00827b94:8"]]
- 00a6acac bytes baf3f697
+ 00a6acf0 bytes a9f3f697
- 00a6acb4 ["INT_ADD", "register:40f0:8", ["const:a6acb4:8", "const:4:8"]]
- 00a6acb4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a6acf8 ["INT_ADD", "register:40f0:8", ["const:a6acf8:8", "const:4:8"]]
+ 00a6acf8 ["CALL", null, ["callee:0081f580:8"]]
- 00a6acb4 bytes 33d2f697
+ 00a6acf8 bytes 22d2f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57430c5e08aeda63efd500a5411851c7"></a>

### [`00a6b198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b198.md) → [`00a6b1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b1dc.md) FUN_00a6b1dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) · 呼出先 2件 [`00a6d06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d06c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) · 呼出先 2件 [`00a6d0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d0b0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6b1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b198.md#insn-00a6b1d4) · [`00a6b200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b198.md#insn-00a6b200) · [`00a6b210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b198.md#insn-00a6b210)
- 新版 [`00a6b218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b1dc.md#insn-00a6b218) · [`00a6b244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b1dc.md#insn-00a6b244) · [`00a6b254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b1dc.md#insn-00a6b254)

~~~diff
- 00a6b1d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00a6b1d4 ["INT_ADD", "register:40f0:8", ["const:a6b1d4:8", "const:4:8"]]
- 00a6b1d4 ["CALLIND", null, ["register:0:8"]]
+ 00a6b218 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00a6b218 ["INT_ADD", "register:40f0:8", ["const:a6b218:8", "const:4:8"]]
+ 00a6b218 ["CALLIND", null, ["register:0:8"]]
- 00a6b1d4 bytes 20013fd6
+ 00a6b218 bytes 20013fd6
- 00a6b200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6b200 ["INT_ADD", "register:40f0:8", ["const:a6b200:8", "const:4:8"]]
- 00a6b200 ["CALLIND", null, ["register:0:8"]]
+ 00a6b244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6b244 ["INT_ADD", "register:40f0:8", ["const:a6b244:8", "const:4:8"]]
+ 00a6b244 ["CALLIND", null, ["register:0:8"]]
- 00a6b200 bytes 00013fd6
+ 00a6b244 bytes 00013fd6
- 00a6b210 ["INT_ADD", "register:40f0:8", ["const:a6b210:8", "const:4:8"]]
- 00a6b210 ["CALL", null, ["callee:00a6d0b0:8"]]
+ 00a6b254 ["INT_ADD", "register:40f0:8", ["const:a6b254:8", "const:4:8"]]
+ 00a6b254 ["CALL", null, ["callee:00a6d0b0:8"]]
- 00a6b210 bytes 97070094
+ 00a6b254 bytes 97070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5e754b5fd83d2a015a58bdc90fd3dfd"></a>

### [`00a6b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b3c0.md) → [`00a6b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b404.md) FUN_00a6b404

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`00763a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763a24.md) [`00763d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763d6c.md) [`007f9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md) [`0088f628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088f/0088f628.md) [`008c9490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md) · 呼出先 3件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d34.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md)
- 新版 呼出元 12件 [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) [`00763d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763d6c.md) [`007f9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f9cd4.md) [`0088f628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f628.md) [`008c9490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9490.md) · 呼出先 3件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d34.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6b3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b3c0.md#insn-00a6b3d0) · [`00a6b3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b3c0.md#insn-00a6b3e0) · [`00a6b3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b3c0.md#insn-00a6b3e8)
- 新版 [`00a6b414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b404.md#insn-00a6b414) · [`00a6b424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b404.md#insn-00a6b424) · [`00a6b42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b404.md#insn-00a6b42c)

~~~diff
- 00a6b3d0 ["INT_ADD", "register:40f0:8", ["const:a6b3d0:8", "const:4:8"]]
- 00a6b3d0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a6b414 ["INT_ADD", "register:40f0:8", ["const:a6b414:8", "const:4:8"]]
+ 00a6b414 ["CALL", null, ["callee:0081f580:8"]]
- 00a6b3d0 bytes 6cd0f697
+ 00a6b414 bytes 5bd0f697
- 00a6b3e0 ["INT_ADD", "register:40f0:8", ["const:a6b3e0:8", "const:4:8"]]
- 00a6b3e0 ["CALL", null, ["callee:008847e4:8"]]
+ 00a6b424 ["INT_ADD", "register:40f0:8", ["const:a6b424:8", "const:4:8"]]
+ 00a6b424 ["CALL", null, ["callee:008847e4:8"]]
- 00a6b3e0 bytes 0165f897
+ 00a6b424 bytes f064f897
- 00a6b3e8 ["INT_ADD", "register:40f0:8", ["const:a6b3e8:8", "const:4:8"]]
- 00a6b3e8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a6b42c ["INT_ADD", "register:40f0:8", ["const:a6b42c:8", "const:4:8"]]
+ 00a6b42c ["CALL", null, ["callee:0081f580:8"]]
- 00a6b3e8 bytes 66d0f697
+ 00a6b42c bytes 55d0f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-540f020b2bcd5c3b5402d5a039c2eb57"></a>

### [`00a6ce94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ce94.md) → [`00a6ced8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md) FUN_00a6ced8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a6a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a7d4.md) [`00a6b264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b264.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00a6a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md) [`00a6b2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b2a8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6cf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ce94.md#insn-00a6cf00) · [`00a6cf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ce94.md#insn-00a6cf10) · [`00a6cf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ce94.md#insn-00a6cf30)
- 新版 [`00a6cf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md#insn-00a6cf44) · [`00a6cf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md#insn-00a6cf54) · [`00a6cf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md#insn-00a6cf74)

~~~diff
- 00a6cf00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6cf00 ["INT_ADD", "register:40f0:8", ["const:a6cf00:8", "const:4:8"]]
- 00a6cf00 ["CALLIND", null, ["register:0:8"]]
+ 00a6cf44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6cf44 ["INT_ADD", "register:40f0:8", ["const:a6cf44:8", "const:4:8"]]
+ 00a6cf44 ["CALLIND", null, ["register:0:8"]]
- 00a6cf00 bytes 00013fd6
+ 00a6cf44 bytes 00013fd6
- 00a6cf10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6cf10 ["INT_ADD", "register:40f0:8", ["const:a6cf10:8", "const:4:8"]]
- 00a6cf10 ["CALLIND", null, ["register:0:8"]]
+ 00a6cf54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6cf54 ["INT_ADD", "register:40f0:8", ["const:a6cf54:8", "const:4:8"]]
+ 00a6cf54 ["CALLIND", null, ["register:0:8"]]
- 00a6cf10 bytes 00013fd6
+ 00a6cf54 bytes 00013fd6
- 00a6cf30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6cf30 ["INT_ADD", "register:40f0:8", ["const:a6cf30:8", "const:4:8"]]
- 00a6cf30 ["CALLIND", null, ["register:0:8"]]
+ 00a6cf74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6cf74 ["INT_ADD", "register:40f0:8", ["const:a6cf74:8", "const:4:8"]]
+ 00a6cf74 ["CALLIND", null, ["register:0:8"]]
- 00a6cf30 bytes 00013fd6
+ 00a6cf74 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75b20a8d561b355a409abd58d47b2268"></a>

### [`00a6d988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d988.md) → [`00a6d9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md) FUN_00a6d9cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00900f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900f40.md) · 呼出先 4件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00900f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900f40.md) · 呼出先 4件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6d9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d988.md#insn-00a6d9e8) · [`00a6d9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d988.md#insn-00a6d9fc) · [`00a6da0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d988.md#insn-00a6da0c)
- 新版 [`00a6da2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md#insn-00a6da2c) · [`00a6da40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md#insn-00a6da40) · [`00a6da50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d9cc.md#insn-00a6da50)

~~~diff
- 00a6d9e8 ["INT_ADD", "register:40f0:8", ["const:a6d9e8:8", "const:4:8"]]
- 00a6d9e8 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00a6da2c ["INT_ADD", "register:40f0:8", ["const:a6da2c:8", "const:4:8"]]
+ 00a6da2c ["CALL", null, ["callee:00bd6e60:8"]]
- 00a6d9e8 bytes 0ea50594
+ 00a6da2c bytes 0da50594
- 00a6d9fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6d9fc ["INT_ADD", "register:40f0:8", ["const:a6d9fc:8", "const:4:8"]]
- 00a6d9fc ["CALLIND", null, ["register:0:8"]]
+ 00a6da40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6da40 ["INT_ADD", "register:40f0:8", ["const:a6da40:8", "const:4:8"]]
+ 00a6da40 ["CALLIND", null, ["register:0:8"]]
- 00a6d9fc bytes 00013fd6
+ 00a6da40 bytes 00013fd6
- 00a6da0c ["INT_ADD", "register:40f0:8", ["const:a6da0c:8", "const:4:8"]]
- 00a6da0c ["CALL", null, ["callee:00bd6e90:8"]]
+ 00a6da50 ["INT_ADD", "register:40f0:8", ["const:a6da50:8", "const:4:8"]]
+ 00a6da50 ["CALL", null, ["callee:00bd6e90:8"]]
- 00a6da0c bytes 11a50594
+ 00a6da50 bytes 10a50594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55d11b01bf5d8176cf561aaf98c36941"></a>

### [`00a6da80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6da80.md) → [`00a6dac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md) FUN_00a6dac4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6dae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6da80.md#insn-00a6dae0) · [`00a6daf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6da80.md#insn-00a6daf4) · [`00a6db04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6da80.md#insn-00a6db04)
- 新版 [`00a6db24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md#insn-00a6db24) · [`00a6db38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md#insn-00a6db38) · [`00a6db48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dac4.md#insn-00a6db48)

~~~diff
- 00a6dae0 ["INT_ADD", "register:40f0:8", ["const:a6dae0:8", "const:4:8"]]
- 00a6dae0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00a6db24 ["INT_ADD", "register:40f0:8", ["const:a6db24:8", "const:4:8"]]
+ 00a6db24 ["CALL", null, ["callee:00bd6e60:8"]]
- 00a6dae0 bytes d0a40594
+ 00a6db24 bytes cfa40594
- 00a6daf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6daf4 ["INT_ADD", "register:40f0:8", ["const:a6daf4:8", "const:4:8"]]
- 00a6daf4 ["CALLIND", null, ["register:0:8"]]
+ 00a6db38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6db38 ["INT_ADD", "register:40f0:8", ["const:a6db38:8", "const:4:8"]]
+ 00a6db38 ["CALLIND", null, ["register:0:8"]]
- 00a6daf4 bytes 00013fd6
+ 00a6db38 bytes 00013fd6
- 00a6db04 ["INT_ADD", "register:40f0:8", ["const:a6db04:8", "const:4:8"]]
- 00a6db04 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00a6db48 ["INT_ADD", "register:40f0:8", ["const:a6db48:8", "const:4:8"]]
+ 00a6db48 ["CALL", null, ["callee:00bd6e90:8"]]
- 00a6db04 bytes d3a40594
+ 00a6db48 bytes d2a40594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4bc76b78fa745970146ecf5f95bafcb"></a>

### [`00a6dd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dd58.md) → [`00a6dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md) FUN_00a6dd9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00983a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983a68.md) [`00a6dd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dd58.md) · 呼出先 5件 [`00a6dd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dd58.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00983a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983a68.md) [`00a6dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md) · 呼出先 5件 [`00a6dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6ddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dd58.md#insn-00a6ddb4) · [`00a6ddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dd58.md#insn-00a6ddc0) · [`00a6ddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dd58.md#insn-00a6ddd0)
- 新版 [`00a6ddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md#insn-00a6ddf8) · [`00a6de04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md#insn-00a6de04) · [`00a6de14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd9c.md#insn-00a6de14)

~~~diff
- 00a6ddb4 ["INT_ADD", "register:40f0:8", ["const:a6ddb4:8", "const:4:8"]]
- 00a6ddb4 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00a6ddf8 ["INT_ADD", "register:40f0:8", ["const:a6ddf8:8", "const:4:8"]]
+ 00a6ddf8 ["CALL", null, ["callee:00bd6e60:8"]]
- 00a6ddb4 bytes 1ba40594
+ 00a6ddf8 bytes 1aa40594
- 00a6ddc0 ["INT_ADD", "register:40f0:8", ["const:a6ddc0:8", "const:4:8"]]
- 00a6ddc0 ["CALL", null, ["local:b0:8"]]
+ 00a6de04 ["INT_ADD", "register:40f0:8", ["const:a6de04:8", "const:4:8"]]
+ 00a6de04 ["CALL", null, ["local:b0:8"]]
- 00a6ddc0 bytes e6ffff97
+ 00a6de04 bytes e6ffff97
- 00a6ddd0 ["INT_ADD", "register:40f0:8", ["const:a6ddd0:8", "const:4:8"]]
- 00a6ddd0 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00a6de14 ["INT_ADD", "register:40f0:8", ["const:a6de14:8", "const:4:8"]]
+ 00a6de14 ["CALL", null, ["callee:00bd6e90:8"]]
- 00a6ddd0 bytes 20a40594
+ 00a6de14 bytes 1fa40594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc7c3c67aa87135ddfd46c6005ad560"></a>

### [`00a6de44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6de44.md) → [`00a6de88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6de88.md) FUN_00a6de88

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6de60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6de44.md#insn-00a6de60)
- 新版 [`00a6dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6de88.md#insn-00a6dea4)

~~~diff
- 00a6de60 ["INT_ADD", "register:40f0:8", ["const:a6de60:8", "const:4:8"]]
- 00a6de60 ["CALL", null, ["callee:00a6d8f8:8"]]
+ 00a6dea4 ["INT_ADD", "register:40f0:8", ["const:a6dea4:8", "const:4:8"]]
+ 00a6dea4 ["CALL", null, ["callee:00a6d8f8:8"]]
- 00a6de60 bytes 95feff97
+ 00a6dea4 bytes 95feff97
~~~


<a id="compare-6672527b94a07567e9024bef83e56cc1"></a>

### [`00a6de80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6de80.md) → [`00a6dec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dec4.md) FUN_00a6dec4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6de90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6de80.md#insn-00a6de90)
- 新版 [`00a6ded4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dec4.md#insn-00a6ded4)

~~~diff
- 00a6de90 ["INT_ADD", "register:40f0:8", ["const:a6de90:8", "const:4:8"]]
- 00a6de90 ["CALL", null, ["callee:00bdb050:8"]]
+ 00a6ded4 ["INT_ADD", "register:40f0:8", ["const:a6ded4:8", "const:4:8"]]
+ 00a6ded4 ["CALL", null, ["callee:00bdb050:8"]]
- 00a6de90 bytes 5cb40594
+ 00a6ded4 bytes 5fb40594
~~~


<a id="compare-34d413d868e8933333da55d7742b53a5"></a>

### [`00a6dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dea4.md) → [`00a6dee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dee8.md) FUN_00a6dee8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a6db78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6db78.md) · 呼出先 2件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a6dbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dbbc.md) · 呼出先 2件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6debc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dea4.md#insn-00a6debc)
- 新版 [`00a6df00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dee8.md#insn-00a6df00)

~~~diff
- 00a6debc ["INT_ADD", "register:40f0:8", ["const:a6debc:8", "const:4:8"]]
- 00a6debc ["CALL", null, ["callee:00a6d8f8:8"]]
+ 00a6df00 ["INT_ADD", "register:40f0:8", ["const:a6df00:8", "const:4:8"]]
+ 00a6df00 ["CALL", null, ["callee:00a6d8f8:8"]]
- 00a6debc bytes 7efeff97
+ 00a6df00 bytes 7efeff97
~~~


<a id="compare-9e90a8b36fda3db3165275acb85f7d30"></a>

### [`00a712b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a712b0.md) → [`00a712f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a712f4.md) FUN_00a712f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 3件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 3件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a712d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a712b0.md#insn-00a712d4) · [`00a712ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a712b0.md#insn-00a712ec) · [`00a71300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a712b0.md#insn-00a71300)
- 新版 [`00a71318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a712f4.md#insn-00a71318) · [`00a71330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a712f4.md#insn-00a71330) · [`00a71344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a712f4.md#insn-00a71344)

~~~diff
- 00a712d4 ["INT_ADD", "register:40f0:8", ["const:a712d4:8", "const:4:8"]]
- 00a712d4 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00a71318 ["INT_ADD", "register:40f0:8", ["const:a71318:8", "const:4:8"]]
+ 00a71318 ["CALL", null, ["callee:00bd6e60:8"]]
- 00a712d4 bytes d3960594
+ 00a71318 bytes d2960594
- 00a712ec ["INT_ADD", "register:40f0:8", ["const:a712ec:8", "const:4:8"]]
- 00a712ec ["CALL", null, ["callee:00bd6e90:8"]]
+ 00a71330 ["INT_ADD", "register:40f0:8", ["const:a71330:8", "const:4:8"]]
+ 00a71330 ["CALL", null, ["callee:00bd6e90:8"]]
- 00a712ec bytes d9960594
+ 00a71330 bytes d8960594
- 00a71300 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a71300 ["INT_ADD", "register:40f0:8", ["const:a71300:8", "const:4:8"]]
- 00a71300 ["CALLIND", null, ["register:0:8"]]
+ 00a71344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a71344 ["INT_ADD", "register:40f0:8", ["const:a71344:8", "const:4:8"]]
+ 00a71344 ["CALLIND", null, ["register:0:8"]]
- 00a71300 bytes 00013fd6
+ 00a71344 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

