# v15.7.3 → v15.7.4 · 要調査の変更候補 (4)

[一覧の目次](README.md)

<a id="compare-60b81efa0013fded99c854c4dcfcfdbc"></a>

### [`00a95c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95c6c.md) → [`00a95cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95cb0.md) FUN_00a95cb0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95c6c.md#insn-00a95c88)
- 新版 `00a95ccc`（命令位置の公開資料なし）

~~~diff
- 00a95c88 ["INT_ADD", "register:40f0:8", ["const:a95c88:8", "const:4:8"]]
- 00a95c88 ["CALL", null, ["callee:0081f580:8"]]
+ 00a95ccc ["INT_ADD", "register:40f0:8", ["const:a95ccc:8", "const:4:8"]]
+ 00a95ccc ["CALL", null, ["callee:0081f580:8"]]
- 00a95c88 bytes 3e26f697
+ 00a95ccc bytes 2d26f697
~~~


<a id="compare-407e8d5d966ec6fa125df1697c6329d9"></a>

### [`00a95cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95cb8.md) → [`00a95cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95cfc.md) FUN_00a95cfc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95cb8.md#insn-00a95ccc)
- 新版 `00a95d10`（命令位置の公開資料なし）

~~~diff
- 00a95ccc ["INT_ADD", "register:40f0:8", ["const:a95ccc:8", "const:4:8"]]
- 00a95ccc ["CALL", null, ["callee:0081f580:8"]]
+ 00a95d10 ["INT_ADD", "register:40f0:8", ["const:a95d10:8", "const:4:8"]]
+ 00a95d10 ["CALL", null, ["callee:0081f580:8"]]
- 00a95ccc bytes 2d26f697
+ 00a95d10 bytes 1c26f697
~~~


<a id="compare-f057d05d1d1c5dcac72a09b250d49296"></a>

### [`00a95cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95cf8.md) → [`00a95d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95d3c.md) FUN_00a95d3c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95cf8.md#insn-00a95d14)
- 新版 `00a95d58`（命令位置の公開資料なし）

~~~diff
- 00a95d14 ["INT_ADD", "register:40f0:8", ["const:a95d14:8", "const:4:8"]]
- 00a95d14 ["CALL", null, ["callee:0081f580:8"]]
+ 00a95d58 ["INT_ADD", "register:40f0:8", ["const:a95d58:8", "const:4:8"]]
+ 00a95d58 ["CALL", null, ["callee:0081f580:8"]]
- 00a95d14 bytes 1b26f697
+ 00a95d58 bytes 0a26f697
~~~


<a id="compare-f5269dea468652950e9437b91a931d47"></a>

