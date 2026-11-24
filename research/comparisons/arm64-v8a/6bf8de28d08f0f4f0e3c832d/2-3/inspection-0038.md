# v16.0.2 → v16.0.3 · 要調査の変更候補 (38)

[一覧の目次](README.md)

<a id="compare-72a09f9e4a48604d7e71c8b4cc1161fa"></a>

### [`00bf4bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4bbc.md) → [`00bf5bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5bb0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c5f0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4bbc.md#insn-00bf4c08)
- 新版 [`00bf5bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5bb0.md#insn-00bf5bfc)

~~~diff
- 00bf4c08 ["INT_ADD", "register:40f0:8", ["const:bf4c08:8", "const:4:8"]]
- 00bf4c08 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf5bfc ["INT_ADD", "register:40f0:8", ["const:bf5bfc:8", "const:4:8"]]
+ 00bf5bfc ["CALL", null, ["callee:00bf3968:8"]]
- 00bf4c08 bytes 5bf7ff97
+ 00bf5bfc bytes 5bf7ff97
~~~


<a id="compare-07bbd1cd9b83ae9f7c7887807de49bf0"></a>

### [`00bf6764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6764.md) → [`00bf7758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf7758.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00bf82f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf82f4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c59830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59830.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00bf92e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf92e8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6764.md#insn-00bf678c) · [`00bf67d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6764.md#insn-00bf67d0) · [`00bf67fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6764.md#insn-00bf67fc)
- 新版 [`00bf7780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf7758.md#insn-00bf7780) · [`00bf77c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf7758.md#insn-00bf77c4) · [`00bf77f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf7758.md#insn-00bf77f0)

~~~diff
- 00bf678c ["INT_ADD", "register:40f0:8", ["const:bf678c:8", "const:4:8"]]
- 00bf678c ["CALL", null, ["callee:00bf92e8:8"]]
+ 00bf7780 ["INT_ADD", "register:40f0:8", ["const:bf7780:8", "const:4:8"]]
+ 00bf7780 ["CALL", null, ["callee:00bf92e8:8"]]
- 00bf678c bytes da060094
+ 00bf7780 bytes da060094
- 00bf67d0 ["INT_ADD", "register:40f0:8", ["const:bf67d0:8", "const:4:8"]]
- 00bf67d0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf77c4 ["INT_ADD", "register:40f0:8", ["const:bf77c4:8", "const:4:8"]]
+ 00bf77c4 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf67d0 bytes e4850194
+ 00bf77c4 bytes db850194
- 00bf67fc ["INT_ADD", "register:40f0:8", ["const:bf67fc:8", "const:4:8"]]
- 00bf67fc ["CALL", null, ["callee:00c590a0:8"]]
+ 00bf77f0 ["INT_ADD", "register:40f0:8", ["const:bf77f0:8", "const:4:8"]]
+ 00bf77f0 ["CALL", null, ["callee:00c590a0:8"]]
- 00bf67fc bytes 35860194
+ 00bf77f0 bytes 2c860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a931de955192f680bfa2cc75231349f9"></a>

### [`00bf90d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf90d8.md) → [`00bfa0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa0cc.md) _ZNSt6__ndk112system_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf90ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf90d8.md#insn-00bf90ec)
- 新版 [`00bfa0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa0cc.md#insn-00bfa0e0)

~~~diff
- 00bf90ec ["INT_ADD", "register:40f0:8", ["const:bf90ec:8", "const:4:8"]]
- 00bf90ec ["CALL", null, ["callee:00c5f220:8"]]
+ 00bfa0e0 ["INT_ADD", "register:40f0:8", ["const:bfa0e0:8", "const:4:8"]]
+ 00bfa0e0 ["CALL", null, ["callee:00c5f220:8"]]
- 00bf90ec bytes 59940194
+ 00bfa0e0 bytes 50940194
~~~


<a id="compare-2bd359d6b836cf454d043113d30bd4c3"></a>

### [`00bf918c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf918c.md) → [`00bfa180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa180.md) FUN_00bfa180

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf91a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf918c.md#insn-00bf91a0)
- 新版 [`00bfa194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa180.md#insn-00bfa194)

~~~diff
- 00bf91a0 ["INT_ADD", "register:40f0:8", ["const:bf91a0:8", "const:4:8"]]
- 00bf91a0 ["CALL", null, ["callee:00c5ef90:8"]]
+ 00bfa194 ["INT_ADD", "register:40f0:8", ["const:bfa194:8", "const:4:8"]]
+ 00bfa194 ["CALL", null, ["callee:00c5ef90:8"]]
- 00bf91a0 bytes 88930194
+ 00bfa194 bytes 7f930194
~~~


<a id="compare-8d126f2d044026da73adfc0af7083348"></a>

### [`00bf91b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf91b8.md) → [`00bfa1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa1ac.md) FUN_00bfa1ac

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf91cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf91b8.md#insn-00bf91cc)
- 新版 [`00bfa1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa1ac.md#insn-00bfa1c0)

~~~diff
- 00bf91cc ["INT_ADD", "register:40f0:8", ["const:bf91cc:8", "const:4:8"]]
- 00bf91cc ["CALL", null, ["callee:00c5ef90:8"]]
+ 00bfa1c0 ["INT_ADD", "register:40f0:8", ["const:bfa1c0:8", "const:4:8"]]
+ 00bfa1c0 ["CALL", null, ["callee:00c5ef90:8"]]
- 00bf91cc bytes 7d930194
+ 00bfa1c0 bytes 74930194
~~~


<a id="compare-0aca42ecf7eba8cd03af6ae7c682ecdb"></a>

### [`00bf9220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9220.md) → [`00bfa214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa214.md) _ZNKSt6__ndk114error_category10equivalentEiRKNS_15error_conditionE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf923c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9220.md#insn-00bf923c)
- 新版 [`00bfa230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa214.md#insn-00bfa230)

~~~diff
- 00bf923c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf923c ["INT_ADD", "register:40f0:8", ["const:bf923c:8", "const:4:8"]]
- 00bf923c ["CALLIND", null, ["register:0:8"]]
+ 00bfa230 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfa230 ["INT_ADD", "register:40f0:8", ["const:bfa230:8", "const:4:8"]]
+ 00bfa230 ["CALLIND", null, ["register:0:8"]]
- 00bf923c bytes 00013fd6
+ 00bfa230 bytes 00013fd6
~~~


<a id="compare-5c0208d5b434a02eb7e0394d2f65bce9"></a>

### [`00bf9280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9280.md) → [`00bfa274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa274.md) _ZNSt6__ndk118condition_variableD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) · 呼出先 1件 [`00c5d6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d6f0.md)
- 新版 呼出元 1件 [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) · 呼出先 1件 [`00c5e6c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e6c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf928c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9280.md#insn-00bf928c)
- 新版 [`00bfa280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa274.md#insn-00bfa280)

~~~diff
- 00bf928c ["INT_ADD", "register:40f0:8", ["const:bf928c:8", "const:4:8"]]
- 00bf928c ["CALL", null, ["callee:00c5e6c0:8"]]
+ 00bfa280 ["INT_ADD", "register:40f0:8", ["const:bfa280:8", "const:4:8"]]
+ 00bfa280 ["CALL", null, ["callee:00c5e6c0:8"]]
- 00bf928c bytes 19910194
+ 00bfa280 bytes 10910194
~~~


<a id="compare-b9b3e7655ffcd341d864f84529384042"></a>

### [`00bf92a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf92a0.md) → [`00bfa294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa294.md) _ZNSt6__ndk118condition_variable10notify_oneEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c591e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591e0.md) · 呼出先 1件 [`00c5d700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d700.md)
- 新版 呼出元 1件 [`00c5a1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a1b0.md) · 呼出先 1件 [`00c5e6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e6d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf92ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf92a0.md#insn-00bf92ac)
- 新版 [`00bfa2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa294.md#insn-00bfa2a0)

~~~diff
- 00bf92ac ["INT_ADD", "register:40f0:8", ["const:bf92ac:8", "const:4:8"]]
- 00bf92ac ["CALL", null, ["callee:00c5e6d0:8"]]
+ 00bfa2a0 ["INT_ADD", "register:40f0:8", ["const:bfa2a0:8", "const:4:8"]]
+ 00bfa2a0 ["CALL", null, ["callee:00c5e6d0:8"]]
- 00bf92ac bytes 15910194
+ 00bfa2a0 bytes 0c910194
~~~


<a id="compare-9ccae2f491af57d7398b37374974d957"></a>

### [`00bf92c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf92c0.md) → [`00bfa2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa2b4.md) _ZNSt6__ndk118condition_variable10notify_allEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md) · 呼出先 1件 [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)
- 新版 呼出元 1件 [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md) · 呼出先 1件 [`00c5f260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf92cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf92c0.md#insn-00bf92cc)
- 新版 [`00bfa2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa2b4.md#insn-00bfa2c0)

~~~diff
- 00bf92cc ["INT_ADD", "register:40f0:8", ["const:bf92cc:8", "const:4:8"]]
- 00bf92cc ["CALL", null, ["callee:00c5f260:8"]]
+ 00bfa2c0 ["INT_ADD", "register:40f0:8", ["const:bfa2c0:8", "const:4:8"]]
+ 00bfa2c0 ["CALL", null, ["callee:00c5f260:8"]]
- 00bf92cc bytes f1930194
+ 00bfa2c0 bytes e8930194
~~~


<a id="compare-43abcc3029e8faf8348c057a0d146579"></a>

### [`00bf93cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf93cc.md) → [`00bfa3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa3c0.md) _ZNSt6__ndk125notify_all_at_thread_exitERNS_18condition_variableENS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c581d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581d0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5e2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c591a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591a0.md) [`00c591d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591d0.md) [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5f290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf93e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf93cc.md#insn-00bf93e8) · [`00bf93f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf93cc.md#insn-00bf93f4) · [`00bf9400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf93cc.md#insn-00bf9400)
- 新版 [`00bfa3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa3c0.md#insn-00bfa3dc) · [`00bfa3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa3c0.md#insn-00bfa3e8) · [`00bfa3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa3c0.md#insn-00bfa3f4)

~~~diff
- 00bf93e8 ["INT_ADD", "register:40f0:8", ["const:bf93e8:8", "const:4:8"]]
- 00bf93e8 ["CALL", null, ["callee:00c591d0:8"]]
+ 00bfa3dc ["INT_ADD", "register:40f0:8", ["const:bfa3dc:8", "const:4:8"]]
+ 00bfa3dc ["CALL", null, ["callee:00c591d0:8"]]
- 00bf93e8 bytes 867b0194
+ 00bfa3dc bytes 7d7b0194
- 00bf93f4 ["INT_ADD", "register:40f0:8", ["const:bf93f4:8", "const:4:8"]]
- 00bf93f4 ["CALL", null, ["callee:00c5f290:8"]]
+ 00bfa3e8 ["INT_ADD", "register:40f0:8", ["const:bfa3e8:8", "const:4:8"]]
+ 00bfa3e8 ["CALL", null, ["callee:00c5f290:8"]]
- 00bf93f4 bytes b3930194
+ 00bfa3e8 bytes aa930194
- 00bf9400 ["INT_ADD", "register:40f0:8", ["const:bf9400:8", "const:4:8"]]
- 00bf9400 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bfa3f4 ["INT_ADD", "register:40f0:8", ["const:bfa3f4:8", "const:4:8"]]
+ 00bfa3f4 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf9400 bytes d87a0194
+ 00bfa3f4 bytes cf7a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d19ab387fb64c5e2703f0eb51d5a233"></a>

### [`00bf96dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf96dc.md) → [`00bfa6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa6d0.md) _ZNSt6__ndk112future_errorD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf96f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf96dc.md#insn-00bf96f0)
- 新版 [`00bfa6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa6d0.md#insn-00bfa6e4)

~~~diff
- 00bf96f0 ["INT_ADD", "register:40f0:8", ["const:bf96f0:8", "const:4:8"]]
- 00bf96f0 ["CALL", null, ["callee:00c59410:8"]]
+ 00bfa6e4 ["INT_ADD", "register:40f0:8", ["const:bfa6e4:8", "const:4:8"]]
+ 00bfa6e4 ["CALL", null, ["callee:00c59410:8"]]
- 00bf96f0 bytes 547b0194
+ 00bfa6e4 bytes 4b7b0194
~~~


<a id="compare-45a7e629dc537394faf3c37ce5cccc01"></a>

### [`00bf9718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9718.md) → [`00bfa70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa70c.md) _ZNSt6__ndk117__assoc_sub_state9set_valueEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58620.md) · 呼出先 5件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`00c595f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595f0.md) · 呼出先 5件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9718.md#insn-00bf9734) · [`00bf974c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9718.md#insn-00bf974c) · [`00bf9768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9718.md#insn-00bf9768)
- 新版 [`00bfa728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa70c.md#insn-00bfa728) · [`00bfa740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa70c.md#insn-00bfa740) · [`00bfa75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa70c.md#insn-00bfa75c)

~~~diff
- 00bf9734 ["INT_ADD", "register:40f0:8", ["const:bf9734:8", "const:4:8"]]
- 00bf9734 ["CALL", null, ["callee:00c59180:8"]]
+ 00bfa728 ["INT_ADD", "register:40f0:8", ["const:bfa728:8", "const:4:8"]]
+ 00bfa728 ["CALL", null, ["callee:00c59180:8"]]
- 00bf9734 bytes 9f7a0194
+ 00bfa728 bytes 967a0194
- 00bf974c ["INT_ADD", "register:40f0:8", ["const:bf974c:8", "const:4:8"]]
- 00bf974c ["CALL", null, ["callee:00c59390:8"]]
+ 00bfa740 ["INT_ADD", "register:40f0:8", ["const:bfa740:8", "const:4:8"]]
+ 00bfa740 ["CALL", null, ["callee:00c59390:8"]]
- 00bf974c bytes 1d7b0194
+ 00bfa740 bytes 147b0194
- 00bf9768 ["INT_ADD", "register:40f0:8", ["const:bf9768:8", "const:4:8"]]
- 00bf9768 ["CALL", null, ["callee:00c59420:8"]]
+ 00bfa75c ["INT_ADD", "register:40f0:8", ["const:bfa75c:8", "const:4:8"]]
+ 00bfa75c ["CALL", null, ["callee:00c59420:8"]]
- 00bf9768 bytes 3a7b0194
+ 00bfa75c bytes 317b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed5f5ca03f6299a33ed09989682de60"></a>

### [`00bf97a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf97a4.md) → [`00bfa798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa798.md) _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2f0.md) · 呼出先 7件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)
- 新版 呼出元 1件 [`00c5f2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f2c0.md) · 呼出先 7件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c591d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591d0.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf97c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf97a4.md#insn-00bf97c0) · [`00bf97d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf97a4.md#insn-00bf97d8) · [`00bf97ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf97a4.md#insn-00bf97ec)
- 新版 [`00bfa7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa798.md#insn-00bfa7b4) · [`00bfa7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa798.md#insn-00bfa7cc) · [`00bfa7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa798.md#insn-00bfa7e0)

~~~diff
- 00bf97c0 ["INT_ADD", "register:40f0:8", ["const:bf97c0:8", "const:4:8"]]
- 00bf97c0 ["CALL", null, ["callee:00c59180:8"]]
+ 00bfa7b4 ["INT_ADD", "register:40f0:8", ["const:bfa7b4:8", "const:4:8"]]
+ 00bfa7b4 ["CALL", null, ["callee:00c59180:8"]]
- 00bf97c0 bytes 7c7a0194
+ 00bfa7b4 bytes 737a0194
- 00bf97d8 ["INT_ADD", "register:40f0:8", ["const:bf97d8:8", "const:4:8"]]
- 00bf97d8 ["CALL", null, ["callee:00c59390:8"]]
+ 00bfa7cc ["INT_ADD", "register:40f0:8", ["const:bfa7cc:8", "const:4:8"]]
+ 00bfa7cc ["CALL", null, ["callee:00c59390:8"]]
- 00bf97d8 bytes fa7a0194
+ 00bfa7cc bytes f17a0194
- 00bf97ec ["INT_ADD", "register:40f0:8", ["const:bf97ec:8", "const:4:8"]]
- 00bf97ec ["CALL", null, ["callee:00c591d0:8"]]
+ 00bfa7e0 ["INT_ADD", "register:40f0:8", ["const:bfa7e0:8", "const:4:8"]]
+ 00bfa7e0 ["CALL", null, ["callee:00c591d0:8"]]
- 00bf97ec bytes 857a0194
+ 00bfa7e0 bytes 7c7a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a00ba29b107a5aa80d5ab4a63afd53f2"></a>

### [`00bf9838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9838.md) → [`00bfa82c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa82c.md) _ZNSt6__ndk117__assoc_sub_state13set_exceptionESt13exception_ptr

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58430.md) · 呼出先 6件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`00c59400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59400.md) · 呼出先 6件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf985c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9838.md#insn-00bf985c) · [`00bf9878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9838.md#insn-00bf9878) · [`00bf9888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9838.md#insn-00bf9888)
- 新版 [`00bfa850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa82c.md#insn-00bfa850) · [`00bfa86c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa82c.md#insn-00bfa86c) · [`00bfa87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa82c.md#insn-00bfa87c)

~~~diff
- 00bf985c ["INT_ADD", "register:40f0:8", ["const:bf985c:8", "const:4:8"]]
- 00bf985c ["CALL", null, ["callee:00c59180:8"]]
+ 00bfa850 ["INT_ADD", "register:40f0:8", ["const:bfa850:8", "const:4:8"]]
+ 00bfa850 ["CALL", null, ["callee:00c59180:8"]]
- 00bf985c bytes 557a0194
+ 00bfa850 bytes 4c7a0194
- 00bf9878 ["INT_ADD", "register:40f0:8", ["const:bf9878:8", "const:4:8"]]
- 00bf9878 ["CALL", null, ["callee:00c59390:8"]]
+ 00bfa86c ["INT_ADD", "register:40f0:8", ["const:bfa86c:8", "const:4:8"]]
+ 00bfa86c ["CALL", null, ["callee:00c59390:8"]]
- 00bf9878 bytes d27a0194
+ 00bfa86c bytes c97a0194
- 00bf9888 ["INT_ADD", "register:40f0:8", ["const:bf9888:8", "const:4:8"]]
- 00bf9888 ["CALL", null, ["callee:00c5efd0:8"]]
+ 00bfa87c ["INT_ADD", "register:40f0:8", ["const:bfa87c:8", "const:4:8"]]
+ 00bfa87c ["CALL", null, ["callee:00c5efd0:8"]]
- 00bf9888 bytes de910194
+ 00bfa87c bytes d5910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-023e0c12eaee0a2060d0a095cc87127e"></a>

### [`00bf98dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf98dc.md) → [`00bfa8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa8d0.md) _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e310.md) · 呼出先 8件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)
- 新版 呼出元 1件 [`00c5f2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f2e0.md) · 呼出先 8件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c591d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591d0.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf98dc.md#insn-00bf9900) · [`00bf991c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf98dc.md#insn-00bf991c) · [`00bf992c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf98dc.md#insn-00bf992c)
- 新版 [`00bfa8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa8d0.md#insn-00bfa8f4) · [`00bfa910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa8d0.md#insn-00bfa910) · [`00bfa920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa8d0.md#insn-00bfa920)

~~~diff
- 00bf9900 ["INT_ADD", "register:40f0:8", ["const:bf9900:8", "const:4:8"]]
- 00bf9900 ["CALL", null, ["callee:00c59180:8"]]
+ 00bfa8f4 ["INT_ADD", "register:40f0:8", ["const:bfa8f4:8", "const:4:8"]]
+ 00bfa8f4 ["CALL", null, ["callee:00c59180:8"]]
- 00bf9900 bytes 2c7a0194
+ 00bfa8f4 bytes 237a0194
- 00bf991c ["INT_ADD", "register:40f0:8", ["const:bf991c:8", "const:4:8"]]
- 00bf991c ["CALL", null, ["callee:00c59390:8"]]
+ 00bfa910 ["INT_ADD", "register:40f0:8", ["const:bfa910:8", "const:4:8"]]
+ 00bfa910 ["CALL", null, ["callee:00c59390:8"]]
- 00bf991c bytes a97a0194
+ 00bfa910 bytes a07a0194
- 00bf992c ["INT_ADD", "register:40f0:8", ["const:bf992c:8", "const:4:8"]]
- 00bf992c ["CALL", null, ["callee:00c5efd0:8"]]
+ 00bfa920 ["INT_ADD", "register:40f0:8", ["const:bfa920:8", "const:4:8"]]
+ 00bfa920 ["CALL", null, ["callee:00c5efd0:8"]]
- 00bf992c bytes b5910194
+ 00bfa920 bytes ac910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-438f3d9d3b051580f21ad4867ab0e160"></a>

### [`00bf9980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9980.md) → [`00bfa974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa974.md) _ZNSt6__ndk117__assoc_sub_state12__make_readyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e320.md) · 呼出先 3件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`00c5f2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f2f0.md) · 呼出先 3件 [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9980.md#insn-00bf9998) · [`00bf99ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9980.md#insn-00bf99ac)
- 新版 [`00bfa98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa974.md#insn-00bfa98c) · [`00bfa9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa974.md#insn-00bfa9a0)

~~~diff
- 00bf9998 ["INT_ADD", "register:40f0:8", ["const:bf9998:8", "const:4:8"]]
- 00bf9998 ["CALL", null, ["callee:00c59180:8"]]
+ 00bfa98c ["INT_ADD", "register:40f0:8", ["const:bfa98c:8", "const:4:8"]]
+ 00bfa98c ["CALL", null, ["callee:00c59180:8"]]
- 00bf9998 bytes 067a0194
+ 00bfa98c bytes fd790194
- 00bf99ac ["INT_ADD", "register:40f0:8", ["const:bf99ac:8", "const:4:8"]]
- 00bf99ac ["CALL", null, ["callee:00c59420:8"]]
+ 00bfa9a0 ["INT_ADD", "register:40f0:8", ["const:bfa9a0:8", "const:4:8"]]
+ 00bfa9a0 ["CALL", null, ["callee:00c59420:8"]]
- 00bf99ac bytes a97a0194
+ 00bfa9a0 bytes a07a0194
~~~


<a id="compare-b04398cfd3a32d034d45417004b4f940"></a>

### [`00bf99c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf99c4.md) → [`00bfa9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa9b8.md) _ZNSt6__ndk117__assoc_sub_state4copyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e330.md) · 呼出先 7件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)
- 新版 呼出元 1件 [`00c5f300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f300.md) · 呼出先 7件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c59520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf99f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf99c4.md#insn-00bf99f0) · [`00bf9a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf99c4.md#insn-00bf9a08) · [`00bf9a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf99c4.md#insn-00bf9a24)
- 新版 [`00bfa9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa9b8.md#insn-00bfa9e4) · [`00bfa9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa9b8.md#insn-00bfa9fc) · [`00bfaa18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa9b8.md#insn-00bfaa18)

~~~diff
- 00bf99f0 ["INT_ADD", "register:40f0:8", ["const:bf99f0:8", "const:4:8"]]
- 00bf99f0 ["CALL", null, ["callee:00c59180:8"]]
+ 00bfa9e4 ["INT_ADD", "register:40f0:8", ["const:bfa9e4:8", "const:4:8"]]
+ 00bfa9e4 ["CALL", null, ["callee:00c59180:8"]]
- 00bf99f0 bytes f0790194
+ 00bfa9e4 bytes e7790194
- 00bf9a08 ["INT_ADD", "register:40f0:8", ["const:bf9a08:8", "const:4:8"]]
- 00bf9a08 ["CALL", null, ["callee:00c59520:8"]]
+ 00bfa9fc ["INT_ADD", "register:40f0:8", ["const:bfa9fc:8", "const:4:8"]]
+ 00bfa9fc ["CALL", null, ["callee:00c59520:8"]]
- 00bf9a08 bytes d27a0194
+ 00bfa9fc bytes c97a0194
- 00bf9a24 ["INT_ADD", "register:40f0:8", ["const:bf9a24:8", "const:4:8"]]
- 00bf9a24 ["CALL", null, ["callee:00c59190:8"]]
+ 00bfaa18 ["INT_ADD", "register:40f0:8", ["const:bfaa18:8", "const:4:8"]]
+ 00bfaa18 ["CALL", null, ["callee:00c59190:8"]]
- 00bf9a24 bytes e7790194
+ 00bfaa18 bytes de790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941ce8d335d1bd54dfeaf8b229618056"></a>

### [`00bf9b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9b3c.md) → [`00bfab30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfab30.md) _ZNSt6__ndk117__assoc_sub_state4waitEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58600.md) · 呼出先 3件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)
- 新版 呼出元 1件 [`00c595d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595d0.md) · 呼出先 3件 [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9b3c.md#insn-00bf9b68) · [`00bf9b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9b3c.md#insn-00bf9b80) · [`00bf9b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9b3c.md#insn-00bf9b98)
- 新版 [`00bfab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfab30.md#insn-00bfab5c) · [`00bfab74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfab30.md#insn-00bfab74) · [`00bfab8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfab30.md#insn-00bfab8c)

~~~diff
- 00bf9b68 ["INT_ADD", "register:40f0:8", ["const:bf9b68:8", "const:4:8"]]
- 00bf9b68 ["CALL", null, ["callee:00c59180:8"]]
+ 00bfab5c ["INT_ADD", "register:40f0:8", ["const:bfab5c:8", "const:4:8"]]
+ 00bfab5c ["CALL", null, ["callee:00c59180:8"]]
- 00bf9b68 bytes 92790194
+ 00bfab5c bytes 89790194
- 00bf9b80 ["INT_ADD", "register:40f0:8", ["const:bf9b80:8", "const:4:8"]]
- 00bf9b80 ["CALL", null, ["callee:00c59520:8"]]
+ 00bfab74 ["INT_ADD", "register:40f0:8", ["const:bfab74:8", "const:4:8"]]
+ 00bfab74 ["CALL", null, ["callee:00c59520:8"]]
- 00bf9b80 bytes 747a0194
+ 00bfab74 bytes 6b7a0194
- 00bf9b98 ["INT_ADD", "register:40f0:8", ["const:bf9b98:8", "const:4:8"]]
- 00bf9b98 ["CALL", null, ["callee:00c59190:8"]]
+ 00bfab8c ["INT_ADD", "register:40f0:8", ["const:bfab8c:8", "const:4:8"]]
+ 00bfab8c ["CALL", null, ["callee:00c59190:8"]]
- 00bf9b98 bytes 8a790194
+ 00bfab8c bytes 81790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60a43e82cfcb92ca0a2f8d9585f94cfb"></a>

### [`00bf9be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9be0.md) → [`00bfabd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfabd4.md) _ZNSt6__ndk117__assoc_sub_state9__executeEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9be0.md#insn-00bf9bf0)
- 新版 [`00bfabe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfabd4.md#insn-00bfabe4)

~~~diff
- 00bf9bf0 ["INT_ADD", "register:40f0:8", ["const:bf9bf0:8", "const:4:8"]]
- 00bf9bf0 ["CALL", null, ["callee:0045aa34:8"]]
+ 00bfabe4 ["INT_ADD", "register:40f0:8", ["const:bfabe4:8", "const:4:8"]]
+ 00bfabe4 ["CALL", null, ["callee:0045aa34:8"]]
- 00bf9bf0 bytes c982e197
+ 00bfabe4 bytes 947fe197
~~~


<a id="compare-a2c5242c36a25690c2c9b861ea11060f"></a>

### [`00bf9bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9bf4.md) → [`00bfabe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfabe8.md) _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c585f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585f0.md) · 呼出先 4件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)
- 新版 呼出元 1件 [`00c595c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595c0.md) · 呼出先 4件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9bf4.md#insn-00bf9c10) · [`00bf9c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9bf4.md#insn-00bf9c24) · [`00bf9c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9bf4.md#insn-00bf9c48)
- 新版 [`00bfac04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfabe8.md#insn-00bfac04) · [`00bfac18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfabe8.md#insn-00bfac18) · [`00bfac3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfabe8.md#insn-00bfac3c)

~~~diff
- 00bf9c10 ["INT_ADD", "register:40f0:8", ["const:bf9c10:8", "const:4:8"]]
- 00bf9c10 ["CALL", null, ["callee:00c59180:8"]]
+ 00bfac04 ["INT_ADD", "register:40f0:8", ["const:bfac04:8", "const:4:8"]]
+ 00bfac04 ["CALL", null, ["callee:00c59180:8"]]
- 00bf9c10 bytes 68790194
+ 00bfac04 bytes 5f790194
- 00bf9c24 ["INT_ADD", "register:40f0:8", ["const:bf9c24:8", "const:4:8"]]
- 00bf9c24 ["CALL", null, ["callee:00c54d60:8"]]
+ 00bfac18 ["INT_ADD", "register:40f0:8", ["const:bfac18:8", "const:4:8"]]
+ 00bfac18 ["CALL", null, ["callee:00c54d60:8"]]
- 00bf9c24 bytes 53680194
+ 00bfac18 bytes 52680194
- 00bf9c48 ["INT_ADD", "register:40f0:8", ["const:bf9c48:8", "const:4:8"]]
- 00bf9c48 ["CALL", null, ["callee:0045aa34:8"]]
+ 00bfac3c ["INT_ADD", "register:40f0:8", ["const:bfac3c:8", "const:4:8"]]
+ 00bfac3c ["CALL", null, ["callee:0045aa34:8"]]
- 00bf9c48 bytes b382e197
+ 00bfac3c bytes 7e7fe197
~~~


<a id="compare-e11b5a666784e4c0bd7ee28bb617bc70"></a>

### [`00bf9c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9c60.md) → [`00bfac54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfac54.md) _ZNSt6__ndk16futureIvED1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c585b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585b0.md) · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c59580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59580.md) · 呼出先 1件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9c60.md#insn-00bf9c80)
- 新版 [`00bfac74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfac54.md#insn-00bfac74)

~~~diff
- 00bf9c80 ["INT_ADD", "register:40f0:8", ["const:bf9c80:8", "const:4:8"]]
- 00bf9c80 ["CALL", null, ["callee:00c54d90:8"]]
+ 00bfac74 ["INT_ADD", "register:40f0:8", ["const:bfac74:8", "const:4:8"]]
+ 00bfac74 ["CALL", null, ["callee:00c54d90:8"]]
- 00bf9c80 bytes 48680194
+ 00bfac74 bytes 47680194
~~~


<a id="compare-2d6ca0c685a1c2bf3db8db4771738329"></a>

### [`00bf9cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9cb4.md) → [`00bfaca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaca8.md) _ZNSt6__ndk16futureIvE3getEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5e330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e330.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5f300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9cb4.md#insn-00bf9cd0) · [`00bf9cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9cb4.md#insn-00bf9cdc)
- 新版 [`00bfacc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaca8.md#insn-00bfacc4) · [`00bfacd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaca8.md#insn-00bfacd0)

~~~diff
- 00bf9cd0 ["INT_ADD", "register:40f0:8", ["const:bf9cd0:8", "const:4:8"]]
- 00bf9cd0 ["CALL", null, ["callee:00c5f300:8"]]
+ 00bfacc4 ["INT_ADD", "register:40f0:8", ["const:bfacc4:8", "const:4:8"]]
+ 00bfacc4 ["CALL", null, ["callee:00c5f300:8"]]
- 00bf9cd0 bytes 98910194
+ 00bfacc4 bytes 8f910194
- 00bf9cdc ["INT_ADD", "register:40f0:8", ["const:bf9cdc:8", "const:4:8"]]
- 00bf9cdc ["CALL", null, ["callee:00c54d90:8"]]
+ 00bfacd0 ["INT_ADD", "register:40f0:8", ["const:bfacd0:8", "const:4:8"]]
+ 00bfacd0 ["CALL", null, ["callee:00c54d90:8"]]
- 00bf9cdc bytes 31680194
+ 00bfacd0 bytes 30680194
~~~


<a id="compare-35b15bc3815fc1d2968b4ac94c70860f"></a>

### [`00bf9f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f28.md) → [`00bfaf1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf1c.md) _ZNSt6__ndk17promiseIvE10get_futureEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c585f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c595c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f28.md#insn-00bf9f4c)
- 新版 [`00bfaf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf1c.md#insn-00bfaf40)

~~~diff
- 00bf9f4c ["INT_ADD", "register:40f0:8", ["const:bf9f4c:8", "const:4:8"]]
- 00bf9f4c ["CALL", null, ["callee:0045aa34:8"]]
+ 00bfaf40 ["INT_ADD", "register:40f0:8", ["const:bfaf40:8", "const:4:8"]]
+ 00bfaf40 ["CALL", null, ["callee:0045aa34:8"]]
- 00bf9f4c bytes f281e197
+ 00bfaf40 bytes bd7ee197
~~~


<a id="compare-f74de4bc266330fa472f386c72923557"></a>

### [`00bf9f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f50.md) → [`00bfaf44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf44.md) _ZNSt6__ndk17promiseIvE9set_valueEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c58620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58620.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c595f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f50.md#insn-00bf9f70)
- 新版 [`00bfaf64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf44.md#insn-00bfaf64)

~~~diff
- 00bf9f70 ["INT_ADD", "register:40f0:8", ["const:bf9f70:8", "const:4:8"]]
- 00bf9f70 ["CALL", null, ["callee:0045aa34:8"]]
+ 00bfaf64 ["INT_ADD", "register:40f0:8", ["const:bfaf64:8", "const:4:8"]]
+ 00bfaf64 ["CALL", null, ["callee:0045aa34:8"]]
- 00bf9f70 bytes e981e197
+ 00bfaf64 bytes b47ee197
~~~


<a id="compare-113ed3bcb951eac2abeba6fba51392bb"></a>

### [`00bf9f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f74.md) → [`00bfaf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf68.md) _ZNSt6__ndk17promiseIvE13set_exceptionESt13exception_ptr

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58430.md) [`00c58580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58580.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c59400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59400.md) [`00c59550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f74.md#insn-00bf9f90) · [`00bf9f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f74.md#insn-00bf9f9c) · [`00bf9fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f74.md#insn-00bf9fa4)
- 新版 [`00bfaf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf68.md#insn-00bfaf84) · [`00bfaf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf68.md#insn-00bfaf90) · [`00bfaf98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaf68.md#insn-00bfaf98)

~~~diff
- 00bf9f90 ["INT_ADD", "register:40f0:8", ["const:bf9f90:8", "const:4:8"]]
- 00bf9f90 ["CALL", null, ["callee:00c59550:8"]]
+ 00bfaf84 ["INT_ADD", "register:40f0:8", ["const:bfaf84:8", "const:4:8"]]
+ 00bfaf84 ["CALL", null, ["callee:00c59550:8"]]
- 00bf9f90 bytes 7c790194
+ 00bfaf84 bytes 73790194
- 00bf9f9c ["INT_ADD", "register:40f0:8", ["const:bf9f9c:8", "const:4:8"]]
- 00bf9f9c ["CALL", null, ["callee:00c59400:8"]]
+ 00bfaf90 ["INT_ADD", "register:40f0:8", ["const:bfaf90:8", "const:4:8"]]
+ 00bfaf90 ["CALL", null, ["callee:00c59400:8"]]
- 00bf9f9c bytes 25790194
+ 00bfaf90 bytes 1c790194
- 00bf9fa4 ["INT_ADD", "register:40f0:8", ["const:bf9fa4:8", "const:4:8"]]
- 00bf9fa4 ["CALL", null, ["callee:00c59390:8"]]
+ 00bfaf98 ["INT_ADD", "register:40f0:8", ["const:bfaf98:8", "const:4:8"]]
+ 00bfaf98 ["CALL", null, ["callee:00c59390:8"]]
- 00bf9fa4 bytes 07790194
+ 00bfaf98 bytes fe780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a945dce85658a3342ed8c05a56961e44"></a>

### [`00bf9fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9fd4.md) → [`00bfafc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfafc8.md) _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c5e2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c5f2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9fd4.md#insn-00bf9ff4)
- 新版 [`00bfafe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfafc8.md#insn-00bfafe8)

~~~diff
- 00bf9ff4 ["INT_ADD", "register:40f0:8", ["const:bf9ff4:8", "const:4:8"]]
- 00bf9ff4 ["CALL", null, ["callee:0045aa34:8"]]
+ 00bfafe8 ["INT_ADD", "register:40f0:8", ["const:bfafe8:8", "const:4:8"]]
+ 00bfafe8 ["CALL", null, ["callee:0045aa34:8"]]
- 00bf9ff4 bytes c881e197
+ 00bfafe8 bytes 937ee197
~~~


<a id="compare-65443d507f3fe6579c82ccf12c4253fc"></a>

### [`00bf9ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9ff8.md) → [`00bfafec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfafec.md) _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58580.md) [`00c5e310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e310.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c59550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59550.md) [`00c5f2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9ff8.md#insn-00bfa014) · [`00bfa020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9ff8.md#insn-00bfa020) · [`00bfa028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9ff8.md#insn-00bfa028)
- 新版 [`00bfb008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfafec.md#insn-00bfb008) · [`00bfb014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfafec.md#insn-00bfb014) · [`00bfb01c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfafec.md#insn-00bfb01c)

~~~diff
- 00bfa014 ["INT_ADD", "register:40f0:8", ["const:bfa014:8", "const:4:8"]]
- 00bfa014 ["CALL", null, ["callee:00c59550:8"]]
+ 00bfb008 ["INT_ADD", "register:40f0:8", ["const:bfb008:8", "const:4:8"]]
+ 00bfb008 ["CALL", null, ["callee:00c59550:8"]]
- 00bfa014 bytes 5b790194
+ 00bfb008 bytes 52790194
- 00bfa020 ["INT_ADD", "register:40f0:8", ["const:bfa020:8", "const:4:8"]]
- 00bfa020 ["CALL", null, ["callee:00c5f2e0:8"]]
+ 00bfb014 ["INT_ADD", "register:40f0:8", ["const:bfb014:8", "const:4:8"]]
+ 00bfb014 ["CALL", null, ["callee:00c5f2e0:8"]]
- 00bfa020 bytes bc900194
+ 00bfb014 bytes b3900194
- 00bfa028 ["INT_ADD", "register:40f0:8", ["const:bfa028:8", "const:4:8"]]
- 00bfa028 ["CALL", null, ["callee:00c59390:8"]]
+ 00bfb01c ["INT_ADD", "register:40f0:8", ["const:bfb01c:8", "const:4:8"]]
+ 00bfb01c ["CALL", null, ["callee:00c59390:8"]]
- 00bfa028 bytes e6780194
+ 00bfb01c bytes dd780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa5a420975e8978cd0c28d5f8477d832"></a>

### [`00bfa058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa058.md) → [`00bfb04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb04c.md) _ZNSt6__ndk113shared_futureIvED1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa058.md#insn-00bfa078)
- 新版 [`00bfb06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb04c.md#insn-00bfb06c)

~~~diff
- 00bfa078 ["INT_ADD", "register:40f0:8", ["const:bfa078:8", "const:4:8"]]
- 00bfa078 ["CALL", null, ["callee:00c54d90:8"]]
+ 00bfb06c ["INT_ADD", "register:40f0:8", ["const:bfb06c:8", "const:4:8"]]
+ 00bfb06c ["CALL", null, ["callee:00c54d90:8"]]
- 00bfa078 bytes 4a670194
+ 00bfb06c bytes 49670194
~~~


<a id="compare-214612c03e5c6b060feae361339b2336"></a>

### [`00bfa0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa0ac.md) → [`00bfb0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb0a0.md) _ZNSt6__ndk113shared_futureIvEaSERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa0ac.md#insn-00bfa0d8) · [`00bfa0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa0ac.md#insn-00bfa0ec) · [`00bfa100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa0ac.md#insn-00bfa100)
- 新版 [`00bfb0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb0a0.md#insn-00bfb0cc) · [`00bfb0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb0a0.md#insn-00bfb0e0) · [`00bfb0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb0a0.md#insn-00bfb0f4)

~~~diff
- 00bfa0d8 ["INT_ADD", "register:40f0:8", ["const:bfa0d8:8", "const:4:8"]]
- 00bfa0d8 ["CALL", null, ["callee:00c54d60:8"]]
+ 00bfb0cc ["INT_ADD", "register:40f0:8", ["const:bfb0cc:8", "const:4:8"]]
+ 00bfb0cc ["CALL", null, ["callee:00c54d60:8"]]
- 00bfa0d8 bytes 26670194
+ 00bfb0cc bytes 25670194
- 00bfa0ec ["INT_ADD", "register:40f0:8", ["const:bfa0ec:8", "const:4:8"]]
- 00bfa0ec ["CALL", null, ["callee:00c54d90:8"]]
+ 00bfb0e0 ["INT_ADD", "register:40f0:8", ["const:bfb0e0:8", "const:4:8"]]
+ 00bfb0e0 ["CALL", null, ["callee:00c54d90:8"]]
- 00bfa0ec bytes 2d670194
+ 00bfb0e0 bytes 2c670194
- 00bfa100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfa100 ["INT_ADD", "register:40f0:8", ["const:bfa100:8", "const:4:8"]]
- 00bfa100 ["CALLIND", null, ["register:0:8"]]
+ 00bfb0f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb0f4 ["INT_ADD", "register:40f0:8", ["const:bfb0f4:8", "const:4:8"]]
+ 00bfb0f4 ["CALLIND", null, ["register:0:8"]]
- 00bfa100 bytes 00013fd6
+ 00bfb0f4 bytes 00013fd6
~~~


<a id="compare-5267369e3564847df7c090ed32175906"></a>

### [`00bfa180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa180.md) → [`00bfb174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb174.md) FUN_00bfb174

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa180.md#insn-00bfa194)
- 新版 [`00bfb188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb174.md#insn-00bfb188)

~~~diff
- 00bfa194 ["INT_ADD", "register:40f0:8", ["const:bfa194:8", "const:4:8"]]
- 00bfa194 ["CALL", null, ["callee:00c5ef90:8"]]
+ 00bfb188 ["INT_ADD", "register:40f0:8", ["const:bfb188:8", "const:4:8"]]
+ 00bfb188 ["CALL", null, ["callee:00c5ef90:8"]]
- 00bfa194 bytes 8b8f0194
+ 00bfb188 bytes 828f0194
~~~


<a id="compare-d528d5c8bb035f6741cce93fc7537d61"></a>

### [`00bfa1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1ac.md) → [`00bfb1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1a0.md) _ZNSt6__ndk15mutexD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0043aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb8.md) [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`0048bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048bb30.md) [`0058f6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md) · 呼出先 1件 [`00c5b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b760.md)
- 新版 呼出元 6件 [`0043b1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d8.md) [`00452848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452848.md) [`00452fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452fb4.md) [`0048be50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048be50.md) [`0058fa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fa10.md) · 呼出先 1件 [`00c5c730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1ac.md#insn-00bfa1b8)
- 新版 [`00bfb1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1a0.md#insn-00bfb1ac)

~~~diff
- 00bfa1b8 ["INT_ADD", "register:40f0:8", ["const:bfa1b8:8", "const:4:8"]]
- 00bfa1b8 ["CALL", null, ["callee:00c5c730:8"]]
+ 00bfb1ac ["INT_ADD", "register:40f0:8", ["const:bfb1ac:8", "const:4:8"]]
+ 00bfb1ac ["CALL", null, ["callee:00c5c730:8"]]
- 00bfa1b8 bytes 6a850194
+ 00bfb1ac bytes 61850194
~~~


<a id="compare-e0c9ec7e4c79bb22d3d33fac40d8b0fc"></a>

### [`00bfa1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1f8.md) → [`00bfb1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1ec.md) _ZNSt6__ndk15mutex8try_lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1f8.md#insn-00bfa204)
- 新版 [`00bfb1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1ec.md#insn-00bfb1f8)

~~~diff
- 00bfa204 ["INT_ADD", "register:40f0:8", ["const:bfa204:8", "const:4:8"]]
- 00bfa204 ["CALL", null, ["callee:00c5f310:8"]]
+ 00bfb1f8 ["INT_ADD", "register:40f0:8", ["const:bfb1f8:8", "const:4:8"]]
+ 00bfb1f8 ["CALL", null, ["callee:00c5f310:8"]]
- 00bfa204 bytes 4f900194
+ 00bfb1f8 bytes 46900194
~~~


<a id="compare-23fec7b1f4a0c1d427e42b7ee85b5215"></a>

### [`00bfa220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa220.md) → [`00bfb214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb214.md) _ZNSt6__ndk15mutex6unlockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 1件 [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) · 呼出先 1件 [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa220.md#insn-00bfa22c)
- 新版 [`00bfb220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb214.md#insn-00bfb220)

~~~diff
- 00bfa22c ["INT_ADD", "register:40f0:8", ["const:bfa22c:8", "const:4:8"]]
- 00bfa22c ["CALL", null, ["callee:00c5c750:8"]]
+ 00bfb220 ["INT_ADD", "register:40f0:8", ["const:bfb220:8", "const:4:8"]]
+ 00bfb220 ["CALL", null, ["callee:00c5c750:8"]]
- 00bfa22c bytes 55850194
+ 00bfb220 bytes 4c850194
~~~


<a id="compare-41a3ff430547a2f8c77fba1feefb8276"></a>

### [`00bfa2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa2e4.md) → [`00bfb2d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb2d8.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1a0.md) · 呼出先 1件 [`00c5b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b760.md)
- 新版 呼出元 1件 [`00c5b170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b170.md) · 呼出先 1件 [`00c5c730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c730.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa2e4.md#insn-00bfa2f0)
- 新版 [`00bfb2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb2d8.md#insn-00bfb2e4)

~~~diff
- 00bfa2f0 ["INT_ADD", "register:40f0:8", ["const:bfa2f0:8", "const:4:8"]]
- 00bfa2f0 ["CALL", null, ["callee:00c5c730:8"]]
+ 00bfb2e4 ["INT_ADD", "register:40f0:8", ["const:bfb2e4:8", "const:4:8"]]
+ 00bfb2e4 ["CALL", null, ["callee:00c5c730:8"]]
- 00bfa2f0 bytes 1c850194
+ 00bfb2e4 bytes 13850194
~~~


<a id="compare-8bcb46af7d183c1ad88f71c78bb76cbc"></a>

### [`00bfa330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa330.md) → [`00bfb324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb324.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1c0.md) · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 1件 [`00c5b190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b190.md) · 呼出先 1件 [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa330.md#insn-00bfa33c)
- 新版 [`00bfb330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb324.md#insn-00bfb330)

~~~diff
- 00bfa33c ["INT_ADD", "register:40f0:8", ["const:bfa33c:8", "const:4:8"]]
- 00bfa33c ["CALL", null, ["callee:00c5c750:8"]]
+ 00bfb330 ["INT_ADD", "register:40f0:8", ["const:bfb330:8", "const:4:8"]]
+ 00bfb330 ["CALL", null, ["callee:00c5c750:8"]]
- 00bfa33c bytes 11850194
+ 00bfb330 bytes 08850194
~~~


<a id="compare-946333073ee7ecf3babacb6ad463cae4"></a>

### [`00bfa350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa350.md) → [`00bfb344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb344.md) _ZNSt6__ndk115recursive_mutex8try_lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa350.md#insn-00bfa35c)
- 新版 [`00bfb350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb344.md#insn-00bfb350)

~~~diff
- 00bfa35c ["INT_ADD", "register:40f0:8", ["const:bfa35c:8", "const:4:8"]]
- 00bfa35c ["CALL", null, ["callee:00c5f310:8"]]
+ 00bfb350 ["INT_ADD", "register:40f0:8", ["const:bfb350:8", "const:4:8"]]
+ 00bfb350 ["CALL", null, ["callee:00c5f310:8"]]
- 00bfa35c bytes f98f0194
+ 00bfb350 bytes f08f0194
~~~


<a id="compare-6865bd2d651ad5d201dd7aac0a2a64f7"></a>

### [`00bfa478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa478.md) → [`00bfb46c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb46c.md) _ZNSt6__ndk111timed_mutex8try_lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md) [`00c5f310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa478.md#insn-00bfa48c) · [`00bfa4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa478.md#insn-00bfa4b8)
- 新版 [`00bfb480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb46c.md#insn-00bfb480) · [`00bfb4ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb46c.md#insn-00bfb4ac)

~~~diff
- 00bfa48c ["INT_ADD", "register:40f0:8", ["const:bfa48c:8", "const:4:8"]]
- 00bfa48c ["CALL", null, ["callee:00c5f310:8"]]
+ 00bfb480 ["INT_ADD", "register:40f0:8", ["const:bfb480:8", "const:4:8"]]
+ 00bfb480 ["CALL", null, ["callee:00c5f310:8"]]
- 00bfa48c bytes ad8f0194
+ 00bfb480 bytes a48f0194
- 00bfa4b8 ["INT_ADD", "register:40f0:8", ["const:bfa4b8:8", "const:4:8"]]
- 00bfa4b8 ["CALL", null, ["callee:00c5c750:8"]]
+ 00bfb4ac ["INT_ADD", "register:40f0:8", ["const:bfb4ac:8", "const:4:8"]]
+ 00bfb4ac ["CALL", null, ["callee:00c5c750:8"]]
- 00bfa4b8 bytes b2840194
+ 00bfb4ac bytes a9840194
~~~


<a id="compare-0f157fc323dc5cc9b11e762b0c3dac4e"></a>

### [`00bfa67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa67c.md) → [`00bfb670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb670.md) _ZNSt6__ndk121recursive_timed_mutex8try_lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c586f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586f0.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e340.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c596c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596c0.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md) [`00c5f310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa67c.md#insn-00bfa694) · [`00bfa6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa67c.md#insn-00bfa6a0) · [`00bfa6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa67c.md#insn-00bfa6e0)
- 新版 [`00bfb688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb670.md#insn-00bfb688) · [`00bfb694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb670.md#insn-00bfb694) · [`00bfb6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb670.md#insn-00bfb6d4)

~~~diff
- 00bfa694 ["INT_ADD", "register:40f0:8", ["const:bfa694:8", "const:4:8"]]
- 00bfa694 ["CALL", null, ["callee:00c596c0:8"]]
+ 00bfb688 ["INT_ADD", "register:40f0:8", ["const:bfb688:8", "const:4:8"]]
+ 00bfb688 ["CALL", null, ["callee:00c596c0:8"]]
- 00bfa694 bytes 17780194
+ 00bfb688 bytes 0e780194
- 00bfa6a0 ["INT_ADD", "register:40f0:8", ["const:bfa6a0:8", "const:4:8"]]
- 00bfa6a0 ["CALL", null, ["callee:00c5f310:8"]]
+ 00bfb694 ["INT_ADD", "register:40f0:8", ["const:bfb694:8", "const:4:8"]]
+ 00bfb694 ["CALL", null, ["callee:00c5f310:8"]]
- 00bfa6a0 bytes 288f0194
+ 00bfb694 bytes 1f8f0194
- 00bfa6e0 ["INT_ADD", "register:40f0:8", ["const:bfa6e0:8", "const:4:8"]]
- 00bfa6e0 ["CALL", null, ["callee:00c5c750:8"]]
+ 00bfb6d4 ["INT_ADD", "register:40f0:8", ["const:bfb6d4:8", "const:4:8"]]
+ 00bfb6d4 ["CALL", null, ["callee:00c5c750:8"]]
- 00bfa6e0 bytes 28840194
+ 00bfb6d4 bytes 1f840194
~~~


<a id="compare-6e8564fc7fd553c123d092840dd3c5c1"></a>

### [`00bfa780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa780.md) → [`00bfb774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb774.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58250.md) · 呼出先 1件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c59220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59220.md) · 呼出先 1件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa780.md#insn-00bfa79c)
- 新版 [`00bfb790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb774.md#insn-00bfb790)

~~~diff
- 00bfa79c ["INT_ADD", "register:40f0:8", ["const:bfa79c:8", "const:4:8"]]
- 00bfa79c ["CALL", null, ["callee:00c590c0:8"]]
+ 00bfb790 ["INT_ADD", "register:40f0:8", ["const:bfb790:8", "const:4:8"]]
+ 00bfb790 ["CALL", null, ["callee:00c590c0:8"]]
- 00bfa79c bytes 55760194
+ 00bfb790 bytes 4c760194
~~~


<a id="compare-13d38bb7f114d546c406aaf33084c540"></a>

### [`00bfa834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa834.md) → [`00bfb828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb828.md) _ZNSt6__ndk16thread20hardware_concurrencyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa834.md#insn-00bfa844)
- 新版 [`00bfb838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb828.md#insn-00bfb838)

~~~diff
- 00bfa844 ["INT_ADD", "register:40f0:8", ["const:bfa844:8", "const:4:8"]]
- 00bfa844 ["CALL", null, ["callee:00c5f330:8"]]
+ 00bfb838 ["INT_ADD", "register:40f0:8", ["const:bfb838:8", "const:4:8"]]
+ 00bfb838 ["CALL", null, ["callee:00c5f330:8"]]
- 00bfa844 bytes c78e0194
+ 00bfb838 bytes be8e0194
~~~


<a id="compare-f349a52e5c08e4bd2a49dc3cc18ea179"></a>

### [`00bfa860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa860.md) → [`00bfb854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb854.md) _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58560.md) · 呼出先 2件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e370.md)
- 新版 呼出元 1件 [`00c59530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59530.md) · 呼出先 2件 [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa860.md#insn-00bfa8b4) · [`00bfa8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa860.md#insn-00bfa8c0)
- 新版 [`00bfb8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb854.md#insn-00bfb8a8) · [`00bfb8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb854.md#insn-00bfb8b4)

~~~diff
- 00bfa8b4 ["INT_ADD", "register:40f0:8", ["const:bfa8b4:8", "const:4:8"]]
- 00bfa8b4 ["CALL", null, ["callee:00c5f340:8"]]
+ 00bfb8a8 ["INT_ADD", "register:40f0:8", ["const:bfb8a8:8", "const:4:8"]]
+ 00bfb8a8 ["CALL", null, ["callee:00c5f340:8"]]
- 00bfa8b4 bytes af8e0194
+ 00bfb8a8 bytes a68e0194
- 00bfa8c0 ["INT_ADD", "register:40f0:8", ["const:bfa8c0:8", "const:4:8"]]
- 00bfa8c0 ["CALL", null, ["callee:00c59160:8"]]
+ 00bfb8b4 ["INT_ADD", "register:40f0:8", ["const:bfb8b4:8", "const:4:8"]]
+ 00bfb8b4 ["CALL", null, ["callee:00c59160:8"]]
- 00bfa8c0 bytes 34760194
+ 00bfb8b4 bytes 2b760194
~~~


<a id="compare-a7be9901d3a5bed8c45e7f4a6e25035b"></a>

### [`00bfa998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md) → [`00bfb98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb98c.md) FUN_00bfb98c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfac8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac8c.md) · 呼出先 5件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md) [`00c5e320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e320.md)
- 新版 呼出元 1件 [`00bfbc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbc80.md) · 呼出先 5件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md) [`00c5f2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md#insn-00bfa9c0) · [`00bfa9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md#insn-00bfa9c8) · [`00bfa9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md#insn-00bfa9f0)
- 新版 [`00bfb9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb98c.md#insn-00bfb9b4) · [`00bfb9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb98c.md#insn-00bfb9bc) · [`00bfb9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb98c.md#insn-00bfb9e4)

~~~diff
- 00bfa9c0 ["INT_ADD", "register:40f0:8", ["const:bfa9c0:8", "const:4:8"]]
- 00bfa9c0 ["CALL", null, ["callee:00c59420:8"]]
+ 00bfb9b4 ["INT_ADD", "register:40f0:8", ["const:bfb9b4:8", "const:4:8"]]
+ 00bfb9b4 ["CALL", null, ["callee:00c59420:8"]]
- 00bfa9c0 bytes a4760194
+ 00bfb9b4 bytes 9b760194
- 00bfa9c8 ["INT_ADD", "register:40f0:8", ["const:bfa9c8:8", "const:4:8"]]
- 00bfa9c8 ["CALL", null, ["callee:00c59190:8"]]
+ 00bfb9bc ["INT_ADD", "register:40f0:8", ["const:bfb9bc:8", "const:4:8"]]
+ 00bfb9bc ["CALL", null, ["callee:00c59190:8"]]
- 00bfa9c8 bytes fe750194
+ 00bfb9bc bytes f5750194
- 00bfa9f0 ["INT_ADD", "register:40f0:8", ["const:bfa9f0:8", "const:4:8"]]
- 00bfa9f0 ["CALL", null, ["callee:00c5f2f0:8"]]
+ 00bfb9e4 ["INT_ADD", "register:40f0:8", ["const:bfb9e4:8", "const:4:8"]]
+ 00bfb9e4 ["CALL", null, ["callee:00c5f2f0:8"]]
- 00bfa9f0 bytes 4c8e0194
+ 00bfb9e4 bytes 438e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-275d7d5871f2754b2c66ea6de5a25b53"></a>

### [`00bfaa64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaa64.md) → [`00bfba58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfba58.md) FUN_00bfba58

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfacd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfacd0.md) · 呼出先 4件 [`00bface8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00bfbcc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcc4.md) · 呼出先 4件 [`00bfbcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcdc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfaae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaa64.md#insn-00bfaae0) · [`00bfab24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaa64.md#insn-00bfab24) · [`00bfab38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaa64.md#insn-00bfab38)
- 新版 [`00bfbad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfba58.md#insn-00bfbad4) · [`00bfbb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfba58.md#insn-00bfbb18) · [`00bfbb2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfba58.md#insn-00bfbb2c)

~~~diff
- 00bfaae0 ["INT_ADD", "register:40f0:8", ["const:bfaae0:8", "const:4:8"]]
- 00bfaae0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bfbad4 ["INT_ADD", "register:40f0:8", ["const:bfbad4:8", "const:4:8"]]
+ 00bfbad4 ["CALL", null, ["callee:00c58f30:8"]]
- 00bfaae0 bytes 20750194
+ 00bfbad4 bytes 17750194
- 00bfab24 ["INT_ADD", "register:40f0:8", ["const:bfab24:8", "const:4:8"]]
- 00bfab24 ["CALL", null, ["callee:00c590a0:8"]]
+ 00bfbb18 ["INT_ADD", "register:40f0:8", ["const:bfbb18:8", "const:4:8"]]
+ 00bfbb18 ["CALL", null, ["callee:00c590a0:8"]]
- 00bfab24 bytes 6b750194
+ 00bfbb18 bytes 62750194
- 00bfab38 ["INT_ADD", "register:40f0:8", ["const:bfab38:8", "const:4:8"]]
- 00bfab38 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bfbb2c ["INT_ADD", "register:40f0:8", ["const:bfbb2c:8", "const:4:8"]]
+ 00bfbb2c ["CALL", null, ["callee:00c58f50:8"]]
- 00bfab38 bytes 12750194
+ 00bfbb2c bytes 09750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-836932a50c8bf0db42079ab2445e9b5f"></a>

### [`00bfab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md) → [`00bfbb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbb54.md) FUN_00bfbb54

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfacdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfacdc.md) · 呼出先 5件 [`00bfad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00bfbcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcd0.md) · 呼出先 5件 [`00bfbcf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcf4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfabd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md#insn-00bfabd4) · [`00bfac08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md#insn-00bfac08) · [`00bfac1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md#insn-00bfac1c)
- 新版 [`00bfbbc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbb54.md#insn-00bfbbc8) · [`00bfbbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbb54.md#insn-00bfbbfc) · [`00bfbc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbb54.md#insn-00bfbc10)

~~~diff
- 00bfabd4 ["INT_ADD", "register:40f0:8", ["const:bfabd4:8", "const:4:8"]]
- 00bfabd4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bfbbc8 ["INT_ADD", "register:40f0:8", ["const:bfbbc8:8", "const:4:8"]]
+ 00bfbbc8 ["CALL", null, ["callee:00c58f30:8"]]
- 00bfabd4 bytes e3740194
+ 00bfbbc8 bytes da740194
- 00bfac08 ["INT_ADD", "register:40f0:8", ["const:bfac08:8", "const:4:8"]]
- 00bfac08 ["CALL", null, ["callee:00c590a0:8"]]
+ 00bfbbfc ["INT_ADD", "register:40f0:8", ["const:bfbbfc:8", "const:4:8"]]
+ 00bfbbfc ["CALL", null, ["callee:00c590a0:8"]]
- 00bfac08 bytes 32750194
+ 00bfbbfc bytes 29750194
- 00bfac1c ["INT_ADD", "register:40f0:8", ["const:bfac1c:8", "const:4:8"]]
- 00bfac1c ["CALL", null, ["callee:00c58f50:8"]]
+ 00bfbc10 ["INT_ADD", "register:40f0:8", ["const:bfbc10:8", "const:4:8"]]
+ 00bfbc10 ["CALL", null, ["callee:00c58f50:8"]]
- 00bfac1c bytes d9740194
+ 00bfbc10 bytes d0740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6649a3f58f70e57bf8d528174a457d2c"></a>

### [`00bfac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac50.md) → [`00bfbc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbc44.md) _ZNSt6__ndk115__thread_structC1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c581d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581d0.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c591a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591a0.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfac68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac50.md#insn-00bfac68)
- 新版 [`00bfbc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbc44.md#insn-00bfbc5c)

~~~diff
- 00bfac68 ["INT_ADD", "register:40f0:8", ["const:bfac68:8", "const:4:8"]]
- 00bfac68 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bfbc5c ["INT_ADD", "register:40f0:8", ["const:bfbc5c:8", "const:4:8"]]
+ 00bfbc5c ["CALL", null, ["callee:00c58f30:8"]]
- 00bfac68 bytes be740194
+ 00bfbc5c bytes b5740194
~~~


<a id="compare-c40fc7ba5d1489fc78018cda99821503"></a>

### [`00bfac8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac8c.md) → [`00bfbc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbc80.md) _ZNSt6__ndk115__thread_structD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md) · 呼出先 2件 [`00bfa998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c591f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591f0.md) · 呼出先 2件 [`00bfb98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb98c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfaca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac8c.md#insn-00bfaca8)
- 新版 [`00bfbc9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbc80.md#insn-00bfbc9c)

~~~diff
- 00bfaca8 ["INT_ADD", "register:40f0:8", ["const:bfaca8:8", "const:4:8"]]
- 00bfaca8 ["CALL", null, ["callee:00bfb98c:8"]]
+ 00bfbc9c ["INT_ADD", "register:40f0:8", ["const:bfbc9c:8", "const:4:8"]]
+ 00bfbc9c ["CALL", null, ["callee:00bfb98c:8"]]
- 00bfaca8 bytes 3cffff97
+ 00bfbc9c bytes 3cffff97
~~~


<a id="compare-e68544a74a00aeba07ade381774c5141"></a>

### [`00bfad18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad18.md) → [`00bfbd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbd0c.md) FUN_00bfbd0c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bfa964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)
- 新版 呼出元 1件 [`00bfb958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb958.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c591f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad18.md#insn-00bfad34)
- 新版 [`00bfbd28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbd0c.md#insn-00bfbd28)

~~~diff
- 00bfad34 ["INT_ADD", "register:40f0:8", ["const:bfad34:8", "const:4:8"]]
- 00bfad34 ["CALL", null, ["callee:00c591f0:8"]]
+ 00bfbd28 ["INT_ADD", "register:40f0:8", ["const:bfbd28:8", "const:4:8"]]
+ 00bfbd28 ["CALL", null, ["callee:00c591f0:8"]]
- 00bfad34 bytes 3b750194
+ 00bfbd28 bytes 32750194
~~~


<a id="compare-d2af5fa10dd6cc688fe5eb764313944c"></a>

### [`00bfadf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfadf4.md) → [`00bfbde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbde8.md) _ZNSt6__ndk113random_deviceD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005607cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005607cc.md) [`00c584a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c584a0.md) · 呼出先 1件 [`00c598a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598a0.md)
- 新版 呼出元 2件 [`00560aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560aec.md) [`00c59470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59470.md) · 呼出先 1件 [`00c5a870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a870.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfae04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfadf4.md#insn-00bfae04)
- 新版 [`00bfbdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbde8.md#insn-00bfbdf8)

~~~diff
- 00bfae04 ["INT_ADD", "register:40f0:8", ["const:bfae04:8", "const:4:8"]]
- 00bfae04 ["CALL", null, ["callee:00c5a870:8"]]
+ 00bfbdf8 ["INT_ADD", "register:40f0:8", ["const:bfbdf8:8", "const:4:8"]]
+ 00bfbdf8 ["CALL", null, ["callee:00c5a870:8"]]
- 00bfae04 bytes a77a0194
+ 00bfbdf8 bytes 9e7a0194
~~~


<a id="compare-59d9d9c6eac7d23d0cfa9f95feeb376d"></a>

### [`00bfaeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaeac.md) → [`00bfbea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbea0.md) _ZNKSt6__ndk113random_device7entropyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e380.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfaecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaeac.md#insn-00bfaecc)
- 新版 [`00bfbec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbea0.md#insn-00bfbec0)

~~~diff
- 00bfaecc ["INT_ADD", "register:40f0:8", ["const:bfaecc:8", "const:4:8"]]
- 00bfaecc ["CALL", null, ["callee:00c5f350:8"]]
+ 00bfbec0 ["INT_ADD", "register:40f0:8", ["const:bfbec0:8", "const:4:8"]]
+ 00bfbec0 ["CALL", null, ["callee:00c5f350:8"]]
- 00bfaecc bytes 2d8d0194
+ 00bfbec0 bytes 248d0194
~~~


<a id="compare-82deddafa9b6440bfee7516e0e02b115"></a>

### [`00bfb060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb060.md) → [`00bfc054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc054.md) _ZNSt6__ndk18ios_base7failureD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e390.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f360.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb060.md#insn-00bfb074)
- 新版 [`00bfc068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc054.md#insn-00bfc068)

~~~diff
- 00bfb074 ["INT_ADD", "register:40f0:8", ["const:bfb074:8", "const:4:8"]]
- 00bfb074 ["CALL", null, ["callee:00c5f360:8"]]
+ 00bfc068 ["INT_ADD", "register:40f0:8", ["const:bfc068:8", "const:4:8"]]
+ 00bfc068 ["CALL", null, ["callee:00c5f360:8"]]
- 00bfb074 bytes c78c0194
+ 00bfc068 bytes be8c0194
~~~


<a id="compare-3adf1e495cc466694049eedcffa60fc1"></a>

### [`00bfb08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb08c.md) → [`00bfc080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc080.md) _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5f370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f370.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb08c.md#insn-00bfb0cc)
- 新版 [`00bfc0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc080.md#insn-00bfc0c0)

~~~diff
- 00bfb0cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfb0cc ["INT_ADD", "register:40f0:8", ["const:bfb0cc:8", "const:4:8"]]
- 00bfb0cc ["CALLIND", null, ["register:0:8"]]
+ 00bfc0c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc0c0 ["INT_ADD", "register:40f0:8", ["const:bfc0c0:8", "const:4:8"]]
+ 00bfc0c0 ["CALLIND", null, ["register:0:8"]]
- 00bfb0cc bytes 00013fd6
+ 00bfc0c0 bytes 00013fd6
~~~


<a id="compare-8580da0389372eba280e473a9930ae4e"></a>

### [`00bfb0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb0f0.md) → [`00bfc0e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc0e4.md) _ZNSt6__ndk18ios_base5imbueERKNS_6localeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb0f0.md#insn-00bfb118) · [`00bfb124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb0f0.md#insn-00bfb124) · [`00bfb148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb0f0.md#insn-00bfb148)
- 新版 [`00bfc10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc0e4.md#insn-00bfc10c) · [`00bfc118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc0e4.md#insn-00bfc118) · [`00bfc13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc0e4.md#insn-00bfc13c)

~~~diff
- 00bfb118 ["INT_ADD", "register:40f0:8", ["const:bfb118:8", "const:4:8"]]
- 00bfb118 ["CALL", null, ["callee:00c5b870:8"]]
+ 00bfc10c ["INT_ADD", "register:40f0:8", ["const:bfc10c:8", "const:4:8"]]
+ 00bfc10c ["CALL", null, ["callee:00c5b870:8"]]
- 00bfb118 bytes e27d0194
+ 00bfc10c bytes d97d0194
- 00bfb124 ["INT_ADD", "register:40f0:8", ["const:bfb124:8", "const:4:8"]]
- 00bfb124 ["CALL", null, ["callee:00c5f380:8"]]
+ 00bfc118 ["INT_ADD", "register:40f0:8", ["const:bfc118:8", "const:4:8"]]
+ 00bfc118 ["CALL", null, ["callee:00c5f380:8"]]
- 00bfb124 bytes a38c0194
+ 00bfc118 bytes 9a8c0194
- 00bfb148 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfb148 ["INT_ADD", "register:40f0:8", ["const:bfb148:8", "const:4:8"]]
- 00bfb148 ["CALLIND", null, ["register:0:8"]]
+ 00bfc13c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc13c ["INT_ADD", "register:40f0:8", ["const:bfc13c:8", "const:4:8"]]
+ 00bfc13c ["CALLIND", null, ["register:0:8"]]
- 00bfb148 bytes 00013fd6
+ 00bfc13c bytes 00013fd6
~~~


<a id="compare-eb7a082ddf8630be7363ebd762965afb"></a>

### [`00bfb574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb574.md) → [`00bfc568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc568.md) _ZNSt6__ndk18ios_baseD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb574.md#insn-00bfb588)
- 新版 [`00bfc57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc568.md#insn-00bfc57c)

~~~diff
- 00bfb588 ["INT_ADD", "register:40f0:8", ["const:bfb588:8", "const:4:8"]]
- 00bfb588 ["CALL", null, ["callee:00c5f390:8"]]
+ 00bfc57c ["INT_ADD", "register:40f0:8", ["const:bfc57c:8", "const:4:8"]]
+ 00bfc57c ["CALL", null, ["callee:00c5f390:8"]]
- 00bfb588 bytes 8e8b0194
+ 00bfc57c bytes 858b0194
~~~


<a id="compare-bbf569e92eb392cead5468cd2aec41b6"></a>

### [`00bfb6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb6cc.md) → [`00bfc6c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc6c0.md) _ZNSt6__ndk18ios_base7copyfmtERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3e0.md) · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 1件 [`00c5f3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3b0.md) · 呼出先 5件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f020.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb6cc.md#insn-00bfb700) · [`00bfb710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb6cc.md#insn-00bfb710) · [`00bfb73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb6cc.md#insn-00bfb73c)
- 新版 [`00bfc6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc6c0.md#insn-00bfc6f4) · [`00bfc704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc6c0.md#insn-00bfc704) · [`00bfc730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc6c0.md#insn-00bfc730)

~~~diff
- 00bfb700 ["INT_ADD", "register:40f0:8", ["const:bfb700:8", "const:4:8"]]
- 00bfb700 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00bfc6f4 ["INT_ADD", "register:40f0:8", ["const:bfc6f4:8", "const:4:8"]]
+ 00bfc6f4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00bfb700 bytes 7c7a0194
+ 00bfc6f4 bytes 737a0194
- 00bfb710 ["INT_ADD", "register:40f0:8", ["const:bfb710:8", "const:4:8"]]
- 00bfb710 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00bfc704 ["INT_ADD", "register:40f0:8", ["const:bfc704:8", "const:4:8"]]
+ 00bfc704 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00bfb710 bytes 787a0194
+ 00bfc704 bytes 6f7a0194
- 00bfb73c ["INT_ADD", "register:40f0:8", ["const:bfb73c:8", "const:4:8"]]
- 00bfb73c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00bfc730 ["INT_ADD", "register:40f0:8", ["const:bfc730:8", "const:4:8"]]
+ 00bfc730 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00bfb73c bytes 6d7a0194
+ 00bfc730 bytes 647a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f360f72306e4a2a1d8741140906e40cc"></a>

### [`00bfb98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb98c.md) → [`00bfc980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc980.md) _ZNSt6__ndk18ios_base4moveERS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfb9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb98c.md#insn-00bfb9c8)
- 新版 [`00bfc9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc980.md#insn-00bfc9bc)

~~~diff
- 00bfb9c8 ["INT_ADD", "register:40f0:8", ["const:bfb9c8:8", "const:4:8"]]
- 00bfb9c8 ["CALL", null, ["callee:00c5b870:8"]]
+ 00bfc9bc ["INT_ADD", "register:40f0:8", ["const:bfc9bc:8", "const:4:8"]]
+ 00bfc9bc ["CALL", null, ["callee:00c5b870:8"]]
- 00bfb9c8 bytes b67b0194
+ 00bfc9bc bytes ad7b0194
~~~


<a id="compare-0d4204ed8efc93c8f13130a82d68aebd"></a>

### [`00bfba28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfba28.md) → [`00bfca1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfca1c.md) _ZNSt6__ndk18ios_base4swapERS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 1件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md) · 呼出先 3件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfba9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfba28.md#insn-00bfba9c) · [`00bfbaa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfba28.md#insn-00bfbaa8) · [`00bfbab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfba28.md#insn-00bfbab4)
- 新版 [`00bfca90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfca1c.md#insn-00bfca90) · [`00bfca9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfca1c.md#insn-00bfca9c) · [`00bfcaa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfca1c.md#insn-00bfcaa8)

~~~diff
- 00bfba9c ["INT_ADD", "register:40f0:8", ["const:bfba9c:8", "const:4:8"]]
- 00bfba9c ["CALL", null, ["callee:00c5b870:8"]]
+ 00bfca90 ["INT_ADD", "register:40f0:8", ["const:bfca90:8", "const:4:8"]]
+ 00bfca90 ["CALL", null, ["callee:00c5b870:8"]]
- 00bfba9c bytes 817b0194
+ 00bfca90 bytes 787b0194
- 00bfbaa8 ["INT_ADD", "register:40f0:8", ["const:bfbaa8:8", "const:4:8"]]
- 00bfbaa8 ["CALL", null, ["callee:00c5f380:8"]]
+ 00bfca9c ["INT_ADD", "register:40f0:8", ["const:bfca9c:8", "const:4:8"]]
+ 00bfca9c ["CALL", null, ["callee:00c5f380:8"]]
- 00bfbaa8 bytes 428a0194
+ 00bfca9c bytes 398a0194
- 00bfbab4 ["INT_ADD", "register:40f0:8", ["const:bfbab4:8", "const:4:8"]]
- 00bfbab4 ["CALL", null, ["callee:00c5f380:8"]]
+ 00bfcaa8 ["INT_ADD", "register:40f0:8", ["const:bfcaa8:8", "const:4:8"]]
+ 00bfcaa8 ["CALL", null, ["callee:00c5f380:8"]]
- 00bfbab4 bytes 3f8a0194
+ 00bfcaa8 bytes 368a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec0de9731e4144af13e43dfff6e00a0a"></a>

### [`00bfbb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb44.md) → [`00bfcb38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcb38.md) _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58390.md) · 呼出先 1件 [`00c585d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585d0.md)
- 新版 呼出元 1件 [`00c59360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59360.md) · 呼出先 1件 [`00c595a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb44.md#insn-00bfbb6c)
- 新版 [`00bfcb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcb38.md#insn-00bfcb60)

~~~diff
- 00bfbb6c ["INT_ADD", "register:40f0:8", ["const:bfbb6c:8", "const:4:8"]]
- 00bfbb6c ["CALL", null, ["callee:00c595a0:8"]]
+ 00bfcb60 ["INT_ADD", "register:40f0:8", ["const:bfcb60:8", "const:4:8"]]
+ 00bfcb60 ["CALL", null, ["callee:00c595a0:8"]]
- 00bfbb6c bytes 99720194
+ 00bfcb60 bytes 90720194
~~~


<a id="compare-24992a96f221b05ba89f7d2f9252984f"></a>

### [`00bfbb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb70.md) → [`00bfcb64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcb64.md) _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e400.md) · 呼出先 1件 [`00c585d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585d0.md)
- 新版 呼出元 1件 [`00c5f3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3d0.md) · 呼出先 1件 [`00c595a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbb98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb70.md#insn-00bfbb98)
- 新版 [`00bfcb8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcb64.md#insn-00bfcb8c)

~~~diff
- 00bfbb98 ["INT_ADD", "register:40f0:8", ["const:bfbb98:8", "const:4:8"]]
- 00bfbb98 ["CALL", null, ["callee:00c595a0:8"]]
+ 00bfcb8c ["INT_ADD", "register:40f0:8", ["const:bfcb8c:8", "const:4:8"]]
+ 00bfcb8c ["CALL", null, ["callee:00c595a0:8"]]
- 00bfbb98 bytes 8e720194
+ 00bfcb8c bytes 85720194
~~~


<a id="compare-95f4f70f26357a00ea285cb255b70770"></a>

### [`00bfbbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbb8.md) → [`00bfcbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcbac.md) FUN_00bfcbac

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbb8.md#insn-00bfbbcc)
- 新版 [`00bfcbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcbac.md#insn-00bfcbc0)

~~~diff
- 00bfbbcc ["INT_ADD", "register:40f0:8", ["const:bfbbcc:8", "const:4:8"]]
- 00bfbbcc ["CALL", null, ["callee:00c5ef90:8"]]
+ 00bfcbc0 ["INT_ADD", "register:40f0:8", ["const:bfcbc0:8", "const:4:8"]]
+ 00bfcbc0 ["CALL", null, ["callee:00c5ef90:8"]]
- 00bfbbcc bytes fd880194
+ 00bfcbc0 bytes f4880194
~~~


<a id="compare-81f8c58ae8e46beb16079a078d600e9d"></a>

### [`00bfbbec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbec.md) → [`00bfcbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcbe0.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e410.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbec.md#insn-00bfbc00)
- 新版 [`00bfcbf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcbe0.md#insn-00bfcbf4)

~~~diff
- 00bfbc00 ["INT_ADD", "register:40f0:8", ["const:bfbc00:8", "const:4:8"]]
- 00bfbc00 ["CALL", null, ["callee:00c5f3e0:8"]]
+ 00bfcbf4 ["INT_ADD", "register:40f0:8", ["const:bfcbf4:8", "const:4:8"]]
+ 00bfcbf4 ["CALL", null, ["callee:00c5f3e0:8"]]
- 00bfbc00 bytes 048a0194
+ 00bfcbf4 bytes fb890194
~~~


<a id="compare-5628f74b0d60089859e9d3af85444e34"></a>

### [`00bfbc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbc18.md) → [`00bfcc0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcc0c.md) _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3a0.md) [`00c5e3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f370.md) [`00c5f3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbc18.md#insn-00bfbc40) · [`00bfbc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbc18.md#insn-00bfbc4c) · [`00bfbc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbc18.md#insn-00bfbc68)
- 新版 [`00bfcc34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcc0c.md#insn-00bfcc34) · [`00bfcc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcc0c.md#insn-00bfcc40) · [`00bfcc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcc0c.md#insn-00bfcc5c)

~~~diff
- 00bfbc40 ["INT_ADD", "register:40f0:8", ["const:bfbc40:8", "const:4:8"]]
- 00bfbc40 ["CALL", null, ["callee:00c5f370:8"]]
+ 00bfcc34 ["INT_ADD", "register:40f0:8", ["const:bfcc34:8", "const:4:8"]]
+ 00bfcc34 ["CALL", null, ["callee:00c5f370:8"]]
- 00bfbc40 bytes d8890194
+ 00bfcc34 bytes cf890194
- 00bfbc4c ["INT_ADD", "register:40f0:8", ["const:bfbc4c:8", "const:4:8"]]
- 00bfbc4c ["CALL", null, ["callee:00c5f3b0:8"]]
+ 00bfcc40 ["INT_ADD", "register:40f0:8", ["const:bfcc40:8", "const:4:8"]]
+ 00bfcc40 ["CALL", null, ["callee:00c5f3b0:8"]]
- 00bfbc4c bytes e5890194
+ 00bfcc40 bytes dc890194
- 00bfbc68 ["INT_ADD", "register:40f0:8", ["const:bfbc68:8", "const:4:8"]]
- 00bfbc68 ["CALL", null, ["callee:00c5f370:8"]]
+ 00bfcc5c ["INT_ADD", "register:40f0:8", ["const:bfcc5c:8", "const:4:8"]]
+ 00bfcc5c ["CALL", null, ["callee:00c5f370:8"]]
- 00bfbc68 bytes ce890194
+ 00bfcc5c bytes c5890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfdfa1b7f3fc6d4879bbadbe7bf3a292"></a>

### [`00bfbcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcac.md) → [`00bfcca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcca0.md) FUN_00bfcca0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcac.md#insn-00bfbcc0)
- 新版 [`00bfccb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcca0.md#insn-00bfccb4)

~~~diff
- 00bfbcc0 ["INT_ADD", "register:40f0:8", ["const:bfbcc0:8", "const:4:8"]]
- 00bfbcc0 ["CALL", null, ["callee:00c5f3f0:8"]]
+ 00bfccb4 ["INT_ADD", "register:40f0:8", ["const:bfccb4:8", "const:4:8"]]
+ 00bfccb4 ["CALL", null, ["callee:00c5f3f0:8"]]
- 00bfbcc0 bytes d8890194
+ 00bfccb4 bytes cf890194
~~~


<a id="compare-c0e5070f215241102472a66c04e0049f"></a>

### [`00bfbcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcd8.md) → [`00bfcccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcccc.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcd8.md#insn-00bfbd00) · [`00bfbd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcd8.md#insn-00bfbd0c)
- 新版 [`00bfccf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcccc.md#insn-00bfccf4) · [`00bfcd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcccc.md#insn-00bfcd00)

~~~diff
- 00bfbd00 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bfbd00 ["INT_ADD", "register:40f0:8", ["const:bfbd00:8", "const:4:8"]]
- 00bfbd00 ["CALLIND", null, ["register:0:8"]]
+ 00bfccf4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bfccf4 ["INT_ADD", "register:40f0:8", ["const:bfccf4:8", "const:4:8"]]
+ 00bfccf4 ["CALLIND", null, ["register:0:8"]]
- 00bfbd00 bytes 20013fd6
+ 00bfccf4 bytes 20013fd6
- 00bfbd0c ["INT_ADD", "register:40f0:8", ["const:bfbd0c:8", "const:4:8"]]
- 00bfbd0c ["CALL", null, ["callee:00c5b870:8"]]
+ 00bfcd00 ["INT_ADD", "register:40f0:8", ["const:bfcd00:8", "const:4:8"]]
+ 00bfcd00 ["CALL", null, ["callee:00c5b870:8"]]
- 00bfbd0c bytes e57a0194
+ 00bfcd00 bytes dc7a0194
~~~


<a id="compare-73e7e2afa4e92a4181ec0a119faa6062"></a>

### [`00bfbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbda0.md) → [`00bfcd94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcd94.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbda0.md#insn-00bfbde0)
- 新版 [`00bfcdd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcd94.md#insn-00bfcdd4)

~~~diff
- 00bfbde0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfbde0 ["INT_ADD", "register:40f0:8", ["const:bfbde0:8", "const:4:8"]]
- 00bfbde0 ["CALLIND", null, ["register:0:8"]]
+ 00bfcdd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfcdd4 ["INT_ADD", "register:40f0:8", ["const:bfcdd4:8", "const:4:8"]]
+ 00bfcdd4 ["CALLIND", null, ["register:0:8"]]
- 00bfbde0 bytes 00013fd6
+ 00bfcdd4 bytes 00013fd6
~~~


<a id="compare-eda56d0b1c394a09d6471b3212c72753"></a>

### [`00bfbfd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbfd4.md) → [`00bfcfc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcfc8.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfbff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbfd4.md#insn-00bfbff4)
- 新版 [`00bfcfe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcfc8.md#insn-00bfcfe8)

~~~diff
- 00bfbff4 ["INT_ADD", "register:40f0:8", ["const:bfbff4:8", "const:4:8"]]
- 00bfbff4 ["CALL", null, ["callee:00c5f380:8"]]
+ 00bfcfe8 ["INT_ADD", "register:40f0:8", ["const:bfcfe8:8", "const:4:8"]]
+ 00bfcfe8 ["CALL", null, ["callee:00c5f380:8"]]
- 00bfbff4 bytes ef880194
+ 00bfcfe8 bytes e6880194
~~~


<a id="compare-fd77823b91897b72810b32b37951e610"></a>

### [`00bfc024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc024.md) → [`00bfd018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd018.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc024.md#insn-00bfc048) · [`00bfc054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc024.md#insn-00bfc054) · [`00bfc060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc024.md#insn-00bfc060)
- 新版 [`00bfd03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd018.md#insn-00bfd03c) · [`00bfd048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd018.md#insn-00bfd048) · [`00bfd054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd018.md#insn-00bfd054)

~~~diff
- 00bfc048 ["INT_ADD", "register:40f0:8", ["const:bfc048:8", "const:4:8"]]
- 00bfc048 ["CALL", null, ["callee:00c5b870:8"]]
+ 00bfd03c ["INT_ADD", "register:40f0:8", ["const:bfd03c:8", "const:4:8"]]
+ 00bfd03c ["CALL", null, ["callee:00c5b870:8"]]
- 00bfc048 bytes 167a0194
+ 00bfd03c bytes 0d7a0194
- 00bfc054 ["INT_ADD", "register:40f0:8", ["const:bfc054:8", "const:4:8"]]
- 00bfc054 ["CALL", null, ["callee:00c5f380:8"]]
+ 00bfd048 ["INT_ADD", "register:40f0:8", ["const:bfd048:8", "const:4:8"]]
+ 00bfd048 ["CALL", null, ["callee:00c5f380:8"]]
- 00bfc054 bytes d7880194
+ 00bfd048 bytes ce880194
- 00bfc060 ["INT_ADD", "register:40f0:8", ["const:bfc060:8", "const:4:8"]]
- 00bfc060 ["CALL", null, ["callee:00c5f380:8"]]
+ 00bfd054 ["INT_ADD", "register:40f0:8", ["const:bfd054:8", "const:4:8"]]
+ 00bfd054 ["CALL", null, ["callee:00c5f380:8"]]
- 00bfc060 bytes d4880194
+ 00bfd054 bytes cb880194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc6321447986a1fec77cbacf1cc032c"></a>

### [`00bfc128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc128.md) → [`00bfd11c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd11c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc128.md#insn-00bfc164)
- 新版 [`00bfd158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd11c.md#insn-00bfd158)

~~~diff
- 00bfc164 ["INT_ADD", "register:40f0:8", ["const:bfc164:8", "const:4:8"]]
- 00bfc164 ["CALL", null, ["callee:00c59280:8"]]
+ 00bfd158 ["INT_ADD", "register:40f0:8", ["const:bfd158:8", "const:4:8"]]
+ 00bfd158 ["CALL", null, ["callee:00c59280:8"]]
- 00bfc164 bytes 53700194
+ 00bfd158 bytes 4a700194
~~~


<a id="compare-b9b90f8b13937303981666c31fd8b449"></a>

### [`00bfc1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc1f8.md) → [`00bfd1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd1ec.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc1f8.md#insn-00bfc230)
- 新版 [`00bfd224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd1ec.md#insn-00bfd224)

~~~diff
- 00bfc230 ["INT_ADD", "register:40f0:8", ["const:bfc230:8", "const:4:8"]]
- 00bfc230 ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00bfd224 ["INT_ADD", "register:40f0:8", ["const:bfd224:8", "const:4:8"]]
+ 00bfd224 ["CALL", null, ["callee:00c5f3c0:8"]]
- 00bfc230 bytes 70880194
+ 00bfd224 bytes 67880194
~~~


<a id="compare-db820031eed27c8bb60d0dfdd75663d2"></a>

### [`00bfc448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc448.md) → [`00bfd43c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd43c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc448.md#insn-00bfc468)
- 新版 [`00bfd45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd43c.md#insn-00bfd45c)

~~~diff
- 00bfc468 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfc468 ["INT_ADD", "register:40f0:8", ["const:bfc468:8", "const:4:8"]]
- 00bfc468 ["CALLIND", null, ["register:0:8"]]
+ 00bfd45c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfd45c ["INT_ADD", "register:40f0:8", ["const:bfd45c:8", "const:4:8"]]
+ 00bfd45c ["CALLIND", null, ["register:0:8"]]
- 00bfc468 bytes 20003fd6
+ 00bfd45c bytes 20003fd6
~~~


<a id="compare-552faa50bb76629abcc3c3728de71a66"></a>

### [`00bfc480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc480.md) → [`00bfd474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd474.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc480.md#insn-00bfc4a0)
- 新版 [`00bfd494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd474.md#insn-00bfd494)

~~~diff
- 00bfc4a0 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfc4a0 ["INT_ADD", "register:40f0:8", ["const:bfc4a0:8", "const:4:8"]]
- 00bfc4a0 ["CALLIND", null, ["register:0:8"]]
+ 00bfd494 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bfd494 ["INT_ADD", "register:40f0:8", ["const:bfd494:8", "const:4:8"]]
+ 00bfd494 ["CALLIND", null, ["register:0:8"]]
- 00bfc4a0 bytes 20003fd6
+ 00bfd494 bytes 20003fd6
~~~


<a id="compare-5b81c4737a5b7f4b200f6bb4b1bde60f"></a>

### [`00bfc4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc4b8.md) → [`00bfd4ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd4ac.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfc4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc4b8.md#insn-00bfc4e8) · [`00bfc54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc4b8.md#insn-00bfc54c) · [`00bfc584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc4b8.md#insn-00bfc584)
- 新版 [`00bfd4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd4ac.md#insn-00bfd4dc) · [`00bfd540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd4ac.md#insn-00bfd540) · [`00bfd578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd4ac.md#insn-00bfd578)

~~~diff
- 00bfc4e8 ["INT_ADD", "register:40f0:8", ["const:bfc4e8:8", "const:4:8"]]
- 00bfc4e8 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bfd4dc ["INT_ADD", "register:40f0:8", ["const:bfd4dc:8", "const:4:8"]]
+ 00bfd4dc ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfc4e8 bytes 6e760194
+ 00bfd4dc bytes 65760194
- 00bfc54c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfc54c ["INT_ADD", "register:40f0:8", ["const:bfc54c:8", "const:4:8"]]
- 00bfc54c ["CALLIND", null, ["register:0:8"]]
+ 00bfd540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd540 ["INT_ADD", "register:40f0:8", ["const:bfd540:8", "const:4:8"]]
+ 00bfd540 ["CALLIND", null, ["register:0:8"]]
- 00bfc54c bytes 00013fd6
+ 00bfd540 bytes 00013fd6
- 00bfc584 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfc584 ["INT_ADD", "register:40f0:8", ["const:bfc584:8", "const:4:8"]]
- 00bfc584 ["CALLIND", null, ["register:0:8"]]
+ 00bfd578 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd578 ["INT_ADD", "register:40f0:8", ["const:bfd578:8", "const:4:8"]]
+ 00bfd578 ["CALLIND", null, ["register:0:8"]]
- 00bfc584 bytes 00013fd6
+ 00bfd578 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e9d0da3a4dfa7175a8e7cd0f1d7b8f1"></a>

### [`00bfd6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd6c8.md) → [`00bfe6bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe6bc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e430.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00c5f400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f400.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd6c8.md#insn-00bfd6f0) · [`00bfd738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd6c8.md#insn-00bfd738) · [`00bfd768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd6c8.md#insn-00bfd768)
- 新版 [`00bfe6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe6bc.md#insn-00bfe6e4) · [`00bfe72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe6bc.md#insn-00bfe72c) · [`00bfe75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe6bc.md#insn-00bfe75c)

~~~diff
- 00bfd6f0 ["INT_ADD", "register:40f0:8", ["const:bfd6f0:8", "const:4:8"]]
- 00bfd6f0 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bfe6e4 ["INT_ADD", "register:40f0:8", ["const:bfe6e4:8", "const:4:8"]]
+ 00bfe6e4 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfd6f0 bytes ec710194
+ 00bfe6e4 bytes e3710194
- 00bfd738 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd738 ["INT_ADD", "register:40f0:8", ["const:bfd738:8", "const:4:8"]]
- 00bfd738 ["CALLIND", null, ["register:0:8"]]
+ 00bfe72c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe72c ["INT_ADD", "register:40f0:8", ["const:bfe72c:8", "const:4:8"]]
+ 00bfe72c ["CALLIND", null, ["register:0:8"]]
- 00bfd738 bytes 00013fd6
+ 00bfe72c bytes 00013fd6
- 00bfd768 ["INT_ADD", "register:40f0:8", ["const:bfd768:8", "const:4:8"]]
- 00bfd768 ["CALL", null, ["callee:00c59340:8"]]
+ 00bfe75c ["INT_ADD", "register:40f0:8", ["const:bfe75c:8", "const:4:8"]]
+ 00bfe75c ["CALL", null, ["callee:00c59340:8"]]
- 00bfd768 bytes 026b0194
+ 00bfe75c bytes f96a0194
~~~


<a id="compare-88584bc7f43c0cdb123b8258a68748c7"></a>

### [`00bfd7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd7e0.md) → [`00bfe7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe7d4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e430.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd7e0.md#insn-00bfd7f8)
- 新版 [`00bfe7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe7d4.md#insn-00bfe7ec)

~~~diff
- 00bfd7f8 ["INT_ADD", "register:40f0:8", ["const:bfd7f8:8", "const:4:8"]]
- 00bfd7f8 ["CALL", null, ["callee:00c5f400:8"]]
+ 00bfe7ec ["INT_ADD", "register:40f0:8", ["const:bfe7ec:8", "const:4:8"]]
+ 00bfe7ec ["CALL", null, ["callee:00c5f400:8"]]
- 00bfd7f8 bytes 0e830194
+ 00bfe7ec bytes 05830194
~~~


<a id="compare-2537a0a7e123b5a24ecc4e5cd8584246"></a>

### [`00bfd8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd8c0.md) → [`00bfe8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe8b4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e440.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00c5f410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f410.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfd8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd8c0.md#insn-00bfd8fc) · [`00bfd978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd8c0.md#insn-00bfd978) · [`00bfd9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd8c0.md#insn-00bfd9b8)
- 新版 [`00bfe8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe8b4.md#insn-00bfe8f0) · [`00bfe96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe8b4.md#insn-00bfe96c) · [`00bfe9ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfe8b4.md#insn-00bfe9ac)

~~~diff
- 00bfd8fc ["INT_ADD", "register:40f0:8", ["const:bfd8fc:8", "const:4:8"]]
- 00bfd8fc ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bfe8f0 ["INT_ADD", "register:40f0:8", ["const:bfe8f0:8", "const:4:8"]]
+ 00bfe8f0 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfd8fc bytes 69710194
+ 00bfe8f0 bytes 60710194
- 00bfd978 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd978 ["INT_ADD", "register:40f0:8", ["const:bfd978:8", "const:4:8"]]
- 00bfd978 ["CALLIND", null, ["register:0:8"]]
+ 00bfe96c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe96c ["INT_ADD", "register:40f0:8", ["const:bfe96c:8", "const:4:8"]]
+ 00bfe96c ["CALLIND", null, ["register:0:8"]]
- 00bfd978 bytes 00013fd6
+ 00bfe96c bytes 00013fd6
- 00bfd9b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfd9b8 ["INT_ADD", "register:40f0:8", ["const:bfd9b8:8", "const:4:8"]]
- 00bfd9b8 ["CALLIND", null, ["register:0:8"]]
+ 00bfe9ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfe9ac ["INT_ADD", "register:40f0:8", ["const:bfe9ac:8", "const:4:8"]]
+ 00bfe9ac ["CALLIND", null, ["register:0:8"]]
- 00bfd9b8 bytes 00013fd6
+ 00bfe9ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9806d80f0f46720ca01727245bc2ea35"></a>

### [`00bfdb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdb28.md) → [`00bfeb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfeb1c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e450.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00c5f420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f420.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdb28.md#insn-00bfdb5c) · [`00bfdbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdb28.md#insn-00bfdbc0) · [`00bfdc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdb28.md#insn-00bfdc04)
- 新版 [`00bfeb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfeb1c.md#insn-00bfeb50) · [`00bfebb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfeb1c.md#insn-00bfebb4) · [`00bfebf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfeb1c.md#insn-00bfebf8)

~~~diff
- 00bfdb5c ["INT_ADD", "register:40f0:8", ["const:bfdb5c:8", "const:4:8"]]
- 00bfdb5c ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bfeb50 ["INT_ADD", "register:40f0:8", ["const:bfeb50:8", "const:4:8"]]
+ 00bfeb50 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfdb5c bytes d1700194
+ 00bfeb50 bytes c8700194
- 00bfdbc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdbc0 ["INT_ADD", "register:40f0:8", ["const:bfdbc0:8", "const:4:8"]]
- 00bfdbc0 ["CALLIND", null, ["register:0:8"]]
+ 00bfebb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfebb4 ["INT_ADD", "register:40f0:8", ["const:bfebb4:8", "const:4:8"]]
+ 00bfebb4 ["CALLIND", null, ["register:0:8"]]
- 00bfdbc0 bytes 00013fd6
+ 00bfebb4 bytes 00013fd6
- 00bfdc04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfdc04 ["INT_ADD", "register:40f0:8", ["const:bfdc04:8", "const:4:8"]]
- 00bfdc04 ["CALLIND", null, ["register:0:8"]]
+ 00bfebf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfebf8 ["INT_ADD", "register:40f0:8", ["const:bfebf8:8", "const:4:8"]]
+ 00bfebf8 ["CALLIND", null, ["register:0:8"]]
- 00bfdc04 bytes 00013fd6
+ 00bfebf8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0d26b4f0776e547803ad8439c34551"></a>

### [`00bfdd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdd3c.md) → [`00bfed30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfed30.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e460.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00c5f430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f430.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdd7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdd3c.md#insn-00bfdd7c) · [`00bfddc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdd3c.md#insn-00bfddc0) · [`00bfde18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdd3c.md#insn-00bfde18)
- 新版 [`00bfed70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfed30.md#insn-00bfed70) · [`00bfedb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfed30.md#insn-00bfedb4) · [`00bfee0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfed30.md#insn-00bfee0c)

~~~diff
- 00bfdd7c ["INT_ADD", "register:40f0:8", ["const:bfdd7c:8", "const:4:8"]]
- 00bfdd7c ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bfed70 ["INT_ADD", "register:40f0:8", ["const:bfed70:8", "const:4:8"]]
+ 00bfed70 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfdd7c bytes 49700194
+ 00bfed70 bytes 40700194
- 00bfddc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfddc0 ["INT_ADD", "register:40f0:8", ["const:bfddc0:8", "const:4:8"]]
- 00bfddc0 ["CALLIND", null, ["register:0:8"]]
+ 00bfedb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfedb4 ["INT_ADD", "register:40f0:8", ["const:bfedb4:8", "const:4:8"]]
+ 00bfedb4 ["CALLIND", null, ["register:0:8"]]
- 00bfddc0 bytes 00013fd6
+ 00bfedb4 bytes 00013fd6
- 00bfde18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfde18 ["INT_ADD", "register:40f0:8", ["const:bfde18:8", "const:4:8"]]
- 00bfde18 ["CALLIND", null, ["register:0:8"]]
+ 00bfee0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfee0c ["INT_ADD", "register:40f0:8", ["const:bfee0c:8", "const:4:8"]]
+ 00bfee0c ["CALLIND", null, ["register:0:8"]]
- 00bfde18 bytes 00013fd6
+ 00bfee0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-239c132c8a6e70cf9e0f3607f59f5ffd"></a>

### [`00bfdf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdf80.md) → [`00bfef74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfef74.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfdfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdf80.md#insn-00bfdfb4) · [`00bfe00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdf80.md#insn-00bfe00c) · [`00bfe088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdf80.md#insn-00bfe088)
- 新版 [`00bfefa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfef74.md#insn-00bfefa8) · [`00bff000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfef74.md#insn-00bff000) · [`00bff07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfef74.md#insn-00bff07c)

~~~diff
- 00bfdfb4 ["INT_ADD", "register:40f0:8", ["const:bfdfb4:8", "const:4:8"]]
- 00bfdfb4 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bfefa8 ["INT_ADD", "register:40f0:8", ["const:bfefa8:8", "const:4:8"]]
+ 00bfefa8 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfdfb4 bytes bb6f0194
+ 00bfefa8 bytes b26f0194
- 00bfe00c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe00c ["INT_ADD", "register:40f0:8", ["const:bfe00c:8", "const:4:8"]]
- 00bfe00c ["CALLIND", null, ["register:0:8"]]
+ 00bff000 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff000 ["INT_ADD", "register:40f0:8", ["const:bff000:8", "const:4:8"]]
+ 00bff000 ["CALLIND", null, ["register:0:8"]]
- 00bfe00c bytes 00013fd6
+ 00bff000 bytes 00013fd6
- 00bfe088 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe088 ["INT_ADD", "register:40f0:8", ["const:bfe088:8", "const:4:8"]]
- 00bfe088 ["CALLIND", null, ["register:0:8"]]
+ 00bff07c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff07c ["INT_ADD", "register:40f0:8", ["const:bff07c:8", "const:4:8"]]
+ 00bff07c ["CALLIND", null, ["register:0:8"]]
- 00bfe088 bytes 00013fd6
+ 00bff07c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faa2e768ae1733f22ff20ed19d162632"></a>

### [`00bfe13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe13c.md) → [`00bff130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff130.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4peekEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe13c.md#insn-00bfe164) · [`00bfe1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe13c.md#insn-00bfe1a4) · [`00bfe1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe13c.md#insn-00bfe1cc)
- 新版 [`00bff158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff130.md#insn-00bff158) · [`00bff198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff130.md#insn-00bff198) · [`00bff1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff130.md#insn-00bff1c0)

~~~diff
- 00bfe164 ["INT_ADD", "register:40f0:8", ["const:bfe164:8", "const:4:8"]]
- 00bfe164 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bff158 ["INT_ADD", "register:40f0:8", ["const:bff158:8", "const:4:8"]]
+ 00bff158 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfe164 bytes 4f6f0194
+ 00bff158 bytes 466f0194
- 00bfe1a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe1a4 ["INT_ADD", "register:40f0:8", ["const:bfe1a4:8", "const:4:8"]]
- 00bfe1a4 ["CALLIND", null, ["register:0:8"]]
+ 00bff198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff198 ["INT_ADD", "register:40f0:8", ["const:bff198:8", "const:4:8"]]
+ 00bff198 ["CALLIND", null, ["register:0:8"]]
- 00bfe1a4 bytes 00013fd6
+ 00bff198 bytes 00013fd6
- 00bfe1cc ["INT_ADD", "register:40f0:8", ["const:bfe1cc:8", "const:4:8"]]
- 00bfe1cc ["CALL", null, ["callee:00c59340:8"]]
+ 00bff1c0 ["INT_ADD", "register:40f0:8", ["const:bff1c0:8", "const:4:8"]]
+ 00bff1c0 ["CALL", null, ["callee:00c59340:8"]]
- 00bfe1cc bytes 69680194
+ 00bff1c0 bytes 60680194
~~~


<a id="compare-24618cd2f601a79c1866e225d3ea4766"></a>

### [`00bfe23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe23c.md) → [`00bff230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff230.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4readEPcl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c591a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591a0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00c5a170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a170.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe23c.md#insn-00bfe26c) · [`00bfe298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe23c.md#insn-00bfe298) · [`00bfe2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe23c.md#insn-00bfe2c8)
- 新版 [`00bff260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff230.md#insn-00bff260) · [`00bff28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff230.md#insn-00bff28c) · [`00bff2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff230.md#insn-00bff2bc)

~~~diff
- 00bfe26c ["INT_ADD", "register:40f0:8", ["const:bfe26c:8", "const:4:8"]]
- 00bfe26c ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bff260 ["INT_ADD", "register:40f0:8", ["const:bff260:8", "const:4:8"]]
+ 00bff260 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfe26c bytes 0d6f0194
+ 00bff260 bytes 046f0194
- 00bfe298 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe298 ["INT_ADD", "register:40f0:8", ["const:bfe298:8", "const:4:8"]]
- 00bfe298 ["CALLIND", null, ["register:0:8"]]
+ 00bff28c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff28c ["INT_ADD", "register:40f0:8", ["const:bff28c:8", "const:4:8"]]
+ 00bff28c ["CALLIND", null, ["register:0:8"]]
- 00bfe298 bytes 00013fd6
+ 00bff28c bytes 00013fd6
- 00bfe2c8 ["INT_ADD", "register:40f0:8", ["const:bfe2c8:8", "const:4:8"]]
- 00bfe2c8 ["CALL", null, ["callee:00c59340:8"]]
+ 00bff2bc ["INT_ADD", "register:40f0:8", ["const:bff2bc:8", "const:4:8"]]
+ 00bff2bc ["CALL", null, ["callee:00c59340:8"]]
- 00bfe2c8 bytes 2a680194
+ 00bff2bc bytes 21680194
~~~


<a id="compare-31635775e52b5d2f1d179508d90df565"></a>

### [`00bfe334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe334.md) → [`00bff328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff328.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE8readsomeEPcl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe334.md#insn-00bfe364) · [`00bfe3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe334.md#insn-00bfe3a4) · [`00bfe3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe334.md#insn-00bfe3f0)
- 新版 [`00bff358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff328.md#insn-00bff358) · [`00bff398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff328.md#insn-00bff398) · [`00bff3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff328.md#insn-00bff3e4)

~~~diff
- 00bfe364 ["INT_ADD", "register:40f0:8", ["const:bfe364:8", "const:4:8"]]
- 00bfe364 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bff358 ["INT_ADD", "register:40f0:8", ["const:bff358:8", "const:4:8"]]
+ 00bff358 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfe364 bytes cf6e0194
+ 00bff358 bytes c66e0194
- 00bfe3a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe3a4 ["INT_ADD", "register:40f0:8", ["const:bfe3a4:8", "const:4:8"]]
- 00bfe3a4 ["CALLIND", null, ["register:0:8"]]
+ 00bff398 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff398 ["INT_ADD", "register:40f0:8", ["const:bff398:8", "const:4:8"]]
+ 00bff398 ["CALLIND", null, ["register:0:8"]]
- 00bfe3a4 bytes 00013fd6
+ 00bff398 bytes 00013fd6
- 00bfe3f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bfe3f0 ["INT_ADD", "register:40f0:8", ["const:bfe3f0:8", "const:4:8"]]
- 00bfe3f0 ["CALLIND", null, ["register:0:8"]]
+ 00bff3e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bff3e4 ["INT_ADD", "register:40f0:8", ["const:bff3e4:8", "const:4:8"]]
+ 00bff3e4 ["CALLIND", null, ["register:0:8"]]
- 00bfe3f0 bytes 20013fd6
+ 00bff3e4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29031949b3f57b3c0a5080044afddf22"></a>

### [`00bfe484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe484.md) → [`00bff478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff478.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe484.md#insn-00bfe4c4) · [`00bfe4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe484.md#insn-00bfe4d4) · [`00bfe528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe484.md#insn-00bfe528)
- 新版 [`00bff4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff478.md#insn-00bff4b8) · [`00bff4c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff478.md#insn-00bff4c8) · [`00bff51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff478.md#insn-00bff51c)

~~~diff
- 00bfe4c4 ["INT_ADD", "register:40f0:8", ["const:bfe4c4:8", "const:4:8"]]
- 00bfe4c4 ["CALL", null, ["callee:00c59340:8"]]
+ 00bff4b8 ["INT_ADD", "register:40f0:8", ["const:bff4b8:8", "const:4:8"]]
+ 00bff4b8 ["CALL", null, ["callee:00c59340:8"]]
- 00bfe4c4 bytes ab670194
+ 00bff4b8 bytes a2670194
- 00bfe4d4 ["INT_ADD", "register:40f0:8", ["const:bfe4d4:8", "const:4:8"]]
- 00bfe4d4 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bff4c8 ["INT_ADD", "register:40f0:8", ["const:bff4c8:8", "const:4:8"]]
+ 00bff4c8 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfe4d4 bytes 736e0194
+ 00bff4c8 bytes 6a6e0194
- 00bfe528 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe528 ["INT_ADD", "register:40f0:8", ["const:bfe528:8", "const:4:8"]]
- 00bfe528 ["CALLIND", null, ["register:0:8"]]
+ 00bff51c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff51c ["INT_ADD", "register:40f0:8", ["const:bff51c:8", "const:4:8"]]
+ 00bff51c ["CALLIND", null, ["register:0:8"]]
- 00bfe528 bytes 00013fd6
+ 00bff51c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d69f8586842d39dd8997820e66ba1674"></a>

### [`00bfe5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe5b8.md) → [`00bff5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff5ac.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe5b8.md#insn-00bfe5f4) · [`00bfe604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe5b8.md#insn-00bfe604) · [`00bfe650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe5b8.md#insn-00bfe650)
- 新版 [`00bff5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff5ac.md#insn-00bff5e8) · [`00bff5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff5ac.md#insn-00bff5f8) · [`00bff644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff5ac.md#insn-00bff644)

~~~diff
- 00bfe5f4 ["INT_ADD", "register:40f0:8", ["const:bfe5f4:8", "const:4:8"]]
- 00bfe5f4 ["CALL", null, ["callee:00c59340:8"]]
+ 00bff5e8 ["INT_ADD", "register:40f0:8", ["const:bff5e8:8", "const:4:8"]]
+ 00bff5e8 ["CALL", null, ["callee:00c59340:8"]]
- 00bfe5f4 bytes 5f670194
+ 00bff5e8 bytes 56670194
- 00bfe604 ["INT_ADD", "register:40f0:8", ["const:bfe604:8", "const:4:8"]]
- 00bfe604 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bff5f8 ["INT_ADD", "register:40f0:8", ["const:bff5f8:8", "const:4:8"]]
+ 00bff5f8 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfe604 bytes 276e0194
+ 00bff5f8 bytes 1e6e0194
- 00bfe650 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe650 ["INT_ADD", "register:40f0:8", ["const:bfe650:8", "const:4:8"]]
- 00bfe650 ["CALLIND", null, ["register:0:8"]]
+ 00bff644 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff644 ["INT_ADD", "register:40f0:8", ["const:bff644:8", "const:4:8"]]
+ 00bff644 ["CALLIND", null, ["register:0:8"]]
- 00bfe650 bytes 00013fd6
+ 00bff644 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c81c081fc2a5d8339dbd3872d57d3d7"></a>

### [`00bfe6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe6e0.md) → [`00bff6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff6d4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe6e0.md#insn-00bfe704) · [`00bfe72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe6e0.md#insn-00bfe72c) · [`00bfe750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe6e0.md#insn-00bfe750)
- 新版 [`00bff6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff6d4.md#insn-00bff6f8) · [`00bff720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff6d4.md#insn-00bff720) · [`00bff744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff6d4.md#insn-00bff744)

~~~diff
- 00bfe704 ["INT_ADD", "register:40f0:8", ["const:bfe704:8", "const:4:8"]]
- 00bfe704 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bff6f8 ["INT_ADD", "register:40f0:8", ["const:bff6f8:8", "const:4:8"]]
+ 00bff6f8 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfe704 bytes e76d0194
+ 00bff6f8 bytes de6d0194
- 00bfe72c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe72c ["INT_ADD", "register:40f0:8", ["const:bfe72c:8", "const:4:8"]]
- 00bfe72c ["CALLIND", null, ["register:0:8"]]
+ 00bff720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff720 ["INT_ADD", "register:40f0:8", ["const:bff720:8", "const:4:8"]]
+ 00bff720 ["CALLIND", null, ["register:0:8"]]
- 00bfe72c bytes 00013fd6
+ 00bff720 bytes 00013fd6
- 00bfe750 ["INT_ADD", "register:40f0:8", ["const:bfe750:8", "const:4:8"]]
- 00bfe750 ["CALL", null, ["callee:00c59340:8"]]
+ 00bff744 ["INT_ADD", "register:40f0:8", ["const:bff744:8", "const:4:8"]]
+ 00bff744 ["CALL", null, ["callee:00c59340:8"]]
- 00bfe750 bytes 08670194
+ 00bff744 bytes ff660194
~~~


<a id="compare-08d1e0c316b4cb7312d7d479bc949b33"></a>

### [`00bfe7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe7d0.md) → [`00bff7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff7c4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c598d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598d0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00c5a8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a8a0.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe7d0.md#insn-00bfe80c) · [`00bfe81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe7d0.md#insn-00bfe81c) · [`00bfe84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe7d0.md#insn-00bfe84c)
- 新版 [`00bff800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff7c4.md#insn-00bff800) · [`00bff810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff7c4.md#insn-00bff810) · [`00bff840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff7c4.md#insn-00bff840)

~~~diff
- 00bfe80c ["INT_ADD", "register:40f0:8", ["const:bfe80c:8", "const:4:8"]]
- 00bfe80c ["CALL", null, ["callee:00c59340:8"]]
+ 00bff800 ["INT_ADD", "register:40f0:8", ["const:bff800:8", "const:4:8"]]
+ 00bff800 ["CALL", null, ["callee:00c59340:8"]]
- 00bfe80c bytes d9660194
+ 00bff800 bytes d0660194
- 00bfe81c ["INT_ADD", "register:40f0:8", ["const:bfe81c:8", "const:4:8"]]
- 00bfe81c ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bff810 ["INT_ADD", "register:40f0:8", ["const:bff810:8", "const:4:8"]]
+ 00bff810 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bfe81c bytes a16d0194
+ 00bff810 bytes 986d0194
- 00bfe84c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfe84c ["INT_ADD", "register:40f0:8", ["const:bfe84c:8", "const:4:8"]]
- 00bfe84c ["CALLIND", null, ["register:0:8"]]
+ 00bff840 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff840 ["INT_ADD", "register:40f0:8", ["const:bff840:8", "const:4:8"]]
+ 00bff840 ["CALLIND", null, ["register:0:8"]]
- 00bfe84c bytes 00013fd6
+ 00bff840 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c085c19f9eb9491060a3fd2559972877"></a>

### [`00bfe8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe8e0.md) → [`00bff8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff8d4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe8e0.md#insn-00bfe918)
- 新版 [`00bff90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff8d4.md#insn-00bff90c)

~~~diff
- 00bfe918 ["INT_ADD", "register:40f0:8", ["const:bfe918:8", "const:4:8"]]
- 00bfe918 ["CALL", null, ["callee:00c59280:8"]]
+ 00bff90c ["INT_ADD", "register:40f0:8", ["const:bff90c:8", "const:4:8"]]
+ 00bff90c ["CALL", null, ["callee:00c59280:8"]]
- 00bfe918 bytes 66660194
+ 00bff90c bytes 5d660194
~~~


<a id="compare-3aad40a159f1fdf987951255e39f4d67"></a>

### [`00bfe9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe9ac.md) → [`00bff9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff9a0.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfe9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe9ac.md#insn-00bfe9dc)
- 新版 [`00bff9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff9a0.md#insn-00bff9d0)

~~~diff
- 00bfe9dc ["INT_ADD", "register:40f0:8", ["const:bfe9dc:8", "const:4:8"]]
- 00bfe9dc ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00bff9d0 ["INT_ADD", "register:40f0:8", ["const:bff9d0:8", "const:4:8"]]
+ 00bff9d0 ["CALL", null, ["callee:00c5f3c0:8"]]
- 00bfe9dc bytes 857e0194
+ 00bff9d0 bytes 7c7e0194
~~~


<a id="compare-11b1cf961c50e8ed639518d4be7ba072"></a>

### [`00bfea10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea10.md) → [`00bffa04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffa04.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) · 呼出先 1件 [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md)
- 新版 呼出元 1件 [`00c59300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59300.md) · 呼出先 1件 [`00c59f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfea54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea10.md#insn-00bfea54)
- 新版 [`00bffa48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffa04.md#insn-00bffa48)

~~~diff
- 00bfea54 ["INT_ADD", "register:40f0:8", ["const:bfea54:8", "const:4:8"]]
- 00bfea54 ["CALL", null, ["callee:00c59f90:8"]]
+ 00bffa48 ["INT_ADD", "register:40f0:8", ["const:bffa48:8", "const:4:8"]]
+ 00bffa48 ["CALL", null, ["callee:00c59f90:8"]]
- 00bfea54 bytes 5b690194
+ 00bffa48 bytes 52690194
~~~


<a id="compare-0904e356e901451c8bdf0427921570a5"></a>

### [`00bfea74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea74.md) → [`00bffa68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffa68.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md)
- 新版 呼出元 1件 [`00c59350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59350.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5e190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfeab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea74.md#insn-00bfeab0) · [`00bfead4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea74.md#insn-00bfead4) · [`00bfeaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfea74.md#insn-00bfeaf8)
- 新版 [`00bffaa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffa68.md#insn-00bffaa4) · [`00bffac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffa68.md#insn-00bffac8) · [`00bffaec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffa68.md#insn-00bffaec)

~~~diff
- 00bfeab0 ["INT_ADD", "register:40f0:8", ["const:bfeab0:8", "const:4:8"]]
- 00bfeab0 ["CALL", null, ["callee:00c5e190:8"]]
+ 00bffaa4 ["INT_ADD", "register:40f0:8", ["const:bffaa4:8", "const:4:8"]]
+ 00bffaa4 ["CALL", null, ["callee:00c5e190:8"]]
- 00bfeab0 bytes c4790194
+ 00bffaa4 bytes bb790194
- 00bfead4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfead4 ["INT_ADD", "register:40f0:8", ["const:bfead4:8", "const:4:8"]]
- 00bfead4 ["CALLIND", null, ["register:0:8"]]
+ 00bffac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bffac8 ["INT_ADD", "register:40f0:8", ["const:bffac8:8", "const:4:8"]]
+ 00bffac8 ["CALLIND", null, ["register:0:8"]]
- 00bfead4 bytes 00013fd6
+ 00bffac8 bytes 00013fd6
- 00bfeaf8 ["INT_ADD", "register:40f0:8", ["const:bfeaf8:8", "const:4:8"]]
- 00bfeaf8 ["CALL", null, ["callee:00c59340:8"]]
+ 00bffaec ["INT_ADD", "register:40f0:8", ["const:bffaec:8", "const:4:8"]]
+ 00bffaec ["CALL", null, ["callee:00c59340:8"]]
- 00bfeaf8 bytes 1e660194
+ 00bffaec bytes 15660194
~~~


<a id="compare-a0dc52496d1eb221621d7c3973b983bb"></a>

### [`00bfeb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb28.md) → [`00bffb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffb1c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfeb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb28.md#insn-00bfeb48)
- 新版 [`00bffb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffb1c.md#insn-00bffb3c)

~~~diff
- 00bfeb48 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfeb48 ["INT_ADD", "register:40f0:8", ["const:bfeb48:8", "const:4:8"]]
- 00bfeb48 ["CALLIND", null, ["register:0:8"]]
+ 00bffb3c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bffb3c ["INT_ADD", "register:40f0:8", ["const:bffb3c:8", "const:4:8"]]
+ 00bffb3c ["CALLIND", null, ["register:0:8"]]
- 00bfeb48 bytes 20003fd6
+ 00bffb3c bytes 20003fd6
~~~


<a id="compare-b5fdc5368596ca29779ac824345d6f65"></a>

### [`00bfeb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb60.md) → [`00bffb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffb54.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfeb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb60.md#insn-00bfeb80)
- 新版 [`00bffb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffb54.md#insn-00bffb74)

~~~diff
- 00bfeb80 ["COPY", "register:0:8", ["register:4008:8"]]
- 00bfeb80 ["INT_ADD", "register:40f0:8", ["const:bfeb80:8", "const:4:8"]]
- 00bfeb80 ["CALLIND", null, ["register:0:8"]]
+ 00bffb74 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00bffb74 ["INT_ADD", "register:40f0:8", ["const:bffb74:8", "const:4:8"]]
+ 00bffb74 ["CALLIND", null, ["register:0:8"]]
- 00bfeb80 bytes 20003fd6
+ 00bffb74 bytes 20003fd6
~~~


<a id="compare-235483113c8faf81b38316ac5f4a2f61"></a>

### [`00bff500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff500.md) → [`00c004f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c004f4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE3putEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59300.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff500.md#insn-00bff524) · [`00bff56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff500.md#insn-00bff56c) · [`00bff58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff500.md#insn-00bff58c)
- 新版 [`00c00518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c004f4.md#insn-00c00518) · [`00c00560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c004f4.md#insn-00c00560) · [`00c00580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c004f4.md#insn-00c00580)

~~~diff
- 00bff524 ["INT_ADD", "register:40f0:8", ["const:bff524:8", "const:4:8"]]
- 00bff524 ["CALL", null, ["callee:00c59300:8"]]
+ 00c00518 ["INT_ADD", "register:40f0:8", ["const:c00518:8", "const:4:8"]]
+ 00c00518 ["CALL", null, ["callee:00c59300:8"]]
- 00bff524 bytes 83630194
+ 00c00518 bytes 7a630194
- 00bff56c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff56c ["INT_ADD", "register:40f0:8", ["const:bff56c:8", "const:4:8"]]
- 00bff56c ["CALLIND", null, ["register:0:8"]]
+ 00c00560 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00560 ["INT_ADD", "register:40f0:8", ["const:c00560:8", "const:4:8"]]
+ 00c00560 ["CALLIND", null, ["register:0:8"]]
- 00bff56c bytes 00013fd6
+ 00c00560 bytes 00013fd6
- 00bff58c ["INT_ADD", "register:40f0:8", ["const:bff58c:8", "const:4:8"]]
- 00bff58c ["CALL", null, ["callee:00c59340:8"]]
+ 00c00580 ["INT_ADD", "register:40f0:8", ["const:c00580:8", "const:4:8"]]
+ 00c00580 ["CALL", null, ["callee:00c59340:8"]]
- 00bff58c bytes 79630194
+ 00c00580 bytes 70630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e53bfdce5119db59d3dd63932faa4e7"></a>

### [`00bff5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff5f8.md) → [`00c005ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c005ec.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5tellpEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff5f8.md#insn-00bff648)
- 新版 [`00c0063c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c005ec.md#insn-00c0063c)

~~~diff
- 00bff648 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff648 ["INT_ADD", "register:40f0:8", ["const:bff648:8", "const:4:8"]]
- 00bff648 ["CALLIND", null, ["register:0:8"]]
+ 00c0063c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0063c ["INT_ADD", "register:40f0:8", ["const:c0063c:8", "const:4:8"]]
+ 00c0063c ["CALLIND", null, ["register:0:8"]]
- 00bff648 bytes 00013fd6
+ 00c0063c bytes 00013fd6
~~~


<a id="compare-9a7ce2b7ed491b39f48cf7e6d4ee30f9"></a>

### [`00bff658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff658.md) → [`00c0064c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c0064c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59300.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff658.md#insn-00bff684) · [`00bff6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff658.md#insn-00bff6bc) · [`00bff6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff658.md#insn-00bff6dc)
- 新版 [`00c00678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c0064c.md#insn-00c00678) · [`00c006b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c0064c.md#insn-00c006b0) · [`00c006d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c0064c.md#insn-00c006d0)

~~~diff
- 00bff684 ["INT_ADD", "register:40f0:8", ["const:bff684:8", "const:4:8"]]
- 00bff684 ["CALL", null, ["callee:00c59300:8"]]
+ 00c00678 ["INT_ADD", "register:40f0:8", ["const:c00678:8", "const:4:8"]]
+ 00c00678 ["CALL", null, ["callee:00c59300:8"]]
- 00bff684 bytes 2b630194
+ 00c00678 bytes 22630194
- 00bff6bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff6bc ["INT_ADD", "register:40f0:8", ["const:bff6bc:8", "const:4:8"]]
- 00bff6bc ["CALLIND", null, ["register:0:8"]]
+ 00c006b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c006b0 ["INT_ADD", "register:40f0:8", ["const:c006b0:8", "const:4:8"]]
+ 00c006b0 ["CALLIND", null, ["register:0:8"]]
- 00bff6bc bytes 00013fd6
+ 00c006b0 bytes 00013fd6
- 00bff6dc ["INT_ADD", "register:40f0:8", ["const:bff6dc:8", "const:4:8"]]
- 00bff6dc ["CALL", null, ["callee:00c59340:8"]]
+ 00c006d0 ["INT_ADD", "register:40f0:8", ["const:c006d0:8", "const:4:8"]]
+ 00c006d0 ["CALL", null, ["callee:00c59340:8"]]
- 00bff6dc bytes 25630194
+ 00c006d0 bytes 1c630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38b17f5b4df0831cbdc513bb0d99244b"></a>

### [`00bff71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff71c.md) → [`00c00710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00710.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58380.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59300.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59350.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff71c.md#insn-00bff748) · [`00bff780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff71c.md#insn-00bff780) · [`00bff7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff71c.md#insn-00bff7a0)
- 新版 [`00c0073c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00710.md#insn-00c0073c) · [`00c00774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00710.md#insn-00c00774) · [`00c00794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00710.md#insn-00c00794)

~~~diff
- 00bff748 ["INT_ADD", "register:40f0:8", ["const:bff748:8", "const:4:8"]]
- 00bff748 ["CALL", null, ["callee:00c59300:8"]]
+ 00c0073c ["INT_ADD", "register:40f0:8", ["const:c0073c:8", "const:4:8"]]
+ 00c0073c ["CALL", null, ["callee:00c59300:8"]]
- 00bff748 bytes fa620194
+ 00c0073c bytes f1620194
- 00bff780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bff780 ["INT_ADD", "register:40f0:8", ["const:bff780:8", "const:4:8"]]
- 00bff780 ["CALLIND", null, ["register:0:8"]]
+ 00c00774 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00774 ["INT_ADD", "register:40f0:8", ["const:c00774:8", "const:4:8"]]
+ 00c00774 ["CALLIND", null, ["register:0:8"]]
- 00bff780 bytes 00013fd6
+ 00c00774 bytes 00013fd6
- 00bff7a0 ["INT_ADD", "register:40f0:8", ["const:bff7a0:8", "const:4:8"]]
- 00bff7a0 ["CALL", null, ["callee:00c59340:8"]]
+ 00c00794 ["INT_ADD", "register:40f0:8", ["const:c00794:8", "const:4:8"]]
+ 00c00794 ["CALL", null, ["callee:00c59340:8"]]
- 00bff7a0 bytes f4620194
+ 00c00794 bytes eb620194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e10adf831f4fc9003140d6cac60a23c9"></a>

### [`00bff7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff7e0.md) → [`00c007d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c007d4.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff7e0.md#insn-00bff828)
- 新版 [`00c0081c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c007d4.md#insn-00c0081c)

~~~diff
- 00bff828 ["INT_ADD", "register:40f0:8", ["const:bff828:8", "const:4:8"]]
- 00bff828 ["CALL", null, ["callee:00c59280:8"]]
+ 00c0081c ["INT_ADD", "register:40f0:8", ["const:c0081c:8", "const:4:8"]]
+ 00c0081c ["CALL", null, ["callee:00c59280:8"]]
- 00bff828 bytes a2620194
+ 00c0081c bytes 99620194
~~~


<a id="compare-2aca13f6ffda680fa253125711533010"></a>

### [`00bff940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff940.md) → [`00c00934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00934.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff940.md#insn-00bff958)
- 新版 [`00c0094c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00934.md#insn-00c0094c)

~~~diff
- 00bff958 ["INT_ADD", "register:40f0:8", ["const:bff958:8", "const:4:8"]]
- 00bff958 ["CALL", null, ["callee:00c5e180:8"]]
+ 00c0094c ["INT_ADD", "register:40f0:8", ["const:c0094c:8", "const:4:8"]]
+ 00c0094c ["CALL", null, ["callee:00c5e180:8"]]
- 00bff958 bytes 16760194
+ 00c0094c bytes 0d760194
~~~


<a id="compare-eefced0febb18a26fbd162173a9bb375"></a>

### [`00bff970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff970.md) → [`00c00964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00964.md) _ZThn16_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff970.md#insn-00bff988)
- 新版 [`00c0097c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00964.md#insn-00c0097c)

~~~diff
- 00bff988 ["INT_ADD", "register:40f0:8", ["const:bff988:8", "const:4:8"]]
- 00bff988 ["CALL", null, ["callee:00c5e180:8"]]
+ 00c0097c ["INT_ADD", "register:40f0:8", ["const:c0097c:8", "const:4:8"]]
+ 00c0097c ["CALL", null, ["callee:00c5e180:8"]]
- 00bff988 bytes 0a760194
+ 00c0097c bytes 01760194
~~~


<a id="compare-f56710212921834a495ea4a258ce2012"></a>

### [`00bff9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff9a0.md) → [`00c00994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00994.md) _ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff9a0.md#insn-00bff9c0)
- 新版 [`00c009b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00994.md#insn-00c009b4)

~~~diff
- 00bff9c0 ["INT_ADD", "register:40f0:8", ["const:bff9c0:8", "const:4:8"]]
- 00bff9c0 ["CALL", null, ["callee:00c5e180:8"]]
+ 00c009b4 ["INT_ADD", "register:40f0:8", ["const:c009b4:8", "const:4:8"]]
+ 00c009b4 ["CALL", null, ["callee:00c5e180:8"]]
- 00bff9c0 bytes fc750194
+ 00c009b4 bytes f3750194
~~~


<a id="compare-d898618566307433046cb636fce2de76"></a>

### [`00bff9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff9d8.md) → [`00c009cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c009cc.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffa10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff9d8.md#insn-00bffa10)
- 新版 [`00c00a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c009cc.md#insn-00c00a04)

~~~diff
- 00bffa10 ["INT_ADD", "register:40f0:8", ["const:bffa10:8", "const:4:8"]]
- 00bffa10 ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00c00a04 ["INT_ADD", "register:40f0:8", ["const:c00a04:8", "const:4:8"]]
+ 00c00a04 ["CALL", null, ["callee:00c5f3c0:8"]]
- 00bffa10 bytes 787a0194
+ 00c00a04 bytes 6f7a0194
~~~


<a id="compare-b617a5a41dc5b323d62120f907b4b6ab"></a>

### [`00bffa4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa4c.md) → [`00c00a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00a40.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e480.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa4c.md#insn-00bffa60)
- 新版 [`00c00a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00a40.md#insn-00c00a54)

~~~diff
- 00bffa60 ["INT_ADD", "register:40f0:8", ["const:bffa60:8", "const:4:8"]]
- 00bffa60 ["CALL", null, ["callee:00c5f450:8"]]
+ 00c00a54 ["INT_ADD", "register:40f0:8", ["const:c00a54:8", "const:4:8"]]
+ 00c00a54 ["CALL", null, ["callee:00c5f450:8"]]
- 00bffa60 bytes 887a0194
+ 00c00a54 bytes 7f7a0194
~~~


