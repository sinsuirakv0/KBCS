# v15.7.3 → v15.7.4 · 要調査の変更候補 (18)

[一覧の目次](README.md)

<a id="compare-bb7e499e25666bf03251a0b25a4ef8c0"></a>

### [`00bbad34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad34.md) → [`00bbad78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad78.md) _ZNSt13bad_exceptionD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbad48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad34.md#insn-00bbad48)
- 新版 `00bbad8c`（命令位置の公開資料なし）

~~~diff
- 00bbad48 ["INT_ADD", "register:40f0:8", ["const:bbad48:8", "const:4:8"]]
- 00bbad48 ["CALL", null, ["callee:00be1e50:8"]]
+ 00bbad8c ["INT_ADD", "register:40f0:8", ["const:bbad8c:8", "const:4:8"]]
+ 00bbad8c ["CALL", null, ["callee:00be1e50:8"]]
- 00bbad48 bytes 2e9c0094
+ 00bbad8c bytes 319c0094
~~~


<a id="compare-3033a4ba3723bd1f37aa8b1acdc1da34"></a>

### [`00bbad88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad88.md) → [`00bbadcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadcc.md) _ZNSt9bad_allocD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdbbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdbc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbad9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad88.md#insn-00bbad9c)
- 新版 `00bbade0`（命令位置の公開資料なし）

~~~diff
- 00bbad9c ["INT_ADD", "register:40f0:8", ["const:bbad9c:8", "const:4:8"]]
- 00bbad9c ["CALL", null, ["callee:00bdbc00:8"]]
+ 00bbade0 ["INT_ADD", "register:40f0:8", ["const:bbade0:8", "const:4:8"]]
+ 00bbade0 ["CALL", null, ["callee:00bdbc00:8"]]
- 00bbad9c bytes 85830094
+ 00bbade0 bytes 88830094
~~~


<a id="compare-34e5a7301ee267c9b93a70e645735fbc"></a>

### [`00bbaddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaddc.md) → [`00bbae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae20.md) _ZNSt20bad_array_new_lengthD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbadf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaddc.md#insn-00bbadf0)
- 新版 `00bbae34`（命令位置の公開資料なし）

~~~diff
- 00bbadf0 ["INT_ADD", "register:40f0:8", ["const:bbadf0:8", "const:4:8"]]
- 00bbadf0 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00bbae34 ["INT_ADD", "register:40f0:8", ["const:bbae34:8", "const:4:8"]]
+ 00bbae34 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00bbadf0 bytes ec800094
+ 00bbae34 bytes ef800094
~~~


<a id="compare-cbe6b926c9f14556b4db2638fd80d4c3"></a>

### [`00bbae70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae70.md) → [`00bbaeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeb4.md) _ZNSt11logic_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbae84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae70.md#insn-00bbae84)
- 新版 `00bbaec8`（命令位置の公開資料なし）

~~~diff
- 00bbae84 ["INT_ADD", "register:40f0:8", ["const:bbae84:8", "const:4:8"]]
- 00bbae84 ["CALL", null, ["callee:00be1e60:8"]]
+ 00bbaec8 ["INT_ADD", "register:40f0:8", ["const:bbaec8:8", "const:4:8"]]
+ 00bbaec8 ["CALL", null, ["callee:00be1e60:8"]]
- 00bbae84 bytes e39b0094
+ 00bbaec8 bytes e69b0094
~~~


<a id="compare-fa1fbcb7dd192216804af40e733855af"></a>

### [`00bbaf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf00.md) → [`00bbaf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaf44.md) _ZNSt13runtime_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbaf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf00.md#insn-00bbaf14)
- 新版 `00bbaf58`（命令位置の公開資料なし）

~~~diff
- 00bbaf14 ["INT_ADD", "register:40f0:8", ["const:bbaf14:8", "const:4:8"]]
- 00bbaf14 ["CALL", null, ["callee:00be0fd0:8"]]
+ 00bbaf58 ["INT_ADD", "register:40f0:8", ["const:bbaf58:8", "const:4:8"]]
+ 00bbaf58 ["CALL", null, ["callee:00be0fd0:8"]]
- 00bbaf14 bytes 1b980094
+ 00bbaf58 bytes 1e980094
~~~


<a id="compare-b97cf3b0a9ab48f74f4cd30895ff2092"></a>

### [`00bbaf38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf38.md) → [`00bbaf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaf7c.md) _ZNSt12domain_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbaf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf38.md#insn-00bbaf4c)
- 新版 `00bbaf90`（命令位置の公開資料なし）

~~~diff
- 00bbaf4c ["INT_ADD", "register:40f0:8", ["const:bbaf4c:8", "const:4:8"]]
- 00bbaf4c ["CALL", null, ["callee:00be1e70:8"]]
+ 00bbaf90 ["INT_ADD", "register:40f0:8", ["const:bbaf90:8", "const:4:8"]]
+ 00bbaf90 ["CALL", null, ["callee:00be1e70:8"]]
- 00bbaf4c bytes b59b0094
+ 00bbaf90 bytes b89b0094
~~~


<a id="compare-360b83c5873947e5563733a0a43e3a96"></a>

### [`00bbaf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf64.md) → [`00bbafa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbafa8.md) _ZNSt16invalid_argumentD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be10e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbaf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf64.md#insn-00bbaf78)
- 新版 `00bbafbc`（命令位置の公開資料なし）

~~~diff
- 00bbaf78 ["INT_ADD", "register:40f0:8", ["const:bbaf78:8", "const:4:8"]]
- 00bbaf78 ["CALL", null, ["callee:00be1130:8"]]
+ 00bbafbc ["INT_ADD", "register:40f0:8", ["const:bbafbc:8", "const:4:8"]]
+ 00bbafbc ["CALL", null, ["callee:00be1130:8"]]
- 00bbaf78 bytes 5a980094
+ 00bbafbc bytes 5d980094
~~~


<a id="compare-726d460294396abf0baa1f1b89537954"></a>

### [`00bbaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf90.md) → [`00bbafd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbafd4.md) _ZNSt12length_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf90.md#insn-00bbafa4)
- 新版 `00bbafe8`（命令位置の公開資料なし）

~~~diff
- 00bbafa4 ["INT_ADD", "register:40f0:8", ["const:bbafa4:8", "const:4:8"]]
- 00bbafa4 ["CALL", null, ["callee:00bdb0b0:8"]]
+ 00bbafe8 ["INT_ADD", "register:40f0:8", ["const:bbafe8:8", "const:4:8"]]
+ 00bbafe8 ["CALL", null, ["callee:00bdb0b0:8"]]
- 00bbafa4 bytes 2f800094
+ 00bbafe8 bytes 32800094
~~~


<a id="compare-e8ef04253a8b34e7fe39eb6209456445"></a>

### [`00bbafbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbafbc.md) → [`00bbb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md) _ZNSt12out_of_rangeD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbafbc.md#insn-00bbafd0)
- 新版 `00bbb014`（命令位置の公開資料なし）

~~~diff
- 00bbafd0 ["INT_ADD", "register:40f0:8", ["const:bbafd0:8", "const:4:8"]]
- 00bbafd0 ["CALL", null, ["callee:00bdb250:8"]]
+ 00bbb014 ["INT_ADD", "register:40f0:8", ["const:bbb014:8", "const:4:8"]]
+ 00bbb014 ["CALL", null, ["callee:00bdb250:8"]]
- 00bbafd0 bytes 8c800094
+ 00bbb014 bytes 8f800094
~~~


<a id="compare-541442f88b30c93637537bdbc8f20e7e"></a>

### [`00bbafe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbafe8.md) → [`00bbb02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb02c.md) _ZNSt11range_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdda20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbaffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbafe8.md#insn-00bbaffc)
- 新版 `00bbb040`（命令位置の公開資料なし）

~~~diff
- 00bbaffc ["INT_ADD", "register:40f0:8", ["const:bbaffc:8", "const:4:8"]]
- 00bbaffc ["CALL", null, ["callee:00bdda70:8"]]
+ 00bbb040 ["INT_ADD", "register:40f0:8", ["const:bbb040:8", "const:4:8"]]
+ 00bbb040 ["CALL", null, ["callee:00bdda70:8"]]
- 00bbaffc bytes 898a0094
+ 00bbb040 bytes 8c8a0094
~~~


<a id="compare-3736ccc4db580e02bcfa5661b3c77f6c"></a>

### [`00bbb014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb014.md) → [`00bbb058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb058.md) _ZNSt14overflow_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb014.md#insn-00bbb028)
- 新版 `00bbb06c`（命令位置の公開資料なし）

~~~diff
- 00bbb028 ["INT_ADD", "register:40f0:8", ["const:bbb028:8", "const:4:8"]]
- 00bbb028 ["CALL", null, ["callee:00be0f70:8"]]
+ 00bbb06c ["INT_ADD", "register:40f0:8", ["const:bbb06c:8", "const:4:8"]]
+ 00bbb06c ["CALL", null, ["callee:00be0f70:8"]]
- 00bbb028 bytes be970094
+ 00bbb06c bytes c1970094
~~~


<a id="compare-934a40106b532143c1988c5704831aae"></a>

### [`00bbb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb040.md) → [`00bbb084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb084.md) _ZNSt15underflow_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb040.md#insn-00bbb054)
- 新版 `00bbb098`（命令位置の公開資料なし）

~~~diff
- 00bbb054 ["INT_ADD", "register:40f0:8", ["const:bbb054:8", "const:4:8"]]
- 00bbb054 ["CALL", null, ["callee:00be1e80:8"]]
+ 00bbb098 ["INT_ADD", "register:40f0:8", ["const:bbb098:8", "const:4:8"]]
+ 00bbb098 ["CALL", null, ["callee:00be1e80:8"]]
- 00bbb054 bytes 779b0094
+ 00bbb098 bytes 7a9b0094
~~~


<a id="compare-4f65f18aaafc39a46ea2cd1d97075aa9"></a>

### [`00bbb074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb074.md) → [`00bbb0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb0b8.md) _ZNSt9type_infoD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb074.md#insn-00bbb088)
- 新版 `00bbb0cc`（命令位置の公開資料なし）

~~~diff
- 00bbb088 ["INT_ADD", "register:40f0:8", ["const:bbb088:8", "const:4:8"]]
- 00bbb088 ["CALL", null, ["callee:00be1ea0:8"]]
+ 00bbb0cc ["INT_ADD", "register:40f0:8", ["const:bbb0cc:8", "const:4:8"]]
+ 00bbb0cc ["CALL", null, ["callee:00be1ea0:8"]]
- 00bbb088 bytes 729b0094
+ 00bbb0cc bytes 759b0094
~~~


<a id="compare-8275579a9833e405ed3a08620598305c"></a>

### [`00bbb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0c0.md) → [`00bbb104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb104.md) _ZNSt8bad_castD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0c0.md#insn-00bbb0d4)
- 新版 `00bbb118`（命令位置の公開資料なし）

~~~diff
- 00bbb0d4 ["INT_ADD", "register:40f0:8", ["const:bbb0d4:8", "const:4:8"]]
- 00bbb0d4 ["CALL", null, ["callee:00be1490:8"]]
+ 00bbb118 ["INT_ADD", "register:40f0:8", ["const:bbb118:8", "const:4:8"]]
+ 00bbb118 ["CALL", null, ["callee:00be1490:8"]]
- 00bbb0d4 bytes db980094
+ 00bbb118 bytes de980094
~~~


<a id="compare-89653f1375d5e46e0b9c50b70286a820"></a>

### [`00bbb11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb11c.md) → [`00bbb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb160.md) _ZNSt10bad_typeidD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb11c.md#insn-00bbb130)
- 新版 `00bbb174`（命令位置の公開資料なし）

~~~diff
- 00bbb130 ["INT_ADD", "register:40f0:8", ["const:bbb130:8", "const:4:8"]]
- 00bbb130 ["CALL", null, ["callee:00be1dc0:8"]]
+ 00bbb174 ["INT_ADD", "register:40f0:8", ["const:bbb174:8", "const:4:8"]]
+ 00bbb174 ["CALL", null, ["callee:00be1dc0:8"]]
- 00bbb130 bytes 109b0094
+ 00bbb174 bytes 139b0094
~~~


<a id="compare-a6299066c434d02fba7e1407e511f8f8"></a>

### [`00bbb27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb27c.md) → [`00bbb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2c0.md) FUN_00bbb2c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb27c.md#insn-00bbb290)
- 新版 `00bbb2d4`（命令位置の公開資料なし）

~~~diff
- 00bbb290 ["INT_ADD", "register:40f0:8", ["const:bbb290:8", "const:4:8"]]
- 00bbb290 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb2d4 ["INT_ADD", "register:40f0:8", ["const:bbb2d4:8", "const:4:8"]]
+ 00bbb2d4 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb290 bytes ec9a0094
+ 00bbb2d4 bytes ef9a0094
~~~


<a id="compare-c328c9c14d1e0d87efbfff3f80745d98"></a>

### [`00bbb2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb2a8.md) → [`00bbb2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2ec.md) FUN_00bbb2ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb2a8.md#insn-00bbb2bc)
- 新版 `00bbb300`（命令位置の公開資料なし）

~~~diff
- 00bbb2bc ["INT_ADD", "register:40f0:8", ["const:bbb2bc:8", "const:4:8"]]
- 00bbb2bc ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb300 ["INT_ADD", "register:40f0:8", ["const:bbb300:8", "const:4:8"]]
+ 00bbb300 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb2bc bytes e19a0094
+ 00bbb300 bytes e49a0094
~~~


<a id="compare-a8bc4ae244e2b0b79f92ad5ff67568e8"></a>

### [`00bbb2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb2d4.md) → [`00bbb318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb318.md) FUN_00bbb318

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb2d4.md#insn-00bbb2e8)
- 新版 `00bbb32c`（命令位置の公開資料なし）

~~~diff
- 00bbb2e8 ["INT_ADD", "register:40f0:8", ["const:bbb2e8:8", "const:4:8"]]
- 00bbb2e8 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb32c ["INT_ADD", "register:40f0:8", ["const:bbb32c:8", "const:4:8"]]
+ 00bbb32c ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb2e8 bytes d69a0094
+ 00bbb32c bytes d99a0094
~~~


<a id="compare-c016fd3368ac10f64d827de93b649ac3"></a>

### [`00bbb300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb300.md) → [`00bbb344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb344.md) FUN_00bbb344

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb300.md#insn-00bbb314)
- 新版 `00bbb358`（命令位置の公開資料なし）

~~~diff
- 00bbb314 ["INT_ADD", "register:40f0:8", ["const:bbb314:8", "const:4:8"]]
- 00bbb314 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb358 ["INT_ADD", "register:40f0:8", ["const:bbb358:8", "const:4:8"]]
+ 00bbb358 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb314 bytes cb9a0094
+ 00bbb358 bytes ce9a0094
~~~


<a id="compare-be1df195b30dd768e98b1785577338d3"></a>

### [`00bbb32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb32c.md) → [`00bbb370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb370.md) FUN_00bbb370

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb32c.md#insn-00bbb340)
- 新版 `00bbb384`（命令位置の公開資料なし）

~~~diff
- 00bbb340 ["INT_ADD", "register:40f0:8", ["const:bbb340:8", "const:4:8"]]
- 00bbb340 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb384 ["INT_ADD", "register:40f0:8", ["const:bbb384:8", "const:4:8"]]
+ 00bbb384 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb340 bytes c09a0094
+ 00bbb384 bytes c39a0094
~~~


<a id="compare-591be105d0720602e7856b3f48061168"></a>

### [`00bbb358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb358.md) → [`00bbb39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb39c.md) FUN_00bbb39c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb358.md#insn-00bbb36c)
- 新版 `00bbb3b0`（命令位置の公開資料なし）

~~~diff
- 00bbb36c ["INT_ADD", "register:40f0:8", ["const:bbb36c:8", "const:4:8"]]
- 00bbb36c ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb3b0 ["INT_ADD", "register:40f0:8", ["const:bbb3b0:8", "const:4:8"]]
+ 00bbb3b0 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb36c bytes b59a0094
+ 00bbb3b0 bytes b89a0094
~~~


<a id="compare-be482893045105bf30633f92cb41bf93"></a>

### [`00bbb384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb384.md) → [`00bbb3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb3c8.md) FUN_00bbb3c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb384.md#insn-00bbb398)
- 新版 `00bbb3dc`（命令位置の公開資料なし）

~~~diff
- 00bbb398 ["INT_ADD", "register:40f0:8", ["const:bbb398:8", "const:4:8"]]
- 00bbb398 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb3dc ["INT_ADD", "register:40f0:8", ["const:bbb3dc:8", "const:4:8"]]
+ 00bbb3dc ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb398 bytes aa9a0094
+ 00bbb3dc bytes ad9a0094
~~~


<a id="compare-6f5d12e687439f178dd2b7e3ccb0f569"></a>

### [`00bbb3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb3b0.md) → [`00bbb3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb3f4.md) FUN_00bbb3f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb3b0.md#insn-00bbb3c4)
- 新版 `00bbb408`（命令位置の公開資料なし）

~~~diff
- 00bbb3c4 ["INT_ADD", "register:40f0:8", ["const:bbb3c4:8", "const:4:8"]]
- 00bbb3c4 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb408 ["INT_ADD", "register:40f0:8", ["const:bbb408:8", "const:4:8"]]
+ 00bbb408 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb3c4 bytes 9f9a0094
+ 00bbb408 bytes a29a0094
~~~


