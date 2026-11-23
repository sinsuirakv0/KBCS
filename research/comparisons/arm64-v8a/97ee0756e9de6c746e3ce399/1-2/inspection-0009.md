# v15.7.3 → v15.7.4 · 要調査の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-563babeecd68384e1c1cb8d9bba04366"></a>

### [`00b002a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002a4.md) → [`00b002e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b002e8.md) FUN_00b002e8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b00094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00094.md) · 呼出先 1件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md)
- 新版 呼出元 1件 [`00b000d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b000d8.md) · 呼出先 1件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b002d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002a4.md#insn-00b002d8)
- 新版 `00b0031c`（命令位置の公開資料なし）

~~~diff
- 00b002d8 ["INT_ADD", "register:40f0:8", ["const:b002d8:8", "const:4:8"]]
- 00b002d8 ["CALL", null, ["callee:00b010ec:8"]]
+ 00b0031c ["INT_ADD", "register:40f0:8", ["const:b0031c:8", "const:4:8"]]
+ 00b0031c ["CALL", null, ["callee:00b010ec:8"]]
- 00b002d8 bytes 74030094
+ 00b0031c bytes 74030094
~~~


<a id="compare-d54e04445a2e2b2b4874fe9b389cb34d"></a>

### [`00b002dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002dc.md) → [`00b00320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00320.md) FUN_00b00320

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b00094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00094.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00b000d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b000d8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002dc.md#insn-00b00318)
- 新版 `00b0035c`（命令位置の公開資料なし）

~~~diff
- 00b00318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b00318 ["INT_ADD", "register:40f0:8", ["const:b00318:8", "const:4:8"]]
- 00b00318 ["CALLIND", null, ["register:0:8"]]
+ 00b0035c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b0035c ["INT_ADD", "register:40f0:8", ["const:b0035c:8", "const:4:8"]]
+ 00b0035c ["CALLIND", null, ["register:0:8"]]
- 00b00318 bytes 00013fd6
+ 00b0035c bytes 00013fd6
~~~


<a id="compare-e596ed0a80c8c33f96d4b4e52ff67515"></a>

### [`00b0032c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b0032c.md) → [`00b00370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00370.md) _ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdede0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdede0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bdee30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee30.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b0032c.md#insn-00b00344) · [`00b003d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b0032c.md#insn-00b003d8)
- 新版 `00b00388`（命令位置の公開資料なし） · `00b0041c`（命令位置の公開資料なし）

~~~diff
- 00b00344 ["INT_ADD", "register:40f0:8", ["const:b00344:8", "const:4:8"]]
- 00b00344 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b00388 ["INT_ADD", "register:40f0:8", ["const:b00388:8", "const:4:8"]]
+ 00b00388 ["CALL", null, ["callee:00bddc20:8"]]
- 00b00344 bytes 23760394
+ 00b00388 bytes 26760394
- 00b003d8 ["INT_ADD", "register:40f0:8", ["const:b003d8:8", "const:4:8"]]
- 00b003d8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b0041c ["INT_ADD", "register:40f0:8", ["const:b0041c:8", "const:4:8"]]
+ 00b0041c ["CALL", null, ["callee:00bddc30:8"]]
- 00b003d8 bytes 02760394
+ 00b0041c bytes 05760394
~~~


<a id="compare-7cf892eec07a5d2e02b6bdb005498283"></a>

### [`00b003ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b003ec.md) → [`00b00430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00430.md) _ZNK8firebase26ReferenceCountedFutureImpl17IsRunningCallbackEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b003ec.md#insn-00b00404) · [`00b00410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b003ec.md#insn-00b00410)
- 新版 `00b00448`（命令位置の公開資料なし） · `00b00454`（命令位置の公開資料なし）

~~~diff
- 00b00404 ["INT_ADD", "register:40f0:8", ["const:b00404:8", "const:4:8"]]
- 00b00404 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b00448 ["INT_ADD", "register:40f0:8", ["const:b00448:8", "const:4:8"]]
+ 00b00448 ["CALL", null, ["callee:00bddc20:8"]]
- 00b00404 bytes f3750394
+ 00b00448 bytes f6750394
- 00b00410 ["INT_ADD", "register:40f0:8", ["const:b00410:8", "const:4:8"]]
- 00b00410 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b00454 ["INT_ADD", "register:40f0:8", ["const:b00454:8", "const:4:8"]]
+ 00b00454 ["CALL", null, ["callee:00bddc30:8"]]
- 00b00410 bytes f4750394
+ 00b00454 bytes f7750394
~~~


<a id="compare-a96563bb334efcdb1683f1e51bf138bf"></a>

### [`00b00424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00424.md) → [`00b00468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00468.md) _ZNK8firebase26ReferenceCountedFutureImpl22IsReferencedExternallyEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00424.md#insn-00b00448) · [`00b004f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00424.md#insn-00b004f0) · [`00b00514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00424.md#insn-00b00514)
- 新版 `00b0048c`（命令位置の公開資料なし） · `00b00534`（命令位置の公開資料なし） · `00b00558`（命令位置の公開資料なし）

~~~diff
- 00b00448 ["INT_ADD", "register:40f0:8", ["const:b00448:8", "const:4:8"]]
- 00b00448 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b0048c ["INT_ADD", "register:40f0:8", ["const:b0048c:8", "const:4:8"]]
+ 00b0048c ["CALL", null, ["callee:00bddc20:8"]]
- 00b00448 bytes e2750394
+ 00b0048c bytes e5750394
- 00b004f0 ["INT_ADD", "register:40f0:8", ["const:b004f0:8", "const:4:8"]]
- 00b004f0 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b00534 ["INT_ADD", "register:40f0:8", ["const:b00534:8", "const:4:8"]]
+ 00b00534 ["CALL", null, ["callee:00bddc30:8"]]
- 00b004f0 bytes bc750394
+ 00b00534 bytes bf750394
- 00b00514 ["INT_ADD", "register:40f0:8", ["const:b00514:8", "const:4:8"]]
- 00b00514 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b00558 ["INT_ADD", "register:40f0:8", ["const:b00558:8", "const:4:8"]]
+ 00b00558 ["CALL", null, ["callee:00bddc20:8"]]
- 00b00514 bytes af750394
+ 00b00558 bytes b2750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54d0be57c1f8bd33a798091e152f372c"></a>

### [`00b00b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md) → [`00b00bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bb4.md) _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdedc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedc0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bdee10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md#insn-00b00b90) · [`00b00b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md#insn-00b00b9c) · [`00b00be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md#insn-00b00be0)
- 新版 `00b00bd4`（命令位置の公開資料なし） · `00b00be0`（命令位置の公開資料なし） · `00b00c24`（命令位置の公開資料なし）

~~~diff
- 00b00b90 ["INT_ADD", "register:40f0:8", ["const:b00b90:8", "const:4:8"]]
- 00b00b90 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b00bd4 ["INT_ADD", "register:40f0:8", ["const:b00bd4:8", "const:4:8"]]
+ 00b00bd4 ["CALL", null, ["callee:00bddc20:8"]]
- 00b00b90 bytes 10740394
+ 00b00bd4 bytes 13740394
- 00b00b9c ["INT_ADD", "register:40f0:8", ["const:b00b9c:8", "const:4:8"]]
- 00b00b9c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b00be0 ["INT_ADD", "register:40f0:8", ["const:b00be0:8", "const:4:8"]]
+ 00b00be0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b00b9c bytes 0d740394
+ 00b00be0 bytes 10740394
- 00b00be0 ["INT_ADD", "register:40f0:8", ["const:b00be0:8", "const:4:8"]]
- 00b00be0 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b00c24 ["INT_ADD", "register:40f0:8", ["const:b00c24:8", "const:4:8"]]
+ 00b00c24 ["CALL", null, ["callee:00bddc30:8"]]
- 00b00be0 bytes 00740394
+ 00b00c24 bytes 03740394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3200e89cb46635cdcf092f449bcca00"></a>

### [`00b00c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00c28.md) → [`00b00c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00c6c.md) _ZN8firebase26ReferenceCountedFutureImpl12MarkOrphanedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00c28.md#insn-00b00c40)
- 新版 `00b00c84`（命令位置の公開資料なし）

~~~diff
- 00b00c40 ["INT_ADD", "register:40f0:8", ["const:b00c40:8", "const:4:8"]]
- 00b00c40 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b00c84 ["INT_ADD", "register:40f0:8", ["const:b00c84:8", "const:4:8"]]
+ 00b00c84 ["CALL", null, ["callee:00bddc20:8"]]
- 00b00c40 bytes e4730394
+ 00b00c84 bytes e7730394
~~~


<a id="compare-3827cd4add20ddb26e553c13748c812d"></a>

### [`00b00cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cc4.md) → [`00b00d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d08.md) _ZN8firebase12FutureHandleD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b0132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) · 呼出先 1件 [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 2件 [`00b01370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01370.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) · 呼出先 1件 [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cc4.md#insn-00b00ce4)
- 新版 `00b00d28`（命令位置の公開資料なし）

~~~diff
- 00b00ce4 ["INT_ADD", "register:40f0:8", ["const:b00ce4:8", "const:4:8"]]
- 00b00ce4 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b00d28 ["INT_ADD", "register:40f0:8", ["const:b00d28:8", "const:4:8"]]
+ 00b00d28 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b00ce4 bytes 1f740394
+ 00b00d28 bytes 22740394
~~~


<a id="compare-0ac0500b37e4cedc80e6e5cd3c0496cc"></a>

### [`00b00ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00ef4.md) → [`00b00f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f38.md) _ZN8firebase12FutureHandle6DetachEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) · 呼出先 1件 [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 1件 [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) · 呼出先 1件 [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00ef4.md#insn-00b00f14) · [`00b00f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00ef4.md#insn-00b00f28)
- 新版 `00b00f58`（命令位置の公開資料なし） · `00b00f6c`（命令位置の公開資料なし）

~~~diff
- 00b00f14 ["INT_ADD", "register:40f0:8", ["const:b00f14:8", "const:4:8"]]
- 00b00f14 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b00f58 ["INT_ADD", "register:40f0:8", ["const:b00f58:8", "const:4:8"]]
+ 00b00f58 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b00f14 bytes 93730394
+ 00b00f58 bytes 96730394
- 00b00f28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b00f28 ["INT_ADD", "register:40f0:8", ["const:b00f28:8", "const:4:8"]]
- 00b00f28 ["CALLIND", null, ["register:0:8"]]
+ 00b00f6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b00f6c ["INT_ADD", "register:40f0:8", ["const:b00f6c:8", "const:4:8"]]
+ 00b00f6c ["CALLIND", null, ["register:0:8"]]
- 00b00f28 bytes 00013fd6
+ 00b00f6c bytes 00013fd6
~~~


<a id="compare-c261360413124b45cbd9f4cc3f82d8a0"></a>

### [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md) → [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md) FUN_00b010ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00b002a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002a4.md) [`00b0817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md) [`00b59b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59b24.md) [`00b59ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md) [`00b5aa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md) · 呼出先 1件 [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 6件 [`00b002e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b002e8.md) [`00b081c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md) [`00b59b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59b68.md) [`00b59d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59d2c.md) [`00b5aaac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aaac.md) · 呼出先 1件 [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b010b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md#insn-00b010b0)
- 新版 `00b010f4`（命令位置の公開資料なし）

~~~diff
- 00b010b0 ["INT_ADD", "register:40f0:8", ["const:b010b0:8", "const:4:8"]]
- 00b010b0 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b010f4 ["INT_ADD", "register:40f0:8", ["const:b010f4:8", "const:4:8"]]
+ 00b010f4 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b010b0 bytes 70740394
+ 00b010f4 bytes 73740394
~~~


<a id="compare-82bc6d1f6049db7fd9f53cd6e6a1ab62"></a>

### [`00b0129c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0129c.md) → [`00b012e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b012e0.md) FUN_00b012e0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00afeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md) · 呼出先 4件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 1件 [`00afeb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md) · 呼出先 4件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b012b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0129c.md#insn-00b012b0) · [`00b012c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0129c.md#insn-00b012c8) · [`00b012dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0129c.md#insn-00b012dc)
- 新版 `00b012f4`（命令位置の公開資料なし） · `00b0130c`（命令位置の公開資料なし） · `00b01320`（命令位置の公開資料なし）

~~~diff
- 00b012b0 ["INT_ADD", "register:40f0:8", ["const:b012b0:8", "const:4:8"]]
- 00b012b0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b012f4 ["INT_ADD", "register:40f0:8", ["const:b012f4:8", "const:4:8"]]
+ 00b012f4 ["CALL", null, ["callee:00bddc20:8"]]
- 00b012b0 bytes 48720394
+ 00b012f4 bytes 4b720394
- 00b012c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b012c8 ["INT_ADD", "register:40f0:8", ["const:b012c8:8", "const:4:8"]]
- 00b012c8 ["CALLIND", null, ["register:0:8"]]
+ 00b0130c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b0130c ["INT_ADD", "register:40f0:8", ["const:b0130c:8", "const:4:8"]]
+ 00b0130c ["CALLIND", null, ["register:0:8"]]
- 00b012c8 bytes 00013fd6
+ 00b0130c bytes 00013fd6
- 00b012dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b012dc ["INT_ADD", "register:40f0:8", ["const:b012dc:8", "const:4:8"]]
- 00b012dc ["CALLIND", null, ["register:0:8"]]
+ 00b01320 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b01320 ["INT_ADD", "register:40f0:8", ["const:b01320:8", "const:4:8"]]
+ 00b01320 ["CALLIND", null, ["register:0:8"]]
- 00b012dc bytes 00013fd6
+ 00b01320 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7beaa0b51133a5df1df723d6530ac7ea"></a>

### [`00b018ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b018ac.md) → [`00b018f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b018f0.md) _ZN8firebase17ModuleInitializer20InitializeLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b018cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b018ac.md#insn-00b018cc) · [`00b018d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b018ac.md#insn-00b018d8) · [`00b018e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b018ac.md#insn-00b018e4)
- 新版 `00b01910`（命令位置の公開資料なし） · `00b0191c`（命令位置の公開資料なし） · `00b01928`（命令位置の公開資料なし）

~~~diff
- 00b018cc ["INT_ADD", "register:40f0:8", ["const:b018cc:8", "const:4:8"]]
- 00b018cc ["CALL", null, ["callee:00bddc20:8"]]
+ 00b01910 ["INT_ADD", "register:40f0:8", ["const:b01910:8", "const:4:8"]]
+ 00b01910 ["CALL", null, ["callee:00bddc20:8"]]
- 00b018cc bytes c1700394
+ 00b01910 bytes c4700394
- 00b018d8 ["INT_ADD", "register:40f0:8", ["const:b018d8:8", "const:4:8"]]
- 00b018d8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b0191c ["INT_ADD", "register:40f0:8", ["const:b0191c:8", "const:4:8"]]
+ 00b0191c ["CALL", null, ["callee:00bddc30:8"]]
- 00b018d8 bytes c2700394
+ 00b0191c bytes c5700394
- 00b018e4 ["INT_ADD", "register:40f0:8", ["const:b018e4:8", "const:4:8"]]
- 00b018e4 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b01928 ["INT_ADD", "register:40f0:8", ["const:b01928:8", "const:4:8"]]
+ 00b01928 ["CALL", null, ["callee:00bdde10:8"]]
- 00b018e4 bytes 37710394
+ 00b01928 bytes 3a710394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c72a3609c57119bc602fdd583063c1"></a>

### [`00b024cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b024cc.md) → [`00b02510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02510.md) _ZN8firebase16StaticFutureData13CreateNewDataEPKvi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddde0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b024e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b024cc.md#insn-00b024e0) · [`00b024ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b024cc.md#insn-00b024ec)
- 新版 `00b02524`（命令位置の公開資料なし） · `00b02530`（命令位置の公開資料なし）

~~~diff
- 00b024e0 ["INT_ADD", "register:40f0:8", ["const:b024e0:8", "const:4:8"]]
- 00b024e0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b02524 ["INT_ADD", "register:40f0:8", ["const:b02524:8", "const:4:8"]]
+ 00b02524 ["CALL", null, ["callee:00bdb040:8"]]
- 00b024e0 bytes c4620394
+ 00b02524 bytes c7620394
- 00b024ec ["INT_ADD", "register:40f0:8", ["const:b024ec:8", "const:4:8"]]
- 00b024ec ["CALL", null, ["callee:00bddde0:8"]]
+ 00b02530 ["INT_ADD", "register:40f0:8", ["const:b02530:8", "const:4:8"]]
+ 00b02530 ["CALL", null, ["callee:00bddde0:8"]]
- 00b024ec bytes 296e0394
+ 00b02530 bytes 2c6e0394
~~~


<a id="compare-f11dfe04f6885f8eeb6a68b6498b2ec0"></a>

### [`00b02500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02500.md) → [`00b02544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02544.md) _ZN8firebase11SplitStringERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b025c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02500.md#insn-00b025c4) · [`00b025ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02500.md#insn-00b025ec) · [`00b02628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02500.md#insn-00b02628)
- 新版 `00b02608`（命令位置の公開資料なし） · `00b02630`（命令位置の公開資料なし） · `00b0266c`（命令位置の公開資料なし）

~~~diff
- 00b025c4 ["INT_ADD", "register:40f0:8", ["const:b025c4:8", "const:4:8"]]
- 00b025c4 ["CALL", null, ["callee:00bdb180:8"]]
+ 00b02608 ["INT_ADD", "register:40f0:8", ["const:b02608:8", "const:4:8"]]
+ 00b02608 ["CALL", null, ["callee:00bdb180:8"]]
- 00b025c4 bytes db620394
+ 00b02608 bytes de620394
- 00b025ec ["INT_ADD", "register:40f0:8", ["const:b025ec:8", "const:4:8"]]
- 00b025ec ["CALL", null, ["callee:00bde970:8"]]
+ 00b02630 ["INT_ADD", "register:40f0:8", ["const:b02630:8", "const:4:8"]]
+ 00b02630 ["CALL", null, ["callee:00bde970:8"]]
- 00b025ec bytes cd700394
+ 00b02630 bytes d0700394
- 00b02628 ["INT_ADD", "register:40f0:8", ["const:b02628:8", "const:4:8"]]
- 00b02628 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b0266c ["INT_ADD", "register:40f0:8", ["const:b0266c:8", "const:4:8"]]
+ 00b0266c ["CALL", null, ["callee:00bde7d0:8"]]
- 00b02628 bytes 56700394
+ 00b0266c bytes 59700394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c41ccb28acd7781ffae4cf081bcbe834"></a>

### [`00b027b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b027b0.md) → [`00b027f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b027f4.md) FUN_00b027f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b02710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02710.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdeec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeec0.md)
- 新版 呼出元 1件 [`00b02754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdef10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0282c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b027b0.md#insn-00b0282c) · [`00b02850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b027b0.md#insn-00b02850)
- 新版 `00b02870`（命令位置の公開資料なし） · `00b02894`（命令位置の公開資料なし）

~~~diff
- 00b0282c ["INT_ADD", "register:40f0:8", ["const:b0282c:8", "const:4:8"]]
- 00b0282c ["CALL", null, ["callee:00bdef10:8"]]
+ 00b02870 ["INT_ADD", "register:40f0:8", ["const:b02870:8", "const:4:8"]]
+ 00b02870 ["CALL", null, ["callee:00bdef10:8"]]
- 00b0282c bytes a5710394
+ 00b02870 bytes a8710394
- 00b02850 ["INT_ADD", "register:40f0:8", ["const:b02850:8", "const:4:8"]]
- 00b02850 ["CALL", null, ["callee:00bdb090:8"]]
+ 00b02894 ["INT_ADD", "register:40f0:8", ["const:b02894:8", "const:4:8"]]
+ 00b02894 ["CALL", null, ["callee:00bdb090:8"]]
- 00b02850 bytes fc610394
+ 00b02894 bytes ff610394
~~~


<a id="compare-0d3ea352b9865ef49174bd349925bfc1"></a>

### [`00b02998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02998.md) → [`00b029dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b029dc.md) _ZNSt6__ndk16vectorIPFN8firebase10InitResultEPNS1_3AppEPvENS_9allocatorIS7_EEE21__push_back_slow_pathIRKS7_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeeb0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdef00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef00.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b029fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02998.md#insn-00b029fc) · [`00b02a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02998.md#insn-00b02a08) · [`00b02a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02998.md#insn-00b02a34)
- 新版 `00b02a40`（命令位置の公開資料なし） · `00b02a4c`（命令位置の公開資料なし） · `00b02a78`（命令位置の公開資料なし）

~~~diff
- 00b029fc ["INT_ADD", "register:40f0:8", ["const:b029fc:8", "const:4:8"]]
- 00b029fc ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b02a40 ["INT_ADD", "register:40f0:8", ["const:b02a40:8", "const:4:8"]]
+ 00b02a40 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b029fc bytes 1d6e0394
+ 00b02a40 bytes 206e0394
- 00b02a08 ["INT_ADD", "register:40f0:8", ["const:b02a08:8", "const:4:8"]]
- 00b02a08 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b02a4c ["INT_ADD", "register:40f0:8", ["const:b02a4c:8", "const:4:8"]]
+ 00b02a4c ["CALL", null, ["callee:00bdb040:8"]]
- 00b02a08 bytes 7a610394
+ 00b02a4c bytes 7d610394
- 00b02a34 ["INT_ADD", "register:40f0:8", ["const:b02a34:8", "const:4:8"]]
- 00b02a34 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b02a78 ["INT_ADD", "register:40f0:8", ["const:b02a78:8", "const:4:8"]]
+ 00b02a78 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02a34 bytes cb610394
+ 00b02a78 bytes ce610394
~~~


<a id="compare-c900e04b449da61f99a16b7e81252166"></a>

### [`00b02a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02a80.md) → [`00b02ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ac4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdee80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdee80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee80.md)
- 新版 呼出元 1件 [`00bdeed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeed0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02a80.md#insn-00b02a9c) · [`00b02aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02a80.md#insn-00b02aa8) · [`00b02ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02a80.md#insn-00b02ab8)
- 新版 `00b02ae0`（命令位置の公開資料なし） · `00b02aec`（命令位置の公開資料なし） · `00b02afc`（命令位置の公開資料なし）

~~~diff
- 00b02a9c ["INT_ADD", "register:40f0:8", ["const:b02a9c:8", "const:4:8"]]
- 00b02a9c ["CALL", null, ["callee:00bdeed0:8"]]
+ 00b02ae0 ["INT_ADD", "register:40f0:8", ["const:b02ae0:8", "const:4:8"]]
+ 00b02ae0 ["CALL", null, ["callee:00bdeed0:8"]]
- 00b02a9c bytes f9700394
+ 00b02ae0 bytes fc700394
- 00b02aa8 ["INT_ADD", "register:40f0:8", ["const:b02aa8:8", "const:4:8"]]
- 00b02aa8 ["CALL", null, ["callee:00bdeed0:8"]]
+ 00b02aec ["INT_ADD", "register:40f0:8", ["const:b02aec:8", "const:4:8"]]
+ 00b02aec ["CALL", null, ["callee:00bdeed0:8"]]
- 00b02aa8 bytes f6700394
+ 00b02aec bytes f9700394
- 00b02ab8 ["INT_ADD", "register:40f0:8", ["const:b02ab8:8", "const:4:8"]]
- 00b02ab8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b02afc ["INT_ADD", "register:40f0:8", ["const:b02afc:8", "const:4:8"]]
+ 00b02afc ["CALL", null, ["callee:00bdb060:8"]]
- 00b02ab8 bytes 56610394
+ 00b02afc bytes 59610394
~~~


<a id="compare-485a73697dd4ec286abee06b865b8883"></a>

### [`00b02ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02ad0.md) → [`00b02b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02b14.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdee70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee70.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdeec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeec0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02ad0.md#insn-00b02b6c) · [`00b02bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02ad0.md#insn-00b02bac)
- 新版 `00b02bb0`（命令位置の公開資料なし） · `00b02bf0`（命令位置の公開資料なし）

~~~diff
- 00b02b6c ["INT_ADD", "register:40f0:8", ["const:b02b6c:8", "const:4:8"]]
- 00b02b6c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b02bb0 ["INT_ADD", "register:40f0:8", ["const:b02bb0:8", "const:4:8"]]
+ 00b02bb0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b02b6c bytes 91610394
+ 00b02bb0 bytes 94610394
- 00b02bac ["INT_ADD", "register:40f0:8", ["const:b02bac:8", "const:4:8"]]
- 00b02bac ["CALL", null, ["callee:00bdb200:8"]]
+ 00b02bf0 ["INT_ADD", "register:40f0:8", ["const:b02bf0:8", "const:4:8"]]
+ 00b02bf0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b02bac bytes 81610394
+ 00b02bf0 bytes 84610394
~~~


<a id="compare-0f19be81653fd2c39828eb927907b294"></a>

### [`00b02bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02bf0.md) → [`00b02c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02c34.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeea0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdeef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeef0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02bf0.md#insn-00b02c88) · [`00b02cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02bf0.md#insn-00b02cd0)
- 新版 `00b02ccc`（命令位置の公開資料なし） · `00b02d14`（命令位置の公開資料なし）

~~~diff
- 00b02c88 ["INT_ADD", "register:40f0:8", ["const:b02c88:8", "const:4:8"]]
- 00b02c88 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b02ccc ["INT_ADD", "register:40f0:8", ["const:b02ccc:8", "const:4:8"]]
+ 00b02ccc ["CALL", null, ["callee:00bdb200:8"]]
- 00b02c88 bytes 4a610394
+ 00b02ccc bytes 4d610394
- 00b02cd0 ["INT_ADD", "register:40f0:8", ["const:b02cd0:8", "const:4:8"]]
- 00b02cd0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b02d14 ["INT_ADD", "register:40f0:8", ["const:b02d14:8", "const:4:8"]]
+ 00b02d14 ["CALL", null, ["callee:00bdb200:8"]]
- 00b02cd0 bytes 38610394
+ 00b02d14 bytes 3b610394
~~~


<a id="compare-cfb04542ca1857ba0536bdc6b7715a18"></a>

### [`00b02d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02d04.md) → [`00b02d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02d48.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdee90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee90.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdeee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeee0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02d04.md#insn-00b02da0) · [`00b02de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02d04.md#insn-00b02de0)
- 新版 `00b02de4`（命令位置の公開資料なし） · `00b02e24`（命令位置の公開資料なし）

~~~diff
- 00b02da0 ["INT_ADD", "register:40f0:8", ["const:b02da0:8", "const:4:8"]]
- 00b02da0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b02de4 ["INT_ADD", "register:40f0:8", ["const:b02de4:8", "const:4:8"]]
+ 00b02de4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b02da0 bytes 04610394
+ 00b02de4 bytes 07610394
- 00b02de0 ["INT_ADD", "register:40f0:8", ["const:b02de0:8", "const:4:8"]]
- 00b02de0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b02e24 ["INT_ADD", "register:40f0:8", ["const:b02e24:8", "const:4:8"]]
+ 00b02e24 ["CALL", null, ["callee:00bdb200:8"]]
- 00b02de0 bytes f4600394
+ 00b02e24 bytes f7600394
~~~


<a id="compare-6f794e869c6feaf236a585cb0658d515"></a>

### [`00b04830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04830.md) → [`00b04874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04874.md) FUN_00b04874

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b0468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde280.md)
- 新版 呼出元 1件 [`00b046d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b048a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04830.md#insn-00b048a0) · [`00b048c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04830.md#insn-00b048c4)
- 新版 `00b048e4`（命令位置の公開資料なし） · `00b04908`（命令位置の公開資料なし）

~~~diff
- 00b048a0 ["INT_ADD", "register:40f0:8", ["const:b048a0:8", "const:4:8"]]
- 00b048a0 ["CALL", null, ["callee:00bde2d0:8"]]
+ 00b048e4 ["INT_ADD", "register:40f0:8", ["const:b048e4:8", "const:4:8"]]
+ 00b048e4 ["CALL", null, ["callee:00bde2d0:8"]]
- 00b048a0 bytes 78660394
+ 00b048e4 bytes 7b660394
- 00b048c4 ["INT_ADD", "register:40f0:8", ["const:b048c4:8", "const:4:8"]]
- 00b048c4 ["CALL", null, ["callee:00bdb090:8"]]
+ 00b04908 ["INT_ADD", "register:40f0:8", ["const:b04908:8", "const:4:8"]]
+ 00b04908 ["CALL", null, ["callee:00bdb090:8"]]
- 00b048c4 bytes df590394
+ 00b04908 bytes e2590394
~~~


<a id="compare-15c69578546f46e583f9fc2fe196a605"></a>

### [`00b04d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d7c.md) → [`00b04dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04dc0.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE6assignIPS2_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constru

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdef30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef30.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdef80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef80.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b04dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d7c.md#insn-00b04dec) · [`00b04e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d7c.md#insn-00b04e2c) · [`00b04e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d7c.md#insn-00b04e60)
- 新版 `00b04e30`（命令位置の公開資料なし） · `00b04e70`（命令位置の公開資料なし） · `00b04ea4`（命令位置の公開資料なし）

~~~diff
- 00b04dec ["INT_ADD", "register:40f0:8", ["const:b04dec:8", "const:4:8"]]
- 00b04dec ["CALL", null, ["callee:00bdd9e0:8"]]
+ 00b04e30 ["INT_ADD", "register:40f0:8", ["const:b04e30:8", "const:4:8"]]
+ 00b04e30 ["CALL", null, ["callee:00bdd9e0:8"]]
- 00b04dec bytes e9620394
+ 00b04e30 bytes ec620394
- 00b04e2c ["INT_ADD", "register:40f0:8", ["const:b04e2c:8", "const:4:8"]]
- 00b04e2c ["CALL", null, ["callee:00bddaa0:8"]]
+ 00b04e70 ["INT_ADD", "register:40f0:8", ["const:b04e70:8", "const:4:8"]]
+ 00b04e70 ["CALL", null, ["callee:00bddaa0:8"]]
- 00b04e2c bytes 09630394
+ 00b04e70 bytes 0c630394
- 00b04e60 ["INT_ADD", "register:40f0:8", ["const:b04e60:8", "const:4:8"]]
- 00b04e60 ["CALL", null, ["callee:00bddaa0:8"]]
+ 00b04ea4 ["INT_ADD", "register:40f0:8", ["const:b04ea4:8", "const:4:8"]]
+ 00b04ea4 ["CALL", null, ["callee:00bddaa0:8"]]
- 00b04e60 bytes fc620394
+ 00b04ea4 bytes ff620394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747af83f323695522a233471e25ca108"></a>

### [`00b04f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04f64.md) → [`00b04fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04fa8.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE14__ass

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdef00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef00.md) · 呼出先 5件 [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bdef10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef10.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)
- 新版 呼出元 1件 [`00bdef50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef50.md) · 呼出先 5件 [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bdef60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef60.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04f64.md#insn-00b05040) · [`00b0504c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04f64.md#insn-00b0504c) · [`00b05078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04f64.md#insn-00b05078)
- 新版 `00b05084`（命令位置の公開資料なし） · `00b05090`（命令位置の公開資料なし） · `00b050bc`（命令位置の公開資料なし）

~~~diff
- 00b05040 ["INT_ADD", "register:40f0:8", ["const:b05040:8", "const:4:8"]]
- 00b05040 ["CALL", null, ["callee:00bddaa0:8"]]
+ 00b05084 ["INT_ADD", "register:40f0:8", ["const:b05084:8", "const:4:8"]]
+ 00b05084 ["CALL", null, ["callee:00bddaa0:8"]]
- 00b05040 bytes 84620394
+ 00b05084 bytes 87620394
- 00b0504c ["INT_ADD", "register:40f0:8", ["const:b0504c:8", "const:4:8"]]
- 00b0504c ["CALL", null, ["callee:00bddaa0:8"]]
+ 00b05090 ["INT_ADD", "register:40f0:8", ["const:b05090:8", "const:4:8"]]
+ 00b05090 ["CALL", null, ["callee:00bddaa0:8"]]
- 00b0504c bytes 81620394
+ 00b05090 bytes 84620394
- 00b05078 ["INT_ADD", "register:40f0:8", ["const:b05078:8", "const:4:8"]]
- 00b05078 ["CALL", null, ["callee:00bde720:8"]]
+ 00b050bc ["INT_ADD", "register:40f0:8", ["const:b050bc:8", "const:4:8"]]
+ 00b050bc ["CALL", null, ["callee:00bde720:8"]]
- 00b05078 bytes 96650394
+ 00b050bc bytes 99650394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c64407f8de13d380f74aabdd49cb56b0"></a>

### [`00b05258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05258.md) → [`00b0529c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0529c.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destro

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)
- 新版 呼出元 1件 [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05258.md#insn-00b05274) · [`00b05280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05258.md#insn-00b05280) · [`00b05290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05258.md#insn-00b05290)
- 新版 `00b052b8`（命令位置の公開資料なし） · `00b052c4`（命令位置の公開資料なし） · `00b052d4`（命令位置の公開資料なし）

~~~diff
- 00b05274 ["INT_ADD", "register:40f0:8", ["const:b05274:8", "const:4:8"]]
- 00b05274 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b052b8 ["INT_ADD", "register:40f0:8", ["const:b052b8:8", "const:4:8"]]
+ 00b052b8 ["CALL", null, ["callee:00bdef70:8"]]
- 00b05274 bytes 2b670394
+ 00b052b8 bytes 2e670394
- 00b05280 ["INT_ADD", "register:40f0:8", ["const:b05280:8", "const:4:8"]]
- 00b05280 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b052c4 ["INT_ADD", "register:40f0:8", ["const:b052c4:8", "const:4:8"]]
+ 00b052c4 ["CALL", null, ["callee:00bdef70:8"]]
- 00b05280 bytes 28670394
+ 00b052c4 bytes 2b670394
- 00b05290 ["INT_ADD", "register:40f0:8", ["const:b05290:8", "const:4:8"]]
- 00b05290 ["CALL", null, ["callee:00bdd9e0:8"]]
+ 00b052d4 ["INT_ADD", "register:40f0:8", ["const:b052d4:8", "const:4:8"]]
+ 00b052d4 ["CALL", null, ["callee:00bdd9e0:8"]]
- 00b05290 bytes c0610394
+ 00b052d4 bytes c3610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75aca3c22446028b547c77e7ea4e528c"></a>

### [`00b052b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b052b4.md) → [`00b052f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b052f8.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE15__emp

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdef10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef10.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)
- 新版 呼出元 1件 [`00bdef60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef60.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b052d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b052b4.md#insn-00b052d0) · [`00b052e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b052b4.md#insn-00b052e8) · [`00b052f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b052b4.md#insn-00b052f8)
- 新版 `00b05314`（命令位置の公開資料なし） · `00b0532c`（命令位置の公開資料なし） · `00b0533c`（命令位置の公開資料なし）

~~~diff
- 00b052d0 ["INT_ADD", "register:40f0:8", ["const:b052d0:8", "const:4:8"]]
- 00b052d0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b05314 ["INT_ADD", "register:40f0:8", ["const:b05314:8", "const:4:8"]]
+ 00b05314 ["CALL", null, ["callee:00bdb040:8"]]
- 00b052d0 bytes 48570394
+ 00b05314 bytes 4b570394
- 00b052e8 ["INT_ADD", "register:40f0:8", ["const:b052e8:8", "const:4:8"]]
- 00b052e8 ["CALL", null, ["callee:00bddaa0:8"]]
+ 00b0532c ["INT_ADD", "register:40f0:8", ["const:b0532c:8", "const:4:8"]]
+ 00b0532c ["CALL", null, ["callee:00bddaa0:8"]]
- 00b052e8 bytes da610394
+ 00b0532c bytes dd610394
- 00b052f8 ["INT_ADD", "register:40f0:8", ["const:b052f8:8", "const:4:8"]]
- 00b052f8 ["CALL", null, ["callee:00bddaa0:8"]]
+ 00b0533c ["INT_ADD", "register:40f0:8", ["const:b0533c:8", "const:4:8"]]
+ 00b0533c ["CALL", null, ["callee:00bddaa0:8"]]
- 00b052f8 bytes d6610394
+ 00b0533c bytes d9610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3d96842e62ce0e1830ce3b802bfc88"></a>

### [`00b06b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06b34.md) → [`00b06b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md) _ZN8firebase3AppD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8f0.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2f0.md) [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 1件 [`00bde940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde940.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde340.md) [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06b34.md#insn-00b06b48) · [`00b06b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06b34.md#insn-00b06b54) · [`00b06b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06b34.md#insn-00b06b68)
- 新版 `00b06b8c`（命令位置の公開資料なし） · `00b06b98`（命令位置の公開資料なし） · `00b06bac`（命令位置の公開資料なし）

~~~diff
- 00b06b48 ["INT_ADD", "register:40f0:8", ["const:b06b48:8", "const:4:8"]]
- 00b06b48 ["CALL", null, ["callee:00bde8e0:8"]]
+ 00b06b8c ["INT_ADD", "register:40f0:8", ["const:b06b8c:8", "const:4:8"]]
+ 00b06b8c ["CALL", null, ["callee:00bde8e0:8"]]
- 00b06b48 bytes 525f0394
+ 00b06b8c bytes 555f0394
- 00b06b54 ["INT_ADD", "register:40f0:8", ["const:b06b54:8", "const:4:8"]]
- 00b06b54 ["CALL", null, ["callee:00bde540:8"]]
+ 00b06b98 ["INT_ADD", "register:40f0:8", ["const:b06b98:8", "const:4:8"]]
+ 00b06b98 ["CALL", null, ["callee:00bde540:8"]]
- 00b06b54 bytes 675e0394
+ 00b06b98 bytes 6a5e0394
- 00b06b68 ["INT_ADD", "register:40f0:8", ["const:b06b68:8", "const:4:8"]]
- 00b06b68 ["CALL", null, ["callee:00bde340:8"]]
+ 00b06bac ["INT_ADD", "register:40f0:8", ["const:b06bac:8", "const:4:8"]]
+ 00b06bac ["CALL", null, ["callee:00bde340:8"]]
- 00b06b68 bytes e25d0394
+ 00b06bac bytes e55d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0e4f9de1e74651fd5b30dd9d19fe1d"></a>

### [`00b0817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md) → [`00b081c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md) _ZN8firebase28CallAfterEnsureMethodsCachedEP7_JNIEnvP8_jobjectNSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b08190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md#insn-00b08190) · [`00b081a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md#insn-00b081a8) · [`00b081c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md#insn-00b081c8)
- 新版 `00b081d4`（命令位置の公開資料なし） · `00b081ec`（命令位置の公開資料なし） · `00b0820c`（命令位置の公開資料なし）

~~~diff
- 00b08190 ["INT_ADD", "register:40f0:8", ["const:b08190:8", "const:4:8"]]
- 00b08190 ["CALL", null, ["callee:00b063d4:8"]]
+ 00b081d4 ["INT_ADD", "register:40f0:8", ["const:b081d4:8", "const:4:8"]]
+ 00b081d4 ["CALL", null, ["callee:00b063d4:8"]]
- 00b08190 bytes 80f8ff97
+ 00b081d4 bytes 80f8ff97
- 00b081a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b081a8 ["INT_ADD", "register:40f0:8", ["const:b081a8:8", "const:4:8"]]
- 00b081a8 ["CALLIND", null, ["register:0:8"]]
+ 00b081ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b081ec ["INT_ADD", "register:40f0:8", ["const:b081ec:8", "const:4:8"]]
+ 00b081ec ["CALLIND", null, ["register:0:8"]]
- 00b081a8 bytes 00013fd6
+ 00b081ec bytes 00013fd6
- 00b081c8 ["INT_ADD", "register:40f0:8", ["const:b081c8:8", "const:4:8"]]
- 00b081c8 ["CALL", null, ["callee:00b010ec:8"]]
+ 00b0820c ["INT_ADD", "register:40f0:8", ["const:b0820c:8", "const:4:8"]]
+ 00b0820c ["CALL", null, ["callee:00b010ec:8"]]
- 00b081c8 bytes b8e3ff97
+ 00b0820c bytes b8e3ff97
~~~


<a id="compare-071c624d5e6d59d9179c6bd00e6166eb"></a>

### [`00b081cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b081cc.md) → [`00b08210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08210.md) _ZNK8firebase10AppOptionseqERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdefe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefe0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdf030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf030.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b08274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b081cc.md#insn-00b08274) · [`00b08318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b081cc.md#insn-00b08318) · [`00b083bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b081cc.md#insn-00b083bc)
- 新版 `00b082b8`（命令位置の公開資料なし） · `00b0835c`（命令位置の公開資料なし） · `00b08400`（命令位置の公開資料なし）

~~~diff
- 00b08274 ["INT_ADD", "register:40f0:8", ["const:b08274:8", "const:4:8"]]
- 00b08274 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b082b8 ["INT_ADD", "register:40f0:8", ["const:b082b8:8", "const:4:8"]]
+ 00b082b8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b08274 bytes cf4b0394
+ 00b082b8 bytes d24b0394
- 00b08318 ["INT_ADD", "register:40f0:8", ["const:b08318:8", "const:4:8"]]
- 00b08318 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b0835c ["INT_ADD", "register:40f0:8", ["const:b0835c:8", "const:4:8"]]
+ 00b0835c ["CALL", null, ["callee:00bdb200:8"]]
- 00b08318 bytes a64b0394
+ 00b0835c bytes a94b0394
- 00b083bc ["INT_ADD", "register:40f0:8", ["const:b083bc:8", "const:4:8"]]
- 00b083bc ["CALL", null, ["callee:00bdb200:8"]]
+ 00b08400 ["INT_ADD", "register:40f0:8", ["const:b08400:8", "const:4:8"]]
+ 00b08400 ["CALL", null, ["callee:00bdb200:8"]]
- 00b083bc bytes 7d4b0394
+ 00b08400 bytes 804b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf88894f82f2474c770591b76e0ff51a"></a>

### [`00b0a478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a478.md) → [`00b0a4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a4bc.md) _ZN11flatbuffers6ParserD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea30.md) · 呼出先 14件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`007101c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/007101c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) [`00bde9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9c0.md)
- 新版 呼出元 1件 [`00bdea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea80.md) · 呼出先 14件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdea10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a478.md#insn-00b0a4a8) · [`00b0a4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a478.md#insn-00b0a4b0) · [`00b0a504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a478.md#insn-00b0a504)
- 新版 `00b0a4ec`（命令位置の公開資料なし） · `00b0a4f4`（命令位置の公開資料なし） · `00b0a548`（命令位置の公開資料なし）

~~~diff
- 00b0a4a8 ["INT_ADD", "register:40f0:8", ["const:b0a4a8:8", "const:4:8"]]
- 00b0a4a8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0a4ec ["INT_ADD", "register:40f0:8", ["const:b0a4ec:8", "const:4:8"]]
+ 00b0a4ec ["CALL", null, ["callee:00bdb060:8"]]
- 00b0a4a8 bytes da420394
+ 00b0a4ec bytes dd420394
- 00b0a4b0 ["INT_ADD", "register:40f0:8", ["const:b0a4b0:8", "const:4:8"]]
- 00b0a4b0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0a4f4 ["INT_ADD", "register:40f0:8", ["const:b0a4f4:8", "const:4:8"]]
+ 00b0a4f4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0a4b0 bytes d8420394
+ 00b0a4f4 bytes db420394
- 00b0a504 ["INT_ADD", "register:40f0:8", ["const:b0a504:8", "const:4:8"]]
- 00b0a504 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0a548 ["INT_ADD", "register:40f0:8", ["const:b0a548:8", "const:4:8"]]
+ 00b0a548 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0a504 bytes c3420394
+ 00b0a548 bytes c6420394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4a1c5c10d34d6121c9126ed7468aa21"></a>

### [`00b0a7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md) → [`00b0a808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a808.md) _ZN11flatbuffers10IDLOptionsD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9c0.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdea10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea10.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md#insn-00b0a854) · [`00b0a864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md#insn-00b0a864) · [`00b0a874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md#insn-00b0a874)
- 新版 `00b0a898`（命令位置の公開資料なし） · `00b0a8a8`（命令位置の公開資料なし） · `00b0a8b8`（命令位置の公開資料なし）

~~~diff
- 00b0a854 ["INT_ADD", "register:40f0:8", ["const:b0a854:8", "const:4:8"]]
- 00b0a854 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0a898 ["INT_ADD", "register:40f0:8", ["const:b0a898:8", "const:4:8"]]
+ 00b0a898 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0a854 bytes ef410394
+ 00b0a898 bytes f2410394
- 00b0a864 ["INT_ADD", "register:40f0:8", ["const:b0a864:8", "const:4:8"]]
- 00b0a864 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0a8a8 ["INT_ADD", "register:40f0:8", ["const:b0a8a8:8", "const:4:8"]]
+ 00b0a8a8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0a864 bytes eb410394
+ 00b0a8a8 bytes ee410394
- 00b0a874 ["INT_ADD", "register:40f0:8", ["const:b0a874:8", "const:4:8"]]
- 00b0a874 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0a8b8 ["INT_ADD", "register:40f0:8", ["const:b0a8b8:8", "const:4:8"]]
+ 00b0a8b8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0a874 bytes e7410394
+ 00b0a8b8 bytes ea410394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9cf4108677f4515fca6a4776016901a"></a>

### [`00b0aba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0aba4.md) → [`00b0abe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0abe8.md) _ZN11flatbuffers10IDLOptionsC2ERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9b0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00bdea00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea00.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0abd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0aba4.md#insn-00b0abd4) · [`00b0abe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0aba4.md#insn-00b0abe0) · [`00b0abf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0aba4.md#insn-00b0abf4)
- 新版 `00b0ac18`（命令位置の公開資料なし） · `00b0ac24`（命令位置の公開資料なし） · `00b0ac38`（命令位置の公開資料なし）

~~~diff
- 00b0abd4 ["INT_ADD", "register:40f0:8", ["const:b0abd4:8", "const:4:8"]]
- 00b0abd4 ["CALL", null, ["callee:00bde730:8"]]
+ 00b0ac18 ["INT_ADD", "register:40f0:8", ["const:b0ac18:8", "const:4:8"]]
+ 00b0ac18 ["CALL", null, ["callee:00bde730:8"]]
- 00b0abd4 bytes c34e0394
+ 00b0ac18 bytes c64e0394
- 00b0abe0 ["INT_ADD", "register:40f0:8", ["const:b0abe0:8", "const:4:8"]]
- 00b0abe0 ["CALL", null, ["callee:00bde730:8"]]
+ 00b0ac24 ["INT_ADD", "register:40f0:8", ["const:b0ac24:8", "const:4:8"]]
+ 00b0ac24 ["CALL", null, ["callee:00bde730:8"]]
- 00b0abe0 bytes c04e0394
+ 00b0ac24 bytes c34e0394
- 00b0abf4 ["INT_ADD", "register:40f0:8", ["const:b0abf4:8", "const:4:8"]]
- 00b0abf4 ["CALL", null, ["callee:00bde730:8"]]
+ 00b0ac38 ["INT_ADD", "register:40f0:8", ["const:b0ac38:8", "const:4:8"]]
+ 00b0ac38 ["CALL", null, ["callee:00bde730:8"]]
- 00b0abf4 bytes bb4e0394
+ 00b0ac38 bytes be4e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e210da509bb20509d0ddd468e91234"></a>

### [`00b0ad40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ad40.md) → [`00b0ad84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0ad84.md) _ZNSt6__ndk16vectorIPN11flatbuffers9NamespaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebd0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdec20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec20.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ada4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ad40.md#insn-00b0ada4) · [`00b0adb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ad40.md#insn-00b0adb0) · [`00b0addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ad40.md#insn-00b0addc)
- 新版 `00b0ade8`（命令位置の公開資料なし） · `00b0adf4`（命令位置の公開資料なし） · `00b0ae20`（命令位置の公開資料なし）

~~~diff
- 00b0ada4 ["INT_ADD", "register:40f0:8", ["const:b0ada4:8", "const:4:8"]]
- 00b0ada4 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b0ade8 ["INT_ADD", "register:40f0:8", ["const:b0ade8:8", "const:4:8"]]
+ 00b0ade8 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b0ada4 bytes 334d0394
+ 00b0ade8 bytes 364d0394
- 00b0adb0 ["INT_ADD", "register:40f0:8", ["const:b0adb0:8", "const:4:8"]]
- 00b0adb0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b0adf4 ["INT_ADD", "register:40f0:8", ["const:b0adf4:8", "const:4:8"]]
+ 00b0adf4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b0adb0 bytes 90400394
+ 00b0adf4 bytes 93400394
- 00b0addc ["INT_ADD", "register:40f0:8", ["const:b0addc:8", "const:4:8"]]
- 00b0addc ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b0ae20 ["INT_ADD", "register:40f0:8", ["const:b0ae20:8", "const:4:8"]]
+ 00b0ae20 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b0addc bytes e1400394
+ 00b0ae20 bytes e4400394
~~~


<a id="compare-ef4028ff616067ee06f089b7735271cd"></a>

### [`00b0ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ae28.md) → [`00b0ae6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0ae6c.md) _ZNK8firebase3fbs14GoogleServices6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeaa0.md) · 呼出先 2件 [`00bdea90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea90.md) [`00bdeaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeaf0.md)
- 新版 呼出元 1件 [`00bdeaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeaf0.md) · 呼出先 2件 [`00bdeae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeae0.md) [`00bdeb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0af84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ae28.md#insn-00b0af84) · [`00b0b0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ae28.md#insn-00b0b0b0)
- 新版 `00b0afc8`（命令位置の公開資料なし） · `00b0b0f4`（命令位置の公開資料なし）

~~~diff
- 00b0af84 ["INT_ADD", "register:40f0:8", ["const:b0af84:8", "const:4:8"]]
- 00b0af84 ["CALL", null, ["callee:00bdeae0:8"]]
+ 00b0afc8 ["INT_ADD", "register:40f0:8", ["const:b0afc8:8", "const:4:8"]]
+ 00b0afc8 ["CALL", null, ["callee:00bdeae0:8"]]
- 00b0af84 bytes c34e0394
+ 00b0afc8 bytes c64e0394
- 00b0b0b0 ["INT_ADD", "register:40f0:8", ["const:b0b0b0:8", "const:4:8"]]
- 00b0b0b0 ["CALL", null, ["callee:00bdeb40:8"]]
+ 00b0b0f4 ["INT_ADD", "register:40f0:8", ["const:b0b0f4:8", "const:4:8"]]
+ 00b0b0f4 ["CALL", null, ["callee:00bdeb40:8"]]
- 00b0b0b0 bytes 904e0394
+ 00b0b0f4 bytes 934e0394
~~~


<a id="compare-f6b0d9158333d1ad303738688cac9cb6"></a>

### [`00b0b62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0b62c.md) → [`00b0b670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0b/00b0b670.md) _ZNK8firebase3fbs6Client6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeaf0.md) · 呼出先 4件 [`00bdea60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea60.md) [`00bdea80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea80.md) [`00bdeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeae0.md) [`00bdeb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb00.md)
- 新版 呼出元 1件 [`00bdeb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb40.md) · 呼出先 4件 [`00bdeab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeab0.md) [`00bdead0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdead0.md) [`00bdeb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb30.md) [`00bdeb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0b788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0b62c.md#insn-00b0b788) · [`00b0b8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0b62c.md#insn-00b0b8b4) · [`00b0b9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0b62c.md#insn-00b0b9f4)
- 新版 `00b0b7cc`（命令位置の公開資料なし） · `00b0b8f8`（命令位置の公開資料なし） · `00b0ba38`（命令位置の公開資料なし）

~~~diff
- 00b0b788 ["INT_ADD", "register:40f0:8", ["const:b0b788:8", "const:4:8"]]
- 00b0b788 ["CALL", null, ["callee:00bdeab0:8"]]
+ 00b0b7cc ["INT_ADD", "register:40f0:8", ["const:b0b7cc:8", "const:4:8"]]
+ 00b0b7cc ["CALL", null, ["callee:00bdeab0:8"]]
- 00b0b788 bytes b64c0394
+ 00b0b7cc bytes b94c0394
- 00b0b8b4 ["INT_ADD", "register:40f0:8", ["const:b0b8b4:8", "const:4:8"]]
- 00b0b8b4 ["CALL", null, ["callee:00bdead0:8"]]
+ 00b0b8f8 ["INT_ADD", "register:40f0:8", ["const:b0b8f8:8", "const:4:8"]]
+ 00b0b8f8 ["CALL", null, ["callee:00bdead0:8"]]
- 00b0b8b4 bytes 734c0394
+ 00b0b8f8 bytes 764c0394
- 00b0b9f4 ["INT_ADD", "register:40f0:8", ["const:b0b9f4:8", "const:4:8"]]
- 00b0b9f4 ["CALL", null, ["callee:00bdeb30:8"]]
+ 00b0ba38 ["INT_ADD", "register:40f0:8", ["const:b0ba38:8", "const:4:8"]]
+ 00b0ba38 ["CALL", null, ["callee:00bdeb30:8"]]
- 00b0b9f4 bytes 3b4c0394
+ 00b0ba38 bytes 3e4c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-945d0d33d914866cc6b601180c2d618d"></a>

### [`00b0babc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0babc.md) → [`00b0bb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0b/00b0bb00.md) _ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea60.md) · 呼出先 1件 [`00bdead0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdead0.md)
- 新版 呼出元 1件 [`00bdeab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeab0.md) · 呼出先 1件 [`00bdeb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0bce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0babc.md#insn-00b0bce0)
- 新版 `00b0bd24`（命令位置の公開資料なし）

~~~diff
- 00b0bce0 ["INT_ADD", "register:40f0:8", ["const:b0bce0:8", "const:4:8"]]
- 00b0bce0 ["CALL", null, ["callee:00bdeb20:8"]]
+ 00b0bd24 ["INT_ADD", "register:40f0:8", ["const:b0bd24:8", "const:4:8"]]
+ 00b0bd24 ["CALL", null, ["callee:00bdeb20:8"]]
- 00b0bce0 bytes 7c4b0394
+ 00b0bd24 bytes 7f4b0394
~~~


<a id="compare-1370dee1babc24b3e69ac1d6deb33b64"></a>

### [`00b0bea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0bea8.md) → [`00b0beec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0b/00b0beec.md) _ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea80.md) · 呼出先 1件 [`00bdea70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea70.md)
- 新版 呼出元 1件 [`00bdead0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdead0.md) · 呼出先 1件 [`00bdeac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0c0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0bea8.md#insn-00b0c0e8)
- 新版 `00b0c12c`（命令位置の公開資料なし）

~~~diff
- 00b0c0e8 ["INT_ADD", "register:40f0:8", ["const:b0c0e8:8", "const:4:8"]]
- 00b0c0e8 ["CALL", null, ["callee:00bdeac0:8"]]
+ 00b0c12c ["INT_ADD", "register:40f0:8", ["const:b0c12c:8", "const:4:8"]]
+ 00b0c12c ["CALL", null, ["callee:00bdeac0:8"]]
- 00b0c0e8 bytes 624a0394
+ 00b0c12c bytes 654a0394
~~~


<a id="compare-6f6a4e5445da2c0bf5df39a1ec5ca549"></a>

### [`00b0c538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0c538.md) → [`00b0c57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0c57c.md) _ZNK8firebase3fbs8Services6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb00.md) · 呼出先 2件 [`00bdea50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea50.md) [`00bdeab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeab0.md)
- 新版 呼出元 1件 [`00bdeb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb50.md) · 呼出先 2件 [`00bdeaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeaa0.md) [`00bdeb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0c684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0c538.md#insn-00b0c684) · [`00b0c878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0c538.md#insn-00b0c878)
- 新版 `00b0c6c8`（命令位置の公開資料なし） · `00b0c8bc`（命令位置の公開資料なし）

~~~diff
- 00b0c684 ["INT_ADD", "register:40f0:8", ["const:b0c684:8", "const:4:8"]]
- 00b0c684 ["CALL", null, ["callee:00bdeb00:8"]]
+ 00b0c6c8 ["INT_ADD", "register:40f0:8", ["const:b0c6c8:8", "const:4:8"]]
+ 00b0c6c8 ["CALL", null, ["callee:00bdeb00:8"]]
- 00b0c684 bytes 0b490394
+ 00b0c6c8 bytes 0e490394
- 00b0c878 ["INT_ADD", "register:40f0:8", ["const:b0c878:8", "const:4:8"]]
- 00b0c878 ["CALL", null, ["callee:00bdeaa0:8"]]
+ 00b0c8bc ["INT_ADD", "register:40f0:8", ["const:b0c8bc:8", "const:4:8"]]
+ 00b0c8bc ["CALL", null, ["callee:00bdeaa0:8"]]
- 00b0c878 bytes 76480394
+ 00b0c8bc bytes 79480394
~~~


<a id="compare-cbd39b3f8746b513ea509c3d31740b0a"></a>

### [`00b0c894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0c894.md) → [`00b0c8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0c8d8.md) _ZNK8firebase3fbs16AnalyticsService6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeab0.md) · 呼出先 1件 [`00bdeac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeac0.md)
- 新版 呼出元 1件 [`00bdeb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb00.md) · 呼出先 1件 [`00bdeb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0c9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0c894.md#insn-00b0c9f8)
- 新版 `00b0ca3c`（命令位置の公開資料なし）

~~~diff
- 00b0c9f8 ["INT_ADD", "register:40f0:8", ["const:b0c9f8:8", "const:4:8"]]
- 00b0c9f8 ["CALL", null, ["callee:00bdeb10:8"]]
+ 00b0ca3c ["INT_ADD", "register:40f0:8", ["const:b0ca3c:8", "const:4:8"]]
+ 00b0ca3c ["CALL", null, ["callee:00bdeb10:8"]]
- 00b0c9f8 bytes 32480394
+ 00b0ca3c bytes 35480394
~~~


<a id="compare-07e9d440cc89d7a1b00cca13a3b3e64f"></a>

### [`00b0cbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cbbc.md) → [`00b0cc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cc00.md) _ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea50.md) · 呼出先 1件 [`00bdeab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeab0.md)
- 新版 呼出元 1件 [`00bdeaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeaa0.md) · 呼出先 1件 [`00bdeb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0cee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cbbc.md#insn-00b0cee0)
- 新版 `00b0cf24`（命令位置の公開資料なし）

~~~diff
- 00b0cee0 ["INT_ADD", "register:40f0:8", ["const:b0cee0:8", "const:4:8"]]
- 00b0cee0 ["CALL", null, ["callee:00bdeb00:8"]]
+ 00b0cf24 ["INT_ADD", "register:40f0:8", ["const:b0cf24:8", "const:4:8"]]
+ 00b0cf24 ["CALL", null, ["callee:00bdeb00:8"]]
- 00b0cee0 bytes f4460394
+ 00b0cf24 bytes f7460394
~~~


<a id="compare-36fd7fcaed168b19dca8b52b6182d87c"></a>

### [`00b0cefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cefc.md) → [`00b0cf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cf40.md) _ZN11flatbuffers17FlatBufferBuilderD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdea10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea10.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb10.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md)
- 新版 呼出元 1件 [`00bdea60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea60.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb60.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0cf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cefc.md#insn-00b0cf1c) · [`00b0cf24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cefc.md#insn-00b0cf24) · [`00b0cf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cefc.md#insn-00b0cf44)
- 新版 `00b0cf60`（命令位置の公開資料なし） · `00b0cf68`（命令位置の公開資料なし） · `00b0cf88`（命令位置の公開資料なし）

~~~diff
- 00b0cf1c ["INT_ADD", "register:40f0:8", ["const:b0cf1c:8", "const:4:8"]]
- 00b0cf1c ["CALL", null, ["callee:00bdeb60:8"]]
+ 00b0cf60 ["INT_ADD", "register:40f0:8", ["const:b0cf60:8", "const:4:8"]]
+ 00b0cf60 ["CALL", null, ["callee:00bdeb60:8"]]
- 00b0cf1c bytes fd460394
+ 00b0cf60 bytes 00470394
- 00b0cf24 ["INT_ADD", "register:40f0:8", ["const:b0cf24:8", "const:4:8"]]
- 00b0cf24 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0cf68 ["INT_ADD", "register:40f0:8", ["const:b0cf68:8", "const:4:8"]]
+ 00b0cf68 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0cf24 bytes 3b380394
+ 00b0cf68 bytes 3e380394
- 00b0cf44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0cf44 ["INT_ADD", "register:40f0:8", ["const:b0cf44:8", "const:4:8"]]
- 00b0cf44 ["CALLIND", null, ["register:0:8"]]
+ 00b0cf88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b0cf88 ["INT_ADD", "register:40f0:8", ["const:b0cf88:8", "const:4:8"]]
+ 00b0cf88 ["CALLIND", null, ["register:0:8"]]
- 00b0cf44 bytes 00013fd6
+ 00b0cf88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62736d35255178387459280806d19c58"></a>

### [`00b0cf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md) → [`00b0cfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cfcc.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9d0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) [`00bdeb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb30.md) [`00bdeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb80.md)
- 新版 呼出元 1件 [`00bdea20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea20.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdeb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb80.md) [`00bdebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0cfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md#insn-00b0cfb8) · [`00b0cfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md#insn-00b0cfe0) · [`00b0cfe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md#insn-00b0cfe8)
- 新版 `00b0cffc`（命令位置の公開資料なし） · `00b0d024`（命令位置の公開資料なし） · `00b0d02c`（命令位置の公開資料なし）

~~~diff
- 00b0cfb8 ["INT_ADD", "register:40f0:8", ["const:b0cfb8:8", "const:4:8"]]
- 00b0cfb8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0cffc ["INT_ADD", "register:40f0:8", ["const:b0cffc:8", "const:4:8"]]
+ 00b0cffc ["CALL", null, ["callee:00bdb060:8"]]
- 00b0cfb8 bytes 16380394
+ 00b0cffc bytes 19380394
- 00b0cfe0 ["INT_ADD", "register:40f0:8", ["const:b0cfe0:8", "const:4:8"]]
- 00b0cfe0 ["CALL", null, ["callee:00bdebd0:8"]]
+ 00b0d024 ["INT_ADD", "register:40f0:8", ["const:b0d024:8", "const:4:8"]]
+ 00b0d024 ["CALL", null, ["callee:00bdebd0:8"]]
- 00b0cfe0 bytes e8460394
+ 00b0d024 bytes eb460394
- 00b0cfe8 ["INT_ADD", "register:40f0:8", ["const:b0cfe8:8", "const:4:8"]]
- 00b0cfe8 ["CALL", null, ["callee:00bde9f0:8"]]
+ 00b0d02c ["INT_ADD", "register:40f0:8", ["const:b0d02c:8", "const:4:8"]]
+ 00b0d02c ["CALL", null, ["callee:00bde9f0:8"]]
- 00b0cfe8 bytes 6e460394
+ 00b0d02c bytes 71460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31488f798d9fe9f556a2670dcc8334ea"></a>

### [`00b0d070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d070.md) → [`00b0d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d0b4.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea00.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) [`00bde9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9f0.md) [`00bdeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeba0.md)
- 新版 呼出元 1件 [`00bdea50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea50.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea40.md) [`00bdebf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d070.md#insn-00b0d09c) · [`00b0d0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d070.md#insn-00b0d0bc) · [`00b0d0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d070.md#insn-00b0d0c4)
- 新版 `00b0d0e0`（命令位置の公開資料なし） · `00b0d100`（命令位置の公開資料なし） · `00b0d108`（命令位置の公開資料なし）

~~~diff
- 00b0d09c ["INT_ADD", "register:40f0:8", ["const:b0d09c:8", "const:4:8"]]
- 00b0d09c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d0e0 ["INT_ADD", "register:40f0:8", ["const:b0d0e0:8", "const:4:8"]]
+ 00b0d0e0 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d09c bytes dd370394
+ 00b0d0e0 bytes e0370394
- 00b0d0bc ["INT_ADD", "register:40f0:8", ["const:b0d0bc:8", "const:4:8"]]
- 00b0d0bc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d100 ["INT_ADD", "register:40f0:8", ["const:b0d100:8", "const:4:8"]]
+ 00b0d100 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d0bc bytes d5370394
+ 00b0d100 bytes d8370394
- 00b0d0c4 ["INT_ADD", "register:40f0:8", ["const:b0d0c4:8", "const:4:8"]]
- 00b0d0c4 ["CALL", null, ["callee:00bdea40:8"]]
+ 00b0d108 ["INT_ADD", "register:40f0:8", ["const:b0d108:8", "const:4:8"]]
+ 00b0d108 ["CALL", null, ["callee:00bdea40:8"]]
- 00b0d0c4 bytes 4b460394
+ 00b0d108 bytes 4e460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88899d578b2e20dcfaaf6994acb9267b"></a>

### [`00b0d11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d11c.md) → [`00b0d160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d160.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb20.md) · 呼出先 3件 [`0051d9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d9f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb20.md)
- 新版 呼出元 1件 [`00bdeb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb70.md) · 呼出先 3件 [`0051d9f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d11c.md#insn-00b0d138) · [`00b0d144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d11c.md#insn-00b0d144) · [`00b0d150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d11c.md#insn-00b0d150)
- 新版 `00b0d17c`（命令位置の公開資料なし） · `00b0d188`（命令位置の公開資料なし） · `00b0d194`（命令位置の公開資料なし）

~~~diff
- 00b0d138 ["INT_ADD", "register:40f0:8", ["const:b0d138:8", "const:4:8"]]
- 00b0d138 ["CALL", null, ["callee:00bdeb70:8"]]
+ 00b0d17c ["INT_ADD", "register:40f0:8", ["const:b0d17c:8", "const:4:8"]]
+ 00b0d17c ["CALL", null, ["callee:00bdeb70:8"]]
- 00b0d138 bytes 7a460394
+ 00b0d17c bytes 7d460394
- 00b0d144 ["INT_ADD", "register:40f0:8", ["const:b0d144:8", "const:4:8"]]
- 00b0d144 ["CALL", null, ["callee:00bdeb70:8"]]
+ 00b0d188 ["INT_ADD", "register:40f0:8", ["const:b0d188:8", "const:4:8"]]
+ 00b0d188 ["CALL", null, ["callee:00bdeb70:8"]]
- 00b0d144 bytes 77460394
+ 00b0d188 bytes 7a460394
- 00b0d150 ["INT_ADD", "register:40f0:8", ["const:b0d150:8", "const:4:8"]]
- 00b0d150 ["CALL", null, ["callee:0051d9f8:8"]]
+ 00b0d194 ["INT_ADD", "register:40f0:8", ["const:b0d194:8", "const:4:8"]]
+ 00b0d194 ["CALL", null, ["callee:0051d9f8:8"]]
- 00b0d150 bytes 2a42e897
+ 00b0d194 bytes 1942e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ea28a9cfc59e858c4a88b93f48947fd"></a>

### [`00b0d178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d178.md) → [`00b0d1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1bc.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdebb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebb0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdebb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebb0.md)
- 新版 呼出元 1件 [`00bdec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec00.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d178.md#insn-00b0d194) · [`00b0d1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d178.md#insn-00b0d1a0)
- 新版 `00b0d1d8`（命令位置の公開資料なし） · `00b0d1e4`（命令位置の公開資料なし）

~~~diff
- 00b0d194 ["INT_ADD", "register:40f0:8", ["const:b0d194:8", "const:4:8"]]
- 00b0d194 ["CALL", null, ["callee:00bdec00:8"]]
+ 00b0d1d8 ["INT_ADD", "register:40f0:8", ["const:b0d1d8:8", "const:4:8"]]
+ 00b0d1d8 ["CALL", null, ["callee:00bdec00:8"]]
- 00b0d194 bytes 87460394
+ 00b0d1d8 bytes 8a460394
- 00b0d1a0 ["INT_ADD", "register:40f0:8", ["const:b0d1a0:8", "const:4:8"]]
- 00b0d1a0 ["CALL", null, ["callee:00bdec00:8"]]
+ 00b0d1e4 ["INT_ADD", "register:40f0:8", ["const:b0d1e4:8", "const:4:8"]]
+ 00b0d1e4 ["CALL", null, ["callee:00bdec00:8"]]
- 00b0d1a0 bytes 84460394
+ 00b0d1e4 bytes 87460394
~~~


<a id="compare-0836f839a7400c6e25fee0a412550127"></a>

### [`00b0d1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1b8.md) → [`00b0d1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d1fc.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdebc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebc0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdebc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebc0.md)
- 新版 呼出元 1件 [`00bdec10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec10.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdec10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1b8.md#insn-00b0d1d4) · [`00b0d1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1b8.md#insn-00b0d1e0)
- 新版 `00b0d218`（命令位置の公開資料なし） · `00b0d224`（命令位置の公開資料なし）

~~~diff
- 00b0d1d4 ["INT_ADD", "register:40f0:8", ["const:b0d1d4:8", "const:4:8"]]
- 00b0d1d4 ["CALL", null, ["callee:00bdec10:8"]]
+ 00b0d218 ["INT_ADD", "register:40f0:8", ["const:b0d218:8", "const:4:8"]]
+ 00b0d218 ["CALL", null, ["callee:00bdec10:8"]]
- 00b0d1d4 bytes 7b460394
+ 00b0d218 bytes 7e460394
- 00b0d1e0 ["INT_ADD", "register:40f0:8", ["const:b0d1e0:8", "const:4:8"]]
- 00b0d1e0 ["CALL", null, ["callee:00bdec10:8"]]
+ 00b0d224 ["INT_ADD", "register:40f0:8", ["const:b0d224:8", "const:4:8"]]
+ 00b0d224 ["CALL", null, ["callee:00bdec10:8"]]
- 00b0d1e0 bytes 78460394
+ 00b0d224 bytes 7b460394
~~~


<a id="compare-48b23411d8c59ba5a1ebeaee569010bc"></a>

### [`00b0d1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1f8.md) → [`00b0d23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d23c.md) _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_17FlatBufferBuilder19StringOffsetCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb10.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb10.md)
- 新版 呼出元 1件 [`00bdeb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb60.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1f8.md#insn-00b0d214) · [`00b0d220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1f8.md#insn-00b0d220)
- 新版 `00b0d258`（命令位置の公開資料なし） · `00b0d264`（命令位置の公開資料なし）

~~~diff
- 00b0d214 ["INT_ADD", "register:40f0:8", ["const:b0d214:8", "const:4:8"]]
- 00b0d214 ["CALL", null, ["callee:00bdeb60:8"]]
+ 00b0d258 ["INT_ADD", "register:40f0:8", ["const:b0d258:8", "const:4:8"]]
+ 00b0d258 ["CALL", null, ["callee:00bdeb60:8"]]
- 00b0d214 bytes 3f460394
+ 00b0d258 bytes 42460394
- 00b0d220 ["INT_ADD", "register:40f0:8", ["const:b0d220:8", "const:4:8"]]
- 00b0d220 ["CALL", null, ["callee:00bdeb60:8"]]
+ 00b0d264 ["INT_ADD", "register:40f0:8", ["const:b0d264:8", "const:4:8"]]
+ 00b0d264 ["CALL", null, ["callee:00bdeb60:8"]]
- 00b0d220 bytes 3c460394
+ 00b0d264 bytes 3f460394
~~~


<a id="compare-3694167d5d5cc60803453fd09168e0d5"></a>

### [`00b0d238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d238.md) → [`00b0d27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d27c.md) _ZN11flatbuffers10DefinitionD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb50.md)
- 新版 呼出元 1件 [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d238.md#insn-00b0d264) · [`00b0d270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d238.md#insn-00b0d270) · [`00b0d2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d238.md#insn-00b0d2ac)
- 新版 `00b0d2a8`（命令位置の公開資料なし） · `00b0d2b4`（命令位置の公開資料なし） · `00b0d2f0`（命令位置の公開資料なし）

~~~diff
- 00b0d264 ["INT_ADD", "register:40f0:8", ["const:b0d264:8", "const:4:8"]]
- 00b0d264 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d2a8 ["INT_ADD", "register:40f0:8", ["const:b0d2a8:8", "const:4:8"]]
+ 00b0d2a8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d264 bytes 6b370394
+ 00b0d2a8 bytes 6e370394
- 00b0d270 ["INT_ADD", "register:40f0:8", ["const:b0d270:8", "const:4:8"]]
- 00b0d270 ["CALL", null, ["callee:00bdeba0:8"]]
+ 00b0d2b4 ["INT_ADD", "register:40f0:8", ["const:b0d2b4:8", "const:4:8"]]
+ 00b0d2b4 ["CALL", null, ["callee:00bdeba0:8"]]
- 00b0d270 bytes 38460394
+ 00b0d2b4 bytes 3b460394
- 00b0d2ac ["INT_ADD", "register:40f0:8", ["const:b0d2ac:8", "const:4:8"]]
- 00b0d2ac ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d2f0 ["INT_ADD", "register:40f0:8", ["const:b0d2f0:8", "const:4:8"]]
+ 00b0d2f0 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d2ac bytes 59370394
+ 00b0d2f0 bytes 5c370394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eea4827e3b46c18e8a13344d7dbfe5f6"></a>

### [`00b0d34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d34c.md) → [`00b0d390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d390.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb80.md)
- 新版 呼出元 1件 [`00bdebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebd0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d34c.md#insn-00b0d368) · [`00b0d374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d34c.md#insn-00b0d374) · [`00b0d384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d34c.md#insn-00b0d384)
- 新版 `00b0d3ac`（命令位置の公開資料なし） · `00b0d3b8`（命令位置の公開資料なし） · `00b0d3c8`（命令位置の公開資料なし）

~~~diff
- 00b0d368 ["INT_ADD", "register:40f0:8", ["const:b0d368:8", "const:4:8"]]
- 00b0d368 ["CALL", null, ["callee:00bdebd0:8"]]
+ 00b0d3ac ["INT_ADD", "register:40f0:8", ["const:b0d3ac:8", "const:4:8"]]
+ 00b0d3ac ["CALL", null, ["callee:00bdebd0:8"]]
- 00b0d368 bytes 06460394
+ 00b0d3ac bytes 09460394
- 00b0d374 ["INT_ADD", "register:40f0:8", ["const:b0d374:8", "const:4:8"]]
- 00b0d374 ["CALL", null, ["callee:00bdebd0:8"]]
+ 00b0d3b8 ["INT_ADD", "register:40f0:8", ["const:b0d3b8:8", "const:4:8"]]
+ 00b0d3b8 ["CALL", null, ["callee:00bdebd0:8"]]
- 00b0d374 bytes 03460394
+ 00b0d3b8 bytes 06460394
- 00b0d384 ["INT_ADD", "register:40f0:8", ["const:b0d384:8", "const:4:8"]]
- 00b0d384 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d3c8 ["INT_ADD", "register:40f0:8", ["const:b0d3c8:8", "const:4:8"]]
+ 00b0d3c8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d384 bytes 23370394
+ 00b0d3c8 bytes 26370394
~~~


<a id="compare-ff915966abcb383a3b1391a4309bea19"></a>

### [`00b0d39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md) → [`00b0d3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d3e0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb50.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb50.md)
- 新版 呼出元 1件 [`00bdeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeba0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md#insn-00b0d3b8) · [`00b0d3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md#insn-00b0d3c4) · [`00b0d3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md#insn-00b0d3d4)
- 新版 `00b0d3fc`（命令位置の公開資料なし） · `00b0d408`（命令位置の公開資料なし） · `00b0d418`（命令位置の公開資料なし）

~~~diff
- 00b0d3b8 ["INT_ADD", "register:40f0:8", ["const:b0d3b8:8", "const:4:8"]]
- 00b0d3b8 ["CALL", null, ["callee:00bdeba0:8"]]
+ 00b0d3fc ["INT_ADD", "register:40f0:8", ["const:b0d3fc:8", "const:4:8"]]
+ 00b0d3fc ["CALL", null, ["callee:00bdeba0:8"]]
- 00b0d3b8 bytes e6450394
+ 00b0d3fc bytes e9450394
- 00b0d3c4 ["INT_ADD", "register:40f0:8", ["const:b0d3c4:8", "const:4:8"]]
- 00b0d3c4 ["CALL", null, ["callee:00bdeba0:8"]]
+ 00b0d408 ["INT_ADD", "register:40f0:8", ["const:b0d408:8", "const:4:8"]]
+ 00b0d408 ["CALL", null, ["callee:00bdeba0:8"]]
- 00b0d3c4 bytes e3450394
+ 00b0d408 bytes e6450394
- 00b0d3d4 ["INT_ADD", "register:40f0:8", ["const:b0d3d4:8", "const:4:8"]]
- 00b0d3d4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d418 ["INT_ADD", "register:40f0:8", ["const:b0d418:8", "const:4:8"]]
+ 00b0d418 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d3d4 bytes 0f370394
+ 00b0d418 bytes 12370394
~~~


<a id="compare-c4e216818d1394cf6eb9f2715f073aa9"></a>

### [`00b0d3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d3ec.md) → [`00b0d430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d430.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb30.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb30.md)
- 新版 呼出元 1件 [`00bdeb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb80.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d3ec.md#insn-00b0d408) · [`00b0d414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d3ec.md#insn-00b0d414) · [`00b0d424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d3ec.md#insn-00b0d424)
- 新版 `00b0d44c`（命令位置の公開資料なし） · `00b0d458`（命令位置の公開資料なし） · `00b0d468`（命令位置の公開資料なし）

~~~diff
- 00b0d408 ["INT_ADD", "register:40f0:8", ["const:b0d408:8", "const:4:8"]]
- 00b0d408 ["CALL", null, ["callee:00bdeb80:8"]]
+ 00b0d44c ["INT_ADD", "register:40f0:8", ["const:b0d44c:8", "const:4:8"]]
+ 00b0d44c ["CALL", null, ["callee:00bdeb80:8"]]
- 00b0d408 bytes ca450394
+ 00b0d44c bytes cd450394
- 00b0d414 ["INT_ADD", "register:40f0:8", ["const:b0d414:8", "const:4:8"]]
- 00b0d414 ["CALL", null, ["callee:00bdeb80:8"]]
+ 00b0d458 ["INT_ADD", "register:40f0:8", ["const:b0d458:8", "const:4:8"]]
+ 00b0d458 ["CALL", null, ["callee:00bdeb80:8"]]
- 00b0d414 bytes c7450394
+ 00b0d458 bytes ca450394
- 00b0d424 ["INT_ADD", "register:40f0:8", ["const:b0d424:8", "const:4:8"]]
- 00b0d424 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d468 ["INT_ADD", "register:40f0:8", ["const:b0d468:8", "const:4:8"]]
+ 00b0d468 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d424 bytes fb360394
+ 00b0d468 bytes fe360394
~~~


<a id="compare-48204c3df6a219cfd2c3b900a38504a9"></a>

### [`00b0d43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d43c.md) → [`00b0d480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d480.md) _ZN11flatbuffers11SymbolTableINS_7EnumValEED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9e0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb70.md)
- 新版 呼出元 1件 [`00bdea30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea30.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d43c.md#insn-00b0d46c) · [`00b0d490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d43c.md#insn-00b0d490) · [`00b0d4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d43c.md#insn-00b0d4e4)
- 新版 `00b0d4b0`（命令位置の公開資料なし） · `00b0d4d4`（命令位置の公開資料なし） · `00b0d528`（命令位置の公開資料なし）

~~~diff
- 00b0d46c ["INT_ADD", "register:40f0:8", ["const:b0d46c:8", "const:4:8"]]
- 00b0d46c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d4b0 ["INT_ADD", "register:40f0:8", ["const:b0d4b0:8", "const:4:8"]]
+ 00b0d4b0 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d46c bytes e9360394
+ 00b0d4b0 bytes ec360394
- 00b0d490 ["INT_ADD", "register:40f0:8", ["const:b0d490:8", "const:4:8"]]
- 00b0d490 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d4d4 ["INT_ADD", "register:40f0:8", ["const:b0d4d4:8", "const:4:8"]]
+ 00b0d4d4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d490 bytes e0360394
+ 00b0d4d4 bytes e3360394
- 00b0d4e4 ["INT_ADD", "register:40f0:8", ["const:b0d4e4:8", "const:4:8"]]
- 00b0d4e4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d528 ["INT_ADD", "register:40f0:8", ["const:b0d528:8", "const:4:8"]]
+ 00b0d528 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d4e4 bytes cb360394
+ 00b0d528 bytes ce360394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f2410100508fba81f7eb101da99ea96"></a>

### [`00b0d520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d520.md) → [`00b0d564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d564.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb70.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb70.md)
- 新版 呼出元 1件 [`00bdebc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebc0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d520.md#insn-00b0d53c) · [`00b0d548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d520.md#insn-00b0d548) · [`00b0d558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d520.md#insn-00b0d558)
- 新版 `00b0d580`（命令位置の公開資料なし） · `00b0d58c`（命令位置の公開資料なし） · `00b0d59c`（命令位置の公開資料なし）

~~~diff
- 00b0d53c ["INT_ADD", "register:40f0:8", ["const:b0d53c:8", "const:4:8"]]
- 00b0d53c ["CALL", null, ["callee:00bdebc0:8"]]
+ 00b0d580 ["INT_ADD", "register:40f0:8", ["const:b0d580:8", "const:4:8"]]
+ 00b0d580 ["CALL", null, ["callee:00bdebc0:8"]]
- 00b0d53c bytes 8d450394
+ 00b0d580 bytes 90450394
- 00b0d548 ["INT_ADD", "register:40f0:8", ["const:b0d548:8", "const:4:8"]]
- 00b0d548 ["CALL", null, ["callee:00bdebc0:8"]]
+ 00b0d58c ["INT_ADD", "register:40f0:8", ["const:b0d58c:8", "const:4:8"]]
+ 00b0d58c ["CALL", null, ["callee:00bdebc0:8"]]
- 00b0d548 bytes 8a450394
+ 00b0d58c bytes 8d450394
- 00b0d558 ["INT_ADD", "register:40f0:8", ["const:b0d558:8", "const:4:8"]]
- 00b0d558 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d59c ["INT_ADD", "register:40f0:8", ["const:b0d59c:8", "const:4:8"]]
+ 00b0d59c ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d558 bytes ae360394
+ 00b0d59c bytes b1360394
~~~


<a id="compare-a7380be0880b405e3887165fdfdf1b24"></a>

### [`00b0d570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d570.md) → [`00b0d5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d5b4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb60.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb60.md)
- 新版 呼出元 1件 [`00bdebb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebb0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d570.md#insn-00b0d58c) · [`00b0d598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d570.md#insn-00b0d598) · [`00b0d5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d570.md#insn-00b0d5a8)
- 新版 `00b0d5d0`（命令位置の公開資料なし） · `00b0d5dc`（命令位置の公開資料なし） · `00b0d5ec`（命令位置の公開資料なし）

~~~diff
- 00b0d58c ["INT_ADD", "register:40f0:8", ["const:b0d58c:8", "const:4:8"]]
- 00b0d58c ["CALL", null, ["callee:00bdebb0:8"]]
+ 00b0d5d0 ["INT_ADD", "register:40f0:8", ["const:b0d5d0:8", "const:4:8"]]
+ 00b0d5d0 ["CALL", null, ["callee:00bdebb0:8"]]
- 00b0d58c bytes 75450394
+ 00b0d5d0 bytes 78450394
- 00b0d598 ["INT_ADD", "register:40f0:8", ["const:b0d598:8", "const:4:8"]]
- 00b0d598 ["CALL", null, ["callee:00bdebb0:8"]]
+ 00b0d5dc ["INT_ADD", "register:40f0:8", ["const:b0d5dc:8", "const:4:8"]]
+ 00b0d5dc ["CALL", null, ["callee:00bdebb0:8"]]
- 00b0d598 bytes 72450394
+ 00b0d5dc bytes 75450394
- 00b0d5a8 ["INT_ADD", "register:40f0:8", ["const:b0d5a8:8", "const:4:8"]]
- 00b0d5a8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d5ec ["INT_ADD", "register:40f0:8", ["const:b0d5ec:8", "const:4:8"]]
+ 00b0d5ec ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d5a8 bytes 9a360394
+ 00b0d5ec bytes 9d360394
~~~


<a id="compare-9255b5d99f00c71e7ade786a06be4ed3"></a>

### [`00b0d5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md) → [`00b0d604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d604.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9f0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) [`00bdeb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb90.md)
- 新版 呼出元 1件 [`00bdea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea40.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdebe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md#insn-00b0d5ec) · [`00b0d60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md#insn-00b0d60c) · [`00b0d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md#insn-00b0d614)
- 新版 `00b0d630`（命令位置の公開資料なし） · `00b0d650`（命令位置の公開資料なし） · `00b0d658`（命令位置の公開資料なし）

~~~diff
- 00b0d5ec ["INT_ADD", "register:40f0:8", ["const:b0d5ec:8", "const:4:8"]]
- 00b0d5ec ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d630 ["INT_ADD", "register:40f0:8", ["const:b0d630:8", "const:4:8"]]
+ 00b0d630 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d5ec bytes 89360394
+ 00b0d630 bytes 8c360394
- 00b0d60c ["INT_ADD", "register:40f0:8", ["const:b0d60c:8", "const:4:8"]]
- 00b0d60c ["CALL", null, ["callee:00bde9f0:8"]]
+ 00b0d650 ["INT_ADD", "register:40f0:8", ["const:b0d650:8", "const:4:8"]]
+ 00b0d650 ["CALL", null, ["callee:00bde9f0:8"]]
- 00b0d60c bytes e5440394
+ 00b0d650 bytes e8440394
- 00b0d614 ["INT_ADD", "register:40f0:8", ["const:b0d614:8", "const:4:8"]]
- 00b0d614 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d658 ["INT_ADD", "register:40f0:8", ["const:b0d658:8", "const:4:8"]]
+ 00b0d658 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d614 bytes 7f360394
+ 00b0d658 bytes 82360394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26755af337875d109303e4a85b6b0bcf"></a>

### [`00b0d650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d650.md) → [`00b0d694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d694.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb90.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb90.md)
- 新版 呼出元 1件 [`00bdebe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebe0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d650.md#insn-00b0d66c) · [`00b0d678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d650.md#insn-00b0d678) · [`00b0d688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d650.md#insn-00b0d688)
- 新版 `00b0d6b0`（命令位置の公開資料なし） · `00b0d6bc`（命令位置の公開資料なし） · `00b0d6cc`（命令位置の公開資料なし）

~~~diff
- 00b0d66c ["INT_ADD", "register:40f0:8", ["const:b0d66c:8", "const:4:8"]]
- 00b0d66c ["CALL", null, ["callee:00bdebe0:8"]]
+ 00b0d6b0 ["INT_ADD", "register:40f0:8", ["const:b0d6b0:8", "const:4:8"]]
+ 00b0d6b0 ["CALL", null, ["callee:00bdebe0:8"]]
- 00b0d66c bytes 49450394
+ 00b0d6b0 bytes 4c450394
- 00b0d678 ["INT_ADD", "register:40f0:8", ["const:b0d678:8", "const:4:8"]]
- 00b0d678 ["CALL", null, ["callee:00bdebe0:8"]]
+ 00b0d6bc ["INT_ADD", "register:40f0:8", ["const:b0d6bc:8", "const:4:8"]]
+ 00b0d6bc ["CALL", null, ["callee:00bdebe0:8"]]
- 00b0d678 bytes 46450394
+ 00b0d6bc bytes 49450394
- 00b0d688 ["INT_ADD", "register:40f0:8", ["const:b0d688:8", "const:4:8"]]
- 00b0d688 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d6cc ["INT_ADD", "register:40f0:8", ["const:b0d6cc:8", "const:4:8"]]
+ 00b0d6cc ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d688 bytes 62360394
+ 00b0d6cc bytes 65360394
~~~


<a id="compare-95963b1a6bcf9eda08e551f1535d33ea"></a>

### [`00b0d6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6a0.md) → [`00b0d6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d6e4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeba0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeba0.md)
- 新版 呼出元 1件 [`00bdebf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebf0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6a0.md#insn-00b0d6bc) · [`00b0d6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6a0.md#insn-00b0d6c8) · [`00b0d6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6a0.md#insn-00b0d6d8)
- 新版 `00b0d700`（命令位置の公開資料なし） · `00b0d70c`（命令位置の公開資料なし） · `00b0d71c`（命令位置の公開資料なし）

~~~diff
- 00b0d6bc ["INT_ADD", "register:40f0:8", ["const:b0d6bc:8", "const:4:8"]]
- 00b0d6bc ["CALL", null, ["callee:00bdebf0:8"]]
+ 00b0d700 ["INT_ADD", "register:40f0:8", ["const:b0d700:8", "const:4:8"]]
+ 00b0d700 ["CALL", null, ["callee:00bdebf0:8"]]
- 00b0d6bc bytes 39450394
+ 00b0d700 bytes 3c450394
- 00b0d6c8 ["INT_ADD", "register:40f0:8", ["const:b0d6c8:8", "const:4:8"]]
- 00b0d6c8 ["CALL", null, ["callee:00bdebf0:8"]]
+ 00b0d70c ["INT_ADD", "register:40f0:8", ["const:b0d70c:8", "const:4:8"]]
+ 00b0d70c ["CALL", null, ["callee:00bdebf0:8"]]
- 00b0d6c8 bytes 36450394
+ 00b0d70c bytes 39450394
- 00b0d6d8 ["INT_ADD", "register:40f0:8", ["const:b0d6d8:8", "const:4:8"]]
- 00b0d6d8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d71c ["INT_ADD", "register:40f0:8", ["const:b0d71c:8", "const:4:8"]]
+ 00b0d71c ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d6d8 bytes 4e360394
+ 00b0d71c bytes 51360394
~~~


<a id="compare-e49d5f2b7758d38b3b8064e13c02c678"></a>

### [`00b0d6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md) → [`00b0d734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d734.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb40.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb40.md)
- 新版 呼出元 1件 [`00bdeb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb90.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md#insn-00b0d70c) · [`00b0d718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md#insn-00b0d718) · [`00b0d728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md#insn-00b0d728)
- 新版 `00b0d750`（命令位置の公開資料なし） · `00b0d75c`（命令位置の公開資料なし） · `00b0d76c`（命令位置の公開資料なし）

~~~diff
- 00b0d70c ["INT_ADD", "register:40f0:8", ["const:b0d70c:8", "const:4:8"]]
- 00b0d70c ["CALL", null, ["callee:00bdeb90:8"]]
+ 00b0d750 ["INT_ADD", "register:40f0:8", ["const:b0d750:8", "const:4:8"]]
+ 00b0d750 ["CALL", null, ["callee:00bdeb90:8"]]
- 00b0d70c bytes 0d450394
+ 00b0d750 bytes 10450394
- 00b0d718 ["INT_ADD", "register:40f0:8", ["const:b0d718:8", "const:4:8"]]
- 00b0d718 ["CALL", null, ["callee:00bdeb90:8"]]
+ 00b0d75c ["INT_ADD", "register:40f0:8", ["const:b0d75c:8", "const:4:8"]]
+ 00b0d75c ["CALL", null, ["callee:00bdeb90:8"]]
- 00b0d718 bytes 0a450394
+ 00b0d75c bytes 0d450394
- 00b0d728 ["INT_ADD", "register:40f0:8", ["const:b0d728:8", "const:4:8"]]
- 00b0d728 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0d76c ["INT_ADD", "register:40f0:8", ["const:b0d76c:8", "const:4:8"]]
+ 00b0d76c ["CALL", null, ["callee:00bdb060:8"]]
- 00b0d728 bytes 3a360394
+ 00b0d76c bytes 3d360394
~~~


<a id="compare-775c53ab5620f165d28fecbe8f39d1e9"></a>

### [`00b0de94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0de94.md) → [`00b0ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0ded8.md) _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdf040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf040.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdf090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf090.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0df08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0de94.md#insn-00b0df08) · [`00b0df2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0de94.md#insn-00b0df2c)
- 新版 `00b0df4c`（命令位置の公開資料なし） · `00b0df70`（命令位置の公開資料なし）

~~~diff
- 00b0df08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0df08 ["INT_ADD", "register:40f0:8", ["const:b0df08:8", "const:4:8"]]
- 00b0df08 ["CALLIND", null, ["register:0:8"]]
+ 00b0df4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b0df4c ["INT_ADD", "register:40f0:8", ["const:b0df4c:8", "const:4:8"]]
+ 00b0df4c ["CALLIND", null, ["register:0:8"]]
- 00b0df08 bytes 00013fd6
+ 00b0df4c bytes 00013fd6
- 00b0df2c ["INT_ADD", "register:40f0:8", ["const:b0df2c:8", "const:4:8"]]
- 00b0df2c ["CALL", null, ["callee:00bdb090:8"]]
+ 00b0df70 ["INT_ADD", "register:40f0:8", ["const:b0df70:8", "const:4:8"]]
+ 00b0df70 ["CALL", null, ["callee:00bdb090:8"]]
- 00b0df2c bytes 45340394
+ 00b0df70 bytes 48340394
~~~


<a id="compare-1309a12d75be2282adad8f11b34cb881"></a>

### [`00b0e2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e2cc.md) → [`00b0e310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e310.md) _ZN11flatbuffers9MakeCamelERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa70.md) · 呼出先 2件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) [`00be0210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0210.md)
- 新版 呼出元 1件 [`00bdfac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfac0.md) · 呼出先 2件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) [`00be0260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0e3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e2cc.md#insn-00b0e3ac) · [`00b0e3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e2cc.md#insn-00b0e3d8) · [`00b0e448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e2cc.md#insn-00b0e448)
- 新版 `00b0e3f0`（命令位置の公開資料なし） · `00b0e41c`（命令位置の公開資料なし） · `00b0e48c`（命令位置の公開資料なし）

~~~diff
- 00b0e3ac ["INT_ADD", "register:40f0:8", ["const:b0e3ac:8", "const:4:8"]]
- 00b0e3ac ["CALL", null, ["callee:00be0260:8"]]
+ 00b0e3f0 ["INT_ADD", "register:40f0:8", ["const:b0e3f0:8", "const:4:8"]]
+ 00b0e3f0 ["CALL", null, ["callee:00be0260:8"]]
- 00b0e3ac bytes 99470394
+ 00b0e3f0 bytes 9c470394
- 00b0e3d8 ["INT_ADD", "register:40f0:8", ["const:b0e3d8:8", "const:4:8"]]
- 00b0e3d8 ["CALL", null, ["callee:00be0260:8"]]
+ 00b0e41c ["INT_ADD", "register:40f0:8", ["const:b0e41c:8", "const:4:8"]]
+ 00b0e41c ["CALL", null, ["callee:00be0260:8"]]
- 00b0e3d8 bytes 8e470394
+ 00b0e41c bytes 91470394
- 00b0e448 ["INT_ADD", "register:40f0:8", ["const:b0e448:8", "const:4:8"]]
- 00b0e448 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b0e48c ["INT_ADD", "register:40f0:8", ["const:b0e48c:8", "const:4:8"]]
+ 00b0e48c ["CALL", null, ["callee:00bdda90:8"]]
- 00b0e448 bytes 7e3d0394
+ 00b0e48c bytes 813d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f47906ed025dbbff18ab555315f7c0"></a>

### [`00b0e538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e538.md) → [`00b0e57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e57c.md) _ZN11flatbuffers18MakeScreamingCamelERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) [`00be0210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) [`00be0260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0e5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e538.md#insn-00b0e5e0) · [`00b0e660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e538.md#insn-00b0e660) · [`00b0e6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e538.md#insn-00b0e6a4)
- 新版 `00b0e624`（命令位置の公開資料なし） · `00b0e6a4`（命令位置の公開資料なし） · `00b0e6e8`（命令位置の公開資料なし）

~~~diff
- 00b0e5e0 ["INT_ADD", "register:40f0:8", ["const:b0e5e0:8", "const:4:8"]]
- 00b0e5e0 ["CALL", null, ["callee:00be0260:8"]]
+ 00b0e624 ["INT_ADD", "register:40f0:8", ["const:b0e624:8", "const:4:8"]]
+ 00b0e624 ["CALL", null, ["callee:00be0260:8"]]
- 00b0e5e0 bytes 0c470394
+ 00b0e624 bytes 0f470394
- 00b0e660 ["INT_ADD", "register:40f0:8", ["const:b0e660:8", "const:4:8"]]
- 00b0e660 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b0e6a4 ["INT_ADD", "register:40f0:8", ["const:b0e6a4:8", "const:4:8"]]
+ 00b0e6a4 ["CALL", null, ["callee:00bdda90:8"]]
- 00b0e660 bytes f83c0394
+ 00b0e6a4 bytes fb3c0394
- 00b0e6a4 ["INT_ADD", "register:40f0:8", ["const:b0e6a4:8", "const:4:8"]]
- 00b0e6a4 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b0e6e8 ["INT_ADD", "register:40f0:8", ["const:b0e6e8:8", "const:4:8"]]
+ 00b0e6e8 ["CALL", null, ["callee:00bdda90:8"]]
- 00b0e6a4 bytes e73c0394
+ 00b0e6e8 bytes ea3c0394
~~~


<a id="compare-bd0a206586d6e39072bc04d3e69562ef"></a>

### [`00b0e6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md) → [`00b0e73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e73c.md) _ZN11flatbuffers14DeserializeDocERNSt6__ndk16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEPKNS_6VectorINS

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf260.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md)
- 新版 呼出元 1件 [`00bdf2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2b0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0e7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md#insn-00b0e7bc) · [`00b0e7dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md#insn-00b0e7dc) · [`00b0e7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md#insn-00b0e7f8)
- 新版 `00b0e800`（命令位置の公開資料なし） · `00b0e820`（命令位置の公開資料なし） · `00b0e83c`（命令位置の公開資料なし）

~~~diff
- 00b0e7bc ["INT_ADD", "register:40f0:8", ["const:b0e7bc:8", "const:4:8"]]
- 00b0e7bc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b0e800 ["INT_ADD", "register:40f0:8", ["const:b0e800:8", "const:4:8"]]
+ 00b0e800 ["CALL", null, ["callee:00bdb040:8"]]
- 00b0e7bc bytes 0d320394
+ 00b0e800 bytes 10320394
- 00b0e7dc ["INT_ADD", "register:40f0:8", ["const:b0e7dc:8", "const:4:8"]]
- 00b0e7dc ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b0e820 ["INT_ADD", "register:40f0:8", ["const:b0e820:8", "const:4:8"]]
+ 00b0e820 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b0e7dc bytes 61320394
+ 00b0e820 bytes 64320394
- 00b0e7f8 ["INT_ADD", "register:40f0:8", ["const:b0e7f8:8", "const:4:8"]]
- 00b0e7f8 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b0e83c ["INT_ADD", "register:40f0:8", ["const:b0e83c:8", "const:4:8"]]
+ 00b0e83c ["CALL", null, ["callee:00bde7d0:8"]]
- 00b0e7f8 bytes e23f0394
+ 00b0e83c bytes e53f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c7be2d833083d073fbf51dc1bd6cec9"></a>

### [`00b0eda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eda4.md) → [`00b0ede8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ede8.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0edd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eda4.md#insn-00b0edd0) · [`00b0ee24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eda4.md#insn-00b0ee24) · [`00b0ee4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eda4.md#insn-00b0ee4c)
- 新版 `00b0ee14`（命令位置の公開資料なし） · `00b0ee68`（命令位置の公開資料なし） · `00b0ee90`（命令位置の公開資料なし）

~~~diff
- 00b0edd0 ["INT_ADD", "register:40f0:8", ["const:b0edd0:8", "const:4:8"]]
- 00b0edd0 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b0ee14 ["INT_ADD", "register:40f0:8", ["const:b0ee14:8", "const:4:8"]]
+ 00b0ee14 ["CALL", null, ["callee:00bdb190:8"]]
- 00b0edd0 bytes dc300394
+ 00b0ee14 bytes df300394
- 00b0ee24 ["INT_ADD", "register:40f0:8", ["const:b0ee24:8", "const:4:8"]]
- 00b0ee24 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b0ee68 ["INT_ADD", "register:40f0:8", ["const:b0ee68:8", "const:4:8"]]
+ 00b0ee68 ["CALL", null, ["callee:00bdb040:8"]]
- 00b0ee24 bytes 73300394
+ 00b0ee68 bytes 76300394
- 00b0ee4c ["INT_ADD", "register:40f0:8", ["const:b0ee4c:8", "const:4:8"]]
- 00b0ee4c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b0ee90 ["INT_ADD", "register:40f0:8", ["const:b0ee90:8", "const:4:8"]]
+ 00b0ee90 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b0ee4c bytes c5300394
+ 00b0ee90 bytes c8300394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e20e0965de4a5d7342eb8fae86344c4b"></a>

### [`00b0ee84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ee84.md) → [`00b0eec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eec8.md) _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0eeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ee84.md#insn-00b0eeb0) · [`00b0eebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ee84.md#insn-00b0eebc) · [`00b0eecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ee84.md#insn-00b0eecc)
- 新版 `00b0eef4`（命令位置の公開資料なし） · `00b0ef00`（命令位置の公開資料なし） · `00b0ef10`（命令位置の公開資料なし）

~~~diff
- 00b0eeb0 ["INT_ADD", "register:40f0:8", ["const:b0eeb0:8", "const:4:8"]]
- 00b0eeb0 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b0eef4 ["INT_ADD", "register:40f0:8", ["const:b0eef4:8", "const:4:8"]]
+ 00b0eef4 ["CALL", null, ["callee:00bdb260:8"]]
- 00b0eeb0 bytes d8300394
+ 00b0eef4 bytes db300394
- 00b0eebc ["INT_ADD", "register:40f0:8", ["const:b0eebc:8", "const:4:8"]]
- 00b0eebc ["CALL", null, ["callee:00bdf9d0:8"]]
+ 00b0ef00 ["INT_ADD", "register:40f0:8", ["const:b0ef00:8", "const:4:8"]]
+ 00b0ef00 ["CALL", null, ["callee:00bdf9d0:8"]]
- 00b0eebc bytes b1420394
+ 00b0ef00 bytes b4420394
- 00b0eecc ["INT_ADD", "register:40f0:8", ["const:b0eecc:8", "const:4:8"]]
- 00b0eecc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0ef10 ["INT_ADD", "register:40f0:8", ["const:b0ef10:8", "const:4:8"]]
+ 00b0ef10 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0eecc bytes 51300394
+ 00b0ef10 bytes 54300394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87e228feeaac7031c70e37c0d53464aa"></a>

### [`00b0eef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eef4.md) → [`00b0ef38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ef38.md) _ZN11flatbuffers6Parser5ErrorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ef28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eef4.md#insn-00b0ef28) · [`00b0ef34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eef4.md#insn-00b0ef34) · [`00b0ef44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eef4.md#insn-00b0ef44)
- 新版 `00b0ef6c`（命令位置の公開資料なし） · `00b0ef78`（命令位置の公開資料なし） · `00b0ef88`（命令位置の公開資料なし）

~~~diff
- 00b0ef28 ["INT_ADD", "register:40f0:8", ["const:b0ef28:8", "const:4:8"]]
- 00b0ef28 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b0ef6c ["INT_ADD", "register:40f0:8", ["const:b0ef6c:8", "const:4:8"]]
+ 00b0ef6c ["CALL", null, ["callee:00bdb260:8"]]
- 00b0ef28 bytes ba300394
+ 00b0ef6c bytes bd300394
- 00b0ef34 ["INT_ADD", "register:40f0:8", ["const:b0ef34:8", "const:4:8"]]
- 00b0ef34 ["CALL", null, ["callee:00bdf9d0:8"]]
+ 00b0ef78 ["INT_ADD", "register:40f0:8", ["const:b0ef78:8", "const:4:8"]]
+ 00b0ef78 ["CALL", null, ["callee:00bdf9d0:8"]]
- 00b0ef34 bytes 93420394
+ 00b0ef78 bytes 96420394
- 00b0ef44 ["INT_ADD", "register:40f0:8", ["const:b0ef44:8", "const:4:8"]]
- 00b0ef44 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b0ef88 ["INT_ADD", "register:40f0:8", ["const:b0ef88:8", "const:4:8"]]
+ 00b0ef88 ["CALL", null, ["callee:00bdb060:8"]]
- 00b0ef44 bytes 33300394
+ 00b0ef88 bytes 36300394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e485530b953b8a9da4a1531572e53439"></a>

### [`00b0f0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f0ac.md) → [`00b0f0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f0f0.md) _ZNK11flatbuffers9Namespace21GetFullyQualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc20.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc70.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0f1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f0ac.md#insn-00b0f1c0) · [`00b0f254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f0ac.md#insn-00b0f254) · [`00b0f278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f0ac.md#insn-00b0f278)
- 新版 `00b0f204`（命令位置の公開資料なし） · `00b0f298`（命令位置の公開資料なし） · `00b0f2bc`（命令位置の公開資料なし）

~~~diff
- 00b0f1c0 ["INT_ADD", "register:40f0:8", ["const:b0f1c0:8", "const:4:8"]]
- 00b0f1c0 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b0f204 ["INT_ADD", "register:40f0:8", ["const:b0f204:8", "const:4:8"]]
+ 00b0f204 ["CALL", null, ["callee:00bdda90:8"]]
- 00b0f1c0 bytes 203a0394
+ 00b0f204 bytes 233a0394
- 00b0f254 ["INT_ADD", "register:40f0:8", ["const:b0f254:8", "const:4:8"]]
- 00b0f254 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b0f298 ["INT_ADD", "register:40f0:8", ["const:b0f298:8", "const:4:8"]]
+ 00b0f298 ["CALL", null, ["callee:00bdb040:8"]]
- 00b0f254 bytes 672f0394
+ 00b0f298 bytes 6a2f0394
- 00b0f278 ["INT_ADD", "register:40f0:8", ["const:b0f278:8", "const:4:8"]]
- 00b0f278 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b0f2bc ["INT_ADD", "register:40f0:8", ["const:b0f2bc:8", "const:4:8"]]
+ 00b0f2bc ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b0f278 bytes ba2f0394
+ 00b0f2bc bytes bd2f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64272ed5e0b83099bfaaa73673ad7e8a"></a>

### [`00b10bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10bc8.md) → [`00b10c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10c0c.md) _ZN11flatbuffers6ToUTF8EjPNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa00.md) · 呼出先 1件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)
- 新版 呼出元 1件 [`00bdfa50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa50.md) · 呼出先 1件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b10cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10bc8.md#insn-00b10cb4) · [`00b10d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10bc8.md#insn-00b10d80)
- 新版 `00b10cf8`（命令位置の公開資料なし） · `00b10dc4`（命令位置の公開資料なし）

~~~diff
- 00b10cb4 ["INT_ADD", "register:40f0:8", ["const:b10cb4:8", "const:4:8"]]
- 00b10cb4 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b10cf8 ["INT_ADD", "register:40f0:8", ["const:b10cf8:8", "const:4:8"]]
+ 00b10cf8 ["CALL", null, ["callee:00bdda90:8"]]
- 00b10cb4 bytes 63330394
+ 00b10cf8 bytes 66330394
- 00b10d80 ["INT_ADD", "register:40f0:8", ["const:b10d80:8", "const:4:8"]]
- 00b10d80 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b10dc4 ["INT_ADD", "register:40f0:8", ["const:b10dc4:8", "const:4:8"]]
+ 00b10dc4 ["CALL", null, ["callee:00bdda90:8"]]
- 00b10d80 bytes 30330394
+ 00b10dc4 bytes 33330394
~~~


<a id="compare-9f9e2fc1308eec137239e238c8e9b6e5"></a>

### [`00b10dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10dd4.md) → [`00b10e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10e18.md) _ZNK11flatbuffers6Parser7IsIdentEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b10df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10dd4.md#insn-00b10df8) · [`00b10e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10dd4.md#insn-00b10e3c) · [`00b10e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10dd4.md#insn-00b10e64)
- 新版 `00b10e3c`（命令位置の公開資料なし） · `00b10e80`（命令位置の公開資料なし） · `00b10ea8`（命令位置の公開資料なし）

~~~diff
- 00b10df8 ["INT_ADD", "register:40f0:8", ["const:b10df8:8", "const:4:8"]]
- 00b10df8 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b10e3c ["INT_ADD", "register:40f0:8", ["const:b10e3c:8", "const:4:8"]]
+ 00b10e3c ["CALL", null, ["callee:00bdb190:8"]]
- 00b10df8 bytes d2280394
+ 00b10e3c bytes d5280394
- 00b10e3c ["INT_ADD", "register:40f0:8", ["const:b10e3c:8", "const:4:8"]]
- 00b10e3c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b10e80 ["INT_ADD", "register:40f0:8", ["const:b10e80:8", "const:4:8"]]
+ 00b10e80 ["CALL", null, ["callee:00bdb200:8"]]
- 00b10e3c bytes dd280394
+ 00b10e80 bytes e0280394
- 00b10e64 ["INT_ADD", "register:40f0:8", ["const:b10e64:8", "const:4:8"]]
- 00b10e64 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b10ea8 ["INT_ADD", "register:40f0:8", ["const:b10ea8:8", "const:4:8"]]
+ 00b10ea8 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b10e64 bytes 03350394
+ 00b10ea8 bytes 06350394
~~~


<a id="compare-c7559c85ab96120d6d621eb9e24f31a6"></a>

### [`00b11328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11328.md) → [`00b1136c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1136c.md) _ZN11flatbuffers6Parser10LookupEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdfc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc20.md) [`00bdfc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc70.md) [`00bdfca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b11390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11328.md#insn-00b11390) · [`00b1139c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11328.md#insn-00b1139c) · [`00b113b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11328.md#insn-00b113b8)
- 新版 `00b113d4`（命令位置の公開資料なし） · `00b113e0`（命令位置の公開資料なし） · `00b113fc`（命令位置の公開資料なし）

~~~diff
- 00b11390 ["INT_ADD", "register:40f0:8", ["const:b11390:8", "const:4:8"]]
- 00b11390 ["CALL", null, ["callee:00bdfc70:8"]]
+ 00b113d4 ["INT_ADD", "register:40f0:8", ["const:b113d4:8", "const:4:8"]]
+ 00b113d4 ["CALL", null, ["callee:00bdfc70:8"]]
- 00b11390 bytes 243a0394
+ 00b113d4 bytes 273a0394
- 00b1139c ["INT_ADD", "register:40f0:8", ["const:b1139c:8", "const:4:8"]]
- 00b1139c ["CALL", null, ["callee:00bdfca0:8"]]
+ 00b113e0 ["INT_ADD", "register:40f0:8", ["const:b113e0:8", "const:4:8"]]
+ 00b113e0 ["CALL", null, ["callee:00bdfca0:8"]]
- 00b1139c bytes 2d3a0394
+ 00b113e0 bytes 303a0394
- 00b113b8 ["INT_ADD", "register:40f0:8", ["const:b113b8:8", "const:4:8"]]
- 00b113b8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b113fc ["INT_ADD", "register:40f0:8", ["const:b113fc:8", "const:4:8"]]
+ 00b113fc ["CALL", null, ["callee:00bdb060:8"]]
- 00b113b8 bytes 16270394
+ 00b113fc bytes 19270394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fc8b5cc681b5475d2eee1f6475f380a"></a>

### [`00b11418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11418.md) → [`00b1145c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1145c.md) _ZNK11flatbuffers6Parser12LookupStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdfc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdfcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1142c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11418.md#insn-00b1142c)
- 新版 `00b11470`（命令位置の公開資料なし）

~~~diff
- 00b1142c ["INT_ADD", "register:40f0:8", ["const:b1142c:8", "const:4:8"]]
- 00b1142c ["CALL", null, ["callee:00bdfcd0:8"]]
+ 00b11470 ["INT_ADD", "register:40f0:8", ["const:b11470:8", "const:4:8"]]
+ 00b11470 ["CALL", null, ["callee:00bdfcd0:8"]]
- 00b1142c bytes 153a0394
+ 00b11470 bytes 183a0394
~~~


<a id="compare-9594c0db32f1f3c45ec223f8bbd2b8b6"></a>

### [`00b11464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11464.md) → [`00b114a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b114a8.md) _ZN11flatbuffers6Parser14ParseTypeIdentERNS_4TypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf820.md) · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf870.md) · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b114fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11464.md#insn-00b114fc) · [`00b1151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11464.md#insn-00b1151c) · [`00b11530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11464.md#insn-00b11530)
- 新版 `00b11540`（命令位置の公開資料なし） · `00b11560`（命令位置の公開資料なし） · `00b11574`（命令位置の公開資料なし）

~~~diff
- 00b114fc ["INT_ADD", "register:40f0:8", ["const:b114fc:8", "const:4:8"]]
- 00b114fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b11540 ["INT_ADD", "register:40f0:8", ["const:b11540:8", "const:4:8"]]
+ 00b11540 ["CALL", null, ["callee:00bdb040:8"]]
- 00b114fc bytes bd260394
+ 00b11540 bytes c0260394
- 00b1151c ["INT_ADD", "register:40f0:8", ["const:b1151c:8", "const:4:8"]]
- 00b1151c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b11560 ["INT_ADD", "register:40f0:8", ["const:b11560:8", "const:4:8"]]
+ 00b11560 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b1151c bytes 11270394
+ 00b11560 bytes 14270394
- 00b11530 ["INT_ADD", "register:40f0:8", ["const:b11530:8", "const:4:8"]]
- 00b11530 ["CALL", null, ["callee:00bdf9b0:8"]]
+ 00b11574 ["INT_ADD", "register:40f0:8", ["const:b11574:8", "const:4:8"]]
+ 00b11574 ["CALL", null, ["callee:00bdf9b0:8"]]
- 00b11530 bytes 0c390394
+ 00b11574 bytes 0f390394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b22d294a0598da58f8a99cc6e0360fb9"></a>

### [`00b12624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12624.md) → [`00b12668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12668.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf210.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf260.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b126b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12624.md#insn-00b126b4) · [`00b126c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12624.md#insn-00b126c0) · [`00b126e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12624.md#insn-00b126e8)
- 新版 `00b126f8`（命令位置の公開資料なし） · `00b12704`（命令位置の公開資料なし） · `00b1272c`（命令位置の公開資料なし）

~~~diff
- 00b126b4 ["INT_ADD", "register:40f0:8", ["const:b126b4:8", "const:4:8"]]
- 00b126b4 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b126f8 ["INT_ADD", "register:40f0:8", ["const:b126f8:8", "const:4:8"]]
+ 00b126f8 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b126b4 bytes ef2e0394
+ 00b126f8 bytes f22e0394
- 00b126c0 ["INT_ADD", "register:40f0:8", ["const:b126c0:8", "const:4:8"]]
- 00b126c0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b12704 ["INT_ADD", "register:40f0:8", ["const:b12704:8", "const:4:8"]]
+ 00b12704 ["CALL", null, ["callee:00bdb040:8"]]
- 00b126c0 bytes 4c220394
+ 00b12704 bytes 4f220394
- 00b126e8 ["INT_ADD", "register:40f0:8", ["const:b126e8:8", "const:4:8"]]
- 00b126e8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b1272c ["INT_ADD", "register:40f0:8", ["const:b1272c:8", "const:4:8"]]
+ 00b1272c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b126e8 bytes 9e220394
+ 00b1272c bytes a1220394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff0b19dc273ae4aedcb55976f6565307"></a>

### [`00b14e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md) → [`00b14ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b14/00b14ed4.md) _ZNK11flatbuffers7EnumDef11FindByValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfbd0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf590.md) [`00bdf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5a0.md)
- 新版 呼出元 1件 [`00bdfc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc20.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5e0.md) [`00bdf5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b14ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md#insn-00b14ee0) · [`00b14f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md#insn-00b14f34) · [`00b14fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md#insn-00b14fc4)
- 新版 `00b14f24`（命令位置の公開資料なし） · `00b14f78`（命令位置の公開資料なし） · `00b15008`（命令位置の公開資料なし）

~~~diff
- 00b14ee0 ["INT_ADD", "register:40f0:8", ["const:b14ee0:8", "const:4:8"]]
- 00b14ee0 ["CALL", null, ["callee:00bdf5f0:8"]]
+ 00b14f24 ["INT_ADD", "register:40f0:8", ["const:b14f24:8", "const:4:8"]]
+ 00b14f24 ["CALL", null, ["callee:00bdf5f0:8"]]
- 00b14ee0 bytes b0290394
+ 00b14f24 bytes b3290394
- 00b14f34 ["INT_ADD", "register:40f0:8", ["const:b14f34:8", "const:4:8"]]
- 00b14f34 ["CALL", null, ["callee:00bdf5e0:8"]]
+ 00b14f78 ["INT_ADD", "register:40f0:8", ["const:b14f78:8", "const:4:8"]]
+ 00b14f78 ["CALL", null, ["callee:00bdf5e0:8"]]
- 00b14f34 bytes 97290394
+ 00b14f78 bytes 9a290394
- 00b14fc4 ["INT_ADD", "register:40f0:8", ["const:b14fc4:8", "const:4:8"]]
- 00b14fc4 ["CALL", null, ["callee:00bdb090:8"]]
+ 00b15008 ["INT_ADD", "register:40f0:8", ["const:b15008:8", "const:4:8"]]
+ 00b15008 ["CALL", null, ["callee:00bdb090:8"]]
- 00b14fc4 bytes 1f180394
+ 00b15008 bytes 22180394
~~~


<a id="compare-b0f68ba0408f8e5d5047c8cb860de8c0"></a>

### [`00b1531c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1531c.md) → [`00b15360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15360.md) _ZN11flatbuffers11SymbolTableINS_5ValueEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1d0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf220.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b153ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1531c.md#insn-00b153ac) · [`00b153b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1531c.md#insn-00b153b8) · [`00b153e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1531c.md#insn-00b153e0)
- 新版 `00b153f0`（命令位置の公開資料なし） · `00b153fc`（命令位置の公開資料なし） · `00b15424`（命令位置の公開資料なし）

~~~diff
- 00b153ac ["INT_ADD", "register:40f0:8", ["const:b153ac:8", "const:4:8"]]
- 00b153ac ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b153f0 ["INT_ADD", "register:40f0:8", ["const:b153f0:8", "const:4:8"]]
+ 00b153f0 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b153ac bytes b1230394
+ 00b153f0 bytes b4230394
- 00b153b8 ["INT_ADD", "register:40f0:8", ["const:b153b8:8", "const:4:8"]]
- 00b153b8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b153fc ["INT_ADD", "register:40f0:8", ["const:b153fc:8", "const:4:8"]]
+ 00b153fc ["CALL", null, ["callee:00bdb040:8"]]
- 00b153b8 bytes 0e170394
+ 00b153fc bytes 11170394
- 00b153e0 ["INT_ADD", "register:40f0:8", ["const:b153e0:8", "const:4:8"]]
- 00b153e0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b15424 ["INT_ADD", "register:40f0:8", ["const:b15424:8", "const:4:8"]]
+ 00b15424 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b153e0 bytes 60170394
+ 00b15424 bytes 63170394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024445b09577d76037eba1a10c757aa3"></a>

### [`00b154d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b154d4.md) → [`00b15518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15518.md) _ZN11flatbuffers6Parser11ParseStringERNS_5ValueE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf750.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7a0.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b154d4.md#insn-00b1556c) · [`00b1558c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b154d4.md#insn-00b1558c) · [`00b155a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b154d4.md#insn-00b155a0)
- 新版 `00b155b0`（命令位置の公開資料なし） · `00b155d0`（命令位置の公開資料なし） · `00b155e4`（命令位置の公開資料なし）

~~~diff
- 00b1556c ["INT_ADD", "register:40f0:8", ["const:b1556c:8", "const:4:8"]]
- 00b1556c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b155b0 ["INT_ADD", "register:40f0:8", ["const:b155b0:8", "const:4:8"]]
+ 00b155b0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b1556c bytes a1160394
+ 00b155b0 bytes a4160394
- 00b1558c ["INT_ADD", "register:40f0:8", ["const:b1558c:8", "const:4:8"]]
- 00b1558c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b155d0 ["INT_ADD", "register:40f0:8", ["const:b155d0:8", "const:4:8"]]
+ 00b155d0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b1558c bytes f5160394
+ 00b155d0 bytes f8160394
- 00b155a0 ["INT_ADD", "register:40f0:8", ["const:b155a0:8", "const:4:8"]]
- 00b155a0 ["CALL", null, ["callee:00bdf9b0:8"]]
+ 00b155e4 ["INT_ADD", "register:40f0:8", ["const:b155e4:8", "const:4:8"]]
+ 00b155e4 ["CALL", null, ["callee:00bdf9b0:8"]]
- 00b155a0 bytes f0280394
+ 00b155e4 bytes f3280394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f230bc0eae0314b368bc4e43d03522"></a>

### [`00b157e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b157e8.md) → [`00b1582c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1582c.md) _ZN11flatbuffers6Parser10ParseCommaEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdf9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b15808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b157e8.md#insn-00b15808)
- 新版 `00b1584c`（命令位置の公開資料なし）

~~~diff
- 00b15808 ["INT_ADD", "register:40f0:8", ["const:b15808:8", "const:4:8"]]
- 00b15808 ["CALL", null, ["callee:00bdf9b0:8"]]
+ 00b1584c ["INT_ADD", "register:40f0:8", ["const:b1584c:8", "const:4:8"]]
+ 00b1584c ["CALL", null, ["callee:00bdf9b0:8"]]
- 00b15808 bytes 56280394
+ 00b1584c bytes 59280394
~~~


<a id="compare-7aa33226e2f19d6dbdef3697b30726e0"></a>

### [`00b16844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md) → [`00b16888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md) _ZN11flatbuffers6Parser16SkipAnyJsonValueEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b16844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md) [`00bdf8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8b0.md) · 呼出先 9件 [`00b16844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 2件 [`00b16888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md) [`00bdf900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf900.md) · 呼出先 9件 [`00b16888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b16898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md#insn-00b16898) · [`00b168d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md#insn-00b168d0) · [`00b16950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md#insn-00b16950)
- 新版 `00b168dc`（命令位置の公開資料なし） · `00b16914`（命令位置の公開資料なし） · `00b16994`（命令位置の公開資料なし）

~~~diff
- 00b16898 ["INT_ADD", "register:40f0:8", ["const:b16898:8", "const:4:8"]]
- 00b16898 ["CALL", null, ["callee:00bdf970:8"]]
+ 00b168dc ["INT_ADD", "register:40f0:8", ["const:b168dc:8", "const:4:8"]]
+ 00b168dc ["CALL", null, ["callee:00bdf970:8"]]
- 00b16898 bytes 22240394
+ 00b168dc bytes 25240394
- 00b168d0 ["INT_ADD", "register:40f0:8", ["const:b168d0:8", "const:4:8"]]
- 00b168d0 ["CALL", null, ["callee:00bdf9b0:8"]]
+ 00b16914 ["INT_ADD", "register:40f0:8", ["const:b16914:8", "const:4:8"]]
+ 00b16914 ["CALL", null, ["callee:00bdf9b0:8"]]
- 00b168d0 bytes 24240394
+ 00b16914 bytes 27240394
- 00b16950 ["INT_ADD", "register:40f0:8", ["const:b16950:8", "const:4:8"]]
- 00b16950 ["CALL", null, ["callee:00bde230:8"]]
+ 00b16994 ["INT_ADD", "register:40f0:8", ["const:b16994:8", "const:4:8"]]
+ 00b16994 ["CALL", null, ["callee:00bde230:8"]]
- 00b16950 bytes 241e0394
+ 00b16994 bytes 271e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7949dd4881e8c46af23b30d0702ebb6e"></a>

### [`00b1a0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a0a4.md) → [`00b1a0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a0e8.md) _ZN11flatbuffers6Parser15SerializeStructERNS_17FlatBufferBuilderERKNS_9StructDefERKNS_5ValueE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf840.md) · 呼出先 2件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf890.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1a108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a0a4.md#insn-00b1a108) · [`00b1a18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a0a4.md#insn-00b1a18c) · [`00b1a1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a0a4.md#insn-00b1a1a4)
- 新版 `00b1a14c`（命令位置の公開資料なし） · `00b1a1d0`（命令位置の公開資料なし） · `00b1a1e8`（命令位置の公開資料なし）

~~~diff
- 00b1a108 ["INT_ADD", "register:40f0:8", ["const:b1a108:8", "const:4:8"]]
- 00b1a108 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1a14c ["INT_ADD", "register:40f0:8", ["const:b1a14c:8", "const:4:8"]]
+ 00b1a14c ["CALL", null, ["callee:00bdf390:8"]]
- 00b1a108 bytes 8e140394
+ 00b1a14c bytes 91140394
- 00b1a18c ["INT_ADD", "register:40f0:8", ["const:b1a18c:8", "const:4:8"]]
- 00b1a18c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1a1d0 ["INT_ADD", "register:40f0:8", ["const:b1a1d0:8", "const:4:8"]]
+ 00b1a1d0 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1a18c bytes 6d140394
+ 00b1a1d0 bytes 70140394
- 00b1a1a4 ["INT_ADD", "register:40f0:8", ["const:b1a1a4:8", "const:4:8"]]
- 00b1a1a4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b1a1e8 ["INT_ADD", "register:40f0:8", ["const:b1a1e8:8", "const:4:8"]]
+ 00b1a1e8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b1a1a4 bytes ef030394
+ 00b1a1e8 bytes f2030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7a76a0df22a501fe4c6352167e3bbc2"></a>

### [`00b1a21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a21c.md) → [`00b1a260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a260.md) _ZN11flatbuffers17FlatBufferBuilder10AddElementIhEEvtT_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf360.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3b0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1a270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a21c.md#insn-00b1a270) · [`00b1a2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a21c.md#insn-00b1a2a8)
- 新版 `00b1a2b4`（命令位置の公開資料なし） · `00b1a2ec`（命令位置の公開資料なし）

~~~diff
- 00b1a270 ["INT_ADD", "register:40f0:8", ["const:b1a270:8", "const:4:8"]]
- 00b1a270 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1a2b4 ["INT_ADD", "register:40f0:8", ["const:b1a2b4:8", "const:4:8"]]
+ 00b1a2b4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1a270 bytes 34140394
+ 00b1a2b4 bytes 37140394
- 00b1a2a8 ["INT_ADD", "register:40f0:8", ["const:b1a2a8:8", "const:4:8"]]
- 00b1a2a8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1a2ec ["INT_ADD", "register:40f0:8", ["const:b1a2ec:8", "const:4:8"]]
+ 00b1a2ec ["CALL", null, ["callee:00bdf390:8"]]
- 00b1a2a8 bytes 26140394
+ 00b1a2ec bytes 29140394
~~~


<a id="compare-3796d04f8fde03673dc42418c48ef25b"></a>

### [`00b1a75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a75c.md) → [`00b1a7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a7a0.md) _ZN11flatbuffers17FlatBufferBuilder10AddElementIaEEvtT_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf350.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3a0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1a7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a75c.md#insn-00b1a7b0) · [`00b1a7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a75c.md#insn-00b1a7e8)
- 新版 `00b1a7f4`（命令位置の公開資料なし） · `00b1a82c`（命令位置の公開資料なし）

~~~diff
- 00b1a7b0 ["INT_ADD", "register:40f0:8", ["const:b1a7b0:8", "const:4:8"]]
- 00b1a7b0 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1a7f4 ["INT_ADD", "register:40f0:8", ["const:b1a7f4:8", "const:4:8"]]
+ 00b1a7f4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1a7b0 bytes e4120394
+ 00b1a7f4 bytes e7120394
- 00b1a7e8 ["INT_ADD", "register:40f0:8", ["const:b1a7e8:8", "const:4:8"]]
- 00b1a7e8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1a82c ["INT_ADD", "register:40f0:8", ["const:b1a82c:8", "const:4:8"]]
+ 00b1a82c ["CALL", null, ["callee:00bdf390:8"]]
- 00b1a7e8 bytes d6120394
+ 00b1a82c bytes d9120394
~~~


<a id="compare-1deece168a16d71231a72351f89c4521"></a>

### [`00b1b0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b0f0.md) → [`00b1b134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b134.md) _ZN11flatbuffers17FlatBufferBuilder10AddElementItEEvtT_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf370.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3c0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1b160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b0f0.md#insn-00b1b160) · [`00b1b19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b0f0.md#insn-00b1b19c) · [`00b1b1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b0f0.md#insn-00b1b1d0)
- 新版 `00b1b1a4`（命令位置の公開資料なし） · `00b1b1e0`（命令位置の公開資料なし） · `00b1b214`（命令位置の公開資料なし）

~~~diff
- 00b1b160 ["INT_ADD", "register:40f0:8", ["const:b1b160:8", "const:4:8"]]
- 00b1b160 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1b1a4 ["INT_ADD", "register:40f0:8", ["const:b1b1a4:8", "const:4:8"]]
+ 00b1b1a4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1b160 bytes 78100394
+ 00b1b1a4 bytes 7b100394
- 00b1b19c ["INT_ADD", "register:40f0:8", ["const:b1b19c:8", "const:4:8"]]
- 00b1b19c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1b1e0 ["INT_ADD", "register:40f0:8", ["const:b1b1e0:8", "const:4:8"]]
+ 00b1b1e0 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1b19c bytes 69100394
+ 00b1b1e0 bytes 6c100394
- 00b1b1d0 ["INT_ADD", "register:40f0:8", ["const:b1b1d0:8", "const:4:8"]]
- 00b1b1d0 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1b214 ["INT_ADD", "register:40f0:8", ["const:b1b214:8", "const:4:8"]]
+ 00b1b214 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1b1d0 bytes 5c100394
+ 00b1b214 bytes 5f100394
~~~


<a id="compare-9ac8ab62e5af0f6d2e7e0b262335b4de"></a>

### [`00b1b684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b684.md) → [`00b1b6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b6c8.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIiEEjT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf470.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1b6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b684.md#insn-00b1b6e0) · [`00b1b73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b684.md#insn-00b1b73c)
- 新版 `00b1b724`（命令位置の公開資料なし） · `00b1b780`（命令位置の公開資料なし）

~~~diff
- 00b1b6e0 ["INT_ADD", "register:40f0:8", ["const:b1b6e0:8", "const:4:8"]]
- 00b1b6e0 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1b724 ["INT_ADD", "register:40f0:8", ["const:b1b724:8", "const:4:8"]]
+ 00b1b724 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1b6e0 bytes 180f0394
+ 00b1b724 bytes 1b0f0394
- 00b1b73c ["INT_ADD", "register:40f0:8", ["const:b1b73c:8", "const:4:8"]]
- 00b1b73c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1b780 ["INT_ADD", "register:40f0:8", ["const:b1b780:8", "const:4:8"]]
+ 00b1b780 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1b73c bytes 010f0394
+ 00b1b780 bytes 040f0394
~~~


<a id="compare-5fcbd503ec4bd60ed7eeae29dadbe4aa"></a>

### [`00b1b770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b770.md) → [`00b1b7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b7b4.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIjEEjT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1b7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b770.md#insn-00b1b7cc) · [`00b1b828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b770.md#insn-00b1b828)
- 新版 `00b1b810`（命令位置の公開資料なし） · `00b1b86c`（命令位置の公開資料なし）

~~~diff
- 00b1b7cc ["INT_ADD", "register:40f0:8", ["const:b1b7cc:8", "const:4:8"]]
- 00b1b7cc ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1b810 ["INT_ADD", "register:40f0:8", ["const:b1b810:8", "const:4:8"]]
+ 00b1b810 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1b7cc bytes dd0e0394
+ 00b1b810 bytes e00e0394
- 00b1b828 ["INT_ADD", "register:40f0:8", ["const:b1b828:8", "const:4:8"]]
- 00b1b828 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1b86c ["INT_ADD", "register:40f0:8", ["const:b1b86c:8", "const:4:8"]]
+ 00b1b86c ["CALL", null, ["callee:00bdf390:8"]]
- 00b1b828 bytes c60e0394
+ 00b1b86c bytes c90e0394
~~~


<a id="compare-8f180dbc709e8769cf98a6dd4a06e0b3"></a>

### [`00b1bc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bc3c.md) → [`00b1bc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bc80.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIlEEjT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf490.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1bc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bc3c.md#insn-00b1bc98) · [`00b1bcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bc3c.md#insn-00b1bcf4)
- 新版 `00b1bcdc`（命令位置の公開資料なし） · `00b1bd38`（命令位置の公開資料なし）

~~~diff
- 00b1bc98 ["INT_ADD", "register:40f0:8", ["const:b1bc98:8", "const:4:8"]]
- 00b1bc98 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1bcdc ["INT_ADD", "register:40f0:8", ["const:b1bcdc:8", "const:4:8"]]
+ 00b1bcdc ["CALL", null, ["callee:00bdf390:8"]]
- 00b1bc98 bytes aa0d0394
+ 00b1bcdc bytes ad0d0394
- 00b1bcf4 ["INT_ADD", "register:40f0:8", ["const:b1bcf4:8", "const:4:8"]]
- 00b1bcf4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1bd38 ["INT_ADD", "register:40f0:8", ["const:b1bd38:8", "const:4:8"]]
+ 00b1bd38 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1bcf4 bytes 930d0394
+ 00b1bd38 bytes 960d0394
~~~


<a id="compare-9928a1415a5a53adb06a3ac065a47fc2"></a>

### [`00b1c158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c158.md) → [`00b1c19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c19c.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementImEEjT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf450.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4a0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c158.md#insn-00b1c1b4) · [`00b1c210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c158.md#insn-00b1c210)
- 新版 `00b1c1f8`（命令位置の公開資料なし） · `00b1c254`（命令位置の公開資料なし）

~~~diff
- 00b1c1b4 ["INT_ADD", "register:40f0:8", ["const:b1c1b4:8", "const:4:8"]]
- 00b1c1b4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c1f8 ["INT_ADD", "register:40f0:8", ["const:b1c1f8:8", "const:4:8"]]
+ 00b1c1f8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c1b4 bytes 630c0394
+ 00b1c1f8 bytes 660c0394
- 00b1c210 ["INT_ADD", "register:40f0:8", ["const:b1c210:8", "const:4:8"]]
- 00b1c210 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c254 ["INT_ADD", "register:40f0:8", ["const:b1c254:8", "const:4:8"]]
+ 00b1c254 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c210 bytes 4c0c0394
+ 00b1c254 bytes 4f0c0394
~~~


<a id="compare-8718d45de9201d0970c1b1145560fc35"></a>

### [`00b1c42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c42c.md) → [`00b1c470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c470.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIfEEjT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf410.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf460.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c42c.md#insn-00b1c488) · [`00b1c4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c42c.md#insn-00b1c4e4)
- 新版 `00b1c4cc`（命令位置の公開資料なし） · `00b1c528`（命令位置の公開資料なし）

~~~diff
- 00b1c488 ["INT_ADD", "register:40f0:8", ["const:b1c488:8", "const:4:8"]]
- 00b1c488 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c4cc ["INT_ADD", "register:40f0:8", ["const:b1c4cc:8", "const:4:8"]]
+ 00b1c4cc ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c488 bytes ae0b0394
+ 00b1c4cc bytes b10b0394
- 00b1c4e4 ["INT_ADD", "register:40f0:8", ["const:b1c4e4:8", "const:4:8"]]
- 00b1c4e4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c528 ["INT_ADD", "register:40f0:8", ["const:b1c528:8", "const:4:8"]]
+ 00b1c528 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c4e4 bytes 970b0394
+ 00b1c528 bytes 9a0b0394
~~~


<a id="compare-d34d2c478dc8948409d1e049d22ad2f2"></a>

### [`00b1c6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c6fc.md) → [`00b1c740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c740.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIdEEjT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf400.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf450.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c6fc.md#insn-00b1c758) · [`00b1c7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c6fc.md#insn-00b1c7b4)
- 新版 `00b1c79c`（命令位置の公開資料なし） · `00b1c7f8`（命令位置の公開資料なし）

~~~diff
- 00b1c758 ["INT_ADD", "register:40f0:8", ["const:b1c758:8", "const:4:8"]]
- 00b1c758 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c79c ["INT_ADD", "register:40f0:8", ["const:b1c79c:8", "const:4:8"]]
+ 00b1c79c ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c758 bytes fa0a0394
+ 00b1c79c bytes fd0a0394
- 00b1c7b4 ["INT_ADD", "register:40f0:8", ["const:b1c7b4:8", "const:4:8"]]
- 00b1c7b4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c7f8 ["INT_ADD", "register:40f0:8", ["const:b1c7f8:8", "const:4:8"]]
+ 00b1c7f8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c7b4 bytes e30a0394
+ 00b1c7f8 bytes e60a0394
~~~


<a id="compare-884eef904388d4664c5f8bdd90e5625c"></a>

### [`00b1c7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c7e8.md) → [`00b1c82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c82c.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetIvEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf580.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5d0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c7e8.md#insn-00b1c84c) · [`00b1c8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c7e8.md#insn-00b1c8bc) · [`00b1c8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c7e8.md#insn-00b1c8dc)
- 新版 `00b1c890`（命令位置の公開資料なし） · `00b1c900`（命令位置の公開資料なし） · `00b1c920`（命令位置の公開資料なし）

~~~diff
- 00b1c84c ["INT_ADD", "register:40f0:8", ["const:b1c84c:8", "const:4:8"]]
- 00b1c84c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c890 ["INT_ADD", "register:40f0:8", ["const:b1c890:8", "const:4:8"]]
+ 00b1c890 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c84c bytes bd0a0394
+ 00b1c890 bytes c00a0394
- 00b1c8bc ["INT_ADD", "register:40f0:8", ["const:b1c8bc:8", "const:4:8"]]
- 00b1c8bc ["CALL", null, ["callee:00bdf480:8"]]
+ 00b1c900 ["INT_ADD", "register:40f0:8", ["const:b1c900:8", "const:4:8"]]
+ 00b1c900 ["CALL", null, ["callee:00bdf480:8"]]
- 00b1c8bc bytes dd0a0394
+ 00b1c900 bytes e00a0394
- 00b1c8dc ["INT_ADD", "register:40f0:8", ["const:b1c8dc:8", "const:4:8"]]
- 00b1c8dc ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c920 ["INT_ADD", "register:40f0:8", ["const:b1c920:8", "const:4:8"]]
+ 00b1c920 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c8dc bytes 990a0394
+ 00b1c920 bytes 9c0a0394
~~~


<a id="compare-d59ae6fd055c235e3c2fec97a9e41419"></a>

### [`00b1c92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c92c.md) → [`00b1c970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c970.md) _ZN11flatbuffers17FlatBufferBuilder8EndTableEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4c0.md) · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md)
- 新版 呼出元 1件 [`00bdf510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf510.md) · 呼出先 4件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c92c.md#insn-00b1c958) · [`00b1c998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c92c.md#insn-00b1c998) · [`00b1c9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c92c.md#insn-00b1c9b0)
- 新版 `00b1c99c`（命令位置の公開資料なし） · `00b1c9dc`（命令位置の公開資料なし） · `00b1c9f4`（命令位置の公開資料なし）

~~~diff
- 00b1c958 ["INT_ADD", "register:40f0:8", ["const:b1c958:8", "const:4:8"]]
- 00b1c958 ["CALL", null, ["callee:00bdf470:8"]]
+ 00b1c99c ["INT_ADD", "register:40f0:8", ["const:b1c99c:8", "const:4:8"]]
+ 00b1c99c ["CALL", null, ["callee:00bdf470:8"]]
- 00b1c958 bytes b20a0394
+ 00b1c99c bytes b50a0394
- 00b1c998 ["INT_ADD", "register:40f0:8", ["const:b1c998:8", "const:4:8"]]
- 00b1c998 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1c9dc ["INT_ADD", "register:40f0:8", ["const:b1c9dc:8", "const:4:8"]]
+ 00b1c9dc ["CALL", null, ["callee:00bdf390:8"]]
- 00b1c998 bytes 6a0a0394
+ 00b1c9dc bytes 6d0a0394
- 00b1c9b0 ["INT_ADD", "register:40f0:8", ["const:b1c9b0:8", "const:4:8"]]
- 00b1c9b0 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b1c9f4 ["INT_ADD", "register:40f0:8", ["const:b1c9f4:8", "const:4:8"]]
+ 00b1c9f4 ["CALL", null, ["callee:00bdb240:8"]]
- 00b1c9b0 bytes 10fa0294
+ 00b1c9f4 bytes 13fa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484dc084b1f6ff487b9740240c5136b3"></a>

### [`00b1caf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1caf4.md) → [`00b1cb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cb38.md) _ZN11flatbuffers17FlatBufferBuilder11StartVectorEmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf470.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)
- 新版 呼出元 1件 [`00bdf4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4c0.md) · 呼出先 1件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1cb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1caf4.md#insn-00b1cb60) · [`00b1cbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1caf4.md#insn-00b1cbec)
- 新版 `00b1cba4`（命令位置の公開資料なし） · `00b1cc30`（命令位置の公開資料なし）

~~~diff
- 00b1cb60 ["INT_ADD", "register:40f0:8", ["const:b1cb60:8", "const:4:8"]]
- 00b1cb60 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1cba4 ["INT_ADD", "register:40f0:8", ["const:b1cba4:8", "const:4:8"]]
+ 00b1cba4 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1cb60 bytes f8090394
+ 00b1cba4 bytes fb090394
- 00b1cbec ["INT_ADD", "register:40f0:8", ["const:b1cbec:8", "const:4:8"]]
- 00b1cbec ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1cc30 ["INT_ADD", "register:40f0:8", ["const:b1cc30:8", "const:4:8"]]
+ 00b1cc30 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1cbec bytes d5090394
+ 00b1cc30 bytes d8090394
~~~


<a id="compare-76cec8b6c6b095ce80a05e78cc9c9ab9"></a>

### [`00b1cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cc40.md) → [`00b1cc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cc84.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIvEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf460.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4b0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1cc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cc40.md#insn-00b1cc9c)
- 新版 `00b1cce0`（命令位置の公開資料なし）

~~~diff
- 00b1cc9c ["INT_ADD", "register:40f0:8", ["const:b1cc9c:8", "const:4:8"]]
- 00b1cc9c ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1cce0 ["INT_ADD", "register:40f0:8", ["const:b1cce0:8", "const:4:8"]]
+ 00b1cce0 ["CALL", null, ["callee:00bdf390:8"]]
- 00b1cc9c bytes a9090394
+ 00b1cce0 bytes ac090394
~~~


<a id="compare-7325224d96877ffd49a7795ab7f3dd29"></a>

### [`00b1d4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d4c4.md) → [`00b1d508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d508.md) _ZN11flatbuffers10IDLOptionsaSERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf110.md) · 呼出先 2件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0040.md)
- 新版 呼出元 1件 [`00bdf160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf160.md) · 呼出先 2件 [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00be0090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1d510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d4c4.md#insn-00b1d510) · [`00b1d534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d4c4.md#insn-00b1d534) · [`00b1d560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d4c4.md#insn-00b1d560)
- 新版 `00b1d554`（命令位置の公開資料なし） · `00b1d578`（命令位置の公開資料なし） · `00b1d5a4`（命令位置の公開資料なし）

~~~diff
- 00b1d510 ["INT_ADD", "register:40f0:8", ["const:b1d510:8", "const:4:8"]]
- 00b1d510 ["CALL", null, ["callee:00bde230:8"]]
+ 00b1d554 ["INT_ADD", "register:40f0:8", ["const:b1d554:8", "const:4:8"]]
+ 00b1d554 ["CALL", null, ["callee:00bde230:8"]]
- 00b1d510 bytes 34030394
+ 00b1d554 bytes 37030394
- 00b1d534 ["INT_ADD", "register:40f0:8", ["const:b1d534:8", "const:4:8"]]
- 00b1d534 ["CALL", null, ["callee:00bde230:8"]]
+ 00b1d578 ["INT_ADD", "register:40f0:8", ["const:b1d578:8", "const:4:8"]]
+ 00b1d578 ["CALL", null, ["callee:00bde230:8"]]
- 00b1d534 bytes 2b030394
+ 00b1d578 bytes 2e030394
- 00b1d560 ["INT_ADD", "register:40f0:8", ["const:b1d560:8", "const:4:8"]]
- 00b1d560 ["CALL", null, ["callee:00bde230:8"]]
+ 00b1d5a4 ["INT_ADD", "register:40f0:8", ["const:b1d5a4:8", "const:4:8"]]
+ 00b1d5a4 ["CALL", null, ["callee:00bde230:8"]]
- 00b1d560 bytes 20030394
+ 00b1d5a4 bytes 23030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96b30b842f90675f975c9582e3b72d1f"></a>

### [`00b1d750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d750.md) → [`00b1d794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d794.md) _ZN11flatbuffers6Parser5ParseEPKcPS2_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf010.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf830.md) [`00bdf8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8f0.md) [`00bdf9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9d0.md) [`00bdfae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfae0.md)
- 新版 呼出元 1件 [`00bdf060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf060.md) · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf880.md) [`00bdf940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf940.md) [`00bdfa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa20.md) [`00bdfb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1d788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d750.md#insn-00b1d788) · [`00b1d7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d750.md#insn-00b1d7ac) · [`00b1d7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d750.md#insn-00b1d7c8)
- 新版 `00b1d7cc`（命令位置の公開資料なし） · `00b1d7f0`（命令位置の公開資料なし） · `00b1d80c`（命令位置の公開資料なし）

~~~diff
- 00b1d788 ["INT_ADD", "register:40f0:8", ["const:b1d788:8", "const:4:8"]]
- 00b1d788 ["CALL", null, ["callee:00bdf880:8"]]
+ 00b1d7cc ["INT_ADD", "register:40f0:8", ["const:b1d7cc:8", "const:4:8"]]
+ 00b1d7cc ["CALL", null, ["callee:00bdf880:8"]]
- 00b1d788 bytes 2a080394
+ 00b1d7cc bytes 2d080394
- 00b1d7ac ["INT_ADD", "register:40f0:8", ["const:b1d7ac:8", "const:4:8"]]
- 00b1d7ac ["CALL", null, ["callee:00bdf940:8"]]
+ 00b1d7f0 ["INT_ADD", "register:40f0:8", ["const:b1d7f0:8", "const:4:8"]]
+ 00b1d7f0 ["CALL", null, ["callee:00bdf940:8"]]
- 00b1d7ac bytes 51080394
+ 00b1d7f0 bytes 54080394
- 00b1d7c8 ["INT_ADD", "register:40f0:8", ["const:b1d7c8:8", "const:4:8"]]
- 00b1d7c8 ["CALL", null, ["callee:00bdfa20:8"]]
+ 00b1d80c ["INT_ADD", "register:40f0:8", ["const:b1d80c:8", "const:4:8"]]
+ 00b1d80c ["CALL", null, ["callee:00bdfa20:8"]]
- 00b1d7c8 bytes 82080394
+ 00b1d80c bytes 85080394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57e1bf3265d16acac9c3a71708c6ee34"></a>

### [`00b1f370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f370.md) → [`00b1f3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f3b4.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf220.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf270.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1f400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f370.md#insn-00b1f400) · [`00b1f40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f370.md#insn-00b1f40c) · [`00b1f434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f370.md#insn-00b1f434)
- 新版 `00b1f444`（命令位置の公開資料なし） · `00b1f450`（命令位置の公開資料なし） · `00b1f478`（命令位置の公開資料なし）

~~~diff
- 00b1f400 ["INT_ADD", "register:40f0:8", ["const:b1f400:8", "const:4:8"]]
- 00b1f400 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b1f444 ["INT_ADD", "register:40f0:8", ["const:b1f444:8", "const:4:8"]]
+ 00b1f444 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b1f400 bytes 9cfb0294
+ 00b1f444 bytes 9ffb0294
- 00b1f40c ["INT_ADD", "register:40f0:8", ["const:b1f40c:8", "const:4:8"]]
- 00b1f40c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b1f450 ["INT_ADD", "register:40f0:8", ["const:b1f450:8", "const:4:8"]]
+ 00b1f450 ["CALL", null, ["callee:00bdb040:8"]]
- 00b1f40c bytes f9ee0294
+ 00b1f450 bytes fcee0294
- 00b1f434 ["INT_ADD", "register:40f0:8", ["const:b1f434:8", "const:4:8"]]
- 00b1f434 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b1f478 ["INT_ADD", "register:40f0:8", ["const:b1f478:8", "const:4:8"]]
+ 00b1f478 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b1f434 bytes 4bef0294
+ 00b1f478 bytes 4eef0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6369099fca6acb6c2c1a704f19eaaa8"></a>

### [`00b1f65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f65c.md) → [`00b1f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f6a0.md) _ZN11flatbuffers7EnumDef16RemoveDuplicatesEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa20.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00bdfa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa70.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1f708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f65c.md#insn-00b1f708) · [`00b1f794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f65c.md#insn-00b1f794) · [`00b1f7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f65c.md#insn-00b1f7a4)
- 新版 `00b1f74c`（命令位置の公開資料なし） · `00b1f7d8`（命令位置の公開資料なし） · `00b1f7e8`（命令位置の公開資料なし）

~~~diff
- 00b1f708 ["INT_ADD", "register:40f0:8", ["const:b1f708:8", "const:4:8"]]
- 00b1f708 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b1f74c ["INT_ADD", "register:40f0:8", ["const:b1f74c:8", "const:4:8"]]
+ 00b1f74c ["CALL", null, ["callee:00bdb060:8"]]
- 00b1f708 bytes 42ee0294
+ 00b1f74c bytes 45ee0294
- 00b1f794 ["INT_ADD", "register:40f0:8", ["const:b1f794:8", "const:4:8"]]
- 00b1f794 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b1f7d8 ["INT_ADD", "register:40f0:8", ["const:b1f7d8:8", "const:4:8"]]
+ 00b1f7d8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b1f794 bytes 1fee0294
+ 00b1f7d8 bytes 22ee0294
- 00b1f7a4 ["INT_ADD", "register:40f0:8", ["const:b1f7a4:8", "const:4:8"]]
- 00b1f7a4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b1f7e8 ["INT_ADD", "register:40f0:8", ["const:b1f7e8:8", "const:4:8"]]
+ 00b1f7e8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b1f7a4 bytes 1bee0294
+ 00b1f7e8 bytes 1eee0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb6005b1a30f74000c8e06a29183946"></a>

### [`00b20abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20abc.md) → [`00b20b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20b00.md) _ZN11flatbuffers6Parser16ParseProtoOptionEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf890.md) · 呼出先 3件 [`00bdf7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7e0.md) [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md) [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md)
- 新版 呼出元 1件 [`00bdf8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8e0.md) · 呼出先 3件 [`00bdf830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf830.md) [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md) [`00bdf9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b20ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20abc.md#insn-00b20ad4) · [`00b20af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20abc.md#insn-00b20af0) · [`00b20b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20abc.md#insn-00b20b0c)
- 新版 `00b20b18`（命令位置の公開資料なし） · `00b20b34`（命令位置の公開資料なし） · `00b20b50`（命令位置の公開資料なし）

~~~diff
- 00b20ad4 ["INT_ADD", "register:40f0:8", ["const:b20ad4:8", "const:4:8"]]
- 00b20ad4 ["CALL", null, ["callee:00bdf970:8"]]
+ 00b20b18 ["INT_ADD", "register:40f0:8", ["const:b20b18:8", "const:4:8"]]
+ 00b20b18 ["CALL", null, ["callee:00bdf970:8"]]
- 00b20ad4 bytes 93fb0294
+ 00b20b18 bytes 96fb0294
- 00b20af0 ["INT_ADD", "register:40f0:8", ["const:b20af0:8", "const:4:8"]]
- 00b20af0 ["CALL", null, ["callee:00bdf830:8"]]
+ 00b20b34 ["INT_ADD", "register:40f0:8", ["const:b20b34:8", "const:4:8"]]
+ 00b20b34 ["CALL", null, ["callee:00bdf830:8"]]
- 00b20af0 bytes 3cfb0294
+ 00b20b34 bytes 3ffb0294
- 00b20b0c ["INT_ADD", "register:40f0:8", ["const:b20b0c:8", "const:4:8"]]
- 00b20b0c ["CALL", null, ["callee:00bdf9b0:8"]]
+ 00b20b50 ["INT_ADD", "register:40f0:8", ["const:b20b50:8", "const:4:8"]]
+ 00b20b50 ["CALL", null, ["callee:00bdf9b0:8"]]
- 00b20b0c bytes 95fb0294
+ 00b20b50 bytes 98fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94257081df71701d14712355a592677d"></a>

### [`00b20e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20e50.md) → [`00b20e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20e94.md) _ZN11flatbuffers11SymbolTableINS_4TypeEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1c0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf210.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b20ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20e50.md#insn-00b20ee0) · [`00b20eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20e50.md#insn-00b20eec) · [`00b20f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20e50.md#insn-00b20f14)
- 新版 `00b20f24`（命令位置の公開資料なし） · `00b20f30`（命令位置の公開資料なし） · `00b20f58`（命令位置の公開資料なし）

~~~diff
- 00b20ee0 ["INT_ADD", "register:40f0:8", ["const:b20ee0:8", "const:4:8"]]
- 00b20ee0 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b20f24 ["INT_ADD", "register:40f0:8", ["const:b20f24:8", "const:4:8"]]
+ 00b20f24 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b20ee0 bytes e4f40294
+ 00b20f24 bytes e7f40294
- 00b20eec ["INT_ADD", "register:40f0:8", ["const:b20eec:8", "const:4:8"]]
- 00b20eec ["CALL", null, ["callee:00bdb040:8"]]
+ 00b20f30 ["INT_ADD", "register:40f0:8", ["const:b20f30:8", "const:4:8"]]
+ 00b20f30 ["CALL", null, ["callee:00bdb040:8"]]
- 00b20eec bytes 41e80294
+ 00b20f30 bytes 44e80294
- 00b20f14 ["INT_ADD", "register:40f0:8", ["const:b20f14:8", "const:4:8"]]
- 00b20f14 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b20f58 ["INT_ADD", "register:40f0:8", ["const:b20f58:8", "const:4:8"]]
+ 00b20f58 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b20f14 bytes 93e80294
+ 00b20f58 bytes 96e80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-084c4f356fa85f1bf485a0d3dfebe984"></a>

### [`00b21008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b21008.md) → [`00b2104c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b2104c.md) _ZN11flatbuffers6Parser11StartStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPPNS_9StructDefE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf780.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bdf8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8d0.md)
- 新版 呼出元 1件 [`00bdf7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7d0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bdf920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b21044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b21008.md#insn-00b21044) · [`00b2107c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b21008.md#insn-00b2107c) · [`00b210ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b21008.md#insn-00b210ac)
- 新版 `00b21088`（命令位置の公開資料なし） · `00b210c0`（命令位置の公開資料なし） · `00b210f0`（命令位置の公開資料なし）

~~~diff
- 00b21044 ["INT_ADD", "register:40f0:8", ["const:b21044:8", "const:4:8"]]
- 00b21044 ["CALL", null, ["callee:00bdf920:8"]]
+ 00b21088 ["INT_ADD", "register:40f0:8", ["const:b21088:8", "const:4:8"]]
+ 00b21088 ["CALL", null, ["callee:00bdf920:8"]]
- 00b21044 bytes 23fa0294
+ 00b21088 bytes 26fa0294
- 00b2107c ["INT_ADD", "register:40f0:8", ["const:b2107c:8", "const:4:8"]]
- 00b2107c ["CALL", null, ["callee:00bde230:8"]]
+ 00b210c0 ["INT_ADD", "register:40f0:8", ["const:b210c0:8", "const:4:8"]]
+ 00b210c0 ["CALL", null, ["callee:00bde230:8"]]
- 00b2107c bytes 59f40294
+ 00b210c0 bytes 5cf40294
- 00b210ac ["INT_ADD", "register:40f0:8", ["const:b210ac:8", "const:4:8"]]
- 00b210ac ["CALL", null, ["callee:00bde230:8"]]
+ 00b210f0 ["INT_ADD", "register:40f0:8", ["const:b210f0:8", "const:4:8"]]
+ 00b210f0 ["CALL", null, ["callee:00bde230:8"]]
- 00b210ac bytes 4df40294
+ 00b210f0 bytes 50f40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea62b365c1c95deeb75e254e5aad224c"></a>

### [`00b2148c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2148c.md) → [`00b214d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b214d0.md) _ZN11flatbuffers6Parser15UniqueNamespaceEPNS_9NamespaceE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf850.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdf8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8a0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b21590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2148c.md#insn-00b21590) · [`00b215f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2148c.md#insn-00b215f4) · [`00b21638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2148c.md#insn-00b21638)
- 新版 `00b215d4`（命令位置の公開資料なし） · `00b21638`（命令位置の公開資料なし） · `00b2167c`（命令位置の公開資料なし）

~~~diff
- 00b21590 ["INT_ADD", "register:40f0:8", ["const:b21590:8", "const:4:8"]]
- 00b21590 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b215d4 ["INT_ADD", "register:40f0:8", ["const:b215d4:8", "const:4:8"]]
+ 00b215d4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b21590 bytes 08e70294
+ 00b215d4 bytes 0be70294
- 00b215f4 ["INT_ADD", "register:40f0:8", ["const:b215f4:8", "const:4:8"]]
- 00b215f4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b21638 ["INT_ADD", "register:40f0:8", ["const:b21638:8", "const:4:8"]]
+ 00b21638 ["CALL", null, ["callee:00bdb060:8"]]
- 00b215f4 bytes 87e60294
+ 00b21638 bytes 8ae60294
- 00b21638 ["INT_ADD", "register:40f0:8", ["const:b21638:8", "const:4:8"]]
- 00b21638 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b2167c ["INT_ADD", "register:40f0:8", ["const:b2167c:8", "const:4:8"]]
+ 00b2167c ["CALL", null, ["callee:00bde2c0:8"]]
- 00b21638 bytes 0ef30294
+ 00b2167c bytes 11f30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b57026fb2909277307974a1c0032b75c"></a>

### [`00b216dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b216dc.md) → [`00b21720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b21720.md) _ZN11flatbuffers6Parser15UnqualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf860.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md)
- 新版 呼出元 1件 [`00bdf8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8b0.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b21714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b216dc.md#insn-00b21714) · [`00b21748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b216dc.md#insn-00b21748) · [`00b21778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b216dc.md#insn-00b21778)
- 新版 `00b21758`（命令位置の公開資料なし） · `00b2178c`（命令位置の公開資料なし） · `00b217bc`（命令位置の公開資料なし）

~~~diff
- 00b21714 ["INT_ADD", "register:40f0:8", ["const:b21714:8", "const:4:8"]]
- 00b21714 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b21758 ["INT_ADD", "register:40f0:8", ["const:b21758:8", "const:4:8"]]
+ 00b21758 ["CALL", null, ["callee:00bdb040:8"]]
- 00b21714 bytes 37e60294
+ 00b21758 bytes 3ae60294
- 00b21748 ["INT_ADD", "register:40f0:8", ["const:b21748:8", "const:4:8"]]
- 00b21748 ["CALL", null, ["callee:00bdb180:8"]]
+ 00b2178c ["INT_ADD", "register:40f0:8", ["const:b2178c:8", "const:4:8"]]
+ 00b2178c ["CALL", null, ["callee:00bdb180:8"]]
- 00b21748 bytes 7ae60294
+ 00b2178c bytes 7de60294
- 00b21778 ["INT_ADD", "register:40f0:8", ["const:b21778:8", "const:4:8"]]
- 00b21778 ["CALL", null, ["callee:00bde970:8"]]
+ 00b217bc ["INT_ADD", "register:40f0:8", ["const:b217bc:8", "const:4:8"]]
+ 00b217bc ["CALL", null, ["callee:00bde970:8"]]
- 00b21778 bytes 6af40294
+ 00b217bc bytes 6df40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7cb53f1269ed096af0d652ec47d43ac"></a>

### [`00b222dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b222dc.md) → [`00b22320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22320.md) FUN_00b22320

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2186c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2186c.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdda90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda90.md) [`00bdfc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc40.md)
- 新版 呼出元 1件 [`00b218b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b218b0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddae0.md) [`00bdfc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b22328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b222dc.md#insn-00b22328) · [`00b2235c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b222dc.md#insn-00b2235c) · [`00b22370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b222dc.md#insn-00b22370)
- 新版 `00b2236c`（命令位置の公開資料なし） · `00b223a0`（命令位置の公開資料なし） · `00b223b4`（命令位置の公開資料なし）

~~~diff
- 00b22328 ["INT_ADD", "register:40f0:8", ["const:b22328:8", "const:4:8"]]
- 00b22328 ["CALL", null, ["callee:00bdfc90:8"]]
+ 00b2236c ["INT_ADD", "register:40f0:8", ["const:b2236c:8", "const:4:8"]]
+ 00b2236c ["CALL", null, ["callee:00bdfc90:8"]]
- 00b22328 bytes 46f60294
+ 00b2236c bytes 49f60294
- 00b2235c ["INT_ADD", "register:40f0:8", ["const:b2235c:8", "const:4:8"]]
- 00b2235c ["CALL", null, ["callee:00bddae0:8"]]
+ 00b223a0 ["INT_ADD", "register:40f0:8", ["const:b223a0:8", "const:4:8"]]
+ 00b223a0 ["CALL", null, ["callee:00bddae0:8"]]
- 00b2235c bytes cded0294
+ 00b223a0 bytes d0ed0294
- 00b22370 ["INT_ADD", "register:40f0:8", ["const:b22370:8", "const:4:8"]]
- 00b22370 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b223b4 ["INT_ADD", "register:40f0:8", ["const:b223b4:8", "const:4:8"]]
+ 00b223b4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b22370 bytes 28e30294
+ 00b223b4 bytes 2be30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

