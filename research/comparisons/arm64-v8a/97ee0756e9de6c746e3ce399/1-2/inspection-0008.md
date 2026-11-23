# v15.7.3 → v15.7.4 · 要調査の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-d793d767c894bdd23c8a94fd4adb8434"></a>

### [`00af3a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md) → [`00af3a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3a64.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE7reserveEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde760.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7b0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md#insn-00af3a80) · [`00af3ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md#insn-00af3ac0) · [`00af3afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md#insn-00af3afc)
- 新版 `00af3ac4`（命令位置の公開資料なし） · `00af3b04`（命令位置の公開資料なし） · `00af3b40`（命令位置の公開資料なし）

~~~diff
- 00af3a80 ["INT_ADD", "register:40f0:8", ["const:af3a80:8", "const:4:8"]]
- 00af3a80 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af3ac4 ["INT_ADD", "register:40f0:8", ["const:af3ac4:8", "const:4:8"]]
+ 00af3ac4 ["CALL", null, ["callee:00bdb040:8"]]
- 00af3a80 bytes 5c9d0394
+ 00af3ac4 bytes 5f9d0394
- 00af3ac0 ["INT_ADD", "register:40f0:8", ["const:af3ac0:8", "const:4:8"]]
- 00af3ac0 ["CALL", null, ["callee:00bdd9f0:8"]]
+ 00af3b04 ["INT_ADD", "register:40f0:8", ["const:af3b04:8", "const:4:8"]]
+ 00af3b04 ["CALL", null, ["callee:00bdd9f0:8"]]
- 00af3ac0 bytes b8a70394
+ 00af3b04 bytes bba70394
- 00af3afc ["INT_ADD", "register:40f0:8", ["const:af3afc:8", "const:4:8"]]
- 00af3afc ["CALL", null, ["callee:00bdd9e0:8"]]
+ 00af3b40 ["INT_ADD", "register:40f0:8", ["const:af3b40:8", "const:4:8"]]
+ 00af3b40 ["CALL", null, ["callee:00bdd9e0:8"]]
- 00af3afc bytes a5a70394
+ 00af3b40 bytes a8a70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e459ccc7b0d017df220681cbeab6cc57"></a>

### [`00af3b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md) → [`00af3b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3b80.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md#insn-00af3b60) · [`00af3b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md#insn-00af3b94) · [`00af3bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md#insn-00af3bb4)
- 新版 `00af3ba4`（命令位置の公開資料なし） · `00af3bd8`（命令位置の公開資料なし） · `00af3bf8`（命令位置の公開資料なし）

~~~diff
- 00af3b60 ["INT_ADD", "register:40f0:8", ["const:af3b60:8", "const:4:8"]]
- 00af3b60 ["CALL", null, ["callee:00bdb190:8"]]
+ 00af3ba4 ["INT_ADD", "register:40f0:8", ["const:af3ba4:8", "const:4:8"]]
+ 00af3ba4 ["CALL", null, ["callee:00bdb190:8"]]
- 00af3b60 bytes 789d0394
+ 00af3ba4 bytes 7b9d0394
- 00af3b94 ["INT_ADD", "register:40f0:8", ["const:af3b94:8", "const:4:8"]]
- 00af3b94 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af3bd8 ["INT_ADD", "register:40f0:8", ["const:af3bd8:8", "const:4:8"]]
+ 00af3bd8 ["CALL", null, ["callee:00bdb040:8"]]
- 00af3b94 bytes 179d0394
+ 00af3bd8 bytes 1a9d0394
- 00af3bb4 ["INT_ADD", "register:40f0:8", ["const:af3bb4:8", "const:4:8"]]
- 00af3bb4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00af3bf8 ["INT_ADD", "register:40f0:8", ["const:af3bf8:8", "const:4:8"]]
+ 00af3bf8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00af3bb4 bytes 6b9d0394
+ 00af3bf8 bytes 6e9d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc2e599c43297d53edf6f4b788a2bd0a"></a>

### [`00af3dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3dec.md) → [`00af3e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3e30.md) _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde330.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde380.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3dec.md#insn-00af3e60) · [`00af3e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3dec.md#insn-00af3e84)
- 新版 `00af3ea4`（命令位置の公開資料なし） · `00af3ec8`（命令位置の公開資料なし）

~~~diff
- 00af3e60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af3e60 ["INT_ADD", "register:40f0:8", ["const:af3e60:8", "const:4:8"]]
- 00af3e60 ["CALLIND", null, ["register:0:8"]]
+ 00af3ea4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af3ea4 ["INT_ADD", "register:40f0:8", ["const:af3ea4:8", "const:4:8"]]
+ 00af3ea4 ["CALLIND", null, ["register:0:8"]]
- 00af3e60 bytes 00013fd6
+ 00af3ea4 bytes 00013fd6
- 00af3e84 ["INT_ADD", "register:40f0:8", ["const:af3e84:8", "const:4:8"]]
- 00af3e84 ["CALL", null, ["callee:00bdb090:8"]]
+ 00af3ec8 ["INT_ADD", "register:40f0:8", ["const:af3ec8:8", "const:4:8"]]
+ 00af3ec8 ["CALL", null, ["callee:00bdb090:8"]]
- 00af3e84 bytes 6f9c0394
+ 00af3ec8 bytes 729c0394
~~~


<a id="compare-60a54a4ec40b38f05241f31542f05def"></a>

### [`00af3ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ef0.md) → [`00af3f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3f34.md) _ZN7_JNIEnv14CallCharMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde340.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde390.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ef0.md#insn-00af3f64) · [`00af3f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ef0.md#insn-00af3f88)
- 新版 `00af3fa8`（命令位置の公開資料なし） · `00af3fcc`（命令位置の公開資料なし）

~~~diff
- 00af3f64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af3f64 ["INT_ADD", "register:40f0:8", ["const:af3f64:8", "const:4:8"]]
- 00af3f64 ["CALLIND", null, ["register:0:8"]]
+ 00af3fa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af3fa8 ["INT_ADD", "register:40f0:8", ["const:af3fa8:8", "const:4:8"]]
+ 00af3fa8 ["CALLIND", null, ["register:0:8"]]
- 00af3f64 bytes 00013fd6
+ 00af3fa8 bytes 00013fd6
- 00af3f88 ["INT_ADD", "register:40f0:8", ["const:af3f88:8", "const:4:8"]]
- 00af3f88 ["CALL", null, ["callee:00bdb090:8"]]
+ 00af3fcc ["INT_ADD", "register:40f0:8", ["const:af3fcc:8", "const:4:8"]]
+ 00af3fcc ["CALL", null, ["callee:00bdb090:8"]]
- 00af3f88 bytes 2e9c0394
+ 00af3fcc bytes 319c0394
~~~


<a id="compare-f5b386320c22afcf1c7e66b52e0d2a8d"></a>

### [`00af3ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ff4.md) → [`00af4038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4038.md) _ZN7_JNIEnv15CallShortMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde350.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3a0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ff4.md#insn-00af4068) · [`00af408c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ff4.md#insn-00af408c)
- 新版 `00af40ac`（命令位置の公開資料なし） · `00af40d0`（命令位置の公開資料なし）

~~~diff
- 00af4068 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4068 ["INT_ADD", "register:40f0:8", ["const:af4068:8", "const:4:8"]]
- 00af4068 ["CALLIND", null, ["register:0:8"]]
+ 00af40ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af40ac ["INT_ADD", "register:40f0:8", ["const:af40ac:8", "const:4:8"]]
+ 00af40ac ["CALLIND", null, ["register:0:8"]]
- 00af4068 bytes 00013fd6
+ 00af40ac bytes 00013fd6
- 00af408c ["INT_ADD", "register:40f0:8", ["const:af408c:8", "const:4:8"]]
- 00af408c ["CALL", null, ["callee:00bdb090:8"]]
+ 00af40d0 ["INT_ADD", "register:40f0:8", ["const:af40d0:8", "const:4:8"]]
+ 00af40d0 ["CALL", null, ["callee:00bdb090:8"]]
- 00af408c bytes ed9b0394
+ 00af40d0 bytes f09b0394
~~~


<a id="compare-6aba15fb49cdf9fa2225dacda913a1bd"></a>

### [`00af4240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4240.md) → [`00af4284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4284.md) _ZN7_JNIEnv16CallDoubleMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde360.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3b0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af42b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4240.md#insn-00af42b4) · [`00af42d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4240.md#insn-00af42d8)
- 新版 `00af42f8`（命令位置の公開資料なし） · `00af431c`（命令位置の公開資料なし）

~~~diff
- 00af42b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af42b4 ["INT_ADD", "register:40f0:8", ["const:af42b4:8", "const:4:8"]]
- 00af42b4 ["CALLIND", null, ["register:0:8"]]
+ 00af42f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af42f8 ["INT_ADD", "register:40f0:8", ["const:af42f8:8", "const:4:8"]]
+ 00af42f8 ["CALLIND", null, ["register:0:8"]]
- 00af42b4 bytes 00013fd6
+ 00af42f8 bytes 00013fd6
- 00af42d8 ["INT_ADD", "register:40f0:8", ["const:af42d8:8", "const:4:8"]]
- 00af42d8 ["CALL", null, ["callee:00bdb090:8"]]
+ 00af431c ["INT_ADD", "register:40f0:8", ["const:af431c:8", "const:4:8"]]
+ 00af431c ["CALL", null, ["callee:00bdb090:8"]]
- 00af42d8 bytes 5a9b0394
+ 00af431c bytes 5d9b0394
~~~


<a id="compare-f86a08937f7db1ca84a350ddee272d98"></a>

### [`00af4354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4354.md) → [`00af4398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4398.md) _ZN8firebase4util12IsJByteArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af437c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4354.md#insn-00af437c) · [`00af4398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4354.md#insn-00af4398) · [`00af43b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4354.md#insn-00af43b4)
- 新版 `00af43c0`（命令位置の公開資料なし） · `00af43dc`（命令位置の公開資料なし） · `00af43f8`（命令位置の公開資料なし）

~~~diff
- 00af437c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af437c ["INT_ADD", "register:40f0:8", ["const:af437c:8", "const:4:8"]]
- 00af437c ["CALLIND", null, ["register:0:8"]]
+ 00af43c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af43c0 ["INT_ADD", "register:40f0:8", ["const:af43c0:8", "const:4:8"]]
+ 00af43c0 ["CALLIND", null, ["register:0:8"]]
- 00af437c bytes 00013fd6
+ 00af43c0 bytes 00013fd6
- 00af4398 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4398 ["INT_ADD", "register:40f0:8", ["const:af4398:8", "const:4:8"]]
- 00af4398 ["CALLIND", null, ["register:0:8"]]
+ 00af43dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af43dc ["INT_ADD", "register:40f0:8", ["const:af43dc:8", "const:4:8"]]
+ 00af43dc ["CALLIND", null, ["register:0:8"]]
- 00af4398 bytes 00013fd6
+ 00af43dc bytes 00013fd6
- 00af43b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af43b4 ["INT_ADD", "register:40f0:8", ["const:af43b4:8", "const:4:8"]]
- 00af43b4 ["CALLIND", null, ["register:0:8"]]
+ 00af43f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af43f8 ["INT_ADD", "register:40f0:8", ["const:af43f8:8", "const:4:8"]]
+ 00af43f8 ["CALLIND", null, ["register:0:8"]]
- 00af43b4 bytes 00013fd6
+ 00af43f8 bytes 00013fd6
~~~


<a id="compare-10dcffa9bc2dad37bfe271012aaf0f96"></a>

### [`00af44bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af44bc.md) → [`00af4500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4500.md) _ZN8firebase4util11IsJIntArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af44e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af44bc.md#insn-00af44e4) · [`00af4500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af44bc.md#insn-00af4500) · [`00af451c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af44bc.md#insn-00af451c)
- 新版 `00af4528`（命令位置の公開資料なし） · `00af4544`（命令位置の公開資料なし） · `00af4560`（命令位置の公開資料なし）

~~~diff
- 00af44e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af44e4 ["INT_ADD", "register:40f0:8", ["const:af44e4:8", "const:4:8"]]
- 00af44e4 ["CALLIND", null, ["register:0:8"]]
+ 00af4528 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4528 ["INT_ADD", "register:40f0:8", ["const:af4528:8", "const:4:8"]]
+ 00af4528 ["CALLIND", null, ["register:0:8"]]
- 00af44e4 bytes 00013fd6
+ 00af4528 bytes 00013fd6
- 00af4500 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4500 ["INT_ADD", "register:40f0:8", ["const:af4500:8", "const:4:8"]]
- 00af4500 ["CALLIND", null, ["register:0:8"]]
+ 00af4544 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4544 ["INT_ADD", "register:40f0:8", ["const:af4544:8", "const:4:8"]]
+ 00af4544 ["CALLIND", null, ["register:0:8"]]
- 00af4500 bytes 00013fd6
+ 00af4544 bytes 00013fd6
- 00af451c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af451c ["INT_ADD", "register:40f0:8", ["const:af451c:8", "const:4:8"]]
- 00af451c ["CALLIND", null, ["register:0:8"]]
+ 00af4560 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4560 ["INT_ADD", "register:40f0:8", ["const:af4560:8", "const:4:8"]]
+ 00af4560 ["CALLIND", null, ["register:0:8"]]
- 00af451c bytes 00013fd6
+ 00af4560 bytes 00013fd6
~~~


<a id="compare-877ed7ffb468e4ddd70660275e547227"></a>

### [`00af469c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md) → [`00af46e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af46e0.md) _ZN8firebase4util22JBooleanArrayToVariantEP7_JNIEnvP14_jbooleanArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5e0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde630.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af46dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md#insn-00af46dc) · [`00af46f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md#insn-00af46f8) · [`00af4704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md#insn-00af4704)
- 新版 `00af4720`（命令位置の公開資料なし） · `00af473c`（命令位置の公開資料なし） · `00af4748`（命令位置の公開資料なし）

~~~diff
- 00af46dc ["COPY", "register:0:8", ["register:4048:8"]]
- 00af46dc ["INT_ADD", "register:40f0:8", ["const:af46dc:8", "const:4:8"]]
- 00af46dc ["CALLIND", null, ["register:0:8"]]
+ 00af4720 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4720 ["INT_ADD", "register:40f0:8", ["const:af4720:8", "const:4:8"]]
+ 00af4720 ["CALLIND", null, ["register:0:8"]]
- 00af46dc bytes 20013fd6
+ 00af4720 bytes 20013fd6
- 00af46f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af46f8 ["INT_ADD", "register:40f0:8", ["const:af46f8:8", "const:4:8"]]
- 00af46f8 ["CALLIND", null, ["register:0:8"]]
+ 00af473c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af473c ["INT_ADD", "register:40f0:8", ["const:af473c:8", "const:4:8"]]
+ 00af473c ["CALLIND", null, ["register:0:8"]]
- 00af46f8 bytes 00013fd6
+ 00af473c bytes 00013fd6
- 00af4704 ["INT_ADD", "register:40f0:8", ["const:af4704:8", "const:4:8"]]
- 00af4704 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af4748 ["INT_ADD", "register:40f0:8", ["const:af4748:8", "const:4:8"]]
+ 00af4748 ["CALL", null, ["callee:00bdb040:8"]]
- 00af4704 bytes 3b9a0394
+ 00af4748 bytes 3e9a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa9820bc70c07c03e1c18001789b20a7"></a>

### [`00af4820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md) → [`00af4864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4864.md) _ZN8firebase4util19JByteArrayToVariantEP7_JNIEnvP11_jbyteArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde500.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde550.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md#insn-00af4860) · [`00af487c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md#insn-00af487c) · [`00af4888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md#insn-00af4888)
- 新版 `00af48a4`（命令位置の公開資料なし） · `00af48c0`（命令位置の公開資料なし） · `00af48cc`（命令位置の公開資料なし）

~~~diff
- 00af4860 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4860 ["INT_ADD", "register:40f0:8", ["const:af4860:8", "const:4:8"]]
- 00af4860 ["CALLIND", null, ["register:0:8"]]
+ 00af48a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af48a4 ["INT_ADD", "register:40f0:8", ["const:af48a4:8", "const:4:8"]]
+ 00af48a4 ["CALLIND", null, ["register:0:8"]]
- 00af4860 bytes 20013fd6
+ 00af48a4 bytes 20013fd6
- 00af487c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af487c ["INT_ADD", "register:40f0:8", ["const:af487c:8", "const:4:8"]]
- 00af487c ["CALLIND", null, ["register:0:8"]]
+ 00af48c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af48c0 ["INT_ADD", "register:40f0:8", ["const:af48c0:8", "const:4:8"]]
+ 00af48c0 ["CALLIND", null, ["register:0:8"]]
- 00af487c bytes 00013fd6
+ 00af48c0 bytes 00013fd6
- 00af4888 ["INT_ADD", "register:40f0:8", ["const:af4888:8", "const:4:8"]]
- 00af4888 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af48cc ["INT_ADD", "register:40f0:8", ["const:af48cc:8", "const:4:8"]]
+ 00af48cc ["CALL", null, ["callee:00bdb040:8"]]
- 00af4888 bytes da990394
+ 00af48cc bytes dd990394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccb037bc3f2e2c44dd2352c1e6c2c1e9"></a>

### [`00af499c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af499c.md) → [`00af49e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af49e0.md) _ZN8firebase4util19JCharArrayToVariantEP7_JNIEnvP11_jcharArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde510.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde560.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af49dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af499c.md#insn-00af49dc) · [`00af49f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af499c.md#insn-00af49f8) · [`00af4a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af499c.md#insn-00af4a04)
- 新版 `00af4a20`（命令位置の公開資料なし） · `00af4a3c`（命令位置の公開資料なし） · `00af4a48`（命令位置の公開資料なし）

~~~diff
- 00af49dc ["COPY", "register:0:8", ["register:4048:8"]]
- 00af49dc ["INT_ADD", "register:40f0:8", ["const:af49dc:8", "const:4:8"]]
- 00af49dc ["CALLIND", null, ["register:0:8"]]
+ 00af4a20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4a20 ["INT_ADD", "register:40f0:8", ["const:af4a20:8", "const:4:8"]]
+ 00af4a20 ["CALLIND", null, ["register:0:8"]]
- 00af49dc bytes 20013fd6
+ 00af4a20 bytes 20013fd6
- 00af49f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af49f8 ["INT_ADD", "register:40f0:8", ["const:af49f8:8", "const:4:8"]]
- 00af49f8 ["CALLIND", null, ["register:0:8"]]
+ 00af4a3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4a3c ["INT_ADD", "register:40f0:8", ["const:af4a3c:8", "const:4:8"]]
+ 00af4a3c ["CALLIND", null, ["register:0:8"]]
- 00af49f8 bytes 00013fd6
+ 00af4a3c bytes 00013fd6
- 00af4a04 ["INT_ADD", "register:40f0:8", ["const:af4a04:8", "const:4:8"]]
- 00af4a04 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af4a48 ["INT_ADD", "register:40f0:8", ["const:af4a48:8", "const:4:8"]]
+ 00af4a48 ["CALL", null, ["callee:00bdb040:8"]]
- 00af4a04 bytes 7b990394
+ 00af4a48 bytes 7e990394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-714bb430716788a2289e4a4156a70e70"></a>

### [`00af4b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4b1c.md) → [`00af4b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4b60.md) _ZN8firebase4util20JShortArrayToVariantEP7_JNIEnvP12_jshortArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde590.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5e0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4b1c.md#insn-00af4b5c) · [`00af4b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4b1c.md#insn-00af4b78) · [`00af4b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4b1c.md#insn-00af4b84)
- 新版 `00af4ba0`（命令位置の公開資料なし） · `00af4bbc`（命令位置の公開資料なし） · `00af4bc8`（命令位置の公開資料なし）

~~~diff
- 00af4b5c ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4b5c ["INT_ADD", "register:40f0:8", ["const:af4b5c:8", "const:4:8"]]
- 00af4b5c ["CALLIND", null, ["register:0:8"]]
+ 00af4ba0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4ba0 ["INT_ADD", "register:40f0:8", ["const:af4ba0:8", "const:4:8"]]
+ 00af4ba0 ["CALLIND", null, ["register:0:8"]]
- 00af4b5c bytes 20013fd6
+ 00af4ba0 bytes 20013fd6
- 00af4b78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4b78 ["INT_ADD", "register:40f0:8", ["const:af4b78:8", "const:4:8"]]
- 00af4b78 ["CALLIND", null, ["register:0:8"]]
+ 00af4bbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4bbc ["INT_ADD", "register:40f0:8", ["const:af4bbc:8", "const:4:8"]]
+ 00af4bbc ["CALLIND", null, ["register:0:8"]]
- 00af4b78 bytes 00013fd6
+ 00af4bbc bytes 00013fd6
- 00af4b84 ["INT_ADD", "register:40f0:8", ["const:af4b84:8", "const:4:8"]]
- 00af4b84 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af4bc8 ["INT_ADD", "register:40f0:8", ["const:af4bc8:8", "const:4:8"]]
+ 00af4bc8 ["CALL", null, ["callee:00bdb040:8"]]
- 00af4b84 bytes 1b990394
+ 00af4bc8 bytes 1e990394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d830bf938afd9beeffc1203cd8a6d48"></a>

### [`00af4c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md) → [`00af4cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4cdc.md) _ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4e0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde530.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md#insn-00af4cd8) · [`00af4cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md#insn-00af4cf4) · [`00af4d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md#insn-00af4d00)
- 新版 `00af4d1c`（命令位置の公開資料なし） · `00af4d38`（命令位置の公開資料なし） · `00af4d44`（命令位置の公開資料なし）