<a id="compare-db9a95e854956cdc2142eb0f87c70007"></a>

### [`00bbb3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb3dc.md) → [`00bbb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb420.md) FUN_00bbb420

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb3dc.md#insn-00bbb3f0)
- 新版 `00bbb434`（命令位置の公開資料なし）

~~~diff
- 00bbb3f0 ["INT_ADD", "register:40f0:8", ["const:bbb3f0:8", "const:4:8"]]
- 00bbb3f0 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb434 ["INT_ADD", "register:40f0:8", ["const:bbb434:8", "const:4:8"]]
+ 00bbb434 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb3f0 bytes 949a0094
+ 00bbb434 bytes 979a0094
~~~


<a id="compare-aa98d7d9a5dab54974a33f0d9159db54"></a>

### [`00bbb408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb408.md) → [`00bbb44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb44c.md) FUN_00bbb44c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb408.md#insn-00bbb41c)
- 新版 `00bbb460`（命令位置の公開資料なし）

~~~diff
- 00bbb41c ["INT_ADD", "register:40f0:8", ["const:bbb41c:8", "const:4:8"]]
- 00bbb41c ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb460 ["INT_ADD", "register:40f0:8", ["const:bbb460:8", "const:4:8"]]
+ 00bbb460 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb41c bytes 899a0094
+ 00bbb460 bytes 8c9a0094
~~~


<a id="compare-f33e6e4cf45ed7f03a3259351865ddfc"></a>

### [`00bbb568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb568.md) → [`00bbb5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb5ac.md) __dynamic_cast

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb568.md#insn-00bbb60c) · [`00bbb66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb568.md#insn-00bbb66c) · [`00bbb744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb568.md#insn-00bbb744)
- 新版 `00bbb650`（命令位置の公開資料なし） · `00bbb6b0`（命令位置の公開資料なし） · `00bbb788`（命令位置の公開資料なし）

~~~diff
- 00bbb60c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bbb60c ["INT_ADD", "register:40f0:8", ["const:bbb60c:8", "const:4:8"]]
- 00bbb60c ["CALLIND", null, ["register:0:8"]]
+ 00bbb650 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bbb650 ["INT_ADD", "register:40f0:8", ["const:bbb650:8", "const:4:8"]]
+ 00bbb650 ["CALLIND", null, ["register:0:8"]]
- 00bbb60c bytes 20013fd6
+ 00bbb650 bytes 20013fd6
- 00bbb66c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbb66c ["INT_ADD", "register:40f0:8", ["const:bbb66c:8", "const:4:8"]]
- 00bbb66c ["CALLIND", null, ["register:0:8"]]
+ 00bbb6b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbb6b0 ["INT_ADD", "register:40f0:8", ["const:bbb6b0:8", "const:4:8"]]
+ 00bbb6b0 ["CALLIND", null, ["register:0:8"]]
- 00bbb66c bytes 00013fd6
+ 00bbb6b0 bytes 00013fd6
- 00bbb744 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbb744 ["INT_ADD", "register:40f0:8", ["const:bbb744:8", "const:4:8"]]
- 00bbb744 ["CALLIND", null, ["register:0:8"]]
+ 00bbb788 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbb788 ["INT_ADD", "register:40f0:8", ["const:bbb788:8", "const:4:8"]]
+ 00bbb788 ["CALLIND", null, ["register:0:8"]]
- 00bbb744 bytes 00013fd6
+ 00bbb788 bytes 00013fd6
~~~


<a id="compare-3a63ade685fea36cf352cb47edc98ebb"></a>

### [`00bbb890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb890.md) → [`00bbb8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb8d4.md) FUN_00bbb8d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb890.md#insn-00bbb998) · [`00bbba1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb890.md#insn-00bbba1c)
- 新版 `00bbb9dc`（命令位置の公開資料なし） · `00bbba60`（命令位置の公開資料なし）

~~~diff
- 00bbb998 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbb998 ["INT_ADD", "register:40f0:8", ["const:bbb998:8", "const:4:8"]]
- 00bbb998 ["CALLIND", null, ["register:0:8"]]
+ 00bbb9dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbb9dc ["INT_ADD", "register:40f0:8", ["const:bbb9dc:8", "const:4:8"]]
+ 00bbb9dc ["CALLIND", null, ["register:0:8"]]
- 00bbb998 bytes 00013fd6
+ 00bbb9dc bytes 00013fd6
- 00bbba1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbba1c ["INT_ADD", "register:40f0:8", ["const:bbba1c:8", "const:4:8"]]
- 00bbba1c ["CALLIND", null, ["register:0:8"]]
+ 00bbba60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbba60 ["INT_ADD", "register:40f0:8", ["const:bbba60:8", "const:4:8"]]
+ 00bbba60 ["CALLIND", null, ["register:0:8"]]
- 00bbba1c bytes 00013fd6
+ 00bbba60 bytes 00013fd6
~~~


<a id="compare-29553f09eb95e9f17ec585f9d2c45a23"></a>

### [`00bbc0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc0c8.md) → [`00bbc10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc10c.md) FUN_00bbc10c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbc118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc0c8.md#insn-00bbc118) · [`00bbc134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc0c8.md#insn-00bbc134) · [`00bbc1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc0c8.md#insn-00bbc1e4)
- 新版 `00bbc15c`（命令位置の公開資料なし） · `00bbc178`（命令位置の公開資料なし） · `00bbc228`（命令位置の公開資料なし）

~~~diff
- 00bbc118 ["INT_ADD", "register:40f0:8", ["const:bbc118:8", "const:4:8"]]
- 00bbc118 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbc15c ["INT_ADD", "register:40f0:8", ["const:bbc15c:8", "const:4:8"]]
+ 00bbc15c ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbc118 bytes 1a8a0094
+ 00bbc15c bytes 1d8a0094
- 00bbc134 ["INT_ADD", "register:40f0:8", ["const:bbc134:8", "const:4:8"]]
- 00bbc134 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbc178 ["INT_ADD", "register:40f0:8", ["const:bbc178:8", "const:4:8"]]
+ 00bbc178 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbc134 bytes 138a0094
+ 00bbc178 bytes 168a0094
- 00bbc1e4 ["COPY", "register:0:8", ["register:4050:8"]]
- 00bbc1e4 ["INT_ADD", "register:40f0:8", ["const:bbc1e4:8", "const:4:8"]]
- 00bbc1e4 ["CALLIND", null, ["register:0:8"]]
+ 00bbc228 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00bbc228 ["INT_ADD", "register:40f0:8", ["const:bbc228:8", "const:4:8"]]
+ 00bbc228 ["CALLIND", null, ["register:0:8"]]
- 00bbc1e4 bytes 40013fd6
+ 00bbc228 bytes 40013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1068db90c6d62fa38338e4934b87736"></a>

### [`00bbc478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc478.md) → [`00bbc4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc4bc.md) FUN_00bbc4bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbc4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc478.md#insn-00bbc4c0) · [`00bbc4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc478.md#insn-00bbc4e0) · [`00bbc538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc478.md#insn-00bbc538)
- 新版 `00bbc504`（命令位置の公開資料なし） · `00bbc524`（命令位置の公開資料なし） · `00bbc57c`（命令位置の公開資料なし）

~~~diff
- 00bbc4c0 ["INT_ADD", "register:40f0:8", ["const:bbc4c0:8", "const:4:8"]]
- 00bbc4c0 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbc504 ["INT_ADD", "register:40f0:8", ["const:bbc504:8", "const:4:8"]]
+ 00bbc504 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbc4c0 bytes 30890094
+ 00bbc504 bytes 33890094
- 00bbc4e0 ["INT_ADD", "register:40f0:8", ["const:bbc4e0:8", "const:4:8"]]
- 00bbc4e0 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbc524 ["INT_ADD", "register:40f0:8", ["const:bbc524:8", "const:4:8"]]
+ 00bbc524 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbc4e0 bytes 28890094
+ 00bbc524 bytes 2b890094
- 00bbc538 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbc538 ["INT_ADD", "register:40f0:8", ["const:bbc538:8", "const:4:8"]]
- 00bbc538 ["CALLIND", null, ["register:0:8"]]
+ 00bbc57c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbc57c ["INT_ADD", "register:40f0:8", ["const:bbc57c:8", "const:4:8"]]
+ 00bbc57c ["CALLIND", null, ["register:0:8"]]
- 00bbc538 bytes 00013fd6
+ 00bbc57c bytes 00013fd6
~~~


<a id="compare-4dbc8ae456a4ffa392039a8f413f4794"></a>

### [`00bbc628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc628.md) → [`00bbc66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc66c.md) FUN_00bbc66c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbc66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc628.md#insn-00bbc66c) · [`00bbc688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc628.md#insn-00bbc688)
- 新版 `00bbc6b0`（命令位置の公開資料なし） · `00bbc6cc`（命令位置の公開資料なし）

~~~diff
- 00bbc66c ["INT_ADD", "register:40f0:8", ["const:bbc66c:8", "const:4:8"]]
- 00bbc66c ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbc6b0 ["INT_ADD", "register:40f0:8", ["const:bbc6b0:8", "const:4:8"]]
+ 00bbc6b0 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbc66c bytes c5880094
+ 00bbc6b0 bytes c8880094
- 00bbc688 ["INT_ADD", "register:40f0:8", ["const:bbc688:8", "const:4:8"]]
- 00bbc688 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbc6cc ["INT_ADD", "register:40f0:8", ["const:bbc6cc:8", "const:4:8"]]
+ 00bbc6cc ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbc688 bytes be880094
+ 00bbc6cc bytes c1880094
~~~


<a id="compare-a338c756ff1a5ac05d985636bbcf85ab"></a>

### [`00bbc984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc984.md) → [`00bbc9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc9c8.md) FUN_00bbc9c8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbc9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc984.md#insn-00bbc9d4)
- 新版 `00bbca18`（命令位置の公開資料なし）

~~~diff
- 00bbc9d4 ["INT_ADD", "register:40f0:8", ["const:bbc9d4:8", "const:4:8"]]
- 00bbc9d4 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbca18 ["INT_ADD", "register:40f0:8", ["const:bbca18:8", "const:4:8"]]
+ 00bbca18 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbc9d4 bytes eb870094
+ 00bbca18 bytes ee870094
~~~


<a id="compare-914d337d18c1732d2adc52b0fbf7f268"></a>

### [`00bbcac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcac8.md) → [`00bbcb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcb0c.md) FUN_00bbcb0c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbcb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcac8.md#insn-00bbcb0c)
- 新版 `00bbcb50`（命令位置の公開資料なし）

~~~diff
- 00bbcb0c ["INT_ADD", "register:40f0:8", ["const:bbcb0c:8", "const:4:8"]]
- 00bbcb0c ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbcb50 ["INT_ADD", "register:40f0:8", ["const:bbcb50:8", "const:4:8"]]
+ 00bbcb50 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbcb0c bytes 9d870094
+ 00bbcb50 bytes a0870094
~~~


<a id="compare-08eaf040de8a28b8b5206751988cb60f"></a>

### [`00bbd194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd194.md) → [`00bbd1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd1d8.md) FUN_00bbd1d8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbd1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd194.md#insn-00bbd1b8) · [`00bbd1f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd194.md#insn-00bbd1f4) · [`00bbd208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd194.md#insn-00bbd208)
- 新版 `00bbd1fc`（命令位置の公開資料なし） · `00bbd238`（命令位置の公開資料なし） · `00bbd24c`（命令位置の公開資料なし）

~~~diff
- 00bbd1b8 ["INT_ADD", "register:40f0:8", ["const:bbd1b8:8", "const:4:8"]]
- 00bbd1b8 ["CALL", null, ["callee:00bdb810:8"]]
+ 00bbd1fc ["INT_ADD", "register:40f0:8", ["const:bbd1fc:8", "const:4:8"]]
+ 00bbd1fc ["CALL", null, ["callee:00bdb810:8"]]
- 00bbd1b8 bytes 82790094
+ 00bbd1fc bytes 85790094
- 00bbd1f4 ["INT_ADD", "register:40f0:8", ["const:bbd1f4:8", "const:4:8"]]
- 00bbd1f4 ["CALL", null, ["callee:00bdb810:8"]]
+ 00bbd238 ["INT_ADD", "register:40f0:8", ["const:bbd238:8", "const:4:8"]]
+ 00bbd238 ["CALL", null, ["callee:00bdb810:8"]]
- 00bbd1f4 bytes 73790094
+ 00bbd238 bytes 76790094
- 00bbd208 ["INT_ADD", "register:40f0:8", ["const:bbd208:8", "const:4:8"]]
- 00bbd208 ["CALL", null, ["callee:00bdb810:8"]]
+ 00bbd24c ["INT_ADD", "register:40f0:8", ["const:bbd24c:8", "const:4:8"]]
+ 00bbd24c ["CALL", null, ["callee:00bdb810:8"]]
- 00bbd208 bytes 6e790094
+ 00bbd24c bytes 71790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f3afa596743f3e1140d56252746a3b"></a>

### [`00bbd264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd264.md) → [`00bbd2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md) FUN_00bbd2a8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbd294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd264.md#insn-00bbd294)
- 新版 `00bbd2d8`（命令位置の公開資料なし）

~~~diff
- 00bbd294 ["INT_ADD", "register:40f0:8", ["const:bbd294:8", "const:4:8"]]
- 00bbd294 ["CALL", null, ["callee:00bdb200:8"]]
+ 00bbd2d8 ["INT_ADD", "register:40f0:8", ["const:bbd2d8:8", "const:4:8"]]
+ 00bbd2d8 ["CALL", null, ["callee:00bdb200:8"]]
- 00bbd294 bytes c7770094
+ 00bbd2d8 bytes ca770094
~~~


<a id="compare-27ffa58b45fccf770f9df73e3ad9ea51"></a>

### [`00bbf1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md) → [`00bbf1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf1f4.md) FUN_00bbf1f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 2件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbf24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md#insn-00bbf24c) · [`00bbf2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md#insn-00bbf2c8) · [`00bbf2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md#insn-00bbf2e8)
- 新版 `00bbf290`（命令位置の公開資料なし） · `00bbf30c`（命令位置の公開資料なし） · `00bbf32c`（命令位置の公開資料なし）

~~~diff
- 00bbf24c ["INT_ADD", "register:40f0:8", ["const:bbf24c:8", "const:4:8"]]
- 00bbf24c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00bbf290 ["INT_ADD", "register:40f0:8", ["const:bbf290:8", "const:4:8"]]
+ 00bbf290 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00bbf24c bytes 956f0094
+ 00bbf290 bytes 986f0094
- 00bbf2c8 ["INT_ADD", "register:40f0:8", ["const:bbf2c8:8", "const:4:8"]]
- 00bbf2c8 ["CALL", null, ["callee:00bdb810:8"]]
+ 00bbf30c ["INT_ADD", "register:40f0:8", ["const:bbf30c:8", "const:4:8"]]
+ 00bbf30c ["CALL", null, ["callee:00bdb810:8"]]
- 00bbf2c8 bytes 3e710094
+ 00bbf30c bytes 41710094
- 00bbf2e8 ["INT_ADD", "register:40f0:8", ["const:bbf2e8:8", "const:4:8"]]
- 00bbf2e8 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00bbf32c ["INT_ADD", "register:40f0:8", ["const:bbf32c:8", "const:4:8"]]
+ 00bbf32c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00bbf2e8 bytes 6e6f0094
+ 00bbf32c bytes 716f0094
~~~


<a id="compare-d9b71af5466806dc710052541da539f3"></a>

### [`00bbfdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md) → [`00bbfdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md) FUN_00bbfdf8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 4件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 4件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbfdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md#insn-00bbfdfc) · [`00bbfe10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md#insn-00bbfe10) · [`00bbfe18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md#insn-00bbfe18)
- 新版 `00bbfe40`（命令位置の公開資料なし） · `00bbfe54`（命令位置の公開資料なし） · `00bbfe5c`（命令位置の公開資料なし）

~~~diff
- 00bbfdfc ["INT_ADD", "register:40f0:8", ["const:bbfdfc:8", "const:4:8"]]
- 00bbfdfc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bbfe40 ["INT_ADD", "register:40f0:8", ["const:bbfe40:8", "const:4:8"]]
+ 00bbfe40 ["CALL", null, ["callee:00bdd250:8"]]
- 00bbfdfc bytes 01750094
+ 00bbfe40 bytes 04750094
- 00bbfe10 ["INT_ADD", "register:40f0:8", ["const:bbfe10:8", "const:4:8"]]
- 00bbfe10 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bbfe54 ["INT_ADD", "register:40f0:8", ["const:bbfe54:8", "const:4:8"]]
+ 00bbfe54 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bbfe10 bytes 18790094
+ 00bbfe54 bytes 1b790094
- 00bbfe18 ["INT_ADD", "register:40f0:8", ["const:bbfe18:8", "const:4:8"]]
- 00bbfe18 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bbfe5c ["INT_ADD", "register:40f0:8", ["const:bbfe5c:8", "const:4:8"]]
+ 00bbfe5c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bbfe18 bytes da740094
+ 00bbfe5c bytes dd740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40b4fee0c9bf75ca8d3d0f9778dcb52c"></a>

