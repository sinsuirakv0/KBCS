# v15.7.3 → v15.7.4 · 要調査の変更候補 (10)

[一覧の目次](README.md)

<a id="compare-f65bb3e0bec19e1e8a2d74436141d794"></a>

### [`00b22c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22c78.md) → [`00b22cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22cbc.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1b0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf200.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b22d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22c78.md#insn-00b22d08) · [`00b22d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22c78.md#insn-00b22d14) · [`00b22d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22c78.md#insn-00b22d3c)
- 新版 `00b22d4c`（命令位置の公開資料なし） · `00b22d58`（命令位置の公開資料なし） · `00b22d80`（命令位置の公開資料なし）

~~~diff
- 00b22d08 ["INT_ADD", "register:40f0:8", ["const:b22d08:8", "const:4:8"]]
- 00b22d08 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b22d4c ["INT_ADD", "register:40f0:8", ["const:b22d4c:8", "const:4:8"]]
+ 00b22d4c ["CALL", null, ["callee:00bde2c0:8"]]
- 00b22d08 bytes 5aed0294
+ 00b22d4c bytes 5ded0294
- 00b22d14 ["INT_ADD", "register:40f0:8", ["const:b22d14:8", "const:4:8"]]
- 00b22d14 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b22d58 ["INT_ADD", "register:40f0:8", ["const:b22d58:8", "const:4:8"]]
+ 00b22d58 ["CALL", null, ["callee:00bdb040:8"]]
- 00b22d14 bytes b7e00294
+ 00b22d58 bytes bae00294
- 00b22d3c ["INT_ADD", "register:40f0:8", ["const:b22d3c:8", "const:4:8"]]
- 00b22d3c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b22d80 ["INT_ADD", "register:40f0:8", ["const:b22d80:8", "const:4:8"]]
+ 00b22d80 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b22d3c bytes 09e10294
+ 00b22d80 bytes 0ce10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02714a89cb50ed180b831c54cc8e4a91"></a>

### [`00b22e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22e30.md) → [`00b22e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22e74.md) _ZN11flatbuffers11SymbolTableINS_7RPCCallEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf200.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf250.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b22ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22e30.md#insn-00b22ec0) · [`00b22ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22e30.md#insn-00b22ecc) · [`00b22ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22e30.md#insn-00b22ef4)
- 新版 `00b22f04`（命令位置の公開資料なし） · `00b22f10`（命令位置の公開資料なし） · `00b22f38`（命令位置の公開資料なし）

~~~diff
- 00b22ec0 ["INT_ADD", "register:40f0:8", ["const:b22ec0:8", "const:4:8"]]
- 00b22ec0 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b22f04 ["INT_ADD", "register:40f0:8", ["const:b22f04:8", "const:4:8"]]
+ 00b22f04 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b22ec0 bytes ecec0294
+ 00b22f04 bytes efec0294
- 00b22ecc ["INT_ADD", "register:40f0:8", ["const:b22ecc:8", "const:4:8"]]
- 00b22ecc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b22f10 ["INT_ADD", "register:40f0:8", ["const:b22f10:8", "const:4:8"]]
+ 00b22f10 ["CALL", null, ["callee:00bdb040:8"]]
- 00b22ecc bytes 49e00294
+ 00b22f10 bytes 4ce00294
- 00b22ef4 ["INT_ADD", "register:40f0:8", ["const:b22ef4:8", "const:4:8"]]
- 00b22ef4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b22f38 ["INT_ADD", "register:40f0:8", ["const:b22f38:8", "const:4:8"]]
+ 00b22f38 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b22ef4 bytes 9be00294
+ 00b22f38 bytes 9ee00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1a76ab55d9e3ce48b5a29123a01641"></a>

### [`00b22fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22fe8.md) → [`00b2302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b2302c.md) _ZN11flatbuffers6Parser11SetRootTypeEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf770.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7c0.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b23028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22fe8.md#insn-00b23028) · [`00b23064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22fe8.md#insn-00b23064) · [`00b23084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22fe8.md#insn-00b23084)
- 新版 `00b2306c`（命令位置の公開資料なし） · `00b230a8`（命令位置の公開資料なし） · `00b230c8`（命令位置の公開資料なし）

~~~diff
- 00b23028 ["INT_ADD", "register:40f0:8", ["const:b23028:8", "const:4:8"]]
- 00b23028 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b2306c ["INT_ADD", "register:40f0:8", ["const:b2306c:8", "const:4:8"]]
+ 00b2306c ["CALL", null, ["callee:00bdb190:8"]]
- 00b23028 bytes 46e00294
+ 00b2306c bytes 49e00294
- 00b23064 ["INT_ADD", "register:40f0:8", ["const:b23064:8", "const:4:8"]]
- 00b23064 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b230a8 ["INT_ADD", "register:40f0:8", ["const:b230a8:8", "const:4:8"]]
+ 00b230a8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b23064 bytes e3df0294
+ 00b230a8 bytes e6df0294
- 00b23084 ["INT_ADD", "register:40f0:8", ["const:b23084:8", "const:4:8"]]
- 00b23084 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b230c8 ["INT_ADD", "register:40f0:8", ["const:b230c8:8", "const:4:8"]]
+ 00b230c8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b23084 bytes 37e00294
+ 00b230c8 bytes 3ae00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14beb7df4820641d51d710aece77ea0f"></a>

### [`00b23318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23318.md) → [`00b2335c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b2335c.md) _ZN11flatbuffers6Parser14ParseNamespaceEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf800.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00bdf850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf850.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2333c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23318.md#insn-00b2333c) · [`00b23370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23318.md#insn-00b23370) · [`00b233d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23318.md#insn-00b233d8)
- 新版 `00b23380`（命令位置の公開資料なし） · `00b233b4`（命令位置の公開資料なし） · `00b2341c`（命令位置の公開資料なし）

~~~diff
- 00b2333c ["INT_ADD", "register:40f0:8", ["const:b2333c:8", "const:4:8"]]
- 00b2333c ["CALL", null, ["callee:00bdf970:8"]]
+ 00b23380 ["INT_ADD", "register:40f0:8", ["const:b23380:8", "const:4:8"]]
+ 00b23380 ["CALL", null, ["callee:00bdf970:8"]]
- 00b2333c bytes 79f10294
+ 00b23380 bytes 7cf10294
- 00b23370 ["INT_ADD", "register:40f0:8", ["const:b23370:8", "const:4:8"]]
- 00b23370 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b233b4 ["INT_ADD", "register:40f0:8", ["const:b233b4:8", "const:4:8"]]
+ 00b233b4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b23370 bytes 20df0294
+ 00b233b4 bytes 23df0294
- 00b233d8 ["INT_ADD", "register:40f0:8", ["const:b233d8:8", "const:4:8"]]
- 00b233d8 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b2341c ["INT_ADD", "register:40f0:8", ["const:b2341c:8", "const:4:8"]]
+ 00b2341c ["CALL", null, ["callee:00bde2c0:8"]]
- 00b233d8 bytes a6eb0294
+ 00b2341c bytes a9eb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f97f435ac74ace1346e2a77a0fd67f"></a>

### [`00b25134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25134.md) → [`00b25178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25178.md) _ZN11flatbuffers6Parser24ParseProtoCurliesOrIdentEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25134.md#insn-00b25150) · [`00b25188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25134.md#insn-00b25188)
- 新版 `00b25194`（命令位置の公開資料なし） · `00b251cc`（命令位置の公開資料なし）

~~~diff
- 00b25150 ["INT_ADD", "register:40f0:8", ["const:b25150:8", "const:4:8"]]
- 00b25150 ["CALL", null, ["callee:00bdf970:8"]]
+ 00b25194 ["INT_ADD", "register:40f0:8", ["const:b25194:8", "const:4:8"]]
+ 00b25194 ["CALL", null, ["callee:00bdf970:8"]]
- 00b25150 bytes f4e90294
+ 00b25194 bytes f7e90294
- 00b25188 ["INT_ADD", "register:40f0:8", ["const:b25188:8", "const:4:8"]]
- 00b25188 ["CALL", null, ["callee:00bdf970:8"]]
+ 00b251cc ["INT_ADD", "register:40f0:8", ["const:b251cc:8", "const:4:8"]]
+ 00b251cc ["CALL", null, ["callee:00bdf970:8"]]
- 00b25188 bytes e6e90294
+ 00b251cc bytes e9e90294
~~~


<a id="compare-9d8f498a7bf3d1f8fab9942b60c38cf3"></a>

### [`00b251d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b251d0.md) → [`00b25214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25214.md) _ZN11flatbuffers11SymbolTableINS_7EnumDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1e0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf230.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b251d0.md#insn-00b25260) · [`00b2526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b251d0.md#insn-00b2526c) · [`00b25294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b251d0.md#insn-00b25294)
- 新版 `00b252a4`（命令位置の公開資料なし） · `00b252b0`（命令位置の公開資料なし） · `00b252d8`（命令位置の公開資料なし）

~~~diff
- 00b25260 ["INT_ADD", "register:40f0:8", ["const:b25260:8", "const:4:8"]]
- 00b25260 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b252a4 ["INT_ADD", "register:40f0:8", ["const:b252a4:8", "const:4:8"]]
+ 00b252a4 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b25260 bytes 04e40294
+ 00b252a4 bytes 07e40294
- 00b2526c ["INT_ADD", "register:40f0:8", ["const:b2526c:8", "const:4:8"]]
- 00b2526c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b252b0 ["INT_ADD", "register:40f0:8", ["const:b252b0:8", "const:4:8"]]
+ 00b252b0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2526c bytes 61d70294
+ 00b252b0 bytes 64d70294
- 00b25294 ["INT_ADD", "register:40f0:8", ["const:b25294:8", "const:4:8"]]
- 00b25294 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b252d8 ["INT_ADD", "register:40f0:8", ["const:b252d8:8", "const:4:8"]]
+ 00b252d8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b25294 bytes b3d70294
+ 00b252d8 bytes b6d70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4918e439598e8543930bbecffdac067d"></a>