~~~diff
- 00af4cd8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4cd8 ["INT_ADD", "register:40f0:8", ["const:af4cd8:8", "const:4:8"]]
- 00af4cd8 ["CALLIND", null, ["register:0:8"]]
+ 00af4d1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4d1c ["INT_ADD", "register:40f0:8", ["const:af4d1c:8", "const:4:8"]]
+ 00af4d1c ["CALLIND", null, ["register:0:8"]]
- 00af4cd8 bytes 20013fd6
+ 00af4d1c bytes 20013fd6
- 00af4cf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4cf4 ["INT_ADD", "register:40f0:8", ["const:af4cf4:8", "const:4:8"]]
- 00af4cf4 ["CALLIND", null, ["register:0:8"]]
+ 00af4d38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4d38 ["INT_ADD", "register:40f0:8", ["const:af4d38:8", "const:4:8"]]
+ 00af4d38 ["CALLIND", null, ["register:0:8"]]
- 00af4cf4 bytes 00013fd6
+ 00af4d38 bytes 00013fd6
- 00af4d00 ["INT_ADD", "register:40f0:8", ["const:af4d00:8", "const:4:8"]]
- 00af4d00 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af4d44 ["INT_ADD", "register:40f0:8", ["const:af4d44:8", "const:4:8"]]
+ 00af4d44 ["CALL", null, ["callee:00bdb040:8"]]
- 00af4d00 bytes bc980394
+ 00af4d44 bytes bf980394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7248c59839c63ab781bd653519d6f545"></a>

### [`00af4e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4e14.md) → [`00af4e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4e58.md) _ZN8firebase4util19JLongArrayToVariantEP7_JNIEnvP11_jlongArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde520.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde570.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4e14.md#insn-00af4e54) · [`00af4e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4e14.md#insn-00af4e70) · [`00af4e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4e14.md#insn-00af4e7c)
- 新版 `00af4e98`（命令位置の公開資料なし） · `00af4eb4`（命令位置の公開資料なし） · `00af4ec0`（命令位置の公開資料なし）

~~~diff
- 00af4e54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4e54 ["INT_ADD", "register:40f0:8", ["const:af4e54:8", "const:4:8"]]
- 00af4e54 ["CALLIND", null, ["register:0:8"]]
+ 00af4e98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4e98 ["INT_ADD", "register:40f0:8", ["const:af4e98:8", "const:4:8"]]
+ 00af4e98 ["CALLIND", null, ["register:0:8"]]
- 00af4e54 bytes 20013fd6
+ 00af4e98 bytes 20013fd6
- 00af4e70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4e70 ["INT_ADD", "register:40f0:8", ["const:af4e70:8", "const:4:8"]]
- 00af4e70 ["CALLIND", null, ["register:0:8"]]
+ 00af4eb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4eb4 ["INT_ADD", "register:40f0:8", ["const:af4eb4:8", "const:4:8"]]
+ 00af4eb4 ["CALLIND", null, ["register:0:8"]]
- 00af4e70 bytes 00013fd6
+ 00af4eb4 bytes 00013fd6
- 00af4e7c ["INT_ADD", "register:40f0:8", ["const:af4e7c:8", "const:4:8"]]
- 00af4e7c ["CALL", null, ["callee:00bdb040:8"]]
+ 00af4ec0 ["INT_ADD", "register:40f0:8", ["const:af4ec0:8", "const:4:8"]]
+ 00af4ec0 ["CALL", null, ["callee:00bdb040:8"]]
- 00af4e7c bytes 5d980394
+ 00af4ec0 bytes 60980394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94a118ac31021ad1381bdc0a62d1778d"></a>

### [`00af4f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4f90.md) → [`00af4fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4fd4.md) _ZN8firebase4util20JFloatArrayToVariantEP7_JNIEnvP12_jfloatArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde580.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5d0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4f90.md#insn-00af4fd4) · [`00af4ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4f90.md#insn-00af4ff0) · [`00af4ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4f90.md#insn-00af4ffc)
- 新版 `00af5018`（命令位置の公開資料なし） · `00af5034`（命令位置の公開資料なし） · `00af5040`（命令位置の公開資料なし）

~~~diff
- 00af4fd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4fd4 ["INT_ADD", "register:40f0:8", ["const:af4fd4:8", "const:4:8"]]
- 00af4fd4 ["CALLIND", null, ["register:0:8"]]
+ 00af5018 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af5018 ["INT_ADD", "register:40f0:8", ["const:af5018:8", "const:4:8"]]
+ 00af5018 ["CALLIND", null, ["register:0:8"]]
- 00af4fd4 bytes 20013fd6
+ 00af5018 bytes 20013fd6
- 00af4ff0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4ff0 ["INT_ADD", "register:40f0:8", ["const:af4ff0:8", "const:4:8"]]
- 00af4ff0 ["CALLIND", null, ["register:0:8"]]
+ 00af5034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af5034 ["INT_ADD", "register:40f0:8", ["const:af5034:8", "const:4:8"]]
+ 00af5034 ["CALLIND", null, ["register:0:8"]]
- 00af4ff0 bytes 00013fd6
+ 00af5034 bytes 00013fd6
- 00af4ffc ["INT_ADD", "register:40f0:8", ["const:af4ffc:8", "const:4:8"]]
- 00af4ffc ["CALL", null, ["callee:00bdb040:8"]]
+ 00af5040 ["INT_ADD", "register:40f0:8", ["const:af5040:8", "const:4:8"]]
+ 00af5040 ["CALL", null, ["callee:00bdb040:8"]]
- 00af4ffc bytes fd970394
+ 00af5040 bytes 00980394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce802992579e5d3a4241bd1659895c7c"></a>

### [`00af5118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md) → [`00af515c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af515c.md) _ZN8firebase4util21JDoubleArrayToVariantEP7_JNIEnvP13_jdoubleArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5b0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde600.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af5158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md#insn-00af5158) · [`00af5174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md#insn-00af5174) · [`00af5180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md#insn-00af5180)
- 新版 `00af519c`（命令位置の公開資料なし） · `00af51b8`（命令位置の公開資料なし） · `00af51c4`（命令位置の公開資料なし）

~~~diff
- 00af5158 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af5158 ["INT_ADD", "register:40f0:8", ["const:af5158:8", "const:4:8"]]
- 00af5158 ["CALLIND", null, ["register:0:8"]]
+ 00af519c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af519c ["INT_ADD", "register:40f0:8", ["const:af519c:8", "const:4:8"]]
+ 00af519c ["CALLIND", null, ["register:0:8"]]
- 00af5158 bytes 20013fd6
+ 00af519c bytes 20013fd6
- 00af5174 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5174 ["INT_ADD", "register:40f0:8", ["const:af5174:8", "const:4:8"]]
- 00af5174 ["CALLIND", null, ["register:0:8"]]
+ 00af51b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af51b8 ["INT_ADD", "register:40f0:8", ["const:af51b8:8", "const:4:8"]]
+ 00af51b8 ["CALLIND", null, ["register:0:8"]]
- 00af5174 bytes 00013fd6
+ 00af51b8 bytes 00013fd6
- 00af5180 ["INT_ADD", "register:40f0:8", ["const:af5180:8", "const:4:8"]]
- 00af5180 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af51c4 ["INT_ADD", "register:40f0:8", ["const:af51c4:8", "const:4:8"]]
+ 00af51c4 ["CALL", null, ["callee:00bdb040:8"]]
- 00af5180 bytes 9c970394
+ 00af51c4 bytes 9f970394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbaa97823bebeab504606c4d47b7de84"></a>