### [`00bc017c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md) → [`00bc01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc01c0.md) FUN_00bc01c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 2件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc01f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md#insn-00bc01f0) · [`00bc0218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md#insn-00bc0218) · [`00bc02ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md#insn-00bc02ac)
- 新版 `00bc0234`（命令位置の公開資料なし） · `00bc025c`（命令位置の公開資料なし） · `00bc02f0`（命令位置の公開資料なし）

~~~diff
- 00bc01f0 ["INT_ADD", "register:40f0:8", ["const:bc01f0:8", "const:4:8"]]
- 00bc01f0 ["CALL", null, ["callee:00bdb810:8"]]
+ 00bc0234 ["INT_ADD", "register:40f0:8", ["const:bc0234:8", "const:4:8"]]
+ 00bc0234 ["CALL", null, ["callee:00bdb810:8"]]
- 00bc01f0 bytes 746d0094
+ 00bc0234 bytes 776d0094
- 00bc0218 ["INT_ADD", "register:40f0:8", ["const:bc0218:8", "const:4:8"]]
- 00bc0218 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00bc025c ["INT_ADD", "register:40f0:8", ["const:bc025c:8", "const:4:8"]]
+ 00bc025c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00bc0218 bytes a26b0094
+ 00bc025c bytes a56b0094
- 00bc02ac ["INT_ADD", "register:40f0:8", ["const:bc02ac:8", "const:4:8"]]
- 00bc02ac ["CALL", null, ["callee:00bdb810:8"]]
+ 00bc02f0 ["INT_ADD", "register:40f0:8", ["const:bc02f0:8", "const:4:8"]]
+ 00bc02f0 ["CALL", null, ["callee:00bdb810:8"]]
- 00bc02ac bytes 456d0094
+ 00bc02f0 bytes 486d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a4d355ce5380f752b7b073f448e93e2"></a>

### [`00bc0e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md) → [`00bc0ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ec0.md) FUN_00bc0ec0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc0ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md#insn-00bc0ecc) · [`00bc0ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md#insn-00bc0ee8) · [`00bc0f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md#insn-00bc0f0c)
- 新版 `00bc0f10`（命令位置の公開資料なし） · `00bc0f2c`（命令位置の公開資料なし） · `00bc0f50`（命令位置の公開資料なし）

~~~diff
- 00bc0ecc ["INT_ADD", "register:40f0:8", ["const:bc0ecc:8", "const:4:8"]]
- 00bc0ecc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc0f10 ["INT_ADD", "register:40f0:8", ["const:bc0f10:8", "const:4:8"]]
+ 00bc0f10 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc0ecc bytes cd700094
+ 00bc0f10 bytes d0700094
- 00bc0ee8 ["INT_ADD", "register:40f0:8", ["const:bc0ee8:8", "const:4:8"]]
- 00bc0ee8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bc0f2c ["INT_ADD", "register:40f0:8", ["const:bc0f2c:8", "const:4:8"]]
+ 00bc0f2c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bc0ee8 bytes 9e680094
+ 00bc0f2c bytes a1680094
- 00bc0f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc0f0c ["INT_ADD", "register:40f0:8", ["const:bc0f0c:8", "const:4:8"]]
- 00bc0f0c ["CALLIND", null, ["register:0:8"]]
+ 00bc0f50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc0f50 ["INT_ADD", "register:40f0:8", ["const:bc0f50:8", "const:4:8"]]
+ 00bc0f50 ["CALLIND", null, ["register:0:8"]]
- 00bc0f0c bytes 00013fd6
+ 00bc0f50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbc78c786640f498bf52dcba17d38c88"></a>

### [`00bc0f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f7c.md) → [`00bc0fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0fc0.md) FUN_00bc0fc0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc0fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f7c.md#insn-00bc0fc4) · [`00bc1014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f7c.md#insn-00bc1014) · [`00bc1038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f7c.md#insn-00bc1038)
- 新版 `00bc1008`（命令位置の公開資料なし） · `00bc1058`（命令位置の公開資料なし） · `00bc107c`（命令位置の公開資料なし）

~~~diff
- 00bc0fc4 ["INT_ADD", "register:40f0:8", ["const:bc0fc4:8", "const:4:8"]]
- 00bc0fc4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc1008 ["INT_ADD", "register:40f0:8", ["const:bc1008:8", "const:4:8"]]
+ 00bc1008 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc0fc4 bytes 8f700094
+ 00bc1008 bytes 92700094
- 00bc1014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1014 ["INT_ADD", "register:40f0:8", ["const:bc1014:8", "const:4:8"]]
- 00bc1014 ["CALLIND", null, ["register:0:8"]]
+ 00bc1058 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1058 ["INT_ADD", "register:40f0:8", ["const:bc1058:8", "const:4:8"]]
+ 00bc1058 ["CALLIND", null, ["register:0:8"]]
- 00bc1014 bytes 00013fd6
+ 00bc1058 bytes 00013fd6
- 00bc1038 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1038 ["INT_ADD", "register:40f0:8", ["const:bc1038:8", "const:4:8"]]
- 00bc1038 ["CALLIND", null, ["register:0:8"]]
+ 00bc107c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc107c ["INT_ADD", "register:40f0:8", ["const:bc107c:8", "const:4:8"]]
+ 00bc107c ["CALLIND", null, ["register:0:8"]]
- 00bc1038 bytes 00013fd6
+ 00bc107c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad0221f8a1a80885a71ff8e105884a0"></a>

### [`00bc13c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md) → [`00bc140c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc140c.md) FUN_00bc140c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md#insn-00bc1418) · [`00bc1434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md#insn-00bc1434) · [`00bc1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md#insn-00bc1458)
- 新版 `00bc145c`（命令位置の公開資料なし） · `00bc1478`（命令位置の公開資料なし） · `00bc149c`（命令位置の公開資料なし）

~~~diff
- 00bc1418 ["INT_ADD", "register:40f0:8", ["const:bc1418:8", "const:4:8"]]
- 00bc1418 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc145c ["INT_ADD", "register:40f0:8", ["const:bc145c:8", "const:4:8"]]
+ 00bc145c ["CALL", null, ["callee:00bdd250:8"]]
- 00bc1418 bytes 7a6f0094
+ 00bc145c bytes 7d6f0094
- 00bc1434 ["INT_ADD", "register:40f0:8", ["const:bc1434:8", "const:4:8"]]
- 00bc1434 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bc1478 ["INT_ADD", "register:40f0:8", ["const:bc1478:8", "const:4:8"]]
+ 00bc1478 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bc1434 bytes 4b670094
+ 00bc1478 bytes 4e670094
- 00bc1458 ["INT_ADD", "register:40f0:8", ["const:bc1458:8", "const:4:8"]]
- 00bc1458 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bc149c ["INT_ADD", "register:40f0:8", ["const:bc149c:8", "const:4:8"]]
+ 00bc149c ["CALL", null, ["callee:00bde2c0:8"]]
- 00bc1458 bytes 86730094
+ 00bc149c bytes 89730094
~~~


<a id="compare-db8ef62e42bc5171503f2c187412dbd8"></a>

### [`00bc1474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md) → [`00bc14b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc14b8.md) FUN_00bc14b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc14a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md#insn-00bc14a8) · [`00bc14cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md#insn-00bc14cc) · [`00bc1518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md#insn-00bc1518)
- 新版 `00bc14ec`（命令位置の公開資料なし） · `00bc1510`（命令位置の公開資料なし） · `00bc155c`（命令位置の公開資料なし）

~~~diff
- 00bc14a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc14a8 ["INT_ADD", "register:40f0:8", ["const:bc14a8:8", "const:4:8"]]
- 00bc14a8 ["CALLIND", null, ["register:0:8"]]
+ 00bc14ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc14ec ["INT_ADD", "register:40f0:8", ["const:bc14ec:8", "const:4:8"]]
+ 00bc14ec ["CALLIND", null, ["register:0:8"]]
- 00bc14a8 bytes 00013fd6
+ 00bc14ec bytes 00013fd6
- 00bc14cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc14cc ["INT_ADD", "register:40f0:8", ["const:bc14cc:8", "const:4:8"]]
- 00bc14cc ["CALLIND", null, ["register:0:8"]]
+ 00bc1510 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1510 ["INT_ADD", "register:40f0:8", ["const:bc1510:8", "const:4:8"]]
+ 00bc1510 ["CALLIND", null, ["register:0:8"]]
- 00bc14cc bytes 00013fd6
+ 00bc1510 bytes 00013fd6
- 00bc1518 ["INT_ADD", "register:40f0:8", ["const:bc1518:8", "const:4:8"]]
- 00bc1518 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc155c ["INT_ADD", "register:40f0:8", ["const:bc155c:8", "const:4:8"]]
+ 00bc155c ["CALL", null, ["callee:00bdd250:8"]]
- 00bc1518 bytes 3a6f0094
+ 00bc155c bytes 3d6f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-293a879bdad9728916240131e9ef5bea"></a>

### [`00bc2abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md) → [`00bc2b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md) FUN_00bc2b00

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) · 呼出先 4件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) · 呼出先 4件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md#insn-00bc2b04) · [`00bc2b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md#insn-00bc2b18) · [`00bc2b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md#insn-00bc2b20)
- 新版 `00bc2b48`（命令位置の公開資料なし） · `00bc2b5c`（命令位置の公開資料なし） · `00bc2b64`（命令位置の公開資料なし）

~~~diff
- 00bc2b04 ["INT_ADD", "register:40f0:8", ["const:bc2b04:8", "const:4:8"]]
- 00bc2b04 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc2b48 ["INT_ADD", "register:40f0:8", ["const:bc2b48:8", "const:4:8"]]
+ 00bc2b48 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc2b04 bytes bf690094
+ 00bc2b48 bytes c2690094
- 00bc2b18 ["INT_ADD", "register:40f0:8", ["const:bc2b18:8", "const:4:8"]]
- 00bc2b18 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bc2b5c ["INT_ADD", "register:40f0:8", ["const:bc2b5c:8", "const:4:8"]]
+ 00bc2b5c ["CALL", null, ["callee:00bde2c0:8"]]
- 00bc2b18 bytes d66d0094
+ 00bc2b5c bytes d96d0094
- 00bc2b20 ["INT_ADD", "register:40f0:8", ["const:bc2b20:8", "const:4:8"]]
- 00bc2b20 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc2b64 ["INT_ADD", "register:40f0:8", ["const:bc2b64:8", "const:4:8"]]
+ 00bc2b64 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc2b20 bytes 98690094
+ 00bc2b64 bytes 9b690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9901e61b8c55270cddac2bbcaa075f62"></a>

### [`00bc2c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2c40.md) → [`00bc2c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2c84.md) FUN_00bc2c84

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2c40.md#insn-00bc2c8c)
- 新版 `00bc2cd0`（命令位置の公開資料なし）

~~~diff
- 00bc2c8c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2c8c ["INT_ADD", "register:40f0:8", ["const:bc2c8c:8", "const:4:8"]]
- 00bc2c8c ["CALLIND", null, ["register:0:8"]]
+ 00bc2cd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2cd0 ["INT_ADD", "register:40f0:8", ["const:bc2cd0:8", "const:4:8"]]
+ 00bc2cd0 ["CALLIND", null, ["register:0:8"]]
- 00bc2c8c bytes 20013fd6
+ 00bc2cd0 bytes 20013fd6
~~~


<a id="compare-3ecb0bcf9dcb1a939fdbfbca06d14401"></a>

### [`00bc2cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2cc4.md) → [`00bc2d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d08.md) FUN_00bc2d08

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2cc4.md#insn-00bc2d10)
- 新版 `00bc2d54`（命令位置の公開資料なし）

~~~diff
- 00bc2d10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2d10 ["INT_ADD", "register:40f0:8", ["const:bc2d10:8", "const:4:8"]]
- 00bc2d10 ["CALLIND", null, ["register:0:8"]]
+ 00bc2d54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2d54 ["INT_ADD", "register:40f0:8", ["const:bc2d54:8", "const:4:8"]]
+ 00bc2d54 ["CALLIND", null, ["register:0:8"]]
- 00bc2d10 bytes 20013fd6
+ 00bc2d54 bytes 20013fd6
~~~


<a id="compare-3947ca73cc7296362b5d280fe2e07333"></a>

### [`00bc2d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2d48.md) → [`00bc2d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d8c.md) FUN_00bc2d8c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2d48.md#insn-00bc2d94)
- 新版 `00bc2dd8`（命令位置の公開資料なし）

~~~diff
- 00bc2d94 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2d94 ["INT_ADD", "register:40f0:8", ["const:bc2d94:8", "const:4:8"]]
- 00bc2d94 ["CALLIND", null, ["register:0:8"]]
+ 00bc2dd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2dd8 ["INT_ADD", "register:40f0:8", ["const:bc2dd8:8", "const:4:8"]]
+ 00bc2dd8 ["CALLIND", null, ["register:0:8"]]
- 00bc2d94 bytes 20013fd6
+ 00bc2dd8 bytes 20013fd6
~~~


<a id="compare-84543769376f12f8d4e7f64e9f9ceb56"></a>

### [`00bc2dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2dcc.md) → [`00bc2e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2e10.md) FUN_00bc2e10

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2dcc.md#insn-00bc2e00)
- 新版 `00bc2e44`（命令位置の公開資料なし）

~~~diff
- 00bc2e00 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2e00 ["INT_ADD", "register:40f0:8", ["const:bc2e00:8", "const:4:8"]]
- 00bc2e00 ["CALLIND", null, ["register:0:8"]]
+ 00bc2e44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2e44 ["INT_ADD", "register:40f0:8", ["const:bc2e44:8", "const:4:8"]]
+ 00bc2e44 ["CALLIND", null, ["register:0:8"]]
- 00bc2e00 bytes 20013fd6
+ 00bc2e44 bytes 20013fd6
~~~


<a id="compare-e146650316ed2cc7284f8f025bd03128"></a>

### [`00bc2e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e20.md) → [`00bc2e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2e64.md) FUN_00bc2e64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e20.md#insn-00bc2e50)
- 新版 `00bc2e94`（命令位置の公開資料なし）

~~~diff
- 00bc2e50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2e50 ["INT_ADD", "register:40f0:8", ["const:bc2e50:8", "const:4:8"]]
- 00bc2e50 ["CALLIND", null, ["register:0:8"]]
+ 00bc2e94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2e94 ["INT_ADD", "register:40f0:8", ["const:bc2e94:8", "const:4:8"]]
+ 00bc2e94 ["CALLIND", null, ["register:0:8"]]
- 00bc2e50 bytes 00013fd6
+ 00bc2e94 bytes 00013fd6
~~~


<a id="compare-ed9329d0a8b303a20747d08aeffbccfc"></a>

### [`00bc2e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e70.md) → [`00bc2eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2eb4.md) FUN_00bc2eb4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e70.md#insn-00bc2ea0)
- 新版 `00bc2ee4`（命令位置の公開資料なし）

~~~diff
- 00bc2ea0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2ea0 ["INT_ADD", "register:40f0:8", ["const:bc2ea0:8", "const:4:8"]]
- 00bc2ea0 ["CALLIND", null, ["register:0:8"]]
+ 00bc2ee4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2ee4 ["INT_ADD", "register:40f0:8", ["const:bc2ee4:8", "const:4:8"]]
+ 00bc2ee4 ["CALLIND", null, ["register:0:8"]]
- 00bc2ea0 bytes 00013fd6
+ 00bc2ee4 bytes 00013fd6
~~~


<a id="compare-80fcf06e48637f1ea62ee185913c6dec"></a>

### [`00bc6ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md) → [`00bc6f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6f3c.md) FUN_00bc6f3c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc6f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md#insn-00bc6f6c) · [`00bc6f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md#insn-00bc6f90) · [`00bc6fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md#insn-00bc6fcc)
- 新版 `00bc6fb0`（命令位置の公開資料なし） · `00bc6fd4`（命令位置の公開資料なし） · `00bc7010`（命令位置の公開資料なし）

~~~diff
- 00bc6f6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc6f6c ["INT_ADD", "register:40f0:8", ["const:bc6f6c:8", "const:4:8"]]
- 00bc6f6c ["CALLIND", null, ["register:0:8"]]
+ 00bc6fb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc6fb0 ["INT_ADD", "register:40f0:8", ["const:bc6fb0:8", "const:4:8"]]
+ 00bc6fb0 ["CALLIND", null, ["register:0:8"]]
- 00bc6f6c bytes 00013fd6
+ 00bc6fb0 bytes 00013fd6
- 00bc6f90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc6f90 ["INT_ADD", "register:40f0:8", ["const:bc6f90:8", "const:4:8"]]
- 00bc6f90 ["CALLIND", null, ["register:0:8"]]
+ 00bc6fd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc6fd4 ["INT_ADD", "register:40f0:8", ["const:bc6fd4:8", "const:4:8"]]
+ 00bc6fd4 ["CALLIND", null, ["register:0:8"]]
- 00bc6f90 bytes 00013fd6
+ 00bc6fd4 bytes 00013fd6
- 00bc6fcc ["INT_ADD", "register:40f0:8", ["const:bc6fcc:8", "const:4:8"]]
- 00bc6fcc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc7010 ["INT_ADD", "register:40f0:8", ["const:bc7010:8", "const:4:8"]]
+ 00bc7010 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc6fcc bytes 8d580094
+ 00bc7010 bytes 90580094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ba4642afff5700e515e5942c8513a7"></a>