### [`00b25498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25498.md) → [`00b254dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b254dc.md) _ZN11flatbuffers6Parser13ParseProtoKeyEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7e0.md) · 呼出先 2件 [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md) [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md)
- 新版 呼出元 1件 [`00bdf830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf830.md) · 呼出先 2件 [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md) [`00bdf9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b254c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25498.md#insn-00b254c4) · [`00b254e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25498.md#insn-00b254e4) · [`00b25514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25498.md#insn-00b25514)
- 新版 `00b25508`（命令位置の公開資料なし） · `00b25528`（命令位置の公開資料なし） · `00b25558`（命令位置の公開資料なし）

~~~diff
- 00b254c4 ["INT_ADD", "register:40f0:8", ["const:b254c4:8", "const:4:8"]]
- 00b254c4 ["CALL", null, ["callee:00bdf970:8"]]
+ 00b25508 ["INT_ADD", "register:40f0:8", ["const:b25508:8", "const:4:8"]]
+ 00b25508 ["CALL", null, ["callee:00bdf970:8"]]
- 00b254c4 bytes 17e90294
+ 00b25508 bytes 1ae90294
- 00b254e4 ["INT_ADD", "register:40f0:8", ["const:b254e4:8", "const:4:8"]]
- 00b254e4 ["CALL", null, ["callee:00bdf970:8"]]
+ 00b25528 ["INT_ADD", "register:40f0:8", ["const:b25528:8", "const:4:8"]]
+ 00b25528 ["CALL", null, ["callee:00bdf970:8"]]
- 00b254e4 bytes 0fe90294
+ 00b25528 bytes 12e90294
- 00b25514 ["INT_ADD", "register:40f0:8", ["const:b25514:8", "const:4:8"]]
- 00b25514 ["CALL", null, ["callee:00bdf9b0:8"]]
+ 00b25558 ["INT_ADD", "register:40f0:8", ["const:b25558:8", "const:4:8"]]
+ 00b25558 ["CALL", null, ["callee:00bdf9b0:8"]]
- 00b25514 bytes 13e90294
+ 00b25558 bytes 16e90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a330fd9d3ba53839c230fb43b4b8e56"></a>

### [`00b25d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25d44.md) → [`00b25d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25d88.md) _ZN11flexbuffers7Builder6EndMapEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfad0.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdfb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb20.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25d44.md#insn-00b25dbc) · [`00b25ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25d44.md#insn-00b25ddc) · [`00b25e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25d44.md#insn-00b25e00)
- 新版 `00b25e00`（命令位置の公開資料なし） · `00b25e20`（命令位置の公開資料なし） · `00b25e44`（命令位置の公開資料なし）

~~~diff
- 00b25dbc ["INT_ADD", "register:40f0:8", ["const:b25dbc:8", "const:4:8"]]
- 00b25dbc ["CALL", null, ["callee:00bdfed0:8"]]
+ 00b25e00 ["INT_ADD", "register:40f0:8", ["const:b25e00:8", "const:4:8"]]
+ 00b25e00 ["CALL", null, ["callee:00bdfed0:8"]]
- 00b25dbc bytes 31e80294
+ 00b25e00 bytes 34e80294
- 00b25ddc ["INT_ADD", "register:40f0:8", ["const:b25ddc:8", "const:4:8"]]
- 00b25ddc ["CALL", null, ["callee:00bdfb00:8"]]
+ 00b25e20 ["INT_ADD", "register:40f0:8", ["const:b25e20:8", "const:4:8"]]
+ 00b25e20 ["CALL", null, ["callee:00bdfb00:8"]]
- 00b25ddc bytes 35e70294
+ 00b25e20 bytes 38e70294
- 00b25e00 ["INT_ADD", "register:40f0:8", ["const:b25e00:8", "const:4:8"]]
- 00b25e00 ["CALL", null, ["callee:00bdfb00:8"]]
+ 00b25e44 ["INT_ADD", "register:40f0:8", ["const:b25e44:8", "const:4:8"]]
+ 00b25e44 ["CALL", null, ["callee:00bdfb00:8"]]
- 00b25e00 bytes 2ce70294
+ 00b25e44 bytes 2fe70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f9e589e869f0515e6065d3faa656ea"></a>

### [`00b25f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25f28.md) → [`00b25f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25f6c.md) _ZN11flexbuffers7Builder9EndVectorEmbb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb10.md) · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bdfab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfab0.md)
- 新版 呼出元 1件 [`00bdfb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb60.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bdfb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25f28.md#insn-00b25f74) · [`00b25fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25f28.md#insn-00b25fa0) · [`00b26010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25f28.md#insn-00b26010)
- 新版 `00b25fb8`（命令位置の公開資料なし） · `00b25fe4`（命令位置の公開資料なし） · `00b26054`（命令位置の公開資料なし）

~~~diff
- 00b25f74 ["INT_ADD", "register:40f0:8", ["const:b25f74:8", "const:4:8"]]
- 00b25f74 ["CALL", null, ["callee:00bdfb00:8"]]
+ 00b25fb8 ["INT_ADD", "register:40f0:8", ["const:b25fb8:8", "const:4:8"]]
+ 00b25fb8 ["CALL", null, ["callee:00bdfb00:8"]]
- 00b25f74 bytes cfe60294
+ 00b25fb8 bytes d2e60294
- 00b25fa0 ["INT_ADD", "register:40f0:8", ["const:b25fa0:8", "const:4:8"]]
- 00b25fa0 ["CALL", null, ["callee:00be0070:8"]]
+ 00b25fe4 ["INT_ADD", "register:40f0:8", ["const:b25fe4:8", "const:4:8"]]
+ 00b25fe4 ["CALL", null, ["callee:00be0070:8"]]
- 00b25fa0 bytes 20e80294
+ 00b25fe4 bytes 23e80294
- 00b26010 ["INT_ADD", "register:40f0:8", ["const:b26010:8", "const:4:8"]]
- 00b26010 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b26054 ["INT_ADD", "register:40f0:8", ["const:b26054:8", "const:4:8"]]
+ 00b26054 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b26010 bytes 98e00294
+ 00b26054 bytes 9be00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ec024a0eb66ac7a772dbfedc735c33e"></a>

### [`00b26084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26084.md) → [`00b260c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b260c8.md) _ZN11flatbuffers6Parser15ParseFlexBufferEPKcS2_PN11flexbuffers7BuilderE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf830.md) [`00bdf8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8f0.md) [`00bdfae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf880.md) [`00bdf940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf940.md) [`00bdfb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b260b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26084.md#insn-00b260b0) · [`00b260d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26084.md#insn-00b260d0) · [`00b26108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26084.md#insn-00b26108)
- 新版 `00b260f4`（命令位置の公開資料なし） · `00b26114`（命令位置の公開資料なし） · `00b2614c`（命令位置の公開資料なし）

~~~diff
- 00b260b0 ["INT_ADD", "register:40f0:8", ["const:b260b0:8", "const:4:8"]]
- 00b260b0 ["CALL", null, ["callee:00bdf880:8"]]
+ 00b260f4 ["INT_ADD", "register:40f0:8", ["const:b260f4:8", "const:4:8"]]
+ 00b260f4 ["CALL", null, ["callee:00bdf880:8"]]
- 00b260b0 bytes e0e50294
+ 00b260f4 bytes e3e50294
- 00b260d0 ["INT_ADD", "register:40f0:8", ["const:b260d0:8", "const:4:8"]]
- 00b260d0 ["CALL", null, ["callee:00bdf940:8"]]
+ 00b26114 ["INT_ADD", "register:40f0:8", ["const:b26114:8", "const:4:8"]]
+ 00b26114 ["CALL", null, ["callee:00bdf940:8"]]
- 00b260d0 bytes 08e60294
+ 00b26114 bytes 0be60294
- 00b26108 ["INT_ADD", "register:40f0:8", ["const:b26108:8", "const:4:8"]]
- 00b26108 ["CALL", null, ["callee:00bdfb30:8"]]
+ 00b2614c ["INT_ADD", "register:40f0:8", ["const:b2614c:8", "const:4:8"]]
+ 00b2614c ["CALL", null, ["callee:00bdfb30:8"]]
- 00b26108 bytes 76e60294
+ 00b2614c bytes 79e60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc92e2c99ce6ddde0872a56ffe6afa4"></a>

### [`00b2628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md) → [`00b262d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b262d0.md) _ZN11flexbuffers7Builder6FinishEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfae0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdfb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb00.md) [`00be0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md) [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md)
- 新版 呼出元 1件 [`00bdfb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb30.md) · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdfb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb50.md) [`00be00d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md) [`00be00e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b26358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md#insn-00b26358) · [`00b26368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md#insn-00b26368) · [`00b263bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md#insn-00b263bc)
- 新版 `00b2639c`（命令位置の公開資料なし） · `00b263ac`（命令位置の公開資料なし） · `00b26400`（命令位置の公開資料なし）

~~~diff
- 00b26358 ["INT_ADD", "register:40f0:8", ["const:b26358:8", "const:4:8"]]
- 00b26358 ["CALL", null, ["callee:00be00d0:8"]]
+ 00b2639c ["INT_ADD", "register:40f0:8", ["const:b2639c:8", "const:4:8"]]
+ 00b2639c ["CALL", null, ["callee:00be00d0:8"]]
- 00b26358 bytes 4ae70294
+ 00b2639c bytes 4de70294
- 00b26368 ["INT_ADD", "register:40f0:8", ["const:b26368:8", "const:4:8"]]
- 00b26368 ["CALL", null, ["callee:00bdfb50:8"]]
+ 00b263ac ["INT_ADD", "register:40f0:8", ["const:b263ac:8", "const:4:8"]]
+ 00b263ac ["CALL", null, ["callee:00bdfb50:8"]]
- 00b26368 bytes e6e50294
+ 00b263ac bytes e9e50294
- 00b263bc ["INT_ADD", "register:40f0:8", ["const:b263bc:8", "const:4:8"]]
- 00b263bc ["CALL", null, ["callee:00be00e0:8"]]
+ 00b26400 ["INT_ADD", "register:40f0:8", ["const:b26400:8", "const:4:8"]]
+ 00b26400 ["CALL", null, ["callee:00be00e0:8"]]
- 00b263bc bytes 35e70294
+ 00b26400 bytes 38e70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1eb44d835a0043aa9289c13ebcbce52"></a>

### [`00b28480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28480.md) → [`00b284c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b284c4.md) _ZNK11flatbuffers6Parser25GetIncludedFilesRecursiveERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`0052773c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00527/0052773c.md) [`0052ad78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052ad78.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0052773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md) [`0052ad78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ad78.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b284f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28480.md#insn-00b284f4) · [`00b28504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28480.md#insn-00b28504) · [`00b285b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28480.md#insn-00b285b0)
- 新版 `00b28538`（命令位置の公開資料なし） · `00b28548`（命令位置の公開資料なし） · `00b285f4`（命令位置の公開資料なし）

~~~diff
- 00b284f4 ["INT_ADD", "register:40f0:8", ["const:b284f4:8", "const:4:8"]]
- 00b284f4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b28538 ["INT_ADD", "register:40f0:8", ["const:b28538:8", "const:4:8"]]
+ 00b28538 ["CALL", null, ["callee:00bdb040:8"]]
- 00b284f4 bytes bfca0294
+ 00b28538 bytes c2ca0294
- 00b28504 ["INT_ADD", "register:40f0:8", ["const:b28504:8", "const:4:8"]]
- 00b28504 ["CALL", null, ["callee:00bde730:8"]]
+ 00b28548 ["INT_ADD", "register:40f0:8", ["const:b28548:8", "const:4:8"]]
+ 00b28548 ["CALL", null, ["callee:00bde730:8"]]
- 00b28504 bytes 77d80294
+ 00b28548 bytes 7ad80294
- 00b285b0 ["INT_ADD", "register:40f0:8", ["const:b285b0:8", "const:4:8"]]
- 00b285b0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b285f4 ["INT_ADD", "register:40f0:8", ["const:b285f4:8", "const:4:8"]]
+ 00b285f4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b285b0 bytes 90ca0294
+ 00b285f4 bytes 93ca0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff1ef69fd26dd6db84e809da4b61832a"></a>

### [`00b29a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29a24.md) → [`00b29a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b29a68.md) _ZNK11flatbuffers8FieldDef9SerializeEPNS_17FlatBufferBuilderEtRKNS_6ParserE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc10.md) · 呼出先 8件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb700.md) [`00bdb720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb720.md) [`00bdf050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf050.md) [`00bdf060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf060.md)
- 新版 呼出元 1件 [`00bdfc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc60.md) · 呼出先 8件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb750.md) [`00bdb770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb770.md) [`00bdf0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0a0.md) [`00bdf0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29a24.md#insn-00b29a74) · [`00b29a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29a24.md#insn-00b29a9c) · [`00b29ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29a24.md#insn-00b29ab0)
- 新版 `00b29ab8`（命令位置の公開資料なし） · `00b29ae0`（命令位置の公開資料なし） · `00b29af4`（命令位置の公開資料なし）

~~~diff
- 00b29a74 ["INT_ADD", "register:40f0:8", ["const:b29a74:8", "const:4:8"]]
- 00b29a74 ["CALL", null, ["callee:00bdf4d0:8"]]
+ 00b29ab8 ["INT_ADD", "register:40f0:8", ["const:b29ab8:8", "const:4:8"]]
+ 00b29ab8 ["CALL", null, ["callee:00bdf4d0:8"]]
- 00b29a74 bytes 83d60294
+ 00b29ab8 bytes 86d60294
- 00b29a9c ["INT_ADD", "register:40f0:8", ["const:b29a9c:8", "const:4:8"]]
- 00b29a9c ["CALL", null, ["callee:00bdf0a0:8"]]
+ 00b29ae0 ["INT_ADD", "register:40f0:8", ["const:b29ae0:8", "const:4:8"]]
+ 00b29ae0 ["CALL", null, ["callee:00bdf0a0:8"]]
- 00b29a9c bytes 6dd50294
+ 00b29ae0 bytes 70d50294
- 00b29ab0 ["INT_ADD", "register:40f0:8", ["const:b29ab0:8", "const:4:8"]]
- 00b29ab0 ["CALL", null, ["callee:00bdfc00:8"]]
+ 00b29af4 ["INT_ADD", "register:40f0:8", ["const:b29af4:8", "const:4:8"]]
+ 00b29af4 ["CALL", null, ["callee:00bdfc00:8"]]
- 00b29ab0 bytes 40d80294
+ 00b29af4 bytes 43d80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03c57d8ddba6918a000d4b754d7fff0c"></a>

### [`00b2a064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a064.md) → [`00b2a0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a0a8.md) _ZN10reflection12CreateObjectERN11flatbuffers17FlatBufferBuilderENS0_6OffsetINS0_6StringEEENS3_INS0_6VectorINS3_INS_5FieldEEEEEEEbiiNS3_INS6

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0a0.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0f0.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md) [`00bdf4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4c0.md)
- 新版 呼出元 1件 [`00bdf0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0f0.md) · 呼出先 9件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf140.md) [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf470.md) [`00bdf510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a064.md#insn-00b2a0d4) · [`00b2a0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a064.md#insn-00b2a0e4) · [`00b2a0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a064.md#insn-00b2a0fc)
- 新版 `00b2a118`（命令位置の公開資料なし） · `00b2a128`（命令位置の公開資料なし） · `00b2a140`（命令位置の公開資料なし）

~~~diff
- 00b2a0d4 ["INT_ADD", "register:40f0:8", ["const:b2a0d4:8", "const:4:8"]]
- 00b2a0d4 ["CALL", null, ["callee:00bdf5c0:8"]]
+ 00b2a118 ["INT_ADD", "register:40f0:8", ["const:b2a118:8", "const:4:8"]]
+ 00b2a118 ["CALL", null, ["callee:00bdf5c0:8"]]
- 00b2a0d4 bytes 27d50294
+ 00b2a118 bytes 2ad50294
- 00b2a0e4 ["INT_ADD", "register:40f0:8", ["const:b2a0e4:8", "const:4:8"]]
- 00b2a0e4 ["CALL", null, ["callee:00bdf5b0:8"]]
+ 00b2a128 ["INT_ADD", "register:40f0:8", ["const:b2a128:8", "const:4:8"]]
+ 00b2a128 ["CALL", null, ["callee:00bdf5b0:8"]]
- 00b2a0e4 bytes 1fd50294
+ 00b2a128 bytes 22d50294
- 00b2a0fc ["INT_ADD", "register:40f0:8", ["const:b2a0fc:8", "const:4:8"]]
- 00b2a0fc ["CALL", null, ["callee:00bdf470:8"]]
+ 00b2a140 ["INT_ADD", "register:40f0:8", ["const:b2a140:8", "const:4:8"]]
+ 00b2a140 ["CALL", null, ["callee:00bdf470:8"]]
- 00b2a0fc bytes c9d40294
+ 00b2a140 bytes ccd40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6f28e9b0347698e0ad97a845cf7485"></a>

### [`00b2b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b064.md) → [`00b2b0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b0a8.md) _ZNK11flatbuffers4Type9SerializeEPNS_17FlatBufferBuilderE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdf050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdf0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b064.md#insn-00b2b090)
- 新版 `00b2b0d4`（命令位置の公開資料なし）

~~~diff
- 00b2b090 ["INT_ADD", "register:40f0:8", ["const:b2b090:8", "const:4:8"]]
- 00b2b090 ["CALL", null, ["callee:00bdf0a0:8"]]
+ 00b2b0d4 ["INT_ADD", "register:40f0:8", ["const:b2b0d4:8", "const:4:8"]]
+ 00b2b0d4 ["CALL", null, ["callee:00bdf0a0:8"]]
- 00b2b090 bytes f0cf0294
+ 00b2b0d4 bytes f3cf0294
~~~


<a id="compare-c5ac205b35bb71315bc73bc587395237"></a>

### [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) → [`00b2b0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b0ec.md) _ZN10reflection11CreateFieldERN11flatbuffers17FlatBufferBuilderENS0_6OffsetINS0_6StringEEENS3_INS_4TypeEEEttldbbbNS3_INS0_6VectorINS3_INS_8K

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf060.md) · 呼出先 13件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0b0.md) [`00bdf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md) [`00bdf0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0d0.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0b0.md) · 呼出先 13件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf100.md) [`00bdf110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf110.md) [`00bdf120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf120.md) [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md#insn-00b2b128) · [`00b2b148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md#insn-00b2b148) · [`00b2b1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md#insn-00b2b1a8)
- 新版 `00b2b16c`（命令位置の公開資料なし） · `00b2b18c`（命令位置の公開資料なし） · `00b2b1ec`（命令位置の公開資料なし）

~~~diff
- 00b2b128 ["INT_ADD", "register:40f0:8", ["const:b2b128:8", "const:4:8"]]
- 00b2b128 ["CALL", null, ["callee:00bdf450:8"]]
+ 00b2b16c ["INT_ADD", "register:40f0:8", ["const:b2b16c:8", "const:4:8"]]
+ 00b2b16c ["CALL", null, ["callee:00bdf450:8"]]
- 00b2b128 bytes b6d00294
+ 00b2b16c bytes b9d00294
- 00b2b148 ["INT_ADD", "register:40f0:8", ["const:b2b148:8", "const:4:8"]]
- 00b2b148 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b2b18c ["INT_ADD", "register:40f0:8", ["const:b2b18c:8", "const:4:8"]]
+ 00b2b18c ["CALL", null, ["callee:00bdf390:8"]]
- 00b2b148 bytes 7ed00294
+ 00b2b18c bytes 81d00294
- 00b2b1a8 ["INT_ADD", "register:40f0:8", ["const:b2b1a8:8", "const:4:8"]]
- 00b2b1a8 ["CALL", null, ["callee:00bdf490:8"]]
+ 00b2b1ec ["INT_ADD", "register:40f0:8", ["const:b2b1ec:8", "const:4:8"]]
+ 00b2b1ec ["CALL", null, ["callee:00bdf490:8"]]
- 00b2b1a8 bytes a6d00294
+ 00b2b1ec bytes a9d00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cd432bc754d6aebc7d6501bb810689d"></a>

### [`00b2b664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b664.md) → [`00b2b6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b6a8.md) _ZNK11flatbuffers7RPCCall9SerializeEPNS_17FlatBufferBuilderERKNS_6ParserE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc00.md) · 呼出先 8件 [`00bdf480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md) [`00bdf4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4a0.md) [`00bdf4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4c0.md) [`00bdf4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4e0.md) [`00bdf4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4f0.md)
- 新版 呼出元 1件 [`00bdfc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc50.md) · 呼出先 8件 [`00bdf4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4d0.md) [`00bdf4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4f0.md) [`00bdf510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf510.md) [`00bdf530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf530.md) [`00bdf540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b664.md#insn-00b2b6a0) · [`00b2b6b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b664.md#insn-00b2b6b4) · [`00b2b6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b664.md#insn-00b2b6cc)
- 新版 `00b2b6e4`（命令位置の公開資料なし） · `00b2b6f8`（命令位置の公開資料なし） · `00b2b710`（命令位置の公開資料なし）

~~~diff
- 00b2b6a0 ["INT_ADD", "register:40f0:8", ["const:b2b6a0:8", "const:4:8"]]
- 00b2b6a0 ["CALL", null, ["callee:00bdf4d0:8"]]
+ 00b2b6e4 ["INT_ADD", "register:40f0:8", ["const:b2b6e4:8", "const:4:8"]]
+ 00b2b6e4 ["CALL", null, ["callee:00bdf4d0:8"]]
- 00b2b6a0 bytes 78cf0294
+ 00b2b6e4 bytes 7bcf0294
- 00b2b6b4 ["INT_ADD", "register:40f0:8", ["const:b2b6b4:8", "const:4:8"]]
- 00b2b6b4 ["CALL", null, ["callee:00bdfc00:8"]]
+ 00b2b6f8 ["INT_ADD", "register:40f0:8", ["const:b2b6f8:8", "const:4:8"]]
+ 00b2b6f8 ["CALL", null, ["callee:00bdfc00:8"]]
- 00b2b6b4 bytes 3fd10294
+ 00b2b6f8 bytes 42d10294
- 00b2b6cc ["INT_ADD", "register:40f0:8", ["const:b2b6cc:8", "const:4:8"]]
- 00b2b6cc ["CALL", null, ["callee:00bdf4f0:8"]]
+ 00b2b710 ["INT_ADD", "register:40f0:8", ["const:b2b710:8", "const:4:8"]]
+ 00b2b710 ["CALL", null, ["callee:00bdf4f0:8"]]
- 00b2b6cc bytes 75cf0294
+ 00b2b710 bytes 78cf0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf85c79e3700de0eb03f0d1aa5a4473"></a>

### [`00b2b778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b778.md) → [`00b2b7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b7bc.md) _ZN11flatbuffers7RPCCall11DeserializeERNS_6ParserEPKN10reflection7RPCCallE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa40.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdf100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf100.md)
- 新版 呼出元 1件 [`00bdfa90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa90.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdf150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b778.md#insn-00b2b7fc) · [`00b2b81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b778.md#insn-00b2b81c) · [`00b2b84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b778.md#insn-00b2b84c)
- 新版 `00b2b840`（命令位置の公開資料なし） · `00b2b860`（命令位置の公開資料なし） · `00b2b890`（命令位置の公開資料なし）

~~~diff
- 00b2b7fc ["INT_ADD", "register:40f0:8", ["const:b2b7fc:8", "const:4:8"]]
- 00b2b7fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2b840 ["INT_ADD", "register:40f0:8", ["const:b2b840:8", "const:4:8"]]
+ 00b2b840 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2b7fc bytes fdbd0294
+ 00b2b840 bytes 00be0294
- 00b2b81c ["INT_ADD", "register:40f0:8", ["const:b2b81c:8", "const:4:8"]]
- 00b2b81c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b2b860 ["INT_ADD", "register:40f0:8", ["const:b2b860:8", "const:4:8"]]
+ 00b2b860 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b2b81c bytes 51be0294
+ 00b2b860 bytes 54be0294
- 00b2b84c ["INT_ADD", "register:40f0:8", ["const:b2b84c:8", "const:4:8"]]
- 00b2b84c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b2b890 ["INT_ADD", "register:40f0:8", ["const:b2b890:8", "const:4:8"]]
+ 00b2b890 ["CALL", null, ["callee:00bdb060:8"]]
- 00b2b84c bytes f1bd0294
+ 00b2b890 bytes f4bd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22a805d0db822889b5afa5c6fe014bde"></a>

### [`00b2baf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2baf8.md) → [`00b2bb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2bb3c.md) _ZN11flatbuffers10ServiceDef11DeserializeERNS_6ParserEPKN10reflection7ServiceE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf130.md) · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md)
- 新版 呼出元 1件 [`00bdf180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf180.md) · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2bb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2baf8.md#insn-00b2bb84) · [`00b2bba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2baf8.md#insn-00b2bba4) · [`00b2bbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2baf8.md#insn-00b2bbb8)
- 新版 `00b2bbc8`（命令位置の公開資料なし） · `00b2bbe8`（命令位置の公開資料なし） · `00b2bbfc`（命令位置の公開資料なし）

~~~diff
- 00b2bb84 ["INT_ADD", "register:40f0:8", ["const:b2bb84:8", "const:4:8"]]
- 00b2bb84 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2bbc8 ["INT_ADD", "register:40f0:8", ["const:b2bbc8:8", "const:4:8"]]
+ 00b2bbc8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2bb84 bytes 1bbd0294
+ 00b2bbc8 bytes 1ebd0294
- 00b2bba4 ["INT_ADD", "register:40f0:8", ["const:b2bba4:8", "const:4:8"]]
- 00b2bba4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b2bbe8 ["INT_ADD", "register:40f0:8", ["const:b2bbe8:8", "const:4:8"]]
+ 00b2bbe8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b2bba4 bytes 6fbd0294
+ 00b2bbe8 bytes 72bd0294
- 00b2bbb8 ["INT_ADD", "register:40f0:8", ["const:b2bbb8:8", "const:4:8"]]
- 00b2bbb8 ["CALL", null, ["callee:00bdf8b0:8"]]
+ 00b2bbfc ["INT_ADD", "register:40f0:8", ["const:b2bbfc:8", "const:4:8"]]
+ 00b2bbfc ["CALL", null, ["callee:00bdf8b0:8"]]
- 00b2bbb8 bytes 2acf0294
+ 00b2bbfc bytes 2dcf0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4fc99570b804956a6c9073926547ddb"></a>

### [`00b2bde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2bde0.md) → [`00b2be24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2be24.md) _ZNK11flatbuffers7EnumVal9SerializeEPNS_17FlatBufferBuilderERKNS_6ParserE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfbf0.md) · 呼出先 4件 [`00bdf050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf050.md) [`00bdf0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0e0.md) [`00bdf480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md) [`00bdf4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4a0.md)
- 新版 呼出元 1件 [`00bdfc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc40.md) · 呼出先 4件 [`00bdf0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0a0.md) [`00bdf130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf130.md) [`00bdf4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4d0.md) [`00bdf4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2be18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2bde0.md#insn-00b2be18) · [`00b2be40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2bde0.md#insn-00b2be40) · [`00b2be58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2bde0.md#insn-00b2be58)
- 新版 `00b2be5c`（命令位置の公開資料なし） · `00b2be84`（命令位置の公開資料なし） · `00b2be9c`（命令位置の公開資料なし）

~~~diff
- 00b2be18 ["INT_ADD", "register:40f0:8", ["const:b2be18:8", "const:4:8"]]
- 00b2be18 ["CALL", null, ["callee:00bdf4d0:8"]]
+ 00b2be5c ["INT_ADD", "register:40f0:8", ["const:b2be5c:8", "const:4:8"]]
+ 00b2be5c ["CALL", null, ["callee:00bdf4d0:8"]]
- 00b2be18 bytes 9acd0294
+ 00b2be5c bytes 9dcd0294
- 00b2be40 ["INT_ADD", "register:40f0:8", ["const:b2be40:8", "const:4:8"]]
- 00b2be40 ["CALL", null, ["callee:00bdf0a0:8"]]
+ 00b2be84 ["INT_ADD", "register:40f0:8", ["const:b2be84:8", "const:4:8"]]
+ 00b2be84 ["CALL", null, ["callee:00bdf0a0:8"]]
- 00b2be40 bytes 84cc0294
+ 00b2be84 bytes 87cc0294
- 00b2be58 ["INT_ADD", "register:40f0:8", ["const:b2be58:8", "const:4:8"]]
- 00b2be58 ["CALL", null, ["callee:00bdf4f0:8"]]
+ 00b2be9c ["INT_ADD", "register:40f0:8", ["const:b2be9c:8", "const:4:8"]]
+ 00b2be9c ["CALL", null, ["callee:00bdf4f0:8"]]
- 00b2be58 bytes 92cd0294
+ 00b2be9c bytes 95cd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3b67aa37fa73d524951b81355aa98fc"></a>

### [`00b2beac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2beac.md) → [`00b2bef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2bef0.md) _ZN11flatbuffers7EnumDef11DeserializeERNS_6ParserEPKN10reflection4EnumE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa10.md) · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdf100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf100.md)
- 新版 呼出元 1件 [`00bdfa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa60.md) · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdf150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2bf34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2beac.md#insn-00b2bf34) · [`00b2bf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2beac.md#insn-00b2bf54) · [`00b2bf68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2beac.md#insn-00b2bf68)
- 新版 `00b2bf78`（命令位置の公開資料なし） · `00b2bf98`（命令位置の公開資料なし） · `00b2bfac`（命令位置の公開資料なし）

~~~diff
- 00b2bf34 ["INT_ADD", "register:40f0:8", ["const:b2bf34:8", "const:4:8"]]
- 00b2bf34 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2bf78 ["INT_ADD", "register:40f0:8", ["const:b2bf78:8", "const:4:8"]]
+ 00b2bf78 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2bf34 bytes 2fbc0294
+ 00b2bf78 bytes 32bc0294
- 00b2bf54 ["INT_ADD", "register:40f0:8", ["const:b2bf54:8", "const:4:8"]]
- 00b2bf54 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b2bf98 ["INT_ADD", "register:40f0:8", ["const:b2bf98:8", "const:4:8"]]
+ 00b2bf98 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b2bf54 bytes 83bc0294
+ 00b2bf98 bytes 86bc0294
- 00b2bf68 ["INT_ADD", "register:40f0:8", ["const:b2bf68:8", "const:4:8"]]
- 00b2bf68 ["CALL", null, ["callee:00bdf8b0:8"]]
+ 00b2bfac ["INT_ADD", "register:40f0:8", ["const:b2bfac:8", "const:4:8"]]
+ 00b2bfac ["CALL", null, ["callee:00bdf8b0:8"]]
- 00b2bf68 bytes 3ece0294
+ 00b2bfac bytes 41ce0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38e198ce971fde8382f0c5e24c19056b"></a>

### [`00b2c204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c204.md) → [`00b2c248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c248.md) _ZN11flatbuffers7EnumVal11DeserializeERKNS_6ParserEPKN10reflection7EnumValE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa30.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdf260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf260.md) [`00bdf630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf630.md)
- 新版 呼出元 1件 [`00bdfa80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa80.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdf2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2b0.md) [`00bdf680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2c27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c204.md#insn-00b2c27c) · [`00b2c29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c204.md#insn-00b2c29c) · [`00b2c2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c204.md#insn-00b2c2cc)
- 新版 `00b2c2c0`（命令位置の公開資料なし） · `00b2c2e0`（命令位置の公開資料なし） · `00b2c310`（命令位置の公開資料なし）

~~~diff
- 00b2c27c ["INT_ADD", "register:40f0:8", ["const:b2c27c:8", "const:4:8"]]
- 00b2c27c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2c2c0 ["INT_ADD", "register:40f0:8", ["const:b2c2c0:8", "const:4:8"]]
+ 00b2c2c0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2c27c bytes 5dbb0294
+ 00b2c2c0 bytes 60bb0294
- 00b2c29c ["INT_ADD", "register:40f0:8", ["const:b2c29c:8", "const:4:8"]]
- 00b2c29c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b2c2e0 ["INT_ADD", "register:40f0:8", ["const:b2c2e0:8", "const:4:8"]]
+ 00b2c2e0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b2c29c bytes b1bb0294
+ 00b2c2e0 bytes b4bb0294
- 00b2c2cc ["INT_ADD", "register:40f0:8", ["const:b2c2cc:8", "const:4:8"]]
- 00b2c2cc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b2c310 ["INT_ADD", "register:40f0:8", ["const:b2c310:8", "const:4:8"]]
+ 00b2c310 ["CALL", null, ["callee:00bdb060:8"]]
- 00b2c2cc bytes 51bb0294
+ 00b2c310 bytes 54bb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bdd74724b0511f14d44891d01203a7f"></a>

### [`00b2c3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md) → [`00b2c3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c3f0.md) _ZN11flatbuffers11SymbolTableINS_7EnumValEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1f0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf240.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2c43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md#insn-00b2c43c) · [`00b2c448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md#insn-00b2c448) · [`00b2c470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md#insn-00b2c470)
- 新版 `00b2c480`（命令位置の公開資料なし） · `00b2c48c`（命令位置の公開資料なし） · `00b2c4b4`（命令位置の公開資料なし）

~~~diff
- 00b2c43c ["INT_ADD", "register:40f0:8", ["const:b2c43c:8", "const:4:8"]]
- 00b2c43c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b2c480 ["INT_ADD", "register:40f0:8", ["const:b2c480:8", "const:4:8"]]
+ 00b2c480 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b2c43c bytes 8dc70294
+ 00b2c480 bytes 90c70294
- 00b2c448 ["INT_ADD", "register:40f0:8", ["const:b2c448:8", "const:4:8"]]
- 00b2c448 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2c48c ["INT_ADD", "register:40f0:8", ["const:b2c48c:8", "const:4:8"]]
+ 00b2c48c ["CALL", null, ["callee:00bdb040:8"]]
- 00b2c448 bytes eaba0294
+ 00b2c48c bytes edba0294
- 00b2c470 ["INT_ADD", "register:40f0:8", ["const:b2c470:8", "const:4:8"]]
- 00b2c470 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b2c4b4 ["INT_ADD", "register:40f0:8", ["const:b2c4b4:8", "const:4:8"]]
+ 00b2c4b4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b2c470 bytes 3cbb0294
+ 00b2c4b4 bytes 3fbb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee8185cebd6e79f1ca200b4627747f4"></a>

### [`00b2c564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md) → [`00b2c5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c5a8.md) _ZN10reflection13CreateEnumValERN11flatbuffers17FlatBufferBuilderENS0_6OffsetINS0_6StringEEElNS3_INS_6ObjectEEENS3_INS_4TypeEEENS3_INS0_6Vec

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0e0.md) · 呼出先 7件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md) [`00bdf4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4c0.md) [`00bdf4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4d0.md) [`00bdf4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4e0.md)
- 新版 呼出元 1件 [`00bdf130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf130.md) · 呼出先 7件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf490.md) [`00bdf510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf510.md) [`00bdf520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf520.md) [`00bdf530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2c5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md#insn-00b2c5c0) · [`00b2c5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md#insn-00b2c5e0) · [`00b2c62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md#insn-00b2c62c)
- 新版 `00b2c604`（命令位置の公開資料なし） · `00b2c624`（命令位置の公開資料なし） · `00b2c670`（命令位置の公開資料なし）

~~~diff
- 00b2c5c0 ["INT_ADD", "register:40f0:8", ["const:b2c5c0:8", "const:4:8"]]
- 00b2c5c0 ["CALL", null, ["callee:00bdf490:8"]]
+ 00b2c604 ["INT_ADD", "register:40f0:8", ["const:b2c604:8", "const:4:8"]]
+ 00b2c604 ["CALL", null, ["callee:00bdf490:8"]]
- 00b2c5c0 bytes a0cb0294
+ 00b2c604 bytes a3cb0294
- 00b2c5e0 ["INT_ADD", "register:40f0:8", ["const:b2c5e0:8", "const:4:8"]]
- 00b2c5e0 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b2c624 ["INT_ADD", "register:40f0:8", ["const:b2c624:8", "const:4:8"]]
+ 00b2c624 ["CALL", null, ["callee:00bdf390:8"]]
- 00b2c5e0 bytes 58cb0294
+ 00b2c624 bytes 5bcb0294
- 00b2c62c ["INT_ADD", "register:40f0:8", ["const:b2c62c:8", "const:4:8"]]
- 00b2c62c ["CALL", null, ["callee:00bdf5c0:8"]]
+ 00b2c670 ["INT_ADD", "register:40f0:8", ["const:b2c670:8", "const:4:8"]]
+ 00b2c670 ["CALL", null, ["callee:00bdf5c0:8"]]
- 00b2c62c bytes d1cb0294
+ 00b2c670 bytes d4cb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a24e7dc699e5ad9d6f978a2db25c7ed"></a>

### [`00b2c688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c688.md) → [`00b2c6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c6cc.md) _ZN10reflection10CreateTypeERN11flatbuffers17FlatBufferBuilderENS_8BaseTypeES3_it

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf050.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf080.md) [`00bdf090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf090.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf370.md)
- 新版 呼出元 1件 [`00bdf0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0a0.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0d0.md) [`00bdf0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0e0.md) [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2c6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c688.md#insn-00b2c6f8) · [`00b2c718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c688.md#insn-00b2c718) · [`00b2c76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c688.md#insn-00b2c76c)
- 新版 `00b2c73c`（命令位置の公開資料なし） · `00b2c75c`（命令位置の公開資料なし） · `00b2c7b0`（命令位置の公開資料なし）

~~~diff
- 00b2c6f8 ["INT_ADD", "register:40f0:8", ["const:b2c6f8:8", "const:4:8"]]
- 00b2c6f8 ["CALL", null, ["callee:00bdf470:8"]]
+ 00b2c73c ["INT_ADD", "register:40f0:8", ["const:b2c73c:8", "const:4:8"]]
+ 00b2c73c ["CALL", null, ["callee:00bdf470:8"]]
- 00b2c6f8 bytes 4acb0294
+ 00b2c73c bytes 4dcb0294
- 00b2c718 ["INT_ADD", "register:40f0:8", ["const:b2c718:8", "const:4:8"]]
- 00b2c718 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b2c75c ["INT_ADD", "register:40f0:8", ["const:b2c75c:8", "const:4:8"]]
+ 00b2c75c ["CALL", null, ["callee:00bdf390:8"]]
- 00b2c718 bytes 0acb0294
+ 00b2c75c bytes 0dcb0294
- 00b2c76c ["INT_ADD", "register:40f0:8", ["const:b2c76c:8", "const:4:8"]]
- 00b2c76c ["CALL", null, ["callee:00bdf3c0:8"]]
+ 00b2c7b0 ["INT_ADD", "register:40f0:8", ["const:b2c7b0:8", "const:4:8"]]
+ 00b2c7b0 ["CALL", null, ["callee:00bdf3c0:8"]]
- 00b2c76c bytes 01cb0294
+ 00b2c7b0 bytes 04cb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c8151810c34300bc9f89ac19e6df2ce"></a>

### [`00b2c9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c9dc.md) → [`00b2ca20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2ca20.md) _ZN11flatbuffers6Parser11DeserializeEPKN10reflection6SchemaE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf730.md) · 呼出先 19件 [`00b2d8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2d8bc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf780.md) · 呼出先 19件 [`00b2d900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2d/00b2d900.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2caa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c9dc.md#insn-00b2caa8) · [`00b2cb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c9dc.md#insn-00b2cb54) · [`00b2cc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c9dc.md#insn-00b2cc00)
- 新版 `00b2caec`（命令位置の公開資料なし） · `00b2cb98`（命令位置の公開資料なし） · `00b2cc44`（命令位置の公開資料なし）

~~~diff
- 00b2caa8 ["INT_ADD", "register:40f0:8", ["const:b2caa8:8", "const:4:8"]]
- 00b2caa8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b2caec ["INT_ADD", "register:40f0:8", ["const:b2caec:8", "const:4:8"]]
+ 00b2caec ["CALL", null, ["callee:00bdb060:8"]]
- 00b2caa8 bytes 5ab90294
+ 00b2caec bytes 5db90294
- 00b2cb54 ["INT_ADD", "register:40f0:8", ["const:b2cb54:8", "const:4:8"]]
- 00b2cb54 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b2cb98 ["INT_ADD", "register:40f0:8", ["const:b2cb98:8", "const:4:8"]]
+ 00b2cb98 ["CALL", null, ["callee:00bdb060:8"]]
- 00b2cb54 bytes 2fb90294
+ 00b2cb98 bytes 32b90294
- 00b2cc00 ["INT_ADD", "register:40f0:8", ["const:b2cc00:8", "const:4:8"]]
- 00b2cc00 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2cc44 ["INT_ADD", "register:40f0:8", ["const:b2cc44:8", "const:4:8"]]
+ 00b2cc44 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2cc00 bytes fcb80294
+ 00b2cc44 bytes ffb80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84c8f1df95777a7dbb34e5f8e771f18a"></a>

### [`00b2d8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2d8bc.md) → [`00b2d900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2d/00b2d900.md) FUN_00b2d900

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2c9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c9dc.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00b2ca20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2ca20.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2d8bc.md#insn-00b2d984) · [`00b2d9a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2d8bc.md#insn-00b2d9a4) · [`00b2da0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2d8bc.md#insn-00b2da0c)
- 新版 `00b2d9c8`（命令位置の公開資料なし） · `00b2d9e8`（命令位置の公開資料なし） · `00b2da50`（命令位置の公開資料なし）

~~~diff
- 00b2d984 ["INT_ADD", "register:40f0:8", ["const:b2d984:8", "const:4:8"]]
- 00b2d984 ["CALL", null, ["callee:00bdfff0:8"]]
+ 00b2d9c8 ["INT_ADD", "register:40f0:8", ["const:b2d9c8:8", "const:4:8"]]
+ 00b2d9c8 ["CALL", null, ["callee:00bdfff0:8"]]
- 00b2d984 bytes 87c90294
+ 00b2d9c8 bytes 8ac90294
- 00b2d9a4 ["INT_ADD", "register:40f0:8", ["const:b2d9a4:8", "const:4:8"]]
- 00b2d9a4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2d9e8 ["INT_ADD", "register:40f0:8", ["const:b2d9e8:8", "const:4:8"]]
+ 00b2d9e8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2d9a4 bytes 93b50294
+ 00b2d9e8 bytes 96b50294
- 00b2da0c ["INT_ADD", "register:40f0:8", ["const:b2da0c:8", "const:4:8"]]
- 00b2da0c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2da50 ["INT_ADD", "register:40f0:8", ["const:b2da50:8", "const:4:8"]]
+ 00b2da50 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2da0c bytes 79b50294
+ 00b2da50 bytes 7cb50294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855885958f0664dde24967343be36437"></a>

### [`00b2dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dff0.md) → [`00b2e034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e034.md) _ZN11flatbuffers11EqualByNameERKNS_4TypeES2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf140.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdf190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf190.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2e0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dff0.md#insn-00b2e0b0) · [`00b2e158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dff0.md#insn-00b2e158)
- 新版 `00b2e0f4`（命令位置の公開資料なし） · `00b2e19c`（命令位置の公開資料なし）

~~~diff
- 00b2e0b0 ["INT_ADD", "register:40f0:8", ["const:b2e0b0:8", "const:4:8"]]
- 00b2e0b0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b2e0f4 ["INT_ADD", "register:40f0:8", ["const:b2e0f4:8", "const:4:8"]]
+ 00b2e0f4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b2e0b0 bytes 40b40294
+ 00b2e0f4 bytes 43b40294
- 00b2e158 ["INT_ADD", "register:40f0:8", ["const:b2e158:8", "const:4:8"]]
- 00b2e158 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b2e19c ["INT_ADD", "register:40f0:8", ["const:b2e19c:8", "const:4:8"]]
+ 00b2e19c ["CALL", null, ["callee:00bdb200:8"]]
- 00b2e158 bytes 16b40294
+ 00b2e19c bytes 19b40294
~~~


<a id="compare-b6eaf3ac507df959e15a345bc9c1fb46"></a>

### [`00b2e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e170.md) → [`00b2e1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e1b4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) · 呼出先 2件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)
- 新版 呼出元 1件 [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) · 呼出先 2件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e170.md#insn-00b2e1dc) · [`00b2e200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e170.md#insn-00b2e200)
- 新版 `00b2e220`（命令位置の公開資料なし） · `00b2e244`（命令位置の公開資料なし）

~~~diff
- 00b2e1dc ["INT_ADD", "register:40f0:8", ["const:b2e1dc:8", "const:4:8"]]
- 00b2e1dc ["CALL", null, ["callee:00bdda90:8"]]
+ 00b2e220 ["INT_ADD", "register:40f0:8", ["const:b2e220:8", "const:4:8"]]
+ 00b2e220 ["CALL", null, ["callee:00bdda90:8"]]
- 00b2e1dc bytes 19be0294
+ 00b2e220 bytes 1cbe0294
- 00b2e200 ["INT_ADD", "register:40f0:8", ["const:b2e200:8", "const:4:8"]]
- 00b2e200 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b2e244 ["INT_ADD", "register:40f0:8", ["const:b2e244:8", "const:4:8"]]
+ 00b2e244 ["CALL", null, ["callee:00bdb240:8"]]
- 00b2e200 bytes fcb30294
+ 00b2e244 bytes ffb30294
~~~


<a id="compare-ef4141c2882dec8233ab81c766223d82"></a>

### [`00b2e23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e23c.md) → [`00b2e280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e280.md) _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5a0.md) · 呼出先 2件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be0200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0200.md)
- 新版 呼出元 1件 [`00bdf5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md) · 呼出先 2件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be0250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2e26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e23c.md#insn-00b2e26c) · [`00b2e2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e23c.md#insn-00b2e2cc) · [`00b2e2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e23c.md#insn-00b2e2e4)
- 新版 `00b2e2b0`（命令位置の公開資料なし） · `00b2e310`（命令位置の公開資料なし） · `00b2e328`（命令位置の公開資料なし）

~~~diff
- 00b2e26c ["INT_ADD", "register:40f0:8", ["const:b2e26c:8", "const:4:8"]]
- 00b2e26c ["CALL", null, ["callee:00bdb270:8"]]
+ 00b2e2b0 ["INT_ADD", "register:40f0:8", ["const:b2e2b0:8", "const:4:8"]]
+ 00b2e2b0 ["CALL", null, ["callee:00bdb270:8"]]
- 00b2e26c bytes edb30294
+ 00b2e2b0 bytes f0b30294
- 00b2e2cc ["INT_ADD", "register:40f0:8", ["const:b2e2cc:8", "const:4:8"]]
- 00b2e2cc ["CALL", null, ["callee:00bdb270:8"]]
+ 00b2e310 ["INT_ADD", "register:40f0:8", ["const:b2e310:8", "const:4:8"]]
+ 00b2e310 ["CALL", null, ["callee:00bdb270:8"]]
- 00b2e2cc bytes d5b30294
+ 00b2e310 bytes d8b30294
- 00b2e2e4 ["INT_ADD", "register:40f0:8", ["const:b2e2e4:8", "const:4:8"]]
- 00b2e2e4 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b2e328 ["INT_ADD", "register:40f0:8", ["const:b2e328:8", "const:4:8"]]
+ 00b2e328 ["CALL", null, ["callee:00bdb270:8"]]
- 00b2e2e4 bytes cfb30294
+ 00b2e328 bytes d2b30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46b7ee5914c6d9f8bf30a0c47678e725"></a>

### [`00b2e4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e4b4.md) → [`00b2e4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e4f8.md) _ZN11flatbuffers17FlatBufferBuilder12CreateStringEPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md) · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4d0.md) · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2e51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e4b4.md#insn-00b2e51c) · [`00b2e574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e4b4.md#insn-00b2e574) · [`00b2e5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e4b4.md#insn-00b2e5a4)
- 新版 `00b2e560`（命令位置の公開資料なし） · `00b2e5b8`（命令位置の公開資料なし） · `00b2e5e8`（命令位置の公開資料なし）

~~~diff
- 00b2e51c ["INT_ADD", "register:40f0:8", ["const:b2e51c:8", "const:4:8"]]
- 00b2e51c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b2e560 ["INT_ADD", "register:40f0:8", ["const:b2e560:8", "const:4:8"]]
+ 00b2e560 ["CALL", null, ["callee:00bdf390:8"]]
- 00b2e51c bytes 89c30294
+ 00b2e560 bytes 8cc30294
- 00b2e574 ["INT_ADD", "register:40f0:8", ["const:b2e574:8", "const:4:8"]]
- 00b2e574 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b2e5b8 ["INT_ADD", "register:40f0:8", ["const:b2e5b8:8", "const:4:8"]]
+ 00b2e5b8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b2e574 bytes 73c30294
+ 00b2e5b8 bytes 76c30294
- 00b2e5a4 ["INT_ADD", "register:40f0:8", ["const:b2e5a4:8", "const:4:8"]]
- 00b2e5a4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b2e5e8 ["INT_ADD", "register:40f0:8", ["const:b2e5e8:8", "const:4:8"]]
+ 00b2e5e8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b2e5a4 bytes 67c30294
+ 00b2e5e8 bytes 6ac30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4720a2bf98df6c194a0484f18dd1f7d"></a>

### [`00b2e5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e5f0.md) → [`00b2e634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e634.md) _ZN11flatbuffers15vector_downward10reallocateEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00bdef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md)
- 新版 呼出元 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00bdefa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2e68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e5f0.md#insn-00b2e68c) · [`00b2e6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e5f0.md#insn-00b2e6a4) · [`00b2e6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e5f0.md#insn-00b2e6b0)
- 新版 `00b2e6d0`（命令位置の公開資料なし） · `00b2e6e8`（命令位置の公開資料なし） · `00b2e6f4`（命令位置の公開資料なし）

~~~diff
- 00b2e68c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2e68c ["INT_ADD", "register:40f0:8", ["const:b2e68c:8", "const:4:8"]]
- 00b2e68c ["CALLIND", null, ["register:0:8"]]
+ 00b2e6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2e6d0 ["INT_ADD", "register:40f0:8", ["const:b2e6d0:8", "const:4:8"]]
+ 00b2e6d0 ["CALLIND", null, ["register:0:8"]]
- 00b2e68c bytes 00013fd6
+ 00b2e6d0 bytes 00013fd6
- 00b2e6a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2e6a4 ["INT_ADD", "register:40f0:8", ["const:b2e6a4:8", "const:4:8"]]
- 00b2e6a4 ["CALLIND", null, ["register:0:8"]]
+ 00b2e6e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2e6e8 ["INT_ADD", "register:40f0:8", ["const:b2e6e8:8", "const:4:8"]]
+ 00b2e6e8 ["CALLIND", null, ["register:0:8"]]
- 00b2e6a4 bytes 00013fd6
+ 00b2e6e8 bytes 00013fd6
- 00b2e6b0 ["INT_ADD", "register:40f0:8", ["const:b2e6b0:8", "const:4:8"]]
- 00b2e6b0 ["CALL", null, ["callee:00bdefa0:8"]]
+ 00b2e6f4 ["INT_ADD", "register:40f0:8", ["const:b2e6f4:8", "const:4:8"]]
+ 00b2e6f4 ["CALL", null, ["callee:00bdefa0:8"]]
- 00b2e6b0 bytes 28c20294
+ 00b2e6f4 bytes 2bc20294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-851713464b9cc724bc718aedcbdc2687"></a>

### [`00b2e72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e72c.md) → [`00b2e770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e770.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff10.md) · 呼出先 5件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bdeb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb60.md) [`00bdff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff20.md)
- 新版 呼出元 1件 [`00bdff60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff60.md) · 呼出先 5件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bdebb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebb0.md) [`00bdff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2e828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e72c.md#insn-00b2e828) · [`00b2e8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e72c.md#insn-00b2e8a4) · [`00b2e914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e72c.md#insn-00b2e914)
- 新版 `00b2e86c`（命令位置の公開資料なし） · `00b2e8e8`（命令位置の公開資料なし） · `00b2e958`（命令位置の公開資料なし）

~~~diff
- 00b2e828 ["INT_ADD", "register:40f0:8", ["const:b2e828:8", "const:4:8"]]
- 00b2e828 ["CALL", null, ["callee:00bde230:8"]]
+ 00b2e86c ["INT_ADD", "register:40f0:8", ["const:b2e86c:8", "const:4:8"]]
+ 00b2e86c ["CALL", null, ["callee:00bde230:8"]]
- 00b2e828 bytes 6ebe0294
+ 00b2e86c bytes 71be0294
- 00b2e8a4 ["INT_ADD", "register:40f0:8", ["const:b2e8a4:8", "const:4:8"]]
- 00b2e8a4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b2e8e8 ["INT_ADD", "register:40f0:8", ["const:b2e8e8:8", "const:4:8"]]
+ 00b2e8e8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b2e8a4 bytes 43b20294
+ 00b2e8e8 bytes 46b20294
- 00b2e914 ["INT_ADD", "register:40f0:8", ["const:b2e914:8", "const:4:8"]]
- 00b2e914 ["CALL", null, ["callee:00bde760:8"]]
+ 00b2e958 ["INT_ADD", "register:40f0:8", ["const:b2e958:8", "const:4:8"]]
+ 00b2e958 ["CALL", null, ["callee:00bde760:8"]]
- 00b2e914 bytes 7fbf0294
+ 00b2e958 bytes 82bf0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d69bf730f29b4f01433bbffc148a448a"></a>

### [`00b2eab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2eab8.md) → [`00b2eafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2eafc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff20.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)
- 新版 呼出元 1件 [`00bdff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff70.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ead8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2eab8.md#insn-00b2ead8) · [`00b2eae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2eab8.md#insn-00b2eae8) · [`00b2eb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2eab8.md#insn-00b2eb60)
- 新版 `00b2eb1c`（命令位置の公開資料なし） · `00b2eb2c`（命令位置の公開資料なし） · `00b2eba4`（命令位置の公開資料なし）

~~~diff
- 00b2ead8 ["INT_ADD", "register:40f0:8", ["const:b2ead8:8", "const:4:8"]]
- 00b2ead8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2eb1c ["INT_ADD", "register:40f0:8", ["const:b2eb1c:8", "const:4:8"]]
+ 00b2eb1c ["CALL", null, ["callee:00bdb040:8"]]
- 00b2ead8 bytes 46b10294
+ 00b2eb1c bytes 49b10294
- 00b2eae8 ["INT_ADD", "register:40f0:8", ["const:b2eae8:8", "const:4:8"]]
- 00b2eae8 ["CALL", null, ["callee:00bde730:8"]]
+ 00b2eb2c ["INT_ADD", "register:40f0:8", ["const:b2eb2c:8", "const:4:8"]]
+ 00b2eb2c ["CALL", null, ["callee:00bde730:8"]]
- 00b2eae8 bytes febe0294
+ 00b2eb2c bytes 01bf0294
- 00b2eb60 ["INT_ADD", "register:40f0:8", ["const:b2eb60:8", "const:4:8"]]
- 00b2eb60 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b2eba4 ["INT_ADD", "register:40f0:8", ["const:b2eba4:8", "const:4:8"]]
+ 00b2eba4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b2eb60 bytes 94b10294
+ 00b2eba4 bytes 97b10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab1b513b9dad517c11e004bfe18bd671"></a>

### [`00b2ebec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ebec.md) → [`00b2ec30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ec30.md) _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_co

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0070.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00be00c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00c0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ec34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ebec.md#insn-00b2ec34) · [`00b2ec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ebec.md#insn-00b2ec70) · [`00b2eca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ebec.md#insn-00b2eca4)
- 新版 `00b2ec78`（命令位置の公開資料なし） · `00b2ecb4`（命令位置の公開資料なし） · `00b2ece8`（命令位置の公開資料なし）

~~~diff
- 00b2ec34 ["INT_ADD", "register:40f0:8", ["const:b2ec34:8", "const:4:8"]]
- 00b2ec34 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b2ec78 ["INT_ADD", "register:40f0:8", ["const:b2ec78:8", "const:4:8"]]
+ 00b2ec78 ["CALL", null, ["callee:00bdb060:8"]]
- 00b2ec34 bytes f7b00294
+ 00b2ec78 bytes fab00294
- 00b2ec70 ["INT_ADD", "register:40f0:8", ["const:b2ec70:8", "const:4:8"]]
- 00b2ec70 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b2ecb4 ["INT_ADD", "register:40f0:8", ["const:b2ecb4:8", "const:4:8"]]
+ 00b2ecb4 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b2ec70 bytes 80bd0294
+ 00b2ecb4 bytes 83bd0294
- 00b2eca4 ["INT_ADD", "register:40f0:8", ["const:b2eca4:8", "const:4:8"]]
- 00b2eca4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b2ece8 ["INT_ADD", "register:40f0:8", ["const:b2ece8:8", "const:4:8"]]
+ 00b2ece8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b2eca4 bytes ffb00294
+ 00b2ece8 bytes 02b10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b71d25301271ddca848aed797747d090"></a>

### [`00b2ed44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ed44.md) → [`00b2ed88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ed88.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc60.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcb0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2eddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ed44.md#insn-00b2eddc) · [`00b2ee24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ed44.md#insn-00b2ee24)
- 新版 `00b2ee20`（命令位置の公開資料なし） · `00b2ee68`（命令位置の公開資料なし）

~~~diff
- 00b2eddc ["INT_ADD", "register:40f0:8", ["const:b2eddc:8", "const:4:8"]]
- 00b2eddc ["CALL", null, ["callee:00bdb200:8"]]
+ 00b2ee20 ["INT_ADD", "register:40f0:8", ["const:b2ee20:8", "const:4:8"]]
+ 00b2ee20 ["CALL", null, ["callee:00bdb200:8"]]
- 00b2eddc bytes f5b00294
+ 00b2ee20 bytes f8b00294
- 00b2ee24 ["INT_ADD", "register:40f0:8", ["const:b2ee24:8", "const:4:8"]]
- 00b2ee24 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b2ee68 ["INT_ADD", "register:40f0:8", ["const:b2ee68:8", "const:4:8"]]
+ 00b2ee68 ["CALL", null, ["callee:00bdb200:8"]]
- 00b2ee24 bytes e3b00294
+ 00b2ee68 bytes e6b00294
~~~


<a id="compare-5fa6ac1d92853d0738de15bc03223a99"></a>

### [`00b2ee58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md) → [`00b2ee9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ee9c.md) _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf590.md) · 呼出先 2件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb700.md)
- 新版 呼出元 1件 [`00bdf5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5e0.md) · 呼出先 2件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ee88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md#insn-00b2ee88) · [`00b2eee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md#insn-00b2eee8) · [`00b2ef00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md#insn-00b2ef00)
- 新版 `00b2eecc`（命令位置の公開資料なし） · `00b2ef2c`（命令位置の公開資料なし） · `00b2ef44`（命令位置の公開資料なし）

~~~diff
- 00b2ee88 ["INT_ADD", "register:40f0:8", ["const:b2ee88:8", "const:4:8"]]
- 00b2ee88 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b2eecc ["INT_ADD", "register:40f0:8", ["const:b2eecc:8", "const:4:8"]]
+ 00b2eecc ["CALL", null, ["callee:00bdb270:8"]]
- 00b2ee88 bytes e6b00294
+ 00b2eecc bytes e9b00294
- 00b2eee8 ["INT_ADD", "register:40f0:8", ["const:b2eee8:8", "const:4:8"]]
- 00b2eee8 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b2ef2c ["INT_ADD", "register:40f0:8", ["const:b2ef2c:8", "const:4:8"]]
+ 00b2ef2c ["CALL", null, ["callee:00bdb270:8"]]
- 00b2eee8 bytes ceb00294
+ 00b2ef2c bytes d1b00294
- 00b2ef00 ["INT_ADD", "register:40f0:8", ["const:b2ef00:8", "const:4:8"]]
- 00b2ef00 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b2ef44 ["INT_ADD", "register:40f0:8", ["const:b2ef44:8", "const:4:8"]]
+ 00b2ef44 ["CALL", null, ["callee:00bdb270:8"]]
- 00b2ef00 bytes c8b00294
+ 00b2ef44 bytes cbb00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0cd90339fb8f680101abc251cd92002"></a>

### [`00b31420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31420.md) → [`00b31464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31464.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31420.md#insn-00b31434)
- 新版 `00b31478`（命令位置の公開資料なし）

~~~diff
- 00b31434 ["INT_ADD", "register:40f0:8", ["const:b31434:8", "const:4:8"]]
- 00b31434 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b31478 ["INT_ADD", "register:40f0:8", ["const:b31478:8", "const:4:8"]]
+ 00b31478 ["CALL", null, ["callee:00be01e0:8"]]
- 00b31434 bytes 57bb0294
+ 00b31478 bytes 5abb0294
~~~


<a id="compare-b525d005cf5cb178c741795132404726"></a>

### [`00b3145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3145c.md) → [`00b314a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314a0.md) _ZTv0_n24_NSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3145c.md#insn-00b31478)
- 新版 `00b314bc`（命令位置の公開資料なし）

~~~diff
- 00b31478 ["INT_ADD", "register:40f0:8", ["const:b31478:8", "const:4:8"]]
- 00b31478 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b314bc ["INT_ADD", "register:40f0:8", ["const:b314bc:8", "const:4:8"]]
+ 00b314bc ["CALL", null, ["callee:00be01e0:8"]]
- 00b31478 bytes 46bb0294
+ 00b314bc bytes 49bb0294
~~~


<a id="compare-b7e36acee4e2b7a3189d2cba6139700d"></a>

### [`00b318dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b318dc.md) → [`00b31920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31920.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsgetnEPcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3195c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b318dc.md#insn-00b3195c) · [`00b31970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b318dc.md#insn-00b31970)
- 新版 `00b319a0`（命令位置の公開資料なし） · `00b319b4`（命令位置の公開資料なし）

~~~diff
- 00b3195c ["INT_ADD", "register:40f0:8", ["const:b3195c:8", "const:4:8"]]
- 00b3195c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b319a0 ["INT_ADD", "register:40f0:8", ["const:b319a0:8", "const:4:8"]]
+ 00b319a0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3195c bytes 01a60294
+ 00b319a0 bytes 04a60294
- 00b31970 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31970 ["INT_ADD", "register:40f0:8", ["const:b31970:8", "const:4:8"]]
- 00b31970 ["CALLIND", null, ["register:0:8"]]
+ 00b319b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b319b4 ["INT_ADD", "register:40f0:8", ["const:b319b4:8", "const:4:8"]]
+ 00b319b4 ["CALLIND", null, ["register:0:8"]]
- 00b31970 bytes 00013fd6
+ 00b319b4 bytes 00013fd6
~~~


<a id="compare-72ba1b08a19f2d66b6353484b9145a9c"></a>

### [`00b319f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b319f4.md) → [`00b31a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31a38.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5uflowEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b319f4.md#insn-00b31a0c)
- 新版 `00b31a50`（命令位置の公開資料なし）

~~~diff
- 00b31a0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31a0c ["INT_ADD", "register:40f0:8", ["const:b31a0c:8", "const:4:8"]]
- 00b31a0c ["CALLIND", null, ["register:0:8"]]
+ 00b31a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b31a50 ["INT_ADD", "register:40f0:8", ["const:b31a50:8", "const:4:8"]]
+ 00b31a50 ["CALLIND", null, ["register:0:8"]]
- 00b31a0c bytes 00013fd6
+ 00b31a50 bytes 00013fd6
~~~


<a id="compare-715d3c7e91b39672cb54f83d46976226"></a>

### [`00b31aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31aa4.md) → [`00b31ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31ae8.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsputnEPKcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31aa4.md#insn-00b31b18) · [`00b31b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31aa4.md#insn-00b31b30)
- 新版 `00b31b5c`（命令位置の公開資料なし） · `00b31b74`（命令位置の公開資料なし）

~~~diff
- 00b31b18 ["INT_ADD", "register:40f0:8", ["const:b31b18:8", "const:4:8"]]
- 00b31b18 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b31b5c ["INT_ADD", "register:40f0:8", ["const:b31b5c:8", "const:4:8"]]
+ 00b31b5c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b31b18 bytes 92a50294
+ 00b31b5c bytes 95a50294
- 00b31b30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31b30 ["INT_ADD", "register:40f0:8", ["const:b31b30:8", "const:4:8"]]
- 00b31b30 ["CALLIND", null, ["register:0:8"]]
+ 00b31b74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b31b74 ["INT_ADD", "register:40f0:8", ["const:b31b74:8", "const:4:8"]]
+ 00b31b74 ["CALLIND", null, ["register:0:8"]]
- 00b31b30 bytes 00013fd6
+ 00b31b74 bytes 00013fd6
~~~


<a id="compare-ee56ca38e486c5b656125c779cd94bdd"></a>

### [`00b31b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31b6c.md) → [`00b31bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31bb0.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE8overflowEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31b6c.md#insn-00b31c1c) · [`00b31c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31b6c.md#insn-00b31c98)
- 新版 `00b31c60`（命令位置の公開資料なし） · `00b31cdc`（命令位置の公開資料なし）

~~~diff
- 00b31c1c ["INT_ADD", "register:40f0:8", ["const:b31c1c:8", "const:4:8"]]
- 00b31c1c ["CALL", null, ["callee:00bdda90:8"]]
+ 00b31c60 ["INT_ADD", "register:40f0:8", ["const:b31c60:8", "const:4:8"]]
+ 00b31c60 ["CALL", null, ["callee:00bdda90:8"]]
- 00b31c1c bytes 89af0294
+ 00b31c60 bytes 8caf0294
- 00b31c98 ["INT_ADD", "register:40f0:8", ["const:b31c98:8", "const:4:8"]]
- 00b31c98 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b31cdc ["INT_ADD", "register:40f0:8", ["const:b31cdc:8", "const:4:8"]]
+ 00b31cdc ["CALL", null, ["callee:00bdefc0:8"]]
- 00b31c98 bytes b6b40294
+ 00b31cdc bytes b9b40294
~~~


<a id="compare-38964cff720a03e1cf81e1cb7b24bd73"></a>

### [`00b31e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31e08.md) → [`00b31e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31e4c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md) · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)
- 新版 呼出元 1件 [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md) · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31e08.md#insn-00b31e40) · [`00b31e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31e08.md#insn-00b31e5c) · [`00b31e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31e08.md#insn-00b31e7c)
- 新版 `00b31e84`（命令位置の公開資料なし） · `00b31ea0`（命令位置の公開資料なし） · `00b31ec0`（命令位置の公開資料なし）

~~~diff
- 00b31e40 ["INT_ADD", "register:40f0:8", ["const:b31e40:8", "const:4:8"]]
- 00b31e40 ["CALL", null, ["callee:00bdc0a0:8"]]
+ 00b31e84 ["INT_ADD", "register:40f0:8", ["const:b31e84:8", "const:4:8"]]
+ 00b31e84 ["CALL", null, ["callee:00bdc0a0:8"]]
- 00b31e40 bytes 84a80294
+ 00b31e84 bytes 87a80294
- 00b31e5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31e5c ["INT_ADD", "register:40f0:8", ["const:b31e5c:8", "const:4:8"]]
- 00b31e5c ["CALLIND", null, ["register:0:8"]]
+ 00b31ea0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b31ea0 ["INT_ADD", "register:40f0:8", ["const:b31ea0:8", "const:4:8"]]
+ 00b31ea0 ["CALLIND", null, ["register:0:8"]]
- 00b31e5c bytes 00013fd6
+ 00b31ea0 bytes 00013fd6
- 00b31e7c ["INT_ADD", "register:40f0:8", ["const:b31e7c:8", "const:4:8"]]
- 00b31e7c ["CALL", null, ["callee:00bdb450:8"]]
+ 00b31ec0 ["INT_ADD", "register:40f0:8", ["const:b31ec0:8", "const:4:8"]]
+ 00b31ec0 ["CALL", null, ["callee:00bdb450:8"]]
- 00b31e7c bytes 61a50294
+ 00b31ec0 bytes 64a50294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66147f82bbf9cb6ecaea23acf065a0f2"></a>

### [`00b31ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31ef8.md) → [`00b31f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31f3c.md) _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31ef8.md#insn-00b31fd0) · [`00b32018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31ef8.md#insn-00b32018) · [`00b32100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31ef8.md#insn-00b32100)
- 新版 `00b32014`（命令位置の公開資料なし） · `00b3205c`（命令位置の公開資料なし） · `00b32144`（命令位置の公開資料なし）

~~~diff
- 00b31fd0 ["INT_ADD", "register:40f0:8", ["const:b31fd0:8", "const:4:8"]]
- 00b31fd0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b32014 ["INT_ADD", "register:40f0:8", ["const:b32014:8", "const:4:8"]]
+ 00b32014 ["CALL", null, ["callee:00bdb040:8"]]
- 00b31fd0 bytes 08a40294
+ 00b32014 bytes 0ba40294
- 00b32018 ["INT_ADD", "register:40f0:8", ["const:b32018:8", "const:4:8"]]
- 00b32018 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b3205c ["INT_ADD", "register:40f0:8", ["const:b3205c:8", "const:4:8"]]
+ 00b3205c ["CALL", null, ["callee:00bdb040:8"]]
- 00b32018 bytes f6a30294
+ 00b3205c bytes f9a30294
- 00b32100 ["INT_ADD", "register:40f0:8", ["const:b32100:8", "const:4:8"]]
- 00b32100 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b32144 ["INT_ADD", "register:40f0:8", ["const:b32144:8", "const:4:8"]]
+ 00b32144 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b32100 bytes 5cb00294
+ 00b32144 bytes 5fb00294
~~~


<a id="compare-735c86dee51a3186b941a99b1b1f3fbd"></a>

### [`00b32ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32ae0.md) → [`00b32b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32b24.md) _ZNSt6__ndk17__sort3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEjT0_S9_S9_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be00f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00f0.md) · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 1件 [`00be0140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0140.md) · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b32b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32ae0.md#insn-00b32b30) · [`00b32b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32ae0.md#insn-00b32b44) · [`00b32bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32ae0.md#insn-00b32bac)
- 新版 `00b32b74`（命令位置の公開資料なし） · `00b32b88`（命令位置の公開資料なし） · `00b32bf0`（命令位置の公開資料なし）

~~~diff
- 00b32b30 ["INT_ADD", "register:40f0:8", ["const:b32b30:8", "const:4:8"]]
- 00b32b30 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32b74 ["INT_ADD", "register:40f0:8", ["const:b32b74:8", "const:4:8"]]
+ 00b32b74 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32b30 bytes 94af0294
+ 00b32b74 bytes 97af0294
- 00b32b44 ["INT_ADD", "register:40f0:8", ["const:b32b44:8", "const:4:8"]]
- 00b32b44 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32b88 ["INT_ADD", "register:40f0:8", ["const:b32b88:8", "const:4:8"]]
+ 00b32b88 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32b44 bytes 8faf0294
+ 00b32b88 bytes 92af0294
- 00b32bac ["INT_ADD", "register:40f0:8", ["const:b32bac:8", "const:4:8"]]
- 00b32bac ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32bf0 ["INT_ADD", "register:40f0:8", ["const:b32bf0:8", "const:4:8"]]
+ 00b32bf0 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32bac bytes 75af0294
+ 00b32bf0 bytes 78af0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f826275fc893e8ed60a3b663026da90f"></a>

### [`00b32c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32c58.md) → [`00b32c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32c9c.md) _ZNSt6__ndk17__sort4IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEjT0_S9_S9_S9_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0180.md) · 呼出先 2件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00be00f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00f0.md)
- 新版 呼出元 1件 [`00be01d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01d0.md) · 呼出先 2件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00be0140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b32c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32c58.md#insn-00b32c88) · [`00b32cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32c58.md#insn-00b32cb0) · [`00b32cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32c58.md#insn-00b32cf0)
- 新版 `00b32ccc`（命令位置の公開資料なし） · `00b32cf4`（命令位置の公開資料なし） · `00b32d34`（命令位置の公開資料なし）

~~~diff
- 00b32c88 ["INT_ADD", "register:40f0:8", ["const:b32c88:8", "const:4:8"]]
- 00b32c88 ["CALL", null, ["callee:00be0140:8"]]
+ 00b32ccc ["INT_ADD", "register:40f0:8", ["const:b32ccc:8", "const:4:8"]]
+ 00b32ccc ["CALL", null, ["callee:00be0140:8"]]
- 00b32c88 bytes 1ab50294
+ 00b32ccc bytes 1db50294
- 00b32cb0 ["INT_ADD", "register:40f0:8", ["const:b32cb0:8", "const:4:8"]]
- 00b32cb0 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32cf4 ["INT_ADD", "register:40f0:8", ["const:b32cf4:8", "const:4:8"]]
+ 00b32cf4 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32cb0 bytes 34af0294
+ 00b32cf4 bytes 37af0294
- 00b32cf0 ["INT_ADD", "register:40f0:8", ["const:b32cf0:8", "const:4:8"]]
- 00b32cf0 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32d34 ["INT_ADD", "register:40f0:8", ["const:b32d34:8", "const:4:8"]]
+ 00b32d34 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32cf0 bytes 24af0294
+ 00b32d34 bytes 27af0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1c499005de36187ca42495f174f41be"></a>

### [`00b32d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32d80.md) → [`00b32dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32dc4.md) FUN_00b32dc4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b32634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32634.md) [`00b3303c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b3303c.md) · 呼出先 2件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00be0180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0180.md)
- 新版 呼出元 2件 [`00b32678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32678.md) [`00b33080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33080.md) · 呼出先 2件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00be01d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b32db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32d80.md#insn-00b32db8) · [`00b32de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32d80.md#insn-00b32de0) · [`00b32e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32d80.md#insn-00b32e20)
- 新版 `00b32dfc`（命令位置の公開資料なし） · `00b32e24`（命令位置の公開資料なし） · `00b32e64`（命令位置の公開資料なし）

~~~diff
- 00b32db8 ["INT_ADD", "register:40f0:8", ["const:b32db8:8", "const:4:8"]]
- 00b32db8 ["CALL", null, ["callee:00be01d0:8"]]
+ 00b32dfc ["INT_ADD", "register:40f0:8", ["const:b32dfc:8", "const:4:8"]]
+ 00b32dfc ["CALL", null, ["callee:00be01d0:8"]]
- 00b32db8 bytes f2b40294
+ 00b32dfc bytes f5b40294
- 00b32de0 ["INT_ADD", "register:40f0:8", ["const:b32de0:8", "const:4:8"]]
- 00b32de0 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32e24 ["INT_ADD", "register:40f0:8", ["const:b32e24:8", "const:4:8"]]
+ 00b32e24 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32de0 bytes e8ae0294
+ 00b32e24 bytes ebae0294
- 00b32e20 ["INT_ADD", "register:40f0:8", ["const:b32e20:8", "const:4:8"]]
- 00b32e20 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32e64 ["INT_ADD", "register:40f0:8", ["const:b32e64:8", "const:4:8"]]
+ 00b32e64 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32e20 bytes d8ae0294
+ 00b32e64 bytes dbae0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e5b5c63849502e2f8e05a0619bfc0ab"></a>

### [`00b32efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32efc.md) → [`00b32f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32f40.md) _ZNSt6__ndk118__insertion_sort_3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEvT0_S9_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd60.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00be00f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00f0.md)
- 新版 呼出元 1件 [`00bdfdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfdb0.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00be0140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b32f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32efc.md#insn-00b32f40) · [`00b32fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32efc.md#insn-00b32fa8) · [`00b32ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32efc.md#insn-00b32ff4)
- 新版 `00b32f84`（命令位置の公開資料なし） · `00b32fec`（命令位置の公開資料なし） · `00b33038`（命令位置の公開資料なし）

~~~diff
- 00b32f40 ["INT_ADD", "register:40f0:8", ["const:b32f40:8", "const:4:8"]]
- 00b32f40 ["CALL", null, ["callee:00be0140:8"]]
+ 00b32f84 ["INT_ADD", "register:40f0:8", ["const:b32f84:8", "const:4:8"]]
+ 00b32f84 ["CALL", null, ["callee:00be0140:8"]]
- 00b32f40 bytes 6cb40294
+ 00b32f84 bytes 6fb40294
- 00b32fa8 ["INT_ADD", "register:40f0:8", ["const:b32fa8:8", "const:4:8"]]
- 00b32fa8 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b32fec ["INT_ADD", "register:40f0:8", ["const:b32fec:8", "const:4:8"]]
+ 00b32fec ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32fa8 bytes 76ae0294
+ 00b32fec bytes 79ae0294
- 00b32ff4 ["INT_ADD", "register:40f0:8", ["const:b32ff4:8", "const:4:8"]]
- 00b32ff4 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b33038 ["INT_ADD", "register:40f0:8", ["const:b33038:8", "const:4:8"]]
+ 00b33038 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b32ff4 bytes 63ae0294
+ 00b33038 bytes 66ae0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62699383128f175f4daa1be349d0baf0"></a>

### [`00b3335c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b3335c.md) → [`00b333a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b333a0.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00be00d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b33418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b3335c.md#insn-00b33418) · [`00b334b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b3335c.md#insn-00b334b4) · [`00b334d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b3335c.md#insn-00b334d8)
- 新版 `00b3345c`（命令位置の公開資料なし） · `00b334f8`（命令位置の公開資料なし） · `00b3351c`（命令位置の公開資料なし）

~~~diff
- 00b33418 ["INT_ADD", "register:40f0:8", ["const:b33418:8", "const:4:8"]]
- 00b33418 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b3345c ["INT_ADD", "register:40f0:8", ["const:b3345c:8", "const:4:8"]]
+ 00b3345c ["CALL", null, ["callee:00bdb040:8"]]
- 00b33418 bytes f69e0294
+ 00b3345c bytes f99e0294
- 00b334b4 ["INT_ADD", "register:40f0:8", ["const:b334b4:8", "const:4:8"]]
- 00b334b4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b334f8 ["INT_ADD", "register:40f0:8", ["const:b334f8:8", "const:4:8"]]
+ 00b334f8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b334b4 bytes 2b9f0294
+ 00b334f8 bytes 2e9f0294
- 00b334d8 ["INT_ADD", "register:40f0:8", ["const:b334d8:8", "const:4:8"]]
- 00b334d8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3351c ["INT_ADD", "register:40f0:8", ["const:b3351c:8", "const:4:8"]]
+ 00b3351c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b334d8 bytes 229f0294
+ 00b3351c bytes 259f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce7c86b6ae6b75427afd38bf74ab91b0"></a>

### [`00b336c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b336c8.md) → [`00b3370c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b3370c.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00be00e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00e0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3377c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b336c8.md#insn-00b3377c) · [`00b337a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b336c8.md#insn-00b337a0) · [`00b33850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b336c8.md#insn-00b33850)
- 新版 `00b337c0`（命令位置の公開資料なし） · `00b337e4`（命令位置の公開資料なし） · `00b33894`（命令位置の公開資料なし）

~~~diff
- 00b3377c ["INT_ADD", "register:40f0:8", ["const:b3377c:8", "const:4:8"]]
- 00b3377c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b337c0 ["INT_ADD", "register:40f0:8", ["const:b337c0:8", "const:4:8"]]
+ 00b337c0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3377c bytes 799e0294
+ 00b337c0 bytes 7c9e0294
- 00b337a0 ["INT_ADD", "register:40f0:8", ["const:b337a0:8", "const:4:8"]]
- 00b337a0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b337e4 ["INT_ADD", "register:40f0:8", ["const:b337e4:8", "const:4:8"]]
+ 00b337e4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b337a0 bytes 149e0294
+ 00b337e4 bytes 179e0294
- 00b33850 ["INT_ADD", "register:40f0:8", ["const:b33850:8", "const:4:8"]]
- 00b33850 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b33894 ["INT_ADD", "register:40f0:8", ["const:b33894:8", "const:4:8"]]
+ 00b33894 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b33850 bytes 449e0294
+ 00b33894 bytes 479e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2468dd178114ab9305010793066a008a"></a>

### [`00b33998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33998.md) → [`00b339dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b339dc.md) _ZNSt6__ndk16vectorIN11flexbuffers7Builder5ValueENS_9allocatorIS3_EEE8__appendEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0020.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00be0070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0070.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b33a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33998.md#insn-00b33a08) · [`00b33a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33998.md#insn-00b33a44) · [`00b33a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33998.md#insn-00b33a60)
- 新版 `00b33a4c`（命令位置の公開資料なし） · `00b33a88`（命令位置の公開資料なし） · `00b33aa4`（命令位置の公開資料なし）

~~~diff
- 00b33a08 ["INT_ADD", "register:40f0:8", ["const:b33a08:8", "const:4:8"]]
- 00b33a08 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b33a4c ["INT_ADD", "register:40f0:8", ["const:b33a4c:8", "const:4:8"]]
+ 00b33a4c ["CALL", null, ["callee:00bde2c0:8"]]
- 00b33a08 bytes 1aaa0294
+ 00b33a4c bytes 1daa0294
- 00b33a44 ["INT_ADD", "register:40f0:8", ["const:b33a44:8", "const:4:8"]]
- 00b33a44 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b33a88 ["INT_ADD", "register:40f0:8", ["const:b33a88:8", "const:4:8"]]
+ 00b33a88 ["CALL", null, ["callee:00bdb040:8"]]
- 00b33a44 bytes 6b9d0294
+ 00b33a88 bytes 6e9d0294
- 00b33a60 ["INT_ADD", "register:40f0:8", ["const:b33a60:8", "const:4:8"]]
- 00b33a60 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b33aa4 ["INT_ADD", "register:40f0:8", ["const:b33aa4:8", "const:4:8"]]
+ 00b33aa4 ["CALL", null, ["callee:00bdb240:8"]]
- 00b33a60 bytes e49d0294
+ 00b33aa4 bytes e79d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a71dd2ebbb027edd405dfb20c95db501"></a>

### [`00b33ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33ac4.md) → [`00b33b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33b08.md) _ZN11flexbuffers7Builder6StringEPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfaf0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde790.md) [`00bdfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfaa0.md) [`00bdfff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfff0.md) [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md)
- 新版 呼出元 1件 [`00bdfb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb40.md) · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7e0.md) [`00bdfaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfaf0.md) [`00be0040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0040.md) [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b33b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33ac4.md#insn-00b33b04) · [`00b33b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33ac4.md#insn-00b33b58) · [`00b33b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33ac4.md#insn-00b33b90)
- 新版 `00b33b48`（命令位置の公開資料なし） · `00b33b9c`（命令位置の公開資料なし） · `00b33bd4`（命令位置の公開資料なし）

~~~diff
- 00b33b04 ["INT_ADD", "register:40f0:8", ["const:b33b04:8", "const:4:8"]]
- 00b33b04 ["CALL", null, ["callee:00bdfaf0:8"]]
+ 00b33b48 ["INT_ADD", "register:40f0:8", ["const:b33b48:8", "const:4:8"]]
+ 00b33b48 ["CALL", null, ["callee:00bdfaf0:8"]]
- 00b33b04 bytes e7af0294
+ 00b33b48 bytes eaaf0294
- 00b33b58 ["INT_ADD", "register:40f0:8", ["const:b33b58:8", "const:4:8"]]
- 00b33b58 ["CALL", null, ["callee:00be0230:8"]]
+ 00b33b9c ["INT_ADD", "register:40f0:8", ["const:b33b9c:8", "const:4:8"]]
+ 00b33b9c ["CALL", null, ["callee:00be0230:8"]]
- 00b33b58 bytes a2b10294
+ 00b33b9c bytes a5b10294
- 00b33b90 ["INT_ADD", "register:40f0:8", ["const:b33b90:8", "const:4:8"]]
- 00b33b90 ["CALL", null, ["callee:00be0230:8"]]
+ 00b33bd4 ["INT_ADD", "register:40f0:8", ["const:b33bd4:8", "const:4:8"]]
+ 00b33bd4 ["CALL", null, ["callee:00be0230:8"]]
- 00b33b90 bytes 94b10294
+ 00b33bd4 bytes 97b10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d67ed19fa9e2e9b2d4867f2ab05a9793"></a>

### [`00b33c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md) → [`00b33c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33c60.md) _ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfaa0.md) · 呼出先 4件 [`00b33d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33d38.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00be0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md) [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md)
- 新版 呼出元 1件 [`00bdfaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfaf0.md) · 呼出先 4件 [`00b33d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33d7c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00be00d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md) [`00be00e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b33cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md#insn-00b33cb4) · [`00b33ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md#insn-00b33ccc) · [`00b33ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md#insn-00b33ce8)
- 新版 `00b33cf8`（命令位置の公開資料なし） · `00b33d10`（命令位置の公開資料なし） · `00b33d2c`（命令位置の公開資料なし）

~~~diff
- 00b33cb4 ["INT_ADD", "register:40f0:8", ["const:b33cb4:8", "const:4:8"]]
- 00b33cb4 ["CALL", null, ["callee:00be00d0:8"]]
+ 00b33cf8 ["INT_ADD", "register:40f0:8", ["const:b33cf8:8", "const:4:8"]]
+ 00b33cf8 ["CALL", null, ["callee:00be00d0:8"]]
- 00b33cb4 bytes f3b00294
+ 00b33cf8 bytes f6b00294
- 00b33ccc ["INT_ADD", "register:40f0:8", ["const:b33ccc:8", "const:4:8"]]
- 00b33ccc ["CALL", null, ["callee:00be00e0:8"]]
+ 00b33d10 ["INT_ADD", "register:40f0:8", ["const:b33d10:8", "const:4:8"]]
+ 00b33d10 ["CALL", null, ["callee:00be00e0:8"]]
- 00b33ccc bytes f1b00294
+ 00b33d10 bytes f4b00294
- 00b33ce8 ["INT_ADD", "register:40f0:8", ["const:b33ce8:8", "const:4:8"]]
- 00b33ce8 ["CALL", null, ["callee:00be00e0:8"]]
+ 00b33d2c ["INT_ADD", "register:40f0:8", ["const:b33d2c:8", "const:4:8"]]
+ 00b33d2c ["CALL", null, ["callee:00be00e0:8"]]
- 00b33ce8 bytes eab00294
+ 00b33d2c bytes edb00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d35e59a623fa986bf5599e9f00e10c4"></a>

### [`00b33d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33d38.md) → [`00b33d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33d7c.md) FUN_00b33d7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b256a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b256a0.md) [`00b33c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md) [`00b442c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 3件 [`00b256e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b256e4.md) [`00b33c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33c60.md) [`00b4430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b33db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33d38.md#insn-00b33db8) · [`00b33dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33d38.md#insn-00b33dc4) · [`00b33df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33d38.md#insn-00b33df4)
- 新版 `00b33dfc`（命令位置の公開資料なし） · `00b33e08`（命令位置の公開資料なし） · `00b33e38`（命令位置の公開資料なし）

~~~diff
- 00b33db8 ["INT_ADD", "register:40f0:8", ["const:b33db8:8", "const:4:8"]]
- 00b33db8 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b33dfc ["INT_ADD", "register:40f0:8", ["const:b33dfc:8", "const:4:8"]]
+ 00b33dfc ["CALL", null, ["callee:00bde2c0:8"]]
- 00b33db8 bytes 2ea90294
+ 00b33dfc bytes 31a90294
- 00b33dc4 ["INT_ADD", "register:40f0:8", ["const:b33dc4:8", "const:4:8"]]
- 00b33dc4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b33e08 ["INT_ADD", "register:40f0:8", ["const:b33e08:8", "const:4:8"]]
+ 00b33e08 ["CALL", null, ["callee:00bdb040:8"]]
- 00b33dc4 bytes 8b9c0294
+ 00b33e08 bytes 8e9c0294
- 00b33df4 ["INT_ADD", "register:40f0:8", ["const:b33df4:8", "const:4:8"]]
- 00b33df4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b33e38 ["INT_ADD", "register:40f0:8", ["const:b33e38:8", "const:4:8"]]
+ 00b33e38 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b33df4 bytes db9c0294
+ 00b33e38 bytes de9c0294
~~~


<a id="compare-03345387c2bd827360e838645aa2290e"></a>

### [`00b33e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33e40.md) → [`00b33e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33e84.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS1

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfff0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md)
- 新版 呼出元 1件 [`00be0040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0040.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b33eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33e40.md#insn-00b33eac) · [`00b33ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33e40.md#insn-00b33ed4) · [`00b33f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33e40.md#insn-00b33f14)
- 新版 `00b33ef0`（命令位置の公開資料なし） · `00b33f18`（命令位置の公開資料なし） · `00b33f58`（命令位置の公開資料なし）

~~~diff
- 00b33eac ["INT_ADD", "register:40f0:8", ["const:b33eac:8", "const:4:8"]]
- 00b33eac ["CALL", null, ["callee:00be0230:8"]]
+ 00b33ef0 ["INT_ADD", "register:40f0:8", ["const:b33ef0:8", "const:4:8"]]
+ 00b33ef0 ["CALL", null, ["callee:00be0230:8"]]
- 00b33eac bytes cdb00294
+ 00b33ef0 bytes d0b00294
- 00b33ed4 ["INT_ADD", "register:40f0:8", ["const:b33ed4:8", "const:4:8"]]
- 00b33ed4 ["CALL", null, ["callee:00be0230:8"]]
+ 00b33f18 ["INT_ADD", "register:40f0:8", ["const:b33f18:8", "const:4:8"]]
+ 00b33f18 ["CALL", null, ["callee:00be0230:8"]]
- 00b33ed4 bytes c3b00294
+ 00b33f18 bytes c6b00294
- 00b33f14 ["INT_ADD", "register:40f0:8", ["const:b33f14:8", "const:4:8"]]
- 00b33f14 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b33f58 ["INT_ADD", "register:40f0:8", ["const:b33f58:8", "const:4:8"]]
+ 00b33f58 ["CALL", null, ["callee:00bdb040:8"]]
- 00b33f14 bytes 379c0294
+ 00b33f58 bytes 3a9c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dbb27d063c6b1cf5f2c56fe788313a8"></a>

### [`00b33f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33f84.md) → [`00b33fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33fc8.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection7ServiceEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf550.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5a0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b33fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33f84.md#insn-00b33fe8) · [`00b34058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33f84.md#insn-00b34058) · [`00b34078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33f84.md#insn-00b34078)
- 新版 `00b3402c`（命令位置の公開資料なし） · `00b3409c`（命令位置の公開資料なし） · `00b340bc`（命令位置の公開資料なし）

~~~diff
- 00b33fe8 ["INT_ADD", "register:40f0:8", ["const:b33fe8:8", "const:4:8"]]
- 00b33fe8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3402c ["INT_ADD", "register:40f0:8", ["const:b3402c:8", "const:4:8"]]
+ 00b3402c ["CALL", null, ["callee:00bdf390:8"]]
- 00b33fe8 bytes d6ac0294
+ 00b3402c bytes d9ac0294
- 00b34058 ["INT_ADD", "register:40f0:8", ["const:b34058:8", "const:4:8"]]
- 00b34058 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b3409c ["INT_ADD", "register:40f0:8", ["const:b3409c:8", "const:4:8"]]
+ 00b3409c ["CALL", null, ["callee:00bdf480:8"]]
- 00b34058 bytes f6ac0294
+ 00b3409c bytes f9ac0294
- 00b34078 ["INT_ADD", "register:40f0:8", ["const:b34078:8", "const:4:8"]]
- 00b34078 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b340bc ["INT_ADD", "register:40f0:8", ["const:b340bc:8", "const:4:8"]]
+ 00b340bc ["CALL", null, ["callee:00bdf390:8"]]
- 00b34078 bytes b2ac0294
+ 00b340bc bytes b5ac0294
~~~


<a id="compare-cd4b4f537a144ef7b60559a860b24d69"></a>

### [`00b340c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b340c8.md) → [`00b3410c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b3410c.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetIN10reflection6ObjectEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4e0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf530.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3412c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b340c8.md#insn-00b3412c) · [`00b3419c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b340c8.md#insn-00b3419c) · [`00b341bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b340c8.md#insn-00b341bc)
- 新版 `00b34170`（命令位置の公開資料なし） · `00b341e0`（命令位置の公開資料なし） · `00b34200`（命令位置の公開資料なし）

~~~diff
- 00b3412c ["INT_ADD", "register:40f0:8", ["const:b3412c:8", "const:4:8"]]
- 00b3412c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34170 ["INT_ADD", "register:40f0:8", ["const:b34170:8", "const:4:8"]]
+ 00b34170 ["CALL", null, ["callee:00bdf390:8"]]
- 00b3412c bytes 85ac0294
+ 00b34170 bytes 88ac0294
- 00b3419c ["INT_ADD", "register:40f0:8", ["const:b3419c:8", "const:4:8"]]
- 00b3419c ["CALL", null, ["callee:00bdf480:8"]]
+ 00b341e0 ["INT_ADD", "register:40f0:8", ["const:b341e0:8", "const:4:8"]]
+ 00b341e0 ["CALL", null, ["callee:00bdf480:8"]]
- 00b3419c bytes a5ac0294
+ 00b341e0 bytes a8ac0294
- 00b341bc ["INT_ADD", "register:40f0:8", ["const:b341bc:8", "const:4:8"]]
- 00b341bc ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34200 ["INT_ADD", "register:40f0:8", ["const:b34200:8", "const:4:8"]]
+ 00b34200 ["CALL", null, ["callee:00bdf390:8"]]
- 00b341bc bytes 61ac0294
+ 00b34200 bytes 64ac0294
~~~


<a id="compare-8a13a2a2c42074366a7f2e6efce2c0b2"></a>

### [`00b3420c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b3420c.md) → [`00b34250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34250.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6StringEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4f0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf540.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b3420c.md#insn-00b34270) · [`00b342e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b3420c.md#insn-00b342e0) · [`00b34300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b3420c.md#insn-00b34300)
- 新版 `00b342b4`（命令位置の公開資料なし） · `00b34324`（命令位置の公開資料なし） · `00b34344`（命令位置の公開資料なし）

~~~diff
- 00b34270 ["INT_ADD", "register:40f0:8", ["const:b34270:8", "const:4:8"]]
- 00b34270 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b342b4 ["INT_ADD", "register:40f0:8", ["const:b342b4:8", "const:4:8"]]
+ 00b342b4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34270 bytes 34ac0294
+ 00b342b4 bytes 37ac0294
- 00b342e0 ["INT_ADD", "register:40f0:8", ["const:b342e0:8", "const:4:8"]]
- 00b342e0 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b34324 ["INT_ADD", "register:40f0:8", ["const:b34324:8", "const:4:8"]]
+ 00b34324 ["CALL", null, ["callee:00bdf480:8"]]
- 00b342e0 bytes 54ac0294
+ 00b34324 bytes 57ac0294
- 00b34300 ["INT_ADD", "register:40f0:8", ["const:b34300:8", "const:4:8"]]
- 00b34300 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34344 ["INT_ADD", "register:40f0:8", ["const:b34344:8", "const:4:8"]]
+ 00b34344 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34300 bytes 10ac0294
+ 00b34344 bytes 13ac0294
~~~


<a id="compare-a061a94f9531054e9cf8499f8518f026"></a>

### [`00b34350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34350.md) → [`00b34394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34394.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection4EnumEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf500.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf550.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b343b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34350.md#insn-00b343b4) · [`00b34424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34350.md#insn-00b34424) · [`00b34444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34350.md#insn-00b34444)
- 新版 `00b343f8`（命令位置の公開資料なし） · `00b34468`（命令位置の公開資料なし） · `00b34488`（命令位置の公開資料なし）

~~~diff
- 00b343b4 ["INT_ADD", "register:40f0:8", ["const:b343b4:8", "const:4:8"]]
- 00b343b4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b343f8 ["INT_ADD", "register:40f0:8", ["const:b343f8:8", "const:4:8"]]
+ 00b343f8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b343b4 bytes e3ab0294
+ 00b343f8 bytes e6ab0294
- 00b34424 ["INT_ADD", "register:40f0:8", ["const:b34424:8", "const:4:8"]]
- 00b34424 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b34468 ["INT_ADD", "register:40f0:8", ["const:b34468:8", "const:4:8"]]
+ 00b34468 ["CALL", null, ["callee:00bdf480:8"]]
- 00b34424 bytes 03ac0294
+ 00b34468 bytes 06ac0294
- 00b34444 ["INT_ADD", "register:40f0:8", ["const:b34444:8", "const:4:8"]]
- 00b34444 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34488 ["INT_ADD", "register:40f0:8", ["const:b34488:8", "const:4:8"]]
+ 00b34488 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34444 bytes bfab0294
+ 00b34488 bytes c2ab0294
~~~


<a id="compare-8edf4e02062196462a224d46181d1d33"></a>

### [`00b34494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34494.md) → [`00b344d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b344d8.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection6ObjectEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf520.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf570.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b344f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34494.md#insn-00b344f8) · [`00b34568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34494.md#insn-00b34568) · [`00b34588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34494.md#insn-00b34588)
- 新版 `00b3453c`（命令位置の公開資料なし） · `00b345ac`（命令位置の公開資料なし） · `00b345cc`（命令位置の公開資料なし）

~~~diff
- 00b344f8 ["INT_ADD", "register:40f0:8", ["const:b344f8:8", "const:4:8"]]
- 00b344f8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3453c ["INT_ADD", "register:40f0:8", ["const:b3453c:8", "const:4:8"]]
+ 00b3453c ["CALL", null, ["callee:00bdf390:8"]]
- 00b344f8 bytes 92ab0294
+ 00b3453c bytes 95ab0294
- 00b34568 ["INT_ADD", "register:40f0:8", ["const:b34568:8", "const:4:8"]]
- 00b34568 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b345ac ["INT_ADD", "register:40f0:8", ["const:b345ac:8", "const:4:8"]]
+ 00b345ac ["CALL", null, ["callee:00bdf480:8"]]
- 00b34568 bytes b2ab0294
+ 00b345ac bytes b5ab0294
- 00b34588 ["INT_ADD", "register:40f0:8", ["const:b34588:8", "const:4:8"]]
- 00b34588 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b345cc ["INT_ADD", "register:40f0:8", ["const:b345cc:8", "const:4:8"]]
+ 00b345cc ["CALL", null, ["callee:00bdf390:8"]]
- 00b34588 bytes 6eab0294
+ 00b345cc bytes 71ab0294
~~~


<a id="compare-782796d57c64475d92361026385575e7"></a>

### [`00b345d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b345d8.md) → [`00b3461c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b3461c.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementINS_6StringEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3f0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf440.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b345d8.md#insn-00b34634)
- 新版 `00b34678`（命令位置の公開資料なし）

~~~diff
- 00b34634 ["INT_ADD", "register:40f0:8", ["const:b34634:8", "const:4:8"]]
- 00b34634 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34678 ["INT_ADD", "register:40f0:8", ["const:b34678:8", "const:4:8"]]
+ 00b34678 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34634 bytes 43ab0294
+ 00b34678 bytes 46ab0294
~~~


<a id="compare-6a8a9bc5c6621c8232080e61c3b228ce"></a>

### [`00b346a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b346a8.md) → [`00b346ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b346ec.md) _ZN10reflection13ObjectBuilder13add_is_structEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0f0.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf140.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b346ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b346a8.md#insn-00b346ec) · [`00b34724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b346a8.md#insn-00b34724)
- 新版 `00b34730`（命令位置の公開資料なし） · `00b34768`（命令位置の公開資料なし）

~~~diff
- 00b346ec ["INT_ADD", "register:40f0:8", ["const:b346ec:8", "const:4:8"]]
- 00b346ec ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34730 ["INT_ADD", "register:40f0:8", ["const:b34730:8", "const:4:8"]]
+ 00b34730 ["CALL", null, ["callee:00bdf390:8"]]
- 00b346ec bytes 15ab0294
+ 00b34730 bytes 18ab0294
- 00b34724 ["INT_ADD", "register:40f0:8", ["const:b34724:8", "const:4:8"]]
- 00b34724 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34768 ["INT_ADD", "register:40f0:8", ["const:b34768:8", "const:4:8"]]
+ 00b34768 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34724 bytes 07ab0294
+ 00b34768 bytes 0aab0294
~~~


<a id="compare-9f260957de8c1106a4c79350286d360f"></a>

### [`00b34770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34770.md) → [`00b347b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b347b4.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetINS_6StringEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf570.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5c0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b347d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34770.md#insn-00b347d4) · [`00b34844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34770.md#insn-00b34844) · [`00b34864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34770.md#insn-00b34864)
- 新版 `00b34818`（命令位置の公開資料なし） · `00b34888`（命令位置の公開資料なし） · `00b348a8`（命令位置の公開資料なし）

~~~diff
- 00b347d4 ["INT_ADD", "register:40f0:8", ["const:b347d4:8", "const:4:8"]]
- 00b347d4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34818 ["INT_ADD", "register:40f0:8", ["const:b34818:8", "const:4:8"]]
+ 00b34818 ["CALL", null, ["callee:00bdf390:8"]]
- 00b347d4 bytes dbaa0294
+ 00b34818 bytes deaa0294
- 00b34844 ["INT_ADD", "register:40f0:8", ["const:b34844:8", "const:4:8"]]
- 00b34844 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b34888 ["INT_ADD", "register:40f0:8", ["const:b34888:8", "const:4:8"]]
+ 00b34888 ["CALL", null, ["callee:00bdf480:8"]]
- 00b34844 bytes fbaa0294
+ 00b34888 bytes feaa0294
- 00b34864 ["INT_ADD", "register:40f0:8", ["const:b34864:8", "const:4:8"]]
- 00b34864 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b348a8 ["INT_ADD", "register:40f0:8", ["const:b348a8:8", "const:4:8"]]
+ 00b348a8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34864 bytes b7aa0294
+ 00b348a8 bytes baaa0294
~~~


<a id="compare-17606b2a5d676e38dc471f205219f351"></a>

### [`00b348b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b348b4.md) → [`00b348f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b348f8.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection8KeyValueEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf560.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5b0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b348b4.md#insn-00b34918) · [`00b34988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b348b4.md#insn-00b34988) · [`00b349a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b348b4.md#insn-00b349a8)
- 新版 `00b3495c`（命令位置の公開資料なし） · `00b349cc`（命令位置の公開資料なし） · `00b349ec`（命令位置の公開資料なし）

~~~diff
- 00b34918 ["INT_ADD", "register:40f0:8", ["const:b34918:8", "const:4:8"]]
- 00b34918 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3495c ["INT_ADD", "register:40f0:8", ["const:b3495c:8", "const:4:8"]]
+ 00b3495c ["CALL", null, ["callee:00bdf390:8"]]
- 00b34918 bytes 8aaa0294
+ 00b3495c bytes 8daa0294
- 00b34988 ["INT_ADD", "register:40f0:8", ["const:b34988:8", "const:4:8"]]
- 00b34988 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b349cc ["INT_ADD", "register:40f0:8", ["const:b349cc:8", "const:4:8"]]
+ 00b349cc ["CALL", null, ["callee:00bdf480:8"]]
- 00b34988 bytes aaaa0294
+ 00b349cc bytes adaa0294
- 00b349a8 ["INT_ADD", "register:40f0:8", ["const:b349a8:8", "const:4:8"]]
- 00b349a8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b349ec ["INT_ADD", "register:40f0:8", ["const:b349ec:8", "const:4:8"]]
+ 00b349ec ["CALL", null, ["callee:00bdf390:8"]]
- 00b349a8 bytes 66aa0294
+ 00b349ec bytes 69aa0294
~~~


<a id="compare-0f2ee4cce0fcf9ef2fd4c489e9e88d81"></a>

### [`00b349f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b349f8.md) → [`00b34a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34a3c.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection5FieldEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf510.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf560.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b349f8.md#insn-00b34a5c) · [`00b34acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b349f8.md#insn-00b34acc) · [`00b34aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b349f8.md#insn-00b34aec)
- 新版 `00b34aa0`（命令位置の公開資料なし） · `00b34b10`（命令位置の公開資料なし） · `00b34b30`（命令位置の公開資料なし）

~~~diff
- 00b34a5c ["INT_ADD", "register:40f0:8", ["const:b34a5c:8", "const:4:8"]]
- 00b34a5c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34aa0 ["INT_ADD", "register:40f0:8", ["const:b34aa0:8", "const:4:8"]]
+ 00b34aa0 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34a5c bytes 39aa0294
+ 00b34aa0 bytes 3caa0294
- 00b34acc ["INT_ADD", "register:40f0:8", ["const:b34acc:8", "const:4:8"]]
- 00b34acc ["CALL", null, ["callee:00bdf480:8"]]
+ 00b34b10 ["INT_ADD", "register:40f0:8", ["const:b34b10:8", "const:4:8"]]
+ 00b34b10 ["CALL", null, ["callee:00bdf480:8"]]
- 00b34acc bytes 59aa0294
+ 00b34b10 bytes 5caa0294
- 00b34aec ["INT_ADD", "register:40f0:8", ["const:b34aec:8", "const:4:8"]]
- 00b34aec ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34b30 ["INT_ADD", "register:40f0:8", ["const:b34b30:8", "const:4:8"]]
+ 00b34b30 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34aec bytes 15aa0294
+ 00b34b30 bytes 18aa0294
~~~


<a id="compare-92f41a71ac45a278894e5bceb413fb1b"></a>

### [`00b34b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34b3c.md) → [`00b34b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34b80.md) _ZN10reflection12FieldBuilder7add_keyEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0d0.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf120.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34b3c.md#insn-00b34b80) · [`00b34bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34b3c.md#insn-00b34bb8)
- 新版 `00b34bc4`（命令位置の公開資料なし） · `00b34bfc`（命令位置の公開資料なし）

~~~diff
- 00b34b80 ["INT_ADD", "register:40f0:8", ["const:b34b80:8", "const:4:8"]]
- 00b34b80 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34bc4 ["INT_ADD", "register:40f0:8", ["const:b34bc4:8", "const:4:8"]]
+ 00b34bc4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34b80 bytes f0a90294
+ 00b34bc4 bytes f3a90294
- 00b34bb8 ["INT_ADD", "register:40f0:8", ["const:b34bb8:8", "const:4:8"]]
- 00b34bb8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34bfc ["INT_ADD", "register:40f0:8", ["const:b34bfc:8", "const:4:8"]]
+ 00b34bfc ["CALL", null, ["callee:00bdf390:8"]]
- 00b34bb8 bytes e2a90294
+ 00b34bfc bytes e5a90294
~~~


<a id="compare-fe8a052ccf136530d38349dbe34d305c"></a>

### [`00b34c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34c04.md) → [`00b34c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34c48.md) _ZN10reflection12FieldBuilder12add_requiredEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0b0.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf100.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34c04.md#insn-00b34c48) · [`00b34c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34c04.md#insn-00b34c80)
- 新版 `00b34c8c`（命令位置の公開資料なし） · `00b34cc4`（命令位置の公開資料なし）

~~~diff
- 00b34c48 ["INT_ADD", "register:40f0:8", ["const:b34c48:8", "const:4:8"]]
- 00b34c48 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34c8c ["INT_ADD", "register:40f0:8", ["const:b34c8c:8", "const:4:8"]]
+ 00b34c8c ["CALL", null, ["callee:00bdf390:8"]]
- 00b34c48 bytes bea90294
+ 00b34c8c bytes c1a90294
- 00b34c80 ["INT_ADD", "register:40f0:8", ["const:b34c80:8", "const:4:8"]]
- 00b34c80 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34cc4 ["INT_ADD", "register:40f0:8", ["const:b34cc4:8", "const:4:8"]]
+ 00b34cc4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34c80 bytes b0a90294
+ 00b34cc4 bytes b3a90294
~~~


<a id="compare-b41b122933209eb1ef4b3a5e5cf2924b"></a>

### [`00b34ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md) → [`00b34d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34d10.md) _ZN10reflection12FieldBuilder14add_deprecatedEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf110.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md#insn-00b34d10) · [`00b34d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md#insn-00b34d48)
- 新版 `00b34d54`（命令位置の公開資料なし） · `00b34d8c`（命令位置の公開資料なし）

~~~diff
- 00b34d10 ["INT_ADD", "register:40f0:8", ["const:b34d10:8", "const:4:8"]]
- 00b34d10 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34d54 ["INT_ADD", "register:40f0:8", ["const:b34d54:8", "const:4:8"]]
+ 00b34d54 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34d10 bytes 8ca90294
+ 00b34d54 bytes 8fa90294
- 00b34d48 ["INT_ADD", "register:40f0:8", ["const:b34d48:8", "const:4:8"]]
- 00b34d48 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34d8c ["INT_ADD", "register:40f0:8", ["const:b34d8c:8", "const:4:8"]]
+ 00b34d8c ["CALL", null, ["callee:00bdf390:8"]]
- 00b34d48 bytes 7ea90294
+ 00b34d8c bytes 81a90294
~~~


<a id="compare-ac4a2d0b0d312a4686f407885d006ce9"></a>

### [`00b34d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34d94.md) → [`00b34dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34dd8.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetIN10reflection4TypeEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4d0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf520.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34d94.md#insn-00b34df8) · [`00b34e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34d94.md#insn-00b34e68) · [`00b34e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34d94.md#insn-00b34e88)
- 新版 `00b34e3c`（命令位置の公開資料なし） · `00b34eac`（命令位置の公開資料なし） · `00b34ecc`（命令位置の公開資料なし）

~~~diff
- 00b34df8 ["INT_ADD", "register:40f0:8", ["const:b34df8:8", "const:4:8"]]
- 00b34df8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34e3c ["INT_ADD", "register:40f0:8", ["const:b34e3c:8", "const:4:8"]]
+ 00b34e3c ["CALL", null, ["callee:00bdf390:8"]]
- 00b34df8 bytes 52a90294
+ 00b34e3c bytes 55a90294
- 00b34e68 ["INT_ADD", "register:40f0:8", ["const:b34e68:8", "const:4:8"]]
- 00b34e68 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b34eac ["INT_ADD", "register:40f0:8", ["const:b34eac:8", "const:4:8"]]
+ 00b34eac ["CALL", null, ["callee:00bdf480:8"]]
- 00b34e68 bytes 72a90294
+ 00b34eac bytes 75a90294
- 00b34e88 ["INT_ADD", "register:40f0:8", ["const:b34e88:8", "const:4:8"]]
- 00b34e88 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34ecc ["INT_ADD", "register:40f0:8", ["const:b34ecc:8", "const:4:8"]]
+ 00b34ecc ["CALL", null, ["callee:00bdf390:8"]]
- 00b34e88 bytes 2ea90294
+ 00b34ecc bytes 31a90294
~~~


<a id="compare-07721783fb9e81f65fea3f99d311b4bb"></a>

### [`00b34ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ed8.md) → [`00b34f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34f1c.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection7RPCCallEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf540.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf590.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ed8.md#insn-00b34f3c) · [`00b34fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ed8.md#insn-00b34fac) · [`00b34fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ed8.md#insn-00b34fcc)
- 新版 `00b34f80`（命令位置の公開資料なし） · `00b34ff0`（命令位置の公開資料なし） · `00b35010`（命令位置の公開資料なし）

~~~diff
- 00b34f3c ["INT_ADD", "register:40f0:8", ["const:b34f3c:8", "const:4:8"]]
- 00b34f3c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b34f80 ["INT_ADD", "register:40f0:8", ["const:b34f80:8", "const:4:8"]]
+ 00b34f80 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34f3c bytes 01a90294
+ 00b34f80 bytes 04a90294
- 00b34fac ["INT_ADD", "register:40f0:8", ["const:b34fac:8", "const:4:8"]]
- 00b34fac ["CALL", null, ["callee:00bdf480:8"]]
+ 00b34ff0 ["INT_ADD", "register:40f0:8", ["const:b34ff0:8", "const:4:8"]]
+ 00b34ff0 ["CALL", null, ["callee:00bdf480:8"]]
- 00b34fac bytes 21a90294
+ 00b34ff0 bytes 24a90294
- 00b34fcc ["INT_ADD", "register:40f0:8", ["const:b34fcc:8", "const:4:8"]]
- 00b34fcc ["CALL", null, ["callee:00bdf390:8"]]
+ 00b35010 ["INT_ADD", "register:40f0:8", ["const:b35010:8", "const:4:8"]]
+ 00b35010 ["CALL", null, ["callee:00bdf390:8"]]
- 00b34fcc bytes dda80294
+ 00b35010 bytes e0a80294
~~~


<a id="compare-cd8e899e37e6e5d2be85f737106fb64b"></a>

### [`00b3501c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b3501c.md) → [`00b35060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b35/00b35060.md) _ZN10reflection11EnumBuilder12add_is_unionEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf070.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0c0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b3501c.md#insn-00b35060) · [`00b35098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b3501c.md#insn-00b35098)
- 新版 `00b350a4`（命令位置の公開資料なし） · `00b350dc`（命令位置の公開資料なし）

~~~diff
- 00b35060 ["INT_ADD", "register:40f0:8", ["const:b35060:8", "const:4:8"]]
- 00b35060 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b350a4 ["INT_ADD", "register:40f0:8", ["const:b350a4:8", "const:4:8"]]
+ 00b350a4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b35060 bytes b8a80294
+ 00b350a4 bytes bba80294
- 00b35098 ["INT_ADD", "register:40f0:8", ["const:b35098:8", "const:4:8"]]
- 00b35098 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b350dc ["INT_ADD", "register:40f0:8", ["const:b350dc:8", "const:4:8"]]
+ 00b350dc ["CALL", null, ["callee:00bdf390:8"]]
- 00b35098 bytes aaa80294
+ 00b350dc bytes ada80294
~~~


<a id="compare-3b6e59eec2ce17a3149682b87b8dfb93"></a>

### [`00b350e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b350e4.md) → [`00b35128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b35/00b35128.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection7EnumValEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf530.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf580.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b350e4.md#insn-00b35148) · [`00b351b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b350e4.md#insn-00b351b8) · [`00b351d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b350e4.md#insn-00b351d8)
- 新版 `00b3518c`（命令位置の公開資料なし） · `00b351fc`（命令位置の公開資料なし） · `00b3521c`（命令位置の公開資料なし）

~~~diff
- 00b35148 ["INT_ADD", "register:40f0:8", ["const:b35148:8", "const:4:8"]]
- 00b35148 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3518c ["INT_ADD", "register:40f0:8", ["const:b3518c:8", "const:4:8"]]
+ 00b3518c ["CALL", null, ["callee:00bdf390:8"]]
- 00b35148 bytes 7ea80294
+ 00b3518c bytes 81a80294
- 00b351b8 ["INT_ADD", "register:40f0:8", ["const:b351b8:8", "const:4:8"]]
- 00b351b8 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b351fc ["INT_ADD", "register:40f0:8", ["const:b351fc:8", "const:4:8"]]
+ 00b351fc ["CALL", null, ["callee:00bdf480:8"]]
- 00b351b8 bytes 9ea80294
+ 00b351fc bytes a1a80294
- 00b351d8 ["INT_ADD", "register:40f0:8", ["const:b351d8:8", "const:4:8"]]
- 00b351d8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3521c ["INT_ADD", "register:40f0:8", ["const:b3521c:8", "const:4:8"]]
+ 00b3521c ["CALL", null, ["callee:00bdf390:8"]]
- 00b351d8 bytes 5aa80294
+ 00b3521c bytes 5da80294
~~~


<a id="compare-a836db99b6d7e71e16a604d4a0a32123"></a>

### [`00b35228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35228.md) → [`00b3526c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b35/00b3526c.md) _ZN10reflection11TypeBuilder11add_elementENS_8BaseTypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf080.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0d0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35228.md#insn-00b35270) · [`00b352a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35228.md#insn-00b352a8)
- 新版 `00b352b4`（命令位置の公開資料なし） · `00b352ec`（命令位置の公開資料なし）

~~~diff
- 00b35270 ["INT_ADD", "register:40f0:8", ["const:b35270:8", "const:4:8"]]
- 00b35270 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b352b4 ["INT_ADD", "register:40f0:8", ["const:b352b4:8", "const:4:8"]]
+ 00b352b4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b35270 bytes 34a80294
+ 00b352b4 bytes 37a80294
- 00b352a8 ["INT_ADD", "register:40f0:8", ["const:b352a8:8", "const:4:8"]]
- 00b352a8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b352ec ["INT_ADD", "register:40f0:8", ["const:b352ec:8", "const:4:8"]]
+ 00b352ec ["CALL", null, ["callee:00bdf390:8"]]
- 00b352a8 bytes 26a80294
+ 00b352ec bytes 29a80294
~~~


<a id="compare-1f6e9b3c4d344b8172d6548ea022b446"></a>

### [`00b352f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b352f4.md) → [`00b35338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b35/00b35338.md) _ZN10reflection11TypeBuilder13add_base_typeENS_8BaseTypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf090.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf0e0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3533c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b352f4.md#insn-00b3533c) · [`00b35374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b352f4.md#insn-00b35374)
- 新版 `00b35380`（命令位置の公開資料なし） · `00b353b8`（命令位置の公開資料なし）

~~~diff
- 00b3533c ["INT_ADD", "register:40f0:8", ["const:b3533c:8", "const:4:8"]]
- 00b3533c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b35380 ["INT_ADD", "register:40f0:8", ["const:b35380:8", "const:4:8"]]
+ 00b35380 ["CALL", null, ["callee:00bdf390:8"]]
- 00b3533c bytes 01a80294
+ 00b35380 bytes 04a80294
- 00b35374 ["INT_ADD", "register:40f0:8", ["const:b35374:8", "const:4:8"]]
- 00b35374 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b353b8 ["INT_ADD", "register:40f0:8", ["const:b353b8:8", "const:4:8"]]
+ 00b353b8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b35374 bytes f3a70294
+ 00b353b8 bytes f6a70294
~~~


<a id="compare-02826a408f770845f3ba1e2aa775f943"></a>

### [`00b353c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b353c0.md) → [`00b35404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b35/00b35404.md) _ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb60.md) · 呼出先 3件 [`00bdfb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb20.md) [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md) [`00bdfb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb90.md)
- 新版 呼出元 1件 [`00bdfbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbb0.md) · 呼出先 3件 [`00bdfb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb70.md) [`00bdfba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfba0.md) [`00bdfbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b355a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b353c0.md#insn-00b355a0) · [`00b356d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b353c0.md#insn-00b356d0) · [`00b35964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b353c0.md#insn-00b35964)
- 新版 `00b355e4`（命令位置の公開資料なし） · `00b35714`（命令位置の公開資料なし） · `00b359a8`（命令位置の公開資料なし）

~~~diff
- 00b355a0 ["INT_ADD", "register:40f0:8", ["const:b355a0:8", "const:4:8"]]
- 00b355a0 ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b355e4 ["INT_ADD", "register:40f0:8", ["const:b355e4:8", "const:4:8"]]
+ 00b355e4 ["CALL", null, ["callee:00bdfba0:8"]]
- 00b355a0 bytes 6ca90294
+ 00b355e4 bytes 6fa90294
- 00b356d0 ["INT_ADD", "register:40f0:8", ["const:b356d0:8", "const:4:8"]]
- 00b356d0 ["CALL", null, ["callee:00bdfb70:8"]]
+ 00b35714 ["INT_ADD", "register:40f0:8", ["const:b35714:8", "const:4:8"]]
+ 00b35714 ["CALL", null, ["callee:00bdfb70:8"]]
- 00b356d0 bytes 14a90294
+ 00b35714 bytes 17a90294
- 00b35964 ["INT_ADD", "register:40f0:8", ["const:b35964:8", "const:4:8"]]
- 00b35964 ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b359a8 ["INT_ADD", "register:40f0:8", ["const:b359a8:8", "const:4:8"]]
+ 00b359a8 ["CALL", null, ["callee:00bdfba0:8"]]
- 00b35964 bytes 7ba80294
+ 00b359a8 bytes 7ea80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-524d2d24e689f8cccaaaea94e92fb792"></a>

### [`00b35ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35ac0.md) → [`00b35b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b35/00b35b04.md) _ZNK10reflection6Object6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md) · 呼出先 2件 [`00bdfb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb40.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)
- 新版 呼出元 1件 [`00bdfba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfba0.md) · 呼出先 2件 [`00bdfb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb90.md) [`00bdfbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35ac0.md#insn-00b35d80) · [`00b35f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35ac0.md#insn-00b35f68)
- 新版 `00b35dc4`（命令位置の公開資料なし） · `00b35fac`（命令位置の公開資料なし）

~~~diff
- 00b35d80 ["INT_ADD", "register:40f0:8", ["const:b35d80:8", "const:4:8"]]
- 00b35d80 ["CALL", null, ["callee:00bdfb90:8"]]
+ 00b35dc4 ["INT_ADD", "register:40f0:8", ["const:b35dc4:8", "const:4:8"]]
+ 00b35dc4 ["CALL", null, ["callee:00bdfb90:8"]]
- 00b35d80 bytes 70a70294
+ 00b35dc4 bytes 73a70294
- 00b35f68 ["INT_ADD", "register:40f0:8", ["const:b35f68:8", "const:4:8"]]
- 00b35f68 ["CALL", null, ["callee:00bdfbf0:8"]]
+ 00b35fac ["INT_ADD", "register:40f0:8", ["const:b35fac:8", "const:4:8"]]
+ 00b35fac ["CALL", null, ["callee:00bdfbf0:8"]]
- 00b35f68 bytes 0ea70294
+ 00b35fac bytes 11a70294
~~~


<a id="compare-db1f19dc324baa4a21e87955f9a0735b"></a>

### [`00b36130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36130.md) → [`00b36174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b36/00b36174.md) _ZNK10reflection5Field6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb40.md) · 呼出先 2件 [`00bdfb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb30.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)
- 新版 呼出元 1件 [`00bdfb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb90.md) · 呼出先 2件 [`00bdfb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb80.md) [`00bdfbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b36360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36130.md#insn-00b36360) · [`00b3661c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36130.md#insn-00b3661c)
- 新版 `00b363a4`（命令位置の公開資料なし） · `00b36660`（命令位置の公開資料なし）

~~~diff
- 00b36360 ["INT_ADD", "register:40f0:8", ["const:b36360:8", "const:4:8"]]
- 00b36360 ["CALL", null, ["callee:00bdfb80:8"]]
+ 00b363a4 ["INT_ADD", "register:40f0:8", ["const:b363a4:8", "const:4:8"]]
+ 00b363a4 ["CALL", null, ["callee:00bdfb80:8"]]
- 00b36360 bytes f4a50294
+ 00b363a4 bytes f7a50294
- 00b3661c ["INT_ADD", "register:40f0:8", ["const:b3661c:8", "const:4:8"]]
- 00b3661c ["CALL", null, ["callee:00bdfbf0:8"]]
+ 00b36660 ["INT_ADD", "register:40f0:8", ["const:b36660:8", "const:4:8"]]
+ 00b36660 ["CALL", null, ["callee:00bdfbf0:8"]]
- 00b3661c bytes 61a50294
+ 00b36660 bytes 64a50294
~~~


<a id="compare-d272548d361a7bcbfb7400888adf62bf"></a>

### [`00b36be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36be0.md) → [`00b36c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b36/00b36c24.md) _ZNK10reflection4Enum6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb20.md) · 呼出先 3件 [`00bdfb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb30.md) [`00bdfb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb70.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)
- 新版 呼出元 1件 [`00bdfb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb70.md) · 呼出先 3件 [`00bdfb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb80.md) [`00bdfbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbc0.md) [`00bdfbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b36ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36be0.md#insn-00b36ea0) · [`00b36f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36be0.md#insn-00b36f88) · [`00b370b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36be0.md#insn-00b370b4)
- 新版 `00b36ee4`（命令位置の公開資料なし） · `00b36fcc`（命令位置の公開資料なし） · `00b370f8`（命令位置の公開資料なし）

~~~diff
- 00b36ea0 ["INT_ADD", "register:40f0:8", ["const:b36ea0:8", "const:4:8"]]
- 00b36ea0 ["CALL", null, ["callee:00bdfbc0:8"]]
+ 00b36ee4 ["INT_ADD", "register:40f0:8", ["const:b36ee4:8", "const:4:8"]]
+ 00b36ee4 ["CALL", null, ["callee:00bdfbc0:8"]]
- 00b36ea0 bytes 34a30294
+ 00b36ee4 bytes 37a30294
- 00b36f88 ["INT_ADD", "register:40f0:8", ["const:b36f88:8", "const:4:8"]]
- 00b36f88 ["CALL", null, ["callee:00bdfb80:8"]]
+ 00b36fcc ["INT_ADD", "register:40f0:8", ["const:b36fcc:8", "const:4:8"]]
+ 00b36fcc ["CALL", null, ["callee:00bdfb80:8"]]
- 00b36f88 bytes eaa20294
+ 00b36fcc bytes eda20294
- 00b370b4 ["INT_ADD", "register:40f0:8", ["const:b370b4:8", "const:4:8"]]
- 00b370b4 ["CALL", null, ["callee:00bdfbf0:8"]]
+ 00b370f8 ["INT_ADD", "register:40f0:8", ["const:b370f8:8", "const:4:8"]]
+ 00b370f8 ["CALL", null, ["callee:00bdfbf0:8"]]
- 00b370b4 bytes bba20294
+ 00b370f8 bytes bea20294
~~~


<a id="compare-2f3d7adde769f94c6c1058a9c17d1081"></a>

### [`00b3727c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b3727c.md) → [`00b372c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b37/00b372c0.md) _ZNK10reflection7EnumVal6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb70.md) · 呼出先 2件 [`00bdfb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb30.md) [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md)
- 新版 呼出元 1件 [`00bdfbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbc0.md) · 呼出先 2件 [`00bdfb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb80.md) [`00bdfba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b374c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b3727c.md#insn-00b374c4) · [`00b3755c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b3727c.md#insn-00b3755c)
- 新版 `00b37508`（命令位置の公開資料なし） · `00b375a0`（命令位置の公開資料なし）

~~~diff
- 00b374c4 ["INT_ADD", "register:40f0:8", ["const:b374c4:8", "const:4:8"]]
- 00b374c4 ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b37508 ["INT_ADD", "register:40f0:8", ["const:b37508:8", "const:4:8"]]
+ 00b37508 ["CALL", null, ["callee:00bdfba0:8"]]
- 00b374c4 bytes a3a10294
+ 00b37508 bytes a6a10294
- 00b3755c ["INT_ADD", "register:40f0:8", ["const:b3755c:8", "const:4:8"]]
- 00b3755c ["CALL", null, ["callee:00bdfb80:8"]]
+ 00b375a0 ["INT_ADD", "register:40f0:8", ["const:b375a0:8", "const:4:8"]]
+ 00b375a0 ["CALL", null, ["callee:00bdfb80:8"]]
- 00b3755c bytes 75a10294
+ 00b375a0 bytes 78a10294
~~~


<a id="compare-15484ee10ec21e8ef6079d48f0b4cedf"></a>

### [`00b37710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37710.md) → [`00b37754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b37/00b37754.md) _ZNK10reflection7Service6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb90.md) · 呼出先 2件 [`00bdfb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb80.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)
- 新版 呼出元 1件 [`00bdfbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbe0.md) · 呼出先 2件 [`00bdfbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbd0.md) [`00bdfbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b379cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37710.md#insn-00b379cc) · [`00b37b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37710.md#insn-00b37b10)
- 新版 `00b37a10`（命令位置の公開資料なし） · `00b37b54`（命令位置の公開資料なし）

~~~diff
- 00b379cc ["INT_ADD", "register:40f0:8", ["const:b379cc:8", "const:4:8"]]
- 00b379cc ["CALL", null, ["callee:00bdfbd0:8"]]
+ 00b37a10 ["INT_ADD", "register:40f0:8", ["const:b37a10:8", "const:4:8"]]
+ 00b37a10 ["CALL", null, ["callee:00bdfbd0:8"]]
- 00b379cc bytes 6da00294
+ 00b37a10 bytes 70a00294
- 00b37b10 ["INT_ADD", "register:40f0:8", ["const:b37b10:8", "const:4:8"]]
- 00b37b10 ["CALL", null, ["callee:00bdfbf0:8"]]
+ 00b37b54 ["INT_ADD", "register:40f0:8", ["const:b37b54:8", "const:4:8"]]
+ 00b37b54 ["CALL", null, ["callee:00bdfbf0:8"]]
- 00b37b10 bytes 24a00294
+ 00b37b54 bytes 27a00294
~~~


<a id="compare-efbbbeb96c9597f7ebdacad8ed5dff53"></a>

### [`00b37cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37cd8.md) → [`00b37d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b37/00b37d1c.md) _ZNK10reflection7RPCCall6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb80.md) · 呼出先 2件 [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)
- 新版 呼出元 1件 [`00bdfbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbd0.md) · 呼出先 2件 [`00bdfba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfba0.md) [`00bdfbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b37f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37cd8.md#insn-00b37f08) · [`00b37fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37cd8.md#insn-00b37fa0) · [`00b380cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37cd8.md#insn-00b380cc)
- 新版 `00b37f4c`（命令位置の公開資料なし） · `00b37fe4`（命令位置の公開資料なし） · `00b38110`（命令位置の公開資料なし）

~~~diff
- 00b37f08 ["INT_ADD", "register:40f0:8", ["const:b37f08:8", "const:4:8"]]
- 00b37f08 ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b37f4c ["INT_ADD", "register:40f0:8", ["const:b37f4c:8", "const:4:8"]]
+ 00b37f4c ["CALL", null, ["callee:00bdfba0:8"]]
- 00b37f08 bytes 129f0294
+ 00b37f4c bytes 159f0294
- 00b37fa0 ["INT_ADD", "register:40f0:8", ["const:b37fa0:8", "const:4:8"]]
- 00b37fa0 ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b37fe4 ["INT_ADD", "register:40f0:8", ["const:b37fe4:8", "const:4:8"]]
+ 00b37fe4 ["CALL", null, ["callee:00bdfba0:8"]]
- 00b37fa0 bytes ec9e0294
+ 00b37fe4 bytes ef9e0294
- 00b380cc ["INT_ADD", "register:40f0:8", ["const:b380cc:8", "const:4:8"]]
- 00b380cc ["CALL", null, ["callee:00bdfbf0:8"]]
+ 00b38110 ["INT_ADD", "register:40f0:8", ["const:b38110:8", "const:4:8"]]
+ 00b38110 ["CALL", null, ["callee:00bdfbf0:8"]]
- 00b380cc bytes b59e0294
+ 00b38110 bytes b89e0294
~~~


<a id="compare-c4dff54b2b9b82c09ce664aeeedcb74a"></a>

### [`00b38294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b38/00b38294.md) → [`00b382d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b38/00b382d8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdffa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffa0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfff0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b38330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b38/00b38294.md#insn-00b38330) · [`00b38370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b38/00b38294.md#insn-00b38370)
- 新版 `00b38374`（命令位置の公開資料なし） · `00b383b4`（命令位置の公開資料なし）

~~~diff
- 00b38330 ["INT_ADD", "register:40f0:8", ["const:b38330:8", "const:4:8"]]
- 00b38330 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b38374 ["INT_ADD", "register:40f0:8", ["const:b38374:8", "const:4:8"]]
+ 00b38374 ["CALL", null, ["callee:00bdb200:8"]]
- 00b38330 bytes a08b0294
+ 00b38374 bytes a38b0294
- 00b38370 ["INT_ADD", "register:40f0:8", ["const:b38370:8", "const:4:8"]]
- 00b38370 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b383b4 ["INT_ADD", "register:40f0:8", ["const:b383b4:8", "const:4:8"]]
+ 00b383b4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b38370 bytes 908b0294
+ 00b383b4 bytes 938b0294
~~~


<a id="compare-0903498fd35b011174262739cc9692d5"></a>

### [`00b391e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b391e8.md) → [`00b3922c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b3922c.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00e0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0130.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b39270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b391e8.md#insn-00b39270) · [`00b392c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b391e8.md#insn-00b392c0) · [`00b39354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b391e8.md#insn-00b39354)
- 新版 `00b392b4`（命令位置の公開資料なし） · `00b39304`（命令位置の公開資料なし） · `00b39398`（命令位置の公開資料なし）

~~~diff
- 00b39270 ["INT_ADD", "register:40f0:8", ["const:b39270:8", "const:4:8"]]
- 00b39270 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b392b4 ["INT_ADD", "register:40f0:8", ["const:b392b4:8", "const:4:8"]]
+ 00b392b4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b39270 bytes d0870294
+ 00b392b4 bytes d3870294
- 00b392c0 ["INT_ADD", "register:40f0:8", ["const:b392c0:8", "const:4:8"]]
- 00b392c0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b39304 ["INT_ADD", "register:40f0:8", ["const:b39304:8", "const:4:8"]]
+ 00b39304 ["CALL", null, ["callee:00bdb200:8"]]
- 00b392c0 bytes bc870294
+ 00b39304 bytes bf870294
- 00b39354 ["INT_ADD", "register:40f0:8", ["const:b39354:8", "const:4:8"]]
- 00b39354 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b39398 ["INT_ADD", "register:40f0:8", ["const:b39398:8", "const:4:8"]]
+ 00b39398 ["CALL", null, ["callee:00bdb200:8"]]
- 00b39354 bytes 97870294
+ 00b39398 bytes 9a870294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c139bc60e2a5bce6a4b5a522e83fa82"></a>

### [`00b39434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39434.md) → [`00b39478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b39478.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0140.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00e0.md)
- 新版 呼出元 1件 [`00be0190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0190.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b39468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39434.md#insn-00b39468) · [`00b394cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39434.md#insn-00b394cc) · [`00b39544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39434.md#insn-00b39544)
- 新版 `00b394ac`（命令位置の公開資料なし） · `00b39510`（命令位置の公開資料なし） · `00b39588`（命令位置の公開資料なし）

~~~diff
- 00b39468 ["INT_ADD", "register:40f0:8", ["const:b39468:8", "const:4:8"]]
- 00b39468 ["CALL", null, ["callee:00be0130:8"]]
+ 00b394ac ["INT_ADD", "register:40f0:8", ["const:b394ac:8", "const:4:8"]]
+ 00b394ac ["CALL", null, ["callee:00be0130:8"]]
- 00b39468 bytes 1e9b0294
+ 00b394ac bytes 219b0294
- 00b394cc ["INT_ADD", "register:40f0:8", ["const:b394cc:8", "const:4:8"]]
- 00b394cc ["CALL", null, ["callee:00bdb200:8"]]
+ 00b39510 ["INT_ADD", "register:40f0:8", ["const:b39510:8", "const:4:8"]]
+ 00b39510 ["CALL", null, ["callee:00bdb200:8"]]
- 00b394cc bytes 39870294
+ 00b39510 bytes 3c870294
- 00b39544 ["INT_ADD", "register:40f0:8", ["const:b39544:8", "const:4:8"]]
- 00b39544 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b39588 ["INT_ADD", "register:40f0:8", ["const:b39588:8", "const:4:8"]]
+ 00b39588 ["CALL", null, ["callee:00bdb200:8"]]
- 00b39544 bytes 1b870294
+ 00b39588 bytes 1e870294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08795e0ac48260257929595d0b1c5aae"></a>

### [`00b39618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39618.md) → [`00b3965c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b3965c.md) FUN_00b3965c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b38aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b38/00b38aa4.md) [`00b39a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39a2c.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be0140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0140.md)
- 新版 呼出元 2件 [`00b38ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b38/00b38ae8.md) [`00b39a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b39a70.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b39654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39618.md#insn-00b39654) · [`00b396b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39618.md#insn-00b396b8) · [`00b39738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39618.md#insn-00b39738)
- 新版 `00b39698`（命令位置の公開資料なし） · `00b396fc`（命令位置の公開資料なし） · `00b3977c`（命令位置の公開資料なし）

~~~diff
- 00b39654 ["INT_ADD", "register:40f0:8", ["const:b39654:8", "const:4:8"]]
- 00b39654 ["CALL", null, ["callee:00be0190:8"]]
+ 00b39698 ["INT_ADD", "register:40f0:8", ["const:b39698:8", "const:4:8"]]
+ 00b39698 ["CALL", null, ["callee:00be0190:8"]]
- 00b39654 bytes bb9a0294
+ 00b39698 bytes be9a0294
- 00b396b8 ["INT_ADD", "register:40f0:8", ["const:b396b8:8", "const:4:8"]]
- 00b396b8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b396fc ["INT_ADD", "register:40f0:8", ["const:b396fc:8", "const:4:8"]]
+ 00b396fc ["CALL", null, ["callee:00bdb200:8"]]
- 00b396b8 bytes be860294
+ 00b396fc bytes c1860294
- 00b39738 ["INT_ADD", "register:40f0:8", ["const:b39738:8", "const:4:8"]]
- 00b39738 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3977c ["INT_ADD", "register:40f0:8", ["const:b3977c:8", "const:4:8"]]
+ 00b3977c ["CALL", null, ["callee:00bdb200:8"]]
- 00b39738 bytes 9e860294
+ 00b3977c bytes a1860294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5854d06310483766344ad37af90dd35a"></a>

### [`00b39890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39890.md) → [`00b398d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b398d4.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS5_EEEEvT0_SB_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd20.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00e0.md)
- 新版 呼出元 1件 [`00bdfd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd70.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b398cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39890.md#insn-00b398cc) · [`00b39968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39890.md#insn-00b39968) · [`00b399e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39890.md#insn-00b399e4)
- 新版 `00b39910`（命令位置の公開資料なし） · `00b399ac`（命令位置の公開資料なし） · `00b39a28`（命令位置の公開資料なし）

~~~diff
- 00b398cc ["INT_ADD", "register:40f0:8", ["const:b398cc:8", "const:4:8"]]
- 00b398cc ["CALL", null, ["callee:00be0130:8"]]
+ 00b39910 ["INT_ADD", "register:40f0:8", ["const:b39910:8", "const:4:8"]]
+ 00b39910 ["CALL", null, ["callee:00be0130:8"]]
- 00b398cc bytes 059a0294
+ 00b39910 bytes 089a0294
- 00b39968 ["INT_ADD", "register:40f0:8", ["const:b39968:8", "const:4:8"]]
- 00b39968 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b399ac ["INT_ADD", "register:40f0:8", ["const:b399ac:8", "const:4:8"]]
+ 00b399ac ["CALL", null, ["callee:00bdb200:8"]]
- 00b39968 bytes 12860294
+ 00b399ac bytes 15860294
- 00b399e4 ["INT_ADD", "register:40f0:8", ["const:b399e4:8", "const:4:8"]]
- 00b399e4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b39a28 ["INT_ADD", "register:40f0:8", ["const:b39a28:8", "const:4:8"]]
+ 00b39a28 ["CALL", null, ["callee:00bdb200:8"]]
- 00b399e4 bytes f3850294
+ 00b39a28 bytes f6850294
~~~


<a id="compare-ce9bc29d4fa53ebe8caaad5e852ebf47"></a>

### [`00b39cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39cfc.md) → [`00b39d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b39d40.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection8KeyValueEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3e0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf430.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b39d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39cfc.md#insn-00b39d58)
- 新版 `00b39d9c`（命令位置の公開資料なし）

~~~diff
- 00b39d58 ["INT_ADD", "register:40f0:8", ["const:b39d58:8", "const:4:8"]]
- 00b39d58 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b39d9c ["INT_ADD", "register:40f0:8", ["const:b39d9c:8", "const:4:8"]]
+ 00b39d9c ["CALL", null, ["callee:00bdf390:8"]]
- 00b39d58 bytes 7a950294
+ 00b39d9c bytes 7d950294
~~~


<a id="compare-4cb332ca6f0a3724e574d78d2744ee24"></a>

### [`00b3a510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a510.md) → [`00b3a554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3a554.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0100.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3a598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a510.md#insn-00b3a598) · [`00b3a5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a510.md#insn-00b3a5e8) · [`00b3a67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a510.md#insn-00b3a67c)
- 新版 `00b3a5dc`（命令位置の公開資料なし） · `00b3a62c`（命令位置の公開資料なし） · `00b3a6c0`（命令位置の公開資料なし）

~~~diff
- 00b3a598 ["INT_ADD", "register:40f0:8", ["const:b3a598:8", "const:4:8"]]
- 00b3a598 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3a5dc ["INT_ADD", "register:40f0:8", ["const:b3a5dc:8", "const:4:8"]]
+ 00b3a5dc ["CALL", null, ["callee:00bdb200:8"]]
- 00b3a598 bytes 06830294
+ 00b3a5dc bytes 09830294
- 00b3a5e8 ["INT_ADD", "register:40f0:8", ["const:b3a5e8:8", "const:4:8"]]
- 00b3a5e8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3a62c ["INT_ADD", "register:40f0:8", ["const:b3a62c:8", "const:4:8"]]
+ 00b3a62c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3a5e8 bytes f2820294
+ 00b3a62c bytes f5820294
- 00b3a67c ["INT_ADD", "register:40f0:8", ["const:b3a67c:8", "const:4:8"]]
- 00b3a67c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3a6c0 ["INT_ADD", "register:40f0:8", ["const:b3a6c0:8", "const:4:8"]]
+ 00b3a6c0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3a67c bytes cd820294
+ 00b3a6c0 bytes d0820294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4146401003a7ac9e1d03d89ed4888881"></a>

### [`00b3a75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md) → [`00b3a7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3a7a0.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0110.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md)
- 新版 呼出元 1件 [`00be0160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0160.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3a790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md#insn-00b3a790) · [`00b3a7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md#insn-00b3a7f4) · [`00b3a86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md#insn-00b3a86c)
- 新版 `00b3a7d4`（命令位置の公開資料なし） · `00b3a838`（命令位置の公開資料なし） · `00b3a8b0`（命令位置の公開資料なし）

~~~diff
- 00b3a790 ["INT_ADD", "register:40f0:8", ["const:b3a790:8", "const:4:8"]]
- 00b3a790 ["CALL", null, ["callee:00be0100:8"]]
+ 00b3a7d4 ["INT_ADD", "register:40f0:8", ["const:b3a7d4:8", "const:4:8"]]
+ 00b3a7d4 ["CALL", null, ["callee:00be0100:8"]]
- 00b3a790 bytes 48960294
+ 00b3a7d4 bytes 4b960294
- 00b3a7f4 ["INT_ADD", "register:40f0:8", ["const:b3a7f4:8", "const:4:8"]]
- 00b3a7f4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3a838 ["INT_ADD", "register:40f0:8", ["const:b3a838:8", "const:4:8"]]
+ 00b3a838 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3a7f4 bytes 6f820294
+ 00b3a838 bytes 72820294
- 00b3a86c ["INT_ADD", "register:40f0:8", ["const:b3a86c:8", "const:4:8"]]
- 00b3a86c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3a8b0 ["INT_ADD", "register:40f0:8", ["const:b3a8b0:8", "const:4:8"]]
+ 00b3a8b0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3a86c bytes 51820294
+ 00b3a8b0 bytes 54820294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-525f26cc3433bfef0bd7724bde5ac0eb"></a>

### [`00b3a940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a940.md) → [`00b3a984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3a984.md) FUN_00b3a984

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b39dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39dcc.md) [`00b3ad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3ad54.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be0110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0110.md)
- 新版 呼出元 2件 [`00b39e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b39e10.md) [`00b3ad98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3ad98.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3a97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a940.md#insn-00b3a97c) · [`00b3a9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a940.md#insn-00b3a9e0) · [`00b3aa60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a940.md#insn-00b3aa60)
- 新版 `00b3a9c0`（命令位置の公開資料なし） · `00b3aa24`（命令位置の公開資料なし） · `00b3aaa4`（命令位置の公開資料なし）

~~~diff
- 00b3a97c ["INT_ADD", "register:40f0:8", ["const:b3a97c:8", "const:4:8"]]
- 00b3a97c ["CALL", null, ["callee:00be0160:8"]]
+ 00b3a9c0 ["INT_ADD", "register:40f0:8", ["const:b3a9c0:8", "const:4:8"]]
+ 00b3a9c0 ["CALL", null, ["callee:00be0160:8"]]
- 00b3a97c bytes e5950294
+ 00b3a9c0 bytes e8950294
- 00b3a9e0 ["INT_ADD", "register:40f0:8", ["const:b3a9e0:8", "const:4:8"]]
- 00b3a9e0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3aa24 ["INT_ADD", "register:40f0:8", ["const:b3aa24:8", "const:4:8"]]
+ 00b3aa24 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3a9e0 bytes f4810294
+ 00b3aa24 bytes f7810294
- 00b3aa60 ["INT_ADD", "register:40f0:8", ["const:b3aa60:8", "const:4:8"]]
- 00b3aa60 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3aaa4 ["INT_ADD", "register:40f0:8", ["const:b3aaa4:8", "const:4:8"]]
+ 00b3aaa4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3aa60 bytes d4810294
+ 00b3aaa4 bytes d7810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-071dc8853389ceddc262c7ade37b6d52"></a>

### [`00b3abb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md) → [`00b3abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3abfc.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfcf0.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md)
- 新版 呼出元 1件 [`00bdfd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd40.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3abf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md#insn-00b3abf4) · [`00b3ac90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md#insn-00b3ac90) · [`00b3ad0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md#insn-00b3ad0c)
- 新版 `00b3ac38`（命令位置の公開資料なし） · `00b3acd4`（命令位置の公開資料なし） · `00b3ad50`（命令位置の公開資料なし）

~~~diff
- 00b3abf4 ["INT_ADD", "register:40f0:8", ["const:b3abf4:8", "const:4:8"]]
- 00b3abf4 ["CALL", null, ["callee:00be0100:8"]]
+ 00b3ac38 ["INT_ADD", "register:40f0:8", ["const:b3ac38:8", "const:4:8"]]
+ 00b3ac38 ["CALL", null, ["callee:00be0100:8"]]
- 00b3abf4 bytes 2f950294
+ 00b3ac38 bytes 32950294
- 00b3ac90 ["INT_ADD", "register:40f0:8", ["const:b3ac90:8", "const:4:8"]]
- 00b3ac90 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3acd4 ["INT_ADD", "register:40f0:8", ["const:b3acd4:8", "const:4:8"]]
+ 00b3acd4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3ac90 bytes 48810294
+ 00b3acd4 bytes 4b810294
- 00b3ad0c ["INT_ADD", "register:40f0:8", ["const:b3ad0c:8", "const:4:8"]]
- 00b3ad0c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3ad50 ["INT_ADD", "register:40f0:8", ["const:b3ad50:8", "const:4:8"]]
+ 00b3ad50 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3ad0c bytes 29810294
+ 00b3ad50 bytes 2c810294
~~~


<a id="compare-c40ccff4968efa54ea8ca13fcb6a1745"></a>

### [`00b3b024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b024.md) → [`00b3b068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3b068.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection5FieldEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf390.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3e0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b024.md#insn-00b3b080)
- 新版 `00b3b0c4`（命令位置の公開資料なし）

~~~diff
- 00b3b080 ["INT_ADD", "register:40f0:8", ["const:b3b080:8", "const:4:8"]]
- 00b3b080 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3b0c4 ["INT_ADD", "register:40f0:8", ["const:b3b0c4:8", "const:4:8"]]
+ 00b3b0c4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b3b080 bytes b0900294
+ 00b3b0c4 bytes b3900294
~~~


<a id="compare-6efc3551c1ab1d1e2c2815fae1016971"></a>

### [`00b3b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b838.md) → [`00b3b87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3b87c.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0110.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b838.md#insn-00b3b8c0) · [`00b3b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b838.md#insn-00b3b910) · [`00b3b9a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b838.md#insn-00b3b9a4)
- 新版 `00b3b904`（命令位置の公開資料なし） · `00b3b954`（命令位置の公開資料なし） · `00b3b9e8`（命令位置の公開資料なし）

~~~diff
- 00b3b8c0 ["INT_ADD", "register:40f0:8", ["const:b3b8c0:8", "const:4:8"]]
- 00b3b8c0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3b904 ["INT_ADD", "register:40f0:8", ["const:b3b904:8", "const:4:8"]]
+ 00b3b904 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3b8c0 bytes 3c7e0294
+ 00b3b904 bytes 3f7e0294
- 00b3b910 ["INT_ADD", "register:40f0:8", ["const:b3b910:8", "const:4:8"]]
- 00b3b910 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3b954 ["INT_ADD", "register:40f0:8", ["const:b3b954:8", "const:4:8"]]
+ 00b3b954 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3b910 bytes 287e0294
+ 00b3b954 bytes 2b7e0294
- 00b3b9a4 ["INT_ADD", "register:40f0:8", ["const:b3b9a4:8", "const:4:8"]]
- 00b3b9a4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3b9e8 ["INT_ADD", "register:40f0:8", ["const:b3b9e8:8", "const:4:8"]]
+ 00b3b9e8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3b9a4 bytes 037e0294
+ 00b3b9e8 bytes 067e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-698c0ffaeb2006825fe88d92c263328e"></a>

### [`00b3ba84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3ba84.md) → [`00b3bac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3bac8.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0120.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md)
- 新版 呼出元 1件 [`00be0170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0170.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3bab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3ba84.md#insn-00b3bab8) · [`00b3bb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3ba84.md#insn-00b3bb1c) · [`00b3bb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3ba84.md#insn-00b3bb94)
- 新版 `00b3bafc`（命令位置の公開資料なし） · `00b3bb60`（命令位置の公開資料なし） · `00b3bbd8`（命令位置の公開資料なし）

~~~diff
- 00b3bab8 ["INT_ADD", "register:40f0:8", ["const:b3bab8:8", "const:4:8"]]
- 00b3bab8 ["CALL", null, ["callee:00be0110:8"]]
+ 00b3bafc ["INT_ADD", "register:40f0:8", ["const:b3bafc:8", "const:4:8"]]
+ 00b3bafc ["CALL", null, ["callee:00be0110:8"]]
- 00b3bab8 bytes 82910294
+ 00b3bafc bytes 85910294
- 00b3bb1c ["INT_ADD", "register:40f0:8", ["const:b3bb1c:8", "const:4:8"]]
- 00b3bb1c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3bb60 ["INT_ADD", "register:40f0:8", ["const:b3bb60:8", "const:4:8"]]
+ 00b3bb60 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3bb1c bytes a57d0294
+ 00b3bb60 bytes a87d0294
- 00b3bb94 ["INT_ADD", "register:40f0:8", ["const:b3bb94:8", "const:4:8"]]
- 00b3bb94 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3bbd8 ["INT_ADD", "register:40f0:8", ["const:b3bbd8:8", "const:4:8"]]
+ 00b3bbd8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3bb94 bytes 877d0294
+ 00b3bbd8 bytes 8a7d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da81e6ad7af607fd23b1f6af2840b287"></a>

### [`00b3bc68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bc68.md) → [`00b3bcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3bcac.md) FUN_00b3bcac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b3b0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b0f4.md) [`00b3c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c07c.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be0120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0120.md)
- 新版 呼出元 2件 [`00b3b138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3b138.md) [`00b3c0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3c0c0.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3bca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bc68.md#insn-00b3bca4) · [`00b3bd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bc68.md#insn-00b3bd08) · [`00b3bd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bc68.md#insn-00b3bd88)
- 新版 `00b3bce8`（命令位置の公開資料なし） · `00b3bd4c`（命令位置の公開資料なし） · `00b3bdcc`（命令位置の公開資料なし）

~~~diff
- 00b3bca4 ["INT_ADD", "register:40f0:8", ["const:b3bca4:8", "const:4:8"]]
- 00b3bca4 ["CALL", null, ["callee:00be0170:8"]]
+ 00b3bce8 ["INT_ADD", "register:40f0:8", ["const:b3bce8:8", "const:4:8"]]
+ 00b3bce8 ["CALL", null, ["callee:00be0170:8"]]
- 00b3bca4 bytes 1f910294
+ 00b3bce8 bytes 22910294
- 00b3bd08 ["INT_ADD", "register:40f0:8", ["const:b3bd08:8", "const:4:8"]]
- 00b3bd08 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3bd4c ["INT_ADD", "register:40f0:8", ["const:b3bd4c:8", "const:4:8"]]
+ 00b3bd4c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3bd08 bytes 2a7d0294
+ 00b3bd4c bytes 2d7d0294
- 00b3bd88 ["INT_ADD", "register:40f0:8", ["const:b3bd88:8", "const:4:8"]]
- 00b3bd88 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3bdcc ["INT_ADD", "register:40f0:8", ["const:b3bdcc:8", "const:4:8"]]
+ 00b3bdcc ["CALL", null, ["callee:00bdb200:8"]]
- 00b3bd88 bytes 0a7d0294
+ 00b3bdcc bytes 0d7d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2c200721ecd24c8b4f90d5d5f7fa5f4"></a>

### [`00b3bee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md) → [`00b3bf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3bf24.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd00.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md)
- 新版 呼出元 1件 [`00bdfd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd50.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3bf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md#insn-00b3bf1c) · [`00b3bfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md#insn-00b3bfb8) · [`00b3c034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md#insn-00b3c034)
- 新版 `00b3bf60`（命令位置の公開資料なし） · `00b3bffc`（命令位置の公開資料なし） · `00b3c078`（命令位置の公開資料なし）

~~~diff
- 00b3bf1c ["INT_ADD", "register:40f0:8", ["const:b3bf1c:8", "const:4:8"]]
- 00b3bf1c ["CALL", null, ["callee:00be0110:8"]]
+ 00b3bf60 ["INT_ADD", "register:40f0:8", ["const:b3bf60:8", "const:4:8"]]
+ 00b3bf60 ["CALL", null, ["callee:00be0110:8"]]
- 00b3bf1c bytes 69900294
+ 00b3bf60 bytes 6c900294
- 00b3bfb8 ["INT_ADD", "register:40f0:8", ["const:b3bfb8:8", "const:4:8"]]
- 00b3bfb8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3bffc ["INT_ADD", "register:40f0:8", ["const:b3bffc:8", "const:4:8"]]
+ 00b3bffc ["CALL", null, ["callee:00bdb200:8"]]
- 00b3bfb8 bytes 7e7c0294
+ 00b3bffc bytes 817c0294
- 00b3c034 ["INT_ADD", "register:40f0:8", ["const:b3c034:8", "const:4:8"]]
- 00b3c034 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3c078 ["INT_ADD", "register:40f0:8", ["const:b3c078:8", "const:4:8"]]
+ 00b3c078 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3c034 bytes 5f7c0294
+ 00b3c078 bytes 627c0294
~~~


<a id="compare-6b8c98b6026ff330d1cd3396f747238e"></a>

### [`00b3c34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c34c.md) → [`00b3c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3c390.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection6ObjectEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3a0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3f0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3c3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c34c.md#insn-00b3c3a8)
- 新版 `00b3c3ec`（命令位置の公開資料なし）

~~~diff
- 00b3c3a8 ["INT_ADD", "register:40f0:8", ["const:b3c3a8:8", "const:4:8"]]
- 00b3c3a8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3c3ec ["INT_ADD", "register:40f0:8", ["const:b3c3ec:8", "const:4:8"]]
+ 00b3c3ec ["CALL", null, ["callee:00bdf390:8"]]
- 00b3c3a8 bytes e68b0294
+ 00b3c3ec bytes e98b0294
~~~


<a id="compare-559adcf3da4c0a447f85307f6a5f494b"></a>

### [`00b3cb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cb60.md) → [`00b3cba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cba4.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be00f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00f0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3cbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cb60.md#insn-00b3cbe8) · [`00b3cc38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cb60.md#insn-00b3cc38) · [`00b3cccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cb60.md#insn-00b3cccc)
- 新版 `00b3cc2c`（命令位置の公開資料なし） · `00b3cc7c`（命令位置の公開資料なし） · `00b3cd10`（命令位置の公開資料なし）

~~~diff
- 00b3cbe8 ["INT_ADD", "register:40f0:8", ["const:b3cbe8:8", "const:4:8"]]
- 00b3cbe8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3cc2c ["INT_ADD", "register:40f0:8", ["const:b3cc2c:8", "const:4:8"]]
+ 00b3cc2c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3cbe8 bytes 72790294
+ 00b3cc2c bytes 75790294
- 00b3cc38 ["INT_ADD", "register:40f0:8", ["const:b3cc38:8", "const:4:8"]]
- 00b3cc38 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3cc7c ["INT_ADD", "register:40f0:8", ["const:b3cc7c:8", "const:4:8"]]
+ 00b3cc7c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3cc38 bytes 5e790294
+ 00b3cc7c bytes 61790294
- 00b3cccc ["INT_ADD", "register:40f0:8", ["const:b3cccc:8", "const:4:8"]]
- 00b3cccc ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3cd10 ["INT_ADD", "register:40f0:8", ["const:b3cd10:8", "const:4:8"]]
+ 00b3cd10 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3cccc bytes 39790294
+ 00b3cd10 bytes 3c790294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ac47a4b989677fa3c812f26c5968d76"></a>

### [`00b3cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md) → [`00b3cdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cdf0.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0100.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md)
- 新版 呼出元 1件 [`00be0150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0150.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be00f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3cde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md#insn-00b3cde0) · [`00b3ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md#insn-00b3ce44) · [`00b3cebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md#insn-00b3cebc)
- 新版 `00b3ce24`（命令位置の公開資料なし） · `00b3ce88`（命令位置の公開資料なし） · `00b3cf00`（命令位置の公開資料なし）

~~~diff
- 00b3cde0 ["INT_ADD", "register:40f0:8", ["const:b3cde0:8", "const:4:8"]]
- 00b3cde0 ["CALL", null, ["callee:00be00f0:8"]]
+ 00b3ce24 ["INT_ADD", "register:40f0:8", ["const:b3ce24:8", "const:4:8"]]
+ 00b3ce24 ["CALL", null, ["callee:00be00f0:8"]]
- 00b3cde0 bytes b08c0294
+ 00b3ce24 bytes b38c0294
- 00b3ce44 ["INT_ADD", "register:40f0:8", ["const:b3ce44:8", "const:4:8"]]
- 00b3ce44 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3ce88 ["INT_ADD", "register:40f0:8", ["const:b3ce88:8", "const:4:8"]]
+ 00b3ce88 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3ce44 bytes db780294
+ 00b3ce88 bytes de780294
- 00b3cebc ["INT_ADD", "register:40f0:8", ["const:b3cebc:8", "const:4:8"]]
- 00b3cebc ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3cf00 ["INT_ADD", "register:40f0:8", ["const:b3cf00:8", "const:4:8"]]
+ 00b3cf00 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3cebc bytes bd780294
+ 00b3cf00 bytes c0780294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

