# v16.0.0 → v16.0.1 · 要調査の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-15b24f842ae217454a40b2f846834a58"></a>

### [`00bc0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md) → [`00bc10a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d160.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d560.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc0d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md#insn-00bc0d18) · [`00bc0e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md#insn-00bc0e04) · [`00bc0e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0c7c.md#insn-00bc0e40)
- 新版 [`00bc1140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md#insn-00bc1140) · [`00bc122c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md#insn-00bc122c) · [`00bc1268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc10a4.md#insn-00bc1268)

~~~diff
- 00bc0d18 ["INT_ADD", "register:40f0:8", ["const:bc0d18:8", "const:4:8"]]
- 00bc0d18 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bc1140 ["INT_ADD", "register:40f0:8", ["const:bc1140:8", "const:4:8"]]
+ 00bc1140 ["CALL", null, ["callee:00c57e90:8"]]
- 00bc0d18 bytes 5e5b0294
+ 00bc1140 bytes 545b0294
- 00bc0e04 ["INT_ADD", "register:40f0:8", ["const:bc0e04:8", "const:4:8"]]
- 00bc0e04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bc122c ["INT_ADD", "register:40f0:8", ["const:bc122c:8", "const:4:8"]]
+ 00bc122c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bc0e04 bytes 2b5b0294
+ 00bc122c bytes 215b0294
- 00bc0e40 ["INT_ADD", "register:40f0:8", ["const:bc0e40:8", "const:4:8"]]
- 00bc0e40 ["CALL", null, ["callee:00c5ad10:8"]]
+ 00bc1268 ["INT_ADD", "register:40f0:8", ["const:bc1268:8", "const:4:8"]]
+ 00bc1268 ["CALL", null, ["callee:00c5ad10:8"]]
- 00bc0e40 bytes b4660294
+ 00bc1268 bytes aa660294
~~~


<a id="compare-1614aac952b78990a6acc17caa9e8b06"></a>

### [`00bc13c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc13c0.md) → [`00bc17e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc17e8.md) _ZN8firebase13remote_config12RemoteConfigD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc13c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc13c0.md#insn-00bc13c8)
- 新版 [`00bc17f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc17e8.md#insn-00bc17f0)

~~~diff
- 00bc13c8 ["INT_ADD", "register:40f0:8", ["const:bc13c8:8", "const:4:8"]]
- 00bc13c8 ["CALL", null, ["callee:00c5d6b0:8"]]
+ 00bc17f0 ["INT_ADD", "register:40f0:8", ["const:bc17f0:8", "const:4:8"]]
+ 00bc17f0 ["CALL", null, ["callee:00c5d6b0:8"]]
- 00bc13c8 bytes ba6f0294
+ 00bc17f0 bytes b06f0294
~~~


<a id="compare-e6c9b1a1e208b0b8f4a5fd27d83ae7db"></a>

### [`00bc1408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1408.md) → [`00bc1830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1830.md) _ZN8firebase13remote_config12RemoteConfig5FetchEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d350.md) [`00c5d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d750.md) [`00c5d7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1408.md#insn-00bc1420)
- 新版 [`00bc1848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1830.md#insn-00bc1848)

~~~diff
- 00bc1420 ["INT_ADD", "register:40f0:8", ["const:bc1420:8", "const:4:8"]]
- 00bc1420 ["CALL", null, ["callee:00c5d750:8"]]
+ 00bc1848 ["INT_ADD", "register:40f0:8", ["const:bc1848:8", "const:4:8"]]
+ 00bc1848 ["CALL", null, ["callee:00c5d750:8"]]
- 00bc1420 bytes cc6f0294
+ 00bc1848 bytes c26f0294
~~~


<a id="compare-7f4707f2a60b6b7ca85147188507b740"></a>

### [`00bc1530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md) → [`00bc1958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md) _ZN8firebase13remote_config12RemoteConfig25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5d390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d390.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md#insn-00bc1574) · [`00bc159c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md#insn-00bc159c) · [`00bc15b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1530.md#insn-00bc15b0)
- 新版 [`00bc199c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md#insn-00bc199c) · [`00bc19c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md#insn-00bc19c4) · [`00bc19d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1958.md#insn-00bc19d8)

~~~diff
- 00bc1574 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1574 ["INT_ADD", "register:40f0:8", ["const:bc1574:8", "const:4:8"]]
- 00bc1574 ["CALLIND", null, ["register:0:8"]]
+ 00bc199c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc199c ["INT_ADD", "register:40f0:8", ["const:bc199c:8", "const:4:8"]]
+ 00bc199c ["CALLIND", null, ["register:0:8"]]
- 00bc1574 bytes 00013fd6
+ 00bc199c bytes 00013fd6
- 00bc159c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc159c ["INT_ADD", "register:40f0:8", ["const:bc159c:8", "const:4:8"]]
- 00bc159c ["CALLIND", null, ["register:0:8"]]
+ 00bc19c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc19c4 ["INT_ADD", "register:40f0:8", ["const:bc19c4:8", "const:4:8"]]
+ 00bc19c4 ["CALLIND", null, ["register:0:8"]]
- 00bc159c bytes 00013fd6
+ 00bc19c4 bytes 00013fd6
- 00bc15b0 ["INT_ADD", "register:40f0:8", ["const:bc15b0:8", "const:4:8"]]
- 00bc15b0 ["CALL", null, ["callee:00c5d790:8"]]
+ 00bc19d8 ["INT_ADD", "register:40f0:8", ["const:bc19d8:8", "const:4:8"]]
+ 00bc19d8 ["CALL", null, ["callee:00c5d790:8"]]
- 00bc15b0 bytes 786f0294
+ 00bc19d8 bytes 6e6f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-678695a0507326eb60d18a68ccc64f9a"></a>

### [`00bc1670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1670.md) → [`00bc1a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a98.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_13remote_config12RemoteConfigEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4b0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4b0.md)
- 新版 呼出元 1件 [`00c5d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8b0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1670.md#insn-00bc168c) · [`00bc1698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1670.md#insn-00bc1698)
- 新版 [`00bc1ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a98.md#insn-00bc1ab4) · [`00bc1ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a98.md#insn-00bc1ac0)

~~~diff
- 00bc168c ["INT_ADD", "register:40f0:8", ["const:bc168c:8", "const:4:8"]]
- 00bc168c ["CALL", null, ["callee:00c5d8b0:8"]]
+ 00bc1ab4 ["INT_ADD", "register:40f0:8", ["const:bc1ab4:8", "const:4:8"]]
+ 00bc1ab4 ["CALL", null, ["callee:00c5d8b0:8"]]
- 00bc168c bytes 896f0294
+ 00bc1ab4 bytes 7f6f0294
- 00bc1698 ["INT_ADD", "register:40f0:8", ["const:bc1698:8", "const:4:8"]]
- 00bc1698 ["CALL", null, ["callee:00c5d8b0:8"]]
+ 00bc1ac0 ["INT_ADD", "register:40f0:8", ["const:bc1ac0:8", "const:4:8"]]
+ 00bc1ac0 ["CALL", null, ["callee:00c5d8b0:8"]]
- 00bc1698 bytes 866f0294
+ 00bc1ac0 bytes 7c6f0294
~~~


<a id="compare-1bcae8219c692b7f393b854676ef53a5"></a>

### [`00bc44b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc44b0.md) → [`00bc48d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md) _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d530.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5d930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d930.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc44d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc44b0.md#insn-00bc44d0) · [`00bc44e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc44b0.md#insn-00bc44e8) · [`00bc44f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc44b0.md#insn-00bc44f0)
- 新版 [`00bc48f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md#insn-00bc48f8) · [`00bc4910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md#insn-00bc4910) · [`00bc4918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc48d8.md#insn-00bc4918)

~~~diff
- 00bc44d0 ["INT_ADD", "register:40f0:8", ["const:bc44d0:8", "const:4:8"]]
- 00bc44d0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc48f8 ["INT_ADD", "register:40f0:8", ["const:bc48f8:8", "const:4:8"]]
+ 00bc48f8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc44d0 bytes 4c580294
+ 00bc48f8 bytes 42580294
- 00bc44e8 ["INT_ADD", "register:40f0:8", ["const:bc44e8:8", "const:4:8"]]
- 00bc44e8 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc4910 ["INT_ADD", "register:40f0:8", ["const:bc4910:8", "const:4:8"]]
+ 00bc4910 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc44e8 bytes 4a580294
+ 00bc4910 bytes 40580294
- 00bc44f0 ["INT_ADD", "register:40f0:8", ["const:bc44f0:8", "const:4:8"]]
- 00bc44f0 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc4918 ["INT_ADD", "register:40f0:8", ["const:bc4918:8", "const:4:8"]]
+ 00bc4918 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc44f0 bytes 48580294
+ 00bc4918 bytes 3e580294
~~~


<a id="compare-a0cdf3bca0a26d7f10601b32903f2ae6"></a>

### [`00bc4520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4520.md) → [`00bc4948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4948.md) FUN_00bc4948

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc456c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4520.md#insn-00bc456c)
- 新版 [`00bc4994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4948.md#insn-00bc4994)

~~~diff
- 00bc456c ["INT_ADD", "register:40f0:8", ["const:bc456c:8", "const:4:8"]]
- 00bc456c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bc4994 ["INT_ADD", "register:40f0:8", ["const:bc4994:8", "const:4:8"]]
+ 00bc4994 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bc456c bytes 514d0294
+ 00bc4994 bytes 474d0294
~~~


<a id="compare-399c3f3a674711e28ce7f4ea308afff4"></a>

### [`00bc4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md) → [`00bc4f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md) _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bc52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc52ac.md) · 呼出先 6件 [`00bc4c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00bc56d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc56d4.md) · 呼出先 6件 [`00bc505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc4b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md#insn-00bc4b40) · [`00bc4b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md#insn-00bc4b5c) · [`00bc4b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md#insn-00bc4b84)
- 新版 [`00bc4f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md#insn-00bc4f68) · [`00bc4f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md#insn-00bc4f84) · [`00bc4fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md#insn-00bc4fac)

~~~diff
- 00bc4b40 ["INT_ADD", "register:40f0:8", ["const:bc4b40:8", "const:4:8"]]
- 00bc4b40 ["CALL", null, ["callee:00bc505c:8"]]
+ 00bc4f68 ["INT_ADD", "register:40f0:8", ["const:bc4f68:8", "const:4:8"]]
+ 00bc4f68 ["CALL", null, ["callee:00bc505c:8"]]
- 00bc4b40 bytes 3d000094
+ 00bc4f68 bytes 3d000094
- 00bc4b5c ["INT_ADD", "register:40f0:8", ["const:bc4b5c:8", "const:4:8"]]
- 00bc4b5c ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bc4f84 ["INT_ADD", "register:40f0:8", ["const:bc4f84:8", "const:4:8"]]
+ 00bc4f84 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bc4b5c bytes a9570294
+ 00bc4f84 bytes 9f570294
- 00bc4b84 ["INT_ADD", "register:40f0:8", ["const:bc4b84:8", "const:4:8"]]
- 00bc4b84 ["CALL", null, ["callee:00c5d8d0:8"]]
+ 00bc4fac ["INT_ADD", "register:40f0:8", ["const:bc4fac:8", "const:4:8"]]
+ 00bc4fac ["CALL", null, ["callee:00c5d8d0:8"]]
- 00bc4b84 bytes 53620294
+ 00bc4fac bytes 49620294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b9be073d6ec968d2f903d9bb2f9e1b"></a>

### [`00bc4e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md) → [`00bc5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md) _ZN8firebase13remote_config8internal20CompleteVoidCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bc6ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md) [`00bc7314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7314.md) [`00c5d4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4c0.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 3件 [`00bc72e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc72e8.md) [`00bc773c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc773c.md) [`00c5d8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8c0.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc4e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md#insn-00bc4e64) · [`00bc4e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md#insn-00bc4e80) · [`00bc4e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md#insn-00bc4e88)
- 新版 [`00bc528c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md#insn-00bc528c) · [`00bc52a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md#insn-00bc52a8) · [`00bc52b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md#insn-00bc52b0)

~~~diff
- 00bc4e64 ["INT_ADD", "register:40f0:8", ["const:bc4e64:8", "const:4:8"]]
- 00bc4e64 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bc528c ["INT_ADD", "register:40f0:8", ["const:bc528c:8", "const:4:8"]]
+ 00bc528c ["CALL", null, ["callee:00c5ae00:8"]]
- 00bc4e64 bytes e7560294
+ 00bc528c bytes dd560294
- 00bc4e80 ["INT_ADD", "register:40f0:8", ["const:bc4e80:8", "const:4:8"]]
- 00bc4e80 ["CALL", null, ["callee:00c5ada0:8"]]
+ 00bc52a8 ["INT_ADD", "register:40f0:8", ["const:bc52a8:8", "const:4:8"]]
+ 00bc52a8 ["CALL", null, ["callee:00c5ada0:8"]]
- 00bc4e80 bytes c8560294
+ 00bc52a8 bytes be560294
- 00bc4e88 ["INT_ADD", "register:40f0:8", ["const:bc4e88:8", "const:4:8"]]
- 00bc4e88 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00bc52b0 ["INT_ADD", "register:40f0:8", ["const:bc52b0:8", "const:4:8"]]
+ 00bc52b0 ["CALL", null, ["callee:00c5aa90:8"]]
- 00bc4e88 bytes 02560294
+ 00bc52b0 bytes f8550294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cae6281443d685aeb69ce51628dcbd4b"></a>

### [`00bc5188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md) → [`00bc55b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d580.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5d980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d980.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc51d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md#insn-00bc51d8) · [`00bc5204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md#insn-00bc5204) · [`00bc5230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5188.md#insn-00bc5230)
- 新版 [`00bc5600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md#insn-00bc5600) · [`00bc562c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md#insn-00bc562c) · [`00bc5658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc55b0.md#insn-00bc5658)

~~~diff
- 00bc51d8 ["INT_ADD", "register:40f0:8", ["const:bc51d8:8", "const:4:8"]]
- 00bc51d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bc5600 ["INT_ADD", "register:40f0:8", ["const:bc5600:8", "const:4:8"]]
+ 00bc5600 ["CALL", null, ["callee:00c57e90:8"]]
- 00bc51d8 bytes 2e4a0294
+ 00bc5600 bytes 244a0294
- 00bc5204 ["INT_ADD", "register:40f0:8", ["const:bc5204:8", "const:4:8"]]
- 00bc5204 ["CALL", null, ["callee:00c5b5b0:8"]]
+ 00bc562c ["INT_ADD", "register:40f0:8", ["const:bc562c:8", "const:4:8"]]
+ 00bc562c ["CALL", null, ["callee:00c5b5b0:8"]]
- 00bc5204 bytes eb570294
+ 00bc562c bytes e1570294
- 00bc5230 ["INT_ADD", "register:40f0:8", ["const:bc5230:8", "const:4:8"]]
- 00bc5230 ["CALL", null, ["callee:00c5ad10:8"]]
+ 00bc5658 ["INT_ADD", "register:40f0:8", ["const:bc5658:8", "const:4:8"]]
+ 00bc5658 ["CALL", null, ["callee:00c5ad10:8"]]
- 00bc5230 bytes b8550294
+ 00bc5658 bytes ae550294
~~~


<a id="compare-8f096195440256d4d4db6e9c37da2118"></a>

### [`00bc5548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5548.md) → [`00bc5970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27EnsureInitializedLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3c0.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7c0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5548.md#insn-00bc5568) · [`00bc5574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5548.md#insn-00bc5574) · [`00bc5580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5548.md#insn-00bc5580)
- 新版 [`00bc5990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md#insn-00bc5990) · [`00bc599c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md#insn-00bc599c) · [`00bc59a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5970.md#insn-00bc59a8)

~~~diff
- 00bc5568 ["INT_ADD", "register:40f0:8", ["const:bc5568:8", "const:4:8"]]
- 00bc5568 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc5990 ["INT_ADD", "register:40f0:8", ["const:bc5990:8", "const:4:8"]]
+ 00bc5990 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc5568 bytes 26540294
+ 00bc5990 bytes 1c540294
- 00bc5574 ["INT_ADD", "register:40f0:8", ["const:bc5574:8", "const:4:8"]]
- 00bc5574 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc599c ["INT_ADD", "register:40f0:8", ["const:bc599c:8", "const:4:8"]]
+ 00bc599c ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc5574 bytes 27540294
+ 00bc599c bytes 1d540294
- 00bc5580 ["INT_ADD", "register:40f0:8", ["const:bc5580:8", "const:4:8"]]
- 00bc5580 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc59a8 ["INT_ADD", "register:40f0:8", ["const:bc59a8:8", "const:4:8"]]
+ 00bc59a8 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc5580 bytes bc540294
+ 00bc59a8 bytes b2540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3587c9418562c5705f5a18bf78d9005b"></a>

### [`00bc5874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5874.md) → [`00bc5c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal18ActivateLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d370.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d770.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5874.md#insn-00bc5894) · [`00bc58a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5874.md#insn-00bc58a0) · [`00bc58ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5874.md#insn-00bc58ac)
- 新版 [`00bc5cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md#insn-00bc5cbc) · [`00bc5cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md#insn-00bc5cc8) · [`00bc5cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5c9c.md#insn-00bc5cd4)

~~~diff
- 00bc5894 ["INT_ADD", "register:40f0:8", ["const:bc5894:8", "const:4:8"]]
- 00bc5894 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc5cbc ["INT_ADD", "register:40f0:8", ["const:bc5cbc:8", "const:4:8"]]
+ 00bc5cbc ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc5894 bytes 5b530294
+ 00bc5cbc bytes 51530294
- 00bc58a0 ["INT_ADD", "register:40f0:8", ["const:bc58a0:8", "const:4:8"]]
- 00bc58a0 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc5cc8 ["INT_ADD", "register:40f0:8", ["const:bc5cc8:8", "const:4:8"]]
+ 00bc5cc8 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc58a0 bytes 5c530294
+ 00bc5cc8 bytes 52530294
- 00bc58ac ["INT_ADD", "register:40f0:8", ["const:bc58ac:8", "const:4:8"]]
- 00bc58ac ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc5cd4 ["INT_ADD", "register:40f0:8", ["const:bc5cd4:8", "const:4:8"]]
+ 00bc5cd4 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc58ac bytes f1530294
+ 00bc5cd4 bytes e7530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90f9a7f326d57a56246b49bd18590af4"></a>

### [`00bc5ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ba0.md) → [`00bc5fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26FetchAndActivateLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3a0.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7a0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ba0.md#insn-00bc5bc0) · [`00bc5bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ba0.md#insn-00bc5bcc) · [`00bc5bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ba0.md#insn-00bc5bd8)
- 新版 [`00bc5fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md#insn-00bc5fe8) · [`00bc5ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md#insn-00bc5ff4) · [`00bc6000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5fc8.md#insn-00bc6000)

~~~diff
- 00bc5bc0 ["INT_ADD", "register:40f0:8", ["const:bc5bc0:8", "const:4:8"]]
- 00bc5bc0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc5fe8 ["INT_ADD", "register:40f0:8", ["const:bc5fe8:8", "const:4:8"]]
+ 00bc5fe8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc5bc0 bytes 90520294
+ 00bc5fe8 bytes 86520294
- 00bc5bcc ["INT_ADD", "register:40f0:8", ["const:bc5bcc:8", "const:4:8"]]
- 00bc5bcc ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc5ff4 ["INT_ADD", "register:40f0:8", ["const:bc5ff4:8", "const:4:8"]]
+ 00bc5ff4 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc5bcc bytes 91520294
+ 00bc5ff4 bytes 87520294
- 00bc5bd8 ["INT_ADD", "register:40f0:8", ["const:bc5bd8:8", "const:4:8"]]
- 00bc5bd8 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc6000 ["INT_ADD", "register:40f0:8", ["const:bc6000:8", "const:4:8"]]
+ 00bc6000 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc5bd8 bytes 26530294
+ 00bc6000 bytes 1c530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-528ce7083e6c52b1e1c1fef0ac2533a6"></a>

### [`00bc5ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ec8.md) → [`00bc62f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15FetchLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d300.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d700.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ec8.md#insn-00bc5ee8) · [`00bc5ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ec8.md#insn-00bc5ef4) · [`00bc5f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ec8.md#insn-00bc5f00)
- 新版 [`00bc6310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md#insn-00bc6310) · [`00bc631c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md#insn-00bc631c) · [`00bc6328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc62f0.md#insn-00bc6328)

~~~diff
- 00bc5ee8 ["INT_ADD", "register:40f0:8", ["const:bc5ee8:8", "const:4:8"]]
- 00bc5ee8 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc6310 ["INT_ADD", "register:40f0:8", ["const:bc6310:8", "const:4:8"]]
+ 00bc6310 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc5ee8 bytes c6510294
+ 00bc6310 bytes bc510294
- 00bc5ef4 ["INT_ADD", "register:40f0:8", ["const:bc5ef4:8", "const:4:8"]]
- 00bc5ef4 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc631c ["INT_ADD", "register:40f0:8", ["const:bc631c:8", "const:4:8"]]
+ 00bc631c ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc5ef4 bytes c7510294
+ 00bc631c bytes bd510294
- 00bc5f00 ["INT_ADD", "register:40f0:8", ["const:bc5f00:8", "const:4:8"]]
- 00bc5f00 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc6328 ["INT_ADD", "register:40f0:8", ["const:bc6328:8", "const:4:8"]]
+ 00bc6328 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc5f00 bytes 5c520294
+ 00bc6328 bytes 52520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90a81c05425da6ed389bc98dc68352cc"></a>

### [`00bc6e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md) → [`00bc7258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal21SetDefaultsLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d380.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d780.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc6e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md#insn-00bc6e50) · [`00bc6e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md#insn-00bc6e5c) · [`00bc6e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md#insn-00bc6e68)
- 新版 [`00bc7278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md#insn-00bc7278) · [`00bc7284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md#insn-00bc7284) · [`00bc7290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7258.md#insn-00bc7290)

~~~diff
- 00bc6e50 ["INT_ADD", "register:40f0:8", ["const:bc6e50:8", "const:4:8"]]
- 00bc6e50 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc7278 ["INT_ADD", "register:40f0:8", ["const:bc7278:8", "const:4:8"]]
+ 00bc7278 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc6e50 bytes ec4d0294
+ 00bc7278 bytes e24d0294
- 00bc6e5c ["INT_ADD", "register:40f0:8", ["const:bc6e5c:8", "const:4:8"]]
- 00bc6e5c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc7284 ["INT_ADD", "register:40f0:8", ["const:bc7284:8", "const:4:8"]]
+ 00bc7284 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc6e5c bytes ed4d0294
+ 00bc7284 bytes e34d0294
- 00bc6e68 ["INT_ADD", "register:40f0:8", ["const:bc6e68:8", "const:4:8"]]
- 00bc6e68 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc7290 ["INT_ADD", "register:40f0:8", ["const:bc7290:8", "const:4:8"]]
+ 00bc7290 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc6e68 bytes 824e0294
+ 00bc7290 bytes 784e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fffe203fe6972b3c604c2f7f2c8dd0e"></a>

### [`00bc7284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md) → [`00bc76ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27SetConfigSettingsLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3d0.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7d0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc72a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md#insn-00bc72a4) · [`00bc72b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md#insn-00bc72b0) · [`00bc72bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md#insn-00bc72bc)
- 新版 [`00bc76cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md#insn-00bc76cc) · [`00bc76d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md#insn-00bc76d8) · [`00bc76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc76ac.md#insn-00bc76e4)

~~~diff
- 00bc72a4 ["INT_ADD", "register:40f0:8", ["const:bc72a4:8", "const:4:8"]]
- 00bc72a4 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc76cc ["INT_ADD", "register:40f0:8", ["const:bc76cc:8", "const:4:8"]]
+ 00bc76cc ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc72a4 bytes d74c0294
+ 00bc76cc bytes cd4c0294
- 00bc72b0 ["INT_ADD", "register:40f0:8", ["const:bc72b0:8", "const:4:8"]]
- 00bc72b0 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc76d8 ["INT_ADD", "register:40f0:8", ["const:bc76d8:8", "const:4:8"]]
+ 00bc76d8 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc72b0 bytes d84c0294
+ 00bc76d8 bytes ce4c0294
- 00bc72bc ["INT_ADD", "register:40f0:8", ["const:bc72bc:8", "const:4:8"]]
- 00bc72bc ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc76e4 ["INT_ADD", "register:40f0:8", ["const:bc76e4:8", "const:4:8"]]
+ 00bc76e4 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc72bc bytes 6d4d0294
+ 00bc76e4 bytes 634d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14eed1b8b244606ea9910cbba6ca6b45"></a>

### [`00bc79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc79cc.md) → [`00bc7df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26SetCustomSignalsLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3b0.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7b0.md) · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc79ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc79cc.md#insn-00bc79ec) · [`00bc79f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc79cc.md#insn-00bc79f8) · [`00bc7a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc79cc.md#insn-00bc7a04)
- 新版 [`00bc7e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md#insn-00bc7e14) · [`00bc7e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md#insn-00bc7e20) · [`00bc7e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7df4.md#insn-00bc7e2c)

~~~diff
- 00bc79ec ["INT_ADD", "register:40f0:8", ["const:bc79ec:8", "const:4:8"]]
- 00bc79ec ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc7e14 ["INT_ADD", "register:40f0:8", ["const:bc7e14:8", "const:4:8"]]
+ 00bc7e14 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc79ec bytes 054b0294
+ 00bc7e14 bytes fb4a0294
- 00bc79f8 ["INT_ADD", "register:40f0:8", ["const:bc79f8:8", "const:4:8"]]
- 00bc79f8 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc7e20 ["INT_ADD", "register:40f0:8", ["const:bc7e20:8", "const:4:8"]]
+ 00bc7e20 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc79f8 bytes 064b0294
+ 00bc7e20 bytes fc4a0294
- 00bc7a04 ["INT_ADD", "register:40f0:8", ["const:bc7a04:8", "const:4:8"]]
- 00bc7a04 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc7e2c ["INT_ADD", "register:40f0:8", ["const:bc7e2c:8", "const:4:8"]]
+ 00bc7e2c ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc7a04 bytes 9b4b0294
+ 00bc7e2c bytes 914b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5538fae2cb6349c860f98a217620a6f4"></a>

### [`00bc858c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc858c.md) → [`00bc89b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89b4.md) _ZN8firebase9MutexLockD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d540.md) · 呼出先 1件 [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5d940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d940.md) · 呼出先 1件 [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc858c.md#insn-00bc8598)
- 新版 [`00bc89c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89b4.md#insn-00bc89c0)

~~~diff
- 00bc8598 ["INT_ADD", "register:40f0:8", ["const:bc8598:8", "const:4:8"]]
- 00bc8598 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc89c0 ["INT_ADD", "register:40f0:8", ["const:bc89c0:8", "const:4:8"]]
+ 00bc89c0 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc8598 bytes 1e480294
+ 00bc89c0 bytes 14480294
~~~


<a id="compare-fcf16cf4c838f41ef8e074a00c974f61"></a>

### [`00bc922c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md) → [`00bc9654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md) _ZN8firebase13remote_config8internal37JniConfigUpdateListener_nativeOnErrorEP7_JNIEnvP8_jobjectli

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md#insn-00bc927c) · [`00bc92b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md#insn-00bc92b8) · [`00bc92d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc922c.md#insn-00bc92d0)
- 新版 [`00bc96a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md#insn-00bc96a4) · [`00bc96e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md#insn-00bc96e0) · [`00bc96f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md#insn-00bc96f8)

~~~diff
- 00bc927c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc927c ["INT_ADD", "register:40f0:8", ["const:bc927c:8", "const:4:8"]]
- 00bc927c ["CALLIND", null, ["register:0:8"]]
+ 00bc96a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc96a4 ["INT_ADD", "register:40f0:8", ["const:bc96a4:8", "const:4:8"]]
+ 00bc96a4 ["CALLIND", null, ["register:0:8"]]
- 00bc927c bytes 00013fd6
+ 00bc96a4 bytes 00013fd6
- 00bc92b8 ["INT_ADD", "register:40f0:8", ["const:bc92b8:8", "const:4:8"]]
- 00bc92b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bc96e0 ["INT_ADD", "register:40f0:8", ["const:bc96e0:8", "const:4:8"]]
+ 00bc96e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bc92b8 bytes fe390294
+ 00bc96e0 bytes f4390294
- 00bc92d0 ["INT_ADD", "register:40f0:8", ["const:bc92d0:8", "const:4:8"]]
- 00bc92d0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bc96f8 ["INT_ADD", "register:40f0:8", ["const:bc96f8:8", "const:4:8"]]
+ 00bc96f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bc92d0 bytes f8390294
+ 00bc96f8 bytes ee390294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc74225e1ad2afb9b12e9ea8469e455"></a>

### [`00bc9360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md) → [`00bc9788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d560.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5d550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d550.md)
- 新版 呼出元 1件 [`00c5d960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d960.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5d950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md#insn-00bc9394) · [`00bc93b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md#insn-00bc93b0) · [`00bc93d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9360.md#insn-00bc93d8)
- 新版 [`00bc97bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md#insn-00bc97bc) · [`00bc97d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md#insn-00bc97d8) · [`00bc9800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9788.md#insn-00bc9800)

~~~diff
- 00bc9394 ["INT_ADD", "register:40f0:8", ["const:bc9394:8", "const:4:8"]]
- 00bc9394 ["CALL", null, ["callee:00c5d950:8"]]
+ 00bc97bc ["INT_ADD", "register:40f0:8", ["const:bc97bc:8", "const:4:8"]]
+ 00bc97bc ["CALL", null, ["callee:00c5d950:8"]]
- 00bc9394 bytes 6f500294
+ 00bc97bc bytes 65500294
- 00bc93b0 ["INT_ADD", "register:40f0:8", ["const:bc93b0:8", "const:4:8"]]
- 00bc93b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bc97d8 ["INT_ADD", "register:40f0:8", ["const:bc97d8:8", "const:4:8"]]
+ 00bc97d8 ["CALL", null, ["callee:00c57e90:8"]]
- 00bc93b0 bytes b8390294
+ 00bc97d8 bytes ae390294
- 00bc93d8 ["INT_ADD", "register:40f0:8", ["const:bc93d8:8", "const:4:8"]]
- 00bc93d8 ["CALL", null, ["callee:00c5a840:8"]]
+ 00bc9800 ["INT_ADD", "register:40f0:8", ["const:bc9800:8", "const:4:8"]]
+ 00bc9800 ["CALL", null, ["callee:00c5a840:8"]]
- 00bc93d8 bytes 1a440294
+ 00bc9800 bytes 10440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca2bd51312298343f7080904c49be9d"></a>

### [`00bc9450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9450.md) → [`00bc9878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9878.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d550.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5d950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d950.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc94ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9450.md#insn-00bc94ec) · [`00bc952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9450.md#insn-00bc952c)
- 新版 [`00bc9914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9878.md#insn-00bc9914) · [`00bc9954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9878.md#insn-00bc9954)

~~~diff
- 00bc94ec ["INT_ADD", "register:40f0:8", ["const:bc94ec:8", "const:4:8"]]
- 00bc94ec ["CALL", null, ["callee:00c58050:8"]]
+ 00bc9914 ["INT_ADD", "register:40f0:8", ["const:bc9914:8", "const:4:8"]]
+ 00bc9914 ["CALL", null, ["callee:00c58050:8"]]
- 00bc94ec bytes d9390294
+ 00bc9914 bytes cf390294
- 00bc952c ["INT_ADD", "register:40f0:8", ["const:bc952c:8", "const:4:8"]]
- 00bc952c ["CALL", null, ["callee:00c58050:8"]]
+ 00bc9954 ["INT_ADD", "register:40f0:8", ["const:bc9954:8", "const:4:8"]]
+ 00bc9954 ["CALL", null, ["callee:00c58050:8"]]
- 00bc952c bytes c9390294
+ 00bc9954 bytes bf390294
~~~


<a id="compare-cd7576b326e6c4f29d6b795a124379be"></a>

### [`00bc9570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9570.md) → [`00bc9998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9998.md) FUN_00bc9998

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bc8dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8dcc.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d290.md)
- 新版 呼出元 1件 [`00bc91f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d690.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9570.md#insn-00bc9584)
- 新版 [`00bc99ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9998.md#insn-00bc99ac)

~~~diff
- 00bc9584 ["INT_ADD", "register:40f0:8", ["const:bc9584:8", "const:4:8"]]
- 00bc9584 ["CALL", null, ["callee:00c5d690:8"]]
+ 00bc99ac ["INT_ADD", "register:40f0:8", ["const:bc99ac:8", "const:4:8"]]
+ 00bc99ac ["CALL", null, ["callee:00c5d690:8"]]
- 00bc9584 bytes 434f0294
+ 00bc99ac bytes 394f0294
~~~


<a id="compare-329b749aa1f3fb0b9df348194ccc7424"></a>

### [`00bc9efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9efc.md) → [`00bca324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca324.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d270.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9efc.md#insn-00bc9f1c)
- 新版 [`00bca344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca324.md#insn-00bca344)

~~~diff
- 00bc9f1c ["INT_ADD", "register:40f0:8", ["const:bc9f1c:8", "const:4:8"]]
- 00bc9f1c ["CALL", null, ["callee:00c5d670:8"]]
+ 00bca344 ["INT_ADD", "register:40f0:8", ["const:bca344:8", "const:4:8"]]
+ 00bca344 ["CALL", null, ["callee:00c5d670:8"]]
- 00bc9f1c bytes d54c0294
+ 00bca344 bytes cb4c0294
~~~


<a id="compare-5e8fe54e6a95a9db9baf9f09b86eee26"></a>

### [`00bc9f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f40.md) → [`00bca368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca368.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalC2EPNS1_20RemoteConfigInternalENSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d280.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d680.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f40.md#insn-00bc9f74) · [`00bc9f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f40.md#insn-00bc9f98)
- 新版 [`00bca39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca368.md#insn-00bca39c) · [`00bca3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca368.md#insn-00bca3c0)

~~~diff
- 00bc9f74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9f74 ["INT_ADD", "register:40f0:8", ["const:bc9f74:8", "const:4:8"]]
- 00bc9f74 ["CALLIND", null, ["register:0:8"]]
+ 00bca39c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca39c ["INT_ADD", "register:40f0:8", ["const:bca39c:8", "const:4:8"]]
+ 00bca39c ["CALLIND", null, ["register:0:8"]]
- 00bc9f74 bytes 00013fd6
+ 00bca39c bytes 00013fd6
- 00bc9f98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9f98 ["INT_ADD", "register:40f0:8", ["const:bc9f98:8", "const:4:8"]]
- 00bc9f98 ["CALLIND", null, ["register:0:8"]]
+ 00bca3c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca3c0 ["INT_ADD", "register:40f0:8", ["const:bca3c0:8", "const:4:8"]]
+ 00bca3c0 ["CALLIND", null, ["register:0:8"]]
- 00bc9f98 bytes 00013fd6
+ 00bca3c0 bytes 00013fd6
~~~


<a id="compare-267140ddb15bf358c83d583a59530783"></a>

### [`00bc9fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9fac.md) → [`00bca3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca3d4.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d290.md) · 呼出先 1件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md)
- 新版 呼出元 1件 [`00c5d690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d690.md) · 呼出先 1件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9fac.md#insn-00bc9fdc) · [`00bca020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9fac.md#insn-00bca020)
- 新版 [`00bca404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca3d4.md#insn-00bca404) · [`00bca448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca3d4.md#insn-00bca448)

~~~diff
- 00bc9fdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9fdc ["INT_ADD", "register:40f0:8", ["const:bc9fdc:8", "const:4:8"]]
- 00bc9fdc ["CALLIND", null, ["register:0:8"]]
+ 00bca404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca404 ["INT_ADD", "register:40f0:8", ["const:bca404:8", "const:4:8"]]
+ 00bca404 ["CALLIND", null, ["register:0:8"]]
- 00bc9fdc bytes 00013fd6
+ 00bca404 bytes 00013fd6
- 00bca020 ["INT_ADD", "register:40f0:8", ["const:bca020:8", "const:4:8"]]
- 00bca020 ["CALL", null, ["callee:00b6112c:8"]]
+ 00bca448 ["INT_ADD", "register:40f0:8", ["const:bca448:8", "const:4:8"]]
+ 00bca448 ["CALL", null, ["callee:00b6112c:8"]]
- 00bca020 bytes 395bfe97
+ 00bca448 bytes 395bfe97
~~~


<a id="compare-16f5a68c2a96641f787c73f0ef2b9190"></a>

### [`00bca870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md) → [`00bcac98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md) _ZN8firebase4auth8AuthDataD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6b0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5d5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5a0.md)
- 新版 呼出元 1件 [`00c5dab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dab0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa50.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md) [`00c5d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md#insn-00bca880) · [`00bca89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md#insn-00bca89c) · [`00bca8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md#insn-00bca8ac)
- 新版 [`00bcaca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md#insn-00bcaca8) · [`00bcacc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md#insn-00bcacc4) · [`00bcacd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcac98.md#insn-00bcacd4)

~~~diff
- 00bca880 ["INT_ADD", "register:40f0:8", ["const:bca880:8", "const:4:8"]]
- 00bca880 ["CALL", null, ["callee:00c5d9a0:8"]]
+ 00bcaca8 ["INT_ADD", "register:40f0:8", ["const:bcaca8:8", "const:4:8"]]
+ 00bcaca8 ["CALL", null, ["callee:00c5d9a0:8"]]
- 00bca880 bytes 484b0294
+ 00bcaca8 bytes 3e4b0294
- 00bca89c ["INT_ADD", "register:40f0:8", ["const:bca89c:8", "const:4:8"]]
- 00bca89c ["CALL", null, ["callee:00c5da70:8"]]
+ 00bcacc4 ["INT_ADD", "register:40f0:8", ["const:bcacc4:8", "const:4:8"]]
+ 00bcacc4 ["CALL", null, ["callee:00c5da70:8"]]
- 00bca89c bytes 754b0294
+ 00bcacc4 bytes 6b4b0294
- 00bca8ac ["INT_ADD", "register:40f0:8", ["const:bca8ac:8", "const:4:8"]]
- 00bca8ac ["CALL", null, ["callee:00c5da60:8"]]
+ 00bcacd4 ["INT_ADD", "register:40f0:8", ["const:bcacd4:8", "const:4:8"]]
+ 00bcacd4 ["CALL", null, ["callee:00c5da60:8"]]
- 00bca8ac bytes 6d4b0294
+ 00bcacd4 bytes 634b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e308a3780c8d134432002b5c37c2e50a"></a>

### [`00bca9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9bc.md) → [`00bcade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcade4.md) _ZN8firebase4auth4AuthD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5da30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9bc.md#insn-00bca9c4)
- 新版 [`00bcadec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcade4.md#insn-00bcadec)

~~~diff
- 00bca9c4 ["INT_ADD", "register:40f0:8", ["const:bca9c4:8", "const:4:8"]]
- 00bca9c4 ["CALL", null, ["callee:00c5da30:8"]]
+ 00bcadec ["INT_ADD", "register:40f0:8", ["const:bcadec:8", "const:4:8"]]
+ 00bcadec ["CALL", null, ["callee:00c5da30:8"]]
- 00bca9c4 bytes 1b4b0294
+ 00bcadec bytes 114b0294
~~~


<a id="compare-16bb6671bed0ebf7ebb4b2b9a448ca21"></a>

### [`00bcb57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md) → [`00bcb9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md) _ZNK8firebase4auth4Auth32FetchProvidersForEmailLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md#insn-00bcb59c) · [`00bcb5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md#insn-00bcb5a8) · [`00bcb5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md#insn-00bcb5b4)
- 新版 [`00bcb9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md#insn-00bcb9c4) · [`00bcb9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md#insn-00bcb9d0) · [`00bcb9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb9a4.md#insn-00bcb9dc)

~~~diff
- 00bcb59c ["INT_ADD", "register:40f0:8", ["const:bcb59c:8", "const:4:8"]]
- 00bcb59c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcb9c4 ["INT_ADD", "register:40f0:8", ["const:bcb9c4:8", "const:4:8"]]
+ 00bcb9c4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcb59c bytes 193c0294
+ 00bcb9c4 bytes 0f3c0294
- 00bcb5a8 ["INT_ADD", "register:40f0:8", ["const:bcb5a8:8", "const:4:8"]]
- 00bcb5a8 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bcb9d0 ["INT_ADD", "register:40f0:8", ["const:bcb9d0:8", "const:4:8"]]
+ 00bcb9d0 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bcb5a8 bytes 1a3c0294
+ 00bcb9d0 bytes 103c0294
- 00bcb5b4 ["INT_ADD", "register:40f0:8", ["const:bcb5b4:8", "const:4:8"]]
- 00bcb5b4 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bcb9dc ["INT_ADD", "register:40f0:8", ["const:bcb9dc:8", "const:4:8"]]
+ 00bcb9dc ["CALL", null, ["callee:00c5ac70:8"]]
- 00bcb5b4 bytes af3c0294
+ 00bcb9dc bytes a53c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed94bccff480c609450094d9194069ae"></a>

### [`00bcbe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbe7c.md) → [`00bcc2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2a4.md) _ZNK8firebase4auth4UsereqERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a660.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbe7c.md#insn-00bcbe8c) · [`00bcbe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbe7c.md#insn-00bcbe98)
- 新版 [`00bcc2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2a4.md#insn-00bcc2b4) · [`00bcc2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2a4.md#insn-00bcc2c0)

~~~diff
- 00bcbe8c ["INT_ADD", "register:40f0:8", ["const:bcbe8c:8", "const:4:8"]]
- 00bcbe8c ["CALL", null, ["callee:00c5aa60:8"]]
+ 00bcc2b4 ["INT_ADD", "register:40f0:8", ["const:bcc2b4:8", "const:4:8"]]
+ 00bcc2b4 ["CALL", null, ["callee:00c5aa60:8"]]
- 00bcbe8c bytes f5390294
+ 00bcc2b4 bytes eb390294
- 00bcbe98 ["INT_ADD", "register:40f0:8", ["const:bcbe98:8", "const:4:8"]]
- 00bcbe98 ["CALL", null, ["callee:00c5aa60:8"]]
+ 00bcc2c0 ["INT_ADD", "register:40f0:8", ["const:bcc2c0:8", "const:4:8"]]
+ 00bcc2c0 ["CALL", null, ["callee:00c5aa60:8"]]
- 00bcbe98 bytes f2390294
+ 00bcc2c0 bytes e8390294
~~~


<a id="compare-84ae7ad3a1feaa207ce9f60f152eb97a"></a>

### [`00bcbeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbeb0.md) → [`00bcc2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2d8.md) _ZNK8firebase4auth4UserneERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a660.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbeb0.md#insn-00bcbec0) · [`00bcbecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbeb0.md#insn-00bcbecc)
- 新版 [`00bcc2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2d8.md#insn-00bcc2e8) · [`00bcc2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2d8.md#insn-00bcc2f4)

~~~diff
- 00bcbec0 ["INT_ADD", "register:40f0:8", ["const:bcbec0:8", "const:4:8"]]
- 00bcbec0 ["CALL", null, ["callee:00c5aa60:8"]]
+ 00bcc2e8 ["INT_ADD", "register:40f0:8", ["const:bcc2e8:8", "const:4:8"]]
+ 00bcc2e8 ["CALL", null, ["callee:00c5aa60:8"]]
- 00bcbec0 bytes e8390294
+ 00bcc2e8 bytes de390294
- 00bcbecc ["INT_ADD", "register:40f0:8", ["const:bcbecc:8", "const:4:8"]]
- 00bcbecc ["CALL", null, ["callee:00c5aa60:8"]]
+ 00bcc2f4 ["INT_ADD", "register:40f0:8", ["const:bcc2f4:8", "const:4:8"]]
+ 00bcc2f4 ["CALL", null, ["callee:00c5aa60:8"]]
- 00bcbecc bytes e5390294
+ 00bcc2f4 bytes db390294
~~~


<a id="compare-3e9d4d431fd9a1935ea25b37ac241728"></a>

### [`00bcd744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md) → [`00bcdb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md) _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5f0.md) [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9f0.md) [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md#insn-00bcd75c) · [`00bcd768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md#insn-00bcd768) · [`00bcd770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md#insn-00bcd770)
- 新版 [`00bcdb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md#insn-00bcdb84) · [`00bcdb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md#insn-00bcdb90) · [`00bcdb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md#insn-00bcdb98)

~~~diff
- 00bcd75c ["INT_ADD", "register:40f0:8", ["const:bcd75c:8", "const:4:8"]]
- 00bcd75c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcdb84 ["INT_ADD", "register:40f0:8", ["const:bcdb84:8", "const:4:8"]]
+ 00bcdb84 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcd75c bytes a9330294
+ 00bcdb84 bytes 9f330294
- 00bcd768 ["INT_ADD", "register:40f0:8", ["const:bcd768:8", "const:4:8"]]
- 00bcd768 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bcdb90 ["INT_ADD", "register:40f0:8", ["const:bcdb90:8", "const:4:8"]]
+ 00bcdb90 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bcd768 bytes aa330294
+ 00bcdb90 bytes a0330294
- 00bcd770 ["INT_ADD", "register:40f0:8", ["const:bcd770:8", "const:4:8"]]
- 00bcd770 ["CALL", null, ["callee:00c5dc30:8"]]
+ 00bcdb98 ["INT_ADD", "register:40f0:8", ["const:bcdb98:8", "const:4:8"]]
+ 00bcdb98 ["CALL", null, ["callee:00c5dc30:8"]]
- 00bcd770 bytes 30400294
+ 00bcdb98 bytes 26400294
~~~


<a id="compare-7d537d69d6bad779010d6c7da83716a4"></a>

### [`00bce364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce364.md) → [`00bce78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7e0.md)
- 新版 呼出元 1件 [`00c5dcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dcf0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce364.md#insn-00bce398) · [`00bce3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce364.md#insn-00bce3ac) · [`00bce3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce364.md#insn-00bce3d8)
- 新版 [`00bce7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md#insn-00bce7c0) · [`00bce7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md#insn-00bce7d4) · [`00bce800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce78c.md#insn-00bce800)

~~~diff
- 00bce398 ["INT_ADD", "register:40f0:8", ["const:bce398:8", "const:4:8"]]
- 00bce398 ["CALL", null, ["callee:00c5dd10:8"]]
+ 00bce7c0 ["INT_ADD", "register:40f0:8", ["const:bce7c0:8", "const:4:8"]]
+ 00bce7c0 ["CALL", null, ["callee:00c5dd10:8"]]
- 00bce398 bytes 5e3d0294
+ 00bce7c0 bytes 543d0294
- 00bce3ac ["INT_ADD", "register:40f0:8", ["const:bce3ac:8", "const:4:8"]]
- 00bce3ac ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bce7d4 ["INT_ADD", "register:40f0:8", ["const:bce7d4:8", "const:4:8"]]
+ 00bce7d4 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bce3ac bytes 95310294
+ 00bce7d4 bytes 8b310294
- 00bce3d8 ["INT_ADD", "register:40f0:8", ["const:bce3d8:8", "const:4:8"]]
- 00bce3d8 ["CALL", null, ["callee:00c5dbe0:8"]]
+ 00bce800 ["INT_ADD", "register:40f0:8", ["const:bce800:8", "const:4:8"]]
+ 00bce800 ["CALL", null, ["callee:00c5dbe0:8"]]
- 00bce3d8 bytes 023d0294
+ 00bce800 bytes f83c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c84ae322cde55e659b94c40fa24bce3"></a>

### [`00bcf604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md) → [`00bcfa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md) _ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcd788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7a0.md)
- 新版 呼出元 1件 [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md#insn-00bcf63c) · [`00bcf654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md#insn-00bcf654) · [`00bcf67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md#insn-00bcf67c)
- 新版 [`00bcfa64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md#insn-00bcfa64) · [`00bcfa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md#insn-00bcfa7c) · [`00bcfaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md#insn-00bcfaa4)

~~~diff
- 00bcf63c ["INT_ADD", "register:40f0:8", ["const:bcf63c:8", "const:4:8"]]
- 00bcf63c ["CALL", null, ["callee:00c5dd20:8"]]
+ 00bcfa64 ["INT_ADD", "register:40f0:8", ["const:bcfa64:8", "const:4:8"]]
+ 00bcfa64 ["CALL", null, ["callee:00c5dd20:8"]]
- 00bcf63c bytes b9380294
+ 00bcfa64 bytes af380294
- 00bcf654 ["INT_ADD", "register:40f0:8", ["const:bcf654:8", "const:4:8"]]
- 00bcf654 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bcfa7c ["INT_ADD", "register:40f0:8", ["const:bcfa7c:8", "const:4:8"]]
+ 00bcfa7c ["CALL", null, ["callee:00c5ae00:8"]]
- 00bcf654 bytes eb2c0294
+ 00bcfa7c bytes e12c0294
- 00bcf67c ["INT_ADD", "register:40f0:8", ["const:bcf67c:8", "const:4:8"]]
- 00bcf67c ["CALL", null, ["callee:00c5dba0:8"]]
+ 00bcfaa4 ["INT_ADD", "register:40f0:8", ["const:bcfaa4:8", "const:4:8"]]
+ 00bcfaa4 ["CALL", null, ["callee:00c5dba0:8"]]
- 00bcf67c bytes 49380294
+ 00bcfaa4 bytes 3f380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa98bd266dea1de9906c71f584ff40c"></a>

### [`00bcf810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf810.md) → [`00bcfc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md) _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d940.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd40.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf810.md#insn-00bcf830) · [`00bcf844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf810.md#insn-00bcf844) · [`00bcf858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf810.md#insn-00bcf858)
- 新版 [`00bcfc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md#insn-00bcfc58) · [`00bcfc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md#insn-00bcfc6c) · [`00bcfc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md#insn-00bcfc80)

~~~diff
- 00bcf830 ["INT_ADD", "register:40f0:8", ["const:bcf830:8", "const:4:8"]]
- 00bcf830 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bcfc58 ["INT_ADD", "register:40f0:8", ["const:bcfc58:8", "const:4:8"]]
+ 00bcfc58 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bcf830 bytes 102c0294
+ 00bcfc58 bytes 062c0294
- 00bcf844 ["INT_ADD", "register:40f0:8", ["const:bcf844:8", "const:4:8"]]
- 00bcf844 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bcfc6c ["INT_ADD", "register:40f0:8", ["const:bcfc6c:8", "const:4:8"]]
+ 00bcfc6c ["CALL", null, ["callee:00c5ae00:8"]]
- 00bcf844 bytes 6f2c0294
+ 00bcfc6c bytes 652c0294
- 00bcf858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf858 ["INT_ADD", "register:40f0:8", ["const:bcf858:8", "const:4:8"]]
- 00bcf858 ["CALLIND", null, ["register:0:8"]]
+ 00bcfc80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfc80 ["INT_ADD", "register:40f0:8", ["const:bcfc80:8", "const:4:8"]]
+ 00bcfc80 ["CALLIND", null, ["register:0:8"]]
- 00bcf858 bytes 00013fd6
+ 00bcfc80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e713da92de405a214a90e18205d0aa0"></a>

### [`00bcf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) → [`00bcfcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bcde64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md) [`00bdb744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md) [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md)
- 新版 呼出元 2件 [`00bce28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce28c.md) [`00bdbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbb6c.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9f0.md) [`00c5aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa50.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md#insn-00bcf8c8) · [`00bcf8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md#insn-00bcf8d0) · [`00bcf8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md#insn-00bcf8d8)
- 新版 [`00bcfcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md#insn-00bcfcf0) · [`00bcfcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md#insn-00bcfcf8) · [`00bcfd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md#insn-00bcfd00)

~~~diff
- 00bcf8c8 ["INT_ADD", "register:40f0:8", ["const:bcf8c8:8", "const:4:8"]]
- 00bcf8c8 ["CALL", null, ["callee:00c5aa50:8"]]
+ 00bcfcf0 ["INT_ADD", "register:40f0:8", ["const:bcfcf0:8", "const:4:8"]]
+ 00bcfcf0 ["CALL", null, ["callee:00c5aa50:8"]]
- 00bcf8c8 bytes 622b0294
+ 00bcfcf0 bytes 582b0294
- 00bcf8d0 ["INT_ADD", "register:40f0:8", ["const:bcf8d0:8", "const:4:8"]]
- 00bcf8d0 ["CALL", null, ["callee:00c5a9f0:8"]]
+ 00bcfcf8 ["INT_ADD", "register:40f0:8", ["const:bcfcf8:8", "const:4:8"]]
+ 00bcfcf8 ["CALL", null, ["callee:00c5a9f0:8"]]
- 00bcf8d0 bytes 482b0294
+ 00bcfcf8 bytes 3e2b0294
- 00bcf8d8 ["INT_ADD", "register:40f0:8", ["const:bcf8d8:8", "const:4:8"]]
- 00bcf8d8 ["CALL", null, ["callee:00c5a9f0:8"]]
+ 00bcfd00 ["INT_ADD", "register:40f0:8", ["const:bcfd00:8", "const:4:8"]]
+ 00bcfd00 ["CALL", null, ["callee:00c5a9f0:8"]]
- 00bcf8d8 bytes 462b0294
+ 00bcfd00 bytes 3c2b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fa948f8a851bdc1e3b0aaba9349cd96"></a>

### [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) → [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) _ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00bcdca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md) [`00bce468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md) [`00bce6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md) [`00bce864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md) [`00bceaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d790.md)
- 新版 呼出元 8件 [`00bce0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md) [`00bce890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md) [`00bceb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md) [`00bcec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md) [`00bcef18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5db90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md#insn-00bcf954) · [`00bcf96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md#insn-00bcf96c) · [`00bcf994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md#insn-00bcf994)
- 新版 [`00bcfd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md#insn-00bcfd7c) · [`00bcfd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md#insn-00bcfd94) · [`00bcfdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md#insn-00bcfdbc)

~~~diff
- 00bcf954 ["INT_ADD", "register:40f0:8", ["const:bcf954:8", "const:4:8"]]
- 00bcf954 ["CALL", null, ["callee:00c5dd20:8"]]
+ 00bcfd7c ["INT_ADD", "register:40f0:8", ["const:bcfd7c:8", "const:4:8"]]
+ 00bcfd7c ["CALL", null, ["callee:00c5dd20:8"]]
- 00bcf954 bytes f3370294
+ 00bcfd7c bytes e9370294
- 00bcf96c ["INT_ADD", "register:40f0:8", ["const:bcf96c:8", "const:4:8"]]
- 00bcf96c ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bcfd94 ["INT_ADD", "register:40f0:8", ["const:bcfd94:8", "const:4:8"]]
+ 00bcfd94 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bcf96c bytes 252c0294
+ 00bcfd94 bytes 1b2c0294
- 00bcf994 ["INT_ADD", "register:40f0:8", ["const:bcf994:8", "const:4:8"]]
- 00bcf994 ["CALL", null, ["callee:00c5db90:8"]]
+ 00bcfdbc ["INT_ADD", "register:40f0:8", ["const:bcfdbc:8", "const:4:8"]]
+ 00bcfdbc ["CALL", null, ["callee:00c5db90:8"]]
- 00bcf994 bytes 7f370294
+ 00bcfdbc bytes 75370294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27ec8ed444ddc4d812c510f05d90c19f"></a>

### [`00bd4940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4940.md) → [`00bd4d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md) _ZN8firebase4auth18AdditionalUserInfoaSEOS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d970.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md) [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md)
- 新版 呼出元 1件 [`00c5dd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd70.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4940.md#insn-00bd4980) · [`00bd49d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4940.md#insn-00bd49d0) · [`00bd4a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4940.md#insn-00bd4a00)
- 新版 [`00bd4da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md#insn-00bd4da8) · [`00bd4df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md#insn-00bd4df8) · [`00bd4e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4d68.md#insn-00bd4e28)

~~~diff
- 00bd4980 ["INT_ADD", "register:40f0:8", ["const:bd4980:8", "const:4:8"]]
- 00bd4980 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bd4da8 ["INT_ADD", "register:40f0:8", ["const:bd4da8:8", "const:4:8"]]
+ 00bd4da8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bd4980 bytes 4c0c0294
+ 00bd4da8 bytes 420c0294
- 00bd49d0 ["INT_ADD", "register:40f0:8", ["const:bd49d0:8", "const:4:8"]]
- 00bd49d0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bd4df8 ["INT_ADD", "register:40f0:8", ["const:bd4df8:8", "const:4:8"]]
+ 00bd4df8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bd49d0 bytes 380c0294
+ 00bd4df8 bytes 2e0c0294
- 00bd4a00 ["INT_ADD", "register:40f0:8", ["const:bd4a00:8", "const:4:8"]]
- 00bd4a00 ["CALL", null, ["callee:00c5be20:8"]]
+ 00bd4e28 ["INT_ADD", "register:40f0:8", ["const:bd4e28:8", "const:4:8"]]
+ 00bd4e28 ["CALL", null, ["callee:00c5be20:8"]]
- 00bd4a00 bytes 081c0294
+ 00bd4e28 bytes fe1b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e8c49c0c61bd77b4e312d6e24552917"></a>

### [`00bd8e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e48.md) → [`00bd9270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9270.md) _ZN8firebase4auth10CredentialC2ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd8e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e48.md#insn-00bd8e6c)
- 新版 [`00bd9294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9270.md#insn-00bd9294)

~~~diff
- 00bd8e6c ["INT_ADD", "register:40f0:8", ["const:bd8e6c:8", "const:4:8"]]
- 00bd8e6c ["CALL", null, ["callee:00c5dd60:8"]]
+ 00bd9294 ["INT_ADD", "register:40f0:8", ["const:bd9294:8", "const:4:8"]]
+ 00bd9294 ["CALL", null, ["callee:00c5dd60:8"]]
- 00bd8e6c bytes bd120294
+ 00bd9294 bytes b3120294
~~~


<a id="compare-2e50d94e0b1850d215af137ebc49581f"></a>

### [`00bd92ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd92ec.md) → [`00bd9714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9714.md) _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da30.md) · 呼出先 2件 [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md)
- 新版 呼出元 1件 [`00c5de30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de30.md) · 呼出先 2件 [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd9300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd92ec.md#insn-00bd9300) · [`00bd932c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd92ec.md#insn-00bd932c)
- 新版 [`00bd9728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9714.md#insn-00bd9728) · [`00bd9754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9714.md#insn-00bd9754)

~~~diff
- 00bd9300 ["INT_ADD", "register:40f0:8", ["const:bd9300:8", "const:4:8"]]
- 00bd9300 ["CALL", null, ["callee:00c5dd60:8"]]
+ 00bd9728 ["INT_ADD", "register:40f0:8", ["const:bd9728:8", "const:4:8"]]
+ 00bd9728 ["CALL", null, ["callee:00c5dd60:8"]]
- 00bd9300 bytes 98110294
+ 00bd9728 bytes 8e110294
- 00bd932c ["INT_ADD", "register:40f0:8", ["const:bd932c:8", "const:4:8"]]
- 00bd932c ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00bd9754 ["INT_ADD", "register:40f0:8", ["const:bd9754:8", "const:4:8"]]
+ 00bd9754 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00bd932c bytes 61060294
+ 00bd9754 bytes 57060294
~~~


<a id="compare-1ed6941b10aff8f7ab691becee16675e"></a>

### [`00bda10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda10c.md) → [`00bda534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md) _ZN8firebase4auth22GameCenterAuthProvider23GetCredentialLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 8件 [`0087b37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda10c.md#insn-00bda130) · [`00bda140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda10c.md#insn-00bda140) · [`00bda14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda10c.md#insn-00bda14c)
- 新版 [`00bda558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md#insn-00bda558) · [`00bda568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md#insn-00bda568) · [`00bda574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda534.md#insn-00bda574)

~~~diff
- 00bda130 ["INT_ADD", "register:40f0:8", ["const:bda130:8", "const:4:8"]]
- 00bda130 ["CALL", null, ["callee:00c5db50:8"]]
+ 00bda558 ["INT_ADD", "register:40f0:8", ["const:bda558:8", "const:4:8"]]
+ 00bda558 ["CALL", null, ["callee:00c5db50:8"]]
- 00bda130 bytes 880d0294
+ 00bda558 bytes 7e0d0294
- 00bda140 ["INT_ADD", "register:40f0:8", ["const:bda140:8", "const:4:8"]]
- 00bda140 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bda568 ["INT_ADD", "register:40f0:8", ["const:bda568:8", "const:4:8"]]
+ 00bda568 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bda140 bytes 30010294
+ 00bda568 bytes 26010294
- 00bda14c ["INT_ADD", "register:40f0:8", ["const:bda14c:8", "const:4:8"]]
- 00bda14c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bda574 ["INT_ADD", "register:40f0:8", ["const:bda574:8", "const:4:8"]]
+ 00bda574 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bda14c bytes 31010294
+ 00bda574 bytes 27010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9a0b7d1d2168173a8b8b89a3d665b9"></a>

### [`00bda250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda250.md) → [`00bda678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda678.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda250.md#insn-00bda264)
- 新版 [`00bda68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda678.md#insn-00bda68c)

~~~diff
- 00bda264 ["INT_ADD", "register:40f0:8", ["const:bda264:8", "const:4:8"]]
- 00bda264 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bda68c ["INT_ADD", "register:40f0:8", ["const:bda68c:8", "const:4:8"]]
+ 00bda68c ["CALL", null, ["callee:00c57e90:8"]]
- 00bda264 bytes 0bf60194
+ 00bda68c bytes 01f60194
~~~


<a id="compare-0c5668f29304daa9834652f4aa4cd2d4"></a>

### [`00bda2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda2e8.md) → [`00bda710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda710.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC1ERKS2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda2e8.md#insn-00bda300)
- 新版 [`00bda728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda710.md#insn-00bda728)

~~~diff
- 00bda300 ["INT_ADD", "register:40f0:8", ["const:bda300:8", "const:4:8"]]
- 00bda300 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bda728 ["INT_ADD", "register:40f0:8", ["const:bda728:8", "const:4:8"]]
+ 00bda728 ["CALL", null, ["callee:00c57e90:8"]]
- 00bda300 bytes e4f50194
+ 00bda728 bytes daf50194
~~~


<a id="compare-7dee335f5822380e6d75e40b53a27043"></a>

### [`00bda3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3c4.md) → [`00bda7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda7ec.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3c4.md#insn-00bda3e0)
- 新版 [`00bda808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda7ec.md#insn-00bda808)

~~~diff
- 00bda3e0 ["INT_ADD", "register:40f0:8", ["const:bda3e0:8", "const:4:8"]]
- 00bda3e0 ["CALL", null, ["callee:00c5de40:8"]]
+ 00bda808 ["INT_ADD", "register:40f0:8", ["const:bda808:8", "const:4:8"]]
+ 00bda808 ["CALL", null, ["callee:00c5de40:8"]]
- 00bda3e0 bytes 980d0294
+ 00bda808 bytes 8e0d0294
~~~


<a id="compare-b279b91d77c930ab5ce6c51566a31f4f"></a>

### [`00bdaeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md) → [`00bdb2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md) _ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdaee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md#insn-00bdaee0) · [`00bdaef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md#insn-00bdaef4) · [`00bdaf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaeb8.md#insn-00bdaf04)
- 新版 [`00bdb308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md#insn-00bdb308) · [`00bdb31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md#insn-00bdb31c) · [`00bdb32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md#insn-00bdb32c)

~~~diff
- 00bdaee0 ["INT_ADD", "register:40f0:8", ["const:bdaee0:8", "const:4:8"]]
- 00bdaee0 ["CALL", null, ["callee:00c5af20:8"]]
+ 00bdb308 ["INT_ADD", "register:40f0:8", ["const:bdb308:8", "const:4:8"]]
+ 00bdb308 ["CALL", null, ["callee:00c5af20:8"]]
- 00bdaee0 bytes 10ff0194
+ 00bdb308 bytes 06ff0194
- 00bdaef4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdaef4 ["INT_ADD", "register:40f0:8", ["const:bdaef4:8", "const:4:8"]]
- 00bdaef4 ["CALLIND", null, ["register:0:8"]]
+ 00bdb31c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdb31c ["INT_ADD", "register:40f0:8", ["const:bdb31c:8", "const:4:8"]]
+ 00bdb31c ["CALLIND", null, ["register:0:8"]]
- 00bdaef4 bytes 00013fd6
+ 00bdb31c bytes 00013fd6
- 00bdaf04 ["INT_ADD", "register:40f0:8", ["const:bdaf04:8", "const:4:8"]]
- 00bdaf04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bdb32c ["INT_ADD", "register:40f0:8", ["const:bdb32c:8", "const:4:8"]]
+ 00bdb32c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bdaf04 bytes ebf20194
+ 00bdb32c bytes e1f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d5d7f112eea494db1ed16439543116c"></a>

### [`00bdb0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb0c8.md) → [`00bdb4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md) _ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdb0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb0c8.md#insn-00bdb0f0) · [`00bdb104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb0c8.md#insn-00bdb104) · [`00bdb114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb0c8.md#insn-00bdb114)
- 新版 [`00bdb518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md#insn-00bdb518) · [`00bdb52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md#insn-00bdb52c) · [`00bdb53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb4f0.md#insn-00bdb53c)

~~~diff
- 00bdb0f0 ["INT_ADD", "register:40f0:8", ["const:bdb0f0:8", "const:4:8"]]
- 00bdb0f0 ["CALL", null, ["callee:00c5b390:8"]]
+ 00bdb518 ["INT_ADD", "register:40f0:8", ["const:bdb518:8", "const:4:8"]]
+ 00bdb518 ["CALL", null, ["callee:00c5b390:8"]]
- 00bdb0f0 bytes a8ff0194
+ 00bdb518 bytes 9eff0194
- 00bdb104 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdb104 ["INT_ADD", "register:40f0:8", ["const:bdb104:8", "const:4:8"]]
- 00bdb104 ["CALLIND", null, ["register:0:8"]]
+ 00bdb52c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdb52c ["INT_ADD", "register:40f0:8", ["const:bdb52c:8", "const:4:8"]]
+ 00bdb52c ["CALLIND", null, ["register:0:8"]]
- 00bdb104 bytes 00013fd6
+ 00bdb52c bytes 00013fd6
- 00bdb114 ["INT_ADD", "register:40f0:8", ["const:bdb114:8", "const:4:8"]]
- 00bdb114 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bdb53c ["INT_ADD", "register:40f0:8", ["const:bdb53c:8", "const:4:8"]]
+ 00bdb53c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bdb114 bytes 67f20194
+ 00bdb53c bytes 5df20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbba2036de62758f13459c2a4fcf4c4f"></a>

### [`00bdc000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc000.md) → [`00bdc428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc428.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd9fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9fe8.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5da00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da00.md)
- 新版 呼出元 1件 [`00bda410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5de00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc000.md#insn-00bdc014)
- 新版 [`00bdc43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc428.md#insn-00bdc43c)

~~~diff
- 00bdc014 ["INT_ADD", "register:40f0:8", ["const:bdc014:8", "const:4:8"]]
- 00bdc014 ["CALL", null, ["callee:00c5de00:8"]]
+ 00bdc43c ["INT_ADD", "register:40f0:8", ["const:bdc43c:8", "const:4:8"]]
+ 00bdc43c ["CALL", null, ["callee:00c5de00:8"]]
- 00bdc014 bytes 7b060294
+ 00bdc43c bytes 71060294
~~~


<a id="compare-7846eff7d206b80389eab9935e167f18"></a>

### [`00bdc998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc998.md) → [`00bdcdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcdc0.md) _ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5de30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc998.md#insn-00bdc9bc)
- 新版 [`00bdcde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcdc0.md#insn-00bdcde4)

~~~diff
- 00bdc9bc ["INT_ADD", "register:40f0:8", ["const:bdc9bc:8", "const:4:8"]]
- 00bdc9bc ["CALL", null, ["callee:00c5de30:8"]]
+ 00bdcde4 ["INT_ADD", "register:40f0:8", ["const:bdcde4:8", "const:4:8"]]
+ 00bdcde4 ["CALL", null, ["callee:00c5de30:8"]]
- 00bdc9bc bytes 1d040294
+ 00bdcde4 bytes 13040294
~~~


<a id="compare-7b2582018aa4a0e335113c420b217731"></a>

### [`00bde650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde650.md) → [`00bdea78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEbP7_JNIEnvPNS_26Refere

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dab0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d910.md)
- 新版 呼出元 1件 [`00c5deb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5deb0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bde684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde650.md#insn-00bde684) · [`00bde698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde650.md#insn-00bde698) · [`00bde6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde650.md#insn-00bde6c4)
- 新版 [`00bdeaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md#insn-00bdeaac) · [`00bdeac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md#insn-00bdeac0) · [`00bdeaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdea78.md#insn-00bdeaec)

~~~diff
- 00bde684 ["INT_ADD", "register:40f0:8", ["const:bde684:8", "const:4:8"]]
- 00bde684 ["CALL", null, ["callee:00c5dd10:8"]]
+ 00bdeaac ["INT_ADD", "register:40f0:8", ["const:bdeaac:8", "const:4:8"]]
+ 00bdeaac ["CALL", null, ["callee:00c5dd10:8"]]
- 00bde684 bytes a3fc0194
+ 00bdeaac bytes 99fc0194
- 00bde698 ["INT_ADD", "register:40f0:8", ["const:bde698:8", "const:4:8"]]
- 00bde698 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bdeac0 ["INT_ADD", "register:40f0:8", ["const:bdeac0:8", "const:4:8"]]
+ 00bdeac0 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bde698 bytes daf00194
+ 00bdeac0 bytes d0f00194
- 00bde6c4 ["INT_ADD", "register:40f0:8", ["const:bde6c4:8", "const:4:8"]]
- 00bde6c4 ["CALL", null, ["callee:00c5de90:8"]]
+ 00bdeaec ["INT_ADD", "register:40f0:8", ["const:bdeaec:8", "const:4:8"]]
+ 00bdeaec ["CALL", null, ["callee:00c5de90:8"]]
- 00bde6c4 bytes f3fc0194
+ 00bdeaec bytes e9fc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba76ca55e6fe1737ac0daf2475ecd01d"></a>

### [`00be0f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0f8c.md) → [`00be13b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md) _ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureR

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde3f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d920.md)
- 新版 呼出元 1件 [`00bde818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde818.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be0fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0f8c.md#insn-00be0fc4) · [`00be0fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0f8c.md#insn-00be0fdc) · [`00be1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0f8c.md#insn-00be1004)
- 新版 [`00be13ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md#insn-00be13ec) · [`00be1404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md#insn-00be1404) · [`00be142c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be13b4.md#insn-00be142c)

~~~diff
- 00be0fc4 ["INT_ADD", "register:40f0:8", ["const:be0fc4:8", "const:4:8"]]
- 00be0fc4 ["CALL", null, ["callee:00c5dd20:8"]]
+ 00be13ec ["INT_ADD", "register:40f0:8", ["const:be13ec:8", "const:4:8"]]
+ 00be13ec ["CALL", null, ["callee:00c5dd20:8"]]
- 00be0fc4 bytes 57f20194
+ 00be13ec bytes 4df20194
- 00be0fdc ["INT_ADD", "register:40f0:8", ["const:be0fdc:8", "const:4:8"]]
- 00be0fdc ["CALL", null, ["callee:00c5ae00:8"]]
+ 00be1404 ["INT_ADD", "register:40f0:8", ["const:be1404:8", "const:4:8"]]
+ 00be1404 ["CALL", null, ["callee:00c5ae00:8"]]
- 00be0fdc bytes 89e60194
+ 00be1404 bytes 7fe60194
- 00be1004 ["INT_ADD", "register:40f0:8", ["const:be1004:8", "const:4:8"]]
- 00be1004 ["CALL", null, ["callee:00c5de80:8"]]
+ 00be142c ["INT_ADD", "register:40f0:8", ["const:be142c:8", "const:4:8"]]
+ 00be142c ["CALL", null, ["callee:00c5de80:8"]]
- 00be1004 bytes 9ff20194
+ 00be142c bytes 95f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f908acf8792537a7aa50cb17a7b499b9"></a>

### [`00be1300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1300.md) → [`00be1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dac0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md) [`00c5daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daa0.md)
- 新版 呼出元 1件 [`00c5dec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dec0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md) [`00c5dea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be139c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1300.md#insn-00be139c) · [`00be13b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1300.md#insn-00be13b4) · [`00be13d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1300.md#insn-00be13d4)
- 新版 [`00be17c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md#insn-00be17c4) · [`00be17dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md#insn-00be17dc) · [`00be17fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1728.md#insn-00be17fc)

~~~diff
- 00be139c ["INT_ADD", "register:40f0:8", ["const:be139c:8", "const:4:8"]]
- 00be139c ["CALL", null, ["callee:00c57e90:8"]]
+ 00be17c4 ["INT_ADD", "register:40f0:8", ["const:be17c4:8", "const:4:8"]]
+ 00be17c4 ["CALL", null, ["callee:00c57e90:8"]]
- 00be139c bytes bdd90194
+ 00be17c4 bytes b3d90194
- 00be13b4 ["INT_ADD", "register:40f0:8", ["const:be13b4:8", "const:4:8"]]
- 00be13b4 ["CALL", null, ["callee:00c5dea0:8"]]
+ 00be17dc ["INT_ADD", "register:40f0:8", ["const:be17dc:8", "const:4:8"]]
+ 00be17dc ["CALL", null, ["callee:00c5dea0:8"]]
- 00be13b4 bytes bbf10194
+ 00be17dc bytes b1f10194
- 00be13d4 ["INT_ADD", "register:40f0:8", ["const:be13d4:8", "const:4:8"]]
- 00be13d4 ["CALL", null, ["callee:00c5dea0:8"]]
+ 00be17fc ["INT_ADD", "register:40f0:8", ["const:be17fc:8", "const:4:8"]]
+ 00be17fc ["CALL", null, ["callee:00c5dea0:8"]]
- 00be13d4 bytes b3f10194
+ 00be17fc bytes a9f10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28fff1984ccaa4f7aae96f3302304bc"></a>

### [`00be14b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be14b0.md) → [`00be18d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md) _ZNK8firebase4auth4User18GetTokenLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be14d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be14b0.md#insn-00be14d0) · [`00be14dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be14b0.md#insn-00be14dc) · [`00be14e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be14b0.md#insn-00be14e8)
- 新版 [`00be18f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md#insn-00be18f8) · [`00be1904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md#insn-00be1904) · [`00be1910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be18d8.md#insn-00be1910)

~~~diff
- 00be14d0 ["INT_ADD", "register:40f0:8", ["const:be14d0:8", "const:4:8"]]
- 00be14d0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be18f8 ["INT_ADD", "register:40f0:8", ["const:be18f8:8", "const:4:8"]]
+ 00be18f8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be14d0 bytes 4ce40194
+ 00be18f8 bytes 42e40194
- 00be14dc ["INT_ADD", "register:40f0:8", ["const:be14dc:8", "const:4:8"]]
- 00be14dc ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1904 ["INT_ADD", "register:40f0:8", ["const:be1904:8", "const:4:8"]]
+ 00be1904 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be14dc bytes 4de40194
+ 00be1904 bytes 43e40194
- 00be14e8 ["INT_ADD", "register:40f0:8", ["const:be14e8:8", "const:4:8"]]
- 00be14e8 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1910 ["INT_ADD", "register:40f0:8", ["const:be1910:8", "const:4:8"]]
+ 00be1910 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be14e8 bytes e2e40194
+ 00be1910 bytes d8e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb63917c7a667b35c4a1da66f304c82"></a>

### [`00be1540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1540.md) → [`00be1968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md) _ZNK8firebase4auth4User24UpdatePasswordLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1540.md#insn-00be1560) · [`00be156c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1540.md#insn-00be156c) · [`00be1578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1540.md#insn-00be1578)
- 新版 [`00be1988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md#insn-00be1988) · [`00be1994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md#insn-00be1994) · [`00be19a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1968.md#insn-00be19a0)

~~~diff
- 00be1560 ["INT_ADD", "register:40f0:8", ["const:be1560:8", "const:4:8"]]
- 00be1560 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1988 ["INT_ADD", "register:40f0:8", ["const:be1988:8", "const:4:8"]]
+ 00be1988 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1560 bytes 28e40194
+ 00be1988 bytes 1ee40194
- 00be156c ["INT_ADD", "register:40f0:8", ["const:be156c:8", "const:4:8"]]
- 00be156c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1994 ["INT_ADD", "register:40f0:8", ["const:be1994:8", "const:4:8"]]
+ 00be1994 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be156c bytes 29e40194
+ 00be1994 bytes 1fe40194
- 00be1578 ["INT_ADD", "register:40f0:8", ["const:be1578:8", "const:4:8"]]
- 00be1578 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be19a0 ["INT_ADD", "register:40f0:8", ["const:be19a0:8", "const:4:8"]]
+ 00be19a0 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1578 bytes bee40194
+ 00be19a0 bytes b4e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21106d143c11f2985e2c71ffac64d4d9"></a>

### [`00be15d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be15d0.md) → [`00be19f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md) _ZNK8firebase4auth4User28LinkWithCredentialLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be15f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be15d0.md#insn-00be15f0) · [`00be15fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be15d0.md#insn-00be15fc) · [`00be1608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be15d0.md#insn-00be1608)
- 新版 [`00be1a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md#insn-00be1a18) · [`00be1a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md#insn-00be1a24) · [`00be1a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be19f8.md#insn-00be1a30)

~~~diff
- 00be15f0 ["INT_ADD", "register:40f0:8", ["const:be15f0:8", "const:4:8"]]
- 00be15f0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1a18 ["INT_ADD", "register:40f0:8", ["const:be1a18:8", "const:4:8"]]
+ 00be1a18 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be15f0 bytes 04e40194
+ 00be1a18 bytes fae30194
- 00be15fc ["INT_ADD", "register:40f0:8", ["const:be15fc:8", "const:4:8"]]
- 00be15fc ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1a24 ["INT_ADD", "register:40f0:8", ["const:be1a24:8", "const:4:8"]]
+ 00be1a24 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be15fc bytes 05e40194
+ 00be1a24 bytes fbe30194
- 00be1608 ["INT_ADD", "register:40f0:8", ["const:be1608:8", "const:4:8"]]
- 00be1608 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1a30 ["INT_ADD", "register:40f0:8", ["const:be1a30:8", "const:4:8"]]
+ 00be1a30 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1608 bytes 9ae40194
+ 00be1a30 bytes 90e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b12ec71184044b4194044fbc313e4939"></a>

### [`00be1660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1660.md) → [`00be1a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md) _ZNK8firebase4auth4User24ReauthenticateLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1660.md#insn-00be1680) · [`00be168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1660.md#insn-00be168c) · [`00be1698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1660.md#insn-00be1698)
- 新版 [`00be1aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md#insn-00be1aa8) · [`00be1ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md#insn-00be1ab4) · [`00be1ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1a88.md#insn-00be1ac0)

~~~diff
- 00be1680 ["INT_ADD", "register:40f0:8", ["const:be1680:8", "const:4:8"]]
- 00be1680 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1aa8 ["INT_ADD", "register:40f0:8", ["const:be1aa8:8", "const:4:8"]]
+ 00be1aa8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1680 bytes e0e30194
+ 00be1aa8 bytes d6e30194
- 00be168c ["INT_ADD", "register:40f0:8", ["const:be168c:8", "const:4:8"]]
- 00be168c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1ab4 ["INT_ADD", "register:40f0:8", ["const:be1ab4:8", "const:4:8"]]
+ 00be1ab4 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be168c bytes e1e30194
+ 00be1ab4 bytes d7e30194
- 00be1698 ["INT_ADD", "register:40f0:8", ["const:be1698:8", "const:4:8"]]
- 00be1698 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1ac0 ["INT_ADD", "register:40f0:8", ["const:be1ac0:8", "const:4:8"]]
+ 00be1ac0 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1698 bytes 76e40194
+ 00be1ac0 bytes 6ce40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-088fd7b9587ae9359aa95a5bfd30bdff"></a>

### [`00be16f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be16f0.md) → [`00be1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md) _ZNK8firebase4auth4User39ReauthenticateAndRetrieveDataLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be16f0.md#insn-00be1710) · [`00be171c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be16f0.md#insn-00be171c) · [`00be1728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be16f0.md#insn-00be1728)
- 新版 [`00be1b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md#insn-00be1b38) · [`00be1b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md#insn-00be1b44) · [`00be1b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1b18.md#insn-00be1b50)

~~~diff
- 00be1710 ["INT_ADD", "register:40f0:8", ["const:be1710:8", "const:4:8"]]
- 00be1710 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1b38 ["INT_ADD", "register:40f0:8", ["const:be1b38:8", "const:4:8"]]
+ 00be1b38 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1710 bytes bce30194
+ 00be1b38 bytes b2e30194
- 00be171c ["INT_ADD", "register:40f0:8", ["const:be171c:8", "const:4:8"]]
- 00be171c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1b44 ["INT_ADD", "register:40f0:8", ["const:be1b44:8", "const:4:8"]]
+ 00be1b44 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be171c bytes bde30194
+ 00be1b44 bytes b3e30194
- 00be1728 ["INT_ADD", "register:40f0:8", ["const:be1728:8", "const:4:8"]]
- 00be1728 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1b50 ["INT_ADD", "register:40f0:8", ["const:be1b50:8", "const:4:8"]]
+ 00be1b50 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1728 bytes 52e40194
+ 00be1b50 bytes 48e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31b391ffd4095625676918ceae026150"></a>

### [`00be1780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1780.md) → [`00be1ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md) _ZNK8firebase4auth4User31SendEmailVerificationLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1780.md#insn-00be17a0) · [`00be17ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1780.md#insn-00be17ac) · [`00be17b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1780.md#insn-00be17b8)
- 新版 [`00be1bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md#insn-00be1bc8) · [`00be1bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md#insn-00be1bd4) · [`00be1be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1ba8.md#insn-00be1be0)

~~~diff
- 00be17a0 ["INT_ADD", "register:40f0:8", ["const:be17a0:8", "const:4:8"]]
- 00be17a0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1bc8 ["INT_ADD", "register:40f0:8", ["const:be1bc8:8", "const:4:8"]]
+ 00be1bc8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be17a0 bytes 98e30194
+ 00be1bc8 bytes 8ee30194
- 00be17ac ["INT_ADD", "register:40f0:8", ["const:be17ac:8", "const:4:8"]]
- 00be17ac ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1bd4 ["INT_ADD", "register:40f0:8", ["const:be1bd4:8", "const:4:8"]]
+ 00be1bd4 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be17ac bytes 99e30194
+ 00be1bd4 bytes 8fe30194
- 00be17b8 ["INT_ADD", "register:40f0:8", ["const:be17b8:8", "const:4:8"]]
- 00be17b8 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1be0 ["INT_ADD", "register:40f0:8", ["const:be1be0:8", "const:4:8"]]
+ 00be1be0 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be17b8 bytes 2ee40194
+ 00be1be0 bytes 24e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3c5cfe4b6099939a2119d3854e8c1a8"></a>

### [`00be1810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1810.md) → [`00be1c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md) _ZNK8firebase4auth4User50SendEmailVerificationBeforeUpdatingEmailLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1810.md#insn-00be1830) · [`00be183c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1810.md#insn-00be183c) · [`00be1848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1810.md#insn-00be1848)
- 新版 [`00be1c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md#insn-00be1c58) · [`00be1c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md#insn-00be1c64) · [`00be1c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1c38.md#insn-00be1c70)

~~~diff
- 00be1830 ["INT_ADD", "register:40f0:8", ["const:be1830:8", "const:4:8"]]
- 00be1830 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1c58 ["INT_ADD", "register:40f0:8", ["const:be1c58:8", "const:4:8"]]
+ 00be1c58 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1830 bytes 74e30194
+ 00be1c58 bytes 6ae30194
- 00be183c ["INT_ADD", "register:40f0:8", ["const:be183c:8", "const:4:8"]]
- 00be183c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1c64 ["INT_ADD", "register:40f0:8", ["const:be1c64:8", "const:4:8"]]
+ 00be1c64 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be183c bytes 75e30194
+ 00be1c64 bytes 6be30194
- 00be1848 ["INT_ADD", "register:40f0:8", ["const:be1848:8", "const:4:8"]]
- 00be1848 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1c70 ["INT_ADD", "register:40f0:8", ["const:be1c70:8", "const:4:8"]]
+ 00be1c70 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1848 bytes 0ae40194
+ 00be1c70 bytes 00e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc394ac7d1a75e49e9d35df0505dfeb0"></a>

### [`00be18a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be18a0.md) → [`00be1cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md) _ZNK8firebase4auth4User16UnlinkLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be18a0.md#insn-00be18c0) · [`00be18cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be18a0.md#insn-00be18cc) · [`00be18d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be18a0.md#insn-00be18d8)
- 新版 [`00be1ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md#insn-00be1ce8) · [`00be1cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md#insn-00be1cf4) · [`00be1d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1cc8.md#insn-00be1d00)

~~~diff
- 00be18c0 ["INT_ADD", "register:40f0:8", ["const:be18c0:8", "const:4:8"]]
- 00be18c0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1ce8 ["INT_ADD", "register:40f0:8", ["const:be1ce8:8", "const:4:8"]]
+ 00be1ce8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be18c0 bytes 50e30194
+ 00be1ce8 bytes 46e30194
- 00be18cc ["INT_ADD", "register:40f0:8", ["const:be18cc:8", "const:4:8"]]
- 00be18cc ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1cf4 ["INT_ADD", "register:40f0:8", ["const:be1cf4:8", "const:4:8"]]
+ 00be1cf4 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be18cc bytes 51e30194
+ 00be1cf4 bytes 47e30194
- 00be18d8 ["INT_ADD", "register:40f0:8", ["const:be18d8:8", "const:4:8"]]
- 00be18d8 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1d00 ["INT_ADD", "register:40f0:8", ["const:be1d00:8", "const:4:8"]]
+ 00be1d00 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be18d8 bytes e6e30194
+ 00be1d00 bytes dce30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c79b46827fca160d9f35eb835eb5864f"></a>

### [`00be1930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1930.md) → [`00be1d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md) _ZNK8firebase4auth4User27UpdateUserProfileLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1930.md#insn-00be1950) · [`00be195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1930.md#insn-00be195c) · [`00be1968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1930.md#insn-00be1968)
- 新版 [`00be1d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md#insn-00be1d78) · [`00be1d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md#insn-00be1d84) · [`00be1d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1d58.md#insn-00be1d90)

~~~diff
- 00be1950 ["INT_ADD", "register:40f0:8", ["const:be1950:8", "const:4:8"]]
- 00be1950 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1d78 ["INT_ADD", "register:40f0:8", ["const:be1d78:8", "const:4:8"]]
+ 00be1d78 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1950 bytes 2ce30194
+ 00be1d78 bytes 22e30194
- 00be195c ["INT_ADD", "register:40f0:8", ["const:be195c:8", "const:4:8"]]
- 00be195c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1d84 ["INT_ADD", "register:40f0:8", ["const:be1d84:8", "const:4:8"]]
+ 00be1d84 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be195c bytes 2de30194
+ 00be1d84 bytes 23e30194
- 00be1968 ["INT_ADD", "register:40f0:8", ["const:be1968:8", "const:4:8"]]
- 00be1968 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1d90 ["INT_ADD", "register:40f0:8", ["const:be1d90:8", "const:4:8"]]
+ 00be1d90 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1968 bytes c2e30194
+ 00be1d90 bytes b8e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a869624ecb5d145e6f47ff395b4ec18"></a>

### [`00be19c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be19c0.md) → [`00be1de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md) _ZNK8firebase4auth4User16ReloadLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be19e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be19c0.md#insn-00be19e0) · [`00be19ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be19c0.md#insn-00be19ec) · [`00be19f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be19c0.md#insn-00be19f8)
- 新版 [`00be1e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md#insn-00be1e08) · [`00be1e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md#insn-00be1e14) · [`00be1e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1de8.md#insn-00be1e20)

~~~diff
- 00be19e0 ["INT_ADD", "register:40f0:8", ["const:be19e0:8", "const:4:8"]]
- 00be19e0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1e08 ["INT_ADD", "register:40f0:8", ["const:be1e08:8", "const:4:8"]]
+ 00be1e08 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be19e0 bytes 08e30194
+ 00be1e08 bytes fee20194
- 00be19ec ["INT_ADD", "register:40f0:8", ["const:be19ec:8", "const:4:8"]]
- 00be19ec ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1e14 ["INT_ADD", "register:40f0:8", ["const:be1e14:8", "const:4:8"]]
+ 00be1e14 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be19ec bytes 09e30194
+ 00be1e14 bytes ffe20194
- 00be19f8 ["INT_ADD", "register:40f0:8", ["const:be19f8:8", "const:4:8"]]
- 00be19f8 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1e20 ["INT_ADD", "register:40f0:8", ["const:be1e20:8", "const:4:8"]]
+ 00be1e20 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be19f8 bytes 9ee30194
+ 00be1e20 bytes 94e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4acdc90616250b832a397a217597e401"></a>

### [`00be1a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1a50.md) → [`00be1e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md) _ZNK8firebase4auth4User16DeleteLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1a50.md#insn-00be1a70) · [`00be1a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1a50.md#insn-00be1a7c) · [`00be1a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1a50.md#insn-00be1a88)
- 新版 [`00be1e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md#insn-00be1e98) · [`00be1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md#insn-00be1ea4) · [`00be1eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1e78.md#insn-00be1eb0)

~~~diff
- 00be1a70 ["INT_ADD", "register:40f0:8", ["const:be1a70:8", "const:4:8"]]
- 00be1a70 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1e98 ["INT_ADD", "register:40f0:8", ["const:be1e98:8", "const:4:8"]]
+ 00be1e98 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1a70 bytes e4e20194
+ 00be1e98 bytes dae20194
- 00be1a7c ["INT_ADD", "register:40f0:8", ["const:be1a7c:8", "const:4:8"]]
- 00be1a7c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1ea4 ["INT_ADD", "register:40f0:8", ["const:be1ea4:8", "const:4:8"]]
+ 00be1ea4 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be1a7c bytes e5e20194
+ 00be1ea4 bytes dbe20194
- 00be1a88 ["INT_ADD", "register:40f0:8", ["const:be1a88:8", "const:4:8"]]
- 00be1a88 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1eb0 ["INT_ADD", "register:40f0:8", ["const:be1eb0:8", "const:4:8"]]
+ 00be1eb0 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1a88 bytes 7ae30194
+ 00be1eb0 bytes 70e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9b7f5af862fa5fb0de4f2dded5b11e2"></a>

### [`00be1ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1ae0.md) → [`00be1f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md) _ZNK8firebase4auth4User37UpdatePhoneNumberCredentialLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1ae0.md#insn-00be1b00) · [`00be1b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1ae0.md#insn-00be1b0c) · [`00be1b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1ae0.md#insn-00be1b18)
- 新版 [`00be1f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md#insn-00be1f28) · [`00be1f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md#insn-00be1f34) · [`00be1f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md#insn-00be1f40)

~~~diff
- 00be1b00 ["INT_ADD", "register:40f0:8", ["const:be1b00:8", "const:4:8"]]
- 00be1b00 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1f28 ["INT_ADD", "register:40f0:8", ["const:be1f28:8", "const:4:8"]]
+ 00be1f28 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1b00 bytes c0e20194
+ 00be1f28 bytes b6e20194
- 00be1b0c ["INT_ADD", "register:40f0:8", ["const:be1b0c:8", "const:4:8"]]
- 00be1b0c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00be1f34 ["INT_ADD", "register:40f0:8", ["const:be1f34:8", "const:4:8"]]
+ 00be1f34 ["CALL", null, ["callee:00c5aa10:8"]]
- 00be1b0c bytes c1e20194
+ 00be1f34 bytes b7e20194
- 00be1b18 ["INT_ADD", "register:40f0:8", ["const:be1b18:8", "const:4:8"]]
- 00be1b18 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be1f40 ["INT_ADD", "register:40f0:8", ["const:be1f40:8", "const:4:8"]]
+ 00be1f40 ["CALL", null, ["callee:00c5ac70:8"]]
- 00be1b18 bytes 56e30194
+ 00be1f40 bytes 4ce30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae1cb9aba3bede4f3c6962a77272a5a6"></a>

### [`00be1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1b70.md) → [`00be1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md) _ZN8firebase4auth4User18GetTokenThreadSafeEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0087b37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a670.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1b70.md#insn-00be1ba0) · [`00be1ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1b70.md#insn-00be1ba8) · [`00be1bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1b70.md#insn-00be1bc4)
- 新版 [`00be1fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md#insn-00be1fc8) · [`00be1fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md#insn-00be1fd0) · [`00be1fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md#insn-00be1fec)

~~~diff
- 00be1ba0 ["INT_ADD", "register:40f0:8", ["const:be1ba0:8", "const:4:8"]]
- 00be1ba0 ["CALL", null, ["callee:00c5aa70:8"]]
+ 00be1fc8 ["INT_ADD", "register:40f0:8", ["const:be1fc8:8", "const:4:8"]]
+ 00be1fc8 ["CALL", null, ["callee:00c5aa70:8"]]
- 00be1ba0 bytes b4e20194
+ 00be1fc8 bytes aae20194
- 00be1ba8 ["INT_ADD", "register:40f0:8", ["const:be1ba8:8", "const:4:8"]]
- 00be1ba8 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be1fd0 ["INT_ADD", "register:40f0:8", ["const:be1fd0:8", "const:4:8"]]
+ 00be1fd0 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1ba8 bytes 96e20194
+ 00be1fd0 bytes 8ce20194
- 00be1bc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00be1bc4 ["INT_ADD", "register:40f0:8", ["const:be1bc4:8", "const:4:8"]]
- 00be1bc4 ["CALLIND", null, ["register:0:8"]]
+ 00be1fec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00be1fec ["INT_ADD", "register:40f0:8", ["const:be1fec:8", "const:4:8"]]
+ 00be1fec ["CALLIND", null, ["register:0:8"]]
- 00be1bc4 bytes 00013fd6
+ 00be1fec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c729b2593de4a3daa2a1cb6d2eef27"></a>

### [`00be1db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1db8.md) → [`00be21e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be21e0.md) _ZN8firebase4auth17UserInfoInterfaceD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1db8.md#insn-00be1dc8)
- 新版 [`00be21f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be21e0.md#insn-00be21f0)

~~~diff
- 00be1dc8 ["INT_ADD", "register:40f0:8", ["const:be1dc8:8", "const:4:8"]]
- 00be1dc8 ["CALL", null, ["callee:00c5db80:8"]]
+ 00be21f0 ["INT_ADD", "register:40f0:8", ["const:be21f0:8", "const:4:8"]]
+ 00be21f0 ["CALL", null, ["callee:00c5db80:8"]]
- 00be1dc8 bytes 6eee0194
+ 00be21f0 bytes 64ee0194
~~~


<a id="compare-4f92cae6831938f7505141e6b3eae20d"></a>

### [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) → [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) FUN_00be8658

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00be8210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8210.md) [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) · 呼出先 5件 [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) [`00beeaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md) [`00beef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md) [`00bef16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef16c.md) [`00c52fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52fa0.md)
- 新版 呼出元 2件 [`00be8638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8638.md) [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) · 呼出先 5件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) [`00beef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) [`00bef33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md) [`00bef594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md) [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be82d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md#insn-00be82d4) · [`00be82e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md#insn-00be82e0) · [`00be8304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md#insn-00be8304)
- 新版 [`00be86fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md#insn-00be86fc) · [`00be8708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md#insn-00be8708) · [`00be872c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md#insn-00be872c)

~~~diff
- 00be82d4 ["INT_ADD", "register:40f0:8", ["const:be82d4:8", "const:4:8"]]
- 00be82d4 ["CALL", null, ["callee:00c533c8:8"]]
+ 00be86fc ["INT_ADD", "register:40f0:8", ["const:be86fc:8", "const:4:8"]]
+ 00be86fc ["CALL", null, ["callee:00c533c8:8"]]
- 00be82d4 bytes 33ab0194
+ 00be86fc bytes 33ab0194
- 00be82e0 ["INT_ADD", "register:40f0:8", ["const:be82e0:8", "const:4:8"]]
- 00be82e0 ["CALL", null, ["callee:00c533c8:8"]]
+ 00be8708 ["INT_ADD", "register:40f0:8", ["const:be8708:8", "const:4:8"]]
+ 00be8708 ["CALL", null, ["callee:00c533c8:8"]]
- 00be82e0 bytes 30ab0194
+ 00be8708 bytes 30ab0194
- 00be8304 ["INT_ADD", "register:40f0:8", ["const:be8304:8", "const:4:8"]]
- 00be8304 ["CALL", null, ["callee:00c533c8:8"]]
+ 00be872c ["INT_ADD", "register:40f0:8", ["const:be872c:8", "const:4:8"]]
+ 00be872c ["CALL", null, ["callee:00c533c8:8"]]
- 00be8304 bytes 27ab0194
+ 00be872c bytes 27ab0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292af319030447cbb838a4d952403c3f"></a>

### [`00beeaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md) → [`00beef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) FUN_00beef20

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) · 呼出先 2件 [`00beef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md) [`00c52fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52fa0.md)
- 新版 呼出元 1件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) · 呼出先 2件 [`00bef33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md) [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00beeb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md#insn-00beeb48) · [`00beeb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md#insn-00beeb94) · [`00beebb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md#insn-00beebb0)
- 新版 [`00beef70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md#insn-00beef70) · [`00beefbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md#insn-00beefbc) · [`00beefd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md#insn-00beefd8)

~~~diff
- 00beeb48 ["INT_ADD", "register:40f0:8", ["const:beeb48:8", "const:4:8"]]
- 00beeb48 ["CALL", null, ["callee:00c533c8:8"]]
+ 00beef70 ["INT_ADD", "register:40f0:8", ["const:beef70:8", "const:4:8"]]
+ 00beef70 ["CALL", null, ["callee:00c533c8:8"]]
- 00beeb48 bytes 16910194
+ 00beef70 bytes 16910194
- 00beeb94 ["INT_ADD", "register:40f0:8", ["const:beeb94:8", "const:4:8"]]
- 00beeb94 ["CALL", null, ["callee:00bef33c:8"]]
+ 00beefbc ["INT_ADD", "register:40f0:8", ["const:beefbc:8", "const:4:8"]]
+ 00beefbc ["CALL", null, ["callee:00bef33c:8"]]
- 00beeb94 bytes e0000094
+ 00beefbc bytes e0000094
- 00beebb0 ["INT_ADD", "register:40f0:8", ["const:beebb0:8", "const:4:8"]]
- 00beebb0 ["CALL", null, ["callee:00c533c8:8"]]
+ 00beefd8 ["INT_ADD", "register:40f0:8", ["const:beefd8:8", "const:4:8"]]
+ 00beefd8 ["CALL", null, ["callee:00c533c8:8"]]
- 00beebb0 bytes fc900194
+ 00beefd8 bytes fc900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a092c3ef33f46668703dc18fdf05ab35"></a>

### [`00beef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md) → [`00bef33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md) FUN_00bef33c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) [`00beeaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md) · 呼出先 1件 [`00c52fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52fa0.md)
- 新版 呼出元 2件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) [`00beef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) · 呼出先 1件 [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00beef5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md#insn-00beef5c) · [`00beef6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md#insn-00beef6c) · [`00beef8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md#insn-00beef8c)
- 新版 [`00bef384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md#insn-00bef384) · [`00bef394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md#insn-00bef394) · [`00bef3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md#insn-00bef3b4)

~~~diff
- 00beef5c ["INT_ADD", "register:40f0:8", ["const:beef5c:8", "const:4:8"]]
- 00beef5c ["CALL", null, ["callee:00c533c8:8"]]
+ 00bef384 ["INT_ADD", "register:40f0:8", ["const:bef384:8", "const:4:8"]]
+ 00bef384 ["CALL", null, ["callee:00c533c8:8"]]
- 00beef5c bytes 11900194
+ 00bef384 bytes 11900194
- 00beef6c ["INT_ADD", "register:40f0:8", ["const:beef6c:8", "const:4:8"]]
- 00beef6c ["CALL", null, ["callee:00c533c8:8"]]
+ 00bef394 ["INT_ADD", "register:40f0:8", ["const:bef394:8", "const:4:8"]]
+ 00bef394 ["CALL", null, ["callee:00c533c8:8"]]
- 00beef6c bytes 0d900194
+ 00bef394 bytes 0d900194
- 00beef8c ["INT_ADD", "register:40f0:8", ["const:beef8c:8", "const:4:8"]]
- 00beef8c ["CALL", null, ["callee:00c533c8:8"]]
+ 00bef3b4 ["INT_ADD", "register:40f0:8", ["const:bef3b4:8", "const:4:8"]]
+ 00bef3b4 ["CALL", null, ["callee:00c533c8:8"]]
- 00beef8c bytes 05900194
+ 00bef3b4 bytes 05900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83160e55c9d2fe2b971b0d05cf62a210"></a>

### [`00bef16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef16c.md) → [`00bef594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md) FUN_00bef594

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) · 呼出先 1件 [`00c52fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52fa0.md)
- 新版 呼出元 1件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) · 呼出先 1件 [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef16c.md#insn-00bef20c) · [`00bef230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef16c.md#insn-00bef230) · [`00bef24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef16c.md#insn-00bef24c)
- 新版 [`00bef634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md#insn-00bef634) · [`00bef658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md#insn-00bef658) · [`00bef674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md#insn-00bef674)

~~~diff
- 00bef20c ["INT_ADD", "register:40f0:8", ["const:bef20c:8", "const:4:8"]]
- 00bef20c ["CALL", null, ["callee:00c533c8:8"]]
+ 00bef634 ["INT_ADD", "register:40f0:8", ["const:bef634:8", "const:4:8"]]
+ 00bef634 ["CALL", null, ["callee:00c533c8:8"]]
- 00bef20c bytes 658f0194
+ 00bef634 bytes 658f0194
- 00bef230 ["INT_ADD", "register:40f0:8", ["const:bef230:8", "const:4:8"]]
- 00bef230 ["CALL", null, ["callee:00c533c8:8"]]
+ 00bef658 ["INT_ADD", "register:40f0:8", ["const:bef658:8", "const:4:8"]]
+ 00bef658 ["CALL", null, ["callee:00c533c8:8"]]
- 00bef230 bytes 5c8f0194
+ 00bef658 bytes 5c8f0194
- 00bef24c ["INT_ADD", "register:40f0:8", ["const:bef24c:8", "const:4:8"]]
- 00bef24c ["CALL", null, ["callee:00c533c8:8"]]
+ 00bef674 ["INT_ADD", "register:40f0:8", ["const:bef674:8", "const:4:8"]]
+ 00bef674 ["CALL", null, ["callee:00c533c8:8"]]
- 00bef24c bytes 558f0194
+ 00bef674 bytes 558f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ede0dee841329570b8784cdbe33a04"></a>

### [`00bef638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef638.md) → [`00befa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa60.md) _ZSt18uncaught_exceptionv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md) · 呼出先 1件 [`00c5db00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db00.md)
- 新版 呼出元 1件 [`00c5d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0f0.md) · 呼出先 1件 [`00c5df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef638.md#insn-00bef644)
- 新版 [`00befa6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa60.md#insn-00befa6c)

~~~diff
- 00bef644 ["INT_ADD", "register:40f0:8", ["const:bef644:8", "const:4:8"]]
- 00bef644 ["CALL", null, ["callee:00c5df00:8"]]
+ 00befa6c ["INT_ADD", "register:40f0:8", ["const:befa6c:8", "const:4:8"]]
+ 00befa6c ["CALL", null, ["callee:00c5df00:8"]]
- 00bef644 bytes 2fb90194
+ 00befa6c bytes 25b90194
~~~


<a id="compare-0d577db7ffbe559d04c97246427bd82f"></a>

### [`00bef688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef688.md) → [`00befab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befab0.md) _ZNSt13exception_ptraSERKS_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db30.md) · 呼出先 2件 [`00c5db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db10.md) [`00c5db20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db20.md)
- 新版 呼出元 1件 [`00c5df30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df30.md) · 呼出先 2件 [`00c5df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df10.md) [`00c5df20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef688.md#insn-00bef6b0) · [`00bef6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef688.md#insn-00bef6b8)
- 新版 [`00befad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befab0.md#insn-00befad8) · [`00befae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befab0.md#insn-00befae0)

~~~diff
- 00bef6b0 ["INT_ADD", "register:40f0:8", ["const:bef6b0:8", "const:4:8"]]
- 00bef6b0 ["CALL", null, ["callee:00c5df20:8"]]
+ 00befad8 ["INT_ADD", "register:40f0:8", ["const:befad8:8", "const:4:8"]]
+ 00befad8 ["CALL", null, ["callee:00c5df20:8"]]
- 00bef6b0 bytes 1cb90194
+ 00befad8 bytes 12b90194
- 00bef6b8 ["INT_ADD", "register:40f0:8", ["const:bef6b8:8", "const:4:8"]]
- 00bef6b8 ["CALL", null, ["callee:00c5df10:8"]]
+ 00befae0 ["INT_ADD", "register:40f0:8", ["const:befae0:8", "const:4:8"]]
+ 00befae0 ["CALL", null, ["callee:00c5df10:8"]]
- 00bef6b8 bytes 16b90194
+ 00befae0 bytes 0cb90194
~~~


<a id="compare-c9709e394c8401093b4035b2d1ecdbd1"></a>

### [`00bef720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef720.md) → [`00befb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb48.md) _ZSt17current_exceptionv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58160.md) · 呼出先 1件 [`00c5db40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db40.md)
- 新版 呼出元 1件 [`00c58560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58560.md) · 呼出先 1件 [`00c5df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef720.md#insn-00bef734)
- 新版 [`00befb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb48.md#insn-00befb5c)

~~~diff
- 00bef734 ["INT_ADD", "register:40f0:8", ["const:bef734:8", "const:4:8"]]
- 00bef734 ["CALL", null, ["callee:00c5df40:8"]]
+ 00befb5c ["INT_ADD", "register:40f0:8", ["const:befb5c:8", "const:4:8"]]
+ 00befb5c ["CALL", null, ["callee:00c5df40:8"]]
- 00bef734 bytes 03b90194
+ 00befb5c bytes f9b80194
~~~


<a id="compare-5c934df6712def2892a7ad823941719c"></a>

### [`00bef764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef764.md) → [`00befb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb8c.md) _ZNSt16nested_exceptionD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5db50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5df50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef764.md#insn-00bef778)
- 新版 [`00befba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb8c.md#insn-00befba0)

~~~diff
- 00bef778 ["INT_ADD", "register:40f0:8", ["const:bef778:8", "const:4:8"]]
- 00bef778 ["CALL", null, ["callee:00c5df50:8"]]
+ 00befba0 ["INT_ADD", "register:40f0:8", ["const:befba0:8", "const:4:8"]]
+ 00befba0 ["CALL", null, ["callee:00c5df50:8"]]
- 00bef778 bytes f6b80194
+ 00befba0 bytes ecb80194
~~~


<a id="compare-f4bb7e0acae5931d948ec6149bccc45c"></a>

### [`00bef790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef790.md) → [`00befbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md) _ZNKSt16nested_exception14rethrow_nestedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c580b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580b0.md) [`00c580c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c584b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584b0.md) [`00c584c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef790.md#insn-00bef7b4) · [`00bef7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef790.md#insn-00bef7bc) · [`00bef7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef790.md#insn-00bef7c8)
- 新版 [`00befbdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md#insn-00befbdc) · [`00befbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md#insn-00befbe4) · [`00befbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md#insn-00befbf0)

~~~diff
- 00bef7b4 ["INT_ADD", "register:40f0:8", ["const:bef7b4:8", "const:4:8"]]
- 00bef7b4 ["CALL", null, ["callee:00c582f0:8"]]
+ 00befbdc ["INT_ADD", "register:40f0:8", ["const:befbdc:8", "const:4:8"]]
+ 00befbdc ["CALL", null, ["callee:00c582f0:8"]]
- 00bef7b4 bytes cfa10194
+ 00befbdc bytes c5a10194
- 00bef7bc ["INT_ADD", "register:40f0:8", ["const:bef7bc:8", "const:4:8"]]
- 00bef7bc ["CALL", null, ["callee:00c58020:8"]]
+ 00befbe4 ["INT_ADD", "register:40f0:8", ["const:befbe4:8", "const:4:8"]]
+ 00befbe4 ["CALL", null, ["callee:00c58020:8"]]
- 00bef7bc bytes 19a10194
+ 00befbe4 bytes 0fa10194
- 00bef7c8 ["INT_ADD", "register:40f0:8", ["const:bef7c8:8", "const:4:8"]]
- 00bef7c8 ["CALL", null, ["callee:00c584b0:8"]]
+ 00befbf0 ["INT_ADD", "register:40f0:8", ["const:befbf0:8", "const:4:8"]]
+ 00befbf0 ["CALL", null, ["callee:00c584b0:8"]]
- 00bef7c8 bytes 3aa20194
+ 00befbf0 bytes 30a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9871f5a8cc56418df2a3a94861d67514"></a>

### [`00bef7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef7e8.md) → [`00befc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md) _ZSt17rethrow_exceptionSt13exception_ptr

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c580c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580c0.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c5db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db60.md)
- 新版 呼出元 1件 [`00c584c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584c0.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5df60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef7e8.md#insn-00bef7f8) · [`00bef7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef7e8.md#insn-00bef7fc)
- 新版 [`00befc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md#insn-00befc20) · [`00befc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md#insn-00befc24)

~~~diff
- 00bef7f8 ["INT_ADD", "register:40f0:8", ["const:bef7f8:8", "const:4:8"]]
- 00bef7f8 ["CALL", null, ["callee:00c5df60:8"]]
+ 00befc20 ["INT_ADD", "register:40f0:8", ["const:befc20:8", "const:4:8"]]
+ 00befc20 ["CALL", null, ["callee:00c5df60:8"]]
- 00bef7f8 bytes dab80194
+ 00befc20 bytes d0b80194
- 00bef7fc ["INT_ADD", "register:40f0:8", ["const:bef7fc:8", "const:4:8"]]
- 00bef7fc ["CALL", null, ["callee:00c58020:8"]]
+ 00befc24 ["INT_ADD", "register:40f0:8", ["const:befc24:8", "const:4:8"]]
+ 00befc24 ["CALL", null, ["callee:00c58020:8"]]
- 00bef7fc bytes 09a10194
+ 00befc24 bytes ffa00194
~~~


<a id="compare-54592de73b3bba428c3b66bcac085a30"></a>

### [`00beffb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beffb4.md) → [`00bf03dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf03dc.md) _ZNSt6__ndk112bad_weak_ptrD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a390.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00beffc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beffb4.md#insn-00beffc8)
- 新版 [`00bf03f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf03dc.md#insn-00bf03f0)

~~~diff
- 00beffc8 ["INT_ADD", "register:40f0:8", ["const:beffc8:8", "const:4:8"]]
- 00beffc8 ["CALL", null, ["callee:00c5a790:8"]]
+ 00bf03f0 ["INT_ADD", "register:40f0:8", ["const:bf03f0:8", "const:4:8"]]
+ 00bf03f0 ["CALL", null, ["callee:00c5a790:8"]]
- 00beffc8 bytes f2a80194
+ 00bf03f0 bytes e8a80194
~~~


<a id="compare-f81fd0c23c226e6ac341754c0640f61c"></a>

### [`00bf0008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0008.md) → [`00bf0430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0430.md) _ZNSt6__ndk114__shared_count12__add_sharedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf001c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0008.md#insn-00bf001c)
- 新版 [`00bf0444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0430.md#insn-00bf0444)

~~~diff
- 00bf001c ["INT_ADD", "register:40f0:8", ["const:bf001c:8", "const:4:8"]]
- 00bf001c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00bf0444 ["INT_ADD", "register:40f0:8", ["const:bf0444:8", "const:4:8"]]
+ 00bf0444 ["CALL", null, ["callee:00c53cd0:8"]]
- 00bf001c bytes 258e0194
+ 00bf0444 bytes 238e0194
~~~


<a id="compare-8b7d0f5eedd460c07764ff8fec7abf84"></a>

### [`00bf002c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf002c.md) → [`00bf0454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0454.md) _ZNSt6__ndk114__shared_count16__release_sharedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf002c.md#insn-00bf0048) · [`00bf0060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf002c.md#insn-00bf0060)
- 新版 [`00bf0470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0454.md#insn-00bf0470) · [`00bf0488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0454.md#insn-00bf0488)

~~~diff
- 00bf0048 ["INT_ADD", "register:40f0:8", ["const:bf0048:8", "const:4:8"]]
- 00bf0048 ["CALL", null, ["callee:00c53d00:8"]]
+ 00bf0470 ["INT_ADD", "register:40f0:8", ["const:bf0470:8", "const:4:8"]]
+ 00bf0470 ["CALL", null, ["callee:00c53d00:8"]]
- 00bf0048 bytes 268e0194
+ 00bf0470 bytes 248e0194
- 00bf0060 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf0060 ["INT_ADD", "register:40f0:8", ["const:bf0060:8", "const:4:8"]]
- 00bf0060 ["CALLIND", null, ["register:0:8"]]
+ 00bf0488 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf0488 ["INT_ADD", "register:40f0:8", ["const:bf0488:8", "const:4:8"]]
+ 00bf0488 ["CALLIND", null, ["register:0:8"]]
- 00bf0060 bytes 00013fd6
+ 00bf0488 bytes 00013fd6
~~~


<a id="compare-880a3c689cef42f2f04cb2d2b7bc7295"></a>

### [`00bf007c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf007c.md) → [`00bf04a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04a4.md) _ZNSt6__ndk119__shared_weak_count12__add_sharedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf007c.md#insn-00bf0090)
- 新版 [`00bf04b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04a4.md#insn-00bf04b8)

~~~diff
- 00bf0090 ["INT_ADD", "register:40f0:8", ["const:bf0090:8", "const:4:8"]]
- 00bf0090 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00bf04b8 ["INT_ADD", "register:40f0:8", ["const:bf04b8:8", "const:4:8"]]
+ 00bf04b8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00bf0090 bytes 088e0194
+ 00bf04b8 bytes 068e0194
~~~


<a id="compare-3412f20a4e8da81fe4749fd7f1a505e2"></a>

### [`00bf00a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00a0.md) → [`00bf04c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04c8.md) _ZNSt6__ndk119__shared_weak_count10__add_weakEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf00b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00a0.md#insn-00bf00b4)
- 新版 [`00bf04dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04c8.md#insn-00bf04dc)

~~~diff
- 00bf00b4 ["INT_ADD", "register:40f0:8", ["const:bf00b4:8", "const:4:8"]]
- 00bf00b4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00bf04dc ["INT_ADD", "register:40f0:8", ["const:bf04dc:8", "const:4:8"]]
+ 00bf04dc ["CALL", null, ["callee:00c53cd0:8"]]
- 00bf00b4 bytes ff8d0194
+ 00bf04dc bytes fd8d0194
~~~


<a id="compare-3cbf15984e915914a69c04bf5d1937a8"></a>

### [`00bf00c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00c4.md) → [`00bf04ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md) _ZNSt6__ndk119__shared_weak_count16__release_sharedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf00e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00c4.md#insn-00bf00e0) · [`00bf0108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00c4.md#insn-00bf0108) · [`00bf011c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00c4.md#insn-00bf011c)
- 新版 [`00bf0508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md#insn-00bf0508) · [`00bf0530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md#insn-00bf0530) · [`00bf0544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md#insn-00bf0544)

~~~diff
- 00bf00e0 ["INT_ADD", "register:40f0:8", ["const:bf00e0:8", "const:4:8"]]
- 00bf00e0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00bf0508 ["INT_ADD", "register:40f0:8", ["const:bf0508:8", "const:4:8"]]
+ 00bf0508 ["CALL", null, ["callee:00c53d00:8"]]
- 00bf00e0 bytes 008e0194
+ 00bf0508 bytes fe8d0194
- 00bf0108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf0108 ["INT_ADD", "register:40f0:8", ["const:bf0108:8", "const:4:8"]]
- 00bf0108 ["CALLIND", null, ["register:0:8"]]
+ 00bf0530 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf0530 ["INT_ADD", "register:40f0:8", ["const:bf0530:8", "const:4:8"]]
+ 00bf0530 ["CALLIND", null, ["register:0:8"]]
- 00bf0108 bytes 00013fd6
+ 00bf0530 bytes 00013fd6
- 00bf011c ["INT_ADD", "register:40f0:8", ["const:bf011c:8", "const:4:8"]]
- 00bf011c ["CALL", null, ["callee:00c53d00:8"]]
+ 00bf0544 ["INT_ADD", "register:40f0:8", ["const:bf0544:8", "const:4:8"]]
+ 00bf0544 ["CALL", null, ["callee:00c53d00:8"]]
- 00bf011c bytes f18d0194
+ 00bf0544 bytes ef8d0194
~~~


<a id="compare-de2b7c68b1042d1abd3737244f9c3ac4"></a>

### [`00bf0140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0140.md) → [`00bf0568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0568.md) _ZNSt6__ndk119__shared_weak_count14__release_weakEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0140.md#insn-00bf0164)
- 新版 [`00bf058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0568.md#insn-00bf058c)

~~~diff
- 00bf0164 ["INT_ADD", "register:40f0:8", ["const:bf0164:8", "const:4:8"]]
- 00bf0164 ["CALL", null, ["callee:00c53d00:8"]]
+ 00bf058c ["INT_ADD", "register:40f0:8", ["const:bf058c:8", "const:4:8"]]
+ 00bf058c ["CALL", null, ["callee:00c53d00:8"]]
- 00bf0164 bytes df8d0194
+ 00bf058c bytes dd8d0194
~~~


<a id="compare-5ed1246a21ae4dd55222fe201c34084f"></a>

### [`00bf0198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0198.md) → [`00bf05c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf05c0.md) _ZNSt6__ndk119__shared_weak_count4lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c580f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580f0.md) · 呼出先 1件 [`00c537e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c537e0.md)
- 新版 呼出元 1件 [`00c584f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584f0.md) · 呼出先 1件 [`00c53c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf01c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0198.md#insn-00bf01c8)
- 新版 [`00bf05f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf05c0.md#insn-00bf05f0)

~~~diff
- 00bf01c8 ["INT_ADD", "register:40f0:8", ["const:bf01c8:8", "const:4:8"]]
- 00bf01c8 ["CALL", null, ["callee:00c53c00:8"]]
+ 00bf05f0 ["INT_ADD", "register:40f0:8", ["const:bf05f0:8", "const:4:8"]]
+ 00bf05f0 ["CALL", null, ["callee:00c53c00:8"]]
- 00bf01c8 bytes 868d0194
+ 00bf05f0 bytes 848d0194
~~~


<a id="compare-480aed9502b41e9ec26772cae4846bf0"></a>

### [`00bf0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0204.md) → [`00bf062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf062c.md) _ZNSt6__ndk18__sp_mut4lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0204.md#insn-00bf0214)
- 新版 [`00bf063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf062c.md#insn-00bf063c)

~~~diff
- 00bf0214 ["INT_ADD", "register:40f0:8", ["const:bf0214:8", "const:4:8"]]
- 00bf0214 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bf063c ["INT_ADD", "register:40f0:8", ["const:bf063c:8", "const:4:8"]]
+ 00bf063c ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bf0214 bytes 23ac0194
+ 00bf063c bytes 19ac0194
~~~


<a id="compare-03f56e483a4e5691493c11d4a2b5a89a"></a>

### [`00bf0228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0228.md) → [`00bf0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0650.md) _ZNSt6__ndk18__sp_mut6unlockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0228.md#insn-00bf0238)
- 新版 [`00bf0660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0650.md#insn-00bf0660)

~~~diff
- 00bf0238 ["INT_ADD", "register:40f0:8", ["const:bf0238:8", "const:4:8"]]
- 00bf0238 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bf0660 ["INT_ADD", "register:40f0:8", ["const:bf0660:8", "const:4:8"]]
+ 00bf0660 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bf0238 bytes 1eac0194
+ 00bf0660 bytes 14ac0194
~~~


<a id="compare-2f1e95e88a53abf9511ed1bf553ab0b4"></a>

### [`00bf024c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf024c.md) → [`00bf0674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0674.md) _ZNSt6__ndk112__get_sp_mutEPKv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf06c0",
      "incomplete_value": true,
      "site": "00bf06c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca46e8:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0298",
      "incomplete_value": true,
      "site": "00bf029c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca42e8:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
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

- 旧版 [`00bf028c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf024c.md#insn-00bf028c)
- 新版 [`00bf06b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0674.md#insn-00bf06b4)

~~~diff
- 00bf028c ["COPY", "register:4048:8", ["const:ca42e8:8"]]
+ 00bf06b4 ["COPY", "register:4048:8", ["const:ca46e8:8"]]
- 00bf028c bytes e9025a10
+ 00bf06b4 bytes a9015a10
~~~


<a id="compare-27037f11fbb33295b0a7d9880ec9af8c"></a>

### [`00bf047c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md) → [`00bf08a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md) _ZNSt11logic_erroraSERKS_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf04a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md#insn-00bf04a4) · [`00bf04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md#insn-00bf04b0) · [`00bf04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md#insn-00bf04c0)
- 新版 [`00bf08cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md#insn-00bf08cc) · [`00bf08d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md#insn-00bf08d8) · [`00bf08e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md#insn-00bf08e8)

~~~diff
- 00bf04a4 ["INT_ADD", "register:40f0:8", ["const:bf04a4:8", "const:4:8"]]
- 00bf04a4 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00bf08cc ["INT_ADD", "register:40f0:8", ["const:bf08cc:8", "const:4:8"]]
+ 00bf08cc ["CALL", null, ["callee:00c53ca0:8"]]
- 00bf04a4 bytes f78c0194
+ 00bf08cc bytes f58c0194
- 00bf04b0 ["INT_ADD", "register:40f0:8", ["const:bf04b0:8", "const:4:8"]]
- 00bf04b0 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00bf08d8 ["INT_ADD", "register:40f0:8", ["const:bf08d8:8", "const:4:8"]]
+ 00bf08d8 ["CALL", null, ["callee:00c53ca0:8"]]
- 00bf04b0 bytes f48c0194
+ 00bf08d8 bytes f28c0194
- 00bf04c0 ["INT_ADD", "register:40f0:8", ["const:bf04c0:8", "const:4:8"]]
- 00bf04c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bf08e8 ["INT_ADD", "register:40f0:8", ["const:bf08e8:8", "const:4:8"]]
+ 00bf08e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bf04c0 bytes 7c9d0194
+ 00bf08e8 bytes 729d0194
~~~


<a id="compare-b7290ce1dc30a7ca99dc36cdfc48ac60"></a>

### [`00bf062c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf062c.md) → [`00bf0a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md) _ZNSt13runtime_erroraSERKS_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf062c.md#insn-00bf0654) · [`00bf0660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf062c.md#insn-00bf0660) · [`00bf0670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf062c.md#insn-00bf0670)
- 新版 [`00bf0a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md#insn-00bf0a7c) · [`00bf0a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md#insn-00bf0a88) · [`00bf0a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md#insn-00bf0a98)

~~~diff
- 00bf0654 ["INT_ADD", "register:40f0:8", ["const:bf0654:8", "const:4:8"]]
- 00bf0654 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00bf0a7c ["INT_ADD", "register:40f0:8", ["const:bf0a7c:8", "const:4:8"]]
+ 00bf0a7c ["CALL", null, ["callee:00c53ca0:8"]]
- 00bf0654 bytes 8b8c0194
+ 00bf0a7c bytes 898c0194
- 00bf0660 ["INT_ADD", "register:40f0:8", ["const:bf0660:8", "const:4:8"]]
- 00bf0660 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00bf0a88 ["INT_ADD", "register:40f0:8", ["const:bf0a88:8", "const:4:8"]]
+ 00bf0a88 ["CALL", null, ["callee:00c53ca0:8"]]
- 00bf0660 bytes 888c0194
+ 00bf0a88 bytes 868c0194
- 00bf0670 ["INT_ADD", "register:40f0:8", ["const:bf0670:8", "const:4:8"]]
- 00bf0670 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bf0a98 ["INT_ADD", "register:40f0:8", ["const:bf0a98:8", "const:4:8"]]
+ 00bf0a98 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bf0670 bytes 109d0194
+ 00bf0a98 bytes 069d0194
~~~


<a id="compare-e407448e21f515700df1f7d0a751d5ad"></a>

### [`00bf06dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf06dc.md) → [`00bf0b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c70.md) · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)
- 新版 呼出元 1件 [`00c58070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58070.md) · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf077c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf06dc.md#insn-00bf077c) · [`00bf07c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf06dc.md#insn-00bf07c8) · [`00bf07d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf06dc.md#insn-00bf07d8)
- 新版 [`00bf0ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md#insn-00bf0ba4) · [`00bf0bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md#insn-00bf0bf0) · [`00bf0c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md#insn-00bf0c00)

~~~diff
- 00bf077c ["INT_ADD", "register:40f0:8", ["const:bf077c:8", "const:4:8"]]
- 00bf077c ["CALL", null, ["callee:00c5b0a0:8"]]
+ 00bf0ba4 ["INT_ADD", "register:40f0:8", ["const:bf0ba4:8", "const:4:8"]]
+ 00bf0ba4 ["CALL", null, ["callee:00c5b0a0:8"]]
- 00bf077c bytes 49a90194
+ 00bf0ba4 bytes 3fa90194
- 00bf07c8 ["INT_ADD", "register:40f0:8", ["const:bf07c8:8", "const:4:8"]]
- 00bf07c8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf0bf0 ["INT_ADD", "register:40f0:8", ["const:bf0bf0:8", "const:4:8"]]
+ 00bf0bf0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf07c8 bytes de9c0194
+ 00bf0bf0 bytes d49c0194
- 00bf07d8 ["INT_ADD", "register:40f0:8", ["const:bf07d8:8", "const:4:8"]]
- 00bf07d8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf0c00 ["INT_ADD", "register:40f0:8", ["const:bf0c00:8", "const:4:8"]]
+ 00bf0c00 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf07d8 bytes da9c0194
+ 00bf0c00 bytes d09c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886b6612f036203f2b261eed635d9e6f"></a>

### [`00bf0968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md) → [`00bf0d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf09c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md#insn-00bf09c4) · [`00bf09e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md#insn-00bf09e8) · [`00bf0a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0968.md#insn-00bf0a08)
- 新版 [`00bf0dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md#insn-00bf0dec) · [`00bf0e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md#insn-00bf0e10) · [`00bf0e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md#insn-00bf0e30)

~~~diff
- 00bf09c4 ["INT_ADD", "register:40f0:8", ["const:bf09c4:8", "const:4:8"]]
- 00bf09c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf0dec ["INT_ADD", "register:40f0:8", ["const:bf0dec:8", "const:4:8"]]
+ 00bf0dec ["CALL", null, ["callee:00c57e90:8"]]
- 00bf09c4 bytes 339c0194
+ 00bf0dec bytes 299c0194
- 00bf09e8 ["INT_ADD", "register:40f0:8", ["const:bf09e8:8", "const:4:8"]]
- 00bf09e8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf0e10 ["INT_ADD", "register:40f0:8", ["const:bf0e10:8", "const:4:8"]]
+ 00bf0e10 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf09e8 bytes 569c0194
+ 00bf0e10 bytes 4c9c0194
- 00bf0a08 ["INT_ADD", "register:40f0:8", ["const:bf0a08:8", "const:4:8"]]
- 00bf0a08 ["CALL", null, ["callee:0043b764:8"]]
+ 00bf0e30 ["INT_ADD", "register:40f0:8", ["const:bf0e30:8", "const:4:8"]]
+ 00bf0e30 ["CALL", null, ["callee:0043b764:8"]]
- 00bf0a08 bytes 472be197
+ 00bf0e30 bytes 4d2ae197
~~~


<a id="compare-77fd3c9bdc6dbc0633d3a12668602ca1"></a>

### [`00bf0a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0a38.md) → [`00bf0e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0e60.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c80.md) · 呼出先 2件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c70.md)
- 新版 呼出元 1件 [`00c58080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58080.md) · 呼出先 2件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0a38.md#insn-00bf0a60)
- 新版 [`00bf0e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0e60.md#insn-00bf0e88)

~~~diff
- 00bf0a60 ["INT_ADD", "register:40f0:8", ["const:bf0a60:8", "const:4:8"]]
- 00bf0a60 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf0e88 ["INT_ADD", "register:40f0:8", ["const:bf0e88:8", "const:4:8"]]
+ 00bf0e88 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf0a60 bytes 609c0194
+ 00bf0e88 bytes 569c0194
~~~


<a id="compare-aeb3aa9519f3f1e9ed555852f27ed609"></a>

### [`00bf0ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ab8.md) → [`00bf0ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ee0.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16find_last_not_ofEPKcmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ab8.md#insn-00bf0b14)
- 新版 [`00bf0f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ee0.md#insn-00bf0f3c)

~~~diff
- 00bf0b14 ["INT_ADD", "register:40f0:8", ["const:bf0b14:8", "const:4:8"]]
- 00bf0b14 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00bf0f3c ["INT_ADD", "register:40f0:8", ["const:bf0f3c:8", "const:4:8"]]
+ 00bf0f3c ["CALL", null, ["callee:00c57fd0:8"]]
- 00bf0b14 bytes 2f9c0194
+ 00bf0f3c bytes 259c0194
~~~


<a id="compare-6c0b410ba973550cb379831c1fced187"></a>

### [`00bf0b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0b50.md) → [`00bf0f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0f78.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17find_first_not_ofEPKcmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0b50.md#insn-00bf0ba4)
- 新版 [`00bf0fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0f78.md#insn-00bf0fcc)

~~~diff
- 00bf0ba4 ["INT_ADD", "register:40f0:8", ["const:bf0ba4:8", "const:4:8"]]
- 00bf0ba4 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00bf0fcc ["INT_ADD", "register:40f0:8", ["const:bf0fcc:8", "const:4:8"]]
+ 00bf0fcc ["CALL", null, ["callee:00c57fd0:8"]]
- 00bf0ba4 bytes 0b9c0194
+ 00bf0fcc bytes 019c0194
~~~


<a id="compare-090cb8ad53f1bdb69ff3d9e5490878c0"></a>

### [`00bf0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0bdc.md) → [`00bf1004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md) FUN_00bf1004

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf0ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00bf12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0bdc.md#insn-00bf0c88) · [`00bf0ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0bdc.md#insn-00bf0ca0) · [`00bf0cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0bdc.md#insn-00bf0cc0)
- 新版 [`00bf10b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md#insn-00bf10b0) · [`00bf10c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md#insn-00bf10c8) · [`00bf10e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md#insn-00bf10e8)

~~~diff
- 00bf0c88 ["INT_ADD", "register:40f0:8", ["const:bf0c88:8", "const:4:8"]]
- 00bf0c88 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf10b0 ["INT_ADD", "register:40f0:8", ["const:bf10b0:8", "const:4:8"]]
+ 00bf10b0 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf0c88 bytes 829b0194
+ 00bf10b0 bytes 789b0194
- 00bf0ca0 ["INT_ADD", "register:40f0:8", ["const:bf0ca0:8", "const:4:8"]]
- 00bf0ca0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf10c8 ["INT_ADD", "register:40f0:8", ["const:bf10c8:8", "const:4:8"]]
+ 00bf10c8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf0ca0 bytes a89b0194
+ 00bf10c8 bytes 9e9b0194
- 00bf0cc0 ["INT_ADD", "register:40f0:8", ["const:bf0cc0:8", "const:4:8"]]
- 00bf0cc0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf10e8 ["INT_ADD", "register:40f0:8", ["const:bf10e8:8", "const:4:8"]]
+ 00bf10e8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf0cc0 bytes a09b0194
+ 00bf10e8 bytes 969b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf42a971db3ea9a94b7f566d3326f68"></a>

### [`00bf0d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md) → [`00bf116c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md#insn-00bf0da0) · [`00bf0dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md#insn-00bf0dc0) · [`00bf0de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0d44.md#insn-00bf0de0)
- 新版 [`00bf11c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md#insn-00bf11c8) · [`00bf11e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md#insn-00bf11e8) · [`00bf1208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md#insn-00bf1208)

~~~diff
- 00bf0da0 ["INT_ADD", "register:40f0:8", ["const:bf0da0:8", "const:4:8"]]
- 00bf0da0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf11c8 ["INT_ADD", "register:40f0:8", ["const:bf11c8:8", "const:4:8"]]
+ 00bf11c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf0da0 bytes 3c9b0194
+ 00bf11c8 bytes 329b0194
- 00bf0dc0 ["INT_ADD", "register:40f0:8", ["const:bf0dc0:8", "const:4:8"]]
- 00bf0dc0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf11e8 ["INT_ADD", "register:40f0:8", ["const:bf11e8:8", "const:4:8"]]
+ 00bf11e8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf0dc0 bytes 609b0194
+ 00bf11e8 bytes 569b0194
- 00bf0de0 ["INT_ADD", "register:40f0:8", ["const:bf0de0:8", "const:4:8"]]
- 00bf0de0 ["CALL", null, ["callee:0043b764:8"]]
+ 00bf1208 ["INT_ADD", "register:40f0:8", ["const:bf1208:8", "const:4:8"]]
+ 00bf1208 ["CALL", null, ["callee:0043b764:8"]]
- 00bf0de0 bytes 512ae197
+ 00bf1208 bytes 5729e197
~~~


<a id="compare-968eec358786c980d2d702a8241cd379"></a>

### [`00bf0de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0de4.md) → [`00bf120c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf120c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0de4.md#insn-00bf0e24)
- 新版 [`00bf124c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf120c.md#insn-00bf124c)

~~~diff
- 00bf0e24 ["INT_ADD", "register:40f0:8", ["const:bf0e24:8", "const:4:8"]]
- 00bf0e24 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf124c ["INT_ADD", "register:40f0:8", ["const:bf124c:8", "const:4:8"]]
+ 00bf124c ["CALL", null, ["callee:0044291c:8"]]
- 00bf0e24 bytes ae46e197
+ 00bf124c bytes b445e197
~~~


<a id="compare-21acffd2cb418951488d63a415d1b7c0"></a>

### [`00bf0ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md) → [`00bf12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmmc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0bdc.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md#insn-00bf0f3c) · [`00bf0f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md#insn-00bf0f74) · [`00bf0f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md#insn-00bf0f88)
- 新版 [`00bf1364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md#insn-00bf1364) · [`00bf139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md#insn-00bf139c) · [`00bf13b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md#insn-00bf13b0)

~~~diff
- 00bf0f3c ["INT_ADD", "register:40f0:8", ["const:bf0f3c:8", "const:4:8"]]
- 00bf0f3c ["CALL", null, ["callee:00bf1004:8"]]
+ 00bf1364 ["INT_ADD", "register:40f0:8", ["const:bf1364:8", "const:4:8"]]
+ 00bf1364 ["CALL", null, ["callee:00bf1004:8"]]
- 00bf0f3c bytes 28ffff97
+ 00bf1364 bytes 28ffff97
- 00bf0f74 ["INT_ADD", "register:40f0:8", ["const:bf0f74:8", "const:4:8"]]
- 00bf0f74 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf139c ["INT_ADD", "register:40f0:8", ["const:bf139c:8", "const:4:8"]]
+ 00bf139c ["CALL", null, ["callee:00c57f40:8"]]
- 00bf0f74 bytes f39a0194
+ 00bf139c bytes e99a0194
- 00bf0f88 ["INT_ADD", "register:40f0:8", ["const:bf0f88:8", "const:4:8"]]
- 00bf0f88 ["CALL", null, ["callee:00c58090:8"]]
+ 00bf13b0 ["INT_ADD", "register:40f0:8", ["const:bf13b0:8", "const:4:8"]]
+ 00bf13b0 ["CALL", null, ["callee:00c58090:8"]]
- 00bf0f88 bytes 429b0194
+ 00bf13b0 bytes 389b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db851f40ca7c09e96930e27b0fcd9a5f"></a>

### [`00bf0fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md) → [`00bf1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md) FUN_00bf1400

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf1124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1124.md) [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`00bf154c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf154c.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md#insn-00bf1088) · [`00bf10c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md#insn-00bf10c8) · [`00bf10d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md#insn-00bf10d8)
- 新版 [`00bf14b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md#insn-00bf14b0) · [`00bf14f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md#insn-00bf14f0) · [`00bf1500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md#insn-00bf1500)

~~~diff
- 00bf1088 ["INT_ADD", "register:40f0:8", ["const:bf1088:8", "const:4:8"]]
- 00bf1088 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf14b0 ["INT_ADD", "register:40f0:8", ["const:bf14b0:8", "const:4:8"]]
+ 00bf14b0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf1088 bytes ae9a0194
+ 00bf14b0 bytes a49a0194
- 00bf10c8 ["INT_ADD", "register:40f0:8", ["const:bf10c8:8", "const:4:8"]]
- 00bf10c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf14f0 ["INT_ADD", "register:40f0:8", ["const:bf14f0:8", "const:4:8"]]
+ 00bf14f0 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf10c8 bytes 729a0194
+ 00bf14f0 bytes 689a0194
- 00bf10d8 ["INT_ADD", "register:40f0:8", ["const:bf10d8:8", "const:4:8"]]
- 00bf10d8 ["CALL", null, ["callee:00c58000:8"]]
+ 00bf1500 ["INT_ADD", "register:40f0:8", ["const:bf1500:8", "const:4:8"]]
+ 00bf1500 ["CALL", null, ["callee:00c58000:8"]]
- 00bf10d8 bytes ca9a0194
+ 00bf1500 bytes c09a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef32e6eba74bab4c9286610b0ce1c6a7"></a>

### [`00bf1124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1124.md) → [`00bf154c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf154c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf0fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1124.md#insn-00bf1170)
- 新版 [`00bf1598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf154c.md#insn-00bf1598)

~~~diff
- 00bf1170 ["INT_ADD", "register:40f0:8", ["const:bf1170:8", "const:4:8"]]
- 00bf1170 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1598 ["INT_ADD", "register:40f0:8", ["const:bf1598:8", "const:4:8"]]
+ 00bf1598 ["CALL", null, ["callee:0044291c:8"]]
- 00bf1170 bytes db45e197
+ 00bf1598 bytes e144e197
~~~


<a id="compare-5dc9a0f505f26e67f3005782ac691fcf"></a>

### [`00bf1174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1174.md) → [`00bf159c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf159c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4copyEPcmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf11c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1174.md#insn-00bf11c8) · [`00bf11e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1174.md#insn-00bf11e0)
- 新版 [`00bf15f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf159c.md#insn-00bf15f0) · [`00bf1608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf159c.md#insn-00bf1608)

~~~diff
- 00bf11c8 ["INT_ADD", "register:40f0:8", ["const:bf11c8:8", "const:4:8"]]
- 00bf11c8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf15f0 ["INT_ADD", "register:40f0:8", ["const:bf15f0:8", "const:4:8"]]
+ 00bf15f0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf11c8 bytes 5e9a0194
+ 00bf15f0 bytes 549a0194
- 00bf11e0 ["INT_ADD", "register:40f0:8", ["const:bf11e0:8", "const:4:8"]]
- 00bf11e0 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1608 ["INT_ADD", "register:40f0:8", ["const:bf1608:8", "const:4:8"]]
+ 00bf1608 ["CALL", null, ["callee:0044291c:8"]]
- 00bf11e0 bytes bf45e197
+ 00bf1608 bytes c544e197
~~~


<a id="compare-f7303a3eaf5f26eac63eea5d26d28bc3"></a>

### [`00bf11e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf11e4.md) → [`00bf160c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf11e4.md#insn-00bf1270) · [`00bf1290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf11e4.md#insn-00bf1290) · [`00bf12b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf11e4.md#insn-00bf12b4)
- 新版 [`00bf1698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md#insn-00bf1698) · [`00bf16b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md#insn-00bf16b8) · [`00bf16dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md#insn-00bf16dc)

~~~diff
- 00bf1270 ["INT_ADD", "register:40f0:8", ["const:bf1270:8", "const:4:8"]]
- 00bf1270 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf1698 ["INT_ADD", "register:40f0:8", ["const:bf1698:8", "const:4:8"]]
+ 00bf1698 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf1270 bytes 089a0194
+ 00bf1698 bytes fe990194
- 00bf1290 ["INT_ADD", "register:40f0:8", ["const:bf1290:8", "const:4:8"]]
- 00bf1290 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf16b8 ["INT_ADD", "register:40f0:8", ["const:bf16b8:8", "const:4:8"]]
+ 00bf16b8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf1290 bytes 2c9a0194
+ 00bf16b8 bytes 229a0194
- 00bf12b4 ["INT_ADD", "register:40f0:8", ["const:bf12b4:8", "const:4:8"]]
- 00bf12b4 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf16dc ["INT_ADD", "register:40f0:8", ["const:bf16dc:8", "const:4:8"]]
+ 00bf16dc ["CALL", null, ["callee:0044291c:8"]]
- 00bf12b4 bytes 8a45e197
+ 00bf16dc bytes 9044e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