### [`00bc74cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md) → [`00bc7510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7510.md) FUN_00bc7510

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc751c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md#insn-00bc751c) · [`00bc7538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md#insn-00bc7538) · [`00bc7574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md#insn-00bc7574)
- 新版 `00bc7560`（命令位置の公開資料なし） · `00bc757c`（命令位置の公開資料なし） · `00bc75b8`（命令位置の公開資料なし）

~~~diff
- 00bc751c ["INT_ADD", "register:40f0:8", ["const:bc751c:8", "const:4:8"]]
- 00bc751c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc7560 ["INT_ADD", "register:40f0:8", ["const:bc7560:8", "const:4:8"]]
+ 00bc7560 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc751c bytes 39570094
+ 00bc7560 bytes 3c570094
- 00bc7538 ["INT_ADD", "register:40f0:8", ["const:bc7538:8", "const:4:8"]]
- 00bc7538 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bc757c ["INT_ADD", "register:40f0:8", ["const:bc757c:8", "const:4:8"]]
+ 00bc757c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bc7538 bytes 0a4f0094
+ 00bc757c bytes 0d4f0094
- 00bc7574 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7574 ["INT_ADD", "register:40f0:8", ["const:bc7574:8", "const:4:8"]]
- 00bc7574 ["CALLIND", null, ["register:0:8"]]
+ 00bc75b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc75b8 ["INT_ADD", "register:40f0:8", ["const:bc75b8:8", "const:4:8"]]
+ 00bc75b8 ["CALLIND", null, ["register:0:8"]]
- 00bc7574 bytes 00013fd6
+ 00bc75b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d586e6d7f02d3e3ed8be849ba50ee991"></a>

### [`00bc76b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md) → [`00bc76f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc76f8.md) FUN_00bc76f8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md#insn-00bc7700) · [`00bc7724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md#insn-00bc7724) · [`00bc7768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md#insn-00bc7768)
- 新版 `00bc7744`（命令位置の公開資料なし） · `00bc7768`（命令位置の公開資料なし） · `00bc77ac`（命令位置の公開資料なし）

~~~diff
- 00bc7700 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7700 ["INT_ADD", "register:40f0:8", ["const:bc7700:8", "const:4:8"]]
- 00bc7700 ["CALLIND", null, ["register:0:8"]]
+ 00bc7744 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7744 ["INT_ADD", "register:40f0:8", ["const:bc7744:8", "const:4:8"]]
+ 00bc7744 ["CALLIND", null, ["register:0:8"]]
- 00bc7700 bytes 00013fd6
+ 00bc7744 bytes 00013fd6
- 00bc7724 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7724 ["INT_ADD", "register:40f0:8", ["const:bc7724:8", "const:4:8"]]
- 00bc7724 ["CALLIND", null, ["register:0:8"]]
+ 00bc7768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7768 ["INT_ADD", "register:40f0:8", ["const:bc7768:8", "const:4:8"]]
+ 00bc7768 ["CALLIND", null, ["register:0:8"]]
- 00bc7724 bytes 00013fd6
+ 00bc7768 bytes 00013fd6
- 00bc7768 ["INT_ADD", "register:40f0:8", ["const:bc7768:8", "const:4:8"]]
- 00bc7768 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc77ac ["INT_ADD", "register:40f0:8", ["const:bc77ac:8", "const:4:8"]]
+ 00bc77ac ["CALL", null, ["callee:00bdd250:8"]]
- 00bc7768 bytes a6560094
+ 00bc77ac bytes a9560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8846c7977acc173903c6963ec4aa507d"></a>

### [`00bc789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md) → [`00bc78e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc78e0.md) FUN_00bc78e0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc78e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md#insn-00bc78e4) · [`00bc7908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md#insn-00bc7908) · [`00bc7944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md#insn-00bc7944)
- 新版 `00bc7928`（命令位置の公開資料なし） · `00bc794c`（命令位置の公開資料なし） · `00bc7988`（命令位置の公開資料なし）

~~~diff
- 00bc78e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc78e4 ["INT_ADD", "register:40f0:8", ["const:bc78e4:8", "const:4:8"]]
- 00bc78e4 ["CALLIND", null, ["register:0:8"]]
+ 00bc7928 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7928 ["INT_ADD", "register:40f0:8", ["const:bc7928:8", "const:4:8"]]
+ 00bc7928 ["CALLIND", null, ["register:0:8"]]
- 00bc78e4 bytes 00013fd6
+ 00bc7928 bytes 00013fd6
- 00bc7908 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7908 ["INT_ADD", "register:40f0:8", ["const:bc7908:8", "const:4:8"]]
- 00bc7908 ["CALLIND", null, ["register:0:8"]]
+ 00bc794c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc794c ["INT_ADD", "register:40f0:8", ["const:bc794c:8", "const:4:8"]]
+ 00bc794c ["CALLIND", null, ["register:0:8"]]
- 00bc7908 bytes 00013fd6
+ 00bc794c bytes 00013fd6
- 00bc7944 ["INT_ADD", "register:40f0:8", ["const:bc7944:8", "const:4:8"]]
- 00bc7944 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc7988 ["INT_ADD", "register:40f0:8", ["const:bc7988:8", "const:4:8"]]
+ 00bc7988 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc7944 bytes 2f560094
+ 00bc7988 bytes 32560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dabe1c3be6b7c86a462eebe5d5bcf550"></a>

### [`00bc7bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md) → [`00bc7c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7c40.md) FUN_00bc7c40

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md#insn-00bc7c48) · [`00bc7c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md#insn-00bc7c6c) · [`00bc7cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md#insn-00bc7cb0)
- 新版 `00bc7c8c`（命令位置の公開資料なし） · `00bc7cb0`（命令位置の公開資料なし） · `00bc7cf4`（命令位置の公開資料なし）

~~~diff
- 00bc7c48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7c48 ["INT_ADD", "register:40f0:8", ["const:bc7c48:8", "const:4:8"]]
- 00bc7c48 ["CALLIND", null, ["register:0:8"]]
+ 00bc7c8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7c8c ["INT_ADD", "register:40f0:8", ["const:bc7c8c:8", "const:4:8"]]
+ 00bc7c8c ["CALLIND", null, ["register:0:8"]]
- 00bc7c48 bytes 00013fd6
+ 00bc7c8c bytes 00013fd6
- 00bc7c6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7c6c ["INT_ADD", "register:40f0:8", ["const:bc7c6c:8", "const:4:8"]]
- 00bc7c6c ["CALLIND", null, ["register:0:8"]]
+ 00bc7cb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7cb0 ["INT_ADD", "register:40f0:8", ["const:bc7cb0:8", "const:4:8"]]
+ 00bc7cb0 ["CALLIND", null, ["register:0:8"]]
- 00bc7c6c bytes 00013fd6
+ 00bc7cb0 bytes 00013fd6
- 00bc7cb0 ["INT_ADD", "register:40f0:8", ["const:bc7cb0:8", "const:4:8"]]
- 00bc7cb0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc7cf4 ["INT_ADD", "register:40f0:8", ["const:bc7cf4:8", "const:4:8"]]
+ 00bc7cf4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc7cb0 bytes 54550094
+ 00bc7cf4 bytes 57550094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb047292827869fb13ab7a6649d6e967"></a>

### [`00bc7f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md) → [`00bc7f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7f74.md) FUN_00bc7f74

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md#insn-00bc7f80) · [`00bc7fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md#insn-00bc7fcc) · [`00bc802c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md#insn-00bc802c)
- 新版 `00bc7fc4`（命令位置の公開資料なし） · `00bc8010`（命令位置の公開資料なし） · `00bc8070`（命令位置の公開資料なし）

~~~diff
- 00bc7f80 ["INT_ADD", "register:40f0:8", ["const:bc7f80:8", "const:4:8"]]
- 00bc7f80 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc7fc4 ["INT_ADD", "register:40f0:8", ["const:bc7fc4:8", "const:4:8"]]
+ 00bc7fc4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc7f80 bytes a0540094
+ 00bc7fc4 bytes a3540094
- 00bc7fcc ["INT_ADD", "register:40f0:8", ["const:bc7fcc:8", "const:4:8"]]
- 00bc7fcc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8010 ["INT_ADD", "register:40f0:8", ["const:bc8010:8", "const:4:8"]]
+ 00bc8010 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc7fcc bytes 8d540094
+ 00bc8010 bytes 90540094
- 00bc802c ["INT_ADD", "register:40f0:8", ["const:bc802c:8", "const:4:8"]]
- 00bc802c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8070 ["INT_ADD", "register:40f0:8", ["const:bc8070:8", "const:4:8"]]
+ 00bc8070 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc802c bytes 75540094
+ 00bc8070 bytes 78540094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-217acd29dc1a981815c9666cad6c8171"></a>

### [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) → [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) FUN_00bc82d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`00bc7f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md) [`00bc8698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md) [`00bc87c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md) [`00bcbbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md) [`00bcc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md) · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 15件 [`00bc7f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7f74.md) [`00bc86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc86dc.md) [`00bc8808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8808.md) [`00bcbc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md) [`00bcc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md) · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md#insn-00bc8320) · [`00bc8370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md#insn-00bc8370) · [`00bc8394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md#insn-00bc8394)
- 新版 `00bc8364`（命令位置の公開資料なし） · `00bc83b4`（命令位置の公開資料なし） · `00bc83d8`（命令位置の公開資料なし）

~~~diff
- 00bc8320 ["INT_ADD", "register:40f0:8", ["const:bc8320:8", "const:4:8"]]
- 00bc8320 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8364 ["INT_ADD", "register:40f0:8", ["const:bc8364:8", "const:4:8"]]
+ 00bc8364 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc8320 bytes b8530094
+ 00bc8364 bytes bb530094
- 00bc8370 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8370 ["INT_ADD", "register:40f0:8", ["const:bc8370:8", "const:4:8"]]
- 00bc8370 ["CALLIND", null, ["register:0:8"]]
+ 00bc83b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc83b4 ["INT_ADD", "register:40f0:8", ["const:bc83b4:8", "const:4:8"]]
+ 00bc83b4 ["CALLIND", null, ["register:0:8"]]
- 00bc8370 bytes 00013fd6
+ 00bc83b4 bytes 00013fd6
- 00bc8394 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8394 ["INT_ADD", "register:40f0:8", ["const:bc8394:8", "const:4:8"]]
- 00bc8394 ["CALLIND", null, ["register:0:8"]]
+ 00bc83d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc83d8 ["INT_ADD", "register:40f0:8", ["const:bc83d8:8", "const:4:8"]]
+ 00bc83d8 ["CALLIND", null, ["register:0:8"]]
- 00bc8394 bytes 00013fd6
+ 00bc83d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cc54cf629fe621485d9723e822e18e6"></a>

### [`00bc84c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md) → [`00bc8504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8504.md) FUN_00bc8504

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc850c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md#insn-00bc850c) · [`00bc8558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md#insn-00bc8558) · [`00bc85bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md#insn-00bc85bc)
- 新版 `00bc8550`（命令位置の公開資料なし） · `00bc859c`（命令位置の公開資料なし） · `00bc8600`（命令位置の公開資料なし）

~~~diff
- 00bc850c ["INT_ADD", "register:40f0:8", ["const:bc850c:8", "const:4:8"]]
- 00bc850c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8550 ["INT_ADD", "register:40f0:8", ["const:bc8550:8", "const:4:8"]]
+ 00bc8550 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc850c bytes 3d530094
+ 00bc8550 bytes 40530094
- 00bc8558 ["INT_ADD", "register:40f0:8", ["const:bc8558:8", "const:4:8"]]
- 00bc8558 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc859c ["INT_ADD", "register:40f0:8", ["const:bc859c:8", "const:4:8"]]
+ 00bc859c ["CALL", null, ["callee:00bdd250:8"]]
- 00bc8558 bytes 2a530094
+ 00bc859c bytes 2d530094
- 00bc85bc ["INT_ADD", "register:40f0:8", ["const:bc85bc:8", "const:4:8"]]
- 00bc85bc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8600 ["INT_ADD", "register:40f0:8", ["const:bc8600:8", "const:4:8"]]
+ 00bc8600 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc85bc bytes 11530094
+ 00bc8600 bytes 14530094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f09c0f529cd2271d5967c53fea4f97"></a>

### [`00bc8698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md) → [`00bc86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc86dc.md) FUN_00bc86dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc86c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md#insn-00bc86c4) · [`00bc86e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md#insn-00bc86e8) · [`00bc8720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md#insn-00bc8720)
- 新版 `00bc8708`（命令位置の公開資料なし） · `00bc872c`（命令位置の公開資料なし） · `00bc8764`（命令位置の公開資料なし）

~~~diff
- 00bc86c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc86c4 ["INT_ADD", "register:40f0:8", ["const:bc86c4:8", "const:4:8"]]
- 00bc86c4 ["CALLIND", null, ["register:0:8"]]
+ 00bc8708 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc8708 ["INT_ADD", "register:40f0:8", ["const:bc8708:8", "const:4:8"]]
+ 00bc8708 ["CALLIND", null, ["register:0:8"]]
- 00bc86c4 bytes 00013fd6
+ 00bc8708 bytes 00013fd6
- 00bc86e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc86e8 ["INT_ADD", "register:40f0:8", ["const:bc86e8:8", "const:4:8"]]
- 00bc86e8 ["CALLIND", null, ["register:0:8"]]
+ 00bc872c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc872c ["INT_ADD", "register:40f0:8", ["const:bc872c:8", "const:4:8"]]
+ 00bc872c ["CALLIND", null, ["register:0:8"]]
- 00bc86e8 bytes 00013fd6
+ 00bc872c bytes 00013fd6
- 00bc8720 ["INT_ADD", "register:40f0:8", ["const:bc8720:8", "const:4:8"]]
- 00bc8720 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8764 ["INT_ADD", "register:40f0:8", ["const:bc8764:8", "const:4:8"]]
+ 00bc8764 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc8720 bytes b8520094
+ 00bc8764 bytes bb520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c7826f858f4f3db735f677476a60040"></a>

### [`00bc87c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md) → [`00bc8808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8808.md) FUN_00bc8808

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md#insn-00bc8814) · [`00bc8848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md#insn-00bc8848) · [`00bc886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md#insn-00bc886c)
- 新版 `00bc8858`（命令位置の公開資料なし） · `00bc888c`（命令位置の公開資料なし） · `00bc88b0`（命令位置の公開資料なし）

~~~diff
- 00bc8814 ["INT_ADD", "register:40f0:8", ["const:bc8814:8", "const:4:8"]]
- 00bc8814 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8858 ["INT_ADD", "register:40f0:8", ["const:bc8858:8", "const:4:8"]]
+ 00bc8858 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc8814 bytes 7b520094
+ 00bc8858 bytes 7e520094
- 00bc8848 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8848 ["INT_ADD", "register:40f0:8", ["const:bc8848:8", "const:4:8"]]
- 00bc8848 ["CALLIND", null, ["register:0:8"]]
+ 00bc888c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc888c ["INT_ADD", "register:40f0:8", ["const:bc888c:8", "const:4:8"]]
+ 00bc888c ["CALLIND", null, ["register:0:8"]]
- 00bc8848 bytes 00013fd6
+ 00bc888c bytes 00013fd6
- 00bc886c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc886c ["INT_ADD", "register:40f0:8", ["const:bc886c:8", "const:4:8"]]
- 00bc886c ["CALLIND", null, ["register:0:8"]]
+ 00bc88b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc88b0 ["INT_ADD", "register:40f0:8", ["const:bc88b0:8", "const:4:8"]]
+ 00bc88b0 ["CALLIND", null, ["register:0:8"]]
- 00bc886c bytes 00013fd6
+ 00bc88b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa75702dfaa6350ba658d8b584fa3f7a"></a>

### [`00bc89a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md) → [`00bc89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc89e8.md) FUN_00bc89e8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc89ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md#insn-00bc89ec) · [`00bc8a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md#insn-00bc8a10) · [`00bc8a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md#insn-00bc8a4c)
- 新版 `00bc8a30`（命令位置の公開資料なし） · `00bc8a54`（命令位置の公開資料なし） · `00bc8a90`（命令位置の公開資料なし）

~~~diff
- 00bc89ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc89ec ["INT_ADD", "register:40f0:8", ["const:bc89ec:8", "const:4:8"]]
- 00bc89ec ["CALLIND", null, ["register:0:8"]]
+ 00bc8a30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc8a30 ["INT_ADD", "register:40f0:8", ["const:bc8a30:8", "const:4:8"]]
+ 00bc8a30 ["CALLIND", null, ["register:0:8"]]
- 00bc89ec bytes 00013fd6
+ 00bc8a30 bytes 00013fd6
- 00bc8a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8a10 ["INT_ADD", "register:40f0:8", ["const:bc8a10:8", "const:4:8"]]
- 00bc8a10 ["CALLIND", null, ["register:0:8"]]
+ 00bc8a54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc8a54 ["INT_ADD", "register:40f0:8", ["const:bc8a54:8", "const:4:8"]]
+ 00bc8a54 ["CALLIND", null, ["register:0:8"]]
- 00bc8a10 bytes 00013fd6
+ 00bc8a54 bytes 00013fd6
- 00bc8a4c ["INT_ADD", "register:40f0:8", ["const:bc8a4c:8", "const:4:8"]]
- 00bc8a4c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8a90 ["INT_ADD", "register:40f0:8", ["const:bc8a90:8", "const:4:8"]]
+ 00bc8a90 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc8a4c bytes ed510094
+ 00bc8a90 bytes f0510094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b67d29375cc61138df8475875321c766"></a>

