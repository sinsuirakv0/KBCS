# v16.0.2 → v16.0.3 · 要調査の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-defa51e1308340ce90a3e74535722b31"></a>

### [`00501820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501820.md) → [`00501b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501b40.md) _ZNK5Botan16X509_Certificate10subject_dnEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501820.md#insn-00501828)
- 新版 [`00501b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501b40.md#insn-00501b48)

~~~diff
- 00501828 ["INT_ADD", "register:40f0:8", ["const:501828:8", "const:4:8"]]
- 00501828 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00501b48 ["INT_ADD", "register:40f0:8", ["const:501b48:8", "const:4:8"]]
+ 00501b48 ["CALL", null, ["callee:00c5aa90:8"]]
- 00501828 bytes a6601d94
+ 00501b48 bytes d2631d94
~~~


<a id="compare-137d0fffa2b889ae754dc83456f6a2c3"></a>

### [`00501838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501838.md) → [`00501b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501b58.md) FUN_00501b58

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501838.md#insn-00501874) · [`00501890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501838.md#insn-00501890)
- 新版 [`00501b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501b58.md#insn-00501b94) · [`00501bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501b58.md#insn-00501bb0)

~~~diff
- 00501874 ["INT_ADD", "register:40f0:8", ["const:501874:8", "const:4:8"]]
- 00501874 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00501b94 ["INT_ADD", "register:40f0:8", ["const:501b94:8", "const:4:8"]]
+ 00501b94 ["CALL", null, ["callee:0053b2f0:8"]]
- 00501874 bytes d7e50094
+ 00501b94 bytes d7e50094
- 00501890 ["INT_ADD", "register:40f0:8", ["const:501890:8", "const:4:8"]]
- 00501890 ["CALL", null, ["callee:00c58f50:8"]]
+ 00501bb0 ["INT_ADD", "register:40f0:8", ["const:501bb0:8", "const:4:8"]]
+ 00501bb0 ["CALL", null, ["callee:00c58f50:8"]]
- 00501890 bytes bc591d94
+ 00501bb0 bytes e85c1d94
~~~


<a id="compare-9ceb2a06a1391f99065f089d17c97c93"></a>

### [`005018c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005018c0.md) → [`00501be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501be0.md) _ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ad0.md) · 呼出先 9件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5aaa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaa0.md) · 呼出先 9件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050190c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005018c0.md#insn-0050190c) · [`00501914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005018c0.md#insn-00501914) · [`00501920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005018c0.md#insn-00501920)
- 新版 [`00501c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501be0.md#insn-00501c2c) · [`00501c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501be0.md#insn-00501c34) · [`00501c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501be0.md#insn-00501c40)

~~~diff
- 0050190c ["INT_ADD", "register:40f0:8", ["const:50190c:8", "const:4:8"]]
- 0050190c ["CALL", null, ["callee:00c58f50:8"]]
+ 00501c2c ["INT_ADD", "register:40f0:8", ["const:501c2c:8", "const:4:8"]]
+ 00501c2c ["CALL", null, ["callee:00c58f50:8"]]
- 0050190c bytes 9d591d94
+ 00501c2c bytes c95c1d94
- 00501914 ["INT_ADD", "register:40f0:8", ["const:501914:8", "const:4:8"]]
- 00501914 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00501c34 ["INT_ADD", "register:40f0:8", ["const:501c34:8", "const:4:8"]]
+ 00501c34 ["CALL", null, ["callee:00c5aa90:8"]]
- 00501914 bytes 6b601d94
+ 00501c34 bytes 97631d94
- 00501920 ["INT_ADD", "register:40f0:8", ["const:501920:8", "const:4:8"]]
- 00501920 ["CALL", null, ["callee:00c5aab0:8"]]
+ 00501c40 ["INT_ADD", "register:40f0:8", ["const:501c40:8", "const:4:8"]]
+ 00501c40 ["CALL", null, ["callee:00c5aab0:8"]]
- 00501920 bytes 70601d94
+ 00501c40 bytes 9c631d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87217c9e593bfcaaaa3702d454f81cea"></a>

### [`00501a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a5c.md) → [`00501d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501d7c.md) _ZNK5Botan16X509_Certificate14subject_key_idEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a5c.md#insn-00501a64)
- 新版 [`00501d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501d7c.md#insn-00501d84)

~~~diff
- 00501a64 ["INT_ADD", "register:40f0:8", ["const:501a64:8", "const:4:8"]]
- 00501a64 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00501d84 ["INT_ADD", "register:40f0:8", ["const:501d84:8", "const:4:8"]]
+ 00501d84 ["CALL", null, ["callee:00c5aa90:8"]]
- 00501a64 bytes 17601d94
+ 00501d84 bytes 43631d94
~~~


<a id="compare-c090e0602be380cf4d8f68d4a60734cd"></a>

### [`00501a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a74.md) → [`00501d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501d94.md) _ZN5BotaneqERKNS_7X509_DNES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ae0.md) · 呼出先 4件 [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c599c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c599c0.md) [`00c59af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59af0.md)
- 新版 呼出元 1件 [`00c5aab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aab0.md) · 呼出先 4件 [`005499c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005499c8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a990.md) [`00c5aac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a74.md#insn-00501aa0) · [`00501aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a74.md#insn-00501aac) · [`00501b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a74.md#insn-00501b2c)
- 新版 [`00501dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501d94.md#insn-00501dc0) · [`00501dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501d94.md#insn-00501dcc) · [`00501e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501d94.md#insn-00501e4c)

~~~diff
- 00501aa0 ["INT_ADD", "register:40f0:8", ["const:501aa0:8", "const:4:8"]]
- 00501aa0 ["CALL", null, ["callee:00c5aac0:8"]]
+ 00501dc0 ["INT_ADD", "register:40f0:8", ["const:501dc0:8", "const:4:8"]]
+ 00501dc0 ["CALL", null, ["callee:00c5aac0:8"]]
- 00501aa0 bytes 14601d94
+ 00501dc0 bytes 40631d94
- 00501aac ["INT_ADD", "register:40f0:8", ["const:501aac:8", "const:4:8"]]
- 00501aac ["CALL", null, ["callee:00c5aac0:8"]]
+ 00501dcc ["INT_ADD", "register:40f0:8", ["const:501dcc:8", "const:4:8"]]
+ 00501dcc ["CALL", null, ["callee:00c5aac0:8"]]
- 00501aac bytes 11601d94
+ 00501dcc bytes 3d631d94
- 00501b2c ["INT_ADD", "register:40f0:8", ["const:501b2c:8", "const:4:8"]]
- 00501b2c ["CALL", null, ["callee:00c5a990:8"]]
+ 00501e4c ["INT_ADD", "register:40f0:8", ["const:501e4c:8", "const:4:8"]]
+ 00501e4c ["CALL", null, ["callee:00c5a990:8"]]
- 00501b2c bytes a55f1d94
+ 00501e4c bytes d1621d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff39d017536559bec8ffdf46ab8891ae"></a>

### [`00501c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501c2c.md) → [`00501f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501f4c.md) _ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b00.md) · 呼出先 10件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005485d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005485d8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5aad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aad0.md) · 呼出先 10件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`005488f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005488f8.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501c2c.md#insn-00501c80) · [`00501ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501c2c.md#insn-00501ca0) · [`00501cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501c2c.md#insn-00501cc4)
- 新版 [`00501fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501f4c.md#insn-00501fa0) · [`00501fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501f4c.md#insn-00501fc0) · [`00501fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501f4c.md#insn-00501fe4)

~~~diff
- 00501c80 ["INT_ADD", "register:40f0:8", ["const:501c80:8", "const:4:8"]]
- 00501c80 ["CALL", null, ["callee:00c58f50:8"]]
+ 00501fa0 ["INT_ADD", "register:40f0:8", ["const:501fa0:8", "const:4:8"]]
+ 00501fa0 ["CALL", null, ["callee:00c58f50:8"]]
- 00501c80 bytes c0581d94
+ 00501fa0 bytes ec5b1d94
- 00501ca0 ["INT_ADD", "register:40f0:8", ["const:501ca0:8", "const:4:8"]]
- 00501ca0 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00501fc0 ["INT_ADD", "register:40f0:8", ["const:501fc0:8", "const:4:8"]]
+ 00501fc0 ["CALL", null, ["callee:00c5aa90:8"]]
- 00501ca0 bytes 885f1d94
+ 00501fc0 bytes b4621d94
- 00501cc4 ["INT_ADD", "register:40f0:8", ["const:501cc4:8", "const:4:8"]]
- 00501cc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00501fe4 ["INT_ADD", "register:40f0:8", ["const:501fe4:8", "const:4:8"]]
+ 00501fe4 ["CALL", null, ["callee:00c58f30:8"]]
- 00501cc4 bytes a7581d94
+ 00501fe4 bytes d35b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78b76dd681e6bf915d7492f4ac9db86f"></a>

### [`00501df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501df8.md) → [`00502118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502118.md) FUN_00502118

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0052d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d150.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501df8.md#insn-00501e44) · [`00501e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501df8.md#insn-00501e58) · [`00501e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501df8.md#insn-00501e60)
- 新版 [`00502164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502118.md#insn-00502164) · [`00502178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502118.md#insn-00502178) · [`00502180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502118.md#insn-00502180)

~~~diff
- 00501e44 ["INT_ADD", "register:40f0:8", ["const:501e44:8", "const:4:8"]]
- 00501e44 ["CALL", null, ["callee:00c54d90:8"]]
+ 00502164 ["INT_ADD", "register:40f0:8", ["const:502164:8", "const:4:8"]]
+ 00502164 ["CALL", null, ["callee:00c54d90:8"]]
- 00501e44 bytes d7471d94
+ 00502164 bytes 0b4b1d94
- 00501e58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00501e58 ["INT_ADD", "register:40f0:8", ["const:501e58:8", "const:4:8"]]
- 00501e58 ["CALLIND", null, ["register:0:8"]]
+ 00502178 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502178 ["INT_ADD", "register:40f0:8", ["const:502178:8", "const:4:8"]]
+ 00502178 ["CALLIND", null, ["register:0:8"]]
- 00501e58 bytes 00013fd6
+ 00502178 bytes 00013fd6
- 00501e60 ["INT_ADD", "register:40f0:8", ["const:501e60:8", "const:4:8"]]
- 00501e60 ["CALL", null, ["callee:00c58f20:8"]]
+ 00502180 ["INT_ADD", "register:40f0:8", ["const:502180:8", "const:4:8"]]
+ 00502180 ["CALL", null, ["callee:00c58f20:8"]]
- 00501e60 bytes 3c581d94
+ 00502180 bytes 685b1d94
~~~


<a id="compare-c5501a4255ac78c8503a36e38009739e"></a>

### [`00502190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502190.md) → [`005024b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005024b0.md) _ZNK5Botan16X509_Certificate28subject_public_key_bitstringEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502190.md#insn-00502198)
- 新版 [`005024b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005024b0.md#insn-005024b8)

~~~diff
- 00502198 ["INT_ADD", "register:40f0:8", ["const:502198:8", "const:4:8"]]
- 00502198 ["CALL", null, ["callee:00c5aa90:8"]]
+ 005024b8 ["INT_ADD", "register:40f0:8", ["const:5024b8:8", "const:4:8"]]
+ 005024b8 ["CALL", null, ["callee:00c5aa90:8"]]
- 00502198 bytes 4a5e1d94
+ 005024b8 bytes 76611d94
~~~


<a id="compare-911677132139acacf92a7e893955d94d"></a>

### [`005024b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024b0.md) → [`005027d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005027d0.md) _ZNK5Botan16X509_Certificate14raw_subject_dnEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005024b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024b0.md#insn-005024b8)
- 新版 [`005027d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005027d0.md#insn-005027d8)

~~~diff
- 005024b8 ["INT_ADD", "register:40f0:8", ["const:5024b8:8", "const:4:8"]]
- 005024b8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 005027d8 ["INT_ADD", "register:40f0:8", ["const:5027d8:8", "const:4:8"]]
+ 005027d8 ["CALL", null, ["callee:00c5aa90:8"]]
- 005024b8 bytes 825d1d94
+ 005027d8 bytes ae601d94
~~~


<a id="compare-e85f261a66aef37d28d2348bbc942701"></a>

### [`0050263c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050263c.md) → [`0050295c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/0050295c.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b10.md) · 呼出先 11件 [`00502838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00548c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548c00.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c5aae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aae0.md) · 呼出先 11件 [`00502b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b58.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00548f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548f20.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050263c.md#insn-00502670) · [`0050267c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050263c.md#insn-0050267c) · [`00502694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050263c.md#insn-00502694)
- 新版 [`00502990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/0050295c.md#insn-00502990) · [`0050299c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/0050295c.md#insn-0050299c) · [`005029b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/0050295c.md#insn-005029b4)

~~~diff
- 00502670 ["INT_ADD", "register:40f0:8", ["const:502670:8", "const:4:8"]]
- 00502670 ["CALL", null, ["callee:00c5aaf0:8"]]
+ 00502990 ["INT_ADD", "register:40f0:8", ["const:502990:8", "const:4:8"]]
+ 00502990 ["CALL", null, ["callee:00c5aaf0:8"]]
- 00502670 bytes 2c5d1d94
+ 00502990 bytes 58601d94
- 0050267c ["INT_ADD", "register:40f0:8", ["const:50267c:8", "const:4:8"]]
- 0050267c ["CALL", null, ["callee:00502b58:8"]]
+ 0050299c ["INT_ADD", "register:40f0:8", ["const:50299c:8", "const:4:8"]]
+ 0050299c ["CALL", null, ["callee:00502b58:8"]]
- 0050267c bytes 6f000094
+ 0050299c bytes 6f000094
- 00502694 ["INT_ADD", "register:40f0:8", ["const:502694:8", "const:4:8"]]
- 00502694 ["CALL", null, ["callee:00c5aaf0:8"]]
+ 005029b4 ["INT_ADD", "register:40f0:8", ["const:5029b4:8", "const:4:8"]]
+ 005029b4 ["CALL", null, ["callee:00c5aaf0:8"]]
- 00502694 bytes 235d1d94
+ 005029b4 bytes 4f601d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08847649e9c638c512498e49b4626279"></a>

### [`005027e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005027e4.md) → [`00502b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b04.md) FUN_00502b04

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005027e4.md#insn-00502800) · [`00502820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005027e4.md#insn-00502820)
- 新版 [`00502b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b04.md#insn-00502b20) · [`00502b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b04.md#insn-00502b40)

~~~diff
- 00502800 ["INT_ADD", "register:40f0:8", ["const:502800:8", "const:4:8"]]
- 00502800 ["CALL", null, ["callee:00c54d90:8"]]
+ 00502b20 ["INT_ADD", "register:40f0:8", ["const:502b20:8", "const:4:8"]]
+ 00502b20 ["CALL", null, ["callee:00c54d90:8"]]
- 00502800 bytes 68451d94
+ 00502b20 bytes 9c481d94
- 00502820 ["COPY", "register:0:8", ["register:4040:8"]]
- 00502820 ["INT_ADD", "register:40f0:8", ["const:502820:8", "const:4:8"]]
- 00502820 ["CALLIND", null, ["register:0:8"]]
+ 00502b40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502b40 ["INT_ADD", "register:40f0:8", ["const:502b40:8", "const:4:8"]]
+ 00502b40 ["CALLIND", null, ["register:0:8"]]
- 00502820 bytes 00013fd6
+ 00502b40 bytes 00013fd6
~~~


<a id="compare-4940b6c8197f087a733683eae5755c41"></a>

### [`00502964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502964.md) → [`00502c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502c84.md) _ZNK5Botan8X509_CRL11this_updateEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502964.md#insn-0050296c)
- 新版 [`00502c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502c84.md#insn-00502c8c)

~~~diff
- 0050296c ["INT_ADD", "register:40f0:8", ["const:50296c:8", "const:4:8"]]
- 0050296c ["CALL", null, ["callee:00c5aaf0:8"]]
+ 00502c8c ["INT_ADD", "register:40f0:8", ["const:502c8c:8", "const:4:8"]]
+ 00502c8c ["CALL", null, ["callee:00c5aaf0:8"]]
- 0050296c bytes 6d5c1d94
+ 00502c8c bytes 995f1d94
~~~


<a id="compare-325bb35de7082482d3608e3d84512743"></a>

### [`0050297c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050297c.md) → [`00502c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502c9c.md) _ZNK5Botan27Certificate_Store_In_Memory12find_crl_forERKNS_16X509_CertificateE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005029b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050297c.md#insn-005029b8) · [`005029d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050297c.md#insn-005029d4) · [`005029dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050297c.md#insn-005029dc)
- 新版 [`00502cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502c9c.md#insn-00502cd8) · [`00502cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502c9c.md#insn-00502cf4) · [`00502cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502c9c.md#insn-00502cfc)

~~~diff
- 005029b8 ["INT_ADD", "register:40f0:8", ["const:5029b8:8", "const:4:8"]]
- 005029b8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00502cd8 ["INT_ADD", "register:40f0:8", ["const:502cd8:8", "const:4:8"]]
+ 00502cd8 ["CALL", null, ["callee:00c5aa90:8"]]
- 005029b8 bytes 425c1d94
+ 00502cd8 bytes 6e5f1d94
- 005029d4 ["INT_ADD", "register:40f0:8", ["const:5029d4:8", "const:4:8"]]
- 005029d4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00502cf4 ["INT_ADD", "register:40f0:8", ["const:502cf4:8", "const:4:8"]]
+ 00502cf4 ["CALL", null, ["callee:00c58f50:8"]]
- 005029d4 bytes 6b551d94
+ 00502cf4 bytes 97581d94
- 005029dc ["INT_ADD", "register:40f0:8", ["const:5029dc:8", "const:4:8"]]
- 005029dc ["CALL", null, ["callee:00c5aaf0:8"]]
+ 00502cfc ["INT_ADD", "register:40f0:8", ["const:502cfc:8", "const:4:8"]]
+ 00502cfc ["CALL", null, ["callee:00c5aaf0:8"]]
- 005029dc bytes 515c1d94
+ 00502cfc bytes 7d5f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf795627fcf78e219db6907be70f79e"></a>

### [`00502b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b34.md) → [`00502e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e54.md) _ZNK5Botan16X509_Certificate16authority_key_idEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b34.md#insn-00502b3c)
- 新版 [`00502e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e54.md#insn-00502e5c)

~~~diff
- 00502b3c ["INT_ADD", "register:40f0:8", ["const:502b3c:8", "const:4:8"]]
- 00502b3c ["CALL", null, ["callee:00c5aa90:8"]]
+ 00502e5c ["INT_ADD", "register:40f0:8", ["const:502e5c:8", "const:4:8"]]
+ 00502e5c ["CALL", null, ["callee:00c5aa90:8"]]
- 00502b3c bytes e15b1d94
+ 00502e5c bytes 0d5f1d94
~~~


<a id="compare-c9b84d158ba63b3487b89412d2c0cd51"></a>

### [`00502b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b4c.md) → [`00502e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e6c.md) _ZNK5Botan8X509_CRL16authority_key_idEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b4c.md#insn-00502b54)
- 新版 [`00502e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e6c.md#insn-00502e74)

~~~diff
- 00502b54 ["INT_ADD", "register:40f0:8", ["const:502b54:8", "const:4:8"]]
- 00502b54 ["CALL", null, ["callee:00c5aaf0:8"]]
+ 00502e74 ["INT_ADD", "register:40f0:8", ["const:502e74:8", "const:4:8"]]
+ 00502e74 ["CALL", null, ["callee:00c5aaf0:8"]]
- 00502b54 bytes f35b1d94
+ 00502e74 bytes 1f5f1d94
~~~


<a id="compare-0330020493488dafd655ef163105c179"></a>

### [`00502b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b64.md) → [`00502e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e84.md) _ZNK5Botan16X509_Certificate9issuer_dnEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b64.md#insn-00502b6c)
- 新版 [`00502e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e84.md#insn-00502e8c)

~~~diff
- 00502b6c ["INT_ADD", "register:40f0:8", ["const:502b6c:8", "const:4:8"]]
- 00502b6c ["CALL", null, ["callee:00c5aa90:8"]]
+ 00502e8c ["INT_ADD", "register:40f0:8", ["const:502e8c:8", "const:4:8"]]
+ 00502e8c ["CALL", null, ["callee:00c5aa90:8"]]
- 00502b6c bytes d55b1d94
+ 00502e8c bytes 015f1d94
~~~


<a id="compare-544daa2ba6ad6e6a157178f715122c64"></a>

### [`00502be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502be4.md) → [`00502f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f04.md) FUN_00502f04

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502be4.md#insn-00502c30) · [`00502c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502be4.md#insn-00502c44) · [`00502c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502be4.md#insn-00502c4c)
- 新版 [`00502f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f04.md#insn-00502f50) · [`00502f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f04.md#insn-00502f64) · [`00502f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f04.md#insn-00502f6c)

~~~diff
- 00502c30 ["INT_ADD", "register:40f0:8", ["const:502c30:8", "const:4:8"]]
- 00502c30 ["CALL", null, ["callee:00c54d90:8"]]
+ 00502f50 ["INT_ADD", "register:40f0:8", ["const:502f50:8", "const:4:8"]]
+ 00502f50 ["CALL", null, ["callee:00c54d90:8"]]
- 00502c30 bytes 5c441d94
+ 00502f50 bytes 90471d94
- 00502c44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00502c44 ["INT_ADD", "register:40f0:8", ["const:502c44:8", "const:4:8"]]
- 00502c44 ["CALLIND", null, ["register:0:8"]]
+ 00502f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502f64 ["INT_ADD", "register:40f0:8", ["const:502f64:8", "const:4:8"]]
+ 00502f64 ["CALLIND", null, ["register:0:8"]]
- 00502c44 bytes 00013fd6
+ 00502f64 bytes 00013fd6
- 00502c4c ["INT_ADD", "register:40f0:8", ["const:502c4c:8", "const:4:8"]]
- 00502c4c ["CALL", null, ["callee:00c58f20:8"]]
+ 00502f6c ["INT_ADD", "register:40f0:8", ["const:502f6c:8", "const:4:8"]]
+ 00502f6c ["CALL", null, ["callee:00c58f20:8"]]
- 00502c4c bytes c1541d94
+ 00502f6c bytes ed571d94
~~~


<a id="compare-5860fc4b3cf134540ec7e7b2d4e80827"></a>

### [`00502f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f00.md) → [`00503220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503220.md) FUN_00503220

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f00.md#insn-00502f1c) · [`00502f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f00.md#insn-00502f3c)
- 新版 [`0050323c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503220.md#insn-0050323c) · [`0050325c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503220.md#insn-0050325c)

~~~diff
- 00502f1c ["INT_ADD", "register:40f0:8", ["const:502f1c:8", "const:4:8"]]
- 00502f1c ["CALL", null, ["callee:00c54d90:8"]]
+ 0050323c ["INT_ADD", "register:40f0:8", ["const:50323c:8", "const:4:8"]]
+ 0050323c ["CALL", null, ["callee:00c54d90:8"]]
- 00502f1c bytes a1431d94
+ 0050323c bytes d5461d94
- 00502f3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00502f3c ["INT_ADD", "register:40f0:8", ["const:502f3c:8", "const:4:8"]]
- 00502f3c ["CALLIND", null, ["register:0:8"]]
+ 0050325c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050325c ["INT_ADD", "register:40f0:8", ["const:50325c:8", "const:4:8"]]
+ 0050325c ["CALLIND", null, ["register:0:8"]]
- 00502f3c bytes 00013fd6
+ 0050325c bytes 00013fd6
~~~


<a id="compare-c95fe4362439078423e01510d90e0906"></a>

### [`00503500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503500.md) → [`00503820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503820.md) FUN_00503820

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050351c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503500.md#insn-0050351c) · [`0050353c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503500.md#insn-0050353c)
- 新版 [`0050383c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503820.md#insn-0050383c) · [`0050385c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503820.md#insn-0050385c)

~~~diff
- 0050351c ["INT_ADD", "register:40f0:8", ["const:50351c:8", "const:4:8"]]
- 0050351c ["CALL", null, ["callee:00c54d90:8"]]
+ 0050383c ["INT_ADD", "register:40f0:8", ["const:50383c:8", "const:4:8"]]
+ 0050383c ["CALL", null, ["callee:00c54d90:8"]]
- 0050351c bytes 21421d94
+ 0050383c bytes 55451d94
- 0050353c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050353c ["INT_ADD", "register:40f0:8", ["const:50353c:8", "const:4:8"]]
- 0050353c ["CALLIND", null, ["register:0:8"]]
+ 0050385c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050385c ["INT_ADD", "register:40f0:8", ["const:50385c:8", "const:4:8"]]
+ 0050385c ["CALLIND", null, ["register:0:8"]]
- 0050353c bytes 00013fd6
+ 0050385c bytes 00013fd6
~~~


<a id="compare-755bc0e2452ba3e1b2960d655e46551f"></a>

### [`00503550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503550.md) → [`00503870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503870.md) _ZN5BotaneqERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b60.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md) [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)
- 新版 呼出元 1件 [`00c5ab30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab30.md) · 呼出先 3件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md) [`00c5ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503550.md#insn-00503568) · [`00503574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503550.md#insn-00503574) · [`00503594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503550.md#insn-00503594)
- 新版 [`00503888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503870.md#insn-00503888) · [`00503894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503870.md#insn-00503894) · [`005038b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503870.md#insn-005038b4)

~~~diff
- 00503568 ["INT_ADD", "register:40f0:8", ["const:503568:8", "const:4:8"]]
- 00503568 ["CALL", null, ["callee:00c5ab40:8"]]
+ 00503888 ["INT_ADD", "register:40f0:8", ["const:503888:8", "const:4:8"]]
+ 00503888 ["CALL", null, ["callee:00c5ab40:8"]]
- 00503568 bytes 82591d94
+ 00503888 bytes ae5c1d94
- 00503574 ["INT_ADD", "register:40f0:8", ["const:503574:8", "const:4:8"]]
- 00503574 ["CALL", null, ["callee:00c5ab40:8"]]
+ 00503894 ["INT_ADD", "register:40f0:8", ["const:503894:8", "const:4:8"]]
+ 00503894 ["CALL", null, ["callee:00c5ab40:8"]]
- 00503574 bytes 7f591d94
+ 00503894 bytes ab5c1d94
- 00503594 ["INT_ADD", "register:40f0:8", ["const:503594:8", "const:4:8"]]
- 00503594 ["CALL", null, ["callee:00c590f0:8"]]
+ 005038b4 ["INT_ADD", "register:40f0:8", ["const:5038b4:8", "const:4:8"]]
+ 005038b4 ["CALL", null, ["callee:00c590f0:8"]]
- 00503594 bytes e3521d94
+ 005038b4 bytes 0f561d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d183e80802ea922acb842fd2c1817e46"></a>

### [`00503600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503600.md) → [`00503920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503920.md) _ZNK5Botan9CRL_Entry11expire_timeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503600.md#insn-00503608)
- 新版 [`00503928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503920.md#insn-00503928)

~~~diff
- 00503608 ["INT_ADD", "register:40f0:8", ["const:503608:8", "const:4:8"]]
- 00503608 ["CALL", null, ["callee:00c5ab40:8"]]
+ 00503928 ["INT_ADD", "register:40f0:8", ["const:503928:8", "const:4:8"]]
+ 00503928 ["CALL", null, ["callee:00c5ab40:8"]]
- 00503608 bytes 5a591d94
+ 00503928 bytes 865c1d94
~~~


<a id="compare-82e15c7fab74c89e6517434403cf77b8"></a>

### [`00503618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503618.md) → [`00503938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503938.md) _ZNK5Botan9CRL_Entry11reason_codeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503618.md#insn-00503620)
- 新版 [`00503940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503938.md#insn-00503940)

~~~diff
- 00503620 ["INT_ADD", "register:40f0:8", ["const:503620:8", "const:4:8"]]
- 00503620 ["CALL", null, ["callee:00c5ab40:8"]]
+ 00503940 ["INT_ADD", "register:40f0:8", ["const:503940:8", "const:4:8"]]
+ 00503940 ["CALL", null, ["callee:00c5ab40:8"]]
- 00503620 bytes 54591d94
+ 00503940 bytes 805c1d94
~~~


<a id="compare-89d8ca6fbff66c04ab40c79df0c402d7"></a>

### [`00503630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503630.md) → [`00503950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503950.md) _ZN5BotanneERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503630.md#insn-00503638)
- 新版 [`00503958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503950.md#insn-00503958)

~~~diff
- 00503638 ["INT_ADD", "register:40f0:8", ["const:503638:8", "const:4:8"]]
- 00503638 ["CALL", null, ["callee:00c5ab30:8"]]
+ 00503958 ["INT_ADD", "register:40f0:8", ["const:503958:8", "const:4:8"]]
+ 00503958 ["CALL", null, ["callee:00c5ab30:8"]]
- 00503638 bytes 4a591d94
+ 00503958 bytes 765c1d94
~~~


<a id="compare-41a92c3066c486101a53bac1320b614a"></a>

### [`00503794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503794.md) → [`00503ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503ab4.md) _ZNK5Botan9CRL_Entry10extensionsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050379c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503794.md#insn-0050379c)
- 新版 [`00503abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503ab4.md#insn-00503abc)

~~~diff
- 0050379c ["INT_ADD", "register:40f0:8", ["const:50379c:8", "const:4:8"]]
- 0050379c ["CALL", null, ["callee:00c5ab40:8"]]
+ 00503abc ["INT_ADD", "register:40f0:8", ["const:503abc:8", "const:4:8"]]
+ 00503abc ["CALL", null, ["callee:00c5ab40:8"]]
- 0050379c bytes f5581d94
+ 00503abc bytes 215c1d94
~~~


<a id="compare-95d54710f8385a56ad74e792b01284d8"></a>

### [`00503dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503dd8.md) → [`005040f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005040f8.md) _ZNK5Botan10Data_StoreeqERKS0_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00548fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548fc8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005492e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005492e8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503dd8.md#insn-00503e24)
- 新版 [`00504144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005040f8.md#insn-00504144)

~~~diff
- 00503e24 ["INT_ADD", "register:40f0:8", ["const:503e24:8", "const:4:8"]]
- 00503e24 ["CALL", null, ["callee:005492e8:8"]]
+ 00504144 ["INT_ADD", "register:40f0:8", ["const:504144:8", "const:4:8"]]
+ 00504144 ["CALL", null, ["callee:005492e8:8"]]
- 00503e24 bytes 69140194
+ 00504144 bytes 69140194
~~~


<a id="compare-c2086d8e37d8f0fb0bd72d771237b1a6"></a>

### [`00503eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503eb4.md) → [`005041d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005041d4.md) _ZNK5Botan10Data_Store9has_valueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503eb4.md#insn-00503f20)
- 新版 [`00504240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005041d4.md#insn-00504240)

~~~diff
- 00503f20 ["INT_ADD", "register:40f0:8", ["const:503f20:8", "const:4:8"]]
- 00503f20 ["CALL", null, ["callee:00c590f0:8"]]
+ 00504240 ["INT_ADD", "register:40f0:8", ["const:504240:8", "const:4:8"]]
+ 00504240 ["CALL", null, ["callee:00c590f0:8"]]
- 00503f20 bytes 80501d94
+ 00504240 bytes ac531d94
~~~


<a id="compare-9a501f959cd0ae9d8b176f24d7e1172d"></a>

### [`00503f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503f74.md) → [`00504294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504294.md) _ZNK5Botan10Data_Store10search_forENSt6__ndk18functionIFbNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_EEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ba0.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00549114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5ab70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab70.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00549434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/00549434.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00504004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503f74.md#insn-00504004) · [`00504030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503f74.md#insn-00504030) · [`0050404c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503f74.md#insn-0050404c)
- 新版 [`00504324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504294.md#insn-00504324) · [`00504350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504294.md#insn-00504350) · [`0050436c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504294.md#insn-0050436c)

~~~diff
- 00504004 ["INT_ADD", "register:40f0:8", ["const:504004:8", "const:4:8"]]
- 00504004 ["CALL", null, ["callee:0043be80:8"]]
+ 00504324 ["INT_ADD", "register:40f0:8", ["const:504324:8", "const:4:8"]]
+ 00504324 ["CALL", null, ["callee:0043be80:8"]]
- 00504004 bytes d7defc97
+ 00504324 bytes d7defc97
- 00504030 ["INT_ADD", "register:40f0:8", ["const:504030:8", "const:4:8"]]
- 00504030 ["CALL", null, ["callee:0043be80:8"]]
+ 00504350 ["INT_ADD", "register:40f0:8", ["const:504350:8", "const:4:8"]]
+ 00504350 ["CALL", null, ["callee:0043be80:8"]]
- 00504030 bytes ccdefc97
+ 00504350 bytes ccdefc97
- 0050404c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050404c ["INT_ADD", "register:40f0:8", ["const:50404c:8", "const:4:8"]]
- 0050404c ["CALLIND", null, ["register:0:8"]]
+ 0050436c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050436c ["INT_ADD", "register:40f0:8", ["const:50436c:8", "const:4:8"]]
+ 0050436c ["CALLIND", null, ["register:0:8"]]
- 0050404c bytes 00013fd6
+ 0050436c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53fc3160144add843d9b975c063500b0"></a>

### [`00504200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504200.md) → [`00504520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504520.md) _ZNK5Botan10Data_Store3getERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bb0.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md)
- 新版 呼出元 1件 [`00c5ab80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab80.md) · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md) [`005483f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005483f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050421c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504200.md#insn-0050421c) · [`00504274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504200.md#insn-00504274) · [`00504288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504200.md#insn-00504288)
- 新版 [`0050453c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504520.md#insn-0050453c) · [`00504594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504520.md#insn-00504594) · [`005045a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504520.md#insn-005045a8)

~~~diff
- 0050421c ["INT_ADD", "register:40f0:8", ["const:50421c:8", "const:4:8"]]
- 0050421c ["CALL", null, ["callee:005483f8:8"]]
+ 0050453c ["INT_ADD", "register:40f0:8", ["const:50453c:8", "const:4:8"]]
+ 0050453c ["CALL", null, ["callee:005483f8:8"]]
- 0050421c bytes af0f0194
+ 0050453c bytes af0f0194
- 00504274 ["INT_ADD", "register:40f0:8", ["const:504274:8", "const:4:8"]]
- 00504274 ["CALL", null, ["callee:005410dc:8"]]
+ 00504594 ["INT_ADD", "register:40f0:8", ["const:504594:8", "const:4:8"]]
+ 00504594 ["CALL", null, ["callee:005410dc:8"]]
- 00504274 bytes d2f20094
+ 00504594 bytes d2f20094
- 00504288 ["INT_ADD", "register:40f0:8", ["const:504288:8", "const:4:8"]]
- 00504288 ["CALL", null, ["callee:0043be80:8"]]
+ 005045a8 ["INT_ADD", "register:40f0:8", ["const:5045a8:8", "const:4:8"]]
+ 005045a8 ["CALL", null, ["callee:0043be80:8"]]
- 00504288 bytes 36defc97
+ 005045a8 bytes 36defc97
~~~


<a id="compare-79d33ea0e2cb05abc2c684770cd082d6"></a>

### [`00504a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504a08.md) → [`00504d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504d28.md) _ZN5Botan10Data_Store3addERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00504a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504a08.md#insn-00504a38) · [`00504a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504a08.md#insn-00504a48) · [`00504a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504a08.md#insn-00504a58)
- 新版 [`00504d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504d28.md#insn-00504d58) · [`00504d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504d28.md#insn-00504d68) · [`00504d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504d28.md#insn-00504d78)

~~~diff
- 00504a38 ["INT_ADD", "register:40f0:8", ["const:504a38:8", "const:4:8"]]
- 00504a38 ["CALL", null, ["callee:00c59830:8"]]
+ 00504d58 ["INT_ADD", "register:40f0:8", ["const:504d58:8", "const:4:8"]]
+ 00504d58 ["CALL", null, ["callee:00c59830:8"]]
- 00504a38 bytes 8a4f1d94
+ 00504d58 bytes b6521d94
- 00504a48 ["INT_ADD", "register:40f0:8", ["const:504a48:8", "const:4:8"]]
- 00504a48 ["CALL", null, ["callee:004ff500:8"]]
+ 00504d68 ["INT_ADD", "register:40f0:8", ["const:504d68:8", "const:4:8"]]
+ 00504d68 ["CALL", null, ["callee:004ff500:8"]]
- 00504a48 bytes e6e9ff97
+ 00504d68 bytes e6e9ff97
- 00504a58 ["INT_ADD", "register:40f0:8", ["const:504a58:8", "const:4:8"]]
- 00504a58 ["CALL", null, ["callee:00c58f50:8"]]
+ 00504d78 ["INT_ADD", "register:40f0:8", ["const:504d78:8", "const:4:8"]]
+ 00504d78 ["CALL", null, ["callee:00c58f50:8"]]
- 00504a58 bytes 4a4d1d94
+ 00504d78 bytes 76501d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c245e416b39c2f5ee03c59dee8605df"></a>

### [`00504dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504dd0.md) → [`005050f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/005050f0.md) _ZN5Botan10Data_Store3addERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pai

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bbb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053bed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00504e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504dd0.md#insn-00504e0c)
- 新版 [`0050512c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/005050f0.md#insn-0050512c)

~~~diff
- 00504e0c ["INT_ADD", "register:40f0:8", ["const:504e0c:8", "const:4:8"]]
- 00504e0c ["CALL", null, ["callee:0053bed0:8"]]
+ 0050512c ["INT_ADD", "register:40f0:8", ["const:50512c:8", "const:4:8"]]
+ 0050512c ["CALL", null, ["callee:0053bed0:8"]]
- 00504e0c bytes 69db0094
+ 0050512c bytes 69db0094
~~~


<a id="compare-31c145b49d51947cd576529ab339383f"></a>

### [`00505014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505014.md) → [`00505334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505334.md) _ZN5Botan7X509_DN13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5aba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00505044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505014.md#insn-00505044) · [`00505054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505014.md#insn-00505054) · [`00505064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505014.md#insn-00505064)
- 新版 [`00505364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505334.md#insn-00505364) · [`00505374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505334.md#insn-00505374) · [`00505384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505334.md#insn-00505384)

~~~diff
- 00505044 ["INT_ADD", "register:40f0:8", ["const:505044:8", "const:4:8"]]
- 00505044 ["CALL", null, ["callee:00c59720:8"]]
+ 00505364 ["INT_ADD", "register:40f0:8", ["const:505364:8", "const:4:8"]]
+ 00505364 ["CALL", null, ["callee:00c59720:8"]]
- 00505044 bytes c34d1d94
+ 00505364 bytes ef501d94
- 00505054 ["INT_ADD", "register:40f0:8", ["const:505054:8", "const:4:8"]]
- 00505054 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00505374 ["INT_ADD", "register:40f0:8", ["const:505374:8", "const:4:8"]]
+ 00505374 ["CALL", null, ["callee:00c5aba0:8"]]
- 00505054 bytes df521d94
+ 00505374 bytes 0b561d94
- 00505064 ["INT_ADD", "register:40f0:8", ["const:505064:8", "const:4:8"]]
- 00505064 ["CALL", null, ["callee:00c58f50:8"]]
+ 00505384 ["INT_ADD", "register:40f0:8", ["const:505384:8", "const:4:8"]]
+ 00505384 ["CALL", null, ["callee:00c58f50:8"]]
- 00505064 bytes c74b1d94
+ 00505384 bytes f34e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c507cab3513ac195ae227cbfe133a03"></a>

### [`00505314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505314.md) → [`00505634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505634.md) FUN_00505634

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)
- 新版 呼出元 2件 [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) · 呼出先 2件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050532c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505314.md#insn-0050532c)
- 新版 [`0050564c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505634.md#insn-0050564c)

~~~diff
- 0050532c ["INT_ADD", "register:40f0:8", ["const:50532c:8", "const:4:8"]]
- 0050532c ["CALL", null, ["callee:0053b2f0:8"]]
+ 0050564c ["INT_ADD", "register:40f0:8", ["const:50564c:8", "const:4:8"]]
+ 0050564c ["CALL", null, ["callee:0053b2f0:8"]]
- 0050532c bytes 29d70094
+ 0050564c bytes 29d70094
~~~


<a id="compare-cf86e377688011973af74709d4341222"></a>

### [`00507af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507af4.md) → [`00507e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/00507e14.md) _ZNK5Botan16X509_Certificate16subject_alt_nameEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 1件 [`005076cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md) · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00507afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507af4.md#insn-00507afc)
- 新版 [`00507e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/00507e14.md#insn-00507e1c)

~~~diff
- 00507afc ["INT_ADD", "register:40f0:8", ["const:507afc:8", "const:4:8"]]
- 00507afc ["CALL", null, ["callee:00c5aa90:8"]]
+ 00507e1c ["INT_ADD", "register:40f0:8", ["const:507e1c:8", "const:4:8"]]
+ 00507e1c ["CALL", null, ["callee:00c5aa90:8"]]
- 00507afc bytes f1471d94
+ 00507e1c bytes 1d4b1d94
~~~


<a id="compare-99bce9b2301ac6c12f4325ebf38c5224"></a>

### [`00507e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507e44.md) → [`00508164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508164.md) _ZNK5Botan7X509_DN13get_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c30.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`0054b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b2b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5ac00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac00.md) · 呼出先 7件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md) [`0054b5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054b5d4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00507e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507e44.md#insn-00507e78) · [`00507e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507e44.md#insn-00507e84) · [`00507e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507e44.md#insn-00507e94)
- 新版 [`00508198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508164.md#insn-00508198) · [`005081a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508164.md#insn-005081a4) · [`005081b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508164.md#insn-005081b4)

~~~diff
- 00507e78 ["INT_ADD", "register:40f0:8", ["const:507e78:8", "const:4:8"]]
- 00507e78 ["CALL", null, ["callee:00c5ac10:8"]]
+ 00508198 ["INT_ADD", "register:40f0:8", ["const:508198:8", "const:4:8"]]
+ 00508198 ["CALL", null, ["callee:00c5ac10:8"]]
- 00507e78 bytes 72471d94
+ 00508198 bytes 9e4a1d94
- 00507e84 ["INT_ADD", "register:40f0:8", ["const:507e84:8", "const:4:8"]]
- 00507e84 ["CALL", null, ["callee:00c59720:8"]]
+ 005081a4 ["INT_ADD", "register:40f0:8", ["const:5081a4:8", "const:4:8"]]
+ 005081a4 ["CALL", null, ["callee:00c59720:8"]]
- 00507e84 bytes 33421d94
+ 005081a4 bytes 5f451d94
- 00507e94 ["INT_ADD", "register:40f0:8", ["const:507e94:8", "const:4:8"]]
- 00507e94 ["CALL", null, ["callee:00c58f50:8"]]
+ 005081b4 ["INT_ADD", "register:40f0:8", ["const:5081b4:8", "const:4:8"]]
+ 005081b4 ["CALL", null, ["callee:00c58f50:8"]]
- 00507e94 bytes 3b401d94
+ 005081b4 bytes 67431d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0011cc224d695750e8b5c6215a114175"></a>

### [`00508b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508b4c.md) → [`00508e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508e6c.md) _ZNK5Botan7X509_DN14get_attributesEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59af0.md) · 呼出先 4件 [`0054b0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b0ac.md) [`0054b1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b1dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5aac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aac0.md) · 呼出先 4件 [`0054b3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054b3cc.md) [`0054b4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054b4fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508b4c.md#insn-00508bcc) · [`00508bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508b4c.md#insn-00508bd8) · [`00508be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508b4c.md#insn-00508be8)
- 新版 [`00508eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508e6c.md#insn-00508eec) · [`00508ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508e6c.md#insn-00508ef8) · [`00508f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508e6c.md#insn-00508f08)

~~~diff
- 00508bcc ["INT_ADD", "register:40f0:8", ["const:508bcc:8", "const:4:8"]]
- 00508bcc ["CALL", null, ["callee:0054b4fc:8"]]
+ 00508eec ["INT_ADD", "register:40f0:8", ["const:508eec:8", "const:4:8"]]
+ 00508eec ["CALL", null, ["callee:0054b4fc:8"]]
- 00508bcc bytes 84090194
+ 00508eec bytes 84090194
- 00508bd8 ["INT_ADD", "register:40f0:8", ["const:508bd8:8", "const:4:8"]]
- 00508bd8 ["CALL", null, ["callee:0054b3cc:8"]]
+ 00508ef8 ["INT_ADD", "register:40f0:8", ["const:508ef8:8", "const:4:8"]]
+ 00508ef8 ["CALL", null, ["callee:0054b3cc:8"]]
- 00508bd8 bytes 35090194
+ 00508ef8 bytes 35090194
- 00508be8 ["INT_ADD", "register:40f0:8", ["const:508be8:8", "const:4:8"]]
- 00508be8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00508f08 ["INT_ADD", "register:40f0:8", ["const:508f08:8", "const:4:8"]]
+ 00508f08 ["CALL", null, ["callee:00c58f50:8"]]
- 00508be8 bytes e63c1d94
+ 00508f08 bytes 12401d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10bfb87e66f528b53af69fa1cd14c513"></a>

### [`00508d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d44.md) → [`00509064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509064.md) FUN_00509064

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d44.md#insn-00508d60)
- 新版 [`00509080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509064.md#insn-00509080)

~~~diff
- 00508d60 ["INT_ADD", "register:40f0:8", ["const:508d60:8", "const:4:8"]]
- 00508d60 ["CALL", null, ["callee:00c58f50:8"]]
+ 00509080 ["INT_ADD", "register:40f0:8", ["const:509080:8", "const:4:8"]]
+ 00509080 ["CALL", null, ["callee:00c58f50:8"]]
- 00508d60 bytes 883c1d94
+ 00509080 bytes b43f1d94
~~~


<a id="compare-dfa0e396efe55fe02a46daf8fb4a9c01"></a>

### [`00509168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509168.md) → [`00509488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509488.md) FUN_00509488

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509168.md#insn-00509184)
- 新版 [`005094a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509488.md#insn-005094a4)

~~~diff
- 00509184 ["INT_ADD", "register:40f0:8", ["const:509184:8", "const:4:8"]]
- 00509184 ["CALL", null, ["callee:00c58f50:8"]]
+ 005094a4 ["INT_ADD", "register:40f0:8", ["const:5094a4:8", "const:4:8"]]
+ 005094a4 ["CALL", null, ["callee:00c58f50:8"]]
- 00509184 bytes 7f3b1d94
+ 005094a4 bytes ab3e1d94
~~~


<a id="compare-fa75811127d049d5d2ac4a25f39251a2"></a>

### [`005097e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005097e0.md) → [`00509b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509b00.md) _ZN5BotanneERKNS_7X509_DNES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005097e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005097e0.md#insn-005097e8)
- 新版 [`00509b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509b00.md#insn-00509b08)

~~~diff
- 005097e8 ["INT_ADD", "register:40f0:8", ["const:5097e8:8", "const:4:8"]]
- 005097e8 ["CALL", null, ["callee:00c5aab0:8"]]
+ 00509b08 ["INT_ADD", "register:40f0:8", ["const:509b08:8", "const:4:8"]]
+ 00509b08 ["CALL", null, ["callee:00c5aab0:8"]]
- 005097e8 bytes be401d94
+ 00509b08 bytes ea431d94
~~~


<a id="compare-40c2cae52bfae8be54ff7726ae5ffaf5"></a>

### [`00509bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509bb8.md) → [`00509ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ed8.md) _ZNK5Botan4OCSP7Request13base64_encodeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ca0.md) [`00c59c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59c70.md) [`00c5ac50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509bb8.md#insn-00509bdc) · [`00509bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509bb8.md#insn-00509bec) · [`00509bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509bb8.md#insn-00509bfc)
- 新版 [`00509efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ed8.md#insn-00509efc) · [`00509f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ed8.md#insn-00509f0c) · [`00509f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ed8.md#insn-00509f1c)

~~~diff
- 00509bdc ["INT_ADD", "register:40f0:8", ["const:509bdc:8", "const:4:8"]]
- 00509bdc ["CALL", null, ["callee:00c5ac50:8"]]
+ 00509efc ["INT_ADD", "register:40f0:8", ["const:509efc:8", "const:4:8"]]
+ 00509efc ["CALL", null, ["callee:00c5ac50:8"]]
- 00509bdc bytes 29401d94
+ 00509efc bytes 55431d94
- 00509bec ["INT_ADD", "register:40f0:8", ["const:509bec:8", "const:4:8"]]
- 00509bec ["CALL", null, ["callee:00c59c70:8"]]
+ 00509f0c ["INT_ADD", "register:40f0:8", ["const:509f0c:8", "const:4:8"]]
+ 00509f0c ["CALL", null, ["callee:00c59c70:8"]]
- 00509bec bytes 2d3c1d94
+ 00509f0c bytes 593f1d94
- 00509bfc ["INT_ADD", "register:40f0:8", ["const:509bfc:8", "const:4:8"]]
- 00509bfc ["CALL", null, ["callee:00c58f50:8"]]
+ 00509f1c ["INT_ADD", "register:40f0:8", ["const:509f1c:8", "const:4:8"]]
+ 00509f1c ["CALL", null, ["callee:00c58f50:8"]]
- 00509bfc bytes e1381d94
+ 00509f1c bytes 0d3c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38b22fb88961560bca09948a66595210"></a>

### [`0050b39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b39c.md) → [`0050b6bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b6bc.md) FUN_0050b6bc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) · 呼出先 2件 [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`005110b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md) · 呼出先 2件 [`0053b784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b784.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b39c.md#insn-0050b3b8) · [`0050b3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b39c.md#insn-0050b3f0)
- 新版 [`0050b6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b6bc.md#insn-0050b6d8) · [`0050b710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b6bc.md#insn-0050b710)

~~~diff
- 0050b3b8 ["INT_ADD", "register:40f0:8", ["const:50b3b8:8", "const:4:8"]]
- 0050b3b8 ["CALL", null, ["callee:0053b784:8"]]
+ 0050b6d8 ["INT_ADD", "register:40f0:8", ["const:50b6d8:8", "const:4:8"]]
+ 0050b6d8 ["CALL", null, ["callee:0053b784:8"]]
- 0050b3b8 bytes 2bc00094
+ 0050b6d8 bytes 2bc00094
- 0050b3f0 ["INT_ADD", "register:40f0:8", ["const:50b3f0:8", "const:4:8"]]
- 0050b3f0 ["CALL", null, ["callee:00c58f50:8"]]
+ 0050b710 ["INT_ADD", "register:40f0:8", ["const:50b710:8", "const:4:8"]]
+ 0050b710 ["CALL", null, ["callee:00c58f50:8"]]
- 0050b3f0 bytes e4321d94
+ 0050b710 bytes 10361d94
~~~


<a id="compare-982a1db0c423c4150f82da1c8527aa05"></a>

### [`0050b420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b420.md) → [`0050b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b740.md) FUN_0050b740

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054067c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054067c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054099c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054099c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b420.md#insn-0050b458)
- 新版 [`0050b778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b740.md#insn-0050b778)

~~~diff
- 0050b458 ["INT_ADD", "register:40f0:8", ["const:50b458:8", "const:4:8"]]
- 0050b458 ["CALL", null, ["callee:0054099c:8"]]
+ 0050b778 ["INT_ADD", "register:40f0:8", ["const:50b778:8", "const:4:8"]]
+ 0050b778 ["CALL", null, ["callee:0054099c:8"]]
- 0050b458 bytes 89d40094
+ 0050b778 bytes 89d40094
~~~


<a id="compare-a7a9a900710eb3924ad50d114020d89d"></a>

### [`0050b48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b48c.md) → [`0050b7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b7ac.md) FUN_0050b7ac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b48c.md#insn-0050b4cc)
- 新版 [`0050b7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b7ac.md#insn-0050b7ec)

~~~diff
- 0050b4cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0050b4cc ["INT_ADD", "register:40f0:8", ["const:50b4cc:8", "const:4:8"]]
- 0050b4cc ["CALLIND", null, ["register:0:8"]]
+ 0050b7ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050b7ec ["INT_ADD", "register:40f0:8", ["const:50b7ec:8", "const:4:8"]]
+ 0050b7ec ["CALLIND", null, ["register:0:8"]]
- 0050b4cc bytes 00013fd6
+ 0050b7ec bytes 00013fd6
~~~


<a id="compare-eac94a7d7a76a2d0b589e0f9ebad87f8"></a>

### [`0050c018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c018.md) → [`0050c338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c338.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_15Key_ConstraintsE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c018.md#insn-0050c02c) · [`0050c03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c018.md#insn-0050c03c)
- 新版 [`0050c34c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c338.md#insn-0050c34c) · [`0050c35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c338.md#insn-0050c35c)

~~~diff
- 0050c02c ["INT_ADD", "register:40f0:8", ["const:50c02c:8", "const:4:8"]]
- 0050c02c ["CALL", null, ["callee:00c5aa90:8"]]
+ 0050c34c ["INT_ADD", "register:40f0:8", ["const:50c34c:8", "const:4:8"]]
+ 0050c34c ["CALL", null, ["callee:00c5aa90:8"]]
- 0050c02c bytes a5361d94
+ 0050c34c bytes d1391d94
- 0050c03c ["INT_ADD", "register:40f0:8", ["const:50c03c:8", "const:4:8"]]
- 0050c03c ["CALL", null, ["callee:00c5aa90:8"]]
+ 0050c35c ["INT_ADD", "register:40f0:8", ["const:50c35c:8", "const:4:8"]]
+ 0050c35c ["CALL", null, ["callee:00c5aa90:8"]]
- 0050c03c bytes a1361d94
+ 0050c35c bytes cd391d94
~~~


<a id="compare-2ed6feb1ebad9da25534f04195a023a5"></a>

### [`0050c060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c060.md) → [`0050c380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c380.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d10.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 1件 [`00c5ace0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ace0.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c060.md#insn-0050c088) · [`0050c090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c060.md#insn-0050c090) · [`0050c104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c060.md#insn-0050c104)
- 新版 [`0050c3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c380.md#insn-0050c3a8) · [`0050c3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c380.md#insn-0050c3b0) · [`0050c424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c380.md#insn-0050c424)

~~~diff
- 0050c088 ["INT_ADD", "register:40f0:8", ["const:50c088:8", "const:4:8"]]
- 0050c088 ["CALL", null, ["callee:00c59720:8"]]
+ 0050c3a8 ["INT_ADD", "register:40f0:8", ["const:50c3a8:8", "const:4:8"]]
+ 0050c3a8 ["CALL", null, ["callee:00c59720:8"]]
- 0050c088 bytes b2311d94
+ 0050c3a8 bytes de341d94
- 0050c090 ["INT_ADD", "register:40f0:8", ["const:50c090:8", "const:4:8"]]
- 0050c090 ["CALL", null, ["callee:00c5aa90:8"]]
+ 0050c3b0 ["INT_ADD", "register:40f0:8", ["const:50c3b0:8", "const:4:8"]]
+ 0050c3b0 ["CALL", null, ["callee:00c5aa90:8"]]
- 0050c090 bytes 8c361d94
+ 0050c3b0 bytes b8391d94
- 0050c104 ["INT_ADD", "register:40f0:8", ["const:50c104:8", "const:4:8"]]
- 0050c104 ["CALL", null, ["callee:00c58f50:8"]]
+ 0050c424 ["INT_ADD", "register:40f0:8", ["const:50c424:8", "const:4:8"]]
+ 0050c424 ["CALL", null, ["callee:00c58f50:8"]]
- 0050c104 bytes 9f2f1d94
+ 0050c424 bytes cb321d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2091744cbd02d5dc5d97208d3d279926"></a>

### [`0050cc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc4c.md) → [`0050cf6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050cf6c.md) _ZNK5Botan16X509_Certificate13raw_issuer_dnEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc4c.md#insn-0050cc54)
- 新版 [`0050cf74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050cf6c.md#insn-0050cf74)

~~~diff
- 0050cc54 ["INT_ADD", "register:40f0:8", ["const:50cc54:8", "const:4:8"]]
- 0050cc54 ["CALL", null, ["callee:00c5aa90:8"]]
+ 0050cf74 ["INT_ADD", "register:40f0:8", ["const:50cf74:8", "const:4:8"]]
+ 0050cf74 ["CALL", null, ["callee:00c5aa90:8"]]
- 0050cc54 bytes 9b331d94
+ 0050cf74 bytes c7361d94
~~~


<a id="compare-cfb18f1b245bd4454b42c218d316c677"></a>

### [`0050cc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc64.md) → [`0050cf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050cf84.md) _ZNK5Botan4OCSP6CertID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md) [`00c58be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58be0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c59750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59750.md) [`00c59770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59770.md) [`00c598c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598c0.md) [`00c59bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc64.md#insn-0050cc84) · [`0050cc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc64.md#insn-0050cc98) · [`0050ccb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc64.md#insn-0050ccb0)
- 新版 [`0050cfa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050cf84.md#insn-0050cfa4) · [`0050cfb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050cf84.md#insn-0050cfb8) · [`0050cfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050cf84.md#insn-0050cfd0)

~~~diff
- 0050cc84 ["INT_ADD", "register:40f0:8", ["const:50cc84:8", "const:4:8"]]
- 0050cc84 ["CALL", null, ["callee:00c59750:8"]]
+ 0050cfa4 ["INT_ADD", "register:40f0:8", ["const:50cfa4:8", "const:4:8"]]
+ 0050cfa4 ["CALL", null, ["callee:00c59750:8"]]
- 0050cc84 bytes bf2e1d94
+ 0050cfa4 bytes eb311d94
- 0050cc98 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050cc98 ["INT_ADD", "register:40f0:8", ["const:50cc98:8", "const:4:8"]]
- 0050cc98 ["CALLIND", null, ["register:0:8"]]
+ 0050cfb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050cfb8 ["INT_ADD", "register:40f0:8", ["const:50cfb8:8", "const:4:8"]]
+ 0050cfb8 ["CALLIND", null, ["register:0:8"]]
- 0050cc98 bytes 00013fd6
+ 0050cfb8 bytes 00013fd6
- 0050ccb0 ["INT_ADD", "register:40f0:8", ["const:50ccb0:8", "const:4:8"]]
- 0050ccb0 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050cfd0 ["INT_ADD", "register:40f0:8", ["const:50cfd0:8", "const:4:8"]]
+ 0050cfd0 ["CALL", null, ["callee:00c598c0:8"]]
- 0050ccb0 bytes 102f1d94
+ 0050cfd0 bytes 3c321d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf5dd567fb259abbf01fb83cbab5546b"></a>

### [`0050dd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dd90.md) → [`0050e0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e0b0.md) FUN_0050e0b0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dd90.md#insn-0050ddac) · [`0050ddcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dd90.md#insn-0050ddcc)
- 新版 [`0050e0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e0b0.md#insn-0050e0cc) · [`0050e0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e0b0.md#insn-0050e0ec)

~~~diff
- 0050ddac ["INT_ADD", "register:40f0:8", ["const:50ddac:8", "const:4:8"]]
- 0050ddac ["CALL", null, ["callee:00c54d90:8"]]
+ 0050e0cc ["INT_ADD", "register:40f0:8", ["const:50e0cc:8", "const:4:8"]]
+ 0050e0cc ["CALL", null, ["callee:00c54d90:8"]]
- 0050ddac bytes fd171d94
+ 0050e0cc bytes 311b1d94
- 0050ddcc ["COPY", "register:0:8", ["register:4040:8"]]
- 0050ddcc ["INT_ADD", "register:40f0:8", ["const:50ddcc:8", "const:4:8"]]
- 0050ddcc ["CALLIND", null, ["register:0:8"]]
+ 0050e0ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050e0ec ["INT_ADD", "register:40f0:8", ["const:50e0ec:8", "const:4:8"]]
+ 0050e0ec ["CALLIND", null, ["register:0:8"]]
- 0050ddcc bytes 00013fd6
+ 0050e0ec bytes 00013fd6
~~~


<a id="compare-c21823af9e9ca0f8746c5d0cfb8539a0"></a>

### [`0050f0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0ac.md) → [`0050f3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f3cc.md) FUN_0050f3cc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054a46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a46c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054a78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a78c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0ac.md#insn-0050f0c8)
- 新版 [`0050f3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f3cc.md#insn-0050f3e8)

~~~diff
- 0050f0c8 ["INT_ADD", "register:40f0:8", ["const:50f0c8:8", "const:4:8"]]
- 0050f0c8 ["CALL", null, ["callee:0054a78c:8"]]
+ 0050f3e8 ["INT_ADD", "register:40f0:8", ["const:50f3e8:8", "const:4:8"]]
+ 0050f3e8 ["CALL", null, ["callee:0054a78c:8"]]
- 0050f0c8 bytes e9ec0094
+ 0050f3e8 bytes e9ec0094
~~~


<a id="compare-35e8e54d078f1095ec486ff0a1d676a6"></a>

### [`0050f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f1e4.md) → [`0050f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f504.md) _ZNK5Botan14PKCS10_Request18challenge_passwordEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c5ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f1e4.md#insn-0050f1f4)
- 新版 [`0050f514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f504.md#insn-0050f514)

~~~diff
- 0050f1f4 ["INT_ADD", "register:40f0:8", ["const:50f1f4:8", "const:4:8"]]
- 0050f1f4 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f514 ["INT_ADD", "register:40f0:8", ["const:50f514:8", "const:4:8"]]
+ 0050f514 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f1f4 bytes e72a1d94
+ 0050f514 bytes 132e1d94
~~~


<a id="compare-7a89e3f4f1df7262c5157f1145a2ff32"></a>

### [`0050f238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f238.md) → [`0050f558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f558.md) _ZNK5Botan14PKCS10_Request14raw_public_keyEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f238.md#insn-0050f240)
- 新版 [`0050f560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f558.md#insn-0050f560)

~~~diff
- 0050f240 ["INT_ADD", "register:40f0:8", ["const:50f240:8", "const:4:8"]]
- 0050f240 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f560 ["INT_ADD", "register:40f0:8", ["const:50f560:8", "const:4:8"]]
+ 0050f560 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f240 bytes d42a1d94
+ 0050f560 bytes 002e1d94
~~~


<a id="compare-315a551ab372efbb9eabcab0b0def395"></a>

### [`0050f250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f250.md) → [`0050f570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f570.md) _ZNK5Botan14PKCS10_Request16subject_alt_nameEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f250.md#insn-0050f258)
- 新版 [`0050f578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f570.md#insn-0050f578)

~~~diff
- 0050f258 ["INT_ADD", "register:40f0:8", ["const:50f258:8", "const:4:8"]]
- 0050f258 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f578 ["INT_ADD", "register:40f0:8", ["const:50f578:8", "const:4:8"]]
+ 0050f578 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f258 bytes ce2a1d94
+ 0050f578 bytes fa2d1d94
~~~


<a id="compare-b18f568be91890ad17045a37db9b2126"></a>

### [`0050f268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f268.md) → [`0050f588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f588.md) _ZNK5Botan14PKCS10_Request10extensionsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f268.md#insn-0050f270)
- 新版 [`0050f590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f588.md#insn-0050f590)

~~~diff
- 0050f270 ["INT_ADD", "register:40f0:8", ["const:50f270:8", "const:4:8"]]
- 0050f270 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f590 ["INT_ADD", "register:40f0:8", ["const:50f590:8", "const:4:8"]]
+ 0050f590 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f270 bytes c82a1d94
+ 0050f590 bytes f42d1d94
~~~


<a id="compare-703096608c6ca65300b509a8c880935f"></a>

### [`0050f3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f3f8.md) → [`0050f718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f718.md) _ZNK5Botan10Extensions3getERKNS_3OIDE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f3f8.md#insn-0050f408) · [`0050f418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f3f8.md#insn-0050f418)
- 新版 [`0050f728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f718.md#insn-0050f728) · [`0050f738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f718.md#insn-0050f738)

~~~diff
- 0050f408 ["INT_ADD", "register:40f0:8", ["const:50f408:8", "const:4:8"]]
- 0050f408 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0050f728 ["INT_ADD", "register:40f0:8", ["const:50f728:8", "const:4:8"]]
+ 0050f728 ["CALL", null, ["callee:00c5ab60:8"]]
- 0050f408 bytes e2291d94
+ 0050f728 bytes 0e2d1d94
- 0050f418 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f418 ["INT_ADD", "register:40f0:8", ["const:50f418:8", "const:4:8"]]
- 0050f418 ["CALLIND", null, ["register:0:8"]]
+ 0050f738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f738 ["INT_ADD", "register:40f0:8", ["const:50f738:8", "const:4:8"]]
+ 0050f738 ["CALLIND", null, ["register:0:8"]]
- 0050f418 bytes 00013fd6
+ 0050f738 bytes 00013fd6
~~~


<a id="compare-c6be94d71f1e4ca66ab3987ebe21f308"></a>

### [`0050ff50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff50.md) → [`00510270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510270.md) _ZNK5Botan16X509_Certificate10is_CA_certEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ff58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff50.md#insn-0050ff58)
- 新版 [`00510278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510270.md#insn-00510278)

~~~diff
- 0050ff58 ["INT_ADD", "register:40f0:8", ["const:50ff58:8", "const:4:8"]]
- 0050ff58 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00510278 ["INT_ADD", "register:40f0:8", ["const:510278:8", "const:4:8"]]
+ 00510278 ["CALL", null, ["callee:00c5aa90:8"]]
- 0050ff58 bytes da261d94
+ 00510278 bytes 062a1d94
~~~


<a id="compare-4ab41e03e75c97abdf026b19e1a34fd3"></a>

### [`0050ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff68.md) → [`00510288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510288.md) FUN_00510288

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`0050fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fda8.md) · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ff8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff68.md#insn-0050ff8c) · [`0050ffd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff68.md#insn-0050ffd4) · [`0050fff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff68.md#insn-0050fff4)
- 新版 [`005102ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510288.md#insn-005102ac) · [`005102f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510288.md#insn-005102f4) · [`00510314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510288.md#insn-00510314)

~~~diff
- 0050ff8c ["INT_ADD", "register:40f0:8", ["const:50ff8c:8", "const:4:8"]]
- 0050ff8c ["CALL", null, ["callee:00c59080:8"]]
+ 005102ac ["INT_ADD", "register:40f0:8", ["const:5102ac:8", "const:4:8"]]
+ 005102ac ["CALL", null, ["callee:00c59080:8"]]
- 0050ff8c bytes 49201d94
+ 005102ac bytes 75231d94
- 0050ffd4 ["INT_ADD", "register:40f0:8", ["const:50ffd4:8", "const:4:8"]]
- 0050ffd4 ["CALL", null, ["callee:00c58f30:8"]]
+ 005102f4 ["INT_ADD", "register:40f0:8", ["const:5102f4:8", "const:4:8"]]
+ 005102f4 ["CALL", null, ["callee:00c58f30:8"]]
- 0050ffd4 bytes e31f1d94
+ 005102f4 bytes 0f231d94
- 0050fff4 ["INT_ADD", "register:40f0:8", ["const:50fff4:8", "const:4:8"]]
- 0050fff4 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00510314 ["INT_ADD", "register:40f0:8", ["const:510314:8", "const:4:8"]]
+ 00510314 ["CALL", null, ["callee:00c58fe0:8"]]
- 0050fff4 bytes 07201d94
+ 00510314 bytes 33231d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5f2413b78125d5b55d7dc9474554842"></a>

### [`0051005c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/0051005c.md) → [`0051037c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/0051037c.md) FUN_0051037c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`0073d7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073d/0073d7fc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 9件 [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0061491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00614/0061491c.md) [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`0073dbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073d/0073dbac.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/0051005c.md#insn-00510078)
- 新版 [`00510398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/0051037c.md#insn-00510398)

~~~diff
- 00510078 ["INT_ADD", "register:40f0:8", ["const:510078:8", "const:4:8"]]
- 00510078 ["CALL", null, ["callee:00c58f50:8"]]
+ 00510398 ["INT_ADD", "register:40f0:8", ["const:510398:8", "const:4:8"]]
+ 00510398 ["CALL", null, ["callee:00c58f50:8"]]
- 00510078 bytes c21f1d94
+ 00510398 bytes ee221d94
~~~


<a id="compare-50212c35cb9ebbd5ba6c1684fa481726"></a>

### [`00511678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511678.md) → [`00511998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511998.md) FUN_00511998

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`005110b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005116c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511678.md#insn-005116c0)
- 新版 [`005119e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511998.md#insn-005119e0)

~~~diff
- 005116c0 ["INT_ADD", "register:40f0:8", ["const:5116c0:8", "const:4:8"]]
- 005116c0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005119e0 ["INT_ADD", "register:40f0:8", ["const:5119e0:8", "const:4:8"]]
+ 005119e0 ["CALL", null, ["callee:00c58f50:8"]]
- 005116c0 bytes 301a1d94
+ 005119e0 bytes 5c1d1d94
~~~


<a id="compare-1f3c2fb44140a3d00276bf458a370901"></a>

### [`00511d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511d04.md) → [`00512024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512024.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c59e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59620.md) [`00c5ae10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511d04.md#insn-00511d38) · [`00511d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511d04.md#insn-00511d60) · [`00511db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511d04.md#insn-00511db0)
- 新版 [`00512058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512024.md#insn-00512058) · [`00512080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512024.md#insn-00512080) · [`005120d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512024.md#insn-005120d0)

~~~diff
- 00511d38 ["INT_ADD", "register:40f0:8", ["const:511d38:8", "const:4:8"]]
- 00511d38 ["CALL", null, ["callee:00c59620:8"]]
+ 00512058 ["INT_ADD", "register:40f0:8", ["const:512058:8", "const:4:8"]]
+ 00512058 ["CALL", null, ["callee:00c59620:8"]]
- 00511d38 bytes 461a1d94
+ 00512058 bytes 721d1d94
- 00511d60 ["INT_ADD", "register:40f0:8", ["const:511d60:8", "const:4:8"]]
- 00511d60 ["CALL", null, ["callee:00c5ae10:8"]]
+ 00512080 ["INT_ADD", "register:40f0:8", ["const:512080:8", "const:4:8"]]
+ 00512080 ["CALL", null, ["callee:00c5ae10:8"]]
- 00511d60 bytes 38201d94
+ 00512080 bytes 64231d94
- 00511db0 ["INT_ADD", "register:40f0:8", ["const:511db0:8", "const:4:8"]]
- 00511db0 ["CALL", null, ["callee:00c58f80:8"]]
+ 005120d0 ["INT_ADD", "register:40f0:8", ["const:5120d0:8", "const:4:8"]]
+ 005120d0 ["CALL", null, ["callee:00c58f80:8"]]
- 00511db0 bytes 80181d94
+ 005120d0 bytes ac1b1d94
~~~


<a id="compare-00dc3498b430d941b924c9c2e24edaed"></a>

### [`00511db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511db4.md) → [`005120d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/005120d4.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorENSt6__ndk16chrono10time_pointINS4_12system_clockENS4_8durationIxNS3_5ratioILl1ELl1000

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5ae10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511db4.md#insn-00511dec) · [`00511e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511db4.md#insn-00511e38)
- 新版 [`0051210c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/005120d4.md#insn-0051210c) · [`00512158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/005120d4.md#insn-00512158)

~~~diff
- 00511dec ["INT_ADD", "register:40f0:8", ["const:511dec:8", "const:4:8"]]
- 00511dec ["CALL", null, ["callee:00c5ae10:8"]]
+ 0051210c ["INT_ADD", "register:40f0:8", ["const:51210c:8", "const:4:8"]]
+ 0051210c ["CALL", null, ["callee:00c5ae10:8"]]
- 00511dec bytes 15201d94
+ 0051210c bytes 41231d94
- 00511e38 ["INT_ADD", "register:40f0:8", ["const:511e38:8", "const:4:8"]]
- 00511e38 ["CALL", null, ["callee:00c58f80:8"]]
+ 00512158 ["INT_ADD", "register:40f0:8", ["const:512158:8", "const:4:8"]]
+ 00512158 ["CALL", null, ["callee:00c58f80:8"]]
- 00511e38 bytes 5e181d94
+ 00512158 bytes 8a1b1d94
~~~


<a id="compare-0969c3c569338027677a2183c31f48d6"></a>

### [`00511e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511e3c.md) → [`0051215c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/0051215c.md) _ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c59e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59620.md) [`00c5ae20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511e3c.md#insn-00511e68)
- 新版 [`00512188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/0051215c.md#insn-00512188)

~~~diff
- 00511e68 ["INT_ADD", "register:40f0:8", ["const:511e68:8", "const:4:8"]]
- 00511e68 ["CALL", null, ["callee:00c59620:8"]]
+ 00512188 ["INT_ADD", "register:40f0:8", ["const:512188:8", "const:4:8"]]
+ 00512188 ["CALL", null, ["callee:00c59620:8"]]
- 00511e68 bytes fa191d94
+ 00512188 bytes 261d1d94
~~~


<a id="compare-4a14a3c5e3325cd471e3e377d9e348e3"></a>

### [`005126d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005126d0.md) → [`005129f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/005129f0.md) FUN_005129f0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051271c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005126d0.md#insn-0051271c) · [`00512730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005126d0.md#insn-00512730) · [`00512738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005126d0.md#insn-00512738)
- 新版 [`00512a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/005129f0.md#insn-00512a3c) · [`00512a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/005129f0.md#insn-00512a50) · [`00512a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/005129f0.md#insn-00512a58)

~~~diff
- 0051271c ["INT_ADD", "register:40f0:8", ["const:51271c:8", "const:4:8"]]
- 0051271c ["CALL", null, ["callee:00c54d90:8"]]
+ 00512a3c ["INT_ADD", "register:40f0:8", ["const:512a3c:8", "const:4:8"]]
+ 00512a3c ["CALL", null, ["callee:00c54d90:8"]]
- 0051271c bytes a1051d94
+ 00512a3c bytes d5081d94
- 00512730 ["COPY", "register:0:8", ["register:4040:8"]]
- 00512730 ["INT_ADD", "register:40f0:8", ["const:512730:8", "const:4:8"]]
- 00512730 ["CALLIND", null, ["register:0:8"]]
+ 00512a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00512a50 ["INT_ADD", "register:40f0:8", ["const:512a50:8", "const:4:8"]]
+ 00512a50 ["CALLIND", null, ["register:0:8"]]
- 00512730 bytes 00013fd6
+ 00512a50 bytes 00013fd6
- 00512738 ["INT_ADD", "register:40f0:8", ["const:512738:8", "const:4:8"]]
- 00512738 ["CALL", null, ["callee:00c58f20:8"]]
+ 00512a58 ["INT_ADD", "register:40f0:8", ["const:512a58:8", "const:4:8"]]
+ 00512a58 ["CALL", null, ["callee:00c58f20:8"]]
- 00512738 bytes 06161d94
+ 00512a58 bytes 32191d94
~~~


<a id="compare-2997617dd9c8fd3582e1dab2cbb849e7"></a>

### [`00512768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512768.md) → [`00512a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512a88.md) _ZNK5Botan8X509_CRL11get_revokedEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512768.md#insn-00512770)
- 新版 [`00512a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512a88.md#insn-00512a90)

~~~diff
- 00512770 ["INT_ADD", "register:40f0:8", ["const:512770:8", "const:4:8"]]
- 00512770 ["CALL", null, ["callee:00c5aaf0:8"]]
+ 00512a90 ["INT_ADD", "register:40f0:8", ["const:512a90:8", "const:4:8"]]
+ 00512a90 ["CALL", null, ["callee:00c5aaf0:8"]]
- 00512770 bytes ec1c1d94
+ 00512a90 bytes 18201d94
~~~


<a id="compare-8f3c3ef78ac1fd900e1c96bf8af4d68f"></a>

### [`00512780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512780.md) → [`00512aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512aa0.md) _ZNK5Botan8X509_CRL10crl_numberEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512780.md#insn-00512788)
- 新版 [`00512aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512aa0.md#insn-00512aa8)

~~~diff
- 00512788 ["INT_ADD", "register:40f0:8", ["const:512788:8", "const:4:8"]]
- 00512788 ["CALL", null, ["callee:00c5aaf0:8"]]
+ 00512aa8 ["INT_ADD", "register:40f0:8", ["const:512aa8:8", "const:4:8"]]
+ 00512aa8 ["CALL", null, ["callee:00c5aaf0:8"]]
- 00512788 bytes e61c1d94
+ 00512aa8 bytes 12201d94
~~~


<a id="compare-6392531d5faa1ad8523f6fa7603246e0"></a>

### [`005127ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005127ec.md) → [`00512b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512b0c.md) _ZN5Botan17choose_sig_formatERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorI

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`005103c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005127ec.md#insn-00512828) · [`00512838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005127ec.md#insn-00512838) · [`00512888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005127ec.md#insn-00512888)
- 新版 [`00512b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512b0c.md#insn-00512b48) · [`00512b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512b0c.md#insn-00512b58) · [`00512ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512b0c.md#insn-00512ba8)

~~~diff
- 00512828 ["INT_ADD", "register:40f0:8", ["const:512828:8", "const:4:8"]]
- 00512828 ["CALL", null, ["callee:005103c0:8"]]
+ 00512b48 ["INT_ADD", "register:40f0:8", ["const:512b48:8", "const:4:8"]]
+ 00512b48 ["CALL", null, ["callee:005103c0:8"]]
- 00512828 bytes 1ef6ff97
+ 00512b48 bytes 1ef6ff97
- 00512838 ["INT_ADD", "register:40f0:8", ["const:512838:8", "const:4:8"]]
- 00512838 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00512b58 ["INT_ADD", "register:40f0:8", ["const:512b58:8", "const:4:8"]]
+ 00512b58 ["CALL", null, ["callee:0046d7f0:8"]]
- 00512838 bytes 266bfd97
+ 00512b58 bytes 266bfd97
- 00512888 ["INT_ADD", "register:40f0:8", ["const:512888:8", "const:4:8"]]
- 00512888 ["CALL", null, ["callee:00c58f80:8"]]
+ 00512ba8 ["INT_ADD", "register:40f0:8", ["const:512ba8:8", "const:4:8"]]
+ 00512ba8 ["CALL", null, ["callee:00c58f80:8"]]
- 00512888 bytes ca151d94
+ 00512ba8 bytes f6181d94
~~~


<a id="compare-dc9ef66c31f74899309e7bcc8fbadb70"></a>

### [`005128b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005128b0.md) → [`00512bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512bd0.md) _ZNK5Botan8X509_CRL20alternate_PEM_labelsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005128ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005128b0.md#insn-005128ec) · [`005128fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005128b0.md#insn-005128fc) · [`0051294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005128b0.md#insn-0051294c)
- 新版 [`00512c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512bd0.md#insn-00512c0c) · [`00512c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512bd0.md#insn-00512c1c) · [`00512c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512bd0.md#insn-00512c6c)

~~~diff
- 005128ec ["INT_ADD", "register:40f0:8", ["const:5128ec:8", "const:4:8"]]
- 005128ec ["CALL", null, ["callee:004738a0:8"]]
+ 00512c0c ["INT_ADD", "register:40f0:8", ["const:512c0c:8", "const:4:8"]]
+ 00512c0c ["CALL", null, ["callee:004738a0:8"]]
- 005128ec bytes 2583fd97
+ 00512c0c bytes 2583fd97
- 005128fc ["INT_ADD", "register:40f0:8", ["const:5128fc:8", "const:4:8"]]
- 005128fc ["CALL", null, ["callee:00c58f50:8"]]
+ 00512c1c ["INT_ADD", "register:40f0:8", ["const:512c1c:8", "const:4:8"]]
+ 00512c1c ["CALL", null, ["callee:00c58f50:8"]]
- 005128fc bytes a1151d94
+ 00512c1c bytes cd181d94
- 0051294c ["INT_ADD", "register:40f0:8", ["const:51294c:8", "const:4:8"]]
- 0051294c ["CALL", null, ["callee:00c58f80:8"]]
+ 00512c6c ["INT_ADD", "register:40f0:8", ["const:512c6c:8", "const:4:8"]]
+ 00512c6c ["CALL", null, ["callee:00c58f80:8"]]
- 0051294c bytes 99151d94
+ 00512c6c bytes c5181d94
~~~


<a id="compare-1212a26bead0e7e9329e8c5ec4e86427"></a>

### [`00512a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512a54.md) → [`00512d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512d74.md) FUN_00512d74

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512a54.md#insn-00512a70) · [`00512a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512a54.md#insn-00512a90)
- 新版 [`00512d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512d74.md#insn-00512d90) · [`00512db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512d74.md#insn-00512db0)

~~~diff
- 00512a70 ["INT_ADD", "register:40f0:8", ["const:512a70:8", "const:4:8"]]
- 00512a70 ["CALL", null, ["callee:00c54d90:8"]]
+ 00512d90 ["INT_ADD", "register:40f0:8", ["const:512d90:8", "const:4:8"]]
+ 00512d90 ["CALL", null, ["callee:00c54d90:8"]]
- 00512a70 bytes cc041d94
+ 00512d90 bytes 00081d94
- 00512a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00512a90 ["INT_ADD", "register:40f0:8", ["const:512a90:8", "const:4:8"]]
- 00512a90 ["CALLIND", null, ["register:0:8"]]
+ 00512db0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00512db0 ["INT_ADD", "register:40f0:8", ["const:512db0:8", "const:4:8"]]
+ 00512db0 ["CALLIND", null, ["register:0:8"]]
- 00512a90 bytes 00013fd6
+ 00512db0 bytes 00013fd6
~~~


<a id="compare-f52c9a601a474100167e8a369964c3ec"></a>

### [`00512fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512fc8.md) → [`005132e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/005132e8.md) _ZNK5Botan8X509_CRL10is_revokedERKNS_16X509_CertificateE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e70.md) · 呼出先 10件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5ae40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae40.md) · 呼出先 10件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512fc8.md#insn-00513000) · [`0051300c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512fc8.md#insn-0051300c) · [`00513018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512fc8.md#insn-00513018)
- 新版 [`00513320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/005132e8.md#insn-00513320) · [`0051332c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/005132e8.md#insn-0051332c) · [`00513338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/005132e8.md#insn-00513338)

~~~diff
- 00513000 ["INT_ADD", "register:40f0:8", ["const:513000:8", "const:4:8"]]
- 00513000 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00513320 ["INT_ADD", "register:40f0:8", ["const:513320:8", "const:4:8"]]
+ 00513320 ["CALL", null, ["callee:00c5aa90:8"]]
- 00513000 bytes b01a1d94
+ 00513320 bytes dc1d1d94
- 0051300c ["INT_ADD", "register:40f0:8", ["const:51300c:8", "const:4:8"]]
- 0051300c ["CALL", null, ["callee:00c5aaf0:8"]]
+ 0051332c ["INT_ADD", "register:40f0:8", ["const:51332c:8", "const:4:8"]]
+ 0051332c ["CALL", null, ["callee:00c5aaf0:8"]]
- 0051300c bytes c51a1d94
+ 0051332c bytes f11d1d94
- 00513018 ["INT_ADD", "register:40f0:8", ["const:513018:8", "const:4:8"]]
- 00513018 ["CALL", null, ["callee:00c5aab0:8"]]
+ 00513338 ["INT_ADD", "register:40f0:8", ["const:513338:8", "const:4:8"]]
+ 00513338 ["CALL", null, ["callee:00c5aab0:8"]]
- 00513018 bytes b21a1d94
+ 00513338 bytes de1d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-739d60d4f482189a08832f0879b25681"></a>

### [`00513e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e54.md) → [`00514174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514174.md) FUN_00514174

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054aa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054aa8c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054adac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054adac.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e54.md#insn-00513e70)
- 新版 [`00514190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514174.md#insn-00514190)

~~~diff
- 00513e70 ["INT_ADD", "register:40f0:8", ["const:513e70:8", "const:4:8"]]
- 00513e70 ["CALL", null, ["callee:0054adac:8"]]
+ 00514190 ["INT_ADD", "register:40f0:8", ["const:514190:8", "const:4:8"]]
+ 00514190 ["CALL", null, ["callee:0054adac:8"]]
- 00513e70 bytes 07db0094
+ 00514190 bytes 07db0094
~~~


<a id="compare-69c4bb7cdc57007ed4400103fe7eb1e1"></a>

### [`00513f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513f8c.md) → [`005142ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005142ac.md) _ZNK5Botan8X509_CRL10extensionsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513f8c.md#insn-00513f94)
- 新版 [`005142b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005142ac.md#insn-005142b4)

~~~diff
- 00513f94 ["INT_ADD", "register:40f0:8", ["const:513f94:8", "const:4:8"]]
- 00513f94 ["CALL", null, ["callee:00c5aaf0:8"]]
+ 005142b4 ["INT_ADD", "register:40f0:8", ["const:5142b4:8", "const:4:8"]]
+ 005142b4 ["CALL", null, ["callee:00c5aaf0:8"]]
- 00513f94 bytes e3161d94
+ 005142b4 bytes 0f1a1d94
~~~


<a id="compare-5466575862361359afef32caeb9ac969"></a>

### [`00513fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513fa4.md) → [`005142c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005142c4.md) _ZNK5Botan8X509_CRL11next_updateEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513fa4.md#insn-00513fac)
- 新版 [`005142cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005142c4.md#insn-005142cc)

~~~diff
- 00513fac ["INT_ADD", "register:40f0:8", ["const:513fac:8", "const:4:8"]]
- 00513fac ["CALL", null, ["callee:00c5aaf0:8"]]
+ 005142cc ["INT_ADD", "register:40f0:8", ["const:5142cc:8", "const:4:8"]]
+ 005142cc ["CALL", null, ["callee:00c5aaf0:8"]]
- 00513fac bytes dd161d94
+ 005142cc bytes 091a1d94
~~~


<a id="compare-591332361e61fb9c1749260ebdbe3a1e"></a>

### [`00513fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513fbc.md) → [`005142dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005142dc.md) _ZNK5Botan8X509_CRL30crl_issuing_distribution_pointEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513fbc.md#insn-00513fcc)
- 新版 [`005142ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005142dc.md#insn-005142ec)

~~~diff
- 00513fcc ["INT_ADD", "register:40f0:8", ["const:513fcc:8", "const:4:8"]]
- 00513fcc ["CALL", null, ["callee:00c5aaf0:8"]]
+ 005142ec ["INT_ADD", "register:40f0:8", ["const:5142ec:8", "const:4:8"]]
+ 005142ec ["CALL", null, ["callee:00c5aaf0:8"]]
- 00513fcc bytes d5161d94
+ 005142ec bytes 011a1d94
~~~


<a id="compare-873df0bed8508595e8264bdf3ab72938"></a>

### [`005140f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005140f8.md) → [`00514418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514418.md) _ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md) · 呼出先 6件 [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) [`0054aeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054aeec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5aba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aba0.md) · 呼出先 6件 [`004ff6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff6dc.md) [`0054b20c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054b20c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005140f8.md#insn-00514148) · [`005141dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005140f8.md#insn-005141dc) · [`0051421c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005140f8.md#insn-0051421c)
- 新版 [`00514468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514418.md#insn-00514468) · [`005144fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514418.md#insn-005144fc) · [`0051453c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514418.md#insn-0051453c)

~~~diff
- 00514148 ["INT_ADD", "register:40f0:8", ["const:514148:8", "const:4:8"]]
- 00514148 ["CALL", null, ["callee:0054b20c:8"]]
+ 00514468 ["INT_ADD", "register:40f0:8", ["const:514468:8", "const:4:8"]]
+ 00514468 ["CALL", null, ["callee:0054b20c:8"]]
- 00514148 bytes 69db0094
+ 00514468 bytes 69db0094
- 005141dc ["INT_ADD", "register:40f0:8", ["const:5141dc:8", "const:4:8"]]
- 005141dc ["CALL", null, ["callee:00c590f0:8"]]
+ 005144fc ["INT_ADD", "register:40f0:8", ["const:5144fc:8", "const:4:8"]]
+ 005144fc ["CALL", null, ["callee:00c590f0:8"]]
- 005141dc bytes d10f1d94
+ 005144fc bytes fd121d94
- 0051421c ["INT_ADD", "register:40f0:8", ["const:51421c:8", "const:4:8"]]
- 0051421c ["CALL", null, ["callee:00c59990:8"]]
+ 0051453c ["INT_ADD", "register:40f0:8", ["const:51453c:8", "const:4:8"]]
+ 0051453c ["CALL", null, ["callee:00c59990:8"]]
- 0051421c bytes e9111d94
+ 0051453c bytes 15151d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07f333154a7a35c0d2970d9ed5b8e3ca"></a>

### [`0051440c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051440c.md) → [`0051472c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051472c.md) _ZNK5Botan7X509_DN8contentsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a80.md) · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md) [`00c58980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58980.md)
- 新版 呼出元 1件 [`00c5aa50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa50.md) · 呼出先 5件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c598a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598a0.md) [`00c59950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051440c.md#insn-00514488) · [`005144ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051440c.md#insn-005144ac) · [`005144bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051440c.md#insn-005144bc)
- 新版 [`005147a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051472c.md#insn-005147a8) · [`005147cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051472c.md#insn-005147cc) · [`005147dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051472c.md#insn-005147dc)

~~~diff
- 00514488 ["INT_ADD", "register:40f0:8", ["const:514488:8", "const:4:8"]]
- 00514488 ["CALL", null, ["callee:00c59950:8"]]
+ 005147a8 ["INT_ADD", "register:40f0:8", ["const:5147a8:8", "const:4:8"]]
+ 005147a8 ["CALL", null, ["callee:00c59950:8"]]
- 00514488 bytes 3e111d94
+ 005147a8 bytes 6a141d94
- 005144ac ["INT_ADD", "register:40f0:8", ["const:5144ac:8", "const:4:8"]]
- 005144ac ["CALL", null, ["callee:00c598a0:8"]]
+ 005147cc ["INT_ADD", "register:40f0:8", ["const:5147cc:8", "const:4:8"]]
+ 005147cc ["CALL", null, ["callee:00c598a0:8"]]
- 005144ac bytes 09111d94
+ 005147cc bytes 35141d94
- 005144bc ["INT_ADD", "register:40f0:8", ["const:5144bc:8", "const:4:8"]]
- 005144bc ["CALL", null, ["callee:00c58f50:8"]]
+ 005147dc ["INT_ADD", "register:40f0:8", ["const:5147dc:8", "const:4:8"]]
+ 005147dc ["CALL", null, ["callee:00c58f50:8"]]
- 005144bc bytes b10e1d94
+ 005147dc bytes dd111d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d26b5bdcdebdfb2828b541aa8461bc23"></a>

### [`00514568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514568.md) → [`00514888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514888.md) _ZNK5Botan7X509_DN9has_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e90.md) · 呼出先 5件 [`0054b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b2b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c40.md)
- 新版 呼出元 1件 [`00c5ae60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae60.md) · 呼出先 5件 [`0054b5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054b5d4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5ac10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514568.md#insn-00514594) · [`005145a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514568.md#insn-005145a0) · [`005145b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514568.md#insn-005145b0)
- 新版 [`005148b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514888.md#insn-005148b4) · [`005148c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514888.md#insn-005148c0) · [`005148d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514888.md#insn-005148d0)

~~~diff
- 00514594 ["INT_ADD", "register:40f0:8", ["const:514594:8", "const:4:8"]]
- 00514594 ["CALL", null, ["callee:00c5ac10:8"]]
+ 005148b4 ["INT_ADD", "register:40f0:8", ["const:5148b4:8", "const:4:8"]]
+ 005148b4 ["CALL", null, ["callee:00c5ac10:8"]]
- 00514594 bytes ab151d94
+ 005148b4 bytes d7181d94
- 005145a0 ["INT_ADD", "register:40f0:8", ["const:5145a0:8", "const:4:8"]]
- 005145a0 ["CALL", null, ["callee:00c59720:8"]]
+ 005148c0 ["INT_ADD", "register:40f0:8", ["const:5148c0:8", "const:4:8"]]
+ 005148c0 ["CALL", null, ["callee:00c59720:8"]]
- 005145a0 bytes 6c101d94
+ 005148c0 bytes 98131d94
- 005145b0 ["INT_ADD", "register:40f0:8", ["const:5145b0:8", "const:4:8"]]
- 005145b0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005148d0 ["INT_ADD", "register:40f0:8", ["const:5148d0:8", "const:4:8"]]
+ 005148d0 ["CALL", null, ["callee:00c58f50:8"]]
- 005145b0 bytes 740e1d94
+ 005148d0 bytes a0111d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-403cfa588c29c4d0991c50e32ab9aa55"></a>

### [`00514984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514984.md) → [`00514ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514ca4.md) _ZNK5Botan7X509_DN19get_first_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5ac10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005149b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514984.md#insn-005149b4) · [`005149c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514984.md#insn-005149c0) · [`005149d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514984.md#insn-005149d0)
- 新版 [`00514cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514ca4.md#insn-00514cd4) · [`00514ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514ca4.md#insn-00514ce0) · [`00514cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514ca4.md#insn-00514cf0)

~~~diff
- 005149b4 ["INT_ADD", "register:40f0:8", ["const:5149b4:8", "const:4:8"]]
- 005149b4 ["CALL", null, ["callee:00c5ac10:8"]]
+ 00514cd4 ["INT_ADD", "register:40f0:8", ["const:514cd4:8", "const:4:8"]]
+ 00514cd4 ["CALL", null, ["callee:00c5ac10:8"]]
- 005149b4 bytes a3141d94
+ 00514cd4 bytes cf171d94
- 005149c0 ["INT_ADD", "register:40f0:8", ["const:5149c0:8", "const:4:8"]]
- 005149c0 ["CALL", null, ["callee:00c59720:8"]]
+ 00514ce0 ["INT_ADD", "register:40f0:8", ["const:514ce0:8", "const:4:8"]]
+ 00514ce0 ["CALL", null, ["callee:00c59720:8"]]
- 005149c0 bytes 640f1d94
+ 00514ce0 bytes 90121d94
- 005149d0 ["INT_ADD", "register:40f0:8", ["const:5149d0:8", "const:4:8"]]
- 005149d0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00514cf0 ["INT_ADD", "register:40f0:8", ["const:514cf0:8", "const:4:8"]]
+ 00514cf0 ["CALL", null, ["callee:00c58f50:8"]]
- 005149d0 bytes 6c0d1d94
+ 00514cf0 bytes 98101d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0c9bf96a74157f2ff9148dee604c2a5"></a>

### [`00514b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514b48.md) → [`00514e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514e68.md) _ZN5BotanltERKNS_7X509_DNES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c59af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59af0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005499c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005499c8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5aac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514b48.md#insn-00514b7c) · [`00514b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514b48.md#insn-00514b88) · [`00514ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514b48.md#insn-00514ce4)
- 新版 [`00514e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514e68.md#insn-00514e9c) · [`00514ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514e68.md#insn-00514ea8) · [`00515004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514e68.md#insn-00515004)

~~~diff
- 00514b7c ["INT_ADD", "register:40f0:8", ["const:514b7c:8", "const:4:8"]]
- 00514b7c ["CALL", null, ["callee:00c5aac0:8"]]
+ 00514e9c ["INT_ADD", "register:40f0:8", ["const:514e9c:8", "const:4:8"]]
+ 00514e9c ["CALL", null, ["callee:00c5aac0:8"]]
- 00514b7c bytes dd131d94
+ 00514e9c bytes 09171d94
- 00514b88 ["INT_ADD", "register:40f0:8", ["const:514b88:8", "const:4:8"]]
- 00514b88 ["CALL", null, ["callee:00c5aac0:8"]]
+ 00514ea8 ["INT_ADD", "register:40f0:8", ["const:514ea8:8", "const:4:8"]]
+ 00514ea8 ["CALL", null, ["callee:00c5aac0:8"]]
- 00514b88 bytes da131d94
+ 00514ea8 bytes 06171d94
- 00514ce4 ["INT_ADD", "register:40f0:8", ["const:514ce4:8", "const:4:8"]]
- 00514ce4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00515004 ["INT_ADD", "register:40f0:8", ["const:515004:8", "const:4:8"]]
+ 00515004 ["CALL", null, ["callee:00c590f0:8"]]
- 00514ce4 bytes 0f0d1d94
+ 00515004 bytes 3b101d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da24c6da7d0060da6ae893378eb879cd"></a>

### [`00515140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515140.md) → [`00515460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515460.md) FUN_00515460

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00514de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md) · 呼出先 7件 [`0053d3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d3ec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md)
- 新版 呼出元 1件 [`00515104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515104.md) · 呼出先 7件 [`0053d70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d70c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c59750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00515178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515140.md#insn-00515178) · [`00515258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515140.md#insn-00515258) · [`00515278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515140.md#insn-00515278)
- 新版 [`00515498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515460.md#insn-00515498) · [`00515578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515460.md#insn-00515578) · [`00515598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515460.md#insn-00515598)

~~~diff
- 00515178 ["INT_ADD", "register:40f0:8", ["const:515178:8", "const:4:8"]]
- 00515178 ["CALL", null, ["callee:00c59720:8"]]
+ 00515498 ["INT_ADD", "register:40f0:8", ["const:515498:8", "const:4:8"]]
+ 00515498 ["CALL", null, ["callee:00c59720:8"]]
- 00515178 bytes 760d1d94
+ 00515498 bytes a2101d94
- 00515258 ["INT_ADD", "register:40f0:8", ["const:515258:8", "const:4:8"]]
- 00515258 ["CALL", null, ["callee:0053d70c:8"]]
+ 00515578 ["INT_ADD", "register:40f0:8", ["const:515578:8", "const:4:8"]]
+ 00515578 ["CALL", null, ["callee:0053d70c:8"]]
- 00515258 bytes 65a00094
+ 00515578 bytes 65a00094
- 00515278 ["INT_ADD", "register:40f0:8", ["const:515278:8", "const:4:8"]]
- 00515278 ["CALL", null, ["callee:00c58f50:8"]]
+ 00515598 ["INT_ADD", "register:40f0:8", ["const:515598:8", "const:4:8"]]
+ 00515598 ["CALL", null, ["callee:00c58f50:8"]]
- 00515278 bytes 420b1d94
+ 00515598 bytes 6e0e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b431d22df1cecf55433b6f23a2a0fbd7"></a>

### [`005153b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005153b0.md) → [`005156d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/005156d0.md) FUN_005156d0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00508768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00508a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508a88.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5ae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005153e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005153b0.md#insn-005153e4) · [`00515424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005153b0.md#insn-00515424) · [`0051544c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005153b0.md#insn-0051544c)
- 新版 [`00515704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/005156d0.md#insn-00515704) · [`00515744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/005156d0.md#insn-00515744) · [`0051576c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/005156d0.md#insn-0051576c)

~~~diff
- 005153e4 ["INT_ADD", "register:40f0:8", ["const:5153e4:8", "const:4:8"]]
- 005153e4 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00515704 ["INT_ADD", "register:40f0:8", ["const:515704:8", "const:4:8"]]
+ 00515704 ["CALL", null, ["callee:00c5ae70:8"]]
- 005153e4 bytes af121d94
+ 00515704 bytes db151d94
- 00515424 ["COPY", "register:0:8", ["register:4040:8"]]
- 00515424 ["INT_ADD", "register:40f0:8", ["const:515424:8", "const:4:8"]]
- 00515424 ["CALLIND", null, ["register:0:8"]]
+ 00515744 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00515744 ["INT_ADD", "register:40f0:8", ["const:515744:8", "const:4:8"]]
+ 00515744 ["CALLIND", null, ["register:0:8"]]
- 00515424 bytes 00013fd6
+ 00515744 bytes 00013fd6
- 0051544c ["INT_ADD", "register:40f0:8", ["const:51544c:8", "const:4:8"]]
- 0051544c ["CALL", null, ["callee:00c59340:8"]]
+ 0051576c ["INT_ADD", "register:40f0:8", ["const:51576c:8", "const:4:8"]]
+ 0051576c ["CALL", null, ["callee:00c59340:8"]]
- 0051544c bytes c90b1d94
+ 0051576c bytes f50e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d1de17b2296933f1610696d67ce09d1"></a>

### [`005154f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005154f4.md) → [`00515814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515814.md) FUN_00515814

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054f470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054f/0054f470.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054b474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b474.md) [`0054b810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b810.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0054f790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054f/0054f790.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0054b794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054b794.md) [`0054bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054bb30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00515544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005154f4.md#insn-00515544) · [`00515574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005154f4.md#insn-00515574) · [`00515590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005154f4.md#insn-00515590)
- 新版 [`00515864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515814.md#insn-00515864) · [`00515894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515814.md#insn-00515894) · [`005158b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515814.md#insn-005158b0)

~~~diff
- 00515544 ["INT_ADD", "register:40f0:8", ["const:515544:8", "const:4:8"]]
- 00515544 ["CALL", null, ["callee:0043bf04:8"]]
+ 00515864 ["INT_ADD", "register:40f0:8", ["const:515864:8", "const:4:8"]]
+ 00515864 ["CALL", null, ["callee:0043bf04:8"]]
- 00515544 bytes a899fc97
+ 00515864 bytes a899fc97
- 00515574 ["INT_ADD", "register:40f0:8", ["const:515574:8", "const:4:8"]]
- 00515574 ["CALL", null, ["callee:0054b794:8"]]
+ 00515894 ["INT_ADD", "register:40f0:8", ["const:515894:8", "const:4:8"]]
+ 00515894 ["CALL", null, ["callee:0054b794:8"]]
- 00515574 bytes c0d70094
+ 00515894 bytes c0d70094
- 00515590 ["INT_ADD", "register:40f0:8", ["const:515590:8", "const:4:8"]]
- 00515590 ["CALL", null, ["callee:0054bb30:8"]]
+ 005158b0 ["INT_ADD", "register:40f0:8", ["const:5158b0:8", "const:4:8"]]
+ 005158b0 ["CALL", null, ["callee:0054bb30:8"]]
- 00515590 bytes a0d80094
+ 005158b0 bytes a0d80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12be1afa96c0ae9d9eb233a98a6cbec9"></a>

### [`00516c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md) → [`00516f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516f24.md) FUN_00516f24

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00503104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md) [`0051140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00503424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503424.md) [`0051172c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/0051172c.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00516c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md#insn-00516c20) · [`00516c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md#insn-00516c34) · [`00516c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md#insn-00516c54)
- 新版 [`00516f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516f24.md#insn-00516f40) · [`00516f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516f24.md#insn-00516f54) · [`00516f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516f24.md#insn-00516f74)

~~~diff
- 00516c20 ["INT_ADD", "register:40f0:8", ["const:516c20:8", "const:4:8"]]
- 00516c20 ["CALL", null, ["callee:00c58f50:8"]]
+ 00516f40 ["INT_ADD", "register:40f0:8", ["const:516f40:8", "const:4:8"]]
+ 00516f40 ["CALL", null, ["callee:00c58f50:8"]]
- 00516c20 bytes d8041d94
+ 00516f40 bytes 04081d94
- 00516c34 ["INT_ADD", "register:40f0:8", ["const:516c34:8", "const:4:8"]]
- 00516c34 ["CALL", null, ["callee:00c54d90:8"]]
+ 00516f54 ["INT_ADD", "register:40f0:8", ["const:516f54:8", "const:4:8"]]
+ 00516f54 ["CALL", null, ["callee:00c54d90:8"]]
- 00516c34 bytes 5bf41c94
+ 00516f54 bytes 8ff71c94
- 00516c54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00516c54 ["INT_ADD", "register:40f0:8", ["const:516c54:8", "const:4:8"]]
- 00516c54 ["CALLIND", null, ["register:0:8"]]
+ 00516f74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00516f74 ["INT_ADD", "register:40f0:8", ["const:516f74:8", "const:4:8"]]
+ 00516f74 ["CALLIND", null, ["register:0:8"]]
- 00516c54 bytes 00013fd6
+ 00516f74 bytes 00013fd6
~~~


<a id="compare-10517d4519e6f878e6bd84cfa88bc20f"></a>

### [`005170d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005170d4.md) → [`005173f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005173f4.md) FUN_005173f4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005170d4.md#insn-00517120)
- 新版 [`00517440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005173f4.md#insn-00517440)

~~~diff
- 00517120 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517120 ["INT_ADD", "register:40f0:8", ["const:517120:8", "const:4:8"]]
- 00517120 ["CALLIND", null, ["register:0:8"]]
+ 00517440 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517440 ["INT_ADD", "register:40f0:8", ["const:517440:8", "const:4:8"]]
+ 00517440 ["CALLIND", null, ["register:0:8"]]
- 00517120 bytes 00013fd6
+ 00517440 bytes 00013fd6
~~~


<a id="compare-fec7d005e3fbd82f00ee8fdb1fcca659"></a>

### [`00517150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517150.md) → [`00517470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517470.md) _ZNK5Botan10Extensions14extensions_rawEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0054c2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054c2d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0054c5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054c/0054c5f8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005171f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517150.md#insn-005171f4) · [`0051720c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517150.md#insn-0051720c) · [`00517228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517150.md#insn-00517228)
- 新版 [`00517514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517470.md#insn-00517514) · [`0051752c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517470.md#insn-0051752c) · [`00517548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517470.md#insn-00517548)

~~~diff
- 005171f4 ["INT_ADD", "register:40f0:8", ["const:5171f4:8", "const:4:8"]]
- 005171f4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00517514 ["INT_ADD", "register:40f0:8", ["const:517514:8", "const:4:8"]]
+ 00517514 ["CALL", null, ["callee:00c58f30:8"]]
- 005171f4 bytes 5b031d94
+ 00517514 bytes 87061d94
- 0051720c ["INT_ADD", "register:40f0:8", ["const:51720c:8", "const:4:8"]]
- 0051720c ["CALL", null, ["callee:00c590a0:8"]]
+ 0051752c ["INT_ADD", "register:40f0:8", ["const:51752c:8", "const:4:8"]]
+ 0051752c ["CALL", null, ["callee:00c590a0:8"]]
- 0051720c bytes b1031d94
+ 0051752c bytes dd061d94
- 00517228 ["INT_ADD", "register:40f0:8", ["const:517228:8", "const:4:8"]]
- 00517228 ["CALL", null, ["callee:0054c5f8:8"]]
+ 00517548 ["INT_ADD", "register:40f0:8", ["const:517548:8", "const:4:8"]]
+ 00517548 ["CALL", null, ["callee:0054c5f8:8"]]
- 00517228 bytes 2cd40094
+ 00517548 bytes 2cd40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34252f2be66fbddc2139031563891b57"></a>

### [`00517614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517614.md) → [`00517934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517934.md) FUN_00517934

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517614.md#insn-00517630) · [`00517644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517614.md#insn-00517644) · [`00517670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517614.md#insn-00517670)
- 新版 [`00517950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517934.md#insn-00517950) · [`00517964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517934.md#insn-00517964) · [`00517990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517934.md#insn-00517990)

~~~diff
- 00517630 ["INT_ADD", "register:40f0:8", ["const:517630:8", "const:4:8"]]
- 00517630 ["CALL", null, ["callee:00c58f50:8"]]
+ 00517950 ["INT_ADD", "register:40f0:8", ["const:517950:8", "const:4:8"]]
+ 00517950 ["CALL", null, ["callee:00c58f50:8"]]
- 00517630 bytes 54021d94
+ 00517950 bytes 80051d94
- 00517644 ["INT_ADD", "register:40f0:8", ["const:517644:8", "const:4:8"]]
- 00517644 ["CALL", null, ["callee:00c54d90:8"]]
+ 00517964 ["INT_ADD", "register:40f0:8", ["const:517964:8", "const:4:8"]]
+ 00517964 ["CALL", null, ["callee:00c54d90:8"]]
- 00517644 bytes d7f11c94
+ 00517964 bytes 0bf51c94
- 00517670 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517670 ["INT_ADD", "register:40f0:8", ["const:517670:8", "const:4:8"]]
- 00517670 ["CALLIND", null, ["register:0:8"]]
+ 00517990 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517990 ["INT_ADD", "register:40f0:8", ["const:517990:8", "const:4:8"]]
+ 00517990 ["CALLIND", null, ["register:0:8"]]
- 00517670 bytes 00013fd6
+ 00517990 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818f9cedd5114166b1ff393a16be3691"></a>

### [`00519a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519a3c.md) → [`00519d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519d5c.md) _ZNK5Botan14Cert_Extension24Subject_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bbb0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053bed0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5aa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00519a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519a3c.md#insn-00519a6c) · [`00519a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519a3c.md#insn-00519a88) · [`00519ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519a3c.md#insn-00519ac4)
- 新版 [`00519d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519d5c.md#insn-00519d8c) · [`00519da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519d5c.md#insn-00519da8) · [`00519de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519d5c.md#insn-00519de4)

~~~diff
- 00519a6c ["INT_ADD", "register:40f0:8", ["const:519a6c:8", "const:4:8"]]
- 00519a6c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00519d8c ["INT_ADD", "register:40f0:8", ["const:519d8c:8", "const:4:8"]]
+ 00519d8c ["CALL", null, ["callee:00c5aa10:8"]]
- 00519a6c bytes f5ff1c94
+ 00519d8c bytes 21031d94
- 00519a88 ["INT_ADD", "register:40f0:8", ["const:519a88:8", "const:4:8"]]
- 00519a88 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00519da8 ["INT_ADD", "register:40f0:8", ["const:519da8:8", "const:4:8"]]
+ 00519da8 ["CALL", null, ["callee:0046d7f0:8"]]
- 00519a88 bytes 924efd97
+ 00519da8 bytes 924efd97
- 00519ac4 ["INT_ADD", "register:40f0:8", ["const:519ac4:8", "const:4:8"]]
- 00519ac4 ["CALL", null, ["callee:0053bed0:8"]]
+ 00519de4 ["INT_ADD", "register:40f0:8", ["const:519de4:8", "const:4:8"]]
+ 00519de4 ["CALL", null, ["callee:0053bed0:8"]]
- 00519ac4 bytes 3b880094
+ 00519de4 bytes 3b880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0284e8254d2a2210c5bc6ba8ab996d78"></a>

### [`00519b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519b24.md) → [`00519e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519e44.md) _ZNK5Botan14Cert_Extension23Issuer_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bbb0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053bed0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5aa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00519b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519b24.md#insn-00519b54) · [`00519b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519b24.md#insn-00519b70) · [`00519bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519b24.md#insn-00519bac)
- 新版 [`00519e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519e44.md#insn-00519e74) · [`00519e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519e44.md#insn-00519e90) · [`00519ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519e44.md#insn-00519ecc)

~~~diff
- 00519b54 ["INT_ADD", "register:40f0:8", ["const:519b54:8", "const:4:8"]]
- 00519b54 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00519e74 ["INT_ADD", "register:40f0:8", ["const:519e74:8", "const:4:8"]]
+ 00519e74 ["CALL", null, ["callee:00c5aa10:8"]]
- 00519b54 bytes bbff1c94
+ 00519e74 bytes e7021d94
- 00519b70 ["INT_ADD", "register:40f0:8", ["const:519b70:8", "const:4:8"]]
- 00519b70 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00519e90 ["INT_ADD", "register:40f0:8", ["const:519e90:8", "const:4:8"]]
+ 00519e90 ["CALL", null, ["callee:0046d7f0:8"]]
- 00519b70 bytes 584efd97
+ 00519e90 bytes 584efd97
- 00519bac ["INT_ADD", "register:40f0:8", ["const:519bac:8", "const:4:8"]]
- 00519bac ["CALL", null, ["callee:0053bed0:8"]]
+ 00519ecc ["INT_ADD", "register:40f0:8", ["const:519ecc:8", "const:4:8"]]
+ 00519ecc ["CALL", null, ["callee:0053bed0:8"]]
- 00519bac bytes 01880094
+ 00519ecc bytes 01880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d307cdb6347bdbb16718b3842eafd252"></a>

### [`0051aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md) → [`0051ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051ad34.md) FUN_0051ad34

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) · 呼出先 7件 [`0051ade4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ade4.md) [`0053d7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d7a0.md) [`0053d838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d838.md) [`0053d84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d84c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 1件 [`0051a5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a5e0.md) · 呼出先 7件 [`0051b104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b104.md) [`0053dac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053dac0.md) [`0053db58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053db58.md) [`0053db6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053db6c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051aa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md#insn-0051aa8c) · [`0051aab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md#insn-0051aab0) · [`0051aafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md#insn-0051aafc)
- 新版 [`0051adac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051ad34.md#insn-0051adac) · [`0051add0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051ad34.md#insn-0051add0) · [`0051ae1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051ad34.md#insn-0051ae1c)

~~~diff
- 0051aa8c ["INT_ADD", "register:40f0:8", ["const:51aa8c:8", "const:4:8"]]
- 0051aa8c ["CALL", null, ["callee:00c58f30:8"]]
+ 0051adac ["INT_ADD", "register:40f0:8", ["const:51adac:8", "const:4:8"]]
+ 0051adac ["CALL", null, ["callee:00c58f30:8"]]
- 0051aa8c bytes 35f51c94
+ 0051adac bytes 61f81c94
- 0051aab0 ["INT_ADD", "register:40f0:8", ["const:51aab0:8", "const:4:8"]]
- 0051aab0 ["CALL", null, ["callee:0053db6c:8"]]
+ 0051add0 ["INT_ADD", "register:40f0:8", ["const:51add0:8", "const:4:8"]]
+ 0051add0 ["CALL", null, ["callee:0053db6c:8"]]
- 0051aab0 bytes 678b0094
+ 0051add0 bytes 678b0094
- 0051aafc ["INT_ADD", "register:40f0:8", ["const:51aafc:8", "const:4:8"]]
- 0051aafc ["CALL", null, ["callee:00c58f30:8"]]
+ 0051ae1c ["INT_ADD", "register:40f0:8", ["const:51ae1c:8", "const:4:8"]]
+ 0051ae1c ["CALL", null, ["callee:00c58f30:8"]]
- 0051aafc bytes 19f51c94
+ 0051ae1c bytes 45f81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9e33c13d3165f2d323bc3f235e505ca"></a>

### [`0051abdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051abdc.md) → [`0051aefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051aefc.md) FUN_0051aefc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0051a5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a5e0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ac2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051abdc.md#insn-0051ac2c) · [`0051ac3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051abdc.md#insn-0051ac3c) · [`0051ac4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051abdc.md#insn-0051ac4c)
- 新版 [`0051af4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051aefc.md#insn-0051af4c) · [`0051af5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051aefc.md#insn-0051af5c) · [`0051af6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051aefc.md#insn-0051af6c)

~~~diff
- 0051ac2c ["INT_ADD", "register:40f0:8", ["const:51ac2c:8", "const:4:8"]]
- 0051ac2c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051af4c ["INT_ADD", "register:40f0:8", ["const:51af4c:8", "const:4:8"]]
+ 0051af4c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ac2c bytes d5f41c94
+ 0051af4c bytes 01f81c94
- 0051ac3c ["INT_ADD", "register:40f0:8", ["const:51ac3c:8", "const:4:8"]]
- 0051ac3c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051af5c ["INT_ADD", "register:40f0:8", ["const:51af5c:8", "const:4:8"]]
+ 0051af5c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ac3c bytes d1f41c94
+ 0051af5c bytes fdf71c94
- 0051ac4c ["INT_ADD", "register:40f0:8", ["const:51ac4c:8", "const:4:8"]]
- 0051ac4c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051af6c ["INT_ADD", "register:40f0:8", ["const:51af6c:8", "const:4:8"]]
+ 0051af6c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ac4c bytes cdf41c94
+ 0051af6c bytes f9f71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-064574fac6dd70375519acc8e5ad3c97"></a>

### [`0051ad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md) → [`0051b024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b024.md) FUN_0051b024

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) [`00531d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d6c.md) [`00531d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d74.md) [`0054d4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d4e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`0051a5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a5e0.md) [`0053208c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/0053208c.md) [`00532094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532094.md) [`0054d804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054d/0054d804.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ad4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md#insn-0051ad4c) · [`0051ad5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md#insn-0051ad5c) · [`0051ad6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md#insn-0051ad6c)
- 新版 [`0051b06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b024.md#insn-0051b06c) · [`0051b07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b024.md#insn-0051b07c) · [`0051b08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b024.md#insn-0051b08c)

~~~diff
- 0051ad4c ["INT_ADD", "register:40f0:8", ["const:51ad4c:8", "const:4:8"]]
- 0051ad4c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051b06c ["INT_ADD", "register:40f0:8", ["const:51b06c:8", "const:4:8"]]
+ 0051b06c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ad4c bytes 8df41c94
+ 0051b06c bytes b9f71c94
- 0051ad5c ["INT_ADD", "register:40f0:8", ["const:51ad5c:8", "const:4:8"]]
- 0051ad5c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051b07c ["INT_ADD", "register:40f0:8", ["const:51b07c:8", "const:4:8"]]
+ 0051b07c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ad5c bytes 89f41c94
+ 0051b07c bytes b5f71c94
- 0051ad6c ["INT_ADD", "register:40f0:8", ["const:51ad6c:8", "const:4:8"]]
- 0051ad6c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051b08c ["INT_ADD", "register:40f0:8", ["const:51b08c:8", "const:4:8"]]
+ 0051b08c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ad6c bytes 85f41c94
+ 0051b08c bytes b1f71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a03071bac47aca05c6a4f0d8753eb9f"></a>

### [`0051ade4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ade4.md) → [`0051b104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b104.md) FUN_0051b104

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0051aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md) [`0053f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f950.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0051ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051ad34.md) [`0053fc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fc70.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ae2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ade4.md#insn-0051ae2c) · [`0051ae3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ade4.md#insn-0051ae3c)
- 新版 [`0051b14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b104.md#insn-0051b14c) · [`0051b15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b104.md#insn-0051b15c)

~~~diff
- 0051ae2c ["INT_ADD", "register:40f0:8", ["const:51ae2c:8", "const:4:8"]]
- 0051ae2c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051b14c ["INT_ADD", "register:40f0:8", ["const:51b14c:8", "const:4:8"]]
+ 0051b14c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ae2c bytes 55f41c94
+ 0051b14c bytes 81f71c94
- 0051ae3c ["INT_ADD", "register:40f0:8", ["const:51ae3c:8", "const:4:8"]]
- 0051ae3c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051b15c ["INT_ADD", "register:40f0:8", ["const:51b15c:8", "const:4:8"]]
+ 0051b15c ["CALL", null, ["callee:00c58f50:8"]]
- 0051ae3c bytes 51f41c94
+ 0051b15c bytes 7df71c94
~~~


<a id="compare-1ea78c0711fe932c5f129f511d08c619"></a>

### [`0051b8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b8a8.md) → [`0051bbc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051bbc8.md) _ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f20.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 1件 [`00c5aef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aef0.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051b8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b8a8.md#insn-0051b8cc) · [`0051b8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b8a8.md#insn-0051b8dc) · [`0051b9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b8a8.md#insn-0051b9dc)
- 新版 [`0051bbec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051bbc8.md#insn-0051bbec) · [`0051bbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051bbc8.md#insn-0051bbfc) · [`0051bcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051bbc8.md#insn-0051bcfc)

~~~diff
- 0051b8cc ["INT_ADD", "register:40f0:8", ["const:51b8cc:8", "const:4:8"]]
- 0051b8cc ["CALL", null, ["callee:00c5aa90:8"]]
+ 0051bbec ["INT_ADD", "register:40f0:8", ["const:51bbec:8", "const:4:8"]]
+ 0051bbec ["CALL", null, ["callee:00c5aa90:8"]]
- 0051b8cc bytes 7df81c94
+ 0051bbec bytes a9fb1c94
- 0051b8dc ["INT_ADD", "register:40f0:8", ["const:51b8dc:8", "const:4:8"]]
- 0051b8dc ["CALL", null, ["callee:00c59720:8"]]
+ 0051bbfc ["INT_ADD", "register:40f0:8", ["const:51bbfc:8", "const:4:8"]]
+ 0051bbfc ["CALL", null, ["callee:00c59720:8"]]
- 0051b8dc bytes 9df31c94
+ 0051bbfc bytes c9f61c94
- 0051b9dc ["INT_ADD", "register:40f0:8", ["const:51b9dc:8", "const:4:8"]]
- 0051b9dc ["CALL", null, ["callee:00c58f50:8"]]
+ 0051bcfc ["INT_ADD", "register:40f0:8", ["const:51bcfc:8", "const:4:8"]]
+ 0051bcfc ["CALL", null, ["callee:00c58f50:8"]]
- 0051b9dc bytes 69f11c94
+ 0051bcfc bytes 95f41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4315cd5d96170e210449b9bc4e94162"></a>

### [`0051ba14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051ba14.md) → [`0051bd34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051bd34.md) FUN_0051bd34

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051ba14.md#insn-0051ba7c) · [`0051bab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051ba14.md#insn-0051bab0)
- 新版 [`0051bd9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051bd34.md#insn-0051bd9c) · [`0051bdd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051bd34.md#insn-0051bdd0)

~~~diff
- 0051ba7c ["INT_ADD", "register:40f0:8", ["const:51ba7c:8", "const:4:8"]]
- 0051ba7c ["CALL", null, ["callee:00c58f30:8"]]
+ 0051bd9c ["INT_ADD", "register:40f0:8", ["const:51bd9c:8", "const:4:8"]]
+ 0051bd9c ["CALL", null, ["callee:00c58f30:8"]]
- 0051ba7c bytes 39f11c94
+ 0051bd9c bytes 65f41c94
- 0051bab0 ["INT_ADD", "register:40f0:8", ["const:51bab0:8", "const:4:8"]]
- 0051bab0 ["CALL", null, ["callee:0043bf04:8"]]
+ 0051bdd0 ["INT_ADD", "register:40f0:8", ["const:51bdd0:8", "const:4:8"]]
+ 0051bdd0 ["CALL", null, ["callee:0043bf04:8"]]
- 0051bab0 bytes 4d80fc97
+ 0051bdd0 bytes 4d80fc97
~~~


<a id="compare-1bcfc352c99768805701abda1b853c01"></a>

### [`0051bae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bae4.md) → [`0051be04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051be04.md) FUN_0051be04

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bae4.md#insn-0051bb00)
- 新版 [`0051be20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051be04.md#insn-0051be20)

~~~diff
- 0051bb00 ["INT_ADD", "register:40f0:8", ["const:51bb00:8", "const:4:8"]]
- 0051bb00 ["CALL", null, ["callee:00c58f50:8"]]
+ 0051be20 ["INT_ADD", "register:40f0:8", ["const:51be20:8", "const:4:8"]]
+ 0051be20 ["CALL", null, ["callee:00c58f50:8"]]
- 0051bb00 bytes 20f11c94
+ 0051be20 bytes 4cf41c94
~~~


<a id="compare-b6d2c2263a1abc1e47bc53a1ecfb4760"></a>

### [`0051c030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c030.md) → [`0051c350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051c350.md) FUN_0051c350

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051c078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c030.md#insn-0051c078)
- 新版 [`0051c398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051c350.md#insn-0051c398)

~~~diff
- 0051c078 ["INT_ADD", "register:40f0:8", ["const:51c078:8", "const:4:8"]]
- 0051c078 ["CALL", null, ["callee:00c58f50:8"]]
+ 0051c398 ["INT_ADD", "register:40f0:8", ["const:51c398:8", "const:4:8"]]
+ 0051c398 ["CALL", null, ["callee:00c58f50:8"]]
- 0051c078 bytes c2ef1c94
+ 0051c398 bytes eef21c94
~~~


<a id="compare-0d00040fa03c64d586e32d69a91e657f"></a>

### [`0051c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md) → [`0051cb6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051cb6c.md) _ZN5Botan14Cert_Extension20Certificate_Policies8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocator

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0051c9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c9d4.md) [`005408fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md) [`0054d12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d12c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0051ccf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ccf4.md) [`00540c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c1c.md) [`0054d44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054d/0054d44c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051c884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md#insn-0051c884) · [`0051c918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md#insn-0051c918) · [`0051c94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md#insn-0051c94c)
- 新版 [`0051cba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051cb6c.md#insn-0051cba4) · [`0051cc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051cb6c.md#insn-0051cc38) · [`0051cc6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051cb6c.md#insn-0051cc6c)

~~~diff
- 0051c884 ["INT_ADD", "register:40f0:8", ["const:51c884:8", "const:4:8"]]
- 0051c884 ["CALL", null, ["callee:0051ccf4:8"]]
+ 0051cba4 ["INT_ADD", "register:40f0:8", ["const:51cba4:8", "const:4:8"]]
+ 0051cba4 ["CALL", null, ["callee:0051ccf4:8"]]
- 0051c884 bytes 54000094
+ 0051cba4 bytes 54000094
- 0051c918 ["INT_ADD", "register:40f0:8", ["const:51c918:8", "const:4:8"]]
- 0051c918 ["CALL", null, ["callee:00c58f30:8"]]
+ 0051cc38 ["INT_ADD", "register:40f0:8", ["const:51cc38:8", "const:4:8"]]
+ 0051cc38 ["CALL", null, ["callee:00c58f30:8"]]
- 0051c918 bytes 92ed1c94
+ 0051cc38 bytes bef01c94
- 0051c94c ["INT_ADD", "register:40f0:8", ["const:51c94c:8", "const:4:8"]]
- 0051c94c ["CALL", null, ["callee:0043bf04:8"]]
+ 0051cc6c ["INT_ADD", "register:40f0:8", ["const:51cc6c:8", "const:4:8"]]
+ 0051cc6c ["CALL", null, ["callee:0043bf04:8"]]
- 0051c94c bytes a67cfc97
+ 0051cc6c bytes a67cfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47cda0f4f4f3f3df4644400660ae4075"></a>

### [`0051c9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c9d4.md) → [`0051ccf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ccf4.md) FUN_0051ccf4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054cc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054cc74.md) [`0054d010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d010.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0051cb6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051cb6c.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0054cf94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054c/0054cf94.md) [`0054d330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054d/0054d330.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ca24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c9d4.md#insn-0051ca24) · [`0051ca54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c9d4.md#insn-0051ca54) · [`0051ca70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c9d4.md#insn-0051ca70)
- 新版 [`0051cd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ccf4.md#insn-0051cd44) · [`0051cd74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ccf4.md#insn-0051cd74) · [`0051cd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ccf4.md#insn-0051cd90)

~~~diff
- 0051ca24 ["INT_ADD", "register:40f0:8", ["const:51ca24:8", "const:4:8"]]
- 0051ca24 ["CALL", null, ["callee:0043bf04:8"]]
+ 0051cd44 ["INT_ADD", "register:40f0:8", ["const:51cd44:8", "const:4:8"]]
+ 0051cd44 ["CALL", null, ["callee:0043bf04:8"]]
- 0051ca24 bytes 707cfc97
+ 0051cd44 bytes 707cfc97
- 0051ca54 ["INT_ADD", "register:40f0:8", ["const:51ca54:8", "const:4:8"]]
- 0051ca54 ["CALL", null, ["callee:0054cf94:8"]]
+ 0051cd74 ["INT_ADD", "register:40f0:8", ["const:51cd74:8", "const:4:8"]]
+ 0051cd74 ["CALL", null, ["callee:0054cf94:8"]]
- 0051ca54 bytes 88c00094
+ 0051cd74 bytes 88c00094
- 0051ca70 ["INT_ADD", "register:40f0:8", ["const:51ca70:8", "const:4:8"]]
- 0051ca70 ["CALL", null, ["callee:0054d330:8"]]
+ 0051cd90 ["INT_ADD", "register:40f0:8", ["const:51cd90:8", "const:4:8"]]
+ 0051cd90 ["CALL", null, ["callee:0054d330:8"]]
- 0051ca70 bytes 68c10094
+ 0051cd90 bytes 68c10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e43b565f36ea56de99179b32667681b"></a>

### [`0051f088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f088.md) → [`0051f3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f3a8.md) _ZNK5Botan14Cert_Extension17Unknown_Extension12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f088.md#insn-0051f0b8) · [`0051f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f088.md#insn-0051f0d0) · [`0051f0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f088.md#insn-0051f0ec)
- 新版 [`0051f3d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f3a8.md#insn-0051f3d8) · [`0051f3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f3a8.md#insn-0051f3f0) · [`0051f40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f3a8.md#insn-0051f40c)

~~~diff
- 0051f0b8 ["INT_ADD", "register:40f0:8", ["const:51f0b8:8", "const:4:8"]]
- 0051f0b8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0051f3d8 ["INT_ADD", "register:40f0:8", ["const:51f3d8:8", "const:4:8"]]
+ 0051f3d8 ["CALL", null, ["callee:00c58f30:8"]]
- 0051f0b8 bytes aae31c94
+ 0051f3d8 bytes d6e61c94
- 0051f0d0 ["INT_ADD", "register:40f0:8", ["const:51f0d0:8", "const:4:8"]]
- 0051f0d0 ["CALL", null, ["callee:00c590a0:8"]]
+ 0051f3f0 ["INT_ADD", "register:40f0:8", ["const:51f3f0:8", "const:4:8"]]
+ 0051f3f0 ["CALL", null, ["callee:00c590a0:8"]]
- 0051f0d0 bytes 00e41c94
+ 0051f3f0 bytes 2ce71c94
- 0051f0ec ["INT_ADD", "register:40f0:8", ["const:51f0ec:8", "const:4:8"]]
- 0051f0ec ["CALL", null, ["callee:0049f78c:8"]]
+ 0051f40c ["INT_ADD", "register:40f0:8", ["const:51f40c:8", "const:4:8"]]
+ 0051f40c ["CALL", null, ["callee:0049f78c:8"]]
- 0051f0ec bytes e000fe97
+ 0051f40c bytes e000fe97
~~~


<a id="compare-8c4e66819ad414e5b4098f812dc16d6e"></a>

### [`0051f134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f134.md) → [`0051f454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f454.md) _ZNK5Botan11X509_Object11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59750.md) [`00c59760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59760.md) [`00c59770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f134.md#insn-0051f15c) · [`0051f16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f134.md#insn-0051f16c) · [`0051f188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f134.md#insn-0051f188)
- 新版 [`0051f47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f454.md#insn-0051f47c) · [`0051f48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f454.md#insn-0051f48c) · [`0051f4a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f454.md#insn-0051f4a8)

~~~diff
- 0051f15c ["INT_ADD", "register:40f0:8", ["const:51f15c:8", "const:4:8"]]
- 0051f15c ["CALL", null, ["callee:00c59750:8"]]
+ 0051f47c ["INT_ADD", "register:40f0:8", ["const:51f47c:8", "const:4:8"]]
+ 0051f47c ["CALL", null, ["callee:00c59750:8"]]
- 0051f15c bytes 89e51c94
+ 0051f47c bytes b5e81c94
- 0051f16c ["INT_ADD", "register:40f0:8", ["const:51f16c:8", "const:4:8"]]
- 0051f16c ["CALL", null, ["callee:00c59750:8"]]
+ 0051f48c ["INT_ADD", "register:40f0:8", ["const:51f48c:8", "const:4:8"]]
+ 0051f48c ["CALL", null, ["callee:00c59750:8"]]
- 0051f16c bytes 85e51c94
+ 0051f48c bytes b1e81c94
- 0051f188 ["INT_ADD", "register:40f0:8", ["const:51f188:8", "const:4:8"]]
- 0051f188 ["CALL", null, ["callee:00c59760:8"]]
+ 0051f4a8 ["INT_ADD", "register:40f0:8", ["const:51f4a8:8", "const:4:8"]]
+ 0051f4a8 ["CALL", null, ["callee:00c59760:8"]]
- 0051f188 bytes 82e51c94
+ 0051f4a8 bytes aee81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19e76d28680015952a811d91282a7b28"></a>

### [`0051f4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f4d4.md) → [`0051f7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f7f4.md) _ZNK5Botan11X509_Object10PEM_encodeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59560.md) [`00c59f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a530.md) [`00c5af20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f4d4.md#insn-0051f500) · [`0051f514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f4d4.md#insn-0051f514) · [`0051f52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f4d4.md#insn-0051f52c)
- 新版 [`0051f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f7f4.md#insn-0051f820) · [`0051f834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f7f4.md#insn-0051f834) · [`0051f84c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f7f4.md#insn-0051f84c)

~~~diff
- 0051f500 ["INT_ADD", "register:40f0:8", ["const:51f500:8", "const:4:8"]]
- 0051f500 ["CALL", null, ["callee:00c5af20:8"]]
+ 0051f820 ["INT_ADD", "register:40f0:8", ["const:51f820:8", "const:4:8"]]
+ 0051f820 ["CALL", null, ["callee:00c5af20:8"]]
- 0051f500 bytes 94ea1c94
+ 0051f820 bytes c0ed1c94
- 0051f514 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f514 ["INT_ADD", "register:40f0:8", ["const:51f514:8", "const:4:8"]]
- 0051f514 ["CALLIND", null, ["register:0:8"]]
+ 0051f834 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f834 ["INT_ADD", "register:40f0:8", ["const:51f834:8", "const:4:8"]]
+ 0051f834 ["CALLIND", null, ["register:0:8"]]
- 0051f514 bytes 20013fd6
+ 0051f834 bytes 20013fd6
- 0051f52c ["INT_ADD", "register:40f0:8", ["const:51f52c:8", "const:4:8"]]
- 0051f52c ["CALL", null, ["callee:00c5a530:8"]]
+ 0051f84c ["INT_ADD", "register:40f0:8", ["const:51f84c:8", "const:4:8"]]
+ 0051f84c ["CALL", null, ["callee:00c5a530:8"]]
- 0051f52c bytes 0de81c94
+ 0051f84c bytes 39eb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f7635b1d5108c65e1986c7ebc70c16c"></a>

### [`0051fff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fff0.md) → [`00520310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520310.md) FUN_00520310

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052000c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fff0.md#insn-0052000c) · [`0052001c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fff0.md#insn-0052001c) · [`0052002c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fff0.md#insn-0052002c)
- 新版 [`0052032c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520310.md#insn-0052032c) · [`0052033c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520310.md#insn-0052033c) · [`0052034c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520310.md#insn-0052034c)

~~~diff
- 0052000c ["INT_ADD", "register:40f0:8", ["const:52000c:8", "const:4:8"]]
- 0052000c ["CALL", null, ["callee:00c58f50:8"]]
+ 0052032c ["INT_ADD", "register:40f0:8", ["const:52032c:8", "const:4:8"]]
+ 0052032c ["CALL", null, ["callee:00c58f50:8"]]
- 0052000c bytes dddf1c94
+ 0052032c bytes 09e31c94
- 0052001c ["INT_ADD", "register:40f0:8", ["const:52001c:8", "const:4:8"]]
- 0052001c ["CALL", null, ["callee:00c58f50:8"]]
+ 0052033c ["INT_ADD", "register:40f0:8", ["const:52033c:8", "const:4:8"]]
+ 0052033c ["CALL", null, ["callee:00c58f50:8"]]
- 0052001c bytes d9df1c94
+ 0052033c bytes 05e31c94
- 0052002c ["INT_ADD", "register:40f0:8", ["const:52002c:8", "const:4:8"]]
- 0052002c ["CALL", null, ["callee:00c58f50:8"]]
+ 0052034c ["INT_ADD", "register:40f0:8", ["const:52034c:8", "const:4:8"]]
+ 0052034c ["CALL", null, ["callee:00c58f50:8"]]
- 0052002c bytes d5df1c94
+ 0052034c bytes 01e31c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feda75dff98435a5b1445ecb2624a098"></a>

### [`00520074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520074.md) → [`00520394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520394.md) _ZNK5Botan11X509_Object15check_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ad50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052007c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520074.md#insn-0052007c)
- 新版 [`0052039c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520394.md#insn-0052039c)

~~~diff
- 0052007c ["INT_ADD", "register:40f0:8", ["const:52007c:8", "const:4:8"]]
- 0052007c ["CALL", null, ["callee:00c5ad50:8"]]
+ 0052039c ["INT_ADD", "register:40f0:8", ["const:52039c:8", "const:4:8"]]
+ 0052039c ["CALL", null, ["callee:00c5ad50:8"]]
- 0052007c bytes 41e71c94
+ 0052039c bytes 6dea1c94
~~~


