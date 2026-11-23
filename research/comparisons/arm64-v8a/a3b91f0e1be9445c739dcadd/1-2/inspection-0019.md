# v15.7.3 → v15.7.4 · 要調査の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-4d213a974b6fb62d68b2d101d8a9a4d5"></a>

### [`00bd2688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md) → [`00bd26cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md) FUN_00bd26cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd26cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md#insn-00bd26cc) · [`00bd2730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md#insn-00bd2730) · [`00bd2774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md#insn-00bd2774)
- 新版 [`00bd2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md#insn-00bd2710) · [`00bd2774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md#insn-00bd2774) · [`00bd27b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md#insn-00bd27b8)

~~~diff
- 00bd26cc ["INT_ADD", "register:40f0:8", ["const:bd26cc:8", "const:4:8"]]
- 00bd26cc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd2710 ["INT_ADD", "register:40f0:8", ["const:bd2710:8", "const:4:8"]]
+ 00bd2710 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd26cc bytes cd2a0094
+ 00bd2710 bytes d02a0094
- 00bd2730 ["INT_ADD", "register:40f0:8", ["const:bd2730:8", "const:4:8"]]
- 00bd2730 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd2774 ["INT_ADD", "register:40f0:8", ["const:bd2774:8", "const:4:8"]]
+ 00bd2774 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd2730 bytes b42a0094
+ 00bd2774 bytes b72a0094
- 00bd2774 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2774 ["INT_ADD", "register:40f0:8", ["const:bd2774:8", "const:4:8"]]
- 00bd2774 ["CALLIND", null, ["register:0:8"]]
+ 00bd27b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd27b8 ["INT_ADD", "register:40f0:8", ["const:bd27b8:8", "const:4:8"]]
+ 00bd27b8 ["CALLIND", null, ["register:0:8"]]
- 00bd2774 bytes 00013fd6
+ 00bd27b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb22df85fc4389925ec06886a62ce751"></a>

### [`00bd2900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md) → [`00bd2944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md) FUN_00bd2944

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md#insn-00bd2944) · [`00bd29ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md#insn-00bd29ac) · [`00bd29d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md#insn-00bd29d4)
- 新版 [`00bd2988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md#insn-00bd2988) · [`00bd29f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md#insn-00bd29f0) · [`00bd2a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md#insn-00bd2a18)

~~~diff
- 00bd2944 ["INT_ADD", "register:40f0:8", ["const:bd2944:8", "const:4:8"]]
- 00bd2944 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd2988 ["INT_ADD", "register:40f0:8", ["const:bd2988:8", "const:4:8"]]
+ 00bd2988 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd2944 bytes 2f2a0094
+ 00bd2988 bytes 322a0094
- 00bd29ac ["INT_ADD", "register:40f0:8", ["const:bd29ac:8", "const:4:8"]]
- 00bd29ac ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd29f0 ["INT_ADD", "register:40f0:8", ["const:bd29f0:8", "const:4:8"]]
+ 00bd29f0 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd29ac bytes 152a0094
+ 00bd29f0 bytes 182a0094
- 00bd29d4 ["INT_ADD", "register:40f0:8", ["const:bd29d4:8", "const:4:8"]]
- 00bd29d4 ["CALL", null, ["callee:00bc82d4:8"]]
+ 00bd2a18 ["INT_ADD", "register:40f0:8", ["const:bd2a18:8", "const:4:8"]]
+ 00bd2a18 ["CALL", null, ["callee:00bc82d4:8"]]
- 00bd29d4 bytes 2fd6ff97
+ 00bd2a18 bytes 2fd6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80adf62eb0225b1504e4150839c982b0"></a>

### [`00bd2a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md) → [`00bd2aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2aac.md) FUN_00bd2aac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md#insn-00bd2a88) · [`00bd2ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md#insn-00bd2ab4) · [`00bd2ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md#insn-00bd2ae8)
- 新版 [`00bd2acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2aac.md#insn-00bd2acc) · [`00bd2af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2aac.md#insn-00bd2af8) · [`00bd2b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2aac.md#insn-00bd2b2c)

~~~diff
- 00bd2a88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2a88 ["INT_ADD", "register:40f0:8", ["const:bd2a88:8", "const:4:8"]]
- 00bd2a88 ["CALLIND", null, ["register:0:8"]]
+ 00bd2acc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2acc ["INT_ADD", "register:40f0:8", ["const:bd2acc:8", "const:4:8"]]
+ 00bd2acc ["CALLIND", null, ["register:0:8"]]
- 00bd2a88 bytes 00013fd6
+ 00bd2acc bytes 00013fd6
- 00bd2ab4 ["INT_ADD", "register:40f0:8", ["const:bd2ab4:8", "const:4:8"]]
- 00bd2ab4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd2af8 ["INT_ADD", "register:40f0:8", ["const:bd2af8:8", "const:4:8"]]
+ 00bd2af8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd2ab4 bytes d3290094
+ 00bd2af8 bytes d6290094
- 00bd2ae8 ["INT_ADD", "register:40f0:8", ["const:bd2ae8:8", "const:4:8"]]
- 00bd2ae8 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bd2b2c ["INT_ADD", "register:40f0:8", ["const:bd2b2c:8", "const:4:8"]]
+ 00bd2b2c ["CALL", null, ["callee:00bde2c0:8"]]
- 00bd2ae8 bytes e22d0094
+ 00bd2b2c bytes e52d0094
~~~


<a id="compare-b8eef4f7eae7fb70cff19d5c0f66b6e2"></a>

### [`00bd2aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2aec.md) → [`00bd2b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md) FUN_00bd2b30

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2aec.md#insn-00bd2b38) · [`00bd2b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2aec.md#insn-00bd2b60) · [`00bd2b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2aec.md#insn-00bd2b98)
- 新版 [`00bd2b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md#insn-00bd2b7c) · [`00bd2ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md#insn-00bd2ba4) · [`00bd2bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md#insn-00bd2bdc)

~~~diff
- 00bd2b38 ["INT_ADD", "register:40f0:8", ["const:bd2b38:8", "const:4:8"]]
- 00bd2b38 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd2b7c ["INT_ADD", "register:40f0:8", ["const:bd2b7c:8", "const:4:8"]]
+ 00bd2b7c ["CALL", null, ["callee:00bdd250:8"]]
- 00bd2b38 bytes b2290094
+ 00bd2b7c bytes b5290094
- 00bd2b60 ["INT_ADD", "register:40f0:8", ["const:bd2b60:8", "const:4:8"]]
- 00bd2b60 ["CALL", null, ["callee:00bc82d4:8"]]
+ 00bd2ba4 ["INT_ADD", "register:40f0:8", ["const:bd2ba4:8", "const:4:8"]]
+ 00bd2ba4 ["CALL", null, ["callee:00bc82d4:8"]]
- 00bd2b60 bytes ccd5ff97
+ 00bd2ba4 bytes ccd5ff97
- 00bd2b98 ["INT_ADD", "register:40f0:8", ["const:bd2b98:8", "const:4:8"]]
- 00bd2b98 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd2bdc ["INT_ADD", "register:40f0:8", ["const:bd2bdc:8", "const:4:8"]]
+ 00bd2bdc ["CALL", null, ["callee:00bdd250:8"]]
- 00bd2b98 bytes 9a290094
+ 00bd2bdc bytes 9d290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81b2dd3bcd63a4d3f8122cc803183d1a"></a>

### [`00bd2e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md) → [`00bd2ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md) FUN_00bd2ecc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md#insn-00bd2eb4) · [`00bd2ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md#insn-00bd2ed8) · [`00bd2f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md#insn-00bd2f04)
- 新版 [`00bd2ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md#insn-00bd2ef8) · [`00bd2f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md#insn-00bd2f1c) · [`00bd2f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md#insn-00bd2f48)

~~~diff
- 00bd2eb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2eb4 ["INT_ADD", "register:40f0:8", ["const:bd2eb4:8", "const:4:8"]]
- 00bd2eb4 ["CALLIND", null, ["register:0:8"]]
+ 00bd2ef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2ef8 ["INT_ADD", "register:40f0:8", ["const:bd2ef8:8", "const:4:8"]]
+ 00bd2ef8 ["CALLIND", null, ["register:0:8"]]
- 00bd2eb4 bytes 00013fd6
+ 00bd2ef8 bytes 00013fd6
- 00bd2ed8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2ed8 ["INT_ADD", "register:40f0:8", ["const:bd2ed8:8", "const:4:8"]]
- 00bd2ed8 ["CALLIND", null, ["register:0:8"]]
+ 00bd2f1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2f1c ["INT_ADD", "register:40f0:8", ["const:bd2f1c:8", "const:4:8"]]
+ 00bd2f1c ["CALLIND", null, ["register:0:8"]]
- 00bd2ed8 bytes 00013fd6
+ 00bd2f1c bytes 00013fd6
- 00bd2f04 ["INT_ADD", "register:40f0:8", ["const:bd2f04:8", "const:4:8"]]
- 00bd2f04 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd2f48 ["INT_ADD", "register:40f0:8", ["const:bd2f48:8", "const:4:8"]]
+ 00bd2f48 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd2f04 bytes bf280094
+ 00bd2f48 bytes c2280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a47ba5820744877a766457e4f6abf0d6"></a>

### [`00bd2ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md) → [`00bd3040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md) FUN_00bd3040

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md#insn-00bd3028) · [`00bd304c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md#insn-00bd304c) · [`00bd3078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md#insn-00bd3078)
- 新版 [`00bd306c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md#insn-00bd306c) · [`00bd3090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md#insn-00bd3090) · [`00bd30bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md#insn-00bd30bc)

~~~diff
- 00bd3028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3028 ["INT_ADD", "register:40f0:8", ["const:bd3028:8", "const:4:8"]]
- 00bd3028 ["CALLIND", null, ["register:0:8"]]
+ 00bd306c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd306c ["INT_ADD", "register:40f0:8", ["const:bd306c:8", "const:4:8"]]
+ 00bd306c ["CALLIND", null, ["register:0:8"]]
- 00bd3028 bytes 00013fd6
+ 00bd306c bytes 00013fd6
- 00bd304c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd304c ["INT_ADD", "register:40f0:8", ["const:bd304c:8", "const:4:8"]]
- 00bd304c ["CALLIND", null, ["register:0:8"]]
+ 00bd3090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3090 ["INT_ADD", "register:40f0:8", ["const:bd3090:8", "const:4:8"]]
+ 00bd3090 ["CALLIND", null, ["register:0:8"]]
- 00bd304c bytes 00013fd6
+ 00bd3090 bytes 00013fd6
- 00bd3078 ["INT_ADD", "register:40f0:8", ["const:bd3078:8", "const:4:8"]]
- 00bd3078 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd30bc ["INT_ADD", "register:40f0:8", ["const:bd30bc:8", "const:4:8"]]
+ 00bd30bc ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3078 bytes 62280094
+ 00bd30bc bytes 65280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2764a01b2f91ebd27901566ee618e01b"></a>

### [`00bd3200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3200.md) → [`00bd3244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md) FUN_00bd3244

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3200.md#insn-00bd3224) · [`00bd3258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3200.md#insn-00bd3258) · [`00bd32bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3200.md#insn-00bd32bc)
- 新版 [`00bd3268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md#insn-00bd3268) · [`00bd329c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md#insn-00bd329c) · [`00bd3300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md#insn-00bd3300)

~~~diff
- 00bd3224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3224 ["INT_ADD", "register:40f0:8", ["const:bd3224:8", "const:4:8"]]
- 00bd3224 ["CALLIND", null, ["register:0:8"]]
+ 00bd3268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3268 ["INT_ADD", "register:40f0:8", ["const:bd3268:8", "const:4:8"]]
+ 00bd3268 ["CALLIND", null, ["register:0:8"]]
- 00bd3224 bytes 00013fd6
+ 00bd3268 bytes 00013fd6
- 00bd3258 ["INT_ADD", "register:40f0:8", ["const:bd3258:8", "const:4:8"]]
- 00bd3258 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd329c ["INT_ADD", "register:40f0:8", ["const:bd329c:8", "const:4:8"]]
+ 00bd329c ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3258 bytes ea270094
+ 00bd329c bytes ed270094
- 00bd32bc ["INT_ADD", "register:40f0:8", ["const:bd32bc:8", "const:4:8"]]
- 00bd32bc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3300 ["INT_ADD", "register:40f0:8", ["const:bd3300:8", "const:4:8"]]
+ 00bd3300 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd32bc bytes d1270094
+ 00bd3300 bytes d4270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81fa78b36640bc26878001ee1889bedf"></a>

### [`00bd3394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md) → [`00bd33d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md) FUN_00bd33d8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd33e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md#insn-00bd33e8) · [`00bd3404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md#insn-00bd3404) · [`00bd343c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md#insn-00bd343c)
- 新版 [`00bd342c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md#insn-00bd342c) · [`00bd3448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md#insn-00bd3448) · [`00bd3480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md#insn-00bd3480)

~~~diff
- 00bd33e8 ["INT_ADD", "register:40f0:8", ["const:bd33e8:8", "const:4:8"]]
- 00bd33e8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd342c ["INT_ADD", "register:40f0:8", ["const:bd342c:8", "const:4:8"]]
+ 00bd342c ["CALL", null, ["callee:00bdd250:8"]]
- 00bd33e8 bytes 86270094
+ 00bd342c bytes 89270094
- 00bd3404 ["INT_ADD", "register:40f0:8", ["const:bd3404:8", "const:4:8"]]
- 00bd3404 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bd3448 ["INT_ADD", "register:40f0:8", ["const:bd3448:8", "const:4:8"]]
+ 00bd3448 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bd3404 bytes 571f0094
+ 00bd3448 bytes 5a1f0094
- 00bd343c ["INT_ADD", "register:40f0:8", ["const:bd343c:8", "const:4:8"]]
- 00bd343c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3480 ["INT_ADD", "register:40f0:8", ["const:bd3480:8", "const:4:8"]]
+ 00bd3480 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd343c bytes 71270094
+ 00bd3480 bytes 74270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c7910fd01612892af8d54b2664a7ab6"></a>

### [`00bd3508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md) → [`00bd354c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md) FUN_00bd354c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd354c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md#insn-00bd354c) · [`00bd3598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md#insn-00bd3598) · [`00bd35dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md#insn-00bd35dc)
- 新版 [`00bd3590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md#insn-00bd3590) · [`00bd35dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md#insn-00bd35dc) · [`00bd3620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md#insn-00bd3620)

~~~diff
- 00bd354c ["INT_ADD", "register:40f0:8", ["const:bd354c:8", "const:4:8"]]
- 00bd354c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3590 ["INT_ADD", "register:40f0:8", ["const:bd3590:8", "const:4:8"]]
+ 00bd3590 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd354c bytes 2d270094
+ 00bd3590 bytes 30270094
- 00bd3598 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3598 ["INT_ADD", "register:40f0:8", ["const:bd3598:8", "const:4:8"]]
- 00bd3598 ["CALLIND", null, ["register:0:8"]]
+ 00bd35dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd35dc ["INT_ADD", "register:40f0:8", ["const:bd35dc:8", "const:4:8"]]
+ 00bd35dc ["CALLIND", null, ["register:0:8"]]
- 00bd3598 bytes 00013fd6
+ 00bd35dc bytes 00013fd6
- 00bd35dc ["INT_ADD", "register:40f0:8", ["const:bd35dc:8", "const:4:8"]]
- 00bd35dc ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bd3620 ["INT_ADD", "register:40f0:8", ["const:bd3620:8", "const:4:8"]]
+ 00bd3620 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bd35dc bytes 252b0094
+ 00bd3620 bytes 282b0094
~~~


<a id="compare-1c2ed2197d2ad07c80d34e2975931192"></a>

### [`00bd38d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md) → [`00bd3914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md) FUN_00bd3914

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd38f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md#insn-00bd38f8) · [`00bd3930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md#insn-00bd3930) · [`00bd394c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md#insn-00bd394c)
- 新版 [`00bd393c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md#insn-00bd393c) · [`00bd3974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md#insn-00bd3974) · [`00bd3990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md#insn-00bd3990)

~~~diff
- 00bd38f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd38f8 ["INT_ADD", "register:40f0:8", ["const:bd38f8:8", "const:4:8"]]
- 00bd38f8 ["CALLIND", null, ["register:0:8"]]
+ 00bd393c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd393c ["INT_ADD", "register:40f0:8", ["const:bd393c:8", "const:4:8"]]
+ 00bd393c ["CALLIND", null, ["register:0:8"]]
- 00bd38f8 bytes 00013fd6
+ 00bd393c bytes 00013fd6
- 00bd3930 ["INT_ADD", "register:40f0:8", ["const:bd3930:8", "const:4:8"]]
- 00bd3930 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3974 ["INT_ADD", "register:40f0:8", ["const:bd3974:8", "const:4:8"]]
+ 00bd3974 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3930 bytes 34260094
+ 00bd3974 bytes 37260094
- 00bd394c ["INT_ADD", "register:40f0:8", ["const:bd394c:8", "const:4:8"]]
- 00bd394c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bd3990 ["INT_ADD", "register:40f0:8", ["const:bd3990:8", "const:4:8"]]
+ 00bd3990 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bd394c bytes 051e0094
+ 00bd3990 bytes 081e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91ea8da7342a852f5341a2cd61eaaf5a"></a>

### [`00bd3ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3ac4.md) → [`00bd3b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3b08.md) FUN_00bd3b08

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3ac4.md#insn-00bd3b08) · [`00bd3b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3ac4.md#insn-00bd3b58) · [`00bd3b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3ac4.md#insn-00bd3b7c)
- 新版 [`00bd3b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3b08.md#insn-00bd3b4c) · [`00bd3b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3b08.md#insn-00bd3b9c) · [`00bd3bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3b08.md#insn-00bd3bc0)

~~~diff
- 00bd3b08 ["INT_ADD", "register:40f0:8", ["const:bd3b08:8", "const:4:8"]]
- 00bd3b08 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3b4c ["INT_ADD", "register:40f0:8", ["const:bd3b4c:8", "const:4:8"]]
+ 00bd3b4c ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3b08 bytes be250094
+ 00bd3b4c bytes c1250094
- 00bd3b58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3b58 ["INT_ADD", "register:40f0:8", ["const:bd3b58:8", "const:4:8"]]
- 00bd3b58 ["CALLIND", null, ["register:0:8"]]
+ 00bd3b9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3b9c ["INT_ADD", "register:40f0:8", ["const:bd3b9c:8", "const:4:8"]]
+ 00bd3b9c ["CALLIND", null, ["register:0:8"]]
- 00bd3b58 bytes 00013fd6
+ 00bd3b9c bytes 00013fd6
- 00bd3b7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3b7c ["INT_ADD", "register:40f0:8", ["const:bd3b7c:8", "const:4:8"]]
- 00bd3b7c ["CALLIND", null, ["register:0:8"]]
+ 00bd3bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3bc0 ["INT_ADD", "register:40f0:8", ["const:bd3bc0:8", "const:4:8"]]
+ 00bd3bc0 ["CALLIND", null, ["register:0:8"]]
- 00bd3b7c bytes 00013fd6
+ 00bd3bc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5162b3cde52cf9f6b37ae469f4ddf10c"></a>

### [`00bd3bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md) → [`00bd3c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md) FUN_00bd3c30

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md#insn-00bd3c18) · [`00bd3c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md#insn-00bd3c3c) · [`00bd3c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md#insn-00bd3c68)
- 新版 [`00bd3c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md#insn-00bd3c5c) · [`00bd3c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md#insn-00bd3c80) · [`00bd3cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md#insn-00bd3cac)

~~~diff
- 00bd3c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3c18 ["INT_ADD", "register:40f0:8", ["const:bd3c18:8", "const:4:8"]]
- 00bd3c18 ["CALLIND", null, ["register:0:8"]]
+ 00bd3c5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3c5c ["INT_ADD", "register:40f0:8", ["const:bd3c5c:8", "const:4:8"]]
+ 00bd3c5c ["CALLIND", null, ["register:0:8"]]
- 00bd3c18 bytes 00013fd6
+ 00bd3c5c bytes 00013fd6
- 00bd3c3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3c3c ["INT_ADD", "register:40f0:8", ["const:bd3c3c:8", "const:4:8"]]
- 00bd3c3c ["CALLIND", null, ["register:0:8"]]
+ 00bd3c80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3c80 ["INT_ADD", "register:40f0:8", ["const:bd3c80:8", "const:4:8"]]
+ 00bd3c80 ["CALLIND", null, ["register:0:8"]]
- 00bd3c3c bytes 00013fd6
+ 00bd3c80 bytes 00013fd6
- 00bd3c68 ["INT_ADD", "register:40f0:8", ["const:bd3c68:8", "const:4:8"]]
- 00bd3c68 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3cac ["INT_ADD", "register:40f0:8", ["const:bd3cac:8", "const:4:8"]]
+ 00bd3cac ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3c68 bytes 66250094
+ 00bd3cac bytes 69250094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34e9593e454191abc20d711bae39cc15"></a>

### [`00bd40a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md) → [`00bd40ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md) FUN_00bd40ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd40cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md#insn-00bd40cc) · [`00bd40f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md#insn-00bd40f4) · [`00bd4124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md#insn-00bd4124)
- 新版 [`00bd4110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md#insn-00bd4110) · [`00bd4138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md#insn-00bd4138) · [`00bd4168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md#insn-00bd4168)

~~~diff
- 00bd40cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd40cc ["INT_ADD", "register:40f0:8", ["const:bd40cc:8", "const:4:8"]]
- 00bd40cc ["CALLIND", null, ["register:0:8"]]
+ 00bd4110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4110 ["INT_ADD", "register:40f0:8", ["const:bd4110:8", "const:4:8"]]
+ 00bd4110 ["CALLIND", null, ["register:0:8"]]
- 00bd40cc bytes 00013fd6
+ 00bd4110 bytes 00013fd6
- 00bd40f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd40f4 ["INT_ADD", "register:40f0:8", ["const:bd40f4:8", "const:4:8"]]
- 00bd40f4 ["CALLIND", null, ["register:0:8"]]
+ 00bd4138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4138 ["INT_ADD", "register:40f0:8", ["const:bd4138:8", "const:4:8"]]
+ 00bd4138 ["CALLIND", null, ["register:0:8"]]
- 00bd40f4 bytes 00013fd6
+ 00bd4138 bytes 00013fd6
- 00bd4124 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4124 ["INT_ADD", "register:40f0:8", ["const:bd4124:8", "const:4:8"]]
- 00bd4124 ["CALLIND", null, ["register:0:8"]]
+ 00bd4168 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4168 ["INT_ADD", "register:40f0:8", ["const:bd4168:8", "const:4:8"]]
+ 00bd4168 ["CALLIND", null, ["register:0:8"]]
- 00bd4124 bytes 00013fd6
+ 00bd4168 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fce509c1b730b13dc4b1b120039509e6"></a>

### [`00bd4268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md) → [`00bd42ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md) FUN_00bd42ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd42a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md#insn-00bd42a4) · [`00bd42d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md#insn-00bd42d4) · [`00bd4304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md#insn-00bd4304)
- 新版 [`00bd42e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md#insn-00bd42e8) · [`00bd4318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md#insn-00bd4318) · [`00bd4348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md#insn-00bd4348)

~~~diff
- 00bd42a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd42a4 ["INT_ADD", "register:40f0:8", ["const:bd42a4:8", "const:4:8"]]
- 00bd42a4 ["CALLIND", null, ["register:0:8"]]
+ 00bd42e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd42e8 ["INT_ADD", "register:40f0:8", ["const:bd42e8:8", "const:4:8"]]
+ 00bd42e8 ["CALLIND", null, ["register:0:8"]]
- 00bd42a4 bytes 00013fd6
+ 00bd42e8 bytes 00013fd6
- 00bd42d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd42d4 ["INT_ADD", "register:40f0:8", ["const:bd42d4:8", "const:4:8"]]
- 00bd42d4 ["CALLIND", null, ["register:0:8"]]
+ 00bd4318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4318 ["INT_ADD", "register:40f0:8", ["const:bd4318:8", "const:4:8"]]
+ 00bd4318 ["CALLIND", null, ["register:0:8"]]
- 00bd42d4 bytes 00013fd6
+ 00bd4318 bytes 00013fd6
- 00bd4304 ["INT_ADD", "register:40f0:8", ["const:bd4304:8", "const:4:8"]]
- 00bd4304 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd4348 ["INT_ADD", "register:40f0:8", ["const:bd4348:8", "const:4:8"]]
+ 00bd4348 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd4304 bytes bf230094
+ 00bd4348 bytes c2230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53cd91e03661570ff02c0a0d18c666d2"></a>

### [`00bd4354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md) → [`00bd4398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md) FUN_00bd4398

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd43a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md#insn-00bd43a8) · [`00bd43c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md#insn-00bd43c4) · [`00bd43fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md#insn-00bd43fc)
- 新版 [`00bd43ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md#insn-00bd43ec) · [`00bd4408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md#insn-00bd4408) · [`00bd4440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md#insn-00bd4440)

~~~diff
- 00bd43a8 ["INT_ADD", "register:40f0:8", ["const:bd43a8:8", "const:4:8"]]
- 00bd43a8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd43ec ["INT_ADD", "register:40f0:8", ["const:bd43ec:8", "const:4:8"]]
+ 00bd43ec ["CALL", null, ["callee:00bdd250:8"]]
- 00bd43a8 bytes 96230094
+ 00bd43ec bytes 99230094
- 00bd43c4 ["INT_ADD", "register:40f0:8", ["const:bd43c4:8", "const:4:8"]]
- 00bd43c4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bd4408 ["INT_ADD", "register:40f0:8", ["const:bd4408:8", "const:4:8"]]
+ 00bd4408 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bd43c4 bytes 671b0094
+ 00bd4408 bytes 6a1b0094
- 00bd43fc ["INT_ADD", "register:40f0:8", ["const:bd43fc:8", "const:4:8"]]
- 00bd43fc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd4440 ["INT_ADD", "register:40f0:8", ["const:bd4440:8", "const:4:8"]]
+ 00bd4440 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd43fc bytes 81230094
+ 00bd4440 bytes 84230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016b970dab7e2585bb549e30aa0e9052"></a>

### [`00bd44bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md) → [`00bd4500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md) FUN_00bd4500

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md#insn-00bd4548) · [`00bd4570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md#insn-00bd4570) · [`00bd45a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md#insn-00bd45a0)
- 新版 [`00bd458c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md#insn-00bd458c) · [`00bd45b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md#insn-00bd45b4) · [`00bd45e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md#insn-00bd45e4)

~~~diff
- 00bd4548 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4548 ["INT_ADD", "register:40f0:8", ["const:bd4548:8", "const:4:8"]]
- 00bd4548 ["CALLIND", null, ["register:0:8"]]
+ 00bd458c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd458c ["INT_ADD", "register:40f0:8", ["const:bd458c:8", "const:4:8"]]
+ 00bd458c ["CALLIND", null, ["register:0:8"]]
- 00bd4548 bytes 00013fd6
+ 00bd458c bytes 00013fd6
- 00bd4570 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4570 ["INT_ADD", "register:40f0:8", ["const:bd4570:8", "const:4:8"]]
- 00bd4570 ["CALLIND", null, ["register:0:8"]]
+ 00bd45b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd45b4 ["INT_ADD", "register:40f0:8", ["const:bd45b4:8", "const:4:8"]]
+ 00bd45b4 ["CALLIND", null, ["register:0:8"]]
- 00bd4570 bytes 00013fd6
+ 00bd45b4 bytes 00013fd6
- 00bd45a0 ["INT_ADD", "register:40f0:8", ["const:bd45a0:8", "const:4:8"]]
- 00bd45a0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd45e4 ["INT_ADD", "register:40f0:8", ["const:bd45e4:8", "const:4:8"]]
+ 00bd45e4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd45a0 bytes 18230094
+ 00bd45e4 bytes 1b230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6adb72972f53fc2bd3b5b75ca973e8a"></a>

### [`00bd47fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md) → [`00bd4840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4840.md) FUN_00bd4840

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md#insn-00bd4898) · [`00bd48c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md#insn-00bd48c8) · [`00bd48f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md#insn-00bd48f8)
- 新版 [`00bd48dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4840.md#insn-00bd48dc) · [`00bd490c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4840.md#insn-00bd490c) · [`00bd493c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4840.md#insn-00bd493c)

~~~diff
- 00bd4898 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4898 ["INT_ADD", "register:40f0:8", ["const:bd4898:8", "const:4:8"]]
- 00bd4898 ["CALLIND", null, ["register:0:8"]]
+ 00bd48dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd48dc ["INT_ADD", "register:40f0:8", ["const:bd48dc:8", "const:4:8"]]
+ 00bd48dc ["CALLIND", null, ["register:0:8"]]
- 00bd4898 bytes 00013fd6
+ 00bd48dc bytes 00013fd6
- 00bd48c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd48c8 ["INT_ADD", "register:40f0:8", ["const:bd48c8:8", "const:4:8"]]
- 00bd48c8 ["CALLIND", null, ["register:0:8"]]
+ 00bd490c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd490c ["INT_ADD", "register:40f0:8", ["const:bd490c:8", "const:4:8"]]
+ 00bd490c ["CALLIND", null, ["register:0:8"]]
- 00bd48c8 bytes 00013fd6
+ 00bd490c bytes 00013fd6
- 00bd48f8 ["INT_ADD", "register:40f0:8", ["const:bd48f8:8", "const:4:8"]]
- 00bd48f8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd493c ["INT_ADD", "register:40f0:8", ["const:bd493c:8", "const:4:8"]]
+ 00bd493c ["CALL", null, ["callee:00bdd250:8"]]
- 00bd48f8 bytes 42220094
+ 00bd493c bytes 45220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65e0d4d3c23c42a1eba104fd2432fe73"></a>

### [`00bd4b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md) → [`00bd4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md) FUN_00bd4bdc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd4cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd4d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md#insn-00bd4bc4) · [`00bd4bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md#insn-00bd4bf4) · [`00bd4c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md#insn-00bd4c24)
- 新版 [`00bd4c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md#insn-00bd4c08) · [`00bd4c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md#insn-00bd4c38) · [`00bd4c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md#insn-00bd4c68)

~~~diff
- 00bd4bc4 ["INT_ADD", "register:40f0:8", ["const:bd4bc4:8", "const:4:8"]]
- 00bd4bc4 ["CALL", null, ["callee:00bd4d04:8"]]
+ 00bd4c08 ["INT_ADD", "register:40f0:8", ["const:bd4c08:8", "const:4:8"]]
+ 00bd4c08 ["CALL", null, ["callee:00bd4d04:8"]]
- 00bd4bc4 bytes 3f000094
+ 00bd4c08 bytes 3f000094
- 00bd4bf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4bf4 ["INT_ADD", "register:40f0:8", ["const:bd4bf4:8", "const:4:8"]]
- 00bd4bf4 ["CALLIND", null, ["register:0:8"]]
+ 00bd4c38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4c38 ["INT_ADD", "register:40f0:8", ["const:bd4c38:8", "const:4:8"]]
+ 00bd4c38 ["CALLIND", null, ["register:0:8"]]
- 00bd4bf4 bytes 00013fd6
+ 00bd4c38 bytes 00013fd6
- 00bd4c24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4c24 ["INT_ADD", "register:40f0:8", ["const:bd4c24:8", "const:4:8"]]
- 00bd4c24 ["CALLIND", null, ["register:0:8"]]
+ 00bd4c68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4c68 ["INT_ADD", "register:40f0:8", ["const:bd4c68:8", "const:4:8"]]
+ 00bd4c68 ["CALLIND", null, ["register:0:8"]]
- 00bd4c24 bytes 00013fd6
+ 00bd4c68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6eba7574baf464d9a0b7cc7c70717e4"></a>

### [`00bd4e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e6c.md) → [`00bd4eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4eb0.md) _ZnwmRKSt9nothrow_t

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9b0.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdda00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda00.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e6c.md#insn-00bd4e78)
- 新版 [`00bd4ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4eb0.md#insn-00bd4ebc)

~~~diff
- 00bd4e78 ["INT_ADD", "register:40f0:8", ["const:bd4e78:8", "const:4:8"]]
- 00bd4e78 ["CALL", null, ["callee:00bdb040:8"]]
+ 00bd4ebc ["INT_ADD", "register:40f0:8", ["const:bd4ebc:8", "const:4:8"]]
+ 00bd4ebc ["CALL", null, ["callee:00bdb040:8"]]
- 00bd4e78 bytes 5e180094
+ 00bd4ebc bytes 61180094
~~~


<a id="compare-ed4b884608763041d7532b1eac38a315"></a>

### [`00bd4e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e9c.md) → [`00bd4ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4ee0.md) _ZnamRKSt9nothrow_t

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdefa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e9c.md#insn-00bd4ea8)
- 新版 [`00bd4eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4ee0.md#insn-00bd4eec)

~~~diff
- 00bd4ea8 ["INT_ADD", "register:40f0:8", ["const:bd4ea8:8", "const:4:8"]]
- 00bd4ea8 ["CALL", null, ["callee:00bdefa0:8"]]
+ 00bd4eec ["INT_ADD", "register:40f0:8", ["const:bd4eec:8", "const:4:8"]]
+ 00bd4eec ["CALL", null, ["callee:00bdefa0:8"]]
- 00bd4ea8 bytes 2a280094
+ 00bd4eec bytes 2d280094
~~~


<a id="compare-18c392e10fcae497982b888156d525a5"></a>

### [`00bd4efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4efc.md) → [`00bd4f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f40.md) _ZnwmSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4efc.md#insn-00bd4f08)
- 新版 [`00bd4f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f40.md#insn-00bd4f4c)

~~~diff
- 00bd4f08 ["INT_ADD", "register:40f0:8", ["const:bd4f08:8", "const:4:8"]]
- 00bd4f08 ["CALL", null, ["callee:00be1f00:8"]]
+ 00bd4f4c ["INT_ADD", "register:40f0:8", ["const:bd4f4c:8", "const:4:8"]]
+ 00bd4f4c ["CALL", null, ["callee:00be1f00:8"]]
- 00bd4f08 bytes ea330094
+ 00bd4f4c bytes ed330094
~~~


<a id="compare-75ca1a9ce56ab3a88fa014f8a5a182b0"></a>

### [`00bd4f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f2c.md) → [`00bd4f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f70.md) _ZnamSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ed0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f2c.md#insn-00bd4f38)
- 新版 [`00bd4f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f70.md#insn-00bd4f7c)

~~~diff
- 00bd4f38 ["INT_ADD", "register:40f0:8", ["const:bd4f38:8", "const:4:8"]]
- 00bd4f38 ["CALL", null, ["callee:00be1f20:8"]]
+ 00bd4f7c ["INT_ADD", "register:40f0:8", ["const:bd4f7c:8", "const:4:8"]]
+ 00bd4f7c ["CALL", null, ["callee:00be1f20:8"]]
- 00bd4f38 bytes e6330094
+ 00bd4f7c bytes e9330094
~~~


<a id="compare-eb3a488afa08cd3b9b42254203cbb50d"></a>

### [`00bd4fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md) → [`00bd5008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md) __cxa_allocate_exception

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) · 呼出先 3件 [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) · 呼出先 3件 [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md#insn-00bd4fdc) · [`00bd4ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md#insn-00bd4ff4) · [`00bd500c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md#insn-00bd500c)
- 新版 [`00bd5020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md#insn-00bd5020) · [`00bd5038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md#insn-00bd5038) · [`00bd5050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md#insn-00bd5050)

~~~diff
- 00bd4fdc ["INT_ADD", "register:40f0:8", ["const:bd4fdc:8", "const:4:8"]]
- 00bd4fdc ["CALL", null, ["callee:00bd57d4:8"]]
+ 00bd5020 ["INT_ADD", "register:40f0:8", ["const:bd5020:8", "const:4:8"]]
+ 00bd5020 ["CALL", null, ["callee:00bd57d4:8"]]
- 00bd4fdc bytes ed010094
+ 00bd5020 bytes ed010094
- 00bd4ff4 ["INT_ADD", "register:40f0:8", ["const:bd4ff4:8", "const:4:8"]]
- 00bd4ff4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00bd5038 ["INT_ADD", "register:40f0:8", ["const:bd5038:8", "const:4:8"]]
+ 00bd5038 ["CALL", null, ["callee:00bdb240:8"]]
- 00bd4ff4 bytes 7f180094
+ 00bd5038 bytes 82180094
- 00bd500c ["INT_ADD", "register:40f0:8", ["const:bd500c:8", "const:4:8"]]
- 00bd500c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd5050 ["INT_ADD", "register:40f0:8", ["const:bd5050:8", "const:4:8"]]
+ 00bd5050 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd500c bytes 5d180094
+ 00bd5050 bytes 60180094
~~~


<a id="compare-2b5a191eb38c10dae0d720fbc11963c8"></a>

### [`00bd5014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5014.md) → [`00bd5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5058.md) __cxa_begin_catch

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb170.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00be1d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d80.md)
- 新版 呼出元 1件 [`00bdb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1c0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00be1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5014.md#insn-00bd5028) · [`00bd50a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5014.md#insn-00bd50a8)
- 新版 [`00bd506c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5058.md#insn-00bd506c) · [`00bd50ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5058.md#insn-00bd50ec)

~~~diff
- 00bd5028 ["INT_ADD", "register:40f0:8", ["const:bd5028:8", "const:4:8"]]
- 00bd5028 ["CALL", null, ["callee:00be1dd0:8"]]
+ 00bd506c ["INT_ADD", "register:40f0:8", ["const:bd506c:8", "const:4:8"]]
+ 00bd506c ["CALL", null, ["callee:00be1dd0:8"]]
- 00bd5028 bytes 56330094
+ 00bd506c bytes 59330094
- 00bd50a8 ["INT_ADD", "register:40f0:8", ["const:bd50a8:8", "const:4:8"]]
- 00bd50a8 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd50ec ["INT_ADD", "register:40f0:8", ["const:bd50ec:8", "const:4:8"]]
+ 00bd50ec ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd50a8 bytes 36180094
+ 00bd50ec bytes 39180094
~~~


<a id="compare-f60fb2ee77c7a72e2b5f935b7243822f"></a>

### [`00bd50b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50b0.md) → [`00bd50f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd50f4.md) __cxa_free_exception

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb080.md) · 呼出先 1件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md)
- 新版 呼出元 1件 [`00bdb0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0d0.md) · 呼出先 1件 [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd50c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50b0.md#insn-00bd50c0)
- 新版 [`00bd5104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd50f4.md#insn-00bd5104)

~~~diff
- 00bd50c0 ["INT_ADD", "register:40f0:8", ["const:bd50c0:8", "const:4:8"]]
- 00bd50c0 ["CALL", null, ["callee:00bd59a8:8"]]
+ 00bd5104 ["INT_ADD", "register:40f0:8", ["const:bd5104:8", "const:4:8"]]
+ 00bd5104 ["CALL", null, ["callee:00bd59a8:8"]]
- 00bd50c0 bytes 29020094
+ 00bd5104 bytes 29020094
~~~


<a id="compare-f7af2cb82cc4f0e232611c2215d8df6f"></a>

### [`00bd5144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md) → [`00bd5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md) FUN_00bd5188

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bd50d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50d4.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00bd5118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5118.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md#insn-00bd5168) · [`00bd5180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md#insn-00bd5180) · [`00bd5188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md#insn-00bd5188)
- 新版 [`00bd51ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md#insn-00bd51ac) · [`00bd51c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md#insn-00bd51c4) · [`00bd51cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md#insn-00bd51cc)

~~~diff
- 00bd5168 ["INT_ADD", "register:40f0:8", ["const:bd5168:8", "const:4:8"]]
- 00bd5168 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00bd51ac ["INT_ADD", "register:40f0:8", ["const:bd51ac:8", "const:4:8"]]
+ 00bd51ac ["CALL", null, ["callee:00bd6e90:8"]]
- 00bd5168 bytes 3a070094
+ 00bd51ac bytes 39070094
- 00bd5180 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5180 ["INT_ADD", "register:40f0:8", ["const:bd5180:8", "const:4:8"]]
- 00bd5180 ["CALLIND", null, ["register:0:8"]]
+ 00bd51c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd51c4 ["INT_ADD", "register:40f0:8", ["const:bd51c4:8", "const:4:8"]]
+ 00bd51c4 ["CALLIND", null, ["register:0:8"]]
- 00bd5180 bytes 00013fd6
+ 00bd51c4 bytes 00013fd6
- 00bd5188 ["INT_ADD", "register:40f0:8", ["const:bd5188:8", "const:4:8"]]
- 00bd5188 ["CALL", null, ["callee:00bd59a8:8"]]
+ 00bd51cc ["INT_ADD", "register:40f0:8", ["const:bd51cc:8", "const:4:8"]]
+ 00bd51cc ["CALL", null, ["callee:00bd59a8:8"]]
- 00bd5188 bytes f7010094
+ 00bd51cc bytes f7010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-993f936cae9e999b54912766232c39e3"></a>

### [`00bd51ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md) → [`00bd51f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md) __cxa_allocate_dependent_exception

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd51bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md#insn-00bd51bc) · [`00bd51e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md#insn-00bd51e4)
- 新版 [`00bd5200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md#insn-00bd5200) · [`00bd5228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md#insn-00bd5228)

~~~diff
- 00bd51bc ["INT_ADD", "register:40f0:8", ["const:bd51bc:8", "const:4:8"]]
- 00bd51bc ["CALL", null, ["callee:00bd57d4:8"]]
+ 00bd5200 ["INT_ADD", "register:40f0:8", ["const:bd5200:8", "const:4:8"]]
+ 00bd5200 ["CALL", null, ["callee:00bd57d4:8"]]
- 00bd51bc bytes 75010094
+ 00bd5200 bytes 75010094
- 00bd51e4 ["INT_ADD", "register:40f0:8", ["const:bd51e4:8", "const:4:8"]]
- 00bd51e4 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd5228 ["INT_ADD", "register:40f0:8", ["const:bd5228:8", "const:4:8"]]
+ 00bd5228 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd51e4 bytes e7170094
+ 00bd5228 bytes ea170094
~~~


<a id="compare-38d48c47d506cd87818c9892deea7c62"></a>

### [`00bd51f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md) → [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) __cxa_throw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) · 呼出先 4件 [`00bd524c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md) [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bdb490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb490.md) [`00be1d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d80.md)
- 新版 呼出元 1件 [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) · 呼出先 4件 [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bdb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4e0.md) [`00be1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md#insn-00bd5210) · [`00bd522c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md#insn-00bd522c) · [`00bd5240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md#insn-00bd5240)
- 新版 [`00bd5254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md#insn-00bd5254) · [`00bd5270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md#insn-00bd5270) · [`00bd5284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md#insn-00bd5284)

~~~diff
- 00bd5210 ["INT_ADD", "register:40f0:8", ["const:bd5210:8", "const:4:8"]]
- 00bd5210 ["CALL", null, ["callee:00be1dd0:8"]]
+ 00bd5254 ["INT_ADD", "register:40f0:8", ["const:bd5254:8", "const:4:8"]]
+ 00bd5254 ["CALL", null, ["callee:00be1dd0:8"]]
- 00bd5210 bytes dc320094
+ 00bd5254 bytes df320094
- 00bd522c ["INT_ADD", "register:40f0:8", ["const:bd522c:8", "const:4:8"]]
- 00bd522c ["CALL", null, ["callee:00bdb4e0:8"]]
+ 00bd5270 ["INT_ADD", "register:40f0:8", ["const:bd5270:8", "const:4:8"]]
+ 00bd5270 ["CALL", null, ["callee:00bdb4e0:8"]]
- 00bd522c bytes 99180094
+ 00bd5270 bytes 9c180094
- 00bd5240 ["INT_ADD", "register:40f0:8", ["const:bd5240:8", "const:4:8"]]
- 00bd5240 ["CALL", null, ["callee:00bd6ec0:8"]]
+ 00bd5284 ["INT_ADD", "register:40f0:8", ["const:bd5284:8", "const:4:8"]]
+ 00bd5284 ["CALL", null, ["callee:00bd6ec0:8"]]
- 00bd5240 bytes 10070094
+ 00bd5284 bytes 0f070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7fb7c83bcb012b78d9518cc5be32799"></a>

### [`00bd524c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md) → [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) FUN_00bd5290

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd51f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md) · 呼出先 2件 [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bdb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb170.md)
- 新版 呼出元 1件 [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) · 呼出先 2件 [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bdb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md#insn-00bd5264) · [`00bd526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md#insn-00bd526c)
- 新版 [`00bd52a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md#insn-00bd52a8) · [`00bd52b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md#insn-00bd52b0)

~~~diff
- 00bd5264 ["INT_ADD", "register:40f0:8", ["const:bd5264:8", "const:4:8"]]
- 00bd5264 ["CALL", null, ["callee:00bdb1c0:8"]]
+ 00bd52a8 ["INT_ADD", "register:40f0:8", ["const:bd52a8:8", "const:4:8"]]
+ 00bd52a8 ["CALL", null, ["callee:00bdb1c0:8"]]
- 00bd5264 bytes c3170094
+ 00bd52a8 bytes c6170094
- 00bd526c ["INT_ADD", "register:40f0:8", ["const:bd526c:8", "const:4:8"]]
- 00bd526c ["CALL", null, ["callee:00bbaa70:8"]]
+ 00bd52b0 ["INT_ADD", "register:40f0:8", ["const:bd52b0:8", "const:4:8"]]
+ 00bd52b0 ["CALL", null, ["callee:00bbaa70:8"]]
- 00bd526c bytes f095ff97
+ 00bd52b0 bytes f095ff97
~~~


<a id="compare-55cf96936160fa0cb43635d11f454b96"></a>

### [`00bd527c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md) → [`00bd52c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md) __cxa_end_catch

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb430.md) · 呼出先 4件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bd728c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd728c.md) [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)
- 新版 呼出元 1件 [`00bdb480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb480.md) · 呼出先 4件 [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bd72cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72cc.md) [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd528c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md#insn-00bd528c) · [`00bd52ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md#insn-00bd52ec) · [`00bd52fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md#insn-00bd52fc)
- 新版 [`00bd52d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md#insn-00bd52d0) · [`00bd5330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md#insn-00bd5330) · [`00bd5340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md#insn-00bd5340)

~~~diff
- 00bd528c ["INT_ADD", "register:40f0:8", ["const:bd528c:8", "const:4:8"]]
- 00bd528c ["CALL", null, ["callee:00be1de0:8"]]
+ 00bd52d0 ["INT_ADD", "register:40f0:8", ["const:bd52d0:8", "const:4:8"]]
+ 00bd52d0 ["CALL", null, ["callee:00be1de0:8"]]
- 00bd528c bytes c1320094
+ 00bd52d0 bytes c4320094
- 00bd52ec ["INT_ADD", "register:40f0:8", ["const:bd52ec:8", "const:4:8"]]
- 00bd52ec ["CALL", null, ["callee:00bd59a8:8"]]
+ 00bd5330 ["INT_ADD", "register:40f0:8", ["const:bd5330:8", "const:4:8"]]
+ 00bd5330 ["CALL", null, ["callee:00bd59a8:8"]]
- 00bd52ec bytes 9e010094
+ 00bd5330 bytes 9e010094
- 00bd52fc ["INT_ADD", "register:40f0:8", ["const:bd52fc:8", "const:4:8"]]
- 00bd52fc ["CALL", null, ["callee:00bd6e90:8"]]
+ 00bd5340 ["INT_ADD", "register:40f0:8", ["const:bd5340:8", "const:4:8"]]
+ 00bd5340 ["CALL", null, ["callee:00bd6e90:8"]]
- 00bd52fc bytes d5060094
+ 00bd5340 bytes d4060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20c65dea621d3099d4abbf25e00fa300"></a>

### [`00bd5368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md) → [`00bd53ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md) __cxa_decrement_exception_refcount

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ec0.md) · 呼出先 2件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00be0f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f10.md) · 呼出先 2件 [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md#insn-00bd5388) · [`00bd53a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md#insn-00bd53a0) · [`00bd53a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md#insn-00bd53a8)
- 新版 [`00bd53cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md#insn-00bd53cc) · [`00bd53e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md#insn-00bd53e4) · [`00bd53ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md#insn-00bd53ec)

~~~diff
- 00bd5388 ["INT_ADD", "register:40f0:8", ["const:bd5388:8", "const:4:8"]]
- 00bd5388 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00bd53cc ["INT_ADD", "register:40f0:8", ["const:bd53cc:8", "const:4:8"]]
+ 00bd53cc ["CALL", null, ["callee:00bd6e90:8"]]
- 00bd5388 bytes b2060094
+ 00bd53cc bytes b1060094
- 00bd53a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd53a0 ["INT_ADD", "register:40f0:8", ["const:bd53a0:8", "const:4:8"]]
- 00bd53a0 ["CALLIND", null, ["register:0:8"]]
+ 00bd53e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd53e4 ["INT_ADD", "register:40f0:8", ["const:bd53e4:8", "const:4:8"]]
+ 00bd53e4 ["CALLIND", null, ["register:0:8"]]
- 00bd53a0 bytes 00013fd6
+ 00bd53e4 bytes 00013fd6
- 00bd53a8 ["INT_ADD", "register:40f0:8", ["const:bd53a8:8", "const:4:8"]]
- 00bd53a8 ["CALL", null, ["callee:00bd59a8:8"]]
+ 00bd53ec ["INT_ADD", "register:40f0:8", ["const:bd53ec:8", "const:4:8"]]
+ 00bd53ec ["CALL", null, ["callee:00bd59a8:8"]]
- 00bd53a8 bytes 6f010094
+ 00bd53ec bytes 6f010094
~~~


<a id="compare-ab0fa85946fb6c235e23fc6077caec02"></a>

### [`00bd53c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd53c4.md) → [`00bd5408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5408.md) __cxa_current_exception_type

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd53d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd53c4.md#insn-00bd53d0)
- 新版 [`00bd5414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5408.md#insn-00bd5414)

~~~diff
- 00bd53d0 ["INT_ADD", "register:40f0:8", ["const:bd53d0:8", "const:4:8"]]
- 00bd53d0 ["CALL", null, ["callee:00be1de0:8"]]
+ 00bd5414 ["INT_ADD", "register:40f0:8", ["const:bd5414:8", "const:4:8"]]
+ 00bd5414 ["CALL", null, ["callee:00be1de0:8"]]
- 00bd53d0 bytes 70320094
+ 00bd5414 bytes 73320094
~~~


<a id="compare-dea7c19fe90084f0d26b65894b8e3a66"></a>

### [`00bd5414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md) → [`00bd5458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md) __cxa_rethrow

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb660.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00be1d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d80.md)
- 新版 呼出元 1件 [`00bdb6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6b0.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00be1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md#insn-00bd5428) · [`00bd5434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md#insn-00bd5434) · [`00bd5480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md#insn-00bd5480)
- 新版 [`00bd546c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md#insn-00bd546c) · [`00bd5478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md#insn-00bd5478) · [`00bd54c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md#insn-00bd54c4)

~~~diff
- 00bd5428 ["INT_ADD", "register:40f0:8", ["const:bd5428:8", "const:4:8"]]
- 00bd5428 ["CALL", null, ["callee:00be1dd0:8"]]
+ 00bd546c ["INT_ADD", "register:40f0:8", ["const:bd546c:8", "const:4:8"]]
+ 00bd546c ["CALL", null, ["callee:00be1dd0:8"]]
- 00bd5428 bytes 56320094
+ 00bd546c bytes 59320094
- 00bd5434 ["INT_ADD", "register:40f0:8", ["const:bd5434:8", "const:4:8"]]
- 00bd5434 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd5478 ["INT_ADD", "register:40f0:8", ["const:bd5478:8", "const:4:8"]]
+ 00bd5478 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd5434 bytes 53170094
+ 00bd5478 bytes 56170094
- 00bd5480 ["INT_ADD", "register:40f0:8", ["const:bd5480:8", "const:4:8"]]
- 00bd5480 ["CALL", null, ["callee:00bd6ec0:8"]]
+ 00bd54c4 ["INT_ADD", "register:40f0:8", ["const:bd54c4:8", "const:4:8"]]
+ 00bd54c4 ["CALL", null, ["callee:00bd6ec0:8"]]
- 00bd5480 bytes 80060094
+ 00bd54c4 bytes 7f060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c65f15128018908ed6c935c4fc7c4267"></a>

### [`00bd54f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd54f8.md) → [`00bd553c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd553c.md) __cxa_increment_exception_refcount

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ed0.md) · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00be0f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f20.md) · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd54f8.md#insn-00bd5514)
- 新版 [`00bd5558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd553c.md#insn-00bd5558)

~~~diff
- 00bd5514 ["INT_ADD", "register:40f0:8", ["const:bd5514:8", "const:4:8"]]
- 00bd5514 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00bd5558 ["INT_ADD", "register:40f0:8", ["const:bd5558:8", "const:4:8"]]
+ 00bd5558 ["CALL", null, ["callee:00bd6e90:8"]]
- 00bd5514 bytes 4f060094
+ 00bd5558 bytes 4e060094
~~~


<a id="compare-0fa8a13db72ecf45e19888ca90027228"></a>

### [`00bd5524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5524.md) → [`00bd5568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5568.md) __cxa_current_primary_exception

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ef0.md) · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)
- 新版 呼出元 1件 [`00be0f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f40.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5524.md#insn-00bd5534) · [`00bd5580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5524.md#insn-00bd5580)
- 新版 [`00bd5578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5568.md#insn-00bd5578) · [`00bd55c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5568.md#insn-00bd55c4)

~~~diff
- 00bd5534 ["INT_ADD", "register:40f0:8", ["const:bd5534:8", "const:4:8"]]
- 00bd5534 ["CALL", null, ["callee:00be1de0:8"]]
+ 00bd5578 ["INT_ADD", "register:40f0:8", ["const:bd5578:8", "const:4:8"]]
+ 00bd5578 ["CALL", null, ["callee:00be1de0:8"]]
- 00bd5534 bytes 17320094
+ 00bd5578 bytes 1a320094
- 00bd5580 ["INT_ADD", "register:40f0:8", ["const:bd5580:8", "const:4:8"]]
- 00bd5580 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00bd55c4 ["INT_ADD", "register:40f0:8", ["const:bd55c4:8", "const:4:8"]]
+ 00bd55c4 ["CALL", null, ["callee:00bd6e90:8"]]
- 00bd5580 bytes 34060094
+ 00bd55c4 bytes 33060094
~~~


<a id="compare-258d02be16b319eb38998812239df8f4"></a>

### [`00bd56c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md) → [`00bd5708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md) FUN_00bd5708

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bd55a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd55a4.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00bd55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd56f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md#insn-00bd56f0) · [`00bd5708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md#insn-00bd5708) · [`00bd5710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md#insn-00bd5710)
- 新版 [`00bd5734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md#insn-00bd5734) · [`00bd574c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md#insn-00bd574c) · [`00bd5754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md#insn-00bd5754)

~~~diff
- 00bd56f0 ["INT_ADD", "register:40f0:8", ["const:bd56f0:8", "const:4:8"]]
- 00bd56f0 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00bd5734 ["INT_ADD", "register:40f0:8", ["const:bd5734:8", "const:4:8"]]
+ 00bd5734 ["CALL", null, ["callee:00bd6e90:8"]]
- 00bd56f0 bytes d8050094
+ 00bd5734 bytes d7050094
- 00bd5708 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5708 ["INT_ADD", "register:40f0:8", ["const:bd5708:8", "const:4:8"]]
- 00bd5708 ["CALLIND", null, ["register:0:8"]]
+ 00bd574c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd574c ["INT_ADD", "register:40f0:8", ["const:bd574c:8", "const:4:8"]]
+ 00bd574c ["CALLIND", null, ["register:0:8"]]
- 00bd5708 bytes 00013fd6
+ 00bd574c bytes 00013fd6
- 00bd5710 ["INT_ADD", "register:40f0:8", ["const:bd5710:8", "const:4:8"]]
- 00bd5710 ["CALL", null, ["callee:00bd59a8:8"]]
+ 00bd5754 ["INT_ADD", "register:40f0:8", ["const:bd5754:8", "const:4:8"]]
+ 00bd5754 ["CALL", null, ["callee:00bd59a8:8"]]
- 00bd5710 bytes 95000094
+ 00bd5754 bytes 95000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c45d0165e3700483419bc40307d125"></a>

### [`00bd5738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5738.md) → [`00bd577c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd577c.md) __cxa_uncaught_exception

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5738.md#insn-00bd5744)
- 新版 [`00bd5788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd577c.md#insn-00bd5788)

~~~diff
- 00bd5744 ["INT_ADD", "register:40f0:8", ["const:bd5744:8", "const:4:8"]]
- 00bd5744 ["CALL", null, ["callee:00be1de0:8"]]
+ 00bd5788 ["INT_ADD", "register:40f0:8", ["const:bd5788:8", "const:4:8"]]
+ 00bd5788 ["CALL", null, ["callee:00be1de0:8"]]
- 00bd5744 bytes 93310094
+ 00bd5788 bytes 96310094
~~~


<a id="compare-ab51549e3e3e71aca662d686431b9f7f"></a>

### [`00bd5768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5768.md) → [`00bd57ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57ac.md) __cxa_uncaught_exceptions

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0eb0.md) · 呼出先 1件 [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)
- 新版 呼出元 1件 [`00be0f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f00.md) · 呼出先 1件 [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5768.md#insn-00bd5774)
- 新版 [`00bd57b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57ac.md#insn-00bd57b8)

~~~diff
- 00bd5774 ["INT_ADD", "register:40f0:8", ["const:bd5774:8", "const:4:8"]]
- 00bd5774 ["CALL", null, ["callee:00be1de0:8"]]
+ 00bd57b8 ["INT_ADD", "register:40f0:8", ["const:bd57b8:8", "const:4:8"]]
+ 00bd57b8 ["CALL", null, ["callee:00be1de0:8"]]
- 00bd5774 bytes 87310094
+ 00bd57b8 bytes 8a310094
~~~


<a id="compare-16e7bcc8ca84a26b3d4b59934d898f33"></a>

### [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) → [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) FUN_00bd57d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bd4fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md) [`00bd51ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md) [`00bd55a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd55a4.md) · 呼出先 2件 [`00bd57dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd57dc.md) [`00be1ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ec0.md)
- 新版 呼出元 3件 [`00bd5008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md) [`00bd51f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md) [`00bd55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md) · 呼出先 2件 [`00bd5820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md) [`00be1f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd57b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md#insn-00bd57b8) · [`00bd57c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md#insn-00bd57c8)
- 新版 [`00bd57fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md#insn-00bd57fc) · [`00bd580c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md#insn-00bd580c)

~~~diff
- 00bd57b8 ["INT_ADD", "register:40f0:8", ["const:bd57b8:8", "const:4:8"]]
- 00bd57b8 ["CALL", null, ["callee:00be1f10:8"]]
+ 00bd57fc ["INT_ADD", "register:40f0:8", ["const:bd57fc:8", "const:4:8"]]
+ 00bd57fc ["CALL", null, ["callee:00be1f10:8"]]
- 00bd57b8 bytes c2310094
+ 00bd57fc bytes c5310094
- 00bd57c8 ["INT_ADD", "register:40f0:8", ["const:bd57c8:8", "const:4:8"]]
- 00bd57c8 ["CALL", null, ["callee:00bd5820:8"]]
+ 00bd580c ["INT_ADD", "register:40f0:8", ["const:bd580c:8", "const:4:8"]]
+ 00bd580c ["CALL", null, ["callee:00bd5820:8"]]
- 00bd57c8 bytes 05000094
+ 00bd580c bytes 05000094
~~~


<a id="compare-a496ca1ba045ad904447f60d0d0136d3"></a>

### [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) → [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) __gxx_personality_v0

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd4f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f94.md) [`00bd624c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md) [`00bd63f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md) [`00bd7224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd4fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fd8.md) [`00bd6290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md) [`00bd6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md) [`00bd7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md#insn-00bd5b14) · [`00bd5b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md#insn-00bd5b24) · [`00bd5b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md#insn-00bd5b30)
- 新版 [`00bd5b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md#insn-00bd5b58) · [`00bd5b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md#insn-00bd5b68) · [`00bd5b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md#insn-00bd5b74)

~~~diff
- 00bd5b14 ["INT_ADD", "register:40f0:8", ["const:bd5b14:8", "const:4:8"]]
- 00bd5b14 ["CALL", null, ["callee:00bd72e8:8"]]
+ 00bd5b58 ["INT_ADD", "register:40f0:8", ["const:bd5b58:8", "const:4:8"]]
+ 00bd5b58 ["CALL", null, ["callee:00bd72e8:8"]]
- 00bd5b14 bytes e5050094
+ 00bd5b58 bytes e4050094
- 00bd5b24 ["INT_ADD", "register:40f0:8", ["const:bd5b24:8", "const:4:8"]]
- 00bd5b24 ["CALL", null, ["callee:00bd72e8:8"]]
+ 00bd5b68 ["INT_ADD", "register:40f0:8", ["const:bd5b68:8", "const:4:8"]]
+ 00bd5b68 ["CALL", null, ["callee:00bd72e8:8"]]
- 00bd5b24 bytes e1050094
+ 00bd5b68 bytes e0050094
- 00bd5b30 ["INT_ADD", "register:40f0:8", ["const:bd5b30:8", "const:4:8"]]
- 00bd5b30 ["CALL", null, ["callee:00bd7320:8"]]
+ 00bd5b74 ["INT_ADD", "register:40f0:8", ["const:bd5b74:8", "const:4:8"]]
+ 00bd5b74 ["CALL", null, ["callee:00bd7320:8"]]
- 00bd5b30 bytes ec050094
+ 00bd5b74 bytes eb050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1729f62a5dd01a3ae6a0ff3bee709643"></a>

### [`00bd624c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md) → [`00bd6290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md) FUN_00bd6290

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) [`00bd63f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md) · 呼出先 1件 [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 3件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) [`00bd6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md) · 呼出先 1件 [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd63ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md#insn-00bd63ec) · [`00bd63f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md#insn-00bd63f0)
- 新版 [`00bd6430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md#insn-00bd6430) · [`00bd6434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md#insn-00bd6434)

~~~diff
- 00bd63ec ["INT_ADD", "register:40f0:8", ["const:bd63ec:8", "const:4:8"]]
- 00bd63ec ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bd6430 ["INT_ADD", "register:40f0:8", ["const:bd6430:8", "const:4:8"]]
+ 00bd6430 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bd63ec bytes a11f0094
+ 00bd6430 bytes a41f0094
- 00bd63f0 ["INT_ADD", "register:40f0:8", ["const:bd63f0:8", "const:4:8"]]
- 00bd63f0 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bd6434 ["INT_ADD", "register:40f0:8", ["const:bd6434:8", "const:4:8"]]
+ 00bd6434 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bd63f0 bytes a01f0094
+ 00bd6434 bytes a31f0094
~~~


<a id="compare-c1d55b4eab840e7eeaae4d4f89561926"></a>

### [`00bd63f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md) → [`00bd6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md) FUN_00bd6438

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) · 呼出先 4件 [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd624c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md) [`00bdb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb170.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 2件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) · 呼出先 4件 [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd6290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md) [`00bdb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1c0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd64a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md#insn-00bd64a0) · [`00bd64b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md#insn-00bd64b8) · [`00bd64fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md#insn-00bd64fc)
- 新版 [`00bd64e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md#insn-00bd64e4) · [`00bd64fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md#insn-00bd64fc) · [`00bd6540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md#insn-00bd6540)

~~~diff
- 00bd64a0 ["INT_ADD", "register:40f0:8", ["const:bd64a0:8", "const:4:8"]]
- 00bd64a0 ["CALL", null, ["callee:00bd6290:8"]]
+ 00bd64e4 ["INT_ADD", "register:40f0:8", ["const:bd64e4:8", "const:4:8"]]
+ 00bd64e4 ["CALL", null, ["callee:00bd6290:8"]]
- 00bd64a0 bytes 6bffff97
+ 00bd64e4 bytes 6bffff97
- 00bd64b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd64b8 ["INT_ADD", "register:40f0:8", ["const:bd64b8:8", "const:4:8"]]
- 00bd64b8 ["CALLIND", null, ["register:0:8"]]
+ 00bd64fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd64fc ["INT_ADD", "register:40f0:8", ["const:bd64fc:8", "const:4:8"]]
+ 00bd64fc ["CALLIND", null, ["register:0:8"]]
- 00bd64b8 bytes 00013fd6
+ 00bd64fc bytes 00013fd6
- 00bd64fc ["INT_ADD", "register:40f0:8", ["const:bd64fc:8", "const:4:8"]]
- 00bd64fc ["CALL", null, ["callee:00bdb1c0:8"]]
+ 00bd6540 ["INT_ADD", "register:40f0:8", ["const:bd6540:8", "const:4:8"]]
+ 00bd6540 ["CALL", null, ["callee:00bdb1c0:8"]]
- 00bd64fc bytes 1d130094
+ 00bd6540 bytes 20130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19a1cc2bb6434c92b71366940e50d08"></a>

### [`00bd7224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md) → [`00bd7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md) FUN_00bd7264

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) · 呼出先 1件 [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md)
- 新版 呼出元 1件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) · 呼出先 1件 [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md#insn-00bd7238)
- 新版 [`00bd7278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md#insn-00bd7278)

~~~diff
- 00bd7238 ["INT_ADD", "register:40f0:8", ["const:bd7238:8", "const:4:8"]]
- 00bd7238 ["CALL", null, ["callee:00bd7568:8"]]
+ 00bd7278 ["INT_ADD", "register:40f0:8", ["const:bd7278:8", "const:4:8"]]
+ 00bd7278 ["CALL", null, ["callee:00bd7568:8"]]
- 00bd7238 bytes bc000094
+ 00bd7278 bytes bc000094
~~~


<a id="compare-6c722862c40d1c97cb7732143d828b60"></a>

### [`00bd7258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7258.md) → [`00bd7298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7298.md) FUN_00bd7298

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) · 呼出先 1件 [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md)
- 新版 呼出元 1件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) · 呼出先 1件 [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd726c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7258.md#insn-00bd726c)
- 新版 [`00bd72ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7298.md#insn-00bd72ac)

~~~diff
- 00bd726c ["INT_ADD", "register:40f0:8", ["const:bd726c:8", "const:4:8"]]
- 00bd726c ["CALL", null, ["callee:00bd7568:8"]]
+ 00bd72ac ["INT_ADD", "register:40f0:8", ["const:bd72ac:8", "const:4:8"]]
+ 00bd72ac ["CALL", null, ["callee:00bd7568:8"]]
- 00bd726c bytes af000094
+ 00bd72ac bytes af000094
~~~


<a id="compare-7362484b316553c96020ad7ba90a821d"></a>

### [`00bd72b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72b0.md) → [`00bd72f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72f0.md) FUN_00bd72f0

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) · 呼出先 1件 [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md)
- 新版 呼出元 1件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) · 呼出先 1件 [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd72c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72b0.md#insn-00bd72c8)
- 新版 [`00bd7308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72f0.md#insn-00bd7308)

~~~diff
- 00bd72c8 ["INT_ADD", "register:40f0:8", ["const:bd72c8:8", "const:4:8"]]
- 00bd72c8 ["CALL", null, ["callee:00bd73d8:8"]]
+ 00bd7308 ["INT_ADD", "register:40f0:8", ["const:bd7308:8", "const:4:8"]]
+ 00bd7308 ["CALL", null, ["callee:00bd73d8:8"]]
- 00bd72c8 bytes 34000094
+ 00bd7308 bytes 34000094
~~~


<a id="compare-378151f16fd8c62c66a71333b59854a5"></a>

### [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md) → [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md) FUN_00bd73d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd72b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72b0.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd72f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72f0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd73c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md#insn-00bd73c0) · [`00bd73d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md#insn-00bd73d8)
- 新版 [`00bd7400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md#insn-00bd7400) · [`00bd7418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md#insn-00bd7418)

~~~diff
- 00bd73c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd73c0 ["INT_ADD", "register:40f0:8", ["const:bd73c0:8", "const:4:8"]]
- 00bd73c0 ["CALLIND", null, ["register:0:8"]]
+ 00bd7400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7400 ["INT_ADD", "register:40f0:8", ["const:bd7400:8", "const:4:8"]]
+ 00bd7400 ["CALLIND", null, ["register:0:8"]]
- 00bd73c0 bytes 00013fd6
+ 00bd7400 bytes 00013fd6
- 00bd73d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd73d8 ["INT_ADD", "register:40f0:8", ["const:bd73d8:8", "const:4:8"]]
- 00bd73d8 ["CALLIND", null, ["register:0:8"]]
+ 00bd7418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7418 ["INT_ADD", "register:40f0:8", ["const:bd7418:8", "const:4:8"]]
+ 00bd7418 ["CALLIND", null, ["register:0:8"]]
- 00bd73d8 bytes 00013fd6
+ 00bd7418 bytes 00013fd6
~~~


<a id="compare-16745abd0caf805b744d561ee7465c9c"></a>

### [`00bd7414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md) → [`00bd7454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md) FUN_00bd7454

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd72a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72a8.md) [`00bd72e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72e0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00bd72e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72e8.md) [`00bd7320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7320.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md#insn-00bd7440) · [`00bd745c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md#insn-00bd745c) · [`00bd7478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md#insn-00bd7478)
- 新版 [`00bd7480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md#insn-00bd7480) · [`00bd749c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md#insn-00bd749c) · [`00bd74b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md#insn-00bd74b8)

~~~diff
- 00bd7440 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7440 ["INT_ADD", "register:40f0:8", ["const:bd7440:8", "const:4:8"]]
- 00bd7440 ["CALLIND", null, ["register:0:8"]]
+ 00bd7480 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7480 ["INT_ADD", "register:40f0:8", ["const:bd7480:8", "const:4:8"]]
+ 00bd7480 ["CALLIND", null, ["register:0:8"]]
- 00bd7440 bytes 00013fd6
+ 00bd7480 bytes 00013fd6
- 00bd745c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd745c ["INT_ADD", "register:40f0:8", ["const:bd745c:8", "const:4:8"]]
- 00bd745c ["CALLIND", null, ["register:0:8"]]
+ 00bd749c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd749c ["INT_ADD", "register:40f0:8", ["const:bd749c:8", "const:4:8"]]
+ 00bd749c ["CALLIND", null, ["register:0:8"]]
- 00bd745c bytes 00013fd6
+ 00bd749c bytes 00013fd6
- 00bd7478 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7478 ["INT_ADD", "register:40f0:8", ["const:bd7478:8", "const:4:8"]]
- 00bd7478 ["CALLIND", null, ["register:0:8"]]
+ 00bd74b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd74b8 ["INT_ADD", "register:40f0:8", ["const:bd74b8:8", "const:4:8"]]
+ 00bd74b8 ["CALLIND", null, ["register:0:8"]]
- 00bd7478 bytes 00013fd6
+ 00bd74b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4c15d7153fcf415abf059fdc2c229f"></a>

### [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md) → [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md) FUN_00bd7568

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) [`00bd7224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md) [`00bd7258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7258.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) [`00bd7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md) [`00bd7298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7298.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md#insn-00bd7544)
- 新版 [`00bd7584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md#insn-00bd7584)

~~~diff
- 00bd7544 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7544 ["INT_ADD", "register:40f0:8", ["const:bd7544:8", "const:4:8"]]
- 00bd7544 ["CALLIND", null, ["register:0:8"]]
+ 00bd7584 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7584 ["INT_ADD", "register:40f0:8", ["const:bd7584:8", "const:4:8"]]
+ 00bd7584 ["CALLIND", null, ["register:0:8"]]
- 00bd7544 bytes 00013fd6
+ 00bd7584 bytes 00013fd6
~~~


<a id="compare-f86af15de80c330c617375abd55a5ff3"></a>

### [`00bd7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md) → [`00bd75a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md) FUN_00bd75a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md#insn-00bd757c)
- 新版 [`00bd75bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md#insn-00bd75bc)

~~~diff
- 00bd757c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd757c ["INT_ADD", "register:40f0:8", ["const:bd757c:8", "const:4:8"]]
- 00bd757c ["CALLIND", null, ["register:0:8"]]
+ 00bd75bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd75bc ["INT_ADD", "register:40f0:8", ["const:bd75bc:8", "const:4:8"]]
+ 00bd75bc ["CALLIND", null, ["register:0:8"]]
- 00bd757c bytes 00013fd6
+ 00bd75bc bytes 00013fd6
~~~