### [`00bc8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md) → [`00bc8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8e94.md) FUN_00bc8e94

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md#insn-00bc8ea4) · [`00bc8ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md#insn-00bc8ec0) · [`00bc8f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md#insn-00bc8f00)
- 新版 `00bc8ee8`（命令位置の公開資料なし） · `00bc8f04`（命令位置の公開資料なし） · `00bc8f44`（命令位置の公開資料なし）

~~~diff
- 00bc8ea4 ["INT_ADD", "register:40f0:8", ["const:bc8ea4:8", "const:4:8"]]
- 00bc8ea4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8ee8 ["INT_ADD", "register:40f0:8", ["const:bc8ee8:8", "const:4:8"]]
+ 00bc8ee8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc8ea4 bytes d7500094
+ 00bc8ee8 bytes da500094
- 00bc8ec0 ["INT_ADD", "register:40f0:8", ["const:bc8ec0:8", "const:4:8"]]
- 00bc8ec0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bc8f04 ["INT_ADD", "register:40f0:8", ["const:bc8f04:8", "const:4:8"]]
+ 00bc8f04 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bc8ec0 bytes a8480094
+ 00bc8f04 bytes ab480094
- 00bc8f00 ["INT_ADD", "register:40f0:8", ["const:bc8f00:8", "const:4:8"]]
- 00bc8f00 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc8f44 ["INT_ADD", "register:40f0:8", ["const:bc8f44:8", "const:4:8"]]
+ 00bc8f44 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc8f00 bytes c0500094
+ 00bc8f44 bytes c3500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588edaabb5ee5e603e458b39ed6d8eb4"></a>

### [`00bc9194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md) → [`00bc91d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc91d8.md) FUN_00bc91d8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc91e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md#insn-00bc91e8) · [`00bc9204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md#insn-00bc9204) · [`00bc9248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md#insn-00bc9248)
- 新版 `00bc922c`（命令位置の公開資料なし） · `00bc9248`（命令位置の公開資料なし） · `00bc928c`（命令位置の公開資料なし）

~~~diff
- 00bc91e8 ["INT_ADD", "register:40f0:8", ["const:bc91e8:8", "const:4:8"]]
- 00bc91e8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc922c ["INT_ADD", "register:40f0:8", ["const:bc922c:8", "const:4:8"]]
+ 00bc922c ["CALL", null, ["callee:00bdd250:8"]]
- 00bc91e8 bytes 06500094
+ 00bc922c bytes 09500094
- 00bc9204 ["INT_ADD", "register:40f0:8", ["const:bc9204:8", "const:4:8"]]
- 00bc9204 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bc9248 ["INT_ADD", "register:40f0:8", ["const:bc9248:8", "const:4:8"]]
+ 00bc9248 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bc9204 bytes d7470094
+ 00bc9248 bytes da470094
- 00bc9248 ["INT_ADD", "register:40f0:8", ["const:bc9248:8", "const:4:8"]]
- 00bc9248 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc928c ["INT_ADD", "register:40f0:8", ["const:bc928c:8", "const:4:8"]]
+ 00bc928c ["CALL", null, ["callee:00bdd250:8"]]
- 00bc9248 bytes ee4f0094
+ 00bc928c bytes f14f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcf9cde6759dd3ae90e8a9d3b2acabcf"></a>

### [`00bc9f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md) → [`00bc9f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9f7c.md) FUN_00bc9f7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md#insn-00bc9f98) · [`00bc9ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md#insn-00bc9ff0) · [`00bca00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md#insn-00bca00c)
- 新版 `00bc9fdc`（命令位置の公開資料なし） · `00bca034`（命令位置の公開資料なし） · `00bca050`（命令位置の公開資料なし）

~~~diff
- 00bc9f98 ["INT_ADD", "register:40f0:8", ["const:bc9f98:8", "const:4:8"]]
- 00bc9f98 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc9fdc ["INT_ADD", "register:40f0:8", ["const:bc9fdc:8", "const:4:8"]]
+ 00bc9fdc ["CALL", null, ["callee:00bdd250:8"]]
- 00bc9f98 bytes 9a4c0094
+ 00bc9fdc bytes 9d4c0094
- 00bc9ff0 ["INT_ADD", "register:40f0:8", ["const:bc9ff0:8", "const:4:8"]]
- 00bc9ff0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bca034 ["INT_ADD", "register:40f0:8", ["const:bca034:8", "const:4:8"]]
+ 00bca034 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc9ff0 bytes 844c0094
+ 00bca034 bytes 874c0094
- 00bca00c ["INT_ADD", "register:40f0:8", ["const:bca00c:8", "const:4:8"]]
- 00bca00c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bca050 ["INT_ADD", "register:40f0:8", ["const:bca050:8", "const:4:8"]]
+ 00bca050 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bca00c bytes 55440094
+ 00bca050 bytes 58440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-225cb4e78c0e8c3d360f635a545c273c"></a>

### [`00bca86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md) → [`00bca8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca8b0.md) FUN_00bca8b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md#insn-00bca8b0) · [`00bca8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md#insn-00bca8ec) · [`00bca910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md#insn-00bca910)
- 新版 `00bca8f4`（命令位置の公開資料なし） · `00bca930`（命令位置の公開資料なし） · `00bca954`（命令位置の公開資料なし）

~~~diff
- 00bca8b0 ["INT_ADD", "register:40f0:8", ["const:bca8b0:8", "const:4:8"]]
- 00bca8b0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bca8f4 ["INT_ADD", "register:40f0:8", ["const:bca8f4:8", "const:4:8"]]
+ 00bca8f4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bca8b0 bytes 544a0094
+ 00bca8f4 bytes 574a0094
- 00bca8ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca8ec ["INT_ADD", "register:40f0:8", ["const:bca8ec:8", "const:4:8"]]
- 00bca8ec ["CALLIND", null, ["register:0:8"]]
+ 00bca930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca930 ["INT_ADD", "register:40f0:8", ["const:bca930:8", "const:4:8"]]
+ 00bca930 ["CALLIND", null, ["register:0:8"]]
- 00bca8ec bytes 00013fd6
+ 00bca930 bytes 00013fd6
- 00bca910 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca910 ["INT_ADD", "register:40f0:8", ["const:bca910:8", "const:4:8"]]
- 00bca910 ["CALLIND", null, ["register:0:8"]]
+ 00bca954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca954 ["INT_ADD", "register:40f0:8", ["const:bca954:8", "const:4:8"]]
+ 00bca954 ["CALLIND", null, ["register:0:8"]]
- 00bca910 bytes 00013fd6
+ 00bca954 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c01872392182a5d48405c334652f1dbe"></a>

### [`00bcb448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md) → [`00bcb48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb48c.md) FUN_00bcb48c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md#insn-00bcb490) · [`00bcb4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md#insn-00bcb4f8) · [`00bcb514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md#insn-00bcb514)
- 新版 `00bcb4d4`（命令位置の公開資料なし） · `00bcb53c`（命令位置の公開資料なし） · `00bcb558`（命令位置の公開資料なし）

~~~diff
- 00bcb490 ["INT_ADD", "register:40f0:8", ["const:bcb490:8", "const:4:8"]]
- 00bcb490 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcb4d4 ["INT_ADD", "register:40f0:8", ["const:bcb4d4:8", "const:4:8"]]
+ 00bcb4d4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcb490 bytes 5c470094
+ 00bcb4d4 bytes 5f470094
- 00bcb4f8 ["INT_ADD", "register:40f0:8", ["const:bcb4f8:8", "const:4:8"]]
- 00bcb4f8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcb53c ["INT_ADD", "register:40f0:8", ["const:bcb53c:8", "const:4:8"]]
+ 00bcb53c ["CALL", null, ["callee:00bdd250:8"]]
- 00bcb4f8 bytes 42470094
+ 00bcb53c bytes 45470094
- 00bcb514 ["INT_ADD", "register:40f0:8", ["const:bcb514:8", "const:4:8"]]
- 00bcb514 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bcb558 ["INT_ADD", "register:40f0:8", ["const:bcb558:8", "const:4:8"]]
+ 00bcb558 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bcb514 bytes 133f0094
+ 00bcb558 bytes 163f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47cf6a87d12a4053c9f83c9a3becede3"></a>

### [`00bcb638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md) → [`00bcb67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb67c.md) FUN_00bcb67c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md#insn-00bcb6a4) · [`00bcb6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md#insn-00bcb6fc) · [`00bcb75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md#insn-00bcb75c)
- 新版 `00bcb6e8`（命令位置の公開資料なし） · `00bcb740`（命令位置の公開資料なし） · `00bcb7a0`（命令位置の公開資料なし）

~~~diff
- 00bcb6a4 ["INT_ADD", "register:40f0:8", ["const:bcb6a4:8", "const:4:8"]]
- 00bcb6a4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcb6e8 ["INT_ADD", "register:40f0:8", ["const:bcb6e8:8", "const:4:8"]]
+ 00bcb6e8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcb6a4 bytes d7460094
+ 00bcb6e8 bytes da460094
- 00bcb6fc ["INT_ADD", "register:40f0:8", ["const:bcb6fc:8", "const:4:8"]]
- 00bcb6fc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcb740 ["INT_ADD", "register:40f0:8", ["const:bcb740:8", "const:4:8"]]
+ 00bcb740 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcb6fc bytes c1460094
+ 00bcb740 bytes c4460094
- 00bcb75c ["INT_ADD", "register:40f0:8", ["const:bcb75c:8", "const:4:8"]]
- 00bcb75c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcb7a0 ["INT_ADD", "register:40f0:8", ["const:bcb7a0:8", "const:4:8"]]
+ 00bcb7a0 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcb75c bytes a9460094
+ 00bcb7a0 bytes ac460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e2c3d403e90302068a476255c5838a9"></a>

### [`00bcb8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb8f4.md) → [`00bcb938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb938.md) FUN_00bcb938

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb8f4.md#insn-00bcb918)
- 新版 `00bcb95c`（命令位置の公開資料なし）

~~~diff
- 00bcb918 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb918 ["INT_ADD", "register:40f0:8", ["const:bcb918:8", "const:4:8"]]
- 00bcb918 ["CALLIND", null, ["register:0:8"]]
+ 00bcb95c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb95c ["INT_ADD", "register:40f0:8", ["const:bcb95c:8", "const:4:8"]]
+ 00bcb95c ["CALLIND", null, ["register:0:8"]]
- 00bcb918 bytes 00013fd6
+ 00bcb95c bytes 00013fd6
~~~


<a id="compare-48a4e2491a764fd96ac0efe47cc4abe3"></a>

### [`00bcb964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md) → [`00bcb9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb9a8.md) FUN_00bcb9a8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md#insn-00bcb988) · [`00bcb9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md#insn-00bcb9ac) · [`00bcb9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md#insn-00bcb9d8)
- 新版 `00bcb9cc`（命令位置の公開資料なし） · `00bcb9f0`（命令位置の公開資料なし） · `00bcba1c`（命令位置の公開資料なし）

~~~diff
- 00bcb988 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb988 ["INT_ADD", "register:40f0:8", ["const:bcb988:8", "const:4:8"]]
- 00bcb988 ["CALLIND", null, ["register:0:8"]]
+ 00bcb9cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb9cc ["INT_ADD", "register:40f0:8", ["const:bcb9cc:8", "const:4:8"]]
+ 00bcb9cc ["CALLIND", null, ["register:0:8"]]
- 00bcb988 bytes 00013fd6
+ 00bcb9cc bytes 00013fd6
- 00bcb9ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb9ac ["INT_ADD", "register:40f0:8", ["const:bcb9ac:8", "const:4:8"]]
- 00bcb9ac ["CALLIND", null, ["register:0:8"]]
+ 00bcb9f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb9f0 ["INT_ADD", "register:40f0:8", ["const:bcb9f0:8", "const:4:8"]]
+ 00bcb9f0 ["CALLIND", null, ["register:0:8"]]
- 00bcb9ac bytes 00013fd6
+ 00bcb9f0 bytes 00013fd6
- 00bcb9d8 ["INT_ADD", "register:40f0:8", ["const:bcb9d8:8", "const:4:8"]]
- 00bcb9d8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcba1c ["INT_ADD", "register:40f0:8", ["const:bcba1c:8", "const:4:8"]]
+ 00bcba1c ["CALL", null, ["callee:00bdd250:8"]]
- 00bcb9d8 bytes 0a460094
+ 00bcba1c bytes 0d460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33bf2d4b3a0e884273f29ef4a3749818"></a>

### [`00bcba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md) → [`00bcbac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbac4.md) FUN_00bcbac4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md#insn-00bcbaa4) · [`00bcbac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md#insn-00bcbac8) · [`00bcbb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md#insn-00bcbb04)
- 新版 `00bcbae8`（命令位置の公開資料なし） · `00bcbb0c`（命令位置の公開資料なし） · `00bcbb48`（命令位置の公開資料なし）

~~~diff
- 00bcbaa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbaa4 ["INT_ADD", "register:40f0:8", ["const:bcbaa4:8", "const:4:8"]]
- 00bcbaa4 ["CALLIND", null, ["register:0:8"]]
+ 00bcbae8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbae8 ["INT_ADD", "register:40f0:8", ["const:bcbae8:8", "const:4:8"]]
+ 00bcbae8 ["CALLIND", null, ["register:0:8"]]
- 00bcbaa4 bytes 00013fd6
+ 00bcbae8 bytes 00013fd6
- 00bcbac8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbac8 ["INT_ADD", "register:40f0:8", ["const:bcbac8:8", "const:4:8"]]
- 00bcbac8 ["CALLIND", null, ["register:0:8"]]
+ 00bcbb0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbb0c ["INT_ADD", "register:40f0:8", ["const:bcbb0c:8", "const:4:8"]]
+ 00bcbb0c ["CALLIND", null, ["register:0:8"]]
- 00bcbac8 bytes 00013fd6
+ 00bcbb0c bytes 00013fd6
- 00bcbb04 ["INT_ADD", "register:40f0:8", ["const:bcbb04:8", "const:4:8"]]
- 00bcbb04 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcbb48 ["INT_ADD", "register:40f0:8", ["const:bcbb48:8", "const:4:8"]]
+ 00bcbb48 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcbb04 bytes bf450094
+ 00bcbb48 bytes c2450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-231c8ba42800035a662f1cd5fe703ded"></a>

### [`00bcbb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbb3c.md) → [`00bcbb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbb80.md) FUN_00bcbb80

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbb68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbb3c.md#insn-00bcbb68) · [`00bcbb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbb3c.md#insn-00bcbb8c)
- 新版 `00bcbbac`（命令位置の公開資料なし） · `00bcbbd0`（命令位置の公開資料なし）

~~~diff
- 00bcbb68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbb68 ["INT_ADD", "register:40f0:8", ["const:bcbb68:8", "const:4:8"]]
- 00bcbb68 ["CALLIND", null, ["register:0:8"]]
+ 00bcbbac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbbac ["INT_ADD", "register:40f0:8", ["const:bcbbac:8", "const:4:8"]]
+ 00bcbbac ["CALLIND", null, ["register:0:8"]]
- 00bcbb68 bytes 00013fd6
+ 00bcbbac bytes 00013fd6
- 00bcbb8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbb8c ["INT_ADD", "register:40f0:8", ["const:bcbb8c:8", "const:4:8"]]
- 00bcbb8c ["CALLIND", null, ["register:0:8"]]
+ 00bcbbd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbbd0 ["INT_ADD", "register:40f0:8", ["const:bcbbd0:8", "const:4:8"]]
+ 00bcbbd0 ["CALLIND", null, ["register:0:8"]]
- 00bcbb8c bytes 00013fd6
+ 00bcbbd0 bytes 00013fd6
~~~


<a id="compare-1d6ec591c1728ec37e0e7bae3570a175"></a>

### [`00bcbe00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md) → [`00bcbe44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbe44.md) FUN_00bcbe44

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbe20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md#insn-00bcbe20) · [`00bcbe4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md#insn-00bcbe4c) · [`00bcbe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md#insn-00bcbe8c)
- 新版 `00bcbe64`（命令位置の公開資料なし） · `00bcbe90`（命令位置の公開資料なし） · `00bcbed0`（命令位置の公開資料なし）

~~~diff
- 00bcbe20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbe20 ["INT_ADD", "register:40f0:8", ["const:bcbe20:8", "const:4:8"]]
- 00bcbe20 ["CALLIND", null, ["register:0:8"]]
+ 00bcbe64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbe64 ["INT_ADD", "register:40f0:8", ["const:bcbe64:8", "const:4:8"]]
+ 00bcbe64 ["CALLIND", null, ["register:0:8"]]
- 00bcbe20 bytes 00013fd6
+ 00bcbe64 bytes 00013fd6
- 00bcbe4c ["INT_ADD", "register:40f0:8", ["const:bcbe4c:8", "const:4:8"]]
- 00bcbe4c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcbe90 ["INT_ADD", "register:40f0:8", ["const:bcbe90:8", "const:4:8"]]
+ 00bcbe90 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcbe4c bytes ed440094
+ 00bcbe90 bytes f0440094
- 00bcbe8c ["INT_ADD", "register:40f0:8", ["const:bcbe8c:8", "const:4:8"]]
- 00bcbe8c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bcbed0 ["INT_ADD", "register:40f0:8", ["const:bcbed0:8", "const:4:8"]]
+ 00bcbed0 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bcbe8c bytes f9480094
+ 00bcbed0 bytes fc480094
~~~