### [`00a95d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95d44.md) → [`00a95d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95d88.md) FUN_00a95d88

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d6740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6740.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`005d6740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6740.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95d44.md#insn-00a95d58)
- 新版 `00a95d9c`（命令位置の公開資料なし）

~~~diff
- 00a95d58 ["INT_ADD", "register:40f0:8", ["const:a95d58:8", "const:4:8"]]
- 00a95d58 ["CALL", null, ["callee:0081f580:8"]]
+ 00a95d9c ["INT_ADD", "register:40f0:8", ["const:a95d9c:8", "const:4:8"]]
+ 00a95d9c ["CALL", null, ["callee:0081f580:8"]]
- 00a95d58 bytes 0a26f697
+ 00a95d9c bytes f925f697
~~~


<a id="compare-f071c6aef0842eef408d6f768e99df27"></a>

### [`00a95d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95d84.md) → [`00a95dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95dc8.md) FUN_00a95dc8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a931f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a931f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a9323c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a9323c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95d84.md#insn-00a95da0)
- 新版 `00a95de4`（命令位置の公開資料なし）

~~~diff
- 00a95da0 ["INT_ADD", "register:40f0:8", ["const:a95da0:8", "const:4:8"]]
- 00a95da0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a95de4 ["INT_ADD", "register:40f0:8", ["const:a95de4:8", "const:4:8"]]
+ 00a95de4 ["CALL", null, ["callee:0081f580:8"]]
- 00a95da0 bytes f825f697
+ 00a95de4 bytes e725f697
~~~


<a id="compare-0a368fc9a51187a690ff8111b5750070"></a>

### [`00a95dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95dd0.md) → [`00a95e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95e14.md) FUN_00a95e14

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a93204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93204.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a93248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93248.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95dd0.md#insn-00a95dec)
- 新版 `00a95e30`（命令位置の公開資料なし）

~~~diff
- 00a95dec ["INT_ADD", "register:40f0:8", ["const:a95dec:8", "const:4:8"]]
- 00a95dec ["CALL", null, ["callee:0081f580:8"]]
+ 00a95e30 ["INT_ADD", "register:40f0:8", ["const:a95e30:8", "const:4:8"]]
+ 00a95e30 ["CALL", null, ["callee:0081f580:8"]]
- 00a95dec bytes e525f697
+ 00a95e30 bytes d425f697
~~~


<a id="compare-bd5e636fbfd6767a44dffa96a1f7af12"></a>

### [`00a95e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95e1c.md) → [`00a95e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95e60.md) FUN_00a95e60

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95e1c.md#insn-00a95e3c)
- 新版 `00a95e80`（命令位置の公開資料なし）

~~~diff
- 00a95e3c ["INT_ADD", "register:40f0:8", ["const:a95e3c:8", "const:4:8"]]
- 00a95e3c ["CALL", null, ["callee:0081f580:8"]]
+ 00a95e80 ["INT_ADD", "register:40f0:8", ["const:a95e80:8", "const:4:8"]]
+ 00a95e80 ["CALL", null, ["callee:0081f580:8"]]
- 00a95e3c bytes d125f697
+ 00a95e80 bytes c025f697
~~~


<a id="compare-b9ce50ad7056b3f4c3e2674f62a9507c"></a>

### [`00a95e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95e7c.md) → [`00a95ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95ec0.md) FUN_00a95ec0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006ec9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006ec9f4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006ec9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006ec9f4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95e7c.md#insn-00a95e90)
- 新版 `00a95ed4`（命令位置の公開資料なし）

~~~diff
- 00a95e90 ["INT_ADD", "register:40f0:8", ["const:a95e90:8", "const:4:8"]]
- 00a95e90 ["CALL", null, ["callee:0081f580:8"]]
+ 00a95ed4 ["INT_ADD", "register:40f0:8", ["const:a95ed4:8", "const:4:8"]]
+ 00a95ed4 ["CALL", null, ["callee:0081f580:8"]]
- 00a95e90 bytes bc25f697
+ 00a95ed4 bytes ab25f697
~~~


<a id="compare-59b3286b58a406816f3e8ed235affdda"></a>

### [`00a95ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95ebc.md) → [`00a95f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95f00.md) FUN_00a95f00

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95ebc.md#insn-00a95ed8)
- 新版 `00a95f1c`（命令位置の公開資料なし）

~~~diff
- 00a95ed8 ["INT_ADD", "register:40f0:8", ["const:a95ed8:8", "const:4:8"]]
- 00a95ed8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a95f1c ["INT_ADD", "register:40f0:8", ["const:a95f1c:8", "const:4:8"]]
+ 00a95f1c ["CALL", null, ["callee:0081f580:8"]]
- 00a95ed8 bytes aa25f697
+ 00a95f1c bytes 9925f697
~~~


<a id="compare-3c98e8588f3bb1b300633b937ee7c354"></a>

### [`00a95f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95f08.md) → [`00a95f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95f4c.md) FUN_00a95f4c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95f08.md#insn-00a95f24)
- 新版 `00a95f68`（命令位置の公開資料なし）

~~~diff
- 00a95f24 ["INT_ADD", "register:40f0:8", ["const:a95f24:8", "const:4:8"]]
- 00a95f24 ["CALL", null, ["callee:0081f580:8"]]
+ 00a95f68 ["INT_ADD", "register:40f0:8", ["const:a95f68:8", "const:4:8"]]
+ 00a95f68 ["CALL", null, ["callee:0081f580:8"]]
- 00a95f24 bytes 9725f697
+ 00a95f68 bytes 8625f697
~~~


<a id="compare-8ef0e53e7d565fcf985b760a829096e9"></a>

### [`00a95f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95f6c.md) → [`00a95fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a95/00a95fb0.md) FUN_00a95fb0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95f6c.md#insn-00a95f8c)
- 新版 `00a95fd0`（命令位置の公開資料なし）

~~~diff
- 00a95f8c ["INT_ADD", "register:40f0:8", ["const:a95f8c:8", "const:4:8"]]
- 00a95f8c ["CALL", null, ["callee:0081f580:8"]]
+ 00a95fd0 ["INT_ADD", "register:40f0:8", ["const:a95fd0:8", "const:4:8"]]
+ 00a95fd0 ["CALL", null, ["callee:0081f580:8"]]
- 00a95f8c bytes 7d25f697
+ 00a95fd0 bytes 6c25f697
~~~


<a id="compare-bbbddc7363f36cfef77b61042b7b4bff"></a>

### [`00a95fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95fcc.md) → [`00a96010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96010.md) FUN_00a96010

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a95fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a95/00a95fcc.md#insn-00a95fe0)
- 新版 `00a96024`（命令位置の公開資料なし）

~~~diff
- 00a95fe0 ["INT_ADD", "register:40f0:8", ["const:a95fe0:8", "const:4:8"]]
- 00a95fe0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a96024 ["INT_ADD", "register:40f0:8", ["const:a96024:8", "const:4:8"]]
+ 00a96024 ["CALL", null, ["callee:0081f580:8"]]
- 00a95fe0 bytes 6825f697
+ 00a96024 bytes 5725f697
~~~


<a id="compare-8f94a0b0748683d19c398aa421b7e3f5"></a>

### [`00a9600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a9600c.md) → [`00a96050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96050.md) FUN_00a96050

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a9600c.md#insn-00a96028)
- 新版 `00a9606c`（命令位置の公開資料なし）

~~~diff
- 00a96028 ["INT_ADD", "register:40f0:8", ["const:a96028:8", "const:4:8"]]
- 00a96028 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9606c ["INT_ADD", "register:40f0:8", ["const:a9606c:8", "const:4:8"]]
+ 00a9606c ["CALL", null, ["callee:0081f580:8"]]
- 00a96028 bytes 5625f697
+ 00a9606c bytes 4525f697
~~~


<a id="compare-25ef623698ae24ae6221769cc8b0393e"></a>

### [`00a96058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96058.md) → [`00a9609c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a9609c.md) FUN_00a9609c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96058.md#insn-00a96074)
- 新版 `00a960b8`（命令位置の公開資料なし）

~~~diff
- 00a96074 ["INT_ADD", "register:40f0:8", ["const:a96074:8", "const:4:8"]]
- 00a96074 ["CALL", null, ["callee:0081f580:8"]]
+ 00a960b8 ["INT_ADD", "register:40f0:8", ["const:a960b8:8", "const:4:8"]]
+ 00a960b8 ["CALL", null, ["callee:0081f580:8"]]
- 00a96074 bytes 4325f697
+ 00a960b8 bytes 3225f697
~~~


<a id="compare-bfd460b016e70b07d1b66f2b2eea8910"></a>

### [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) → [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) FUN_00a960f0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 17件 [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`005bc1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc1dc.md) [`005bce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bce20.md) [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 17件 [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`005bc1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md) [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a960c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md#insn-00a960c8) · [`00a960dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md#insn-00a960dc) · [`00a96100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md#insn-00a96100)
- 新版 `00a9610c`（命令位置の公開資料なし） · `00a96120`（命令位置の公開資料なし） · `00a96144`（命令位置の公開資料なし）

~~~diff
- 00a960c8 ["INT_ADD", "register:40f0:8", ["const:a960c8:8", "const:4:8"]]
- 00a960c8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9610c ["INT_ADD", "register:40f0:8", ["const:a9610c:8", "const:4:8"]]
+ 00a9610c ["CALL", null, ["callee:0081f580:8"]]
- 00a960c8 bytes 2e25f697
+ 00a9610c bytes 1d25f697
- 00a960dc ["INT_ADD", "register:40f0:8", ["const:a960dc:8", "const:4:8"]]
- 00a960dc ["CALL", null, ["callee:005c2710:8"]]
+ 00a96120 ["INT_ADD", "register:40f0:8", ["const:a96120:8", "const:4:8"]]
+ 00a96120 ["CALL", null, ["callee:005c2710:8"]]
- 00a960dc bytes 8db1ec97
+ 00a96120 bytes 7cb1ec97
- 00a96100 ["INT_ADD", "register:40f0:8", ["const:a96100:8", "const:4:8"]]
- 00a96100 ["CALL", null, ["callee:0081f580:8"]]
+ 00a96144 ["INT_ADD", "register:40f0:8", ["const:a96144:8", "const:4:8"]]
+ 00a96144 ["CALL", null, ["callee:0081f580:8"]]
- 00a96100 bytes 2025f697
+ 00a96144 bytes 0f25f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94e73841661ac735fac73d470b59fe7b"></a>

### [`00a96b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b18.md) → [`00a96b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96b5c.md) FUN_00a96b5c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b18.md#insn-00a96b2c) · [`00a96b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b18.md#insn-00a96b40) · [`00a96b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b18.md#insn-00a96b4c)
- 新版 `00a96b70`（命令位置の公開資料なし） · `00a96b84`（命令位置の公開資料なし） · `00a96b90`（命令位置の公開資料なし）

~~~diff
- 00a96b2c ["INT_ADD", "register:40f0:8", ["const:a96b2c:8", "const:4:8"]]
- 00a96b2c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96b70 ["INT_ADD", "register:40f0:8", ["const:a96b70:8", "const:4:8"]]
+ 00a96b70 ["CALL", null, ["callee:0081f580:8"]]
- 00a96b2c bytes 9522f697
+ 00a96b70 bytes 8422f697
- 00a96b40 ["INT_ADD", "register:40f0:8", ["const:a96b40:8", "const:4:8"]]
- 00a96b40 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96b84 ["INT_ADD", "register:40f0:8", ["const:a96b84:8", "const:4:8"]]
+ 00a96b84 ["CALL", null, ["callee:005c2710:8"]]
- 00a96b40 bytes f4aeec97
+ 00a96b84 bytes e3aeec97
- 00a96b4c ["INT_ADD", "register:40f0:8", ["const:a96b4c:8", "const:4:8"]]
- 00a96b4c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96b90 ["INT_ADD", "register:40f0:8", ["const:a96b90:8", "const:4:8"]]
+ 00a96b90 ["CALL", null, ["callee:0081f580:8"]]
- 00a96b4c bytes 8d22f697
+ 00a96b90 bytes 7c22f697
~~~


<a id="compare-92aae4a1b6e2d2c91ad17840bcf58a20"></a>

### [`00a96b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b88.md) → [`00a96bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96bcc.md) FUN_00a96bcc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b88.md#insn-00a96b9c) · [`00a96bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b88.md#insn-00a96bb0) · [`00a96bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96b88.md#insn-00a96bc4)
- 新版 `00a96be0`（命令位置の公開資料なし） · `00a96bf4`（命令位置の公開資料なし） · `00a96c08`（命令位置の公開資料なし）

~~~diff
- 00a96b9c ["INT_ADD", "register:40f0:8", ["const:a96b9c:8", "const:4:8"]]
- 00a96b9c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96be0 ["INT_ADD", "register:40f0:8", ["const:a96be0:8", "const:4:8"]]
+ 00a96be0 ["CALL", null, ["callee:0081f580:8"]]
- 00a96b9c bytes 7922f697
+ 00a96be0 bytes 6822f697
- 00a96bb0 ["INT_ADD", "register:40f0:8", ["const:a96bb0:8", "const:4:8"]]
- 00a96bb0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96bf4 ["INT_ADD", "register:40f0:8", ["const:a96bf4:8", "const:4:8"]]
+ 00a96bf4 ["CALL", null, ["callee:005c2710:8"]]
- 00a96bb0 bytes d8aeec97
+ 00a96bf4 bytes c7aeec97
- 00a96bc4 ["INT_ADD", "register:40f0:8", ["const:a96bc4:8", "const:4:8"]]
- 00a96bc4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a96c08 ["INT_ADD", "register:40f0:8", ["const:a96c08:8", "const:4:8"]]
+ 00a96c08 ["CALL", null, ["callee:0081f580:8"]]
- 00a96bc4 bytes 6f22f697
+ 00a96c08 bytes 5e22f697
~~~


<a id="compare-fd618eda168fcaac241852f2340ca86e"></a>

### [`00a96e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96e38.md) → [`00a96e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96e7c.md) FUN_00a96e7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96e38.md#insn-00a96e4c) · [`00a96e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96e38.md#insn-00a96e60) · [`00a96e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96e38.md#insn-00a96e6c)
- 新版 `00a96e90`（命令位置の公開資料なし） · `00a96ea4`（命令位置の公開資料なし） · `00a96eb0`（命令位置の公開資料なし）

~~~diff
- 00a96e4c ["INT_ADD", "register:40f0:8", ["const:a96e4c:8", "const:4:8"]]
- 00a96e4c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96e90 ["INT_ADD", "register:40f0:8", ["const:a96e90:8", "const:4:8"]]
+ 00a96e90 ["CALL", null, ["callee:0081f580:8"]]
- 00a96e4c bytes cd21f697
+ 00a96e90 bytes bc21f697
- 00a96e60 ["INT_ADD", "register:40f0:8", ["const:a96e60:8", "const:4:8"]]
- 00a96e60 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96ea4 ["INT_ADD", "register:40f0:8", ["const:a96ea4:8", "const:4:8"]]
+ 00a96ea4 ["CALL", null, ["callee:005c2710:8"]]
- 00a96e60 bytes 2caeec97
+ 00a96ea4 bytes 1baeec97
- 00a96e6c ["INT_ADD", "register:40f0:8", ["const:a96e6c:8", "const:4:8"]]
- 00a96e6c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96eb0 ["INT_ADD", "register:40f0:8", ["const:a96eb0:8", "const:4:8"]]
+ 00a96eb0 ["CALL", null, ["callee:0081f580:8"]]
- 00a96e6c bytes c521f697
+ 00a96eb0 bytes b421f697
~~~


<a id="compare-af99a36207cc86fde3b9f140b6ccce8f"></a>

### [`00a96f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f18.md) → [`00a96f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96f5c.md) FUN_00a96f5c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f18.md#insn-00a96f2c) · [`00a96f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f18.md#insn-00a96f40) · [`00a96f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f18.md#insn-00a96f4c)
- 新版 `00a96f70`（命令位置の公開資料なし） · `00a96f84`（命令位置の公開資料なし） · `00a96f90`（命令位置の公開資料なし）

~~~diff
- 00a96f2c ["INT_ADD", "register:40f0:8", ["const:a96f2c:8", "const:4:8"]]
- 00a96f2c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96f70 ["INT_ADD", "register:40f0:8", ["const:a96f70:8", "const:4:8"]]
+ 00a96f70 ["CALL", null, ["callee:0081f580:8"]]
- 00a96f2c bytes 9521f697
+ 00a96f70 bytes 8421f697
- 00a96f40 ["INT_ADD", "register:40f0:8", ["const:a96f40:8", "const:4:8"]]
- 00a96f40 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96f84 ["INT_ADD", "register:40f0:8", ["const:a96f84:8", "const:4:8"]]
+ 00a96f84 ["CALL", null, ["callee:005c2710:8"]]
- 00a96f40 bytes f4adec97
+ 00a96f84 bytes e3adec97
- 00a96f4c ["INT_ADD", "register:40f0:8", ["const:a96f4c:8", "const:4:8"]]
- 00a96f4c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96f90 ["INT_ADD", "register:40f0:8", ["const:a96f90:8", "const:4:8"]]
+ 00a96f90 ["CALL", null, ["callee:0081f580:8"]]
- 00a96f4c bytes 8d21f697
+ 00a96f90 bytes 7c21f697
~~~


<a id="compare-f2986d9766792e70a15422f0f2d4281a"></a>

### [`00a96f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f88.md) → [`00a96fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96fcc.md) FUN_00a96fcc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f88.md#insn-00a96f9c) · [`00a96fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f88.md#insn-00a96fb0) · [`00a96fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96f88.md#insn-00a96fc4)
- 新版 `00a96fe0`（命令位置の公開資料なし） · `00a96ff4`（命令位置の公開資料なし） · `00a97008`（命令位置の公開資料なし）

~~~diff
- 00a96f9c ["INT_ADD", "register:40f0:8", ["const:a96f9c:8", "const:4:8"]]
- 00a96f9c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96fe0 ["INT_ADD", "register:40f0:8", ["const:a96fe0:8", "const:4:8"]]
+ 00a96fe0 ["CALL", null, ["callee:0081f580:8"]]
- 00a96f9c bytes 7921f697
+ 00a96fe0 bytes 6821f697
- 00a96fb0 ["INT_ADD", "register:40f0:8", ["const:a96fb0:8", "const:4:8"]]
- 00a96fb0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96ff4 ["INT_ADD", "register:40f0:8", ["const:a96ff4:8", "const:4:8"]]
+ 00a96ff4 ["CALL", null, ["callee:005c2710:8"]]
- 00a96fb0 bytes d8adec97
+ 00a96ff4 bytes c7adec97
- 00a96fc4 ["INT_ADD", "register:40f0:8", ["const:a96fc4:8", "const:4:8"]]
- 00a96fc4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97008 ["INT_ADD", "register:40f0:8", ["const:a97008:8", "const:4:8"]]
+ 00a97008 ["CALL", null, ["callee:0081f580:8"]]
- 00a96fc4 bytes 6f21f697
+ 00a97008 bytes 5e21f697
~~~


<a id="compare-0efe702476ead1595d9262beeb1d0b33"></a>

### [`00a96ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ff8.md) → [`00a9703c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a9703c.md) FUN_00a9703c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005d6740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6740.md) [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 7件 [`005d6740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6740.md) [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9700c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ff8.md#insn-00a9700c) · [`00a97020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ff8.md#insn-00a97020) · [`00a9702c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ff8.md#insn-00a9702c)
- 新版 `00a97050`（命令位置の公開資料なし） · `00a97064`（命令位置の公開資料なし） · `00a97070`（命令位置の公開資料なし）

~~~diff
- 00a9700c ["INT_ADD", "register:40f0:8", ["const:a9700c:8", "const:4:8"]]
- 00a9700c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97050 ["INT_ADD", "register:40f0:8", ["const:a97050:8", "const:4:8"]]
+ 00a97050 ["CALL", null, ["callee:0081f580:8"]]
- 00a9700c bytes 5d21f697
+ 00a97050 bytes 4c21f697
- 00a97020 ["INT_ADD", "register:40f0:8", ["const:a97020:8", "const:4:8"]]
- 00a97020 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97064 ["INT_ADD", "register:40f0:8", ["const:a97064:8", "const:4:8"]]
+ 00a97064 ["CALL", null, ["callee:005c2710:8"]]
- 00a97020 bytes bcadec97
+ 00a97064 bytes abadec97
- 00a9702c ["INT_ADD", "register:40f0:8", ["const:a9702c:8", "const:4:8"]]
- 00a9702c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97070 ["INT_ADD", "register:40f0:8", ["const:a97070:8", "const:4:8"]]
+ 00a97070 ["CALL", null, ["callee:0081f580:8"]]
- 00a9702c bytes 5521f697
+ 00a97070 bytes 4421f697
~~~


<a id="compare-3a777c23a520ad353eca5d026cb2da75"></a>

### [`00a970d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a970d8.md) → [`00a9711c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a9711c.md) FUN_00a9711c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a970ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a970d8.md#insn-00a970ec) · [`00a97100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a970d8.md#insn-00a97100) · [`00a9710c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a970d8.md#insn-00a9710c)
- 新版 `00a97130`（命令位置の公開資料なし） · `00a97144`（命令位置の公開資料なし） · `00a97150`（命令位置の公開資料なし）

~~~diff
- 00a970ec ["INT_ADD", "register:40f0:8", ["const:a970ec:8", "const:4:8"]]
- 00a970ec ["CALL", null, ["callee:0081f580:8"]]
+ 00a97130 ["INT_ADD", "register:40f0:8", ["const:a97130:8", "const:4:8"]]
+ 00a97130 ["CALL", null, ["callee:0081f580:8"]]
- 00a970ec bytes 2521f697
+ 00a97130 bytes 1421f697
- 00a97100 ["INT_ADD", "register:40f0:8", ["const:a97100:8", "const:4:8"]]
- 00a97100 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97144 ["INT_ADD", "register:40f0:8", ["const:a97144:8", "const:4:8"]]
+ 00a97144 ["CALL", null, ["callee:005c2710:8"]]
- 00a97100 bytes 84adec97
+ 00a97144 bytes 73adec97
- 00a9710c ["INT_ADD", "register:40f0:8", ["const:a9710c:8", "const:4:8"]]
- 00a9710c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97150 ["INT_ADD", "register:40f0:8", ["const:a97150:8", "const:4:8"]]
+ 00a97150 ["CALL", null, ["callee:0081f580:8"]]
- 00a9710c bytes 1d21f697
+ 00a97150 bytes 0c21f697
~~~


<a id="compare-109e2f27d6868f5b3fe12beb9c98124d"></a>

### [`00a97148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97148.md) → [`00a9718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a9718c.md) FUN_00a9718c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`00a962a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a962a8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`00a962ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a962ec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9715c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97148.md#insn-00a9715c) · [`00a97170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97148.md#insn-00a97170) · [`00a9717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97148.md#insn-00a9717c)
- 新版 `00a971a0`（命令位置の公開資料なし） · `00a971b4`（命令位置の公開資料なし） · `00a971c0`（命令位置の公開資料なし）

~~~diff
- 00a9715c ["INT_ADD", "register:40f0:8", ["const:a9715c:8", "const:4:8"]]
- 00a9715c ["CALL", null, ["callee:0081f580:8"]]
+ 00a971a0 ["INT_ADD", "register:40f0:8", ["const:a971a0:8", "const:4:8"]]
+ 00a971a0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9715c bytes 0921f697
+ 00a971a0 bytes f820f697
- 00a97170 ["INT_ADD", "register:40f0:8", ["const:a97170:8", "const:4:8"]]
- 00a97170 ["CALL", null, ["callee:005c2710:8"]]
+ 00a971b4 ["INT_ADD", "register:40f0:8", ["const:a971b4:8", "const:4:8"]]
+ 00a971b4 ["CALL", null, ["callee:005c2710:8"]]
- 00a97170 bytes 68adec97
+ 00a971b4 bytes 57adec97
- 00a9717c ["INT_ADD", "register:40f0:8", ["const:a9717c:8", "const:4:8"]]
- 00a9717c ["CALL", null, ["callee:0081f580:8"]]
+ 00a971c0 ["INT_ADD", "register:40f0:8", ["const:a971c0:8", "const:4:8"]]
+ 00a971c0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9717c bytes 0121f697
+ 00a971c0 bytes f020f697
~~~


<a id="compare-5ee518e43fbfff5cd18fdf6c2b2db139"></a>

### [`00a971b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a971b8.md) → [`00a971fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a971fc.md) FUN_00a971fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`00a962a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a962a8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`00a962ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a962ec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a971cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a971b8.md#insn-00a971cc) · [`00a971e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a971b8.md#insn-00a971e0) · [`00a971ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a971b8.md#insn-00a971ec)
- 新版 `00a97210`（命令位置の公開資料なし） · `00a97224`（命令位置の公開資料なし） · `00a97230`（命令位置の公開資料なし）

~~~diff
- 00a971cc ["INT_ADD", "register:40f0:8", ["const:a971cc:8", "const:4:8"]]
- 00a971cc ["CALL", null, ["callee:0081f580:8"]]
+ 00a97210 ["INT_ADD", "register:40f0:8", ["const:a97210:8", "const:4:8"]]
+ 00a97210 ["CALL", null, ["callee:0081f580:8"]]
- 00a971cc bytes ed20f697
+ 00a97210 bytes dc20f697
- 00a971e0 ["INT_ADD", "register:40f0:8", ["const:a971e0:8", "const:4:8"]]
- 00a971e0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97224 ["INT_ADD", "register:40f0:8", ["const:a97224:8", "const:4:8"]]
+ 00a97224 ["CALL", null, ["callee:005c2710:8"]]
- 00a971e0 bytes 4cadec97
+ 00a97224 bytes 3badec97
- 00a971ec ["INT_ADD", "register:40f0:8", ["const:a971ec:8", "const:4:8"]]
- 00a971ec ["CALL", null, ["callee:0081f580:8"]]
+ 00a97230 ["INT_ADD", "register:40f0:8", ["const:a97230:8", "const:4:8"]]
+ 00a97230 ["CALL", null, ["callee:0081f580:8"]]
- 00a971ec bytes e520f697
+ 00a97230 bytes d420f697
~~~


<a id="compare-6ac52e093d0dfee812c8b6f55086b7c0"></a>

### [`00a97340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97340.md) → [`00a97384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97384.md) FUN_00a97384

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9735c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97340.md#insn-00a9735c)
- 新版 `00a973a0`（命令位置の公開資料なし）

~~~diff
- 00a9735c ["INT_ADD", "register:40f0:8", ["const:a9735c:8", "const:4:8"]]
- 00a9735c ["CALL", null, ["callee:0081f580:8"]]
+ 00a973a0 ["INT_ADD", "register:40f0:8", ["const:a973a0:8", "const:4:8"]]
+ 00a973a0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9735c bytes 8920f697
+ 00a973a0 bytes 7820f697
~~~


<a id="compare-413666cebf7f54a6d12b43456bd79df2"></a>

### [`00a9738c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9738c.md) → [`00a973d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a973d0.md) FUN_00a973d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a973a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9738c.md#insn-00a973a8) · [`00a973bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9738c.md#insn-00a973bc) · [`00a973c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9738c.md#insn-00a973c8)
- 新版 `00a973ec`（命令位置の公開資料なし） · `00a97400`（命令位置の公開資料なし） · `00a9740c`（命令位置の公開資料なし）

~~~diff
- 00a973a8 ["INT_ADD", "register:40f0:8", ["const:a973a8:8", "const:4:8"]]
- 00a973a8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a973ec ["INT_ADD", "register:40f0:8", ["const:a973ec:8", "const:4:8"]]
+ 00a973ec ["CALL", null, ["callee:0081f580:8"]]
- 00a973a8 bytes 7620f697
+ 00a973ec bytes 6520f697
- 00a973bc ["INT_ADD", "register:40f0:8", ["const:a973bc:8", "const:4:8"]]
- 00a973bc ["CALL", null, ["callee:005c2710:8"]]
+ 00a97400 ["INT_ADD", "register:40f0:8", ["const:a97400:8", "const:4:8"]]
+ 00a97400 ["CALL", null, ["callee:005c2710:8"]]
- 00a973bc bytes d5acec97
+ 00a97400 bytes c4acec97
- 00a973c8 ["INT_ADD", "register:40f0:8", ["const:a973c8:8", "const:4:8"]]
- 00a973c8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9740c ["INT_ADD", "register:40f0:8", ["const:a9740c:8", "const:4:8"]]
+ 00a9740c ["CALL", null, ["callee:0081f580:8"]]
- 00a973c8 bytes 6e20f697
+ 00a9740c bytes 5d20f697
~~~


<a id="compare-239d8ac3acd78e694aeac5eb44ffd60e"></a>

### [`00a9740c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9740c.md) → [`00a97450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97450.md) FUN_00a97450

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9740c.md#insn-00a97428)
- 新版 `00a9746c`（命令位置の公開資料なし）

~~~diff
- 00a97428 ["INT_ADD", "register:40f0:8", ["const:a97428:8", "const:4:8"]]
- 00a97428 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9746c ["INT_ADD", "register:40f0:8", ["const:a9746c:8", "const:4:8"]]
+ 00a9746c ["CALL", null, ["callee:0081f580:8"]]
- 00a97428 bytes 5620f697
+ 00a9746c bytes 4520f697
~~~


<a id="compare-1b13aaffb23f4aec09fe44a77c41b3b4"></a>

### [`00a97458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97458.md) → [`00a9749c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a9749c.md) FUN_00a9749c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97458.md#insn-00a97474)
- 新版 `00a974b8`（命令位置の公開資料なし）

~~~diff
- 00a97474 ["INT_ADD", "register:40f0:8", ["const:a97474:8", "const:4:8"]]
- 00a97474 ["CALL", null, ["callee:0081f580:8"]]
+ 00a974b8 ["INT_ADD", "register:40f0:8", ["const:a974b8:8", "const:4:8"]]
+ 00a974b8 ["CALL", null, ["callee:0081f580:8"]]
- 00a97474 bytes 4320f697
+ 00a974b8 bytes 3220f697
~~~


<a id="compare-b2a9d065b8ae727461cdd7d38f28b909"></a>

### [`00a974a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a974a4.md) → [`00a974e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a974e8.md) FUN_00a974e8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a974c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a974a4.md#insn-00a974c0)
- 新版 `00a97504`（命令位置の公開資料なし）

~~~diff
- 00a974c0 ["INT_ADD", "register:40f0:8", ["const:a974c0:8", "const:4:8"]]
- 00a974c0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97504 ["INT_ADD", "register:40f0:8", ["const:a97504:8", "const:4:8"]]
+ 00a97504 ["CALL", null, ["callee:0081f580:8"]]
- 00a974c0 bytes 3020f697
+ 00a97504 bytes 1f20f697
~~~


<a id="compare-f7a5e512a535a2713b5756d58fa67491"></a>

### [`00a974f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a974f0.md) → [`00a97534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97534.md) FUN_00a97534

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9750c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a974f0.md#insn-00a9750c)
- 新版 `00a97550`（命令位置の公開資料なし）

~~~diff
- 00a9750c ["INT_ADD", "register:40f0:8", ["const:a9750c:8", "const:4:8"]]
- 00a9750c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97550 ["INT_ADD", "register:40f0:8", ["const:a97550:8", "const:4:8"]]
+ 00a97550 ["CALL", null, ["callee:0081f580:8"]]
- 00a9750c bytes 1d20f697
+ 00a97550 bytes 0c20f697
~~~


<a id="compare-179f4bd9c33ad5f57c00ce18ca438c0d"></a>

### [`00a9753c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9753c.md) → [`00a97580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97580.md) FUN_00a97580

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9753c.md#insn-00a97558)
- 新版 `00a9759c`（命令位置の公開資料なし）

~~~diff
- 00a97558 ["INT_ADD", "register:40f0:8", ["const:a97558:8", "const:4:8"]]
- 00a97558 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9759c ["INT_ADD", "register:40f0:8", ["const:a9759c:8", "const:4:8"]]
+ 00a9759c ["CALL", null, ["callee:0081f580:8"]]
- 00a97558 bytes 0a20f697
+ 00a9759c bytes f91ff697
~~~


<a id="compare-4c37146de15b457a3344d22c29d2a708"></a>

### [`00a97588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97588.md) → [`00a975cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a975cc.md) FUN_00a975cc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a975a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97588.md#insn-00a975a4)
- 新版 `00a975e8`（命令位置の公開資料なし）

~~~diff
- 00a975a4 ["INT_ADD", "register:40f0:8", ["const:a975a4:8", "const:4:8"]]
- 00a975a4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a975e8 ["INT_ADD", "register:40f0:8", ["const:a975e8:8", "const:4:8"]]
+ 00a975e8 ["CALL", null, ["callee:0081f580:8"]]
- 00a975a4 bytes f71ff697
+ 00a975e8 bytes e61ff697
~~~


<a id="compare-6fc18b2d70b4a80141227496553b7e81"></a>

### [`00a975d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a975d4.md) → [`00a97618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97618.md) FUN_00a97618

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a975f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a975d4.md#insn-00a975f0)
- 新版 `00a97634`（命令位置の公開資料なし）

~~~diff
- 00a975f0 ["INT_ADD", "register:40f0:8", ["const:a975f0:8", "const:4:8"]]
- 00a975f0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97634 ["INT_ADD", "register:40f0:8", ["const:a97634:8", "const:4:8"]]
+ 00a97634 ["CALL", null, ["callee:0081f580:8"]]
- 00a975f0 bytes e41ff697
+ 00a97634 bytes d31ff697
~~~


<a id="compare-9b181605ebc44bcd73b438262c88581c"></a>

### [`00a97620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97620.md) → [`00a97664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97664.md) FUN_00a97664

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9763c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97620.md#insn-00a9763c)
- 新版 `00a97680`（命令位置の公開資料なし）

~~~diff
- 00a9763c ["INT_ADD", "register:40f0:8", ["const:a9763c:8", "const:4:8"]]
- 00a9763c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97680 ["INT_ADD", "register:40f0:8", ["const:a97680:8", "const:4:8"]]
+ 00a97680 ["CALL", null, ["callee:0081f580:8"]]
- 00a9763c bytes d11ff697
+ 00a97680 bytes c01ff697
~~~


<a id="compare-8f4242e7ba23136d22e33676532892da"></a>

### [`00a9766c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9766c.md) → [`00a976b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a976b0.md) FUN_00a976b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a9766c.md#insn-00a97688)
- 新版 `00a976cc`（命令位置の公開資料なし）

~~~diff
- 00a97688 ["INT_ADD", "register:40f0:8", ["const:a97688:8", "const:4:8"]]
- 00a97688 ["CALL", null, ["callee:0081f580:8"]]
+ 00a976cc ["INT_ADD", "register:40f0:8", ["const:a976cc:8", "const:4:8"]]
+ 00a976cc ["CALL", null, ["callee:0081f580:8"]]
- 00a97688 bytes be1ff697
+ 00a976cc bytes ad1ff697
~~~


<a id="compare-06b1d6872e5055f778eec2d74c6229d4"></a>

### [`00a976b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a976b8.md) → [`00a976fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a976fc.md) FUN_00a976fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a976cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a976b8.md#insn-00a976cc) · [`00a976e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a976b8.md#insn-00a976e0) · [`00a976ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a976b8.md#insn-00a976ec)
- 新版 `00a97710`（命令位置の公開資料なし） · `00a97724`（命令位置の公開資料なし） · `00a97730`（命令位置の公開資料なし）

~~~diff
- 00a976cc ["INT_ADD", "register:40f0:8", ["const:a976cc:8", "const:4:8"]]
- 00a976cc ["CALL", null, ["callee:0081f580:8"]]
+ 00a97710 ["INT_ADD", "register:40f0:8", ["const:a97710:8", "const:4:8"]]
+ 00a97710 ["CALL", null, ["callee:0081f580:8"]]
- 00a976cc bytes ad1ff697
+ 00a97710 bytes 9c1ff697
- 00a976e0 ["INT_ADD", "register:40f0:8", ["const:a976e0:8", "const:4:8"]]
- 00a976e0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97724 ["INT_ADD", "register:40f0:8", ["const:a97724:8", "const:4:8"]]
+ 00a97724 ["CALL", null, ["callee:005c2710:8"]]
- 00a976e0 bytes 0cacec97
+ 00a97724 bytes fbabec97
- 00a976ec ["INT_ADD", "register:40f0:8", ["const:a976ec:8", "const:4:8"]]
- 00a976ec ["CALL", null, ["callee:0081f580:8"]]
+ 00a97730 ["INT_ADD", "register:40f0:8", ["const:a97730:8", "const:4:8"]]
+ 00a97730 ["CALL", null, ["callee:0081f580:8"]]
- 00a976ec bytes a51ff697
+ 00a97730 bytes 941ff697
~~~


<a id="compare-af4bc9a871376cd447c4783572dfa00b"></a>

### [`00a97728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97728.md) → [`00a9776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a9776c.md) FUN_00a9776c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97728.md#insn-00a97744)
- 新版 `00a97788`（命令位置の公開資料なし）

~~~diff
- 00a97744 ["INT_ADD", "register:40f0:8", ["const:a97744:8", "const:4:8"]]
- 00a97744 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97788 ["INT_ADD", "register:40f0:8", ["const:a97788:8", "const:4:8"]]
+ 00a97788 ["CALL", null, ["callee:0081f580:8"]]
- 00a97744 bytes 8f1ff697
+ 00a97788 bytes 7e1ff697
~~~


<a id="compare-c671ea3e758980402943b41395e0bc46"></a>

### [`00a97774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97774.md) → [`00a977b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a977b8.md) FUN_00a977b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97774.md#insn-00a97788) · [`00a9779c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97774.md#insn-00a9779c) · [`00a977a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97774.md#insn-00a977a8)
- 新版 `00a977cc`（命令位置の公開資料なし） · `00a977e0`（命令位置の公開資料なし） · `00a977ec`（命令位置の公開資料なし）

~~~diff
- 00a97788 ["INT_ADD", "register:40f0:8", ["const:a97788:8", "const:4:8"]]
- 00a97788 ["CALL", null, ["callee:0081f580:8"]]
+ 00a977cc ["INT_ADD", "register:40f0:8", ["const:a977cc:8", "const:4:8"]]
+ 00a977cc ["CALL", null, ["callee:0081f580:8"]]
- 00a97788 bytes 7e1ff697
+ 00a977cc bytes 6d1ff697
- 00a9779c ["INT_ADD", "register:40f0:8", ["const:a9779c:8", "const:4:8"]]
- 00a9779c ["CALL", null, ["callee:005c2710:8"]]
+ 00a977e0 ["INT_ADD", "register:40f0:8", ["const:a977e0:8", "const:4:8"]]
+ 00a977e0 ["CALL", null, ["callee:005c2710:8"]]
- 00a9779c bytes ddabec97
+ 00a977e0 bytes ccabec97
- 00a977a8 ["INT_ADD", "register:40f0:8", ["const:a977a8:8", "const:4:8"]]
- 00a977a8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a977ec ["INT_ADD", "register:40f0:8", ["const:a977ec:8", "const:4:8"]]
+ 00a977ec ["CALL", null, ["callee:0081f580:8"]]
- 00a977a8 bytes 761ff697
+ 00a977ec bytes 651ff697
~~~


<a id="compare-bb75a3a2c45ee9a2de4a9cde3fffb8fb"></a>

### [`00a977e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a977e4.md) → [`00a97828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97828.md) FUN_00a97828

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a977e4.md#insn-00a97800)
- 新版 `00a97844`（命令位置の公開資料なし）

~~~diff
- 00a97800 ["INT_ADD", "register:40f0:8", ["const:a97800:8", "const:4:8"]]
- 00a97800 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97844 ["INT_ADD", "register:40f0:8", ["const:a97844:8", "const:4:8"]]
+ 00a97844 ["CALL", null, ["callee:0081f580:8"]]
- 00a97800 bytes 601ff697
+ 00a97844 bytes 4f1ff697
~~~


<a id="compare-2d22708679788ec023c362c4ffd1eac9"></a>

### [`00a97980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97980.md) → [`00a979c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a979c4.md) FUN_00a979c4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97980.md#insn-00a97994)
- 新版 `00a979d8`（命令位置の公開資料なし）

~~~diff
- 00a97994 ["INT_ADD", "register:40f0:8", ["const:a97994:8", "const:4:8"]]
- 00a97994 ["CALL", null, ["callee:0081f580:8"]]
+ 00a979d8 ["INT_ADD", "register:40f0:8", ["const:a979d8:8", "const:4:8"]]
+ 00a979d8 ["CALL", null, ["callee:0081f580:8"]]
- 00a97994 bytes fb1ef697
+ 00a979d8 bytes ea1ef697
~~~


<a id="compare-b208ace852c967f27d744040744c4f4b"></a>

### [`00a97b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97b78.md) → [`00a97bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97bbc.md) FUN_00a97bbc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97b78.md#insn-00a97b8c)
- 新版 `00a97bd0`（命令位置の公開資料なし）

~~~diff
- 00a97b8c ["INT_ADD", "register:40f0:8", ["const:a97b8c:8", "const:4:8"]]
- 00a97b8c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97bd0 ["INT_ADD", "register:40f0:8", ["const:a97bd0:8", "const:4:8"]]
+ 00a97bd0 ["CALL", null, ["callee:0081f580:8"]]
- 00a97b8c bytes 7d1ef697
+ 00a97bd0 bytes 6c1ef697
~~~


<a id="compare-4b9edd797be9a7b5779f17c68b519d55"></a>

### [`00a97ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97ddc.md) → [`00a97e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97e20.md) FUN_00a97e20

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97ddc.md#insn-00a97df8) · [`00a97e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97ddc.md#insn-00a97e0c) · [`00a97e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97ddc.md#insn-00a97e1c)
- 新版 `00a97e3c`（命令位置の公開資料なし） · `00a97e50`（命令位置の公開資料なし） · `00a97e60`（命令位置の公開資料なし）

~~~diff
- 00a97df8 ["INT_ADD", "register:40f0:8", ["const:a97df8:8", "const:4:8"]]
- 00a97df8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97e3c ["INT_ADD", "register:40f0:8", ["const:a97e3c:8", "const:4:8"]]
+ 00a97e3c ["CALL", null, ["callee:0081f580:8"]]
- 00a97df8 bytes e21df697
+ 00a97e3c bytes d11df697
- 00a97e0c ["INT_ADD", "register:40f0:8", ["const:a97e0c:8", "const:4:8"]]
- 00a97e0c ["CALL", null, ["callee:005c2710:8"]]
+ 00a97e50 ["INT_ADD", "register:40f0:8", ["const:a97e50:8", "const:4:8"]]
+ 00a97e50 ["CALL", null, ["callee:005c2710:8"]]
- 00a97e0c bytes 41aaec97
+ 00a97e50 bytes 30aaec97
- 00a97e1c ["INT_ADD", "register:40f0:8", ["const:a97e1c:8", "const:4:8"]]
- 00a97e1c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97e60 ["INT_ADD", "register:40f0:8", ["const:a97e60:8", "const:4:8"]]
+ 00a97e60 ["CALL", null, ["callee:0081f580:8"]]
- 00a97e1c bytes d91df697
+ 00a97e60 bytes c81df697
~~~


<a id="compare-c5924f5fa8a29f72444b475126be4975"></a>

### [`00a97e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97e4c.md) → [`00a97e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97e90.md) FUN_00a97e90

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97e4c.md#insn-00a97e60) · [`00a97e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97e4c.md#insn-00a97e74) · [`00a97e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97e4c.md#insn-00a97e88)
- 新版 `00a97ea4`（命令位置の公開資料なし） · `00a97eb8`（命令位置の公開資料なし） · `00a97ecc`（命令位置の公開資料なし）

~~~diff
- 00a97e60 ["INT_ADD", "register:40f0:8", ["const:a97e60:8", "const:4:8"]]
- 00a97e60 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97ea4 ["INT_ADD", "register:40f0:8", ["const:a97ea4:8", "const:4:8"]]
+ 00a97ea4 ["CALL", null, ["callee:0081f580:8"]]
- 00a97e60 bytes c81df697
+ 00a97ea4 bytes b71df697
- 00a97e74 ["INT_ADD", "register:40f0:8", ["const:a97e74:8", "const:4:8"]]
- 00a97e74 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97eb8 ["INT_ADD", "register:40f0:8", ["const:a97eb8:8", "const:4:8"]]
+ 00a97eb8 ["CALL", null, ["callee:005c2710:8"]]
- 00a97e74 bytes 27aaec97
+ 00a97eb8 bytes 16aaec97
- 00a97e88 ["INT_ADD", "register:40f0:8", ["const:a97e88:8", "const:4:8"]]
- 00a97e88 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97ecc ["INT_ADD", "register:40f0:8", ["const:a97ecc:8", "const:4:8"]]
+ 00a97ecc ["CALL", null, ["callee:0081f580:8"]]
- 00a97e88 bytes be1df697
+ 00a97ecc bytes ad1df697
~~~


<a id="compare-162cc05dc10771e41c510141e9b31ba6"></a>

### [`00a97eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97eb4.md) → [`00a97ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97ef8.md) FUN_00a97ef8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97eb4.md#insn-00a97ed0) · [`00a97ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97eb4.md#insn-00a97ee4) · [`00a97ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97eb4.md#insn-00a97ef0)
- 新版 `00a97f14`（命令位置の公開資料なし） · `00a97f28`（命令位置の公開資料なし） · `00a97f34`（命令位置の公開資料なし）

~~~diff
- 00a97ed0 ["INT_ADD", "register:40f0:8", ["const:a97ed0:8", "const:4:8"]]
- 00a97ed0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97f14 ["INT_ADD", "register:40f0:8", ["const:a97f14:8", "const:4:8"]]
+ 00a97f14 ["CALL", null, ["callee:0081f580:8"]]
- 00a97ed0 bytes ac1df697
+ 00a97f14 bytes 9b1df697
- 00a97ee4 ["INT_ADD", "register:40f0:8", ["const:a97ee4:8", "const:4:8"]]
- 00a97ee4 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97f28 ["INT_ADD", "register:40f0:8", ["const:a97f28:8", "const:4:8"]]
+ 00a97f28 ["CALL", null, ["callee:005c2710:8"]]
- 00a97ee4 bytes 0baaec97
+ 00a97f28 bytes faa9ec97
- 00a97ef0 ["INT_ADD", "register:40f0:8", ["const:a97ef0:8", "const:4:8"]]
- 00a97ef0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97f34 ["INT_ADD", "register:40f0:8", ["const:a97f34:8", "const:4:8"]]
+ 00a97f34 ["CALL", null, ["callee:0081f580:8"]]
- 00a97ef0 bytes a41df697
+ 00a97f34 bytes 931df697
~~~


<a id="compare-3d8d4996a7a6a3d4f7f87044ae207b13"></a>

### [`00a97f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97f20.md) → [`00a97f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97f64.md) FUN_00a97f64

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97f20.md#insn-00a97f3c)
- 新版 `00a97f80`（命令位置の公開資料なし）

~~~diff
- 00a97f3c ["INT_ADD", "register:40f0:8", ["const:a97f3c:8", "const:4:8"]]
- 00a97f3c ["CALL", null, ["callee:0081f580:8"]]
+ 00a97f80 ["INT_ADD", "register:40f0:8", ["const:a97f80:8", "const:4:8"]]
+ 00a97f80 ["CALL", null, ["callee:0081f580:8"]]
- 00a97f3c bytes 911df697
+ 00a97f80 bytes 801df697
~~~


<a id="compare-835b72b84b3240b0bb81f64aa93d5c34"></a>

### [`00a98338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98338.md) → [`00a9837c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a9837c.md) FUN_00a9837c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98338.md#insn-00a98358)
- 新版 `00a9839c`（命令位置の公開資料なし）

~~~diff
- 00a98358 ["INT_ADD", "register:40f0:8", ["const:a98358:8", "const:4:8"]]
- 00a98358 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9839c ["INT_ADD", "register:40f0:8", ["const:a9839c:8", "const:4:8"]]
+ 00a9839c ["CALL", null, ["callee:0081f580:8"]]
- 00a98358 bytes 8a1cf697
+ 00a9839c bytes 791cf697
~~~


<a id="compare-d05eb1115b0e13fdaa761b704bfa2dd6"></a>

### [`00a9846c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a9846c.md) → [`00a984b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a984b0.md) FUN_00a984b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a9846c.md#insn-00a98480)
- 新版 `00a984c4`（命令位置の公開資料なし）

~~~diff
- 00a98480 ["INT_ADD", "register:40f0:8", ["const:a98480:8", "const:4:8"]]
- 00a98480 ["CALL", null, ["callee:0081f580:8"]]
+ 00a984c4 ["INT_ADD", "register:40f0:8", ["const:a984c4:8", "const:4:8"]]
+ 00a984c4 ["CALL", null, ["callee:0081f580:8"]]
- 00a98480 bytes 401cf697
+ 00a984c4 bytes 2f1cf697
~~~


<a id="compare-ab967610c7e7262438e81e010d652b52"></a>

### [`00a984ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a984ac.md) → [`00a984f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a984f0.md) FUN_00a984f0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a984c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a984ac.md#insn-00a984c8)
- 新版 `00a9850c`（命令位置の公開資料なし）

~~~diff
- 00a984c8 ["INT_ADD", "register:40f0:8", ["const:a984c8:8", "const:4:8"]]
- 00a984c8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9850c ["INT_ADD", "register:40f0:8", ["const:a9850c:8", "const:4:8"]]
+ 00a9850c ["CALL", null, ["callee:0081f580:8"]]
- 00a984c8 bytes 2e1cf697
+ 00a9850c bytes 1d1cf697
~~~


<a id="compare-938499e1c6bad674a72dd3c9225d4702"></a>

### [`00a984f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a984f8.md) → [`00a9853c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a9853c.md) FUN_00a9853c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9850c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a984f8.md#insn-00a9850c)
- 新版 `00a98550`（命令位置の公開資料なし）

~~~diff
- 00a9850c ["INT_ADD", "register:40f0:8", ["const:a9850c:8", "const:4:8"]]
- 00a9850c ["CALL", null, ["callee:0081f580:8"]]
+ 00a98550 ["INT_ADD", "register:40f0:8", ["const:a98550:8", "const:4:8"]]
+ 00a98550 ["CALL", null, ["callee:0081f580:8"]]
- 00a9850c bytes 1d1cf697
+ 00a98550 bytes 0c1cf697
~~~


<a id="compare-dc9d31bc2a6652f245cb59b5f68e76e1"></a>

### [`00a98658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98658.md) → [`00a9869c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a9869c.md) FUN_00a9869c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, local_def_use, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00a986cc",
      "incomplete_value": true,
      "site": "00a986d8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a98688",
      "incomplete_value": true,
      "site": "00a98694",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a9866c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98658.md#insn-00a9866c)
- 新版 `00a986b0`（命令位置の公開資料なし）

~~~diff
- 00a9866c ["INT_ADD", "register:40f0:8", ["const:a9866c:8", "const:4:8"]]
- 00a9866c ["CALL", null, ["callee:0081f580:8"]]
+ 00a986b0 ["INT_ADD", "register:40f0:8", ["const:a986b0:8", "const:4:8"]]
+ 00a986b0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9866c bytes c51bf697
+ 00a986b0 bytes b41bf697
~~~


<a id="compare-4c1b077e0f4f6fe66b2350a3fc3f8bc3"></a>

### [`00a98878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98878.md) → [`00a988bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a988bc.md) FUN_00a988bc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98878.md#insn-00a98894)
- 新版 `00a988d8`（命令位置の公開資料なし）

~~~diff
- 00a98894 ["INT_ADD", "register:40f0:8", ["const:a98894:8", "const:4:8"]]
- 00a98894 ["CALL", null, ["callee:0081f580:8"]]
+ 00a988d8 ["INT_ADD", "register:40f0:8", ["const:a988d8:8", "const:4:8"]]
+ 00a988d8 ["CALL", null, ["callee:0081f580:8"]]
- 00a98894 bytes 3b1bf697
+ 00a988d8 bytes 2a1bf697
~~~


<a id="compare-26fa061fce85ca520625d5c864a98afe"></a>

### [`00a98ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98ce4.md) → [`00a98d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98d28.md) FUN_00a98d28

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98ce4.md#insn-00a98d00)
- 新版 `00a98d44`（命令位置の公開資料なし）

~~~diff
- 00a98d00 ["INT_ADD", "register:40f0:8", ["const:a98d00:8", "const:4:8"]]
- 00a98d00 ["CALL", null, ["callee:0081f580:8"]]
+ 00a98d44 ["INT_ADD", "register:40f0:8", ["const:a98d44:8", "const:4:8"]]
+ 00a98d44 ["CALL", null, ["callee:0081f580:8"]]
- 00a98d00 bytes 201af697
+ 00a98d44 bytes 0f1af697
~~~


<a id="compare-c3177249e1c56bdfd3063667002f95de"></a>

### [`00a98d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98d30.md) → [`00a98d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98d74.md) FUN_00a98d74

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98d30.md#insn-00a98d44)
- 新版 `00a98d88`（命令位置の公開資料なし）

~~~diff
- 00a98d44 ["INT_ADD", "register:40f0:8", ["const:a98d44:8", "const:4:8"]]
- 00a98d44 ["CALL", null, ["callee:0081f580:8"]]
+ 00a98d88 ["INT_ADD", "register:40f0:8", ["const:a98d88:8", "const:4:8"]]
+ 00a98d88 ["CALL", null, ["callee:0081f580:8"]]
- 00a98d44 bytes 0f1af697
+ 00a98d88 bytes fe19f697
~~~


<a id="compare-34b257cfa3dd59bd8cf705b94a976edc"></a>

### [`00a98d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98d70.md) → [`00a98db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98db4.md) FUN_00a98db4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98d70.md#insn-00a98d8c)
- 新版 `00a98dd0`（命令位置の公開資料なし）

~~~diff
- 00a98d8c ["INT_ADD", "register:40f0:8", ["const:a98d8c:8", "const:4:8"]]
- 00a98d8c ["CALL", null, ["callee:0081f580:8"]]
+ 00a98dd0 ["INT_ADD", "register:40f0:8", ["const:a98dd0:8", "const:4:8"]]
+ 00a98dd0 ["CALL", null, ["callee:0081f580:8"]]
- 00a98d8c bytes fd19f697
+ 00a98dd0 bytes ec19f697
~~~


<a id="compare-4bca6b345002e1b522ef21df4bd73cc9"></a>

### [`00a98dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98dbc.md) → [`00a98e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98e00.md) FUN_00a98e00

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98dbc.md#insn-00a98dd0)
- 新版 `00a98e14`（命令位置の公開資料なし）

~~~diff
- 00a98dd0 ["INT_ADD", "register:40f0:8", ["const:a98dd0:8", "const:4:8"]]
- 00a98dd0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a98e14 ["INT_ADD", "register:40f0:8", ["const:a98e14:8", "const:4:8"]]
+ 00a98e14 ["CALL", null, ["callee:0081f580:8"]]
- 00a98dd0 bytes ec19f697
+ 00a98e14 bytes db19f697
~~~


<a id="compare-aa87ce8541107b16df37b2beb7581442"></a>

### [`00a98e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98e04.md) → [`00a98e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98e48.md) FUN_00a98e48

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98e04.md#insn-00a98e20)
- 新版 `00a98e64`（命令位置の公開資料なし）

~~~diff
- 00a98e20 ["INT_ADD", "register:40f0:8", ["const:a98e20:8", "const:4:8"]]
- 00a98e20 ["CALL", null, ["callee:0081f580:8"]]
+ 00a98e64 ["INT_ADD", "register:40f0:8", ["const:a98e64:8", "const:4:8"]]
+ 00a98e64 ["CALL", null, ["callee:0081f580:8"]]
- 00a98e20 bytes d819f697
+ 00a98e64 bytes c719f697
~~~


<a id="compare-cdb9cf85b689bac1987100a372ed6f74"></a>

### [`00a98e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98e50.md) → [`00a98e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98e94.md) FUN_00a98e94

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98e50.md#insn-00a98e64)
- 新版 `00a98ea8`（命令位置の公開資料なし）

~~~diff
- 00a98e64 ["INT_ADD", "register:40f0:8", ["const:a98e64:8", "const:4:8"]]
- 00a98e64 ["CALL", null, ["callee:0081f580:8"]]
+ 00a98ea8 ["INT_ADD", "register:40f0:8", ["const:a98ea8:8", "const:4:8"]]
+ 00a98ea8 ["CALL", null, ["callee:0081f580:8"]]
- 00a98e64 bytes c719f697
+ 00a98ea8 bytes b619f697
~~~


<a id="compare-027a29393ed8d5446e0b560fd8ca9778"></a>

### [`00a98e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98e90.md) → [`00a98ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98ed4.md) FUN_00a98ed4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98e90.md#insn-00a98eac)
- 新版 `00a98ef0`（命令位置の公開資料なし）

~~~diff
- 00a98eac ["INT_ADD", "register:40f0:8", ["const:a98eac:8", "const:4:8"]]
- 00a98eac ["CALL", null, ["callee:0081f580:8"]]
+ 00a98ef0 ["INT_ADD", "register:40f0:8", ["const:a98ef0:8", "const:4:8"]]
+ 00a98ef0 ["CALL", null, ["callee:0081f580:8"]]
- 00a98eac bytes b519f697
+ 00a98ef0 bytes a419f697
~~~


<a id="compare-1c0337e662a67a5b28520f7016636065"></a>

### [`00a98ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98ffc.md) → [`00a99040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99040.md) FUN_00a99040

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98ffc.md#insn-00a99010)
- 新版 `00a99054`（命令位置の公開資料なし）

~~~diff
- 00a99010 ["INT_ADD", "register:40f0:8", ["const:a99010:8", "const:4:8"]]
- 00a99010 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99054 ["INT_ADD", "register:40f0:8", ["const:a99054:8", "const:4:8"]]
+ 00a99054 ["CALL", null, ["callee:0081f580:8"]]
- 00a99010 bytes 5c19f697
+ 00a99054 bytes 4b19f697
~~~


<a id="compare-38fab09f560165ee4df54aec97e79b9a"></a>

### [`00a9903c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a9903c.md) → [`00a99080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99080.md) FUN_00a99080

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a9903c.md#insn-00a99058)
- 新版 `00a9909c`（命令位置の公開資料なし）

~~~diff
- 00a99058 ["INT_ADD", "register:40f0:8", ["const:a99058:8", "const:4:8"]]
- 00a99058 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9909c ["INT_ADD", "register:40f0:8", ["const:a9909c:8", "const:4:8"]]
+ 00a9909c ["CALL", null, ["callee:0081f580:8"]]
- 00a99058 bytes 4a19f697
+ 00a9909c bytes 3919f697
~~~


<a id="compare-2701b0508acd1876776f8d6ef1be4e4a"></a>

### [`00a99088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99088.md) → [`00a990cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a990cc.md) FUN_00a990cc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9909c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99088.md#insn-00a9909c)
- 新版 `00a990e0`（命令位置の公開資料なし）

~~~diff
- 00a9909c ["INT_ADD", "register:40f0:8", ["const:a9909c:8", "const:4:8"]]
- 00a9909c ["CALL", null, ["callee:0081f580:8"]]
+ 00a990e0 ["INT_ADD", "register:40f0:8", ["const:a990e0:8", "const:4:8"]]
+ 00a990e0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9909c bytes 3919f697
+ 00a990e0 bytes 2819f697
~~~


<a id="compare-ee24207db85ccfa832d673a2309bcffb"></a>

### [`00a991a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a991a0.md) → [`00a991e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a991e4.md) FUN_00a991e4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a991bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a991a0.md#insn-00a991bc)
- 新版 `00a99200`（命令位置の公開資料なし）

~~~diff
- 00a991bc ["INT_ADD", "register:40f0:8", ["const:a991bc:8", "const:4:8"]]
- 00a991bc ["CALL", null, ["callee:0081f580:8"]]
+ 00a99200 ["INT_ADD", "register:40f0:8", ["const:a99200:8", "const:4:8"]]
+ 00a99200 ["CALL", null, ["callee:0081f580:8"]]
- 00a991bc bytes f118f697
+ 00a99200 bytes e018f697
~~~


<a id="compare-a9ad27a5f759f13959191423e553d1d3"></a>

### [`00a991ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a991ec.md) → [`00a99230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99230.md) FUN_00a99230

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a991ec.md#insn-00a99200)
- 新版 `00a99244`（命令位置の公開資料なし）

~~~diff
- 00a99200 ["INT_ADD", "register:40f0:8", ["const:a99200:8", "const:4:8"]]
- 00a99200 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99244 ["INT_ADD", "register:40f0:8", ["const:a99244:8", "const:4:8"]]
+ 00a99244 ["CALL", null, ["callee:0081f580:8"]]
- 00a99200 bytes e018f697
+ 00a99244 bytes cf18f697
~~~


<a id="compare-fcb59f9ceae75cb272df2cf12ddee171"></a>

### [`00a99234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99234.md) → [`00a99278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99278.md) FUN_00a99278

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99234.md#insn-00a99248)
- 新版 `00a9928c`（命令位置の公開資料なし）

~~~diff
- 00a99248 ["INT_ADD", "register:40f0:8", ["const:a99248:8", "const:4:8"]]
- 00a99248 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9928c ["INT_ADD", "register:40f0:8", ["const:a9928c:8", "const:4:8"]]
+ 00a9928c ["CALL", null, ["callee:0081f580:8"]]
- 00a99248 bytes ce18f697
+ 00a9928c bytes bd18f697
~~~


<a id="compare-cf8785fdfedc0e231fc37428abc3559f"></a>

### [`00a99274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99274.md) → [`00a992b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a992b8.md) FUN_00a992b8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99274.md#insn-00a99290)
- 新版 `00a992d4`（命令位置の公開資料なし）

~~~diff
- 00a99290 ["INT_ADD", "register:40f0:8", ["const:a99290:8", "const:4:8"]]
- 00a99290 ["CALL", null, ["callee:0081f580:8"]]
+ 00a992d4 ["INT_ADD", "register:40f0:8", ["const:a992d4:8", "const:4:8"]]
+ 00a992d4 ["CALL", null, ["callee:0081f580:8"]]
- 00a99290 bytes bc18f697
+ 00a992d4 bytes ab18f697
~~~


<a id="compare-68a7b5846d98d5595c6a882c0fd5483e"></a>

### [`00a992c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a992c0.md) → [`00a99304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99304.md) FUN_00a99304

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) [`00a93b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) [`00a93b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93b48.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a992d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a992c0.md#insn-00a992d4)
- 新版 `00a99318`（命令位置の公開資料なし）

~~~diff
- 00a992d4 ["INT_ADD", "register:40f0:8", ["const:a992d4:8", "const:4:8"]]
- 00a992d4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99318 ["INT_ADD", "register:40f0:8", ["const:a99318:8", "const:4:8"]]
+ 00a99318 ["CALL", null, ["callee:0081f580:8"]]
- 00a992d4 bytes ab18f697
+ 00a99318 bytes 9a18f697
~~~


<a id="compare-b99411e826089ac684defb764af88cfd"></a>

### [`00a99308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99308.md) → [`00a9934c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a9934c.md) FUN_00a9934c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9931c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99308.md#insn-00a9931c)
- 新版 `00a99360`（命令位置の公開資料なし）

~~~diff
- 00a9931c ["INT_ADD", "register:40f0:8", ["const:a9931c:8", "const:4:8"]]
- 00a9931c ["CALL", null, ["callee:0081f580:8"]]
+ 00a99360 ["INT_ADD", "register:40f0:8", ["const:a99360:8", "const:4:8"]]
+ 00a99360 ["CALL", null, ["callee:0081f580:8"]]
- 00a9931c bytes 9918f697
+ 00a99360 bytes 8818f697
~~~


<a id="compare-14011134c3356c5247ea8ecca4c2fb20"></a>

### [`00a99348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99348.md) → [`00a9938c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a9938c.md) FUN_00a9938c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a93b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b0c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a93b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93b50.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99348.md#insn-00a99364)
- 新版 `00a993a8`（命令位置の公開資料なし）

~~~diff
- 00a99364 ["INT_ADD", "register:40f0:8", ["const:a99364:8", "const:4:8"]]
- 00a99364 ["CALL", null, ["callee:0081f580:8"]]
+ 00a993a8 ["INT_ADD", "register:40f0:8", ["const:a993a8:8", "const:4:8"]]
+ 00a993a8 ["CALL", null, ["callee:0081f580:8"]]
- 00a99364 bytes 8718f697
+ 00a993a8 bytes 7618f697
~~~


<a id="compare-12facc09cb5fa60adf675aa4c7686cf0"></a>

### [`00a99394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99394.md) → [`00a993d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a993d8.md) FUN_00a993d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a993a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99394.md#insn-00a993a8)
- 新版 `00a993ec`（命令位置の公開資料なし）

~~~diff
- 00a993a8 ["INT_ADD", "register:40f0:8", ["const:a993a8:8", "const:4:8"]]
- 00a993a8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a993ec ["INT_ADD", "register:40f0:8", ["const:a993ec:8", "const:4:8"]]
+ 00a993ec ["CALL", null, ["callee:0081f580:8"]]
- 00a993a8 bytes 7618f697
+ 00a993ec bytes 6518f697
~~~


<a id="compare-23c3f58bbf59f113462b44006f07d58d"></a>

### [`00a993d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a993d4.md) → [`00a99418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99418.md) FUN_00a99418

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a93b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b18.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a93b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93b5c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a993f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a993d4.md#insn-00a993f0)
- 新版 `00a99434`（命令位置の公開資料なし）

~~~diff
- 00a993f0 ["INT_ADD", "register:40f0:8", ["const:a993f0:8", "const:4:8"]]
- 00a993f0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99434 ["INT_ADD", "register:40f0:8", ["const:a99434:8", "const:4:8"]]
+ 00a99434 ["CALL", null, ["callee:0081f580:8"]]
- 00a993f0 bytes 6418f697
+ 00a99434 bytes 5318f697
~~~


<a id="compare-3f20442621e4493261d1388516da182e"></a>

### [`00a99420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99420.md) → [`00a99464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99464.md) FUN_00a99464

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) [`00a93b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b24.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) [`00a93b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93b68.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99420.md#insn-00a99434)
- 新版 `00a99478`（命令位置の公開資料なし）

~~~diff
- 00a99434 ["INT_ADD", "register:40f0:8", ["const:a99434:8", "const:4:8"]]
- 00a99434 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99478 ["INT_ADD", "register:40f0:8", ["const:a99478:8", "const:4:8"]]
+ 00a99478 ["CALL", null, ["callee:0081f580:8"]]
- 00a99434 bytes 5318f697
+ 00a99478 bytes 4218f697
~~~


<a id="compare-67d1a9786e84c7a182581b12fedc63db"></a>

### [`00a99468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99468.md) → [`00a994ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a994ac.md) FUN_00a994ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9947c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99468.md#insn-00a9947c)
- 新版 `00a994c0`（命令位置の公開資料なし）

~~~diff
- 00a9947c ["INT_ADD", "register:40f0:8", ["const:a9947c:8", "const:4:8"]]
- 00a9947c ["CALL", null, ["callee:0081f580:8"]]
+ 00a994c0 ["INT_ADD", "register:40f0:8", ["const:a994c0:8", "const:4:8"]]
+ 00a994c0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9947c bytes 4118f697
+ 00a994c0 bytes 3018f697
~~~


<a id="compare-5e40af0b62f243e2114b23054bce4f37"></a>

### [`00a994a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a994a8.md) → [`00a994ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a994ec.md) FUN_00a994ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a93b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b2c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a93b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93b70.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a994c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a994a8.md#insn-00a994c4)
- 新版 `00a99508`（命令位置の公開資料なし）

~~~diff
- 00a994c4 ["INT_ADD", "register:40f0:8", ["const:a994c4:8", "const:4:8"]]
- 00a994c4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99508 ["INT_ADD", "register:40f0:8", ["const:a99508:8", "const:4:8"]]
+ 00a99508 ["CALL", null, ["callee:0081f580:8"]]
- 00a994c4 bytes 2f18f697
+ 00a99508 bytes 1e18f697
~~~


<a id="compare-b467251d6e607e769df03bc2dc2be1a7"></a>

### [`00a994f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a994f4.md) → [`00a99538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99538.md) FUN_00a99538

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a994f4.md#insn-00a99508)
- 新版 `00a9954c`（命令位置の公開資料なし）

~~~diff
- 00a99508 ["INT_ADD", "register:40f0:8", ["const:a99508:8", "const:4:8"]]
- 00a99508 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9954c ["INT_ADD", "register:40f0:8", ["const:a9954c:8", "const:4:8"]]
+ 00a9954c ["CALL", null, ["callee:0081f580:8"]]
- 00a99508 bytes 1e18f697
+ 00a9954c bytes 0d18f697
~~~


<a id="compare-a543b7c57e0f488268d65d9a8508bd28"></a>

### [`00a99534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99534.md) → [`00a99578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99578.md) FUN_00a99578

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a93b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b38.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a93b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93b7c.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99534.md#insn-00a99550)
- 新版 `00a99594`（命令位置の公開資料なし）

~~~diff
- 00a99550 ["INT_ADD", "register:40f0:8", ["const:a99550:8", "const:4:8"]]
- 00a99550 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99594 ["INT_ADD", "register:40f0:8", ["const:a99594:8", "const:4:8"]]
+ 00a99594 ["CALL", null, ["callee:0081f580:8"]]
- 00a99550 bytes 0c18f697
+ 00a99594 bytes fb17f697
~~~


<a id="compare-ff7310184ebb9ff66091ba4bdae96a92"></a>

### [`00a99580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99580.md) → [`00a995c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a995c4.md) FUN_00a995c4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99580.md#insn-00a99594)
- 新版 `00a995d8`（命令位置の公開資料なし）

~~~diff
- 00a99594 ["INT_ADD", "register:40f0:8", ["const:a99594:8", "const:4:8"]]
- 00a99594 ["CALL", null, ["callee:0081f580:8"]]
+ 00a995d8 ["INT_ADD", "register:40f0:8", ["const:a995d8:8", "const:4:8"]]
+ 00a995d8 ["CALL", null, ["callee:0081f580:8"]]
- 00a99594 bytes fb17f697
+ 00a995d8 bytes ea17f697
~~~


<a id="compare-3f17c5f1c05d5a70920abd6b8176e892"></a>

### [`00a995c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a995c8.md) → [`00a9960c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a9960c.md) FUN_00a9960c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a995dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a995c8.md#insn-00a995dc)
- 新版 `00a99620`（命令位置の公開資料なし）

~~~diff
- 00a995dc ["INT_ADD", "register:40f0:8", ["const:a995dc:8", "const:4:8"]]
- 00a995dc ["CALL", null, ["callee:0081f580:8"]]
+ 00a99620 ["INT_ADD", "register:40f0:8", ["const:a99620:8", "const:4:8"]]
+ 00a99620 ["CALL", null, ["callee:0081f580:8"]]
- 00a995dc bytes e917f697
+ 00a99620 bytes d817f697
~~~


<a id="compare-ba0f67d612962e57e7a0a86489ddcb90"></a>

### [`00a99608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99608.md) → [`00a9964c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a9964c.md) FUN_00a9964c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99608.md#insn-00a99624)
- 新版 `00a99668`（命令位置の公開資料なし）

~~~diff
- 00a99624 ["INT_ADD", "register:40f0:8", ["const:a99624:8", "const:4:8"]]
- 00a99624 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99668 ["INT_ADD", "register:40f0:8", ["const:a99668:8", "const:4:8"]]
+ 00a99668 ["CALL", null, ["callee:0081f580:8"]]
- 00a99624 bytes d717f697
+ 00a99668 bytes c617f697
~~~


<a id="compare-c5a324f480fd9bc7952d736f03154495"></a>

### [`00a99654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99654.md) → [`00a99698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99698.md) FUN_00a99698

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99654.md#insn-00a99668)
- 新版 `00a996ac`（命令位置の公開資料なし）

~~~diff
- 00a99668 ["INT_ADD", "register:40f0:8", ["const:a99668:8", "const:4:8"]]
- 00a99668 ["CALL", null, ["callee:0081f580:8"]]
+ 00a996ac ["INT_ADD", "register:40f0:8", ["const:a996ac:8", "const:4:8"]]
+ 00a996ac ["CALL", null, ["callee:0081f580:8"]]
- 00a99668 bytes c617f697
+ 00a996ac bytes b517f697
~~~


<a id="compare-0f4589704b99d52eab9d8c19b4a29476"></a>

### [`00a99694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99694.md) → [`00a996d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a996d8.md) FUN_00a996d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a996b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99694.md#insn-00a996b0)
- 新版 `00a996f4`（命令位置の公開資料なし）

~~~diff
- 00a996b0 ["INT_ADD", "register:40f0:8", ["const:a996b0:8", "const:4:8"]]
- 00a996b0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a996f4 ["INT_ADD", "register:40f0:8", ["const:a996f4:8", "const:4:8"]]
+ 00a996f4 ["CALL", null, ["callee:0081f580:8"]]
- 00a996b0 bytes b417f697
+ 00a996f4 bytes a317f697
~~~


<a id="compare-1dc4bf98c381e2e5d8615bffba787c0d"></a>

### [`00a99720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99720.md) → [`00a99764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99764.md) FUN_00a99764

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, local_def_use, operands_and_dependencies, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a9979c",
      "incomplete_value": true,
      "site": "00a9979c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a99758",
      "incomplete_value": true,
      "site": "00a99758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99720.md#insn-00a9973c)
- 新版 `00a99780`（命令位置の公開資料なし）

~~~diff
- 00a9973c ["INT_ADD", "register:40f0:8", ["const:a9973c:8", "const:4:8"]]
- 00a9973c ["CALL", null, ["callee:0081f580:8"]]
+ 00a99780 ["INT_ADD", "register:40f0:8", ["const:a99780:8", "const:4:8"]]
+ 00a99780 ["CALL", null, ["callee:0081f580:8"]]
- 00a9973c bytes 9117f697
+ 00a99780 bytes 8017f697
~~~


<a id="compare-b2816c14de117488b15007902a779345"></a>

### [`00a99d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d04.md) → [`00a99d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99d48.md) FUN_00a99d48

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d04.md#insn-00a99d18) · [`00a99d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d04.md#insn-00a99d2c) · [`00a99d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d04.md#insn-00a99d40)
- 新版 `00a99d5c`（命令位置の公開資料なし） · `00a99d70`（命令位置の公開資料なし） · `00a99d84`（命令位置の公開資料なし）

~~~diff
- 00a99d18 ["INT_ADD", "register:40f0:8", ["const:a99d18:8", "const:4:8"]]
- 00a99d18 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99d5c ["INT_ADD", "register:40f0:8", ["const:a99d5c:8", "const:4:8"]]
+ 00a99d5c ["CALL", null, ["callee:0081f580:8"]]
- 00a99d18 bytes 1a16f697
+ 00a99d5c bytes 0916f697
- 00a99d2c ["INT_ADD", "register:40f0:8", ["const:a99d2c:8", "const:4:8"]]
- 00a99d2c ["CALL", null, ["callee:005c2710:8"]]
+ 00a99d70 ["INT_ADD", "register:40f0:8", ["const:a99d70:8", "const:4:8"]]
+ 00a99d70 ["CALL", null, ["callee:005c2710:8"]]
- 00a99d2c bytes 79a2ec97
+ 00a99d70 bytes 68a2ec97
- 00a99d40 ["INT_ADD", "register:40f0:8", ["const:a99d40:8", "const:4:8"]]
- 00a99d40 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99d84 ["INT_ADD", "register:40f0:8", ["const:a99d84:8", "const:4:8"]]
+ 00a99d84 ["CALL", null, ["callee:0081f580:8"]]
- 00a99d40 bytes 1016f697
+ 00a99d84 bytes ff15f697
~~~


<a id="compare-46ff94b475a3081085674dc34c76c860"></a>

### [`00a99d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d74.md) → [`00a99db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99db8.md) FUN_00a99db8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d74.md#insn-00a99d90) · [`00a99da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d74.md#insn-00a99da4) · [`00a99db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99d74.md#insn-00a99db4)
- 新版 `00a99dd4`（命令位置の公開資料なし） · `00a99de8`（命令位置の公開資料なし） · `00a99df8`（命令位置の公開資料なし）

~~~diff
- 00a99d90 ["INT_ADD", "register:40f0:8", ["const:a99d90:8", "const:4:8"]]
- 00a99d90 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99dd4 ["INT_ADD", "register:40f0:8", ["const:a99dd4:8", "const:4:8"]]
+ 00a99dd4 ["CALL", null, ["callee:0081f580:8"]]
- 00a99d90 bytes fc15f697
+ 00a99dd4 bytes eb15f697
- 00a99da4 ["INT_ADD", "register:40f0:8", ["const:a99da4:8", "const:4:8"]]
- 00a99da4 ["CALL", null, ["callee:005c2710:8"]]
+ 00a99de8 ["INT_ADD", "register:40f0:8", ["const:a99de8:8", "const:4:8"]]
+ 00a99de8 ["CALL", null, ["callee:005c2710:8"]]
- 00a99da4 bytes 5ba2ec97
+ 00a99de8 bytes 4aa2ec97
- 00a99db4 ["INT_ADD", "register:40f0:8", ["const:a99db4:8", "const:4:8"]]
- 00a99db4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99df8 ["INT_ADD", "register:40f0:8", ["const:a99df8:8", "const:4:8"]]
+ 00a99df8 ["CALL", null, ["callee:0081f580:8"]]
- 00a99db4 bytes f315f697
+ 00a99df8 bytes e215f697
~~~


<a id="compare-dbdbf7b9155689cc041a85b1a5dec261"></a>

### [`00a99de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99de4.md) → [`00a99e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99e28.md) FUN_00a99e28

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99de4.md#insn-00a99df8) · [`00a99e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99de4.md#insn-00a99e0c) · [`00a99e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99de4.md#insn-00a99e20)
- 新版 `00a99e3c`（命令位置の公開資料なし） · `00a99e50`（命令位置の公開資料なし） · `00a99e64`（命令位置の公開資料なし）

~~~diff
- 00a99df8 ["INT_ADD", "register:40f0:8", ["const:a99df8:8", "const:4:8"]]
- 00a99df8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99e3c ["INT_ADD", "register:40f0:8", ["const:a99e3c:8", "const:4:8"]]
+ 00a99e3c ["CALL", null, ["callee:0081f580:8"]]
- 00a99df8 bytes e215f697
+ 00a99e3c bytes d115f697
- 00a99e0c ["INT_ADD", "register:40f0:8", ["const:a99e0c:8", "const:4:8"]]
- 00a99e0c ["CALL", null, ["callee:005c2710:8"]]
+ 00a99e50 ["INT_ADD", "register:40f0:8", ["const:a99e50:8", "const:4:8"]]
+ 00a99e50 ["CALL", null, ["callee:005c2710:8"]]
- 00a99e0c bytes 41a2ec97
+ 00a99e50 bytes 30a2ec97
- 00a99e20 ["INT_ADD", "register:40f0:8", ["const:a99e20:8", "const:4:8"]]
- 00a99e20 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99e64 ["INT_ADD", "register:40f0:8", ["const:a99e64:8", "const:4:8"]]
+ 00a99e64 ["CALL", null, ["callee:0081f580:8"]]
- 00a99e20 bytes d815f697
+ 00a99e64 bytes c715f697
~~~


<a id="compare-7d0a73ab8175df0a46246a49db9ec420"></a>

### [`00a99e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99e54.md) → [`00a99e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99e98.md) FUN_00a99e98

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99e54.md#insn-00a99e70) · [`00a99e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99e54.md#insn-00a99e84) · [`00a99e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99e54.md#insn-00a99e94)
- 新版 `00a99eb4`（命令位置の公開資料なし） · `00a99ec8`（命令位置の公開資料なし） · `00a99ed8`（命令位置の公開資料なし）

~~~diff
- 00a99e70 ["INT_ADD", "register:40f0:8", ["const:a99e70:8", "const:4:8"]]
- 00a99e70 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99eb4 ["INT_ADD", "register:40f0:8", ["const:a99eb4:8", "const:4:8"]]
+ 00a99eb4 ["CALL", null, ["callee:0081f580:8"]]
- 00a99e70 bytes c415f697
+ 00a99eb4 bytes b315f697
- 00a99e84 ["INT_ADD", "register:40f0:8", ["const:a99e84:8", "const:4:8"]]
- 00a99e84 ["CALL", null, ["callee:005c2710:8"]]
+ 00a99ec8 ["INT_ADD", "register:40f0:8", ["const:a99ec8:8", "const:4:8"]]
+ 00a99ec8 ["CALL", null, ["callee:005c2710:8"]]
- 00a99e84 bytes 23a2ec97
+ 00a99ec8 bytes 12a2ec97
- 00a99e94 ["INT_ADD", "register:40f0:8", ["const:a99e94:8", "const:4:8"]]
- 00a99e94 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99ed8 ["INT_ADD", "register:40f0:8", ["const:a99ed8:8", "const:4:8"]]
+ 00a99ed8 ["CALL", null, ["callee:0081f580:8"]]
- 00a99e94 bytes bb15f697
+ 00a99ed8 bytes aa15f697
~~~


<a id="compare-5bfffc60985a639dd64089b0e5a5dac6"></a>

### [`00a99ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99ec4.md) → [`00a99f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99f08.md) FUN_00a99f08

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99ec4.md#insn-00a99ed8) · [`00a99eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99ec4.md#insn-00a99eec) · [`00a99f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99ec4.md#insn-00a99f00)
- 新版 `00a99f1c`（命令位置の公開資料なし） · `00a99f30`（命令位置の公開資料なし） · `00a99f44`（命令位置の公開資料なし）

~~~diff
- 00a99ed8 ["INT_ADD", "register:40f0:8", ["const:a99ed8:8", "const:4:8"]]
- 00a99ed8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99f1c ["INT_ADD", "register:40f0:8", ["const:a99f1c:8", "const:4:8"]]
+ 00a99f1c ["CALL", null, ["callee:0081f580:8"]]
- 00a99ed8 bytes aa15f697
+ 00a99f1c bytes 9915f697
- 00a99eec ["INT_ADD", "register:40f0:8", ["const:a99eec:8", "const:4:8"]]
- 00a99eec ["CALL", null, ["callee:005c2710:8"]]
+ 00a99f30 ["INT_ADD", "register:40f0:8", ["const:a99f30:8", "const:4:8"]]
+ 00a99f30 ["CALL", null, ["callee:005c2710:8"]]
- 00a99eec bytes 09a2ec97
+ 00a99f30 bytes f8a1ec97
- 00a99f00 ["INT_ADD", "register:40f0:8", ["const:a99f00:8", "const:4:8"]]
- 00a99f00 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99f44 ["INT_ADD", "register:40f0:8", ["const:a99f44:8", "const:4:8"]]
+ 00a99f44 ["CALL", null, ["callee:0081f580:8"]]
- 00a99f00 bytes a015f697
+ 00a99f44 bytes 8f15f697
~~~


<a id="compare-a8cf16f21065070782336bbde551a656"></a>

### [`00a99f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99f34.md) → [`00a99f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99f78.md) FUN_00a99f78

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99f34.md#insn-00a99f50) · [`00a99f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99f34.md#insn-00a99f64) · [`00a99f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99f34.md#insn-00a99f74)
- 新版 `00a99f94`（命令位置の公開資料なし） · `00a99fa8`（命令位置の公開資料なし） · `00a99fb8`（命令位置の公開資料なし）

~~~diff
- 00a99f50 ["INT_ADD", "register:40f0:8", ["const:a99f50:8", "const:4:8"]]
- 00a99f50 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99f94 ["INT_ADD", "register:40f0:8", ["const:a99f94:8", "const:4:8"]]
+ 00a99f94 ["CALL", null, ["callee:0081f580:8"]]
- 00a99f50 bytes 8c15f697
+ 00a99f94 bytes 7b15f697
- 00a99f64 ["INT_ADD", "register:40f0:8", ["const:a99f64:8", "const:4:8"]]
- 00a99f64 ["CALL", null, ["callee:005c2710:8"]]
+ 00a99fa8 ["INT_ADD", "register:40f0:8", ["const:a99fa8:8", "const:4:8"]]
+ 00a99fa8 ["CALL", null, ["callee:005c2710:8"]]
- 00a99f64 bytes eba1ec97
+ 00a99fa8 bytes daa1ec97
- 00a99f74 ["INT_ADD", "register:40f0:8", ["const:a99f74:8", "const:4:8"]]
- 00a99f74 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99fb8 ["INT_ADD", "register:40f0:8", ["const:a99fb8:8", "const:4:8"]]
+ 00a99fb8 ["CALL", null, ["callee:0081f580:8"]]
- 00a99f74 bytes 8315f697
+ 00a99fb8 bytes 7215f697
~~~


<a id="compare-635ac4a4545f5beeb92a68a8bfac51da"></a>

### [`00a99fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99fa4.md) → [`00a99fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99fe8.md) FUN_00a99fe8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a99fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99fa4.md#insn-00a99fb8) · [`00a99fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99fa4.md#insn-00a99fcc) · [`00a99fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99fa4.md#insn-00a99fe0)
- 新版 `00a99ffc`（命令位置の公開資料なし） · `00a9a010`（命令位置の公開資料なし） · `00a9a024`（命令位置の公開資料なし）

~~~diff
- 00a99fb8 ["INT_ADD", "register:40f0:8", ["const:a99fb8:8", "const:4:8"]]
- 00a99fb8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99ffc ["INT_ADD", "register:40f0:8", ["const:a99ffc:8", "const:4:8"]]
+ 00a99ffc ["CALL", null, ["callee:0081f580:8"]]
- 00a99fb8 bytes 7215f697
+ 00a99ffc bytes 6115f697
- 00a99fcc ["INT_ADD", "register:40f0:8", ["const:a99fcc:8", "const:4:8"]]
- 00a99fcc ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a010 ["INT_ADD", "register:40f0:8", ["const:a9a010:8", "const:4:8"]]
+ 00a9a010 ["CALL", null, ["callee:005c2710:8"]]
- 00a99fcc bytes d1a1ec97
+ 00a9a010 bytes c0a1ec97
- 00a99fe0 ["INT_ADD", "register:40f0:8", ["const:a99fe0:8", "const:4:8"]]
- 00a99fe0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a024 ["INT_ADD", "register:40f0:8", ["const:a9a024:8", "const:4:8"]]
+ 00a9a024 ["CALL", null, ["callee:0081f580:8"]]
- 00a99fe0 bytes 6815f697
+ 00a9a024 bytes 5715f697
~~~


<a id="compare-2ea1f89e39a5ff32cf60d6a7c2572b6b"></a>

### [`00a9a014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a014.md) → [`00a9a058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a058.md) FUN_00a9a058

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a014.md#insn-00a9a030) · [`00a9a044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a014.md#insn-00a9a044) · [`00a9a054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a014.md#insn-00a9a054)
- 新版 `00a9a074`（命令位置の公開資料なし） · `00a9a088`（命令位置の公開資料なし） · `00a9a098`（命令位置の公開資料なし）

~~~diff
- 00a9a030 ["INT_ADD", "register:40f0:8", ["const:a9a030:8", "const:4:8"]]
- 00a9a030 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a074 ["INT_ADD", "register:40f0:8", ["const:a9a074:8", "const:4:8"]]
+ 00a9a074 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a030 bytes 5415f697
+ 00a9a074 bytes 4315f697
- 00a9a044 ["INT_ADD", "register:40f0:8", ["const:a9a044:8", "const:4:8"]]
- 00a9a044 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a088 ["INT_ADD", "register:40f0:8", ["const:a9a088:8", "const:4:8"]]
+ 00a9a088 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a044 bytes b3a1ec97
+ 00a9a088 bytes a2a1ec97
- 00a9a054 ["INT_ADD", "register:40f0:8", ["const:a9a054:8", "const:4:8"]]
- 00a9a054 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a098 ["INT_ADD", "register:40f0:8", ["const:a9a098:8", "const:4:8"]]
+ 00a9a098 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a054 bytes 4b15f697
+ 00a9a098 bytes 3a15f697
~~~


<a id="compare-9f9f2040c394d8ed9c3ef790069390c3"></a>

### [`00a9a084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a084.md) → [`00a9a0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a0c8.md) FUN_00a9a0c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a084.md#insn-00a9a098)
- 新版 `00a9a0dc`（命令位置の公開資料なし）

~~~diff
- 00a9a098 ["INT_ADD", "register:40f0:8", ["const:a9a098:8", "const:4:8"]]
- 00a9a098 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a0dc ["INT_ADD", "register:40f0:8", ["const:a9a0dc:8", "const:4:8"]]
+ 00a9a0dc ["CALL", null, ["callee:0081f580:8"]]
- 00a9a098 bytes 3a15f697
+ 00a9a0dc bytes 2915f697
~~~


<a id="compare-5715290a18daa9bcbb04a438fc170745"></a>

### [`00a9a0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a0cc.md) → [`00a9a110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a110.md) FUN_00a9a110

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a0cc.md#insn-00a9a0e0)
- 新版 `00a9a124`（命令位置の公開資料なし）

~~~diff
- 00a9a0e0 ["INT_ADD", "register:40f0:8", ["const:a9a0e0:8", "const:4:8"]]
- 00a9a0e0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a124 ["INT_ADD", "register:40f0:8", ["const:a9a124:8", "const:4:8"]]
+ 00a9a124 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a0e0 bytes 2815f697
+ 00a9a124 bytes 1715f697
~~~


<a id="compare-16668cbfe0630eb3897ba219b52ce648"></a>

### [`00a9a10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a10c.md) → [`00a9a150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a150.md) FUN_00a9a150

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a10c.md#insn-00a9a128)
- 新版 `00a9a16c`（命令位置の公開資料なし）

~~~diff
- 00a9a128 ["INT_ADD", "register:40f0:8", ["const:a9a128:8", "const:4:8"]]
- 00a9a128 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a16c ["INT_ADD", "register:40f0:8", ["const:a9a16c:8", "const:4:8"]]
+ 00a9a16c ["CALL", null, ["callee:0081f580:8"]]
- 00a9a128 bytes 1615f697
+ 00a9a16c bytes 0515f697
~~~


<a id="compare-d7ace03c94785efae357fae56aff89e0"></a>

### [`00a9a158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a158.md) → [`00a9a19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a19c.md) FUN_00a9a19c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a158.md#insn-00a9a16c)
- 新版 `00a9a1b0`（命令位置の公開資料なし）

~~~diff
- 00a9a16c ["INT_ADD", "register:40f0:8", ["const:a9a16c:8", "const:4:8"]]
- 00a9a16c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a1b0 ["INT_ADD", "register:40f0:8", ["const:a9a1b0:8", "const:4:8"]]
+ 00a9a1b0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a16c bytes 0515f697
+ 00a9a1b0 bytes f414f697
~~~


<a id="compare-237ed86a8d6408a36386d20c9b41fc2c"></a>

### [`00a9a1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a1a0.md) → [`00a9a1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a1e4.md) FUN_00a9a1e4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a1a0.md#insn-00a9a1bc)
- 新版 `00a9a200`（命令位置の公開資料なし）

~~~diff
- 00a9a1bc ["INT_ADD", "register:40f0:8", ["const:a9a1bc:8", "const:4:8"]]
- 00a9a1bc ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a200 ["INT_ADD", "register:40f0:8", ["const:a9a200:8", "const:4:8"]]
+ 00a9a200 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a1bc bytes f114f697
+ 00a9a200 bytes e014f697
~~~


<a id="compare-dbc708836201fafb499595322eb753e2"></a>

### [`00a9a1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a1ec.md) → [`00a9a230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a230.md) FUN_00a9a230

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a1ec.md#insn-00a9a200) · [`00a9a214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a1ec.md#insn-00a9a214) · [`00a9a228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a1ec.md#insn-00a9a228)
- 新版 `00a9a244`（命令位置の公開資料なし） · `00a9a258`（命令位置の公開資料なし） · `00a9a26c`（命令位置の公開資料なし）

~~~diff
- 00a9a200 ["INT_ADD", "register:40f0:8", ["const:a9a200:8", "const:4:8"]]
- 00a9a200 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a244 ["INT_ADD", "register:40f0:8", ["const:a9a244:8", "const:4:8"]]
+ 00a9a244 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a200 bytes e014f697
+ 00a9a244 bytes cf14f697
- 00a9a214 ["INT_ADD", "register:40f0:8", ["const:a9a214:8", "const:4:8"]]
- 00a9a214 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a258 ["INT_ADD", "register:40f0:8", ["const:a9a258:8", "const:4:8"]]
+ 00a9a258 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a214 bytes 3fa1ec97
+ 00a9a258 bytes 2ea1ec97
- 00a9a228 ["INT_ADD", "register:40f0:8", ["const:a9a228:8", "const:4:8"]]
- 00a9a228 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a26c ["INT_ADD", "register:40f0:8", ["const:a9a26c:8", "const:4:8"]]
+ 00a9a26c ["CALL", null, ["callee:0081f580:8"]]
- 00a9a228 bytes d614f697
+ 00a9a26c bytes c514f697
~~~


<a id="compare-d65b6b3cb6f1a3a36c2ea3c7e4ce5273"></a>

### [`00a9a25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a25c.md) → [`00a9a2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a2a0.md) FUN_00a9a2a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a25c.md#insn-00a9a278) · [`00a9a28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a25c.md#insn-00a9a28c) · [`00a9a29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a25c.md#insn-00a9a29c)
- 新版 `00a9a2bc`（命令位置の公開資料なし） · `00a9a2d0`（命令位置の公開資料なし） · `00a9a2e0`（命令位置の公開資料なし）

~~~diff
- 00a9a278 ["INT_ADD", "register:40f0:8", ["const:a9a278:8", "const:4:8"]]
- 00a9a278 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a2bc ["INT_ADD", "register:40f0:8", ["const:a9a2bc:8", "const:4:8"]]
+ 00a9a2bc ["CALL", null, ["callee:0081f580:8"]]
- 00a9a278 bytes c214f697
+ 00a9a2bc bytes b114f697
- 00a9a28c ["INT_ADD", "register:40f0:8", ["const:a9a28c:8", "const:4:8"]]
- 00a9a28c ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a2d0 ["INT_ADD", "register:40f0:8", ["const:a9a2d0:8", "const:4:8"]]
+ 00a9a2d0 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a28c bytes 21a1ec97
+ 00a9a2d0 bytes 10a1ec97
- 00a9a29c ["INT_ADD", "register:40f0:8", ["const:a9a29c:8", "const:4:8"]]
- 00a9a29c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a2e0 ["INT_ADD", "register:40f0:8", ["const:a9a2e0:8", "const:4:8"]]
+ 00a9a2e0 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a29c bytes b914f697
+ 00a9a2e0 bytes a814f697
~~~


<a id="compare-775c7fca11ee5de0f46e1e8149029e31"></a>

### [`00a9a4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a4fc.md) → [`00a9a540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a540.md) FUN_00a9a540

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a4fc.md#insn-00a9a518) · [`00a9a52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a4fc.md#insn-00a9a52c) · [`00a9a53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a4fc.md#insn-00a9a53c)
- 新版 `00a9a55c`（命令位置の公開資料なし） · `00a9a570`（命令位置の公開資料なし） · `00a9a580`（命令位置の公開資料なし）

~~~diff
- 00a9a518 ["INT_ADD", "register:40f0:8", ["const:a9a518:8", "const:4:8"]]
- 00a9a518 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a55c ["INT_ADD", "register:40f0:8", ["const:a9a55c:8", "const:4:8"]]
+ 00a9a55c ["CALL", null, ["callee:0081f580:8"]]
- 00a9a518 bytes 1a14f697
+ 00a9a55c bytes 0914f697
- 00a9a52c ["INT_ADD", "register:40f0:8", ["const:a9a52c:8", "const:4:8"]]
- 00a9a52c ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a570 ["INT_ADD", "register:40f0:8", ["const:a9a570:8", "const:4:8"]]
+ 00a9a570 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a52c bytes 79a0ec97
+ 00a9a570 bytes 68a0ec97
- 00a9a53c ["INT_ADD", "register:40f0:8", ["const:a9a53c:8", "const:4:8"]]
- 00a9a53c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a580 ["INT_ADD", "register:40f0:8", ["const:a9a580:8", "const:4:8"]]
+ 00a9a580 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a53c bytes 1114f697
+ 00a9a580 bytes 0014f697
~~~


<a id="compare-c11286fecb5ba948d250db242f04f508"></a>

### [`00a9a7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a7bc.md) → [`00a9a800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a800.md) FUN_00a9a800

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a7bc.md#insn-00a9a7d0)
- 新版 `00a9a814`（命令位置の公開資料なし）

~~~diff
- 00a9a7d0 ["INT_ADD", "register:40f0:8", ["const:a9a7d0:8", "const:4:8"]]
- 00a9a7d0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a814 ["INT_ADD", "register:40f0:8", ["const:a9a814:8", "const:4:8"]]
+ 00a9a814 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a7d0 bytes 6c13f697
+ 00a9a814 bytes 5b13f697
~~~


<a id="compare-3ce06dafe7f1780972626873252af784"></a>

### [`00a9a804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a804.md) → [`00a9a848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a848.md) FUN_00a9a848

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a804.md#insn-00a9a818)
- 新版 `00a9a85c`（命令位置の公開資料なし）

~~~diff
- 00a9a818 ["INT_ADD", "register:40f0:8", ["const:a9a818:8", "const:4:8"]]
- 00a9a818 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a85c ["INT_ADD", "register:40f0:8", ["const:a9a85c:8", "const:4:8"]]
+ 00a9a85c ["CALL", null, ["callee:0081f580:8"]]
- 00a9a818 bytes 5a13f697
+ 00a9a85c bytes 4913f697
~~~


<a id="compare-18cb30d285e366fcbcc06fd3bc264f7d"></a>

### [`00a9a844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a844.md) → [`00a9a888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a888.md) FUN_00a9a888

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9a860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a844.md#insn-00a9a860)
- 新版 `00a9a8a4`（命令位置の公開資料なし）

~~~diff
- 00a9a860 ["INT_ADD", "register:40f0:8", ["const:a9a860:8", "const:4:8"]]
- 00a9a860 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a8a4 ["INT_ADD", "register:40f0:8", ["const:a9a8a4:8", "const:4:8"]]
+ 00a9a8a4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a860 bytes 4813f697
+ 00a9a8a4 bytes 3713f697
~~~