### [`00af5294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md) → [`00af52d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af52d8.md) _ZN8firebase4util21JObjectArrayToVariantEP7_JNIEnvP13_jobjectArray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5c0.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde540.md)
- 新版 呼出元 1件 [`00bde610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde610.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af52d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md#insn-00af52d4) · [`00af52e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md#insn-00af52e4) · [`00af52f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md#insn-00af52f8)
- 新版 `00af5318`（命令位置の公開資料なし） · `00af5328`（命令位置の公開資料なし） · `00af533c`（命令位置の公開資料なし）

~~~diff
- 00af52d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af52d4 ["INT_ADD", "register:40f0:8", ["const:af52d4:8", "const:4:8"]]
- 00af52d4 ["CALLIND", null, ["register:0:8"]]
+ 00af5318 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af5318 ["INT_ADD", "register:40f0:8", ["const:af5318:8", "const:4:8"]]
+ 00af5318 ["CALLIND", null, ["register:0:8"]]
- 00af52d4 bytes 20013fd6
+ 00af5318 bytes 20013fd6
- 00af52e4 ["INT_ADD", "register:40f0:8", ["const:af52e4:8", "const:4:8"]]
- 00af52e4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af5328 ["INT_ADD", "register:40f0:8", ["const:af5328:8", "const:4:8"]]
+ 00af5328 ["CALL", null, ["callee:00bdb040:8"]]
- 00af52e4 bytes 43970394
+ 00af5328 bytes 46970394
- 00af52f8 ["INT_ADD", "register:40f0:8", ["const:af52f8:8", "const:4:8"]]
- 00af52f8 ["CALL", null, ["callee:00bde7b0:8"]]
+ 00af533c ["INT_ADD", "register:40f0:8", ["const:af533c:8", "const:4:8"]]
+ 00af533c ["CALL", null, ["callee:00bde7b0:8"]]
- 00af52f8 bytes 1aa50394
+ 00af533c bytes 1da50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0762c248c74dc7af032d4f4610d45237"></a>

### [`00af5820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5820.md) → [`00af5864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5864.md) _ZN8firebase4util25ByteBufferToJavaByteArrayEP7_JNIEnvPKhm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af5848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5820.md#insn-00af5848) · [`00af586c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5820.md#insn-00af586c)
- 新版 `00af588c`（命令位置の公開資料なし） · `00af58b0`（命令位置の公開資料なし）

~~~diff
- 00af5848 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5848 ["INT_ADD", "register:40f0:8", ["const:af5848:8", "const:4:8"]]
- 00af5848 ["CALLIND", null, ["register:0:8"]]
+ 00af588c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af588c ["INT_ADD", "register:40f0:8", ["const:af588c:8", "const:4:8"]]
+ 00af588c ["CALLIND", null, ["register:0:8"]]
- 00af5848 bytes 00013fd6
+ 00af588c bytes 00013fd6
- 00af586c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af586c ["INT_ADD", "register:40f0:8", ["const:af586c:8", "const:4:8"]]
- 00af586c ["CALLIND", null, ["register:0:8"]]
+ 00af58b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af58b0 ["INT_ADD", "register:40f0:8", ["const:af58b0:8", "const:4:8"]]
+ 00af58b0 ["CALLIND", null, ["register:0:8"]]
- 00af586c bytes 00013fd6
+ 00af58b0 bytes 00013fd6
~~~


<a id="compare-61b032db048dddbd529ff243c48b53e3"></a>

### [`00af5ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ba8.md) → [`00af5bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5bec.md) _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5a0.md) · 呼出先 1件 [`00bde790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde790.md)
- 新版 呼出元 1件 [`00bde5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5f0.md) · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af5bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ba8.md#insn-00af5bd4) · [`00af5be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ba8.md#insn-00af5be8) · [`00af5c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ba8.md#insn-00af5c08)
- 新版 `00af5c18`（命令位置の公開資料なし） · `00af5c2c`（命令位置の公開資料なし） · `00af5c4c`（命令位置の公開資料なし）

~~~diff
- 00af5bd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5bd4 ["INT_ADD", "register:40f0:8", ["const:af5bd4:8", "const:4:8"]]
- 00af5bd4 ["CALLIND", null, ["register:0:8"]]
+ 00af5c18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af5c18 ["INT_ADD", "register:40f0:8", ["const:af5c18:8", "const:4:8"]]
+ 00af5c18 ["CALLIND", null, ["register:0:8"]]
- 00af5bd4 bytes 00013fd6
+ 00af5c18 bytes 00013fd6
- 00af5be8 ["INT_ADD", "register:40f0:8", ["const:af5be8:8", "const:4:8"]]
- 00af5be8 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00af5c2c ["INT_ADD", "register:40f0:8", ["const:af5c2c:8", "const:4:8"]]
+ 00af5c2c ["CALL", null, ["callee:00bde7e0:8"]]
- 00af5be8 bytes eaa20394
+ 00af5c2c bytes eda20394
- 00af5c08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5c08 ["INT_ADD", "register:40f0:8", ["const:af5c08:8", "const:4:8"]]
- 00af5c08 ["CALLIND", null, ["register:0:8"]]
+ 00af5c4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af5c4c ["INT_ADD", "register:40f0:8", ["const:af5c4c:8", "const:4:8"]]
+ 00af5c4c ["CALLIND", null, ["register:0:8"]]
- 00af5c08 bytes 00013fd6
+ 00af5c4c bytes 00013fd6
~~~


<a id="compare-449846a2f90c5cdc3d581d7fb2a3ef3e"></a>

### [`00af5c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c2c.md) → [`00af5c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5c70.md) _ZN8firebase4util22LocalToGlobalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af5c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c2c.md#insn-00af5c50) · [`00af5c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c2c.md#insn-00af5c68)
- 新版 `00af5c94`（命令位置の公開資料なし） · `00af5cac`（命令位置の公開資料なし）

~~~diff
- 00af5c50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5c50 ["INT_ADD", "register:40f0:8", ["const:af5c50:8", "const:4:8"]]
- 00af5c50 ["CALLIND", null, ["register:0:8"]]
+ 00af5c94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af5c94 ["INT_ADD", "register:40f0:8", ["const:af5c94:8", "const:4:8"]]
+ 00af5c94 ["CALLIND", null, ["register:0:8"]]
- 00af5c50 bytes 00013fd6
+ 00af5c94 bytes 00013fd6
- 00af5c68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5c68 ["INT_ADD", "register:40f0:8", ["const:af5c68:8", "const:4:8"]]
- 00af5c68 ["CALLIND", null, ["register:0:8"]]
+ 00af5cac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af5cac ["INT_ADD", "register:40f0:8", ["const:af5cac:8", "const:4:8"]]
+ 00af5cac ["CALLIND", null, ["register:0:8"]]
- 00af5c68 bytes 00013fd6
+ 00af5cac bytes 00013fd6
~~~


<a id="compare-ae9c9d0508853699c943e8e7015429ea"></a>

### [`00af5c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c88.md) → [`00af5ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5ccc.md) _ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af5ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c88.md#insn-00af5ca0)
- 新版 `00af5ce4`（命令位置の公開資料なし）

~~~diff
- 00af5ca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5ca0 ["INT_ADD", "register:40f0:8", ["const:af5ca0:8", "const:4:8"]]
- 00af5ca0 ["CALLIND", null, ["register:0:8"]]
+ 00af5ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af5ce4 ["INT_ADD", "register:40f0:8", ["const:af5ce4:8", "const:4:8"]]
+ 00af5ce4 ["CALLIND", null, ["register:0:8"]]
- 00af5ca0 bytes 00013fd6
+ 00af5ce4 bytes 00013fd6
~~~


<a id="compare-5f0907476e0f066f39ee859ae3e8f3b3"></a>

### [`00af6da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6da8.md) → [`00af6dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6dec.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7a0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7f0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6da8.md#insn-00af6e18) · [`00af6e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6da8.md#insn-00af6e38) · [`00af6e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6da8.md#insn-00af6e88)
- 新版 `00af6e5c`（命令位置の公開資料なし） · `00af6e7c`（命令位置の公開資料なし） · `00af6ecc`（命令位置の公開資料なし）

~~~diff
- 00af6e18 ["INT_ADD", "register:40f0:8", ["const:af6e18:8", "const:4:8"]]
- 00af6e18 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af6e5c ["INT_ADD", "register:40f0:8", ["const:af6e5c:8", "const:4:8"]]
+ 00af6e5c ["CALL", null, ["callee:00bdb040:8"]]
- 00af6e18 bytes 76900394
+ 00af6e5c bytes 79900394
- 00af6e38 ["INT_ADD", "register:40f0:8", ["const:af6e38:8", "const:4:8"]]
- 00af6e38 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00af6e7c ["INT_ADD", "register:40f0:8", ["const:af6e7c:8", "const:4:8"]]
+ 00af6e7c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00af6e38 bytes ca900394
+ 00af6e7c bytes cd900394
- 00af6e88 ["INT_ADD", "register:40f0:8", ["const:af6e88:8", "const:4:8"]]
- 00af6e88 ["CALL", null, ["callee:00bdda90:8"]]
+ 00af6ecc ["INT_ADD", "register:40f0:8", ["const:af6ecc:8", "const:4:8"]]
+ 00af6ecc ["CALL", null, ["callee:00bdda90:8"]]
- 00af6e88 bytes ee9a0394
+ 00af6ecc bytes f19a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebc7860823d9c5e76af330bb499608c4"></a>

### [`00af71d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md) → [`00af7218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7218.md) _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0a0.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0f0.md) · 呼出先 1件 [`00bde0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af71f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md#insn-00af71f4) · [`00af720c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md#insn-00af720c) · [`00af721c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md#insn-00af721c)
- 新版 `00af7238`（命令位置の公開資料なし） · `00af7250`（命令位置の公開資料なし） · `00af7260`（命令位置の公開資料なし）

~~~diff
- 00af71f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af71f4 ["INT_ADD", "register:40f0:8", ["const:af71f4:8", "const:4:8"]]
- 00af71f4 ["CALLIND", null, ["register:0:8"]]
+ 00af7238 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af7238 ["INT_ADD", "register:40f0:8", ["const:af7238:8", "const:4:8"]]
+ 00af7238 ["CALLIND", null, ["register:0:8"]]
- 00af71f4 bytes 20013fd6
+ 00af7238 bytes 20013fd6
- 00af720c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af720c ["INT_ADD", "register:40f0:8", ["const:af720c:8", "const:4:8"]]
- 00af720c ["CALLIND", null, ["register:0:8"]]
+ 00af7250 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af7250 ["INT_ADD", "register:40f0:8", ["const:af7250:8", "const:4:8"]]
+ 00af7250 ["CALLIND", null, ["register:0:8"]]
- 00af720c bytes 00013fd6
+ 00af7250 bytes 00013fd6
- 00af721c ["INT_ADD", "register:40f0:8", ["const:af721c:8", "const:4:8"]]
- 00af721c ["CALL", null, ["callee:00bde0d0:8"]]
+ 00af7260 ["INT_ADD", "register:40f0:8", ["const:af7260:8", "const:4:8"]]
+ 00af7260 ["CALL", null, ["callee:00bde0d0:8"]]
- 00af721c bytes 999b0394
+ 00af7260 bytes 9c9b0394
~~~


<a id="compare-35975497b6ed17dd5d6b3c29ab437403"></a>

### [`00af76b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af76b0.md) → [`00af76f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af76f4.md) DetachJVMThreads

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00af7728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7728.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00af776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af776c.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af76e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af76b0.md#insn-00af76e0) · [`00af76f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af76b0.md#insn-00af76f0) · [`00af7714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af76b0.md#insn-00af7714)
- 新版 `00af7724`（命令位置の公開資料なし） · `00af7734`（命令位置の公開資料なし） · `00af7758`（命令位置の公開資料なし）

~~~diff
- 00af76e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af76e0 ["INT_ADD", "register:40f0:8", ["const:af76e0:8", "const:4:8"]]
- 00af76e0 ["CALLIND", null, ["register:0:8"]]
+ 00af7724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af7724 ["INT_ADD", "register:40f0:8", ["const:af7724:8", "const:4:8"]]
+ 00af7724 ["CALLIND", null, ["register:0:8"]]
- 00af76e0 bytes 00013fd6
+ 00af7724 bytes 00013fd6
- 00af76f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af76f0 ["INT_ADD", "register:40f0:8", ["const:af76f0:8", "const:4:8"]]
- 00af76f0 ["CALLIND", null, ["register:0:8"]]
+ 00af7734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af7734 ["INT_ADD", "register:40f0:8", ["const:af7734:8", "const:4:8"]]
+ 00af7734 ["CALLIND", null, ["register:0:8"]]
- 00af76f0 bytes 00013fd6
+ 00af7734 bytes 00013fd6
- 00af7714 ["INT_ADD", "register:40f0:8", ["const:af7714:8", "const:4:8"]]
- 00af7714 ["CALL", null, ["callee:00bdb090:8"]]
+ 00af7758 ["INT_ADD", "register:40f0:8", ["const:af7758:8", "const:4:8"]]
+ 00af7758 ["CALL", null, ["callee:00bdb090:8"]]
- 00af7714 bytes 4b8e0394
+ 00af7758 bytes 4e8e0394
~~~


<a id="compare-76fa63bdb525b83ad1d56a3c108946fd"></a>

### [`00af77cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77cc.md) → [`00af7810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7810.md) _ZN8firebase4util16GetJNIEnvFromAppEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde470.md) · 呼出先 3件 [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde380.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 1件 [`00bde4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4c0.md) · 呼出先 3件 [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3d0.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af77d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77cc.md#insn-00af77d4) · [`00af77dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77cc.md#insn-00af77dc)
- 新版 `00af7818`（命令位置の公開資料なし） · `00af7820`（命令位置の公開資料なし）

~~~diff
- 00af77d4 ["INT_ADD", "register:40f0:8", ["const:af77d4:8", "const:4:8"]]
- 00af77d4 ["CALL", null, ["callee:00bde3d0:8"]]
+ 00af7818 ["INT_ADD", "register:40f0:8", ["const:af7818:8", "const:4:8"]]
+ 00af7818 ["CALL", null, ["callee:00bde3d0:8"]]
- 00af77d4 bytes eb9a0394
+ 00af7818 bytes ee9a0394
- 00af77dc ["INT_ADD", "register:40f0:8", ["const:af77dc:8", "const:4:8"]]
- 00af77dc ["CALL", null, ["callee:00bde3e0:8"]]
+ 00af7820 ["INT_ADD", "register:40f0:8", ["const:af7820:8", "const:4:8"]]
+ 00af7820 ["CALL", null, ["callee:00bde3e0:8"]]
- 00af77dc bytes ed9a0394
+ 00af7820 bytes f09a0394
~~~


<a id="compare-0772e13815998b51cda523a4eb77ba6b"></a>

### [`00af77f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md) → [`00af7838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7838.md) _ZN8firebase7Variant18set_mutable_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6b0.md) · 呼出先 3件 [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdda60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda60.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 1件 [`00bde700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde700.md) · 呼出先 3件 [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bddab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddab0.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md#insn-00af7830) · [`00af7854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md#insn-00af7854) · [`00af7864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md#insn-00af7864)
- 新版 `00af7874`（命令位置の公開資料なし） · `00af7898`（命令位置の公開資料なし） · `00af78a8`（命令位置の公開資料なし）

~~~diff
- 00af7830 ["INT_ADD", "register:40f0:8", ["const:af7830:8", "const:4:8"]]
- 00af7830 ["CALL", null, ["callee:00bdd9e0:8"]]
+ 00af7874 ["INT_ADD", "register:40f0:8", ["const:af7874:8", "const:4:8"]]
+ 00af7874 ["CALL", null, ["callee:00bdd9e0:8"]]
- 00af7830 bytes 58980394
+ 00af7874 bytes 5b980394
- 00af7854 ["INT_ADD", "register:40f0:8", ["const:af7854:8", "const:4:8"]]
- 00af7854 ["CALL", null, ["callee:00bddab0:8"]]
+ 00af7898 ["INT_ADD", "register:40f0:8", ["const:af7898:8", "const:4:8"]]
+ 00af7898 ["CALL", null, ["callee:00bddab0:8"]]
- 00af7854 bytes 83980394
+ 00af7898 bytes 86980394
- 00af7864 ["INT_ADD", "register:40f0:8", ["const:af7864:8", "const:4:8"]]
- 00af7864 ["CALL", null, ["callee:00bdd9e0:8"]]
+ 00af78a8 ["INT_ADD", "register:40f0:8", ["const:af78a8:8", "const:4:8"]]
+ 00af78a8 ["CALL", null, ["callee:00bdd9e0:8"]]
- 00af7864 bytes 4b980394
+ 00af78a8 bytes 4e980394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-523f8286ac3430e6e4ad1cd44890479c"></a>

### [`00af789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af789c.md) → [`00af78e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af78e0.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde740.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde740.md)
- 新版 呼出元 1件 [`00bde790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde790.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af78bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af789c.md#insn-00af78bc) · [`00af78c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af789c.md#insn-00af78c8) · [`00af7900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af789c.md#insn-00af7900)
- 新版 `00af7900`（命令位置の公開資料なし） · `00af790c`（命令位置の公開資料なし） · `00af7944`（命令位置の公開資料なし）

~~~diff
- 00af78bc ["INT_ADD", "register:40f0:8", ["const:af78bc:8", "const:4:8"]]
- 00af78bc ["CALL", null, ["callee:00bde790:8"]]
+ 00af7900 ["INT_ADD", "register:40f0:8", ["const:af7900:8", "const:4:8"]]
+ 00af7900 ["CALL", null, ["callee:00bde790:8"]]
- 00af78bc bytes a19b0394
+ 00af7900 bytes a49b0394
- 00af78c8 ["INT_ADD", "register:40f0:8", ["const:af78c8:8", "const:4:8"]]
- 00af78c8 ["CALL", null, ["callee:00bde790:8"]]
+ 00af790c ["INT_ADD", "register:40f0:8", ["const:af790c:8", "const:4:8"]]
+ 00af790c ["CALL", null, ["callee:00bde790:8"]]
- 00af78c8 bytes 9e9b0394
+ 00af790c bytes a19b0394
- 00af7900 ["INT_ADD", "register:40f0:8", ["const:af7900:8", "const:4:8"]]
- 00af7900 ["CALL", null, ["callee:00bdb060:8"]]
+ 00af7944 ["INT_ADD", "register:40f0:8", ["const:af7944:8", "const:4:8"]]
+ 00af7944 ["CALL", null, ["callee:00bdb060:8"]]
- 00af7900 bytes c48d0394
+ 00af7944 bytes c78d0394
~~~


<a id="compare-31c11c17c3130a8cc6106fd2e18f355f"></a>

### [`00af7ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ac8.md) → [`00af7b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7b0c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ac8.md#insn-00af7b34) · [`00af7b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ac8.md#insn-00af7b54) · [`00af7b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ac8.md#insn-00af7b6c)
- 新版 `00af7b78`（命令位置の公開資料なし） · `00af7b98`（命令位置の公開資料なし） · `00af7bb0`（命令位置の公開資料なし）

~~~diff
- 00af7b34 ["INT_ADD", "register:40f0:8", ["const:af7b34:8", "const:4:8"]]
- 00af7b34 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af7b78 ["INT_ADD", "register:40f0:8", ["const:af7b78:8", "const:4:8"]]
+ 00af7b78 ["CALL", null, ["callee:00bdb040:8"]]
- 00af7b34 bytes 2f8d0394
+ 00af7b78 bytes 328d0394
- 00af7b54 ["INT_ADD", "register:40f0:8", ["const:af7b54:8", "const:4:8"]]
- 00af7b54 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00af7b98 ["INT_ADD", "register:40f0:8", ["const:af7b98:8", "const:4:8"]]
+ 00af7b98 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00af7b54 bytes 838d0394
+ 00af7b98 bytes 868d0394
- 00af7b6c ["INT_ADD", "register:40f0:8", ["const:af7b6c:8", "const:4:8"]]
- 00af7b6c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00af7bb0 ["INT_ADD", "register:40f0:8", ["const:af7bb0:8", "const:4:8"]]
+ 00af7bb0 ["CALL", null, ["callee:00bde2c0:8"]]
- 00af7b6c bytes c1990394
+ 00af7bb0 bytes c4990394
~~~


<a id="compare-3200bc25ec031659b0e08f7e1d976ff6"></a>

### [`00af7b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7b70.md) → [`00af7bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7bb4.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE25__emp

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde720.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)
- 新版 呼出元 1件 [`00bde770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde770.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7b70.md#insn-00af7bac) · [`00af7bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7b70.md#insn-00af7bd0) · [`00af7c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7b70.md#insn-00af7c10)
- 新版 `00af7bf0`（命令位置の公開資料なし） · `00af7c14`（命令位置の公開資料なし） · `00af7c54`（命令位置の公開資料なし）

~~~diff
- 00af7bac ["INT_ADD", "register:40f0:8", ["const:af7bac:8", "const:4:8"]]
- 00af7bac ["CALL", null, ["callee:00bde720:8"]]
+ 00af7bf0 ["INT_ADD", "register:40f0:8", ["const:af7bf0:8", "const:4:8"]]
+ 00af7bf0 ["CALL", null, ["callee:00bde720:8"]]
- 00af7bac bytes c99a0394
+ 00af7bf0 bytes cc9a0394
- 00af7bd0 ["INT_ADD", "register:40f0:8", ["const:af7bd0:8", "const:4:8"]]
- 00af7bd0 ["CALL", null, ["callee:00bde720:8"]]
+ 00af7c14 ["INT_ADD", "register:40f0:8", ["const:af7c14:8", "const:4:8"]]
+ 00af7c14 ["CALL", null, ["callee:00bde720:8"]]
- 00af7bd0 bytes c09a0394
+ 00af7c14 bytes c39a0394
- 00af7c10 ["INT_ADD", "register:40f0:8", ["const:af7c10:8", "const:4:8"]]
- 00af7c10 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af7c54 ["INT_ADD", "register:40f0:8", ["const:af7c54:8", "const:4:8"]]
+ 00af7c54 ["CALL", null, ["callee:00bdb040:8"]]
- 00af7c10 bytes f88c0394
+ 00af7c54 bytes fb8c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87801732c51b3c92dea2c3ec48ef7c9c"></a>

### [`00af7c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7c8c.md) → [`00af7cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7cd0.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde770.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00bde7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7c0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7c8c.md#insn-00af7d0c) · [`00af7d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7c8c.md#insn-00af7d24) · [`00af7da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7c8c.md#insn-00af7da0)
- 新版 `00af7d50`（命令位置の公開資料なし） · `00af7d68`（命令位置の公開資料なし） · `00af7de4`（命令位置の公開資料なし）

~~~diff
- 00af7d0c ["INT_ADD", "register:40f0:8", ["const:af7d0c:8", "const:4:8"]]
- 00af7d0c ["CALL", null, ["callee:00bdb040:8"]]
+ 00af7d50 ["INT_ADD", "register:40f0:8", ["const:af7d50:8", "const:4:8"]]
+ 00af7d50 ["CALL", null, ["callee:00bdb040:8"]]
- 00af7d0c bytes b98c0394
+ 00af7d50 bytes bc8c0394
- 00af7d24 ["INT_ADD", "register:40f0:8", ["const:af7d24:8", "const:4:8"]]
- 00af7d24 ["CALL", null, ["callee:00bde730:8"]]
+ 00af7d68 ["INT_ADD", "register:40f0:8", ["const:af7d68:8", "const:4:8"]]
+ 00af7d68 ["CALL", null, ["callee:00bde730:8"]]
- 00af7d24 bytes 6f9a0394
+ 00af7d68 bytes 729a0394
- 00af7da0 ["INT_ADD", "register:40f0:8", ["const:af7da0:8", "const:4:8"]]
- 00af7da0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00af7de4 ["INT_ADD", "register:40f0:8", ["const:af7de4:8", "const:4:8"]]
+ 00af7de4 ["CALL", null, ["callee:00bdb060:8"]]
- 00af7da0 bytes 9c8c0394
+ 00af7de4 bytes 9f8c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12e8fbcb2cce9b173f947845c0649050"></a>

### [`00af7ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ddc.md) → [`00af7e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ddc.md#insn-00af7e5c) · [`00af7f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ddc.md#insn-00af7f00) · [`00af7f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ddc.md#insn-00af7f38)
- 新版 `00af7ea0`（命令位置の公開資料なし） · `00af7f44`（命令位置の公開資料なし） · `00af7f7c`（命令位置の公開資料なし）

~~~diff
- 00af7e5c ["INT_ADD", "register:40f0:8", ["const:af7e5c:8", "const:4:8"]]
- 00af7e5c ["CALL", null, ["callee:00bdb040:8"]]
+ 00af7ea0 ["INT_ADD", "register:40f0:8", ["const:af7ea0:8", "const:4:8"]]
+ 00af7ea0 ["CALL", null, ["callee:00bdb040:8"]]
- 00af7e5c bytes 658c0394
+ 00af7ea0 bytes 688c0394
- 00af7f00 ["INT_ADD", "register:40f0:8", ["const:af7f00:8", "const:4:8"]]
- 00af7f00 ["CALL", null, ["callee:00bdb060:8"]]
+ 00af7f44 ["INT_ADD", "register:40f0:8", ["const:af7f44:8", "const:4:8"]]
+ 00af7f44 ["CALL", null, ["callee:00bdb060:8"]]
- 00af7f00 bytes 448c0394
+ 00af7f44 bytes 478c0394
- 00af7f38 ["INT_ADD", "register:40f0:8", ["const:af7f38:8", "const:4:8"]]
- 00af7f38 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00af7f7c ["INT_ADD", "register:40f0:8", ["const:af7f7c:8", "const:4:8"]]
+ 00af7f7c ["CALL", null, ["callee:00bde2c0:8"]]
- 00af7f38 bytes ce980394
+ 00af7f7c bytes d1980394
~~~


<a id="compare-a70beff36d617659cad407c3ec5c4125"></a>

### [`00af7f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7f3c.md) → [`00af7f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7f80.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde750.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7a0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7f3c.md#insn-00af7fc4) · [`00af7fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7f3c.md#insn-00af7fe8) · [`00af8014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7f3c.md#insn-00af8014)
- 新版 `00af8008`（命令位置の公開資料なし） · `00af802c`（命令位置の公開資料なし） · `00af8058`（命令位置の公開資料なし）

~~~diff
- 00af7fc4 ["INT_ADD", "register:40f0:8", ["const:af7fc4:8", "const:4:8"]]
- 00af7fc4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af8008 ["INT_ADD", "register:40f0:8", ["const:af8008:8", "const:4:8"]]
+ 00af8008 ["CALL", null, ["callee:00bdb040:8"]]
- 00af7fc4 bytes 0b8c0394
+ 00af8008 bytes 0e8c0394
- 00af7fe8 ["INT_ADD", "register:40f0:8", ["const:af7fe8:8", "const:4:8"]]
- 00af7fe8 ["CALL", null, ["callee:00bdd9f0:8"]]
+ 00af802c ["INT_ADD", "register:40f0:8", ["const:af802c:8", "const:4:8"]]
+ 00af802c ["CALL", null, ["callee:00bdd9f0:8"]]
- 00af7fe8 bytes 6e960394
+ 00af802c bytes 71960394
- 00af8014 ["INT_ADD", "register:40f0:8", ["const:af8014:8", "const:4:8"]]
- 00af8014 ["CALL", null, ["callee:00bdd9f0:8"]]
+ 00af8058 ["INT_ADD", "register:40f0:8", ["const:af8058:8", "const:4:8"]]
+ 00af8058 ["CALL", null, ["callee:00bdd9f0:8"]]
- 00af8014 bytes 63960394
+ 00af8058 bytes 66960394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b5a4315e6230ab0d254bc01a6487236"></a>

### [`00af80a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md) → [`00af80e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af80e4.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde790.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7e0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md#insn-00af811c) · [`00af8134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md#insn-00af8134) · [`00af8150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md#insn-00af8150)
- 新版 `00af8160`（命令位置の公開資料なし） · `00af8178`（命令位置の公開資料なし） · `00af8194`（命令位置の公開資料なし）

~~~diff
- 00af811c ["INT_ADD", "register:40f0:8", ["const:af811c:8", "const:4:8"]]
- 00af811c ["CALL", null, ["callee:00bdb240:8"]]
+ 00af8160 ["INT_ADD", "register:40f0:8", ["const:af8160:8", "const:4:8"]]
+ 00af8160 ["CALL", null, ["callee:00bdb240:8"]]
- 00af811c bytes 358c0394
+ 00af8160 bytes 388c0394
- 00af8134 ["INT_ADD", "register:40f0:8", ["const:af8134:8", "const:4:8"]]
- 00af8134 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af8178 ["INT_ADD", "register:40f0:8", ["const:af8178:8", "const:4:8"]]
+ 00af8178 ["CALL", null, ["callee:00bdb040:8"]]
- 00af8134 bytes af8b0394
+ 00af8178 bytes b28b0394
- 00af8150 ["INT_ADD", "register:40f0:8", ["const:af8150:8", "const:4:8"]]
- 00af8150 ["CALL", null, ["callee:00bdb240:8"]]
+ 00af8194 ["INT_ADD", "register:40f0:8", ["const:af8194:8", "const:4:8"]]
+ 00af8194 ["CALL", null, ["callee:00bdb240:8"]]
- 00af8150 bytes 288c0394
+ 00af8194 bytes 2b8c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab5e27125673d395fd3932d6a9271f37"></a>

### [`00af81b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af81b0.md) → [`00af81f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af81f4.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde730.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)
- 新版 呼出元 1件 [`00bde780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde780.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af822c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af81b0.md#insn-00af822c) · [`00af8264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af81b0.md#insn-00af8264) · [`00af8278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af81b0.md#insn-00af8278)
- 新版 `00af8270`（命令位置の公開資料なし） · `00af82a8`（命令位置の公開資料なし） · `00af82bc`（命令位置の公開資料なし）

~~~diff
- 00af822c ["INT_ADD", "register:40f0:8", ["const:af822c:8", "const:4:8"]]
- 00af822c ["CALL", null, ["callee:00bde750:8"]]
+ 00af8270 ["INT_ADD", "register:40f0:8", ["const:af8270:8", "const:4:8"]]
+ 00af8270 ["CALL", null, ["callee:00bde750:8"]]
- 00af822c bytes 35990394
+ 00af8270 bytes 38990394
- 00af8264 ["INT_ADD", "register:40f0:8", ["const:af8264:8", "const:4:8"]]
- 00af8264 ["CALL", null, ["callee:00bdb060:8"]]
+ 00af82a8 ["INT_ADD", "register:40f0:8", ["const:af82a8:8", "const:4:8"]]
+ 00af82a8 ["CALL", null, ["callee:00bdb060:8"]]
- 00af8264 bytes 6b8b0394
+ 00af82a8 bytes 6e8b0394
- 00af8278 ["INT_ADD", "register:40f0:8", ["const:af8278:8", "const:4:8"]]
- 00af8278 ["CALL", null, ["callee:00bdb060:8"]]
+ 00af82bc ["INT_ADD", "register:40f0:8", ["const:af82bc:8", "const:4:8"]]
+ 00af82bc ["CALL", null, ["callee:00bdb060:8"]]
- 00af8278 bytes 668b0394
+ 00af82bc bytes 698b0394
~~~


<a id="compare-1683a04f9fb3281dd4b3aebac8b907d1"></a>

### [`00af8640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8640.md) → [`00af8684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8684.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) · 呼出先 2件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)
- 新版 呼出元 1件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af86a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8640.md#insn-00af86a4) · [`00af86cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8640.md#insn-00af86cc)
- 新版 `00af86e8`（命令位置の公開資料なし） · `00af8710`（命令位置の公開資料なし）

~~~diff
- 00af86a4 ["INT_ADD", "register:40f0:8", ["const:af86a4:8", "const:4:8"]]
- 00af86a4 ["CALL", null, ["callee:00bde220:8"]]
+ 00af86e8 ["INT_ADD", "register:40f0:8", ["const:af86e8:8", "const:4:8"]]
+ 00af86e8 ["CALL", null, ["callee:00bde220:8"]]
- 00af86a4 bytes cb960394
+ 00af86e8 bytes ce960394
- 00af86cc ["INT_ADD", "register:40f0:8", ["const:af86cc:8", "const:4:8"]]
- 00af86cc ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00af8710 ["INT_ADD", "register:40f0:8", ["const:af8710:8", "const:4:8"]]
+ 00af8710 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00af86cc bytes a58a0394
+ 00af8710 bytes a88a0394
~~~


<a id="compare-a9ad78d9a6f082d05ae8d9f4bc1e4954"></a>

### [`00af8704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8704.md) → [`00af8748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8748.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af87a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8704.md#insn-00af87a0) · [`00af87b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8704.md#insn-00af87b8) · [`00af87d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8704.md#insn-00af87d8)
- 新版 `00af87e4`（命令位置の公開資料なし） · `00af87fc`（命令位置の公開資料なし） · `00af881c`（命令位置の公開資料なし）

~~~diff
- 00af87a0 ["INT_ADD", "register:40f0:8", ["const:af87a0:8", "const:4:8"]]
- 00af87a0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af87e4 ["INT_ADD", "register:40f0:8", ["const:af87e4:8", "const:4:8"]]
+ 00af87e4 ["CALL", null, ["callee:00bdb040:8"]]
- 00af87a0 bytes 148a0394
+ 00af87e4 bytes 178a0394
- 00af87b8 ["INT_ADD", "register:40f0:8", ["const:af87b8:8", "const:4:8"]]
- 00af87b8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00af87fc ["INT_ADD", "register:40f0:8", ["const:af87fc:8", "const:4:8"]]
+ 00af87fc ["CALL", null, ["callee:00bdb1b0:8"]]
- 00af87b8 bytes 6a8a0394
+ 00af87fc bytes 6d8a0394
- 00af87d8 ["INT_ADD", "register:40f0:8", ["const:af87d8:8", "const:4:8"]]
- 00af87d8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00af881c ["INT_ADD", "register:40f0:8", ["const:af881c:8", "const:4:8"]]
+ 00af881c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00af87d8 bytes 628a0394
+ 00af881c bytes 658a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc808c11e7db5577918e507eb4cffb27"></a>

### [`00af8900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8900.md) → [`00af8944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8944.md) _ZN8firebase8internal16JObjectReferenceC1EP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2c0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde310.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8900.md#insn-00af8938) · [`00af8964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8900.md#insn-00af8964)
- 新版 `00af897c`（命令位置の公開資料なし） · `00af89a8`（命令位置の公開資料なし）

~~~diff
- 00af8938 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af8938 ["INT_ADD", "register:40f0:8", ["const:af8938:8", "const:4:8"]]
- 00af8938 ["CALLIND", null, ["register:0:8"]]
+ 00af897c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af897c ["INT_ADD", "register:40f0:8", ["const:af897c:8", "const:4:8"]]
+ 00af897c ["CALLIND", null, ["register:0:8"]]
- 00af8938 bytes 20013fd6
+ 00af897c bytes 20013fd6
- 00af8964 ["INT_ADD", "register:40f0:8", ["const:af8964:8", "const:4:8"]]
- 00af8964 ["CALL", null, ["callee:00bdb090:8"]]
+ 00af89a8 ["INT_ADD", "register:40f0:8", ["const:af89a8:8", "const:4:8"]]
+ 00af89a8 ["CALL", null, ["callee:00bdb090:8"]]
- 00af8964 bytes b7890394
+ 00af89a8 bytes ba890394
~~~


<a id="compare-85be8809266ca2c2f594916b6401d298"></a>

### [`00af8968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8968.md) → [`00af89ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af89ac.md) _ZN8firebase8internal16JObjectReference9GetJavaVMEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8968.md#insn-00af8994) · [`00af89bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8968.md#insn-00af89bc)
- 新版 `00af89d8`（命令位置の公開資料なし） · `00af8a00`（命令位置の公開資料なし）

~~~diff
- 00af8994 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8994 ["INT_ADD", "register:40f0:8", ["const:af8994:8", "const:4:8"]]
- 00af8994 ["CALLIND", null, ["register:0:8"]]
+ 00af89d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af89d8 ["INT_ADD", "register:40f0:8", ["const:af89d8:8", "const:4:8"]]
+ 00af89d8 ["CALLIND", null, ["register:0:8"]]
- 00af8994 bytes 00013fd6
+ 00af89d8 bytes 00013fd6
- 00af89bc ["INT_ADD", "register:40f0:8", ["const:af89bc:8", "const:4:8"]]
- 00af89bc ["CALL", null, ["callee:00bdb090:8"]]
+ 00af8a00 ["INT_ADD", "register:40f0:8", ["const:af8a00:8", "const:4:8"]]
+ 00af8a00 ["CALL", null, ["callee:00bdb090:8"]]
- 00af89bc bytes a1890394
+ 00af8a00 bytes a4890394
~~~


<a id="compare-639a61323d45cb20c30da58f59e9ca0b"></a>

### [`00af89c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af89c0.md) → [`00af8a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8a04.md) _ZN8firebase8internal16JObjectReferenceC2EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af89c0.md#insn-00af8a00) · [`00af8a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af89c0.md#insn-00af8a20) · [`00af8a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af89c0.md#insn-00af8a4c)
- 新版 `00af8a44`（命令位置の公開資料なし） · `00af8a64`（命令位置の公開資料なし） · `00af8a90`（命令位置の公開資料なし）

~~~diff
- 00af8a00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8a00 ["INT_ADD", "register:40f0:8", ["const:af8a00:8", "const:4:8"]]
- 00af8a00 ["CALLIND", null, ["register:0:8"]]
+ 00af8a44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8a44 ["INT_ADD", "register:40f0:8", ["const:af8a44:8", "const:4:8"]]
+ 00af8a44 ["CALLIND", null, ["register:0:8"]]
- 00af8a00 bytes 00013fd6
+ 00af8a44 bytes 00013fd6
- 00af8a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8a20 ["INT_ADD", "register:40f0:8", ["const:af8a20:8", "const:4:8"]]
- 00af8a20 ["CALLIND", null, ["register:0:8"]]
+ 00af8a64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8a64 ["INT_ADD", "register:40f0:8", ["const:af8a64:8", "const:4:8"]]
+ 00af8a64 ["CALLIND", null, ["register:0:8"]]
- 00af8a20 bytes 00013fd6
+ 00af8a64 bytes 00013fd6
- 00af8a4c ["INT_ADD", "register:40f0:8", ["const:af8a4c:8", "const:4:8"]]
- 00af8a4c ["CALL", null, ["callee:00bdb090:8"]]
+ 00af8a90 ["INT_ADD", "register:40f0:8", ["const:af8a90:8", "const:4:8"]]
+ 00af8a90 ["CALL", null, ["callee:00bdb090:8"]]
- 00af8a4c bytes 7d890394
+ 00af8a90 bytes 80890394
~~~


<a id="compare-449c430b9887618095708b6e5a4e82f0"></a>

### [`00af8a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8a50.md) → [`00af8a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8a94.md) _ZN8firebase8internal16JObjectReference10InitializeEP7_JavaVMP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8a50.md#insn-00af8a78)
- 新版 `00af8abc`（命令位置の公開資料なし）

~~~diff
- 00af8a78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8a78 ["INT_ADD", "register:40f0:8", ["const:af8a78:8", "const:4:8"]]
- 00af8a78 ["CALLIND", null, ["register:0:8"]]
+ 00af8abc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8abc ["INT_ADD", "register:40f0:8", ["const:af8abc:8", "const:4:8"]]
+ 00af8abc ["CALLIND", null, ["register:0:8"]]
- 00af8a78 bytes 00013fd6
+ 00af8abc bytes 00013fd6
~~~


<a id="compare-b5977e9fa196fec90873d1fe2fafac90"></a>

### [`00af8a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8a8c.md) → [`00af8ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8ad0.md) _ZN8firebase8internal16JObjectReferenceC2ERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2d0.md) · 呼出先 1件 [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 1件 [`00bde320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde320.md) · 呼出先 1件 [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8a8c.md#insn-00af8ab0) · [`00af8ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8a8c.md#insn-00af8ad0)
- 新版 `00af8af4`（命令位置の公開資料なし） · `00af8b14`（命令位置の公開資料なし）

~~~diff
- 00af8ab0 ["INT_ADD", "register:40f0:8", ["const:af8ab0:8", "const:4:8"]]
- 00af8ab0 ["CALL", null, ["callee:00bde540:8"]]
+ 00af8af4 ["INT_ADD", "register:40f0:8", ["const:af8af4:8", "const:4:8"]]
+ 00af8af4 ["CALL", null, ["callee:00bde540:8"]]
- 00af8ab0 bytes 90960394
+ 00af8af4 bytes 93960394
- 00af8ad0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8ad0 ["INT_ADD", "register:40f0:8", ["const:af8ad0:8", "const:4:8"]]
- 00af8ad0 ["CALLIND", null, ["register:0:8"]]
+ 00af8b14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8b14 ["INT_ADD", "register:40f0:8", ["const:af8b14:8", "const:4:8"]]
+ 00af8b14 ["CALLIND", null, ["register:0:8"]]
- 00af8ad0 bytes 00013fd6
+ 00af8b14 bytes 00013fd6
~~~


<a id="compare-18c96f24b4ff1684a34f1b192ed8f8f5"></a>

### [`00af8b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b18.md) → [`00af8b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8b5c.md) _ZN8firebase8internal16JObjectReferenceD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bde2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2e0.md) [`00bde2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2f0.md) · 呼出先 1件 [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 2件 [`00bde330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde330.md) [`00bde340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde340.md) · 呼出先 1件 [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b18.md#insn-00af8b30) · [`00af8b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b18.md#insn-00af8b48)
- 新版 `00af8b74`（命令位置の公開資料なし） · `00af8b8c`（命令位置の公開資料なし）

~~~diff
- 00af8b30 ["INT_ADD", "register:40f0:8", ["const:af8b30:8", "const:4:8"]]
- 00af8b30 ["CALL", null, ["callee:00bde540:8"]]
+ 00af8b74 ["INT_ADD", "register:40f0:8", ["const:af8b74:8", "const:4:8"]]
+ 00af8b74 ["CALL", null, ["callee:00bde540:8"]]
- 00af8b30 bytes 70960394
+ 00af8b74 bytes 73960394
- 00af8b48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8b48 ["INT_ADD", "register:40f0:8", ["const:af8b48:8", "const:4:8"]]
- 00af8b48 ["CALLIND", null, ["register:0:8"]]
+ 00af8b8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8b8c ["INT_ADD", "register:40f0:8", ["const:af8b8c:8", "const:4:8"]]
+ 00af8b8c ["CALLIND", null, ["register:0:8"]]
- 00af8b48 bytes 00013fd6
+ 00af8b8c bytes 00013fd6
~~~


<a id="compare-79fa0db19ffb7ae5663c64a0c66b4f18"></a>

### [`00af8b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b5c.md) → [`00af8ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8ba0.md) _ZN8firebase8internal16JObjectReference3SetEP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2b0.md) · 呼出先 1件 [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 1件 [`00bde300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde300.md) · 呼出先 1件 [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b5c.md#insn-00af8b7c) · [`00af8b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b5c.md#insn-00af8b9c) · [`00af8bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b5c.md#insn-00af8bc8)
- 新版 `00af8bc0`（命令位置の公開資料なし） · `00af8be0`（命令位置の公開資料なし） · `00af8c0c`（命令位置の公開資料なし）

~~~diff
- 00af8b7c ["INT_ADD", "register:40f0:8", ["const:af8b7c:8", "const:4:8"]]
- 00af8b7c ["CALL", null, ["callee:00bde540:8"]]
+ 00af8bc0 ["INT_ADD", "register:40f0:8", ["const:af8bc0:8", "const:4:8"]]
+ 00af8bc0 ["CALL", null, ["callee:00bde540:8"]]
- 00af8b7c bytes 5d960394
+ 00af8bc0 bytes 60960394
- 00af8b9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8b9c ["INT_ADD", "register:40f0:8", ["const:af8b9c:8", "const:4:8"]]
- 00af8b9c ["CALLIND", null, ["register:0:8"]]
+ 00af8be0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8be0 ["INT_ADD", "register:40f0:8", ["const:af8be0:8", "const:4:8"]]
+ 00af8be0 ["CALLIND", null, ["register:0:8"]]
- 00af8b9c bytes 00013fd6
+ 00af8be0 bytes 00013fd6
- 00af8bc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8bc8 ["INT_ADD", "register:40f0:8", ["const:af8bc8:8", "const:4:8"]]
- 00af8bc8 ["CALLIND", null, ["register:0:8"]]
+ 00af8c0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8c0c ["INT_ADD", "register:40f0:8", ["const:af8c0c:8", "const:4:8"]]
+ 00af8c0c ["CALLIND", null, ["register:0:8"]]
- 00af8bc8 bytes 00013fd6
+ 00af8c0c bytes 00013fd6
~~~


<a id="compare-07f34a64cf43e5f529d1997ca9903804"></a>

### [`00af8be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8be0.md) → [`00af8c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8c24.md) _ZN8firebase8internal16JObjectReferenceaSERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8be0.md#insn-00af8c14) · [`00af8c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8be0.md#insn-00af8c38) · [`00af8c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8be0.md#insn-00af8c60)
- 新版 `00af8c58`（命令位置の公開資料なし） · `00af8c7c`（命令位置の公開資料なし） · `00af8ca4`（命令位置の公開資料なし）

~~~diff
- 00af8c14 ["INT_ADD", "register:40f0:8", ["const:af8c14:8", "const:4:8"]]
- 00af8c14 ["CALL", null, ["callee:00bde540:8"]]
+ 00af8c58 ["INT_ADD", "register:40f0:8", ["const:af8c58:8", "const:4:8"]]
+ 00af8c58 ["CALL", null, ["callee:00bde540:8"]]
- 00af8c14 bytes 37960394
+ 00af8c58 bytes 3a960394
- 00af8c38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8c38 ["INT_ADD", "register:40f0:8", ["const:af8c38:8", "const:4:8"]]
- 00af8c38 ["CALLIND", null, ["register:0:8"]]
+ 00af8c7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8c7c ["INT_ADD", "register:40f0:8", ["const:af8c7c:8", "const:4:8"]]
+ 00af8c7c ["CALLIND", null, ["register:0:8"]]
- 00af8c38 bytes 00013fd6
+ 00af8c7c bytes 00013fd6
- 00af8c60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8c60 ["INT_ADD", "register:40f0:8", ["const:af8c60:8", "const:4:8"]]
- 00af8c60 ["CALLIND", null, ["register:0:8"]]
+ 00af8ca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8ca4 ["INT_ADD", "register:40f0:8", ["const:af8ca4:8", "const:4:8"]]
+ 00af8ca4 ["CALLIND", null, ["register:0:8"]]
- 00af8c60 bytes 00013fd6
+ 00af8ca4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78a2e20686cb6f4bead842a3209639b0"></a>

### [`00af8cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8cb4.md) → [`00af8cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8cf8.md) _ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8cb4.md#insn-00af8cf8) · [`00af8d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8cb4.md#insn-00af8d14) · [`00af8d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8cb4.md#insn-00af8d34)
- 新版 `00af8d3c`（命令位置の公開資料なし） · `00af8d58`（命令位置の公開資料なし） · `00af8d78`（命令位置の公開資料なし）

~~~diff
- 00af8cf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8cf8 ["INT_ADD", "register:40f0:8", ["const:af8cf8:8", "const:4:8"]]
- 00af8cf8 ["CALLIND", null, ["register:0:8"]]
+ 00af8d3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8d3c ["INT_ADD", "register:40f0:8", ["const:af8d3c:8", "const:4:8"]]
+ 00af8d3c ["CALLIND", null, ["register:0:8"]]
- 00af8cf8 bytes 00013fd6
+ 00af8d3c bytes 00013fd6
- 00af8d14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8d14 ["INT_ADD", "register:40f0:8", ["const:af8d14:8", "const:4:8"]]
- 00af8d14 ["CALLIND", null, ["register:0:8"]]
+ 00af8d58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8d58 ["INT_ADD", "register:40f0:8", ["const:af8d58:8", "const:4:8"]]
+ 00af8d58 ["CALLIND", null, ["register:0:8"]]
- 00af8d14 bytes 00013fd6
+ 00af8d58 bytes 00013fd6
- 00af8d34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8d34 ["INT_ADD", "register:40f0:8", ["const:af8d34:8", "const:4:8"]]
- 00af8d34 ["CALLIND", null, ["register:0:8"]]
+ 00af8d78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8d78 ["INT_ADD", "register:40f0:8", ["const:af8d78:8", "const:4:8"]]
+ 00af8d78 ["CALLIND", null, ["register:0:8"]]
- 00af8d34 bytes 00013fd6
+ 00af8d78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca8d5232adc43ca12b3c8ab860991dec"></a>

### [`00af8d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8d64.md) → [`00af8da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8da8.md) _ZNK8firebase8internal16JObjectReference11GetLocalRefEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde300.md) · 呼出先 1件 [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 1件 [`00bde350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde350.md) · 呼出先 1件 [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8d64.md#insn-00af8d7c)
- 新版 `00af8dc0`（命令位置の公開資料なし）

~~~diff
- 00af8d7c ["INT_ADD", "register:40f0:8", ["const:af8d7c:8", "const:4:8"]]
- 00af8d7c ["CALL", null, ["callee:00bde540:8"]]
+ 00af8dc0 ["INT_ADD", "register:40f0:8", ["const:af8dc0:8", "const:4:8"]]
+ 00af8dc0 ["CALL", null, ["callee:00bde540:8"]]
- 00af8d7c bytes dd950394
+ 00af8dc0 bytes e0950394
~~~


<a id="compare-b106fbee8d5c8ee2a92287a432b09252"></a>

### [`00af8db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8db0.md) → [`00af8df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8df4.md) _ZN8firebase8internal16JObjectReference18FromLocalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2a0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2f0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8db0.md#insn-00af8dec) · [`00af8e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8db0.md#insn-00af8e0c) · [`00af8e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8db0.md#insn-00af8e24)
- 新版 `00af8e30`（命令位置の公開資料なし） · `00af8e50`（命令位置の公開資料なし） · `00af8e68`（命令位置の公開資料なし）

~~~diff
- 00af8dec ["COPY", "register:0:8", ["register:4048:8"]]
- 00af8dec ["INT_ADD", "register:40f0:8", ["const:af8dec:8", "const:4:8"]]
- 00af8dec ["CALLIND", null, ["register:0:8"]]
+ 00af8e30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af8e30 ["INT_ADD", "register:40f0:8", ["const:af8e30:8", "const:4:8"]]
+ 00af8e30 ["CALLIND", null, ["register:0:8"]]
- 00af8dec bytes 20013fd6
+ 00af8e30 bytes 20013fd6
- 00af8e0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8e0c ["INT_ADD", "register:40f0:8", ["const:af8e0c:8", "const:4:8"]]
- 00af8e0c ["CALLIND", null, ["register:0:8"]]
+ 00af8e50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8e50 ["INT_ADD", "register:40f0:8", ["const:af8e50:8", "const:4:8"]]
+ 00af8e50 ["CALLIND", null, ["register:0:8"]]
- 00af8e0c bytes 00013fd6
+ 00af8e50 bytes 00013fd6
- 00af8e24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8e24 ["INT_ADD", "register:40f0:8", ["const:af8e24:8", "const:4:8"]]
- 00af8e24 ["CALLIND", null, ["register:0:8"]]
+ 00af8e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8e68 ["INT_ADD", "register:40f0:8", ["const:af8e68:8", "const:4:8"]]
+ 00af8e68 ["CALLIND", null, ["register:0:8"]]
- 00af8e24 bytes 00013fd6
+ 00af8e68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435c325130240cf3f0b04e1e9c978c64"></a>

### [`00af9ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ab4.md) → [`00af9af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9af8.md) _ZN8firebase10app_common15LibraryRegistry15RegisterLibraryEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde830.md) · 呼出先 12件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00470ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ef0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde880.md) · 呼出先 12件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00470ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ef0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af9af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ab4.md#insn-00af9af8) · [`00af9b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ab4.md#insn-00af9b34) · [`00af9b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ab4.md#insn-00af9b54)
- 新版 `00af9b3c`（命令位置の公開資料なし） · `00af9b78`（命令位置の公開資料なし） · `00af9b98`（命令位置の公開資料なし）

~~~diff
- 00af9af8 ["INT_ADD", "register:40f0:8", ["const:af9af8:8", "const:4:8"]]
- 00af9af8 ["CALL", null, ["callee:00bdb190:8"]]
+ 00af9b3c ["INT_ADD", "register:40f0:8", ["const:af9b3c:8", "const:4:8"]]
+ 00af9b3c ["CALL", null, ["callee:00bdb190:8"]]
- 00af9af8 bytes 92850394
+ 00af9b3c bytes 95850394
- 00af9b34 ["INT_ADD", "register:40f0:8", ["const:af9b34:8", "const:4:8"]]
- 00af9b34 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af9b78 ["INT_ADD", "register:40f0:8", ["const:af9b78:8", "const:4:8"]]
+ 00af9b78 ["CALL", null, ["callee:00bdb040:8"]]
- 00af9b34 bytes 2f850394
+ 00af9b78 bytes 32850394
- 00af9b54 ["INT_ADD", "register:40f0:8", ["const:af9b54:8", "const:4:8"]]
- 00af9b54 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00af9b98 ["INT_ADD", "register:40f0:8", ["const:af9b98:8", "const:4:8"]]
+ 00af9b98 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00af9b54 bytes 83850394
+ 00af9b98 bytes 86850394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5501b0eb11b59857217676a6c8fe2017"></a>

### [`00af9ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md) → [`00af9f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md) _ZN8firebase10app_common15LibraryRegistry15UpdateUserAgentEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde840.md) · 呼出先 5件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)
- 新版 呼出元 1件 [`00bde890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde890.md) · 呼出先 5件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af9f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md#insn-00af9f78) · [`00af9f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md#insn-00af9f9c) · [`00af9fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md#insn-00af9fc4)
- 新版 `00af9fbc`（命令位置の公開資料なし） · `00af9fe0`（命令位置の公開資料なし） · `00afa008`（命令位置の公開資料なし）

~~~diff
- 00af9f78 ["INT_ADD", "register:40f0:8", ["const:af9f78:8", "const:4:8"]]
- 00af9f78 ["CALL", null, ["callee:00afaa08:8"]]
+ 00af9fbc ["INT_ADD", "register:40f0:8", ["const:af9fbc:8", "const:4:8"]]
+ 00af9fbc ["CALL", null, ["callee:00afaa08:8"]]
- 00af9f78 bytes 93020094
+ 00af9fbc bytes 93020094
- 00af9f9c ["INT_ADD", "register:40f0:8", ["const:af9f9c:8", "const:4:8"]]
- 00af9f9c ["CALL", null, ["callee:00bdb130:8"]]
+ 00af9fe0 ["INT_ADD", "register:40f0:8", ["const:af9fe0:8", "const:4:8"]]
+ 00af9fe0 ["CALL", null, ["callee:00bdb130:8"]]
- 00af9f9c bytes 51840394
+ 00af9fe0 bytes 54840394
- 00af9fc4 ["INT_ADD", "register:40f0:8", ["const:af9fc4:8", "const:4:8"]]
- 00af9fc4 ["CALL", null, ["callee:00bdb130:8"]]
+ 00afa008 ["INT_ADD", "register:40f0:8", ["const:afa008:8", "const:4:8"]]
+ 00afa008 ["CALL", null, ["callee:00bdb130:8"]]
- 00af9fc4 bytes 47840394
+ 00afa008 bytes 4a840394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-440c37cbf2f262e624cad3bcd7c9c5a2"></a>

### [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) → [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) FUN_00afaa08

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00af9ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md) [`00afd448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md) [`00afd50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md) [`00b11684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md) [`00b127dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 8件 [`00af9f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md) [`00afd48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md) [`00afd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md) [`00b116c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md) [`00b12820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afaa00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md#insn-00afaa00) · [`00afaa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md#insn-00afaa18) · [`00afaa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md#insn-00afaa58)
- 新版 `00afaa44`（命令位置の公開資料なし） · `00afaa5c`（命令位置の公開資料なし） · `00afaa9c`（命令位置の公開資料なし）

~~~diff
- 00afaa00 ["INT_ADD", "register:40f0:8", ["const:afaa00:8", "const:4:8"]]
- 00afaa00 ["CALL", null, ["callee:00bdb190:8"]]
+ 00afaa44 ["INT_ADD", "register:40f0:8", ["const:afaa44:8", "const:4:8"]]
+ 00afaa44 ["CALL", null, ["callee:00bdb190:8"]]
- 00afaa00 bytes d0810394
+ 00afaa44 bytes d3810394
- 00afaa18 ["INT_ADD", "register:40f0:8", ["const:afaa18:8", "const:4:8"]]
- 00afaa18 ["CALL", null, ["callee:00bdb190:8"]]
+ 00afaa5c ["INT_ADD", "register:40f0:8", ["const:afaa5c:8", "const:4:8"]]
+ 00afaa5c ["CALL", null, ["callee:00bdb190:8"]]
- 00afaa18 bytes ca810394
+ 00afaa5c bytes cd810394
- 00afaa58 ["INT_ADD", "register:40f0:8", ["const:afaa58:8", "const:4:8"]]
- 00afaa58 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afaa9c ["INT_ADD", "register:40f0:8", ["const:afaa9c:8", "const:4:8"]]
+ 00afaa9c ["CALL", null, ["callee:00bdb040:8"]]
- 00afaa58 bytes 66810394
+ 00afaa9c bytes 69810394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9702e620d9be57dd54ab8d4e0b8dae30"></a>

### [`00afaaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md) → [`00afaaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaaf0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afab2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md#insn-00afab2c) · [`00afab4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md#insn-00afab4c) · [`00afab68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md#insn-00afab68)
- 新版 `00afab70`（命令位置の公開資料なし） · `00afab90`（命令位置の公開資料なし） · `00afabac`（命令位置の公開資料なし）

~~~diff
- 00afab2c ["INT_ADD", "register:40f0:8", ["const:afab2c:8", "const:4:8"]]
- 00afab2c ["CALL", null, ["callee:00bdb040:8"]]
+ 00afab70 ["INT_ADD", "register:40f0:8", ["const:afab70:8", "const:4:8"]]
+ 00afab70 ["CALL", null, ["callee:00bdb040:8"]]
- 00afab2c bytes 31810394
+ 00afab70 bytes 34810394
- 00afab4c ["INT_ADD", "register:40f0:8", ["const:afab4c:8", "const:4:8"]]
- 00afab4c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00afab90 ["INT_ADD", "register:40f0:8", ["const:afab90:8", "const:4:8"]]
+ 00afab90 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00afab4c bytes 85810394
+ 00afab90 bytes 88810394
- 00afab68 ["INT_ADD", "register:40f0:8", ["const:afab68:8", "const:4:8"]]
- 00afab68 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00afabac ["INT_ADD", "register:40f0:8", ["const:afabac:8", "const:4:8"]]
+ 00afabac ["CALL", null, ["callee:00bde2c0:8"]]
- 00afab68 bytes c28d0394
+ 00afabac bytes c58d0394
~~~


<a id="compare-4181f339f0e103f6989ddefca5b18f8d"></a>

### [`00afab6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afab6c.md) → [`00afabb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde930.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bde980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde980.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afac08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afab6c.md#insn-00afac08) · [`00afac48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afab6c.md#insn-00afac48)
- 新版 `00afac4c`（命令位置の公開資料なし） · `00afac8c`（命令位置の公開資料なし）

~~~diff
- 00afac08 ["INT_ADD", "register:40f0:8", ["const:afac08:8", "const:4:8"]]
- 00afac08 ["CALL", null, ["callee:00bdb200:8"]]
+ 00afac4c ["INT_ADD", "register:40f0:8", ["const:afac4c:8", "const:4:8"]]
+ 00afac4c ["CALL", null, ["callee:00bdb200:8"]]
- 00afac08 bytes 6a810394
+ 00afac4c bytes 6d810394
- 00afac48 ["INT_ADD", "register:40f0:8", ["const:afac48:8", "const:4:8"]]
- 00afac48 ["CALL", null, ["callee:00bdb200:8"]]
+ 00afac8c ["INT_ADD", "register:40f0:8", ["const:afac8c:8", "const:4:8"]]
+ 00afac8c ["CALL", null, ["callee:00bdb200:8"]]
- 00afac48 bytes 5a810394
+ 00afac8c bytes 5d810394
~~~


<a id="compare-c88651b0f6ac1d162c1b80a6567d9942"></a>

### [`00afac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md) → [`00afacd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afacd0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde940.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bde990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde990.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afad24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md#insn-00afad24) · [`00afad6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md#insn-00afad6c)
- 新版 `00afad68`（命令位置の公開資料なし） · `00afadb0`（命令位置の公開資料なし）

~~~diff
- 00afad24 ["INT_ADD", "register:40f0:8", ["const:afad24:8", "const:4:8"]]
- 00afad24 ["CALL", null, ["callee:00bdb200:8"]]
+ 00afad68 ["INT_ADD", "register:40f0:8", ["const:afad68:8", "const:4:8"]]
+ 00afad68 ["CALL", null, ["callee:00bdb200:8"]]
- 00afad24 bytes 23810394
+ 00afad68 bytes 26810394
- 00afad6c ["INT_ADD", "register:40f0:8", ["const:afad6c:8", "const:4:8"]]
- 00afad6c ["CALL", null, ["callee:00bdb200:8"]]
+ 00afadb0 ["INT_ADD", "register:40f0:8", ["const:afadb0:8", "const:4:8"]]
+ 00afadb0 ["CALL", null, ["callee:00bdb200:8"]]
- 00afad6c bytes 11810394
+ 00afadb0 bytes 14810394
~~~


<a id="compare-acdbb2b39beee29b069c43cb094d672d"></a>

### [`00afada0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afada0.md) → [`00afade4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afade4.md) _ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde970.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9c0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afae04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afada0.md#insn-00afae04) · [`00afae10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afada0.md#insn-00afae10) · [`00afae3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afada0.md#insn-00afae3c)
- 新版 `00afae48`（命令位置の公開資料なし） · `00afae54`（命令位置の公開資料なし） · `00afae80`（命令位置の公開資料なし）

~~~diff
- 00afae04 ["INT_ADD", "register:40f0:8", ["const:afae04:8", "const:4:8"]]
- 00afae04 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00afae48 ["INT_ADD", "register:40f0:8", ["const:afae48:8", "const:4:8"]]
+ 00afae48 ["CALL", null, ["callee:00bde2c0:8"]]
- 00afae04 bytes 1b8d0394
+ 00afae48 bytes 1e8d0394
- 00afae10 ["INT_ADD", "register:40f0:8", ["const:afae10:8", "const:4:8"]]
- 00afae10 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afae54 ["INT_ADD", "register:40f0:8", ["const:afae54:8", "const:4:8"]]
+ 00afae54 ["CALL", null, ["callee:00bdb040:8"]]
- 00afae10 bytes 78800394
+ 00afae54 bytes 7b800394
- 00afae3c ["INT_ADD", "register:40f0:8", ["const:afae3c:8", "const:4:8"]]
- 00afae3c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00afae80 ["INT_ADD", "register:40f0:8", ["const:afae80:8", "const:4:8"]]
+ 00afae80 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00afae3c bytes c9800394
+ 00afae80 bytes cc800394
~~~


<a id="compare-035ce3079453cc7236c102138edff07c"></a>

### [`00afae88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md) → [`00afaecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde950.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) [`00bde290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde290.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)
- 新版 呼出元 1件 [`00bde9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9a0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddd0.md) [`00bde2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2e0.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afaf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md#insn-00afaf04) · [`00afaf18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md#insn-00afaf18) · [`00afaf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md#insn-00afaf20)
- 新版 `00afaf48`（命令位置の公開資料なし） · `00afaf5c`（命令位置の公開資料なし） · `00afaf64`（命令位置の公開資料なし）

~~~diff
- 00afaf04 ["INT_ADD", "register:40f0:8", ["const:afaf04:8", "const:4:8"]]
- 00afaf04 ["CALL", null, ["callee:00bde750:8"]]
+ 00afaf48 ["INT_ADD", "register:40f0:8", ["const:afaf48:8", "const:4:8"]]
+ 00afaf48 ["CALL", null, ["callee:00bde750:8"]]
- 00afaf04 bytes ff8d0394
+ 00afaf48 bytes 028e0394
- 00afaf18 ["INT_ADD", "register:40f0:8", ["const:afaf18:8", "const:4:8"]]
- 00afaf18 ["CALL", null, ["callee:00bde2e0:8"]]
+ 00afaf5c ["INT_ADD", "register:40f0:8", ["const:afaf5c:8", "const:4:8"]]
+ 00afaf5c ["CALL", null, ["callee:00bde2e0:8"]]
- 00afaf18 bytes de8c0394
+ 00afaf5c bytes e18c0394
- 00afaf20 ["INT_ADD", "register:40f0:8", ["const:afaf20:8", "const:4:8"]]
- 00afaf20 ["CALL", null, ["callee:00bdddd0:8"]]
+ 00afaf64 ["INT_ADD", "register:40f0:8", ["const:afaf64:8", "const:4:8"]]
+ 00afaf64 ["CALL", null, ["callee:00bdddd0:8"]]
- 00afaf20 bytes 988b0394
+ 00afaf64 bytes 9b8b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d7f894153241467ce7a4ba7c7ca043"></a>

### [`00afaf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md) → [`00afaf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaf9c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) [`00bde290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde290.md) [`00bde960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md)
- 新版 呼出元 1件 [`00bde9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9b0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddd0.md) [`00bde2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2e0.md) [`00bde9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afaf74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md#insn-00afaf74) · [`00afaf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md#insn-00afaf80) · [`00afaf94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md#insn-00afaf94)
- 新版 `00afafb8`（命令位置の公開資料なし） · `00afafc4`（命令位置の公開資料なし） · `00afafd8`（命令位置の公開資料なし）

~~~diff
- 00afaf74 ["INT_ADD", "register:40f0:8", ["const:afaf74:8", "const:4:8"]]
- 00afaf74 ["CALL", null, ["callee:00bde9b0:8"]]
+ 00afafb8 ["INT_ADD", "register:40f0:8", ["const:afafb8:8", "const:4:8"]]
+ 00afafb8 ["CALL", null, ["callee:00bde9b0:8"]]
- 00afaf74 bytes 7b8e0394
+ 00afafb8 bytes 7e8e0394
- 00afaf80 ["INT_ADD", "register:40f0:8", ["const:afaf80:8", "const:4:8"]]
- 00afaf80 ["CALL", null, ["callee:00bde9b0:8"]]
+ 00afafc4 ["INT_ADD", "register:40f0:8", ["const:afafc4:8", "const:4:8"]]
+ 00afafc4 ["CALL", null, ["callee:00bde9b0:8"]]
- 00afaf80 bytes 788e0394
+ 00afafc4 bytes 7b8e0394
- 00afaf94 ["INT_ADD", "register:40f0:8", ["const:afaf94:8", "const:4:8"]]
- 00afaf94 ["CALL", null, ["callee:00bde2e0:8"]]
+ 00afafd8 ["INT_ADD", "register:40f0:8", ["const:afafd8:8", "const:4:8"]]
+ 00afafd8 ["CALL", null, ["callee:00bde2e0:8"]]
- 00afaf94 bytes bf8c0394
+ 00afafd8 bytes c28c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e579ff0f21c34b250c091c1f3e4926c8"></a>

### [`00afb024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb024.md) → [`00afb068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb068.md) _ZNK8firebase10LoggerBase8LogDebugEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb024.md#insn-00afb09c) · [`00afb0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb024.md#insn-00afb0c8) · [`00afb0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb024.md#insn-00afb0f0)
- 新版 `00afb0e0`（命令位置の公開資料なし） · `00afb10c`（命令位置の公開資料なし） · `00afb134`（命令位置の公開資料なし）

~~~diff
- 00afb09c ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb09c ["INT_ADD", "register:40f0:8", ["const:afb09c:8", "const:4:8"]]
- 00afb09c ["CALLIND", null, ["register:0:8"]]
+ 00afb0e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb0e0 ["INT_ADD", "register:40f0:8", ["const:afb0e0:8", "const:4:8"]]
+ 00afb0e0 ["CALLIND", null, ["register:0:8"]]
- 00afb09c bytes 00013fd6
+ 00afb0e0 bytes 00013fd6
- 00afb0c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb0c8 ["INT_ADD", "register:40f0:8", ["const:afb0c8:8", "const:4:8"]]
- 00afb0c8 ["CALLIND", null, ["register:0:8"]]
+ 00afb10c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb10c ["INT_ADD", "register:40f0:8", ["const:afb10c:8", "const:4:8"]]
+ 00afb10c ["CALLIND", null, ["register:0:8"]]
- 00afb0c8 bytes 00013fd6
+ 00afb10c bytes 00013fd6
- 00afb0f0 ["INT_ADD", "register:40f0:8", ["const:afb0f0:8", "const:4:8"]]
- 00afb0f0 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb134 ["INT_ADD", "register:40f0:8", ["const:afb134:8", "const:4:8"]]
+ 00afb134 ["CALL", null, ["callee:00bdb090:8"]]
- 00afb0f0 bytes d47f0394
+ 00afb134 bytes d77f0394
~~~


<a id="compare-f4ca403ab8ac22dd7f1cc0e5c76d46de"></a>

### [`00afb0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb0f4.md) → [`00afb138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb138.md) _ZNK8firebase10LoggerBase17FilterLogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb0f4.md#insn-00afb130) · [`00afb15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb0f4.md#insn-00afb15c) · [`00afb188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb0f4.md#insn-00afb188)
- 新版 `00afb174`（命令位置の公開資料なし） · `00afb1a0`（命令位置の公開資料なし） · `00afb1cc`（命令位置の公開資料なし）

~~~diff
- 00afb130 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb130 ["INT_ADD", "register:40f0:8", ["const:afb130:8", "const:4:8"]]
- 00afb130 ["CALLIND", null, ["register:0:8"]]
+ 00afb174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb174 ["INT_ADD", "register:40f0:8", ["const:afb174:8", "const:4:8"]]
+ 00afb174 ["CALLIND", null, ["register:0:8"]]
- 00afb130 bytes 00013fd6
+ 00afb174 bytes 00013fd6
- 00afb15c ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb15c ["INT_ADD", "register:40f0:8", ["const:afb15c:8", "const:4:8"]]
- 00afb15c ["CALLIND", null, ["register:0:8"]]
+ 00afb1a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb1a0 ["INT_ADD", "register:40f0:8", ["const:afb1a0:8", "const:4:8"]]
+ 00afb1a0 ["CALLIND", null, ["register:0:8"]]
- 00afb15c bytes 00013fd6
+ 00afb1a0 bytes 00013fd6
- 00afb188 ["INT_ADD", "register:40f0:8", ["const:afb188:8", "const:4:8"]]
- 00afb188 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb1cc ["INT_ADD", "register:40f0:8", ["const:afb1cc:8", "const:4:8"]]
+ 00afb1cc ["CALL", null, ["callee:00bdb090:8"]]
- 00afb188 bytes ae7f0394
+ 00afb1cc bytes b17f0394
~~~


<a id="compare-a891674ecc0cd59e62af96d872bdbea5"></a>

### [`00afb18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb18c.md) → [`00afb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb1d0.md) _ZNK8firebase10LoggerBase7LogInfoEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb18c.md#insn-00afb204) · [`00afb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb18c.md#insn-00afb230) · [`00afb258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb18c.md#insn-00afb258)
- 新版 `00afb248`（命令位置の公開資料なし） · `00afb274`（命令位置の公開資料なし） · `00afb29c`（命令位置の公開資料なし）

~~~diff
- 00afb204 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb204 ["INT_ADD", "register:40f0:8", ["const:afb204:8", "const:4:8"]]
- 00afb204 ["CALLIND", null, ["register:0:8"]]
+ 00afb248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb248 ["INT_ADD", "register:40f0:8", ["const:afb248:8", "const:4:8"]]
+ 00afb248 ["CALLIND", null, ["register:0:8"]]
- 00afb204 bytes 00013fd6
+ 00afb248 bytes 00013fd6
- 00afb230 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb230 ["INT_ADD", "register:40f0:8", ["const:afb230:8", "const:4:8"]]
- 00afb230 ["CALLIND", null, ["register:0:8"]]
+ 00afb274 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb274 ["INT_ADD", "register:40f0:8", ["const:afb274:8", "const:4:8"]]
+ 00afb274 ["CALLIND", null, ["register:0:8"]]
- 00afb230 bytes 00013fd6
+ 00afb274 bytes 00013fd6
- 00afb258 ["INT_ADD", "register:40f0:8", ["const:afb258:8", "const:4:8"]]
- 00afb258 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb29c ["INT_ADD", "register:40f0:8", ["const:afb29c:8", "const:4:8"]]
+ 00afb29c ["CALL", null, ["callee:00bdb090:8"]]
- 00afb258 bytes 7a7f0394
+ 00afb29c bytes 7d7f0394
~~~


<a id="compare-cd75c4fa7c7d7a651563b3add72fc768"></a>

### [`00afb25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb25c.md) → [`00afb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb2a0.md) _ZNK8firebase10LoggerBase10LogWarningEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb25c.md#insn-00afb2d4) · [`00afb300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb25c.md#insn-00afb300) · [`00afb328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb25c.md#insn-00afb328)
- 新版 `00afb318`（命令位置の公開資料なし） · `00afb344`（命令位置の公開資料なし） · `00afb36c`（命令位置の公開資料なし）

~~~diff
- 00afb2d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb2d4 ["INT_ADD", "register:40f0:8", ["const:afb2d4:8", "const:4:8"]]
- 00afb2d4 ["CALLIND", null, ["register:0:8"]]
+ 00afb318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb318 ["INT_ADD", "register:40f0:8", ["const:afb318:8", "const:4:8"]]
+ 00afb318 ["CALLIND", null, ["register:0:8"]]
- 00afb2d4 bytes 00013fd6
+ 00afb318 bytes 00013fd6
- 00afb300 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb300 ["INT_ADD", "register:40f0:8", ["const:afb300:8", "const:4:8"]]
- 00afb300 ["CALLIND", null, ["register:0:8"]]
+ 00afb344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb344 ["INT_ADD", "register:40f0:8", ["const:afb344:8", "const:4:8"]]
+ 00afb344 ["CALLIND", null, ["register:0:8"]]
- 00afb300 bytes 00013fd6
+ 00afb344 bytes 00013fd6
- 00afb328 ["INT_ADD", "register:40f0:8", ["const:afb328:8", "const:4:8"]]
- 00afb328 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb36c ["INT_ADD", "register:40f0:8", ["const:afb36c:8", "const:4:8"]]
+ 00afb36c ["CALL", null, ["callee:00bdb090:8"]]
- 00afb328 bytes 467f0394
+ 00afb36c bytes 497f0394
~~~


<a id="compare-efa2c827a407df374c34be79f5a104cd"></a>

### [`00afb32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb32c.md) → [`00afb370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb370.md) _ZNK8firebase10LoggerBase8LogErrorEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb32c.md#insn-00afb3a4) · [`00afb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb32c.md#insn-00afb3d0) · [`00afb3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb32c.md#insn-00afb3f8)
- 新版 `00afb3e8`（命令位置の公開資料なし） · `00afb414`（命令位置の公開資料なし） · `00afb43c`（命令位置の公開資料なし）

~~~diff
- 00afb3a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb3a4 ["INT_ADD", "register:40f0:8", ["const:afb3a4:8", "const:4:8"]]
- 00afb3a4 ["CALLIND", null, ["register:0:8"]]
+ 00afb3e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb3e8 ["INT_ADD", "register:40f0:8", ["const:afb3e8:8", "const:4:8"]]
+ 00afb3e8 ["CALLIND", null, ["register:0:8"]]
- 00afb3a4 bytes 00013fd6
+ 00afb3e8 bytes 00013fd6
- 00afb3d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb3d0 ["INT_ADD", "register:40f0:8", ["const:afb3d0:8", "const:4:8"]]
- 00afb3d0 ["CALLIND", null, ["register:0:8"]]
+ 00afb414 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb414 ["INT_ADD", "register:40f0:8", ["const:afb414:8", "const:4:8"]]
+ 00afb414 ["CALLIND", null, ["register:0:8"]]
- 00afb3d0 bytes 00013fd6
+ 00afb414 bytes 00013fd6
- 00afb3f8 ["INT_ADD", "register:40f0:8", ["const:afb3f8:8", "const:4:8"]]
- 00afb3f8 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb43c ["INT_ADD", "register:40f0:8", ["const:afb43c:8", "const:4:8"]]
+ 00afb43c ["CALL", null, ["callee:00bdb090:8"]]
- 00afb3f8 bytes 127f0394
+ 00afb43c bytes 157f0394
~~~


<a id="compare-317ea18519d360e2a28bdfb7a4342da0"></a>

### [`00afb3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb3fc.md) → [`00afb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb440.md) _ZNK8firebase10LoggerBase9LogAssertEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb3fc.md#insn-00afb474) · [`00afb4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb3fc.md#insn-00afb4a0) · [`00afb4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb3fc.md#insn-00afb4c8)
- 新版 `00afb4b8`（命令位置の公開資料なし） · `00afb4e4`（命令位置の公開資料なし） · `00afb50c`（命令位置の公開資料なし）

~~~diff
- 00afb474 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb474 ["INT_ADD", "register:40f0:8", ["const:afb474:8", "const:4:8"]]
- 00afb474 ["CALLIND", null, ["register:0:8"]]
+ 00afb4b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb4b8 ["INT_ADD", "register:40f0:8", ["const:afb4b8:8", "const:4:8"]]
+ 00afb4b8 ["CALLIND", null, ["register:0:8"]]
- 00afb474 bytes 00013fd6
+ 00afb4b8 bytes 00013fd6
- 00afb4a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb4a0 ["INT_ADD", "register:40f0:8", ["const:afb4a0:8", "const:4:8"]]
- 00afb4a0 ["CALLIND", null, ["register:0:8"]]
+ 00afb4e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb4e4 ["INT_ADD", "register:40f0:8", ["const:afb4e4:8", "const:4:8"]]
+ 00afb4e4 ["CALLIND", null, ["register:0:8"]]
- 00afb4a0 bytes 00013fd6
+ 00afb4e4 bytes 00013fd6
- 00afb4c8 ["INT_ADD", "register:40f0:8", ["const:afb4c8:8", "const:4:8"]]
- 00afb4c8 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb50c ["INT_ADD", "register:40f0:8", ["const:afb50c:8", "const:4:8"]]
+ 00afb50c ["CALL", null, ["callee:00bdb090:8"]]
- 00afb4c8 bytes de7e0394
+ 00afb50c bytes e17e0394
~~~


<a id="compare-003c32c00f5f91b744c917942d214452"></a>

### [`00afb4cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb4cc.md) → [`00afb510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb510.md) _ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb4cc.md#insn-00afb54c) · [`00afb578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb4cc.md#insn-00afb578) · [`00afb5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb4cc.md#insn-00afb5a4)
- 新版 `00afb590`（命令位置の公開資料なし） · `00afb5bc`（命令位置の公開資料なし） · `00afb5e8`（命令位置の公開資料なし）

~~~diff
- 00afb54c ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb54c ["INT_ADD", "register:40f0:8", ["const:afb54c:8", "const:4:8"]]
- 00afb54c ["CALLIND", null, ["register:0:8"]]
+ 00afb590 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb590 ["INT_ADD", "register:40f0:8", ["const:afb590:8", "const:4:8"]]
+ 00afb590 ["CALLIND", null, ["register:0:8"]]
- 00afb54c bytes 00013fd6
+ 00afb590 bytes 00013fd6
- 00afb578 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb578 ["INT_ADD", "register:40f0:8", ["const:afb578:8", "const:4:8"]]
- 00afb578 ["CALLIND", null, ["register:0:8"]]
+ 00afb5bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb5bc ["INT_ADD", "register:40f0:8", ["const:afb5bc:8", "const:4:8"]]
+ 00afb5bc ["CALLIND", null, ["register:0:8"]]
- 00afb578 bytes 00013fd6
+ 00afb5bc bytes 00013fd6
- 00afb5a4 ["INT_ADD", "register:40f0:8", ["const:afb5a4:8", "const:4:8"]]
- 00afb5a4 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb5e8 ["INT_ADD", "register:40f0:8", ["const:afb5e8:8", "const:4:8"]]
+ 00afb5e8 ["CALL", null, ["callee:00bdb090:8"]]
- 00afb5a4 bytes a77e0394
+ 00afb5e8 bytes aa7e0394
~~~


<a id="compare-f29ca06f9be7f6ca5e853fd75979c761"></a>

### [`00afb5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb5a8.md) → [`00afb5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb5ec.md) _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb5a8.md#insn-00afb5e4) · [`00afb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb5a8.md#insn-00afb610) · [`00afb638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb5a8.md#insn-00afb638)
- 新版 `00afb628`（命令位置の公開資料なし） · `00afb654`（命令位置の公開資料なし） · `00afb67c`（命令位置の公開資料なし）

~~~diff
- 00afb5e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb5e4 ["INT_ADD", "register:40f0:8", ["const:afb5e4:8", "const:4:8"]]
- 00afb5e4 ["CALLIND", null, ["register:0:8"]]
+ 00afb628 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb628 ["INT_ADD", "register:40f0:8", ["const:afb628:8", "const:4:8"]]
+ 00afb628 ["CALLIND", null, ["register:0:8"]]
- 00afb5e4 bytes 00013fd6
+ 00afb628 bytes 00013fd6
- 00afb610 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb610 ["INT_ADD", "register:40f0:8", ["const:afb610:8", "const:4:8"]]
- 00afb610 ["CALLIND", null, ["register:0:8"]]
+ 00afb654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb654 ["INT_ADD", "register:40f0:8", ["const:afb654:8", "const:4:8"]]
+ 00afb654 ["CALLIND", null, ["register:0:8"]]
- 00afb610 bytes 00013fd6
+ 00afb654 bytes 00013fd6
- 00afb638 ["INT_ADD", "register:40f0:8", ["const:afb638:8", "const:4:8"]]
- 00afb638 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb67c ["INT_ADD", "register:40f0:8", ["const:afb67c:8", "const:4:8"]]
+ 00afb67c ["CALL", null, ["callee:00bdb090:8"]]
- 00afb638 bytes 827e0394
+ 00afb67c bytes 857e0394
~~~


<a id="compare-c7e166049e6c403d43683e1dd03cceab"></a>

### [`00afb64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb64c.md) → [`00afb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb690.md) _ZNK8firebase12SystemLogger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb64c.md#insn-00afb680) · [`00afb6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb64c.md#insn-00afb6a4)
- 新版 `00afb6c4`（命令位置の公開資料なし） · `00afb6e8`（命令位置の公開資料なし）

~~~diff
- 00afb680 ["INT_ADD", "register:40f0:8", ["const:afb680:8", "const:4:8"]]
- 00afb680 ["CALL", null, ["callee:00bde2a0:8"]]
+ 00afb6c4 ["INT_ADD", "register:40f0:8", ["const:afb6c4:8", "const:4:8"]]
+ 00afb6c4 ["CALL", null, ["callee:00bde2a0:8"]]
- 00afb680 bytes f48a0394
+ 00afb6c4 bytes f78a0394
- 00afb6a4 ["INT_ADD", "register:40f0:8", ["const:afb6a4:8", "const:4:8"]]
- 00afb6a4 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb6e8 ["INT_ADD", "register:40f0:8", ["const:afb6e8:8", "const:4:8"]]
+ 00afb6e8 ["CALL", null, ["callee:00bdb090:8"]]
- 00afb6a4 bytes 677e0394
+ 00afb6e8 bytes 6a7e0394
~~~


<a id="compare-956737b9ad3b6db5f49b705aed2f12ca"></a>

### [`00afb6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb6bc.md) → [`00afb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb700.md) _ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb6bc.md#insn-00afb6fc) · [`00afb728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb6bc.md#insn-00afb728) · [`00afb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb6bc.md#insn-00afb750)
- 新版 `00afb740`（命令位置の公開資料なし） · `00afb76c`（命令位置の公開資料なし） · `00afb794`（命令位置の公開資料なし）

~~~diff
- 00afb6fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb6fc ["INT_ADD", "register:40f0:8", ["const:afb6fc:8", "const:4:8"]]
- 00afb6fc ["CALLIND", null, ["register:0:8"]]
+ 00afb740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb740 ["INT_ADD", "register:40f0:8", ["const:afb740:8", "const:4:8"]]
+ 00afb740 ["CALLIND", null, ["register:0:8"]]
- 00afb6fc bytes 00013fd6
+ 00afb740 bytes 00013fd6
- 00afb728 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb728 ["INT_ADD", "register:40f0:8", ["const:afb728:8", "const:4:8"]]
- 00afb728 ["CALLIND", null, ["register:0:8"]]
+ 00afb76c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb76c ["INT_ADD", "register:40f0:8", ["const:afb76c:8", "const:4:8"]]
+ 00afb76c ["CALLIND", null, ["register:0:8"]]
- 00afb728 bytes 00013fd6
+ 00afb76c bytes 00013fd6
- 00afb750 ["INT_ADD", "register:40f0:8", ["const:afb750:8", "const:4:8"]]
- 00afb750 ["CALL", null, ["callee:00bdb090:8"]]
+ 00afb794 ["INT_ADD", "register:40f0:8", ["const:afb794:8", "const:4:8"]]
+ 00afb794 ["CALL", null, ["callee:00bdb090:8"]]
- 00afb750 bytes 3c7e0394
+ 00afb794 bytes 3f7e0394
~~~


<a id="compare-ec32b09e59c5e09641e1fc1c6454d75a"></a>

### [`00afb83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb83c.md) → [`00afb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb880.md) _ZN8firebase8callback18CallbackDispatcher14FlushCallbacksEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdec10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec10.md) · 呼出先 4件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bdec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec60.md) · 呼出先 4件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afb85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb83c.md#insn-00afb85c) · [`00afb874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb83c.md#insn-00afb874) · [`00afb8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb83c.md#insn-00afb8b8)
- 新版 `00afb8a0`（命令位置の公開資料なし） · `00afb8b8`（命令位置の公開資料なし） · `00afb8fc`（命令位置の公開資料なし）

~~~diff
- 00afb85c ["INT_ADD", "register:40f0:8", ["const:afb85c:8", "const:4:8"]]
- 00afb85c ["CALL", null, ["callee:00bddc20:8"]]
+ 00afb8a0 ["INT_ADD", "register:40f0:8", ["const:afb8a0:8", "const:4:8"]]
+ 00afb8a0 ["CALL", null, ["callee:00bddc20:8"]]
- 00afb85c bytes dd880394
+ 00afb8a0 bytes e0880394
- 00afb874 ["INT_ADD", "register:40f0:8", ["const:afb874:8", "const:4:8"]]
- 00afb874 ["CALL", null, ["callee:00bdb060:8"]]
+ 00afb8b8 ["INT_ADD", "register:40f0:8", ["const:afb8b8:8", "const:4:8"]]
+ 00afb8b8 ["CALL", null, ["callee:00bdb060:8"]]
- 00afb874 bytes e77d0394
+ 00afb8b8 bytes ea7d0394
- 00afb8b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb8b8 ["INT_ADD", "register:40f0:8", ["const:afb8b8:8", "const:4:8"]]
- 00afb8b8 ["CALLIND", null, ["register:0:8"]]
+ 00afb8fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afb8fc ["INT_ADD", "register:40f0:8", ["const:afb8fc:8", "const:4:8"]]
+ 00afb8fc ["CALLIND", null, ["register:0:8"]]
- 00afb8b8 bytes 00013fd6
+ 00afb8fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2679667e750b9f38b9467f4c3d95a4fd"></a>

### [`00afbf34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbf34.md) → [`00afbf78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbf78.md) _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdec20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec20.md) · 呼出先 5件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdebf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebf0.md)
- 新版 呼出元 1件 [`00bdec70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec70.md) · 呼出先 5件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdec40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afbf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbf34.md#insn-00afbf58) · [`00afbfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbf34.md#insn-00afbfdc) · [`00afbfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbf34.md#insn-00afbfe4)
- 新版 `00afbf9c`（命令位置の公開資料なし） · `00afc020`（命令位置の公開資料なし） · `00afc028`（命令位置の公開資料なし）

~~~diff
- 00afbf58 ["INT_ADD", "register:40f0:8", ["const:afbf58:8", "const:4:8"]]
- 00afbf58 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afbf9c ["INT_ADD", "register:40f0:8", ["const:afbf9c:8", "const:4:8"]]
+ 00afbf9c ["CALL", null, ["callee:00bddc20:8"]]
- 00afbf58 bytes 1e870394
+ 00afbf9c bytes 21870394
- 00afbfdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00afbfdc ["INT_ADD", "register:40f0:8", ["const:afbfdc:8", "const:4:8"]]
- 00afbfdc ["CALLIND", null, ["register:0:8"]]
+ 00afc020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afc020 ["INT_ADD", "register:40f0:8", ["const:afc020:8", "const:4:8"]]
+ 00afc020 ["CALLIND", null, ["register:0:8"]]
- 00afbfdc bytes 00013fd6
+ 00afc020 bytes 00013fd6
- 00afbfe4 ["INT_ADD", "register:40f0:8", ["const:afbfe4:8", "const:4:8"]]
- 00afbfe4 ["CALL", null, ["callee:00bdb030:8"]]
+ 00afc028 ["INT_ADD", "register:40f0:8", ["const:afc028:8", "const:4:8"]]
+ 00afc028 ["CALL", null, ["callee:00bdb030:8"]]
- 00afbfe4 bytes ff7b0394
+ 00afc028 bytes 027c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23ecc0950178f38e199b26424e3fda59"></a>

### [`00afc304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc304.md) → [`00afc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc348.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEE16__on_zero_sharedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00afbabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbabc.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00afbb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbb00.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afc320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc304.md#insn-00afc320) · [`00afc350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc304.md#insn-00afc350)
- 新版 `00afc364`（命令位置の公開資料なし） · `00afc394`（命令位置の公開資料なし）

~~~diff
- 00afc320 ["INT_ADD", "register:40f0:8", ["const:afc320:8", "const:4:8"]]
- 00afc320 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc364 ["INT_ADD", "register:40f0:8", ["const:afc364:8", "const:4:8"]]
+ 00afc364 ["CALL", null, ["callee:00bddc20:8"]]
- 00afc320 bytes 2c860394
+ 00afc364 bytes 2f860394
- 00afc350 ["INT_ADD", "register:40f0:8", ["const:afc350:8", "const:4:8"]]
- 00afc350 ["CALL", null, ["callee:00bddc30:8"]]
+ 00afc394 ["INT_ADD", "register:40f0:8", ["const:afc394:8", "const:4:8"]]
+ 00afc394 ["CALL", null, ["callee:00bddc30:8"]]
- 00afc350 bytes 24860394
+ 00afc394 bytes 27860394
~~~


<a id="compare-8cb2526430876b91c7e08ccbebcd1e5a"></a>

### [`00afc428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc428.md) → [`00afc46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc46c.md) _ZN8firebase8callback13CallbackEntry7ExecuteEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdebf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebf0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bdec40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec40.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afc444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc428.md#insn-00afc444) · [`00afc45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc428.md#insn-00afc45c) · [`00afc46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc428.md#insn-00afc46c)
- 新版 `00afc488`（命令位置の公開資料なし） · `00afc4a0`（命令位置の公開資料なし） · `00afc4b0`（命令位置の公開資料なし）

~~~diff
- 00afc444 ["INT_ADD", "register:40f0:8", ["const:afc444:8", "const:4:8"]]
- 00afc444 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc488 ["INT_ADD", "register:40f0:8", ["const:afc488:8", "const:4:8"]]
+ 00afc488 ["CALL", null, ["callee:00bddc20:8"]]
- 00afc444 bytes e3850394
+ 00afc488 bytes e6850394
- 00afc45c ["INT_ADD", "register:40f0:8", ["const:afc45c:8", "const:4:8"]]
- 00afc45c ["CALL", null, ["callee:00bddc30:8"]]
+ 00afc4a0 ["INT_ADD", "register:40f0:8", ["const:afc4a0:8", "const:4:8"]]
+ 00afc4a0 ["CALL", null, ["callee:00bddc30:8"]]
- 00afc45c bytes e1850394
+ 00afc4a0 bytes e4850394
- 00afc46c ["COPY", "register:0:8", ["register:4040:8"]]
- 00afc46c ["INT_ADD", "register:40f0:8", ["const:afc46c:8", "const:4:8"]]
- 00afc46c ["CALLIND", null, ["register:0:8"]]
+ 00afc4b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afc4b0 ["INT_ADD", "register:40f0:8", ["const:afc4b0:8", "const:4:8"]]
+ 00afc4b0 ["CALLIND", null, ["register:0:8"]]
- 00afc46c bytes 00013fd6
+ 00afc4b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d761cc9cfeae0430fc8ab95b3900a9da"></a>

### [`00afc694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc694.md) → [`00afc6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc6d8.md) _ZN8firebase15CleanupNotifier10CleanupAllEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8c0.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 1件 [`00bde910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde910.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afc6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc694.md#insn-00afc6a8) · [`00afc6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc694.md#insn-00afc6cc) · [`00afc6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc694.md#insn-00afc6d8)
- 新版 `00afc6ec`（命令位置の公開資料なし） · `00afc710`（命令位置の公開資料なし） · `00afc71c`（命令位置の公開資料なし）

~~~diff
- 00afc6a8 ["INT_ADD", "register:40f0:8", ["const:afc6a8:8", "const:4:8"]]
- 00afc6a8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc6ec ["INT_ADD", "register:40f0:8", ["const:afc6ec:8", "const:4:8"]]
+ 00afc6ec ["CALL", null, ["callee:00bddc20:8"]]
- 00afc6a8 bytes 4a850394
+ 00afc6ec bytes 4d850394
- 00afc6cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00afc6cc ["INT_ADD", "register:40f0:8", ["const:afc6cc:8", "const:4:8"]]
- 00afc6cc ["CALLIND", null, ["register:0:8"]]
+ 00afc710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afc710 ["INT_ADD", "register:40f0:8", ["const:afc710:8", "const:4:8"]]
+ 00afc710 ["CALLIND", null, ["register:0:8"]]
- 00afc6cc bytes 00013fd6
+ 00afc710 bytes 00013fd6
- 00afc6d8 ["INT_ADD", "register:40f0:8", ["const:afc6d8:8", "const:4:8"]]
- 00afc6d8 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00afc71c ["INT_ADD", "register:40f0:8", ["const:afc71c:8", "const:4:8"]]
+ 00afc71c ["CALL", null, ["callee:00bdddb0:8"]]
- 00afc6d8 bytes a2850394
+ 00afc71c bytes a5850394
~~~


<a id="compare-402c828442f12080535beb5eb39e5a60"></a>

### [`00afc7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md) → [`00afc80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc80c.md) _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)
- 新版 呼出元 1件 [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afc7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md#insn-00afc7e8) · [`00afc89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md#insn-00afc89c) · [`00afc8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md#insn-00afc8d0)
- 新版 `00afc82c`（命令位置の公開資料なし） · `00afc8e0`（命令位置の公開資料なし） · `00afc914`（命令位置の公開資料なし）

~~~diff
- 00afc7e8 ["INT_ADD", "register:40f0:8", ["const:afc7e8:8", "const:4:8"]]
- 00afc7e8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc82c ["INT_ADD", "register:40f0:8", ["const:afc82c:8", "const:4:8"]]
+ 00afc82c ["CALL", null, ["callee:00bddc20:8"]]
- 00afc7e8 bytes fa840394
+ 00afc82c bytes fd840394
- 00afc89c ["INT_ADD", "register:40f0:8", ["const:afc89c:8", "const:4:8"]]
- 00afc89c ["CALL", null, ["callee:00bdb040:8"]]
+ 00afc8e0 ["INT_ADD", "register:40f0:8", ["const:afc8e0:8", "const:4:8"]]
+ 00afc8e0 ["CALL", null, ["callee:00bdb040:8"]]
- 00afc89c bytes d5790394
+ 00afc8e0 bytes d8790394
- 00afc8d0 ["INT_ADD", "register:40f0:8", ["const:afc8d0:8", "const:4:8"]]
- 00afc8d0 ["CALL", null, ["callee:00bde760:8"]]
+ 00afc914 ["INT_ADD", "register:40f0:8", ["const:afc914:8", "const:4:8"]]
+ 00afc914 ["CALL", null, ["callee:00bde760:8"]]
- 00afc8d0 bytes 90870394
+ 00afc914 bytes 93870394
~~~


<a id="compare-9019bedd892439415bbc5476a40bc1a2"></a>

### [`00afc8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc8f8.md) → [`00afc93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc93c.md) _ZN8firebase15CleanupNotifier16UnregisterObjectEPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)
- 新版 呼出元 1件 [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afc910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc8f8.md#insn-00afc910) · [`00afc9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc8f8.md#insn-00afc9b8) · [`00afc9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc8f8.md#insn-00afc9c0)
- 新版 `00afc954`（命令位置の公開資料なし） · `00afc9fc`（命令位置の公開資料なし） · `00afca04`（命令位置の公開資料なし）

~~~diff
- 00afc910 ["INT_ADD", "register:40f0:8", ["const:afc910:8", "const:4:8"]]
- 00afc910 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc954 ["INT_ADD", "register:40f0:8", ["const:afc954:8", "const:4:8"]]
+ 00afc954 ["CALL", null, ["callee:00bddc20:8"]]
- 00afc910 bytes b0840394
+ 00afc954 bytes b3840394
- 00afc9b8 ["INT_ADD", "register:40f0:8", ["const:afc9b8:8", "const:4:8"]]
- 00afc9b8 ["CALL", null, ["callee:00bde750:8"]]
+ 00afc9fc ["INT_ADD", "register:40f0:8", ["const:afc9fc:8", "const:4:8"]]
+ 00afc9fc ["CALL", null, ["callee:00bde750:8"]]
- 00afc9b8 bytes 52870394
+ 00afc9fc bytes 55870394
- 00afc9c0 ["INT_ADD", "register:40f0:8", ["const:afc9c0:8", "const:4:8"]]
- 00afc9c0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00afca04 ["INT_ADD", "register:40f0:8", ["const:afca04:8", "const:4:8"]]
+ 00afca04 ["CALL", null, ["callee:00bdb060:8"]]
- 00afc9c0 bytes 94790394
+ 00afca04 bytes 97790394
~~~


<a id="compare-344ebb075f63dc8baa234dd11cc02424"></a>

### [`00afce00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce00.md) → [`00afce44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce44.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPFvS2_EEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tre

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdecb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecb0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdecb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecb0.md)
- 新版 呼出元 1件 [`00bded00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded00.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bded00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afce1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce00.md#insn-00afce1c) · [`00afce28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce00.md#insn-00afce28)
- 新版 `00afce60`（命令位置の公開資料なし） · `00afce6c`（命令位置の公開資料なし）

~~~diff
- 00afce1c ["INT_ADD", "register:40f0:8", ["const:afce1c:8", "const:4:8"]]
- 00afce1c ["CALL", null, ["callee:00bded00:8"]]
+ 00afce60 ["INT_ADD", "register:40f0:8", ["const:afce60:8", "const:4:8"]]
+ 00afce60 ["CALL", null, ["callee:00bded00:8"]]
- 00afce1c bytes a5870394
+ 00afce60 bytes a8870394
- 00afce28 ["INT_ADD", "register:40f0:8", ["const:afce28:8", "const:4:8"]]
- 00afce28 ["CALL", null, ["callee:00bded00:8"]]
+ 00afce6c ["INT_ADD", "register:40f0:8", ["const:afce6c:8", "const:4:8"]]
+ 00afce6c ["CALL", null, ["callee:00bded00:8"]]
- 00afce28 bytes a2870394
+ 00afce6c bytes a5870394
~~~


<a id="compare-952747adb75aa9e4d3bb8f3fa9aa724d"></a>

### [`00afce40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce40.md) → [`00afce84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce84.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdecc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecc0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdecc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecc0.md)
- 新版 呼出元 1件 [`00bded10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded10.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bded10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afce5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce40.md#insn-00afce5c) · [`00afce68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce40.md#insn-00afce68)
- 新版 `00afcea0`（命令位置の公開資料なし） · `00afceac`（命令位置の公開資料なし）

~~~diff
- 00afce5c ["INT_ADD", "register:40f0:8", ["const:afce5c:8", "const:4:8"]]
- 00afce5c ["CALL", null, ["callee:00bded10:8"]]
+ 00afcea0 ["INT_ADD", "register:40f0:8", ["const:afcea0:8", "const:4:8"]]
+ 00afcea0 ["CALL", null, ["callee:00bded10:8"]]
- 00afce5c bytes 99870394
+ 00afcea0 bytes 9c870394
- 00afce68 ["INT_ADD", "register:40f0:8", ["const:afce68:8", "const:4:8"]]
- 00afce68 ["CALL", null, ["callee:00bded10:8"]]
+ 00afceac ["INT_ADD", "register:40f0:8", ["const:afceac:8", "const:4:8"]]
+ 00afceac ["CALL", null, ["callee:00bded10:8"]]
- 00afce68 bytes 96870394
+ 00afceac bytes 99870394
~~~


<a id="compare-5a483935a9d03232310a656bf5962a2c"></a>

### [`00afceb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afceb8.md) → [`00afcefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcefc.md) _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afcec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afceb8.md#insn-00afcec8)
- 新版 `00afcf0c`（命令位置の公開資料なし）

~~~diff
- 00afcec8 ["INT_ADD", "register:40f0:8", ["const:afcec8:8", "const:4:8"]]
- 00afcec8 ["CALL", null, ["callee:00bded30:8"]]
+ 00afcf0c ["INT_ADD", "register:40f0:8", ["const:afcf0c:8", "const:4:8"]]
+ 00afcf0c ["CALL", null, ["callee:00bded30:8"]]
- 00afcec8 bytes 86870394
+ 00afcf0c bytes 89870394
~~~


<a id="compare-aada169c607ff9ca3d2f22292f486fdb"></a>

### [`00afd0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md) → [`00afd108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md) _ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md#insn-00afd120) · [`00afd13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md#insn-00afd13c) · [`00afd168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md#insn-00afd168)
- 新版 `00afd164`（命令位置の公開資料なし） · `00afd180`（命令位置の公開資料なし） · `00afd1ac`（命令位置の公開資料なし）

~~~diff
- 00afd120 ["INT_ADD", "register:40f0:8", ["const:afd120:8", "const:4:8"]]
- 00afd120 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afd164 ["INT_ADD", "register:40f0:8", ["const:afd164:8", "const:4:8"]]
+ 00afd164 ["CALL", null, ["callee:00bdb040:8"]]
- 00afd120 bytes b4770394
+ 00afd164 bytes b7770394
- 00afd13c ["INT_ADD", "register:40f0:8", ["const:afd13c:8", "const:4:8"]]
- 00afd13c ["CALL", null, ["callee:00bde730:8"]]
+ 00afd180 ["INT_ADD", "register:40f0:8", ["const:afd180:8", "const:4:8"]]
+ 00afd180 ["CALL", null, ["callee:00bde730:8"]]
- 00afd13c bytes 69850394
+ 00afd180 bytes 6c850394
- 00afd168 ["INT_ADD", "register:40f0:8", ["const:afd168:8", "const:4:8"]]
- 00afd168 ["CALL", null, ["callee:00afd2ac:8"]]
+ 00afd1ac ["INT_ADD", "register:40f0:8", ["const:afd1ac:8", "const:4:8"]]
+ 00afd1ac ["CALL", null, ["callee:00afd2ac:8"]]
- 00afd168 bytes 40000094
+ 00afd1ac bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2fdf9adc6dde1a19bc5f4fb773a6b42"></a>

### [`00afd1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd1f8.md) → [`00afd23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd23c.md) _ZN8firebase4PathC2ENSt6__ndk111__wrap_iterIPNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEESA_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd1f8.md#insn-00afd224) · [`00afd230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd1f8.md#insn-00afd230) · [`00afd240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd1f8.md#insn-00afd240)
- 新版 `00afd268`（命令位置の公開資料なし） · `00afd274`（命令位置の公開資料なし） · `00afd284`（命令位置の公開資料なし）

~~~diff
- 00afd224 ["INT_ADD", "register:40f0:8", ["const:afd224:8", "const:4:8"]]
- 00afd224 ["CALL", null, ["callee:00afd2ac:8"]]
+ 00afd268 ["INT_ADD", "register:40f0:8", ["const:afd268:8", "const:4:8"]]
+ 00afd268 ["CALL", null, ["callee:00afd2ac:8"]]
- 00afd224 bytes 11000094
+ 00afd268 bytes 11000094
- 00afd230 ["INT_ADD", "register:40f0:8", ["const:afd230:8", "const:4:8"]]
- 00afd230 ["CALL", null, ["callee:00bded30:8"]]
+ 00afd274 ["INT_ADD", "register:40f0:8", ["const:afd274:8", "const:4:8"]]
+ 00afd274 ["CALL", null, ["callee:00bded30:8"]]
- 00afd230 bytes ac860394
+ 00afd274 bytes af860394
- 00afd240 ["INT_ADD", "register:40f0:8", ["const:afd240:8", "const:4:8"]]
- 00afd240 ["CALL", null, ["callee:00bdb060:8"]]
+ 00afd284 ["INT_ADD", "register:40f0:8", ["const:afd284:8", "const:4:8"]]
+ 00afd284 ["CALL", null, ["callee:00bdb060:8"]]
- 00afd240 bytes 74770394
+ 00afd284 bytes 77770394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15abefb222e010d0b2ef88a3ff87a484"></a>

### [`00afd5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md) → [`00afd614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd614.md) _ZNK8firebase4Path9GetParentEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md#insn-00afd644) · [`00afd678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md#insn-00afd678) · [`00afd688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md#insn-00afd688)
- 新版 `00afd688`（命令位置の公開資料なし） · `00afd6bc`（命令位置の公開資料なし） · `00afd6cc`（命令位置の公開資料なし）

~~~diff
- 00afd644 ["INT_ADD", "register:40f0:8", ["const:afd644:8", "const:4:8"]]
- 00afd644 ["CALL", null, ["callee:00bde970:8"]]
+ 00afd688 ["INT_ADD", "register:40f0:8", ["const:afd688:8", "const:4:8"]]
+ 00afd688 ["CALL", null, ["callee:00bde970:8"]]
- 00afd644 bytes b7840394
+ 00afd688 bytes ba840394
- 00afd678 ["INT_ADD", "register:40f0:8", ["const:afd678:8", "const:4:8"]]
- 00afd678 ["CALL", null, ["callee:00bde230:8"]]
+ 00afd6bc ["INT_ADD", "register:40f0:8", ["const:afd6bc:8", "const:4:8"]]
+ 00afd6bc ["CALL", null, ["callee:00bde230:8"]]
- 00afd678 bytes da820394
+ 00afd6bc bytes dd820394
- 00afd688 ["INT_ADD", "register:40f0:8", ["const:afd688:8", "const:4:8"]]
- 00afd688 ["CALL", null, ["callee:00bdb060:8"]]
+ 00afd6cc ["INT_ADD", "register:40f0:8", ["const:afd6cc:8", "const:4:8"]]
+ 00afd6cc ["CALL", null, ["callee:00bdb060:8"]]
- 00afd688 bytes 62760394
+ 00afd6cc bytes 65760394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59fea734397eddf8c87194995b3b00d4"></a>

### [`00afd6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd6c0.md) → [`00afd704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd704.md) _ZN8firebase4Path8MakePathERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd6c0.md#insn-00afd6f4)
- 新版 `00afd738`（命令位置の公開資料なし）

~~~diff
- 00afd6f4 ["INT_ADD", "register:40f0:8", ["const:afd6f4:8", "const:4:8"]]
- 00afd6f4 ["CALL", null, ["callee:00bde230:8"]]
+ 00afd738 ["INT_ADD", "register:40f0:8", ["const:afd738:8", "const:4:8"]]
+ 00afd738 ["CALL", null, ["callee:00bde230:8"]]
- 00afd6f4 bytes bb820394
+ 00afd738 bytes be820394
~~~


<a id="compare-f54e482cf6c8b578e9e329d60ce43163"></a>

### [`00afdb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdb2c.md) → [`00afdb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdb70.md) _ZNK8firebase4Path14FrontDirectoryEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md) [`00bdecf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecf0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md) [`00bded40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdb2c.md#insn-00afdb64) · [`00afdb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdb2c.md#insn-00afdb70) · [`00afdbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdb2c.md#insn-00afdbac)
- 新版 `00afdba8`（命令位置の公開資料なし） · `00afdbb4`（命令位置の公開資料なし） · `00afdbf0`（命令位置の公開資料なし）

~~~diff
- 00afdb64 ["INT_ADD", "register:40f0:8", ["const:afdb64:8", "const:4:8"]]
- 00afdb64 ["CALL", null, ["callee:00bded40:8"]]
+ 00afdba8 ["INT_ADD", "register:40f0:8", ["const:afdba8:8", "const:4:8"]]
+ 00afdba8 ["CALL", null, ["callee:00bded40:8"]]
- 00afdb64 bytes 63840394
+ 00afdba8 bytes 66840394
- 00afdb70 ["INT_ADD", "register:40f0:8", ["const:afdb70:8", "const:4:8"]]
- 00afdb70 ["CALL", null, ["callee:00bded30:8"]]
+ 00afdbb4 ["INT_ADD", "register:40f0:8", ["const:afdbb4:8", "const:4:8"]]
+ 00afdbb4 ["CALL", null, ["callee:00bded30:8"]]
- 00afdb70 bytes 5c840394
+ 00afdbb4 bytes 5f840394
- 00afdbac ["INT_ADD", "register:40f0:8", ["const:afdbac:8", "const:4:8"]]
- 00afdbac ["CALL", null, ["callee:00bdb060:8"]]
+ 00afdbf0 ["INT_ADD", "register:40f0:8", ["const:afdbf0:8", "const:4:8"]]
+ 00afdbf0 ["CALL", null, ["callee:00bdb060:8"]]
- 00afdbac bytes 19750394
+ 00afdbf0 bytes 1c750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f628855e00b89563fd4cefe7c4224288"></a>

### [`00afdc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md) → [`00afdc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md) _ZNK8firebase4Path17PopFrontDirectoryEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md) [`00bdecf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecf0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md) [`00bded40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md#insn-00afdc3c) · [`00afdc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md#insn-00afdc4c) · [`00afdc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md#insn-00afdc58)
- 新版 `00afdc80`（命令位置の公開資料なし） · `00afdc90`（命令位置の公開資料なし） · `00afdc9c`（命令位置の公開資料なし）

~~~diff
- 00afdc3c ["INT_ADD", "register:40f0:8", ["const:afdc3c:8", "const:4:8"]]
- 00afdc3c ["CALL", null, ["callee:00bded40:8"]]
+ 00afdc80 ["INT_ADD", "register:40f0:8", ["const:afdc80:8", "const:4:8"]]
+ 00afdc80 ["CALL", null, ["callee:00bded40:8"]]
- 00afdc3c bytes 2d840394
+ 00afdc80 bytes 30840394
- 00afdc4c ["INT_ADD", "register:40f0:8", ["const:afdc4c:8", "const:4:8"]]
- 00afdc4c ["CALL", null, ["callee:00afd2ac:8"]]
+ 00afdc90 ["INT_ADD", "register:40f0:8", ["const:afdc90:8", "const:4:8"]]
+ 00afdc90 ["CALL", null, ["callee:00afd2ac:8"]]
- 00afdc4c bytes 87fdff97
+ 00afdc90 bytes 87fdff97
- 00afdc58 ["INT_ADD", "register:40f0:8", ["const:afdc58:8", "const:4:8"]]
- 00afdc58 ["CALL", null, ["callee:00bded30:8"]]
+ 00afdc9c ["INT_ADD", "register:40f0:8", ["const:afdc9c:8", "const:4:8"]]
+ 00afdc9c ["CALL", null, ["callee:00bded30:8"]]
- 00afdc58 bytes 22840394
+ 00afdc9c bytes 25840394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-644f3793db22b6ce1c95ee2c317c7655"></a>

### [`00afdcfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdcfc.md) → [`00afdd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdd40.md) _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bdecd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bded20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdcfc.md#insn-00afdd28) · [`00afdd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdcfc.md#insn-00afdd60) · [`00afdd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdcfc.md#insn-00afdd78)
- 新版 `00afdd6c`（命令位置の公開資料なし） · `00afdda4`（命令位置の公開資料なし） · `00afddbc`（命令位置の公開資料なし）

~~~diff
- 00afdd28 ["INT_ADD", "register:40f0:8", ["const:afdd28:8", "const:4:8"]]
- 00afdd28 ["CALL", null, ["callee:00bded20:8"]]
+ 00afdd6c ["INT_ADD", "register:40f0:8", ["const:afdd6c:8", "const:4:8"]]
+ 00afdd6c ["CALL", null, ["callee:00bded20:8"]]
- 00afdd28 bytes ea830394
+ 00afdd6c bytes ed830394
- 00afdd60 ["INT_ADD", "register:40f0:8", ["const:afdd60:8", "const:4:8"]]
- 00afdd60 ["CALL", null, ["callee:00bde230:8"]]
+ 00afdda4 ["INT_ADD", "register:40f0:8", ["const:afdda4:8", "const:4:8"]]
+ 00afdda4 ["CALL", null, ["callee:00bde230:8"]]
- 00afdd60 bytes 20810394
+ 00afdda4 bytes 23810394
- 00afdd78 ["INT_ADD", "register:40f0:8", ["const:afdd78:8", "const:4:8"]]
- 00afdd78 ["CALL", null, ["callee:00bdb060:8"]]
+ 00afddbc ["INT_ADD", "register:40f0:8", ["const:afddbc:8", "const:4:8"]]
+ 00afddbc ["CALL", null, ["callee:00bdb060:8"]]
- 00afdd78 bytes a6740394
+ 00afddbc bytes a9740394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-481345d1ee4aeec1907f4c3b8703ffed"></a>

### [`00afddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md) → [`00afddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md) _ZN8firebase4Path11GetRelativeERKS0_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdecd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecd0.md) · 呼出先 6件 [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 1件 [`00bded20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded20.md) · 呼出先 6件 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md#insn-00afdde8) · [`00afddf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md#insn-00afddf4) · [`00afdeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md#insn-00afdeb0)
- 新版 `00afde2c`（命令位置の公開資料なし） · `00afde38`（命令位置の公開資料なし） · `00afdef4`（命令位置の公開資料なし）

~~~diff
- 00afdde8 ["INT_ADD", "register:40f0:8", ["const:afdde8:8", "const:4:8"]]
- 00afdde8 ["CALL", null, ["callee:00bded40:8"]]
+ 00afde2c ["INT_ADD", "register:40f0:8", ["const:afde2c:8", "const:4:8"]]
+ 00afde2c ["CALL", null, ["callee:00bded40:8"]]
- 00afdde8 bytes c2830394
+ 00afde2c bytes c5830394
- 00afddf4 ["INT_ADD", "register:40f0:8", ["const:afddf4:8", "const:4:8"]]
- 00afddf4 ["CALL", null, ["callee:00bded40:8"]]
+ 00afde38 ["INT_ADD", "register:40f0:8", ["const:afde38:8", "const:4:8"]]
+ 00afde38 ["CALL", null, ["callee:00bded40:8"]]
- 00afddf4 bytes bf830394
+ 00afde38 bytes c2830394
- 00afdeb0 ["INT_ADD", "register:40f0:8", ["const:afdeb0:8", "const:4:8"]]
- 00afdeb0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00afdef4 ["INT_ADD", "register:40f0:8", ["const:afdef4:8", "const:4:8"]]
+ 00afdef4 ["CALL", null, ["callee:00bdb200:8"]]
- 00afdeb0 bytes c0740394
+ 00afdef4 bytes c3740394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0d5953a5092f4b89701fd4ed9849c9"></a>

### [`00afe018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md) → [`00afe05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe05c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iterator

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bded00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded00.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)
- 新版 呼出元 1件 [`00bded50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded50.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md#insn-00afe128) · [`00afe154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md#insn-00afe154) · [`00afe1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md#insn-00afe1a4)
- 新版 `00afe16c`（命令位置の公開資料なし） · `00afe198`（命令位置の公開資料なし） · `00afe1e8`（命令位置の公開資料なし）

~~~diff
- 00afe128 ["INT_ADD", "register:40f0:8", ["const:afe128:8", "const:4:8"]]
- 00afe128 ["CALL", null, ["callee:00bdda90:8"]]
+ 00afe16c ["INT_ADD", "register:40f0:8", ["const:afe16c:8", "const:4:8"]]
+ 00afe16c ["CALL", null, ["callee:00bdda90:8"]]
- 00afe128 bytes 467e0394
+ 00afe16c bytes 497e0394
- 00afe154 ["INT_ADD", "register:40f0:8", ["const:afe154:8", "const:4:8"]]
- 00afe154 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afe198 ["INT_ADD", "register:40f0:8", ["const:afe198:8", "const:4:8"]]
+ 00afe198 ["CALL", null, ["callee:00bdb040:8"]]
- 00afe154 bytes a7730394
+ 00afe198 bytes aa730394
- 00afe1a4 ["INT_ADD", "register:40f0:8", ["const:afe1a4:8", "const:4:8"]]
- 00afe1a4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00afe1e8 ["INT_ADD", "register:40f0:8", ["const:afe1e8:8", "const:4:8"]]
+ 00afe1e8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00afe1a4 bytes bf730394
+ 00afe1e8 bytes c2730394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74af3f941f40d9cf9857990ab91c08ff"></a>

### [`00afe338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md) → [`00afe37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe37c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md#insn-00afe3d4) · [`00afe41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md#insn-00afe41c) · [`00afe440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md#insn-00afe440)
- 新版 `00afe418`（命令位置の公開資料なし） · `00afe460`（命令位置の公開資料なし） · `00afe484`（命令位置の公開資料なし）

~~~diff
- 00afe3d4 ["INT_ADD", "register:40f0:8", ["const:afe3d4:8", "const:4:8"]]
- 00afe3d4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afe418 ["INT_ADD", "register:40f0:8", ["const:afe418:8", "const:4:8"]]
+ 00afe418 ["CALL", null, ["callee:00bdb040:8"]]
- 00afe3d4 bytes 07730394
+ 00afe418 bytes 0a730394
- 00afe41c ["INT_ADD", "register:40f0:8", ["const:afe41c:8", "const:4:8"]]
- 00afe41c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00afe460 ["INT_ADD", "register:40f0:8", ["const:afe460:8", "const:4:8"]]
+ 00afe460 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00afe41c bytes 51730394
+ 00afe460 bytes 54730394
- 00afe440 ["INT_ADD", "register:40f0:8", ["const:afe440:8", "const:4:8"]]
- 00afe440 ["CALL", null, ["callee:00bdb060:8"]]
+ 00afe484 ["INT_ADD", "register:40f0:8", ["const:afe484:8", "const:4:8"]]
+ 00afe484 ["CALL", null, ["callee:00bdb060:8"]]
- 00afe440 bytes f4720394
+ 00afe484 bytes f7720394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-688e2a731d64a99ff04694460b86d1f4"></a>

### [`00afe46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md) → [`00afe4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe4b0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertIPKcEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__li

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bded10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded10.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)
- 新版 呼出元 1件 [`00bded60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded60.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md#insn-00afe57c) · [`00afe5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md#insn-00afe5a8) · [`00afe638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md#insn-00afe638)
- 新版 `00afe5c0`（命令位置の公開資料なし） · `00afe5ec`（命令位置の公開資料なし） · `00afe67c`（命令位置の公開資料なし）

~~~diff
- 00afe57c ["INT_ADD", "register:40f0:8", ["const:afe57c:8", "const:4:8"]]
- 00afe57c ["CALL", null, ["callee:00bdda90:8"]]
+ 00afe5c0 ["INT_ADD", "register:40f0:8", ["const:afe5c0:8", "const:4:8"]]
+ 00afe5c0 ["CALL", null, ["callee:00bdda90:8"]]
- 00afe57c bytes 317d0394
+ 00afe5c0 bytes 347d0394
- 00afe5a8 ["INT_ADD", "register:40f0:8", ["const:afe5a8:8", "const:4:8"]]
- 00afe5a8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afe5ec ["INT_ADD", "register:40f0:8", ["const:afe5ec:8", "const:4:8"]]
+ 00afe5ec ["CALL", null, ["callee:00bdb040:8"]]
- 00afe5a8 bytes 92720394
+ 00afe5ec bytes 95720394
- 00afe638 ["INT_ADD", "register:40f0:8", ["const:afe638:8", "const:4:8"]]
- 00afe638 ["CALL", null, ["callee:00bded60:8"]]
+ 00afe67c ["INT_ADD", "register:40f0:8", ["const:afe67c:8", "const:4:8"]]
+ 00afe67c ["CALL", null, ["callee:00bded60:8"]]
- 00afe638 bytes b6810394
+ 00afe67c bytes b9810394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a980ffe8ab9ddde08c60e9a581c53c0b"></a>

### [`00afe9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md) → [`00afea28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afea28.md) _ZN8firebase17FutureBackingData22ClearExistingCallbacksEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bded70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded70.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdedc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdedc0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afea10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md#insn-00afea10) · [`00afea2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md#insn-00afea2c) · [`00afea88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md#insn-00afea88)
- 新版 `00afea54`（命令位置の公開資料なし） · `00afea70`（命令位置の公開資料なし） · `00afeacc`（命令位置の公開資料なし）

~~~diff
- 00afea10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afea10 ["INT_ADD", "register:40f0:8", ["const:afea10:8", "const:4:8"]]
- 00afea10 ["CALLIND", null, ["register:0:8"]]
+ 00afea54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afea54 ["INT_ADD", "register:40f0:8", ["const:afea54:8", "const:4:8"]]
+ 00afea54 ["CALLIND", null, ["register:0:8"]]
- 00afea10 bytes 00013fd6
+ 00afea54 bytes 00013fd6
- 00afea2c ["INT_ADD", "register:40f0:8", ["const:afea2c:8", "const:4:8"]]
- 00afea2c ["CALL", null, ["callee:00bdb060:8"]]
+ 00afea70 ["INT_ADD", "register:40f0:8", ["const:afea70:8", "const:4:8"]]
+ 00afea70 ["CALL", null, ["callee:00bdb060:8"]]
- 00afea2c bytes 79710394
+ 00afea70 bytes 7c710394
- 00afea88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afea88 ["INT_ADD", "register:40f0:8", ["const:afea88:8", "const:4:8"]]
- 00afea88 ["CALLIND", null, ["register:0:8"]]
+ 00afeacc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afeacc ["INT_ADD", "register:40f0:8", ["const:afeacc:8", "const:4:8"]]
+ 00afeacc ["CALLIND", null, ["register:0:8"]]
- 00afea88 bytes 00013fd6
+ 00afeacc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa2bdc18d2e40c20a96a4f9cb323a6ea"></a>

### [`00afecd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afecd8.md) → [`00afed1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afed1c.md) _ZN8firebase26ReferenceCountedFutureImplD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdedd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdee20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afece8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afecd8.md#insn-00afece8)
- 新版 `00afed2c`（命令位置の公開資料なし）

~~~diff
- 00afece8 ["INT_ADD", "register:40f0:8", ["const:afece8:8", "const:4:8"]]
- 00afece8 ["CALL", null, ["callee:00bdee20:8"]]
+ 00afed2c ["INT_ADD", "register:40f0:8", ["const:afed2c:8", "const:4:8"]]
+ 00afed2c ["CALL", null, ["callee:00bdee20:8"]]
- 00afece8 bytes 3a800394
+ 00afed2c bytes 3d800394
~~~


<a id="compare-4e76bba76d884ec508aae094b633755d"></a>

### [`00aff3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff3ac.md) → [`00aff3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff3f0.md) _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfb0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bde000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde000.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aff3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff3ac.md#insn-00aff3cc) · [`00aff418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff3ac.md#insn-00aff418)
- 新版 `00aff410`（命令位置の公開資料なし） · `00aff45c`（命令位置の公開資料なし）

~~~diff
- 00aff3cc ["INT_ADD", "register:40f0:8", ["const:aff3cc:8", "const:4:8"]]
- 00aff3cc ["CALL", null, ["callee:00bddc20:8"]]
+ 00aff410 ["INT_ADD", "register:40f0:8", ["const:aff410:8", "const:4:8"]]
+ 00aff410 ["CALL", null, ["callee:00bddc20:8"]]
- 00aff3cc bytes 017a0394
+ 00aff410 bytes 047a0394
- 00aff418 ["INT_ADD", "register:40f0:8", ["const:aff418:8", "const:4:8"]]
- 00aff418 ["CALL", null, ["callee:00bddc30:8"]]
+ 00aff45c ["INT_ADD", "register:40f0:8", ["const:aff45c:8", "const:4:8"]]
+ 00aff45c ["CALL", null, ["callee:00bddc30:8"]]
- 00aff418 bytes f2790394
+ 00aff45c bytes f5790394
~~~


<a id="compare-9899681f8cdf8aa8e713c47a150505a9"></a>

### [`00aff764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff764.md) → [`00aff7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff7a8.md) _ZN8firebase26ReferenceCountedFutureImpl11RunCallbackEPNS_10FutureBaseEPFvRKS1_PvES5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aff798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff764.md#insn-00aff798) · [`00aff7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff764.md#insn-00aff7a4) · [`00aff7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff764.md#insn-00aff7ac)
- 新版 `00aff7dc`（命令位置の公開資料なし） · `00aff7e8`（命令位置の公開資料なし） · `00aff7f0`（命令位置の公開資料なし）

~~~diff
- 00aff798 ["INT_ADD", "register:40f0:8", ["const:aff798:8", "const:4:8"]]
- 00aff798 ["CALL", null, ["callee:00bddc30:8"]]
+ 00aff7dc ["INT_ADD", "register:40f0:8", ["const:aff7dc:8", "const:4:8"]]
+ 00aff7dc ["CALL", null, ["callee:00bddc30:8"]]
- 00aff798 bytes 12790394
+ 00aff7dc bytes 15790394
- 00aff7a4 ["COPY", "register:0:8", ["register:40a0:8"]]
- 00aff7a4 ["INT_ADD", "register:40f0:8", ["const:aff7a4:8", "const:4:8"]]
- 00aff7a4 ["CALLIND", null, ["register:0:8"]]
+ 00aff7e8 ["COPY", "register:0:8", ["register:40a0:8"]]
+ 00aff7e8 ["INT_ADD", "register:40f0:8", ["const:aff7e8:8", "const:4:8"]]
+ 00aff7e8 ["CALLIND", null, ["register:0:8"]]
- 00aff7a4 bytes 80023fd6
+ 00aff7e8 bytes 80023fd6
- 00aff7ac ["INT_ADD", "register:40f0:8", ["const:aff7ac:8", "const:4:8"]]
- 00aff7ac ["CALL", null, ["callee:00bddc20:8"]]
+ 00aff7f0 ["INT_ADD", "register:40f0:8", ["const:aff7f0:8", "const:4:8"]]
+ 00aff7f0 ["CALL", null, ["callee:00bddc20:8"]]
- 00aff7ac bytes 09790394
+ 00aff7f0 bytes 0c790394
~~~


<a id="compare-e535e0781867402881080863a1984bee"></a>

### [`00aff7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff7c8.md) → [`00aff80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff80c.md) _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1a0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bde1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1f0.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aff7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff7c8.md#insn-00aff7e0) · [`00aff7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff7c8.md#insn-00aff7ec)
- 新版 `00aff824`（命令位置の公開資料なし） · `00aff830`（命令位置の公開資料なし）

~~~diff
- 00aff7e0 ["INT_ADD", "register:40f0:8", ["const:aff7e0:8", "const:4:8"]]
- 00aff7e0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00aff824 ["INT_ADD", "register:40f0:8", ["const:aff824:8", "const:4:8"]]
+ 00aff824 ["CALL", null, ["callee:00bddc20:8"]]
- 00aff7e0 bytes fc780394
+ 00aff824 bytes ff780394
- 00aff7ec ["INT_ADD", "register:40f0:8", ["const:aff7ec:8", "const:4:8"]]
- 00aff7ec ["CALL", null, ["callee:00bddc30:8"]]
+ 00aff830 ["INT_ADD", "register:40f0:8", ["const:aff830:8", "const:4:8"]]
+ 00aff830 ["CALL", null, ["callee:00bddc30:8"]]
- 00aff7ec bytes fd780394
+ 00aff830 bytes 00790394
~~~


<a id="compare-f4fea65b7e64502685a0566093d3ce8c"></a>

### [`00aff810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff810.md) → [`00aff854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff854.md) FUN_00aff854

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00aff800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff800.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00aff844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff844.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aff820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff810.md#insn-00aff820) · [`00aff838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff810.md#insn-00aff838) · [`00aff84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff810.md#insn-00aff84c)
- 新版 `00aff864`（命令位置の公開資料なし） · `00aff87c`（命令位置の公開資料なし） · `00aff890`（命令位置の公開資料なし）

~~~diff
- 00aff820 ["INT_ADD", "register:40f0:8", ["const:aff820:8", "const:4:8"]]
- 00aff820 ["CALL", null, ["callee:00bddc20:8"]]
+ 00aff864 ["INT_ADD", "register:40f0:8", ["const:aff864:8", "const:4:8"]]
+ 00aff864 ["CALL", null, ["callee:00bddc20:8"]]
- 00aff820 bytes ec780394
+ 00aff864 bytes ef780394
- 00aff838 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aff838 ["INT_ADD", "register:40f0:8", ["const:aff838:8", "const:4:8"]]
- 00aff838 ["CALLIND", null, ["register:0:8"]]
+ 00aff87c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aff87c ["INT_ADD", "register:40f0:8", ["const:aff87c:8", "const:4:8"]]
+ 00aff87c ["CALLIND", null, ["register:0:8"]]
- 00aff838 bytes 00013fd6
+ 00aff87c bytes 00013fd6
- 00aff84c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aff84c ["INT_ADD", "register:40f0:8", ["const:aff84c:8", "const:4:8"]]
- 00aff84c ["CALLIND", null, ["register:0:8"]]
+ 00aff890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aff890 ["INT_ADD", "register:40f0:8", ["const:aff890:8", "const:4:8"]]
+ 00aff890 ["CALLIND", null, ["register:0:8"]]
- 00aff84c bytes 00013fd6
+ 00aff890 bytes 00013fd6
~~~


<a id="compare-786e7a52c0cbebf9e39b40621985cf6e"></a>

### [`00aff86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff86c.md) → [`00aff8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff8b0.md) _ZN8firebase26ReferenceCountedFutureImpl15ReferenceFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aff88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff86c.md#insn-00aff88c) · [`00aff898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff86c.md#insn-00aff898) · [`00aff8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff86c.md#insn-00aff8e4)
- 新版 `00aff8d0`（命令位置の公開資料なし） · `00aff8dc`（命令位置の公開資料なし） · `00aff928`（命令位置の公開資料なし）

~~~diff
- 00aff88c ["INT_ADD", "register:40f0:8", ["const:aff88c:8", "const:4:8"]]
- 00aff88c ["CALL", null, ["callee:00bddc20:8"]]
+ 00aff8d0 ["INT_ADD", "register:40f0:8", ["const:aff8d0:8", "const:4:8"]]
+ 00aff8d0 ["CALL", null, ["callee:00bddc20:8"]]
- 00aff88c bytes d1780394
+ 00aff8d0 bytes d4780394
- 00aff898 ["INT_ADD", "register:40f0:8", ["const:aff898:8", "const:4:8"]]
- 00aff898 ["CALL", null, ["callee:00bddc20:8"]]
+ 00aff8dc ["INT_ADD", "register:40f0:8", ["const:aff8dc:8", "const:4:8"]]
+ 00aff8dc ["CALL", null, ["callee:00bddc20:8"]]
- 00aff898 bytes ce780394
+ 00aff8dc bytes d1780394
- 00aff8e4 ["INT_ADD", "register:40f0:8", ["const:aff8e4:8", "const:4:8"]]
- 00aff8e4 ["CALL", null, ["callee:00bddc30:8"]]
+ 00aff928 ["INT_ADD", "register:40f0:8", ["const:aff928:8", "const:4:8"]]
+ 00aff928 ["CALL", null, ["callee:00bddc30:8"]]
- 00aff8e4 bytes bf780394
+ 00aff928 bytes c2780394
~~~


<a id="compare-9742aee94e3769b93bb95937c7e2c0b0"></a>

### [`00aff908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff908.md) → [`00aff94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff94c.md) _ZN8firebase26ReferenceCountedFutureImpl13ReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aff928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff908.md#insn-00aff928) · [`00aff980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff908.md#insn-00aff980) · [`00aff9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff908.md#insn-00aff9f8)
- 新版 `00aff96c`（命令位置の公開資料なし） · `00aff9c4`（命令位置の公開資料なし） · `00affa3c`（命令位置の公開資料なし）

~~~diff
- 00aff928 ["INT_ADD", "register:40f0:8", ["const:aff928:8", "const:4:8"]]
- 00aff928 ["CALL", null, ["callee:00bddc20:8"]]
+ 00aff96c ["INT_ADD", "register:40f0:8", ["const:aff96c:8", "const:4:8"]]
+ 00aff96c ["CALL", null, ["callee:00bddc20:8"]]
- 00aff928 bytes aa780394
+ 00aff96c bytes ad780394
- 00aff980 ["INT_ADD", "register:40f0:8", ["const:aff980:8", "const:4:8"]]
- 00aff980 ["CALL", null, ["callee:00bde180:8"]]
+ 00aff9c4 ["INT_ADD", "register:40f0:8", ["const:aff9c4:8", "const:4:8"]]
+ 00aff9c4 ["CALL", null, ["callee:00bde180:8"]]
- 00aff980 bytes ec790394
+ 00aff9c4 bytes ef790394
- 00aff9f8 ["INT_ADD", "register:40f0:8", ["const:aff9f8:8", "const:4:8"]]
- 00aff9f8 ["CALL", null, ["callee:00bde750:8"]]
+ 00affa3c ["INT_ADD", "register:40f0:8", ["const:affa3c:8", "const:4:8"]]
+ 00affa3c ["CALL", null, ["callee:00bde750:8"]]
- 00aff9f8 bytes 427b0394
+ 00affa3c bytes 457b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98ea39233a7541d1100f839b37324d7"></a>

### [`00affa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affa2c.md) → [`00affa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affa70.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00affa4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affa2c.md#insn-00affa4c) · [`00affa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affa2c.md#insn-00affa58) · [`00affa98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affa2c.md#insn-00affa98)
- 新版 `00affa90`（命令位置の公開資料なし） · `00affa9c`（命令位置の公開資料なし） · `00affadc`（命令位置の公開資料なし）

~~~diff
- 00affa4c ["INT_ADD", "register:40f0:8", ["const:affa4c:8", "const:4:8"]]
- 00affa4c ["CALL", null, ["callee:00bddc20:8"]]
+ 00affa90 ["INT_ADD", "register:40f0:8", ["const:affa90:8", "const:4:8"]]
+ 00affa90 ["CALL", null, ["callee:00bddc20:8"]]
- 00affa4c bytes 61780394
+ 00affa90 bytes 64780394
- 00affa58 ["INT_ADD", "register:40f0:8", ["const:affa58:8", "const:4:8"]]
- 00affa58 ["CALL", null, ["callee:00bddc20:8"]]
+ 00affa9c ["INT_ADD", "register:40f0:8", ["const:affa9c:8", "const:4:8"]]
+ 00affa9c ["CALL", null, ["callee:00bddc20:8"]]
- 00affa58 bytes 5e780394
+ 00affa9c bytes 61780394
- 00affa98 ["INT_ADD", "register:40f0:8", ["const:affa98:8", "const:4:8"]]
- 00affa98 ["CALL", null, ["callee:00bddc30:8"]]
+ 00affadc ["INT_ADD", "register:40f0:8", ["const:affadc:8", "const:4:8"]]
+ 00affadc ["CALL", null, ["callee:00bddc30:8"]]
- 00affa98 bytes 52780394
+ 00affadc bytes 55780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acaa4a11a348302bc1cd9ffb7ef3d355"></a>

### [`00affad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affad4.md) → [`00affb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affb18.md) _ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00affaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affad4.md#insn-00affaf4) · [`00affb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affad4.md#insn-00affb00) · [`00affb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affad4.md#insn-00affb40)
- 新版 `00affb38`（命令位置の公開資料なし） · `00affb44`（命令位置の公開資料なし） · `00affb84`（命令位置の公開資料なし）

~~~diff
- 00affaf4 ["INT_ADD", "register:40f0:8", ["const:affaf4:8", "const:4:8"]]
- 00affaf4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00affb38 ["INT_ADD", "register:40f0:8", ["const:affb38:8", "const:4:8"]]
+ 00affb38 ["CALL", null, ["callee:00bddc20:8"]]
- 00affaf4 bytes 37780394
+ 00affb38 bytes 3a780394
- 00affb00 ["INT_ADD", "register:40f0:8", ["const:affb00:8", "const:4:8"]]
- 00affb00 ["CALL", null, ["callee:00bddc20:8"]]
+ 00affb44 ["INT_ADD", "register:40f0:8", ["const:affb44:8", "const:4:8"]]
+ 00affb44 ["CALL", null, ["callee:00bddc20:8"]]
- 00affb00 bytes 34780394
+ 00affb44 bytes 37780394
- 00affb40 ["INT_ADD", "register:40f0:8", ["const:affb40:8", "const:4:8"]]
- 00affb40 ["CALL", null, ["callee:00bddc30:8"]]
+ 00affb84 ["INT_ADD", "register:40f0:8", ["const:affb84:8", "const:4:8"]]
+ 00affb84 ["CALL", null, ["callee:00bddc30:8"]]
- 00affb40 bytes 28780394
+ 00affb84 bytes 2b780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1cc65522ddb4a3a66ed4e9379c8d5a3"></a>

### [`00affc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affc3c.md) → [`00affc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affc80.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00affc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affc3c.md#insn-00affc5c) · [`00affc68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affc3c.md#insn-00affc68) · [`00affca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affc3c.md#insn-00affca8)
- 新版 `00affca0`（命令位置の公開資料なし） · `00affcac`（命令位置の公開資料なし） · `00affcec`（命令位置の公開資料なし）

~~~diff
- 00affc5c ["INT_ADD", "register:40f0:8", ["const:affc5c:8", "const:4:8"]]
- 00affc5c ["CALL", null, ["callee:00bddc20:8"]]
+ 00affca0 ["INT_ADD", "register:40f0:8", ["const:affca0:8", "const:4:8"]]
+ 00affca0 ["CALL", null, ["callee:00bddc20:8"]]
- 00affc5c bytes dd770394
+ 00affca0 bytes e0770394
- 00affc68 ["INT_ADD", "register:40f0:8", ["const:affc68:8", "const:4:8"]]
- 00affc68 ["CALL", null, ["callee:00bddc20:8"]]
+ 00affcac ["INT_ADD", "register:40f0:8", ["const:affcac:8", "const:4:8"]]
+ 00affcac ["CALL", null, ["callee:00bddc20:8"]]
- 00affc68 bytes da770394
+ 00affcac bytes dd770394
- 00affca8 ["INT_ADD", "register:40f0:8", ["const:affca8:8", "const:4:8"]]
- 00affca8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00affcec ["INT_ADD", "register:40f0:8", ["const:affcec:8", "const:4:8"]]
+ 00affcec ["CALL", null, ["callee:00bddc30:8"]]
- 00affca8 bytes ce770394
+ 00affcec bytes d1770394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d159c757bb458a807a55301a3e32928"></a>

### [`00affcec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affcec.md) → [`00affd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affd30.md) _ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfc0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00affd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affcec.md#insn-00affd28) · [`00affd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affcec.md#insn-00affd44) · [`00affd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affcec.md#insn-00affd50)
- 新版 `00affd6c`（命令位置の公開資料なし） · `00affd88`（命令位置の公開資料なし） · `00affd94`（命令位置の公開資料なし）

~~~diff
- 00affd28 ["INT_ADD", "register:40f0:8", ["const:affd28:8", "const:4:8"]]
- 00affd28 ["CALL", null, ["callee:00bdb040:8"]]
+ 00affd6c ["INT_ADD", "register:40f0:8", ["const:affd6c:8", "const:4:8"]]
+ 00affd6c ["CALL", null, ["callee:00bdb040:8"]]
- 00affd28 bytes b26c0394
+ 00affd6c bytes b56c0394
- 00affd44 ["INT_ADD", "register:40f0:8", ["const:affd44:8", "const:4:8"]]
- 00affd44 ["CALL", null, ["callee:00bddc20:8"]]
+ 00affd88 ["INT_ADD", "register:40f0:8", ["const:affd88:8", "const:4:8"]]
+ 00affd88 ["CALL", null, ["callee:00bddc20:8"]]
- 00affd44 bytes a3770394
+ 00affd88 bytes a6770394
- 00affd50 ["INT_ADD", "register:40f0:8", ["const:affd50:8", "const:4:8"]]
- 00affd50 ["CALL", null, ["callee:00bddc20:8"]]
+ 00affd94 ["INT_ADD", "register:40f0:8", ["const:affd94:8", "const:4:8"]]
+ 00affd94 ["CALL", null, ["callee:00bddc20:8"]]
- 00affd50 bytes a0770394
+ 00affd94 bytes a3770394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f96a3fbe24ee7b316a3fff42097c3052"></a>

### [`00affea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affea0.md) → [`00affee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affee4.md) _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00affed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affea0.md#insn-00affed8) · [`00affee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affea0.md#insn-00affee4) · [`00afff24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affea0.md#insn-00afff24)
- 新版 `00afff1c`（命令位置の公開資料なし） · `00afff28`（命令位置の公開資料なし） · `00afff68`（命令位置の公開資料なし）

~~~diff
- 00affed8 ["INT_ADD", "register:40f0:8", ["const:affed8:8", "const:4:8"]]
- 00affed8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afff1c ["INT_ADD", "register:40f0:8", ["const:afff1c:8", "const:4:8"]]
+ 00afff1c ["CALL", null, ["callee:00bddc20:8"]]
- 00affed8 bytes 3e770394
+ 00afff1c bytes 41770394
- 00affee4 ["INT_ADD", "register:40f0:8", ["const:affee4:8", "const:4:8"]]
- 00affee4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afff28 ["INT_ADD", "register:40f0:8", ["const:afff28:8", "const:4:8"]]
+ 00afff28 ["CALL", null, ["callee:00bddc20:8"]]
- 00affee4 bytes 3b770394
+ 00afff28 bytes 3e770394
- 00afff24 ["INT_ADD", "register:40f0:8", ["const:afff24:8", "const:4:8"]]
- 00afff24 ["CALL", null, ["callee:00bddc30:8"]]
+ 00afff68 ["INT_ADD", "register:40f0:8", ["const:afff68:8", "const:4:8"]]
+ 00afff68 ["CALL", null, ["callee:00bddc30:8"]]
- 00afff24 bytes 2f770394
+ 00afff68 bytes 32770394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