<a id="compare-c6fb1769378b687d10e77bf825bafc53"></a>

### [`00bcbeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md) → [`00bcbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbef0.md) FUN_00bcbef0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bcc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bcc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md#insn-00bcbef4) · [`00bcbf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md#insn-00bcbf64) · [`00bcbf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md#insn-00bcbf80)
- 新版 `00bcbf38`（命令位置の公開資料なし） · `00bcbfa8`（命令位置の公開資料なし） · `00bcbfc4`（命令位置の公開資料なし）

~~~diff
- 00bcbef4 ["INT_ADD", "register:40f0:8", ["const:bcbef4:8", "const:4:8"]]
- 00bcbef4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcbf38 ["INT_ADD", "register:40f0:8", ["const:bcbf38:8", "const:4:8"]]
+ 00bcbf38 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcbef4 bytes c3440094
+ 00bcbf38 bytes c6440094
- 00bcbf64 ["INT_ADD", "register:40f0:8", ["const:bcbf64:8", "const:4:8"]]
- 00bcbf64 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcbfa8 ["INT_ADD", "register:40f0:8", ["const:bcbfa8:8", "const:4:8"]]
+ 00bcbfa8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcbf64 bytes a7440094
+ 00bcbfa8 bytes aa440094
- 00bcbf80 ["INT_ADD", "register:40f0:8", ["const:bcbf80:8", "const:4:8"]]
- 00bcbf80 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bcbfc4 ["INT_ADD", "register:40f0:8", ["const:bcbfc4:8", "const:4:8"]]
+ 00bcbfc4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bcbf80 bytes 783c0094
+ 00bcbfc4 bytes 7b3c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3b425a2a5e93acdae42e7378fdf125f"></a>

### [`00bcc36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md) → [`00bcc3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc3b0.md) FUN_00bcc3b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bcc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bcc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md#insn-00bcc3b0) · [`00bcc3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md#insn-00bcc3ec) · [`00bcc41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md#insn-00bcc41c)
- 新版 `00bcc3f4`（命令位置の公開資料なし） · `00bcc430`（命令位置の公開資料なし） · `00bcc460`（命令位置の公開資料なし）

~~~diff
- 00bcc3b0 ["INT_ADD", "register:40f0:8", ["const:bcc3b0:8", "const:4:8"]]
- 00bcc3b0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcc3f4 ["INT_ADD", "register:40f0:8", ["const:bcc3f4:8", "const:4:8"]]
+ 00bcc3f4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcc3b0 bytes 94430094
+ 00bcc3f4 bytes 97430094
- 00bcc3ec ["INT_ADD", "register:40f0:8", ["const:bcc3ec:8", "const:4:8"]]
- 00bcc3ec ["CALL", null, ["callee:00bcc050:8"]]
+ 00bcc430 ["INT_ADD", "register:40f0:8", ["const:bcc430:8", "const:4:8"]]
+ 00bcc430 ["CALL", null, ["callee:00bcc050:8"]]
- 00bcc3ec bytes 08ffff97
+ 00bcc430 bytes 08ffff97
- 00bcc41c ["INT_ADD", "register:40f0:8", ["const:bcc41c:8", "const:4:8"]]
- 00bcc41c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcc460 ["INT_ADD", "register:40f0:8", ["const:bcc460:8", "const:4:8"]]
+ 00bcc460 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcc41c bytes 79430094
+ 00bcc460 bytes 7c430094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f83d745663fe78b70faf2c6db2929d"></a>

### [`00bcc470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md) → [`00bcc4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc4b4.md) FUN_00bcc4b4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md#insn-00bcc4c0) · [`00bcc4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md#insn-00bcc4f4) · [`00bcc518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md#insn-00bcc518)
- 新版 `00bcc504`（命令位置の公開資料なし） · `00bcc538`（命令位置の公開資料なし） · `00bcc55c`（命令位置の公開資料なし）

~~~diff
- 00bcc4c0 ["INT_ADD", "register:40f0:8", ["const:bcc4c0:8", "const:4:8"]]
- 00bcc4c0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcc504 ["INT_ADD", "register:40f0:8", ["const:bcc504:8", "const:4:8"]]
+ 00bcc504 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcc4c0 bytes 50430094
+ 00bcc504 bytes 53430094
- 00bcc4f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc4f4 ["INT_ADD", "register:40f0:8", ["const:bcc4f4:8", "const:4:8"]]
- 00bcc4f4 ["CALLIND", null, ["register:0:8"]]
+ 00bcc538 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc538 ["INT_ADD", "register:40f0:8", ["const:bcc538:8", "const:4:8"]]
+ 00bcc538 ["CALLIND", null, ["register:0:8"]]
- 00bcc4f4 bytes 00013fd6
+ 00bcc538 bytes 00013fd6
- 00bcc518 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc518 ["INT_ADD", "register:40f0:8", ["const:bcc518:8", "const:4:8"]]
- 00bcc518 ["CALLIND", null, ["register:0:8"]]
+ 00bcc55c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc55c ["INT_ADD", "register:40f0:8", ["const:bcc55c:8", "const:4:8"]]
+ 00bcc55c ["CALLIND", null, ["register:0:8"]]
- 00bcc518 bytes 00013fd6
+ 00bcc55c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97d1f7bb81607e5d13f06d2e9aa96103"></a>

### [`00bcc748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md) → [`00bcc78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc78c.md) FUN_00bcc78c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md#insn-00bcc790) · [`00bcc7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md#insn-00bcc7ec) · [`00bcc808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md#insn-00bcc808)
- 新版 `00bcc7d4`（命令位置の公開資料なし） · `00bcc830`（命令位置の公開資料なし） · `00bcc84c`（命令位置の公開資料なし）

~~~diff
- 00bcc790 ["INT_ADD", "register:40f0:8", ["const:bcc790:8", "const:4:8"]]
- 00bcc790 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcc7d4 ["INT_ADD", "register:40f0:8", ["const:bcc7d4:8", "const:4:8"]]
+ 00bcc7d4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcc790 bytes 9c420094
+ 00bcc7d4 bytes 9f420094
- 00bcc7ec ["INT_ADD", "register:40f0:8", ["const:bcc7ec:8", "const:4:8"]]
- 00bcc7ec ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcc830 ["INT_ADD", "register:40f0:8", ["const:bcc830:8", "const:4:8"]]
+ 00bcc830 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcc7ec bytes 85420094
+ 00bcc830 bytes 88420094
- 00bcc808 ["INT_ADD", "register:40f0:8", ["const:bcc808:8", "const:4:8"]]
- 00bcc808 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00bcc84c ["INT_ADD", "register:40f0:8", ["const:bcc84c:8", "const:4:8"]]
+ 00bcc84c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00bcc808 bytes 563a0094
+ 00bcc84c bytes 593a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eecc5068ccab37e9af33cd31bfcfa83"></a>

