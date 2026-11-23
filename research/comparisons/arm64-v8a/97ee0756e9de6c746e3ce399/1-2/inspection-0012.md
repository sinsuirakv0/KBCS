# v15.7.3 → v15.7.4 · 要調査の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-1c16f0cb2cf4d9a3747f53aedaef048e"></a>

### [`00b4ffac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4ffac.md) → [`00b4fff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4fff0.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr1

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0530.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0580.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4fff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4ffac.md#insn-00b4fff0) · [`00b50054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4ffac.md#insn-00b50054) · [`00b50208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4ffac.md#insn-00b50208)
- 新版 `00b50034`（命令位置の公開資料なし） · `00b50098`（命令位置の公開資料なし） · `00b5024c`（命令位置の公開資料なし）

~~~diff
- 00b4fff0 ["INT_ADD", "register:40f0:8", ["const:b4fff0:8", "const:4:8"]]
- 00b4fff0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b50034 ["INT_ADD", "register:40f0:8", ["const:b50034:8", "const:4:8"]]
+ 00b50034 ["CALL", null, ["callee:00bdb060:8"]]
- 00b4fff0 bytes 082c0294
+ 00b50034 bytes 0b2c0294
- 00b50054 ["INT_ADD", "register:40f0:8", ["const:b50054:8", "const:4:8"]]
- 00b50054 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b50098 ["INT_ADD", "register:40f0:8", ["const:b50098:8", "const:4:8"]]
+ 00b50098 ["CALL", null, ["callee:00bdb040:8"]]
- 00b50054 bytes e72b0294
+ 00b50098 bytes ea2b0294
- 00b50208 ["INT_ADD", "register:40f0:8", ["const:b50208:8", "const:4:8"]]
- 00b50208 ["CALL", null, ["callee:00bddeb0:8"]]
+ 00b5024c ["INT_ADD", "register:40f0:8", ["const:b5024c:8", "const:4:8"]]
+ 00b5024c ["CALL", null, ["callee:00bddeb0:8"]]
- 00b50208 bytes 16370294
+ 00b5024c bytes 19370294
~~~


<a id="compare-adfd118477476f09dca68dac4601d754"></a>

