# v16.0.2 → v16.0.3 · 要調査の変更候補 (36)

[一覧の目次](README.md)

<a id="compare-a726f899b1779e46eddadf8d2434c1b2"></a>

### [`00bbeec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbeec8.md) → [`00bbfebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfebc.md) _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5b0.md) · 呼出先 2件 [`00c5d5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5c0.md) [`00c5d600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d600.md)
- 新版 呼出元 1件 [`00c5e580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e580.md) · 呼出先 2件 [`00c5e590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e590.md) [`00c5e5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbf334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbeec8.md#insn-00bbf334) · [`00bbf9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbeec8.md#insn-00bbf9c4)
- 新版 [`00bc0328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfebc.md#insn-00bc0328) · [`00bc09b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfebc.md#insn-00bc09b8)

~~~diff
- 00bbf334 ["INT_ADD", "register:40f0:8", ["const:bbf334:8", "const:4:8"]]
- 00bbf334 ["CALL", null, ["callee:00c5e5d0:8"]]
+ 00bc0328 ["INT_ADD", "register:40f0:8", ["const:bc0328:8", "const:4:8"]]
+ 00bc0328 ["CALL", null, ["callee:00c5e5d0:8"]]
- 00bbf334 bytes b3780294
+ 00bc0328 bytes aa780294
- 00bbf9c4 ["INT_ADD", "register:40f0:8", ["const:bbf9c4:8", "const:4:8"]]
- 00bbf9c4 ["CALL", null, ["callee:00c5e590:8"]]
+ 00bc09b8 ["INT_ADD", "register:40f0:8", ["const:bc09b8:8", "const:4:8"]]
+ 00bc09b8 ["CALL", null, ["callee:00c5e590:8"]]
- 00bbf9c4 bytes ff760294
+ 00bc09b8 bytes f6760294
~~~


<a id="compare-b38a40c020077aa4becd772ff1a81f53"></a>

### [`00bc1140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1140.md) → [`00bc2134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2134.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d630.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)
- 新版 呼出元 1件 [`00c5e600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e600.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc11dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1140.md#insn-00bc11dc) · [`00bc12c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1140.md#insn-00bc12c8) · [`00bc1304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1140.md#insn-00bc1304)
- 新版 [`00bc21d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2134.md#insn-00bc21d0) · [`00bc22bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2134.md#insn-00bc22bc) · [`00bc22f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2134.md#insn-00bc22f8)

~~~diff
- 00bc11dc ["INT_ADD", "register:40f0:8", ["const:bc11dc:8", "const:4:8"]]
- 00bc11dc ["CALL", null, ["callee:00c58f30:8"]]
+ 00bc21d0 ["INT_ADD", "register:40f0:8", ["const:bc21d0:8", "const:4:8"]]
+ 00bc21d0 ["CALL", null, ["callee:00c58f30:8"]]
- 00bc11dc bytes 615b0294
+ 00bc21d0 bytes 585b0294
- 00bc12c8 ["INT_ADD", "register:40f0:8", ["const:bc12c8:8", "const:4:8"]]
- 00bc12c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bc22bc ["INT_ADD", "register:40f0:8", ["const:bc22bc:8", "const:4:8"]]
+ 00bc22bc ["CALL", null, ["callee:00c58f50:8"]]
- 00bc12c8 bytes 2e5b0294
+ 00bc22bc bytes 255b0294
- 00bc1304 ["INT_ADD", "register:40f0:8", ["const:bc1304:8", "const:4:8"]]
- 00bc1304 ["CALL", null, ["callee:00c5bdb0:8"]]
+ 00bc22f8 ["INT_ADD", "register:40f0:8", ["const:bc22f8:8", "const:4:8"]]
+ 00bc22f8 ["CALL", null, ["callee:00c5bdb0:8"]]
- 00bc1304 bytes b7660294
+ 00bc22f8 bytes ae660294
~~~


<a id="compare-c6c88bb4e584de0242d5f1711b70ea0f"></a>

### [`00bc1884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1884.md) → [`00bc2878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2878.md) _ZN8firebase13remote_config12RemoteConfigD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc188c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1884.md#insn-00bc188c)
- 新版 [`00bc2880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2878.md#insn-00bc2880)

~~~diff
- 00bc188c ["INT_ADD", "register:40f0:8", ["const:bc188c:8", "const:4:8"]]
- 00bc188c ["CALL", null, ["callee:00c5e750:8"]]
+ 00bc2880 ["INT_ADD", "register:40f0:8", ["const:bc2880:8", "const:4:8"]]
+ 00bc2880 ["CALL", null, ["callee:00c5e750:8"]]
- 00bc188c bytes bd6f0294
+ 00bc2880 bytes b46f0294
~~~


<a id="compare-338dac01e975d5a2c75fa496beda5e88"></a>

### [`00bc18cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc18cc.md) → [`00bc28c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc28c0.md) _ZN8firebase13remote_config12RemoteConfig5FetchEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d820.md) [`00c5d8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e7f0.md) [`00c5e880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc18e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc18cc.md#insn-00bc18e4)
- 新版 [`00bc28d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc28c0.md#insn-00bc28d8)

~~~diff
- 00bc18e4 ["INT_ADD", "register:40f0:8", ["const:bc18e4:8", "const:4:8"]]
- 00bc18e4 ["CALL", null, ["callee:00c5e7f0:8"]]
+ 00bc28d8 ["INT_ADD", "register:40f0:8", ["const:bc28d8:8", "const:4:8"]]
+ 00bc28d8 ["CALL", null, ["callee:00c5e7f0:8"]]
- 00bc18e4 bytes cf6f0294
+ 00bc28d8 bytes c66f0294
~~~


<a id="compare-2d55e7887b9291beb15c57f3250520eb"></a>

### [`00bc19f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc19f4.md) → [`00bc29e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc29e8.md) _ZN8firebase13remote_config12RemoteConfig25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5d860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5e830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc19f4.md#insn-00bc1a38) · [`00bc1a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc19f4.md#insn-00bc1a60) · [`00bc1a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc19f4.md#insn-00bc1a74)
- 新版 [`00bc2a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc29e8.md#insn-00bc2a2c) · [`00bc2a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc29e8.md#insn-00bc2a54) · [`00bc2a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc29e8.md#insn-00bc2a68)

~~~diff
- 00bc1a38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1a38 ["INT_ADD", "register:40f0:8", ["const:bc1a38:8", "const:4:8"]]
- 00bc1a38 ["CALLIND", null, ["register:0:8"]]
+ 00bc2a2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2a2c ["INT_ADD", "register:40f0:8", ["const:bc2a2c:8", "const:4:8"]]
+ 00bc2a2c ["CALLIND", null, ["register:0:8"]]
- 00bc1a38 bytes 00013fd6
+ 00bc2a2c bytes 00013fd6
- 00bc1a60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1a60 ["INT_ADD", "register:40f0:8", ["const:bc1a60:8", "const:4:8"]]
- 00bc1a60 ["CALLIND", null, ["register:0:8"]]
+ 00bc2a54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2a54 ["INT_ADD", "register:40f0:8", ["const:bc2a54:8", "const:4:8"]]
+ 00bc2a54 ["CALLIND", null, ["register:0:8"]]
- 00bc1a60 bytes 00013fd6
+ 00bc2a54 bytes 00013fd6
- 00bc1a74 ["INT_ADD", "register:40f0:8", ["const:bc1a74:8", "const:4:8"]]
- 00bc1a74 ["CALL", null, ["callee:00c5e830:8"]]
+ 00bc2a68 ["INT_ADD", "register:40f0:8", ["const:bc2a68:8", "const:4:8"]]
+ 00bc2a68 ["CALL", null, ["callee:00c5e830:8"]]
- 00bc1a74 bytes 7b6f0294
+ 00bc2a68 bytes 726f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdee0bcef8d220c917aebbf00db67f59"></a>

### [`00bc1b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b34.md) → [`00bc2b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2b28.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_13remote_config12RemoteConfigEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d980.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d980.md)
- 新版 呼出元 1件 [`00c5e950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e950.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b34.md#insn-00bc1b50) · [`00bc1b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b34.md#insn-00bc1b5c)
- 新版 [`00bc2b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2b28.md#insn-00bc2b44) · [`00bc2b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2b28.md#insn-00bc2b50)

~~~diff
- 00bc1b50 ["INT_ADD", "register:40f0:8", ["const:bc1b50:8", "const:4:8"]]
- 00bc1b50 ["CALL", null, ["callee:00c5e950:8"]]
+ 00bc2b44 ["INT_ADD", "register:40f0:8", ["const:bc2b44:8", "const:4:8"]]
+ 00bc2b44 ["CALL", null, ["callee:00c5e950:8"]]
- 00bc1b50 bytes 8c6f0294
+ 00bc2b44 bytes 836f0294
- 00bc1b5c ["INT_ADD", "register:40f0:8", ["const:bc1b5c:8", "const:4:8"]]
- 00bc1b5c ["CALL", null, ["callee:00c5e950:8"]]
+ 00bc2b50 ["INT_ADD", "register:40f0:8", ["const:bc2b50:8", "const:4:8"]]
+ 00bc2b50 ["CALL", null, ["callee:00c5e950:8"]]
- 00bc1b5c bytes 896f0294
+ 00bc2b50 bytes 806f0294
~~~


<a id="compare-d4e704de01df3b029fa457312d251a0c"></a>

### [`00bc48a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc48a0.md) → [`00bc5894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5894.md) _ZNSt6__ndk16vectorIN8firebase8internal12EmbeddedFileENS_9allocatorIS3_EEEC2ERKS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5da40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da40.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)
- 新版 呼出元 1件 [`00c5ea10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ea10.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc48f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc48a0.md#insn-00bc48f0) · [`00bc492c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc48a0.md#insn-00bc492c) · [`00bc4950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc48a0.md#insn-00bc4950)
- 新版 [`00bc58e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5894.md#insn-00bc58e4) · [`00bc5920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5894.md#insn-00bc5920) · [`00bc5944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5894.md#insn-00bc5944)

~~~diff
- 00bc48f0 ["INT_ADD", "register:40f0:8", ["const:bc48f0:8", "const:4:8"]]
- 00bc48f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bc58e4 ["INT_ADD", "register:40f0:8", ["const:bc58e4:8", "const:4:8"]]
+ 00bc58e4 ["CALL", null, ["callee:00c58f30:8"]]
- 00bc48f0 bytes 9c4d0294
+ 00bc58e4 bytes 934d0294
- 00bc492c ["INT_ADD", "register:40f0:8", ["const:bc492c:8", "const:4:8"]]
- 00bc492c ["CALL", null, ["callee:00c590a0:8"]]
+ 00bc5920 ["INT_ADD", "register:40f0:8", ["const:bc5920:8", "const:4:8"]]
+ 00bc5920 ["CALL", null, ["callee:00c590a0:8"]]
- 00bc492c bytes e94d0294
+ 00bc5920 bytes e04d0294
- 00bc4950 ["INT_ADD", "register:40f0:8", ["const:bc4950:8", "const:4:8"]]
- 00bc4950 ["CALL", null, ["callee:00c5bdb0:8"]]
+ 00bc5944 ["INT_ADD", "register:40f0:8", ["const:bc5944:8", "const:4:8"]]
+ 00bc5944 ["CALL", null, ["callee:00c5bdb0:8"]]
- 00bc4950 bytes 24590294
+ 00bc5944 bytes 1b590294
~~~


<a id="compare-74a709e6304e4f3383cda1f186166262"></a>

### [`00bc4974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4974.md) → [`00bc5968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5968.md) _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5da00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da00.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5e9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e9d0.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc4994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4974.md#insn-00bc4994) · [`00bc49ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4974.md#insn-00bc49ac) · [`00bc49b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4974.md#insn-00bc49b4)
- 新版 [`00bc5988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5968.md#insn-00bc5988) · [`00bc59a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5968.md#insn-00bc59a0) · [`00bc59a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5968.md#insn-00bc59a8)

~~~diff
- 00bc4994 ["INT_ADD", "register:40f0:8", ["const:bc4994:8", "const:4:8"]]
- 00bc4994 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc5988 ["INT_ADD", "register:40f0:8", ["const:bc5988:8", "const:4:8"]]
+ 00bc5988 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc4994 bytes 4f580294
+ 00bc5988 bytes 46580294
- 00bc49ac ["INT_ADD", "register:40f0:8", ["const:bc49ac:8", "const:4:8"]]
- 00bc49ac ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc59a0 ["INT_ADD", "register:40f0:8", ["const:bc59a0:8", "const:4:8"]]
+ 00bc59a0 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc49ac bytes 4d580294
+ 00bc59a0 bytes 44580294
- 00bc49b4 ["INT_ADD", "register:40f0:8", ["const:bc49b4:8", "const:4:8"]]
- 00bc49b4 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc59a8 ["INT_ADD", "register:40f0:8", ["const:bc59a8:8", "const:4:8"]]
+ 00bc59a8 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc49b4 bytes 4b580294
+ 00bc59a8 bytes 42580294
~~~


<a id="compare-8a54a9ca0e5575f5feb3abb92ff409af"></a>

### [`00bc49e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc49e4.md) → [`00bc59d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc59d8.md) FUN_00bc59d8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc4a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc49e4.md#insn-00bc4a30)
- 新版 [`00bc5a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc59d8.md#insn-00bc5a24)

~~~diff
- 00bc4a30 ["INT_ADD", "register:40f0:8", ["const:bc4a30:8", "const:4:8"]]
- 00bc4a30 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bc5a24 ["INT_ADD", "register:40f0:8", ["const:bc5a24:8", "const:4:8"]]
+ 00bc5a24 ["CALL", null, ["callee:00c58f50:8"]]
- 00bc4a30 bytes 544d0294
+ 00bc5a24 bytes 4b4d0294
~~~


<a id="compare-2f32ae0019dc3e47cabd345180ad71d2"></a>

### [`00bc4a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4a68.md) → [`00bc5a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5a5c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d950.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5ad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad00.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md) [`00c5afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afd0.md)
- 新版 呼出元 1件 [`00c5e920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e920.md) · 呼出先 7件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md) [`00c5bcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcd0.md) [`00c5bcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcf0.md) [`00c5bfa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc4a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4a68.md#insn-00bc4a84) · [`00bc4a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4a68.md#insn-00bc4a8c) · [`00bc4aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4a68.md#insn-00bc4aa8)
- 新版 [`00bc5a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5a5c.md#insn-00bc5a78) · [`00bc5a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5a5c.md#insn-00bc5a80) · [`00bc5a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5a5c.md#insn-00bc5a9c)

~~~diff
- 00bc4a84 ["INT_ADD", "register:40f0:8", ["const:bc4a84:8", "const:4:8"]]
- 00bc4a84 ["CALL", null, ["callee:00c5c830:8"]]
+ 00bc5a78 ["INT_ADD", "register:40f0:8", ["const:bc5a78:8", "const:4:8"]]
+ 00bc5a78 ["CALL", null, ["callee:00c5c830:8"]]
- 00bc4a84 bytes 775b0294
+ 00bc5a78 bytes 6e5b0294
- 00bc4a8c ["INT_ADD", "register:40f0:8", ["const:bc4a8c:8", "const:4:8"]]
- 00bc4a8c ["CALL", null, ["callee:00c5c120:8"]]
+ 00bc5a80 ["INT_ADD", "register:40f0:8", ["const:bc5a80:8", "const:4:8"]]
+ 00bc5a80 ["CALL", null, ["callee:00c5c120:8"]]
- 00bc4a8c bytes b1590294
+ 00bc5a80 bytes a8590294
- 00bc4aa8 ["INT_ADD", "register:40f0:8", ["const:bc4aa8:8", "const:4:8"]]
- 00bc4aa8 ["CALL", null, ["callee:00c5bfa0:8"]]
+ 00bc5a9c ["INT_ADD", "register:40f0:8", ["const:bc5a9c:8", "const:4:8"]]
+ 00bc5a9c ["CALL", null, ["callee:00c5bfa0:8"]]
- 00bc4aa8 bytes 4a590294
+ 00bc5a9c bytes 41590294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-711be5cb413614bf45b797c805c804dc"></a>

### [`00bc4fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md) → [`00bc5fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5fbc.md) _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bc5770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5770.md) · 呼出先 6件 [`00bc50f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc50f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00bc6764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6764.md) · 呼出先 6件 [`00bc60ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc60ec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md#insn-00bc5004) · [`00bc5020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md#insn-00bc5020) · [`00bc5048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md#insn-00bc5048)
- 新版 [`00bc5ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5fbc.md#insn-00bc5ff8) · [`00bc6014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5fbc.md#insn-00bc6014) · [`00bc603c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5fbc.md#insn-00bc603c)

~~~diff
- 00bc5004 ["INT_ADD", "register:40f0:8", ["const:bc5004:8", "const:4:8"]]
- 00bc5004 ["CALL", null, ["callee:00bc60ec:8"]]
+ 00bc5ff8 ["INT_ADD", "register:40f0:8", ["const:bc5ff8:8", "const:4:8"]]
+ 00bc5ff8 ["CALL", null, ["callee:00bc60ec:8"]]
- 00bc5004 bytes 3d000094
+ 00bc5ff8 bytes 3d000094
- 00bc5020 ["INT_ADD", "register:40f0:8", ["const:bc5020:8", "const:4:8"]]
- 00bc5020 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bc6014 ["INT_ADD", "register:40f0:8", ["const:bc6014:8", "const:4:8"]]
+ 00bc6014 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bc5020 bytes ac570294
+ 00bc6014 bytes a3570294
- 00bc5048 ["INT_ADD", "register:40f0:8", ["const:bc5048:8", "const:4:8"]]
- 00bc5048 ["CALL", null, ["callee:00c5e970:8"]]
+ 00bc603c ["INT_ADD", "register:40f0:8", ["const:bc603c:8", "const:4:8"]]
+ 00bc603c ["CALL", null, ["callee:00c5e970:8"]]
- 00bc5048 bytes 56620294
+ 00bc603c bytes 4d620294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b88d4c310a54f2c4b96ce7488777bdfc"></a>

### [`00bc51bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc51bc.md) → [`00bc61b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc61b0.md) _ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bc5a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a9c.md) [`00bc5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5dc8.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5b3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3b0.md)
- 新版 呼出元 2件 [`00bc6a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6a90.md) [`00bc6dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6dbc.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5c380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc51fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc51bc.md#insn-00bc51fc) · [`00bc521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc51bc.md#insn-00bc521c) · [`00bc5238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc51bc.md#insn-00bc5238)
- 新版 [`00bc61f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc61b0.md#insn-00bc61f0) · [`00bc6210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc61b0.md#insn-00bc6210) · [`00bc622c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc61b0.md#insn-00bc622c)

~~~diff
- 00bc51fc ["INT_ADD", "register:40f0:8", ["const:bc51fc:8", "const:4:8"]]
- 00bc51fc ["CALL", null, ["callee:00c5c380:8"]]
+ 00bc61f0 ["INT_ADD", "register:40f0:8", ["const:bc61f0:8", "const:4:8"]]
+ 00bc61f0 ["CALL", null, ["callee:00c5c380:8"]]
- 00bc51fc bytes 6d580294
+ 00bc61f0 bytes 64580294
- 00bc521c ["INT_ADD", "register:40f0:8", ["const:bc521c:8", "const:4:8"]]
- 00bc521c ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bc6210 ["INT_ADD", "register:40f0:8", ["const:bc6210:8", "const:4:8"]]
+ 00bc6210 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bc521c bytes 2d570294
+ 00bc6210 bytes 24570294
- 00bc5238 ["INT_ADD", "register:40f0:8", ["const:bc5238:8", "const:4:8"]]
- 00bc5238 ["CALL", null, ["callee:00c5e980:8"]]
+ 00bc622c ["INT_ADD", "register:40f0:8", ["const:bc622c:8", "const:4:8"]]
+ 00bc622c ["CALL", null, ["callee:00c5e980:8"]]
- 00bc5238 bytes de610294
+ 00bc622c bytes d5610294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f5f31fb223090b2cafdf349a7b65a1c"></a>

### [`00bc52ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc52ec.md) → [`00bc62e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc62e0.md) _ZN8firebase13remote_config8internal20CompleteVoidCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bc7384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7384.md) [`00bc77d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc77d8.md) [`00c5d990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d990.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 3件 [`00bc8378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc8378.md) [`00bc87cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc87cc.md) [`00c5e960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e960.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5be40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be40.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc52ec.md#insn-00bc5328) · [`00bc5344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc52ec.md#insn-00bc5344) · [`00bc534c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc52ec.md#insn-00bc534c)
- 新版 [`00bc631c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc62e0.md#insn-00bc631c) · [`00bc6338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc62e0.md#insn-00bc6338) · [`00bc6340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc62e0.md#insn-00bc6340)

~~~diff
- 00bc5328 ["INT_ADD", "register:40f0:8", ["const:bc5328:8", "const:4:8"]]
- 00bc5328 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bc631c ["INT_ADD", "register:40f0:8", ["const:bc631c:8", "const:4:8"]]
+ 00bc631c ["CALL", null, ["callee:00c5bea0:8"]]
- 00bc5328 bytes ea560294
+ 00bc631c bytes e1560294
- 00bc5344 ["INT_ADD", "register:40f0:8", ["const:bc5344:8", "const:4:8"]]
- 00bc5344 ["CALL", null, ["callee:00c5be40:8"]]
+ 00bc6338 ["INT_ADD", "register:40f0:8", ["const:bc6338:8", "const:4:8"]]
+ 00bc6338 ["CALL", null, ["callee:00c5be40:8"]]
- 00bc5344 bytes cb560294
+ 00bc6338 bytes c2560294
- 00bc534c ["INT_ADD", "register:40f0:8", ["const:bc534c:8", "const:4:8"]]
- 00bc534c ["CALL", null, ["callee:00c5bb30:8"]]
+ 00bc6340 ["INT_ADD", "register:40f0:8", ["const:bc6340:8", "const:4:8"]]
+ 00bc6340 ["CALL", null, ["callee:00c5bb30:8"]]
- 00bc534c bytes 05560294
+ 00bc6340 bytes fc550294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1448d10248f8180a24c3d934b82fc5d8"></a>

### [`00bc5474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md) → [`00bc6468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6468.md) _ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bc641c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc641c.md) [`00bc66b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc66b4.md) [`00bc6dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6dc8.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d990.md)
- 新版 呼出元 3件 [`00bc7410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7410.md) [`00bc76a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc76a8.md) [`00bc7dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7dbc.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5e960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc54b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md#insn-00bc54b0) · [`00bc54fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md#insn-00bc54fc) · [`00bc5508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md#insn-00bc5508)
- 新版 [`00bc64a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6468.md#insn-00bc64a4) · [`00bc64f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6468.md#insn-00bc64f0) · [`00bc64fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6468.md#insn-00bc64fc)

~~~diff
- 00bc54b0 ["INT_ADD", "register:40f0:8", ["const:bc54b0:8", "const:4:8"]]
- 00bc54b0 ["CALL", null, ["callee:00c5e960:8"]]
+ 00bc64a4 ["INT_ADD", "register:40f0:8", ["const:bc64a4:8", "const:4:8"]]
+ 00bc64a4 ["CALL", null, ["callee:00c5e960:8"]]
- 00bc54b0 bytes 38610294
+ 00bc64a4 bytes 2f610294
- 00bc54fc ["INT_ADD", "register:40f0:8", ["const:bc54fc:8", "const:4:8"]]
- 00bc54fc ["CALL", null, ["callee:00c5ea20:8"]]
+ 00bc64f0 ["INT_ADD", "register:40f0:8", ["const:bc64f0:8", "const:4:8"]]
+ 00bc64f0 ["CALL", null, ["callee:00c5ea20:8"]]
- 00bc54fc bytes 55610294
+ 00bc64f0 bytes 4c610294
- 00bc5508 ["INT_ADD", "register:40f0:8", ["const:bc5508:8", "const:4:8"]]
- 00bc5508 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc64fc ["INT_ADD", "register:40f0:8", ["const:bc64fc:8", "const:4:8"]]
+ 00bc64fc ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc5508 bytes 72550294
+ 00bc64fc bytes 69550294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43caf2a8764f9276d86a6fdedaf16cd7"></a>

### [`00bc564c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc564c.md) → [`00bc6640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6640.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5da50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da50.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5ea20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ea20.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc569c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc564c.md#insn-00bc569c) · [`00bc56c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc564c.md#insn-00bc56c8) · [`00bc56f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc564c.md#insn-00bc56f4)
- 新版 [`00bc6690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6640.md#insn-00bc6690) · [`00bc66bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6640.md#insn-00bc66bc) · [`00bc66e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6640.md#insn-00bc66e8)

~~~diff
- 00bc569c ["INT_ADD", "register:40f0:8", ["const:bc569c:8", "const:4:8"]]
- 00bc569c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bc6690 ["INT_ADD", "register:40f0:8", ["const:bc6690:8", "const:4:8"]]
+ 00bc6690 ["CALL", null, ["callee:00c58f30:8"]]
- 00bc569c bytes 314a0294
+ 00bc6690 bytes 284a0294
- 00bc56c8 ["INT_ADD", "register:40f0:8", ["const:bc56c8:8", "const:4:8"]]
- 00bc56c8 ["CALL", null, ["callee:00c5c650:8"]]
+ 00bc66bc ["INT_ADD", "register:40f0:8", ["const:bc66bc:8", "const:4:8"]]
+ 00bc66bc ["CALL", null, ["callee:00c5c650:8"]]
- 00bc56c8 bytes ee570294
+ 00bc66bc bytes e5570294
- 00bc56f4 ["INT_ADD", "register:40f0:8", ["const:bc56f4:8", "const:4:8"]]
- 00bc56f4 ["CALL", null, ["callee:00c5bdb0:8"]]
+ 00bc66e8 ["INT_ADD", "register:40f0:8", ["const:bc66e8:8", "const:4:8"]]
+ 00bc66e8 ["CALL", null, ["callee:00c5bdb0:8"]]
- 00bc56f4 bytes bb550294
+ 00bc66e8 bytes b2550294
~~~


<a id="compare-84627caa4f053bdd544de3cbbaddb9c9"></a>

### [`00bc5a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a0c.md) → [`00bc6a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6a00.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27EnsureInitializedLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d890.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5e860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e860.md) · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a0c.md#insn-00bc5a2c) · [`00bc5a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a0c.md#insn-00bc5a38) · [`00bc5a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a0c.md#insn-00bc5a44)
- 新版 [`00bc6a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6a00.md#insn-00bc6a20) · [`00bc6a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6a00.md#insn-00bc6a2c) · [`00bc6a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6a00.md#insn-00bc6a38)

~~~diff
- 00bc5a2c ["INT_ADD", "register:40f0:8", ["const:bc5a2c:8", "const:4:8"]]
- 00bc5a2c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc6a20 ["INT_ADD", "register:40f0:8", ["const:bc6a20:8", "const:4:8"]]
+ 00bc6a20 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc5a2c bytes 29540294
+ 00bc6a20 bytes 20540294
- 00bc5a38 ["INT_ADD", "register:40f0:8", ["const:bc5a38:8", "const:4:8"]]
- 00bc5a38 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc6a2c ["INT_ADD", "register:40f0:8", ["const:bc6a2c:8", "const:4:8"]]
+ 00bc6a2c ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc5a38 bytes 2a540294
+ 00bc6a2c bytes 21540294
- 00bc5a44 ["INT_ADD", "register:40f0:8", ["const:bc5a44:8", "const:4:8"]]
- 00bc5a44 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bc6a38 ["INT_ADD", "register:40f0:8", ["const:bc6a38:8", "const:4:8"]]
+ 00bc6a38 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc5a44 bytes bf540294
+ 00bc6a38 bytes b6540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3373f7d694e55195d6beb1a4195b5f4"></a>

### [`00bc5d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5d38.md) → [`00bc6d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6d2c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal18ActivateLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d840.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5e810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e810.md) · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc5d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5d38.md#insn-00bc5d58) · [`00bc5d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5d38.md#insn-00bc5d64) · [`00bc5d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5d38.md#insn-00bc5d70)
- 新版 [`00bc6d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6d2c.md#insn-00bc6d4c) · [`00bc6d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6d2c.md#insn-00bc6d58) · [`00bc6d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc6/00bc6d2c.md#insn-00bc6d64)

~~~diff
- 00bc5d58 ["INT_ADD", "register:40f0:8", ["const:bc5d58:8", "const:4:8"]]
- 00bc5d58 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc6d4c ["INT_ADD", "register:40f0:8", ["const:bc6d4c:8", "const:4:8"]]
+ 00bc6d4c ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc5d58 bytes 5e530294
+ 00bc6d4c bytes 55530294
- 00bc5d64 ["INT_ADD", "register:40f0:8", ["const:bc5d64:8", "const:4:8"]]
- 00bc5d64 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc6d58 ["INT_ADD", "register:40f0:8", ["const:bc6d58:8", "const:4:8"]]
+ 00bc6d58 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc5d64 bytes 5f530294
+ 00bc6d58 bytes 56530294
- 00bc5d70 ["INT_ADD", "register:40f0:8", ["const:bc5d70:8", "const:4:8"]]
- 00bc5d70 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bc6d64 ["INT_ADD", "register:40f0:8", ["const:bc6d64:8", "const:4:8"]]
+ 00bc6d64 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc5d70 bytes f4530294
+ 00bc6d64 bytes eb530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-668a1b864d1e837ff1fa350372e3e4e0"></a>

### [`00bc6064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6064.md) → [`00bc7058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7058.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26FetchAndActivateLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d870.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5e840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e840.md) · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc6084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6064.md#insn-00bc6084) · [`00bc6090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6064.md#insn-00bc6090) · [`00bc609c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6064.md#insn-00bc609c)
- 新版 [`00bc7078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7058.md#insn-00bc7078) · [`00bc7084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7058.md#insn-00bc7084) · [`00bc7090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7058.md#insn-00bc7090)

~~~diff
- 00bc6084 ["INT_ADD", "register:40f0:8", ["const:bc6084:8", "const:4:8"]]
- 00bc6084 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc7078 ["INT_ADD", "register:40f0:8", ["const:bc7078:8", "const:4:8"]]
+ 00bc7078 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc6084 bytes 93520294
+ 00bc7078 bytes 8a520294
- 00bc6090 ["INT_ADD", "register:40f0:8", ["const:bc6090:8", "const:4:8"]]
- 00bc6090 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc7084 ["INT_ADD", "register:40f0:8", ["const:bc7084:8", "const:4:8"]]
+ 00bc7084 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc6090 bytes 94520294
+ 00bc7084 bytes 8b520294
- 00bc609c ["INT_ADD", "register:40f0:8", ["const:bc609c:8", "const:4:8"]]
- 00bc609c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bc7090 ["INT_ADD", "register:40f0:8", ["const:bc7090:8", "const:4:8"]]
+ 00bc7090 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc609c bytes 29530294
+ 00bc7090 bytes 20530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afec778a03a8fa7a8f0686d0d0132c39"></a>

### [`00bc638c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc638c.md) → [`00bc7380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7380.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15FetchLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d7d0.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5e7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e7a0.md) · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc63ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc638c.md#insn-00bc63ac) · [`00bc63b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc638c.md#insn-00bc63b8) · [`00bc63c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc638c.md#insn-00bc63c4)
- 新版 [`00bc73a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7380.md#insn-00bc73a0) · [`00bc73ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7380.md#insn-00bc73ac) · [`00bc73b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc7/00bc7380.md#insn-00bc73b8)

~~~diff
- 00bc63ac ["INT_ADD", "register:40f0:8", ["const:bc63ac:8", "const:4:8"]]
- 00bc63ac ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc73a0 ["INT_ADD", "register:40f0:8", ["const:bc73a0:8", "const:4:8"]]
+ 00bc73a0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc63ac bytes c9510294
+ 00bc73a0 bytes c0510294
- 00bc63b8 ["INT_ADD", "register:40f0:8", ["const:bc63b8:8", "const:4:8"]]
- 00bc63b8 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc73ac ["INT_ADD", "register:40f0:8", ["const:bc73ac:8", "const:4:8"]]
+ 00bc73ac ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc63b8 bytes ca510294
+ 00bc73ac bytes c1510294
- 00bc63c4 ["INT_ADD", "register:40f0:8", ["const:bc63c4:8", "const:4:8"]]
- 00bc63c4 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bc73b8 ["INT_ADD", "register:40f0:8", ["const:bc73b8:8", "const:4:8"]]
+ 00bc73b8 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc63c4 bytes 5f520294
+ 00bc73b8 bytes 56520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d13e6b14d565bb93d2b5f15cf2dad57"></a>

### [`00bc72f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc72f4.md) → [`00bc82e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc82e8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal21SetDefaultsLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d850.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5e820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e820.md) · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc72f4.md#insn-00bc7314) · [`00bc7320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc72f4.md#insn-00bc7320) · [`00bc732c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc72f4.md#insn-00bc732c)
- 新版 [`00bc8308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc82e8.md#insn-00bc8308) · [`00bc8314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc82e8.md#insn-00bc8314) · [`00bc8320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc82e8.md#insn-00bc8320)

~~~diff
- 00bc7314 ["INT_ADD", "register:40f0:8", ["const:bc7314:8", "const:4:8"]]
- 00bc7314 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc8308 ["INT_ADD", "register:40f0:8", ["const:bc8308:8", "const:4:8"]]
+ 00bc8308 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc7314 bytes ef4d0294
+ 00bc8308 bytes e64d0294
- 00bc7320 ["INT_ADD", "register:40f0:8", ["const:bc7320:8", "const:4:8"]]
- 00bc7320 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc8314 ["INT_ADD", "register:40f0:8", ["const:bc8314:8", "const:4:8"]]
+ 00bc8314 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc7320 bytes f04d0294
+ 00bc8314 bytes e74d0294
- 00bc732c ["INT_ADD", "register:40f0:8", ["const:bc732c:8", "const:4:8"]]
- 00bc732c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bc8320 ["INT_ADD", "register:40f0:8", ["const:bc8320:8", "const:4:8"]]
+ 00bc8320 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc732c bytes 854e0294
+ 00bc8320 bytes 7c4e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1daf639e6b145ffa575442311c02ce32"></a>

### [`00bc7748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7748.md) → [`00bc873c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc873c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27SetConfigSettingsLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8a0.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5e870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e870.md) · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7748.md#insn-00bc7768) · [`00bc7774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7748.md#insn-00bc7774) · [`00bc7780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7748.md#insn-00bc7780)
- 新版 [`00bc875c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc873c.md#insn-00bc875c) · [`00bc8768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc873c.md#insn-00bc8768) · [`00bc8774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc873c.md#insn-00bc8774)

~~~diff
- 00bc7768 ["INT_ADD", "register:40f0:8", ["const:bc7768:8", "const:4:8"]]
- 00bc7768 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc875c ["INT_ADD", "register:40f0:8", ["const:bc875c:8", "const:4:8"]]
+ 00bc875c ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc7768 bytes da4c0294
+ 00bc875c bytes d14c0294
- 00bc7774 ["INT_ADD", "register:40f0:8", ["const:bc7774:8", "const:4:8"]]
- 00bc7774 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc8768 ["INT_ADD", "register:40f0:8", ["const:bc8768:8", "const:4:8"]]
+ 00bc8768 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc7774 bytes db4c0294
+ 00bc8768 bytes d24c0294
- 00bc7780 ["INT_ADD", "register:40f0:8", ["const:bc7780:8", "const:4:8"]]
- 00bc7780 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bc8774 ["INT_ADD", "register:40f0:8", ["const:bc8774:8", "const:4:8"]]
+ 00bc8774 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc7780 bytes 704d0294
+ 00bc8774 bytes 674d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e42a187ad67965986a6c8ce7bf46e6"></a>

### [`00bc7e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7e90.md) → [`00bc8e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc8e84.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26SetCustomSignalsLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d880.md) · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5e850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e850.md) · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7e90.md#insn-00bc7eb0) · [`00bc7ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7e90.md#insn-00bc7ebc) · [`00bc7ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7e90.md#insn-00bc7ec8)
- 新版 [`00bc8ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc8e84.md#insn-00bc8ea4) · [`00bc8eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc8e84.md#insn-00bc8eb0) · [`00bc8ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc8e84.md#insn-00bc8ebc)

~~~diff
- 00bc7eb0 ["INT_ADD", "register:40f0:8", ["const:bc7eb0:8", "const:4:8"]]
- 00bc7eb0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc8ea4 ["INT_ADD", "register:40f0:8", ["const:bc8ea4:8", "const:4:8"]]
+ 00bc8ea4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc7eb0 bytes 084b0294
+ 00bc8ea4 bytes ff4a0294
- 00bc7ebc ["INT_ADD", "register:40f0:8", ["const:bc7ebc:8", "const:4:8"]]
- 00bc7ebc ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc8eb0 ["INT_ADD", "register:40f0:8", ["const:bc8eb0:8", "const:4:8"]]
+ 00bc8eb0 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc7ebc bytes 094b0294
+ 00bc8eb0 bytes 004b0294
- 00bc7ec8 ["INT_ADD", "register:40f0:8", ["const:bc7ec8:8", "const:4:8"]]
- 00bc7ec8 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bc8ebc ["INT_ADD", "register:40f0:8", ["const:bc8ebc:8", "const:4:8"]]
+ 00bc8ebc ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc7ec8 bytes 9e4b0294
+ 00bc8ebc bytes 954b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82441ce4c3126c5a5a0858e5a560d84d"></a>

### [`00bc8a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a50.md) → [`00bc9a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc9/00bc9a44.md) _ZN8firebase9MutexLockD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5da10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da10.md) · 呼出先 1件 [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5e9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e9e0.md) · 呼出先 1件 [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a50.md#insn-00bc8a5c)
- 新版 [`00bc9a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc9/00bc9a44.md#insn-00bc9a50)

~~~diff
- 00bc8a5c ["INT_ADD", "register:40f0:8", ["const:bc8a5c:8", "const:4:8"]]
- 00bc8a5c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc9a50 ["INT_ADD", "register:40f0:8", ["const:bc9a50:8", "const:4:8"]]
+ 00bc9a50 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc8a5c bytes 21480294
+ 00bc9a50 bytes 18480294
~~~


<a id="compare-86aa8d5ad431a8f1a616517b5adb54bd"></a>

### [`00bc96f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc96f0.md) → [`00bca6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca6e4.md) _ZN8firebase13remote_config8internal37JniConfigUpdateListener_nativeOnErrorEP7_JNIEnvP8_jobjectli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b621bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc96f0.md#insn-00bc9740) · [`00bc977c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc96f0.md#insn-00bc977c) · [`00bc9794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc96f0.md#insn-00bc9794)
- 新版 [`00bca734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca6e4.md#insn-00bca734) · [`00bca770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca6e4.md#insn-00bca770) · [`00bca788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca6e4.md#insn-00bca788)

~~~diff
- 00bc9740 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9740 ["INT_ADD", "register:40f0:8", ["const:bc9740:8", "const:4:8"]]
- 00bc9740 ["CALLIND", null, ["register:0:8"]]
+ 00bca734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca734 ["INT_ADD", "register:40f0:8", ["const:bca734:8", "const:4:8"]]
+ 00bca734 ["CALLIND", null, ["register:0:8"]]
- 00bc9740 bytes 00013fd6
+ 00bca734 bytes 00013fd6
- 00bc977c ["INT_ADD", "register:40f0:8", ["const:bc977c:8", "const:4:8"]]
- 00bc977c ["CALL", null, ["callee:00c58f50:8"]]
+ 00bca770 ["INT_ADD", "register:40f0:8", ["const:bca770:8", "const:4:8"]]
+ 00bca770 ["CALL", null, ["callee:00c58f50:8"]]
- 00bc977c bytes 013a0294
+ 00bca770 bytes f8390294
- 00bc9794 ["INT_ADD", "register:40f0:8", ["const:bc9794:8", "const:4:8"]]
- 00bc9794 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bca788 ["INT_ADD", "register:40f0:8", ["const:bca788:8", "const:4:8"]]
+ 00bca788 ["CALL", null, ["callee:00c58f50:8"]]
- 00bc9794 bytes fb390294
+ 00bca788 bytes f2390294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a6541e4a0b4f5fdaf16d0a829a0215e"></a>

### [`00bc9824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9824.md) → [`00bca818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca818.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5da30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da30.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da20.md)
- 新版 呼出元 1件 [`00c5ea00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ea00.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md) [`00c5e9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e9f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9824.md#insn-00bc9858) · [`00bc9874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9824.md#insn-00bc9874) · [`00bc989c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9824.md#insn-00bc989c)
- 新版 [`00bca84c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca818.md#insn-00bca84c) · [`00bca868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca818.md#insn-00bca868) · [`00bca890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca818.md#insn-00bca890)

~~~diff
- 00bc9858 ["INT_ADD", "register:40f0:8", ["const:bc9858:8", "const:4:8"]]
- 00bc9858 ["CALL", null, ["callee:00c5e9f0:8"]]
+ 00bca84c ["INT_ADD", "register:40f0:8", ["const:bca84c:8", "const:4:8"]]
+ 00bca84c ["CALL", null, ["callee:00c5e9f0:8"]]
- 00bc9858 bytes 72500294
+ 00bca84c bytes 69500294
- 00bc9874 ["INT_ADD", "register:40f0:8", ["const:bc9874:8", "const:4:8"]]
- 00bc9874 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bca868 ["INT_ADD", "register:40f0:8", ["const:bca868:8", "const:4:8"]]
+ 00bca868 ["CALL", null, ["callee:00c58f30:8"]]
- 00bc9874 bytes bb390294
+ 00bca868 bytes b2390294
- 00bc989c ["INT_ADD", "register:40f0:8", ["const:bc989c:8", "const:4:8"]]
- 00bc989c ["CALL", null, ["callee:00c5b8e0:8"]]
+ 00bca890 ["INT_ADD", "register:40f0:8", ["const:bca890:8", "const:4:8"]]
+ 00bca890 ["CALL", null, ["callee:00c5b8e0:8"]]
- 00bc989c bytes 1d440294
+ 00bca890 bytes 14440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff78d063118415c6c112d3b1189a2237"></a>

### [`00bc9914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9914.md) → [`00bca908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca908.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da20.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5e9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e9f0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc99b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9914.md#insn-00bc99b0) · [`00bc99f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9914.md#insn-00bc99f0)
- 新版 [`00bca9a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca908.md#insn-00bca9a4) · [`00bca9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca908.md#insn-00bca9e4)

~~~diff
- 00bc99b0 ["INT_ADD", "register:40f0:8", ["const:bc99b0:8", "const:4:8"]]
- 00bc99b0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bca9a4 ["INT_ADD", "register:40f0:8", ["const:bca9a4:8", "const:4:8"]]
+ 00bca9a4 ["CALL", null, ["callee:00c590f0:8"]]
- 00bc99b0 bytes dc390294
+ 00bca9a4 bytes d3390294
- 00bc99f0 ["INT_ADD", "register:40f0:8", ["const:bc99f0:8", "const:4:8"]]
- 00bc99f0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bca9e4 ["INT_ADD", "register:40f0:8", ["const:bca9e4:8", "const:4:8"]]
+ 00bca9e4 ["CALL", null, ["callee:00c590f0:8"]]
- 00bc99f0 bytes cc390294
+ 00bca9e4 bytes c3390294
~~~


<a id="compare-e3770a6b06c29e7d2def367d589d3d4a"></a>

### [`00bc9a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9a34.md) → [`00bcaa28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcaa28.md) FUN_00bcaa28

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bc9290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9290.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d760.md)
- 新版 呼出元 1件 [`00bca284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca284.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9a34.md#insn-00bc9a48)
- 新版 [`00bcaa3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcaa28.md#insn-00bcaa3c)

~~~diff
- 00bc9a48 ["INT_ADD", "register:40f0:8", ["const:bc9a48:8", "const:4:8"]]
- 00bc9a48 ["CALL", null, ["callee:00c5e730:8"]]
+ 00bcaa3c ["INT_ADD", "register:40f0:8", ["const:bcaa3c:8", "const:4:8"]]
+ 00bcaa3c ["CALL", null, ["callee:00c5e730:8"]]
- 00bc9a48 bytes 464f0294
+ 00bcaa3c bytes 3d4f0294
~~~


<a id="compare-a4ffbc1142583dec491676fae3699c12"></a>

### [`00bc9dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9dc4.md) → [`00bcadb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcadb8.md) _ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9e0.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5e9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e9b0.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9dc4.md#insn-00bc9de4) · [`00bc9df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9dc4.md#insn-00bc9df8) · [`00bc9e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9dc4.md#insn-00bc9e0c)
- 新版 [`00bcadd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcadb8.md#insn-00bcadd8) · [`00bcadec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcadb8.md#insn-00bcadec) · [`00bcae00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcadb8.md#insn-00bcae00)

~~~diff
- 00bc9de4 ["INT_ADD", "register:40f0:8", ["const:bc9de4:8", "const:4:8"]]
- 00bc9de4 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bcadd8 ["INT_ADD", "register:40f0:8", ["const:bcadd8:8", "const:4:8"]]
+ 00bcadd8 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc9de4 bytes d7430294
+ 00bcadd8 bytes ce430294
- 00bc9df8 ["INT_ADD", "register:40f0:8", ["const:bc9df8:8", "const:4:8"]]
- 00bc9df8 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bcadec ["INT_ADD", "register:40f0:8", ["const:bcadec:8", "const:4:8"]]
+ 00bcadec ["CALL", null, ["callee:00c5bea0:8"]]
- 00bc9df8 bytes 36440294
+ 00bcadec bytes 2d440294
- 00bc9e0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9e0c ["INT_ADD", "register:40f0:8", ["const:bc9e0c:8", "const:4:8"]]
- 00bc9e0c ["CALLIND", null, ["register:0:8"]]
+ 00bcae00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcae00 ["INT_ADD", "register:40f0:8", ["const:bcae00:8", "const:4:8"]]
+ 00bcae00 ["CALLIND", null, ["register:0:8"]]
- 00bc9e0c bytes 00013fd6
+ 00bcae00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2ccf44748f22813e35cc1e8f022d99"></a>

### [`00bc9f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md) → [`00bcaf6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcaf6c.md) _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9f0.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5e9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e9c0.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md#insn-00bc9f98) · [`00bc9fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md#insn-00bc9fac) · [`00bc9fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md#insn-00bc9fc0)
- 新版 [`00bcaf8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcaf6c.md#insn-00bcaf8c) · [`00bcafa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcaf6c.md#insn-00bcafa0) · [`00bcafb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcaf6c.md#insn-00bcafb4)

~~~diff
- 00bc9f98 ["INT_ADD", "register:40f0:8", ["const:bc9f98:8", "const:4:8"]]
- 00bc9f98 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bcaf8c ["INT_ADD", "register:40f0:8", ["const:bcaf8c:8", "const:4:8"]]
+ 00bcaf8c ["CALL", null, ["callee:00c5bd10:8"]]
- 00bc9f98 bytes 6a430294
+ 00bcaf8c bytes 61430294
- 00bc9fac ["INT_ADD", "register:40f0:8", ["const:bc9fac:8", "const:4:8"]]
- 00bc9fac ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bcafa0 ["INT_ADD", "register:40f0:8", ["const:bcafa0:8", "const:4:8"]]
+ 00bcafa0 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bc9fac bytes c9430294
+ 00bcafa0 bytes c0430294
- 00bc9fc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9fc0 ["INT_ADD", "register:40f0:8", ["const:bc9fc0:8", "const:4:8"]]
- 00bc9fc0 ["CALLIND", null, ["register:0:8"]]
+ 00bcafb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcafb4 ["INT_ADD", "register:40f0:8", ["const:bcafb4:8", "const:4:8"]]
+ 00bcafb4 ["CALLIND", null, ["register:0:8"]]
- 00bc9fc0 bytes 00013fd6
+ 00bcafb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f67ffab5e8c052cc3a5385b2f88e38db"></a>

### [`00bca3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca3c0.md) → [`00bcb3b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb3b4.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5d740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d740.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca3c0.md#insn-00bca3e0)
- 新版 [`00bcb3d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb3b4.md#insn-00bcb3d4)

~~~diff
- 00bca3e0 ["INT_ADD", "register:40f0:8", ["const:bca3e0:8", "const:4:8"]]
- 00bca3e0 ["CALL", null, ["callee:00c5e710:8"]]
+ 00bcb3d4 ["INT_ADD", "register:40f0:8", ["const:bcb3d4:8", "const:4:8"]]
+ 00bcb3d4 ["CALL", null, ["callee:00c5e710:8"]]
- 00bca3e0 bytes d84c0294
+ 00bcb3d4 bytes cf4c0294
~~~


<a id="compare-d360380260047cbfc8ace0a1db73f934"></a>

### [`00bca404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca404.md) → [`00bcb3f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb3f8.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalC2EPNS1_20RemoteConfigInternalENSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d750.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e720.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca404.md#insn-00bca438) · [`00bca45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca404.md#insn-00bca45c)
- 新版 [`00bcb42c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb3f8.md#insn-00bcb42c) · [`00bcb450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb3f8.md#insn-00bcb450)

~~~diff
- 00bca438 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca438 ["INT_ADD", "register:40f0:8", ["const:bca438:8", "const:4:8"]]
- 00bca438 ["CALLIND", null, ["register:0:8"]]
+ 00bcb42c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb42c ["INT_ADD", "register:40f0:8", ["const:bcb42c:8", "const:4:8"]]
+ 00bcb42c ["CALLIND", null, ["register:0:8"]]
- 00bca438 bytes 00013fd6
+ 00bcb42c bytes 00013fd6
- 00bca45c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca45c ["INT_ADD", "register:40f0:8", ["const:bca45c:8", "const:4:8"]]
- 00bca45c ["CALLIND", null, ["register:0:8"]]
+ 00bcb450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb450 ["INT_ADD", "register:40f0:8", ["const:bcb450:8", "const:4:8"]]
+ 00bcb450 ["CALLIND", null, ["register:0:8"]]
- 00bca45c bytes 00013fd6
+ 00bcb450 bytes 00013fd6
~~~


<a id="compare-8c724932148edac6ef9a9afc43af2edb"></a>

### [`00bca470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca470.md) → [`00bcb464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb464.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d760.md) · 呼出先 1件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md)
- 新版 呼出元 1件 [`00c5e730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e730.md) · 呼出先 1件 [`00b621bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca470.md#insn-00bca4a0) · [`00bca4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca470.md#insn-00bca4e4)
- 新版 [`00bcb494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb464.md#insn-00bcb494) · [`00bcb4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb464.md#insn-00bcb4d8)

~~~diff
- 00bca4a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca4a0 ["INT_ADD", "register:40f0:8", ["const:bca4a0:8", "const:4:8"]]
- 00bca4a0 ["CALLIND", null, ["register:0:8"]]
+ 00bcb494 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb494 ["INT_ADD", "register:40f0:8", ["const:bcb494:8", "const:4:8"]]
+ 00bcb494 ["CALLIND", null, ["register:0:8"]]
- 00bca4a0 bytes 00013fd6
+ 00bcb494 bytes 00013fd6
- 00bca4e4 ["INT_ADD", "register:40f0:8", ["const:bca4e4:8", "const:4:8"]]
- 00bca4e4 ["CALL", null, ["callee:00b621bc:8"]]
+ 00bcb4d8 ["INT_ADD", "register:40f0:8", ["const:bcb4d8:8", "const:4:8"]]
+ 00bcb4d8 ["CALL", null, ["callee:00b621bc:8"]]
- 00bca4e4 bytes 395bfe97
+ 00bcb4d8 bytes 395bfe97
~~~


<a id="compare-87c369bde74121c05c210ea0c8aab605"></a>

### [`00bca4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca4fc.md) → [`00bcb4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb4f0.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d740.md) · 呼出先 1件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md)
- 新版 呼出元 1件 [`00c5e710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e710.md) · 呼出先 1件 [`00b621bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca4fc.md#insn-00bca538)
- 新版 [`00bcb52c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb4f0.md#insn-00bcb52c)

~~~diff
- 00bca538 ["INT_ADD", "register:40f0:8", ["const:bca538:8", "const:4:8"]]
- 00bca538 ["CALL", null, ["callee:00b621bc:8"]]
+ 00bcb52c ["INT_ADD", "register:40f0:8", ["const:bcb52c:8", "const:4:8"]]
+ 00bcb52c ["CALL", null, ["callee:00b621bc:8"]]
- 00bca538 bytes 245bfe97
+ 00bcb52c bytes 245bfe97
~~~


<a id="compare-c91b67eb18de27b41c638d254b7ddb4e"></a>

### [`00bcad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcad34.md) → [`00bcbd28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbd28.md) _ZN8firebase4auth8AuthDataD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db80.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab20.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md) [`00c5da70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da70.md)
- 新版 呼出元 1件 [`00c5eb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eb50.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baf0.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md) [`00c5bcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcf0.md) [`00c5ea40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ea40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcad44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcad34.md#insn-00bcad44) · [`00bcad60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcad34.md#insn-00bcad60) · [`00bcad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcad34.md#insn-00bcad70)
- 新版 [`00bcbd38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbd28.md#insn-00bcbd38) · [`00bcbd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbd28.md#insn-00bcbd54) · [`00bcbd64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbd28.md#insn-00bcbd64)

~~~diff
- 00bcad44 ["INT_ADD", "register:40f0:8", ["const:bcad44:8", "const:4:8"]]
- 00bcad44 ["CALL", null, ["callee:00c5ea40:8"]]
+ 00bcbd38 ["INT_ADD", "register:40f0:8", ["const:bcbd38:8", "const:4:8"]]
+ 00bcbd38 ["CALL", null, ["callee:00c5ea40:8"]]
- 00bcad44 bytes 4b4b0294
+ 00bcbd38 bytes 424b0294
- 00bcad60 ["INT_ADD", "register:40f0:8", ["const:bcad60:8", "const:4:8"]]
- 00bcad60 ["CALL", null, ["callee:00c5eb10:8"]]
+ 00bcbd54 ["INT_ADD", "register:40f0:8", ["const:bcbd54:8", "const:4:8"]]
+ 00bcbd54 ["CALL", null, ["callee:00c5eb10:8"]]
- 00bcad60 bytes 784b0294
+ 00bcbd54 bytes 6f4b0294
- 00bcad70 ["INT_ADD", "register:40f0:8", ["const:bcad70:8", "const:4:8"]]
- 00bcad70 ["CALL", null, ["callee:00c5eb00:8"]]
+ 00bcbd64 ["INT_ADD", "register:40f0:8", ["const:bcbd64:8", "const:4:8"]]
+ 00bcbd64 ["CALL", null, ["callee:00c5eb00:8"]]
- 00bcad70 bytes 704b0294
+ 00bcbd64 bytes 674b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbd03f02f89fd0ac75dd0108010eb748"></a>

### [`00bcae80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcae80.md) → [`00bcbe74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbe74.md) _ZN8firebase4auth4AuthD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5db00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ead0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcae88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcae80.md#insn-00bcae88)
- 新版 [`00bcbe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbe74.md#insn-00bcbe7c)

~~~diff
- 00bcae88 ["INT_ADD", "register:40f0:8", ["const:bcae88:8", "const:4:8"]]
- 00bcae88 ["CALL", null, ["callee:00c5ead0:8"]]
+ 00bcbe7c ["INT_ADD", "register:40f0:8", ["const:bcbe7c:8", "const:4:8"]]
+ 00bcbe7c ["CALL", null, ["callee:00c5ead0:8"]]
- 00bcae88 bytes 1e4b0294
+ 00bcbe7c bytes 154b0294
~~~


<a id="compare-009cf7570c23d71b9a9df933d1bddeb3"></a>

### [`00bcb278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb278.md) → [`00bcc26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc26c.md) _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db40.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5eb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eb10.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb278.md#insn-00bcb2a0) · [`00bcb374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb278.md#insn-00bcb374)
- 新版 [`00bcc294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc26c.md#insn-00bcc294) · [`00bcc368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc26c.md#insn-00bcc368)

~~~diff
- 00bcb2a0 ["INT_ADD", "register:40f0:8", ["const:bcb2a0:8", "const:4:8"]]
- 00bcb2a0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bcc294 ["INT_ADD", "register:40f0:8", ["const:bcc294:8", "const:4:8"]]
+ 00bcc294 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcb2a0 bytes 0c3e0294
+ 00bcc294 bytes 033e0294
- 00bcb374 ["INT_ADD", "register:40f0:8", ["const:bcb374:8", "const:4:8"]]
- 00bcb374 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bcc368 ["INT_ADD", "register:40f0:8", ["const:bcc368:8", "const:4:8"]]
+ 00bcc368 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcb374 bytes db3d0294
+ 00bcc368 bytes d23d0294
~~~


<a id="compare-37651e8e82b05ba4da500a3b24b29f59"></a>

### [`00bcb38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb38c.md) → [`00bcc380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc380.md) _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db30.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5dad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dad0.md)
- 新版 呼出元 1件 [`00c5eb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eb00.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5eaa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eaa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb38c.md#insn-00bcb3c0) · [`00bcb494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb38c.md#insn-00bcb494)
- 新版 [`00bcc3b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc380.md#insn-00bcc3b4) · [`00bcc488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc380.md#insn-00bcc488)

~~~diff
- 00bcb3c0 ["INT_ADD", "register:40f0:8", ["const:bcb3c0:8", "const:4:8"]]
- 00bcb3c0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bcc3b4 ["INT_ADD", "register:40f0:8", ["const:bcc3b4:8", "const:4:8"]]
+ 00bcc3b4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcb3c0 bytes c43d0294
+ 00bcc3b4 bytes bb3d0294
- 00bcb494 ["INT_ADD", "register:40f0:8", ["const:bcb494:8", "const:4:8"]]
- 00bcb494 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bcc488 ["INT_ADD", "register:40f0:8", ["const:bcc488:8", "const:4:8"]]
+ 00bcc488 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcb494 bytes 933d0294
+ 00bcc488 bytes 8a3d0294
~~~


<a id="compare-2ad160e49d19db3f8292694771af2e62"></a>

### [`00bcb758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb758.md) → [`00bcc74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc74c.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dbd0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)
- 新版 呼出元 1件 [`00c5eba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eba0.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb758.md#insn-00bcb790) · [`00bcb7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb758.md#insn-00bcb7bc) · [`00bcb7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb758.md#insn-00bcb7dc)
- 新版 [`00bcc784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc74c.md#insn-00bcc784) · [`00bcc7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc74c.md#insn-00bcc7b0) · [`00bcc7d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc74c.md#insn-00bcc7d0)

~~~diff
- 00bcb790 ["INT_ADD", "register:40f0:8", ["const:bcb790:8", "const:4:8"]]
- 00bcb790 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bcc784 ["INT_ADD", "register:40f0:8", ["const:bcc784:8", "const:4:8"]]
+ 00bcc784 ["CALL", null, ["callee:00c58f30:8"]]
- 00bcb790 bytes f4310294
+ 00bcc784 bytes eb310294
- 00bcb7bc ["INT_ADD", "register:40f0:8", ["const:bcb7bc:8", "const:4:8"]]
- 00bcb7bc ["CALL", null, ["callee:00c590a0:8"]]
+ 00bcc7b0 ["INT_ADD", "register:40f0:8", ["const:bcc7b0:8", "const:4:8"]]
+ 00bcc7b0 ["CALL", null, ["callee:00c590a0:8"]]
- 00bcb7bc bytes 45320294
+ 00bcc7b0 bytes 3c320294
- 00bcb7dc ["INT_ADD", "register:40f0:8", ["const:bcb7dc:8", "const:4:8"]]
- 00bcb7dc ["CALL", null, ["callee:00c5bdb0:8"]]
+ 00bcc7d0 ["INT_ADD", "register:40f0:8", ["const:bcc7d0:8", "const:4:8"]]
+ 00bcc7d0 ["CALL", null, ["callee:00c5bdb0:8"]]
- 00bcb7dc bytes 813d0294
+ 00bcc7d0 bytes 783d0294
~~~


<a id="compare-134ee453b91ede1f9e4c0fec74a1bd3b"></a>

### [`00bcb980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb980.md) → [`00bcc974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc974.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dbb0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)
- 新版 呼出元 1件 [`00c5eb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eb80.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb980.md#insn-00bcb9b8) · [`00bcb9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb980.md#insn-00bcb9e4) · [`00bcba04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb980.md#insn-00bcba04)
- 新版 [`00bcc9ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc974.md#insn-00bcc9ac) · [`00bcc9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc974.md#insn-00bcc9d8) · [`00bcc9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcc974.md#insn-00bcc9f8)

~~~diff
- 00bcb9b8 ["INT_ADD", "register:40f0:8", ["const:bcb9b8:8", "const:4:8"]]
- 00bcb9b8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bcc9ac ["INT_ADD", "register:40f0:8", ["const:bcc9ac:8", "const:4:8"]]
+ 00bcc9ac ["CALL", null, ["callee:00c58f30:8"]]
- 00bcb9b8 bytes 6a310294
+ 00bcc9ac bytes 61310294
- 00bcb9e4 ["INT_ADD", "register:40f0:8", ["const:bcb9e4:8", "const:4:8"]]
- 00bcb9e4 ["CALL", null, ["callee:00c590a0:8"]]
+ 00bcc9d8 ["INT_ADD", "register:40f0:8", ["const:bcc9d8:8", "const:4:8"]]
+ 00bcc9d8 ["CALL", null, ["callee:00c590a0:8"]]
- 00bcb9e4 bytes bb310294
+ 00bcc9d8 bytes b2310294
- 00bcba04 ["INT_ADD", "register:40f0:8", ["const:bcba04:8", "const:4:8"]]
- 00bcba04 ["CALL", null, ["callee:00c5bdb0:8"]]
+ 00bcc9f8 ["INT_ADD", "register:40f0:8", ["const:bcc9f8:8", "const:4:8"]]
+ 00bcc9f8 ["CALL", null, ["callee:00c5bdb0:8"]]
- 00bcba04 bytes f73c0294
+ 00bcc9f8 bytes ee3c0294
~~~


<a id="compare-e157ee5d5e38b007b31dbaace8cbca56"></a>

### [`00bcba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcba40.md) → [`00bcca34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcca34.md) _ZNK8firebase4auth4Auth32FetchProvidersForEmailLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcba60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcba40.md#insn-00bcba60) · [`00bcba6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcba40.md#insn-00bcba6c) · [`00bcba78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcba40.md#insn-00bcba78)
- 新版 [`00bcca54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcca34.md#insn-00bcca54) · [`00bcca60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcca34.md#insn-00bcca60) · [`00bcca6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcca34.md#insn-00bcca6c)

~~~diff
- 00bcba60 ["INT_ADD", "register:40f0:8", ["const:bcba60:8", "const:4:8"]]
- 00bcba60 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bcca54 ["INT_ADD", "register:40f0:8", ["const:bcca54:8", "const:4:8"]]
+ 00bcca54 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcba60 bytes 1c3c0294
+ 00bcca54 bytes 133c0294
- 00bcba6c ["INT_ADD", "register:40f0:8", ["const:bcba6c:8", "const:4:8"]]
- 00bcba6c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bcca60 ["INT_ADD", "register:40f0:8", ["const:bcca60:8", "const:4:8"]]
+ 00bcca60 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcba6c bytes 1d3c0294
+ 00bcca60 bytes 143c0294
- 00bcba78 ["INT_ADD", "register:40f0:8", ["const:bcba78:8", "const:4:8"]]
- 00bcba78 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bcca6c ["INT_ADD", "register:40f0:8", ["const:bcca6c:8", "const:4:8"]]
+ 00bcca6c ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcba78 bytes b23c0294
+ 00bcca6c bytes a93c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6fae193f31466d55a6803ff88c26c6e"></a>

### [`00bcbad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbad0.md) → [`00bccac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccac4.md) _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbad0.md#insn-00bcbaf0) · [`00bcbafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbad0.md#insn-00bcbafc) · [`00bcbb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbad0.md#insn-00bcbb08)
- 新版 [`00bccae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccac4.md#insn-00bccae4) · [`00bccaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccac4.md#insn-00bccaf0) · [`00bccafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccac4.md#insn-00bccafc)

~~~diff
- 00bcbaf0 ["INT_ADD", "register:40f0:8", ["const:bcbaf0:8", "const:4:8"]]
- 00bcbaf0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bccae4 ["INT_ADD", "register:40f0:8", ["const:bccae4:8", "const:4:8"]]
+ 00bccae4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcbaf0 bytes f83b0294
+ 00bccae4 bytes ef3b0294
- 00bcbafc ["INT_ADD", "register:40f0:8", ["const:bcbafc:8", "const:4:8"]]
- 00bcbafc ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bccaf0 ["INT_ADD", "register:40f0:8", ["const:bccaf0:8", "const:4:8"]]
+ 00bccaf0 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcbafc bytes f93b0294
+ 00bccaf0 bytes f03b0294
- 00bcbb08 ["INT_ADD", "register:40f0:8", ["const:bcbb08:8", "const:4:8"]]
- 00bcbb08 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bccafc ["INT_ADD", "register:40f0:8", ["const:bccafc:8", "const:4:8"]]
+ 00bccafc ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcbb08 bytes 8e3c0294
+ 00bccafc bytes 853c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6920521f60fd88cbce90a1bf6fd664ae"></a>

### [`00bcbb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbb60.md) → [`00bccb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccb54.md) _ZNK8firebase4auth4Auth31SignInWithCustomTokenLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbb60.md#insn-00bcbb80) · [`00bcbb8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbb60.md#insn-00bcbb8c) · [`00bcbb98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbb60.md#insn-00bcbb98)
- 新版 [`00bccb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccb54.md#insn-00bccb74) · [`00bccb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccb54.md#insn-00bccb80) · [`00bccb8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccb54.md#insn-00bccb8c)

~~~diff
- 00bcbb80 ["INT_ADD", "register:40f0:8", ["const:bcbb80:8", "const:4:8"]]
- 00bcbb80 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bccb74 ["INT_ADD", "register:40f0:8", ["const:bccb74:8", "const:4:8"]]
+ 00bccb74 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcbb80 bytes d43b0294
+ 00bccb74 bytes cb3b0294
- 00bcbb8c ["INT_ADD", "register:40f0:8", ["const:bcbb8c:8", "const:4:8"]]
- 00bcbb8c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bccb80 ["INT_ADD", "register:40f0:8", ["const:bccb80:8", "const:4:8"]]
+ 00bccb80 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcbb8c bytes d53b0294
+ 00bccb80 bytes cc3b0294
- 00bcbb98 ["INT_ADD", "register:40f0:8", ["const:bcbb98:8", "const:4:8"]]
- 00bcbb98 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bccb8c ["INT_ADD", "register:40f0:8", ["const:bccb8c:8", "const:4:8"]]
+ 00bccb8c ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcbb98 bytes 6a3c0294
+ 00bccb8c bytes 613c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d73fc7f196e06a3d05177ea56ce4a9"></a>

### [`00bcbbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbbf0.md) → [`00bccbe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccbe4.md) _ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbbf0.md#insn-00bcbc10) · [`00bcbc1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbbf0.md#insn-00bcbc1c) · [`00bcbc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbbf0.md#insn-00bcbc28)
- 新版 [`00bccc04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccbe4.md#insn-00bccc04) · [`00bccc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccbe4.md#insn-00bccc10) · [`00bccc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccbe4.md#insn-00bccc1c)

~~~diff
- 00bcbc10 ["INT_ADD", "register:40f0:8", ["const:bcbc10:8", "const:4:8"]]
- 00bcbc10 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bccc04 ["INT_ADD", "register:40f0:8", ["const:bccc04:8", "const:4:8"]]
+ 00bccc04 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcbc10 bytes b03b0294
+ 00bccc04 bytes a73b0294
- 00bcbc1c ["INT_ADD", "register:40f0:8", ["const:bcbc1c:8", "const:4:8"]]
- 00bcbc1c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bccc10 ["INT_ADD", "register:40f0:8", ["const:bccc10:8", "const:4:8"]]
+ 00bccc10 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcbc1c bytes b13b0294
+ 00bccc10 bytes a83b0294
- 00bcbc28 ["INT_ADD", "register:40f0:8", ["const:bcbc28:8", "const:4:8"]]
- 00bcbc28 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bccc1c ["INT_ADD", "register:40f0:8", ["const:bccc1c:8", "const:4:8"]]
+ 00bccc1c ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcbc28 bytes 463c0294
+ 00bccc1c bytes 3d3c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ad2305a3ea8f0b1ef3caa4ec07bd04f"></a>

### [`00bcbc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md) → [`00bccc74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccc74.md) _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md#insn-00bcbca0) · [`00bcbcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md#insn-00bcbcac) · [`00bcbcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md#insn-00bcbcb8)
- 新版 [`00bccc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccc74.md#insn-00bccc94) · [`00bccca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccc74.md#insn-00bccca0) · [`00bcccac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccc74.md#insn-00bcccac)

~~~diff
- 00bcbca0 ["INT_ADD", "register:40f0:8", ["const:bcbca0:8", "const:4:8"]]
- 00bcbca0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bccc94 ["INT_ADD", "register:40f0:8", ["const:bccc94:8", "const:4:8"]]
+ 00bccc94 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcbca0 bytes 8c3b0294
+ 00bccc94 bytes 833b0294
- 00bcbcac ["INT_ADD", "register:40f0:8", ["const:bcbcac:8", "const:4:8"]]
- 00bcbcac ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bccca0 ["INT_ADD", "register:40f0:8", ["const:bccca0:8", "const:4:8"]]
+ 00bccca0 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcbcac bytes 8d3b0294
+ 00bccca0 bytes 843b0294
- 00bcbcb8 ["INT_ADD", "register:40f0:8", ["const:bcbcb8:8", "const:4:8"]]
- 00bcbcb8 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bcccac ["INT_ADD", "register:40f0:8", ["const:bcccac:8", "const:4:8"]]
+ 00bcccac ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcbcb8 bytes 223c0294
+ 00bcccac bytes 193c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da0d5f1a009857babdda452120147b0a"></a>

### [`00bcbd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbd10.md) → [`00bccd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd04.md) _ZNK8firebase4auth4Auth36SignInWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbd10.md#insn-00bcbd30) · [`00bcbd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbd10.md#insn-00bcbd3c) · [`00bcbd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbd10.md#insn-00bcbd48)
- 新版 [`00bccd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd04.md#insn-00bccd24) · [`00bccd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd04.md#insn-00bccd30) · [`00bccd3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd04.md#insn-00bccd3c)

~~~diff
- 00bcbd30 ["INT_ADD", "register:40f0:8", ["const:bcbd30:8", "const:4:8"]]
- 00bcbd30 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bccd24 ["INT_ADD", "register:40f0:8", ["const:bccd24:8", "const:4:8"]]
+ 00bccd24 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcbd30 bytes 683b0294
+ 00bccd24 bytes 5f3b0294
- 00bcbd3c ["INT_ADD", "register:40f0:8", ["const:bcbd3c:8", "const:4:8"]]
- 00bcbd3c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bccd30 ["INT_ADD", "register:40f0:8", ["const:bccd30:8", "const:4:8"]]
+ 00bccd30 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcbd3c bytes 693b0294
+ 00bccd30 bytes 603b0294
- 00bcbd48 ["INT_ADD", "register:40f0:8", ["const:bcbd48:8", "const:4:8"]]
- 00bcbd48 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bccd3c ["INT_ADD", "register:40f0:8", ["const:bccd3c:8", "const:4:8"]]
+ 00bccd3c ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcbd48 bytes fe3b0294
+ 00bccd3c bytes f53b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e49c0cf600ab758503269cee547962e5"></a>

### [`00bcbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md) → [`00bccd94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd94.md) _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md#insn-00bcbdc0) · [`00bcbdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md#insn-00bcbdcc) · [`00bcbdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md#insn-00bcbdd8)
- 新版 [`00bccdb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd94.md#insn-00bccdb4) · [`00bccdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd94.md#insn-00bccdc0) · [`00bccdcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd94.md#insn-00bccdcc)

~~~diff
- 00bcbdc0 ["INT_ADD", "register:40f0:8", ["const:bcbdc0:8", "const:4:8"]]
- 00bcbdc0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bccdb4 ["INT_ADD", "register:40f0:8", ["const:bccdb4:8", "const:4:8"]]
+ 00bccdb4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcbdc0 bytes 443b0294
+ 00bccdb4 bytes 3b3b0294
- 00bcbdcc ["INT_ADD", "register:40f0:8", ["const:bcbdcc:8", "const:4:8"]]
- 00bcbdcc ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bccdc0 ["INT_ADD", "register:40f0:8", ["const:bccdc0:8", "const:4:8"]]
+ 00bccdc0 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcbdcc bytes 453b0294
+ 00bccdc0 bytes 3c3b0294
- 00bcbdd8 ["INT_ADD", "register:40f0:8", ["const:bcbdd8:8", "const:4:8"]]
- 00bcbdd8 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bccdcc ["INT_ADD", "register:40f0:8", ["const:bccdcc:8", "const:4:8"]]
+ 00bccdcc ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcbdd8 bytes da3b0294
+ 00bccdcc bytes d13b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68ec95c7ff77da52dd71ef903cd8db94"></a>

### [`00bcbe80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe80.md) → [`00bcce74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcce74.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db90.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5db90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db90.md)
- 新版 呼出元 1件 [`00c5eb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eb60.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5eb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbe9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe80.md#insn-00bcbe9c) · [`00bcbea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe80.md#insn-00bcbea8)
- 新版 [`00bcce90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcce74.md#insn-00bcce90) · [`00bcce9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcce74.md#insn-00bcce9c)

~~~diff
- 00bcbe9c ["INT_ADD", "register:40f0:8", ["const:bcbe9c:8", "const:4:8"]]
- 00bcbe9c ["CALL", null, ["callee:00c5eb60:8"]]
+ 00bcce90 ["INT_ADD", "register:40f0:8", ["const:bcce90:8", "const:4:8"]]
+ 00bcce90 ["CALL", null, ["callee:00c5eb60:8"]]
- 00bcbe9c bytes 3d470294
+ 00bcce90 bytes 34470294
- 00bcbea8 ["INT_ADD", "register:40f0:8", ["const:bcbea8:8", "const:4:8"]]
- 00bcbea8 ["CALL", null, ["callee:00c5eb60:8"]]
+ 00bcce9c ["INT_ADD", "register:40f0:8", ["const:bcce9c:8", "const:4:8"]]
+ 00bcce9c ["CALL", null, ["callee:00c5eb60:8"]]
- 00bcbea8 bytes 3a470294
+ 00bcce9c bytes 31470294
~~~


<a id="compare-10569898b3d07b6d0c84fb85f405897f"></a>

### [`00bcc26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc26c.md) → [`00bcd260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd260.md) _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5da70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da70.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ea40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ea40.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc26c.md#insn-00bcc2c8)
- 新版 [`00bcd2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd260.md#insn-00bcd2bc)

~~~diff
- 00bcc2c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc2c8 ["INT_ADD", "register:40f0:8", ["const:bcc2c8:8", "const:4:8"]]
- 00bcc2c8 ["CALLIND", null, ["register:0:8"]]
+ 00bcd2bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd2bc ["INT_ADD", "register:40f0:8", ["const:bcd2bc:8", "const:4:8"]]
+ 00bcd2bc ["CALLIND", null, ["register:0:8"]]
- 00bcc2c8 bytes 00013fd6
+ 00bcd2bc bytes 00013fd6
~~~


<a id="compare-52ad4857c8fd5b957120ebde2c9d6f3a"></a>

### [`00bcc340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc340.md) → [`00bcd334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd334.md) _ZNK8firebase4auth4UsereqERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc340.md#insn-00bcc350) · [`00bcc35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc340.md#insn-00bcc35c)
- 新版 [`00bcd344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd334.md#insn-00bcd344) · [`00bcd350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd334.md#insn-00bcd350)

~~~diff
- 00bcc350 ["INT_ADD", "register:40f0:8", ["const:bcc350:8", "const:4:8"]]
- 00bcc350 ["CALL", null, ["callee:00c5bb00:8"]]
+ 00bcd344 ["INT_ADD", "register:40f0:8", ["const:bcd344:8", "const:4:8"]]
+ 00bcd344 ["CALL", null, ["callee:00c5bb00:8"]]
- 00bcc350 bytes f8390294
+ 00bcd344 bytes ef390294
- 00bcc35c ["INT_ADD", "register:40f0:8", ["const:bcc35c:8", "const:4:8"]]
- 00bcc35c ["CALL", null, ["callee:00c5bb00:8"]]
+ 00bcd350 ["INT_ADD", "register:40f0:8", ["const:bcd350:8", "const:4:8"]]
+ 00bcd350 ["CALL", null, ["callee:00c5bb00:8"]]
- 00bcc35c bytes f5390294
+ 00bcd350 bytes ec390294
~~~


<a id="compare-070122f453a24f20895d1e0d5386b402"></a>

### [`00bcc374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc374.md) → [`00bcd368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd368.md) _ZNK8firebase4auth4UserneERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc374.md#insn-00bcc384) · [`00bcc390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc374.md#insn-00bcc390)
- 新版 [`00bcd378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd368.md#insn-00bcd378) · [`00bcd384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd368.md#insn-00bcd384)

~~~diff
- 00bcc384 ["INT_ADD", "register:40f0:8", ["const:bcc384:8", "const:4:8"]]
- 00bcc384 ["CALL", null, ["callee:00c5bb00:8"]]
+ 00bcd378 ["INT_ADD", "register:40f0:8", ["const:bcd378:8", "const:4:8"]]
+ 00bcd378 ["CALL", null, ["callee:00c5bb00:8"]]
- 00bcc384 bytes eb390294
+ 00bcd378 bytes e2390294
- 00bcc390 ["INT_ADD", "register:40f0:8", ["const:bcc390:8", "const:4:8"]]
- 00bcc390 ["CALL", null, ["callee:00c5bb00:8"]]
+ 00bcd384 ["INT_ADD", "register:40f0:8", ["const:bcd384:8", "const:4:8"]]
+ 00bcd384 ["CALL", null, ["callee:00c5bb00:8"]]
- 00bcc390 bytes e8390294
+ 00bcd384 bytes df390294
~~~


<a id="compare-ba6b4d5dbd17d99ecc66e7d4ad32adeb"></a>

### [`00bcdbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdbe0.md) → [`00bcebd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcebd4.md) _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5dae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dae0.md) [`00c5dd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5eab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eab0.md) [`00c5ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ecd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcdbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdbe0.md#insn-00bcdbf4)
- 新版 [`00bcebe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcebd4.md#insn-00bcebe8)

~~~diff
- 00bcdbf4 ["INT_ADD", "register:40f0:8", ["const:bcdbf4:8", "const:4:8"]]
- 00bcdbf4 ["CALL", null, ["callee:00c5ecd0:8"]]
+ 00bcebe8 ["INT_ADD", "register:40f0:8", ["const:bcebe8:8", "const:4:8"]]
+ 00bcebe8 ["CALL", null, ["callee:00c5ecd0:8"]]
- 00bcdbf4 bytes 43400294
+ 00bcebe8 bytes 3a400294
~~~


<a id="compare-fd31ab5bafa58aca2a0616f21c3ec623"></a>

### [`00bcdc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md) → [`00bcebfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcebfc.md) _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5dac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dac0.md) [`00c5dd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5ea90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ea90.md) [`00c5ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ecd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcdc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md#insn-00bcdc20) · [`00bcdc2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md#insn-00bcdc2c) · [`00bcdc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md#insn-00bcdc34)
- 新版 [`00bcec14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcebfc.md#insn-00bcec14) · [`00bcec20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcebfc.md#insn-00bcec20) · [`00bcec28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcebfc.md#insn-00bcec28)

~~~diff
- 00bcdc20 ["INT_ADD", "register:40f0:8", ["const:bcdc20:8", "const:4:8"]]
- 00bcdc20 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bcec14 ["INT_ADD", "register:40f0:8", ["const:bcec14:8", "const:4:8"]]
+ 00bcec14 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bcdc20 bytes ac330294
+ 00bcec14 bytes a3330294
- 00bcdc2c ["INT_ADD", "register:40f0:8", ["const:bcdc2c:8", "const:4:8"]]
- 00bcdc2c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bcec20 ["INT_ADD", "register:40f0:8", ["const:bcec20:8", "const:4:8"]]
+ 00bcec20 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bcdc2c bytes ad330294
+ 00bcec20 bytes a4330294
- 00bcdc34 ["INT_ADD", "register:40f0:8", ["const:bcdc34:8", "const:4:8"]]
- 00bcdc34 ["CALL", null, ["callee:00c5ecd0:8"]]
+ 00bcec28 ["INT_ADD", "register:40f0:8", ["const:bcec28:8", "const:4:8"]]
+ 00bcec28 ["CALL", null, ["callee:00c5ecd0:8"]]
- 00bcdc34 bytes 33400294
+ 00bcec28 bytes 2a400294
~~~


<a id="compare-3f032bc313a2f47abe4706998cd4113b"></a>

### [`00bcde4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcde4c.md) → [`00bcee40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcee40.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFut

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ddb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddb0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dca0.md)
- 新版 呼出元 1件 [`00c5ed80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed80.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5ec70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcde80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcde4c.md#insn-00bcde80) · [`00bcde94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcde4c.md#insn-00bcde94) · [`00bcdec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcde4c.md#insn-00bcdec0)
- 新版 [`00bcee74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcee40.md#insn-00bcee74) · [`00bcee88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcee40.md#insn-00bcee88) · [`00bceeb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcee40.md#insn-00bceeb4)

~~~diff
- 00bcde80 ["INT_ADD", "register:40f0:8", ["const:bcde80:8", "const:4:8"]]
- 00bcde80 ["CALL", null, ["callee:00c5edb0:8"]]
+ 00bcee74 ["INT_ADD", "register:40f0:8", ["const:bcee74:8", "const:4:8"]]
+ 00bcee74 ["CALL", null, ["callee:00c5edb0:8"]]
- 00bcde80 bytes d83f0294
+ 00bcee74 bytes cf3f0294
- 00bcde94 ["INT_ADD", "register:40f0:8", ["const:bcde94:8", "const:4:8"]]
- 00bcde94 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bcee88 ["INT_ADD", "register:40f0:8", ["const:bcee88:8", "const:4:8"]]
+ 00bcee88 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bcde94 bytes 0f340294
+ 00bcee88 bytes 06340294
- 00bcdec0 ["INT_ADD", "register:40f0:8", ["const:bcdec0:8", "const:4:8"]]
- 00bcdec0 ["CALL", null, ["callee:00c5ec70:8"]]
+ 00bceeb4 ["INT_ADD", "register:40f0:8", ["const:bceeb4:8", "const:4:8"]]
+ 00bceeb4 ["CALL", null, ["callee:00c5ec70:8"]]
- 00bcdec0 bytes 783f0294
+ 00bceeb4 bytes 6f3f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e350382a6a7d39d0efba34c50587a19"></a>

### [`00bce474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce474.md) → [`00bcf468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf468.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dda0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc90.md)
- 新版 呼出元 1件 [`00c5ed70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed70.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5ec60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce474.md#insn-00bce4a8) · [`00bce4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce474.md#insn-00bce4bc) · [`00bce4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce474.md#insn-00bce4e8)
- 新版 [`00bcf49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf468.md#insn-00bcf49c) · [`00bcf4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf468.md#insn-00bcf4b0) · [`00bcf4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf468.md#insn-00bcf4dc)

~~~diff
- 00bce4a8 ["INT_ADD", "register:40f0:8", ["const:bce4a8:8", "const:4:8"]]
- 00bce4a8 ["CALL", null, ["callee:00c5edb0:8"]]
+ 00bcf49c ["INT_ADD", "register:40f0:8", ["const:bcf49c:8", "const:4:8"]]
+ 00bcf49c ["CALL", null, ["callee:00c5edb0:8"]]
- 00bce4a8 bytes 4e3e0294
+ 00bcf49c bytes 453e0294
- 00bce4bc ["INT_ADD", "register:40f0:8", ["const:bce4bc:8", "const:4:8"]]
- 00bce4bc ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bcf4b0 ["INT_ADD", "register:40f0:8", ["const:bcf4b0:8", "const:4:8"]]
+ 00bcf4b0 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bce4bc bytes 85320294
+ 00bcf4b0 bytes 7c320294
- 00bce4e8 ["INT_ADD", "register:40f0:8", ["const:bce4e8:8", "const:4:8"]]
- 00bce4e8 ["CALL", null, ["callee:00c5ec60:8"]]
+ 00bcf4dc ["INT_ADD", "register:40f0:8", ["const:bcf4dc:8", "const:4:8"]]
+ 00bcf4dc ["CALL", null, ["callee:00c5ec60:8"]]
- 00bce4e8 bytes ea3d0294
+ 00bcf4dc bytes e13d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5bad87385f226686683fa0ef6162a7d"></a>

### [`00bce828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce828.md) → [`00bcf81c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf81c.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ddc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddc0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dcb0.md)
- 新版 呼出元 1件 [`00c5ed90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed90.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5ec80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce828.md#insn-00bce85c) · [`00bce870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce828.md#insn-00bce870) · [`00bce89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce828.md#insn-00bce89c)
- 新版 [`00bcf850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf81c.md#insn-00bcf850) · [`00bcf864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf81c.md#insn-00bcf864) · [`00bcf890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf81c.md#insn-00bcf890)

~~~diff
- 00bce85c ["INT_ADD", "register:40f0:8", ["const:bce85c:8", "const:4:8"]]
- 00bce85c ["CALL", null, ["callee:00c5edb0:8"]]
+ 00bcf850 ["INT_ADD", "register:40f0:8", ["const:bcf850:8", "const:4:8"]]
+ 00bcf850 ["CALL", null, ["callee:00c5edb0:8"]]
- 00bce85c bytes 613d0294
+ 00bcf850 bytes 583d0294
- 00bce870 ["INT_ADD", "register:40f0:8", ["const:bce870:8", "const:4:8"]]
- 00bce870 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bcf864 ["INT_ADD", "register:40f0:8", ["const:bcf864:8", "const:4:8"]]
+ 00bcf864 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bce870 bytes 98310294
+ 00bcf864 bytes 8f310294
- 00bce89c ["INT_ADD", "register:40f0:8", ["const:bce89c:8", "const:4:8"]]
- 00bce89c ["CALL", null, ["callee:00c5ec80:8"]]
+ 00bcf890 ["INT_ADD", "register:40f0:8", ["const:bcf890:8", "const:4:8"]]
+ 00bcf890 ["CALL", null, ["callee:00c5ec80:8"]]
- 00bce89c bytes 053d0294
+ 00bcf890 bytes fc3c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53344511a68677e62e66f77ef4e4eec"></a>

### [`00bcf798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md) → [`00bd078c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd078c.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ddd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddd0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5eda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eda0.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5be40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be40.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md#insn-00bcf7cc) · [`00bcf7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md#insn-00bcf7e0) · [`00bcf80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md#insn-00bcf80c)
- 新版 [`00bd07c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd078c.md#insn-00bd07c0) · [`00bd07d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd078c.md#insn-00bd07d4) · [`00bd0800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd078c.md#insn-00bd0800)

~~~diff
- 00bcf7cc ["INT_ADD", "register:40f0:8", ["const:bcf7cc:8", "const:4:8"]]
- 00bcf7cc ["CALL", null, ["callee:00c5edb0:8"]]
+ 00bd07c0 ["INT_ADD", "register:40f0:8", ["const:bd07c0:8", "const:4:8"]]
+ 00bd07c0 ["CALL", null, ["callee:00c5edb0:8"]]
- 00bcf7cc bytes 85390294
+ 00bd07c0 bytes 7c390294
- 00bcf7e0 ["INT_ADD", "register:40f0:8", ["const:bcf7e0:8", "const:4:8"]]
- 00bcf7e0 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd07d4 ["INT_ADD", "register:40f0:8", ["const:bd07d4:8", "const:4:8"]]
+ 00bd07d4 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bcf7e0 bytes bc2d0294
+ 00bd07d4 bytes b32d0294
- 00bcf80c ["INT_ADD", "register:40f0:8", ["const:bcf80c:8", "const:4:8"]]
- 00bcf80c ["CALL", null, ["callee:00c5be40:8"]]
+ 00bd0800 ["INT_ADD", "register:40f0:8", ["const:bd0800:8", "const:4:8"]]
+ 00bd0800 ["CALL", null, ["callee:00c5be40:8"]]
- 00bcf80c bytes 992d0294
+ 00bd0800 bytes 902d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-302d1c3a6e6e6236cd9b00b5079eab9d"></a>

### [`00bcf93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf93c.md) → [`00bd0930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0930.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcdc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc4c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00bcec40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcec40.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf93c.md#insn-00bcf98c) · [`00bcf9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf93c.md#insn-00bcf9a8)
- 新版 [`00bd0980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0930.md#insn-00bd0980) · [`00bd099c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0930.md#insn-00bd099c)

~~~diff
- 00bcf98c ["INT_ADD", "register:40f0:8", ["const:bcf98c:8", "const:4:8"]]
- 00bcf98c ["CALL", null, ["callee:00c58f50:8"]]
+ 00bd0980 ["INT_ADD", "register:40f0:8", ["const:bd0980:8", "const:4:8"]]
+ 00bd0980 ["CALL", null, ["callee:00c58f50:8"]]
- 00bcf98c bytes 7d210294
+ 00bd0980 bytes 74210294
- 00bcf9a8 ["INT_ADD", "register:40f0:8", ["const:bcf9a8:8", "const:4:8"]]
- 00bcf9a8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bd099c ["INT_ADD", "register:40f0:8", ["const:bd099c:8", "const:4:8"]]
+ 00bd099c ["CALL", null, ["callee:00c58f50:8"]]
- 00bcf9a8 bytes 76210294
+ 00bd099c bytes 6d210294
~~~


<a id="compare-7165fc8528fdf4f503e02a9e51c6545b"></a>

### [`00bcfac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md) → [`00bd0abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0abc.md) _ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcdc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc4c.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc70.md)
- 新版 呼出元 1件 [`00bcec40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcec40.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5ec40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md#insn-00bcfb00) · [`00bcfb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md#insn-00bcfb18) · [`00bcfb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md#insn-00bcfb40)
- 新版 [`00bd0af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0abc.md#insn-00bd0af4) · [`00bd0b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0abc.md#insn-00bd0b0c) · [`00bd0b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0abc.md#insn-00bd0b34)

~~~diff
- 00bcfb00 ["INT_ADD", "register:40f0:8", ["const:bcfb00:8", "const:4:8"]]
- 00bcfb00 ["CALL", null, ["callee:00c5edc0:8"]]
+ 00bd0af4 ["INT_ADD", "register:40f0:8", ["const:bd0af4:8", "const:4:8"]]
+ 00bd0af4 ["CALL", null, ["callee:00c5edc0:8"]]
- 00bcfb00 bytes bc380294
+ 00bd0af4 bytes b3380294
- 00bcfb18 ["INT_ADD", "register:40f0:8", ["const:bcfb18:8", "const:4:8"]]
- 00bcfb18 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd0b0c ["INT_ADD", "register:40f0:8", ["const:bd0b0c:8", "const:4:8"]]
+ 00bd0b0c ["CALL", null, ["callee:00c5bea0:8"]]
- 00bcfb18 bytes ee2c0294
+ 00bd0b0c bytes e52c0294
- 00bcfb40 ["INT_ADD", "register:40f0:8", ["const:bcfb40:8", "const:4:8"]]
- 00bcfb40 ["CALL", null, ["callee:00c5ec40:8"]]
+ 00bd0b34 ["INT_ADD", "register:40f0:8", ["const:bd0b34:8", "const:4:8"]]
+ 00bd0b34 ["CALL", null, ["callee:00c5ec40:8"]]
- 00bcfb40 bytes 4c380294
+ 00bd0b34 bytes 43380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f080c3907088fa470acd3697bd33a123"></a>

### [`00bcfcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfcd4.md) → [`00bd0cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0cc8.md) _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de10.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5ede0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ede0.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfcf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfcd4.md#insn-00bcfcf4) · [`00bcfd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfcd4.md#insn-00bcfd08) · [`00bcfd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfcd4.md#insn-00bcfd1c)
- 新版 [`00bd0ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0cc8.md#insn-00bd0ce8) · [`00bd0cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0cc8.md#insn-00bd0cfc) · [`00bd0d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0cc8.md#insn-00bd0d10)

~~~diff
- 00bcfcf4 ["INT_ADD", "register:40f0:8", ["const:bcfcf4:8", "const:4:8"]]
- 00bcfcf4 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bd0ce8 ["INT_ADD", "register:40f0:8", ["const:bd0ce8:8", "const:4:8"]]
+ 00bd0ce8 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bcfcf4 bytes 132c0294
+ 00bd0ce8 bytes 0a2c0294
- 00bcfd08 ["INT_ADD", "register:40f0:8", ["const:bcfd08:8", "const:4:8"]]
- 00bcfd08 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd0cfc ["INT_ADD", "register:40f0:8", ["const:bd0cfc:8", "const:4:8"]]
+ 00bd0cfc ["CALL", null, ["callee:00c5bea0:8"]]
- 00bcfd08 bytes 722c0294
+ 00bd0cfc bytes 692c0294
- 00bcfd1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfd1c ["INT_ADD", "register:40f0:8", ["const:bcfd1c:8", "const:4:8"]]
- 00bcfd1c ["CALLIND", null, ["register:0:8"]]
+ 00bd0d10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0d10 ["INT_ADD", "register:40f0:8", ["const:bd0d10:8", "const:4:8"]]
+ 00bd0d10 ["CALLIND", null, ["register:0:8"]]
- 00bcfd1c bytes 00013fd6
+ 00bd0d10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5657e049df4680ea7374a9bc4a9f207"></a>

### [`00bcfd74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfd74.md) → [`00bd0d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0d68.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bce328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce328.md) [`00bdbc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbc08.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aac0.md) [`00c5ab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab20.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)
- 新版 呼出元 2件 [`00bcf31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf31c.md) [`00bdcbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdcbfc.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ba90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba90.md) [`00c5baf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baf0.md) [`00c5cec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfd74.md#insn-00bcfd8c) · [`00bcfd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfd74.md#insn-00bcfd94) · [`00bcfd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfd74.md#insn-00bcfd9c)
- 新版 [`00bd0d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0d68.md#insn-00bd0d80) · [`00bd0d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0d68.md#insn-00bd0d88) · [`00bd0d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0d68.md#insn-00bd0d90)

~~~diff
- 00bcfd8c ["INT_ADD", "register:40f0:8", ["const:bcfd8c:8", "const:4:8"]]
- 00bcfd8c ["CALL", null, ["callee:00c5baf0:8"]]
+ 00bd0d80 ["INT_ADD", "register:40f0:8", ["const:bd0d80:8", "const:4:8"]]
+ 00bd0d80 ["CALL", null, ["callee:00c5baf0:8"]]
- 00bcfd8c bytes 652b0294
+ 00bd0d80 bytes 5c2b0294
- 00bcfd94 ["INT_ADD", "register:40f0:8", ["const:bcfd94:8", "const:4:8"]]
- 00bcfd94 ["CALL", null, ["callee:00c5ba90:8"]]
+ 00bd0d88 ["INT_ADD", "register:40f0:8", ["const:bd0d88:8", "const:4:8"]]
+ 00bd0d88 ["CALL", null, ["callee:00c5ba90:8"]]
- 00bcfd94 bytes 4b2b0294
+ 00bd0d88 bytes 422b0294
- 00bcfd9c ["INT_ADD", "register:40f0:8", ["const:bcfd9c:8", "const:4:8"]]
- 00bcfd9c ["CALL", null, ["callee:00c5ba90:8"]]
+ 00bd0d90 ["INT_ADD", "register:40f0:8", ["const:bd0d90:8", "const:4:8"]]
+ 00bd0d90 ["CALL", null, ["callee:00c5ba90:8"]]
- 00bcfd9c bytes 492b0294
+ 00bd0d90 bytes 402b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2f640f506219e709930f6a3e7f0ee57"></a>

### [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) → [`00bd0dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0dd4.md) _ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00bce164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce164.md) [`00bce92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce92c.md) [`00bceb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb9c.md) [`00bced28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md) [`00bcefb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bcefb4.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc60.md)
- 新版 呼出元 8件 [`00bcf158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf158.md) [`00bcf920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf920.md) [`00bcfb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcfb90.md) [`00bcfd1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcfd1c.md) [`00bcffa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcffa8.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5ec30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md#insn-00bcfe18) · [`00bcfe30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md#insn-00bcfe30) · [`00bcfe58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md#insn-00bcfe58)
- 新版 [`00bd0e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0dd4.md#insn-00bd0e0c) · [`00bd0e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0dd4.md#insn-00bd0e24) · [`00bd0e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0dd4.md#insn-00bd0e4c)

~~~diff
- 00bcfe18 ["INT_ADD", "register:40f0:8", ["const:bcfe18:8", "const:4:8"]]
- 00bcfe18 ["CALL", null, ["callee:00c5edc0:8"]]
+ 00bd0e0c ["INT_ADD", "register:40f0:8", ["const:bd0e0c:8", "const:4:8"]]
+ 00bd0e0c ["CALL", null, ["callee:00c5edc0:8"]]
- 00bcfe18 bytes f6370294
+ 00bd0e0c bytes ed370294
- 00bcfe30 ["INT_ADD", "register:40f0:8", ["const:bcfe30:8", "const:4:8"]]
- 00bcfe30 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd0e24 ["INT_ADD", "register:40f0:8", ["const:bd0e24:8", "const:4:8"]]
+ 00bd0e24 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bcfe30 bytes 282c0294
+ 00bd0e24 bytes 1f2c0294
- 00bcfe58 ["INT_ADD", "register:40f0:8", ["const:bcfe58:8", "const:4:8"]]
- 00bcfe58 ["CALL", null, ["callee:00c5ec30:8"]]
+ 00bd0e4c ["INT_ADD", "register:40f0:8", ["const:bd0e4c:8", "const:4:8"]]
+ 00bd0e4c ["CALL", null, ["callee:00c5ec30:8"]]
- 00bcfe58 bytes 82370294
+ 00bd0e4c bytes 79370294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9152ec0f4eaf945c387c789b2d727e1e"></a>

### [`00bcffec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcffec.md) → [`00bd0fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0fe0.md) _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de00.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5edd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5edd0.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd000c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcffec.md#insn-00bd000c) · [`00bd0020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcffec.md#insn-00bd0020) · [`00bd0034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcffec.md#insn-00bd0034)
- 新版 [`00bd1000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0fe0.md#insn-00bd1000) · [`00bd1014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0fe0.md#insn-00bd1014) · [`00bd1028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0fe0.md#insn-00bd1028)

~~~diff
- 00bd000c ["INT_ADD", "register:40f0:8", ["const:bd000c:8", "const:4:8"]]
- 00bd000c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bd1000 ["INT_ADD", "register:40f0:8", ["const:bd1000:8", "const:4:8"]]
+ 00bd1000 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bd000c bytes 4d2b0294
+ 00bd1000 bytes 442b0294
- 00bd0020 ["INT_ADD", "register:40f0:8", ["const:bd0020:8", "const:4:8"]]
- 00bd0020 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd1014 ["INT_ADD", "register:40f0:8", ["const:bd1014:8", "const:4:8"]]
+ 00bd1014 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bd0020 bytes ac2b0294
+ 00bd1014 bytes a32b0294
- 00bd0034 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0034 ["INT_ADD", "register:40f0:8", ["const:bd0034:8", "const:4:8"]]
- 00bd0034 ["CALLIND", null, ["register:0:8"]]
+ 00bd1028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1028 ["INT_ADD", "register:40f0:8", ["const:bd1028:8", "const:4:8"]]
+ 00bd1028 ["CALLIND", null, ["register:0:8"]]
- 00bd0034 bytes 00013fd6
+ 00bd1028 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac67195ae120163403473be6e254a368"></a>

### [`00bd01a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd01a8.md) → [`00bd119c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd119c.md) _ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bce578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce578.md) [`00be02a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be02a0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc80.md)
- 新版 呼出元 2件 [`00bcf56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcf56c.md) [`00be1294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1294.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5ec50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd01e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd01a8.md#insn-00bd01e0) · [`00bd01f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd01a8.md#insn-00bd01f8) · [`00bd0220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd01a8.md#insn-00bd0220)
- 新版 [`00bd11d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd119c.md#insn-00bd11d4) · [`00bd11ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd119c.md#insn-00bd11ec) · [`00bd1214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd119c.md#insn-00bd1214)

~~~diff
- 00bd01e0 ["INT_ADD", "register:40f0:8", ["const:bd01e0:8", "const:4:8"]]
- 00bd01e0 ["CALL", null, ["callee:00c5edc0:8"]]
+ 00bd11d4 ["INT_ADD", "register:40f0:8", ["const:bd11d4:8", "const:4:8"]]
+ 00bd11d4 ["CALL", null, ["callee:00c5edc0:8"]]
- 00bd01e0 bytes 04370294
+ 00bd11d4 bytes fb360294
- 00bd01f8 ["INT_ADD", "register:40f0:8", ["const:bd01f8:8", "const:4:8"]]
- 00bd01f8 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd11ec ["INT_ADD", "register:40f0:8", ["const:bd11ec:8", "const:4:8"]]
+ 00bd11ec ["CALL", null, ["callee:00c5bea0:8"]]
- 00bd01f8 bytes 362b0294
+ 00bd11ec bytes 2d2b0294
- 00bd0220 ["INT_ADD", "register:40f0:8", ["const:bd0220:8", "const:4:8"]]
- 00bd0220 ["CALL", null, ["callee:00c5ec50:8"]]
+ 00bd1214 ["INT_ADD", "register:40f0:8", ["const:bd1214:8", "const:4:8"]]
+ 00bd1214 ["CALL", null, ["callee:00c5ec50:8"]]
- 00bd0220 bytes 98360294
+ 00bd1214 bytes 8f360294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0a2f588499cde1875da727e653f2280"></a>

### [`00bd03b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd03b4.md) → [`00bd13a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd13a8.md) _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de20.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5edf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5edf0.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd03d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd03b4.md#insn-00bd03d4) · [`00bd03e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd03b4.md#insn-00bd03e8) · [`00bd03fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd03b4.md#insn-00bd03fc)
- 新版 [`00bd13c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd13a8.md#insn-00bd13c8) · [`00bd13dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd13a8.md#insn-00bd13dc) · [`00bd13f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd13a8.md#insn-00bd13f0)

~~~diff
- 00bd03d4 ["INT_ADD", "register:40f0:8", ["const:bd03d4:8", "const:4:8"]]
- 00bd03d4 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bd13c8 ["INT_ADD", "register:40f0:8", ["const:bd13c8:8", "const:4:8"]]
+ 00bd13c8 ["CALL", null, ["callee:00c5bd10:8"]]
- 00bd03d4 bytes 5b2a0294
+ 00bd13c8 bytes 522a0294
- 00bd03e8 ["INT_ADD", "register:40f0:8", ["const:bd03e8:8", "const:4:8"]]
- 00bd03e8 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd13dc ["INT_ADD", "register:40f0:8", ["const:bd13dc:8", "const:4:8"]]
+ 00bd13dc ["CALL", null, ["callee:00c5bea0:8"]]
- 00bd03e8 bytes ba2a0294
+ 00bd13dc bytes b12a0294
- 00bd03fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd03fc ["INT_ADD", "register:40f0:8", ["const:bd03fc:8", "const:4:8"]]
- 00bd03fc ["CALLIND", null, ["register:0:8"]]
+ 00bd13f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd13f0 ["INT_ADD", "register:40f0:8", ["const:bd13f0:8", "const:4:8"]]
+ 00bd13f0 ["CALLIND", null, ["register:0:8"]]
- 00bd03fc bytes 00013fd6
+ 00bd13f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94663979001c2ad0d65937d757126078"></a>

### [`00bd055c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) → [`00bd1550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1550.md) _ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00bcf54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf54c.md) [`00bdf7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf7ec.md) [`00bdfa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md) [`00be04ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be04ec.md) [`00be06dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be06dc.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dcc0.md)
- 新版 呼出元 8件 [`00bd0540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0540.md) [`00be07e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be07e0.md) [`00be0a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0a08.md) [`00be14e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be14e0.md) [`00be16d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be16d0.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5ec90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md#insn-00bd0594) · [`00bd05ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md#insn-00bd05ac) · [`00bd05d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md#insn-00bd05d4)
- 新版 [`00bd1588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1550.md#insn-00bd1588) · [`00bd15a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1550.md#insn-00bd15a0) · [`00bd15c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1550.md#insn-00bd15c8)

~~~diff
- 00bd0594 ["INT_ADD", "register:40f0:8", ["const:bd0594:8", "const:4:8"]]
- 00bd0594 ["CALL", null, ["callee:00c5edc0:8"]]
+ 00bd1588 ["INT_ADD", "register:40f0:8", ["const:bd1588:8", "const:4:8"]]
+ 00bd1588 ["CALL", null, ["callee:00c5edc0:8"]]
- 00bd0594 bytes 17360294
+ 00bd1588 bytes 0e360294
- 00bd05ac ["INT_ADD", "register:40f0:8", ["const:bd05ac:8", "const:4:8"]]
- 00bd05ac ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bd15a0 ["INT_ADD", "register:40f0:8", ["const:bd15a0:8", "const:4:8"]]
+ 00bd15a0 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bd05ac bytes 492a0294
+ 00bd15a0 bytes 402a0294
- 00bd05d4 ["INT_ADD", "register:40f0:8", ["const:bd05d4:8", "const:4:8"]]
- 00bd05d4 ["CALL", null, ["callee:00c5ec90:8"]]
+ 00bd15c8 ["INT_ADD", "register:40f0:8", ["const:bd15c8:8", "const:4:8"]]
+ 00bd15c8 ["CALL", null, ["callee:00c5ec90:8"]]
- 00bd05d4 bytes bb350294
+ 00bd15c8 bytes b2350294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0796d350c4423bae6224755c4dd6e193"></a>

### [`00bd4714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4714.md) → [`00bd5708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5708.md) _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dde0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b020.md) [`00c5de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de50.md)
- 新版 呼出元 1件 [`00c5edb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5edb0.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bff0.md) [`00c5ee20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4714.md#insn-00bd4748) · [`00bd4760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4714.md#insn-00bd4760) · [`00bd476c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4714.md#insn-00bd476c)
- 新版 [`00bd573c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5708.md#insn-00bd573c) · [`00bd5754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5708.md#insn-00bd5754) · [`00bd5760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5708.md#insn-00bd5760)

~~~diff
- 00bd4748 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4748 ["INT_ADD", "register:40f0:8", ["const:bd4748:8", "const:4:8"]]
- 00bd4748 ["CALLIND", null, ["register:0:8"]]
+ 00bd573c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd573c ["INT_ADD", "register:40f0:8", ["const:bd573c:8", "const:4:8"]]
+ 00bd573c ["CALLIND", null, ["register:0:8"]]
- 00bd4748 bytes 00013fd6
+ 00bd573c bytes 00013fd6
- 00bd4760 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4760 ["INT_ADD", "register:40f0:8", ["const:bd4760:8", "const:4:8"]]
- 00bd4760 ["CALLIND", null, ["register:0:8"]]
+ 00bd5754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5754 ["INT_ADD", "register:40f0:8", ["const:bd5754:8", "const:4:8"]]
+ 00bd5754 ["CALLIND", null, ["register:0:8"]]
- 00bd4760 bytes 00013fd6
+ 00bd5754 bytes 00013fd6
- 00bd476c ["INT_ADD", "register:40f0:8", ["const:bd476c:8", "const:4:8"]]
- 00bd476c ["CALL", null, ["callee:00c5ee20:8"]]
+ 00bd5760 ["INT_ADD", "register:40f0:8", ["const:bd5760:8", "const:4:8"]]
+ 00bd5760 ["CALL", null, ["callee:00c5ee20:8"]]
- 00bd476c bytes b9250294
+ 00bd5760 bytes b0250294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17405fcc3fedb08bca54cb8831545782"></a>

### [`00bd484c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd484c.md) → [`00bd5840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5840.md) _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd50.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ed20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed20.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd487c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd484c.md#insn-00bd487c) · [`00bd4898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd484c.md#insn-00bd4898) · [`00bd48b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd484c.md#insn-00bd48b0)
- 新版 [`00bd5870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5840.md#insn-00bd5870) · [`00bd588c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5840.md#insn-00bd588c) · [`00bd58a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5840.md#insn-00bd58a4)

~~~diff
- 00bd487c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd487c ["INT_ADD", "register:40f0:8", ["const:bd487c:8", "const:4:8"]]
- 00bd487c ["CALLIND", null, ["register:0:8"]]
+ 00bd5870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5870 ["INT_ADD", "register:40f0:8", ["const:bd5870:8", "const:4:8"]]
+ 00bd5870 ["CALLIND", null, ["register:0:8"]]
- 00bd487c bytes 00013fd6
+ 00bd5870 bytes 00013fd6
- 00bd4898 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4898 ["INT_ADD", "register:40f0:8", ["const:bd4898:8", "const:4:8"]]
- 00bd4898 ["CALLIND", null, ["register:0:8"]]
+ 00bd588c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd588c ["INT_ADD", "register:40f0:8", ["const:bd588c:8", "const:4:8"]]
+ 00bd588c ["CALLIND", null, ["register:0:8"]]
- 00bd4898 bytes 00013fd6
+ 00bd588c bytes 00013fd6
- 00bd48b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd48b0 ["INT_ADD", "register:40f0:8", ["const:bd48b0:8", "const:4:8"]]
- 00bd48b0 ["CALLIND", null, ["register:0:8"]]
+ 00bd58a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd58a4 ["INT_ADD", "register:40f0:8", ["const:bd58a4:8", "const:4:8"]]
+ 00bd58a4 ["CALLIND", null, ["register:0:8"]]
- 00bd48b0 bytes 00013fd6
+ 00bd58a4 bytes 00013fd6
~~~


<a id="compare-f355cd5811ace8eb167e888a7eb15efa"></a>

### [`00bd4e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4e04.md) → [`00bd5df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5df8.md) _ZN8firebase4auth18AdditionalUserInfoaSEOS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5de40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de40.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md)
- 新版 呼出元 1件 [`00c5ee10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee10.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cec0.md) [`00c5ee00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4e04.md#insn-00bd4e44) · [`00bd4e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4e04.md#insn-00bd4e94) · [`00bd4ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4e04.md#insn-00bd4ec4)
- 新版 [`00bd5e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5df8.md#insn-00bd5e38) · [`00bd5e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5df8.md#insn-00bd5e88) · [`00bd5eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5df8.md#insn-00bd5eb8)

~~~diff
- 00bd4e44 ["INT_ADD", "register:40f0:8", ["const:bd4e44:8", "const:4:8"]]
- 00bd4e44 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bd5e38 ["INT_ADD", "register:40f0:8", ["const:bd5e38:8", "const:4:8"]]
+ 00bd5e38 ["CALL", null, ["callee:00c58f50:8"]]
- 00bd4e44 bytes 4f0c0294
+ 00bd5e38 bytes 460c0294
- 00bd4e94 ["INT_ADD", "register:40f0:8", ["const:bd4e94:8", "const:4:8"]]
- 00bd4e94 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bd5e88 ["INT_ADD", "register:40f0:8", ["const:bd5e88:8", "const:4:8"]]
+ 00bd5e88 ["CALL", null, ["callee:00c58f50:8"]]
- 00bd4e94 bytes 3b0c0294
+ 00bd5e88 bytes 320c0294
- 00bd4ec4 ["INT_ADD", "register:40f0:8", ["const:bd4ec4:8", "const:4:8"]]
- 00bd4ec4 ["CALL", null, ["callee:00c5cec0:8"]]
+ 00bd5eb8 ["INT_ADD", "register:40f0:8", ["const:bd5eb8:8", "const:4:8"]]
+ 00bd5eb8 ["CALL", null, ["callee:00c5cec0:8"]]
- 00bd4ec4 bytes 0b1c0294
+ 00bd5eb8 bytes 021c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a896bee533c87a103c8ba32c38cf1c"></a>

### [`00bd930c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd930c.md) → [`00bda300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda300.md) _ZN8firebase4auth10CredentialC2ERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ee00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd9330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd930c.md#insn-00bd9330)
- 新版 [`00bda324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda300.md#insn-00bda324)

~~~diff
- 00bd9330 ["INT_ADD", "register:40f0:8", ["const:bd9330:8", "const:4:8"]]
- 00bd9330 ["CALL", null, ["callee:00c5ee00:8"]]
+ 00bda324 ["INT_ADD", "register:40f0:8", ["const:bda324:8", "const:4:8"]]
+ 00bda324 ["CALL", null, ["callee:00c5ee00:8"]]
- 00bd9330 bytes c0120294
+ 00bda324 bytes b7120294
~~~


<a id="compare-5d302a2b40d00b7e8ebd460b8bf7ae55"></a>

### [`00bd97b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd97b0.md) → [`00bda7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda7a4.md) _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df00.md) · 呼出先 2件 [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md)
- 新版 呼出元 1件 [`00c5eed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eed0.md) · 呼出先 2件 [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5ee00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd97c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd97b0.md#insn-00bd97c4) · [`00bd97f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd97b0.md#insn-00bd97f0)
- 新版 [`00bda7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda7a4.md#insn-00bda7b8) · [`00bda7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda7a4.md#insn-00bda7e4)

~~~diff
- 00bd97c4 ["INT_ADD", "register:40f0:8", ["const:bd97c4:8", "const:4:8"]]
- 00bd97c4 ["CALL", null, ["callee:00c5ee00:8"]]
+ 00bda7b8 ["INT_ADD", "register:40f0:8", ["const:bda7b8:8", "const:4:8"]]
+ 00bda7b8 ["CALL", null, ["callee:00c5ee00:8"]]
- 00bd97c4 bytes 9b110294
+ 00bda7b8 bytes 92110294
- 00bd97f0 ["INT_ADD", "register:40f0:8", ["const:bd97f0:8", "const:4:8"]]
- 00bd97f0 ["CALL", null, ["callee:00c5c150:8"]]
+ 00bda7e4 ["INT_ADD", "register:40f0:8", ["const:bda7e4:8", "const:4:8"]]
+ 00bda7e4 ["CALL", null, ["callee:00c5c150:8"]]
- 00bd97f0 bytes 64060294
+ 00bda7e4 bytes 5b060294
~~~


<a id="compare-c38cc77f71a3c6481e1b0b850330b628"></a>

### [`00bda5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda5d0.md) → [`00bdb5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb5c4.md) _ZN8firebase4auth22GameCenterAuthProvider23GetCredentialLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 8件 [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0087c3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c3c0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda5d0.md#insn-00bda5f4) · [`00bda604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda5d0.md#insn-00bda604) · [`00bda610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda5d0.md#insn-00bda610)
- 新版 [`00bdb5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb5c4.md#insn-00bdb5e8) · [`00bdb5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb5c4.md#insn-00bdb5f8) · [`00bdb604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb5c4.md#insn-00bdb604)

~~~diff
- 00bda5f4 ["INT_ADD", "register:40f0:8", ["const:bda5f4:8", "const:4:8"]]
- 00bda5f4 ["CALL", null, ["callee:00c5ebf0:8"]]
+ 00bdb5e8 ["INT_ADD", "register:40f0:8", ["const:bdb5e8:8", "const:4:8"]]
+ 00bdb5e8 ["CALL", null, ["callee:00c5ebf0:8"]]
- 00bda5f4 bytes 8b0d0294
+ 00bdb5e8 bytes 820d0294
- 00bda604 ["INT_ADD", "register:40f0:8", ["const:bda604:8", "const:4:8"]]
- 00bda604 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bdb5f8 ["INT_ADD", "register:40f0:8", ["const:bdb5f8:8", "const:4:8"]]
+ 00bdb5f8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bda604 bytes 33010294
+ 00bdb5f8 bytes 2a010294
- 00bda610 ["INT_ADD", "register:40f0:8", ["const:bda610:8", "const:4:8"]]
- 00bda610 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bdb604 ["INT_ADD", "register:40f0:8", ["const:bdb604:8", "const:4:8"]]
+ 00bdb604 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bda610 bytes 34010294
+ 00bdb604 bytes 2b010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9af9222e24b1ee2af94c0f3b3a80c1f3"></a>

### [`00bda714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda714.md) → [`00bdb708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb708.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda714.md#insn-00bda728)
- 新版 [`00bdb71c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb708.md#insn-00bdb71c)

~~~diff
- 00bda728 ["INT_ADD", "register:40f0:8", ["const:bda728:8", "const:4:8"]]
- 00bda728 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bdb71c ["INT_ADD", "register:40f0:8", ["const:bdb71c:8", "const:4:8"]]
+ 00bdb71c ["CALL", null, ["callee:00c58f30:8"]]
- 00bda728 bytes 0ef60194
+ 00bdb71c bytes 05f60194
~~~


<a id="compare-e07d4cfa9d68599085d2427b1d5c2f3f"></a>

### [`00bda7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7ac.md) → [`00bdb7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb7a0.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC1ERKS2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5eee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7ac.md#insn-00bda7c4)
- 新版 [`00bdb7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb7a0.md#insn-00bdb7b8)

~~~diff
- 00bda7c4 ["INT_ADD", "register:40f0:8", ["const:bda7c4:8", "const:4:8"]]
- 00bda7c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bdb7b8 ["INT_ADD", "register:40f0:8", ["const:bdb7b8:8", "const:4:8"]]
+ 00bdb7b8 ["CALL", null, ["callee:00c58f30:8"]]
- 00bda7c4 bytes e7f50194
+ 00bdb7b8 bytes def50194
~~~


<a id="compare-8c36bb19d9fb383b284caafda8394f3a"></a>

### [`00bda888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda888.md) → [`00bdb87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb87c.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bda8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda888.md#insn-00bda8a4)
- 新版 [`00bdb898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb87c.md#insn-00bdb898)

~~~diff
- 00bda8a4 ["INT_ADD", "register:40f0:8", ["const:bda8a4:8", "const:4:8"]]
- 00bda8a4 ["CALL", null, ["callee:00c5eee0:8"]]
+ 00bdb898 ["INT_ADD", "register:40f0:8", ["const:bdb898:8", "const:4:8"]]
+ 00bdb898 ["CALL", null, ["callee:00c5eee0:8"]]
- 00bda8a4 bytes 9b0d0294
+ 00bdb898 bytes 920d0294
~~~


<a id="compare-214d7c0759ade5a0e6c69252566cf22c"></a>

### [`00bdb37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb37c.md) → [`00bdc370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc370.md) _ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdb3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb37c.md#insn-00bdb3a4) · [`00bdb3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb37c.md#insn-00bdb3b8) · [`00bdb3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb37c.md#insn-00bdb3c8)
- 新版 [`00bdc398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc370.md#insn-00bdc398) · [`00bdc3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc370.md#insn-00bdc3ac) · [`00bdc3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc370.md#insn-00bdc3bc)

~~~diff
- 00bdb3a4 ["INT_ADD", "register:40f0:8", ["const:bdb3a4:8", "const:4:8"]]
- 00bdb3a4 ["CALL", null, ["callee:00c5bfc0:8"]]
+ 00bdc398 ["INT_ADD", "register:40f0:8", ["const:bdc398:8", "const:4:8"]]
+ 00bdc398 ["CALL", null, ["callee:00c5bfc0:8"]]
- 00bdb3a4 bytes 13ff0194
+ 00bdc398 bytes 0aff0194
- 00bdb3b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdb3b8 ["INT_ADD", "register:40f0:8", ["const:bdb3b8:8", "const:4:8"]]
- 00bdb3b8 ["CALLIND", null, ["register:0:8"]]
+ 00bdc3ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdc3ac ["INT_ADD", "register:40f0:8", ["const:bdc3ac:8", "const:4:8"]]
+ 00bdc3ac ["CALLIND", null, ["register:0:8"]]
- 00bdb3b8 bytes 00013fd6
+ 00bdc3ac bytes 00013fd6
- 00bdb3c8 ["INT_ADD", "register:40f0:8", ["const:bdb3c8:8", "const:4:8"]]
- 00bdb3c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bdc3bc ["INT_ADD", "register:40f0:8", ["const:bdc3bc:8", "const:4:8"]]
+ 00bdc3bc ["CALL", null, ["callee:00c58f50:8"]]
- 00bdb3c8 bytes eef20194
+ 00bdc3bc bytes e5f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a039ce53815237633bc595daa222f2af"></a>

### [`00bdb58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb58c.md) → [`00bdc580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc580.md) _ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdb5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb58c.md#insn-00bdb5b4) · [`00bdb5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb58c.md#insn-00bdb5c8) · [`00bdb5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb58c.md#insn-00bdb5d8)
- 新版 [`00bdc5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc580.md#insn-00bdc5a8) · [`00bdc5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc580.md#insn-00bdc5bc) · [`00bdc5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc580.md#insn-00bdc5cc)

~~~diff
- 00bdb5b4 ["INT_ADD", "register:40f0:8", ["const:bdb5b4:8", "const:4:8"]]
- 00bdb5b4 ["CALL", null, ["callee:00c5c430:8"]]
+ 00bdc5a8 ["INT_ADD", "register:40f0:8", ["const:bdc5a8:8", "const:4:8"]]
+ 00bdc5a8 ["CALL", null, ["callee:00c5c430:8"]]
- 00bdb5b4 bytes abff0194
+ 00bdc5a8 bytes a2ff0194
- 00bdb5c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdb5c8 ["INT_ADD", "register:40f0:8", ["const:bdb5c8:8", "const:4:8"]]
- 00bdb5c8 ["CALLIND", null, ["register:0:8"]]
+ 00bdc5bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdc5bc ["INT_ADD", "register:40f0:8", ["const:bdc5bc:8", "const:4:8"]]
+ 00bdc5bc ["CALLIND", null, ["register:0:8"]]
- 00bdb5c8 bytes 00013fd6
+ 00bdc5bc bytes 00013fd6
- 00bdb5d8 ["INT_ADD", "register:40f0:8", ["const:bdb5d8:8", "const:4:8"]]
- 00bdb5d8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bdc5cc ["INT_ADD", "register:40f0:8", ["const:bdc5cc:8", "const:4:8"]]
+ 00bdc5cc ["CALL", null, ["callee:00c58f50:8"]]
- 00bdb5d8 bytes 6af20194
+ 00bdc5cc bytes 61f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a223280433aead69cb8dcd5a4997bdf"></a>

### [`00bdb8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb8c4.md) → [`00bdc8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc8b8.md) _ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b7bc.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d100.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053badc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053badc.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5e0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdb8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb8c4.md#insn-00bdb8fc) · [`00bdb908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb8c4.md#insn-00bdb908)
- 新版 [`00bdc8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc8b8.md#insn-00bdc8f0) · [`00bdc8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc8b8.md#insn-00bdc8fc)

~~~diff
- 00bdb8fc ["INT_ADD", "register:40f0:8", ["const:bdb8fc:8", "const:4:8"]]
- 00bdb8fc ["CALL", null, ["callee:00c5c150:8"]]
+ 00bdc8f0 ["INT_ADD", "register:40f0:8", ["const:bdc8f0:8", "const:4:8"]]
+ 00bdc8f0 ["CALL", null, ["callee:00c5c150:8"]]
- 00bdb8fc bytes 21fe0194
+ 00bdc8f0 bytes 18fe0194
- 00bdb908 ["INT_ADD", "register:40f0:8", ["const:bdb908:8", "const:4:8"]]
- 00bdb908 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bdc8fc ["INT_ADD", "register:40f0:8", ["const:bdc8fc:8", "const:4:8"]]
+ 00bdc8fc ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bdb908 bytes fe050294
+ 00bdc8fc bytes f5050294
~~~


<a id="compare-063baeaedfe67d4baa5b499c8b68bf20"></a>

### [`00bdc4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4c4.md) → [`00bdd4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd4b8.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bda4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda4ac.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ded0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ded0.md)
- 新版 呼出元 1件 [`00bdb4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb4a0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5eea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4c4.md#insn-00bdc4d8)
- 新版 [`00bdd4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd4b8.md#insn-00bdd4cc)

~~~diff
- 00bdc4d8 ["INT_ADD", "register:40f0:8", ["const:bdc4d8:8", "const:4:8"]]
- 00bdc4d8 ["CALL", null, ["callee:00c5eea0:8"]]
+ 00bdd4cc ["INT_ADD", "register:40f0:8", ["const:bdd4cc:8", "const:4:8"]]
+ 00bdd4cc ["CALL", null, ["callee:00c5eea0:8"]]
- 00bdc4d8 bytes 7e060294
+ 00bdd4cc bytes 75060294
~~~


<a id="compare-a338835bb59fc56916da40a1a2d8f167"></a>

### [`00bdc5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc5f8.md) → [`00bdd5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd5ec.md) _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df20.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5eef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eef0.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc5f8.md#insn-00bdc618) · [`00bdc62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc5f8.md#insn-00bdc62c) · [`00bdc640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc5f8.md#insn-00bdc640)
- 新版 [`00bdd60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd5ec.md#insn-00bdd60c) · [`00bdd620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd5ec.md#insn-00bdd620) · [`00bdd634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd5ec.md#insn-00bdd634)

~~~diff
- 00bdc618 ["INT_ADD", "register:40f0:8", ["const:bdc618:8", "const:4:8"]]
- 00bdc618 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00bdd60c ["INT_ADD", "register:40f0:8", ["const:bdd60c:8", "const:4:8"]]
+ 00bdd60c ["CALL", null, ["callee:00c5bd10:8"]]
- 00bdc618 bytes caf90194
+ 00bdd60c bytes c1f90194
- 00bdc62c ["INT_ADD", "register:40f0:8", ["const:bdc62c:8", "const:4:8"]]
- 00bdc62c ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bdd620 ["INT_ADD", "register:40f0:8", ["const:bdd620:8", "const:4:8"]]
+ 00bdd620 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bdc62c bytes 29fa0194
+ 00bdd620 bytes 20fa0194
- 00bdc640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdc640 ["INT_ADD", "register:40f0:8", ["const:bdc640:8", "const:4:8"]]
- 00bdc640 ["CALLIND", null, ["register:0:8"]]
+ 00bdd634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd634 ["INT_ADD", "register:40f0:8", ["const:bdd634:8", "const:4:8"]]
+ 00bdd634 ["CALLIND", null, ["register:0:8"]]
- 00bdc640 bytes 00013fd6
+ 00bdd634 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b7107d2b18aecd9b21428a4fa01344d"></a>

### [`00bdc698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc698.md) → [`00bdd68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd68c.md) _ZN8firebase4auth10AuthResultC2ERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dec0.md) · 呼出先 3件 [`00c5ab10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab10.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md) [`00c5def0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5def0.md)
- 新版 呼出元 1件 [`00c5ee90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee90.md) · 呼出先 3件 [`00c5bae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bae0.md) [`00c5ee00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee00.md) [`00c5eec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc698.md#insn-00bdc6b0) · [`00bdc6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc698.md#insn-00bdc6d4) · [`00bdc6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc698.md#insn-00bdc6e0)
- 新版 [`00bdd6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd68c.md#insn-00bdd6a4) · [`00bdd6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd68c.md#insn-00bdd6c8) · [`00bdd6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd68c.md#insn-00bdd6d4)

~~~diff
- 00bdc6b0 ["INT_ADD", "register:40f0:8", ["const:bdc6b0:8", "const:4:8"]]
- 00bdc6b0 ["CALL", null, ["callee:00c5eec0:8"]]
+ 00bdd6a4 ["INT_ADD", "register:40f0:8", ["const:bdd6a4:8", "const:4:8"]]
+ 00bdd6a4 ["CALL", null, ["callee:00c5eec0:8"]]
- 00bdc6b0 bytes 10060294
+ 00bdd6a4 bytes 07060294
- 00bdc6d4 ["INT_ADD", "register:40f0:8", ["const:bdc6d4:8", "const:4:8"]]
- 00bdc6d4 ["CALL", null, ["callee:00c5ee00:8"]]
+ 00bdd6c8 ["INT_ADD", "register:40f0:8", ["const:bdd6c8:8", "const:4:8"]]
+ 00bdd6c8 ["CALL", null, ["callee:00c5ee00:8"]]
- 00bdc6d4 bytes d7050294
+ 00bdd6c8 bytes ce050294
- 00bdc6e0 ["INT_ADD", "register:40f0:8", ["const:bdc6e0:8", "const:4:8"]]
- 00bdc6e0 ["CALL", null, ["callee:00c5bae0:8"]]
+ 00bdd6d4 ["INT_ADD", "register:40f0:8", ["const:bdd6d4:8", "const:4:8"]]
+ 00bdd6d4 ["CALL", null, ["callee:00c5bae0:8"]]
- 00bdc6e0 bytes 0cf90194
+ 00bdd6d4 bytes 03f90194
~~~


<a id="compare-aa11fa57cf2a042ba5d6cbf34e03f221"></a>

### [`00bdc768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc768.md) → [`00bdd75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd75c.md) _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5def0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5def0.md) · 呼出先 3件 [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md) [`00c5df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df40.md)
- 新版 呼出元 1件 [`00c5eec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eec0.md) · 呼出先 3件 [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md) [`00c5ee00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee00.md) [`00c5ef10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc768.md#insn-00bdc788) · [`00bdc798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc768.md#insn-00bdc798) · [`00bdc7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc768.md#insn-00bdc7e0)
- 新版 [`00bdd77c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd75c.md#insn-00bdd77c) · [`00bdd78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd75c.md#insn-00bdd78c) · [`00bdd7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd75c.md#insn-00bdd7d4)

~~~diff
- 00bdc788 ["INT_ADD", "register:40f0:8", ["const:bdc788:8", "const:4:8"]]
- 00bdc788 ["CALL", null, ["callee:00c5c650:8"]]
+ 00bdd77c ["INT_ADD", "register:40f0:8", ["const:bdd77c:8", "const:4:8"]]
+ 00bdd77c ["CALL", null, ["callee:00c5c650:8"]]
- 00bdc788 bytes befb0194
+ 00bdd77c bytes b5fb0194
- 00bdc798 ["INT_ADD", "register:40f0:8", ["const:bdc798:8", "const:4:8"]]
- 00bdc798 ["CALL", null, ["callee:00c5c650:8"]]
+ 00bdd78c ["INT_ADD", "register:40f0:8", ["const:bdd78c:8", "const:4:8"]]
+ 00bdd78c ["CALL", null, ["callee:00c5c650:8"]]
- 00bdc798 bytes bafb0194
+ 00bdd78c bytes b1fb0194
- 00bdc7e0 ["INT_ADD", "register:40f0:8", ["const:bdc7e0:8", "const:4:8"]]
- 00bdc7e0 ["CALL", null, ["callee:00c5ef10:8"]]
+ 00bdd7d4 ["INT_ADD", "register:40f0:8", ["const:bdd7d4:8", "const:4:8"]]
+ 00bdd7d4 ["CALL", null, ["callee:00c5ef10:8"]]
- 00bdc7e0 bytes d8050294
+ 00bdd7d4 bytes cf050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35556dddcf11f3179c02b60c18819f8f"></a>

### [`00bdc8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md) → [`00bdd8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd8cc.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emp

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df40.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5df30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df30.md)
- 新版 呼出元 1件 [`00c5ef10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef10.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b990.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md) [`00c5ef00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdc910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md#insn-00bdc910) · [`00bdc924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md#insn-00bdc924) · [`00bdc93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md#insn-00bdc93c)
- 新版 [`00bdd904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd8cc.md#insn-00bdd904) · [`00bdd918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd8cc.md#insn-00bdd918) · [`00bdd930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd8cc.md#insn-00bdd930)

~~~diff
- 00bdc910 ["INT_ADD", "register:40f0:8", ["const:bdc910:8", "const:4:8"]]
- 00bdc910 ["CALL", null, ["callee:00c5ef00:8"]]
+ 00bdd904 ["INT_ADD", "register:40f0:8", ["const:bdd904:8", "const:4:8"]]
+ 00bdd904 ["CALL", null, ["callee:00c5ef00:8"]]
- 00bdc910 bytes 88050294
+ 00bdd904 bytes 7f050294
- 00bdc924 ["INT_ADD", "register:40f0:8", ["const:bdc924:8", "const:4:8"]]
- 00bdc924 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bdd918 ["INT_ADD", "register:40f0:8", ["const:bdd918:8", "const:4:8"]]
+ 00bdd918 ["CALL", null, ["callee:00c58f30:8"]]
- 00bdc924 bytes 8fed0194
+ 00bdd918 bytes 86ed0194
- 00bdc93c ["INT_ADD", "register:40f0:8", ["const:bdc93c:8", "const:4:8"]]
- 00bdc93c ["CALL", null, ["callee:00c5b990:8"]]
+ 00bdd930 ["INT_ADD", "register:40f0:8", ["const:bdd930:8", "const:4:8"]]
+ 00bdd930 ["CALL", null, ["callee:00c5b990:8"]]
- 00bdc93c bytes 21f80194
+ 00bdd930 bytes 18f80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dfa2d220b1bfb14bdc6c4ad06230f2c"></a>

### [`00bdc9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc9ec.md) → [`00bdd9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd9e0.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__fin

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df30.md) · 呼出先 1件 [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md)
- 新版 呼出元 1件 [`00c5ef00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef00.md) · 呼出先 1件 [`00c5c640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdca30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc9ec.md#insn-00bdca30) · [`00bdca68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc9ec.md#insn-00bdca68) · [`00bdcaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc9ec.md#insn-00bdcaac)
- 新版 [`00bdda24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd9e0.md#insn-00bdda24) · [`00bdda5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd9e0.md#insn-00bdda5c) · [`00bddaa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd9e0.md#insn-00bddaa0)

~~~diff
- 00bdca30 ["INT_ADD", "register:40f0:8", ["const:bdca30:8", "const:4:8"]]
- 00bdca30 ["CALL", null, ["callee:00c5c640:8"]]
+ 00bdda24 ["INT_ADD", "register:40f0:8", ["const:bdda24:8", "const:4:8"]]
+ 00bdda24 ["CALL", null, ["callee:00c5c640:8"]]
- 00bdca30 bytes 10fb0194
+ 00bdda24 bytes 07fb0194
- 00bdca68 ["INT_ADD", "register:40f0:8", ["const:bdca68:8", "const:4:8"]]
- 00bdca68 ["CALL", null, ["callee:00c5c640:8"]]
+ 00bdda5c ["INT_ADD", "register:40f0:8", ["const:bdda5c:8", "const:4:8"]]
+ 00bdda5c ["CALL", null, ["callee:00c5c640:8"]]
- 00bdca68 bytes 02fb0194
+ 00bdda5c bytes f9fa0194
- 00bdcaac ["INT_ADD", "register:40f0:8", ["const:bdcaac:8", "const:4:8"]]
- 00bdcaac ["CALL", null, ["callee:00c5c640:8"]]
+ 00bddaa0 ["INT_ADD", "register:40f0:8", ["const:bddaa0:8", "const:4:8"]]
+ 00bddaa0 ["CALL", null, ["callee:00c5c640:8"]]
- 00bdcaac bytes f1fa0194
+ 00bddaa0 bytes e8fa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd584640bd208e1bef1166de9f36055"></a>

### [`00bdcc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md) → [`00bddc0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddc0c.md) _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bdb930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb930.md) [`00bdbf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbf14.md) [`00bdc1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5ddf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddf0.md)
- 新版 呼出元 3件 [`00bdc924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc924.md) [`00bdcf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdcf08.md) [`00bdd1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd1e0.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5edc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5edc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdcc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md#insn-00bdcc50) · [`00bdcc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md#insn-00bdcc70) · [`00bdcc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md#insn-00bdcc98)
- 新版 [`00bddc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddc0c.md#insn-00bddc44) · [`00bddc64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddc0c.md#insn-00bddc64) · [`00bddc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddc0c.md#insn-00bddc8c)

~~~diff
- 00bdcc50 ["INT_ADD", "register:40f0:8", ["const:bdcc50:8", "const:4:8"]]
- 00bdcc50 ["CALL", null, ["callee:00c5edc0:8"]]
+ 00bddc44 ["INT_ADD", "register:40f0:8", ["const:bddc44:8", "const:4:8"]]
+ 00bddc44 ["CALL", null, ["callee:00c5edc0:8"]]
- 00bdcc50 bytes 68040294
+ 00bddc44 bytes 5f040294
- 00bdcc70 ["INT_ADD", "register:40f0:8", ["const:bdcc70:8", "const:4:8"]]
- 00bdcc70 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bddc64 ["INT_ADD", "register:40f0:8", ["const:bddc64:8", "const:4:8"]]
+ 00bddc64 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bdcc70 bytes 98f80194
+ 00bddc64 bytes 8ff80194
- 00bdcc98 ["INT_ADD", "register:40f0:8", ["const:bdcc98:8", "const:4:8"]]
- 00bdcc98 ["CALL", null, ["callee:00c5ee60:8"]]
+ 00bddc8c ["INT_ADD", "register:40f0:8", ["const:bddc8c:8", "const:4:8"]]
+ 00bddc8c ["CALL", null, ["callee:00c5ee60:8"]]
- 00bdcc98 bytes 7e040294
+ 00bddc8c bytes 75040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6f591dd40105257deca8b65aa45f8f"></a>

### [`00bdce5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdce5c.md) → [`00bdde50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdde50.md) _ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdce80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdce5c.md#insn-00bdce80)
- 新版 [`00bdde74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdde50.md#insn-00bdde74)

~~~diff
- 00bdce80 ["INT_ADD", "register:40f0:8", ["const:bdce80:8", "const:4:8"]]
- 00bdce80 ["CALL", null, ["callee:00c5eed0:8"]]
+ 00bdde74 ["INT_ADD", "register:40f0:8", ["const:bdde74:8", "const:4:8"]]
+ 00bdde74 ["CALL", null, ["callee:00c5eed0:8"]]
- 00bdce80 bytes 20040294
+ 00bdde74 bytes 17040294
~~~


<a id="compare-e0067e48176610c1484b38b86d833714"></a>

### [`00bdeb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdeb14.md) → [`00bdfb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfb08.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEbP7_JNIEnvPNS_26Refere

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df80.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dde0.md)
- 新版 呼出元 1件 [`00c5ef50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef50.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5edb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5edb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bdeb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdeb14.md#insn-00bdeb48) · [`00bdeb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdeb14.md#insn-00bdeb5c) · [`00bdeb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdeb14.md#insn-00bdeb88)
- 新版 [`00bdfb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfb08.md#insn-00bdfb3c) · [`00bdfb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfb08.md#insn-00bdfb50) · [`00bdfb7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfb08.md#insn-00bdfb7c)

~~~diff
- 00bdeb48 ["INT_ADD", "register:40f0:8", ["const:bdeb48:8", "const:4:8"]]
- 00bdeb48 ["CALL", null, ["callee:00c5edb0:8"]]
+ 00bdfb3c ["INT_ADD", "register:40f0:8", ["const:bdfb3c:8", "const:4:8"]]
+ 00bdfb3c ["CALL", null, ["callee:00c5edb0:8"]]
- 00bdeb48 bytes a6fc0194
+ 00bdfb3c bytes 9dfc0194
- 00bdeb5c ["INT_ADD", "register:40f0:8", ["const:bdeb5c:8", "const:4:8"]]
- 00bdeb5c ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bdfb50 ["INT_ADD", "register:40f0:8", ["const:bdfb50:8", "const:4:8"]]
+ 00bdfb50 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bdeb5c bytes ddf00194
+ 00bdfb50 bytes d4f00194
- 00bdeb88 ["INT_ADD", "register:40f0:8", ["const:bdeb88:8", "const:4:8"]]
- 00bdeb88 ["CALL", null, ["callee:00c5ef30:8"]]
+ 00bdfb7c ["INT_ADD", "register:40f0:8", ["const:bdfb7c:8", "const:4:8"]]
+ 00bdfb7c ["CALL", null, ["callee:00c5ef30:8"]]
- 00bdeb88 bytes f6fc0194
+ 00bdfb7c bytes edfc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42c3800e4601220ae371337adc1b81f1"></a>

### [`00be1450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1450.md) → [`00be2444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2444.md) _ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureR

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde8b4.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5ddf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddf0.md)
- 新版 呼出元 1件 [`00bdf8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf8a8.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md) [`00c5edc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5edc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1450.md#insn-00be1488) · [`00be14a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1450.md#insn-00be14a0) · [`00be14c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1450.md#insn-00be14c8)
- 新版 [`00be247c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2444.md#insn-00be247c) · [`00be2494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2444.md#insn-00be2494) · [`00be24bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2444.md#insn-00be24bc)

~~~diff
- 00be1488 ["INT_ADD", "register:40f0:8", ["const:be1488:8", "const:4:8"]]
- 00be1488 ["CALL", null, ["callee:00c5edc0:8"]]
+ 00be247c ["INT_ADD", "register:40f0:8", ["const:be247c:8", "const:4:8"]]
+ 00be247c ["CALL", null, ["callee:00c5edc0:8"]]
- 00be1488 bytes 5af20194
+ 00be247c bytes 51f20194
- 00be14a0 ["INT_ADD", "register:40f0:8", ["const:be14a0:8", "const:4:8"]]
- 00be14a0 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00be2494 ["INT_ADD", "register:40f0:8", ["const:be2494:8", "const:4:8"]]
+ 00be2494 ["CALL", null, ["callee:00c5bea0:8"]]
- 00be14a0 bytes 8ce60194
+ 00be2494 bytes 83e60194
- 00be14c8 ["INT_ADD", "register:40f0:8", ["const:be14c8:8", "const:4:8"]]
- 00be14c8 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00be24bc ["INT_ADD", "register:40f0:8", ["const:be24bc:8", "const:4:8"]]
+ 00be24bc ["CALL", null, ["callee:00c5ef20:8"]]
- 00be14c8 bytes a2f20194
+ 00be24bc bytes 99f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cde347c17d95ab964e7f34870f6c28fe"></a>

### [`00be17c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be17c4.md) → [`00be27b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be27b8.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df90.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md) [`00c5df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df70.md)
- 新版 呼出元 1件 [`00c5ef60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef60.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md) [`00c5ef40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be17c4.md#insn-00be1860) · [`00be1878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be17c4.md#insn-00be1878) · [`00be1898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be17c4.md#insn-00be1898)
- 新版 [`00be2854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be27b8.md#insn-00be2854) · [`00be286c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be27b8.md#insn-00be286c) · [`00be288c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be27b8.md#insn-00be288c)

~~~diff
- 00be1860 ["INT_ADD", "register:40f0:8", ["const:be1860:8", "const:4:8"]]
- 00be1860 ["CALL", null, ["callee:00c58f30:8"]]
+ 00be2854 ["INT_ADD", "register:40f0:8", ["const:be2854:8", "const:4:8"]]
+ 00be2854 ["CALL", null, ["callee:00c58f30:8"]]
- 00be1860 bytes c0d90194
+ 00be2854 bytes b7d90194
- 00be1878 ["INT_ADD", "register:40f0:8", ["const:be1878:8", "const:4:8"]]
- 00be1878 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00be286c ["INT_ADD", "register:40f0:8", ["const:be286c:8", "const:4:8"]]
+ 00be286c ["CALL", null, ["callee:00c5ef40:8"]]
- 00be1878 bytes bef10194
+ 00be286c bytes b5f10194
- 00be1898 ["INT_ADD", "register:40f0:8", ["const:be1898:8", "const:4:8"]]
- 00be1898 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00be288c ["INT_ADD", "register:40f0:8", ["const:be288c:8", "const:4:8"]]
+ 00be288c ["CALL", null, ["callee:00c5ef40:8"]]
- 00be1898 bytes b6f10194
+ 00be288c bytes adf10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe1427b04caa18c4fed021fdaa9828c6"></a>

### [`00be1974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1974.md) → [`00be2968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2968.md) _ZNK8firebase4auth4User18GetTokenLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1974.md#insn-00be1994) · [`00be19a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1974.md#insn-00be19a0) · [`00be19ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1974.md#insn-00be19ac)
- 新版 [`00be2988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2968.md#insn-00be2988) · [`00be2994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2968.md#insn-00be2994) · [`00be29a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2968.md#insn-00be29a0)

~~~diff
- 00be1994 ["INT_ADD", "register:40f0:8", ["const:be1994:8", "const:4:8"]]
- 00be1994 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2988 ["INT_ADD", "register:40f0:8", ["const:be2988:8", "const:4:8"]]
+ 00be2988 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1994 bytes 4fe40194
+ 00be2988 bytes 46e40194
- 00be19a0 ["INT_ADD", "register:40f0:8", ["const:be19a0:8", "const:4:8"]]
- 00be19a0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2994 ["INT_ADD", "register:40f0:8", ["const:be2994:8", "const:4:8"]]
+ 00be2994 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be19a0 bytes 50e40194
+ 00be2994 bytes 47e40194
- 00be19ac ["INT_ADD", "register:40f0:8", ["const:be19ac:8", "const:4:8"]]
- 00be19ac ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be29a0 ["INT_ADD", "register:40f0:8", ["const:be29a0:8", "const:4:8"]]
+ 00be29a0 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be19ac bytes e5e40194
+ 00be29a0 bytes dce40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cbf81329d57be976d9ff714bbbb2e6c"></a>

### [`00be1a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a04.md) → [`00be29f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be29f8.md) _ZNK8firebase4auth4User24UpdatePasswordLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a04.md#insn-00be1a24) · [`00be1a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a04.md#insn-00be1a30) · [`00be1a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a04.md#insn-00be1a3c)
- 新版 [`00be2a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be29f8.md#insn-00be2a18) · [`00be2a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be29f8.md#insn-00be2a24) · [`00be2a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be29f8.md#insn-00be2a30)

~~~diff
- 00be1a24 ["INT_ADD", "register:40f0:8", ["const:be1a24:8", "const:4:8"]]
- 00be1a24 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2a18 ["INT_ADD", "register:40f0:8", ["const:be2a18:8", "const:4:8"]]
+ 00be2a18 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1a24 bytes 2be40194
+ 00be2a18 bytes 22e40194
- 00be1a30 ["INT_ADD", "register:40f0:8", ["const:be1a30:8", "const:4:8"]]
- 00be1a30 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2a24 ["INT_ADD", "register:40f0:8", ["const:be2a24:8", "const:4:8"]]
+ 00be2a24 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1a30 bytes 2ce40194
+ 00be2a24 bytes 23e40194
- 00be1a3c ["INT_ADD", "register:40f0:8", ["const:be1a3c:8", "const:4:8"]]
- 00be1a3c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2a30 ["INT_ADD", "register:40f0:8", ["const:be2a30:8", "const:4:8"]]
+ 00be2a30 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1a3c bytes c1e40194
+ 00be2a30 bytes b8e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77f227200de596e61ccd2cbd6d15e44e"></a>

### [`00be1a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a94.md) → [`00be2a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2a88.md) _ZNK8firebase4auth4User28LinkWithCredentialLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a94.md#insn-00be1ab4) · [`00be1ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a94.md#insn-00be1ac0) · [`00be1acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1a94.md#insn-00be1acc)
- 新版 [`00be2aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2a88.md#insn-00be2aa8) · [`00be2ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2a88.md#insn-00be2ab4) · [`00be2ac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2a88.md#insn-00be2ac0)

~~~diff
- 00be1ab4 ["INT_ADD", "register:40f0:8", ["const:be1ab4:8", "const:4:8"]]
- 00be1ab4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2aa8 ["INT_ADD", "register:40f0:8", ["const:be2aa8:8", "const:4:8"]]
+ 00be2aa8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1ab4 bytes 07e40194
+ 00be2aa8 bytes fee30194
- 00be1ac0 ["INT_ADD", "register:40f0:8", ["const:be1ac0:8", "const:4:8"]]
- 00be1ac0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2ab4 ["INT_ADD", "register:40f0:8", ["const:be2ab4:8", "const:4:8"]]
+ 00be2ab4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1ac0 bytes 08e40194
+ 00be2ab4 bytes ffe30194
- 00be1acc ["INT_ADD", "register:40f0:8", ["const:be1acc:8", "const:4:8"]]
- 00be1acc ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2ac0 ["INT_ADD", "register:40f0:8", ["const:be2ac0:8", "const:4:8"]]
+ 00be2ac0 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1acc bytes 9de40194
+ 00be2ac0 bytes 94e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442ce0cc2fb1453f9d8ee3b63fa928f7"></a>

### [`00be1b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1b24.md) → [`00be2b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2b18.md) _ZNK8firebase4auth4User24ReauthenticateLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1b24.md#insn-00be1b44) · [`00be1b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1b24.md#insn-00be1b50) · [`00be1b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1b24.md#insn-00be1b5c)
- 新版 [`00be2b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2b18.md#insn-00be2b38) · [`00be2b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2b18.md#insn-00be2b44) · [`00be2b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2b18.md#insn-00be2b50)

~~~diff
- 00be1b44 ["INT_ADD", "register:40f0:8", ["const:be1b44:8", "const:4:8"]]
- 00be1b44 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2b38 ["INT_ADD", "register:40f0:8", ["const:be2b38:8", "const:4:8"]]
+ 00be2b38 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1b44 bytes e3e30194
+ 00be2b38 bytes dae30194
- 00be1b50 ["INT_ADD", "register:40f0:8", ["const:be1b50:8", "const:4:8"]]
- 00be1b50 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2b44 ["INT_ADD", "register:40f0:8", ["const:be2b44:8", "const:4:8"]]
+ 00be2b44 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1b50 bytes e4e30194
+ 00be2b44 bytes dbe30194
- 00be1b5c ["INT_ADD", "register:40f0:8", ["const:be1b5c:8", "const:4:8"]]
- 00be1b5c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2b50 ["INT_ADD", "register:40f0:8", ["const:be2b50:8", "const:4:8"]]
+ 00be2b50 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1b5c bytes 79e40194
+ 00be2b50 bytes 70e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca37f6bd0e3d2313b09651a12b4d990"></a>

### [`00be1bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1bb4.md) → [`00be2ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2ba8.md) _ZNK8firebase4auth4User39ReauthenticateAndRetrieveDataLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1bb4.md#insn-00be1bd4) · [`00be1be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1bb4.md#insn-00be1be0) · [`00be1bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1bb4.md#insn-00be1bec)
- 新版 [`00be2bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2ba8.md#insn-00be2bc8) · [`00be2bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2ba8.md#insn-00be2bd4) · [`00be2be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2ba8.md#insn-00be2be0)

~~~diff
- 00be1bd4 ["INT_ADD", "register:40f0:8", ["const:be1bd4:8", "const:4:8"]]
- 00be1bd4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2bc8 ["INT_ADD", "register:40f0:8", ["const:be2bc8:8", "const:4:8"]]
+ 00be2bc8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1bd4 bytes bfe30194
+ 00be2bc8 bytes b6e30194
- 00be1be0 ["INT_ADD", "register:40f0:8", ["const:be1be0:8", "const:4:8"]]
- 00be1be0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2bd4 ["INT_ADD", "register:40f0:8", ["const:be2bd4:8", "const:4:8"]]
+ 00be2bd4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1be0 bytes c0e30194
+ 00be2bd4 bytes b7e30194
- 00be1bec ["INT_ADD", "register:40f0:8", ["const:be1bec:8", "const:4:8"]]
- 00be1bec ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2be0 ["INT_ADD", "register:40f0:8", ["const:be2be0:8", "const:4:8"]]
+ 00be2be0 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1bec bytes 55e40194
+ 00be2be0 bytes 4ce40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d816dc2b1cfe92cef064a563f36ee4b"></a>

### [`00be1c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1c44.md) → [`00be2c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2c38.md) _ZNK8firebase4auth4User31SendEmailVerificationLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1c44.md#insn-00be1c64) · [`00be1c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1c44.md#insn-00be1c70) · [`00be1c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1c44.md#insn-00be1c7c)
- 新版 [`00be2c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2c38.md#insn-00be2c58) · [`00be2c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2c38.md#insn-00be2c64) · [`00be2c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2c38.md#insn-00be2c70)

~~~diff
- 00be1c64 ["INT_ADD", "register:40f0:8", ["const:be1c64:8", "const:4:8"]]
- 00be1c64 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2c58 ["INT_ADD", "register:40f0:8", ["const:be2c58:8", "const:4:8"]]
+ 00be2c58 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1c64 bytes 9be30194
+ 00be2c58 bytes 92e30194
- 00be1c70 ["INT_ADD", "register:40f0:8", ["const:be1c70:8", "const:4:8"]]
- 00be1c70 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2c64 ["INT_ADD", "register:40f0:8", ["const:be2c64:8", "const:4:8"]]
+ 00be2c64 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1c70 bytes 9ce30194
+ 00be2c64 bytes 93e30194
- 00be1c7c ["INT_ADD", "register:40f0:8", ["const:be1c7c:8", "const:4:8"]]
- 00be1c7c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2c70 ["INT_ADD", "register:40f0:8", ["const:be2c70:8", "const:4:8"]]
+ 00be2c70 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1c7c bytes 31e40194
+ 00be2c70 bytes 28e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbffecd14823dce18d269f5070be7c2c"></a>

### [`00be1cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1cd4.md) → [`00be2cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2cc8.md) _ZNK8firebase4auth4User50SendEmailVerificationBeforeUpdatingEmailLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1cd4.md#insn-00be1cf4) · [`00be1d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1cd4.md#insn-00be1d00) · [`00be1d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1cd4.md#insn-00be1d0c)
- 新版 [`00be2ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2cc8.md#insn-00be2ce8) · [`00be2cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2cc8.md#insn-00be2cf4) · [`00be2d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2cc8.md#insn-00be2d00)

~~~diff
- 00be1cf4 ["INT_ADD", "register:40f0:8", ["const:be1cf4:8", "const:4:8"]]
- 00be1cf4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2ce8 ["INT_ADD", "register:40f0:8", ["const:be2ce8:8", "const:4:8"]]
+ 00be2ce8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1cf4 bytes 77e30194
+ 00be2ce8 bytes 6ee30194
- 00be1d00 ["INT_ADD", "register:40f0:8", ["const:be1d00:8", "const:4:8"]]
- 00be1d00 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2cf4 ["INT_ADD", "register:40f0:8", ["const:be2cf4:8", "const:4:8"]]
+ 00be2cf4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1d00 bytes 78e30194
+ 00be2cf4 bytes 6fe30194
- 00be1d0c ["INT_ADD", "register:40f0:8", ["const:be1d0c:8", "const:4:8"]]
- 00be1d0c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2d00 ["INT_ADD", "register:40f0:8", ["const:be2d00:8", "const:4:8"]]
+ 00be2d00 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1d0c bytes 0de40194
+ 00be2d00 bytes 04e40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d94217905dba68d41554931dade4719"></a>

### [`00be1d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1d64.md) → [`00be2d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2d58.md) _ZNK8firebase4auth4User16UnlinkLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1d64.md#insn-00be1d84) · [`00be1d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1d64.md#insn-00be1d90) · [`00be1d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1d64.md#insn-00be1d9c)
- 新版 [`00be2d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2d58.md#insn-00be2d78) · [`00be2d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2d58.md#insn-00be2d84) · [`00be2d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2d58.md#insn-00be2d90)

~~~diff
- 00be1d84 ["INT_ADD", "register:40f0:8", ["const:be1d84:8", "const:4:8"]]
- 00be1d84 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2d78 ["INT_ADD", "register:40f0:8", ["const:be2d78:8", "const:4:8"]]
+ 00be2d78 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1d84 bytes 53e30194
+ 00be2d78 bytes 4ae30194
- 00be1d90 ["INT_ADD", "register:40f0:8", ["const:be1d90:8", "const:4:8"]]
- 00be1d90 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2d84 ["INT_ADD", "register:40f0:8", ["const:be2d84:8", "const:4:8"]]
+ 00be2d84 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1d90 bytes 54e30194
+ 00be2d84 bytes 4be30194
- 00be1d9c ["INT_ADD", "register:40f0:8", ["const:be1d9c:8", "const:4:8"]]
- 00be1d9c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2d90 ["INT_ADD", "register:40f0:8", ["const:be2d90:8", "const:4:8"]]
+ 00be2d90 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1d9c bytes e9e30194
+ 00be2d90 bytes e0e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7612337417358fa69c04e92b201827cd"></a>

### [`00be1df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1df4.md) → [`00be2de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2de8.md) _ZNK8firebase4auth4User27UpdateUserProfileLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1df4.md#insn-00be1e14) · [`00be1e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1df4.md#insn-00be1e20) · [`00be1e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1df4.md#insn-00be1e2c)
- 新版 [`00be2e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2de8.md#insn-00be2e08) · [`00be2e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2de8.md#insn-00be2e14) · [`00be2e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2de8.md#insn-00be2e20)

~~~diff
- 00be1e14 ["INT_ADD", "register:40f0:8", ["const:be1e14:8", "const:4:8"]]
- 00be1e14 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2e08 ["INT_ADD", "register:40f0:8", ["const:be2e08:8", "const:4:8"]]
+ 00be2e08 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1e14 bytes 2fe30194
+ 00be2e08 bytes 26e30194
- 00be1e20 ["INT_ADD", "register:40f0:8", ["const:be1e20:8", "const:4:8"]]
- 00be1e20 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2e14 ["INT_ADD", "register:40f0:8", ["const:be2e14:8", "const:4:8"]]
+ 00be2e14 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1e20 bytes 30e30194
+ 00be2e14 bytes 27e30194
- 00be1e2c ["INT_ADD", "register:40f0:8", ["const:be1e2c:8", "const:4:8"]]
- 00be1e2c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2e20 ["INT_ADD", "register:40f0:8", ["const:be2e20:8", "const:4:8"]]
+ 00be2e20 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1e2c bytes c5e30194
+ 00be2e20 bytes bce30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce6c9fc4429d52bd00b5e933a11269e7"></a>

### [`00be1e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1e84.md) → [`00be2e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2e78.md) _ZNK8firebase4auth4User16ReloadLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1e84.md#insn-00be1ea4) · [`00be1eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1e84.md#insn-00be1eb0) · [`00be1ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1e84.md#insn-00be1ebc)
- 新版 [`00be2e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2e78.md#insn-00be2e98) · [`00be2ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2e78.md#insn-00be2ea4) · [`00be2eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2e78.md#insn-00be2eb0)

~~~diff
- 00be1ea4 ["INT_ADD", "register:40f0:8", ["const:be1ea4:8", "const:4:8"]]
- 00be1ea4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2e98 ["INT_ADD", "register:40f0:8", ["const:be2e98:8", "const:4:8"]]
+ 00be2e98 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1ea4 bytes 0be30194
+ 00be2e98 bytes 02e30194
- 00be1eb0 ["INT_ADD", "register:40f0:8", ["const:be1eb0:8", "const:4:8"]]
- 00be1eb0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2ea4 ["INT_ADD", "register:40f0:8", ["const:be2ea4:8", "const:4:8"]]
+ 00be2ea4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1eb0 bytes 0ce30194
+ 00be2ea4 bytes 03e30194
- 00be1ebc ["INT_ADD", "register:40f0:8", ["const:be1ebc:8", "const:4:8"]]
- 00be1ebc ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2eb0 ["INT_ADD", "register:40f0:8", ["const:be2eb0:8", "const:4:8"]]
+ 00be2eb0 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1ebc bytes a1e30194
+ 00be2eb0 bytes 98e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-656d0fa4eacd1b0582e6fec708fdca85"></a>

### [`00be1f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1f14.md) → [`00be2f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f08.md) _ZNK8firebase4auth4User16DeleteLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1f14.md#insn-00be1f34) · [`00be1f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1f14.md#insn-00be1f40) · [`00be1f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1f14.md#insn-00be1f4c)
- 新版 [`00be2f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f08.md#insn-00be2f28) · [`00be2f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f08.md#insn-00be2f34) · [`00be2f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f08.md#insn-00be2f40)

~~~diff
- 00be1f34 ["INT_ADD", "register:40f0:8", ["const:be1f34:8", "const:4:8"]]
- 00be1f34 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2f28 ["INT_ADD", "register:40f0:8", ["const:be2f28:8", "const:4:8"]]
+ 00be2f28 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1f34 bytes e7e20194
+ 00be2f28 bytes dee20194
- 00be1f40 ["INT_ADD", "register:40f0:8", ["const:be1f40:8", "const:4:8"]]
- 00be1f40 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2f34 ["INT_ADD", "register:40f0:8", ["const:be2f34:8", "const:4:8"]]
+ 00be2f34 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1f40 bytes e8e20194
+ 00be2f34 bytes dfe20194
- 00be1f4c ["INT_ADD", "register:40f0:8", ["const:be1f4c:8", "const:4:8"]]
- 00be1f4c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2f40 ["INT_ADD", "register:40f0:8", ["const:be2f40:8", "const:4:8"]]
+ 00be2f40 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1f4c bytes 7de30194
+ 00be2f40 bytes 74e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26bdade61fe78ed36089ac17384ac832"></a>

### [`00be1fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1fa4.md) → [`00be2f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f98.md) _ZNK8firebase4auth4User37UpdatePhoneNumberCredentialLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1fa4.md#insn-00be1fc4) · [`00be1fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1fa4.md#insn-00be1fd0) · [`00be1fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1fa4.md#insn-00be1fdc)
- 新版 [`00be2fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f98.md#insn-00be2fb8) · [`00be2fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f98.md#insn-00be2fc4) · [`00be2fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2f98.md#insn-00be2fd0)

~~~diff
- 00be1fc4 ["INT_ADD", "register:40f0:8", ["const:be1fc4:8", "const:4:8"]]
- 00be1fc4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2fb8 ["INT_ADD", "register:40f0:8", ["const:be2fb8:8", "const:4:8"]]
+ 00be2fb8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1fc4 bytes c3e20194
+ 00be2fb8 bytes bae20194
- 00be1fd0 ["INT_ADD", "register:40f0:8", ["const:be1fd0:8", "const:4:8"]]
- 00be1fd0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00be2fc4 ["INT_ADD", "register:40f0:8", ["const:be2fc4:8", "const:4:8"]]
+ 00be2fc4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00be1fd0 bytes c4e20194
+ 00be2fc4 bytes bbe20194
- 00be1fdc ["INT_ADD", "register:40f0:8", ["const:be1fdc:8", "const:4:8"]]
- 00be1fdc ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be2fd0 ["INT_ADD", "register:40f0:8", ["const:be2fd0:8", "const:4:8"]]
+ 00be2fd0 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be1fdc bytes 59e30194
+ 00be2fd0 bytes 50e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