### [`00bccfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md) → [`00bcd004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md) FUN_00bcd004

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bcc83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc83c.md) [`00bce500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce500.md) · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 2件 [`00bcc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md) [`00bce544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md) · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md#insn-00bcd004) · [`00bcd028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md#insn-00bcd028) · [`00bcd084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md#insn-00bcd084)
- 新版 `00bcd048`（命令位置の公開資料なし） · `00bcd06c`（命令位置の公開資料なし） · `00bcd0c8`（命令位置の公開資料なし）

~~~diff
- 00bcd004 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd004 ["INT_ADD", "register:40f0:8", ["const:bcd004:8", "const:4:8"]]
- 00bcd004 ["CALLIND", null, ["register:0:8"]]
+ 00bcd048 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd048 ["INT_ADD", "register:40f0:8", ["const:bcd048:8", "const:4:8"]]
+ 00bcd048 ["CALLIND", null, ["register:0:8"]]
- 00bcd004 bytes 00013fd6
+ 00bcd048 bytes 00013fd6
- 00bcd028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd028 ["INT_ADD", "register:40f0:8", ["const:bcd028:8", "const:4:8"]]
- 00bcd028 ["CALLIND", null, ["register:0:8"]]
+ 00bcd06c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd06c ["INT_ADD", "register:40f0:8", ["const:bcd06c:8", "const:4:8"]]
+ 00bcd06c ["CALLIND", null, ["register:0:8"]]
- 00bcd028 bytes 00013fd6
+ 00bcd06c bytes 00013fd6
- 00bcd084 ["INT_ADD", "register:40f0:8", ["const:bcd084:8", "const:4:8"]]
- 00bcd084 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcd0c8 ["INT_ADD", "register:40f0:8", ["const:bcd0c8:8", "const:4:8"]]
+ 00bcd0c8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcd084 bytes 5f400094
+ 00bcd0c8 bytes 62400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e05304972ddc35019bd310fbc85f9cd"></a>

### [`00bcd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md) → [`00bcd1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd1c4.md) FUN_00bcd1c4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md#insn-00bcd1cc) · [`00bcd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md#insn-00bcd200) · [`00bcd224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md#insn-00bcd224)
- 新版 `00bcd210`（命令位置の公開資料なし） · `00bcd244`（命令位置の公開資料なし） · `00bcd268`（命令位置の公開資料なし）

~~~diff
- 00bcd1cc ["INT_ADD", "register:40f0:8", ["const:bcd1cc:8", "const:4:8"]]
- 00bcd1cc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcd210 ["INT_ADD", "register:40f0:8", ["const:bcd210:8", "const:4:8"]]
+ 00bcd210 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcd1cc bytes 0d400094
+ 00bcd210 bytes 10400094
- 00bcd200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd200 ["INT_ADD", "register:40f0:8", ["const:bcd200:8", "const:4:8"]]
- 00bcd200 ["CALLIND", null, ["register:0:8"]]
+ 00bcd244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd244 ["INT_ADD", "register:40f0:8", ["const:bcd244:8", "const:4:8"]]
+ 00bcd244 ["CALLIND", null, ["register:0:8"]]
- 00bcd200 bytes 00013fd6
+ 00bcd244 bytes 00013fd6
- 00bcd224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd224 ["INT_ADD", "register:40f0:8", ["const:bcd224:8", "const:4:8"]]
- 00bcd224 ["CALLIND", null, ["register:0:8"]]
+ 00bcd268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd268 ["INT_ADD", "register:40f0:8", ["const:bcd268:8", "const:4:8"]]
+ 00bcd268 ["CALLIND", null, ["register:0:8"]]
- 00bcd224 bytes 00013fd6
+ 00bcd268 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23929170774dc34ffa16809d4568e17b"></a>

### [`00bcd3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md) → [`00bcd410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd410.md) FUN_00bcd410

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md#insn-00bcd414) · [`00bcd44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md#insn-00bcd44c) · [`00bcd470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md#insn-00bcd470)
- 新版 `00bcd458`（命令位置の公開資料なし） · `00bcd490`（命令位置の公開資料なし） · `00bcd4b4`（命令位置の公開資料なし）

~~~diff
- 00bcd414 ["INT_ADD", "register:40f0:8", ["const:bcd414:8", "const:4:8"]]
- 00bcd414 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcd458 ["INT_ADD", "register:40f0:8", ["const:bcd458:8", "const:4:8"]]
+ 00bcd458 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcd414 bytes 7b3f0094
+ 00bcd458 bytes 7e3f0094
- 00bcd44c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd44c ["INT_ADD", "register:40f0:8", ["const:bcd44c:8", "const:4:8"]]
- 00bcd44c ["CALLIND", null, ["register:0:8"]]
+ 00bcd490 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd490 ["INT_ADD", "register:40f0:8", ["const:bcd490:8", "const:4:8"]]
+ 00bcd490 ["CALLIND", null, ["register:0:8"]]
- 00bcd44c bytes 00013fd6
+ 00bcd490 bytes 00013fd6
- 00bcd470 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd470 ["INT_ADD", "register:40f0:8", ["const:bcd470:8", "const:4:8"]]
- 00bcd470 ["CALLIND", null, ["register:0:8"]]
+ 00bcd4b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd4b4 ["INT_ADD", "register:40f0:8", ["const:bcd4b4:8", "const:4:8"]]
+ 00bcd4b4 ["CALLIND", null, ["register:0:8"]]
- 00bcd470 bytes 00013fd6
+ 00bcd4b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a541738e7d149f35f7eacc3873ab5ffd"></a>

### [`00bcd638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md) → [`00bcd67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd67c.md) FUN_00bcd67c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md#insn-00bcd66c) · [`00bcd690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md#insn-00bcd690) · [`00bcd6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md#insn-00bcd6bc)
- 新版 `00bcd6b0`（命令位置の公開資料なし） · `00bcd6d4`（命令位置の公開資料なし） · `00bcd700`（命令位置の公開資料なし）

~~~diff
- 00bcd66c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd66c ["INT_ADD", "register:40f0:8", ["const:bcd66c:8", "const:4:8"]]
- 00bcd66c ["CALLIND", null, ["register:0:8"]]
+ 00bcd6b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd6b0 ["INT_ADD", "register:40f0:8", ["const:bcd6b0:8", "const:4:8"]]
+ 00bcd6b0 ["CALLIND", null, ["register:0:8"]]
- 00bcd66c bytes 00013fd6
+ 00bcd6b0 bytes 00013fd6
- 00bcd690 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd690 ["INT_ADD", "register:40f0:8", ["const:bcd690:8", "const:4:8"]]
- 00bcd690 ["CALLIND", null, ["register:0:8"]]
+ 00bcd6d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd6d4 ["INT_ADD", "register:40f0:8", ["const:bcd6d4:8", "const:4:8"]]
+ 00bcd6d4 ["CALLIND", null, ["register:0:8"]]
- 00bcd690 bytes 00013fd6
+ 00bcd6d4 bytes 00013fd6
- 00bcd6bc ["INT_ADD", "register:40f0:8", ["const:bcd6bc:8", "const:4:8"]]
- 00bcd6bc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcd700 ["INT_ADD", "register:40f0:8", ["const:bcd700:8", "const:4:8"]]
+ 00bcd700 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcd6bc bytes d13e0094
+ 00bcd700 bytes d43e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3403676b0539662c36f27b5a42e2527"></a>

### [`00bcd754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md) → [`00bcd798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd798.md) FUN_00bcd798

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md#insn-00bcd7a4) · [`00bcd7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md#insn-00bcd7d8) · [`00bcd7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md#insn-00bcd7fc)
- 新版 `00bcd7e8`（命令位置の公開資料なし） · `00bcd81c`（命令位置の公開資料なし） · `00bcd840`（命令位置の公開資料なし）

~~~diff
- 00bcd7a4 ["INT_ADD", "register:40f0:8", ["const:bcd7a4:8", "const:4:8"]]
- 00bcd7a4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcd7e8 ["INT_ADD", "register:40f0:8", ["const:bcd7e8:8", "const:4:8"]]
+ 00bcd7e8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcd7a4 bytes 973e0094
+ 00bcd7e8 bytes 9a3e0094
- 00bcd7d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd7d8 ["INT_ADD", "register:40f0:8", ["const:bcd7d8:8", "const:4:8"]]
- 00bcd7d8 ["CALLIND", null, ["register:0:8"]]
+ 00bcd81c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd81c ["INT_ADD", "register:40f0:8", ["const:bcd81c:8", "const:4:8"]]
+ 00bcd81c ["CALLIND", null, ["register:0:8"]]
- 00bcd7d8 bytes 00013fd6
+ 00bcd81c bytes 00013fd6
- 00bcd7fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd7fc ["INT_ADD", "register:40f0:8", ["const:bcd7fc:8", "const:4:8"]]
- 00bcd7fc ["CALLIND", null, ["register:0:8"]]
+ 00bcd840 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd840 ["INT_ADD", "register:40f0:8", ["const:bcd840:8", "const:4:8"]]
+ 00bcd840 ["CALLIND", null, ["register:0:8"]]
- 00bcd7fc bytes 00013fd6
+ 00bcd840 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c0f58bf69829de723aae2a6acacd1ef"></a>

### [`00bcdc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdc50.md) → [`00bcdc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdc94.md) FUN_00bcdc94

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcdc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdc50.md#insn-00bcdc94) · [`00bcdce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdc50.md#insn-00bcdce4) · [`00bcdd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdc50.md#insn-00bcdd08)
- 新版 `00bcdcd8`（命令位置の公開資料なし） · `00bcdd28`（命令位置の公開資料なし） · `00bcdd4c`（命令位置の公開資料なし）

~~~diff
- 00bcdc94 ["INT_ADD", "register:40f0:8", ["const:bcdc94:8", "const:4:8"]]
- 00bcdc94 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcdcd8 ["INT_ADD", "register:40f0:8", ["const:bcdcd8:8", "const:4:8"]]
+ 00bcdcd8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcdc94 bytes 5b3d0094
+ 00bcdcd8 bytes 5e3d0094
- 00bcdce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcdce4 ["INT_ADD", "register:40f0:8", ["const:bcdce4:8", "const:4:8"]]
- 00bcdce4 ["CALLIND", null, ["register:0:8"]]
+ 00bcdd28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcdd28 ["INT_ADD", "register:40f0:8", ["const:bcdd28:8", "const:4:8"]]
+ 00bcdd28 ["CALLIND", null, ["register:0:8"]]
- 00bcdce4 bytes 00013fd6
+ 00bcdd28 bytes 00013fd6
- 00bcdd08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcdd08 ["INT_ADD", "register:40f0:8", ["const:bcdd08:8", "const:4:8"]]
- 00bcdd08 ["CALLIND", null, ["register:0:8"]]
+ 00bcdd4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcdd4c ["INT_ADD", "register:40f0:8", ["const:bcdd4c:8", "const:4:8"]]
+ 00bcdd4c ["CALLIND", null, ["register:0:8"]]
- 00bcdd08 bytes 00013fd6
+ 00bcdd4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cc919f41ad79050c9ea8e55e6e16a8a"></a>

### [`00bcde98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md) → [`00bcdedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdedc.md) FUN_00bcdedc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcdee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md#insn-00bcdee0) · [`00bcdf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md#insn-00bcdf44) · [`00bcdf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md#insn-00bcdf98)
- 新版 `00bcdf24`（命令位置の公開資料なし） · `00bcdf88`（命令位置の公開資料なし） · `00bcdfdc`（命令位置の公開資料なし）

~~~diff
- 00bcdee0 ["INT_ADD", "register:40f0:8", ["const:bcdee0:8", "const:4:8"]]
- 00bcdee0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcdf24 ["INT_ADD", "register:40f0:8", ["const:bcdf24:8", "const:4:8"]]
+ 00bcdf24 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcdee0 bytes c83c0094
+ 00bcdf24 bytes cb3c0094
- 00bcdf44 ["INT_ADD", "register:40f0:8", ["const:bcdf44:8", "const:4:8"]]
- 00bcdf44 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcdf88 ["INT_ADD", "register:40f0:8", ["const:bcdf88:8", "const:4:8"]]
+ 00bcdf88 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcdf44 bytes af3c0094
+ 00bcdf88 bytes b23c0094
- 00bcdf98 ["INT_ADD", "register:40f0:8", ["const:bcdf98:8", "const:4:8"]]
- 00bcdf98 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcdfdc ["INT_ADD", "register:40f0:8", ["const:bcdfdc:8", "const:4:8"]]
+ 00bcdfdc ["CALL", null, ["callee:00bdd250:8"]]
- 00bcdf98 bytes 9a3c0094
+ 00bcdfdc bytes 9d3c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d1cf274a0e90826c9ee17128f5583e4"></a>

### [`00bce694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md) → [`00bce6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce6d8.md) FUN_00bce6d8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md#insn-00bce6d8) · [`00bce724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md#insn-00bce724) · [`00bce768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md#insn-00bce768)
- 新版 `00bce71c`（命令位置の公開資料なし） · `00bce768`（命令位置の公開資料なし） · `00bce7ac`（命令位置の公開資料なし）

~~~diff
- 00bce6d8 ["INT_ADD", "register:40f0:8", ["const:bce6d8:8", "const:4:8"]]
- 00bce6d8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bce71c ["INT_ADD", "register:40f0:8", ["const:bce71c:8", "const:4:8"]]
+ 00bce71c ["CALL", null, ["callee:00bdd250:8"]]
- 00bce6d8 bytes ca3a0094
+ 00bce71c bytes cd3a0094
- 00bce724 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce724 ["INT_ADD", "register:40f0:8", ["const:bce724:8", "const:4:8"]]
- 00bce724 ["CALLIND", null, ["register:0:8"]]
+ 00bce768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bce768 ["INT_ADD", "register:40f0:8", ["const:bce768:8", "const:4:8"]]
+ 00bce768 ["CALLIND", null, ["register:0:8"]]
- 00bce724 bytes 00013fd6
+ 00bce768 bytes 00013fd6
- 00bce768 ["INT_ADD", "register:40f0:8", ["const:bce768:8", "const:4:8"]]
- 00bce768 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bce7ac ["INT_ADD", "register:40f0:8", ["const:bce7ac:8", "const:4:8"]]
+ 00bce7ac ["CALL", null, ["callee:00bde2c0:8"]]
- 00bce768 bytes c23e0094
+ 00bce7ac bytes c53e0094
~~~


<a id="compare-7ef7bd29df65a750e93aa66c0b67828d"></a>

### [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) → [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) FUN_00bce7b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) · 呼出先 8件 [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) [`00bc204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md) [`00bc2180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) · 呼出先 8件 [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) [`00bc2090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md) [`00bc21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md#insn-00bce7b0) · [`00bce7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md#insn-00bce7e4) · [`00bce7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md#insn-00bce7f4)
- 新版 `00bce7f4`（命令位置の公開資料なし） · `00bce828`（命令位置の公開資料なし） · `00bce838`（命令位置の公開資料なし）

~~~diff
- 00bce7b0 ["INT_ADD", "register:40f0:8", ["const:bce7b0:8", "const:4:8"]]
- 00bce7b0 ["CALL", null, ["callee:00bc1ccc:8"]]
+ 00bce7f4 ["INT_ADD", "register:40f0:8", ["const:bce7f4:8", "const:4:8"]]
+ 00bce7f4 ["CALL", null, ["callee:00bc1ccc:8"]]
- 00bce7b0 bytes 36cdff97
+ 00bce7f4 bytes 36cdff97
- 00bce7e4 ["INT_ADD", "register:40f0:8", ["const:bce7e4:8", "const:4:8"]]
- 00bce7e4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bce828 ["INT_ADD", "register:40f0:8", ["const:bce828:8", "const:4:8"]]
+ 00bce828 ["CALL", null, ["callee:00bdd250:8"]]
- 00bce7e4 bytes 873a0094
+ 00bce828 bytes 8a3a0094
- 00bce7f4 ["INT_ADD", "register:40f0:8", ["const:bce7f4:8", "const:4:8"]]
- 00bce7f4 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bce838 ["INT_ADD", "register:40f0:8", ["const:bce838:8", "const:4:8"]]
+ 00bce838 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bce7f4 bytes 9f3e0094
+ 00bce838 bytes a23e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ff5be6ad86b3f632dcbfc05ce9ef7dc"></a>

### [`00bceb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md) → [`00bcebcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcebcc.md) FUN_00bcebcc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcebb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md#insn-00bcebb4) · [`00bcebd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md#insn-00bcebd8) · [`00bcec04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md#insn-00bcec04)
- 新版 `00bcebf8`（命令位置の公開資料なし） · `00bcec1c`（命令位置の公開資料なし） · `00bcec48`（命令位置の公開資料なし）

~~~diff
- 00bcebb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcebb4 ["INT_ADD", "register:40f0:8", ["const:bcebb4:8", "const:4:8"]]
- 00bcebb4 ["CALLIND", null, ["register:0:8"]]
+ 00bcebf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcebf8 ["INT_ADD", "register:40f0:8", ["const:bcebf8:8", "const:4:8"]]
+ 00bcebf8 ["CALLIND", null, ["register:0:8"]]
- 00bcebb4 bytes 00013fd6
+ 00bcebf8 bytes 00013fd6
- 00bcebd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcebd8 ["INT_ADD", "register:40f0:8", ["const:bcebd8:8", "const:4:8"]]
- 00bcebd8 ["CALLIND", null, ["register:0:8"]]
+ 00bcec1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcec1c ["INT_ADD", "register:40f0:8", ["const:bcec1c:8", "const:4:8"]]
+ 00bcec1c ["CALLIND", null, ["register:0:8"]]
- 00bcebd8 bytes 00013fd6
+ 00bcec1c bytes 00013fd6
- 00bcec04 ["INT_ADD", "register:40f0:8", ["const:bcec04:8", "const:4:8"]]
- 00bcec04 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcec48 ["INT_ADD", "register:40f0:8", ["const:bcec48:8", "const:4:8"]]
+ 00bcec48 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcec04 bytes 7f390094
+ 00bcec48 bytes 82390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e793e493abd944aa3bc12bb65466de71"></a>

### [`00bcf028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf028.md) → [`00bcf06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf06c.md) FUN_00bcf06c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf028.md#insn-00bcf070) · [`00bcf0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf028.md#insn-00bcf0b8)
- 新版 `00bcf0b4`（命令位置の公開資料なし） · `00bcf0fc`（命令位置の公開資料なし）

~~~diff
- 00bcf070 ["INT_ADD", "register:40f0:8", ["const:bcf070:8", "const:4:8"]]
- 00bcf070 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcf0b4 ["INT_ADD", "register:40f0:8", ["const:bcf0b4:8", "const:4:8"]]
+ 00bcf0b4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcf070 bytes 64380094
+ 00bcf0b4 bytes 67380094
- 00bcf0b8 ["INT_ADD", "register:40f0:8", ["const:bcf0b8:8", "const:4:8"]]
- 00bcf0b8 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bcf0fc ["INT_ADD", "register:40f0:8", ["const:bcf0fc:8", "const:4:8"]]
+ 00bcf0fc ["CALL", null, ["callee:00bde2c0:8"]]
- 00bcf0b8 bytes 6e3c0094
+ 00bcf0fc bytes 713c0094
~~~


<a id="compare-25e24432e61513252b2727cd7ed01289"></a>

### [`00bcf0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf0c4.md) → [`00bcf108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf108.md) FUN_00bcf108

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf0c4.md#insn-00bcf108) · [`00bcf158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf0c4.md#insn-00bcf158) · [`00bcf19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf0c4.md#insn-00bcf19c)
- 新版 `00bcf14c`（命令位置の公開資料なし） · `00bcf19c`（命令位置の公開資料なし） · `00bcf1e0`（命令位置の公開資料なし）

~~~diff
- 00bcf108 ["INT_ADD", "register:40f0:8", ["const:bcf108:8", "const:4:8"]]
- 00bcf108 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcf14c ["INT_ADD", "register:40f0:8", ["const:bcf14c:8", "const:4:8"]]
+ 00bcf14c ["CALL", null, ["callee:00bdd250:8"]]
- 00bcf108 bytes 3e380094
+ 00bcf14c bytes 41380094
- 00bcf158 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf158 ["INT_ADD", "register:40f0:8", ["const:bcf158:8", "const:4:8"]]
- 00bcf158 ["CALLIND", null, ["register:0:8"]]
+ 00bcf19c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf19c ["INT_ADD", "register:40f0:8", ["const:bcf19c:8", "const:4:8"]]
+ 00bcf19c ["CALLIND", null, ["register:0:8"]]
- 00bcf158 bytes 00013fd6
+ 00bcf19c bytes 00013fd6
- 00bcf19c ["INT_ADD", "register:40f0:8", ["const:bcf19c:8", "const:4:8"]]
- 00bcf19c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bcf1e0 ["INT_ADD", "register:40f0:8", ["const:bcf1e0:8", "const:4:8"]]
+ 00bcf1e0 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bcf19c bytes 353c0094
+ 00bcf1e0 bytes 383c0094
~~~


<a id="compare-9ecf0d50d62fa741bbaeff774cf861d4"></a>

### [`00bcf1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf1a8.md) → [`00bcf1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf1ec.md) FUN_00bcf1ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf1a8.md#insn-00bcf1ec) · [`00bcf240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf1a8.md#insn-00bcf240) · [`00bcf284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf1a8.md#insn-00bcf284)
- 新版 `00bcf230`（命令位置の公開資料なし） · `00bcf284`（命令位置の公開資料なし） · `00bcf2c8`（命令位置の公開資料なし）

~~~diff
- 00bcf1ec ["INT_ADD", "register:40f0:8", ["const:bcf1ec:8", "const:4:8"]]
- 00bcf1ec ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcf230 ["INT_ADD", "register:40f0:8", ["const:bcf230:8", "const:4:8"]]
+ 00bcf230 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcf1ec bytes 05380094
+ 00bcf230 bytes 08380094
- 00bcf240 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf240 ["INT_ADD", "register:40f0:8", ["const:bcf240:8", "const:4:8"]]
- 00bcf240 ["CALLIND", null, ["register:0:8"]]
+ 00bcf284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf284 ["INT_ADD", "register:40f0:8", ["const:bcf284:8", "const:4:8"]]
+ 00bcf284 ["CALLIND", null, ["register:0:8"]]
- 00bcf240 bytes 00013fd6
+ 00bcf284 bytes 00013fd6
- 00bcf284 ["INT_ADD", "register:40f0:8", ["const:bcf284:8", "const:4:8"]]
- 00bcf284 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bcf2c8 ["INT_ADD", "register:40f0:8", ["const:bcf2c8:8", "const:4:8"]]
+ 00bcf2c8 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bcf284 bytes fb3b0094
+ 00bcf2c8 bytes fe3b0094
~~~


<a id="compare-40941bb44638b4ba62b6046ed5795002"></a>

### [`00bcf290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md) → [`00bcf2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf2d4.md) FUN_00bcf2d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md#insn-00bcf2d4) · [`00bcf310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md#insn-00bcf310) · [`00bcf354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md#insn-00bcf354)
- 新版 `00bcf318`（命令位置の公開資料なし） · `00bcf354`（命令位置の公開資料なし） · `00bcf398`（命令位置の公開資料なし）

~~~diff
- 00bcf2d4 ["INT_ADD", "register:40f0:8", ["const:bcf2d4:8", "const:4:8"]]
- 00bcf2d4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcf318 ["INT_ADD", "register:40f0:8", ["const:bcf318:8", "const:4:8"]]
+ 00bcf318 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcf2d4 bytes cb370094
+ 00bcf318 bytes ce370094
- 00bcf310 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf310 ["INT_ADD", "register:40f0:8", ["const:bcf310:8", "const:4:8"]]
- 00bcf310 ["CALLIND", null, ["register:0:8"]]
+ 00bcf354 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf354 ["INT_ADD", "register:40f0:8", ["const:bcf354:8", "const:4:8"]]
+ 00bcf354 ["CALLIND", null, ["register:0:8"]]
- 00bcf310 bytes 00013fd6
+ 00bcf354 bytes 00013fd6
- 00bcf354 ["INT_ADD", "register:40f0:8", ["const:bcf354:8", "const:4:8"]]
- 00bcf354 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bcf398 ["INT_ADD", "register:40f0:8", ["const:bcf398:8", "const:4:8"]]
+ 00bcf398 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bcf354 bytes c73b0094
+ 00bcf398 bytes ca3b0094
~~~


<a id="compare-b6df395abcbb3a75c4357f3aeb0fe826"></a>

### [`00bcf98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf98c.md) → [`00bcf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9d0.md) FUN_00bcf9d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf374.md) · 呼出先 1件 [`00bc12a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc12a8.md)
- 新版 呼出元 1件 [`00bcf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md) · 呼出先 1件 [`00bc12ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc12ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf98c.md#insn-00bcf9a8)
- 新版 `00bcf9ec`（命令位置の公開資料なし）

~~~diff
- 00bcf9a8 ["INT_ADD", "register:40f0:8", ["const:bcf9a8:8", "const:4:8"]]
- 00bcf9a8 ["CALL", null, ["callee:00bc12ec:8"]]
+ 00bcf9ec ["INT_ADD", "register:40f0:8", ["const:bcf9ec:8", "const:4:8"]]
+ 00bcf9ec ["CALL", null, ["callee:00bc12ec:8"]]
- 00bcf9a8 bytes 40c6ff97
+ 00bcf9ec bytes 40c6ff97
~~~


<a id="compare-4c3795d35e89480435df959b3d388b82"></a>

### [`00bcf9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md) → [`00bcfa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfa38.md) FUN_00bcfa38

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfa1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md#insn-00bcfa1c) · [`00bcfa48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md#insn-00bcfa48) · [`00bcfab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md#insn-00bcfab0)
- 新版 `00bcfa60`（命令位置の公開資料なし） · `00bcfa8c`（命令位置の公開資料なし） · `00bcfaf4`（命令位置の公開資料なし）

~~~diff
- 00bcfa1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfa1c ["INT_ADD", "register:40f0:8", ["const:bcfa1c:8", "const:4:8"]]
- 00bcfa1c ["CALLIND", null, ["register:0:8"]]
+ 00bcfa60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfa60 ["INT_ADD", "register:40f0:8", ["const:bcfa60:8", "const:4:8"]]
+ 00bcfa60 ["CALLIND", null, ["register:0:8"]]
- 00bcfa1c bytes 00013fd6
+ 00bcfa60 bytes 00013fd6
- 00bcfa48 ["INT_ADD", "register:40f0:8", ["const:bcfa48:8", "const:4:8"]]
- 00bcfa48 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcfa8c ["INT_ADD", "register:40f0:8", ["const:bcfa8c:8", "const:4:8"]]
+ 00bcfa8c ["CALL", null, ["callee:00bdd250:8"]]
- 00bcfa48 bytes ee350094
+ 00bcfa8c bytes f1350094
- 00bcfab0 ["INT_ADD", "register:40f0:8", ["const:bcfab0:8", "const:4:8"]]
- 00bcfab0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcfaf4 ["INT_ADD", "register:40f0:8", ["const:bcfaf4:8", "const:4:8"]]
+ 00bcfaf4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcfab0 bytes d4350094
+ 00bcfaf4 bytes d7350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a0f21da03f19bbba991714cf0d467d"></a>

### [`00bcfb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md) → [`00bcfba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfba8.md) FUN_00bcfba8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md#insn-00bcfbb0) · [`00bcfbd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md#insn-00bcfbd8) · [`00bcfc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md#insn-00bcfc10)
- 新版 `00bcfbf4`（命令位置の公開資料なし） · `00bcfc1c`（命令位置の公開資料なし） · `00bcfc54`（命令位置の公開資料なし）

~~~diff
- 00bcfbb0 ["INT_ADD", "register:40f0:8", ["const:bcfbb0:8", "const:4:8"]]
- 00bcfbb0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcfbf4 ["INT_ADD", "register:40f0:8", ["const:bcfbf4:8", "const:4:8"]]
+ 00bcfbf4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcfbb0 bytes 94350094
+ 00bcfbf4 bytes 97350094
- 00bcfbd8 ["INT_ADD", "register:40f0:8", ["const:bcfbd8:8", "const:4:8"]]
- 00bcfbd8 ["CALL", null, ["callee:00bc82d4:8"]]
+ 00bcfc1c ["INT_ADD", "register:40f0:8", ["const:bcfc1c:8", "const:4:8"]]
+ 00bcfc1c ["CALL", null, ["callee:00bc82d4:8"]]
- 00bcfbd8 bytes aee1ff97
+ 00bcfc1c bytes aee1ff97
- 00bcfc10 ["INT_ADD", "register:40f0:8", ["const:bcfc10:8", "const:4:8"]]
- 00bcfc10 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcfc54 ["INT_ADD", "register:40f0:8", ["const:bcfc54:8", "const:4:8"]]
+ 00bcfc54 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcfc10 bytes 7c350094
+ 00bcfc54 bytes 7f350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a83d20c6df3b8403a3402f7610f1b5"></a>

### [`00bcfd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md) → [`00bcfd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfd54.md) FUN_00bcfd54

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md#insn-00bcfd60) · [`00bcfd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md#insn-00bcfd94) · [`00bcfdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md#insn-00bcfdcc)
- 新版 `00bcfda4`（命令位置の公開資料なし） · `00bcfdd8`（命令位置の公開資料なし） · `00bcfe10`（命令位置の公開資料なし）

~~~diff
- 00bcfd60 ["INT_ADD", "register:40f0:8", ["const:bcfd60:8", "const:4:8"]]
- 00bcfd60 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcfda4 ["INT_ADD", "register:40f0:8", ["const:bcfda4:8", "const:4:8"]]
+ 00bcfda4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcfd60 bytes 28350094
+ 00bcfda4 bytes 2b350094
- 00bcfd94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfd94 ["INT_ADD", "register:40f0:8", ["const:bcfd94:8", "const:4:8"]]
- 00bcfd94 ["CALLIND", null, ["register:0:8"]]
+ 00bcfdd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfdd8 ["INT_ADD", "register:40f0:8", ["const:bcfdd8:8", "const:4:8"]]
+ 00bcfdd8 ["CALLIND", null, ["register:0:8"]]
- 00bcfd94 bytes 00013fd6
+ 00bcfdd8 bytes 00013fd6
- 00bcfdcc ["INT_ADD", "register:40f0:8", ["const:bcfdcc:8", "const:4:8"]]
- 00bcfdcc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcfe10 ["INT_ADD", "register:40f0:8", ["const:bcfe10:8", "const:4:8"]]
+ 00bcfe10 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcfdcc bytes 0d350094
+ 00bcfe10 bytes 10350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68f16932f4016f9a81e810bc0f35f033"></a>

### [`00bcfe1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md) → [`00bcfe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfe60.md) FUN_00bcfe60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md#insn-00bcfe48) · [`00bcfe6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md#insn-00bcfe6c) · [`00bcfe98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md#insn-00bcfe98)
- 新版 `00bcfe8c`（命令位置の公開資料なし） · `00bcfeb0`（命令位置の公開資料なし） · `00bcfedc`（命令位置の公開資料なし）

~~~diff
- 00bcfe48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfe48 ["INT_ADD", "register:40f0:8", ["const:bcfe48:8", "const:4:8"]]
- 00bcfe48 ["CALLIND", null, ["register:0:8"]]
+ 00bcfe8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfe8c ["INT_ADD", "register:40f0:8", ["const:bcfe8c:8", "const:4:8"]]
+ 00bcfe8c ["CALLIND", null, ["register:0:8"]]
- 00bcfe48 bytes 00013fd6
+ 00bcfe8c bytes 00013fd6
- 00bcfe6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfe6c ["INT_ADD", "register:40f0:8", ["const:bcfe6c:8", "const:4:8"]]
- 00bcfe6c ["CALLIND", null, ["register:0:8"]]
+ 00bcfeb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfeb0 ["INT_ADD", "register:40f0:8", ["const:bcfeb0:8", "const:4:8"]]
+ 00bcfeb0 ["CALLIND", null, ["register:0:8"]]
- 00bcfe6c bytes 00013fd6
+ 00bcfeb0 bytes 00013fd6
- 00bcfe98 ["INT_ADD", "register:40f0:8", ["const:bcfe98:8", "const:4:8"]]
- 00bcfe98 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcfedc ["INT_ADD", "register:40f0:8", ["const:bcfedc:8", "const:4:8"]]
+ 00bcfedc ["CALL", null, ["callee:00bdd250:8"]]
- 00bcfe98 bytes da340094
+ 00bcfedc bytes dd340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e8757761fe9f6086d7645de0a352dbf"></a>

### [`00bd006c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md) → [`00bd00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd00b0.md) FUN_00bd00b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md#insn-00bd0098) · [`00bd00bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md#insn-00bd00bc) · [`00bd00e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md#insn-00bd00e8)
- 新版 `00bd00dc`（命令位置の公開資料なし） · `00bd0100`（命令位置の公開資料なし） · `00bd012c`（命令位置の公開資料なし）

~~~diff
- 00bd0098 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0098 ["INT_ADD", "register:40f0:8", ["const:bd0098:8", "const:4:8"]]
- 00bd0098 ["CALLIND", null, ["register:0:8"]]
+ 00bd00dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd00dc ["INT_ADD", "register:40f0:8", ["const:bd00dc:8", "const:4:8"]]
+ 00bd00dc ["CALLIND", null, ["register:0:8"]]
- 00bd0098 bytes 00013fd6
+ 00bd00dc bytes 00013fd6
- 00bd00bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd00bc ["INT_ADD", "register:40f0:8", ["const:bd00bc:8", "const:4:8"]]
- 00bd00bc ["CALLIND", null, ["register:0:8"]]
+ 00bd0100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0100 ["INT_ADD", "register:40f0:8", ["const:bd0100:8", "const:4:8"]]
+ 00bd0100 ["CALLIND", null, ["register:0:8"]]
- 00bd00bc bytes 00013fd6
+ 00bd0100 bytes 00013fd6
- 00bd00e8 ["INT_ADD", "register:40f0:8", ["const:bd00e8:8", "const:4:8"]]
- 00bd00e8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd012c ["INT_ADD", "register:40f0:8", ["const:bd012c:8", "const:4:8"]]
+ 00bd012c ["CALL", null, ["callee:00bdd250:8"]]
- 00bd00e8 bytes 46340094
+ 00bd012c bytes 49340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8865733aecd9483bece762b13ec66823"></a>

### [`00bd0390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md) → [`00bd03d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd03d4.md) FUN_00bd03d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd03bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md#insn-00bd03bc) · [`00bd03e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md#insn-00bd03e0) · [`00bd040c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md#insn-00bd040c)
- 新版 `00bd0400`（命令位置の公開資料なし） · `00bd0424`（命令位置の公開資料なし） · `00bd0450`（命令位置の公開資料なし）

~~~diff
- 00bd03bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd03bc ["INT_ADD", "register:40f0:8", ["const:bd03bc:8", "const:4:8"]]
- 00bd03bc ["CALLIND", null, ["register:0:8"]]
+ 00bd0400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0400 ["INT_ADD", "register:40f0:8", ["const:bd0400:8", "const:4:8"]]
+ 00bd0400 ["CALLIND", null, ["register:0:8"]]
- 00bd03bc bytes 00013fd6
+ 00bd0400 bytes 00013fd6
- 00bd03e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd03e0 ["INT_ADD", "register:40f0:8", ["const:bd03e0:8", "const:4:8"]]
- 00bd03e0 ["CALLIND", null, ["register:0:8"]]
+ 00bd0424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0424 ["INT_ADD", "register:40f0:8", ["const:bd0424:8", "const:4:8"]]
+ 00bd0424 ["CALLIND", null, ["register:0:8"]]
- 00bd03e0 bytes 00013fd6
+ 00bd0424 bytes 00013fd6
- 00bd040c ["INT_ADD", "register:40f0:8", ["const:bd040c:8", "const:4:8"]]
- 00bd040c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd0450 ["INT_ADD", "register:40f0:8", ["const:bd0450:8", "const:4:8"]]
+ 00bd0450 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd040c bytes 7d330094
+ 00bd0450 bytes 80330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06a3eb8166a2750239f94e3c5d7a06aa"></a>

### [`00bd06cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md) → [`00bd0710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0710.md) FUN_00bd0710

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md#insn-00bd0718) · [`00bd0744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md#insn-00bd0744) · [`00bd0770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md#insn-00bd0770)
- 新版 `00bd075c`（命令位置の公開資料なし） · `00bd0788`（命令位置の公開資料なし） · `00bd07b4`（命令位置の公開資料なし）

~~~diff
- 00bd0718 ["INT_ADD", "register:40f0:8", ["const:bd0718:8", "const:4:8"]]
- 00bd0718 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd075c ["INT_ADD", "register:40f0:8", ["const:bd075c:8", "const:4:8"]]
+ 00bd075c ["CALL", null, ["callee:00bdd250:8"]]
- 00bd0718 bytes ba320094
+ 00bd075c bytes bd320094
- 00bd0744 ["INT_ADD", "register:40f0:8", ["const:bd0744:8", "const:4:8"]]
- 00bd0744 ["CALL", null, ["callee:00bc82d4:8"]]
+ 00bd0788 ["INT_ADD", "register:40f0:8", ["const:bd0788:8", "const:4:8"]]
+ 00bd0788 ["CALL", null, ["callee:00bc82d4:8"]]
- 00bd0744 bytes d3deff97
+ 00bd0788 bytes d3deff97
- 00bd0770 ["INT_ADD", "register:40f0:8", ["const:bd0770:8", "const:4:8"]]
- 00bd0770 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd07b4 ["INT_ADD", "register:40f0:8", ["const:bd07b4:8", "const:4:8"]]
+ 00bd07b4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd0770 bytes a4320094
+ 00bd07b4 bytes a7320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b3ce227e5f5d5b965a500a66c7ce7ad"></a>

### [`00bd07c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md) → [`00bd0808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0808.md) FUN_00bd0808

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd07f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md#insn-00bd07f0) · [`00bd0814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md#insn-00bd0814) · [`00bd082c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md#insn-00bd082c)
- 新版 `00bd0834`（命令位置の公開資料なし） · `00bd0858`（命令位置の公開資料なし） · `00bd0870`（命令位置の公開資料なし）

~~~diff
- 00bd07f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd07f0 ["INT_ADD", "register:40f0:8", ["const:bd07f0:8", "const:4:8"]]
- 00bd07f0 ["CALLIND", null, ["register:0:8"]]
+ 00bd0834 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0834 ["INT_ADD", "register:40f0:8", ["const:bd0834:8", "const:4:8"]]
+ 00bd0834 ["CALLIND", null, ["register:0:8"]]
- 00bd07f0 bytes 00013fd6
+ 00bd0834 bytes 00013fd6
- 00bd0814 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0814 ["INT_ADD", "register:40f0:8", ["const:bd0814:8", "const:4:8"]]
- 00bd0814 ["CALLIND", null, ["register:0:8"]]
+ 00bd0858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0858 ["INT_ADD", "register:40f0:8", ["const:bd0858:8", "const:4:8"]]
+ 00bd0858 ["CALLIND", null, ["register:0:8"]]
- 00bd0814 bytes 00013fd6
+ 00bd0858 bytes 00013fd6
- 00bd082c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd082c ["INT_ADD", "register:40f0:8", ["const:bd082c:8", "const:4:8"]]
- 00bd082c ["CALLIND", null, ["register:0:8"]]
+ 00bd0870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0870 ["INT_ADD", "register:40f0:8", ["const:bd0870:8", "const:4:8"]]
+ 00bd0870 ["CALLIND", null, ["register:0:8"]]
- 00bd082c bytes 00013fd6
+ 00bd0870 bytes 00013fd6
~~~


<a id="compare-fbdfa66d14be1683741e8aa2750ff0c5"></a>

### [`00bd0a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md) → [`00bd0a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0a54.md) FUN_00bd0a54

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md#insn-00bd0a54) · [`00bd0aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md#insn-00bd0aa0) · [`00bd0ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md#insn-00bd0ae4)
- 新版 `00bd0a98`（命令位置の公開資料なし） · `00bd0ae4`（命令位置の公開資料なし） · `00bd0b28`（命令位置の公開資料なし）

~~~diff
- 00bd0a54 ["INT_ADD", "register:40f0:8", ["const:bd0a54:8", "const:4:8"]]
- 00bd0a54 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd0a98 ["INT_ADD", "register:40f0:8", ["const:bd0a98:8", "const:4:8"]]
+ 00bd0a98 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd0a54 bytes eb310094
+ 00bd0a98 bytes ee310094
- 00bd0aa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0aa0 ["INT_ADD", "register:40f0:8", ["const:bd0aa0:8", "const:4:8"]]
- 00bd0aa0 ["CALLIND", null, ["register:0:8"]]
+ 00bd0ae4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0ae4 ["INT_ADD", "register:40f0:8", ["const:bd0ae4:8", "const:4:8"]]
+ 00bd0ae4 ["CALLIND", null, ["register:0:8"]]
- 00bd0aa0 bytes 00013fd6
+ 00bd0ae4 bytes 00013fd6
- 00bd0ae4 ["INT_ADD", "register:40f0:8", ["const:bd0ae4:8", "const:4:8"]]
- 00bd0ae4 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bd0b28 ["INT_ADD", "register:40f0:8", ["const:bd0b28:8", "const:4:8"]]
+ 00bd0b28 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bd0ae4 bytes e3350094
+ 00bd0b28 bytes e6350094
~~~


<a id="compare-d93769b2e9ded47f11880707c4a92b48"></a>

### [`00bd0b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md) → [`00bd0b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0b4c.md) FUN_00bd0b4c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md#insn-00bd0b34) · [`00bd0b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md#insn-00bd0b58) · [`00bd0b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md#insn-00bd0b94)
- 新版 `00bd0b78`（命令位置の公開資料なし） · `00bd0b9c`（命令位置の公開資料なし） · `00bd0bd8`（命令位置の公開資料なし）

~~~diff
- 00bd0b34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0b34 ["INT_ADD", "register:40f0:8", ["const:bd0b34:8", "const:4:8"]]
- 00bd0b34 ["CALLIND", null, ["register:0:8"]]
+ 00bd0b78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0b78 ["INT_ADD", "register:40f0:8", ["const:bd0b78:8", "const:4:8"]]
+ 00bd0b78 ["CALLIND", null, ["register:0:8"]]
- 00bd0b34 bytes 00013fd6
+ 00bd0b78 bytes 00013fd6
- 00bd0b58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0b58 ["INT_ADD", "register:40f0:8", ["const:bd0b58:8", "const:4:8"]]
- 00bd0b58 ["CALLIND", null, ["register:0:8"]]
+ 00bd0b9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0b9c ["INT_ADD", "register:40f0:8", ["const:bd0b9c:8", "const:4:8"]]
+ 00bd0b9c ["CALLIND", null, ["register:0:8"]]
- 00bd0b58 bytes 00013fd6
+ 00bd0b9c bytes 00013fd6
- 00bd0b94 ["INT_ADD", "register:40f0:8", ["const:bd0b94:8", "const:4:8"]]
- 00bd0b94 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd0bd8 ["INT_ADD", "register:40f0:8", ["const:bd0bd8:8", "const:4:8"]]
+ 00bd0bd8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd0b94 bytes 9b310094
+ 00bd0bd8 bytes 9e310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f04ed659a00ab8202101933834d69721"></a>

### [`00bd1018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md) → [`00bd105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd105c.md) FUN_00bd105c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd1044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md#insn-00bd1044) · [`00bd1068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md#insn-00bd1068) · [`00bd1094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md#insn-00bd1094)
- 新版 `00bd1088`（命令位置の公開資料なし） · `00bd10ac`（命令位置の公開資料なし） · `00bd10d8`（命令位置の公開資料なし）

~~~diff
- 00bd1044 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1044 ["INT_ADD", "register:40f0:8", ["const:bd1044:8", "const:4:8"]]
- 00bd1044 ["CALLIND", null, ["register:0:8"]]
+ 00bd1088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1088 ["INT_ADD", "register:40f0:8", ["const:bd1088:8", "const:4:8"]]
+ 00bd1088 ["CALLIND", null, ["register:0:8"]]
- 00bd1044 bytes 00013fd6
+ 00bd1088 bytes 00013fd6
- 00bd1068 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1068 ["INT_ADD", "register:40f0:8", ["const:bd1068:8", "const:4:8"]]
- 00bd1068 ["CALLIND", null, ["register:0:8"]]
+ 00bd10ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd10ac ["INT_ADD", "register:40f0:8", ["const:bd10ac:8", "const:4:8"]]
+ 00bd10ac ["CALLIND", null, ["register:0:8"]]
- 00bd1068 bytes 00013fd6
+ 00bd10ac bytes 00013fd6
- 00bd1094 ["INT_ADD", "register:40f0:8", ["const:bd1094:8", "const:4:8"]]
- 00bd1094 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd10d8 ["INT_ADD", "register:40f0:8", ["const:bd10d8:8", "const:4:8"]]
+ 00bd10d8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd1094 bytes 5b300094
+ 00bd10d8 bytes 5e300094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

