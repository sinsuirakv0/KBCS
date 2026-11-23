# v15.7.3 → v15.7.4 · 要調査の変更候補 (14)

[一覧の目次](README.md)

<a id="compare-75ac4b1aba7fedbe7e7588fadcbb55d9"></a>

### [`00b77c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77c6c.md) → [`00b77cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77cb0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be1030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77c6c.md#insn-00b77cb8)
- 新版 [`00b77cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77cb0.md#insn-00b77cfc)

~~~diff
- 00b77cb8 ["INT_ADD", "register:40f0:8", ["const:b77cb8:8", "const:4:8"]]
- 00b77cb8 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b77cfc ["INT_ADD", "register:40f0:8", ["const:b77cfc:8", "const:4:8"]]
+ 00b77cfc ["CALL", null, ["callee:00b75a68:8"]]
- 00b77cb8 bytes 5bf7ff97
+ 00b77cfc bytes 5bf7ff97
~~~


<a id="compare-51c5b7f8cc9060467edf9e61d012a84a"></a>

### [`00b792b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b792b4.md) → [`00b792f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b792f8.md) _ZNSt6__ndk19to_stringEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0b0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7933c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b792b4.md#insn-00b7933c) · [`00b79384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b792b4.md#insn-00b79384) · [`00b793b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b792b4.md#insn-00b793b0)
- 新版 [`00b79380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b792f8.md#insn-00b79380) · [`00b793c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b792f8.md#insn-00b793c8) · [`00b793f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b792f8.md#insn-00b793f4)

~~~diff
- 00b7933c ["INT_ADD", "register:40f0:8", ["const:b7933c:8", "const:4:8"]]
- 00b7933c ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b79380 ["INT_ADD", "register:40f0:8", ["const:b79380:8", "const:4:8"]]
+ 00b79380 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7933c bytes 1a080094
+ 00b79380 bytes 1a080094
- 00b79384 ["INT_ADD", "register:40f0:8", ["const:b79384:8", "const:4:8"]]
- 00b79384 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b793c8 ["INT_ADD", "register:40f0:8", ["const:b793c8:8", "const:4:8"]]
+ 00b793c8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b79384 bytes 1b870194
+ 00b793c8 bytes 1e870194
- 00b793b0 ["INT_ADD", "register:40f0:8", ["const:b793b0:8", "const:4:8"]]
- 00b793b0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b793f4 ["INT_ADD", "register:40f0:8", ["const:b793f4:8", "const:4:8"]]
+ 00b793f4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b793b0 bytes 6c870194
+ 00b793f4 bytes 6f870194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf906b85fe43e31022a744aa270a7a9"></a>

### [`00b793dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b793dc.md) → [`00b79420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md) _ZNSt6__ndk19to_stringEl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb330.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdb380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb380.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b793dc.md#insn-00b79470) · [`00b794ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b793dc.md#insn-00b794ac) · [`00b795a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b793dc.md#insn-00b795a0)
- 新版 [`00b794b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md#insn-00b794b4) · [`00b794f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md#insn-00b794f0) · [`00b795e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md#insn-00b795e4)

~~~diff
- 00b79470 ["INT_ADD", "register:40f0:8", ["const:b79470:8", "const:4:8"]]
- 00b79470 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b794b4 ["INT_ADD", "register:40f0:8", ["const:b794b4:8", "const:4:8"]]
+ 00b794b4 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79470 bytes cd070094
+ 00b794b4 bytes cd070094
- 00b794ac ["INT_ADD", "register:40f0:8", ["const:b794ac:8", "const:4:8"]]
- 00b794ac ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b794f0 ["INT_ADD", "register:40f0:8", ["const:b794f0:8", "const:4:8"]]
+ 00b794f0 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b794ac bytes be070094
+ 00b794f0 bytes be070094
- 00b795a0 ["INT_ADD", "register:40f0:8", ["const:b795a0:8", "const:4:8"]]
- 00b795a0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b795e4 ["INT_ADD", "register:40f0:8", ["const:b795e4:8", "const:4:8"]]
+ 00b795e4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b795a0 bytes 94860194
+ 00b795e4 bytes 97860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-404d53508b7d8352b5dfb2096f0e5fdb"></a>

### [`00b795f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b795f8.md) → [`00b7963c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md) _ZNSt6__ndk19to_stringEx

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddca0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bddcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcf0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7968c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b795f8.md#insn-00b7968c) · [`00b796c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b795f8.md#insn-00b796c8) · [`00b797bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b795f8.md#insn-00b797bc)
- 新版 [`00b796d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md#insn-00b796d0) · [`00b7970c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md#insn-00b7970c) · [`00b79800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md#insn-00b79800)

~~~diff
- 00b7968c ["INT_ADD", "register:40f0:8", ["const:b7968c:8", "const:4:8"]]
- 00b7968c ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b796d0 ["INT_ADD", "register:40f0:8", ["const:b796d0:8", "const:4:8"]]
+ 00b796d0 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7968c bytes 46070094
+ 00b796d0 bytes 46070094
- 00b796c8 ["INT_ADD", "register:40f0:8", ["const:b796c8:8", "const:4:8"]]
- 00b796c8 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7970c ["INT_ADD", "register:40f0:8", ["const:b7970c:8", "const:4:8"]]
+ 00b7970c ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b796c8 bytes 37070094
+ 00b7970c bytes 37070094
- 00b797bc ["INT_ADD", "register:40f0:8", ["const:b797bc:8", "const:4:8"]]
- 00b797bc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b79800 ["INT_ADD", "register:40f0:8", ["const:b79800:8", "const:4:8"]]
+ 00b79800 ["CALL", null, ["callee:00bdb040:8"]]
- 00b797bc bytes 0d860194
+ 00b79800 bytes 10860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78e2fef150a6dcbd8f482aa284ebe9b9"></a>

### [`00b79814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md) → [`00b79858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7983c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md#insn-00b7983c) · [`00b79880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md#insn-00b79880) · [`00b798ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md#insn-00b798ac)
- 新版 [`00b79880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md#insn-00b79880) · [`00b798c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md#insn-00b798c4) · [`00b798f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md#insn-00b798f0)

~~~diff
- 00b7983c ["INT_ADD", "register:40f0:8", ["const:b7983c:8", "const:4:8"]]
- 00b7983c ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b79880 ["INT_ADD", "register:40f0:8", ["const:b79880:8", "const:4:8"]]
+ 00b79880 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7983c bytes da060094
+ 00b79880 bytes da060094
- 00b79880 ["INT_ADD", "register:40f0:8", ["const:b79880:8", "const:4:8"]]
- 00b79880 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b798c4 ["INT_ADD", "register:40f0:8", ["const:b798c4:8", "const:4:8"]]
+ 00b798c4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b79880 bytes dc850194
+ 00b798c4 bytes df850194
- 00b798ac ["INT_ADD", "register:40f0:8", ["const:b798ac:8", "const:4:8"]]
- 00b798ac ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b798f0 ["INT_ADD", "register:40f0:8", ["const:b798f0:8", "const:4:8"]]
+ 00b798f0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b798ac bytes 2d860194
+ 00b798f0 bytes 30860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f782b205a7fdfb57bf162b5fb58bf2d"></a>

### [`00b798d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b798d8.md) → [`00b7991c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md) _ZNSt6__ndk19to_stringEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2c0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdb310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb310.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b798d8.md#insn-00b79908) · [`00b79948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b798d8.md#insn-00b79948) · [`00b79a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b798d8.md#insn-00b79a48)
- 新版 [`00b7994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md#insn-00b7994c) · [`00b7998c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md#insn-00b7998c) · [`00b79a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md#insn-00b79a8c)

~~~diff
- 00b79908 ["INT_ADD", "register:40f0:8", ["const:b79908:8", "const:4:8"]]
- 00b79908 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7994c ["INT_ADD", "register:40f0:8", ["const:b7994c:8", "const:4:8"]]
+ 00b7994c ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79908 bytes a7060094
+ 00b7994c bytes a7060094
- 00b79948 ["INT_ADD", "register:40f0:8", ["const:b79948:8", "const:4:8"]]
- 00b79948 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7998c ["INT_ADD", "register:40f0:8", ["const:b7998c:8", "const:4:8"]]
+ 00b7998c ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79948 bytes 97060094
+ 00b7998c bytes 97060094
- 00b79a48 ["INT_ADD", "register:40f0:8", ["const:b79a48:8", "const:4:8"]]
- 00b79a48 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b79a8c ["INT_ADD", "register:40f0:8", ["const:b79a8c:8", "const:4:8"]]
+ 00b79a8c ["CALL", null, ["callee:00bdb040:8"]]
- 00b79a48 bytes 6a850194
+ 00b79a8c bytes 6d850194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-182b541ff3c95aa44a0f83e140f4167e"></a>

### [`00b79aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79aa0.md) → [`00b79ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md) _ZNSt6__ndk19to_stringEy

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79aa0.md#insn-00b79ad0) · [`00b79b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79aa0.md#insn-00b79b10) · [`00b79c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79aa0.md#insn-00b79c10)
- 新版 [`00b79b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md#insn-00b79b14) · [`00b79b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md#insn-00b79b54) · [`00b79c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md#insn-00b79c54)

~~~diff
- 00b79ad0 ["INT_ADD", "register:40f0:8", ["const:b79ad0:8", "const:4:8"]]
- 00b79ad0 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b79b14 ["INT_ADD", "register:40f0:8", ["const:b79b14:8", "const:4:8"]]
+ 00b79b14 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79ad0 bytes 35060094
+ 00b79b14 bytes 35060094
- 00b79b10 ["INT_ADD", "register:40f0:8", ["const:b79b10:8", "const:4:8"]]
- 00b79b10 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b79b54 ["INT_ADD", "register:40f0:8", ["const:b79b54:8", "const:4:8"]]
+ 00b79b54 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79b10 bytes 25060094
+ 00b79b54 bytes 25060094
- 00b79c10 ["INT_ADD", "register:40f0:8", ["const:b79c10:8", "const:4:8"]]
- 00b79c10 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b79c54 ["INT_ADD", "register:40f0:8", ["const:b79c54:8", "const:4:8"]]
+ 00b79c54 ["CALL", null, ["callee:00bdb040:8"]]
- 00b79c10 bytes f8840194
+ 00b79c54 bytes fb840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d60888fb30fea1ffdce88e734075ea6"></a>

### [`00b79c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79c68.md) → [`00b79cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79cac.md) _ZNSt6__ndk110to_wstringEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79c68.md#insn-00b79cf0) · [`00b79d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79c68.md#insn-00b79d48) · [`00b79e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79c68.md#insn-00b79e38)
- 新版 [`00b79d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79cac.md#insn-00b79d34) · [`00b79d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79cac.md#insn-00b79d8c) · [`00b79e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79cac.md#insn-00b79e7c)

~~~diff
- 00b79cf0 ["INT_ADD", "register:40f0:8", ["const:b79cf0:8", "const:4:8"]]
- 00b79cf0 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b79d34 ["INT_ADD", "register:40f0:8", ["const:b79d34:8", "const:4:8"]]
+ 00b79d34 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79cf0 bytes ad050094
+ 00b79d34 bytes ad050094
- 00b79d48 ["INT_ADD", "register:40f0:8", ["const:b79d48:8", "const:4:8"]]
- 00b79d48 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b79d8c ["INT_ADD", "register:40f0:8", ["const:b79d8c:8", "const:4:8"]]
+ 00b79d8c ["CALL", null, ["callee:00bdb040:8"]]
- 00b79d48 bytes aa840194
+ 00b79d8c bytes ad840194
- 00b79e38 ["INT_ADD", "register:40f0:8", ["const:b79e38:8", "const:4:8"]]
- 00b79e38 ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b79e7c ["INT_ADD", "register:40f0:8", ["const:b79e7c:8", "const:4:8"]]
+ 00b79e7c ["CALL", null, ["callee:006ad8a4:8"]]
- 00b79e38 bytes 9bceec97
+ 00b79e7c bytes 8aceec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6519f1065bcee4996a934dd57af392c5"></a>

### [`00b79e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79e40.md) → [`00b79e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md) _ZNSt6__ndk110to_wstringEl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79e40.md#insn-00b79ed4) · [`00b79f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79e40.md#insn-00b79f10) · [`00b7a014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79e40.md#insn-00b7a014)
- 新版 [`00b79f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md#insn-00b79f18) · [`00b79f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md#insn-00b79f54) · [`00b7a058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md#insn-00b7a058)

~~~diff
- 00b79ed4 ["INT_ADD", "register:40f0:8", ["const:b79ed4:8", "const:4:8"]]
- 00b79ed4 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b79f18 ["INT_ADD", "register:40f0:8", ["const:b79f18:8", "const:4:8"]]
+ 00b79f18 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79ed4 bytes 34050094
+ 00b79f18 bytes 34050094
- 00b79f10 ["INT_ADD", "register:40f0:8", ["const:b79f10:8", "const:4:8"]]
- 00b79f10 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b79f54 ["INT_ADD", "register:40f0:8", ["const:b79f54:8", "const:4:8"]]
+ 00b79f54 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b79f10 bytes 25050094
+ 00b79f54 bytes 25050094
- 00b7a014 ["INT_ADD", "register:40f0:8", ["const:b7a014:8", "const:4:8"]]
- 00b7a014 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7a058 ["INT_ADD", "register:40f0:8", ["const:b7a058:8", "const:4:8"]]
+ 00b7a058 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7a014 bytes f7830194
+ 00b7a058 bytes fa830194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19c1c29f8fd0b0da52b597871a5c3055"></a>

### [`00b7a10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a10c.md) → [`00b7a150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a150.md) _ZNSt6__ndk110to_wstringEx

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7a1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a10c.md#insn-00b7a1a0) · [`00b7a1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a10c.md#insn-00b7a1dc) · [`00b7a2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a10c.md#insn-00b7a2e0)
- 新版 [`00b7a1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a150.md#insn-00b7a1e4) · [`00b7a220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a150.md#insn-00b7a220) · [`00b7a324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a150.md#insn-00b7a324)

~~~diff
- 00b7a1a0 ["INT_ADD", "register:40f0:8", ["const:b7a1a0:8", "const:4:8"]]
- 00b7a1a0 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7a1e4 ["INT_ADD", "register:40f0:8", ["const:b7a1e4:8", "const:4:8"]]
+ 00b7a1e4 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7a1a0 bytes 81040094
+ 00b7a1e4 bytes 81040094
- 00b7a1dc ["INT_ADD", "register:40f0:8", ["const:b7a1dc:8", "const:4:8"]]
- 00b7a1dc ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7a220 ["INT_ADD", "register:40f0:8", ["const:b7a220:8", "const:4:8"]]
+ 00b7a220 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7a1dc bytes 72040094
+ 00b7a220 bytes 72040094
- 00b7a2e0 ["INT_ADD", "register:40f0:8", ["const:b7a2e0:8", "const:4:8"]]
- 00b7a2e0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7a324 ["INT_ADD", "register:40f0:8", ["const:b7a324:8", "const:4:8"]]
+ 00b7a324 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7a2e0 bytes 44830194
+ 00b7a324 bytes 47830194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0885d907e18b9a3cb8339c2d554e4d52"></a>

### [`00b7a3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a3d8.md) → [`00b7a41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a41c.md) _ZNSt6__ndk110to_wstringEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7a400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a3d8.md#insn-00b7a400) · [`00b7a454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a3d8.md#insn-00b7a454) · [`00b7a544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a3d8.md#insn-00b7a544)
- 新版 [`00b7a444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a41c.md#insn-00b7a444) · [`00b7a498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a41c.md#insn-00b7a498) · [`00b7a588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a41c.md#insn-00b7a588)

~~~diff
- 00b7a400 ["INT_ADD", "register:40f0:8", ["const:b7a400:8", "const:4:8"]]
- 00b7a400 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7a444 ["INT_ADD", "register:40f0:8", ["const:b7a444:8", "const:4:8"]]
+ 00b7a444 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7a400 bytes e9030094
+ 00b7a444 bytes e9030094
- 00b7a454 ["INT_ADD", "register:40f0:8", ["const:b7a454:8", "const:4:8"]]
- 00b7a454 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7a498 ["INT_ADD", "register:40f0:8", ["const:b7a498:8", "const:4:8"]]
+ 00b7a498 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7a454 bytes e7820194
+ 00b7a498 bytes ea820194
- 00b7a544 ["INT_ADD", "register:40f0:8", ["const:b7a544:8", "const:4:8"]]
- 00b7a544 ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b7a588 ["INT_ADD", "register:40f0:8", ["const:b7a588:8", "const:4:8"]]
+ 00b7a588 ["CALL", null, ["callee:006ad8a4:8"]]
- 00b7a544 bytes d8ccec97
+ 00b7a588 bytes c7ccec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb87426935fd599435cfbb53d218aef6"></a>

### [`00b7a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a54c.md) → [`00b7a590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md) _ZNSt6__ndk110to_wstringEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7a57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a54c.md#insn-00b7a57c) · [`00b7a5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a54c.md#insn-00b7a5bc) · [`00b7a6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a54c.md#insn-00b7a6cc)
- 新版 [`00b7a5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md#insn-00b7a5c0) · [`00b7a600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md#insn-00b7a600) · [`00b7a710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md#insn-00b7a710)

~~~diff
- 00b7a57c ["INT_ADD", "register:40f0:8", ["const:b7a57c:8", "const:4:8"]]
- 00b7a57c ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7a5c0 ["INT_ADD", "register:40f0:8", ["const:b7a5c0:8", "const:4:8"]]
+ 00b7a5c0 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7a57c bytes 8a030094
+ 00b7a5c0 bytes 8a030094
- 00b7a5bc ["INT_ADD", "register:40f0:8", ["const:b7a5bc:8", "const:4:8"]]
- 00b7a5bc ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7a600 ["INT_ADD", "register:40f0:8", ["const:b7a600:8", "const:4:8"]]
+ 00b7a600 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7a5bc bytes 7a030094
+ 00b7a600 bytes 7a030094
- 00b7a6cc ["INT_ADD", "register:40f0:8", ["const:b7a6cc:8", "const:4:8"]]
- 00b7a6cc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7a710 ["INT_ADD", "register:40f0:8", ["const:b7a710:8", "const:4:8"]]
+ 00b7a710 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7a6cc bytes 49820194
+ 00b7a710 bytes 4c820194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ddac157c5c865b60594e81beafd9cc3"></a>

### [`00b7a7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a7c4.md) → [`00b7a808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md) _ZNSt6__ndk110to_wstringEy

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7a7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a7c4.md#insn-00b7a7f4) · [`00b7a834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a7c4.md#insn-00b7a834) · [`00b7a944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a7c4.md#insn-00b7a944)
- 新版 [`00b7a838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md#insn-00b7a838) · [`00b7a878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md#insn-00b7a878) · [`00b7a988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md#insn-00b7a988)

~~~diff
- 00b7a7f4 ["INT_ADD", "register:40f0:8", ["const:b7a7f4:8", "const:4:8"]]
- 00b7a7f4 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7a838 ["INT_ADD", "register:40f0:8", ["const:b7a838:8", "const:4:8"]]
+ 00b7a838 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7a7f4 bytes ec020094
+ 00b7a838 bytes ec020094
- 00b7a834 ["INT_ADD", "register:40f0:8", ["const:b7a834:8", "const:4:8"]]
- 00b7a834 ["CALL", null, ["callee:00b7b3e8:8"]]
+ 00b7a878 ["INT_ADD", "register:40f0:8", ["const:b7a878:8", "const:4:8"]]
+ 00b7a878 ["CALL", null, ["callee:00b7b3e8:8"]]
- 00b7a834 bytes dc020094
+ 00b7a878 bytes dc020094
- 00b7a944 ["INT_ADD", "register:40f0:8", ["const:b7a944:8", "const:4:8"]]
- 00b7a944 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7a988 ["INT_ADD", "register:40f0:8", ["const:b7a988:8", "const:4:8"]]
+ 00b7a988 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7a944 bytes ab810194
+ 00b7a988 bytes ae810194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-961c9dfc2d0eb127f103740653726598"></a>

### [`00b7aa3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7aa3c.md) → [`00b7aa80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7aa80.md) _ZNSt6__ndk19to_stringEf

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd130.md) · 呼出先 3件 [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)
- 新版 呼出元 1件 [`00bdd180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd180.md) · 呼出先 3件 [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7aa7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7aa3c.md#insn-00b7aa7c) · [`00b7aab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7aa3c.md#insn-00b7aab4) · [`00b7aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7aa3c.md#insn-00b7aad4)
- 新版 [`00b7aac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7aa80.md#insn-00b7aac0) · [`00b7aaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7aa80.md#insn-00b7aaf8) · [`00b7ab18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7aa80.md#insn-00b7ab18)

~~~diff
- 00b7aa7c ["INT_ADD", "register:40f0:8", ["const:b7aa7c:8", "const:4:8"]]
- 00b7aa7c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b7aac0 ["INT_ADD", "register:40f0:8", ["const:b7aac0:8", "const:4:8"]]
+ 00b7aac0 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b7aa7c bytes 3d910194
+ 00b7aac0 bytes 40910194
- 00b7aab4 ["INT_ADD", "register:40f0:8", ["const:b7aab4:8", "const:4:8"]]
- 00b7aab4 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b7aaf8 ["INT_ADD", "register:40f0:8", ["const:b7aaf8:8", "const:4:8"]]
+ 00b7aaf8 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b7aab4 bytes 2f910194
+ 00b7aaf8 bytes 32910194
- 00b7aad4 ["INT_ADD", "register:40f0:8", ["const:b7aad4:8", "const:4:8"]]
- 00b7aad4 ["CALL", null, ["callee:00be1100:8"]]
+ 00b7ab18 ["INT_ADD", "register:40f0:8", ["const:b7ab18:8", "const:4:8"]]
+ 00b7ab18 ["CALL", null, ["callee:00be1100:8"]]
- 00b7aad4 bytes 77990194
+ 00b7ab18 bytes 7a990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bbeedd282a80d9736d3bb302116e11e"></a>

### [`00b7abd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md) → [`00b7ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7ac1c.md) _ZNSt6__ndk19to_stringEd

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8c0.md) · 呼出先 3件 [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)
- 新版 呼出元 1件 [`00bdd910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd910.md) · 呼出先 3件 [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ac18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md#insn-00b7ac18) · [`00b7ac4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md#insn-00b7ac4c) · [`00b7ac6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md#insn-00b7ac6c)
- 新版 [`00b7ac5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7ac1c.md#insn-00b7ac5c) · [`00b7ac90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7ac1c.md#insn-00b7ac90) · [`00b7acb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7ac1c.md#insn-00b7acb0)

~~~diff
- 00b7ac18 ["INT_ADD", "register:40f0:8", ["const:b7ac18:8", "const:4:8"]]
- 00b7ac18 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b7ac5c ["INT_ADD", "register:40f0:8", ["const:b7ac5c:8", "const:4:8"]]
+ 00b7ac5c ["CALL", null, ["callee:00bdefc0:8"]]
- 00b7ac18 bytes d6900194
+ 00b7ac5c bytes d9900194
- 00b7ac4c ["INT_ADD", "register:40f0:8", ["const:b7ac4c:8", "const:4:8"]]
- 00b7ac4c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b7ac90 ["INT_ADD", "register:40f0:8", ["const:b7ac90:8", "const:4:8"]]
+ 00b7ac90 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b7ac4c bytes c9900194
+ 00b7ac90 bytes cc900194
- 00b7ac6c ["INT_ADD", "register:40f0:8", ["const:b7ac6c:8", "const:4:8"]]
- 00b7ac6c ["CALL", null, ["callee:00be1100:8"]]
+ 00b7acb0 ["INT_ADD", "register:40f0:8", ["const:b7acb0:8", "const:4:8"]]
+ 00b7acb0 ["CALL", null, ["callee:00be1100:8"]]
- 00b7ac6c bytes 11990194
+ 00b7acb0 bytes 14990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a65e5b5428e29eecb014a2723303394"></a>

### [`00b7af00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md) → [`00b7af44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7af44.md) _ZNSt6__ndk110to_wstringEf

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) [`00be10c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10c0.md) [`00be10d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdda40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda40.md) [`00be1110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1110.md) [`00be1120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7af2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md#insn-00b7af2c) · [`00b7af64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md#insn-00b7af64) · [`00b7afa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md#insn-00b7afa8)
- 新版 [`00b7af70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7af44.md#insn-00b7af70) · [`00b7afa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7af44.md#insn-00b7afa8) · [`00b7afec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7af44.md#insn-00b7afec)

~~~diff
- 00b7af2c ["INT_ADD", "register:40f0:8", ["const:b7af2c:8", "const:4:8"]]
- 00b7af2c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7af70 ["INT_ADD", "register:40f0:8", ["const:b7af70:8", "const:4:8"]]
+ 00b7af70 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7af2c bytes 31800194
+ 00b7af70 bytes 34800194
- 00b7af64 ["INT_ADD", "register:40f0:8", ["const:b7af64:8", "const:4:8"]]
- 00b7af64 ["CALL", null, ["callee:00bdda40:8"]]
+ 00b7afa8 ["INT_ADD", "register:40f0:8", ["const:b7afa8:8", "const:4:8"]]
+ 00b7afa8 ["CALL", null, ["callee:00bdda40:8"]]
- 00b7af64 bytes a38a0194
+ 00b7afa8 bytes a68a0194
- 00b7afa8 ["INT_ADD", "register:40f0:8", ["const:b7afa8:8", "const:4:8"]]
- 00b7afa8 ["CALL", null, ["callee:00be1110:8"]]
+ 00b7afec ["INT_ADD", "register:40f0:8", ["const:b7afec:8", "const:4:8"]]
+ 00b7afec ["CALL", null, ["callee:00be1110:8"]]
- 00b7afa8 bytes 46980194
+ 00b7afec bytes 49980194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9e0c8e452ade00662e380e487e48ca7"></a>

### [`00b7b048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md) → [`00b7b08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b08c.md) _ZNSt6__ndk110to_wstringEd

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) [`00be10c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10c0.md) [`00be10d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdda40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda40.md) [`00be1110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1110.md) [`00be1120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7b074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md#insn-00b7b074) · [`00b7b0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md#insn-00b7b0ac) · [`00b7b0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md#insn-00b7b0ec)
- 新版 [`00b7b0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b08c.md#insn-00b7b0b8) · [`00b7b0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b08c.md#insn-00b7b0f0) · [`00b7b130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b08c.md#insn-00b7b130)

~~~diff
- 00b7b074 ["INT_ADD", "register:40f0:8", ["const:b7b074:8", "const:4:8"]]
- 00b7b074 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7b0b8 ["INT_ADD", "register:40f0:8", ["const:b7b0b8:8", "const:4:8"]]
+ 00b7b0b8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7b074 bytes df7f0194
+ 00b7b0b8 bytes e27f0194
- 00b7b0ac ["INT_ADD", "register:40f0:8", ["const:b7b0ac:8", "const:4:8"]]
- 00b7b0ac ["CALL", null, ["callee:00bdda40:8"]]
+ 00b7b0f0 ["INT_ADD", "register:40f0:8", ["const:b7b0f0:8", "const:4:8"]]
+ 00b7b0f0 ["CALL", null, ["callee:00bdda40:8"]]
- 00b7b0ac bytes 518a0194
+ 00b7b0f0 bytes 548a0194
- 00b7b0ec ["INT_ADD", "register:40f0:8", ["const:b7b0ec:8", "const:4:8"]]
- 00b7b0ec ["CALL", null, ["callee:00be1110:8"]]
+ 00b7b130 ["INT_ADD", "register:40f0:8", ["const:b7b130:8", "const:4:8"]]
+ 00b7b130 ["CALL", null, ["callee:00be1110:8"]]
- 00b7b0ec bytes f5970194
+ 00b7b130 bytes f8970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e41e7d570ebd81a40ebba097ccfd563"></a>

### [`00b7b18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md) → [`00b7b1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b1d0.md) _ZNSt6__ndk110to_wstringEe

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) [`00be10c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10c0.md) [`00be10d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdda40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda40.md) [`00be1110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1110.md) [`00be1120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7b1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md#insn-00b7b1b4) · [`00b7b1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md#insn-00b7b1ec) · [`00b7b22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md#insn-00b7b22c)
- 新版 [`00b7b1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b1d0.md#insn-00b7b1f8) · [`00b7b230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b1d0.md#insn-00b7b230) · [`00b7b270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b1d0.md#insn-00b7b270)

~~~diff
- 00b7b1b4 ["INT_ADD", "register:40f0:8", ["const:b7b1b4:8", "const:4:8"]]
- 00b7b1b4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7b1f8 ["INT_ADD", "register:40f0:8", ["const:b7b1f8:8", "const:4:8"]]
+ 00b7b1f8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7b1b4 bytes 8f7f0194
+ 00b7b1f8 bytes 927f0194
- 00b7b1ec ["INT_ADD", "register:40f0:8", ["const:b7b1ec:8", "const:4:8"]]
- 00b7b1ec ["CALL", null, ["callee:00bdda40:8"]]
+ 00b7b230 ["INT_ADD", "register:40f0:8", ["const:b7b230:8", "const:4:8"]]
+ 00b7b230 ["CALL", null, ["callee:00bdda40:8"]]
- 00b7b1ec bytes 018a0194
+ 00b7b230 bytes 048a0194
- 00b7b22c ["INT_ADD", "register:40f0:8", ["const:b7b22c:8", "const:4:8"]]
- 00b7b22c ["CALL", null, ["callee:00be1110:8"]]
+ 00b7b270 ["INT_ADD", "register:40f0:8", ["const:b7b270:8", "const:4:8"]]
+ 00b7b270 ["CALL", null, ["callee:00be1110:8"]]
- 00b7b22c bytes a5970194
+ 00b7b270 bytes a8970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-455be09ca9297e5462a50e2a677aa11c"></a>

### [`00b7b958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b958.md) → [`00b7b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b99c.md) FUN_00b7b99c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7b7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b7a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7b97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b958.md#insn-00b7b97c)
- 新版 [`00b7b9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b99c.md#insn-00b7b9c0)

~~~diff
- 00b7b97c ["INT_ADD", "register:40f0:8", ["const:b7b97c:8", "const:4:8"]]
- 00b7b97c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7b9c0 ["INT_ADD", "register:40f0:8", ["const:b7b9c0:8", "const:4:8"]]
+ 00b7b9c0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7b97c bytes 9d7d0194
+ 00b7b9c0 bytes a07d0194
~~~


<a id="compare-4f7e5439c79359e9376d15ff0822b40c"></a>

### [`00b7bb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bb60.md) → [`00b7bba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md) FUN_00b7bba4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00b7ba68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7ba68.md) [`00b7bc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bc34.md) [`00b7be48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7be48.md) [`00b7bf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bf54.md) · 呼出先 3件 [`007aae6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007aa/007aae6c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 4件 [`00b7baac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7baac.md) [`00b7bc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bc78.md) [`00b7be8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7be8c.md) [`00b7bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bf98.md) · 呼出先 3件 [`007aae6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007aa/007aae6c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7bbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bb60.md#insn-00b7bbb0) · [`00b7bbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bb60.md#insn-00b7bbc8) · [`00b7bbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bb60.md#insn-00b7bbd4)
- 新版 [`00b7bbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md#insn-00b7bbf4) · [`00b7bc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md#insn-00b7bc0c) · [`00b7bc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md#insn-00b7bc18)

~~~diff
- 00b7bbb0 ["INT_ADD", "register:40f0:8", ["const:b7bbb0:8", "const:4:8"]]
- 00b7bbb0 ["CALL", null, ["callee:00bdb120:8"]]
+ 00b7bbf4 ["INT_ADD", "register:40f0:8", ["const:b7bbf4:8", "const:4:8"]]
+ 00b7bbf4 ["CALL", null, ["callee:00bdb120:8"]]
- 00b7bbb0 bytes 487d0194
+ 00b7bbf4 bytes 4b7d0194
- 00b7bbc8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7bbc8 ["INT_ADD", "register:40f0:8", ["const:b7bbc8:8", "const:4:8"]]
- 00b7bbc8 ["CALLIND", null, ["register:0:8"]]
+ 00b7bc0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b7bc0c ["INT_ADD", "register:40f0:8", ["const:b7bc0c:8", "const:4:8"]]
+ 00b7bc0c ["CALLIND", null, ["register:0:8"]]
- 00b7bbc8 bytes 20013fd6
+ 00b7bc0c bytes 20013fd6
- 00b7bbd4 ["INT_ADD", "register:40f0:8", ["const:b7bbd4:8", "const:4:8"]]
- 00b7bbd4 ["CALL", null, ["callee:007aae6c:8"]]
+ 00b7bc18 ["INT_ADD", "register:40f0:8", ["const:b7bc18:8", "const:4:8"]]
+ 00b7bc18 ["CALL", null, ["callee:007aae6c:8"]]
- 00b7bbd4 bytes a6bcf097
+ 00b7bc18 bytes 95bcf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83baa858b4320694d33f4b42f740578f"></a>

### [`00b7c188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c188.md) → [`00b7c1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1cc.md) _ZNSt6__ndk112system_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c188.md#insn-00b7c19c)
- 新版 [`00b7c1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1cc.md#insn-00b7c1e0)

~~~diff
- 00b7c19c ["INT_ADD", "register:40f0:8", ["const:b7c19c:8", "const:4:8"]]
- 00b7c19c ["CALL", null, ["callee:00be1180:8"]]
+ 00b7c1e0 ["INT_ADD", "register:40f0:8", ["const:b7c1e0:8", "const:4:8"]]
+ 00b7c1e0 ["CALL", null, ["callee:00be1180:8"]]
- 00b7c19c bytes e5930194
+ 00b7c1e0 bytes e8930194
~~~


<a id="compare-4583cef0c9c6dbcfcc1bb00305ede75f"></a>

### [`00b7c23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c23c.md) → [`00b7c280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c280.md) FUN_00b7c280

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c23c.md#insn-00b7c250)
- 新版 [`00b7c294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c280.md#insn-00b7c294)

~~~diff
- 00b7c250 ["INT_ADD", "register:40f0:8", ["const:b7c250:8", "const:4:8"]]
- 00b7c250 ["CALL", null, ["callee:00be0ef0:8"]]
+ 00b7c294 ["INT_ADD", "register:40f0:8", ["const:b7c294:8", "const:4:8"]]
+ 00b7c294 ["CALL", null, ["callee:00be0ef0:8"]]
- 00b7c250 bytes 14930194
+ 00b7c294 bytes 17930194
~~~


<a id="compare-ab29490610fb29accdd49d62708626f1"></a>

### [`00b7c268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c268.md) → [`00b7c2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c2ac.md) FUN_00b7c2ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c268.md#insn-00b7c27c)
- 新版 [`00b7c2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c2ac.md#insn-00b7c2c0)

~~~diff
- 00b7c27c ["INT_ADD", "register:40f0:8", ["const:b7c27c:8", "const:4:8"]]
- 00b7c27c ["CALL", null, ["callee:00be0ef0:8"]]
+ 00b7c2c0 ["INT_ADD", "register:40f0:8", ["const:b7c2c0:8", "const:4:8"]]
+ 00b7c2c0 ["CALL", null, ["callee:00be0ef0:8"]]
- 00b7c27c bytes 09930194
+ 00b7c2c0 bytes 0c930194
~~~


<a id="compare-b71ca81a25810df9360b96f76c1942ec"></a>

### [`00b7c2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c2d0.md) → [`00b7c314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c314.md) _ZNKSt6__ndk114error_category10equivalentEiRKNS_15error_conditionE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c2d0.md#insn-00b7c2ec)
- 新版 [`00b7c330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c314.md#insn-00b7c330)

~~~diff
- 00b7c2ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7c2ec ["INT_ADD", "register:40f0:8", ["const:b7c2ec:8", "const:4:8"]]
- 00b7c2ec ["CALLIND", null, ["register:0:8"]]
+ 00b7c330 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7c330 ["INT_ADD", "register:40f0:8", ["const:b7c330:8", "const:4:8"]]
+ 00b7c330 ["CALLIND", null, ["register:0:8"]]
- 00b7c2ec bytes 00013fd6
+ 00b7c330 bytes 00013fd6
~~~


<a id="compare-1eccdf1e75f395f2910d744bc555aae8"></a>

### [`00b7c330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c330.md) → [`00b7c374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c374.md) _ZNSt6__ndk118condition_variableD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) · 呼出先 1件 [`00be05f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05f0.md)
- 新版 呼出元 1件 [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) · 呼出先 1件 [`00be0640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c330.md#insn-00b7c33c)
- 新版 [`00b7c380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c374.md#insn-00b7c380)

~~~diff
- 00b7c33c ["INT_ADD", "register:40f0:8", ["const:b7c33c:8", "const:4:8"]]
- 00b7c33c ["CALL", null, ["callee:00be0640:8"]]
+ 00b7c380 ["INT_ADD", "register:40f0:8", ["const:b7c380:8", "const:4:8"]]
+ 00b7c380 ["CALL", null, ["callee:00be0640:8"]]
- 00b7c33c bytes ad900194
+ 00b7c380 bytes b0900194
~~~


<a id="compare-050dd244410b30d7dab4a309aeb5630b"></a>

### [`00b7c350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c350.md) → [`00b7c394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c394.md) _ZNSt6__ndk118condition_variable10notify_oneEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc270.md) · 呼出先 1件 [`00be0600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0600.md)
- 新版 呼出元 1件 [`00bdc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2c0.md) · 呼出先 1件 [`00be0650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c350.md#insn-00b7c35c)
- 新版 [`00b7c3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c394.md#insn-00b7c3a0)

~~~diff
- 00b7c35c ["INT_ADD", "register:40f0:8", ["const:b7c35c:8", "const:4:8"]]
- 00b7c35c ["CALL", null, ["callee:00be0650:8"]]
+ 00b7c3a0 ["INT_ADD", "register:40f0:8", ["const:b7c3a0:8", "const:4:8"]]
+ 00b7c3a0 ["CALL", null, ["callee:00be0650:8"]]
- 00b7c35c bytes a9900194
+ 00b7c3a0 bytes ac900194
~~~


<a id="compare-184c2fad3770395e0725a4dd00efeb95"></a>

### [`00b7c370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c370.md) → [`00b7c3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c3b4.md) _ZNSt6__ndk118condition_variable10notify_allEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md) · 呼出先 1件 [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)
- 新版 呼出元 1件 [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) · 呼出先 1件 [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c370.md#insn-00b7c37c)
- 新版 [`00b7c3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c3b4.md#insn-00b7c3c0)

~~~diff
- 00b7c37c ["INT_ADD", "register:40f0:8", ["const:b7c37c:8", "const:4:8"]]
- 00b7c37c ["CALL", null, ["callee:00be11c0:8"]]
+ 00b7c3c0 ["INT_ADD", "register:40f0:8", ["const:b7c3c0:8", "const:4:8"]]
+ 00b7c3c0 ["CALL", null, ["callee:00be11c0:8"]]
- 00b7c37c bytes 7d930194
+ 00b7c3c0 bytes 80930194
~~~


<a id="compare-7f0fcbfb2ae83f10e67bd65a64d06de6"></a>

### [`00b7c47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md) → [`00b7c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md) _ZNSt6__ndk125notify_all_at_thread_exitERNS_18condition_variableENS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00be11a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11a0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00be11f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md#insn-00b7c498) · [`00b7c4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md#insn-00b7c4a4) · [`00b7c4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md#insn-00b7c4b0)
- 新版 [`00b7c4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md#insn-00b7c4dc) · [`00b7c4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md#insn-00b7c4e8) · [`00b7c4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c4c0.md#insn-00b7c4f4)

~~~diff
- 00b7c498 ["INT_ADD", "register:40f0:8", ["const:b7c498:8", "const:4:8"]]
- 00b7c498 ["CALL", null, ["callee:00bdb2e0:8"]]
+ 00b7c4dc ["INT_ADD", "register:40f0:8", ["const:b7c4dc:8", "const:4:8"]]
+ 00b7c4dc ["CALL", null, ["callee:00bdb2e0:8"]]
- 00b7c498 bytes 7e7b0194
+ 00b7c4dc bytes 817b0194
- 00b7c4a4 ["INT_ADD", "register:40f0:8", ["const:b7c4a4:8", "const:4:8"]]
- 00b7c4a4 ["CALL", null, ["callee:00be11f0:8"]]
+ 00b7c4e8 ["INT_ADD", "register:40f0:8", ["const:b7c4e8:8", "const:4:8"]]
+ 00b7c4e8 ["CALL", null, ["callee:00be11f0:8"]]
- 00b7c4a4 bytes 3f930194
+ 00b7c4e8 bytes 42930194
- 00b7c4b0 ["INT_ADD", "register:40f0:8", ["const:b7c4b0:8", "const:4:8"]]
- 00b7c4b0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7c4f4 ["INT_ADD", "register:40f0:8", ["const:b7c4f4:8", "const:4:8"]]
+ 00b7c4f4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7c4b0 bytes d07a0194
+ 00b7c4f4 bytes d37a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991a36fb9939506fe75015dab2f9c6f3"></a>

### [`00b7c78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c78c.md) → [`00b7c7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c7d0.md) _ZNSt6__ndk112future_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c78c.md#insn-00b7c7a0)
- 新版 [`00b7c7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c7d0.md#insn-00b7c7e4)

~~~diff
- 00b7c7a0 ["INT_ADD", "register:40f0:8", ["const:b7c7a0:8", "const:4:8"]]
- 00b7c7a0 ["CALL", null, ["callee:00bdb520:8"]]
+ 00b7c7e4 ["INT_ADD", "register:40f0:8", ["const:b7c7e4:8", "const:4:8"]]
+ 00b7c7e4 ["CALL", null, ["callee:00bdb520:8"]]
- 00b7c7a0 bytes 4c7b0194
+ 00b7c7e4 bytes 4f7b0194
~~~


<a id="compare-4186cfcec9cb1b6d0d29e7b97d05f06d"></a>

### [`00b7c7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md) → [`00b7c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md) _ZNSt6__ndk117__assoc_sub_state9set_valueEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6b0.md) · 呼出先 5件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md)
- 新版 呼出元 1件 [`00bdb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb700.md) · 呼出先 5件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md#insn-00b7c7e4) · [`00b7c7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md#insn-00b7c7fc) · [`00b7c818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md#insn-00b7c818)
- 新版 [`00b7c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md#insn-00b7c828) · [`00b7c840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md#insn-00b7c840) · [`00b7c85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md#insn-00b7c85c)

~~~diff
- 00b7c7e4 ["INT_ADD", "register:40f0:8", ["const:b7c7e4:8", "const:4:8"]]
- 00b7c7e4 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7c828 ["INT_ADD", "register:40f0:8", ["const:b7c828:8", "const:4:8"]]
+ 00b7c828 ["CALL", null, ["callee:00bdb290:8"]]
- 00b7c7e4 bytes 977a0194
+ 00b7c828 bytes 9a7a0194
- 00b7c7fc ["INT_ADD", "register:40f0:8", ["const:b7c7fc:8", "const:4:8"]]
- 00b7c7fc ["CALL", null, ["callee:00bdb4a0:8"]]
+ 00b7c840 ["INT_ADD", "register:40f0:8", ["const:b7c840:8", "const:4:8"]]
+ 00b7c840 ["CALL", null, ["callee:00bdb4a0:8"]]
- 00b7c7fc bytes 157b0194
+ 00b7c840 bytes 187b0194
- 00b7c818 ["INT_ADD", "register:40f0:8", ["const:b7c818:8", "const:4:8"]]
- 00b7c818 ["CALL", null, ["callee:00bdb530:8"]]
+ 00b7c85c ["INT_ADD", "register:40f0:8", ["const:b7c85c:8", "const:4:8"]]
+ 00b7c85c ["CALL", null, ["callee:00bdb530:8"]]
- 00b7c818 bytes 327b0194
+ 00b7c85c bytes 357b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf9c33d7657cb9813e7d219aa1f2fe28"></a>

### [`00b7c854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md) → [`00b7c898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md) _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be11d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11d0.md) · 呼出先 7件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)
- 新版 呼出元 1件 [`00be1220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1220.md) · 呼出先 7件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md#insn-00b7c870) · [`00b7c888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md#insn-00b7c888) · [`00b7c89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md#insn-00b7c89c)
- 新版 [`00b7c8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md#insn-00b7c8b4) · [`00b7c8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md#insn-00b7c8cc) · [`00b7c8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md#insn-00b7c8e0)

~~~diff
- 00b7c870 ["INT_ADD", "register:40f0:8", ["const:b7c870:8", "const:4:8"]]
- 00b7c870 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7c8b4 ["INT_ADD", "register:40f0:8", ["const:b7c8b4:8", "const:4:8"]]
+ 00b7c8b4 ["CALL", null, ["callee:00bdb290:8"]]
- 00b7c870 bytes 747a0194
+ 00b7c8b4 bytes 777a0194
- 00b7c888 ["INT_ADD", "register:40f0:8", ["const:b7c888:8", "const:4:8"]]
- 00b7c888 ["CALL", null, ["callee:00bdb4a0:8"]]
+ 00b7c8cc ["INT_ADD", "register:40f0:8", ["const:b7c8cc:8", "const:4:8"]]
+ 00b7c8cc ["CALL", null, ["callee:00bdb4a0:8"]]
- 00b7c888 bytes f27a0194
+ 00b7c8cc bytes f57a0194
- 00b7c89c ["INT_ADD", "register:40f0:8", ["const:b7c89c:8", "const:4:8"]]
- 00b7c89c ["CALL", null, ["callee:00bdb2e0:8"]]
+ 00b7c8e0 ["INT_ADD", "register:40f0:8", ["const:b7c8e0:8", "const:4:8"]]
+ 00b7c8e0 ["CALL", null, ["callee:00bdb2e0:8"]]
- 00b7c89c bytes 7d7a0194
+ 00b7c8e0 bytes 807a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49f1c713ebf1646203296701a0ece006"></a>

### [`00b7c8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md) → [`00b7c92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md) _ZNSt6__ndk117__assoc_sub_state13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4c0.md) · 呼出先 6件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md)
- 新版 呼出元 1件 [`00bdb510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb510.md) · 呼出先 6件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c90c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md#insn-00b7c90c) · [`00b7c928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md#insn-00b7c928) · [`00b7c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md#insn-00b7c938)
- 新版 [`00b7c950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md#insn-00b7c950) · [`00b7c96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md#insn-00b7c96c) · [`00b7c97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md#insn-00b7c97c)

~~~diff
- 00b7c90c ["INT_ADD", "register:40f0:8", ["const:b7c90c:8", "const:4:8"]]
- 00b7c90c ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7c950 ["INT_ADD", "register:40f0:8", ["const:b7c950:8", "const:4:8"]]
+ 00b7c950 ["CALL", null, ["callee:00bdb290:8"]]
- 00b7c90c bytes 4d7a0194
+ 00b7c950 bytes 507a0194
- 00b7c928 ["INT_ADD", "register:40f0:8", ["const:b7c928:8", "const:4:8"]]
- 00b7c928 ["CALL", null, ["callee:00bdb4a0:8"]]
+ 00b7c96c ["INT_ADD", "register:40f0:8", ["const:b7c96c:8", "const:4:8"]]
+ 00b7c96c ["CALL", null, ["callee:00bdb4a0:8"]]
- 00b7c928 bytes ca7a0194
+ 00b7c96c bytes cd7a0194
- 00b7c938 ["INT_ADD", "register:40f0:8", ["const:b7c938:8", "const:4:8"]]
- 00b7c938 ["CALL", null, ["callee:00be0f30:8"]]
+ 00b7c97c ["INT_ADD", "register:40f0:8", ["const:b7c97c:8", "const:4:8"]]
+ 00b7c97c ["CALL", null, ["callee:00be0f30:8"]]
- 00b7c938 bytes 6a910194
+ 00b7c97c bytes 6d910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b216d3eae0dbf2c926f9d7ae9e827ac"></a>

### [`00b7c98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md) → [`00b7c9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md) _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11f0.md) · 呼出先 8件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)
- 新版 呼出元 1件 [`00be1240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1240.md) · 呼出先 8件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md#insn-00b7c9b0) · [`00b7c9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md#insn-00b7c9cc) · [`00b7c9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md#insn-00b7c9dc)
- 新版 [`00b7c9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md#insn-00b7c9f4) · [`00b7ca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md#insn-00b7ca10) · [`00b7ca20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md#insn-00b7ca20)

~~~diff
- 00b7c9b0 ["INT_ADD", "register:40f0:8", ["const:b7c9b0:8", "const:4:8"]]
- 00b7c9b0 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7c9f4 ["INT_ADD", "register:40f0:8", ["const:b7c9f4:8", "const:4:8"]]
+ 00b7c9f4 ["CALL", null, ["callee:00bdb290:8"]]
- 00b7c9b0 bytes 247a0194
+ 00b7c9f4 bytes 277a0194
- 00b7c9cc ["INT_ADD", "register:40f0:8", ["const:b7c9cc:8", "const:4:8"]]
- 00b7c9cc ["CALL", null, ["callee:00bdb4a0:8"]]
+ 00b7ca10 ["INT_ADD", "register:40f0:8", ["const:b7ca10:8", "const:4:8"]]
+ 00b7ca10 ["CALL", null, ["callee:00bdb4a0:8"]]
- 00b7c9cc bytes a17a0194
+ 00b7ca10 bytes a47a0194
- 00b7c9dc ["INT_ADD", "register:40f0:8", ["const:b7c9dc:8", "const:4:8"]]
- 00b7c9dc ["CALL", null, ["callee:00be0f30:8"]]
+ 00b7ca20 ["INT_ADD", "register:40f0:8", ["const:b7ca20:8", "const:4:8"]]
+ 00b7ca20 ["CALL", null, ["callee:00be0f30:8"]]
- 00b7c9dc bytes 41910194
+ 00b7ca20 bytes 44910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb3a2a31bffdaac915da89c256dea748"></a>

### [`00b7ca30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca30.md) → [`00b7ca74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ca74.md) _ZNSt6__ndk117__assoc_sub_state12__make_readyEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1200.md) · 呼出先 3件 [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md)
- 新版 呼出元 1件 [`00be1250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1250.md) · 呼出先 3件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca30.md#insn-00b7ca48) · [`00b7ca5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca30.md#insn-00b7ca5c)
- 新版 [`00b7ca8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ca74.md#insn-00b7ca8c) · [`00b7caa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ca74.md#insn-00b7caa0)

~~~diff
- 00b7ca48 ["INT_ADD", "register:40f0:8", ["const:b7ca48:8", "const:4:8"]]
- 00b7ca48 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7ca8c ["INT_ADD", "register:40f0:8", ["const:b7ca8c:8", "const:4:8"]]
+ 00b7ca8c ["CALL", null, ["callee:00bdb290:8"]]
- 00b7ca48 bytes fe790194
+ 00b7ca8c bytes 017a0194
- 00b7ca5c ["INT_ADD", "register:40f0:8", ["const:b7ca5c:8", "const:4:8"]]
- 00b7ca5c ["CALL", null, ["callee:00bdb530:8"]]
+ 00b7caa0 ["INT_ADD", "register:40f0:8", ["const:b7caa0:8", "const:4:8"]]
+ 00b7caa0 ["CALL", null, ["callee:00bdb530:8"]]
- 00b7ca5c bytes a17a0194
+ 00b7caa0 bytes a47a0194
~~~


<a id="compare-8d0e225e7eb2b3506c3066ad067b5d85"></a>

### [`00b7ca74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md) → [`00b7cab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md) _ZNSt6__ndk117__assoc_sub_state4copyEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1210.md) · 呼出先 7件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md)
- 新版 呼出元 1件 [`00be1260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1260.md) · 呼出先 7件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7caa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md#insn-00b7caa0) · [`00b7cab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md#insn-00b7cab8) · [`00b7cad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md#insn-00b7cad4)
- 新版 [`00b7cae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md#insn-00b7cae4) · [`00b7cafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md#insn-00b7cafc) · [`00b7cb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md#insn-00b7cb18)

~~~diff
- 00b7caa0 ["INT_ADD", "register:40f0:8", ["const:b7caa0:8", "const:4:8"]]
- 00b7caa0 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7cae4 ["INT_ADD", "register:40f0:8", ["const:b7cae4:8", "const:4:8"]]
+ 00b7cae4 ["CALL", null, ["callee:00bdb290:8"]]
- 00b7caa0 bytes e8790194
+ 00b7cae4 bytes eb790194
- 00b7cab8 ["INT_ADD", "register:40f0:8", ["const:b7cab8:8", "const:4:8"]]
- 00b7cab8 ["CALL", null, ["callee:00bdb630:8"]]
+ 00b7cafc ["INT_ADD", "register:40f0:8", ["const:b7cafc:8", "const:4:8"]]
+ 00b7cafc ["CALL", null, ["callee:00bdb630:8"]]
- 00b7cab8 bytes ca7a0194
+ 00b7cafc bytes cd7a0194
- 00b7cad4 ["INT_ADD", "register:40f0:8", ["const:b7cad4:8", "const:4:8"]]
- 00b7cad4 ["CALL", null, ["callee:00bdb2a0:8"]]
+ 00b7cb18 ["INT_ADD", "register:40f0:8", ["const:b7cb18:8", "const:4:8"]]
+ 00b7cb18 ["CALL", null, ["callee:00bdb2a0:8"]]
- 00b7cad4 bytes df790194
+ 00b7cb18 bytes e2790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7766fe12a54a251157e6e5b7d9e183b6"></a>

### [`00b7cb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cb5c.md) → [`00b7cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb600.md) · 呼出先 3件 [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md)
- 新版 呼出元 1件 [`00bdb650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb650.md) · 呼出先 3件 [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cb5c.md#insn-00b7cb88) · [`00b7cbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cb5c.md#insn-00b7cbb8) · [`00b7cbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cb5c.md#insn-00b7cbe8)
- 新版 [`00b7cbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md#insn-00b7cbcc) · [`00b7cbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md#insn-00b7cbfc) · [`00b7cc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md#insn-00b7cc2c)

~~~diff
- 00b7cb88 ["INT_ADD", "register:40f0:8", ["const:b7cb88:8", "const:4:8"]]
- 00b7cb88 ["CALL", null, ["callee:00bdb630:8"]]
+ 00b7cbcc ["INT_ADD", "register:40f0:8", ["const:b7cbcc:8", "const:4:8"]]
+ 00b7cbcc ["CALL", null, ["callee:00bdb630:8"]]
- 00b7cb88 bytes 967a0194
+ 00b7cbcc bytes 997a0194
- 00b7cbb8 ["INT_ADD", "register:40f0:8", ["const:b7cbb8:8", "const:4:8"]]
- 00b7cbb8 ["CALL", null, ["callee:00bdb2a0:8"]]
+ 00b7cbfc ["INT_ADD", "register:40f0:8", ["const:b7cbfc:8", "const:4:8"]]
+ 00b7cbfc ["CALL", null, ["callee:00bdb2a0:8"]]
- 00b7cbb8 bytes a6790194
+ 00b7cbfc bytes a9790194
- 00b7cbe8 ["INT_ADD", "register:40f0:8", ["const:b7cbe8:8", "const:4:8"]]
- 00b7cbe8 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7cc2c ["INT_ADD", "register:40f0:8", ["const:b7cc2c:8", "const:4:8"]]
+ 00b7cc2c ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7cbe8 bytes a6790194
+ 00b7cc2c bytes a9790194
~~~


<a id="compare-2856bc0fc7ba1491cd82c89636d7941f"></a>

### [`00b7cbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md) → [`00b7cc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md) _ZNSt6__ndk117__assoc_sub_state4waitEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb690.md) · 呼出先 3件 [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md)
- 新版 呼出元 1件 [`00bdb6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6e0.md) · 呼出先 3件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md#insn-00b7cc18) · [`00b7cc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md#insn-00b7cc30) · [`00b7cc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md#insn-00b7cc48)
- 新版 [`00b7cc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md#insn-00b7cc5c) · [`00b7cc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md#insn-00b7cc74) · [`00b7cc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md#insn-00b7cc8c)

~~~diff
- 00b7cc18 ["INT_ADD", "register:40f0:8", ["const:b7cc18:8", "const:4:8"]]
- 00b7cc18 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7cc5c ["INT_ADD", "register:40f0:8", ["const:b7cc5c:8", "const:4:8"]]
+ 00b7cc5c ["CALL", null, ["callee:00bdb290:8"]]
- 00b7cc18 bytes 8a790194
+ 00b7cc5c bytes 8d790194
- 00b7cc30 ["INT_ADD", "register:40f0:8", ["const:b7cc30:8", "const:4:8"]]
- 00b7cc30 ["CALL", null, ["callee:00bdb630:8"]]
+ 00b7cc74 ["INT_ADD", "register:40f0:8", ["const:b7cc74:8", "const:4:8"]]
+ 00b7cc74 ["CALL", null, ["callee:00bdb630:8"]]
- 00b7cc30 bytes 6c7a0194
+ 00b7cc74 bytes 6f7a0194
- 00b7cc48 ["INT_ADD", "register:40f0:8", ["const:b7cc48:8", "const:4:8"]]
- 00b7cc48 ["CALL", null, ["callee:00bdb2a0:8"]]
+ 00b7cc8c ["INT_ADD", "register:40f0:8", ["const:b7cc8c:8", "const:4:8"]]
+ 00b7cc8c ["CALL", null, ["callee:00bdb2a0:8"]]
- 00b7cc48 bytes 82790194
+ 00b7cc8c bytes 85790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcab2ab631ba4ee435a09b9d6b738167"></a>

### [`00b7cc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cc90.md) → [`00b7ccd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ccd4.md) _ZNSt6__ndk117__assoc_sub_state9__executeEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cc90.md#insn-00b7cca0)
- 新版 [`00b7cce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ccd4.md#insn-00b7cce4)

~~~diff
- 00b7cca0 ["INT_ADD", "register:40f0:8", ["const:b7cca0:8", "const:4:8"]]
- 00b7cca0 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7cce4 ["INT_ADD", "register:40f0:8", ["const:b7cce4:8", "const:4:8"]]
+ 00b7cce4 ["CALL", null, ["callee:004377fc:8"]]
- 00b7cca0 bytes d7eae297
+ 00b7cce4 bytes c6eae297
~~~


<a id="compare-d65e41c177892bf92f88b4744d362279"></a>

### [`00b7cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md) → [`00b7cce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md) _ZNSt6__ndk16futureIvEC2EPNS_17__assoc_sub_stateE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb680.md) · 呼出先 4件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md)
- 新版 呼出元 1件 [`00bdb6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6d0.md) · 呼出先 4件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ccc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md#insn-00b7ccc0) · [`00b7ccd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md#insn-00b7ccd4) · [`00b7ccf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md#insn-00b7ccf8)
- 新版 [`00b7cd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md#insn-00b7cd04) · [`00b7cd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md#insn-00b7cd18) · [`00b7cd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cce8.md#insn-00b7cd3c)

~~~diff
- 00b7ccc0 ["INT_ADD", "register:40f0:8", ["const:b7ccc0:8", "const:4:8"]]
- 00b7ccc0 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7cd04 ["INT_ADD", "register:40f0:8", ["const:b7cd04:8", "const:4:8"]]
+ 00b7cd04 ["CALL", null, ["callee:00bdb290:8"]]
- 00b7ccc0 bytes 60790194
+ 00b7cd04 bytes 63790194
- 00b7ccd4 ["INT_ADD", "register:40f0:8", ["const:b7ccd4:8", "const:4:8"]]
- 00b7ccd4 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00b7cd18 ["INT_ADD", "register:40f0:8", ["const:b7cd18:8", "const:4:8"]]
+ 00b7cd18 ["CALL", null, ["callee:00bd6e60:8"]]
- 00b7ccd4 bytes 53680194
+ 00b7cd18 bytes 52680194
- 00b7ccf8 ["INT_ADD", "register:40f0:8", ["const:b7ccf8:8", "const:4:8"]]
- 00b7ccf8 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7cd3c ["INT_ADD", "register:40f0:8", ["const:b7cd3c:8", "const:4:8"]]
+ 00b7cd3c ["CALL", null, ["callee:004377fc:8"]]
- 00b7ccf8 bytes c1eae297
+ 00b7cd3c bytes b0eae297
~~~


<a id="compare-b6638086dc2d047b401ee6e1052d67ca"></a>

### [`00b7cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd10.md) → [`00b7cd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cd54.md) _ZNSt6__ndk16futureIvED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb640.md) · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00bdb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb690.md) · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd10.md#insn-00b7cd30)
- 新版 [`00b7cd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cd54.md#insn-00b7cd74)

~~~diff
- 00b7cd30 ["INT_ADD", "register:40f0:8", ["const:b7cd30:8", "const:4:8"]]
- 00b7cd30 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b7cd74 ["INT_ADD", "register:40f0:8", ["const:b7cd74:8", "const:4:8"]]
+ 00b7cd74 ["CALL", null, ["callee:00bd6e90:8"]]
- 00b7cd30 bytes 48680194
+ 00b7cd74 bytes 47680194
~~~


<a id="compare-d3ed67ac25a883728f6481598d537ca3"></a>

### [`00b7cd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd64.md) → [`00b7cda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cda8.md) _ZNSt6__ndk16futureIvE3getEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be1210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be1260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd64.md#insn-00b7cd80) · [`00b7cd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd64.md#insn-00b7cd8c)
- 新版 [`00b7cdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cda8.md#insn-00b7cdc4) · [`00b7cdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cda8.md#insn-00b7cdd0)

~~~diff
- 00b7cd80 ["INT_ADD", "register:40f0:8", ["const:b7cd80:8", "const:4:8"]]
- 00b7cd80 ["CALL", null, ["callee:00be1260:8"]]
+ 00b7cdc4 ["INT_ADD", "register:40f0:8", ["const:b7cdc4:8", "const:4:8"]]
+ 00b7cdc4 ["CALL", null, ["callee:00be1260:8"]]
- 00b7cd80 bytes 24910194
+ 00b7cdc4 bytes 27910194
- 00b7cd8c ["INT_ADD", "register:40f0:8", ["const:b7cd8c:8", "const:4:8"]]
- 00b7cd8c ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b7cdd0 ["INT_ADD", "register:40f0:8", ["const:b7cdd0:8", "const:4:8"]]
+ 00b7cdd0 ["CALL", null, ["callee:00bd6e90:8"]]
- 00b7cd8c bytes 31680194
+ 00b7cdd0 bytes 30680194
~~~


<a id="compare-802947c8a2ed71a87b0b6acb900fa12f"></a>

### [`00b7cfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cfd8.md) → [`00b7d01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d01c.md) _ZNSt6__ndk17promiseIvE10get_futureEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb680.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cfd8.md#insn-00b7cffc)
- 新版 [`00b7d040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d01c.md#insn-00b7d040)

~~~diff
- 00b7cffc ["INT_ADD", "register:40f0:8", ["const:b7cffc:8", "const:4:8"]]
- 00b7cffc ["CALL", null, ["callee:004377fc:8"]]
+ 00b7d040 ["INT_ADD", "register:40f0:8", ["const:b7d040:8", "const:4:8"]]
+ 00b7d040 ["CALL", null, ["callee:004377fc:8"]]
- 00b7cffc bytes 00eae297
+ 00b7d040 bytes efe9e297
~~~


<a id="compare-5b8cfe0729536b6b0ccb9dfa9fa9ca5f"></a>

### [`00b7d000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d000.md) → [`00b7d044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d044.md) _ZNSt6__ndk17promiseIvE9set_valueEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d000.md#insn-00b7d020)
- 新版 [`00b7d064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d044.md#insn-00b7d064)

~~~diff
- 00b7d020 ["INT_ADD", "register:40f0:8", ["const:b7d020:8", "const:4:8"]]
- 00b7d020 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7d064 ["INT_ADD", "register:40f0:8", ["const:b7d064:8", "const:4:8"]]
+ 00b7d064 ["CALL", null, ["callee:004377fc:8"]]
- 00b7d020 bytes f7e9e297
+ 00b7d064 bytes e6e9e297
~~~


<a id="compare-cd6a7140c12d4c88fc82a621720f9785"></a>

### [`00b7d024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d024.md) → [`00b7d068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md) _ZNSt6__ndk17promiseIvE13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4c0.md) [`00bdb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb610.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb510.md) [`00bdb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d024.md#insn-00b7d040) · [`00b7d04c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d024.md#insn-00b7d04c) · [`00b7d054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d024.md#insn-00b7d054)
- 新版 [`00b7d084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md#insn-00b7d084) · [`00b7d090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md#insn-00b7d090) · [`00b7d098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md#insn-00b7d098)

~~~diff
- 00b7d040 ["INT_ADD", "register:40f0:8", ["const:b7d040:8", "const:4:8"]]
- 00b7d040 ["CALL", null, ["callee:00bdb660:8"]]
+ 00b7d084 ["INT_ADD", "register:40f0:8", ["const:b7d084:8", "const:4:8"]]
+ 00b7d084 ["CALL", null, ["callee:00bdb660:8"]]
- 00b7d040 bytes 74790194
+ 00b7d084 bytes 77790194
- 00b7d04c ["INT_ADD", "register:40f0:8", ["const:b7d04c:8", "const:4:8"]]
- 00b7d04c ["CALL", null, ["callee:00bdb510:8"]]
+ 00b7d090 ["INT_ADD", "register:40f0:8", ["const:b7d090:8", "const:4:8"]]
+ 00b7d090 ["CALL", null, ["callee:00bdb510:8"]]
- 00b7d04c bytes 1d790194
+ 00b7d090 bytes 20790194
- 00b7d054 ["INT_ADD", "register:40f0:8", ["const:b7d054:8", "const:4:8"]]
- 00b7d054 ["CALL", null, ["callee:00bdb4a0:8"]]
+ 00b7d098 ["INT_ADD", "register:40f0:8", ["const:b7d098:8", "const:4:8"]]
+ 00b7d098 ["CALL", null, ["callee:00bdb4a0:8"]]
- 00b7d054 bytes ff780194
+ 00b7d098 bytes 02790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc49e56059391255482621c9a98bb614"></a>

### [`00b7d084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d084.md) → [`00b7d0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0c8.md) _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00be11d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00be1220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d084.md#insn-00b7d0a4)
- 新版 [`00b7d0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0c8.md#insn-00b7d0e8)

~~~diff
- 00b7d0a4 ["INT_ADD", "register:40f0:8", ["const:b7d0a4:8", "const:4:8"]]
- 00b7d0a4 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7d0e8 ["INT_ADD", "register:40f0:8", ["const:b7d0e8:8", "const:4:8"]]
+ 00b7d0e8 ["CALL", null, ["callee:004377fc:8"]]
- 00b7d0a4 bytes d6e9e297
+ 00b7d0e8 bytes c5e9e297
~~~


<a id="compare-b61ce0c2c9a02f1bb6eff5c23cc8e65d"></a>

### [`00b7d0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md) → [`00b7d0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md) _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb610.md) [`00be11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md) [`00be1240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md#insn-00b7d0c4) · [`00b7d0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md#insn-00b7d0d0) · [`00b7d0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md#insn-00b7d0d8)
- 新版 [`00b7d108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md#insn-00b7d108) · [`00b7d114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md#insn-00b7d114) · [`00b7d11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md#insn-00b7d11c)

~~~diff
- 00b7d0c4 ["INT_ADD", "register:40f0:8", ["const:b7d0c4:8", "const:4:8"]]
- 00b7d0c4 ["CALL", null, ["callee:00bdb660:8"]]
+ 00b7d108 ["INT_ADD", "register:40f0:8", ["const:b7d108:8", "const:4:8"]]
+ 00b7d108 ["CALL", null, ["callee:00bdb660:8"]]
- 00b7d0c4 bytes 53790194
+ 00b7d108 bytes 56790194
- 00b7d0d0 ["INT_ADD", "register:40f0:8", ["const:b7d0d0:8", "const:4:8"]]
- 00b7d0d0 ["CALL", null, ["callee:00be1240:8"]]
+ 00b7d114 ["INT_ADD", "register:40f0:8", ["const:b7d114:8", "const:4:8"]]
+ 00b7d114 ["CALL", null, ["callee:00be1240:8"]]
- 00b7d0d0 bytes 48900194
+ 00b7d114 bytes 4b900194
- 00b7d0d8 ["INT_ADD", "register:40f0:8", ["const:b7d0d8:8", "const:4:8"]]
- 00b7d0d8 ["CALL", null, ["callee:00bdb4a0:8"]]
+ 00b7d11c ["INT_ADD", "register:40f0:8", ["const:b7d11c:8", "const:4:8"]]
+ 00b7d11c ["CALL", null, ["callee:00bdb4a0:8"]]
- 00b7d0d8 bytes de780194
+ 00b7d11c bytes e1780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45f46bb22caaef7d019406dfa479d99a"></a>

### [`00b7d108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d108.md) → [`00b7d14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d14c.md) _ZNSt6__ndk113shared_futureIvED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d108.md#insn-00b7d128)
- 新版 [`00b7d16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d14c.md#insn-00b7d16c)

~~~diff
- 00b7d128 ["INT_ADD", "register:40f0:8", ["const:b7d128:8", "const:4:8"]]
- 00b7d128 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b7d16c ["INT_ADD", "register:40f0:8", ["const:b7d16c:8", "const:4:8"]]
+ 00b7d16c ["CALL", null, ["callee:00bd6e90:8"]]
- 00b7d128 bytes 4a670194
+ 00b7d16c bytes 49670194
~~~


<a id="compare-d951f3a6bfd90b32cca355af66b91352"></a>

### [`00b7d15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d15c.md) → [`00b7d1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md) _ZNSt6__ndk113shared_futureIvEaSERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d15c.md#insn-00b7d188) · [`00b7d19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d15c.md#insn-00b7d19c) · [`00b7d1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d15c.md#insn-00b7d1b0)
- 新版 [`00b7d1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md#insn-00b7d1cc) · [`00b7d1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md#insn-00b7d1e0) · [`00b7d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d1a0.md#insn-00b7d1f4)

~~~diff
- 00b7d188 ["INT_ADD", "register:40f0:8", ["const:b7d188:8", "const:4:8"]]
- 00b7d188 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00b7d1cc ["INT_ADD", "register:40f0:8", ["const:b7d1cc:8", "const:4:8"]]
+ 00b7d1cc ["CALL", null, ["callee:00bd6e60:8"]]
- 00b7d188 bytes 26670194
+ 00b7d1cc bytes 25670194
- 00b7d19c ["INT_ADD", "register:40f0:8", ["const:b7d19c:8", "const:4:8"]]
- 00b7d19c ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b7d1e0 ["INT_ADD", "register:40f0:8", ["const:b7d1e0:8", "const:4:8"]]
+ 00b7d1e0 ["CALL", null, ["callee:00bd6e90:8"]]
- 00b7d19c bytes 2d670194
+ 00b7d1e0 bytes 2c670194
- 00b7d1b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7d1b0 ["INT_ADD", "register:40f0:8", ["const:b7d1b0:8", "const:4:8"]]
- 00b7d1b0 ["CALLIND", null, ["register:0:8"]]
+ 00b7d1f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7d1f4 ["INT_ADD", "register:40f0:8", ["const:b7d1f4:8", "const:4:8"]]
+ 00b7d1f4 ["CALLIND", null, ["register:0:8"]]
- 00b7d1b0 bytes 00013fd6
+ 00b7d1f4 bytes 00013fd6
~~~


<a id="compare-df2506427d4564c7352516047371f5f7"></a>

### [`00b7d230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d230.md) → [`00b7d274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d274.md) FUN_00b7d274

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d230.md#insn-00b7d244)
- 新版 [`00b7d288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d274.md#insn-00b7d288)

~~~diff
- 00b7d244 ["INT_ADD", "register:40f0:8", ["const:b7d244:8", "const:4:8"]]
- 00b7d244 ["CALL", null, ["callee:00be0ef0:8"]]
+ 00b7d288 ["INT_ADD", "register:40f0:8", ["const:b7d288:8", "const:4:8"]]
+ 00b7d288 ["CALL", null, ["callee:00be0ef0:8"]]
- 00b7d244 bytes 178f0194
+ 00b7d288 bytes 1a8f0194
~~~


<a id="compare-3014be40a95046a0e691288d613a6eef"></a>

### [`00b7d25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md) → [`00b7d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md) _ZNSt6__ndk15mutexD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00418338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md) [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00468c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00468/00468c18.md) [`0056c7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7d8.md) · 呼出先 1件 [`00bde7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7c0.md)
- 新版 呼出元 6件 [`00418338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00468c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/00468c18.md) [`0056c7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7d8.md) · 呼出先 1件 [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md#insn-00b7d268)
- 新版 [`00b7d2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md#insn-00b7d2ac)

~~~diff
- 00b7d268 ["INT_ADD", "register:40f0:8", ["const:b7d268:8", "const:4:8"]]
- 00b7d268 ["CALL", null, ["callee:00bde810:8"]]
+ 00b7d2ac ["INT_ADD", "register:40f0:8", ["const:b7d2ac:8", "const:4:8"]]
+ 00b7d2ac ["CALL", null, ["callee:00bde810:8"]]
- 00b7d268 bytes 56850194
+ 00b7d2ac bytes 59850194
~~~


<a id="compare-293eabdea13fd06e0628a6fe7f70a125"></a>

### [`00b7d2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2a8.md) → [`00b7d2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2ec.md) _ZNSt6__ndk15mutex8try_lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2a8.md#insn-00b7d2b4)
- 新版 [`00b7d2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2ec.md#insn-00b7d2f8)

~~~diff
- 00b7d2b4 ["INT_ADD", "register:40f0:8", ["const:b7d2b4:8", "const:4:8"]]
- 00b7d2b4 ["CALL", null, ["callee:00be1270:8"]]
+ 00b7d2f8 ["INT_ADD", "register:40f0:8", ["const:b7d2f8:8", "const:4:8"]]
+ 00b7d2f8 ["CALL", null, ["callee:00be1270:8"]]
- 00b7d2b4 bytes db8f0194
+ 00b7d2f8 bytes de8f0194
~~~


<a id="compare-07d76eda79368428e3a126608b4afa72"></a>

### [`00b7d2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2d0.md) → [`00b7d314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d314.md) _ZNSt6__ndk15mutex6unlockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 1件 [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) · 呼出先 1件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2d0.md#insn-00b7d2dc)
- 新版 [`00b7d320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d314.md#insn-00b7d320)

~~~diff
- 00b7d2dc ["INT_ADD", "register:40f0:8", ["const:b7d2dc:8", "const:4:8"]]
- 00b7d2dc ["CALL", null, ["callee:00bde830:8"]]
+ 00b7d320 ["INT_ADD", "register:40f0:8", ["const:b7d320:8", "const:4:8"]]
+ 00b7d320 ["CALL", null, ["callee:00bde830:8"]]
- 00b7d2dc bytes 41850194
+ 00b7d320 bytes 44850194
~~~


<a id="compare-8e49873328efa65fbe6449ce84c7c86e"></a>

### [`00b7d394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d394.md) → [`00b7d3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3d8.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd230.md) · 呼出先 1件 [`00bde7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7c0.md)
- 新版 呼出元 1件 [`00bdd280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd280.md) · 呼出先 1件 [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d394.md#insn-00b7d3a0)
- 新版 [`00b7d3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3d8.md#insn-00b7d3e4)

~~~diff
- 00b7d3a0 ["INT_ADD", "register:40f0:8", ["const:b7d3a0:8", "const:4:8"]]
- 00b7d3a0 ["CALL", null, ["callee:00bde810:8"]]
+ 00b7d3e4 ["INT_ADD", "register:40f0:8", ["const:b7d3e4:8", "const:4:8"]]
+ 00b7d3e4 ["CALL", null, ["callee:00bde810:8"]]
- 00b7d3a0 bytes 08850194
+ 00b7d3e4 bytes 0b850194
~~~


<a id="compare-10b6b2970c7cce3ec95b9bf9341897a9"></a>

### [`00b7d3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3e0.md) → [`00b7d424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d424.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd250.md) · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 1件 [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md) · 呼出先 1件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3e0.md#insn-00b7d3ec)
- 新版 [`00b7d430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d424.md#insn-00b7d430)

~~~diff
- 00b7d3ec ["INT_ADD", "register:40f0:8", ["const:b7d3ec:8", "const:4:8"]]
- 00b7d3ec ["CALL", null, ["callee:00bde830:8"]]
+ 00b7d430 ["INT_ADD", "register:40f0:8", ["const:b7d430:8", "const:4:8"]]
+ 00b7d430 ["CALL", null, ["callee:00bde830:8"]]
- 00b7d3ec bytes fd840194
+ 00b7d430 bytes 00850194
~~~


<a id="compare-6660730fa5c1b446b2e76549b05e5b5e"></a>

### [`00b7d400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d400.md) → [`00b7d444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d444.md) _ZNSt6__ndk115recursive_mutex8try_lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d400.md#insn-00b7d40c)
- 新版 [`00b7d450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d444.md#insn-00b7d450)

~~~diff
- 00b7d40c ["INT_ADD", "register:40f0:8", ["const:b7d40c:8", "const:4:8"]]
- 00b7d40c ["CALL", null, ["callee:00be1270:8"]]
+ 00b7d450 ["INT_ADD", "register:40f0:8", ["const:b7d450:8", "const:4:8"]]
+ 00b7d450 ["CALL", null, ["callee:00be1270:8"]]
- 00b7d40c bytes 858f0194
+ 00b7d450 bytes 888f0194
~~~


<a id="compare-8a8e7b453386600c36e9defd045ce8d3"></a>

### [`00b7d528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d528.md) → [`00b7d56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d56c.md) _ZNSt6__ndk111timed_mutex8try_lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d528.md#insn-00b7d53c) · [`00b7d568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d528.md#insn-00b7d568)
- 新版 [`00b7d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d56c.md#insn-00b7d580) · [`00b7d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d56c.md#insn-00b7d5ac)

~~~diff
- 00b7d53c ["INT_ADD", "register:40f0:8", ["const:b7d53c:8", "const:4:8"]]
- 00b7d53c ["CALL", null, ["callee:00be1270:8"]]
+ 00b7d580 ["INT_ADD", "register:40f0:8", ["const:b7d580:8", "const:4:8"]]
+ 00b7d580 ["CALL", null, ["callee:00be1270:8"]]
- 00b7d53c bytes 398f0194
+ 00b7d580 bytes 3c8f0194
- 00b7d568 ["INT_ADD", "register:40f0:8", ["const:b7d568:8", "const:4:8"]]
- 00b7d568 ["CALL", null, ["callee:00bde830:8"]]
+ 00b7d5ac ["INT_ADD", "register:40f0:8", ["const:b7d5ac:8", "const:4:8"]]
+ 00b7d5ac ["CALL", null, ["callee:00bde830:8"]]
- 00b7d568 bytes 9e840194
+ 00b7d5ac bytes a1840194
~~~


<a id="compare-f05884e779155f5e68fba5bd82923f96"></a>

### [`00b7d72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d72c.md) → [`00b7d770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md) _ZNSt6__ndk121recursive_timed_mutex8try_lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be1270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d72c.md#insn-00b7d744) · [`00b7d750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d72c.md#insn-00b7d750) · [`00b7d790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d72c.md#insn-00b7d790)
- 新版 [`00b7d788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md#insn-00b7d788) · [`00b7d794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md#insn-00b7d794) · [`00b7d7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d770.md#insn-00b7d7d4)

~~~diff
- 00b7d744 ["INT_ADD", "register:40f0:8", ["const:b7d744:8", "const:4:8"]]
- 00b7d744 ["CALL", null, ["callee:00bdb7d0:8"]]
+ 00b7d788 ["INT_ADD", "register:40f0:8", ["const:b7d788:8", "const:4:8"]]
+ 00b7d788 ["CALL", null, ["callee:00bdb7d0:8"]]
- 00b7d744 bytes 0f780194
+ 00b7d788 bytes 12780194
- 00b7d750 ["INT_ADD", "register:40f0:8", ["const:b7d750:8", "const:4:8"]]
- 00b7d750 ["CALL", null, ["callee:00be1270:8"]]
+ 00b7d794 ["INT_ADD", "register:40f0:8", ["const:b7d794:8", "const:4:8"]]
+ 00b7d794 ["CALL", null, ["callee:00be1270:8"]]
- 00b7d750 bytes b48e0194
+ 00b7d794 bytes b78e0194
- 00b7d790 ["INT_ADD", "register:40f0:8", ["const:b7d790:8", "const:4:8"]]
- 00b7d790 ["CALL", null, ["callee:00bde830:8"]]
+ 00b7d7d4 ["INT_ADD", "register:40f0:8", ["const:b7d7d4:8", "const:4:8"]]
+ 00b7d7d4 ["CALL", null, ["callee:00bde830:8"]]
- 00b7d790 bytes 14840194
+ 00b7d7d4 bytes 17840194
~~~


<a id="compare-56ddb6cb8a691886445a888c7ca2e5d8"></a>

### [`00b7d830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d830.md) → [`00b7d874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d874.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2e0.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00bdb330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb330.md) · 呼出先 1件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d830.md#insn-00b7d84c)
- 新版 [`00b7d890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d874.md#insn-00b7d890)

~~~diff
- 00b7d84c ["INT_ADD", "register:40f0:8", ["const:b7d84c:8", "const:4:8"]]
- 00b7d84c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00b7d890 ["INT_ADD", "register:40f0:8", ["const:b7d890:8", "const:4:8"]]
+ 00b7d890 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00b7d84c bytes 4d760194
+ 00b7d890 bytes 50760194
~~~


<a id="compare-666d9b56a9068e75af02fa9d3ca57056"></a>

### [`00b7d8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d8e4.md) → [`00b7d928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d928.md) _ZNSt6__ndk16thread20hardware_concurrencyEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d8e4.md#insn-00b7d8f4)
- 新版 [`00b7d938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d928.md#insn-00b7d938)

~~~diff
- 00b7d8f4 ["INT_ADD", "register:40f0:8", ["const:b7d8f4:8", "const:4:8"]]
- 00b7d8f4 ["CALL", null, ["callee:00be1290:8"]]
+ 00b7d938 ["INT_ADD", "register:40f0:8", ["const:b7d938:8", "const:4:8"]]
+ 00b7d938 ["CALL", null, ["callee:00be1290:8"]]
- 00b7d8f4 bytes 538e0194
+ 00b7d938 bytes 568e0194
~~~


<a id="compare-874cc90d358a187c9fa491d01ea3220f"></a>

### [`00b7d910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d910.md) → [`00b7d954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d954.md) _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5f0.md) · 呼出先 2件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1250.md)
- 新版 呼出元 1件 [`00bdb640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb640.md) · 呼出先 2件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be12a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d910.md#insn-00b7d964) · [`00b7d970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d910.md#insn-00b7d970)
- 新版 [`00b7d9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d954.md#insn-00b7d9a8) · [`00b7d9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d954.md#insn-00b7d9b4)

~~~diff
- 00b7d964 ["INT_ADD", "register:40f0:8", ["const:b7d964:8", "const:4:8"]]
- 00b7d964 ["CALL", null, ["callee:00be12a0:8"]]
+ 00b7d9a8 ["INT_ADD", "register:40f0:8", ["const:b7d9a8:8", "const:4:8"]]
+ 00b7d9a8 ["CALL", null, ["callee:00be12a0:8"]]
- 00b7d964 bytes 3b8e0194
+ 00b7d9a8 bytes 3e8e0194
- 00b7d970 ["INT_ADD", "register:40f0:8", ["const:b7d970:8", "const:4:8"]]
- 00b7d970 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b7d9b4 ["INT_ADD", "register:40f0:8", ["const:b7d9b4:8", "const:4:8"]]
+ 00b7d9b4 ["CALL", null, ["callee:00bdb270:8"]]
- 00b7d970 bytes 2c760194
+ 00b7d9b4 bytes 2f760194
~~~


<a id="compare-51ce4fb84fb352c01f331b5f5500752c"></a>

### [`00b7da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da48.md) → [`00b7da8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md) FUN_00b7da8c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7dd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd3c.md) · 呼出先 5件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md) [`00be1200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1200.md)
- 新版 呼出元 1件 [`00b7dd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd80.md) · 呼出先 5件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) [`00be1250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7da70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da48.md#insn-00b7da70) · [`00b7da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da48.md#insn-00b7da78) · [`00b7daa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da48.md#insn-00b7daa0)
- 新版 [`00b7dab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md#insn-00b7dab4) · [`00b7dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md#insn-00b7dabc) · [`00b7dae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md#insn-00b7dae4)

~~~diff
- 00b7da70 ["INT_ADD", "register:40f0:8", ["const:b7da70:8", "const:4:8"]]
- 00b7da70 ["CALL", null, ["callee:00bdb530:8"]]
+ 00b7dab4 ["INT_ADD", "register:40f0:8", ["const:b7dab4:8", "const:4:8"]]
+ 00b7dab4 ["CALL", null, ["callee:00bdb530:8"]]
- 00b7da70 bytes 9c760194
+ 00b7dab4 bytes 9f760194
- 00b7da78 ["INT_ADD", "register:40f0:8", ["const:b7da78:8", "const:4:8"]]
- 00b7da78 ["CALL", null, ["callee:00bdb2a0:8"]]
+ 00b7dabc ["INT_ADD", "register:40f0:8", ["const:b7dabc:8", "const:4:8"]]
+ 00b7dabc ["CALL", null, ["callee:00bdb2a0:8"]]
- 00b7da78 bytes f6750194
+ 00b7dabc bytes f9750194
- 00b7daa0 ["INT_ADD", "register:40f0:8", ["const:b7daa0:8", "const:4:8"]]
- 00b7daa0 ["CALL", null, ["callee:00be1250:8"]]
+ 00b7dae4 ["INT_ADD", "register:40f0:8", ["const:b7dae4:8", "const:4:8"]]
+ 00b7dae4 ["CALL", null, ["callee:00be1250:8"]]
- 00b7daa0 bytes d88d0194
+ 00b7dae4 bytes db8d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886218810e92d34bd061b174fd3747b7"></a>

### [`00b7db14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7db14.md) → [`00b7db58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md) FUN_00b7db58

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7dd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd80.md) · 呼出先 4件 [`00b7dd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd98.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00b7ddc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddc4.md) · 呼出先 4件 [`00b7dddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7db90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7db14.md#insn-00b7db90) · [`00b7dbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7db14.md#insn-00b7dbd4) · [`00b7dbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7db14.md#insn-00b7dbe8)
- 新版 [`00b7dbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md#insn-00b7dbd4) · [`00b7dc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md#insn-00b7dc18) · [`00b7dc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md#insn-00b7dc2c)

~~~diff
- 00b7db90 ["INT_ADD", "register:40f0:8", ["const:b7db90:8", "const:4:8"]]
- 00b7db90 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7dbd4 ["INT_ADD", "register:40f0:8", ["const:b7dbd4:8", "const:4:8"]]
+ 00b7dbd4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7db90 bytes 18750194
+ 00b7dbd4 bytes 1b750194
- 00b7dbd4 ["INT_ADD", "register:40f0:8", ["const:b7dbd4:8", "const:4:8"]]
- 00b7dbd4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b7dc18 ["INT_ADD", "register:40f0:8", ["const:b7dc18:8", "const:4:8"]]
+ 00b7dc18 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b7dbd4 bytes 63750194
+ 00b7dc18 bytes 66750194
- 00b7dbe8 ["INT_ADD", "register:40f0:8", ["const:b7dbe8:8", "const:4:8"]]
- 00b7dbe8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b7dc2c ["INT_ADD", "register:40f0:8", ["const:b7dc2c:8", "const:4:8"]]
+ 00b7dc2c ["CALL", null, ["callee:00bdb060:8"]]
- 00b7dbe8 bytes 0a750194
+ 00b7dc2c bytes 0d750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7af22946c281a8634dd5dbd6de473b88"></a>

### [`00b7dc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dc10.md) → [`00b7dc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md) FUN_00b7dc54

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7dd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd8c.md) · 呼出先 5件 [`00b7ddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddb0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00b7ddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddd0.md) · 呼出先 5件 [`00b7ddf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dc84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dc10.md#insn-00b7dc84) · [`00b7dcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dc10.md#insn-00b7dcb8) · [`00b7dccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dc10.md#insn-00b7dccc)
- 新版 [`00b7dcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md#insn-00b7dcc8) · [`00b7dcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md#insn-00b7dcfc) · [`00b7dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md#insn-00b7dd10)

~~~diff
- 00b7dc84 ["INT_ADD", "register:40f0:8", ["const:b7dc84:8", "const:4:8"]]
- 00b7dc84 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7dcc8 ["INT_ADD", "register:40f0:8", ["const:b7dcc8:8", "const:4:8"]]
+ 00b7dcc8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7dc84 bytes db740194
+ 00b7dcc8 bytes de740194
- 00b7dcb8 ["INT_ADD", "register:40f0:8", ["const:b7dcb8:8", "const:4:8"]]
- 00b7dcb8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b7dcfc ["INT_ADD", "register:40f0:8", ["const:b7dcfc:8", "const:4:8"]]
+ 00b7dcfc ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b7dcb8 bytes 2a750194
+ 00b7dcfc bytes 2d750194
- 00b7dccc ["INT_ADD", "register:40f0:8", ["const:b7dccc:8", "const:4:8"]]
- 00b7dccc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b7dd10 ["INT_ADD", "register:40f0:8", ["const:b7dd10:8", "const:4:8"]]
+ 00b7dd10 ["CALL", null, ["callee:00bdb060:8"]]
- 00b7dccc bytes d1740194
+ 00b7dd10 bytes d4740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ebffa0a048783096858a06d378a7d9"></a>

### [`00b7dd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd00.md) → [`00b7dd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd44.md) _ZNSt6__ndk115__thread_structC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd00.md#insn-00b7dd18)
- 新版 [`00b7dd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd44.md#insn-00b7dd5c)

~~~diff
- 00b7dd18 ["INT_ADD", "register:40f0:8", ["const:b7dd18:8", "const:4:8"]]
- 00b7dd18 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7dd5c ["INT_ADD", "register:40f0:8", ["const:b7dd5c:8", "const:4:8"]]
+ 00b7dd5c ["CALL", null, ["callee:00bdb040:8"]]
- 00b7dd18 bytes b6740194
+ 00b7dd5c bytes b9740194
~~~


<a id="compare-fb59b0c045422050114191676598edf6"></a>

### [`00b7dd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd3c.md) → [`00b7dd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd80.md) _ZNSt6__ndk115__thread_structD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2b0.md) · 呼出先 2件 [`00b7da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da48.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdb300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb300.md) · 呼出先 2件 [`00b7da8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd3c.md#insn-00b7dd58)
- 新版 [`00b7dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd80.md#insn-00b7dd9c)

~~~diff
- 00b7dd58 ["INT_ADD", "register:40f0:8", ["const:b7dd58:8", "const:4:8"]]
- 00b7dd58 ["CALL", null, ["callee:00b7da8c:8"]]
+ 00b7dd9c ["INT_ADD", "register:40f0:8", ["const:b7dd9c:8", "const:4:8"]]
+ 00b7dd9c ["CALL", null, ["callee:00b7da8c:8"]]
- 00b7dd58 bytes 3cffff97
+ 00b7dd9c bytes 3cffff97
~~~


<a id="compare-4913d37fdb7baa3bed87028e4c246752"></a>

### [`00b7ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddc8.md) → [`00b7de0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de0c.md) FUN_00b7de0c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7da14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2b0.md)
- 新版 呼出元 1件 [`00b7da58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddc8.md#insn-00b7dde4)
- 新版 [`00b7de28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de0c.md#insn-00b7de28)

~~~diff
- 00b7dde4 ["INT_ADD", "register:40f0:8", ["const:b7dde4:8", "const:4:8"]]
- 00b7dde4 ["CALL", null, ["callee:00bdb300:8"]]
+ 00b7de28 ["INT_ADD", "register:40f0:8", ["const:b7de28:8", "const:4:8"]]
+ 00b7de28 ["CALL", null, ["callee:00bdb300:8"]]
- 00b7dde4 bytes 33750194
+ 00b7de28 bytes 36750194
~~~


<a id="compare-9b65419ea7ba21df055070d787691e4e"></a>

### [`00b7dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dea4.md) → [`00b7dee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dee8.md) _ZNSt6__ndk113random_deviceD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0053d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md) [`00bdb530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb530.md) · 呼出先 1件 [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md)
- 新版 呼出元 2件 [`0053d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8b4.md) [`00bdb580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb580.md) · 呼出先 1件 [`00bdc980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7deb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dea4.md#insn-00b7deb4)
- 新版 [`00b7def8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dee8.md#insn-00b7def8)

~~~diff
- 00b7deb4 ["INT_ADD", "register:40f0:8", ["const:b7deb4:8", "const:4:8"]]
- 00b7deb4 ["CALL", null, ["callee:00bdc980:8"]]
+ 00b7def8 ["INT_ADD", "register:40f0:8", ["const:b7def8:8", "const:4:8"]]
+ 00b7def8 ["CALL", null, ["callee:00bdc980:8"]]
- 00b7deb4 bytes 9f7a0194
+ 00b7def8 bytes a27a0194
~~~


<a id="compare-7738109a3babbed0e19156f0d06610a1"></a>

### [`00b7df5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7df5c.md) → [`00b7dfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dfa0.md) _ZNKSt6__ndk113random_device7entropyEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1260.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7df7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7df5c.md#insn-00b7df7c)
- 新版 [`00b7dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dfa0.md#insn-00b7dfc0)

~~~diff
- 00b7df7c ["INT_ADD", "register:40f0:8", ["const:b7df7c:8", "const:4:8"]]
- 00b7df7c ["CALL", null, ["callee:00be12b0:8"]]
+ 00b7dfc0 ["INT_ADD", "register:40f0:8", ["const:b7dfc0:8", "const:4:8"]]
+ 00b7dfc0 ["CALL", null, ["callee:00be12b0:8"]]
- 00b7df7c bytes b98c0194
+ 00b7dfc0 bytes bc8c0194
~~~


<a id="compare-07f6026e8db7c5c5a3628a5e6aa0cea5"></a>

### [`00b7dfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dfc4.md) → [`00b7e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e008.md) FUN_00b7e008

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7b7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b7a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7dff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dfc4.md#insn-00b7dff4)
- 新版 [`00b7e038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e008.md#insn-00b7e038)

~~~diff
- 00b7dff4 ["INT_ADD", "register:40f0:8", ["const:b7dff4:8", "const:4:8"]]
- 00b7dff4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7e038 ["INT_ADD", "register:40f0:8", ["const:b7e038:8", "const:4:8"]]
+ 00b7e038 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7dff4 bytes ff730194
+ 00b7e038 bytes 02740194
~~~


<a id="compare-1c90a6f9107844c10cad866a869d8635"></a>

### [`00b7e110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e110.md) → [`00b7e154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e154.md) _ZNSt6__ndk18ios_base7failureD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be12c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e110.md#insn-00b7e124)
- 新版 [`00b7e168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e154.md#insn-00b7e168)

~~~diff
- 00b7e124 ["INT_ADD", "register:40f0:8", ["const:b7e124:8", "const:4:8"]]
- 00b7e124 ["CALL", null, ["callee:00be12c0:8"]]
+ 00b7e168 ["INT_ADD", "register:40f0:8", ["const:b7e168:8", "const:4:8"]]
+ 00b7e168 ["CALL", null, ["callee:00be12c0:8"]]
- 00b7e124 bytes 538c0194
+ 00b7e168 bytes 568c0194
~~~


<a id="compare-3c92e454f0a84ff669f587c1136d3ba0"></a>

### [`00b7e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e13c.md) → [`00b7e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e180.md) _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1280.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be12d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e17c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e13c.md#insn-00b7e17c)
- 新版 [`00b7e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e180.md#insn-00b7e1c0)

~~~diff
- 00b7e17c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7e17c ["INT_ADD", "register:40f0:8", ["const:b7e17c:8", "const:4:8"]]
- 00b7e17c ["CALLIND", null, ["register:0:8"]]
+ 00b7e1c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7e1c0 ["INT_ADD", "register:40f0:8", ["const:b7e1c0:8", "const:4:8"]]
+ 00b7e1c0 ["CALLIND", null, ["register:0:8"]]
- 00b7e17c bytes 00013fd6
+ 00b7e1c0 bytes 00013fd6
~~~


<a id="compare-50075fafd118f6ed149f39c261e61019"></a>

### [`00b7e1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e1a0.md) → [`00b7e1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md) _ZNSt6__ndk18ios_base5imbueERKNS_6localeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e1a0.md#insn-00b7e1c8) · [`00b7e1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e1a0.md#insn-00b7e1d4) · [`00b7e1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e1a0.md#insn-00b7e1f8)
- 新版 [`00b7e20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md#insn-00b7e20c) · [`00b7e218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md#insn-00b7e218) · [`00b7e23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md#insn-00b7e23c)

~~~diff
- 00b7e1c8 ["INT_ADD", "register:40f0:8", ["const:b7e1c8:8", "const:4:8"]]
- 00b7e1c8 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b7e20c ["INT_ADD", "register:40f0:8", ["const:b7e20c:8", "const:4:8"]]
+ 00b7e20c ["CALL", null, ["callee:00bdd980:8"]]
- 00b7e1c8 bytes da7d0194
+ 00b7e20c bytes dd7d0194
- 00b7e1d4 ["INT_ADD", "register:40f0:8", ["const:b7e1d4:8", "const:4:8"]]
- 00b7e1d4 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b7e218 ["INT_ADD", "register:40f0:8", ["const:b7e218:8", "const:4:8"]]
+ 00b7e218 ["CALL", null, ["callee:00be12e0:8"]]
- 00b7e1d4 bytes 2f8c0194
+ 00b7e218 bytes 328c0194
- 00b7e1f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7e1f8 ["INT_ADD", "register:40f0:8", ["const:b7e1f8:8", "const:4:8"]]
- 00b7e1f8 ["CALLIND", null, ["register:0:8"]]
+ 00b7e23c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7e23c ["INT_ADD", "register:40f0:8", ["const:b7e23c:8", "const:4:8"]]
+ 00b7e23c ["CALLIND", null, ["register:0:8"]]
- 00b7e1f8 bytes 00013fd6
+ 00b7e23c bytes 00013fd6
~~~


<a id="compare-acf6e744fe298c57aa5bf998558238da"></a>

### [`00b7e624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e624.md) → [`00b7e668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e668.md) _ZNSt6__ndk18ios_baseD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be12a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be12f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e624.md#insn-00b7e638)
- 新版 [`00b7e67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e668.md#insn-00b7e67c)

~~~diff
- 00b7e638 ["INT_ADD", "register:40f0:8", ["const:b7e638:8", "const:4:8"]]
- 00b7e638 ["CALL", null, ["callee:00be12f0:8"]]
+ 00b7e67c ["INT_ADD", "register:40f0:8", ["const:b7e67c:8", "const:4:8"]]
+ 00b7e67c ["CALL", null, ["callee:00be12f0:8"]]
- 00b7e638 bytes 1a8b0194
+ 00b7e67c bytes 1d8b0194
~~~


<a id="compare-56d8186e1cc396a645a5daafd7b3a913"></a>

### [`00b7e77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e77c.md) → [`00b7e7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md) _ZNSt6__ndk18ios_base7copyfmtERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be12c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12c0.md) · 呼出先 5件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 1件 [`00be1310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1310.md) · 呼出先 5件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e77c.md#insn-00b7e7b0) · [`00b7e7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e77c.md#insn-00b7e7c0) · [`00b7e7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e77c.md#insn-00b7e7ec)
- 新版 [`00b7e7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md#insn-00b7e7f4) · [`00b7e804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md#insn-00b7e804) · [`00b7e830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e7c0.md#insn-00b7e830)

~~~diff
- 00b7e7b0 ["INT_ADD", "register:40f0:8", ["const:b7e7b0:8", "const:4:8"]]
- 00b7e7b0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00b7e7f4 ["INT_ADD", "register:40f0:8", ["const:b7e7f4:8", "const:4:8"]]
+ 00b7e7f4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00b7e7b0 bytes 747a0194
+ 00b7e7f4 bytes 777a0194
- 00b7e7c0 ["INT_ADD", "register:40f0:8", ["const:b7e7c0:8", "const:4:8"]]
- 00b7e7c0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00b7e804 ["INT_ADD", "register:40f0:8", ["const:b7e804:8", "const:4:8"]]
+ 00b7e804 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00b7e7c0 bytes 707a0194
+ 00b7e804 bytes 737a0194
- 00b7e7ec ["INT_ADD", "register:40f0:8", ["const:b7e7ec:8", "const:4:8"]]
- 00b7e7ec ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00b7e830 ["INT_ADD", "register:40f0:8", ["const:b7e830:8", "const:4:8"]]
+ 00b7e830 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00b7e7ec bytes 657a0194
+ 00b7e830 bytes 687a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee5411dbe7d3d3a450c63044b5268e9b"></a>

### [`00b7ea3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ea3c.md) → [`00b7ea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ea80.md) _ZNSt6__ndk18ios_base4moveERS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ea78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ea3c.md#insn-00b7ea78)
- 新版 [`00b7eabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ea80.md#insn-00b7eabc)

~~~diff
- 00b7ea78 ["INT_ADD", "register:40f0:8", ["const:b7ea78:8", "const:4:8"]]
- 00b7ea78 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b7eabc ["INT_ADD", "register:40f0:8", ["const:b7eabc:8", "const:4:8"]]
+ 00b7eabc ["CALL", null, ["callee:00bdd980:8"]]
- 00b7ea78 bytes ae7b0194
+ 00b7eabc bytes b17b0194
~~~


<a id="compare-f0f24f50a909b6008f647ae4eb7ecbf5"></a>

### [`00b7ead8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ead8.md) → [`00b7eb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md) _ZNSt6__ndk18ios_base4swapERS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md) · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7eb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ead8.md#insn-00b7eb4c) · [`00b7eb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ead8.md#insn-00b7eb58) · [`00b7eb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ead8.md#insn-00b7eb64)
- 新版 [`00b7eb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md#insn-00b7eb90) · [`00b7eb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md#insn-00b7eb9c) · [`00b7eba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md#insn-00b7eba8)

~~~diff
- 00b7eb4c ["INT_ADD", "register:40f0:8", ["const:b7eb4c:8", "const:4:8"]]
- 00b7eb4c ["CALL", null, ["callee:00bdd980:8"]]
+ 00b7eb90 ["INT_ADD", "register:40f0:8", ["const:b7eb90:8", "const:4:8"]]
+ 00b7eb90 ["CALL", null, ["callee:00bdd980:8"]]
- 00b7eb4c bytes 797b0194
+ 00b7eb90 bytes 7c7b0194
- 00b7eb58 ["INT_ADD", "register:40f0:8", ["const:b7eb58:8", "const:4:8"]]
- 00b7eb58 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b7eb9c ["INT_ADD", "register:40f0:8", ["const:b7eb9c:8", "const:4:8"]]
+ 00b7eb9c ["CALL", null, ["callee:00be12e0:8"]]
- 00b7eb58 bytes ce890194
+ 00b7eb9c bytes d1890194
- 00b7eb64 ["INT_ADD", "register:40f0:8", ["const:b7eb64:8", "const:4:8"]]
- 00b7eb64 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b7eba8 ["INT_ADD", "register:40f0:8", ["const:b7eba8:8", "const:4:8"]]
+ 00b7eba8 ["CALL", null, ["callee:00be12e0:8"]]
- 00b7eb64 bytes cb890194
+ 00b7eba8 bytes ce890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dfd0ed4742aa1d8971bedb47d5af959"></a>

### [`00b7ebf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ebf4.md) → [`00b7ec38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec38.md) _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb420.md) · 呼出先 1件 [`00bdb660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb660.md)
- 新版 呼出元 1件 [`00bdb470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb470.md) · 呼出先 1件 [`00bdb6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ec1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ebf4.md#insn-00b7ec1c)
- 新版 [`00b7ec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec38.md#insn-00b7ec60)

~~~diff
- 00b7ec1c ["INT_ADD", "register:40f0:8", ["const:b7ec1c:8", "const:4:8"]]
- 00b7ec1c ["CALL", null, ["callee:00bdb6b0:8"]]
+ 00b7ec60 ["INT_ADD", "register:40f0:8", ["const:b7ec60:8", "const:4:8"]]
+ 00b7ec60 ["CALL", null, ["callee:00bdb6b0:8"]]
- 00b7ec1c bytes 91720194
+ 00b7ec60 bytes 94720194
~~~


<a id="compare-30364c2606f30f0530132669992fef13"></a>

### [`00b7ec20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec20.md) → [`00b7ec64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec64.md) _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be12e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12e0.md) · 呼出先 1件 [`00bdb660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb660.md)
- 新版 呼出元 1件 [`00be1330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1330.md) · 呼出先 1件 [`00bdb6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ec48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec20.md#insn-00b7ec48)
- 新版 [`00b7ec8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec64.md#insn-00b7ec8c)

~~~diff
- 00b7ec48 ["INT_ADD", "register:40f0:8", ["const:b7ec48:8", "const:4:8"]]
- 00b7ec48 ["CALL", null, ["callee:00bdb6b0:8"]]
+ 00b7ec8c ["INT_ADD", "register:40f0:8", ["const:b7ec8c:8", "const:4:8"]]
+ 00b7ec8c ["CALL", null, ["callee:00bdb6b0:8"]]
- 00b7ec48 bytes 86720194
+ 00b7ec8c bytes 89720194
~~~


<a id="compare-c1f1ddb23840276139be4600992804e2"></a>

### [`00b7ec68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec68.md) → [`00b7ecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ecac.md) FUN_00b7ecac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ec7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec68.md#insn-00b7ec7c)
- 新版 [`00b7ecc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ecac.md#insn-00b7ecc0)

~~~diff
- 00b7ec7c ["INT_ADD", "register:40f0:8", ["const:b7ec7c:8", "const:4:8"]]
- 00b7ec7c ["CALL", null, ["callee:00be0ef0:8"]]
+ 00b7ecc0 ["INT_ADD", "register:40f0:8", ["const:b7ecc0:8", "const:4:8"]]
+ 00b7ecc0 ["CALL", null, ["callee:00be0ef0:8"]]
- 00b7ec7c bytes 89880194
+ 00b7ecc0 bytes 8c880194
~~~


<a id="compare-a45c9b4834ebafff68042da0e844b156"></a>

### [`00b7ec9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec9c.md) → [`00b7ece0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ece0.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be12f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ecb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec9c.md#insn-00b7ecb0)
- 新版 [`00b7ecf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ece0.md#insn-00b7ecf4)

~~~diff
- 00b7ecb0 ["INT_ADD", "register:40f0:8", ["const:b7ecb0:8", "const:4:8"]]
- 00b7ecb0 ["CALL", null, ["callee:00be1340:8"]]
+ 00b7ecf4 ["INT_ADD", "register:40f0:8", ["const:b7ecf4:8", "const:4:8"]]
+ 00b7ecf4 ["CALL", null, ["callee:00be1340:8"]]
- 00b7ecb0 bytes 90890194
+ 00b7ecf4 bytes 93890194
~~~


<a id="compare-a7109ffec9eab6cfc070c23fcf48e5ca"></a>

### [`00b7ecc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ecc8.md) → [`00b7ed0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be1280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1280.md) [`00be12c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be12d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12d0.md) [`00be1310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ecf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ecc8.md#insn-00b7ecf0) · [`00b7ecfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ecc8.md#insn-00b7ecfc) · [`00b7ed18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ecc8.md#insn-00b7ed18)
- 新版 [`00b7ed34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md#insn-00b7ed34) · [`00b7ed40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md#insn-00b7ed40) · [`00b7ed5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ed0c.md#insn-00b7ed5c)

~~~diff
- 00b7ecf0 ["INT_ADD", "register:40f0:8", ["const:b7ecf0:8", "const:4:8"]]
- 00b7ecf0 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b7ed34 ["INT_ADD", "register:40f0:8", ["const:b7ed34:8", "const:4:8"]]
+ 00b7ed34 ["CALL", null, ["callee:00be12d0:8"]]
- 00b7ecf0 bytes 64890194
+ 00b7ed34 bytes 67890194
- 00b7ecfc ["INT_ADD", "register:40f0:8", ["const:b7ecfc:8", "const:4:8"]]
- 00b7ecfc ["CALL", null, ["callee:00be1310:8"]]
+ 00b7ed40 ["INT_ADD", "register:40f0:8", ["const:b7ed40:8", "const:4:8"]]
+ 00b7ed40 ["CALL", null, ["callee:00be1310:8"]]
- 00b7ecfc bytes 71890194
+ 00b7ed40 bytes 74890194
- 00b7ed18 ["INT_ADD", "register:40f0:8", ["const:b7ed18:8", "const:4:8"]]
- 00b7ed18 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b7ed5c ["INT_ADD", "register:40f0:8", ["const:b7ed5c:8", "const:4:8"]]
+ 00b7ed5c ["CALL", null, ["callee:00be12d0:8"]]
- 00b7ed18 bytes 5a890194
+ 00b7ed5c bytes 5d890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea2b9798fc8a91c4115efc8c65a29492"></a>

### [`00b7ed5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed5c.md) → [`00b7eda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eda0.md) FUN_00b7eda0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ed70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed5c.md#insn-00b7ed70)
- 新版 [`00b7edb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eda0.md#insn-00b7edb4)

~~~diff
- 00b7ed70 ["INT_ADD", "register:40f0:8", ["const:b7ed70:8", "const:4:8"]]
- 00b7ed70 ["CALL", null, ["callee:00be1350:8"]]
+ 00b7edb4 ["INT_ADD", "register:40f0:8", ["const:b7edb4:8", "const:4:8"]]
+ 00b7edb4 ["CALL", null, ["callee:00be1350:8"]]
- 00b7ed70 bytes 64890194
+ 00b7edb4 bytes 67890194
~~~


<a id="compare-159b6ced24ade15b38d0d423f3ad43e1"></a>

### [`00b7ed88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed88.md) → [`00b7edcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7edcc.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7edb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed88.md#insn-00b7edb0) · [`00b7edbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed88.md#insn-00b7edbc)
- 新版 [`00b7edf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7edcc.md#insn-00b7edf4) · [`00b7ee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7edcc.md#insn-00b7ee00)

~~~diff
- 00b7edb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7edb0 ["INT_ADD", "register:40f0:8", ["const:b7edb0:8", "const:4:8"]]
- 00b7edb0 ["CALLIND", null, ["register:0:8"]]
+ 00b7edf4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b7edf4 ["INT_ADD", "register:40f0:8", ["const:b7edf4:8", "const:4:8"]]
+ 00b7edf4 ["CALLIND", null, ["register:0:8"]]
- 00b7edb0 bytes 20013fd6
+ 00b7edf4 bytes 20013fd6
- 00b7edbc ["INT_ADD", "register:40f0:8", ["const:b7edbc:8", "const:4:8"]]
- 00b7edbc ["CALL", null, ["callee:00bdd980:8"]]
+ 00b7ee00 ["INT_ADD", "register:40f0:8", ["const:b7ee00:8", "const:4:8"]]
+ 00b7ee00 ["CALL", null, ["callee:00bdd980:8"]]
- 00b7edbc bytes dd7a0194
+ 00b7ee00 bytes e07a0194
~~~


<a id="compare-1c50e5bcda2c8154785f0c9a1a2ef153"></a>

### [`00b7ee50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ee50.md) → [`00b7ee94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ee94.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ee90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ee50.md#insn-00b7ee90)
- 新版 [`00b7eed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ee94.md#insn-00b7eed4)

~~~diff
- 00b7ee90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7ee90 ["INT_ADD", "register:40f0:8", ["const:b7ee90:8", "const:4:8"]]
- 00b7ee90 ["CALLIND", null, ["register:0:8"]]
+ 00b7eed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7eed4 ["INT_ADD", "register:40f0:8", ["const:b7eed4:8", "const:4:8"]]
+ 00b7eed4 ["CALLIND", null, ["register:0:8"]]
- 00b7ee90 bytes 00013fd6
+ 00b7eed4 bytes 00013fd6
~~~


<a id="compare-5ff188ad99a8e0573a87b2d180e744b7"></a>

### [`00b7f084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f084.md) → [`00b7f0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f0c8.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f084.md#insn-00b7f0a4)
- 新版 [`00b7f0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f0c8.md#insn-00b7f0e8)

~~~diff
- 00b7f0a4 ["INT_ADD", "register:40f0:8", ["const:b7f0a4:8", "const:4:8"]]
- 00b7f0a4 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b7f0e8 ["INT_ADD", "register:40f0:8", ["const:b7f0e8:8", "const:4:8"]]
+ 00b7f0e8 ["CALL", null, ["callee:00be12e0:8"]]
- 00b7f0a4 bytes 7b880194
+ 00b7f0e8 bytes 7e880194
~~~


<a id="compare-2f49aa3800971bf76d7702292b4e84a6"></a>

### [`00b7f0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f0d4.md) → [`00b7f118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f0d4.md#insn-00b7f0f8) · [`00b7f104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f0d4.md#insn-00b7f104) · [`00b7f110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f0d4.md#insn-00b7f110)
- 新版 [`00b7f13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md#insn-00b7f13c) · [`00b7f148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md#insn-00b7f148) · [`00b7f154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md#insn-00b7f154)

~~~diff
- 00b7f0f8 ["INT_ADD", "register:40f0:8", ["const:b7f0f8:8", "const:4:8"]]
- 00b7f0f8 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b7f13c ["INT_ADD", "register:40f0:8", ["const:b7f13c:8", "const:4:8"]]
+ 00b7f13c ["CALL", null, ["callee:00bdd980:8"]]
- 00b7f0f8 bytes 0e7a0194
+ 00b7f13c bytes 117a0194
- 00b7f104 ["INT_ADD", "register:40f0:8", ["const:b7f104:8", "const:4:8"]]
- 00b7f104 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b7f148 ["INT_ADD", "register:40f0:8", ["const:b7f148:8", "const:4:8"]]
+ 00b7f148 ["CALL", null, ["callee:00be12e0:8"]]
- 00b7f104 bytes 63880194
+ 00b7f148 bytes 66880194
- 00b7f110 ["INT_ADD", "register:40f0:8", ["const:b7f110:8", "const:4:8"]]
- 00b7f110 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b7f154 ["INT_ADD", "register:40f0:8", ["const:b7f154:8", "const:4:8"]]
+ 00b7f154 ["CALL", null, ["callee:00be12e0:8"]]
- 00b7f110 bytes 60880194
+ 00b7f154 bytes 63880194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b21756421ba2534b9bdb1af92f72848"></a>

### [`00b7f1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f1d8.md) → [`00b7f21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f21c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f1d8.md#insn-00b7f214)
- 新版 [`00b7f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f21c.md#insn-00b7f258)

~~~diff
- 00b7f214 ["INT_ADD", "register:40f0:8", ["const:b7f214:8", "const:4:8"]]
- 00b7f214 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b7f258 ["INT_ADD", "register:40f0:8", ["const:b7f258:8", "const:4:8"]]
+ 00b7f258 ["CALL", null, ["callee:00bdb390:8"]]
- 00b7f214 bytes 4b700194
+ 00b7f258 bytes 4e700194
~~~


<a id="compare-551826d8d17d4bc696ddddfcb6f53e79"></a>

### [`00b7f2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f2a8.md) → [`00b7f2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f2ec.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f2a8.md#insn-00b7f2e0)
- 新版 [`00b7f324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f2ec.md#insn-00b7f324)

~~~diff
- 00b7f2e0 ["INT_ADD", "register:40f0:8", ["const:b7f2e0:8", "const:4:8"]]
- 00b7f2e0 ["CALL", null, ["callee:00be1320:8"]]
+ 00b7f324 ["INT_ADD", "register:40f0:8", ["const:b7f324:8", "const:4:8"]]
+ 00b7f324 ["CALL", null, ["callee:00be1320:8"]]
- 00b7f2e0 bytes fc870194
+ 00b7f324 bytes ff870194
~~~


<a id="compare-4b246917b4bfe577c98e18d1edc44c90"></a>

### [`00b7f4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f4f8.md) → [`00b7f53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f53c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f4f8.md#insn-00b7f518)
- 新版 [`00b7f55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f53c.md#insn-00b7f55c)

~~~diff
- 00b7f518 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b7f518 ["INT_ADD", "register:40f0:8", ["const:b7f518:8", "const:4:8"]]
- 00b7f518 ["CALLIND", null, ["register:0:8"]]
+ 00b7f55c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b7f55c ["INT_ADD", "register:40f0:8", ["const:b7f55c:8", "const:4:8"]]
+ 00b7f55c ["CALLIND", null, ["register:0:8"]]
- 00b7f518 bytes 20003fd6
+ 00b7f55c bytes 20003fd6
~~~


<a id="compare-efe18b5873fc88fb5854f482905c2913"></a>

### [`00b7f530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f530.md) → [`00b7f574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f574.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f530.md#insn-00b7f550)
- 新版 [`00b7f594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f574.md#insn-00b7f594)

~~~diff
- 00b7f550 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b7f550 ["INT_ADD", "register:40f0:8", ["const:b7f550:8", "const:4:8"]]
- 00b7f550 ["CALLIND", null, ["register:0:8"]]
+ 00b7f594 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b7f594 ["INT_ADD", "register:40f0:8", ["const:b7f594:8", "const:4:8"]]
+ 00b7f594 ["CALLIND", null, ["register:0:8"]]
- 00b7f550 bytes 20003fd6
+ 00b7f594 bytes 20003fd6
~~~


<a id="compare-90bba5767b4017318edb432a9d9e9214"></a>

### [`00b7f568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f568.md) → [`00b7f5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7f598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f568.md#insn-00b7f598) · [`00b7f5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f568.md#insn-00b7f5fc) · [`00b7f634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f568.md#insn-00b7f634)
- 新版 [`00b7f5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md#insn-00b7f5dc) · [`00b7f640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md#insn-00b7f640) · [`00b7f678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md#insn-00b7f678)

~~~diff
- 00b7f598 ["INT_ADD", "register:40f0:8", ["const:b7f598:8", "const:4:8"]]
- 00b7f598 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7f5dc ["INT_ADD", "register:40f0:8", ["const:b7f5dc:8", "const:4:8"]]
+ 00b7f5dc ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7f598 bytes 66760194
+ 00b7f5dc bytes 69760194
- 00b7f5fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7f5fc ["INT_ADD", "register:40f0:8", ["const:b7f5fc:8", "const:4:8"]]
- 00b7f5fc ["CALLIND", null, ["register:0:8"]]
+ 00b7f640 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7f640 ["INT_ADD", "register:40f0:8", ["const:b7f640:8", "const:4:8"]]
+ 00b7f640 ["CALLIND", null, ["register:0:8"]]
- 00b7f5fc bytes 00013fd6
+ 00b7f640 bytes 00013fd6
- 00b7f634 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7f634 ["INT_ADD", "register:40f0:8", ["const:b7f634:8", "const:4:8"]]
- 00b7f634 ["CALLIND", null, ["register:0:8"]]
+ 00b7f678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7f678 ["INT_ADD", "register:40f0:8", ["const:b7f678:8", "const:4:8"]]
+ 00b7f678 ["CALLIND", null, ["register:0:8"]]
- 00b7f634 bytes 00013fd6
+ 00b7f678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a075dc86450c87f64a68ab2d17d48aec"></a>

### [`00b80778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80778.md) → [`00b807bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1310.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00be1360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1360.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b807a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80778.md#insn-00b807a0) · [`00b807e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80778.md#insn-00b807e8) · [`00b80818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80778.md#insn-00b80818)
- 新版 [`00b807e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md#insn-00b807e4) · [`00b8082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md#insn-00b8082c) · [`00b8085c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md#insn-00b8085c)

~~~diff
- 00b807a0 ["INT_ADD", "register:40f0:8", ["const:b807a0:8", "const:4:8"]]
- 00b807a0 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b807e4 ["INT_ADD", "register:40f0:8", ["const:b807e4:8", "const:4:8"]]
+ 00b807e4 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b807a0 bytes e4710194
+ 00b807e4 bytes e7710194
- 00b807e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b807e8 ["INT_ADD", "register:40f0:8", ["const:b807e8:8", "const:4:8"]]
- 00b807e8 ["CALLIND", null, ["register:0:8"]]
+ 00b8082c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8082c ["INT_ADD", "register:40f0:8", ["const:b8082c:8", "const:4:8"]]
+ 00b8082c ["CALLIND", null, ["register:0:8"]]
- 00b807e8 bytes 00013fd6
+ 00b8082c bytes 00013fd6
- 00b80818 ["INT_ADD", "register:40f0:8", ["const:b80818:8", "const:4:8"]]
- 00b80818 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b8085c ["INT_ADD", "register:40f0:8", ["const:b8085c:8", "const:4:8"]]
+ 00b8085c ["CALL", null, ["callee:00bdb450:8"]]
- 00b80818 bytes fa6a0194
+ 00b8085c bytes fd6a0194
~~~


<a id="compare-e3cf8565647792ab4b837004da24f1b8"></a>

### [`00b80890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80890.md) → [`00b808d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b808d4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1310.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b808a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80890.md#insn-00b808a8)
- 新版 [`00b808ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b808d4.md#insn-00b808ec)

~~~diff
- 00b808a8 ["INT_ADD", "register:40f0:8", ["const:b808a8:8", "const:4:8"]]
- 00b808a8 ["CALL", null, ["callee:00be1360:8"]]
+ 00b808ec ["INT_ADD", "register:40f0:8", ["const:b808ec:8", "const:4:8"]]
+ 00b808ec ["CALL", null, ["callee:00be1360:8"]]
- 00b808a8 bytes 9a820194
+ 00b808ec bytes 9d820194
~~~


<a id="compare-84000aac2f5ff940fcc36bebc09977f9"></a>

### [`00b80970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80970.md) → [`00b809b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1320.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00be1370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1370.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b809ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80970.md#insn-00b809ac) · [`00b80a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80970.md#insn-00b80a28) · [`00b80a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80970.md#insn-00b80a68)
- 新版 [`00b809f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md#insn-00b809f0) · [`00b80a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md#insn-00b80a6c) · [`00b80aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md#insn-00b80aac)

~~~diff
- 00b809ac ["INT_ADD", "register:40f0:8", ["const:b809ac:8", "const:4:8"]]
- 00b809ac ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b809f0 ["INT_ADD", "register:40f0:8", ["const:b809f0:8", "const:4:8"]]
+ 00b809f0 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b809ac bytes 61710194
+ 00b809f0 bytes 64710194
- 00b80a28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80a28 ["INT_ADD", "register:40f0:8", ["const:b80a28:8", "const:4:8"]]
- 00b80a28 ["CALLIND", null, ["register:0:8"]]
+ 00b80a6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80a6c ["INT_ADD", "register:40f0:8", ["const:b80a6c:8", "const:4:8"]]
+ 00b80a6c ["CALLIND", null, ["register:0:8"]]
- 00b80a28 bytes 00013fd6
+ 00b80a6c bytes 00013fd6
- 00b80a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80a68 ["INT_ADD", "register:40f0:8", ["const:b80a68:8", "const:4:8"]]
- 00b80a68 ["CALLIND", null, ["register:0:8"]]
+ 00b80aac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80aac ["INT_ADD", "register:40f0:8", ["const:b80aac:8", "const:4:8"]]
+ 00b80aac ["CALLIND", null, ["register:0:8"]]
- 00b80a68 bytes 00013fd6
+ 00b80aac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fabfe6a1c50d63fbf2e493e86bc5e752"></a>

### [`00b80bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80bd8.md) → [`00b80c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1330.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00be1380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1380.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80bd8.md#insn-00b80c0c) · [`00b80c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80bd8.md#insn-00b80c70) · [`00b80cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80bd8.md#insn-00b80cb4)
- 新版 [`00b80c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md#insn-00b80c50) · [`00b80cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md#insn-00b80cb4) · [`00b80cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md#insn-00b80cf8)

~~~diff
- 00b80c0c ["INT_ADD", "register:40f0:8", ["const:b80c0c:8", "const:4:8"]]
- 00b80c0c ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b80c50 ["INT_ADD", "register:40f0:8", ["const:b80c50:8", "const:4:8"]]
+ 00b80c50 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b80c0c bytes c9700194
+ 00b80c50 bytes cc700194
- 00b80c70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80c70 ["INT_ADD", "register:40f0:8", ["const:b80c70:8", "const:4:8"]]
- 00b80c70 ["CALLIND", null, ["register:0:8"]]
+ 00b80cb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80cb4 ["INT_ADD", "register:40f0:8", ["const:b80cb4:8", "const:4:8"]]
+ 00b80cb4 ["CALLIND", null, ["register:0:8"]]
- 00b80c70 bytes 00013fd6
+ 00b80cb4 bytes 00013fd6
- 00b80cb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80cb4 ["INT_ADD", "register:40f0:8", ["const:b80cb4:8", "const:4:8"]]
- 00b80cb4 ["CALLIND", null, ["register:0:8"]]
+ 00b80cf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80cf8 ["INT_ADD", "register:40f0:8", ["const:b80cf8:8", "const:4:8"]]
+ 00b80cf8 ["CALLIND", null, ["register:0:8"]]
- 00b80cb4 bytes 00013fd6
+ 00b80cf8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b4d679e40b5157f0f7238a2e9b9bf4"></a>

### [`00b80dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80dec.md) → [`00b80e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1340.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00be1390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1390.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b80e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80dec.md#insn-00b80e2c) · [`00b80e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80dec.md#insn-00b80e70) · [`00b80ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80dec.md#insn-00b80ec8)
- 新版 [`00b80e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md#insn-00b80e70) · [`00b80eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md#insn-00b80eb4) · [`00b80f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md#insn-00b80f0c)

~~~diff
- 00b80e2c ["INT_ADD", "register:40f0:8", ["const:b80e2c:8", "const:4:8"]]
- 00b80e2c ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b80e70 ["INT_ADD", "register:40f0:8", ["const:b80e70:8", "const:4:8"]]
+ 00b80e70 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b80e2c bytes 41700194
+ 00b80e70 bytes 44700194
- 00b80e70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80e70 ["INT_ADD", "register:40f0:8", ["const:b80e70:8", "const:4:8"]]
- 00b80e70 ["CALLIND", null, ["register:0:8"]]
+ 00b80eb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80eb4 ["INT_ADD", "register:40f0:8", ["const:b80eb4:8", "const:4:8"]]
+ 00b80eb4 ["CALLIND", null, ["register:0:8"]]
- 00b80e70 bytes 00013fd6
+ 00b80eb4 bytes 00013fd6
- 00b80ec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80ec8 ["INT_ADD", "register:40f0:8", ["const:b80ec8:8", "const:4:8"]]
- 00b80ec8 ["CALLIND", null, ["register:0:8"]]
+ 00b80f0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b80f0c ["INT_ADD", "register:40f0:8", ["const:b80f0c:8", "const:4:8"]]
+ 00b80f0c ["CALLIND", null, ["register:0:8"]]
- 00b80ec8 bytes 00013fd6
+ 00b80f0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4d3d68348a98b77c49adc1df88d5010"></a>

### [`00b81030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81030.md) → [`00b81074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81030.md#insn-00b81064) · [`00b810bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81030.md#insn-00b810bc) · [`00b81138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81030.md#insn-00b81138)
- 新版 [`00b810a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md#insn-00b810a8) · [`00b81100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md#insn-00b81100) · [`00b8117c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md#insn-00b8117c)

~~~diff
- 00b81064 ["INT_ADD", "register:40f0:8", ["const:b81064:8", "const:4:8"]]
- 00b81064 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b810a8 ["INT_ADD", "register:40f0:8", ["const:b810a8:8", "const:4:8"]]
+ 00b810a8 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b81064 bytes b36f0194
+ 00b810a8 bytes b66f0194
- 00b810bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b810bc ["INT_ADD", "register:40f0:8", ["const:b810bc:8", "const:4:8"]]
- 00b810bc ["CALLIND", null, ["register:0:8"]]
+ 00b81100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81100 ["INT_ADD", "register:40f0:8", ["const:b81100:8", "const:4:8"]]
+ 00b81100 ["CALLIND", null, ["register:0:8"]]
- 00b810bc bytes 00013fd6
+ 00b81100 bytes 00013fd6
- 00b81138 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81138 ["INT_ADD", "register:40f0:8", ["const:b81138:8", "const:4:8"]]
- 00b81138 ["CALLIND", null, ["register:0:8"]]
+ 00b8117c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8117c ["INT_ADD", "register:40f0:8", ["const:b8117c:8", "const:4:8"]]
+ 00b8117c ["CALLIND", null, ["register:0:8"]]
- 00b81138 bytes 00013fd6
+ 00b8117c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b6733e9dd97cf1905b4d1dca2958ff0"></a>

### [`00b811ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b811ec.md) → [`00b81230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4peekEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b811ec.md#insn-00b81214) · [`00b81254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b811ec.md#insn-00b81254) · [`00b8127c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b811ec.md#insn-00b8127c)
- 新版 [`00b81258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md#insn-00b81258) · [`00b81298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md#insn-00b81298) · [`00b812c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md#insn-00b812c0)

~~~diff
- 00b81214 ["INT_ADD", "register:40f0:8", ["const:b81214:8", "const:4:8"]]
- 00b81214 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b81258 ["INT_ADD", "register:40f0:8", ["const:b81258:8", "const:4:8"]]
+ 00b81258 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b81214 bytes 476f0194
+ 00b81258 bytes 4a6f0194
- 00b81254 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81254 ["INT_ADD", "register:40f0:8", ["const:b81254:8", "const:4:8"]]
- 00b81254 ["CALLIND", null, ["register:0:8"]]
+ 00b81298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81298 ["INT_ADD", "register:40f0:8", ["const:b81298:8", "const:4:8"]]
+ 00b81298 ["CALLIND", null, ["register:0:8"]]
- 00b81254 bytes 00013fd6
+ 00b81298 bytes 00013fd6
- 00b8127c ["INT_ADD", "register:40f0:8", ["const:b8127c:8", "const:4:8"]]
- 00b8127c ["CALL", null, ["callee:00bdb450:8"]]
+ 00b812c0 ["INT_ADD", "register:40f0:8", ["const:b812c0:8", "const:4:8"]]
+ 00b812c0 ["CALL", null, ["callee:00bdb450:8"]]
- 00b8127c bytes 61680194
+ 00b812c0 bytes 64680194
~~~


<a id="compare-43f65f70875f133f7195618159e9e454"></a>

### [`00b812ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b812ec.md) → [`00b81330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4readEPcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc230.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00bdc280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc280.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8131c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b812ec.md#insn-00b8131c) · [`00b81348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b812ec.md#insn-00b81348) · [`00b81378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b812ec.md#insn-00b81378)
- 新版 [`00b81360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md#insn-00b81360) · [`00b8138c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md#insn-00b8138c) · [`00b813bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md#insn-00b813bc)

~~~diff
- 00b8131c ["INT_ADD", "register:40f0:8", ["const:b8131c:8", "const:4:8"]]
- 00b8131c ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b81360 ["INT_ADD", "register:40f0:8", ["const:b81360:8", "const:4:8"]]
+ 00b81360 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b8131c bytes 056f0194
+ 00b81360 bytes 086f0194
- 00b81348 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81348 ["INT_ADD", "register:40f0:8", ["const:b81348:8", "const:4:8"]]
- 00b81348 ["CALLIND", null, ["register:0:8"]]
+ 00b8138c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8138c ["INT_ADD", "register:40f0:8", ["const:b8138c:8", "const:4:8"]]
+ 00b8138c ["CALLIND", null, ["register:0:8"]]
- 00b81348 bytes 00013fd6
+ 00b8138c bytes 00013fd6
- 00b81378 ["INT_ADD", "register:40f0:8", ["const:b81378:8", "const:4:8"]]
- 00b81378 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b813bc ["INT_ADD", "register:40f0:8", ["const:b813bc:8", "const:4:8"]]
+ 00b813bc ["CALL", null, ["callee:00bdb450:8"]]
- 00b81378 bytes 22680194
+ 00b813bc bytes 25680194
~~~


<a id="compare-20e00a9861ee56aa1514d1b3142a6f0e"></a>

### [`00b813e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b813e4.md) → [`00b81428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE8readsomeEPcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b813e4.md#insn-00b81414) · [`00b81454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b813e4.md#insn-00b81454) · [`00b814a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b813e4.md#insn-00b814a0)
- 新版 [`00b81458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md#insn-00b81458) · [`00b81498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md#insn-00b81498) · [`00b814e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md#insn-00b814e4)

~~~diff
- 00b81414 ["INT_ADD", "register:40f0:8", ["const:b81414:8", "const:4:8"]]
- 00b81414 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b81458 ["INT_ADD", "register:40f0:8", ["const:b81458:8", "const:4:8"]]
+ 00b81458 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b81414 bytes c76e0194
+ 00b81458 bytes ca6e0194
- 00b81454 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81454 ["INT_ADD", "register:40f0:8", ["const:b81454:8", "const:4:8"]]
- 00b81454 ["CALLIND", null, ["register:0:8"]]
+ 00b81498 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81498 ["INT_ADD", "register:40f0:8", ["const:b81498:8", "const:4:8"]]
+ 00b81498 ["CALLIND", null, ["register:0:8"]]
- 00b81454 bytes 00013fd6
+ 00b81498 bytes 00013fd6
- 00b814a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b814a0 ["INT_ADD", "register:40f0:8", ["const:b814a0:8", "const:4:8"]]
- 00b814a0 ["CALLIND", null, ["register:0:8"]]
+ 00b814e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b814e4 ["INT_ADD", "register:40f0:8", ["const:b814e4:8", "const:4:8"]]
+ 00b814e4 ["CALLIND", null, ["register:0:8"]]
- 00b814a0 bytes 20013fd6
+ 00b814e4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

