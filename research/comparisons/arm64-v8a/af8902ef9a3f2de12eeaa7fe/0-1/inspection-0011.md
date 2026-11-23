# v15.7.3 → v15.7.4 · 要調査の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-acef5a6fb6e90cfaa8e59aad1847db64"></a>

### [`00b3cf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cf90.md) → [`00b3cfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cfd4.md) FUN_00b3cfd4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b3c41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c41c.md) [`00b3d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d3a4.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be0100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0100.md)
- 新版 呼出元 2件 [`00b3c460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3c460.md) [`00b3d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d3e8.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3cfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cf90.md#insn-00b3cfcc) · [`00b3d030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cf90.md#insn-00b3d030) · [`00b3d0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cf90.md#insn-00b3d0b0)
- 新版 [`00b3d010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cfd4.md#insn-00b3d010) · [`00b3d074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cfd4.md#insn-00b3d074) · [`00b3d0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cfd4.md#insn-00b3d0f4)

~~~diff
- 00b3cfcc ["INT_ADD", "register:40f0:8", ["const:b3cfcc:8", "const:4:8"]]
- 00b3cfcc ["CALL", null, ["callee:00be0150:8"]]
+ 00b3d010 ["INT_ADD", "register:40f0:8", ["const:b3d010:8", "const:4:8"]]
+ 00b3d010 ["CALL", null, ["callee:00be0150:8"]]
- 00b3cfcc bytes 4d8c0294
+ 00b3d010 bytes 508c0294
- 00b3d030 ["INT_ADD", "register:40f0:8", ["const:b3d030:8", "const:4:8"]]
- 00b3d030 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3d074 ["INT_ADD", "register:40f0:8", ["const:b3d074:8", "const:4:8"]]
+ 00b3d074 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3d030 bytes 60780294
+ 00b3d074 bytes 63780294
- 00b3d0b0 ["INT_ADD", "register:40f0:8", ["const:b3d0b0:8", "const:4:8"]]
- 00b3d0b0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3d0f4 ["INT_ADD", "register:40f0:8", ["const:b3d0f4:8", "const:4:8"]]
+ 00b3d0f4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3d0b0 bytes 40780294
+ 00b3d0f4 bytes 43780294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92a863b0c54b6fc4eed8e63f13d62fc6"></a>

### [`00b3d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md) → [`00b3d24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d24c.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfce0.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md)
- 新版 呼出元 1件 [`00bdfd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd30.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be00f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3d244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md#insn-00b3d244) · [`00b3d2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md#insn-00b3d2e0) · [`00b3d35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md#insn-00b3d35c)
- 新版 [`00b3d288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d24c.md#insn-00b3d288) · [`00b3d324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d24c.md#insn-00b3d324) · [`00b3d3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d24c.md#insn-00b3d3a0)

~~~diff
- 00b3d244 ["INT_ADD", "register:40f0:8", ["const:b3d244:8", "const:4:8"]]
- 00b3d244 ["CALL", null, ["callee:00be00f0:8"]]
+ 00b3d288 ["INT_ADD", "register:40f0:8", ["const:b3d288:8", "const:4:8"]]
+ 00b3d288 ["CALL", null, ["callee:00be00f0:8"]]
- 00b3d244 bytes 978b0294
+ 00b3d288 bytes 9a8b0294
- 00b3d2e0 ["INT_ADD", "register:40f0:8", ["const:b3d2e0:8", "const:4:8"]]
- 00b3d2e0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3d324 ["INT_ADD", "register:40f0:8", ["const:b3d324:8", "const:4:8"]]
+ 00b3d324 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3d2e0 bytes b4770294
+ 00b3d324 bytes b7770294
- 00b3d35c ["INT_ADD", "register:40f0:8", ["const:b3d35c:8", "const:4:8"]]
- 00b3d35c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3d3a0 ["INT_ADD", "register:40f0:8", ["const:b3d3a0:8", "const:4:8"]]
+ 00b3d3a0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3d35c bytes 95770294
+ 00b3d3a0 bytes 98770294
~~~


<a id="compare-f6a3d9c83fba193328ea1ef068865dfa"></a>

### [`00b3d674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d674.md) → [`00b3d6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d6b8.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection4EnumEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf380.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3d0.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d674.md#insn-00b3d6d0)
- 新版 [`00b3d714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d6b8.md#insn-00b3d714)

~~~diff
- 00b3d6d0 ["INT_ADD", "register:40f0:8", ["const:b3d6d0:8", "const:4:8"]]
- 00b3d6d0 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3d714 ["INT_ADD", "register:40f0:8", ["const:b3d714:8", "const:4:8"]]
+ 00b3d714 ["CALL", null, ["callee:00bdf390:8"]]
- 00b3d6d0 bytes 1c870294
+ 00b3d714 bytes 1f870294
~~~


<a id="compare-86d5c3a13817ea1435dc26f527c0177e"></a>

### [`00b3de88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3de88.md) → [`00b3decc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3decc.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be00d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00d0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0120.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3df10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3de88.md#insn-00b3df10) · [`00b3df60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3de88.md#insn-00b3df60) · [`00b3dff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3de88.md#insn-00b3dff4)
- 新版 [`00b3df54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3decc.md#insn-00b3df54) · [`00b3dfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3decc.md#insn-00b3dfa4) · [`00b3e038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3decc.md#insn-00b3e038)

~~~diff
- 00b3df10 ["INT_ADD", "register:40f0:8", ["const:b3df10:8", "const:4:8"]]
- 00b3df10 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3df54 ["INT_ADD", "register:40f0:8", ["const:b3df54:8", "const:4:8"]]
+ 00b3df54 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3df10 bytes a8740294
+ 00b3df54 bytes ab740294
- 00b3df60 ["INT_ADD", "register:40f0:8", ["const:b3df60:8", "const:4:8"]]
- 00b3df60 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3dfa4 ["INT_ADD", "register:40f0:8", ["const:b3dfa4:8", "const:4:8"]]
+ 00b3dfa4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3df60 bytes 94740294
+ 00b3dfa4 bytes 97740294
- 00b3dff4 ["INT_ADD", "register:40f0:8", ["const:b3dff4:8", "const:4:8"]]
- 00b3dff4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3e038 ["INT_ADD", "register:40f0:8", ["const:b3e038:8", "const:4:8"]]
+ 00b3e038 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3dff4 bytes 6f740294
+ 00b3e038 bytes 72740294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-076db313e111b3662cb2fab0ad96eb8d"></a>

### [`00b3e0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e0d4.md) → [`00b3e118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e118.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0130.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00d0.md)
- 新版 呼出元 1件 [`00be0180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0180.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3e108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e0d4.md#insn-00b3e108) · [`00b3e16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e0d4.md#insn-00b3e16c) · [`00b3e1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e0d4.md#insn-00b3e1e4)
- 新版 [`00b3e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e118.md#insn-00b3e14c) · [`00b3e1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e118.md#insn-00b3e1b0) · [`00b3e228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e118.md#insn-00b3e228)

~~~diff
- 00b3e108 ["INT_ADD", "register:40f0:8", ["const:b3e108:8", "const:4:8"]]
- 00b3e108 ["CALL", null, ["callee:00be0120:8"]]
+ 00b3e14c ["INT_ADD", "register:40f0:8", ["const:b3e14c:8", "const:4:8"]]
+ 00b3e14c ["CALL", null, ["callee:00be0120:8"]]
- 00b3e108 bytes f2870294
+ 00b3e14c bytes f5870294
- 00b3e16c ["INT_ADD", "register:40f0:8", ["const:b3e16c:8", "const:4:8"]]
- 00b3e16c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3e1b0 ["INT_ADD", "register:40f0:8", ["const:b3e1b0:8", "const:4:8"]]
+ 00b3e1b0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3e16c bytes 11740294
+ 00b3e1b0 bytes 14740294
- 00b3e1e4 ["INT_ADD", "register:40f0:8", ["const:b3e1e4:8", "const:4:8"]]
- 00b3e1e4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3e228 ["INT_ADD", "register:40f0:8", ["const:b3e228:8", "const:4:8"]]
+ 00b3e228 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3e1e4 bytes f3730294
+ 00b3e228 bytes f6730294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49e0343dd0a9286a2d1ae0680973626c"></a>

### [`00b3e2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e2b8.md) → [`00b3e2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e2fc.md) FUN_00b3e2fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b3d744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d744.md) [`00b3e6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e6cc.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be0130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0130.md)
- 新版 呼出元 2件 [`00b3d788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d788.md) [`00b3e710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e710.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3e2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e2b8.md#insn-00b3e2f4) · [`00b3e358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e2b8.md#insn-00b3e358) · [`00b3e3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e2b8.md#insn-00b3e3d8)
- 新版 [`00b3e338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e2fc.md#insn-00b3e338) · [`00b3e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e2fc.md#insn-00b3e39c) · [`00b3e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e2fc.md#insn-00b3e41c)

~~~diff
- 00b3e2f4 ["INT_ADD", "register:40f0:8", ["const:b3e2f4:8", "const:4:8"]]
- 00b3e2f4 ["CALL", null, ["callee:00be0180:8"]]
+ 00b3e338 ["INT_ADD", "register:40f0:8", ["const:b3e338:8", "const:4:8"]]
+ 00b3e338 ["CALL", null, ["callee:00be0180:8"]]
- 00b3e2f4 bytes 8f870294
+ 00b3e338 bytes 92870294
- 00b3e358 ["INT_ADD", "register:40f0:8", ["const:b3e358:8", "const:4:8"]]
- 00b3e358 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3e39c ["INT_ADD", "register:40f0:8", ["const:b3e39c:8", "const:4:8"]]
+ 00b3e39c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3e358 bytes 96730294
+ 00b3e39c bytes 99730294
- 00b3e3d8 ["INT_ADD", "register:40f0:8", ["const:b3e3d8:8", "const:4:8"]]
- 00b3e3d8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3e41c ["INT_ADD", "register:40f0:8", ["const:b3e41c:8", "const:4:8"]]
+ 00b3e41c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3e3d8 bytes 76730294
+ 00b3e41c bytes 79730294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c44d588730c2c373fd7425f50365343"></a>

### [`00b3e530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e530.md) → [`00b3e574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e574.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEvT0_SB_T

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd10.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00d0.md)
- 新版 呼出元 1件 [`00bdfd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd60.md) · 呼出先 2件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00be0120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3e56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e530.md#insn-00b3e56c) · [`00b3e608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e530.md#insn-00b3e608) · [`00b3e684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e530.md#insn-00b3e684)
- 新版 [`00b3e5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e574.md#insn-00b3e5b0) · [`00b3e64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e574.md#insn-00b3e64c) · [`00b3e6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e574.md#insn-00b3e6c8)

~~~diff
- 00b3e56c ["INT_ADD", "register:40f0:8", ["const:b3e56c:8", "const:4:8"]]
- 00b3e56c ["CALL", null, ["callee:00be0120:8"]]
+ 00b3e5b0 ["INT_ADD", "register:40f0:8", ["const:b3e5b0:8", "const:4:8"]]
+ 00b3e5b0 ["CALL", null, ["callee:00be0120:8"]]
- 00b3e56c bytes d9860294
+ 00b3e5b0 bytes dc860294
- 00b3e608 ["INT_ADD", "register:40f0:8", ["const:b3e608:8", "const:4:8"]]
- 00b3e608 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3e64c ["INT_ADD", "register:40f0:8", ["const:b3e64c:8", "const:4:8"]]
+ 00b3e64c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3e608 bytes ea720294
+ 00b3e64c bytes ed720294
- 00b3e684 ["INT_ADD", "register:40f0:8", ["const:b3e684:8", "const:4:8"]]
- 00b3e684 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3e6c8 ["INT_ADD", "register:40f0:8", ["const:b3e6c8:8", "const:4:8"]]
+ 00b3e6c8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3e684 bytes cb720294
+ 00b3e6c8 bytes ce720294
~~~


<a id="compare-209d6e8a09a827b7dfb137a843b33e85"></a>

### [`00b3e99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e99c.md) → [`00b3e9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e9e0.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection7ServiceEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3d0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf420.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3e9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e99c.md#insn-00b3e9f8)
- 新版 [`00b3ea3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3e9e0.md#insn-00b3ea3c)

~~~diff
- 00b3e9f8 ["INT_ADD", "register:40f0:8", ["const:b3e9f8:8", "const:4:8"]]
- 00b3e9f8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3ea3c ["INT_ADD", "register:40f0:8", ["const:b3ea3c:8", "const:4:8"]]
+ 00b3ea3c ["CALL", null, ["callee:00bdf390:8"]]
- 00b3e9f8 bytes 52820294
+ 00b3ea3c bytes 55820294
~~~


<a id="compare-39cbcff714ad23d96a45bee4a9a45a00"></a>

### [`00b3ea6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ea6c.md) → [`00b3eab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3eab0.md) _ZN11flatbuffers17FlatBufferBuilder6FinishEjPKcb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4b0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf500.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3eae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ea6c.md#insn-00b3eae8) · [`00b3eb48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ea6c.md#insn-00b3eb48) · [`00b3eba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ea6c.md#insn-00b3eba4)
- 新版 [`00b3eb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3eab0.md#insn-00b3eb2c) · [`00b3eb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3eab0.md#insn-00b3eb8c) · [`00b3ebe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3eab0.md#insn-00b3ebe8)

~~~diff
- 00b3eae8 ["INT_ADD", "register:40f0:8", ["const:b3eae8:8", "const:4:8"]]
- 00b3eae8 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3eb2c ["INT_ADD", "register:40f0:8", ["const:b3eb2c:8", "const:4:8"]]
+ 00b3eb2c ["CALL", null, ["callee:00bdf390:8"]]
- 00b3eae8 bytes 16820294
+ 00b3eb2c bytes 19820294
- 00b3eb48 ["INT_ADD", "register:40f0:8", ["const:b3eb48:8", "const:4:8"]]
- 00b3eb48 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3eb8c ["INT_ADD", "register:40f0:8", ["const:b3eb8c:8", "const:4:8"]]
+ 00b3eb8c ["CALL", null, ["callee:00bdf390:8"]]
- 00b3eb48 bytes fe810294
+ 00b3eb8c bytes 01820294
- 00b3eba4 ["INT_ADD", "register:40f0:8", ["const:b3eba4:8", "const:4:8"]]
- 00b3eba4 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b3ebe8 ["INT_ADD", "register:40f0:8", ["const:b3ebe8:8", "const:4:8"]]
+ 00b3ebe8 ["CALL", null, ["callee:00bdf390:8"]]
- 00b3eba4 bytes e7810294
+ 00b3ebe8 bytes ea810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9eca4c4d1a4a585a0c26b586ab79c2d"></a>

### [`00b3ec48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ec48.md) → [`00b3ec8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3ec8c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) · 呼出先 3件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) · 呼出先 3件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ec48.md#insn-00b3ec80) · [`00b3ecd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ec48.md#insn-00b3ecd4) · [`00b3ed1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ec48.md#insn-00b3ed1c)
- 新版 [`00b3ecc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3ec8c.md#insn-00b3ecc4) · [`00b3ed18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3ec8c.md#insn-00b3ed18) · [`00b3ed60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3ec8c.md#insn-00b3ed60)

~~~diff
- 00b3ec80 ["INT_ADD", "register:40f0:8", ["const:b3ec80:8", "const:4:8"]]
- 00b3ec80 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b3ecc4 ["INT_ADD", "register:40f0:8", ["const:b3ecc4:8", "const:4:8"]]
+ 00b3ecc4 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b3ec80 bytes 7c7d0294
+ 00b3ecc4 bytes 7f7d0294
- 00b3ecd4 ["INT_ADD", "register:40f0:8", ["const:b3ecd4:8", "const:4:8"]]
- 00b3ecd4 ["CALL", null, ["callee:00bde220:8"]]
+ 00b3ed18 ["INT_ADD", "register:40f0:8", ["const:b3ed18:8", "const:4:8"]]
+ 00b3ed18 ["CALL", null, ["callee:00bde220:8"]]
- 00b3ecd4 bytes 3f7d0294
+ 00b3ed18 bytes 427d0294
- 00b3ed1c ["INT_ADD", "register:40f0:8", ["const:b3ed1c:8", "const:4:8"]]
- 00b3ed1c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b3ed60 ["INT_ADD", "register:40f0:8", ["const:b3ed60:8", "const:4:8"]]
+ 00b3ed60 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b3ed1c bytes e1700294
+ 00b3ed60 bytes e4700294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6971e4361857cd35e40a9461e6d10fe5"></a>

### [`00b3ed68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ed68.md) → [`00b3edac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3edac.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfca0.md) · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)
- 新版 呼出元 1件 [`00bdfcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcf0.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ee64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ed68.md#insn-00b3ee64) · [`00b3ef28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ed68.md#insn-00b3ef28) · [`00b3efb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ed68.md#insn-00b3efb0)
- 新版 [`00b3eea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3edac.md#insn-00b3eea8) · [`00b3ef6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3edac.md#insn-00b3ef6c) · [`00b3eff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3edac.md#insn-00b3eff4)

~~~diff
- 00b3ee64 ["INT_ADD", "register:40f0:8", ["const:b3ee64:8", "const:4:8"]]
- 00b3ee64 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b3eea8 ["INT_ADD", "register:40f0:8", ["const:b3eea8:8", "const:4:8"]]
+ 00b3eea8 ["CALL", null, ["callee:00bdda90:8"]]
- 00b3ee64 bytes f77a0294
+ 00b3eea8 bytes fa7a0294
- 00b3ef28 ["INT_ADD", "register:40f0:8", ["const:b3ef28:8", "const:4:8"]]
- 00b3ef28 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b3ef6c ["INT_ADD", "register:40f0:8", ["const:b3ef6c:8", "const:4:8"]]
+ 00b3ef6c ["CALL", null, ["callee:00bdb040:8"]]
- 00b3ef28 bytes 32700294
+ 00b3ef6c bytes 35700294
- 00b3efb0 ["INT_ADD", "register:40f0:8", ["const:b3efb0:8", "const:4:8"]]
- 00b3efb0 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b3eff4 ["INT_ADD", "register:40f0:8", ["const:b3eff4:8", "const:4:8"]]
+ 00b3eff4 ["CALL", null, ["callee:00bdb130:8"]]
- 00b3efb0 bytes 4c700294
+ 00b3eff4 bytes 4f700294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1bd7a3a8903cd3aee2a415e22eed965"></a>

### [`00b3eff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3eff8.md) → [`00b3f03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f03c.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc50.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfca0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3eff8.md#insn-00b3f090) · [`00b3f0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3eff8.md#insn-00b3f0d8)
- 新版 [`00b3f0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f03c.md#insn-00b3f0d4) · [`00b3f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f03c.md#insn-00b3f11c)

~~~diff
- 00b3f090 ["INT_ADD", "register:40f0:8", ["const:b3f090:8", "const:4:8"]]
- 00b3f090 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f0d4 ["INT_ADD", "register:40f0:8", ["const:b3f0d4:8", "const:4:8"]]
+ 00b3f0d4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f090 bytes 48700294
+ 00b3f0d4 bytes 4b700294
- 00b3f0d8 ["INT_ADD", "register:40f0:8", ["const:b3f0d8:8", "const:4:8"]]
- 00b3f0d8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f11c ["INT_ADD", "register:40f0:8", ["const:b3f11c:8", "const:4:8"]]
+ 00b3f11c ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f0d8 bytes 36700294
+ 00b3f11c bytes 39700294
~~~


<a id="compare-e0f8388a3a315b916f76269b757388e7"></a>

### [`00b3f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f10c.md) → [`00b3f150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f150.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_valu

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc80.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcd0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f10c.md#insn-00b3f1a4) · [`00b3f1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f10c.md#insn-00b3f1ec)
- 新版 [`00b3f1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f150.md#insn-00b3f1e8) · [`00b3f230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f150.md#insn-00b3f230)

~~~diff
- 00b3f1a4 ["INT_ADD", "register:40f0:8", ["const:b3f1a4:8", "const:4:8"]]
- 00b3f1a4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f1e8 ["INT_ADD", "register:40f0:8", ["const:b3f1e8:8", "const:4:8"]]
+ 00b3f1e8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f1a4 bytes 03700294
+ 00b3f1e8 bytes 06700294
- 00b3f1ec ["INT_ADD", "register:40f0:8", ["const:b3f1ec:8", "const:4:8"]]
- 00b3f1ec ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f230 ["INT_ADD", "register:40f0:8", ["const:b3f230:8", "const:4:8"]]
+ 00b3f230 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f1ec bytes f16f0294
+ 00b3f230 bytes f46f0294
~~~


<a id="compare-c1adac8a6083644886d1858401f26364"></a>

### [`00b3f220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f220.md) → [`00b3f264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f264.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff90.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdffe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffe0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f220.md#insn-00b3f2b8) · [`00b3f300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f220.md#insn-00b3f300)
- 新版 [`00b3f2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f264.md#insn-00b3f2fc) · [`00b3f344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f264.md#insn-00b3f344)

~~~diff
- 00b3f2b8 ["INT_ADD", "register:40f0:8", ["const:b3f2b8:8", "const:4:8"]]
- 00b3f2b8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f2fc ["INT_ADD", "register:40f0:8", ["const:b3f2fc:8", "const:4:8"]]
+ 00b3f2fc ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f2b8 bytes be6f0294
+ 00b3f2fc bytes c16f0294
- 00b3f300 ["INT_ADD", "register:40f0:8", ["const:b3f300:8", "const:4:8"]]
- 00b3f300 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f344 ["INT_ADD", "register:40f0:8", ["const:b3f344:8", "const:4:8"]]
+ 00b3f344 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f300 bytes ac6f0294
+ 00b3f344 bytes af6f0294
~~~


<a id="compare-fa450331d09a5de53966df077ecba8b6"></a>

### [`00b3f334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f334.md) → [`00b3f378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f378.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff80.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdffd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffd0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f334.md#insn-00b3f3d0) · [`00b3f410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f334.md#insn-00b3f410)
- 新版 [`00b3f414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f378.md#insn-00b3f414) · [`00b3f454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f378.md#insn-00b3f454)

~~~diff
- 00b3f3d0 ["INT_ADD", "register:40f0:8", ["const:b3f3d0:8", "const:4:8"]]
- 00b3f3d0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f414 ["INT_ADD", "register:40f0:8", ["const:b3f414:8", "const:4:8"]]
+ 00b3f414 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f3d0 bytes 786f0294
+ 00b3f414 bytes 7b6f0294
- 00b3f410 ["INT_ADD", "register:40f0:8", ["const:b3f410:8", "const:4:8"]]
- 00b3f410 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f454 ["INT_ADD", "register:40f0:8", ["const:b3f454:8", "const:4:8"]]
+ 00b3f454 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f410 bytes 686f0294
+ 00b3f454 bytes 6b6f0294
~~~


<a id="compare-0366d212a142b810cad3bda030b72eb6"></a>

### [`00b3f454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f454.md) → [`00b3f498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f498.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_co

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc40.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc90.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f4ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f454.md#insn-00b3f4ec) · [`00b3f534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f454.md#insn-00b3f534)
- 新版 [`00b3f530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f498.md#insn-00b3f530) · [`00b3f578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f498.md#insn-00b3f578)

~~~diff
- 00b3f4ec ["INT_ADD", "register:40f0:8", ["const:b3f4ec:8", "const:4:8"]]
- 00b3f4ec ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f530 ["INT_ADD", "register:40f0:8", ["const:b3f530:8", "const:4:8"]]
+ 00b3f530 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f4ec bytes 316f0294
+ 00b3f530 bytes 346f0294
- 00b3f534 ["INT_ADD", "register:40f0:8", ["const:b3f534:8", "const:4:8"]]
- 00b3f534 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f578 ["INT_ADD", "register:40f0:8", ["const:b3f578:8", "const:4:8"]]
+ 00b3f578 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f534 bytes 1f6f0294
+ 00b3f578 bytes 226f0294
~~~


<a id="compare-d0cbd22fe18aa6e26e91be93fbaa3c5d"></a>

### [`00b3f568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f568.md) → [`00b3f5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f5ac.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE6assignIPS6_EENS_9enable_ifIXaasr21__is_forward_ite

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0040.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00be0090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0090.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f568.md#insn-00b3f5f0) · [`00b3f638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f568.md#insn-00b3f638) · [`00b3f688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f568.md#insn-00b3f688)
- 新版 [`00b3f634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f5ac.md#insn-00b3f634) · [`00b3f67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f5ac.md#insn-00b3f67c) · [`00b3f6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f5ac.md#insn-00b3f6cc)

~~~diff
- 00b3f5f0 ["INT_ADD", "register:40f0:8", ["const:b3f5f0:8", "const:4:8"]]
- 00b3f5f0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b3f634 ["INT_ADD", "register:40f0:8", ["const:b3f634:8", "const:4:8"]]
+ 00b3f634 ["CALL", null, ["callee:00bdb060:8"]]
- 00b3f5f0 bytes 886e0294
+ 00b3f634 bytes 8b6e0294
- 00b3f638 ["INT_ADD", "register:40f0:8", ["const:b3f638:8", "const:4:8"]]
- 00b3f638 ["CALL", null, ["callee:00bde730:8"]]
+ 00b3f67c ["INT_ADD", "register:40f0:8", ["const:b3f67c:8", "const:4:8"]]
+ 00b3f67c ["CALL", null, ["callee:00bde730:8"]]
- 00b3f638 bytes 2a7c0294
+ 00b3f67c bytes 2d7c0294
- 00b3f688 ["INT_ADD", "register:40f0:8", ["const:b3f688:8", "const:4:8"]]
- 00b3f688 ["CALL", null, ["callee:00bde230:8"]]
+ 00b3f6cc ["INT_ADD", "register:40f0:8", ["const:b3f6cc:8", "const:4:8"]]
+ 00b3f6cc ["CALL", null, ["callee:00bde230:8"]]
- 00b3f688 bytes d67a0294
+ 00b3f6cc bytes d97a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3be46a7aee102a86c8077558ffeccae1"></a>

### [`00b3f78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f78c.md) → [`00b3f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f7d0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfef0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff40.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f78c.md#insn-00b3f824) · [`00b3f86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f78c.md#insn-00b3f86c)
- 新版 [`00b3f868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f7d0.md#insn-00b3f868) · [`00b3f8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f7d0.md#insn-00b3f8b0)

~~~diff
- 00b3f824 ["INT_ADD", "register:40f0:8", ["const:b3f824:8", "const:4:8"]]
- 00b3f824 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f868 ["INT_ADD", "register:40f0:8", ["const:b3f868:8", "const:4:8"]]
+ 00b3f868 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f824 bytes 636e0294
+ 00b3f868 bytes 666e0294
- 00b3f86c ["INT_ADD", "register:40f0:8", ["const:b3f86c:8", "const:4:8"]]
- 00b3f86c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f8b0 ["INT_ADD", "register:40f0:8", ["const:b3f8b0:8", "const:4:8"]]
+ 00b3f8b0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f86c bytes 516e0294
+ 00b3f8b0 bytes 546e0294
~~~


<a id="compare-71637b8286c51eee515709e59a1144e0"></a>

### [`00b3f8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f8a0.md) → [`00b3f8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f8e4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfee0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff30.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f8a0.md#insn-00b3f93c) · [`00b3f97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f8a0.md#insn-00b3f97c)
- 新版 [`00b3f980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f8e4.md#insn-00b3f980) · [`00b3f9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f8e4.md#insn-00b3f9c0)

~~~diff
- 00b3f93c ["INT_ADD", "register:40f0:8", ["const:b3f93c:8", "const:4:8"]]
- 00b3f93c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f980 ["INT_ADD", "register:40f0:8", ["const:b3f980:8", "const:4:8"]]
+ 00b3f980 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f93c bytes 1d6e0294
+ 00b3f980 bytes 206e0294
- 00b3f97c ["INT_ADD", "register:40f0:8", ["const:b3f97c:8", "const:4:8"]]
- 00b3f97c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3f9c0 ["INT_ADD", "register:40f0:8", ["const:b3f9c0:8", "const:4:8"]]
+ 00b3f9c0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3f97c bytes 0d6e0294
+ 00b3f9c0 bytes 106e0294
~~~


<a id="compare-67a4243f8f48383e02a130b540eae0ab"></a>

### [`00b3fb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fb74.md) → [`00b3fbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fbb8.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc70.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcc0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3fc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fb74.md#insn-00b3fc0c) · [`00b3fc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fb74.md#insn-00b3fc54)
- 新版 [`00b3fc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fbb8.md#insn-00b3fc50) · [`00b3fc98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fbb8.md#insn-00b3fc98)

~~~diff
- 00b3fc0c ["INT_ADD", "register:40f0:8", ["const:b3fc0c:8", "const:4:8"]]
- 00b3fc0c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3fc50 ["INT_ADD", "register:40f0:8", ["const:b3fc50:8", "const:4:8"]]
+ 00b3fc50 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3fc0c bytes 696d0294
+ 00b3fc50 bytes 6c6d0294
- 00b3fc54 ["INT_ADD", "register:40f0:8", ["const:b3fc54:8", "const:4:8"]]
- 00b3fc54 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b3fc98 ["INT_ADD", "register:40f0:8", ["const:b3fc98:8", "const:4:8"]]
+ 00b3fc98 ["CALL", null, ["callee:00bdb200:8"]]
- 00b3fc54 bytes 576d0294
+ 00b3fc98 bytes 5a6d0294
~~~


<a id="compare-6d102eadd876a80876468096e1958674"></a>

### [`00b403bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b403bc.md) → [`00b40400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40400.md) _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE6insertENS_11__wrap_iterIPKS6_EEOS6_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0060.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bdfcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfcd0.md)
- 新版 呼出元 1件 [`00be00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00b0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bdfd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b40540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b403bc.md#insn-00b40540) · [`00b40614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b403bc.md#insn-00b40614) · [`00b40634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b403bc.md#insn-00b40634)
- 新版 [`00b40584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40400.md#insn-00b40584) · [`00b40658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40400.md#insn-00b40658) · [`00b40678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40400.md#insn-00b40678)

~~~diff
- 00b40540 ["INT_ADD", "register:40f0:8", ["const:b40540:8", "const:4:8"]]
- 00b40540 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b40584 ["INT_ADD", "register:40f0:8", ["const:b40584:8", "const:4:8"]]
+ 00b40584 ["CALL", null, ["callee:00bdb060:8"]]
- 00b40540 bytes b46a0294
+ 00b40584 bytes b76a0294
- 00b40614 ["INT_ADD", "register:40f0:8", ["const:b40614:8", "const:4:8"]]
- 00b40614 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b40658 ["INT_ADD", "register:40f0:8", ["const:b40658:8", "const:4:8"]]
+ 00b40658 ["CALL", null, ["callee:00bdb040:8"]]
- 00b40614 bytes 776a0294
+ 00b40658 bytes 7a6a0294
- 00b40634 ["INT_ADD", "register:40f0:8", ["const:b40634:8", "const:4:8"]]
- 00b40634 ["CALL", null, ["callee:00bdfd20:8"]]
+ 00b40678 ["INT_ADD", "register:40f0:8", ["const:b40678:8", "const:4:8"]]
+ 00b40678 ["CALL", null, ["callee:00bdfd20:8"]]
- 00b40634 bytes a77d0294
+ 00b40678 bytes aa7d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97188583841b258d824c3424e67f96d4"></a>

### [`00b40858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40858.md) → [`00b4089c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md) _ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfcd0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdfd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd20.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4094c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40858.md#insn-00b4094c) · [`00b409a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40858.md#insn-00b409a4) · [`00b40a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40858.md#insn-00b40a8c)
- 新版 [`00b40990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md#insn-00b40990) · [`00b409e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md#insn-00b409e8) · [`00b40ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md#insn-00b40ad0)

~~~diff
- 00b4094c ["INT_ADD", "register:40f0:8", ["const:b4094c:8", "const:4:8"]]
- 00b4094c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b40990 ["INT_ADD", "register:40f0:8", ["const:b40990:8", "const:4:8"]]
+ 00b40990 ["CALL", null, ["callee:00bdb060:8"]]
- 00b4094c bytes b1690294
+ 00b40990 bytes b4690294
- 00b409a4 ["INT_ADD", "register:40f0:8", ["const:b409a4:8", "const:4:8"]]
- 00b409a4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b409e8 ["INT_ADD", "register:40f0:8", ["const:b409e8:8", "const:4:8"]]
+ 00b409e8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b409a4 bytes 93690294
+ 00b409e8 bytes 96690294
- 00b40a8c ["INT_ADD", "register:40f0:8", ["const:b40a8c:8", "const:4:8"]]
- 00b40a8c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b40ad0 ["INT_ADD", "register:40f0:8", ["const:b40ad0:8", "const:4:8"]]
+ 00b40ad0 ["CALL", null, ["callee:00bdb060:8"]]
- 00b40a8c bytes 61690294
+ 00b40ad0 bytes 64690294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3f90e1cea885e41e9af03b04108d842"></a>

### [`00b40b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40b10.md) → [`00b40b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40b54.md) FUN_00b40b54

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b40b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40b10.md#insn-00b40b94) · [`00b40bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40b10.md#insn-00b40bd0) · [`00b40c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40b10.md#insn-00b40c04)
- 新版 [`00b40bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40b54.md#insn-00b40bd8) · [`00b40c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40b54.md#insn-00b40c14) · [`00b40c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40b54.md#insn-00b40c48)

~~~diff
- 00b40b94 ["INT_ADD", "register:40f0:8", ["const:b40b94:8", "const:4:8"]]
- 00b40b94 ["CALL", null, ["callee:00bdf7f0:8"]]
+ 00b40bd8 ["INT_ADD", "register:40f0:8", ["const:b40bd8:8", "const:4:8"]]
+ 00b40bd8 ["CALL", null, ["callee:00bdf7f0:8"]]
- 00b40b94 bytes 037b0294
+ 00b40bd8 bytes 067b0294
- 00b40bd0 ["INT_ADD", "register:40f0:8", ["const:b40bd0:8", "const:4:8"]]
- 00b40bd0 ["CALL", null, ["callee:00bdf800:8"]]
+ 00b40c14 ["INT_ADD", "register:40f0:8", ["const:b40c14:8", "const:4:8"]]
+ 00b40c14 ["CALL", null, ["callee:00bdf800:8"]]
- 00b40bd0 bytes f87a0294
+ 00b40c14 bytes fb7a0294
- 00b40c04 ["INT_ADD", "register:40f0:8", ["const:b40c04:8", "const:4:8"]]
- 00b40c04 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b40c48 ["INT_ADD", "register:40f0:8", ["const:b40c48:8", "const:4:8"]]
+ 00b40c48 ["CALL", null, ["callee:00bdb060:8"]]
- 00b40c04 bytes 03690294
+ 00b40c48 bytes 06690294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aa282ad4a3642edeead63122b1ed3fd"></a>

### [`00b40da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40da8.md) → [`00b40dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md) _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0050.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00be00a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00a0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b40e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40da8.md#insn-00b40e3c) · [`00b40f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40da8.md#insn-00b40f34) · [`00b40f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40da8.md#insn-00b40f54)
- 新版 [`00b40e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md#insn-00b40e80) · [`00b40f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md#insn-00b40f78) · [`00b40f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md#insn-00b40f98)

~~~diff
- 00b40e3c ["INT_ADD", "register:40f0:8", ["const:b40e3c:8", "const:4:8"]]
- 00b40e3c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b40e80 ["INT_ADD", "register:40f0:8", ["const:b40e80:8", "const:4:8"]]
+ 00b40e80 ["CALL", null, ["callee:00bdb040:8"]]
- 00b40e3c bytes 6d680294
+ 00b40e80 bytes 70680294
- 00b40f34 ["INT_ADD", "register:40f0:8", ["const:b40f34:8", "const:4:8"]]
- 00b40f34 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b40f78 ["INT_ADD", "register:40f0:8", ["const:b40f78:8", "const:4:8"]]
+ 00b40f78 ["CALL", null, ["callee:00bdb060:8"]]
- 00b40f34 bytes 37680294
+ 00b40f78 bytes 3a680294
- 00b40f54 ["INT_ADD", "register:40f0:8", ["const:b40f54:8", "const:4:8"]]
- 00b40f54 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b40f98 ["INT_ADD", "register:40f0:8", ["const:b40f98:8", "const:4:8"]]
+ 00b40f98 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b40f54 bytes c7740294
+ 00b40f98 bytes ca740294
~~~


<a id="compare-8bf2dd3fe3a2a86a1682ca5447cd7f06"></a>

### [`00b41078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b41078.md) → [`00b410bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b410bc.md) FUN_00b410bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf710.md) [`00bdf8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8a0.md) [`00be0010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0010.md)
- 新版 呼出元 1件 [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf760.md) [`00bdf8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8f0.md) [`00be0060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b41128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b41078.md#insn-00b41128) · [`00b41138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b41078.md#insn-00b41138) · [`00b41184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b41078.md#insn-00b41184)
- 新版 [`00b4116c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b410bc.md#insn-00b4116c) · [`00b4117c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b410bc.md#insn-00b4117c) · [`00b411c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b410bc.md#insn-00b411c8)

~~~diff
- 00b41128 ["INT_ADD", "register:40f0:8", ["const:b41128:8", "const:4:8"]]
- 00b41128 ["CALL", null, ["callee:00be0060:8"]]
+ 00b4116c ["INT_ADD", "register:40f0:8", ["const:b4116c:8", "const:4:8"]]
+ 00b4116c ["CALL", null, ["callee:00be0060:8"]]
- 00b41128 bytes ba7b0294
+ 00b4116c bytes bd7b0294
- 00b41138 ["INT_ADD", "register:40f0:8", ["const:b41138:8", "const:4:8"]]
- 00b41138 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b4117c ["INT_ADD", "register:40f0:8", ["const:b4117c:8", "const:4:8"]]
+ 00b4117c ["CALL", null, ["callee:00bdb060:8"]]
- 00b41138 bytes b6670294
+ 00b4117c bytes b9670294
- 00b41184 ["INT_ADD", "register:40f0:8", ["const:b41184:8", "const:4:8"]]
- 00b41184 ["CALL", null, ["callee:00bdf760:8"]]
+ 00b411c8 ["INT_ADD", "register:40f0:8", ["const:b411c8:8", "const:4:8"]]
+ 00b411c8 ["CALL", null, ["callee:00bdf760:8"]]
- 00b41184 bytes 63790294
+ 00b411c8 bytes 66790294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b435545d2624d464ed3a020b9ecac32"></a>

### [`00b411e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b411e0.md) → [`00b41224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md) _ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0010.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00be0060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0060.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4123c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b411e0.md#insn-00b4123c) · [`00b41248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b411e0.md#insn-00b41248) · [`00b41324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b411e0.md#insn-00b41324)
- 新版 [`00b41280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md#insn-00b41280) · [`00b4128c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md#insn-00b4128c) · [`00b41368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md#insn-00b41368)

~~~diff
- 00b4123c ["INT_ADD", "register:40f0:8", ["const:b4123c:8", "const:4:8"]]
- 00b4123c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b41280 ["INT_ADD", "register:40f0:8", ["const:b41280:8", "const:4:8"]]
+ 00b41280 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b4123c bytes 0d740294
+ 00b41280 bytes 10740294
- 00b41248 ["INT_ADD", "register:40f0:8", ["const:b41248:8", "const:4:8"]]
- 00b41248 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4128c ["INT_ADD", "register:40f0:8", ["const:b4128c:8", "const:4:8"]]
+ 00b4128c ["CALL", null, ["callee:00bdb040:8"]]
- 00b41248 bytes 6a670294
+ 00b4128c bytes 6d670294
- 00b41324 ["INT_ADD", "register:40f0:8", ["const:b41324:8", "const:4:8"]]
- 00b41324 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b41368 ["INT_ADD", "register:40f0:8", ["const:b41368:8", "const:4:8"]]
+ 00b41368 ["CALL", null, ["callee:00bdb060:8"]]
- 00b41324 bytes 3b670294
+ 00b41368 bytes 3e670294
~~~


<a id="compare-08fba3ef66593b2c5f597587534564ba"></a>

### [`00b416cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b416cc.md) → [`00b41710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41710.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdffc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffc0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0010.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b41768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b416cc.md#insn-00b41768) · [`00b417a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b416cc.md#insn-00b417a8)
- 新版 [`00b417ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41710.md#insn-00b417ac) · [`00b417ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41710.md#insn-00b417ec)

~~~diff
- 00b41768 ["INT_ADD", "register:40f0:8", ["const:b41768:8", "const:4:8"]]
- 00b41768 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b417ac ["INT_ADD", "register:40f0:8", ["const:b417ac:8", "const:4:8"]]
+ 00b417ac ["CALL", null, ["callee:00bdb200:8"]]
- 00b41768 bytes 92660294
+ 00b417ac bytes 95660294
- 00b417a8 ["INT_ADD", "register:40f0:8", ["const:b417a8:8", "const:4:8"]]
- 00b417a8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b417ec ["INT_ADD", "register:40f0:8", ["const:b417ec:8", "const:4:8"]]
+ 00b417ec ["CALL", null, ["callee:00bdb200:8"]]
- 00b417a8 bytes 82660294
+ 00b417ec bytes 85660294
~~~


<a id="compare-6c28e19365915e01b885dd8d7fd9028a"></a>

### [`00b42bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42bd4.md) → [`00b42c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42c18.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff50.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdffa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffa0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b42c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42bd4.md#insn-00b42c6c) · [`00b42cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42bd4.md#insn-00b42cb4)
- 新版 [`00b42cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42c18.md#insn-00b42cb0) · [`00b42cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42c18.md#insn-00b42cf8)

~~~diff
- 00b42c6c ["INT_ADD", "register:40f0:8", ["const:b42c6c:8", "const:4:8"]]
- 00b42c6c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b42cb0 ["INT_ADD", "register:40f0:8", ["const:b42cb0:8", "const:4:8"]]
+ 00b42cb0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b42c6c bytes 51610294
+ 00b42cb0 bytes 54610294
- 00b42cb4 ["INT_ADD", "register:40f0:8", ["const:b42cb4:8", "const:4:8"]]
- 00b42cb4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b42cf8 ["INT_ADD", "register:40f0:8", ["const:b42cf8:8", "const:4:8"]]
+ 00b42cf8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b42cb4 bytes 3f610294
+ 00b42cf8 bytes 42610294
~~~


<a id="compare-8934103eec335850de7c807e71c48ef3"></a>

### [`00b42ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42ce8.md) → [`00b42d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42d2c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff40.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff90.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b42d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42ce8.md#insn-00b42d84) · [`00b42dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42ce8.md#insn-00b42dc4)
- 新版 [`00b42dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42d2c.md#insn-00b42dc8) · [`00b42e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42d2c.md#insn-00b42e08)

~~~diff
- 00b42d84 ["INT_ADD", "register:40f0:8", ["const:b42d84:8", "const:4:8"]]
- 00b42d84 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b42dc8 ["INT_ADD", "register:40f0:8", ["const:b42dc8:8", "const:4:8"]]
+ 00b42dc8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b42d84 bytes 0b610294
+ 00b42dc8 bytes 0e610294
- 00b42dc4 ["INT_ADD", "register:40f0:8", ["const:b42dc4:8", "const:4:8"]]
- 00b42dc4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b42e08 ["INT_ADD", "register:40f0:8", ["const:b42e08:8", "const:4:8"]]
+ 00b42e08 ["CALL", null, ["callee:00bdb200:8"]]
- 00b42dc4 bytes fb600294
+ 00b42e08 bytes fe600294
~~~


<a id="compare-67fdcaa43ef56ffadc461858c779ce25"></a>

### [`00b42e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42e08.md) → [`00b42e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42e4c.md) _ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdffe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffe0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdffe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffe0.md)
- 新版 呼出元 1件 [`00be0030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0030.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b42e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42e08.md#insn-00b42e24) · [`00b42e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42e08.md#insn-00b42e30)
- 新版 [`00b42e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42e4c.md#insn-00b42e68) · [`00b42e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42e4c.md#insn-00b42e74)

~~~diff
- 00b42e24 ["INT_ADD", "register:40f0:8", ["const:b42e24:8", "const:4:8"]]
- 00b42e24 ["CALL", null, ["callee:00be0030:8"]]
+ 00b42e68 ["INT_ADD", "register:40f0:8", ["const:b42e68:8", "const:4:8"]]
+ 00b42e68 ["CALL", null, ["callee:00be0030:8"]]
- 00b42e24 bytes 6f740294
+ 00b42e68 bytes 72740294
- 00b42e30 ["INT_ADD", "register:40f0:8", ["const:b42e30:8", "const:4:8"]]
- 00b42e30 ["CALL", null, ["callee:00be0030:8"]]
+ 00b42e74 ["INT_ADD", "register:40f0:8", ["const:b42e74:8", "const:4:8"]]
+ 00b42e74 ["CALL", null, ["callee:00be0030:8"]]
- 00b42e30 bytes 6c740294
+ 00b42e74 bytes 6f740294
~~~


<a id="compare-4d6bd7f99b364f05b268b570531f435c"></a>

### [`00b42e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42e48.md) → [`00b42e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42e8c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfed0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff20.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b42ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42e48.md#insn-00b42ee0) · [`00b42f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42e48.md#insn-00b42f28)
- 新版 [`00b42f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42e8c.md#insn-00b42f24) · [`00b42f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42e8c.md#insn-00b42f6c)

~~~diff
- 00b42ee0 ["INT_ADD", "register:40f0:8", ["const:b42ee0:8", "const:4:8"]]
- 00b42ee0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b42f24 ["INT_ADD", "register:40f0:8", ["const:b42f24:8", "const:4:8"]]
+ 00b42f24 ["CALL", null, ["callee:00bdb200:8"]]
- 00b42ee0 bytes b4600294
+ 00b42f24 bytes b7600294
- 00b42f28 ["INT_ADD", "register:40f0:8", ["const:b42f28:8", "const:4:8"]]
- 00b42f28 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b42f6c ["INT_ADD", "register:40f0:8", ["const:b42f6c:8", "const:4:8"]]
+ 00b42f6c ["CALL", null, ["callee:00bdb200:8"]]
- 00b42f28 bytes a2600294
+ 00b42f6c bytes a5600294
~~~


<a id="compare-7c8378ab110b89218156e1935b1157bd"></a>

### [`00b42f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42f5c.md) → [`00b42fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42fa0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfec0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff10.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b42ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42f5c.md#insn-00b42ff8) · [`00b43038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42f5c.md#insn-00b43038)
- 新版 [`00b4303c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42fa0.md#insn-00b4303c) · [`00b4307c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42fa0.md#insn-00b4307c)

~~~diff
- 00b42ff8 ["INT_ADD", "register:40f0:8", ["const:b42ff8:8", "const:4:8"]]
- 00b42ff8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b4303c ["INT_ADD", "register:40f0:8", ["const:b4303c:8", "const:4:8"]]
+ 00b4303c ["CALL", null, ["callee:00bdb200:8"]]
- 00b42ff8 bytes 6e600294
+ 00b4303c bytes 71600294
- 00b43038 ["INT_ADD", "register:40f0:8", ["const:b43038:8", "const:4:8"]]
- 00b43038 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b4307c ["INT_ADD", "register:40f0:8", ["const:b4307c:8", "const:4:8"]]
+ 00b4307c ["CALL", null, ["callee:00bdb200:8"]]
- 00b43038 bytes 5e600294
+ 00b4307c bytes 61600294
~~~


<a id="compare-4ace4a19db76b668d74877390a5c045f"></a>

### [`00b43594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43594.md) → [`00b435d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b435d8.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0160.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be01b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01b0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b435c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43594.md#insn-00b435c8) · [`00b435e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43594.md#insn-00b435e0) · [`00b43624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43594.md#insn-00b43624)
- 新版 [`00b4360c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b435d8.md#insn-00b4360c) · [`00b43624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b435d8.md#insn-00b43624) · [`00b43668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b435d8.md#insn-00b43668)

~~~diff
- 00b435c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b435c8 ["INT_ADD", "register:40f0:8", ["const:b435c8:8", "const:4:8"]]
- 00b435c8 ["CALLIND", null, ["register:0:8"]]
+ 00b4360c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4360c ["INT_ADD", "register:40f0:8", ["const:b4360c:8", "const:4:8"]]
+ 00b4360c ["CALLIND", null, ["register:0:8"]]
- 00b435c8 bytes 00013fd6
+ 00b4360c bytes 00013fd6
- 00b435e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b435e0 ["INT_ADD", "register:40f0:8", ["const:b435e0:8", "const:4:8"]]
- 00b435e0 ["CALLIND", null, ["register:0:8"]]
+ 00b43624 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b43624 ["INT_ADD", "register:40f0:8", ["const:b43624:8", "const:4:8"]]
+ 00b43624 ["CALLIND", null, ["register:0:8"]]
- 00b435e0 bytes 20013fd6
+ 00b43624 bytes 20013fd6
- 00b43624 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43624 ["INT_ADD", "register:40f0:8", ["const:b43624:8", "const:4:8"]]
- 00b43624 ["CALLIND", null, ["register:0:8"]]
+ 00b43668 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b43668 ["INT_ADD", "register:40f0:8", ["const:b43668:8", "const:4:8"]]
+ 00b43668 ["CALLIND", null, ["register:0:8"]]
- 00b43624 bytes 00013fd6
+ 00b43668 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d74893102a0656ce1f21e92abc7826e"></a>

### [`00b43718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43718.md) → [`00b4375c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md) FUN_00b4375c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b4307c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4307c.md) [`00b4397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4397c.md) · 呼出先 1件 [`00be0160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0160.md)
- 新版 呼出元 2件 [`00b430c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b430c0.md) [`00b439c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b439c0.md) · 呼出先 1件 [`00be01b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4374c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43718.md#insn-00b4374c) · [`00b43764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43718.md#insn-00b43764) · [`00b43788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43718.md#insn-00b43788)
- 新版 [`00b43790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md#insn-00b43790) · [`00b437a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md#insn-00b437a8) · [`00b437cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md#insn-00b437cc)

~~~diff
- 00b4374c ["INT_ADD", "register:40f0:8", ["const:b4374c:8", "const:4:8"]]
- 00b4374c ["CALL", null, ["callee:00be01b0:8"]]
+ 00b43790 ["INT_ADD", "register:40f0:8", ["const:b43790:8", "const:4:8"]]
+ 00b43790 ["CALL", null, ["callee:00be01b0:8"]]
- 00b4374c bytes 85720294
+ 00b43790 bytes 88720294
- 00b43764 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b43764 ["INT_ADD", "register:40f0:8", ["const:b43764:8", "const:4:8"]]
- 00b43764 ["CALLIND", null, ["register:0:8"]]
+ 00b437a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b437a8 ["INT_ADD", "register:40f0:8", ["const:b437a8:8", "const:4:8"]]
+ 00b437a8 ["CALLIND", null, ["register:0:8"]]
- 00b43764 bytes 20013fd6
+ 00b437a8 bytes 20013fd6
- 00b43788 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43788 ["INT_ADD", "register:40f0:8", ["const:b43788:8", "const:4:8"]]
- 00b43788 ["CALLIND", null, ["register:0:8"]]
+ 00b437cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b437cc ["INT_ADD", "register:40f0:8", ["const:b437cc:8", "const:4:8"]]
+ 00b437cc ["CALLIND", null, ["register:0:8"]]
- 00b43788 bytes 00013fd6
+ 00b437cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeef7a4ff15b2c655ab2246b8c541990"></a>

### [`00b43820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43820.md) → [`00b43864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdfd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd40.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdfd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd90.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43820.md#insn-00b43850) · [`00b4386c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43820.md#insn-00b4386c) · [`00b438a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43820.md#insn-00b438a8)
- 新版 [`00b43894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md#insn-00b43894) · [`00b438b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md#insn-00b438b0) · [`00b438ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43864.md#insn-00b438ec)

~~~diff
- 00b43850 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b43850 ["INT_ADD", "register:40f0:8", ["const:b43850:8", "const:4:8"]]
- 00b43850 ["CALLIND", null, ["register:0:8"]]
+ 00b43894 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b43894 ["INT_ADD", "register:40f0:8", ["const:b43894:8", "const:4:8"]]
+ 00b43894 ["CALLIND", null, ["register:0:8"]]
- 00b43850 bytes 20013fd6
+ 00b43894 bytes 20013fd6
- 00b4386c ["COPY", "register:0:8", ["register:4048:8"]]
- 00b4386c ["INT_ADD", "register:40f0:8", ["const:b4386c:8", "const:4:8"]]
- 00b4386c ["CALLIND", null, ["register:0:8"]]
+ 00b438b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b438b0 ["INT_ADD", "register:40f0:8", ["const:b438b0:8", "const:4:8"]]
+ 00b438b0 ["CALLIND", null, ["register:0:8"]]
- 00b4386c bytes 20013fd6
+ 00b438b0 bytes 20013fd6
- 00b438a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b438a8 ["INT_ADD", "register:40f0:8", ["const:b438a8:8", "const:4:8"]]
- 00b438a8 ["CALLIND", null, ["register:0:8"]]
+ 00b438ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b438ec ["INT_ADD", "register:40f0:8", ["const:b438ec:8", "const:4:8"]]
+ 00b438ec ["CALLIND", null, ["register:0:8"]]
- 00b438a8 bytes 00013fd6
+ 00b438ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-399282a41c2ba98e6b6bb681e91128f4"></a>

### [`00b43c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43c2c.md) → [`00b43c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43c70.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfeb0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff00.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43c2c.md#insn-00b43cc4) · [`00b43d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43c2c.md#insn-00b43d0c)
- 新版 [`00b43d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43c70.md#insn-00b43d08) · [`00b43d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43c70.md#insn-00b43d50)

~~~diff
- 00b43cc4 ["INT_ADD", "register:40f0:8", ["const:b43cc4:8", "const:4:8"]]
- 00b43cc4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b43d08 ["INT_ADD", "register:40f0:8", ["const:b43d08:8", "const:4:8"]]
+ 00b43d08 ["CALL", null, ["callee:00bdb200:8"]]
- 00b43cc4 bytes 3b5d0294
+ 00b43d08 bytes 3e5d0294
- 00b43d0c ["INT_ADD", "register:40f0:8", ["const:b43d0c:8", "const:4:8"]]
- 00b43d0c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b43d50 ["INT_ADD", "register:40f0:8", ["const:b43d50:8", "const:4:8"]]
+ 00b43d50 ["CALL", null, ["callee:00bdb200:8"]]
- 00b43d0c bytes 295d0294
+ 00b43d50 bytes 2c5d0294
~~~


<a id="compare-2301aac7ed3763ab19f1e25fd77c3975"></a>

### [`00b43d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43d40.md) → [`00b43d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43d84.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfea0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfef0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43d40.md#insn-00b43ddc) · [`00b43e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43d40.md#insn-00b43e1c)
- 新版 [`00b43e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43d84.md#insn-00b43e20) · [`00b43e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43d84.md#insn-00b43e60)

~~~diff
- 00b43ddc ["INT_ADD", "register:40f0:8", ["const:b43ddc:8", "const:4:8"]]
- 00b43ddc ["CALL", null, ["callee:00bdb200:8"]]
+ 00b43e20 ["INT_ADD", "register:40f0:8", ["const:b43e20:8", "const:4:8"]]
+ 00b43e20 ["CALL", null, ["callee:00bdb200:8"]]
- 00b43ddc bytes f55c0294
+ 00b43e20 bytes f85c0294
- 00b43e1c ["INT_ADD", "register:40f0:8", ["const:b43e1c:8", "const:4:8"]]
- 00b43e1c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b43e60 ["INT_ADD", "register:40f0:8", ["const:b43e60:8", "const:4:8"]]
+ 00b43e60 ["CALL", null, ["callee:00bdb200:8"]]
- 00b43e1c bytes e55c0294
+ 00b43e60 bytes e85c0294
~~~


<a id="compare-39cbbd886e68fa265a16d7b962330ce0"></a>

### [`00b43e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43e60.md) → [`00b43ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43ea4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff70.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdffc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffc0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43e60.md#insn-00b43ef8) · [`00b43f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43e60.md#insn-00b43f40)
- 新版 [`00b43f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43ea4.md#insn-00b43f3c) · [`00b43f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43ea4.md#insn-00b43f84)

~~~diff
- 00b43ef8 ["INT_ADD", "register:40f0:8", ["const:b43ef8:8", "const:4:8"]]
- 00b43ef8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b43f3c ["INT_ADD", "register:40f0:8", ["const:b43f3c:8", "const:4:8"]]
+ 00b43f3c ["CALL", null, ["callee:00bdb200:8"]]
- 00b43ef8 bytes ae5c0294
+ 00b43f3c bytes b15c0294
- 00b43f40 ["INT_ADD", "register:40f0:8", ["const:b43f40:8", "const:4:8"]]
- 00b43f40 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b43f84 ["INT_ADD", "register:40f0:8", ["const:b43f84:8", "const:4:8"]]
+ 00b43f84 ["CALL", null, ["callee:00bdb200:8"]]
- 00b43f40 bytes 9c5c0294
+ 00b43f84 bytes 9f5c0294
~~~


<a id="compare-aa31e074000469078a3702d42b32e969"></a>

### [`00b43f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43f74.md) → [`00b43fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43fb8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff60.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdffb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffb0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43f74.md#insn-00b44010) · [`00b44050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43f74.md#insn-00b44050)
- 新版 [`00b44054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43fb8.md#insn-00b44054) · [`00b44094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43fb8.md#insn-00b44094)

~~~diff
- 00b44010 ["INT_ADD", "register:40f0:8", ["const:b44010:8", "const:4:8"]]
- 00b44010 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b44054 ["INT_ADD", "register:40f0:8", ["const:b44054:8", "const:4:8"]]
+ 00b44054 ["CALL", null, ["callee:00bdb200:8"]]
- 00b44010 bytes 685c0294
+ 00b44054 bytes 6b5c0294
- 00b44050 ["INT_ADD", "register:40f0:8", ["const:b44050:8", "const:4:8"]]
- 00b44050 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b44094 ["INT_ADD", "register:40f0:8", ["const:b44094:8", "const:4:8"]]
+ 00b44094 ["CALL", null, ["callee:00bdb200:8"]]
- 00b44050 bytes 585c0294
+ 00b44094 bytes 5b5c0294
~~~


<a id="compare-2c517302608d31446a4f40b2d3046433"></a>

### [`00b44094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44094.md) → [`00b440d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b440d8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff30.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff80.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4412c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44094.md#insn-00b4412c) · [`00b44174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44094.md#insn-00b44174)
- 新版 [`00b44170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b440d8.md#insn-00b44170) · [`00b441b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b440d8.md#insn-00b441b8)

~~~diff
- 00b4412c ["INT_ADD", "register:40f0:8", ["const:b4412c:8", "const:4:8"]]
- 00b4412c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b44170 ["INT_ADD", "register:40f0:8", ["const:b44170:8", "const:4:8"]]
+ 00b44170 ["CALL", null, ["callee:00bdb200:8"]]
- 00b4412c bytes 215c0294
+ 00b44170 bytes 245c0294
- 00b44174 ["INT_ADD", "register:40f0:8", ["const:b44174:8", "const:4:8"]]
- 00b44174 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b441b8 ["INT_ADD", "register:40f0:8", ["const:b441b8:8", "const:4:8"]]
+ 00b441b8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b44174 bytes 0f5c0294
+ 00b441b8 bytes 125c0294
~~~


<a id="compare-94d973f8bd3b349e640a352d5b19ed1e"></a>

### [`00b441a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b441a8.md) → [`00b441ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b441ec.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdff00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff00.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdff50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff50.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b441a8.md#insn-00b44244) · [`00b44284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b441a8.md#insn-00b44284)
- 新版 [`00b44288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b441ec.md#insn-00b44288) · [`00b442c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b441ec.md#insn-00b442c8)

~~~diff
- 00b44244 ["INT_ADD", "register:40f0:8", ["const:b44244:8", "const:4:8"]]
- 00b44244 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b44288 ["INT_ADD", "register:40f0:8", ["const:b44288:8", "const:4:8"]]
+ 00b44288 ["CALL", null, ["callee:00bdb200:8"]]
- 00b44244 bytes db5b0294
+ 00b44288 bytes de5b0294
- 00b44284 ["INT_ADD", "register:40f0:8", ["const:b44284:8", "const:4:8"]]
- 00b44284 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b442c8 ["INT_ADD", "register:40f0:8", ["const:b442c8:8", "const:4:8"]]
+ 00b442c8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b44284 bytes cb5b0294
+ 00b442c8 bytes ce5b0294
~~~


<a id="compare-6cfe489c1742f29a01f9af1d024c3549"></a>

### [`00b442c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md) → [`00b4430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md) _ZN11flexbuffers7Builder3KeyEPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfac0.md) · 呼出先 6件 [`00b33d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33d38.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde790.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00be0000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0000.md)
- 新版 呼出元 1件 [`00bdfb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb10.md) · 呼出先 6件 [`00b33d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33d7c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7e0.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00be0050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md#insn-00b44310) · [`00b44350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md#insn-00b44350) · [`00b4437c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md#insn-00b4437c)
- 新版 [`00b44354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md#insn-00b44354) · [`00b44394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md#insn-00b44394) · [`00b443c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md#insn-00b443c0)

~~~diff
- 00b44310 ["INT_ADD", "register:40f0:8", ["const:b44310:8", "const:4:8"]]
- 00b44310 ["CALL", null, ["callee:00be00e0:8"]]
+ 00b44354 ["INT_ADD", "register:40f0:8", ["const:b44354:8", "const:4:8"]]
+ 00b44354 ["CALL", null, ["callee:00be00e0:8"]]
- 00b44310 bytes 606f0294
+ 00b44354 bytes 636f0294
- 00b44350 ["INT_ADD", "register:40f0:8", ["const:b44350:8", "const:4:8"]]
- 00b44350 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b44394 ["INT_ADD", "register:40f0:8", ["const:b44394:8", "const:4:8"]]
+ 00b44394 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b44350 bytes 8c690294
+ 00b44394 bytes 8f690294
- 00b4437c ["INT_ADD", "register:40f0:8", ["const:b4437c:8", "const:4:8"]]
- 00b4437c ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b443c0 ["INT_ADD", "register:40f0:8", ["const:b443c0:8", "const:4:8"]]
+ 00b443c0 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b4437c bytes 81690294
+ 00b443c0 bytes 84690294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fffd2dd5c6e85619e3e0a99e483ca360"></a>

### [`00b44420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44420.md) → [`00b44464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44464.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_ite

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0000.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 1件 [`00be0050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0050.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44420.md#insn-00b44478) · [`00b4449c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44420.md#insn-00b4449c) · [`00b444dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44420.md#insn-00b444dc)
- 新版 [`00b444bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44464.md#insn-00b444bc) · [`00b444e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44464.md#insn-00b444e0) · [`00b44520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44464.md#insn-00b44520)

~~~diff
- 00b44478 ["INT_ADD", "register:40f0:8", ["const:b44478:8", "const:4:8"]]
- 00b44478 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b444bc ["INT_ADD", "register:40f0:8", ["const:b444bc:8", "const:4:8"]]
+ 00b444bc ["CALL", null, ["callee:00bde9d0:8"]]
- 00b44478 bytes 42690294
+ 00b444bc bytes 45690294
- 00b4449c ["INT_ADD", "register:40f0:8", ["const:b4449c:8", "const:4:8"]]
- 00b4449c ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b444e0 ["INT_ADD", "register:40f0:8", ["const:b444e0:8", "const:4:8"]]
+ 00b444e0 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b4449c bytes 39690294
+ 00b444e0 bytes 3c690294
- 00b444dc ["INT_ADD", "register:40f0:8", ["const:b444dc:8", "const:4:8"]]
- 00b444dc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b44520 ["INT_ADD", "register:40f0:8", ["const:b44520:8", "const:4:8"]]
+ 00b44520 ["CALL", null, ["callee:00bdb040:8"]]
- 00b444dc bytes c55a0294
+ 00b44520 bytes c85a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-087c3ad548039d315ed92d189a3e16c8"></a>

### [`00b44548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44548.md) → [`00b4458c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdffd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffd0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0020.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b445e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44548.md#insn-00b445e0) · [`00b44628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44548.md#insn-00b44628)
- 新版 [`00b44624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md#insn-00b44624) · [`00b4466c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md#insn-00b4466c)

~~~diff
- 00b445e0 ["INT_ADD", "register:40f0:8", ["const:b445e0:8", "const:4:8"]]
- 00b445e0 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b44624 ["INT_ADD", "register:40f0:8", ["const:b44624:8", "const:4:8"]]
+ 00b44624 ["CALL", null, ["callee:00bdb200:8"]]
- 00b445e0 bytes f45a0294
+ 00b44624 bytes f75a0294
- 00b44628 ["INT_ADD", "register:40f0:8", ["const:b44628:8", "const:4:8"]]
- 00b44628 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b4466c ["INT_ADD", "register:40f0:8", ["const:b4466c:8", "const:4:8"]]
+ 00b4466c ["CALL", null, ["callee:00bdb200:8"]]
- 00b44628 bytes e25a0294
+ 00b4466c bytes e55a0294
~~~


<a id="compare-8fdb3503d30cf8f65b52df79d117bf4c"></a>

### [`00b4465c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4465c.md) → [`00b446a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b446a0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfe90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe90.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfee0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b446f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4465c.md#insn-00b446f8) · [`00b44738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4465c.md#insn-00b44738)
- 新版 [`00b4473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b446a0.md#insn-00b4473c) · [`00b4477c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b446a0.md#insn-00b4477c)

~~~diff
- 00b446f8 ["INT_ADD", "register:40f0:8", ["const:b446f8:8", "const:4:8"]]
- 00b446f8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b4473c ["INT_ADD", "register:40f0:8", ["const:b4473c:8", "const:4:8"]]
+ 00b4473c ["CALL", null, ["callee:00bdb200:8"]]
- 00b446f8 bytes ae5a0294
+ 00b4473c bytes b15a0294
- 00b44738 ["INT_ADD", "register:40f0:8", ["const:b44738:8", "const:4:8"]]
- 00b44738 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b4477c ["INT_ADD", "register:40f0:8", ["const:b4477c:8", "const:4:8"]]
+ 00b4477c ["CALL", null, ["callee:00bdb200:8"]]
- 00b44738 bytes 9e5a0294
+ 00b4477c bytes a15a0294
~~~


<a id="compare-a80f67a7109e44ce8410e1d44a22b78e"></a>

### [`00b4477c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4477c.md) → [`00b447c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEvDpOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0030.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00be0080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0080.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b447fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4477c.md#insn-00b447fc) · [`00b44814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4477c.md#insn-00b44814) · [`00b44890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4477c.md#insn-00b44890)
- 新版 [`00b44840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md#insn-00b44840) · [`00b44858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md#insn-00b44858) · [`00b448d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md#insn-00b448d4)

~~~diff
- 00b447fc ["INT_ADD", "register:40f0:8", ["const:b447fc:8", "const:4:8"]]
- 00b447fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b44840 ["INT_ADD", "register:40f0:8", ["const:b44840:8", "const:4:8"]]
+ 00b44840 ["CALL", null, ["callee:00bdb040:8"]]
- 00b447fc bytes fd590294
+ 00b44840 bytes 005a0294
- 00b44814 ["INT_ADD", "register:40f0:8", ["const:b44814:8", "const:4:8"]]
- 00b44814 ["CALL", null, ["callee:00bde730:8"]]
+ 00b44858 ["INT_ADD", "register:40f0:8", ["const:b44858:8", "const:4:8"]]
+ 00b44858 ["CALL", null, ["callee:00bde730:8"]]
- 00b44814 bytes b3670294
+ 00b44858 bytes b6670294
- 00b44890 ["INT_ADD", "register:40f0:8", ["const:b44890:8", "const:4:8"]]
- 00b44890 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b448d4 ["INT_ADD", "register:40f0:8", ["const:b448d4:8", "const:4:8"]]
+ 00b448d4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b44890 bytes e0590294
+ 00b448d4 bytes e3590294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd98e3c636e194fd7bf6b932a95910f7"></a>

### [`00b448cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b448cc.md) → [`00b44910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44910.md) _ZN11flatbuffers11compareNameINS_9StructDefEEEbPKT_S4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b28f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28f64.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdfc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc20.md)
- 新版 呼出元 1件 [`00b28fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28fa8.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b448cc.md#insn-00b44910) · [`00b44928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b448cc.md#insn-00b44928) · [`00b44984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b448cc.md#insn-00b44984)
- 新版 [`00b44954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44910.md#insn-00b44954) · [`00b4496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44910.md#insn-00b4496c) · [`00b449c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44910.md#insn-00b449c8)

~~~diff
- 00b44910 ["INT_ADD", "register:40f0:8", ["const:b44910:8", "const:4:8"]]
- 00b44910 ["CALL", null, ["callee:00bdfc70:8"]]
+ 00b44954 ["INT_ADD", "register:40f0:8", ["const:b44954:8", "const:4:8"]]
+ 00b44954 ["CALL", null, ["callee:00bdfc70:8"]]
- 00b44910 bytes c46c0294
+ 00b44954 bytes c76c0294
- 00b44928 ["INT_ADD", "register:40f0:8", ["const:b44928:8", "const:4:8"]]
- 00b44928 ["CALL", null, ["callee:00bdfc70:8"]]
+ 00b4496c ["INT_ADD", "register:40f0:8", ["const:b4496c:8", "const:4:8"]]
+ 00b4496c ["CALL", null, ["callee:00bdfc70:8"]]
- 00b44928 bytes be6c0294
+ 00b4496c bytes c16c0294
- 00b44984 ["INT_ADD", "register:40f0:8", ["const:b44984:8", "const:4:8"]]
- 00b44984 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b449c8 ["INT_ADD", "register:40f0:8", ["const:b449c8:8", "const:4:8"]]
+ 00b449c8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b44984 bytes 0b5a0294
+ 00b449c8 bytes 0e5a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e793dd1b1fd14456fcfbe7a350da308"></a>

### [`00b44f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44f18.md) → [`00b44f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0170.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01c0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44f18.md#insn-00b44f4c) · [`00b44f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44f18.md#insn-00b44f64) · [`00b44fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44f18.md#insn-00b44fa8)
- 新版 [`00b44f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md#insn-00b44f90) · [`00b44fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md#insn-00b44fa8) · [`00b44fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md#insn-00b44fec)

~~~diff
- 00b44f4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44f4c ["INT_ADD", "register:40f0:8", ["const:b44f4c:8", "const:4:8"]]
- 00b44f4c ["CALLIND", null, ["register:0:8"]]
+ 00b44f90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b44f90 ["INT_ADD", "register:40f0:8", ["const:b44f90:8", "const:4:8"]]
+ 00b44f90 ["CALLIND", null, ["register:0:8"]]
- 00b44f4c bytes 00013fd6
+ 00b44f90 bytes 00013fd6
- 00b44f64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b44f64 ["INT_ADD", "register:40f0:8", ["const:b44f64:8", "const:4:8"]]
- 00b44f64 ["CALLIND", null, ["register:0:8"]]
+ 00b44fa8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b44fa8 ["INT_ADD", "register:40f0:8", ["const:b44fa8:8", "const:4:8"]]
+ 00b44fa8 ["CALLIND", null, ["register:0:8"]]
- 00b44f64 bytes 20013fd6
+ 00b44fa8 bytes 20013fd6
- 00b44fa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44fa8 ["INT_ADD", "register:40f0:8", ["const:b44fa8:8", "const:4:8"]]
- 00b44fa8 ["CALLIND", null, ["register:0:8"]]
+ 00b44fec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b44fec ["INT_ADD", "register:40f0:8", ["const:b44fec:8", "const:4:8"]]
+ 00b44fec ["CALLIND", null, ["register:0:8"]]
- 00b44fa8 bytes 00013fd6
+ 00b44fec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed19f9182e34c5307a198362e29e25e2"></a>

### [`00b4509c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b4509c.md) → [`00b450e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md) FUN_00b450e0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b44a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44a00.md) [`00b45300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45300.md) · 呼出先 1件 [`00be0170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0170.md)
- 新版 呼出元 2件 [`00b44a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md) [`00b45344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45344.md) · 呼出先 1件 [`00be01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b450d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b4509c.md#insn-00b450d0) · [`00b450e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b4509c.md#insn-00b450e8) · [`00b4510c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b4509c.md#insn-00b4510c)
- 新版 [`00b45114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md#insn-00b45114) · [`00b4512c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md#insn-00b4512c) · [`00b45150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md#insn-00b45150)

~~~diff
- 00b450d0 ["INT_ADD", "register:40f0:8", ["const:b450d0:8", "const:4:8"]]
- 00b450d0 ["CALL", null, ["callee:00be01c0:8"]]
+ 00b45114 ["INT_ADD", "register:40f0:8", ["const:b45114:8", "const:4:8"]]
+ 00b45114 ["CALL", null, ["callee:00be01c0:8"]]
- 00b450d0 bytes 286c0294
+ 00b45114 bytes 2b6c0294
- 00b450e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b450e8 ["INT_ADD", "register:40f0:8", ["const:b450e8:8", "const:4:8"]]
- 00b450e8 ["CALLIND", null, ["register:0:8"]]
+ 00b4512c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b4512c ["INT_ADD", "register:40f0:8", ["const:b4512c:8", "const:4:8"]]
+ 00b4512c ["CALLIND", null, ["register:0:8"]]
- 00b450e8 bytes 20013fd6
+ 00b4512c bytes 20013fd6
- 00b4510c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4510c ["INT_ADD", "register:40f0:8", ["const:b4510c:8", "const:4:8"]]
- 00b4510c ["CALLIND", null, ["register:0:8"]]
+ 00b45150 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45150 ["INT_ADD", "register:40f0:8", ["const:b45150:8", "const:4:8"]]
+ 00b45150 ["CALLIND", null, ["register:0:8"]]
- 00b4510c bytes 00013fd6
+ 00b45150 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-059b7a265c1d6ca5f45a02e5209684f1"></a>

### [`00b451a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b451a4.md) → [`00b451e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b451e8.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdfd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd50.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdfda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfda0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b451d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b451a4.md#insn-00b451d4) · [`00b451f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b451a4.md#insn-00b451f0) · [`00b4522c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b451a4.md#insn-00b4522c)
- 新版 [`00b45218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b451e8.md#insn-00b45218) · [`00b45234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b451e8.md#insn-00b45234) · [`00b45270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b451e8.md#insn-00b45270)

~~~diff
- 00b451d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b451d4 ["INT_ADD", "register:40f0:8", ["const:b451d4:8", "const:4:8"]]
- 00b451d4 ["CALLIND", null, ["register:0:8"]]
+ 00b45218 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b45218 ["INT_ADD", "register:40f0:8", ["const:b45218:8", "const:4:8"]]
+ 00b45218 ["CALLIND", null, ["register:0:8"]]
- 00b451d4 bytes 20013fd6
+ 00b45218 bytes 20013fd6
- 00b451f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b451f0 ["INT_ADD", "register:40f0:8", ["const:b451f0:8", "const:4:8"]]
- 00b451f0 ["CALLIND", null, ["register:0:8"]]
+ 00b45234 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b45234 ["INT_ADD", "register:40f0:8", ["const:b45234:8", "const:4:8"]]
+ 00b45234 ["CALLIND", null, ["register:0:8"]]
- 00b451f0 bytes 20013fd6
+ 00b45234 bytes 20013fd6
- 00b4522c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4522c ["INT_ADD", "register:40f0:8", ["const:b4522c:8", "const:4:8"]]
- 00b4522c ["CALLIND", null, ["register:0:8"]]
+ 00b45270 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45270 ["INT_ADD", "register:40f0:8", ["const:b45270:8", "const:4:8"]]
+ 00b45270 ["CALLIND", null, ["register:0:8"]]
- 00b4522c bytes 00013fd6
+ 00b45270 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197efe8aff7fcb72306b61e560dff1da"></a>

### [`00b455b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b455b0.md) → [`00b455f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md) _ZN11flatbuffers11compareNameINS_7EnumDefEEEbPKT_S4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b29090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29090.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdfc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc20.md)
- 新版 呼出元 1件 [`00b290d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b290d4.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b455f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b455b0.md#insn-00b455f4) · [`00b4560c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b455b0.md#insn-00b4560c) · [`00b45668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b455b0.md#insn-00b45668)
- 新版 [`00b45638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md#insn-00b45638) · [`00b45650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md#insn-00b45650) · [`00b456ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md#insn-00b456ac)

~~~diff
- 00b455f4 ["INT_ADD", "register:40f0:8", ["const:b455f4:8", "const:4:8"]]
- 00b455f4 ["CALL", null, ["callee:00bdfc70:8"]]
+ 00b45638 ["INT_ADD", "register:40f0:8", ["const:b45638:8", "const:4:8"]]
+ 00b45638 ["CALL", null, ["callee:00bdfc70:8"]]
- 00b455f4 bytes 8b690294
+ 00b45638 bytes 8e690294
- 00b4560c ["INT_ADD", "register:40f0:8", ["const:b4560c:8", "const:4:8"]]
- 00b4560c ["CALL", null, ["callee:00bdfc70:8"]]
+ 00b45650 ["INT_ADD", "register:40f0:8", ["const:b45650:8", "const:4:8"]]
+ 00b45650 ["CALL", null, ["callee:00bdfc70:8"]]
- 00b4560c bytes 85690294
+ 00b45650 bytes 88690294
- 00b45668 ["INT_ADD", "register:40f0:8", ["const:b45668:8", "const:4:8"]]
- 00b45668 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b456ac ["INT_ADD", "register:40f0:8", ["const:b456ac:8", "const:4:8"]]
+ 00b456ac ["CALL", null, ["callee:00bdb200:8"]]
- 00b45668 bytes d2560294
+ 00b456ac bytes d5560294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8598ba846fd3d6a18ec1eae827ae63d7"></a>

### [`00b45bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45bfc.md) → [`00b45c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0150.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be01a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01a0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b45c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45bfc.md#insn-00b45c30) · [`00b45c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45bfc.md#insn-00b45c48) · [`00b45c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45bfc.md#insn-00b45c8c)
- 新版 [`00b45c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md#insn-00b45c74) · [`00b45c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md#insn-00b45c8c) · [`00b45cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md#insn-00b45cd0)

~~~diff
- 00b45c30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45c30 ["INT_ADD", "register:40f0:8", ["const:b45c30:8", "const:4:8"]]
- 00b45c30 ["CALLIND", null, ["register:0:8"]]
+ 00b45c74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45c74 ["INT_ADD", "register:40f0:8", ["const:b45c74:8", "const:4:8"]]
+ 00b45c74 ["CALLIND", null, ["register:0:8"]]
- 00b45c30 bytes 00013fd6
+ 00b45c74 bytes 00013fd6
- 00b45c48 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b45c48 ["INT_ADD", "register:40f0:8", ["const:b45c48:8", "const:4:8"]]
- 00b45c48 ["CALLIND", null, ["register:0:8"]]
+ 00b45c8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b45c8c ["INT_ADD", "register:40f0:8", ["const:b45c8c:8", "const:4:8"]]
+ 00b45c8c ["CALLIND", null, ["register:0:8"]]
- 00b45c48 bytes 20013fd6
+ 00b45c8c bytes 20013fd6
- 00b45c8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45c8c ["INT_ADD", "register:40f0:8", ["const:b45c8c:8", "const:4:8"]]
- 00b45c8c ["CALLIND", null, ["register:0:8"]]
+ 00b45cd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45cd0 ["INT_ADD", "register:40f0:8", ["const:b45cd0:8", "const:4:8"]]
+ 00b45cd0 ["CALLIND", null, ["register:0:8"]]
- 00b45c8c bytes 00013fd6
+ 00b45cd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01b3d782247286e331bacf3335260c65"></a>

### [`00b45d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45d80.md) → [`00b45dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md) FUN_00b45dc4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b456e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b456e4.md) [`00b45fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45fe4.md) · 呼出先 1件 [`00be0150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0150.md)
- 新版 呼出元 2件 [`00b45728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45728.md) [`00b46028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46028.md) · 呼出先 1件 [`00be01a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b45db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45d80.md#insn-00b45db4) · [`00b45dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45d80.md#insn-00b45dcc) · [`00b45df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45d80.md#insn-00b45df0)
- 新版 [`00b45df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md#insn-00b45df8) · [`00b45e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md#insn-00b45e10) · [`00b45e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md#insn-00b45e34)

~~~diff
- 00b45db4 ["INT_ADD", "register:40f0:8", ["const:b45db4:8", "const:4:8"]]
- 00b45db4 ["CALL", null, ["callee:00be01a0:8"]]
+ 00b45df8 ["INT_ADD", "register:40f0:8", ["const:b45df8:8", "const:4:8"]]
+ 00b45df8 ["CALL", null, ["callee:00be01a0:8"]]
- 00b45db4 bytes e7680294
+ 00b45df8 bytes ea680294
- 00b45dcc ["COPY", "register:0:8", ["register:4048:8"]]
- 00b45dcc ["INT_ADD", "register:40f0:8", ["const:b45dcc:8", "const:4:8"]]
- 00b45dcc ["CALLIND", null, ["register:0:8"]]
+ 00b45e10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b45e10 ["INT_ADD", "register:40f0:8", ["const:b45e10:8", "const:4:8"]]
+ 00b45e10 ["CALLIND", null, ["register:0:8"]]
- 00b45dcc bytes 20013fd6
+ 00b45e10 bytes 20013fd6
- 00b45df0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45df0 ["INT_ADD", "register:40f0:8", ["const:b45df0:8", "const:4:8"]]
- 00b45df0 ["CALLIND", null, ["register:0:8"]]
+ 00b45e34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45e34 ["INT_ADD", "register:40f0:8", ["const:b45e34:8", "const:4:8"]]
+ 00b45e34 ["CALLIND", null, ["register:0:8"]]
- 00b45df0 bytes 00013fd6
+ 00b45e34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b8efcf4cbc9b7a6ab64faf048f76fd"></a>

### [`00b45e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45e88.md) → [`00b45ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45ecc.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdfd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd30.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdfd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd80.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b45eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45e88.md#insn-00b45eb8) · [`00b45ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45e88.md#insn-00b45ed4) · [`00b45f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45e88.md#insn-00b45f10)
- 新版 [`00b45efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45ecc.md#insn-00b45efc) · [`00b45f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45ecc.md#insn-00b45f18) · [`00b45f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45ecc.md#insn-00b45f54)

~~~diff
- 00b45eb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b45eb8 ["INT_ADD", "register:40f0:8", ["const:b45eb8:8", "const:4:8"]]
- 00b45eb8 ["CALLIND", null, ["register:0:8"]]
+ 00b45efc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b45efc ["INT_ADD", "register:40f0:8", ["const:b45efc:8", "const:4:8"]]
+ 00b45efc ["CALLIND", null, ["register:0:8"]]
- 00b45eb8 bytes 20013fd6
+ 00b45efc bytes 20013fd6
- 00b45ed4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b45ed4 ["INT_ADD", "register:40f0:8", ["const:b45ed4:8", "const:4:8"]]
- 00b45ed4 ["CALLIND", null, ["register:0:8"]]
+ 00b45f18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b45f18 ["INT_ADD", "register:40f0:8", ["const:b45f18:8", "const:4:8"]]
+ 00b45f18 ["CALLIND", null, ["register:0:8"]]
- 00b45ed4 bytes 20013fd6
+ 00b45f18 bytes 20013fd6
- 00b45f10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45f10 ["INT_ADD", "register:40f0:8", ["const:b45f10:8", "const:4:8"]]
- 00b45f10 ["CALLIND", null, ["register:0:8"]]
+ 00b45f54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45f54 ["INT_ADD", "register:40f0:8", ["const:b45f54:8", "const:4:8"]]
+ 00b45f54 ["CALLIND", null, ["register:0:8"]]
- 00b45f10 bytes 00013fd6
+ 00b45f54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e711c9b704ea10adeaed402eda42ae19"></a>

### [`00b46294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46294.md) → [`00b462d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b462d8.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection7RPCCallEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3c0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf410.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b462f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46294.md#insn-00b462f0)
- 新版 [`00b46334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b462d8.md#insn-00b46334)

~~~diff
- 00b462f0 ["INT_ADD", "register:40f0:8", ["const:b462f0:8", "const:4:8"]]
- 00b462f0 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b46334 ["INT_ADD", "register:40f0:8", ["const:b46334:8", "const:4:8"]]
+ 00b46334 ["CALL", null, ["callee:00bdf390:8"]]
- 00b462f0 bytes 14640294
+ 00b46334 bytes 17640294
~~~


<a id="compare-f6cbf6098c33b28c516887062b5632be"></a>

### [`00b46364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46364.md) → [`00b463a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b463a8.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection7EnumValEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3b0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf400.md) · 呼出先 2件 [`00bdf390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf390.md) [`00bdf480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b463c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46364.md#insn-00b463c0)
- 新版 [`00b46404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b463a8.md#insn-00b46404)

~~~diff
- 00b463c0 ["INT_ADD", "register:40f0:8", ["const:b463c0:8", "const:4:8"]]
- 00b463c0 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b46404 ["INT_ADD", "register:40f0:8", ["const:b46404:8", "const:4:8"]]
+ 00b46404 ["CALL", null, ["callee:00bdf390:8"]]
- 00b463c0 bytes e0630294
+ 00b46404 bytes e3630294
~~~


<a id="compare-1588c9552e3331923dd5dd407264651a"></a>

### [`00b46434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46434.md) → [`00b46478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46478.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_19__map_value_compareIS7_S8_NS_4lessI

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc90.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdfce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfce0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b464cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46434.md#insn-00b464cc) · [`00b46514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46434.md#insn-00b46514)
- 新版 [`00b46510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46478.md#insn-00b46510) · [`00b46558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46478.md#insn-00b46558)

~~~diff
- 00b464cc ["INT_ADD", "register:40f0:8", ["const:b464cc:8", "const:4:8"]]
- 00b464cc ["CALL", null, ["callee:00bdb200:8"]]
+ 00b46510 ["INT_ADD", "register:40f0:8", ["const:b46510:8", "const:4:8"]]
+ 00b46510 ["CALL", null, ["callee:00bdb200:8"]]
- 00b464cc bytes 39530294
+ 00b46510 bytes 3c530294
- 00b46514 ["INT_ADD", "register:40f0:8", ["const:b46514:8", "const:4:8"]]
- 00b46514 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b46558 ["INT_ADD", "register:40f0:8", ["const:b46558:8", "const:4:8"]]
+ 00b46558 ["CALL", null, ["callee:00bdb200:8"]]
- 00b46514 bytes 27530294
+ 00b46558 bytes 2a530294
~~~


<a id="compare-00645c21c0d1464b22c435c4a1581ce5"></a>

### [`00b46548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46548.md) → [`00b4658c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4658c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffb0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffb0.md)
- 新版 呼出元 1件 [`00be0000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0000.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b46564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46548.md#insn-00b46564) · [`00b46570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46548.md#insn-00b46570) · [`00b46580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46548.md#insn-00b46580)
- 新版 [`00b465a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4658c.md#insn-00b465a8) · [`00b465b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4658c.md#insn-00b465b4) · [`00b465c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4658c.md#insn-00b465c4)

~~~diff
- 00b46564 ["INT_ADD", "register:40f0:8", ["const:b46564:8", "const:4:8"]]
- 00b46564 ["CALL", null, ["callee:00be0000:8"]]
+ 00b465a8 ["INT_ADD", "register:40f0:8", ["const:b465a8:8", "const:4:8"]]
+ 00b465a8 ["CALL", null, ["callee:00be0000:8"]]
- 00b46564 bytes 93660294
+ 00b465a8 bytes 96660294
- 00b46570 ["INT_ADD", "register:40f0:8", ["const:b46570:8", "const:4:8"]]
- 00b46570 ["CALL", null, ["callee:00be0000:8"]]
+ 00b465b4 ["INT_ADD", "register:40f0:8", ["const:b465b4:8", "const:4:8"]]
+ 00b465b4 ["CALL", null, ["callee:00be0000:8"]]
- 00b46570 bytes 90660294
+ 00b465b4 bytes 93660294
- 00b46580 ["INT_ADD", "register:40f0:8", ["const:b46580:8", "const:4:8"]]
- 00b46580 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b465c4 ["INT_ADD", "register:40f0:8", ["const:b465c4:8", "const:4:8"]]
+ 00b465c4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b46580 bytes a4520294
+ 00b465c4 bytes a7520294
~~~


<a id="compare-a924c72a64573aceb8cb9c30b5a92c73"></a>

### [`00b46b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46b1c.md) → [`00b46b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b60.md) _ZN11flatbuffers9DirExistsEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc9c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b46b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46b1c.md#insn-00b46b2c)
- 新版 [`00b46b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b60.md#insn-00b46b70)

~~~diff
- 00b46b2c ["INT_ADD", "register:40f0:8", ["const:b46b2c:8", "const:4:8"]]
- 00b46b2c ["CALL", null, ["callee:00bdca10:8"]]
+ 00b46b70 ["INT_ADD", "register:40f0:8", ["const:b46b70:8", "const:4:8"]]
+ 00b46b70 ["CALL", null, ["callee:00bdca10:8"]]
- 00b46b2c bytes a5570294
+ 00b46b70 bytes a8570294
~~~


<a id="compare-189cb5d3c512bc05d7e926dd2cefe9c3"></a>

### [`00b46b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46b50.md) → [`00b46b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b94.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc950.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md)
- 新版 呼出元 1件 [`00bdc9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9a0.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b46b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46b50.md#insn-00b46b84) · [`00b46bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46b50.md#insn-00b46bac) · [`00b46be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46b50.md#insn-00b46be0)
- 新版 [`00b46bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b94.md#insn-00b46bc8) · [`00b46bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b94.md#insn-00b46bf0) · [`00b46c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b94.md#insn-00b46c24)

~~~diff
- 00b46b84 ["INT_ADD", "register:40f0:8", ["const:b46b84:8", "const:4:8"]]
- 00b46b84 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b46bc8 ["INT_ADD", "register:40f0:8", ["const:b46bc8:8", "const:4:8"]]
+ 00b46bc8 ["CALL", null, ["callee:00bdb450:8"]]
- 00b46b84 bytes 1f520294
+ 00b46bc8 bytes 22520294
- 00b46bac ["INT_ADD", "register:40f0:8", ["const:b46bac:8", "const:4:8"]]
- 00b46bac ["CALL", null, ["callee:00bdc0a0:8"]]
+ 00b46bf0 ["INT_ADD", "register:40f0:8", ["const:b46bf0:8", "const:4:8"]]
+ 00b46bf0 ["CALL", null, ["callee:00bdc0a0:8"]]
- 00b46bac bytes 29550294
+ 00b46bf0 bytes 2c550294
- 00b46be0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46be0 ["INT_ADD", "register:40f0:8", ["const:b46be0:8", "const:4:8"]]
- 00b46be0 ["CALLIND", null, ["register:0:8"]]
+ 00b46c24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46c24 ["INT_ADD", "register:40f0:8", ["const:b46c24:8", "const:4:8"]]
+ 00b46c24 ["CALLIND", null, ["register:0:8"]]
- 00b46be0 bytes 00013fd6
+ 00b46c24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b70b36cd8a611d012f9fe9a978a2d4a1"></a>

### [`00b46c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46c1c.md) → [`00b46c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46c60.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5tellgEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc940.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md)
- 新版 呼出元 1件 [`00bdc990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc990.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b46c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46c1c.md#insn-00b46c44) · [`00b46c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46c1c.md#insn-00b46c5c) · [`00b46c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46c1c.md#insn-00b46c90)
- 新版 [`00b46c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46c60.md#insn-00b46c88) · [`00b46ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46c60.md#insn-00b46ca0) · [`00b46cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46c60.md#insn-00b46cd4)

~~~diff
- 00b46c44 ["INT_ADD", "register:40f0:8", ["const:b46c44:8", "const:4:8"]]
- 00b46c44 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b46c88 ["INT_ADD", "register:40f0:8", ["const:b46c88:8", "const:4:8"]]
+ 00b46c88 ["CALL", null, ["callee:00bdb450:8"]]
- 00b46c44 bytes ef510294
+ 00b46c88 bytes f2510294
- 00b46c5c ["INT_ADD", "register:40f0:8", ["const:b46c5c:8", "const:4:8"]]
- 00b46c5c ["CALL", null, ["callee:00bdc0a0:8"]]
+ 00b46ca0 ["INT_ADD", "register:40f0:8", ["const:b46ca0:8", "const:4:8"]]
+ 00b46ca0 ["CALL", null, ["callee:00bdc0a0:8"]]
- 00b46c5c bytes fd540294
+ 00b46ca0 bytes 00550294
- 00b46c90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46c90 ["INT_ADD", "register:40f0:8", ["const:b46c90:8", "const:4:8"]]
- 00b46c90 ["CALLIND", null, ["register:0:8"]]
+ 00b46cd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46cd4 ["INT_ADD", "register:40f0:8", ["const:b46cd4:8", "const:4:8"]]
+ 00b46cd4 ["CALLIND", null, ["register:0:8"]]
- 00b46c90 bytes 00013fd6
+ 00b46cd4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffb55c36743bbbf2647f7ebb491fd6d8"></a>

### [`00b46cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46cc8.md) → [`00b46d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46d0c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0260.md) · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)
- 新版 呼出元 1件 [`00be02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02b0.md) · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b46cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46cc8.md#insn-00b46cfc) · [`00b46d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46cc8.md#insn-00b46d28) · [`00b46d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46cc8.md#insn-00b46d48)
- 新版 [`00b46d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46d0c.md#insn-00b46d40) · [`00b46d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46d0c.md#insn-00b46d6c) · [`00b46d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46d0c.md#insn-00b46d8c)

~~~diff
- 00b46cfc ["INT_ADD", "register:40f0:8", ["const:b46cfc:8", "const:4:8"]]
- 00b46cfc ["CALL", null, ["callee:00bdc0a0:8"]]
+ 00b46d40 ["INT_ADD", "register:40f0:8", ["const:b46d40:8", "const:4:8"]]
+ 00b46d40 ["CALL", null, ["callee:00bdc0a0:8"]]
- 00b46cfc bytes d5540294
+ 00b46d40 bytes d8540294
- 00b46d28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46d28 ["INT_ADD", "register:40f0:8", ["const:b46d28:8", "const:4:8"]]
- 00b46d28 ["CALLIND", null, ["register:0:8"]]
+ 00b46d6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46d6c ["INT_ADD", "register:40f0:8", ["const:b46d6c:8", "const:4:8"]]
+ 00b46d6c ["CALLIND", null, ["register:0:8"]]
- 00b46d28 bytes 00013fd6
+ 00b46d6c bytes 00013fd6
- 00b46d48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46d48 ["INT_ADD", "register:40f0:8", ["const:b46d48:8", "const:4:8"]]
- 00b46d48 ["CALLIND", null, ["register:0:8"]]
+ 00b46d8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46d8c ["INT_ADD", "register:40f0:8", ["const:b46d8c:8", "const:4:8"]]
+ 00b46d8c ["CALLIND", null, ["register:0:8"]]
- 00b46d48 bytes 00013fd6
+ 00b46d8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da6a5d2f6d311a9042d8d6d0d2c34773"></a>

### [`00b4704c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4704c.md) → [`00b47090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47090.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbdd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbdd0.md) · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)
- 新版 呼出元 1件 [`00bdbe20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe20.md) · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4704c.md#insn-00b47098) · [`00b470b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4704c.md#insn-00b470b8) · [`00b470d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4704c.md#insn-00b470d8)
- 新版 [`00b470dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47090.md#insn-00b470dc) · [`00b470fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47090.md#insn-00b470fc) · [`00b4711c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47090.md#insn-00b4711c)

~~~diff
- 00b47098 ["INT_ADD", "register:40f0:8", ["const:b47098:8", "const:4:8"]]
- 00b47098 ["CALL", null, ["callee:00be01f0:8"]]
+ 00b470dc ["INT_ADD", "register:40f0:8", ["const:b470dc:8", "const:4:8"]]
+ 00b470dc ["CALL", null, ["callee:00be01f0:8"]]
- 00b47098 bytes 42640294
+ 00b470dc bytes 45640294
- 00b470b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b470b8 ["INT_ADD", "register:40f0:8", ["const:b470b8:8", "const:4:8"]]
- 00b470b8 ["CALLIND", null, ["register:0:8"]]
+ 00b470fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b470fc ["INT_ADD", "register:40f0:8", ["const:b470fc:8", "const:4:8"]]
+ 00b470fc ["CALLIND", null, ["register:0:8"]]
- 00b470b8 bytes 00013fd6
+ 00b470fc bytes 00013fd6
- 00b470d8 ["INT_ADD", "register:40f0:8", ["const:b470d8:8", "const:4:8"]]
- 00b470d8 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b4711c ["INT_ADD", "register:40f0:8", ["const:b4711c:8", "const:4:8"]]
+ 00b4711c ["CALL", null, ["callee:00bdb450:8"]]
- 00b470d8 bytes ca500294
+ 00b4711c bytes cd500294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e793a7976fdec9d2ac7daeea8f219a"></a>

### [`00b47394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47394.md) → [`00b473d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b473d8.md) _ZN11flatbuffers18ConCatPathFileNameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf950.md) · 呼出先 4件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00bdf9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9a0.md) · 呼出先 4件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b473b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47394.md#insn-00b473b4) · [`00b47448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47394.md#insn-00b47448) · [`00b47498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47394.md#insn-00b47498)
- 新版 [`00b473f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b473d8.md#insn-00b473f8) · [`00b4748c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b473d8.md#insn-00b4748c) · [`00b474dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b473d8.md#insn-00b474dc)

~~~diff
- 00b473b4 ["INT_ADD", "register:40f0:8", ["const:b473b4:8", "const:4:8"]]
- 00b473b4 ["CALL", null, ["callee:00bde730:8"]]
+ 00b473f8 ["INT_ADD", "register:40f0:8", ["const:b473f8:8", "const:4:8"]]
+ 00b473f8 ["CALL", null, ["callee:00bde730:8"]]
- 00b473b4 bytes cb5c0294
+ 00b473f8 bytes ce5c0294
- 00b47448 ["INT_ADD", "register:40f0:8", ["const:b47448:8", "const:4:8"]]
- 00b47448 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b4748c ["INT_ADD", "register:40f0:8", ["const:b4748c:8", "const:4:8"]]
+ 00b4748c ["CALL", null, ["callee:00bdda90:8"]]
- 00b47448 bytes 7e590294
+ 00b4748c bytes 81590294
- 00b47498 ["INT_ADD", "register:40f0:8", ["const:b47498:8", "const:4:8"]]
- 00b47498 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b474dc ["INT_ADD", "register:40f0:8", ["const:b474dc:8", "const:4:8"]]
+ 00b474dc ["CALL", null, ["callee:00bdb130:8"]]
- 00b47498 bytes 124f0294
+ 00b474dc bytes 154f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c02ca0ba08c9a8e62719226bb02b8eb"></a>

### [`00b47524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47524.md) → [`00b47568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47568.md) _ZN11flatbuffers9PosixPathEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa80.md) · 呼出先 1件 [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)
- 新版 呼出元 1件 [`00bdfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfad0.md) · 呼出先 1件 [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4753c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47524.md#insn-00b4753c)
- 新版 [`00b47580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47568.md#insn-00b47580)

~~~diff
- 00b4753c ["INT_ADD", "register:40f0:8", ["const:b4753c:8", "const:4:8"]]
- 00b4753c ["CALL", null, ["callee:00bde740:8"]]
+ 00b47580 ["INT_ADD", "register:40f0:8", ["const:b47580:8", "const:4:8"]]
+ 00b47580 ["CALL", null, ["callee:00bde740:8"]]
- 00b4753c bytes 6d5c0294
+ 00b47580 bytes 705c0294
~~~


<a id="compare-a61639a921334f3262fbff02d3c769bd"></a>

### [`00b4778c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4778c.md) → [`00b477d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b477d0.md) _ZN11flatbuffers12AbsolutePathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf940.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md) [`00be0290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0290.md)
- 新版 呼出元 1件 [`00bdf990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf990.md) · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md) [`00be02e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b477cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4778c.md#insn-00b477cc) · [`00b477dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4778c.md#insn-00b477dc) · [`00b477ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4778c.md#insn-00b477ec)
- 新版 [`00b47810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b477d0.md#insn-00b47810) · [`00b47820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b477d0.md#insn-00b47820) · [`00b47830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b477d0.md#insn-00b47830)

~~~diff
- 00b477cc ["INT_ADD", "register:40f0:8", ["const:b477cc:8", "const:4:8"]]
- 00b477cc ["CALL", null, ["callee:00be02e0:8"]]
+ 00b47810 ["INT_ADD", "register:40f0:8", ["const:b47810:8", "const:4:8"]]
+ 00b47810 ["CALL", null, ["callee:00be02e0:8"]]
- 00b477cc bytes b1620294
+ 00b47810 bytes b4620294
- 00b477dc ["INT_ADD", "register:40f0:8", ["const:b477dc:8", "const:4:8"]]
- 00b477dc ["CALL", null, ["callee:00bde740:8"]]
+ 00b47820 ["INT_ADD", "register:40f0:8", ["const:b47820:8", "const:4:8"]]
+ 00b47820 ["CALL", null, ["callee:00bde740:8"]]
- 00b477dc bytes c55b0294
+ 00b47820 bytes c85b0294
- 00b477ec ["INT_ADD", "register:40f0:8", ["const:b477ec:8", "const:4:8"]]
- 00b477ec ["CALL", null, ["callee:00bde730:8"]]
+ 00b47830 ["INT_ADD", "register:40f0:8", ["const:b47830:8", "const:4:8"]]
+ 00b47830 ["CALL", null, ["callee:00bde730:8"]]
- 00b477ec bytes bd5b0294
+ 00b47830 bytes c05b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82d3254c2bc3617900b43367e8d2d09c"></a>

### [`00b47878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47878.md) → [`00b478bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md) _ZN11flatbuffers19SetGlobalTestLocaleEPKcPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47878.md#insn-00b4789c) · [`00b478b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47878.md#insn-00b478b4) · [`00b478f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47878.md#insn-00b478f0)
- 新版 [`00b478e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md#insn-00b478e0) · [`00b478f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md#insn-00b478f8) · [`00b47934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md#insn-00b47934)

~~~diff
- 00b4789c ["INT_ADD", "register:40f0:8", ["const:b4789c:8", "const:4:8"]]
- 00b4789c ["CALL", null, ["callee:00be02f0:8"]]
+ 00b478e0 ["INT_ADD", "register:40f0:8", ["const:b478e0:8", "const:4:8"]]
+ 00b478e0 ["CALL", null, ["callee:00be02f0:8"]]
- 00b4789c bytes 81620294
+ 00b478e0 bytes 84620294
- 00b478b4 ["INT_ADD", "register:40f0:8", ["const:b478b4:8", "const:4:8"]]
- 00b478b4 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b478f8 ["INT_ADD", "register:40f0:8", ["const:b478f8:8", "const:4:8"]]
+ 00b478f8 ["CALL", null, ["callee:00bdb190:8"]]
- 00b478b4 bytes 234e0294
+ 00b478f8 bytes 264e0294
- 00b478f0 ["INT_ADD", "register:40f0:8", ["const:b478f0:8", "const:4:8"]]
- 00b478f0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b47934 ["INT_ADD", "register:40f0:8", ["const:b47934:8", "const:4:8"]]
+ 00b47934 ["CALL", null, ["callee:00bdb040:8"]]
- 00b478f0 bytes c04d0294
+ 00b47934 bytes c34d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f87c392fa05e3eae30ccc7e89a2a1ad"></a>

### [`00b47978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47978.md) → [`00b479bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b479bc.md) _ZN11flatbuffers23ReadEnvironmentVariableEPKcPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdca00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca00.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47978.md#insn-00b47994) · [`00b479ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47978.md#insn-00b479ac) · [`00b479e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47978.md#insn-00b479e8)
- 新版 [`00b479d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b479bc.md#insn-00b479d8) · [`00b479f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b479bc.md#insn-00b479f0) · [`00b47a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b479bc.md#insn-00b47a2c)

~~~diff
- 00b47994 ["INT_ADD", "register:40f0:8", ["const:b47994:8", "const:4:8"]]
- 00b47994 ["CALL", null, ["callee:00bdca50:8"]]
+ 00b479d8 ["INT_ADD", "register:40f0:8", ["const:b479d8:8", "const:4:8"]]
+ 00b479d8 ["CALL", null, ["callee:00bdca50:8"]]
- 00b47994 bytes 1b540294
+ 00b479d8 bytes 1e540294
- 00b479ac ["INT_ADD", "register:40f0:8", ["const:b479ac:8", "const:4:8"]]
- 00b479ac ["CALL", null, ["callee:00bdb190:8"]]
+ 00b479f0 ["INT_ADD", "register:40f0:8", ["const:b479f0:8", "const:4:8"]]
+ 00b479f0 ["CALL", null, ["callee:00bdb190:8"]]
- 00b479ac bytes e54d0294
+ 00b479f0 bytes e84d0294
- 00b479e8 ["INT_ADD", "register:40f0:8", ["const:b479e8:8", "const:4:8"]]
- 00b479e8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b47a2c ["INT_ADD", "register:40f0:8", ["const:b47a2c:8", "const:4:8"]]
+ 00b47a2c ["CALL", null, ["callee:00bdb040:8"]]
- 00b479e8 bytes 824d0294
+ 00b47a2c bytes 854d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c56f0c9e28dcc8ba041deda1bc64572c"></a>

### [`00b47bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47bf4.md) → [`00b47c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47c38.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47bf4.md#insn-00b47c04)
- 新版 [`00b47c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47c38.md#insn-00b47c48)

~~~diff
- 00b47c04 ["INT_ADD", "register:40f0:8", ["const:b47c04:8", "const:4:8"]]
- 00b47c04 ["CALL", null, ["callee:00be02a0:8"]]
+ 00b47c48 ["INT_ADD", "register:40f0:8", ["const:b47c48:8", "const:4:8"]]
+ 00b47c48 ["CALL", null, ["callee:00be02a0:8"]]
- 00b47c04 bytes 93610294
+ 00b47c48 bytes 96610294
~~~


<a id="compare-fade5cb66f8c3950237d2ba734a403d5"></a>

### [`00b47d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47d08.md) → [`00b47d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE6setbufEPcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00b47b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b58.md) [`00b4890c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b4890c.md) [`00b887d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b887d8.md) [`00b88a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88a90.md) · 呼出先 2件 [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00bdef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md)
- 新版 呼出元 4件 [`00b47b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b9c.md) [`00b48950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48950.md) [`00b8881c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md) [`00b88ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md) · 呼出先 2件 [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00bdefa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47d08.md#insn-00b47d40) · [`00b47d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47d08.md#insn-00b47d54) · [`00b47da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47d08.md#insn-00b47da8)
- 新版 [`00b47d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md#insn-00b47d84) · [`00b47d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md#insn-00b47d98) · [`00b47dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md#insn-00b47dec)

~~~diff
- 00b47d40 ["INT_ADD", "register:40f0:8", ["const:b47d40:8", "const:4:8"]]
- 00b47d40 ["CALL", null, ["callee:00bdef90:8"]]
+ 00b47d84 ["INT_ADD", "register:40f0:8", ["const:b47d84:8", "const:4:8"]]
+ 00b47d84 ["CALL", null, ["callee:00bdef90:8"]]
- 00b47d40 bytes 805c0294
+ 00b47d84 bytes 835c0294
- 00b47d54 ["INT_ADD", "register:40f0:8", ["const:b47d54:8", "const:4:8"]]
- 00b47d54 ["CALL", null, ["callee:00bdef90:8"]]
+ 00b47d98 ["INT_ADD", "register:40f0:8", ["const:b47d98:8", "const:4:8"]]
+ 00b47d98 ["CALL", null, ["callee:00bdef90:8"]]
- 00b47d54 bytes 7b5c0294
+ 00b47d98 bytes 7e5c0294
- 00b47da8 ["INT_ADD", "register:40f0:8", ["const:b47da8:8", "const:4:8"]]
- 00b47da8 ["CALL", null, ["callee:00bdefa0:8"]]
+ 00b47dec ["INT_ADD", "register:40f0:8", ["const:b47dec:8", "const:4:8"]]
+ 00b47dec ["CALL", null, ["callee:00bdefa0:8"]]
- 00b47da8 bytes 6a5c0294
+ 00b47dec bytes 6d5c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d981de3bfd44bbb6c0f693282e74cf8"></a>

### [`00b47e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md) → [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekoffExNS_8ios_base7seekdirEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md) [`00be0280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0280.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b48678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md) [`00be02c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02c0.md) [`00be02d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md#insn-00b47e2c) · [`00b47e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md#insn-00b47e54) · [`00b47e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md#insn-00b47e84)
- 新版 [`00b47e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md#insn-00b47e70) · [`00b47e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md#insn-00b47e98) · [`00b47ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md#insn-00b47ec8)

~~~diff
- 00b47e2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47e2c ["INT_ADD", "register:40f0:8", ["const:b47e2c:8", "const:4:8"]]
- 00b47e2c ["CALLIND", null, ["register:0:8"]]
+ 00b47e70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47e70 ["INT_ADD", "register:40f0:8", ["const:b47e70:8", "const:4:8"]]
+ 00b47e70 ["CALLIND", null, ["register:0:8"]]
- 00b47e2c bytes 00013fd6
+ 00b47e70 bytes 00013fd6
- 00b47e54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47e54 ["INT_ADD", "register:40f0:8", ["const:b47e54:8", "const:4:8"]]
- 00b47e54 ["CALLIND", null, ["register:0:8"]]
+ 00b47e98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47e98 ["INT_ADD", "register:40f0:8", ["const:b47e98:8", "const:4:8"]]
+ 00b47e98 ["CALLIND", null, ["register:0:8"]]
- 00b47e54 bytes 00013fd6
+ 00b47e98 bytes 00013fd6
- 00b47e84 ["INT_ADD", "register:40f0:8", ["const:b47e84:8", "const:4:8"]]
- 00b47e84 ["CALL", null, ["callee:00be02c0:8"]]
+ 00b47ec8 ["INT_ADD", "register:40f0:8", ["const:b47ec8:8", "const:4:8"]]
+ 00b47ec8 ["CALL", null, ["callee:00be02c0:8"]]
- 00b47e84 bytes fb600294
+ 00b47ec8 bytes fe600294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dacc4719cf6f8a47689845fcb6bccfab"></a>

### [`00b47ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47ec0.md) → [`00b47f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f04.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekposENS_4fposI9mbstate_tEEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be02c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47ec0.md#insn-00b47eec) · [`00b47f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47ec0.md#insn-00b47f00)
- 新版 [`00b47f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f04.md#insn-00b47f30) · [`00b47f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f04.md#insn-00b47f44)

~~~diff
- 00b47eec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47eec ["INT_ADD", "register:40f0:8", ["const:b47eec:8", "const:4:8"]]
- 00b47eec ["CALLIND", null, ["register:0:8"]]
+ 00b47f30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47f30 ["INT_ADD", "register:40f0:8", ["const:b47f30:8", "const:4:8"]]
+ 00b47f30 ["CALLIND", null, ["register:0:8"]]
- 00b47eec bytes 00013fd6
+ 00b47f30 bytes 00013fd6
- 00b47f00 ["INT_ADD", "register:40f0:8", ["const:b47f00:8", "const:4:8"]]
- 00b47f00 ["CALL", null, ["callee:00be02c0:8"]]
+ 00b47f44 ["INT_ADD", "register:40f0:8", ["const:b47f44:8", "const:4:8"]]
+ 00b47f44 ["CALL", null, ["callee:00be02c0:8"]]
- 00b47f00 bytes dc600294
+ 00b47f44 bytes df600294
~~~


<a id="compare-f32195aa7afe68d9350e500d6bac1eae"></a>

### [`00b47f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md) → [`00b47f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0230.md) · 呼出先 5件 [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md) [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md)
- 新版 呼出元 1件 [`00be0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md) · 呼出先 5件 [`00b48678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md) [`00be02c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md#insn-00b47fb4) · [`00b47fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md#insn-00b47fe4) · [`00b48004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md#insn-00b48004)
- 新版 [`00b47ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md#insn-00b47ff8) · [`00b48028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md#insn-00b48028) · [`00b48048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md#insn-00b48048)

~~~diff
- 00b47fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47fb4 ["INT_ADD", "register:40f0:8", ["const:b47fb4:8", "const:4:8"]]
- 00b47fb4 ["CALLIND", null, ["register:0:8"]]
+ 00b47ff8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47ff8 ["INT_ADD", "register:40f0:8", ["const:b47ff8:8", "const:4:8"]]
+ 00b47ff8 ["CALLIND", null, ["register:0:8"]]
- 00b47fb4 bytes 00013fd6
+ 00b47ff8 bytes 00013fd6
- 00b47fe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47fe4 ["INT_ADD", "register:40f0:8", ["const:b47fe4:8", "const:4:8"]]
- 00b47fe4 ["CALLIND", null, ["register:0:8"]]
+ 00b48028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48028 ["INT_ADD", "register:40f0:8", ["const:b48028:8", "const:4:8"]]
+ 00b48028 ["CALLIND", null, ["register:0:8"]]
- 00b47fe4 bytes 00013fd6
+ 00b48028 bytes 00013fd6
- 00b48004 ["INT_ADD", "register:40f0:8", ["const:b48004:8", "const:4:8"]]
- 00b48004 ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b48048 ["INT_ADD", "register:40f0:8", ["const:b48048:8", "const:4:8"]]
+ 00b48048 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b48004 bytes df540294
+ 00b48048 bytes e2540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841d13ee3dabd3f3d82f609d79c1a85c"></a>

### [`00b48120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48120.md) → [`00b48164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48164.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE9underflowEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdd1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b48678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdd230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4821c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48120.md#insn-00b4821c) · [`00b48244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48120.md#insn-00b48244) · [`00b48274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48120.md#insn-00b48274)
- 新版 [`00b48260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48164.md#insn-00b48260) · [`00b48288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48164.md#insn-00b48288) · [`00b482b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48164.md#insn-00b482b8)

~~~diff
- 00b4821c ["INT_ADD", "register:40f0:8", ["const:b4821c:8", "const:4:8"]]
- 00b4821c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b48260 ["INT_ADD", "register:40f0:8", ["const:b48260:8", "const:4:8"]]
+ 00b48260 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b4821c bytes a14b0294
+ 00b48260 bytes a44b0294
- 00b48244 ["INT_ADD", "register:40f0:8", ["const:b48244:8", "const:4:8"]]
- 00b48244 ["CALL", null, ["callee:00bdd230:8"]]
+ 00b48288 ["INT_ADD", "register:40f0:8", ["const:b48288:8", "const:4:8"]]
+ 00b48288 ["CALL", null, ["callee:00bdd230:8"]]
- 00b48244 bytes e7530294
+ 00b48288 bytes ea530294
- 00b48274 ["INT_ADD", "register:40f0:8", ["const:b48274:8", "const:4:8"]]
- 00b48274 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b482b8 ["INT_ADD", "register:40f0:8", ["const:b482b8:8", "const:4:8"]]
+ 00b482b8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b48274 bytes 8b4b0294
+ 00b482b8 bytes 8e4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfe735aad45cdce3dd5569c26c051eeb"></a>

### [`00b483fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md) → [`00b48440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48440.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE8overflowEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b48678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b484f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md#insn-00b484f0) · [`00b48540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md#insn-00b48540) · [`00b48580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md#insn-00b48580)
- 新版 [`00b48534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48440.md#insn-00b48534) · [`00b48584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48440.md#insn-00b48584) · [`00b485c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48440.md#insn-00b485c4)

~~~diff
- 00b484f0 ["INT_ADD", "register:40f0:8", ["const:b484f0:8", "const:4:8"]]
- 00b484f0 ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b48534 ["INT_ADD", "register:40f0:8", ["const:b48534:8", "const:4:8"]]
+ 00b48534 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b484f0 bytes a4530294
+ 00b48534 bytes a7530294
- 00b48540 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48540 ["INT_ADD", "register:40f0:8", ["const:b48540:8", "const:4:8"]]
- 00b48540 ["CALLIND", null, ["register:0:8"]]
+ 00b48584 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48584 ["INT_ADD", "register:40f0:8", ["const:b48584:8", "const:4:8"]]
+ 00b48584 ["CALLIND", null, ["register:0:8"]]
- 00b48540 bytes 00013fd6
+ 00b48584 bytes 00013fd6
- 00b48580 ["INT_ADD", "register:40f0:8", ["const:b48580:8", "const:4:8"]]
- 00b48580 ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b485c4 ["INT_ADD", "register:40f0:8", ["const:b485c4:8", "const:4:8"]]
+ 00b485c4 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b48580 bytes 80530294
+ 00b485c4 bytes 83530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65a308287038dd66209203251d3a92bd"></a>

### [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) → [`00b48678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md) FUN_00b48678

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00b47e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md) [`00b47f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md) [`00b48120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48120.md) [`00b483fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md) · 呼出先 1件 [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 4件 [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md) [`00b47f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md) [`00b48164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48164.md) [`00b48440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48440.md) · 呼出先 1件 [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4863c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md#insn-00b4863c)
- 新版 [`00b48680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md#insn-00b48680)

~~~diff
- 00b4863c ["INT_ADD", "register:40f0:8", ["const:b4863c:8", "const:4:8"]]
- 00b4863c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00b48680 ["INT_ADD", "register:40f0:8", ["const:b48680:8", "const:4:8"]]
+ 00b48680 ["CALL", null, ["callee:00bde2c0:8"]]
- 00b4863c bytes 0d570294
+ 00b48680 bytes 10570294
~~~


<a id="compare-f9f35f36543818d2c391f353e978d63e"></a>

### [`00b486c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b486c4.md) → [`00b48708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48708.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b486d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b486c4.md#insn-00b486d8)
- 新版 [`00b4871c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48708.md#insn-00b4871c)

~~~diff
- 00b486d8 ["INT_ADD", "register:40f0:8", ["const:b486d8:8", "const:4:8"]]
- 00b486d8 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b4871c ["INT_ADD", "register:40f0:8", ["const:b4871c:8", "const:4:8"]]
+ 00b4871c ["CALL", null, ["callee:00be01e0:8"]]
- 00b486d8 bytes ae5e0294
+ 00b4871c bytes b15e0294
~~~


<a id="compare-8b86ac20c761ce287bbc2f30d6a66429"></a>

### [`00b48700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48700.md) → [`00b48744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48744.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4871c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48700.md#insn-00b4871c)
- 新版 [`00b48760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48744.md#insn-00b48760)

~~~diff
- 00b4871c ["INT_ADD", "register:40f0:8", ["const:b4871c:8", "const:4:8"]]
- 00b4871c ["CALL", null, ["callee:00be01e0:8"]]
+ 00b48760 ["INT_ADD", "register:40f0:8", ["const:b48760:8", "const:4:8"]]
+ 00b48760 ["CALL", null, ["callee:00be01e0:8"]]
- 00b4871c bytes 9d5e0294
+ 00b48760 bytes a05e0294
~~~


<a id="compare-ac6c1c1132747abbb2ff202430aed9da"></a>

### [`00b48b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b50.md) → [`00b48b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48b94.md) FUN_00b48b94

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b4aa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aa58.md) · 呼出先 2件 [`00bddc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc30.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00b4aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aa9c.md) · 呼出先 2件 [`00bddc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc80.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b48b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b50.md#insn-00b48b60)
- 新版 [`00b48ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48b94.md#insn-00b48ba4)

~~~diff
- 00b48b60 ["INT_ADD", "register:40f0:8", ["const:b48b60:8", "const:4:8"]]
- 00b48b60 ["CALL", null, ["callee:00bdde00:8"]]
+ 00b48ba4 ["INT_ADD", "register:40f0:8", ["const:b48ba4:8", "const:4:8"]]
+ 00b48ba4 ["CALL", null, ["callee:00bdde00:8"]]
- 00b48b60 bytes 94540294
+ 00b48ba4 bytes 97540294
~~~


<a id="compare-0e37ab8ac30ba2c3f13df6d4002b06ce"></a>

### [`00b48b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b90.md) → [`00b48bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md) FUN_00b48bd4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b4aa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aa58.md) · 呼出先 2件 [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md) [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md)
- 新版 呼出元 1件 [`00b4aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aa9c.md) · 呼出先 2件 [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md) [`00be0470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b48ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b90.md#insn-00b48ba0)
- 新版 [`00b48be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md#insn-00b48be4)

~~~diff
- 00b48ba0 ["INT_ADD", "register:40f0:8", ["const:b48ba0:8", "const:4:8"]]
- 00b48ba0 ["CALL", null, ["callee:00bdde00:8"]]
+ 00b48be4 ["INT_ADD", "register:40f0:8", ["const:b48be4:8", "const:4:8"]]
+ 00b48be4 ["CALL", null, ["callee:00bdde00:8"]]
- 00b48ba0 bytes 84540294
+ 00b48be4 bytes 87540294
~~~


<a id="compare-fd9ba51f0e16f4ebe92b24b0f2500216"></a>

### [`00b48c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md) → [`00b48c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c48.md) _ZN8firebase9messaging8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0410.md) · 呼出先 5件 [`00bddd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd20.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md) [`00be03f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03f0.md)
- 新版 呼出元 1件 [`00be0460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0460.md) · 呼出先 5件 [`00bddd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd70.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md) [`00be0440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0440.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b48c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md#insn-00b48c14) · [`00b48c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md#insn-00b48c1c) · [`00b48c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md#insn-00b48c24)
- 新版 [`00b48c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c48.md#insn-00b48c58) · [`00b48c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c48.md#insn-00b48c60) · [`00b48c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c48.md#insn-00b48c68)

~~~diff
- 00b48c14 ["INT_ADD", "register:40f0:8", ["const:b48c14:8", "const:4:8"]]
- 00b48c14 ["CALL", null, ["callee:00bddd70:8"]]
+ 00b48c58 ["INT_ADD", "register:40f0:8", ["const:b48c58:8", "const:4:8"]]
+ 00b48c58 ["CALL", null, ["callee:00bddd70:8"]]
- 00b48c14 bytes 43540294
+ 00b48c58 bytes 46540294
- 00b48c1c ["INT_ADD", "register:40f0:8", ["const:b48c1c:8", "const:4:8"]]
- 00b48c1c ["CALL", null, ["callee:00be0440:8"]]
+ 00b48c60 ["INT_ADD", "register:40f0:8", ["const:b48c60:8", "const:4:8"]]
+ 00b48c60 ["CALL", null, ["callee:00be0440:8"]]
- 00b48c1c bytes f55d0294
+ 00b48c60 bytes f85d0294
- 00b48c24 ["INT_ADD", "register:40f0:8", ["const:b48c24:8", "const:4:8"]]
- 00b48c24 ["CALL", null, ["callee:00bdde00:8"]]
+ 00b48c68 ["INT_ADD", "register:40f0:8", ["const:b48c68:8", "const:4:8"]]
+ 00b48c68 ["CALL", null, ["callee:00bdde00:8"]]
- 00b48c24 bytes 63540294
+ 00b48c68 bytes 66540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2154002da2ae3541eae35dadde2ef94"></a>

### [`00b49074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49074.md) → [`00b490b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490b8.md) _ZN8firebase9messaging16PollableListenerD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49074.md#insn-00b49084)
- 新版 [`00b490c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490b8.md#insn-00b490c8)

~~~diff
- 00b49084 ["INT_ADD", "register:40f0:8", ["const:b49084:8", "const:4:8"]]
- 00b49084 ["CALL", null, ["callee:00be0380:8"]]
+ 00b490c8 ["INT_ADD", "register:40f0:8", ["const:b490c8:8", "const:4:8"]]
+ 00b490c8 ["CALL", null, ["callee:00be0380:8"]]
- 00b49084 bytes ab5c0294
+ 00b490c8 bytes ae5c0294
~~~


<a id="compare-2392d8f2efe472ef37e012bea21245eb"></a>

### [`00b490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md) → [`00b490e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md) _ZN8firebase9messaging20PollableListenerImpl9OnMessageERKNS0_7MessageE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0380.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be03c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03c0.md) [`00be03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md)
- 新版 呼出元 1件 [`00be03d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03d0.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0410.md) [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b490c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md#insn-00b490c8) · [`00b490d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md#insn-00b490d0) · [`00b490fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md#insn-00b490fc)
- 新版 [`00b4910c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md#insn-00b4910c) · [`00b49114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md#insn-00b49114) · [`00b49140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md#insn-00b49140)

~~~diff
- 00b490c8 ["INT_ADD", "register:40f0:8", ["const:b490c8:8", "const:4:8"]]
- 00b490c8 ["CALL", null, ["callee:00be0410:8"]]
+ 00b4910c ["INT_ADD", "register:40f0:8", ["const:b4910c:8", "const:4:8"]]
+ 00b4910c ["CALL", null, ["callee:00be0410:8"]]
- 00b490c8 bytes be5c0294
+ 00b4910c bytes c15c0294
- 00b490d0 ["INT_ADD", "register:40f0:8", ["const:b490d0:8", "const:4:8"]]
- 00b490d0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b49114 ["INT_ADD", "register:40f0:8", ["const:b49114:8", "const:4:8"]]
+ 00b49114 ["CALL", null, ["callee:00bddc20:8"]]
- 00b490d0 bytes c0520294
+ 00b49114 bytes c3520294
- 00b490fc ["INT_ADD", "register:40f0:8", ["const:b490fc:8", "const:4:8"]]
- 00b490fc ["CALL", null, ["callee:00be04e0:8"]]
+ 00b49140 ["INT_ADD", "register:40f0:8", ["const:b49140:8", "const:4:8"]]
+ 00b49140 ["CALL", null, ["callee:00be04e0:8"]]
- 00b490fc bytes e55c0294
+ 00b49140 bytes e85c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0801b36bf760b8b0fab1ea917ff14195"></a>

### [`00b491b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b491b4.md) → [`00b491f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b491f8.md) _ZN8firebase9messaging20PollableListenerImpl15OnTokenReceivedEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0360.md) · 呼出先 4件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 1件 [`00be03b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03b0.md) · 呼出先 4件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b491cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b491b4.md#insn-00b491cc) · [`00b491d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b491b4.md#insn-00b491d8) · [`00b491e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b491b4.md#insn-00b491e8)
- 新版 [`00b49210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b491f8.md#insn-00b49210) · [`00b4921c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b491f8.md#insn-00b4921c) · [`00b4922c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b491f8.md#insn-00b4922c)

~~~diff
- 00b491cc ["INT_ADD", "register:40f0:8", ["const:b491cc:8", "const:4:8"]]
- 00b491cc ["CALL", null, ["callee:00bddc20:8"]]
+ 00b49210 ["INT_ADD", "register:40f0:8", ["const:b49210:8", "const:4:8"]]
+ 00b49210 ["CALL", null, ["callee:00bddc20:8"]]
- 00b491cc bytes 81520294
+ 00b49210 bytes 84520294
- 00b491d8 ["INT_ADD", "register:40f0:8", ["const:b491d8:8", "const:4:8"]]
- 00b491d8 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b4921c ["INT_ADD", "register:40f0:8", ["const:b4921c:8", "const:4:8"]]
+ 00b4921c ["CALL", null, ["callee:00bdb190:8"]]
- 00b491d8 bytes da470294
+ 00b4921c bytes dd470294
- 00b491e8 ["INT_ADD", "register:40f0:8", ["const:b491e8:8", "const:4:8"]]
- 00b491e8 ["CALL", null, ["callee:00bde230:8"]]
+ 00b4922c ["INT_ADD", "register:40f0:8", ["const:b4922c:8", "const:4:8"]]
+ 00b4922c ["CALL", null, ["callee:00bde230:8"]]
- 00b491e8 bytes fe530294
+ 00b4922c bytes 01540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9226245556b269cade480da8be931c7"></a>

### [`00b49228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49228.md) → [`00b4926c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md) _ZN8firebase9messaging20PollableListenerImpl11PollMessageEPNS0_7MessageE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0350.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md) [`00be03e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03e0.md)
- 新版 呼出元 1件 [`00be03a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03a0.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md) [`00be0430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4923c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49228.md#insn-00b4923c) · [`00b4926c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49228.md#insn-00b4926c) · [`00b49290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49228.md#insn-00b49290)
- 新版 [`00b49280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md#insn-00b49280) · [`00b492b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md#insn-00b492b0) · [`00b492d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md#insn-00b492d4)

~~~diff
- 00b4923c ["INT_ADD", "register:40f0:8", ["const:b4923c:8", "const:4:8"]]
- 00b4923c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b49280 ["INT_ADD", "register:40f0:8", ["const:b49280:8", "const:4:8"]]
+ 00b49280 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4923c bytes 65520294
+ 00b49280 bytes 68520294
- 00b4926c ["INT_ADD", "register:40f0:8", ["const:b4926c:8", "const:4:8"]]
- 00b4926c ["CALL", null, ["callee:00be0430:8"]]
+ 00b492b0 ["INT_ADD", "register:40f0:8", ["const:b492b0:8", "const:4:8"]]
+ 00b492b0 ["CALL", null, ["callee:00be0430:8"]]
- 00b4926c bytes 5d5c0294
+ 00b492b0 bytes 605c0294
- 00b49290 ["INT_ADD", "register:40f0:8", ["const:b49290:8", "const:4:8"]]
- 00b49290 ["CALL", null, ["callee:00be0420:8"]]
+ 00b492d4 ["INT_ADD", "register:40f0:8", ["const:b492d4:8", "const:4:8"]]
+ 00b492d4 ["CALL", null, ["callee:00be0420:8"]]
- 00b49290 bytes 505c0294
+ 00b492d4 bytes 535c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30ed134aa8441c21a173f7a91a2ca61"></a>

### [`00b49318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49318.md) → [`00b4935c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4935c.md) _ZN8firebase9messaging16PollableListener21PollRegistrationTokenEPb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0370.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be03c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4933c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49318.md#insn-00b4933c)
- 新版 [`00b49380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4935c.md#insn-00b49380)

~~~diff
- 00b4933c ["INT_ADD", "register:40f0:8", ["const:b4933c:8", "const:4:8"]]
- 00b4933c ["CALL", null, ["callee:00be03c0:8"]]
+ 00b49380 ["INT_ADD", "register:40f0:8", ["const:b49380:8", "const:4:8"]]
+ 00b49380 ["CALL", null, ["callee:00be03c0:8"]]
- 00b4933c bytes 0d5c0294
+ 00b49380 bytes 105c0294
~~~


<a id="compare-059216ba0c0ac4497edcf69c13b2bb9d"></a>

### [`00b49370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49370.md) → [`00b493b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b493b4.md) _ZN8firebase9messaging20PollableListenerImpl21PollRegistrationTokenEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0370.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 1件 [`00be03c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03c0.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49370.md#insn-00b49388) · [`00b493c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49370.md#insn-00b493c0) · [`00b493f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49370.md#insn-00b493f8)
- 新版 [`00b493cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b493b4.md#insn-00b493cc) · [`00b49404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b493b4.md#insn-00b49404) · [`00b4943c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b493b4.md#insn-00b4943c)

~~~diff
- 00b49388 ["INT_ADD", "register:40f0:8", ["const:b49388:8", "const:4:8"]]
- 00b49388 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b493cc ["INT_ADD", "register:40f0:8", ["const:b493cc:8", "const:4:8"]]
+ 00b493cc ["CALL", null, ["callee:00bddc20:8"]]
- 00b49388 bytes 12520294
+ 00b493cc bytes 15520294
- 00b493c0 ["INT_ADD", "register:40f0:8", ["const:b493c0:8", "const:4:8"]]
- 00b493c0 ["CALL", null, ["callee:00bde230:8"]]
+ 00b49404 ["INT_ADD", "register:40f0:8", ["const:b49404:8", "const:4:8"]]
+ 00b49404 ["CALL", null, ["callee:00bde230:8"]]
- 00b493c0 bytes 88530294
+ 00b49404 bytes 8b530294
- 00b493f8 ["INT_ADD", "register:40f0:8", ["const:b493f8:8", "const:4:8"]]
- 00b493f8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b4943c ["INT_ADD", "register:40f0:8", ["const:b4943c:8", "const:4:8"]]
+ 00b4943c ["CALL", null, ["callee:00bddc30:8"]]
- 00b493f8 bytes fa510294
+ 00b4943c bytes fd510294
~~~


<a id="compare-0af55d386eee355de647231031edd38f"></a>

### [`00b494c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494c8.md) → [`00b4950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4950c.md) FUN_00b4950c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b48bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48bc4.md) · 呼出先 3件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00be03f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03f0.md) [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md)
- 新版 呼出元 1件 [`00b48c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c08.md) · 呼出先 3件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00be0440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0440.md) [`00be0470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b494d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494c8.md#insn-00b494d8) · [`00b494dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494c8.md#insn-00b494dc)
- 新版 [`00b4951c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4950c.md#insn-00b4951c) · [`00b49520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4950c.md#insn-00b49520)

~~~diff
- 00b494d8 ["INT_ADD", "register:40f0:8", ["const:b494d8:8", "const:4:8"]]
- 00b494d8 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b4951c ["INT_ADD", "register:40f0:8", ["const:b4951c:8", "const:4:8"]]
+ 00b4951c ["CALL", null, ["callee:00bdde40:8"]]
- 00b494d8 bytes 46520294
+ 00b4951c bytes 49520294
- 00b494dc ["INT_ADD", "register:40f0:8", ["const:b494dc:8", "const:4:8"]]
- 00b494dc ["CALL", null, ["callee:00be0440:8"]]
+ 00b49520 ["INT_ADD", "register:40f0:8", ["const:b49520:8", "const:4:8"]]
+ 00b49520 ["CALL", null, ["callee:00be0440:8"]]
- 00b494dc bytes c55b0294
+ 00b49520 bytes c85b0294
~~~


<a id="compare-b9fc5dc534d0051dc6fa1855a38a9e5f"></a>

### [`00b494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494f4.md) → [`00b49538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49538.md) _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0440.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md)
- 新版 呼出元 1件 [`00be0490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0490.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494f4.md#insn-00b49574) · [`00b495b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494f4.md#insn-00b495b8)
- 新版 [`00b495b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49538.md#insn-00b495b8) · [`00b495fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49538.md#insn-00b495fc)

~~~diff
- 00b49574 ["INT_ADD", "register:40f0:8", ["const:b49574:8", "const:4:8"]]
- 00b49574 ["CALL", null, ["callee:00be0420:8"]]
+ 00b495b8 ["INT_ADD", "register:40f0:8", ["const:b495b8:8", "const:4:8"]]
+ 00b495b8 ["CALL", null, ["callee:00be0420:8"]]
- 00b49574 bytes 975b0294
+ 00b495b8 bytes 9a5b0294
- 00b495b8 ["INT_ADD", "register:40f0:8", ["const:b495b8:8", "const:4:8"]]
- 00b495b8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b495fc ["INT_ADD", "register:40f0:8", ["const:b495fc:8", "const:4:8"]]
+ 00b495fc ["CALL", null, ["callee:00bdb060:8"]]
- 00b495b8 bytes 96460294
+ 00b495fc bytes 99460294
~~~


<a id="compare-30e6f68e26797be077cb7becd58db03e"></a>

### [`00b4960c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4960c.md) → [`00b49650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md) _ZN8firebase9messaging7MessageD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md) · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0310.md)
- 新版 呼出元 1件 [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md) · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4960c.md#insn-00b49628) · [`00b49630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4960c.md#insn-00b49630) · [`00b49678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4960c.md#insn-00b49678)
- 新版 [`00b4966c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md#insn-00b4966c) · [`00b49674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md#insn-00b49674) · [`00b496bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md#insn-00b496bc)

~~~diff
- 00b49628 ["INT_ADD", "register:40f0:8", ["const:b49628:8", "const:4:8"]]
- 00b49628 ["CALL", null, ["callee:00be0360:8"]]
+ 00b4966c ["INT_ADD", "register:40f0:8", ["const:b4966c:8", "const:4:8"]]
+ 00b4966c ["CALL", null, ["callee:00be0360:8"]]
- 00b49628 bytes 3a5b0294
+ 00b4966c bytes 3d5b0294
- 00b49630 ["INT_ADD", "register:40f0:8", ["const:b49630:8", "const:4:8"]]
- 00b49630 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b49674 ["INT_ADD", "register:40f0:8", ["const:b49674:8", "const:4:8"]]
+ 00b49674 ["CALL", null, ["callee:00bdb060:8"]]
- 00b49630 bytes 78460294
+ 00b49674 bytes 7b460294
- 00b49678 ["INT_ADD", "register:40f0:8", ["const:b49678:8", "const:4:8"]]
- 00b49678 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b496bc ["INT_ADD", "register:40f0:8", ["const:b496bc:8", "const:4:8"]]
+ 00b496bc ["CALL", null, ["callee:00bdb060:8"]]
- 00b49678 bytes 66460294
+ 00b496bc bytes 69460294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bfffef875ced95847e44700cd81fc65"></a>

### [`00b49750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49750.md) → [`00b49794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49794.md) _ZN8firebase9messaging12NotificationD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0310.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be0360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0360.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49750.md#insn-00b49778) · [`00b49780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49750.md#insn-00b49780) · [`00b497bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49750.md#insn-00b497bc)
- 新版 [`00b497bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49794.md#insn-00b497bc) · [`00b497c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49794.md#insn-00b497c4) · [`00b49800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49794.md#insn-00b49800)

~~~diff
- 00b49778 ["INT_ADD", "register:40f0:8", ["const:b49778:8", "const:4:8"]]
- 00b49778 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b497bc ["INT_ADD", "register:40f0:8", ["const:b497bc:8", "const:4:8"]]
+ 00b497bc ["CALL", null, ["callee:00bdb060:8"]]
- 00b49778 bytes 26460294
+ 00b497bc bytes 29460294
- 00b49780 ["INT_ADD", "register:40f0:8", ["const:b49780:8", "const:4:8"]]
- 00b49780 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b497c4 ["INT_ADD", "register:40f0:8", ["const:b497c4:8", "const:4:8"]]
+ 00b497c4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b49780 bytes 24460294
+ 00b497c4 bytes 27460294
- 00b497bc ["INT_ADD", "register:40f0:8", ["const:b497bc:8", "const:4:8"]]
- 00b497bc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b49800 ["INT_ADD", "register:40f0:8", ["const:b49800:8", "const:4:8"]]
+ 00b49800 ["CALL", null, ["callee:00bdb060:8"]]
- 00b497bc bytes 15460294
+ 00b49800 bytes 18460294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18d977dd64946521ba0cf649b45472fe"></a>

### [`00b49928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49928.md) → [`00b4996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4996c.md) _ZN8firebase9messaging7MessageC2ERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be03c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03c0.md) · 呼出先 1件 [`00be03e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03e0.md)
- 新版 呼出元 1件 [`00be0410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0410.md) · 呼出先 1件 [`00be0430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49928.md#insn-00b49998)
- 新版 [`00b499dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4996c.md#insn-00b499dc)

~~~diff
- 00b49998 ["INT_ADD", "register:40f0:8", ["const:b49998:8", "const:4:8"]]
- 00b49998 ["CALL", null, ["callee:00be0430:8"]]
+ 00b499dc ["INT_ADD", "register:40f0:8", ["const:b499dc:8", "const:4:8"]]
+ 00b499dc ["CALL", null, ["callee:00be0430:8"]]
- 00b49998 bytes 925a0294
+ 00b499dc bytes 955a0294
~~~


<a id="compare-dc25a7b300438d3923c0fdf0589f691c"></a>

### [`00b49acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49acc.md) → [`00b49b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md) _ZN8firebase9messaging7MessageaSERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be03e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03e0.md) · 呼出先 7件 [`005188a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005188a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0300.md)
- 新版 呼出元 1件 [`00be0430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0430.md) · 呼出先 7件 [`005188a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005188a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00be0350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49acc.md#insn-00b49b08) · [`00b49b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49acc.md#insn-00b49b2c) · [`00b49b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49acc.md#insn-00b49b50)
- 新版 [`00b49b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md#insn-00b49b4c) · [`00b49b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md#insn-00b49b70) · [`00b49b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md#insn-00b49b94)

~~~diff
- 00b49b08 ["INT_ADD", "register:40f0:8", ["const:b49b08:8", "const:4:8"]]
- 00b49b08 ["CALL", null, ["callee:00bde230:8"]]
+ 00b49b4c ["INT_ADD", "register:40f0:8", ["const:b49b4c:8", "const:4:8"]]
+ 00b49b4c ["CALL", null, ["callee:00bde230:8"]]
- 00b49b08 bytes b6510294
+ 00b49b4c bytes b9510294
- 00b49b2c ["INT_ADD", "register:40f0:8", ["const:b49b2c:8", "const:4:8"]]
- 00b49b2c ["CALL", null, ["callee:00bde230:8"]]
+ 00b49b70 ["INT_ADD", "register:40f0:8", ["const:b49b70:8", "const:4:8"]]
+ 00b49b70 ["CALL", null, ["callee:00bde230:8"]]
- 00b49b2c bytes ad510294
+ 00b49b70 bytes b0510294
- 00b49b50 ["INT_ADD", "register:40f0:8", ["const:b49b50:8", "const:4:8"]]
- 00b49b50 ["CALL", null, ["callee:00bde230:8"]]
+ 00b49b94 ["INT_ADD", "register:40f0:8", ["const:b49b94:8", "const:4:8"]]
+ 00b49b94 ["CALL", null, ["callee:00bde230:8"]]
- 00b49b50 bytes a4510294
+ 00b49b94 bytes a7510294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8084154ec814017c543669c8cc24024"></a>

### [`00b49cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49cfc.md) → [`00b49d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49d40.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0300.md) · 呼出先 1件 [`00be0320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0320.md)
- 新版 呼出元 1件 [`00be0350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md) · 呼出先 1件 [`00be0370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49cfc.md#insn-00b49d3c)
- 新版 [`00b49d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49d40.md#insn-00b49d80)

~~~diff
- 00b49d3c ["INT_ADD", "register:40f0:8", ["const:b49d3c:8", "const:4:8"]]
- 00b49d3c ["CALL", null, ["callee:00be0370:8"]]
+ 00b49d80 ["INT_ADD", "register:40f0:8", ["const:b49d80:8", "const:4:8"]]
+ 00b49d80 ["CALL", null, ["callee:00be0370:8"]]
- 00b49d3c bytes 79590294
+ 00b49d80 bytes 7c590294
~~~


<a id="compare-6c7133fc048ab3e4b450308345d46f37"></a>

### [`00b49eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49eec.md) → [`00b49f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be04a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04a0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04f0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49eec.md#insn-00b49f30) · [`00b49f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49eec.md#insn-00b49f8c) · [`00b49fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49eec.md#insn-00b49fb4)
- 新版 [`00b49f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md#insn-00b49f74) · [`00b49fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md#insn-00b49fd0) · [`00b49ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md#insn-00b49ff8)

~~~diff
- 00b49f30 ["INT_ADD", "register:40f0:8", ["const:b49f30:8", "const:4:8"]]
- 00b49f30 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b49f74 ["INT_ADD", "register:40f0:8", ["const:b49f74:8", "const:4:8"]]
+ 00b49f74 ["CALL", null, ["callee:00bdb060:8"]]
- 00b49f30 bytes 38440294
+ 00b49f74 bytes 3b440294
- 00b49f8c ["INT_ADD", "register:40f0:8", ["const:b49f8c:8", "const:4:8"]]
- 00b49f8c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b49fd0 ["INT_ADD", "register:40f0:8", ["const:b49fd0:8", "const:4:8"]]
+ 00b49fd0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b49f8c bytes 45440294
+ 00b49fd0 bytes 48440294
- 00b49fb4 ["INT_ADD", "register:40f0:8", ["const:b49fb4:8", "const:4:8"]]
- 00b49fb4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b49ff8 ["INT_ADD", "register:40f0:8", ["const:b49ff8:8", "const:4:8"]]
+ 00b49ff8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b49fb4 bytes 6b440294
+ 00b49ff8 bytes 6e440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c5b99332b5fcc6877c36aaeaa4fb180"></a>

### [`00b4a01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a01c.md) → [`00b4a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md) _ZN8firebase9messaging12NotificationaSERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0320.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) [`00be0040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0040.md)
- 新版 呼出元 1件 [`00be0370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0370.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00be0090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4a058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a01c.md#insn-00b4a058) · [`00b4a07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a01c.md#insn-00b4a07c) · [`00b4a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a01c.md#insn-00b4a0a0)
- 新版 [`00b4a09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md#insn-00b4a09c) · [`00b4a0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md#insn-00b4a0c0) · [`00b4a0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md#insn-00b4a0e4)

~~~diff
- 00b4a058 ["INT_ADD", "register:40f0:8", ["const:b4a058:8", "const:4:8"]]
- 00b4a058 ["CALL", null, ["callee:00bde230:8"]]
+ 00b4a09c ["INT_ADD", "register:40f0:8", ["const:b4a09c:8", "const:4:8"]]
+ 00b4a09c ["CALL", null, ["callee:00bde230:8"]]
- 00b4a058 bytes 62500294
+ 00b4a09c bytes 65500294
- 00b4a07c ["INT_ADD", "register:40f0:8", ["const:b4a07c:8", "const:4:8"]]
- 00b4a07c ["CALL", null, ["callee:00bde230:8"]]
+ 00b4a0c0 ["INT_ADD", "register:40f0:8", ["const:b4a0c0:8", "const:4:8"]]
+ 00b4a0c0 ["CALL", null, ["callee:00bde230:8"]]
- 00b4a07c bytes 59500294
+ 00b4a0c0 bytes 5c500294
- 00b4a0a0 ["INT_ADD", "register:40f0:8", ["const:b4a0a0:8", "const:4:8"]]
- 00b4a0a0 ["CALL", null, ["callee:00bde230:8"]]
+ 00b4a0e4 ["INT_ADD", "register:40f0:8", ["const:b4a0e4:8", "const:4:8"]]
+ 00b4a0e4 ["CALL", null, ["callee:00bde230:8"]]
- 00b4a0a0 bytes 50500294
+ 00b4a0e4 bytes 53500294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56c9aabf2e81882594a7d52eb08014aa"></a>

### [`00b4b4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b4a8.md) → [`00b4b4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b4ec.md) _ZN8firebase9messaging10FileLockerC2EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0550.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be05a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be05a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4b4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b4a8.md#insn-00b4b4c8)
- 新版 [`00b4b50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b4ec.md#insn-00b4b50c)

~~~diff
- 00b4b4c8 ["INT_ADD", "register:40f0:8", ["const:b4b4c8:8", "const:4:8"]]
- 00b4b4c8 ["CALL", null, ["callee:00be05a0:8"]]
+ 00b4b50c ["INT_ADD", "register:40f0:8", ["const:b4b50c:8", "const:4:8"]]
+ 00b4b50c ["CALL", null, ["callee:00be05a0:8"]]
- 00b4b4c8 bytes 22540294
+ 00b4b50c bytes 25540294
~~~


<a id="compare-943d1277ac2d890f06cd36dbb7f31db8"></a>

### [`00b4eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md) → [`00b4eb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4eb58.md) FUN_00b4eb58

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b4d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md) [`00b4da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md)
- 新版 呼出元 2件 [`00b4d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d518.md) [`00b4dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4dabc.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bdee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4eb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md#insn-00b4eb4c) · [`00b4eb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md#insn-00b4eb5c) · [`00b4eb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md#insn-00b4eb74)
- 新版 [`00b4eb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4eb58.md#insn-00b4eb90) · [`00b4eba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4eb58.md#insn-00b4eba0) · [`00b4ebb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4eb58.md#insn-00b4ebb8)

~~~diff
- 00b4eb4c ["INT_ADD", "register:40f0:8", ["const:b4eb4c:8", "const:4:8"]]
- 00b4eb4c ["CALL", null, ["callee:00be0300:8"]]
+ 00b4eb90 ["INT_ADD", "register:40f0:8", ["const:b4eb90:8", "const:4:8"]]
+ 00b4eb90 ["CALL", null, ["callee:00be0300:8"]]
- 00b4eb4c bytes d9450294
+ 00b4eb90 bytes dc450294
- 00b4eb5c ["INT_ADD", "register:40f0:8", ["const:b4eb5c:8", "const:4:8"]]
- 00b4eb5c ["CALL", null, ["callee:00bddf80:8"]]
+ 00b4eba0 ["INT_ADD", "register:40f0:8", ["const:b4eba0:8", "const:4:8"]]
+ 00b4eba0 ["CALL", null, ["callee:00bddf80:8"]]
- 00b4eb5c bytes f53c0294
+ 00b4eba0 bytes f83c0294
- 00b4eb74 ["INT_ADD", "register:40f0:8", ["const:b4eb74:8", "const:4:8"]]
- 00b4eb74 ["CALL", null, ["callee:00bdee00:8"]]
+ 00b4ebb8 ["INT_ADD", "register:40f0:8", ["const:b4ebb8:8", "const:4:8"]]
+ 00b4ebb8 ["CALL", null, ["callee:00bdee00:8"]]
- 00b4eb74 bytes 8f400294
+ 00b4ebb8 bytes 92400294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-499bf0de4430f98659a90266d0db5981"></a>

### [`00b4ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ebd0.md) → [`00b4ec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ec14.md) _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0540.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00be0590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0590.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4ebf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ebd0.md#insn-00b4ebf0) · [`00b4ec04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ebd0.md#insn-00b4ec04) · [`00b4ec18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ebd0.md#insn-00b4ec18)
- 新版 [`00b4ec34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ec14.md#insn-00b4ec34) · [`00b4ec48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ec14.md#insn-00b4ec48) · [`00b4ec5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ec14.md#insn-00b4ec5c)

~~~diff
- 00b4ebf0 ["INT_ADD", "register:40f0:8", ["const:b4ebf0:8", "const:4:8"]]
- 00b4ebf0 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b4ec34 ["INT_ADD", "register:40f0:8", ["const:b4ec34:8", "const:4:8"]]
+ 00b4ec34 ["CALL", null, ["callee:00bdde10:8"]]
- 00b4ebf0 bytes 743c0294
+ 00b4ec34 bytes 773c0294
- 00b4ec04 ["INT_ADD", "register:40f0:8", ["const:b4ec04:8", "const:4:8"]]
- 00b4ec04 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b4ec48 ["INT_ADD", "register:40f0:8", ["const:b4ec48:8", "const:4:8"]]
+ 00b4ec48 ["CALL", null, ["callee:00bddf80:8"]]
- 00b4ec04 bytes cb3c0294
+ 00b4ec48 bytes ce3c0294
- 00b4ec18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ec18 ["INT_ADD", "register:40f0:8", ["const:b4ec18:8", "const:4:8"]]
- 00b4ec18 ["CALLIND", null, ["register:0:8"]]
+ 00b4ec5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ec5c ["INT_ADD", "register:40f0:8", ["const:b4ec5c:8", "const:4:8"]]
+ 00b4ec5c ["CALLIND", null, ["register:0:8"]]
- 00b4ec18 bytes 00013fd6
+ 00b4ec5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e75d771b023750481b6d1665b1537c8"></a>

### [`00b4ec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ec70.md) → [`00b4ecb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ecb4.md) _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be05a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05a0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) [`00bded50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded50.md)
- 新版 呼出元 1件 [`00be05f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be05f0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md) [`00bdeda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeda0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4ecf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ec70.md#insn-00b4ecf8) · [`00b4ed28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ec70.md#insn-00b4ed28) · [`00b4ed6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ec70.md#insn-00b4ed6c)
- 新版 [`00b4ed3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ecb4.md#insn-00b4ed3c) · [`00b4ed6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ecb4.md#insn-00b4ed6c) · [`00b4edb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ecb4.md#insn-00b4edb0)

~~~diff
- 00b4ecf8 ["INT_ADD", "register:40f0:8", ["const:b4ecf8:8", "const:4:8"]]
- 00b4ecf8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4ed3c ["INT_ADD", "register:40f0:8", ["const:b4ed3c:8", "const:4:8"]]
+ 00b4ed3c ["CALL", null, ["callee:00bdb040:8"]]
- 00b4ecf8 bytes be300294
+ 00b4ed3c bytes c1300294
- 00b4ed28 ["INT_ADD", "register:40f0:8", ["const:b4ed28:8", "const:4:8"]]
- 00b4ed28 ["CALL", null, ["callee:00bdeda0:8"]]
+ 00b4ed6c ["INT_ADD", "register:40f0:8", ["const:b4ed6c:8", "const:4:8"]]
+ 00b4ed6c ["CALL", null, ["callee:00bdeda0:8"]]
- 00b4ed28 bytes 0a400294
+ 00b4ed6c bytes 0d400294
- 00b4ed6c ["INT_ADD", "register:40f0:8", ["const:b4ed6c:8", "const:4:8"]]
- 00b4ed6c ["CALL", null, ["callee:00bdeda0:8"]]
+ 00b4edb0 ["INT_ADD", "register:40f0:8", ["const:b4edb0:8", "const:4:8"]]
+ 00b4edb0 ["CALL", null, ["callee:00bdeda0:8"]]
- 00b4ed6c bytes f93f0294
+ 00b4edb0 bytes fc3f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