### [`00b5020c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b5020c.md) → [`00b50250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b50/00b50250.md) _ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be04b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04b0.md) · 呼出先 2件 [`00be04c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04c0.md) [`00be04e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04e0.md)
- 新版 呼出元 1件 [`00be0500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0500.md) · 呼出先 2件 [`00be0510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0510.md) [`00be0530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b503a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b5020c.md#insn-00b503a4) · [`00b503bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b5020c.md#insn-00b503bc)
- 新版 `00b503e8`（命令位置の公開資料なし） · `00b50400`（命令位置の公開資料なし）

~~~diff
- 00b503a4 ["INT_ADD", "register:40f0:8", ["const:b503a4:8", "const:4:8"]]
- 00b503a4 ["CALL", null, ["callee:00be0510:8"]]
+ 00b503e8 ["INT_ADD", "register:40f0:8", ["const:b503e8:8", "const:4:8"]]
+ 00b503e8 ["CALL", null, ["callee:00be0510:8"]]
- 00b503a4 bytes 47400294
+ 00b503e8 bytes 4a400294
- 00b503bc ["INT_ADD", "register:40f0:8", ["const:b503bc:8", "const:4:8"]]
- 00b503bc ["CALL", null, ["callee:00be0530:8"]]
+ 00b50400 ["INT_ADD", "register:40f0:8", ["const:b50400:8", "const:4:8"]]
+ 00b50400 ["CALL", null, ["callee:00be0530:8"]]
- 00b503bc bytes 49400294
+ 00b50400 bytes 4c400294
~~~


<a id="compare-0a5a1f0261a2cb54a7233043167cb7ff"></a>

### [`00b503d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b503d8.md) → [`00b5041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b50/00b5041c.md) _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be04c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04c0.md) · 呼出先 2件 [`00be04d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04d0.md) [`00be04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04f0.md)
- 新版 呼出元 1件 [`00be0510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0510.md) · 呼出先 2件 [`00be0520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0520.md) [`00be0540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b50860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b503d8.md#insn-00b50860) · [`00b50ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b503d8.md#insn-00b50ee0)
- 新版 `00b508a4`（命令位置の公開資料なし） · `00b50f24`（命令位置の公開資料なし）

~~~diff
- 00b50860 ["INT_ADD", "register:40f0:8", ["const:b50860:8", "const:4:8"]]
- 00b50860 ["CALL", null, ["callee:00be0540:8"]]
+ 00b508a4 ["INT_ADD", "register:40f0:8", ["const:b508a4:8", "const:4:8"]]
+ 00b508a4 ["CALL", null, ["callee:00be0540:8"]]
- 00b50860 bytes 243f0294
+ 00b508a4 bytes 273f0294
- 00b50ee0 ["INT_ADD", "register:40f0:8", ["const:b50ee0:8", "const:4:8"]]
- 00b50ee0 ["CALL", null, ["callee:00be0520:8"]]
+ 00b50f24 ["INT_ADD", "register:40f0:8", ["const:b50f24:8", "const:4:8"]]
+ 00b50f24 ["CALL", null, ["callee:00be0520:8"]]
- 00b50ee0 bytes 7c3d0294
+ 00b50f24 bytes 7f3d0294
~~~


<a id="compare-09267c6af2667cdb7d9f881fcd4946a8"></a>

### [`00b522d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b522d4.md) → [`00b52318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52318.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0520.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0570.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b522d4.md#insn-00b52370) · [`00b5245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b522d4.md#insn-00b5245c) · [`00b52498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b522d4.md#insn-00b52498)
- 新版 `00b523b4`（命令位置の公開資料なし） · `00b524a0`（命令位置の公開資料なし） · `00b524dc`（命令位置の公開資料なし）

~~~diff
- 00b52370 ["INT_ADD", "register:40f0:8", ["const:b52370:8", "const:4:8"]]
- 00b52370 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b523b4 ["INT_ADD", "register:40f0:8", ["const:b523b4:8", "const:4:8"]]
+ 00b523b4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b52370 bytes 20230294
+ 00b523b4 bytes 23230294
- 00b5245c ["INT_ADD", "register:40f0:8", ["const:b5245c:8", "const:4:8"]]
- 00b5245c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b524a0 ["INT_ADD", "register:40f0:8", ["const:b524a0:8", "const:4:8"]]
+ 00b524a0 ["CALL", null, ["callee:00bdb060:8"]]
- 00b5245c bytes ed220294
+ 00b524a0 bytes f0220294
- 00b52498 ["INT_ADD", "register:40f0:8", ["const:b52498:8", "const:4:8"]]
- 00b52498 ["CALL", null, ["callee:00bddeb0:8"]]
+ 00b524dc ["INT_ADD", "register:40f0:8", ["const:b524dc:8", "const:4:8"]]
+ 00b524dc ["CALL", null, ["callee:00bddeb0:8"]]
- 00b52498 bytes 722e0294
+ 00b524dc bytes 752e0294
~~~


<a id="compare-06fd9d7425873b10e908eedb521c2d70"></a>

### [`00b52a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52a18.md) → [`00b52a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52a5c.md) _ZN8firebase13remote_config12RemoteConfigD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0680.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be06d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52a18.md#insn-00b52a20)
- 新版 `00b52a64`（命令位置の公開資料なし）

~~~diff
- 00b52a20 ["INT_ADD", "register:40f0:8", ["const:b52a20:8", "const:4:8"]]
- 00b52a20 ["CALL", null, ["callee:00be06d0:8"]]
+ 00b52a64 ["INT_ADD", "register:40f0:8", ["const:b52a64:8", "const:4:8"]]
+ 00b52a64 ["CALL", null, ["callee:00be06d0:8"]]
- 00b52a20 bytes 18370294
+ 00b52a64 bytes 1b370294
~~~


<a id="compare-a33cf8745c11e04688ae0f85031aefb4"></a>

### [`00b52a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52a60.md) → [`00b52aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52aa4.md) _ZN8firebase13remote_config12RemoteConfig5FetchEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0710.md) [`00be0790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0790.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be0760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0760.md) [`00be07e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52a60.md#insn-00b52a78)
- 新版 `00b52abc`（命令位置の公開資料なし）

~~~diff
- 00b52a78 ["INT_ADD", "register:40f0:8", ["const:b52a78:8", "const:4:8"]]
- 00b52a78 ["CALL", null, ["callee:00be0760:8"]]
+ 00b52abc ["INT_ADD", "register:40f0:8", ["const:b52abc:8", "const:4:8"]]
+ 00b52abc ["CALL", null, ["callee:00be0760:8"]]
- 00b52a78 bytes 26370294
+ 00b52abc bytes 29370294
~~~


<a id="compare-cb4e2552531a1e7af2db9576345884d2"></a>

### [`00b52b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b78.md) → [`00b52bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52bbc.md) _ZN8firebase13remote_config12RemoteConfig25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00be0750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0750.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00be07a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b78.md#insn-00b52bbc) · [`00b52be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b78.md#insn-00b52be4) · [`00b52bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b78.md#insn-00b52bf8)
- 新版 `00b52c00`（命令位置の公開資料なし） · `00b52c28`（命令位置の公開資料なし） · `00b52c3c`（命令位置の公開資料なし）

~~~diff
- 00b52bbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52bbc ["INT_ADD", "register:40f0:8", ["const:b52bbc:8", "const:4:8"]]
- 00b52bbc ["CALLIND", null, ["register:0:8"]]
+ 00b52c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52c00 ["INT_ADD", "register:40f0:8", ["const:b52c00:8", "const:4:8"]]
+ 00b52c00 ["CALLIND", null, ["register:0:8"]]
- 00b52bbc bytes 00013fd6
+ 00b52c00 bytes 00013fd6
- 00b52be4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52be4 ["INT_ADD", "register:40f0:8", ["const:b52be4:8", "const:4:8"]]
- 00b52be4 ["CALLIND", null, ["register:0:8"]]
+ 00b52c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52c28 ["INT_ADD", "register:40f0:8", ["const:b52c28:8", "const:4:8"]]
+ 00b52c28 ["CALLIND", null, ["register:0:8"]]
- 00b52be4 bytes 00013fd6
+ 00b52c28 bytes 00013fd6
- 00b52bf8 ["INT_ADD", "register:40f0:8", ["const:b52bf8:8", "const:4:8"]]
- 00b52bf8 ["CALL", null, ["callee:00be07a0:8"]]
+ 00b52c3c ["INT_ADD", "register:40f0:8", ["const:b52c3c:8", "const:4:8"]]
+ 00b52c3c ["CALL", null, ["callee:00be07a0:8"]]
- 00b52bf8 bytes d6360294
+ 00b52c3c bytes d9360294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4a65142ae0fb4d0129199d213723443"></a>

### [`00b52cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cb8.md) → [`00b52cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cfc.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_13remote_config12RemoteConfigEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0860.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0860.md)
- 新版 呼出元 1件 [`00be08b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08b0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be08b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cb8.md#insn-00b52cd4) · [`00b52ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cb8.md#insn-00b52ce0)
- 新版 `00b52d18`（命令位置の公開資料なし） · `00b52d24`（命令位置の公開資料なし）

~~~diff
- 00b52cd4 ["INT_ADD", "register:40f0:8", ["const:b52cd4:8", "const:4:8"]]
- 00b52cd4 ["CALL", null, ["callee:00be08b0:8"]]
+ 00b52d18 ["INT_ADD", "register:40f0:8", ["const:b52d18:8", "const:4:8"]]
+ 00b52d18 ["CALL", null, ["callee:00be08b0:8"]]
- 00b52cd4 bytes e3360294
+ 00b52d18 bytes e6360294
- 00b52ce0 ["INT_ADD", "register:40f0:8", ["const:b52ce0:8", "const:4:8"]]
- 00b52ce0 ["CALL", null, ["callee:00be08b0:8"]]
+ 00b52d24 ["INT_ADD", "register:40f0:8", ["const:b52d24:8", "const:4:8"]]
+ 00b52d24 ["CALL", null, ["callee:00be08b0:8"]]
- 00b52ce0 bytes e0360294
+ 00b52d24 bytes e3360294
~~~


<a id="compare-8ede553b0c2293807a9da67092dc9d41"></a>

### [`00b5562c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b5562c.md) → [`00b55670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55670.md) _ZNSt6__ndk16vectorIN8firebase8internal12EmbeddedFileENS_9allocatorIS3_EEEC2ERKS6_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0920.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0970.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5567c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b5562c.md#insn-00b5567c) · [`00b556b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b5562c.md#insn-00b556b8) · [`00b556dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b5562c.md#insn-00b556dc)
- 新版 `00b556c0`（命令位置の公開資料なし） · `00b556fc`（命令位置の公開資料なし） · `00b55720`（命令位置の公開資料なし）

~~~diff
- 00b5567c ["INT_ADD", "register:40f0:8", ["const:b5567c:8", "const:4:8"]]
- 00b5567c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b556c0 ["INT_ADD", "register:40f0:8", ["const:b556c0:8", "const:4:8"]]
+ 00b556c0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b5567c bytes 5d160294
+ 00b556c0 bytes 60160294
- 00b556b8 ["INT_ADD", "register:40f0:8", ["const:b556b8:8", "const:4:8"]]
- 00b556b8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b556fc ["INT_ADD", "register:40f0:8", ["const:b556fc:8", "const:4:8"]]
+ 00b556fc ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b556b8 bytes aa160294
+ 00b556fc bytes ad160294
- 00b556dc ["INT_ADD", "register:40f0:8", ["const:b556dc:8", "const:4:8"]]
- 00b556dc ["CALL", null, ["callee:00bddeb0:8"]]
+ 00b55720 ["INT_ADD", "register:40f0:8", ["const:b55720:8", "const:4:8"]]
+ 00b55720 ["CALL", null, ["callee:00bddeb0:8"]]
- 00b556dc bytes e1210294
+ 00b55720 bytes e4210294
~~~


<a id="compare-6ad5314b94473e2ffca432c53d31dcff"></a>

### [`00b55700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55700.md) → [`00b55744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55744.md) _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be08e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08e0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00be0930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0930.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55700.md#insn-00b55720) · [`00b55738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55700.md#insn-00b55738) · [`00b55740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55700.md#insn-00b55740)
- 新版 `00b55764`（命令位置の公開資料なし） · `00b5577c`（命令位置の公開資料なし） · `00b55784`（命令位置の公開資料なし）

~~~diff
- 00b55720 ["INT_ADD", "register:40f0:8", ["const:b55720:8", "const:4:8"]]
- 00b55720 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b55764 ["INT_ADD", "register:40f0:8", ["const:b55764:8", "const:4:8"]]
+ 00b55764 ["CALL", null, ["callee:00bddc20:8"]]
- 00b55720 bytes 2c210294
+ 00b55764 bytes 2f210294
- 00b55738 ["INT_ADD", "register:40f0:8", ["const:b55738:8", "const:4:8"]]
- 00b55738 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5577c ["INT_ADD", "register:40f0:8", ["const:b5577c:8", "const:4:8"]]
+ 00b5577c ["CALL", null, ["callee:00bddc30:8"]]
- 00b55738 bytes 2a210294
+ 00b5577c bytes 2d210294
- 00b55740 ["INT_ADD", "register:40f0:8", ["const:b55740:8", "const:4:8"]]
- 00b55740 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b55784 ["INT_ADD", "register:40f0:8", ["const:b55784:8", "const:4:8"]]
+ 00b55784 ["CALL", null, ["callee:00bddc30:8"]]
- 00b55740 bytes 28210294
+ 00b55784 bytes 2b210294
~~~


<a id="compare-f343d26a41a4379947def4a50a366bdf"></a>

### [`00b55770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55770.md) → [`00b557b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b557b4.md) FUN_00b557b4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b557bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55770.md#insn-00b557bc)
- 新版 `00b55800`（命令位置の公開資料なし）

~~~diff
- 00b557bc ["INT_ADD", "register:40f0:8", ["const:b557bc:8", "const:4:8"]]
- 00b557bc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b55800 ["INT_ADD", "register:40f0:8", ["const:b55800:8", "const:4:8"]]
+ 00b55800 ["CALL", null, ["callee:00bdb060:8"]]
- 00b557bc bytes 15160294
+ 00b55800 bytes 18160294
~~~


<a id="compare-c03c553b221c2c056975fc4f5190839c"></a>

### [`00b557f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b557f4.md) → [`00b55838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55838.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0830.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md)
- 新版 呼出元 1件 [`00be0880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0880.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md) [`00bdddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddd0.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b557f4.md#insn-00b55810) · [`00b55818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b557f4.md#insn-00b55818) · [`00b55834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b557f4.md#insn-00b55834)
- 新版 `00b55854`（命令位置の公開資料なし） · `00b5585c`（命令位置の公開資料なし） · `00b55878`（命令位置の公開資料なし）

~~~diff
- 00b55810 ["INT_ADD", "register:40f0:8", ["const:b55810:8", "const:4:8"]]
- 00b55810 ["CALL", null, ["callee:00bde910:8"]]
+ 00b55854 ["INT_ADD", "register:40f0:8", ["const:b55854:8", "const:4:8"]]
+ 00b55854 ["CALL", null, ["callee:00bde910:8"]]
- 00b55810 bytes 2c240294
+ 00b55854 bytes 2f240294
- 00b55818 ["INT_ADD", "register:40f0:8", ["const:b55818:8", "const:4:8"]]
- 00b55818 ["CALL", null, ["callee:00bde200:8"]]
+ 00b5585c ["INT_ADD", "register:40f0:8", ["const:b5585c:8", "const:4:8"]]
+ 00b5585c ["CALL", null, ["callee:00bde200:8"]]
- 00b55818 bytes 66220294
+ 00b5585c bytes 69220294
- 00b55834 ["INT_ADD", "register:40f0:8", ["const:b55834:8", "const:4:8"]]
- 00b55834 ["CALL", null, ["callee:00bde080:8"]]
+ 00b55878 ["INT_ADD", "register:40f0:8", ["const:b55878:8", "const:4:8"]]
+ 00b55878 ["CALL", null, ["callee:00bde080:8"]]
- 00b55834 bytes ff210294
+ 00b55878 bytes 02220294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0991c268f8d6d898577649403cfbb6d5"></a>

### [`00b55d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md) → [`00b55d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md) _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b564b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b564b0.md) · 呼出先 6件 [`00b55e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55e38.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00b564f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md) · 呼出先 6件 [`00b55e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md#insn-00b55d44) · [`00b55d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md#insn-00b55d60) · [`00b55d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md#insn-00b55d88)
- 新版 `00b55d88`（命令位置の公開資料なし） · `00b55da4`（命令位置の公開資料なし） · `00b55dcc`（命令位置の公開資料なし）

~~~diff
- 00b55d44 ["INT_ADD", "register:40f0:8", ["const:b55d44:8", "const:4:8"]]
- 00b55d44 ["CALL", null, ["callee:00b55e7c:8"]]
+ 00b55d88 ["INT_ADD", "register:40f0:8", ["const:b55d88:8", "const:4:8"]]
+ 00b55d88 ["CALL", null, ["callee:00b55e7c:8"]]
- 00b55d44 bytes 3d000094
+ 00b55d88 bytes 3d000094
- 00b55d60 ["INT_ADD", "register:40f0:8", ["const:b55d60:8", "const:4:8"]]
- 00b55d60 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b55da4 ["INT_ADD", "register:40f0:8", ["const:b55da4:8", "const:4:8"]]
+ 00b55da4 ["CALL", null, ["callee:00bddf80:8"]]
- 00b55d60 bytes 74200294
+ 00b55da4 bytes 77200294
- 00b55d88 ["INT_ADD", "register:40f0:8", ["const:b55d88:8", "const:4:8"]]
- 00b55d88 ["CALL", null, ["callee:00be08d0:8"]]
+ 00b55dcc ["INT_ADD", "register:40f0:8", ["const:b55dcc:8", "const:4:8"]]
+ 00b55dcc ["CALL", null, ["callee:00be08d0:8"]]
- 00b55d88 bytes be2a0294
+ 00b55dcc bytes c12a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aacd2a9acf5fc54ba7c9faeb78644c5"></a>

### [`00b55efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md) → [`00b55f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md) _ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b567dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b567dc.md) [`00b56b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56b08.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bde410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde410.md)
- 新版 呼出元 2件 [`00b56820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md) [`00b56b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bde460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md#insn-00b55f3c) · [`00b55f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md#insn-00b55f5c) · [`00b55f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md#insn-00b55f78)
- 新版 `00b55f80`（命令位置の公開資料なし） · `00b55fa0`（命令位置の公開資料なし） · `00b55fbc`（命令位置の公開資料なし）

~~~diff
- 00b55f3c ["INT_ADD", "register:40f0:8", ["const:b55f3c:8", "const:4:8"]]
- 00b55f3c ["CALL", null, ["callee:00bde460:8"]]
+ 00b55f80 ["INT_ADD", "register:40f0:8", ["const:b55f80:8", "const:4:8"]]
+ 00b55f80 ["CALL", null, ["callee:00bde460:8"]]
- 00b55f3c bytes 35210294
+ 00b55f80 bytes 38210294
- 00b55f5c ["INT_ADD", "register:40f0:8", ["const:b55f5c:8", "const:4:8"]]
- 00b55f5c ["CALL", null, ["callee:00bddf80:8"]]
+ 00b55fa0 ["INT_ADD", "register:40f0:8", ["const:b55fa0:8", "const:4:8"]]
+ 00b55fa0 ["CALL", null, ["callee:00bddf80:8"]]
- 00b55f5c bytes f51f0294
+ 00b55fa0 bytes f81f0294
- 00b55f78 ["INT_ADD", "register:40f0:8", ["const:b55f78:8", "const:4:8"]]
- 00b55f78 ["CALL", null, ["callee:00be08e0:8"]]
+ 00b55fbc ["INT_ADD", "register:40f0:8", ["const:b55fbc:8", "const:4:8"]]
+ 00b55fbc ["CALL", null, ["callee:00be08e0:8"]]
- 00b55f78 bytes 462a0294
+ 00b55fbc bytes 492a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d01302b96254ca1b0921a0fdf1faaa2"></a>

### [`00b5602c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5602c.md) → [`00b56070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56070.md) _ZN8firebase13remote_config8internal20CompleteVoidCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b580c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b580c4.md) [`00be0870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0870.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md)
- 新版 呼出元 2件 [`00b58108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md) [`00be08c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08c0.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bdee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b56068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5602c.md#insn-00b56068) · [`00b56084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5602c.md#insn-00b56084) · [`00b5608c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5602c.md#insn-00b5608c)
- 新版 `00b560ac`（命令位置の公開資料なし） · `00b560c8`（命令位置の公開資料なし） · `00b560d0`（命令位置の公開資料なし）

~~~diff
- 00b56068 ["INT_ADD", "register:40f0:8", ["const:b56068:8", "const:4:8"]]
- 00b56068 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b560ac ["INT_ADD", "register:40f0:8", ["const:b560ac:8", "const:4:8"]]
+ 00b560ac ["CALL", null, ["callee:00bddf80:8"]]
- 00b56068 bytes b21f0294
+ 00b560ac bytes b51f0294
- 00b56084 ["INT_ADD", "register:40f0:8", ["const:b56084:8", "const:4:8"]]
- 00b56084 ["CALL", null, ["callee:00bdee00:8"]]
+ 00b560c8 ["INT_ADD", "register:40f0:8", ["const:b560c8:8", "const:4:8"]]
+ 00b560c8 ["CALL", null, ["callee:00bdee00:8"]]
- 00b56084 bytes 4b230294
+ 00b560c8 bytes 4e230294
- 00b5608c ["INT_ADD", "register:40f0:8", ["const:b5608c:8", "const:4:8"]]
- 00b5608c ["CALL", null, ["callee:00bddc40:8"]]
+ 00b560d0 ["INT_ADD", "register:40f0:8", ["const:b560d0:8", "const:4:8"]]
+ 00b560d0 ["CALL", null, ["callee:00bddc40:8"]]
- 00b5608c bytes d91e0294
+ 00b560d0 bytes dc1e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e31821081b4efdb96305bb882e2d4d30"></a>

### [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) → [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) _ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b5715c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b5715c.md) [`00b573f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b573f4.md) [`00b57b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b57b08.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be0870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0870.md)
- 新版 呼出元 3件 [`00b571a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b571a0.md) [`00b57438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57438.md) [`00b57b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be08c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b561f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md#insn-00b561f0) · [`00b5623c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md#insn-00b5623c) · [`00b56248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md#insn-00b56248)
- 新版 `00b56234`（命令位置の公開資料なし） · `00b56280`（命令位置の公開資料なし） · `00b5628c`（命令位置の公開資料なし）

~~~diff
- 00b561f0 ["INT_ADD", "register:40f0:8", ["const:b561f0:8", "const:4:8"]]
- 00b561f0 ["CALL", null, ["callee:00be08c0:8"]]
+ 00b56234 ["INT_ADD", "register:40f0:8", ["const:b56234:8", "const:4:8"]]
+ 00b56234 ["CALL", null, ["callee:00be08c0:8"]]
- 00b561f0 bytes a0290294
+ 00b56234 bytes a3290294
- 00b5623c ["INT_ADD", "register:40f0:8", ["const:b5623c:8", "const:4:8"]]
- 00b5623c ["CALL", null, ["callee:00be0980:8"]]
+ 00b56280 ["INT_ADD", "register:40f0:8", ["const:b56280:8", "const:4:8"]]
+ 00b56280 ["CALL", null, ["callee:00be0980:8"]]
- 00b5623c bytes bd290294
+ 00b56280 bytes c0290294
- 00b56248 ["INT_ADD", "register:40f0:8", ["const:b56248:8", "const:4:8"]]
- 00b56248 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5628c ["INT_ADD", "register:40f0:8", ["const:b5628c:8", "const:4:8"]]
+ 00b5628c ["CALL", null, ["callee:00bddc20:8"]]
- 00b56248 bytes 621e0294
+ 00b5628c bytes 651e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1133e3276b05a01625b877f04db69260"></a>

### [`00b5638c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5638c.md) → [`00b563d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b563d0.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0930.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00be0980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0980.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b563dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5638c.md#insn-00b563dc) · [`00b56408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5638c.md#insn-00b56408) · [`00b56434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5638c.md#insn-00b56434)
- 新版 `00b56420`（命令位置の公開資料なし） · `00b5644c`（命令位置の公開資料なし） · `00b56478`（命令位置の公開資料なし）

~~~diff
- 00b563dc ["INT_ADD", "register:40f0:8", ["const:b563dc:8", "const:4:8"]]
- 00b563dc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b56420 ["INT_ADD", "register:40f0:8", ["const:b56420:8", "const:4:8"]]
+ 00b56420 ["CALL", null, ["callee:00bdb040:8"]]
- 00b563dc bytes 05130294
+ 00b56420 bytes 08130294
- 00b56408 ["INT_ADD", "register:40f0:8", ["const:b56408:8", "const:4:8"]]
- 00b56408 ["CALL", null, ["callee:00bde730:8"]]
+ 00b5644c ["INT_ADD", "register:40f0:8", ["const:b5644c:8", "const:4:8"]]
+ 00b5644c ["CALL", null, ["callee:00bde730:8"]]
- 00b56408 bytes b6200294
+ 00b5644c bytes b9200294
- 00b56434 ["INT_ADD", "register:40f0:8", ["const:b56434:8", "const:4:8"]]
- 00b56434 ["CALL", null, ["callee:00bddeb0:8"]]
+ 00b56478 ["INT_ADD", "register:40f0:8", ["const:b56478:8", "const:4:8"]]
+ 00b56478 ["CALL", null, ["callee:00bddeb0:8"]]
- 00b56434 bytes 8b1e0294
+ 00b56478 bytes 8e1e0294
~~~


<a id="compare-2165f37b89926405e9b08c9f9df7f943"></a>

### [`00b5674c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5674c.md) → [`00b56790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56790.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27EnsureInitializedLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0770.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 1件 [`00be07c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07c0.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5676c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5674c.md#insn-00b5676c) · [`00b56778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5674c.md#insn-00b56778) · [`00b56784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5674c.md#insn-00b56784)
- 新版 `00b567b0`（命令位置の公開資料なし） · `00b567bc`（命令位置の公開資料なし） · `00b567c8`（命令位置の公開資料なし）

~~~diff
- 00b5676c ["INT_ADD", "register:40f0:8", ["const:b5676c:8", "const:4:8"]]
- 00b5676c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b567b0 ["INT_ADD", "register:40f0:8", ["const:b567b0:8", "const:4:8"]]
+ 00b567b0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5676c bytes 191d0294
+ 00b567b0 bytes 1c1d0294
- 00b56778 ["INT_ADD", "register:40f0:8", ["const:b56778:8", "const:4:8"]]
- 00b56778 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b567bc ["INT_ADD", "register:40f0:8", ["const:b567bc:8", "const:4:8"]]
+ 00b567bc ["CALL", null, ["callee:00bddc30:8"]]
- 00b56778 bytes 1a1d0294
+ 00b567bc bytes 1d1d0294
- 00b56784 ["INT_ADD", "register:40f0:8", ["const:b56784:8", "const:4:8"]]
- 00b56784 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b567c8 ["INT_ADD", "register:40f0:8", ["const:b567c8:8", "const:4:8"]]
+ 00b567c8 ["CALL", null, ["callee:00bdde10:8"]]
- 00b56784 bytes 8f1d0294
+ 00b567c8 bytes 921d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d692debb8ab227bf82a019d75daf144"></a>

### [`00b56a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56a78.md) → [`00b56abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56abc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal18ActivateLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0730.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 1件 [`00be0780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0780.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b56a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56a78.md#insn-00b56a98) · [`00b56aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56a78.md#insn-00b56aa4) · [`00b56ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56a78.md#insn-00b56ab0)
- 新版 `00b56adc`（命令位置の公開資料なし） · `00b56ae8`（命令位置の公開資料なし） · `00b56af4`（命令位置の公開資料なし）

~~~diff
- 00b56a98 ["INT_ADD", "register:40f0:8", ["const:b56a98:8", "const:4:8"]]
- 00b56a98 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b56adc ["INT_ADD", "register:40f0:8", ["const:b56adc:8", "const:4:8"]]
+ 00b56adc ["CALL", null, ["callee:00bddc20:8"]]
- 00b56a98 bytes 4e1c0294
+ 00b56adc bytes 511c0294
- 00b56aa4 ["INT_ADD", "register:40f0:8", ["const:b56aa4:8", "const:4:8"]]
- 00b56aa4 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b56ae8 ["INT_ADD", "register:40f0:8", ["const:b56ae8:8", "const:4:8"]]
+ 00b56ae8 ["CALL", null, ["callee:00bddc30:8"]]
- 00b56aa4 bytes 4f1c0294
+ 00b56ae8 bytes 521c0294
- 00b56ab0 ["INT_ADD", "register:40f0:8", ["const:b56ab0:8", "const:4:8"]]
- 00b56ab0 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b56af4 ["INT_ADD", "register:40f0:8", ["const:b56af4:8", "const:4:8"]]
+ 00b56af4 ["CALL", null, ["callee:00bdde10:8"]]
- 00b56ab0 bytes c41c0294
+ 00b56af4 bytes c71c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73b06f858e1950b450d2c1b34a2c5207"></a>

### [`00b56da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56da4.md) → [`00b56de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56de8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26FetchAndActivateLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0760.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 1件 [`00be07b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07b0.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b56dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56da4.md#insn-00b56dc4) · [`00b56dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56da4.md#insn-00b56dd0) · [`00b56ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56da4.md#insn-00b56ddc)
- 新版 `00b56e08`（命令位置の公開資料なし） · `00b56e14`（命令位置の公開資料なし） · `00b56e20`（命令位置の公開資料なし）

~~~diff
- 00b56dc4 ["INT_ADD", "register:40f0:8", ["const:b56dc4:8", "const:4:8"]]
- 00b56dc4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b56e08 ["INT_ADD", "register:40f0:8", ["const:b56e08:8", "const:4:8"]]
+ 00b56e08 ["CALL", null, ["callee:00bddc20:8"]]
- 00b56dc4 bytes 831b0294
+ 00b56e08 bytes 861b0294
- 00b56dd0 ["INT_ADD", "register:40f0:8", ["const:b56dd0:8", "const:4:8"]]
- 00b56dd0 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b56e14 ["INT_ADD", "register:40f0:8", ["const:b56e14:8", "const:4:8"]]
+ 00b56e14 ["CALL", null, ["callee:00bddc30:8"]]
- 00b56dd0 bytes 841b0294
+ 00b56e14 bytes 871b0294
- 00b56ddc ["INT_ADD", "register:40f0:8", ["const:b56ddc:8", "const:4:8"]]
- 00b56ddc ["CALL", null, ["callee:00bdde10:8"]]
+ 00b56e20 ["INT_ADD", "register:40f0:8", ["const:b56e20:8", "const:4:8"]]
+ 00b56e20 ["CALL", null, ["callee:00bdde10:8"]]
- 00b56ddc bytes f91b0294
+ 00b56e20 bytes fc1b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e321320347cbbdd611930fe99149ae86"></a>

### [`00b570cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b570cc.md) → [`00b57110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57110.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15FetchLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be06d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06d0.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 1件 [`00be0720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0720.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b570ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b570cc.md#insn-00b570ec) · [`00b570f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b570cc.md#insn-00b570f8) · [`00b57104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b570cc.md#insn-00b57104)
- 新版 `00b57130`（命令位置の公開資料なし） · `00b5713c`（命令位置の公開資料なし） · `00b57148`（命令位置の公開資料なし）

~~~diff
- 00b570ec ["INT_ADD", "register:40f0:8", ["const:b570ec:8", "const:4:8"]]
- 00b570ec ["CALL", null, ["callee:00bddc20:8"]]
+ 00b57130 ["INT_ADD", "register:40f0:8", ["const:b57130:8", "const:4:8"]]
+ 00b57130 ["CALL", null, ["callee:00bddc20:8"]]
- 00b570ec bytes b91a0294
+ 00b57130 bytes bc1a0294
- 00b570f8 ["INT_ADD", "register:40f0:8", ["const:b570f8:8", "const:4:8"]]
- 00b570f8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5713c ["INT_ADD", "register:40f0:8", ["const:b5713c:8", "const:4:8"]]
+ 00b5713c ["CALL", null, ["callee:00bddc30:8"]]
- 00b570f8 bytes ba1a0294
+ 00b5713c bytes bd1a0294
- 00b57104 ["INT_ADD", "register:40f0:8", ["const:b57104:8", "const:4:8"]]
- 00b57104 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b57148 ["INT_ADD", "register:40f0:8", ["const:b57148:8", "const:4:8"]]
+ 00b57148 ["CALL", null, ["callee:00bdde10:8"]]
- 00b57104 bytes 2f1b0294
+ 00b57148 bytes 321b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eb6a08bed6e50f710933224b526f3e8"></a>

### [`00b58034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58034.md) → [`00b58078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58078.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal21SetDefaultsLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0740.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 1件 [`00be0790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0790.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58034.md#insn-00b58054) · [`00b58060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58034.md#insn-00b58060) · [`00b5806c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58034.md#insn-00b5806c)
- 新版 `00b58098`（命令位置の公開資料なし） · `00b580a4`（命令位置の公開資料なし） · `00b580b0`（命令位置の公開資料なし）

~~~diff
- 00b58054 ["INT_ADD", "register:40f0:8", ["const:b58054:8", "const:4:8"]]
- 00b58054 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b58098 ["INT_ADD", "register:40f0:8", ["const:b58098:8", "const:4:8"]]
+ 00b58098 ["CALL", null, ["callee:00bddc20:8"]]
- 00b58054 bytes df160294
+ 00b58098 bytes e2160294
- 00b58060 ["INT_ADD", "register:40f0:8", ["const:b58060:8", "const:4:8"]]
- 00b58060 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b580a4 ["INT_ADD", "register:40f0:8", ["const:b580a4:8", "const:4:8"]]
+ 00b580a4 ["CALL", null, ["callee:00bddc30:8"]]
- 00b58060 bytes e0160294
+ 00b580a4 bytes e3160294
- 00b5806c ["INT_ADD", "register:40f0:8", ["const:b5806c:8", "const:4:8"]]
- 00b5806c ["CALL", null, ["callee:00bdde10:8"]]
+ 00b580b0 ["INT_ADD", "register:40f0:8", ["const:b580b0:8", "const:4:8"]]
+ 00b580b0 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5806c bytes 55170294
+ 00b580b0 bytes 58170294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa134c793b06f935fe9a2a2bfa4b7b74"></a>

### [`00b58488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58488.md) → [`00b584cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b584cc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27SetConfigSettingsLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0780.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 1件 [`00be07d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07d0.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b584a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58488.md#insn-00b584a8) · [`00b584b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58488.md#insn-00b584b4) · [`00b584c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58488.md#insn-00b584c0)
- 新版 `00b584ec`（命令位置の公開資料なし） · `00b584f8`（命令位置の公開資料なし） · `00b58504`（命令位置の公開資料なし）

~~~diff
- 00b584a8 ["INT_ADD", "register:40f0:8", ["const:b584a8:8", "const:4:8"]]
- 00b584a8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b584ec ["INT_ADD", "register:40f0:8", ["const:b584ec:8", "const:4:8"]]
+ 00b584ec ["CALL", null, ["callee:00bddc20:8"]]
- 00b584a8 bytes ca150294
+ 00b584ec bytes cd150294
- 00b584b4 ["INT_ADD", "register:40f0:8", ["const:b584b4:8", "const:4:8"]]
- 00b584b4 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b584f8 ["INT_ADD", "register:40f0:8", ["const:b584f8:8", "const:4:8"]]
+ 00b584f8 ["CALL", null, ["callee:00bddc30:8"]]
- 00b584b4 bytes cb150294
+ 00b584f8 bytes ce150294
- 00b584c0 ["INT_ADD", "register:40f0:8", ["const:b584c0:8", "const:4:8"]]
- 00b584c0 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b58504 ["INT_ADD", "register:40f0:8", ["const:b58504:8", "const:4:8"]]
+ 00b58504 ["CALL", null, ["callee:00bdde10:8"]]
- 00b584c0 bytes 40160294
+ 00b58504 bytes 43160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b7c22e7ceab8cceead1f7c5ef3d89d"></a>

### [`00b59048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59048.md) → [`00b5908c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b5908c.md) _ZN8firebase9MutexLockD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be08f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08f0.md) · 呼出先 1件 [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00be0940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0940.md) · 呼出先 1件 [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59048.md#insn-00b59054)
- 新版 `00b59098`（命令位置の公開資料なし）

~~~diff
- 00b59054 ["INT_ADD", "register:40f0:8", ["const:b59054:8", "const:4:8"]]
- 00b59054 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b59098 ["INT_ADD", "register:40f0:8", ["const:b59098:8", "const:4:8"]]
+ 00b59098 ["CALL", null, ["callee:00bddc30:8"]]
- 00b59054 bytes e3120294
+ 00b59098 bytes e6120294
~~~


<a id="compare-aea9a7a422977bb8ca186841380562bb"></a>

### [`00b59ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md) → [`00b59d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59d2c.md) _ZN8firebase13remote_config8internal37JniConfigUpdateListener_nativeOnErrorEP7_JNIEnvP8_jobjectli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md#insn-00b59d38) · [`00b59d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md#insn-00b59d74) · [`00b59d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md#insn-00b59d8c)
- 新版 `00b59d7c`（命令位置の公開資料なし） · `00b59db8`（命令位置の公開資料なし） · `00b59dd0`（命令位置の公開資料なし）

~~~diff
- 00b59d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b59d38 ["INT_ADD", "register:40f0:8", ["const:b59d38:8", "const:4:8"]]
- 00b59d38 ["CALLIND", null, ["register:0:8"]]
+ 00b59d7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59d7c ["INT_ADD", "register:40f0:8", ["const:b59d7c:8", "const:4:8"]]
+ 00b59d7c ["CALLIND", null, ["register:0:8"]]
- 00b59d38 bytes 00013fd6
+ 00b59d7c bytes 00013fd6
- 00b59d74 ["INT_ADD", "register:40f0:8", ["const:b59d74:8", "const:4:8"]]
- 00b59d74 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b59db8 ["INT_ADD", "register:40f0:8", ["const:b59db8:8", "const:4:8"]]
+ 00b59db8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b59d74 bytes a7040294
+ 00b59db8 bytes aa040294
- 00b59d8c ["INT_ADD", "register:40f0:8", ["const:b59d8c:8", "const:4:8"]]
- 00b59d8c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b59dd0 ["INT_ADD", "register:40f0:8", ["const:b59dd0:8", "const:4:8"]]
+ 00b59dd0 ["CALL", null, ["callee:00bdb060:8"]]
- 00b59d8c bytes a1040294
+ 00b59dd0 bytes a4040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06f97cafd9ce88cf68c22d7c381fb095"></a>

### [`00b59e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md) → [`00b59e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59e60.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0910.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00be0900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0900.md)
- 新版 呼出元 1件 [`00be0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0960.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00be0950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md#insn-00b59e50) · [`00b59e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md#insn-00b59e6c) · [`00b59e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md#insn-00b59e94)
- 新版 `00b59e94`（命令位置の公開資料なし） · `00b59eb0`（命令位置の公開資料なし） · `00b59ed8`（命令位置の公開資料なし）

~~~diff
- 00b59e50 ["INT_ADD", "register:40f0:8", ["const:b59e50:8", "const:4:8"]]
- 00b59e50 ["CALL", null, ["callee:00be0950:8"]]
+ 00b59e94 ["INT_ADD", "register:40f0:8", ["const:b59e94:8", "const:4:8"]]
+ 00b59e94 ["CALL", null, ["callee:00be0950:8"]]
- 00b59e50 bytes ac1a0294
+ 00b59e94 bytes af1a0294
- 00b59e6c ["INT_ADD", "register:40f0:8", ["const:b59e6c:8", "const:4:8"]]
- 00b59e6c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b59eb0 ["INT_ADD", "register:40f0:8", ["const:b59eb0:8", "const:4:8"]]
+ 00b59eb0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b59e6c bytes 61040294
+ 00b59eb0 bytes 64040294
- 00b59e94 ["INT_ADD", "register:40f0:8", ["const:b59e94:8", "const:4:8"]]
- 00b59e94 ["CALL", null, ["callee:00bdd9f0:8"]]
+ 00b59ed8 ["INT_ADD", "register:40f0:8", ["const:b59ed8:8", "const:4:8"]]
+ 00b59ed8 ["CALL", null, ["callee:00bdd9f0:8"]]
- 00b59e94 bytes c30e0294
+ 00b59ed8 bytes c60e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddbe0d16a829eaf3f6769142a436f9b2"></a>

### [`00b59f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59f0c.md) → [`00b59f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b59f50.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0900.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0950.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59f0c.md#insn-00b59fa8) · [`00b59fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59f0c.md#insn-00b59fe8)
- 新版 `00b59fec`（命令位置の公開資料なし） · `00b5a02c`（命令位置の公開資料なし）

~~~diff
- 00b59fa8 ["INT_ADD", "register:40f0:8", ["const:b59fa8:8", "const:4:8"]]
- 00b59fa8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b59fec ["INT_ADD", "register:40f0:8", ["const:b59fec:8", "const:4:8"]]
+ 00b59fec ["CALL", null, ["callee:00bdb200:8"]]
- 00b59fa8 bytes 82040294
+ 00b59fec bytes 85040294
- 00b59fe8 ["INT_ADD", "register:40f0:8", ["const:b59fe8:8", "const:4:8"]]
- 00b59fe8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b5a02c ["INT_ADD", "register:40f0:8", ["const:b5a02c:8", "const:4:8"]]
+ 00b5a02c ["CALL", null, ["callee:00bdb200:8"]]
- 00b59fe8 bytes 72040294
+ 00b5a02c bytes 75040294
~~~


<a id="compare-0b87c07ea7da300ba10c504712a1feeb"></a>

### [`00b5a02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a02c.md) → [`00b5a070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a070.md) FUN_00b5a070

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b59888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59888.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0660.md)
- 新版 呼出元 1件 [`00b598cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be06b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5a040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a02c.md#insn-00b5a040)
- 新版 `00b5a084`（命令位置の公開資料なし）

~~~diff
- 00b5a040 ["INT_ADD", "register:40f0:8", ["const:b5a040:8", "const:4:8"]]
- 00b5a040 ["CALL", null, ["callee:00be06b0:8"]]
+ 00b5a084 ["INT_ADD", "register:40f0:8", ["const:b5a084:8", "const:4:8"]]
+ 00b5a084 ["CALL", null, ["callee:00be06b0:8"]]
- 00b5a040 bytes 88190294
+ 00b5a084 bytes 8b190294
~~~


<a id="compare-a1c51a57a59468d40ff81229fc43edd0"></a>

### [`00b5a3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a3bc.md) → [`00b5a400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a400.md) _ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be08c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08c0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00be0910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0910.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5a3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a3bc.md#insn-00b5a3dc) · [`00b5a3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a3bc.md#insn-00b5a3f0) · [`00b5a404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a3bc.md#insn-00b5a404)
- 新版 `00b5a420`（命令位置の公開資料なし） · `00b5a434`（命令位置の公開資料なし） · `00b5a448`（命令位置の公開資料なし）

~~~diff
- 00b5a3dc ["INT_ADD", "register:40f0:8", ["const:b5a3dc:8", "const:4:8"]]
- 00b5a3dc ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5a420 ["INT_ADD", "register:40f0:8", ["const:b5a420:8", "const:4:8"]]
+ 00b5a420 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5a3dc bytes 790e0294
+ 00b5a420 bytes 7c0e0294
- 00b5a3f0 ["INT_ADD", "register:40f0:8", ["const:b5a3f0:8", "const:4:8"]]
- 00b5a3f0 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b5a434 ["INT_ADD", "register:40f0:8", ["const:b5a434:8", "const:4:8"]]
+ 00b5a434 ["CALL", null, ["callee:00bddf80:8"]]
- 00b5a3f0 bytes d00e0294
+ 00b5a434 bytes d30e0294
- 00b5a404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5a404 ["INT_ADD", "register:40f0:8", ["const:b5a404:8", "const:4:8"]]
- 00b5a404 ["CALLIND", null, ["register:0:8"]]
+ 00b5a448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5a448 ["INT_ADD", "register:40f0:8", ["const:b5a448:8", "const:4:8"]]
+ 00b5a448 ["CALLIND", null, ["register:0:8"]]
- 00b5a404 bytes 00013fd6
+ 00b5a448 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b4a8ab6e379ba018be08e9db11dedc4"></a>

### [`00b5a570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a570.md) → [`00b5a5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a5b4.md) _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be08d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08d0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00be0920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0920.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5a590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a570.md#insn-00b5a590) · [`00b5a5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a570.md#insn-00b5a5a4) · [`00b5a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a570.md#insn-00b5a5b8)
- 新版 `00b5a5d4`（命令位置の公開資料なし） · `00b5a5e8`（命令位置の公開資料なし） · `00b5a5fc`（命令位置の公開資料なし）

~~~diff
- 00b5a590 ["INT_ADD", "register:40f0:8", ["const:b5a590:8", "const:4:8"]]
- 00b5a590 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5a5d4 ["INT_ADD", "register:40f0:8", ["const:b5a5d4:8", "const:4:8"]]
+ 00b5a5d4 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5a590 bytes 0c0e0294
+ 00b5a5d4 bytes 0f0e0294
- 00b5a5a4 ["INT_ADD", "register:40f0:8", ["const:b5a5a4:8", "const:4:8"]]
- 00b5a5a4 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b5a5e8 ["INT_ADD", "register:40f0:8", ["const:b5a5e8:8", "const:4:8"]]
+ 00b5a5e8 ["CALL", null, ["callee:00bddf80:8"]]
- 00b5a5a4 bytes 630e0294
+ 00b5a5e8 bytes 660e0294
- 00b5a5b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5a5b8 ["INT_ADD", "register:40f0:8", ["const:b5a5b8:8", "const:4:8"]]
- 00b5a5b8 ["CALLIND", null, ["register:0:8"]]
+ 00b5a5fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5a5fc ["INT_ADD", "register:40f0:8", ["const:b5a5fc:8", "const:4:8"]]
+ 00b5a5fc ["CALLIND", null, ["register:0:8"]]
- 00b5a5b8 bytes 00013fd6
+ 00b5a5fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f670c9d86b33f7083755b527e765ce81"></a>

### [`00b5a9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9b8.md) → [`00b5a9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a9fc.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0640.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0690.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9b8.md#insn-00b5a9d8)
- 新版 `00b5aa1c`（命令位置の公開資料なし）

~~~diff
- 00b5a9d8 ["INT_ADD", "register:40f0:8", ["const:b5a9d8:8", "const:4:8"]]
- 00b5a9d8 ["CALL", null, ["callee:00be0690:8"]]
+ 00b5aa1c ["INT_ADD", "register:40f0:8", ["const:b5aa1c:8", "const:4:8"]]
+ 00b5aa1c ["CALL", null, ["callee:00be0690:8"]]
- 00b5a9d8 bytes 1a170294
+ 00b5aa1c bytes 1d170294
~~~


<a id="compare-6db6ffd8e10ba14c2e9e56bdf168c764"></a>

### [`00b5a9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9fc.md) → [`00b5aa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aa40.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalC2EPNS1_20RemoteConfigInternalENSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0650.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06a0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5aa30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9fc.md#insn-00b5aa30) · [`00b5aa54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9fc.md#insn-00b5aa54)
- 新版 `00b5aa74`（命令位置の公開資料なし） · `00b5aa98`（命令位置の公開資料なし）

~~~diff
- 00b5aa30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5aa30 ["INT_ADD", "register:40f0:8", ["const:b5aa30:8", "const:4:8"]]
- 00b5aa30 ["CALLIND", null, ["register:0:8"]]
+ 00b5aa74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5aa74 ["INT_ADD", "register:40f0:8", ["const:b5aa74:8", "const:4:8"]]
+ 00b5aa74 ["CALLIND", null, ["register:0:8"]]
- 00b5aa30 bytes 00013fd6
+ 00b5aa74 bytes 00013fd6
- 00b5aa54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5aa54 ["INT_ADD", "register:40f0:8", ["const:b5aa54:8", "const:4:8"]]
- 00b5aa54 ["CALLIND", null, ["register:0:8"]]
+ 00b5aa98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5aa98 ["INT_ADD", "register:40f0:8", ["const:b5aa98:8", "const:4:8"]]
+ 00b5aa98 ["CALLIND", null, ["register:0:8"]]
- 00b5aa54 bytes 00013fd6
+ 00b5aa98 bytes 00013fd6
~~~


<a id="compare-a7120a3431571ef3302bae0d09bc8a33"></a>

### [`00b5aa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md) → [`00b5aaac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aaac.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0660.md) · 呼出先 1件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md)
- 新版 呼出元 1件 [`00be06b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06b0.md) · 呼出先 1件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5aa98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md#insn-00b5aa98) · [`00b5aadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md#insn-00b5aadc)
- 新版 `00b5aadc`（命令位置の公開資料なし） · `00b5ab20`（命令位置の公開資料なし）

~~~diff
- 00b5aa98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5aa98 ["INT_ADD", "register:40f0:8", ["const:b5aa98:8", "const:4:8"]]
- 00b5aa98 ["CALLIND", null, ["register:0:8"]]
+ 00b5aadc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5aadc ["INT_ADD", "register:40f0:8", ["const:b5aadc:8", "const:4:8"]]
+ 00b5aadc ["CALLIND", null, ["register:0:8"]]
- 00b5aa98 bytes 00013fd6
+ 00b5aadc bytes 00013fd6
- 00b5aadc ["INT_ADD", "register:40f0:8", ["const:b5aadc:8", "const:4:8"]]
- 00b5aadc ["CALL", null, ["callee:00b010ec:8"]]
+ 00b5ab20 ["INT_ADD", "register:40f0:8", ["const:b5ab20:8", "const:4:8"]]
+ 00b5ab20 ["CALL", null, ["callee:00b010ec:8"]]
- 00b5aadc bytes 7399fe97
+ 00b5ab20 bytes 7399fe97
~~~


<a id="compare-36467a48ee0c9945366216c12f3d88bb"></a>

### [`00b5aaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aaf4.md) → [`00b5ab38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ab38.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0640.md) · 呼出先 1件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md)
- 新版 呼出元 1件 [`00be0690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0690.md) · 呼出先 1件 [`00b010ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ab30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aaf4.md#insn-00b5ab30)
- 新版 `00b5ab74`（命令位置の公開資料なし）

~~~diff
- 00b5ab30 ["INT_ADD", "register:40f0:8", ["const:b5ab30:8", "const:4:8"]]
- 00b5ab30 ["CALL", null, ["callee:00b010ec:8"]]
+ 00b5ab74 ["INT_ADD", "register:40f0:8", ["const:b5ab74:8", "const:4:8"]]
+ 00b5ab74 ["CALL", null, ["callee:00b010ec:8"]]
- 00b5ab30 bytes 5e99fe97
+ 00b5ab74 bytes 5e99fe97
~~~


<a id="compare-6501ebb0b96deccfa16c22b63a25a31b"></a>

### [`00b5b32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md) → [`00b5b370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b370.md) _ZN8firebase4auth8AuthDataD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a60.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00be0950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0950.md)
- 新版 呼出元 1件 [`00be0ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ab0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbe0.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00be09a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md#insn-00b5b33c) · [`00b5b358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md#insn-00b5b358) · [`00b5b368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md#insn-00b5b368)
- 新版 `00b5b380`（命令位置の公開資料なし） · `00b5b39c`（命令位置の公開資料なし） · `00b5b3ac`（命令位置の公開資料なし）

~~~diff
- 00b5b33c ["INT_ADD", "register:40f0:8", ["const:b5b33c:8", "const:4:8"]]
- 00b5b33c ["CALL", null, ["callee:00be09a0:8"]]
+ 00b5b380 ["INT_ADD", "register:40f0:8", ["const:b5b380:8", "const:4:8"]]
+ 00b5b380 ["CALL", null, ["callee:00be09a0:8"]]
- 00b5b33c bytes 85150294
+ 00b5b380 bytes 88150294
- 00b5b358 ["INT_ADD", "register:40f0:8", ["const:b5b358:8", "const:4:8"]]
- 00b5b358 ["CALL", null, ["callee:00be0a70:8"]]
+ 00b5b39c ["INT_ADD", "register:40f0:8", ["const:b5b39c:8", "const:4:8"]]
+ 00b5b39c ["CALL", null, ["callee:00be0a70:8"]]
- 00b5b358 bytes b2150294
+ 00b5b39c bytes b5150294
- 00b5b368 ["INT_ADD", "register:40f0:8", ["const:b5b368:8", "const:4:8"]]
- 00b5b368 ["CALL", null, ["callee:00be0a60:8"]]
+ 00b5b3ac ["INT_ADD", "register:40f0:8", ["const:b5b3ac:8", "const:4:8"]]
+ 00b5b3ac ["CALL", null, ["callee:00be0a60:8"]]
- 00b5b368 bytes aa150294
+ 00b5b3ac bytes ad150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d8450149419df224cf732cb9bc4690"></a>

### [`00b5b478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b478.md) → [`00b5b4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4bc.md) _ZN8firebase4auth4AuthD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be09e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b478.md#insn-00b5b480)
- 新版 `00b5b4c4`（命令位置の公開資料なし）

~~~diff
- 00b5b480 ["INT_ADD", "register:40f0:8", ["const:b5b480:8", "const:4:8"]]
- 00b5b480 ["CALL", null, ["callee:00be0a30:8"]]
+ 00b5b4c4 ["INT_ADD", "register:40f0:8", ["const:b5b4c4:8", "const:4:8"]]
+ 00b5b4c4 ["CALL", null, ["callee:00be0a30:8"]]
- 00b5b480 bytes 58150294
+ 00b5b4c4 bytes 5b150294
~~~


<a id="compare-1edb9e85bef7dfa136cdfaeb9fd6aa9b"></a>

### [`00b5b870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b870.md) → [`00b5b8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b8b4.md) _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a20.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00be0a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a70.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b870.md#insn-00b5b898) · [`00b5b96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b870.md#insn-00b5b96c)
- 新版 `00b5b8dc`（命令位置の公開資料なし） · `00b5b9b0`（命令位置の公開資料なし）

~~~diff
- 00b5b898 ["INT_ADD", "register:40f0:8", ["const:b5b898:8", "const:4:8"]]
- 00b5b898 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5b8dc ["INT_ADD", "register:40f0:8", ["const:b5b8dc:8", "const:4:8"]]
+ 00b5b8dc ["CALL", null, ["callee:00bddc20:8"]]
- 00b5b898 bytes ce080294
+ 00b5b8dc bytes d1080294
- 00b5b96c ["INT_ADD", "register:40f0:8", ["const:b5b96c:8", "const:4:8"]]
- 00b5b96c ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5b9b0 ["INT_ADD", "register:40f0:8", ["const:b5b9b0:8", "const:4:8"]]
+ 00b5b9b0 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5b96c bytes 9d080294
+ 00b5b9b0 bytes a0080294
~~~


<a id="compare-18f1244b9f724623519a05460dedfdf1"></a>

### [`00b5b984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b984.md) → [`00b5b9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b9c8.md) _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a10.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be09b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09b0.md)
- 新版 呼出元 1件 [`00be0a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a60.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b984.md#insn-00b5b9b8) · [`00b5ba8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b984.md#insn-00b5ba8c)
- 新版 `00b5b9fc`（命令位置の公開資料なし） · `00b5bad0`（命令位置の公開資料なし）

~~~diff
- 00b5b9b8 ["INT_ADD", "register:40f0:8", ["const:b5b9b8:8", "const:4:8"]]
- 00b5b9b8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5b9fc ["INT_ADD", "register:40f0:8", ["const:b5b9fc:8", "const:4:8"]]
+ 00b5b9fc ["CALL", null, ["callee:00bddc20:8"]]
- 00b5b9b8 bytes 86080294
+ 00b5b9fc bytes 89080294
- 00b5ba8c ["INT_ADD", "register:40f0:8", ["const:b5ba8c:8", "const:4:8"]]
- 00b5ba8c ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5bad0 ["INT_ADD", "register:40f0:8", ["const:b5bad0:8", "const:4:8"]]
+ 00b5bad0 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5ba8c bytes 55080294
+ 00b5bad0 bytes 58080294
~~~


<a id="compare-6e36c41a3784819ac85d799099f68e1e"></a>

### [`00b5bbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bbe8.md) → [`00b5bc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bc2c.md) _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be09c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09c0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)
- 新版 呼出元 1件 [`00be0a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a10.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5bc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bbe8.md#insn-00b5bc14) · [`00b5bc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bbe8.md#insn-00b5bc24) · [`00b5bc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bbe8.md#insn-00b5bc3c)
- 新版 `00b5bc58`（命令位置の公開資料なし） · `00b5bc68`（命令位置の公開資料なし） · `00b5bc80`（命令位置の公開資料なし）

~~~diff
- 00b5bc14 ["INT_ADD", "register:40f0:8", ["const:b5bc14:8", "const:4:8"]]
- 00b5bc14 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5bc58 ["INT_ADD", "register:40f0:8", ["const:b5bc58:8", "const:4:8"]]
+ 00b5bc58 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5bc14 bytes ef070294
+ 00b5bc58 bytes f2070294
- 00b5bc24 ["INT_ADD", "register:40f0:8", ["const:b5bc24:8", "const:4:8"]]
- 00b5bc24 ["CALL", null, ["callee:00be0b00:8"]]
+ 00b5bc68 ["INT_ADD", "register:40f0:8", ["const:b5bc68:8", "const:4:8"]]
+ 00b5bc68 ["CALL", null, ["callee:00be0b00:8"]]
- 00b5bc24 bytes a3130294
+ 00b5bc68 bytes a6130294
- 00b5bc3c ["INT_ADD", "register:40f0:8", ["const:b5bc3c:8", "const:4:8"]]
- 00b5bc3c ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b5bc80 ["INT_ADD", "register:40f0:8", ["const:b5bc80:8", "const:4:8"]]
+ 00b5bc80 ["CALL", null, ["callee:00bde2b0:8"]]
- 00b5bc3c bytes 89090294
+ 00b5bc80 bytes 8c090294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-948db61b3fc6b350668b6cbbc37ef855"></a>

### [`00b5bd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bd50.md) → [`00b5bd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bd94.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ab0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b00.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5bd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bd50.md#insn-00b5bd88) · [`00b5bdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bd50.md#insn-00b5bdb4) · [`00b5bdd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bd50.md#insn-00b5bdd4)
- 新版 `00b5bdcc`（命令位置の公開資料なし） · `00b5bdf8`（命令位置の公開資料なし） · `00b5be18`（命令位置の公開資料なし）

~~~diff
- 00b5bd88 ["INT_ADD", "register:40f0:8", ["const:b5bd88:8", "const:4:8"]]
- 00b5bd88 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b5bdcc ["INT_ADD", "register:40f0:8", ["const:b5bdcc:8", "const:4:8"]]
+ 00b5bdcc ["CALL", null, ["callee:00bdb040:8"]]
- 00b5bd88 bytes 9afc0194
+ 00b5bdcc bytes 9dfc0194
- 00b5bdb4 ["INT_ADD", "register:40f0:8", ["const:b5bdb4:8", "const:4:8"]]
- 00b5bdb4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b5bdf8 ["INT_ADD", "register:40f0:8", ["const:b5bdf8:8", "const:4:8"]]
+ 00b5bdf8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b5bdb4 bytes ebfc0194
+ 00b5bdf8 bytes eefc0194
- 00b5bdd4 ["INT_ADD", "register:40f0:8", ["const:b5bdd4:8", "const:4:8"]]
- 00b5bdd4 ["CALL", null, ["callee:00bddeb0:8"]]
+ 00b5be18 ["INT_ADD", "register:40f0:8", ["const:b5be18:8", "const:4:8"]]
+ 00b5be18 ["CALL", null, ["callee:00bddeb0:8"]]
- 00b5bdd4 bytes 23080294
+ 00b5be18 bytes 26080294
~~~


<a id="compare-712e04fa053288fa04e26bb02fbbf6de"></a>

### [`00b5bf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bf78.md) → [`00b5bfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bfbc.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a90.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ae0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5bfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bf78.md#insn-00b5bfb0) · [`00b5bfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bf78.md#insn-00b5bfdc) · [`00b5bffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bf78.md#insn-00b5bffc)
- 新版 `00b5bff4`（命令位置の公開資料なし） · `00b5c020`（命令位置の公開資料なし） · `00b5c040`（命令位置の公開資料なし）

~~~diff
- 00b5bfb0 ["INT_ADD", "register:40f0:8", ["const:b5bfb0:8", "const:4:8"]]
- 00b5bfb0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b5bff4 ["INT_ADD", "register:40f0:8", ["const:b5bff4:8", "const:4:8"]]
+ 00b5bff4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b5bfb0 bytes 10fc0194
+ 00b5bff4 bytes 13fc0194
- 00b5bfdc ["INT_ADD", "register:40f0:8", ["const:b5bfdc:8", "const:4:8"]]
- 00b5bfdc ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b5c020 ["INT_ADD", "register:40f0:8", ["const:b5c020:8", "const:4:8"]]
+ 00b5c020 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b5bfdc bytes 61fc0194
+ 00b5c020 bytes 64fc0194
- 00b5bffc ["INT_ADD", "register:40f0:8", ["const:b5bffc:8", "const:4:8"]]
- 00b5bffc ["CALL", null, ["callee:00bddeb0:8"]]
+ 00b5c040 ["INT_ADD", "register:40f0:8", ["const:b5c040:8", "const:4:8"]]
+ 00b5c040 ["CALL", null, ["callee:00bddeb0:8"]]
- 00b5bffc bytes 99070294
+ 00b5c040 bytes 9c070294
~~~


<a id="compare-40394998874bb3055819a7b3580a806b"></a>

### [`00b5c038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c038.md) → [`00b5c07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c07c.md) _ZNK8firebase4auth4Auth32FetchProvidersForEmailLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c038.md#insn-00b5c058) · [`00b5c064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c038.md#insn-00b5c064) · [`00b5c070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c038.md#insn-00b5c070)
- 新版 `00b5c09c`（命令位置の公開資料なし） · `00b5c0a8`（命令位置の公開資料なし） · `00b5c0b4`（命令位置の公開資料なし）

~~~diff
- 00b5c058 ["INT_ADD", "register:40f0:8", ["const:b5c058:8", "const:4:8"]]
- 00b5c058 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5c09c ["INT_ADD", "register:40f0:8", ["const:b5c09c:8", "const:4:8"]]
+ 00b5c09c ["CALL", null, ["callee:00bddc20:8"]]
- 00b5c058 bytes de060294
+ 00b5c09c bytes e1060294
- 00b5c064 ["INT_ADD", "register:40f0:8", ["const:b5c064:8", "const:4:8"]]
- 00b5c064 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5c0a8 ["INT_ADD", "register:40f0:8", ["const:b5c0a8:8", "const:4:8"]]
+ 00b5c0a8 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5c064 bytes df060294
+ 00b5c0a8 bytes e2060294
- 00b5c070 ["INT_ADD", "register:40f0:8", ["const:b5c070:8", "const:4:8"]]
- 00b5c070 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5c0b4 ["INT_ADD", "register:40f0:8", ["const:b5c0b4:8", "const:4:8"]]
+ 00b5c0b4 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5c070 bytes 54070294
+ 00b5c0b4 bytes 57070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0d0256ca51f664b11c8e170d33ff2d4"></a>

### [`00b5c0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c0c8.md) → [`00b5c10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c10c.md) _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c0c8.md#insn-00b5c0e8) · [`00b5c0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c0c8.md#insn-00b5c0f4) · [`00b5c100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c0c8.md#insn-00b5c100)
- 新版 `00b5c12c`（命令位置の公開資料なし） · `00b5c138`（命令位置の公開資料なし） · `00b5c144`（命令位置の公開資料なし）

~~~diff
- 00b5c0e8 ["INT_ADD", "register:40f0:8", ["const:b5c0e8:8", "const:4:8"]]
- 00b5c0e8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5c12c ["INT_ADD", "register:40f0:8", ["const:b5c12c:8", "const:4:8"]]
+ 00b5c12c ["CALL", null, ["callee:00bddc20:8"]]
- 00b5c0e8 bytes ba060294
+ 00b5c12c bytes bd060294
- 00b5c0f4 ["INT_ADD", "register:40f0:8", ["const:b5c0f4:8", "const:4:8"]]
- 00b5c0f4 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5c138 ["INT_ADD", "register:40f0:8", ["const:b5c138:8", "const:4:8"]]
+ 00b5c138 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5c0f4 bytes bb060294
+ 00b5c138 bytes be060294
- 00b5c100 ["INT_ADD", "register:40f0:8", ["const:b5c100:8", "const:4:8"]]
- 00b5c100 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5c144 ["INT_ADD", "register:40f0:8", ["const:b5c144:8", "const:4:8"]]
+ 00b5c144 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5c100 bytes 30070294
+ 00b5c144 bytes 33070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a521831e7ffd4f32bc231d0f4f907489"></a>

### [`00b5c158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c158.md) → [`00b5c19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c19c.md) _ZNK8firebase4auth4Auth31SignInWithCustomTokenLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c158.md#insn-00b5c178) · [`00b5c184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c158.md#insn-00b5c184) · [`00b5c190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c158.md#insn-00b5c190)
- 新版 `00b5c1bc`（命令位置の公開資料なし） · `00b5c1c8`（命令位置の公開資料なし） · `00b5c1d4`（命令位置の公開資料なし）

~~~diff
- 00b5c178 ["INT_ADD", "register:40f0:8", ["const:b5c178:8", "const:4:8"]]
- 00b5c178 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5c1bc ["INT_ADD", "register:40f0:8", ["const:b5c1bc:8", "const:4:8"]]
+ 00b5c1bc ["CALL", null, ["callee:00bddc20:8"]]
- 00b5c178 bytes 96060294
+ 00b5c1bc bytes 99060294
- 00b5c184 ["INT_ADD", "register:40f0:8", ["const:b5c184:8", "const:4:8"]]
- 00b5c184 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5c1c8 ["INT_ADD", "register:40f0:8", ["const:b5c1c8:8", "const:4:8"]]
+ 00b5c1c8 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5c184 bytes 97060294
+ 00b5c1c8 bytes 9a060294
- 00b5c190 ["INT_ADD", "register:40f0:8", ["const:b5c190:8", "const:4:8"]]
- 00b5c190 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5c1d4 ["INT_ADD", "register:40f0:8", ["const:b5c1d4:8", "const:4:8"]]
+ 00b5c1d4 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5c190 bytes 0c070294
+ 00b5c1d4 bytes 0f070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea244641c3c523ca8a0c18c22bf9608"></a>

### [`00b5c1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c1e8.md) → [`00b5c22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c22c.md) _ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c1e8.md#insn-00b5c208) · [`00b5c214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c1e8.md#insn-00b5c214) · [`00b5c220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c1e8.md#insn-00b5c220)
- 新版 `00b5c24c`（命令位置の公開資料なし） · `00b5c258`（命令位置の公開資料なし） · `00b5c264`（命令位置の公開資料なし）

~~~diff
- 00b5c208 ["INT_ADD", "register:40f0:8", ["const:b5c208:8", "const:4:8"]]
- 00b5c208 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5c24c ["INT_ADD", "register:40f0:8", ["const:b5c24c:8", "const:4:8"]]
+ 00b5c24c ["CALL", null, ["callee:00bddc20:8"]]
- 00b5c208 bytes 72060294
+ 00b5c24c bytes 75060294
- 00b5c214 ["INT_ADD", "register:40f0:8", ["const:b5c214:8", "const:4:8"]]
- 00b5c214 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5c258 ["INT_ADD", "register:40f0:8", ["const:b5c258:8", "const:4:8"]]
+ 00b5c258 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5c214 bytes 73060294
+ 00b5c258 bytes 76060294
- 00b5c220 ["INT_ADD", "register:40f0:8", ["const:b5c220:8", "const:4:8"]]
- 00b5c220 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5c264 ["INT_ADD", "register:40f0:8", ["const:b5c264:8", "const:4:8"]]
+ 00b5c264 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5c220 bytes e8060294
+ 00b5c264 bytes eb060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e8da789dea438c243a3dd3e7cd40b37"></a>

### [`00b5c278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c278.md) → [`00b5c2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c2bc.md) _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c278.md#insn-00b5c298) · [`00b5c2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c278.md#insn-00b5c2a4) · [`00b5c2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c278.md#insn-00b5c2b0)
- 新版 `00b5c2dc`（命令位置の公開資料なし） · `00b5c2e8`（命令位置の公開資料なし） · `00b5c2f4`（命令位置の公開資料なし）

~~~diff
- 00b5c298 ["INT_ADD", "register:40f0:8", ["const:b5c298:8", "const:4:8"]]
- 00b5c298 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5c2dc ["INT_ADD", "register:40f0:8", ["const:b5c2dc:8", "const:4:8"]]
+ 00b5c2dc ["CALL", null, ["callee:00bddc20:8"]]
- 00b5c298 bytes 4e060294
+ 00b5c2dc bytes 51060294
- 00b5c2a4 ["INT_ADD", "register:40f0:8", ["const:b5c2a4:8", "const:4:8"]]
- 00b5c2a4 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5c2e8 ["INT_ADD", "register:40f0:8", ["const:b5c2e8:8", "const:4:8"]]
+ 00b5c2e8 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5c2a4 bytes 4f060294
+ 00b5c2e8 bytes 52060294
- 00b5c2b0 ["INT_ADD", "register:40f0:8", ["const:b5c2b0:8", "const:4:8"]]
- 00b5c2b0 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5c2f4 ["INT_ADD", "register:40f0:8", ["const:b5c2f4:8", "const:4:8"]]
+ 00b5c2f4 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5c2b0 bytes c4060294
+ 00b5c2f4 bytes c7060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-537f2f84abaf0d0c5fac00477aa74566"></a>

### [`00b5c308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c308.md) → [`00b5c34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c34c.md) _ZNK8firebase4auth4Auth36SignInWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c308.md#insn-00b5c328) · [`00b5c334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c308.md#insn-00b5c334) · [`00b5c340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c308.md#insn-00b5c340)
- 新版 `00b5c36c`（命令位置の公開資料なし） · `00b5c378`（命令位置の公開資料なし） · `00b5c384`（命令位置の公開資料なし）

~~~diff
- 00b5c328 ["INT_ADD", "register:40f0:8", ["const:b5c328:8", "const:4:8"]]
- 00b5c328 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5c36c ["INT_ADD", "register:40f0:8", ["const:b5c36c:8", "const:4:8"]]
+ 00b5c36c ["CALL", null, ["callee:00bddc20:8"]]
- 00b5c328 bytes 2a060294
+ 00b5c36c bytes 2d060294
- 00b5c334 ["INT_ADD", "register:40f0:8", ["const:b5c334:8", "const:4:8"]]
- 00b5c334 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5c378 ["INT_ADD", "register:40f0:8", ["const:b5c378:8", "const:4:8"]]
+ 00b5c378 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5c334 bytes 2b060294
+ 00b5c378 bytes 2e060294
- 00b5c340 ["INT_ADD", "register:40f0:8", ["const:b5c340:8", "const:4:8"]]
- 00b5c340 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5c384 ["INT_ADD", "register:40f0:8", ["const:b5c384:8", "const:4:8"]]
+ 00b5c384 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5c340 bytes a0060294
+ 00b5c384 bytes a3060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0abe55b7e1fda8e9a7720f7cccd70ede"></a>

### [`00b5c398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c398.md) → [`00b5c3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c3dc.md) _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c398.md#insn-00b5c3b8) · [`00b5c3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c398.md#insn-00b5c3c4) · [`00b5c3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c398.md#insn-00b5c3d0)
- 新版 `00b5c3fc`（命令位置の公開資料なし） · `00b5c408`（命令位置の公開資料なし） · `00b5c414`（命令位置の公開資料なし）

~~~diff
- 00b5c3b8 ["INT_ADD", "register:40f0:8", ["const:b5c3b8:8", "const:4:8"]]
- 00b5c3b8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5c3fc ["INT_ADD", "register:40f0:8", ["const:b5c3fc:8", "const:4:8"]]
+ 00b5c3fc ["CALL", null, ["callee:00bddc20:8"]]
- 00b5c3b8 bytes 06060294
+ 00b5c3fc bytes 09060294
- 00b5c3c4 ["INT_ADD", "register:40f0:8", ["const:b5c3c4:8", "const:4:8"]]
- 00b5c3c4 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5c408 ["INT_ADD", "register:40f0:8", ["const:b5c408:8", "const:4:8"]]
+ 00b5c408 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5c3c4 bytes 07060294
+ 00b5c408 bytes 0a060294
- 00b5c3d0 ["INT_ADD", "register:40f0:8", ["const:b5c3d0:8", "const:4:8"]]
- 00b5c3d0 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5c414 ["INT_ADD", "register:40f0:8", ["const:b5c414:8", "const:4:8"]]
+ 00b5c414 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5c3d0 bytes 7c060294
+ 00b5c414 bytes 7f060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a31305e8014121945d78979f5ed8e8f"></a>

### [`00b5c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c478.md) → [`00b5c4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4bc.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a70.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a70.md)
- 新版 呼出元 1件 [`00be0ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ac0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c478.md#insn-00b5c494) · [`00b5c4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c478.md#insn-00b5c4a0)
- 新版 `00b5c4d8`（命令位置の公開資料なし） · `00b5c4e4`（命令位置の公開資料なし）

~~~diff
- 00b5c494 ["INT_ADD", "register:40f0:8", ["const:b5c494:8", "const:4:8"]]
- 00b5c494 ["CALL", null, ["callee:00be0ac0:8"]]
+ 00b5c4d8 ["INT_ADD", "register:40f0:8", ["const:b5c4d8:8", "const:4:8"]]
+ 00b5c4d8 ["CALL", null, ["callee:00be0ac0:8"]]
- 00b5c494 bytes 77110294
+ 00b5c4d8 bytes 7a110294
- 00b5c4a0 ["INT_ADD", "register:40f0:8", ["const:b5c4a0:8", "const:4:8"]]
- 00b5c4a0 ["CALL", null, ["callee:00be0ac0:8"]]
+ 00b5c4e4 ["INT_ADD", "register:40f0:8", ["const:b5c4e4:8", "const:4:8"]]
+ 00b5c4e4 ["CALL", null, ["callee:00be0ac0:8"]]
- 00b5c4a0 bytes 74110294
+ 00b5c4e4 bytes 77110294
~~~


<a id="compare-cf7ac15256a7e0cfbb71ef7191daf719"></a>

### [`00b5c864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c864.md) → [`00b5c8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c8a8.md) _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0950.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be09a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09a0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c864.md#insn-00b5c8c0)
- 新版 `00b5c904`（命令位置の公開資料なし）

~~~diff
- 00b5c8c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5c8c0 ["INT_ADD", "register:40f0:8", ["const:b5c8c0:8", "const:4:8"]]
- 00b5c8c0 ["CALLIND", null, ["register:0:8"]]
+ 00b5c904 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c904 ["INT_ADD", "register:40f0:8", ["const:b5c904:8", "const:4:8"]]
+ 00b5c904 ["CALLIND", null, ["register:0:8"]]
- 00b5c8c0 bytes 00013fd6
+ 00b5c904 bytes 00013fd6
~~~


<a id="compare-6b13bcefab9b0898794301b5d9b5be19"></a>

### [`00b5c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c938.md) → [`00b5c97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c97c.md) _ZNK8firebase4auth4UsereqERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bddbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c938.md#insn-00b5c948) · [`00b5c954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c938.md#insn-00b5c954)
- 新版 `00b5c98c`（命令位置の公開資料なし） · `00b5c998`（命令位置の公開資料なし）

~~~diff
- 00b5c948 ["INT_ADD", "register:40f0:8", ["const:b5c948:8", "const:4:8"]]
- 00b5c948 ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b5c98c ["INT_ADD", "register:40f0:8", ["const:b5c98c:8", "const:4:8"]]
+ 00b5c98c ["CALL", null, ["callee:00bddbf0:8"]]
- 00b5c948 bytes 96040294
+ 00b5c98c bytes 99040294
- 00b5c954 ["INT_ADD", "register:40f0:8", ["const:b5c954:8", "const:4:8"]]
- 00b5c954 ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b5c998 ["INT_ADD", "register:40f0:8", ["const:b5c998:8", "const:4:8"]]
+ 00b5c998 ["CALL", null, ["callee:00bddbf0:8"]]
- 00b5c954 bytes 93040294
+ 00b5c998 bytes 96040294
~~~


<a id="compare-347bcd7441a1c0d1a5bcbb9888b7606d"></a>

### [`00b5c96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c96c.md) → [`00b5c9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9b0.md) _ZNK8firebase4auth4UserneERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bddbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c96c.md#insn-00b5c97c) · [`00b5c988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c96c.md#insn-00b5c988)
- 新版 `00b5c9c0`（命令位置の公開資料なし） · `00b5c9cc`（命令位置の公開資料なし）

~~~diff
- 00b5c97c ["INT_ADD", "register:40f0:8", ["const:b5c97c:8", "const:4:8"]]
- 00b5c97c ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b5c9c0 ["INT_ADD", "register:40f0:8", ["const:b5c9c0:8", "const:4:8"]]
+ 00b5c9c0 ["CALL", null, ["callee:00bddbf0:8"]]
- 00b5c97c bytes 89040294
+ 00b5c9c0 bytes 8c040294
- 00b5c988 ["INT_ADD", "register:40f0:8", ["const:b5c988:8", "const:4:8"]]
- 00b5c988 ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b5c9cc ["INT_ADD", "register:40f0:8", ["const:b5c9cc:8", "const:4:8"]]
+ 00b5c9cc ["CALL", null, ["callee:00bddbf0:8"]]
- 00b5c988 bytes 86040294
+ 00b5c9cc bytes 89040294
~~~


<a id="compare-01eba091ea9f85062f3aa63b6e7d9140"></a>

### [`00b5e1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e1d8.md) → [`00b5e21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e21c.md) _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be09c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09c0.md) [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be0a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a10.md) [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e1d8.md#insn-00b5e1ec)
- 新版 `00b5e230`（命令位置の公開資料なし）

~~~diff
- 00b5e1ec ["INT_ADD", "register:40f0:8", ["const:b5e1ec:8", "const:4:8"]]
- 00b5e1ec ["CALL", null, ["callee:00be0c30:8"]]
+ 00b5e230 ["INT_ADD", "register:40f0:8", ["const:b5e230:8", "const:4:8"]]
+ 00b5e230 ["CALL", null, ["callee:00be0c30:8"]]
- 00b5e1ec bytes 7d0a0294
+ 00b5e230 bytes 800a0294
~~~


<a id="compare-d07c81d48a0f53315dcb652ad8ccabbe"></a>

### [`00b5e200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md) → [`00b5e244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e244.md) _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be09a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09a0.md) [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be09f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09f0.md) [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md#insn-00b5e218) · [`00b5e224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md#insn-00b5e224) · [`00b5e22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md#insn-00b5e22c)
- 新版 `00b5e25c`（命令位置の公開資料なし） · `00b5e268`（命令位置の公開資料なし） · `00b5e270`（命令位置の公開資料なし）

~~~diff
- 00b5e218 ["INT_ADD", "register:40f0:8", ["const:b5e218:8", "const:4:8"]]
- 00b5e218 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5e25c ["INT_ADD", "register:40f0:8", ["const:b5e25c:8", "const:4:8"]]
+ 00b5e25c ["CALL", null, ["callee:00bddc20:8"]]
- 00b5e218 bytes 6efe0194
+ 00b5e25c bytes 71fe0194
- 00b5e224 ["INT_ADD", "register:40f0:8", ["const:b5e224:8", "const:4:8"]]
- 00b5e224 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b5e268 ["INT_ADD", "register:40f0:8", ["const:b5e268:8", "const:4:8"]]
+ 00b5e268 ["CALL", null, ["callee:00bddc30:8"]]
- 00b5e224 bytes 6ffe0194
+ 00b5e268 bytes 72fe0194
- 00b5e22c ["INT_ADD", "register:40f0:8", ["const:b5e22c:8", "const:4:8"]]
- 00b5e22c ["CALL", null, ["callee:00be0c30:8"]]
+ 00b5e270 ["INT_ADD", "register:40f0:8", ["const:b5e270:8", "const:4:8"]]
+ 00b5e270 ["CALL", null, ["callee:00be0c30:8"]]
- 00b5e22c bytes 6d0a0294
+ 00b5e270 bytes 700a0294
~~~


<a id="compare-c2b7771c09e893ebe2fca03f3c550508"></a>

### [`00b5e444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e444.md) → [`00b5e488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e488.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFut

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c90.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b80.md)
- 新版 呼出元 1件 [`00be0ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ce0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e444.md#insn-00b5e478) · [`00b5e48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e444.md#insn-00b5e48c) · [`00b5e4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e444.md#insn-00b5e4b8)
- 新版 `00b5e4bc`（命令位置の公開資料なし） · `00b5e4d0`（命令位置の公開資料なし） · `00b5e4fc`（命令位置の公開資料なし）

~~~diff
- 00b5e478 ["INT_ADD", "register:40f0:8", ["const:b5e478:8", "const:4:8"]]
- 00b5e478 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b5e4bc ["INT_ADD", "register:40f0:8", ["const:b5e4bc:8", "const:4:8"]]
+ 00b5e4bc ["CALL", null, ["callee:00be0d10:8"]]
- 00b5e478 bytes 120a0294
+ 00b5e4bc bytes 150a0294
- 00b5e48c ["INT_ADD", "register:40f0:8", ["const:b5e48c:8", "const:4:8"]]
- 00b5e48c ["CALL", null, ["callee:00bddf80:8"]]
+ 00b5e4d0 ["INT_ADD", "register:40f0:8", ["const:b5e4d0:8", "const:4:8"]]
+ 00b5e4d0 ["CALL", null, ["callee:00bddf80:8"]]
- 00b5e48c bytes a9fe0194
+ 00b5e4d0 bytes acfe0194
- 00b5e4b8 ["INT_ADD", "register:40f0:8", ["const:b5e4b8:8", "const:4:8"]]
- 00b5e4b8 ["CALL", null, ["callee:00be0bd0:8"]]
+ 00b5e4fc ["INT_ADD", "register:40f0:8", ["const:b5e4fc:8", "const:4:8"]]
+ 00b5e4fc ["CALL", null, ["callee:00be0bd0:8"]]
- 00b5e4b8 bytes b2090294
+ 00b5e4fc bytes b5090294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad52d5c56ffb4343d07db4982e465110"></a>

### [`00b5ea6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ea6c.md) → [`00b5eab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eab0.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c80.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b70.md)
- 新版 呼出元 1件 [`00be0cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cd0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5eaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ea6c.md#insn-00b5eaa0) · [`00b5eab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ea6c.md#insn-00b5eab4) · [`00b5eae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ea6c.md#insn-00b5eae0)
- 新版 `00b5eae4`（命令位置の公開資料なし） · `00b5eaf8`（命令位置の公開資料なし） · `00b5eb24`（命令位置の公開資料なし）

~~~diff
- 00b5eaa0 ["INT_ADD", "register:40f0:8", ["const:b5eaa0:8", "const:4:8"]]
- 00b5eaa0 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b5eae4 ["INT_ADD", "register:40f0:8", ["const:b5eae4:8", "const:4:8"]]
+ 00b5eae4 ["CALL", null, ["callee:00be0d10:8"]]
- 00b5eaa0 bytes 88080294
+ 00b5eae4 bytes 8b080294
- 00b5eab4 ["INT_ADD", "register:40f0:8", ["const:b5eab4:8", "const:4:8"]]
- 00b5eab4 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b5eaf8 ["INT_ADD", "register:40f0:8", ["const:b5eaf8:8", "const:4:8"]]
+ 00b5eaf8 ["CALL", null, ["callee:00bddf80:8"]]
- 00b5eab4 bytes 1ffd0194
+ 00b5eaf8 bytes 22fd0194
- 00b5eae0 ["INT_ADD", "register:40f0:8", ["const:b5eae0:8", "const:4:8"]]
- 00b5eae0 ["CALL", null, ["callee:00be0bc0:8"]]
+ 00b5eb24 ["INT_ADD", "register:40f0:8", ["const:b5eb24:8", "const:4:8"]]
+ 00b5eb24 ["CALL", null, ["callee:00be0bc0:8"]]
- 00b5eae0 bytes 24080294
+ 00b5eb24 bytes 27080294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ce6cf93d38d83955a31aba4044a246a"></a>

### [`00b5ee20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ee20.md) → [`00b5ee64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ee64.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ca0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b90.md)
- 新版 呼出元 1件 [`00be0cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cf0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ee54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ee20.md#insn-00b5ee54) · [`00b5ee68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ee20.md#insn-00b5ee68) · [`00b5ee94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ee20.md#insn-00b5ee94)
- 新版 `00b5ee98`（命令位置の公開資料なし） · `00b5eeac`（命令位置の公開資料なし） · `00b5eed8`（命令位置の公開資料なし）

~~~diff
- 00b5ee54 ["INT_ADD", "register:40f0:8", ["const:b5ee54:8", "const:4:8"]]
- 00b5ee54 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b5ee98 ["INT_ADD", "register:40f0:8", ["const:b5ee98:8", "const:4:8"]]
+ 00b5ee98 ["CALL", null, ["callee:00be0d10:8"]]
- 00b5ee54 bytes 9b070294
+ 00b5ee98 bytes 9e070294
- 00b5ee68 ["INT_ADD", "register:40f0:8", ["const:b5ee68:8", "const:4:8"]]
- 00b5ee68 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b5eeac ["INT_ADD", "register:40f0:8", ["const:b5eeac:8", "const:4:8"]]
+ 00b5eeac ["CALL", null, ["callee:00bddf80:8"]]
- 00b5ee68 bytes 32fc0194
+ 00b5eeac bytes 35fc0194
- 00b5ee94 ["INT_ADD", "register:40f0:8", ["const:b5ee94:8", "const:4:8"]]
- 00b5ee94 ["CALL", null, ["callee:00be0be0:8"]]
+ 00b5eed8 ["INT_ADD", "register:40f0:8", ["const:b5eed8:8", "const:4:8"]]
+ 00b5eed8 ["CALL", null, ["callee:00be0be0:8"]]
- 00b5ee94 bytes 3f070294
+ 00b5eed8 bytes 42070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59e6d799174b2614a735800c978c52d9"></a>

### [`00b5fd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fd90.md) → [`00b5fdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fdd4.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cb0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md)
- 新版 呼出元 1件 [`00be0d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d00.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bdee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fdc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fd90.md#insn-00b5fdc4) · [`00b5fdd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fd90.md#insn-00b5fdd8) · [`00b5fe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fd90.md#insn-00b5fe04)
- 新版 `00b5fe08`（命令位置の公開資料なし） · `00b5fe1c`（命令位置の公開資料なし） · `00b5fe48`（命令位置の公開資料なし）

~~~diff
- 00b5fdc4 ["INT_ADD", "register:40f0:8", ["const:b5fdc4:8", "const:4:8"]]
- 00b5fdc4 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b5fe08 ["INT_ADD", "register:40f0:8", ["const:b5fe08:8", "const:4:8"]]
+ 00b5fe08 ["CALL", null, ["callee:00be0d10:8"]]
- 00b5fdc4 bytes bf030294
+ 00b5fe08 bytes c2030294
- 00b5fdd8 ["INT_ADD", "register:40f0:8", ["const:b5fdd8:8", "const:4:8"]]
- 00b5fdd8 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b5fe1c ["INT_ADD", "register:40f0:8", ["const:b5fe1c:8", "const:4:8"]]
+ 00b5fe1c ["CALL", null, ["callee:00bddf80:8"]]
- 00b5fdd8 bytes 56f80194
+ 00b5fe1c bytes 59f80194
- 00b5fe04 ["INT_ADD", "register:40f0:8", ["const:b5fe04:8", "const:4:8"]]
- 00b5fe04 ["CALL", null, ["callee:00bdee00:8"]]
+ 00b5fe48 ["INT_ADD", "register:40f0:8", ["const:b5fe48:8", "const:4:8"]]
+ 00b5fe48 ["CALL", null, ["callee:00bdee00:8"]]
- 00b5fe04 bytes ebfb0194
+ 00b5fe48 bytes eefb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b9a4a89461dc994fee9fd9c94eeef61"></a>

### [`00b5ff34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ff34.md) → [`00b5ff78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5ff78.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b5e244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e244.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00b5e288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e288.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ff34.md#insn-00b5ff84) · [`00b5ffa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ff34.md#insn-00b5ffa0)
- 新版 `00b5ffc8`（命令位置の公開資料なし） · `00b5ffe4`（命令位置の公開資料なし）

~~~diff
- 00b5ff84 ["INT_ADD", "register:40f0:8", ["const:b5ff84:8", "const:4:8"]]
- 00b5ff84 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b5ffc8 ["INT_ADD", "register:40f0:8", ["const:b5ffc8:8", "const:4:8"]]
+ 00b5ffc8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b5ff84 bytes 23ec0194
+ 00b5ffc8 bytes 26ec0194
- 00b5ffa0 ["INT_ADD", "register:40f0:8", ["const:b5ffa0:8", "const:4:8"]]
- 00b5ffa0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b5ffe4 ["INT_ADD", "register:40f0:8", ["const:b5ffe4:8", "const:4:8"]]
+ 00b5ffe4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b5ffa0 bytes 1cec0194
+ 00b5ffe4 bytes 1fec0194
~~~


<a id="compare-6523b6ac26d1175b1dda2d7a0bd2eb11"></a>

### [`00b600c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md) → [`00b60104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60104.md) _ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b5e244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e244.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b50.md)
- 新版 呼出元 1件 [`00b5e288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e288.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b600f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md#insn-00b600f8) · [`00b60110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md#insn-00b60110) · [`00b60138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md#insn-00b60138)
- 新版 `00b6013c`（命令位置の公開資料なし） · `00b60154`（命令位置の公開資料なし） · `00b6017c`（命令位置の公開資料なし）

~~~diff
- 00b600f8 ["INT_ADD", "register:40f0:8", ["const:b600f8:8", "const:4:8"]]
- 00b600f8 ["CALL", null, ["callee:00be0d20:8"]]
+ 00b6013c ["INT_ADD", "register:40f0:8", ["const:b6013c:8", "const:4:8"]]
+ 00b6013c ["CALL", null, ["callee:00be0d20:8"]]
- 00b600f8 bytes f6020294
+ 00b6013c bytes f9020294
- 00b60110 ["INT_ADD", "register:40f0:8", ["const:b60110:8", "const:4:8"]]
- 00b60110 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b60154 ["INT_ADD", "register:40f0:8", ["const:b60154:8", "const:4:8"]]
+ 00b60154 ["CALL", null, ["callee:00bddf80:8"]]
- 00b60110 bytes 88f70194
+ 00b60154 bytes 8bf70194
- 00b60138 ["INT_ADD", "register:40f0:8", ["const:b60138:8", "const:4:8"]]
- 00b60138 ["CALL", null, ["callee:00be0ba0:8"]]
+ 00b6017c ["INT_ADD", "register:40f0:8", ["const:b6017c:8", "const:4:8"]]
+ 00b6017c ["CALL", null, ["callee:00be0ba0:8"]]
- 00b60138 bytes 86020294
+ 00b6017c bytes 89020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1d8a78c8ab4c416d85dac636767ae5c"></a>

### [`00b602cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md) → [`00b60310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60310.md) _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cf0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00be0d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d40.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b602ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md#insn-00b602ec) · [`00b60300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md#insn-00b60300) · [`00b60314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md#insn-00b60314)
- 新版 `00b60330`（命令位置の公開資料なし） · `00b60344`（命令位置の公開資料なし） · `00b60358`（命令位置の公開資料なし）

~~~diff
- 00b602ec ["INT_ADD", "register:40f0:8", ["const:b602ec:8", "const:4:8"]]
- 00b602ec ["CALL", null, ["callee:00bdde10:8"]]
+ 00b60330 ["INT_ADD", "register:40f0:8", ["const:b60330:8", "const:4:8"]]
+ 00b60330 ["CALL", null, ["callee:00bdde10:8"]]
- 00b602ec bytes b5f60194
+ 00b60330 bytes b8f60194
- 00b60300 ["INT_ADD", "register:40f0:8", ["const:b60300:8", "const:4:8"]]
- 00b60300 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b60344 ["INT_ADD", "register:40f0:8", ["const:b60344:8", "const:4:8"]]
+ 00b60344 ["CALL", null, ["callee:00bddf80:8"]]
- 00b60300 bytes 0cf70194
+ 00b60344 bytes 0ff70194
- 00b60314 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60314 ["INT_ADD", "register:40f0:8", ["const:b60314:8", "const:4:8"]]
- 00b60314 ["CALLIND", null, ["register:0:8"]]
+ 00b60358 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60358 ["INT_ADD", "register:40f0:8", ["const:b60358:8", "const:4:8"]]
+ 00b60358 ["CALLIND", null, ["register:0:8"]]
- 00b60314 bytes 00013fd6
+ 00b60358 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0de1b2e390cfd918f7345f33d936e11"></a>

### [`00b6036c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md) → [`00b603b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b603b0.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b5e920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e920.md) [`00b6c200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c200.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00bddb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)
- 新版 呼出元 2件 [`00b5e964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e964.md) [`00b6c244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c244.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00bddbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbe0.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md#insn-00b60384) · [`00b6038c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md#insn-00b6038c) · [`00b60394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md#insn-00b60394)
- 新版 `00b603c8`（命令位置の公開資料なし） · `00b603d0`（命令位置の公開資料なし） · `00b603d8`（命令位置の公開資料なし）

~~~diff
- 00b60384 ["INT_ADD", "register:40f0:8", ["const:b60384:8", "const:4:8"]]
- 00b60384 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b603c8 ["INT_ADD", "register:40f0:8", ["const:b603c8:8", "const:4:8"]]
+ 00b603c8 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b60384 bytes 03f60194
+ 00b603c8 bytes 06f60194
- 00b6038c ["INT_ADD", "register:40f0:8", ["const:b6038c:8", "const:4:8"]]
- 00b6038c ["CALL", null, ["callee:00bddba0:8"]]
+ 00b603d0 ["INT_ADD", "register:40f0:8", ["const:b603d0:8", "const:4:8"]]
+ 00b603d0 ["CALL", null, ["callee:00bddba0:8"]]
- 00b6038c bytes f1f50194
+ 00b603d0 bytes f4f50194
- 00b60394 ["INT_ADD", "register:40f0:8", ["const:b60394:8", "const:4:8"]]
- 00b60394 ["CALL", null, ["callee:00bddba0:8"]]
+ 00b603d8 ["INT_ADD", "register:40f0:8", ["const:b603d8:8", "const:4:8"]]
+ 00b603d8 ["CALL", null, ["callee:00bddba0:8"]]
- 00b60394 bytes eff50194
+ 00b603d8 bytes f2f50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91dc89dd09cf8f29447231bbb26ab746"></a>

### [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) → [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) _ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00b5e75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e75c.md) [`00b5ef24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ef24.md) [`00b5f194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f194.md) [`00b5f320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f320.md) [`00b5f5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b40.md)
- 新版 呼出元 8件 [`00b5e7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md) [`00b5ef68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ef68.md) [`00b5f1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f1d8.md) [`00b5f364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f364.md) [`00b5f5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md#insn-00b60410) · [`00b60428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md#insn-00b60428) · [`00b60450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md#insn-00b60450)
- 新版 `00b60454`（命令位置の公開資料なし） · `00b6046c`（命令位置の公開資料なし） · `00b60494`（命令位置の公開資料なし）

~~~diff
- 00b60410 ["INT_ADD", "register:40f0:8", ["const:b60410:8", "const:4:8"]]
- 00b60410 ["CALL", null, ["callee:00be0d20:8"]]
+ 00b60454 ["INT_ADD", "register:40f0:8", ["const:b60454:8", "const:4:8"]]
+ 00b60454 ["CALL", null, ["callee:00be0d20:8"]]
- 00b60410 bytes 30020294
+ 00b60454 bytes 33020294
- 00b60428 ["INT_ADD", "register:40f0:8", ["const:b60428:8", "const:4:8"]]
- 00b60428 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b6046c ["INT_ADD", "register:40f0:8", ["const:b6046c:8", "const:4:8"]]
+ 00b6046c ["CALL", null, ["callee:00bddf80:8"]]
- 00b60428 bytes c2f60194
+ 00b6046c bytes c5f60194
- 00b60450 ["INT_ADD", "register:40f0:8", ["const:b60450:8", "const:4:8"]]
- 00b60450 ["CALL", null, ["callee:00be0b90:8"]]
+ 00b60494 ["INT_ADD", "register:40f0:8", ["const:b60494:8", "const:4:8"]]
+ 00b60494 ["CALL", null, ["callee:00be0b90:8"]]
- 00b60450 bytes bc010294
+ 00b60494 bytes bf010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91b9d4708bbc280d4db1fcca41fbb88f"></a>

### [`00b605e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b605e4.md) → [`00b60628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60628.md) _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ce0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00be0d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d30.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b605e4.md#insn-00b60604) · [`00b60618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b605e4.md#insn-00b60618) · [`00b6062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b605e4.md#insn-00b6062c)
- 新版 `00b60648`（命令位置の公開資料なし） · `00b6065c`（命令位置の公開資料なし） · `00b60670`（命令位置の公開資料なし）

~~~diff
- 00b60604 ["INT_ADD", "register:40f0:8", ["const:b60604:8", "const:4:8"]]
- 00b60604 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b60648 ["INT_ADD", "register:40f0:8", ["const:b60648:8", "const:4:8"]]
+ 00b60648 ["CALL", null, ["callee:00bdde10:8"]]
- 00b60604 bytes eff50194
+ 00b60648 bytes f2f50194
- 00b60618 ["INT_ADD", "register:40f0:8", ["const:b60618:8", "const:4:8"]]
- 00b60618 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b6065c ["INT_ADD", "register:40f0:8", ["const:b6065c:8", "const:4:8"]]
+ 00b6065c ["CALL", null, ["callee:00bddf80:8"]]
- 00b60618 bytes 46f60194
+ 00b6065c bytes 49f60194
- 00b6062c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6062c ["INT_ADD", "register:40f0:8", ["const:b6062c:8", "const:4:8"]]
- 00b6062c ["CALLIND", null, ["register:0:8"]]
+ 00b60670 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60670 ["INT_ADD", "register:40f0:8", ["const:b60670:8", "const:4:8"]]
+ 00b60670 ["CALLIND", null, ["register:0:8"]]
- 00b6062c bytes 00013fd6
+ 00b60670 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dcb25ca5b0a92d5fa6f21c885333340"></a>

### [`00b607a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md) → [`00b607e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md) _ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b5eb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5eb70.md) [`00b70898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b60.md)
- 新版 呼出元 2件 [`00b5ebb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ebb4.md) [`00b708dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b607d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md#insn-00b607d8) · [`00b607f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md#insn-00b607f0) · [`00b60818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md#insn-00b60818)
- 新版 `00b6081c`（命令位置の公開資料なし） · `00b60834`（命令位置の公開資料なし） · `00b6085c`（命令位置の公開資料なし）

~~~diff
- 00b607d8 ["INT_ADD", "register:40f0:8", ["const:b607d8:8", "const:4:8"]]
- 00b607d8 ["CALL", null, ["callee:00be0d20:8"]]
+ 00b6081c ["INT_ADD", "register:40f0:8", ["const:b6081c:8", "const:4:8"]]
+ 00b6081c ["CALL", null, ["callee:00be0d20:8"]]
- 00b607d8 bytes 3e010294
+ 00b6081c bytes 41010294
- 00b607f0 ["INT_ADD", "register:40f0:8", ["const:b607f0:8", "const:4:8"]]
- 00b607f0 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b60834 ["INT_ADD", "register:40f0:8", ["const:b60834:8", "const:4:8"]]
+ 00b60834 ["CALL", null, ["callee:00bddf80:8"]]
- 00b607f0 bytes d0f50194
+ 00b60834 bytes d3f50194
- 00b60818 ["INT_ADD", "register:40f0:8", ["const:b60818:8", "const:4:8"]]
- 00b60818 ["CALL", null, ["callee:00be0bb0:8"]]
+ 00b6085c ["INT_ADD", "register:40f0:8", ["const:b6085c:8", "const:4:8"]]
+ 00b6085c ["CALL", null, ["callee:00be0bb0:8"]]
- 00b60818 bytes d2000294
+ 00b6085c bytes d5000294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22eff72b3bf9792f22bbe3c323a58f53"></a>

### [`00b609ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b609ac.md) → [`00b609f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b609f0.md) _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d00.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00be0d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d50.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b609cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b609ac.md#insn-00b609cc) · [`00b609e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b609ac.md#insn-00b609e0) · [`00b609f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b609ac.md#insn-00b609f4)
- 新版 `00b60a10`（命令位置の公開資料なし） · `00b60a24`（命令位置の公開資料なし） · `00b60a38`（命令位置の公開資料なし）

~~~diff
- 00b609cc ["INT_ADD", "register:40f0:8", ["const:b609cc:8", "const:4:8"]]
- 00b609cc ["CALL", null, ["callee:00bdde10:8"]]
+ 00b60a10 ["INT_ADD", "register:40f0:8", ["const:b60a10:8", "const:4:8"]]
+ 00b60a10 ["CALL", null, ["callee:00bdde10:8"]]
- 00b609cc bytes fdf40194
+ 00b60a10 bytes 00f50194
- 00b609e0 ["INT_ADD", "register:40f0:8", ["const:b609e0:8", "const:4:8"]]
- 00b609e0 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b60a24 ["INT_ADD", "register:40f0:8", ["const:b60a24:8", "const:4:8"]]
+ 00b60a24 ["CALL", null, ["callee:00bddf80:8"]]
- 00b609e0 bytes 54f50194
+ 00b60a24 bytes 57f50194
- 00b609f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b609f4 ["INT_ADD", "register:40f0:8", ["const:b609f4:8", "const:4:8"]]
- 00b609f4 ["CALLIND", null, ["register:0:8"]]
+ 00b60a38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60a38 ["INT_ADD", "register:40f0:8", ["const:b60a38:8", "const:4:8"]]
+ 00b60a38 ["CALLIND", null, ["register:0:8"]]
- 00b609f4 bytes 00013fd6
+ 00b60a38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ef4532d5fdc8f1db97d952cb71e7a5"></a>

### [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) → [`00b60b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md) _ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00b5fb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fb44.md) [`00b6fde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fde4.md) [`00b7000c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md) [`00b70ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ae4.md) [`00b70cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70cd4.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ba0.md)
- 新版 呼出元 8件 [`00b5fb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fb88.md) [`00b6fe28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fe28.md) [`00b70050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70050.md) [`00b70b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70b28.md) [`00b70d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70d18.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md#insn-00b60b8c) · [`00b60ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md#insn-00b60ba4) · [`00b60bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md#insn-00b60bcc)
- 新版 `00b60bd0`（命令位置の公開資料なし） · `00b60be8`（命令位置の公開資料なし） · `00b60c10`（命令位置の公開資料なし）

~~~diff
- 00b60b8c ["INT_ADD", "register:40f0:8", ["const:b60b8c:8", "const:4:8"]]
- 00b60b8c ["CALL", null, ["callee:00be0d20:8"]]
+ 00b60bd0 ["INT_ADD", "register:40f0:8", ["const:b60bd0:8", "const:4:8"]]
+ 00b60bd0 ["CALL", null, ["callee:00be0d20:8"]]
- 00b60b8c bytes 51000294
+ 00b60bd0 bytes 54000294
- 00b60ba4 ["INT_ADD", "register:40f0:8", ["const:b60ba4:8", "const:4:8"]]
- 00b60ba4 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b60be8 ["INT_ADD", "register:40f0:8", ["const:b60be8:8", "const:4:8"]]
+ 00b60be8 ["CALL", null, ["callee:00bddf80:8"]]
- 00b60ba4 bytes e3f40194
+ 00b60be8 bytes e6f40194
- 00b60bcc ["INT_ADD", "register:40f0:8", ["const:b60bcc:8", "const:4:8"]]
- 00b60bcc ["CALL", null, ["callee:00be0bf0:8"]]
+ 00b60c10 ["INT_ADD", "register:40f0:8", ["const:b60c10:8", "const:4:8"]]
+ 00b60c10 ["CALL", null, ["callee:00be0bf0:8"]]
- 00b60bcc bytes f5ff0194
+ 00b60c10 bytes f8ff0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98581ac73879b052ca2499bca151ac3a"></a>

### [`00b64d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64d0c.md) → [`00b64d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64d50.md) _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cc0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde080.md) [`00be0d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d30.md)
- 新版 呼出元 1件 [`00be0d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d10.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0d0.md) [`00be0d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b64d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64d0c.md#insn-00b64d40) · [`00b64d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64d0c.md#insn-00b64d58) · [`00b64d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64d0c.md#insn-00b64d64)
- 新版 `00b64d84`（命令位置の公開資料なし） · `00b64d9c`（命令位置の公開資料なし） · `00b64da8`（命令位置の公開資料なし）

~~~diff
- 00b64d40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64d40 ["INT_ADD", "register:40f0:8", ["const:b64d40:8", "const:4:8"]]
- 00b64d40 ["CALLIND", null, ["register:0:8"]]
+ 00b64d84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64d84 ["INT_ADD", "register:40f0:8", ["const:b64d84:8", "const:4:8"]]
+ 00b64d84 ["CALLIND", null, ["register:0:8"]]
- 00b64d40 bytes 00013fd6
+ 00b64d84 bytes 00013fd6
- 00b64d58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64d58 ["INT_ADD", "register:40f0:8", ["const:b64d58:8", "const:4:8"]]
- 00b64d58 ["CALLIND", null, ["register:0:8"]]
+ 00b64d9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64d9c ["INT_ADD", "register:40f0:8", ["const:b64d9c:8", "const:4:8"]]
+ 00b64d9c ["CALLIND", null, ["register:0:8"]]
- 00b64d58 bytes 00013fd6
+ 00b64d9c bytes 00013fd6
- 00b64d64 ["INT_ADD", "register:40f0:8", ["const:b64d64:8", "const:4:8"]]
- 00b64d64 ["CALL", null, ["callee:00be0d80:8"]]
+ 00b64da8 ["INT_ADD", "register:40f0:8", ["const:b64da8:8", "const:4:8"]]
+ 00b64da8 ["CALL", null, ["callee:00be0d80:8"]]
- 00b64d64 bytes f3ef0194
+ 00b64da8 bytes f6ef0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f08dc551f84032fb2c9d9161cafdf51"></a>

### [`00b64e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md) → [`00b64e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64e88.md) _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c30.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be0c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c80.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b64e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md#insn-00b64e74) · [`00b64e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md#insn-00b64e90) · [`00b64ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md#insn-00b64ea8)
- 新版 `00b64eb8`（命令位置の公開資料なし） · `00b64ed4`（命令位置の公開資料なし） · `00b64eec`（命令位置の公開資料なし）

~~~diff
- 00b64e74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64e74 ["INT_ADD", "register:40f0:8", ["const:b64e74:8", "const:4:8"]]
- 00b64e74 ["CALLIND", null, ["register:0:8"]]
+ 00b64eb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64eb8 ["INT_ADD", "register:40f0:8", ["const:b64eb8:8", "const:4:8"]]
+ 00b64eb8 ["CALLIND", null, ["register:0:8"]]
- 00b64e74 bytes 00013fd6
+ 00b64eb8 bytes 00013fd6
- 00b64e90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64e90 ["INT_ADD", "register:40f0:8", ["const:b64e90:8", "const:4:8"]]
- 00b64e90 ["CALLIND", null, ["register:0:8"]]
+ 00b64ed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64ed4 ["INT_ADD", "register:40f0:8", ["const:b64ed4:8", "const:4:8"]]
+ 00b64ed4 ["CALLIND", null, ["register:0:8"]]
- 00b64e90 bytes 00013fd6
+ 00b64ed4 bytes 00013fd6
- 00b64ea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64ea8 ["INT_ADD", "register:40f0:8", ["const:b64ea8:8", "const:4:8"]]
- 00b64ea8 ["CALLIND", null, ["register:0:8"]]
+ 00b64eec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64eec ["INT_ADD", "register:40f0:8", ["const:b64eec:8", "const:4:8"]]
+ 00b64eec ["CALLIND", null, ["register:0:8"]]
- 00b64ea8 bytes 00013fd6
+ 00b64eec bytes 00013fd6
~~~


<a id="compare-05bf3d277b5690201f4755a0b90c8eeb"></a>

### [`00b653fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b653fc.md) → [`00b65440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65440.md) _ZN8firebase4auth18AdditionalUserInfoaSEOS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d20.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md)
- 新版 呼出元 1件 [`00be0d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d70.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md) [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6543c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b653fc.md#insn-00b6543c) · [`00b6548c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b653fc.md#insn-00b6548c) · [`00b654bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b653fc.md#insn-00b654bc)
- 新版 `00b65480`（命令位置の公開資料なし） · `00b654d0`（命令位置の公開資料なし） · `00b65500`（命令位置の公開資料なし）

~~~diff
- 00b6543c ["INT_ADD", "register:40f0:8", ["const:b6543c:8", "const:4:8"]]
- 00b6543c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b65480 ["INT_ADD", "register:40f0:8", ["const:b65480:8", "const:4:8"]]
+ 00b65480 ["CALL", null, ["callee:00bdb060:8"]]
- 00b6543c bytes f5d60194
+ 00b65480 bytes f8d60194
- 00b6548c ["INT_ADD", "register:40f0:8", ["const:b6548c:8", "const:4:8"]]
- 00b6548c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b654d0 ["INT_ADD", "register:40f0:8", ["const:b654d0:8", "const:4:8"]]
+ 00b654d0 ["CALL", null, ["callee:00bdb060:8"]]
- 00b6548c bytes e1d60194
+ 00b654d0 bytes e4d60194
- 00b654bc ["INT_ADD", "register:40f0:8", ["const:b654bc:8", "const:4:8"]]
- 00b654bc ["CALL", null, ["callee:00bdef70:8"]]
+ 00b65500 ["INT_ADD", "register:40f0:8", ["const:b65500:8", "const:4:8"]]
+ 00b65500 ["CALL", null, ["callee:00bdef70:8"]]
- 00b654bc bytes 99e60194
+ 00b65500 bytes 9ce60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a253e14841876ef7c8280f171f5837"></a>

### [`00b69904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69904.md) → [`00b69948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69948.md) _ZN8firebase4auth10CredentialC1ERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b69928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69904.md#insn-00b69928)
- 新版 `00b6996c`（命令位置の公開資料なし）

~~~diff
- 00b69928 ["INT_ADD", "register:40f0:8", ["const:b69928:8", "const:4:8"]]
- 00b69928 ["CALL", null, ["callee:00be0d60:8"]]
+ 00b6996c ["INT_ADD", "register:40f0:8", ["const:b6996c:8", "const:4:8"]]
+ 00b6996c ["CALL", null, ["callee:00be0d60:8"]]
- 00b69928 bytes fadc0194
+ 00b6996c bytes fddc0194
~~~


<a id="compare-e3bbb684efed9cd9f304cfe8973e0885"></a>

### [`00b69da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69da8.md) → [`00b69dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69dec.md) _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0de0.md) · 呼出先 2件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md)
- 新版 呼出元 1件 [`00be0e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e30.md) · 呼出先 2件 [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b69dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69da8.md#insn-00b69dbc) · [`00b69de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69da8.md#insn-00b69de8)
- 新版 `00b69e00`（命令位置の公開資料なし） · `00b69e2c`（命令位置の公開資料なし）

~~~diff
- 00b69dbc ["INT_ADD", "register:40f0:8", ["const:b69dbc:8", "const:4:8"]]
- 00b69dbc ["CALL", null, ["callee:00be0d60:8"]]
+ 00b69e00 ["INT_ADD", "register:40f0:8", ["const:b69e00:8", "const:4:8"]]
+ 00b69e00 ["CALL", null, ["callee:00be0d60:8"]]
- 00b69dbc bytes d5db0194
+ 00b69e00 bytes d8db0194
- 00b69de8 ["INT_ADD", "register:40f0:8", ["const:b69de8:8", "const:4:8"]]
- 00b69de8 ["CALL", null, ["callee:00bde230:8"]]
+ 00b69e2c ["INT_ADD", "register:40f0:8", ["const:b69e2c:8", "const:4:8"]]
+ 00b69e2c ["CALL", null, ["callee:00bde230:8"]]
- 00b69de8 bytes fed00194
+ 00b69e2c bytes 01d10194
~~~


<a id="compare-d6545ea290b9ddb889ada85562d71e8f"></a>

### [`00b6abc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md) → [`00b6ac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ac0c.md) _ZN8firebase4auth22GameCenterAuthProvider23GetCredentialLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 8件 [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6abec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md#insn-00b6abec) · [`00b6abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md#insn-00b6abfc) · [`00b6ac08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md#insn-00b6ac08)
- 新版 `00b6ac30`（命令位置の公開資料なし） · `00b6ac40`（命令位置の公開資料なし） · `00b6ac4c`（命令位置の公開資料なし）

~~~diff
- 00b6abec ["INT_ADD", "register:40f0:8", ["const:b6abec:8", "const:4:8"]]
- 00b6abec ["CALL", null, ["callee:00be0b50:8"]]
+ 00b6ac30 ["INT_ADD", "register:40f0:8", ["const:b6ac30:8", "const:4:8"]]
+ 00b6ac30 ["CALL", null, ["callee:00be0b50:8"]]
- 00b6abec bytes c5d70194
+ 00b6ac30 bytes c8d70194
- 00b6abfc ["INT_ADD", "register:40f0:8", ["const:b6abfc:8", "const:4:8"]]
- 00b6abfc ["CALL", null, ["callee:00bddc20:8"]]
+ 00b6ac40 ["INT_ADD", "register:40f0:8", ["const:b6ac40:8", "const:4:8"]]
+ 00b6ac40 ["CALL", null, ["callee:00bddc20:8"]]
- 00b6abfc bytes f5cb0194
+ 00b6ac40 bytes f8cb0194
- 00b6ac08 ["INT_ADD", "register:40f0:8", ["const:b6ac08:8", "const:4:8"]]
- 00b6ac08 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b6ac4c ["INT_ADD", "register:40f0:8", ["const:b6ac4c:8", "const:4:8"]]
+ 00b6ac4c ["CALL", null, ["callee:00bddc30:8"]]
- 00b6ac08 bytes f6cb0194
+ 00b6ac4c bytes f9cb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89deb7a5a473f11377a72b76722db1fe"></a>

### [`00b6ad0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad0c.md) → [`00b6ad50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad50.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ad20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad0c.md#insn-00b6ad20)
- 新版 `00b6ad64`（命令位置の公開資料なし）

~~~diff
- 00b6ad20 ["INT_ADD", "register:40f0:8", ["const:b6ad20:8", "const:4:8"]]
- 00b6ad20 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b6ad64 ["INT_ADD", "register:40f0:8", ["const:b6ad64:8", "const:4:8"]]
+ 00b6ad64 ["CALL", null, ["callee:00bdb040:8"]]
- 00b6ad20 bytes b4c00194
+ 00b6ad64 bytes b7c00194
~~~


<a id="compare-c5adf7f5c643470982c1fdd43612e488"></a>

### [`00b6ada4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ada4.md) → [`00b6ade8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ade8.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2ERKS2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00be0df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0df0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00be0e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6adbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ada4.md#insn-00b6adbc)
- 新版 `00b6ae00`（命令位置の公開資料なし）

~~~diff
- 00b6adbc ["INT_ADD", "register:40f0:8", ["const:b6adbc:8", "const:4:8"]]
- 00b6adbc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b6ae00 ["INT_ADD", "register:40f0:8", ["const:b6ae00:8", "const:4:8"]]
+ 00b6ae00 ["CALL", null, ["callee:00bdb040:8"]]
- 00b6adbc bytes 8dc00194
+ 00b6ae00 bytes 90c00194
~~~


<a id="compare-f82c2894baba982f2da5731c7bb7c293"></a>

### [`00b6ae80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ae80.md) → [`00b6aec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aec4.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0df0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ae9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ae80.md#insn-00b6ae9c)
- 新版 `00b6aee0`（命令位置の公開資料なし）

~~~diff
- 00b6ae9c ["INT_ADD", "register:40f0:8", ["const:b6ae9c:8", "const:4:8"]]
- 00b6ae9c ["CALL", null, ["callee:00be0e40:8"]]
+ 00b6aee0 ["INT_ADD", "register:40f0:8", ["const:b6aee0:8", "const:4:8"]]
+ 00b6aee0 ["CALL", null, ["callee:00be0e40:8"]]
- 00b6ae9c bytes d5d70194
+ 00b6aee0 bytes d8d70194
~~~


<a id="compare-23eef0e523b2011a3993bd1f571ff072"></a>

### [`00b6b974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b974.md) → [`00b6b9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b9b8.md) _ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6b99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b974.md#insn-00b6b99c) · [`00b6b9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b974.md#insn-00b6b9b0) · [`00b6b9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b974.md#insn-00b6b9c0)
- 新版 `00b6b9e0`（命令位置の公開資料なし） · `00b6b9f4`（命令位置の公開資料なし） · `00b6ba04`（命令位置の公開資料なし）

~~~diff
- 00b6b99c ["INT_ADD", "register:40f0:8", ["const:b6b99c:8", "const:4:8"]]
- 00b6b99c ["CALL", null, ["callee:00bde0a0:8"]]
+ 00b6b9e0 ["INT_ADD", "register:40f0:8", ["const:b6b9e0:8", "const:4:8"]]
+ 00b6b9e0 ["CALL", null, ["callee:00bde0a0:8"]]
- 00b6b99c bytes adc90194
+ 00b6b9e0 bytes b0c90194
- 00b6b9b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6b9b0 ["INT_ADD", "register:40f0:8", ["const:b6b9b0:8", "const:4:8"]]
- 00b6b9b0 ["CALLIND", null, ["register:0:8"]]
+ 00b6b9f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6b9f4 ["INT_ADD", "register:40f0:8", ["const:b6b9f4:8", "const:4:8"]]
+ 00b6b9f4 ["CALLIND", null, ["register:0:8"]]
- 00b6b9b0 bytes 00013fd6
+ 00b6b9f4 bytes 00013fd6
- 00b6b9c0 ["INT_ADD", "register:40f0:8", ["const:b6b9c0:8", "const:4:8"]]
- 00b6b9c0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b6ba04 ["INT_ADD", "register:40f0:8", ["const:b6ba04:8", "const:4:8"]]
+ 00b6ba04 ["CALL", null, ["callee:00bdb060:8"]]
- 00b6b9c0 bytes 94bd0194
+ 00b6ba04 bytes 97bd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3c35ffcaf59eed72df119319e45f5bb"></a>

### [`00b6bb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bb84.md) → [`00b6bbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bbc8.md) _ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6bbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bb84.md#insn-00b6bbac) · [`00b6bbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bb84.md#insn-00b6bbc0) · [`00b6bbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bb84.md#insn-00b6bbd0)
- 新版 `00b6bbf0`（命令位置の公開資料なし） · `00b6bc04`（命令位置の公開資料なし） · `00b6bc14`（命令位置の公開資料なし）

~~~diff
- 00b6bbac ["INT_ADD", "register:40f0:8", ["const:b6bbac:8", "const:4:8"]]
- 00b6bbac ["CALL", null, ["callee:00bde510:8"]]
+ 00b6bbf0 ["INT_ADD", "register:40f0:8", ["const:b6bbf0:8", "const:4:8"]]
+ 00b6bbf0 ["CALL", null, ["callee:00bde510:8"]]
- 00b6bbac bytes 45ca0194
+ 00b6bbf0 bytes 48ca0194
- 00b6bbc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6bbc0 ["INT_ADD", "register:40f0:8", ["const:b6bbc0:8", "const:4:8"]]
- 00b6bbc0 ["CALLIND", null, ["register:0:8"]]
+ 00b6bc04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6bc04 ["INT_ADD", "register:40f0:8", ["const:b6bc04:8", "const:4:8"]]
+ 00b6bc04 ["CALLIND", null, ["register:0:8"]]
- 00b6bbc0 bytes 00013fd6
+ 00b6bc04 bytes 00013fd6
- 00b6bbd0 ["INT_ADD", "register:40f0:8", ["const:b6bbd0:8", "const:4:8"]]
- 00b6bbd0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b6bc14 ["INT_ADD", "register:40f0:8", ["const:b6bc14:8", "const:4:8"]]
+ 00b6bc14 ["CALL", null, ["callee:00bdb060:8"]]
- 00b6bbd0 bytes 10bd0194
+ 00b6bc14 bytes 13bd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde8920fc76d620988e85daaaae819f0"></a>

### [`00b6bebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bebc.md) → [`00b6bf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf00.md) _ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005188a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005188a4.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005188a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005188a4.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00be0090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6bef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bebc.md#insn-00b6bef4) · [`00b6bf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bebc.md#insn-00b6bf00)
- 新版 `00b6bf38`（命令位置の公開資料なし） · `00b6bf44`（命令位置の公開資料なし）

~~~diff
- 00b6bef4 ["INT_ADD", "register:40f0:8", ["const:b6bef4:8", "const:4:8"]]
- 00b6bef4 ["CALL", null, ["callee:00bde230:8"]]
+ 00b6bf38 ["INT_ADD", "register:40f0:8", ["const:b6bf38:8", "const:4:8"]]
+ 00b6bf38 ["CALL", null, ["callee:00bde230:8"]]
- 00b6bef4 bytes bbc80194
+ 00b6bf38 bytes bec80194
- 00b6bf00 ["INT_ADD", "register:40f0:8", ["const:b6bf00:8", "const:4:8"]]
- 00b6bf00 ["CALL", null, ["callee:00be0090:8"]]
+ 00b6bf44 ["INT_ADD", "register:40f0:8", ["const:b6bf44:8", "const:4:8"]]
+ 00b6bf44 ["CALL", null, ["callee:00be0090:8"]]
- 00b6bf00 bytes 50d00194
+ 00b6bf44 bytes 53d00194
~~~


<a id="compare-a1291028dde80de91509364c02f9c673"></a>

### [`00b6cabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cabc.md) → [`00b6cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb00.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b6aaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0db0.md)
- 新版 呼出元 1件 [`00b6aae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cabc.md#insn-00b6cad0)
- 新版 `00b6cb14`（命令位置の公開資料なし）

~~~diff
- 00b6cad0 ["INT_ADD", "register:40f0:8", ["const:b6cad0:8", "const:4:8"]]
- 00b6cad0 ["CALL", null, ["callee:00be0e00:8"]]
+ 00b6cb14 ["INT_ADD", "register:40f0:8", ["const:b6cb14:8", "const:4:8"]]
+ 00b6cb14 ["CALL", null, ["callee:00be0e00:8"]]
- 00b6cad0 bytes b8d00194
+ 00b6cb14 bytes bbd00194
~~~


<a id="compare-f53a9961f01437b049a668f848fcb2e9"></a>

### [`00b6cbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md) → [`00b6cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cc34.md) _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e00.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00be0e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e50.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md#insn-00b6cc10) · [`00b6cc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md#insn-00b6cc24) · [`00b6cc38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md#insn-00b6cc38)
- 新版 `00b6cc54`（命令位置の公開資料なし） · `00b6cc68`（命令位置の公開資料なし） · `00b6cc7c`（命令位置の公開資料なし）

~~~diff
- 00b6cc10 ["INT_ADD", "register:40f0:8", ["const:b6cc10:8", "const:4:8"]]
- 00b6cc10 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b6cc54 ["INT_ADD", "register:40f0:8", ["const:b6cc54:8", "const:4:8"]]
+ 00b6cc54 ["CALL", null, ["callee:00bdde10:8"]]
- 00b6cc10 bytes 6cc40194
+ 00b6cc54 bytes 6fc40194
- 00b6cc24 ["INT_ADD", "register:40f0:8", ["const:b6cc24:8", "const:4:8"]]
- 00b6cc24 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b6cc68 ["INT_ADD", "register:40f0:8", ["const:b6cc68:8", "const:4:8"]]
+ 00b6cc68 ["CALL", null, ["callee:00bddf80:8"]]
- 00b6cc24 bytes c3c40194
+ 00b6cc68 bytes c6c40194
- 00b6cc38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6cc38 ["INT_ADD", "register:40f0:8", ["const:b6cc38:8", "const:4:8"]]
- 00b6cc38 ["CALLIND", null, ["register:0:8"]]
+ 00b6cc7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6cc7c ["INT_ADD", "register:40f0:8", ["const:b6cc7c:8", "const:4:8"]]
+ 00b6cc7c ["CALLIND", null, ["register:0:8"]]
- 00b6cc38 bytes 00013fd6
+ 00b6cc7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef734baf7e278646e58d3ab09160db76"></a>

### [`00b6cc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md) → [`00b6ccd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6ccd4.md) _ZN8firebase4auth10AuthResultC2ERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0da0.md) · 呼出先 3件 [`00bddb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb80.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md) [`00be0dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0dd0.md)
- 新版 呼出元 1件 [`00be0df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0df0.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbd0.md) [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md) [`00be0e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md#insn-00b6cca8) · [`00b6cccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md#insn-00b6cccc) · [`00b6ccd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md#insn-00b6ccd8)
- 新版 `00b6ccec`（命令位置の公開資料なし） · `00b6cd10`（命令位置の公開資料なし） · `00b6cd1c`（命令位置の公開資料なし）

~~~diff
- 00b6cca8 ["INT_ADD", "register:40f0:8", ["const:b6cca8:8", "const:4:8"]]
- 00b6cca8 ["CALL", null, ["callee:00be0e20:8"]]
+ 00b6ccec ["INT_ADD", "register:40f0:8", ["const:b6ccec:8", "const:4:8"]]
+ 00b6ccec ["CALL", null, ["callee:00be0e20:8"]]
- 00b6cca8 bytes 4ad00194
+ 00b6ccec bytes 4dd00194
- 00b6cccc ["INT_ADD", "register:40f0:8", ["const:b6cccc:8", "const:4:8"]]
- 00b6cccc ["CALL", null, ["callee:00be0d60:8"]]
+ 00b6cd10 ["INT_ADD", "register:40f0:8", ["const:b6cd10:8", "const:4:8"]]
+ 00b6cd10 ["CALL", null, ["callee:00be0d60:8"]]
- 00b6cccc bytes 11d00194
+ 00b6cd10 bytes 14d00194
- 00b6ccd8 ["INT_ADD", "register:40f0:8", ["const:b6ccd8:8", "const:4:8"]]
- 00b6ccd8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b6cd1c ["INT_ADD", "register:40f0:8", ["const:b6cd1c:8", "const:4:8"]]
+ 00b6cd1c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b6ccd8 bytes aac30194
+ 00b6cd1c bytes adc30194
~~~


<a id="compare-4c996d5add98a6406e2442c9040820e9"></a>

### [`00b6cd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md) → [`00b6cda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cda4.md) _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0dd0.md) · 呼出先 3件 [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md) [`00be0e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e20.md)
- 新版 呼出元 1件 [`00be0e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e20.md) · 呼出先 3件 [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md) [`00be0e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md#insn-00b6cd80) · [`00b6cd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md#insn-00b6cd90) · [`00b6cdd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md#insn-00b6cdd8)
- 新版 `00b6cdc4`（命令位置の公開資料なし） · `00b6cdd4`（命令位置の公開資料なし） · `00b6ce1c`（命令位置の公開資料なし）

~~~diff
- 00b6cd80 ["INT_ADD", "register:40f0:8", ["const:b6cd80:8", "const:4:8"]]
- 00b6cd80 ["CALL", null, ["callee:00bde730:8"]]
+ 00b6cdc4 ["INT_ADD", "register:40f0:8", ["const:b6cdc4:8", "const:4:8"]]
+ 00b6cdc4 ["CALL", null, ["callee:00bde730:8"]]
- 00b6cd80 bytes 58c60194
+ 00b6cdc4 bytes 5bc60194
- 00b6cd90 ["INT_ADD", "register:40f0:8", ["const:b6cd90:8", "const:4:8"]]
- 00b6cd90 ["CALL", null, ["callee:00bde730:8"]]
+ 00b6cdd4 ["INT_ADD", "register:40f0:8", ["const:b6cdd4:8", "const:4:8"]]
+ 00b6cdd4 ["CALL", null, ["callee:00bde730:8"]]
- 00b6cd90 bytes 54c60194
+ 00b6cdd4 bytes 57c60194
- 00b6cdd8 ["INT_ADD", "register:40f0:8", ["const:b6cdd8:8", "const:4:8"]]
- 00b6cdd8 ["CALL", null, ["callee:00be0e70:8"]]
+ 00b6ce1c ["INT_ADD", "register:40f0:8", ["const:b6ce1c:8", "const:4:8"]]
+ 00b6ce1c ["CALL", null, ["callee:00be0e70:8"]]
- 00b6cdd8 bytes 12d00194
+ 00b6ce1c bytes 15d00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c429c9a29df6948e583d6a07b18d4676"></a>

### [`00b6ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6ced0.md) → [`00b6cf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cf14.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emp

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e20.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00be0e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e10.md)
- 新版 呼出元 1件 [`00be0e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e70.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00be0e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cf08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6ced0.md#insn-00b6cf08) · [`00b6cf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6ced0.md#insn-00b6cf1c) · [`00b6cf34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6ced0.md#insn-00b6cf34)
- 新版 `00b6cf4c`（命令位置の公開資料なし） · `00b6cf60`（命令位置の公開資料なし） · `00b6cf78`（命令位置の公開資料なし）

~~~diff
- 00b6cf08 ["INT_ADD", "register:40f0:8", ["const:b6cf08:8", "const:4:8"]]
- 00b6cf08 ["CALL", null, ["callee:00be0e60:8"]]
+ 00b6cf4c ["INT_ADD", "register:40f0:8", ["const:b6cf4c:8", "const:4:8"]]
+ 00b6cf4c ["CALL", null, ["callee:00be0e60:8"]]
- 00b6cf08 bytes c2cf0194
+ 00b6cf4c bytes c5cf0194
- 00b6cf1c ["INT_ADD", "register:40f0:8", ["const:b6cf1c:8", "const:4:8"]]
- 00b6cf1c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b6cf60 ["INT_ADD", "register:40f0:8", ["const:b6cf60:8", "const:4:8"]]
+ 00b6cf60 ["CALL", null, ["callee:00bdb040:8"]]
- 00b6cf1c bytes 35b80194
+ 00b6cf60 bytes 38b80194
- 00b6cf34 ["INT_ADD", "register:40f0:8", ["const:b6cf34:8", "const:4:8"]]
- 00b6cf34 ["CALL", null, ["callee:00bddaa0:8"]]
+ 00b6cf78 ["INT_ADD", "register:40f0:8", ["const:b6cf78:8", "const:4:8"]]
+ 00b6cf78 ["CALL", null, ["callee:00bddaa0:8"]]
- 00b6cf34 bytes c7c20194
+ 00b6cf78 bytes cac20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9fa1e900f9ccd250512f4e53d8084f3"></a>

### [`00b6cfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cfe4.md) → [`00b6d028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d028.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__fin

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e10.md) · 呼出先 1件 [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md)
- 新版 呼出元 1件 [`00be0e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e60.md) · 呼出先 1件 [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cfe4.md#insn-00b6d028) · [`00b6d060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cfe4.md#insn-00b6d060) · [`00b6d0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cfe4.md#insn-00b6d0a4)
- 新版 `00b6d06c`（命令位置の公開資料なし） · `00b6d0a4`（命令位置の公開資料なし） · `00b6d0e8`（命令位置の公開資料なし）

~~~diff
- 00b6d028 ["INT_ADD", "register:40f0:8", ["const:b6d028:8", "const:4:8"]]
- 00b6d028 ["CALL", null, ["callee:00bde720:8"]]
+ 00b6d06c ["INT_ADD", "register:40f0:8", ["const:b6d06c:8", "const:4:8"]]
+ 00b6d06c ["CALL", null, ["callee:00bde720:8"]]
- 00b6d028 bytes aac50194
+ 00b6d06c bytes adc50194
- 00b6d060 ["INT_ADD", "register:40f0:8", ["const:b6d060:8", "const:4:8"]]
- 00b6d060 ["CALL", null, ["callee:00bde720:8"]]
+ 00b6d0a4 ["INT_ADD", "register:40f0:8", ["const:b6d0a4:8", "const:4:8"]]
+ 00b6d0a4 ["CALL", null, ["callee:00bde720:8"]]
- 00b6d060 bytes 9cc50194
+ 00b6d0a4 bytes 9fc50194
- 00b6d0a4 ["INT_ADD", "register:40f0:8", ["const:b6d0a4:8", "const:4:8"]]
- 00b6d0a4 ["CALL", null, ["callee:00bde720:8"]]
+ 00b6d0e8 ["INT_ADD", "register:40f0:8", ["const:b6d0e8:8", "const:4:8"]]
+ 00b6d0e8 ["CALL", null, ["callee:00bde720:8"]]
- 00b6d0a4 bytes 8bc50194
+ 00b6d0e8 bytes 8ec50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdfe4c156d1f7e3430e03a1fce11520b"></a>

### [`00b6d210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d210.md) → [`00b6d254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md) _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b6bf28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bf28.md) [`00b6c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c50c.md) [`00b6c7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c7e4.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cd0.md)
- 新版 呼出元 3件 [`00b6bf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md) [`00b6c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md) [`00b6c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d210.md#insn-00b6d248) · [`00b6d268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d210.md#insn-00b6d268) · [`00b6d290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d210.md#insn-00b6d290)
- 新版 `00b6d28c`（命令位置の公開資料なし） · `00b6d2ac`（命令位置の公開資料なし） · `00b6d2d4`（命令位置の公開資料なし）

~~~diff
- 00b6d248 ["INT_ADD", "register:40f0:8", ["const:b6d248:8", "const:4:8"]]
- 00b6d248 ["CALL", null, ["callee:00be0d20:8"]]
+ 00b6d28c ["INT_ADD", "register:40f0:8", ["const:b6d28c:8", "const:4:8"]]
+ 00b6d28c ["CALL", null, ["callee:00be0d20:8"]]
- 00b6d248 bytes a2ce0194
+ 00b6d28c bytes a5ce0194
- 00b6d268 ["INT_ADD", "register:40f0:8", ["const:b6d268:8", "const:4:8"]]
- 00b6d268 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b6d2ac ["INT_ADD", "register:40f0:8", ["const:b6d2ac:8", "const:4:8"]]
+ 00b6d2ac ["CALL", null, ["callee:00bddf80:8"]]
- 00b6d268 bytes 32c30194
+ 00b6d2ac bytes 35c30194
- 00b6d290 ["INT_ADD", "register:40f0:8", ["const:b6d290:8", "const:4:8"]]
- 00b6d290 ["CALL", null, ["callee:00be0dc0:8"]]
+ 00b6d2d4 ["INT_ADD", "register:40f0:8", ["const:b6d2d4:8", "const:4:8"]]
+ 00b6d2d4 ["CALL", null, ["callee:00be0dc0:8"]]
- 00b6d290 bytes b8ce0194
+ 00b6d2d4 bytes bbce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-884b92e8c24b21f611b8bae3d0db9a82"></a>

### [`00b6d454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d454.md) → [`00b6d498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d498.md) _ZN8firebase4auth19PhoneAuthCredentialC1ERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d454.md#insn-00b6d478)
- 新版 `00b6d4bc`（命令位置の公開資料なし）

~~~diff
- 00b6d478 ["INT_ADD", "register:40f0:8", ["const:b6d478:8", "const:4:8"]]
- 00b6d478 ["CALL", null, ["callee:00be0e30:8"]]
+ 00b6d4bc ["INT_ADD", "register:40f0:8", ["const:b6d4bc:8", "const:4:8"]]
+ 00b6d4bc ["CALL", null, ["callee:00be0e30:8"]]
- 00b6d478 bytes 5ace0194
+ 00b6d4bc bytes 5dce0194
~~~


<a id="compare-205b13fe0bca184e4de9b1239f1e1771"></a>

### [`00b6f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f10c.md) → [`00b6f150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f150.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEbP7_JNIEnvPNS_26Refere

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e60.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cc0.md)
- 新版 呼出元 1件 [`00be0eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0eb0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6f140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f10c.md#insn-00b6f140) · [`00b6f154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f10c.md#insn-00b6f154) · [`00b6f180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f10c.md#insn-00b6f180)
- 新版 `00b6f184`（命令位置の公開資料なし） · `00b6f198`（命令位置の公開資料なし） · `00b6f1c4`（命令位置の公開資料なし）

~~~diff
- 00b6f140 ["INT_ADD", "register:40f0:8", ["const:b6f140:8", "const:4:8"]]
- 00b6f140 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b6f184 ["INT_ADD", "register:40f0:8", ["const:b6f184:8", "const:4:8"]]
+ 00b6f184 ["CALL", null, ["callee:00be0d10:8"]]
- 00b6f140 bytes e0c60194
+ 00b6f184 bytes e3c60194
- 00b6f154 ["INT_ADD", "register:40f0:8", ["const:b6f154:8", "const:4:8"]]
- 00b6f154 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b6f198 ["INT_ADD", "register:40f0:8", ["const:b6f198:8", "const:4:8"]]
+ 00b6f198 ["CALL", null, ["callee:00bddf80:8"]]
- 00b6f154 bytes 77bb0194
+ 00b6f198 bytes 7abb0194
- 00b6f180 ["INT_ADD", "register:40f0:8", ["const:b6f180:8", "const:4:8"]]
- 00b6f180 ["CALL", null, ["callee:00be0e90:8"]]
+ 00b6f1c4 ["INT_ADD", "register:40f0:8", ["const:b6f1c4:8", "const:4:8"]]
+ 00b6f1c4 ["CALL", null, ["callee:00be0e90:8"]]
- 00b6f180 bytes 30c70194
+ 00b6f1c4 bytes 33c70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77b732afd8fcc9436bef30456fab1a5"></a>

### [`00b71a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md) → [`00b71a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71a8c.md) _ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureR

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b6eeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eeac.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cd0.md)
- 新版 呼出元 1件 [`00b6eef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eef0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md#insn-00b71a80) · [`00b71a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md#insn-00b71a98) · [`00b71ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md#insn-00b71ac0)
- 新版 `00b71ac4`（命令位置の公開資料なし） · `00b71adc`（命令位置の公開資料なし） · `00b71b04`（命令位置の公開資料なし）

~~~diff
- 00b71a80 ["INT_ADD", "register:40f0:8", ["const:b71a80:8", "const:4:8"]]
- 00b71a80 ["CALL", null, ["callee:00be0d20:8"]]
+ 00b71ac4 ["INT_ADD", "register:40f0:8", ["const:b71ac4:8", "const:4:8"]]
+ 00b71ac4 ["CALL", null, ["callee:00be0d20:8"]]
- 00b71a80 bytes 94bc0194
+ 00b71ac4 bytes 97bc0194
- 00b71a98 ["INT_ADD", "register:40f0:8", ["const:b71a98:8", "const:4:8"]]
- 00b71a98 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b71adc ["INT_ADD", "register:40f0:8", ["const:b71adc:8", "const:4:8"]]
+ 00b71adc ["CALL", null, ["callee:00bddf80:8"]]
- 00b71a98 bytes 26b10194
+ 00b71adc bytes 29b10194
- 00b71ac0 ["INT_ADD", "register:40f0:8", ["const:b71ac0:8", "const:4:8"]]
- 00b71ac0 ["CALL", null, ["callee:00be0e80:8"]]
+ 00b71b04 ["INT_ADD", "register:40f0:8", ["const:b71b04:8", "const:4:8"]]
+ 00b71b04 ["CALL", null, ["callee:00be0e80:8"]]
- 00b71ac0 bytes dcbc0194
+ 00b71b04 bytes dfbc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d8dc1d5d6121f8f83f8cf879421eb5c"></a>

### [`00b71dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71dbc.md) → [`00b71e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71e00.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e70.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) [`00be0e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e50.md)
- 新版 呼出元 1件 [`00be0ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ec0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md) [`00be0ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71dbc.md#insn-00b71e58) · [`00b71e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71dbc.md#insn-00b71e70) · [`00b71e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71dbc.md#insn-00b71e90)
- 新版 `00b71e9c`（命令位置の公開資料なし） · `00b71eb4`（命令位置の公開資料なし） · `00b71ed4`（命令位置の公開資料なし）

~~~diff
- 00b71e58 ["INT_ADD", "register:40f0:8", ["const:b71e58:8", "const:4:8"]]
- 00b71e58 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b71e9c ["INT_ADD", "register:40f0:8", ["const:b71e9c:8", "const:4:8"]]
+ 00b71e9c ["CALL", null, ["callee:00bdb040:8"]]
- 00b71e58 bytes 66a40194
+ 00b71e9c bytes 69a40194
- 00b71e70 ["INT_ADD", "register:40f0:8", ["const:b71e70:8", "const:4:8"]]
- 00b71e70 ["CALL", null, ["callee:00be0ea0:8"]]
+ 00b71eb4 ["INT_ADD", "register:40f0:8", ["const:b71eb4:8", "const:4:8"]]
+ 00b71eb4 ["CALL", null, ["callee:00be0ea0:8"]]
- 00b71e70 bytes f8bb0194
+ 00b71eb4 bytes fbbb0194
- 00b71e90 ["INT_ADD", "register:40f0:8", ["const:b71e90:8", "const:4:8"]]
- 00b71e90 ["CALL", null, ["callee:00be0ea0:8"]]
+ 00b71ed4 ["INT_ADD", "register:40f0:8", ["const:b71ed4:8", "const:4:8"]]
+ 00b71ed4 ["CALL", null, ["callee:00be0ea0:8"]]
- 00b71e90 bytes f0bb0194
+ 00b71ed4 bytes f3bb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9d3e297d5cd57ccea9a48ebb404bd07"></a>

### [`00b71f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md) → [`00b71fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71fb0.md) _ZNK8firebase4auth4User18GetTokenLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md#insn-00b71f8c) · [`00b71f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md#insn-00b71f98) · [`00b71fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md#insn-00b71fa4)
- 新版 `00b71fd0`（命令位置の公開資料なし） · `00b71fdc`（命令位置の公開資料なし） · `00b71fe8`（命令位置の公開資料なし）

~~~diff
- 00b71f8c ["INT_ADD", "register:40f0:8", ["const:b71f8c:8", "const:4:8"]]
- 00b71f8c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b71fd0 ["INT_ADD", "register:40f0:8", ["const:b71fd0:8", "const:4:8"]]
+ 00b71fd0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b71f8c bytes 11af0194
+ 00b71fd0 bytes 14af0194
- 00b71f98 ["INT_ADD", "register:40f0:8", ["const:b71f98:8", "const:4:8"]]
- 00b71f98 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b71fdc ["INT_ADD", "register:40f0:8", ["const:b71fdc:8", "const:4:8"]]
+ 00b71fdc ["CALL", null, ["callee:00bddc30:8"]]
- 00b71f98 bytes 12af0194
+ 00b71fdc bytes 15af0194
- 00b71fa4 ["INT_ADD", "register:40f0:8", ["const:b71fa4:8", "const:4:8"]]
- 00b71fa4 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b71fe8 ["INT_ADD", "register:40f0:8", ["const:b71fe8:8", "const:4:8"]]
+ 00b71fe8 ["CALL", null, ["callee:00bdde10:8"]]
- 00b71fa4 bytes 87af0194
+ 00b71fe8 bytes 8aaf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f1a2d78890d31892ad48402a9b44513"></a>

### [`00b71ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md) → [`00b72040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72040.md) _ZNK8firebase4auth4User24UpdatePasswordLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7201c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md#insn-00b7201c) · [`00b72028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md#insn-00b72028) · [`00b72034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md#insn-00b72034)
- 新版 `00b72060`（命令位置の公開資料なし） · `00b7206c`（命令位置の公開資料なし） · `00b72078`（命令位置の公開資料なし）

~~~diff
- 00b7201c ["INT_ADD", "register:40f0:8", ["const:b7201c:8", "const:4:8"]]
- 00b7201c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b72060 ["INT_ADD", "register:40f0:8", ["const:b72060:8", "const:4:8"]]
+ 00b72060 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7201c bytes edae0194
+ 00b72060 bytes f0ae0194
- 00b72028 ["INT_ADD", "register:40f0:8", ["const:b72028:8", "const:4:8"]]
- 00b72028 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b7206c ["INT_ADD", "register:40f0:8", ["const:b7206c:8", "const:4:8"]]
+ 00b7206c ["CALL", null, ["callee:00bddc30:8"]]
- 00b72028 bytes eeae0194
+ 00b7206c bytes f1ae0194
- 00b72034 ["INT_ADD", "register:40f0:8", ["const:b72034:8", "const:4:8"]]
- 00b72034 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72078 ["INT_ADD", "register:40f0:8", ["const:b72078:8", "const:4:8"]]
+ 00b72078 ["CALL", null, ["callee:00bdde10:8"]]
- 00b72034 bytes 63af0194
+ 00b72078 bytes 66af0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b06127abe9e391a9bf53634bc6a9cef"></a>

### [`00b7208c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7208c.md) → [`00b720d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b720d0.md) _ZNK8firebase4auth4User28LinkWithCredentialLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b720ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7208c.md#insn-00b720ac) · [`00b720b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7208c.md#insn-00b720b8) · [`00b720c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7208c.md#insn-00b720c4)
- 新版 `00b720f0`（命令位置の公開資料なし） · `00b720fc`（命令位置の公開資料なし） · `00b72108`（命令位置の公開資料なし）

~~~diff
- 00b720ac ["INT_ADD", "register:40f0:8", ["const:b720ac:8", "const:4:8"]]
- 00b720ac ["CALL", null, ["callee:00bddc20:8"]]
+ 00b720f0 ["INT_ADD", "register:40f0:8", ["const:b720f0:8", "const:4:8"]]
+ 00b720f0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b720ac bytes c9ae0194
+ 00b720f0 bytes ccae0194
- 00b720b8 ["INT_ADD", "register:40f0:8", ["const:b720b8:8", "const:4:8"]]
- 00b720b8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b720fc ["INT_ADD", "register:40f0:8", ["const:b720fc:8", "const:4:8"]]
+ 00b720fc ["CALL", null, ["callee:00bddc30:8"]]
- 00b720b8 bytes caae0194
+ 00b720fc bytes cdae0194
- 00b720c4 ["INT_ADD", "register:40f0:8", ["const:b720c4:8", "const:4:8"]]
- 00b720c4 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72108 ["INT_ADD", "register:40f0:8", ["const:b72108:8", "const:4:8"]]
+ 00b72108 ["CALL", null, ["callee:00bdde10:8"]]
- 00b720c4 bytes 3faf0194
+ 00b72108 bytes 42af0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e22827e67a670f4192ecce8aceba1b6"></a>

### [`00b7211c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md) → [`00b72160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72160.md) _ZNK8firebase4auth4User24ReauthenticateLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md#insn-00b7213c) · [`00b72148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md#insn-00b72148) · [`00b72154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md#insn-00b72154)
- 新版 `00b72180`（命令位置の公開資料なし） · `00b7218c`（命令位置の公開資料なし） · `00b72198`（命令位置の公開資料なし）

~~~diff
- 00b7213c ["INT_ADD", "register:40f0:8", ["const:b7213c:8", "const:4:8"]]
- 00b7213c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b72180 ["INT_ADD", "register:40f0:8", ["const:b72180:8", "const:4:8"]]
+ 00b72180 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7213c bytes a5ae0194
+ 00b72180 bytes a8ae0194
- 00b72148 ["INT_ADD", "register:40f0:8", ["const:b72148:8", "const:4:8"]]
- 00b72148 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b7218c ["INT_ADD", "register:40f0:8", ["const:b7218c:8", "const:4:8"]]
+ 00b7218c ["CALL", null, ["callee:00bddc30:8"]]
- 00b72148 bytes a6ae0194
+ 00b7218c bytes a9ae0194
- 00b72154 ["INT_ADD", "register:40f0:8", ["const:b72154:8", "const:4:8"]]
- 00b72154 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72198 ["INT_ADD", "register:40f0:8", ["const:b72198:8", "const:4:8"]]
+ 00b72198 ["CALL", null, ["callee:00bdde10:8"]]
- 00b72154 bytes 1baf0194
+ 00b72198 bytes 1eaf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-651c1f40503f09918dbd8d664885f1d7"></a>

### [`00b721ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b721ac.md) → [`00b721f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b721f0.md) _ZNK8firebase4auth4User39ReauthenticateAndRetrieveDataLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b721cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b721ac.md#insn-00b721cc) · [`00b721d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b721ac.md#insn-00b721d8) · [`00b721e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b721ac.md#insn-00b721e4)
- 新版 `00b72210`（命令位置の公開資料なし） · `00b7221c`（命令位置の公開資料なし） · `00b72228`（命令位置の公開資料なし）

~~~diff
- 00b721cc ["INT_ADD", "register:40f0:8", ["const:b721cc:8", "const:4:8"]]
- 00b721cc ["CALL", null, ["callee:00bddc20:8"]]
+ 00b72210 ["INT_ADD", "register:40f0:8", ["const:b72210:8", "const:4:8"]]
+ 00b72210 ["CALL", null, ["callee:00bddc20:8"]]
- 00b721cc bytes 81ae0194
+ 00b72210 bytes 84ae0194
- 00b721d8 ["INT_ADD", "register:40f0:8", ["const:b721d8:8", "const:4:8"]]
- 00b721d8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b7221c ["INT_ADD", "register:40f0:8", ["const:b7221c:8", "const:4:8"]]
+ 00b7221c ["CALL", null, ["callee:00bddc30:8"]]
- 00b721d8 bytes 82ae0194
+ 00b7221c bytes 85ae0194
- 00b721e4 ["INT_ADD", "register:40f0:8", ["const:b721e4:8", "const:4:8"]]
- 00b721e4 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72228 ["INT_ADD", "register:40f0:8", ["const:b72228:8", "const:4:8"]]
+ 00b72228 ["CALL", null, ["callee:00bdde10:8"]]
- 00b721e4 bytes f7ae0194
+ 00b72228 bytes faae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0092a69055b40f8bbcb462894ac7b679"></a>

### [`00b7223c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7223c.md) → [`00b72280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72280.md) _ZNK8firebase4auth4User31SendEmailVerificationLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7225c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7223c.md#insn-00b7225c) · [`00b72268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7223c.md#insn-00b72268) · [`00b72274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7223c.md#insn-00b72274)
- 新版 `00b722a0`（命令位置の公開資料なし） · `00b722ac`（命令位置の公開資料なし） · `00b722b8`（命令位置の公開資料なし）

~~~diff
- 00b7225c ["INT_ADD", "register:40f0:8", ["const:b7225c:8", "const:4:8"]]
- 00b7225c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b722a0 ["INT_ADD", "register:40f0:8", ["const:b722a0:8", "const:4:8"]]
+ 00b722a0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7225c bytes 5dae0194
+ 00b722a0 bytes 60ae0194
- 00b72268 ["INT_ADD", "register:40f0:8", ["const:b72268:8", "const:4:8"]]
- 00b72268 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b722ac ["INT_ADD", "register:40f0:8", ["const:b722ac:8", "const:4:8"]]
+ 00b722ac ["CALL", null, ["callee:00bddc30:8"]]
- 00b72268 bytes 5eae0194
+ 00b722ac bytes 61ae0194
- 00b72274 ["INT_ADD", "register:40f0:8", ["const:b72274:8", "const:4:8"]]
- 00b72274 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b722b8 ["INT_ADD", "register:40f0:8", ["const:b722b8:8", "const:4:8"]]
+ 00b722b8 ["CALL", null, ["callee:00bdde10:8"]]
- 00b72274 bytes d3ae0194
+ 00b722b8 bytes d6ae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-188ff8e3839e3136c17158a63488dbbb"></a>

### [`00b722cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md) → [`00b72310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72310.md) _ZNK8firebase4auth4User50SendEmailVerificationBeforeUpdatingEmailLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b722ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md#insn-00b722ec) · [`00b722f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md#insn-00b722f8) · [`00b72304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md#insn-00b72304)
- 新版 `00b72330`（命令位置の公開資料なし） · `00b7233c`（命令位置の公開資料なし） · `00b72348`（命令位置の公開資料なし）

~~~diff
- 00b722ec ["INT_ADD", "register:40f0:8", ["const:b722ec:8", "const:4:8"]]
- 00b722ec ["CALL", null, ["callee:00bddc20:8"]]
+ 00b72330 ["INT_ADD", "register:40f0:8", ["const:b72330:8", "const:4:8"]]
+ 00b72330 ["CALL", null, ["callee:00bddc20:8"]]
- 00b722ec bytes 39ae0194
+ 00b72330 bytes 3cae0194
- 00b722f8 ["INT_ADD", "register:40f0:8", ["const:b722f8:8", "const:4:8"]]
- 00b722f8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b7233c ["INT_ADD", "register:40f0:8", ["const:b7233c:8", "const:4:8"]]
+ 00b7233c ["CALL", null, ["callee:00bddc30:8"]]
- 00b722f8 bytes 3aae0194
+ 00b7233c bytes 3dae0194
- 00b72304 ["INT_ADD", "register:40f0:8", ["const:b72304:8", "const:4:8"]]
- 00b72304 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72348 ["INT_ADD", "register:40f0:8", ["const:b72348:8", "const:4:8"]]
+ 00b72348 ["CALL", null, ["callee:00bdde10:8"]]
- 00b72304 bytes afae0194
+ 00b72348 bytes b2ae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a53b6cb999d2fc5c9cb433048a395355"></a>

### [`00b7235c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md) → [`00b723a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b723a0.md) _ZNK8firebase4auth4User16UnlinkLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7237c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md#insn-00b7237c) · [`00b72388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md#insn-00b72388) · [`00b72394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md#insn-00b72394)
- 新版 `00b723c0`（命令位置の公開資料なし） · `00b723cc`（命令位置の公開資料なし） · `00b723d8`（命令位置の公開資料なし）

~~~diff
- 00b7237c ["INT_ADD", "register:40f0:8", ["const:b7237c:8", "const:4:8"]]
- 00b7237c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b723c0 ["INT_ADD", "register:40f0:8", ["const:b723c0:8", "const:4:8"]]
+ 00b723c0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7237c bytes 15ae0194
+ 00b723c0 bytes 18ae0194
- 00b72388 ["INT_ADD", "register:40f0:8", ["const:b72388:8", "const:4:8"]]
- 00b72388 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b723cc ["INT_ADD", "register:40f0:8", ["const:b723cc:8", "const:4:8"]]
+ 00b723cc ["CALL", null, ["callee:00bddc30:8"]]
- 00b72388 bytes 16ae0194
+ 00b723cc bytes 19ae0194
- 00b72394 ["INT_ADD", "register:40f0:8", ["const:b72394:8", "const:4:8"]]
- 00b72394 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b723d8 ["INT_ADD", "register:40f0:8", ["const:b723d8:8", "const:4:8"]]
+ 00b723d8 ["CALL", null, ["callee:00bdde10:8"]]
- 00b72394 bytes 8bae0194
+ 00b723d8 bytes 8eae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfcc865da5f9201d66699e42b39e16a2"></a>

### [`00b723ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b723ec.md) → [`00b72430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72430.md) _ZNK8firebase4auth4User27UpdateUserProfileLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7240c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b723ec.md#insn-00b7240c) · [`00b72418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b723ec.md#insn-00b72418) · [`00b72424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b723ec.md#insn-00b72424)
- 新版 `00b72450`（命令位置の公開資料なし） · `00b7245c`（命令位置の公開資料なし） · `00b72468`（命令位置の公開資料なし）

~~~diff
- 00b7240c ["INT_ADD", "register:40f0:8", ["const:b7240c:8", "const:4:8"]]
- 00b7240c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b72450 ["INT_ADD", "register:40f0:8", ["const:b72450:8", "const:4:8"]]
+ 00b72450 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7240c bytes f1ad0194
+ 00b72450 bytes f4ad0194
- 00b72418 ["INT_ADD", "register:40f0:8", ["const:b72418:8", "const:4:8"]]
- 00b72418 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b7245c ["INT_ADD", "register:40f0:8", ["const:b7245c:8", "const:4:8"]]
+ 00b7245c ["CALL", null, ["callee:00bddc30:8"]]
- 00b72418 bytes f2ad0194
+ 00b7245c bytes f5ad0194
- 00b72424 ["INT_ADD", "register:40f0:8", ["const:b72424:8", "const:4:8"]]
- 00b72424 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72468 ["INT_ADD", "register:40f0:8", ["const:b72468:8", "const:4:8"]]
+ 00b72468 ["CALL", null, ["callee:00bdde10:8"]]
- 00b72424 bytes 67ae0194
+ 00b72468 bytes 6aae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3adffb77e7c8d1908202a48db2165d"></a>

### [`00b7247c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7247c.md) → [`00b724c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b724c0.md) _ZNK8firebase4auth4User16ReloadLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7249c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7247c.md#insn-00b7249c) · [`00b724a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7247c.md#insn-00b724a8) · [`00b724b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7247c.md#insn-00b724b4)
- 新版 `00b724e0`（命令位置の公開資料なし） · `00b724ec`（命令位置の公開資料なし） · `00b724f8`（命令位置の公開資料なし）

~~~diff
- 00b7249c ["INT_ADD", "register:40f0:8", ["const:b7249c:8", "const:4:8"]]
- 00b7249c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b724e0 ["INT_ADD", "register:40f0:8", ["const:b724e0:8", "const:4:8"]]
+ 00b724e0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7249c bytes cdad0194
+ 00b724e0 bytes d0ad0194
- 00b724a8 ["INT_ADD", "register:40f0:8", ["const:b724a8:8", "const:4:8"]]
- 00b724a8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b724ec ["INT_ADD", "register:40f0:8", ["const:b724ec:8", "const:4:8"]]
+ 00b724ec ["CALL", null, ["callee:00bddc30:8"]]
- 00b724a8 bytes cead0194
+ 00b724ec bytes d1ad0194
- 00b724b4 ["INT_ADD", "register:40f0:8", ["const:b724b4:8", "const:4:8"]]
- 00b724b4 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b724f8 ["INT_ADD", "register:40f0:8", ["const:b724f8:8", "const:4:8"]]
+ 00b724f8 ["CALL", null, ["callee:00bdde10:8"]]
- 00b724b4 bytes 43ae0194
+ 00b724f8 bytes 46ae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

